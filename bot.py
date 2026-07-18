# ==============================================================================
# --- BOT TELEGRAM: thêm từ + sửa thẻ Anki từ xa (chạy 24/7 trên VPS) ---
# Luồng dùng (chỉ user có TELEGRAM_USER_ID được phép):
# NGUYÊN TẮC: bấm chức năng TRƯỚC, bot hỏi, rồi mới gõ từ/tên — để user dùng
# bàn phím tiếng Nga liên tục, không phải đổi bàn phím gõ lệnh Latin giữa chừng.
#   (bắt đầu phiên)           -> bot hiện nút chọn deck, chọn xong mới thêm từ
#   <gõ 1 từ tiếng Nga>       -> thêm thẻ mới vào deck hiện tại
#     (từ không có trên OpenRussian -> AI đoán từ nguyên mẫu, user bấm nút xác nhận)
#   /deck (hoặc nút 📚)       -> bảng chọn deck bằng nút
#   /sua (hoặc nút ✏️)        -> bot hỏi từ cần sửa -> gõ từ -> chọn kiểu sửa bằng nút
#   /menu                     -> menu nút bấm
#   /sync                     -> ép đồng bộ AnkiWeb ngay
#   (/deck <tên>, /sua <từ> [yêu cầu] vẫn chạy — đường tắt cho ai thích gõ 1 dòng)
#
# Nghỉ >3 phút -> tự reset phiên (quên deck + trạng thái dở dang) và gửi 1 tin
# menu nút bấm để lần sau thao tác nhanh.
#
# Kiến trúc: long-polling (không cần mở port/domain/SSL). Mọi thao tác nặng
# (cào web, gọi AI, AnkiConnect) chạy qua asyncio.to_thread để không nghẽn bot.
# Logic thêm/sửa từ nằm ở anki_tools/pipeline.py - DÙNG CHUNG với main.py (CLI).
# ==============================================================================
import asyncio
import json
import os
import time

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)

from anki_tools.config import TELEGRAM_BOT_TOKEN, TELEGRAM_USER_ID, TOPIC_DECK_PARENT
from anki_tools.topics import FALLBACK_TOPIC
from anki_tools.utils import strip_accents_perfectly, hl_to_bracket
from anki_tools.ai_client import check_claude_ready, call_claude_lemma
from anki_tools.pipeline import process_word, refine_note, refine_note_id
from anki_tools.anki_client import (
    check_anki_ready,
    find_duplicate_notes,
    change_note_deck,
    delete_notes,
    ensure_deck_exists,
    get_deck_names,
    get_deck_note_ids,
    get_topic_stats,
    setup_anki_environment,
    trigger_sync,
)

IDLE_RESET_SECONDS = 180  # nghỉ 3 phút -> reset phiên + gửi menu

HELP_TEXT = (
    "🇷🇺 Bot Anki tiếng Nga\n"
    "───────────────────\n"
    "• Gõ 1 từ tiếng Nga → thêm thẻ mới. Mặc định 🤖 TỰ ĐỘNG: AI chọn chủ đề,\n"
    "  thẻ vào thẳng deck con tương ứng (vd RUSSIAN::food)\n"
    "• Muốn deck cố định: /deck → nút (🤖 tự động / 🕘 gần nhất / 📂 có sẵn / ➕ mới)\n"
    "• Từ không có trên OpenRussian (biến cách/sai chính tả) → AI đoán từ nguyên mẫu, bấm nút xác nhận\n"
    "• /deck → bảng chọn deck bằng nút\n"
    "• /sua → bot hỏi từ cần sửa, gõ từ xong chọn kiểu sửa bằng nút\n"
    "• /suadeck → sửa TOÀN BỘ thẻ trong 1 deck (ít dùng — có xác nhận + nút Dừng)\n"
    "• /menu → menu nút bấm\n"
    "• /thongke → phân bố thẻ theo chủ đề, cảnh báo khi cần tách deck\n"
    "• /sync → đồng bộ AnkiWeb ngay\n"
    "• Nghỉ >3 phút → bot tự reset phiên (về chế độ 🤖 tự động)"
)


SYNC_OK_TEXT = "☁️ Đã sync AnkiWeb."
SYNC_FAIL_TEXT = "⚠️ SYNC ANKIWEB THẤT BẠI — thay đổi mới chỉ nằm trên VPS! Thử /sync hoặc xem log."


# ---------------------------------------------------------------------------
# Trạng thái phiên + tiện ích
# ---------------------------------------------------------------------------

def _current_deck(context):
    return context.bot_data.get("deck")


# File nhớ deck dùng gần nhất — để nút "🕘 Deck gần nhất" sống sót cả khi
# phiên bị reset (nghỉ >3 phút) LẪN khi bot restart trên VPS. Gitignore.
LAST_DECK_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "last_deck.json")


def _load_last_deck():
    """Đọc tên deck dùng gần nhất. Trả về str hoặc None."""
    try:
        with open(LAST_DECK_FILE, encoding="utf-8") as f:
            return (json.load(f).get("deck") or "").strip() or None
    except Exception:
        return None


def _save_last_deck(deck_name):
    """Ghi nhớ deck vừa chọn (deck_name=None -> quên luôn, vd deck đã bị xóa)."""
    try:
        if not deck_name:
            if os.path.exists(LAST_DECK_FILE):
                os.remove(LAST_DECK_FILE)
            return
        with open(LAST_DECK_FILE, "w", encoding="utf-8") as f:
            json.dump({"deck": deck_name}, f, ensure_ascii=False)
    except Exception:
        pass  # nhớ deck chỉ là tiện ích, lỗi ghi file không được làm gãy luồng chính


def _set_deck(context, deck_name):
    """Điểm DUY NHẤT đặt deck hiện tại cho phiên (mọi luồng chọn deck gọi vào đây
    để chắc chắn deck nào cũng được ghi nhớ cho nút 🕘 Deck gần nhất).
    deck_name=None = chế độ TỰ ĐỘNG theo chủ đề (không ghi đè deck gần nhất)."""
    context.bot_data["deck"] = deck_name
    context.bot_data["awaiting_deck"] = False
    if deck_name:
        _save_last_deck(deck_name)


async def _sync_report_line():
    """Sync AnkiWeb ngay (chính sách: MỌI hành động sửa đổi đều sync liền)
    và trả về dòng text kết quả để nối vào tin nhắn trả lời."""
    ok = await asyncio.to_thread(trigger_sync)
    return SYNC_OK_TEXT if ok else SYNC_FAIL_TEXT


def _deck_choose_keyboard():
    """Bảng chọn cách lấy deck: deck gần nhất (nếu nhớ) / deck có sẵn / tạo mới.
    Nút deck gần nhất mang callback cố định 'deck:last' (tên deck Cyrillic có thể
    vượt 64 byte callback_data nên không nhét tên vào callback)."""
    rows = [[InlineKeyboardButton("🤖 Tự động theo chủ đề (AI)", callback_data="deck:auto")]]
    last = _load_last_deck()
    if last:
        rows.append([InlineKeyboardButton(f"🕘 Deck gần nhất: {last}", callback_data="deck:last")])
    rows.append([
        InlineKeyboardButton("📂 Deck có sẵn", callback_data="deck:list"),
        InlineKeyboardButton("➕ Tạo deck mới", callback_data="deck:new"),
    ])
    return InlineKeyboardMarkup(rows)


MAX_DECK_BUTTONS = 24  # tránh bảng nút quá dài nếu collection có rất nhiều deck


def _deck_buttons_rows(names, prefix):
    """Xếp danh sách tên deck thành các hàng nút (2 nút/hàng), callback = prefix:i.
    Tên deck (Cyrillic) có thể vượt 64 byte callback_data -> nút chỉ mang chỉ số,
    danh sách tên phải được lưu vào user_data ở phía gọi."""
    rows, row = [], []
    for i, name in enumerate(names):
        row.append(InlineKeyboardButton(name, callback_data=f"{prefix}:{i}"))
        if len(row) == 2:
            rows.append(row)
            row = []
    if row:
        rows.append(row)
    return rows


async def _show_deck_list(query, context):
    """Liệt kê toàn bộ deck trong Anki thành nút bấm để chọn."""
    names = await asyncio.to_thread(get_deck_names)
    if not names:
        context.bot_data["awaiting_deck"] = True
        await query.edit_message_text("📂 Chưa có deck nào trong Anki. Gõ tên deck mới để tạo:")
        return
    names = names[:MAX_DECK_BUTTONS]
    context.user_data["deck_choices"] = names
    rows = _deck_buttons_rows(names, "deckpick")
    rows.append([InlineKeyboardButton("➕ Tạo deck mới", callback_data="deck:new")])
    await query.edit_message_text("📂 Chọn deck:", reply_markup=InlineKeyboardMarkup(rows))


def _degraded_fix_keyboard(word):
    """2 nút cho thẻ AI tạo bị thiếu nội dung: tự sửa (preset 2 - đổi ví dụ,
    giống bấm nút 2 ở /sua) hoặc bỏ qua. Trả về None nếu từ quá dài so với
    giới hạn 64 byte của callback_data (khi đó tin nhắn vẫn còn dòng gợi ý /sua)."""
    data = f"fix:{word}"
    if not word or len(data.encode("utf-8")) > 64:
        return None
    return InlineKeyboardMarkup([[
        InlineKeyboardButton("🔧 Tự sửa (đổi ví dụ)", callback_data=data),
        InlineKeyboardButton("⏭ Bỏ qua", callback_data="fix:"),
    ]])


def _menu_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📚 Chọn deck", callback_data="menu:deck"),
            InlineKeyboardButton("✏️ Sửa thẻ", callback_data="menu:sua"),
        ],
        [
            InlineKeyboardButton("☁️ Sync", callback_data="menu:sync"),
            InlineKeyboardButton("❓ Hướng dẫn", callback_data="menu:help"),
        ],
    ])


def _menu_text(context):
    deck = _current_deck(context)
    deck_line = (f"📦 Deck hiện tại: {deck}" if deck
                 else f"📦 Deck: 🤖 tự động theo chủ đề ({TOPIC_DECK_PARENT}::<topic>)")
    return f"🎛 MENU\n{deck_line}\nBấm nút hoặc gõ từ để thao tác:"


async def _idle_reset_job(context, chat_id):
    """Chạy sau IDLE_RESET_SECONDS im lặng: reset phiên (quên deck + trạng thái
    dở dang) rồi gửi ĐÚNG 1 tin menu. Bị hủy nếu user tương tác lại."""
    try:
        await asyncio.sleep(IDLE_RESET_SECONDS)
    except asyncio.CancelledError:
        return
    # Về trạng thái "không làm gì": quên deck + mọi thao tác dở dang
    context.bot_data["deck"] = None
    context.bot_data["awaiting_deck"] = False
    user_data = context.application.user_data.get(TELEGRAM_USER_ID)
    if user_data:
        user_data.pop("pending", None)
        user_data.pop("sua_word", None)
        user_data.pop("awaiting", None)
        user_data.pop("deck_choices", None)
        user_data.pop("lemma_choices", None)
        # Trạng thái CHỌN dở của /suadeck (batch đang CHẠY không bị ảnh hưởng:
        # _run_suadeck tự đẩy đồng hồ idle mỗi thẻ nên không rơi vào đây)
        for k in ("sd_deck_choices", "sd_deck", "sd_note_ids", "sd_instruction", "sd_label"):
            user_data.pop(k, None)
    try:
        # 1 tin duy nhất: báo đã reset + menu y hệt /menu để lần vào tới bấm luôn
        await context.bot.send_message(
            chat_id,
            f"⏸ Nghỉ >3 phút — đã reset phiên, về chế độ 🤖 tự động theo chủ đề (thẻ trong Anki không mất gì).\n\n{_menu_text(context)}",
            reply_markup=_menu_keyboard(),
        )
    except Exception:
        pass


def _reset_idle_timer(context, chat_id):
    """Mỗi tương tác gọi hàm này 1 lần: hủy đồng hồ cũ, đặt đồng hồ 3 phút mới."""
    old_task = context.bot_data.get("idle_task")
    if old_task and not old_task.done():
        old_task.cancel()
    context.bot_data["idle_task"] = asyncio.create_task(_idle_reset_job(context, chat_id))


def format_card_summary(card_info, elapsed):
    """Bản Telegram của print_card_summary() - text thuần, không markdown."""
    w = hl_to_bracket(card_info["word"])
    forced = " ⚠️ FORCE" if card_info.get("is_forced") else ""
    lines = [
        f"✅ THẺ MỚI{forced}: {w}",
        f"🇬🇧 {', '.join(card_info['en_meanings'])}",
        f"🇻🇳 {card_info['vi_meaning']}",
    ]
    if card_info.get("gender"):
        lines.append(f"🏷️ {card_info['pos']} ({card_info['gender']})")
    else:
        lines.append(f"🏷️ {card_info['pos']}")
    if card_info.get("topic"):
        lines.append(f"📂 {card_info['topic']}")

    for i, ex in enumerate(card_info.get("simplified_examples", [])[:3]):
        ru = hl_to_bracket(ex.get("ru", ""))
        en = hl_to_bracket(ex.get("en", ""))
        vi = hl_to_bracket(ex.get("vi") or ex.get("vietnamese") or "")
        lines.append(f"💡 {i + 1}. {ru}")
        if en:
            lines.append(f"     🇬🇧 {en}")
        if vi:
            lines.append(f"     🇻🇳 {vi}")

    if card_info.get("ai_degraded"):
        lines.append(
            "⚠️ AI không tạo được ví dụ/nghĩa Việt lần này — thẻ vẫn được thêm nhưng THIẾU nội dung."
        )
        lines.append(
            f"👉 Bấm nút bên dưới, hoặc gõ /sua {card_info.get('clean_word', '')} để AI làm lại."
        )

    lines.append(f"📦 {card_info['deck']} | ⏱ {elapsed:.1f}s")
    if card_info.get("synced") is False:
        lines.append(SYNC_FAIL_TEXT)
    else:
        lines.append("☁️ Đã sync AnkiWeb — mở app Anki bấm sync để thấy thẻ.")
    return "\n".join(lines)


async def _do_add(status_msg, word, deck_name, is_forced, context=None):
    """Chạy pipeline thêm từ (trong thread) rồi cập nhật tin nhắn trạng thái."""
    t0 = time.time()
    await status_msg.edit_text(f"⏳ Đang xử lý '{word}' (cào OpenRussian → AI → Anki)...")
    success, card_info, error_msg = await asyncio.to_thread(
        process_word, word, deck_name, is_forced, True  # do_sync=True trên VPS
    )
    if success:
        markup = None
        if card_info.get("ai_degraded"):
            markup = _degraded_fix_keyboard(card_info.get("clean_word", ""))
        await status_msg.edit_text(
            format_card_summary(card_info, time.time() - t0), reply_markup=markup
        )
    elif (card_info or {}).get("not_found") and context is not None:
        # Từ không có trên OpenRussian: có thể sai chính tả hoặc là dạng biến cách
        # -> nhờ AI đoán từ nguyên mẫu rồi hỏi user xác nhận trước khi cào lại.
        await _suggest_lemma(status_msg, word, context)
    else:
        await status_msg.edit_text(f"❌ {error_msg}")


async def _suggest_lemma(status_msg, word, context):
    """Hỏi AI từ nguyên mẫu của 1 từ không tìm thấy, rồi hiện nút để user xác nhận."""
    await status_msg.edit_text(
        f"🔍 Không thấy '{word}' trên OpenRussian — đang hỏi AI từ nguyên mẫu..."
    )
    guess = await asyncio.to_thread(call_claude_lemma, word)
    if not guess:
        await status_msg.edit_text(
            f"❌ Không tìm thấy '{word}' trên OpenRussian, và AI cũng không đoán được "
            "từ nguyên mẫu. Kiểm tra lại chính tả rồi gõ lại nhé."
        )
        return
    candidates = [guess["lemma"]] + guess["alternatives"]
    # Tên từ (Cyrillic) có thể vượt 64 byte callback_data -> nút chỉ mang chỉ số
    context.user_data["lemma_choices"] = candidates
    lines = [
        f"⚠️ Không tìm thấy '{word}' trên OpenRussian.",
        f"🤖 AI đoán từ nguyên mẫu: {guess['lemma']}",
    ]
    if guess["reason_vi"]:
        lines.append(f"💬 {guess['reason_vi']}")
    lines.append("Bấm từ đúng để thêm thẻ, hoặc hủy:")
    rows = [
        [InlineKeyboardButton(f"✅ Thêm '{c}'", callback_data=f"lemma:{i}")]
        for i, c in enumerate(candidates)
    ]
    rows.append([InlineKeyboardButton("🚫 Hủy", callback_data="lemma:cancel")])
    await status_msg.edit_text("\n".join(lines), reply_markup=InlineKeyboardMarkup(rows))


async def _add_with_dup_check(status_msg, word, context):
    """Dò trùng rồi thêm từ — luồng chung cho tin nhắn gõ từ và nút xác nhận lemma."""
    clean_word = strip_accents_perfectly(word)
    duplicates = await asyncio.to_thread(find_duplicate_notes, clean_word)
    if duplicates:
        context.user_data["pending"] = {"word": word, "dups": duplicates, "sel": 0}
        dup_text, keyboard = _duplicate_text_and_keyboard(context.user_data["pending"])
        await status_msg.edit_text(dup_text, reply_markup=keyboard)
        return
    await _do_add(status_msg, word, _current_deck(context), is_forced=False, context=context)


async def _do_sua(status_msg, word, instruction):
    """Chạy pipeline sửa thẻ (trong thread) rồi cập nhật tin nhắn trạng thái."""
    t0 = time.time()
    await status_msg.edit_text(f"⏳ Đang sửa thẻ '{word}'...")
    success, result, error_msg = await asyncio.to_thread(refine_note, word, instruction, True)
    if not success:
        await status_msg.edit_text(f"❌ {error_msg}")
        return
    lines = [f"✏️ ĐÃ SỬA THẺ: {hl_to_bracket(result['word'])}", f"🇻🇳 {result['vi']}"]
    for i, ex in enumerate(result["examples"][:3]):
        lines.append(f"💡 {i + 1}. {hl_to_bracket(ex.get('ru', ''))}")
        en = hl_to_bracket(ex.get("en", ""))
        vi = hl_to_bracket(ex.get("vi") or ex.get("vietnamese") or "")
        if en:
            lines.append(f"     🇬🇧 {en}")
        if vi:
            lines.append(f"     🇻🇳 {vi}")
    lines.append(f"⏱ {time.time() - t0:.1f}s")
    if result.get("synced") is False:
        lines.append(SYNC_FAIL_TEXT)
    else:
        lines.append("☁️ Đã sync AnkiWeb — mở app Anki bấm sync để thấy thẻ mới.")
    await status_msg.edit_text("\n".join(lines))


def _duplicate_text_and_keyboard(pending):
    """Dựng nội dung tin nhắn + bàn phím nút bấm cho tình huống từ bị trùng."""
    dups = pending["dups"]
    word = pending["word"]
    lines = [f"⚠️ Từ '{word}' đã tồn tại ({len(dups)} note):"]
    for i, d in enumerate(dups):
        marker = "👉 " if i == pending["sel"] else ""
        lines.append(f"{marker}[{i + 1}] {d['word']} │ {d['deck']} │ {d['status_text']}")

    rows = []
    if len(dups) > 1:
        rows.append([
            InlineKeyboardButton(f"Chọn [{i + 1}]", callback_data=f"sel:{i}")
            for i in range(min(len(dups), 4))
        ])
    rows.append([
        InlineKeyboardButton("🚫 Hủy", callback_data="act:huy"),
        InlineKeyboardButton("📦 Chuyển deck", callback_data="act:chuyen"),
    ])
    rows.append([
        InlineKeyboardButton("🗑 Xóa cũ + thêm mới", callback_data="act:xoa"),
        InlineKeyboardButton("➕ Vẫn thêm trùng", callback_data="act:trung"),
    ])
    return "\n".join(lines), InlineKeyboardMarkup(rows)


# ---------------------------------------------------------------------------
# /suadeck — sửa TOÀN BỘ thẻ trong 1 deck (ít dùng; ghi đè hàng loạt nên có
# màn xác nhận trước khi chạy + nút Dừng giữa chừng)
# ---------------------------------------------------------------------------

SUADECK_QUOTA_WARN = 450  # gần trần 500 lượt Gemini free/ngày thì cảnh báo đậm
SUADECK_DELAY_SECONDS = 3  # nghỉ giữa 2 thẻ để không dồn dập chạm giới hạn RPM

_SD_LABELS = {"1": "1️⃣ Ngắn hơn", "2": "2️⃣ Đổi ví dụ", "3": "3️⃣ Dài hơn"}

# File lưu danh sách thẻ CHƯA sửa xong của đợt /suadeck gần nhất (bị Dừng /
# lỗi giữa chừng / bot restart). /suadeck lần sau sẽ hỏi "Sửa tiếp?" từ file này.
SUADECK_RESUME_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "suadeck_resume.json")


def _sd_load_resume():
    """Đọc đợt sửa deck dở (nếu có). Trả về dict {"deck", "note_ids", ...} hoặc None."""
    try:
        with open(SUADECK_RESUME_FILE, encoding="utf-8") as f:
            state = json.load(f)
        if state.get("deck") and state.get("note_ids"):
            return state
    except Exception:
        pass
    return None


def _sd_save_resume(deck, note_ids):
    try:
        with open(SUADECK_RESUME_FILE, "w", encoding="utf-8") as f:
            json.dump({
                "deck": deck,
                "note_ids": note_ids,
                "saved_at": time.strftime("%Y-%m-%d %H:%M:%S"),
            }, f, ensure_ascii=False)
    except Exception:
        pass


def _sd_delete_resume():
    try:
        os.remove(SUADECK_RESUME_FILE)
    except OSError:
        pass


def _sd_clear(user_data):
    """Dọn toàn bộ trạng thái chọn dở của /suadeck."""
    for k in ("sd_deck_choices", "sd_deck", "sd_note_ids", "sd_instruction", "sd_label"):
        user_data.pop(k, None)


def _sd_confirm_text_keyboard(context):
    """Màn xác nhận cuối trước khi chạy batch: deck, số thẻ, kiểu sửa, ước tính."""
    deck = context.user_data["sd_deck"]
    total = len(context.user_data["sd_note_ids"])
    label = context.user_data.get("sd_label", "")
    minutes = max(1, round(total * 11 / 60))  # ~8s AI + 3s nghỉ chống RPM mỗi thẻ
    lines = [
        "🛠 XÁC NHẬN SỬA TOÀN BỘ DECK",
        f"📦 Deck: {deck}",
        f"🃏 Số thẻ sẽ bị GHI ĐÈ nghĩa + ví dụ: {total}",
        f"✏️ Kiểu sửa: {label}",
        f"⏱ Ước tính: ~{minutes} phút (mỗi thẻ 1 lượt AI)",
    ]
    if total > SUADECK_QUOTA_WARN:
        lines.append(
            f"🚨 {total} thẻ VƯỢT gần hết hạn mức AI miễn phí (~500 lượt/ngày) — "
            "nên chia nhỏ deck hoặc chạy sang 2 ngày."
        )
    lines.append("Chạy chứ?")
    kb = InlineKeyboardMarkup([[
        InlineKeyboardButton("🚀 Bắt đầu", callback_data="sdgo"),
        InlineKeyboardButton("🚫 Hủy", callback_data="sdcancel"),
    ]])
    return "\n".join(lines), kb


async def _run_suadeck(context, chat_id, msg, deck, note_ids, instruction):
    """Task chạy nền sửa cả deck. PHẢI chạy bằng asyncio.create_task: PTB xử lý
    update tuần tự, nếu chạy ngay trong handler thì nút ⏹ Dừng không bao giờ
    được xử lý. Tiến độ hiển thị trong ĐÚNG 1 tin nhắn edit tại chỗ:
    xong từ nào nội dung từ đó tự biến mất, chỗ đó hiện từ đang sửa tiếp theo."""
    context.bot_data["sd_running"] = True
    context.bot_data["sd_stop"] = False
    total = len(note_ids)
    done, failed_words, failed_ids = 0, [], []
    attempted = 0
    stop_kb = InlineKeyboardMarkup([[InlineKeyboardButton("⏹ Dừng", callback_data="sdstop")]])
    stopped = False

    try:
        for i, note_id in enumerate(note_ids):
            if context.bot_data.get("sd_stop"):
                stopped = True
                break
            # Đẩy đồng hồ idle mỗi thẻ để menu reset 3 phút không chen giữa batch
            _reset_idle_timer(context, chat_id)

            success, result, error_msg = await asyncio.to_thread(
                refine_note_id, note_id, instruction, False
            )
            attempted = i + 1
            word = hl_to_bracket((result or {}).get("word", "")) or f"note {note_id}"
            if success:
                done += 1
            else:
                failed_words.append(word)
                failed_ids.append(note_id)

            progress = (
                f"🔄 Sửa deck '{deck}': thẻ {attempted}/{total}\n"
                f"📝 Vừa xong: {word} {'✅' if success else '❌'}\n"
                f"✅ xong {done} │ ❌ lỗi {len(failed_words)}"
            )
            try:
                await msg.edit_text(progress, reply_markup=stop_kb)
            except Exception:
                pass  # nội dung trùng / mạng chớp — bỏ qua, vòng sau edit tiếp

            # Nghỉ ngắn giữa 2 thẻ: tránh dồn dập chạm giới hạn mỗi-phút (RPM)
            if attempted < total and not context.bot_data.get("sd_stop"):
                await asyncio.sleep(SUADECK_DELAY_SECONDS)
    finally:
        context.bot_data["sd_running"] = False
        context.bot_data["sd_stop"] = False

    # Danh sách thẻ CHƯA xong (lỗi + chưa chạy tới) -> lưu để /suadeck hỏi "Sửa tiếp"
    leftover_ids = failed_ids + list(note_ids[attempted:])
    if leftover_ids:
        _sd_save_resume(deck, leftover_ids)
    else:
        _sd_delete_resume()

    # Sync 1 lần cho cả đợt (chính sách: mọi sửa đổi đều lên AnkiWeb ngay)
    synced = await asyncio.to_thread(trigger_sync)

    title = "⏹ ĐÃ DỪNG sửa deck" if stopped else "🏁 XONG sửa deck"
    lines = [
        f"{title} '{deck}': ✅ {done} thẻ │ ❌ {len(failed_words)} lỗi │ tổng {total}",
    ]
    if failed_words:
        shown = ", ".join(failed_words[:10])
        more = f" (+{len(failed_words) - 10} từ nữa)" if len(failed_words) > 10 else ""
        lines.append(f"❌ Từ bị lỗi (thẻ giữ nguyên): {shown}{more}")
    if leftover_ids:
        lines.append(
            f"💾 Đã lưu {len(leftover_ids)} thẻ còn dở — gọi /suadeck sẽ có nút ▶️ Sửa tiếp."
        )
    lines.append(SYNC_OK_TEXT if synced else SYNC_FAIL_TEXT)
    try:
        await msg.edit_text("\n".join(lines))
    except Exception:
        pass


def _sua_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("1️⃣ Ngắn hơn", callback_data="sua:1"),
            InlineKeyboardButton("2️⃣ Đổi ví dụ", callback_data="sua:2"),
            InlineKeyboardButton("3️⃣ Dài hơn", callback_data="sua:3"),
        ],
        [InlineKeyboardButton("✏️ Tự viết yêu cầu", callback_data="sua:custom")],
    ])


# ---------------------------------------------------------------------------
# Handlers
# ---------------------------------------------------------------------------

async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _reset_idle_timer(context, update.effective_chat.id)
    deck = _current_deck(context)
    if deck:
        await update.message.reply_text(f"{HELP_TEXT}\n\n📦 Deck hiện tại: {deck}")
    else:
        await update.message.reply_text(
            f"{HELP_TEXT}\n\n🤖 Đang ở chế độ tự động ({TOPIC_DECK_PARENT}::<chủ đề>) "
            "— gõ từ luôn, hoặc chọn deck cố định:",
            reply_markup=_deck_choose_keyboard(),
        )


async def cmd_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _reset_idle_timer(context, update.effective_chat.id)
    await update.message.reply_text(_menu_text(context), reply_markup=_menu_keyboard())


async def cmd_deck(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _reset_idle_timer(context, update.effective_chat.id)
    if not context.args:
        # Không có tham số -> hiện 2 tùy chọn (deck có sẵn / tạo mới) như menu khởi đầu
        deck = _current_deck(context)
        current = (f"📦 Deck hiện tại: {deck}" if deck
                   else f"📦 Deck: 🤖 tự động theo chủ đề ({TOPIC_DECK_PARENT}::<topic>).")
        await update.message.reply_text(
            f"{current}\n📚 Chọn deck:", reply_markup=_deck_choose_keyboard()
        )
        return
    deck_name = " ".join(context.args).strip()
    ok = await asyncio.to_thread(ensure_deck_exists, deck_name)
    if ok:
        _set_deck(context, deck_name)
        sync_line = await _sync_report_line()  # deck mới tạo phải lên AnkiWeb ngay
        await update.message.reply_text(f"📦 Đã chuyển sang deck: {deck_name}\n{sync_line}")
    else:
        await update.message.reply_text("❌ Không tạo/kiểm tra được deck (AnkiConnect lỗi?).")


# Ngưỡng "đèn báo" cần tách chủ đề (xem CHANGELOG 18/07/2026: quy tắc 100 thẻ / 15% other)
TOPIC_DECK_WARN = 100     # deck con vượt mức này -> nên tách chủ đề con
OTHER_WARN_PCT = 15       # other chiếm quá % này của kho -> phân loại đang "rò rỉ"


async def cmd_thongke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Phân bố thẻ theo chủ đề + cảnh báo khi chạm ngưỡng cần tách deck."""
    _reset_idle_timer(context, update.effective_chat.id)
    msg = await update.message.reply_text("⏳ Đang đếm thẻ theo chủ đề...")
    stats, untagged = await asyncio.to_thread(get_topic_stats)
    if stats is None:
        await msg.edit_text("❌ Không đếm được (AnkiConnect trên VPS lỗi?).")
        return

    total = sum(stats.values())
    lines = [f"📊 KHO {TOPIC_DECK_PARENT}: {total} thẻ", "─" * 22]
    for slug, n in sorted(stats.items(), key=lambda x: -x[1]):
        if n == 0:
            continue
        mark = " ⚠️" if n >= TOPIC_DECK_WARN else ""
        lines.append(f"{n:>4} │ {slug}{mark}")

    warns = []
    for slug, n in stats.items():
        if n >= TOPIC_DECK_WARN:
            warns.append(f"⚠️ '{slug}' đã {n} thẻ (≥{TOPIC_DECK_WARN}) — nên tách chủ đề con "
                         f"(thêm slug dạng '{slug}::nhanh-con' vào topics.py).")
    other_pct = (stats.get(FALLBACK_TOPIC, 0) * 100 // total) if total else 0
    if other_pct > OTHER_WARN_PCT:
        warns.append(f"⚠️ '{FALLBACK_TOPIC}' chiếm {other_pct}% kho (>{OTHER_WARN_PCT}%) — trong đó chắc "
                     "đã có cụm từ đủ lớn để thành chủ đề riêng.")
    if untagged:
        warns.append(f"⚠️ {untagged} thẻ CHƯA có tag chủ đề — chạy `python tag_topics.py --missing` trên PC.")

    lines.append("─" * 22)
    if warns:
        lines.extend(warns)
    else:
        lines.append(f"✅ Chưa chạm ngưỡng tách deck ({TOPIC_DECK_WARN} thẻ/chủ đề, {FALLBACK_TOPIC} ≤{OTHER_WARN_PCT}%).")
    await msg.edit_text("\n".join(lines))


async def cmd_sync(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _reset_idle_timer(context, update.effective_chat.id)
    msg = await update.message.reply_text("⏳ Đang sync AnkiWeb...")
    ok = await asyncio.to_thread(trigger_sync)
    await msg.edit_text("☁️ Đã sync AnkiWeb." if ok else "❌ Sync thất bại (xem log trên VPS).")


async def cmd_sua(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _reset_idle_timer(context, update.effective_chat.id)
    if not context.args:
        # Luồng chính: bot hỏi từ trước -> user chỉ cần gõ từ bằng bàn phím Nga,
        # không phải đổi bàn phím để gõ lệnh Latin.
        context.user_data["awaiting"] = "sua_word"
        await update.message.reply_text("✏️ Gõ từ cần sửa (chỉ cần gõ từ):")
        return
    word = context.args[0]
    instruction = " ".join(context.args[1:]).strip()

    if not instruction:
        # Chưa có yêu cầu -> hiện 4 nút chọn kiểu sửa
        context.user_data["sua_word"] = word
        await update.message.reply_text(
            f"✏️ Sửa thẻ '{word}' — chọn kiểu:", reply_markup=_sua_keyboard()
        )
        return

    msg = await update.message.reply_text("⏳ Chuẩn bị sửa thẻ...")
    await _do_sua(msg, word, instruction)


def _sd_kind_keyboard():
    """Bàn phím chọn kiểu sửa áp dụng cho cả deck."""
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("1️⃣ Ngắn hơn", callback_data="sdsua:1"),
            InlineKeyboardButton("2️⃣ Đổi ví dụ", callback_data="sdsua:2"),
            InlineKeyboardButton("3️⃣ Dài hơn", callback_data="sdsua:3"),
        ],
        [InlineKeyboardButton("✏️ Tự viết yêu cầu", callback_data="sdsua:custom")],
        [InlineKeyboardButton("🚫 Hủy", callback_data="sdcancel")],
    ])


async def _sd_deck_list_markup(context):
    """Dựng (text, keyboard) danh sách deck cho /suadeck. Trả về (None, None) nếu trống."""
    names = await asyncio.to_thread(get_deck_names)
    if not names:
        return None, None
    names = names[:MAX_DECK_BUTTONS]
    _sd_clear(context.user_data)
    context.user_data["sd_deck_choices"] = names
    rows = _deck_buttons_rows(names, "sd")
    rows.append([InlineKeyboardButton("🚫 Hủy", callback_data="sdcancel")])
    text = (
        "🛠 SỬA TOÀN BỘ DECK — AI làm lại nghĩa + ví dụ của MỌI thẻ trong deck.\n"
        "Chọn deck cần sửa:"
    )
    return text, InlineKeyboardMarkup(rows)


async def cmd_suadeck(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Sửa TOÀN BỘ thẻ trong 1 deck: chọn deck bằng nút -> kiểu sửa -> xác nhận.
    Nếu có đợt sửa dở (bị Dừng / lỗi giữa chừng) thì hỏi Sửa tiếp trước."""
    _reset_idle_timer(context, update.effective_chat.id)
    if context.bot_data.get("sd_running"):
        await update.message.reply_text(
            "⏳ Đang có một đợt sửa deck chạy dở — chờ xong hoặc bấm ⏹ Dừng ở tin tiến độ đã nhé."
        )
        return

    state = _sd_load_resume()
    if state:
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton(
                f"▶️ Sửa tiếp {len(state['note_ids'])} thẻ", callback_data="sdresume"
            )],
            [InlineKeyboardButton("📂 Chọn deck khác (bỏ đợt dở)", callback_data="sdfresh")],
            [InlineKeyboardButton("🚫 Hủy", callback_data="sdcancel")],
        ])
        await update.message.reply_text(
            f"🔁 Có đợt sửa dở: deck '{state['deck']}' còn {len(state['note_ids'])} thẻ "
            f"chưa sửa (lưu lúc {state.get('saved_at', '?')}).",
            reply_markup=kb,
        )
        return

    text, kb = await _sd_deck_list_markup(context)
    if not text:
        await update.message.reply_text("📂 Chưa có deck nào trong Anki.")
        return
    await update.message.reply_text(text, reply_markup=kb)


async def on_word(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Tin nhắn text thường. Ưu tiên theo trạng thái đang chờ: tên deck mới /
    từ cần sửa / yêu cầu sửa tự viết; không chờ gì thì text = từ cần thêm thẻ."""
    text = update.message.text.strip()
    if not text:
        return
    _reset_idle_timer(context, update.effective_chat.id)

    # --- Đang chờ tên deck mới (sau khi bấm nút "Tạo deck mới") ---
    if context.bot_data.get("awaiting_deck"):
        deck_name = text
        ok = await asyncio.to_thread(ensure_deck_exists, deck_name)
        if ok:
            _set_deck(context, deck_name)
            sync_line = await _sync_report_line()  # deck mới tạo phải lên AnkiWeb ngay
            await update.message.reply_text(
                f"📦 Deck: {deck_name} — giờ gõ từ tiếng Nga để thêm thẻ.\n{sync_line}"
            )
        else:
            await update.message.reply_text("❌ Không tạo được deck. Nhập tên khác thử:")
        return

    # --- Đang chờ TỪ cần sửa (sau khi bấm /sua hoặc nút ✏️ Sửa thẻ) ---
    if context.user_data.get("awaiting") == "sua_word":
        context.user_data.pop("awaiting", None)
        context.user_data["sua_word"] = text
        await update.message.reply_text(
            f"✏️ Sửa thẻ '{text}' — chọn kiểu:", reply_markup=_sua_keyboard()
        )
        return

    # --- Đang chờ YÊU CẦU tự viết cho cả deck (/suadeck -> Tự viết) ---
    if context.user_data.get("awaiting") == "sdeck_custom":
        context.user_data.pop("awaiting", None)
        if not context.user_data.get("sd_deck"):
            await update.message.reply_text("⌛ Phiên sửa deck đã hết hạn, gọi lại /suadeck nhé.")
            return
        context.user_data["sd_instruction"] = text
        context.user_data["sd_label"] = f"✏️ {text[:80]}"
        confirm_text, kb = _sd_confirm_text_keyboard(context)
        await update.message.reply_text(confirm_text, reply_markup=kb)
        return

    # --- Đang chờ YÊU CẦU tự viết (sau khi bấm nút "Tự viết yêu cầu") ---
    if context.user_data.get("awaiting") == "sua_custom":
        context.user_data.pop("awaiting", None)
        word = context.user_data.pop("sua_word", None)
        if not word:
            await update.message.reply_text("⌛ Phiên sửa đã hết hạn, gọi lại /sua nhé.")
            return
        msg = await update.message.reply_text("⏳ Chuẩn bị sửa thẻ...")
        await _do_sua(msg, word, text)
        return

    # --- Không chọn deck = chế độ TỰ ĐỘNG (AI bỏ thẻ vào deck con theo chủ đề),
    # nên KHÔNG chặn nữa; muốn deck cố định thì /deck hoặc nút 📚 trong menu ---

    # --- Còn lại: text là từ cần thêm ---
    word = text
    status = await update.message.reply_text(f"🔍 Đang kiểm tra '{word}'...")
    await _add_with_dup_check(status, word, context)


async def on_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Xử lý mọi nút bấm inline: menu:*, sua:*, và luồng từ trùng (sel:/act:)."""
    query = update.callback_query
    if query.from_user.id != TELEGRAM_USER_ID:
        await query.answer("Bạn không có quyền dùng bot này.")
        return
    await query.answer()
    _reset_idle_timer(context, query.message.chat_id)
    data = query.data

    # --- Chọn deck: tự động theo chủ đề / deck gần nhất / có sẵn / tạo mới ---
    if data == "deck:auto":
        _set_deck(context, None)
        await query.edit_message_text(
            f"🤖 Chế độ TỰ ĐỘNG: thẻ mới vào {TOPIC_DECK_PARENT}::<chủ đề> do AI chọn "
            "(vd ::food, ::animals).\nGõ từ tiếng Nga để thêm thẻ."
        )
        return
    if data == "deck:last":
        deck_name = _load_last_deck()
        if not deck_name:
            await query.edit_message_text(
                "⌛ Bot không còn nhớ deck gần nhất — chọn lại nhé:",
                reply_markup=_deck_choose_keyboard(),
            )
            return
        # Kiểm tra deck còn tồn tại (KHÔNG dùng ensure_deck_exists để khỏi
        # vô tình tạo lại deck user đã xóa/đổi tên trong Anki)
        names = await asyncio.to_thread(get_deck_names)
        if deck_name not in names:
            _save_last_deck(None)  # quên deck đã chết để nút không hiện nữa
            await query.edit_message_text(
                f"⚠️ Deck '{deck_name}' không còn trong Anki — chọn deck khác nhé:",
                reply_markup=_deck_choose_keyboard(),
            )
            return
        _set_deck(context, deck_name)
        await query.edit_message_text(f"📦 Deck: {deck_name} — gõ từ tiếng Nga để thêm thẻ.")
        return
    if data == "deck:list":
        await _show_deck_list(query, context)
        return
    if data == "deck:new":
        context.bot_data["awaiting_deck"] = True
        await query.edit_message_text("➕ Gõ tên deck mới:")
        return
    if data.startswith("deckpick:"):
        idx = int(data.split(":", 1)[1])
        choices = context.user_data.get("deck_choices") or []
        if idx >= len(choices):
            await query.edit_message_text("⌛ Danh sách đã cũ, bấm lại nút Chọn deck nhé.")
            return
        deck_name = choices[idx]
        _set_deck(context, deck_name)
        context.user_data.pop("deck_choices", None)
        # Chọn deck có sẵn không sửa đổi collection -> không cần sync
        await query.edit_message_text(f"📦 Deck: {deck_name} — gõ từ tiếng Nga để thêm thẻ.")
        return

    # --- Nút menu ---
    if data.startswith("menu:"):
        action = data.split(":", 1)[1]
        if action == "deck":
            await query.edit_message_text(
                "📚 Chọn deck:", reply_markup=_deck_choose_keyboard()
            )
        elif action == "sua":
            context.user_data["awaiting"] = "sua_word"
            await query.edit_message_text("✏️ Gõ từ cần sửa (chỉ cần gõ từ):")
        elif action == "sync":
            await query.edit_message_text("⏳ Đang sync AnkiWeb...")
            ok = await asyncio.to_thread(trigger_sync)
            await query.edit_message_text("☁️ Đã sync AnkiWeb." if ok else "❌ Sync thất bại.")
        elif action == "help":
            await query.edit_message_text(HELP_TEXT)
        return

    # --- Luồng /suadeck: chọn deck -> kiểu sửa -> xác nhận -> chạy/dừng ---
    if data == "sdcancel":
        _sd_clear(context.user_data)
        await query.edit_message_text("⏭️ Đã hủy sửa deck.")
        return
    if data == "sdstop":
        if context.bot_data.get("sd_running"):
            context.bot_data["sd_stop"] = True
            # Tin tiến độ sẽ tự chuyển thành tổng kết ở vòng lặp kế tiếp
        return
    if data.startswith("sd:"):
        idx = int(data.split(":", 1)[1])
        choices = context.user_data.get("sd_deck_choices") or []
        if idx >= len(choices):
            await query.edit_message_text("⌛ Danh sách đã cũ, gọi lại /suadeck nhé.")
            return
        deck_name = choices[idx]
        note_ids = await asyncio.to_thread(get_deck_note_ids, deck_name)
        if not note_ids:
            _sd_clear(context.user_data)
            await query.edit_message_text(
                f"📂 Deck '{deck_name}' không có thẻ nào (của bot) để sửa."
            )
            return
        context.user_data["sd_deck"] = deck_name
        context.user_data["sd_note_ids"] = note_ids
        await query.edit_message_text(
            f"🛠 Deck '{deck_name}' có {len(note_ids)} thẻ.\n"
            "Chọn kiểu sửa áp dụng cho TẤT CẢ:",
            reply_markup=_sd_kind_keyboard(),
        )
        return
    if data == "sdresume":
        state = _sd_load_resume()
        if not state:
            await query.edit_message_text("⌛ Không còn đợt sửa dở nào, gọi lại /suadeck nhé.")
            return
        context.user_data["sd_deck"] = state["deck"]
        context.user_data["sd_note_ids"] = state["note_ids"]
        await query.edit_message_text(
            f"🔁 Sửa tiếp deck '{state['deck']}' — còn {len(state['note_ids'])} thẻ.\n"
            "Chọn kiểu sửa (nên chọn ĐÚNG kiểu đã dùng lần trước cho đồng bộ):",
            reply_markup=_sd_kind_keyboard(),
        )
        return
    if data == "sdfresh":
        _sd_delete_resume()
        text, kb = await _sd_deck_list_markup(context)
        if not text:
            await query.edit_message_text("📂 Chưa có deck nào trong Anki.")
            return
        await query.edit_message_text(text, reply_markup=kb)
        return
    if data.startswith("sdsua:"):
        choice = data.split(":", 1)[1]
        if not context.user_data.get("sd_deck"):
            await query.edit_message_text("⌛ Phiên sửa deck đã hết hạn, gọi lại /suadeck nhé.")
            return
        if choice == "custom":
            context.user_data["awaiting"] = "sdeck_custom"
            await query.edit_message_text(
                f"✏️ Gõ yêu cầu sửa áp dụng cho TẤT CẢ thẻ trong deck "
                f"'{context.user_data['sd_deck']}':"
            )
            return
        context.user_data["sd_instruction"] = choice
        context.user_data["sd_label"] = _SD_LABELS.get(choice, choice)
        confirm_text, kb = _sd_confirm_text_keyboard(context)
        await query.edit_message_text(confirm_text, reply_markup=kb)
        return
    if data == "sdgo":
        deck = context.user_data.get("sd_deck")
        note_ids = context.user_data.get("sd_note_ids")
        instruction = context.user_data.get("sd_instruction")
        if not deck or not note_ids or instruction is None:
            await query.edit_message_text("⌛ Phiên sửa deck đã hết hạn, gọi lại /suadeck nhé.")
            return
        if context.bot_data.get("sd_running"):
            await query.edit_message_text("⏳ Đang có một đợt sửa deck khác chạy dở.")
            return
        _sd_clear(context.user_data)
        await query.edit_message_text(f"🔄 Bắt đầu sửa deck '{deck}' ({len(note_ids)} thẻ)...")
        # Task riêng để bot vẫn nhận update (đặc biệt là nút ⏹ Dừng) trong lúc chạy
        asyncio.create_task(
            _run_suadeck(context, query.message.chat_id, query.message, deck, note_ids, instruction)
        )
        return

    # --- Nút xác nhận từ nguyên mẫu (từ gõ vào không có trên OpenRussian) ---
    if data.startswith("lemma:"):
        arg = data.split(":", 1)[1]
        if arg == "cancel":
            context.user_data.pop("lemma_choices", None)
            await query.edit_message_text("⏭️ Đã hủy.")
            return
        choices = context.user_data.get("lemma_choices") or []
        idx = int(arg)
        if idx >= len(choices):
            await query.edit_message_text("⌛ Phiên đã hết hạn, gõ lại từ nhé.")
            return
        word = choices[idx]
        context.user_data.pop("lemma_choices", None)
        # (deck None = chế độ tự động theo chủ đề -> không cần chặn chọn deck)
        await query.edit_message_text(f"🔍 Đang kiểm tra '{word}'...")
        await _add_with_dup_check(query.message, word, context)
        return

    # --- Nút trên thẻ AI tạo thiếu nội dung: tự sửa (preset 2) / bỏ qua ---
    if data.startswith("fix:"):
        word = data.split(":", 1)[1]
        if not word:  # "fix:" rỗng = Bỏ qua -> chỉ gỡ nút, giữ nguyên tin nhắn thẻ
            try:
                await query.edit_message_reply_markup(None)
            except Exception:
                pass
            return
        await _do_sua(query.message, word, "2")  # "2" = preset đổi ví dụ, như /sua
        return

    # --- Nút chọn kiểu sửa thẻ ---
    if data.startswith("sua:"):
        choice = data.split(":", 1)[1]
        word = context.user_data.get("sua_word")
        if not word:
            await query.edit_message_text("⌛ Phiên sửa đã hết hạn, gọi lại /sua <từ> nhé.")
            return
        if choice == "custom":
            # Giữ sua_word, chờ user gõ thẳng yêu cầu (không cần gõ lại lệnh/từ)
            context.user_data["awaiting"] = "sua_custom"
            await query.edit_message_text(
                f"✏️ Gõ yêu cầu sửa cho '{word}':\nvd: ví dụ về chủ đề công việc"
            )
            return
        context.user_data.pop("sua_word", None)
        await _do_sua(query.message, word, choice)  # choice = "1"/"2"/"3", pipeline tự resolve
        return

    # --- Luồng từ trùng (sel:/act:) ---
    pending = context.user_data.get("pending")
    if not pending:
        await query.edit_message_text("⌛ Phiên xử lý đã hết hạn, gõ lại từ nhé.")
        return

    deck_name = _current_deck(context)

    if data.startswith("sel:"):
        pending["sel"] = int(data.split(":", 1)[1])
        dup_text, keyboard = _duplicate_text_and_keyboard(pending)
        await query.edit_message_text(dup_text, reply_markup=keyboard)
        return

    selected = pending["dups"][pending["sel"]]
    word = pending["word"]
    context.user_data.pop("pending", None)

    if data == "act:huy":
        await query.edit_message_text("⏭️ Đã hủy.")

    elif data == "act:chuyen":
        if not deck_name:
            # Chế độ tự động không có "deck hiện tại" để chuyển note cũ sang
            await query.edit_message_text(
                "🤖 Đang ở chế độ tự động (không có deck cố định). "
                "Dùng /deck chọn deck trước rồi gõ lại từ để chuyển."
            )
            return
        ok = await asyncio.to_thread(change_note_deck, selected["card_ids"], deck_name)
        if ok:
            sync_line = await _sync_report_line()
            await query.edit_message_text(
                f"✅ Đã chuyển note '{selected['word']}' sang deck '{deck_name}'.\n{sync_line}"
            )
        else:
            await query.edit_message_text("❌ Chuyển deck thất bại.")

    elif data == "act:xoa":
        ok = await asyncio.to_thread(delete_notes, [selected["note_id"]])
        if not ok:
            await query.edit_message_text("❌ Xóa note cũ thất bại. Đã hủy.")
            return
        # Sync ngay sau khi xóa (phòng trường hợp bước thêm mới bên dưới thất bại
        # thì việc xóa vẫn đã được đẩy lên AnkiWeb, không bị lệch 2 bên)
        await asyncio.to_thread(trigger_sync)
        await _do_add(query.message, word, deck_name, is_forced=False, context=context)

    elif data == "act:trung":
        await _do_add(query.message, word, deck_name, is_forced=True, context=context)


# ---------------------------------------------------------------------------
# Khởi động
# ---------------------------------------------------------------------------

def wait_for_anki(max_wait_seconds=180):
    """Chờ AnkiConnect sẵn sàng (container Anki có thể khởi động chậm hơn bot)."""
    waited = 0
    while waited < max_wait_seconds:
        if check_anki_ready():
            return True
        time.sleep(5)
        waited += 5
        print(f"⏳ Chờ AnkiConnect... ({waited}s)")
    return False


async def _post_init(app):
    """Đăng ký menu lệnh gốc của Telegram (nút '/' cạnh ô gõ chữ)."""
    await app.bot.set_my_commands([
        BotCommand("menu", "Menu nút bấm"),
        BotCommand("deck", "Đổi bộ bài (bảng chọn nút)"),
        BotCommand("sua", "Sửa thẻ (bot sẽ hỏi từ)"),
        BotCommand("suadeck", "Sửa TOÀN BỘ thẻ trong 1 deck (ít dùng, tốn AI)"),
        BotCommand("thongke", "Thống kê thẻ theo chủ đề + cảnh báo tách deck"),
        BotCommand("sync", "Đồng bộ AnkiWeb ngay"),
        BotCommand("help", "Hướng dẫn"),
    ])


def main():
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_USER_ID:
        print("❌ Thiếu TELEGRAM_BOT_TOKEN hoặc TELEGRAM_USER_ID trong .env")
        return

    print("🤖 Bot Anki khởi động...")

    if not wait_for_anki():
        print("❌ AnkiConnect không phản hồi sau 3 phút. Kiểm tra container anki (docker ps).")
        return
    print("✅ AnkiConnect sẵn sàng.")

    if check_claude_ready():
        print("✅ AI (Gemini) sẵn sàng.")
    else:
        print("⚠️ AI chưa phản hồi - bot vẫn chạy, sẽ thử lại khi có yêu cầu.")

    setup_anki_environment()
    # Sync ngay sau khi cập nhật môi trường (template/CSS): đẩy mọi thay đổi lên
    # AnkiWeb liền để các thiết bị khác luôn thấy bản mới nhất, tránh lệch pha.
    if trigger_sync():
        print("☁️ Sync khởi động: OK.")
    else:
        print("⚠️ Sync khởi động thất bại - sẽ sync lại ở thao tác đầu tiên.")

    app = Application.builder().token(TELEGRAM_BOT_TOKEN).post_init(_post_init).build()
    only_me = filters.User(user_id=TELEGRAM_USER_ID)

    app.add_handler(CommandHandler(["start", "help"], cmd_start, filters=only_me))
    app.add_handler(CommandHandler("menu", cmd_menu, filters=only_me))
    app.add_handler(CommandHandler("deck", cmd_deck, filters=only_me))
    app.add_handler(CommandHandler("thongke", cmd_thongke, filters=only_me))
    app.add_handler(CommandHandler("sync", cmd_sync, filters=only_me))
    app.add_handler(CommandHandler("sua", cmd_sua, filters=only_me))
    app.add_handler(CommandHandler("suadeck", cmd_suadeck, filters=only_me))
    app.add_handler(CallbackQueryHandler(on_callback))
    app.add_handler(MessageHandler(only_me & filters.TEXT & ~filters.COMMAND, on_word))

    print("🚀 Bot đang chạy (long polling). Mặc định 🤖 tự động: thẻ vào deck con theo chủ đề AI chọn.")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
