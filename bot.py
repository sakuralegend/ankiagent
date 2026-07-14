# ==============================================================================
# --- BOT TELEGRAM: thêm từ + sửa thẻ Anki từ xa (chạy 24/7 trên VPS) ---
# Luồng dùng (chỉ user có TELEGRAM_USER_ID được phép, giống CLI main.py):
#   (bắt đầu phiên)           -> bot hỏi tên bộ bài trước, nhập xong mới thêm từ
#   <gõ 1 từ tiếng Nga>       -> thêm thẻ mới vào deck hiện tại
#   c                         -> đổi bộ bài (như gõ 'c' trong CLI)
#   /deck <tên>               -> đổi bộ bài 1 bước
#   /sua <từ>                 -> hiện 4 nút: 1 Ngắn hơn / 2 Đổi ví dụ / 3 Dài hơn / Tự viết
#   /sua <từ> 1|2|3           -> chạy thẳng lệnh sửa nhanh tương ứng
#   /sua <từ> <yêu cầu>       -> sửa theo yêu cầu tự do
#   /menu                     -> menu nút bấm
#   /sync                     -> ép đồng bộ AnkiWeb ngay
#
# Nghỉ >3 phút -> tự reset phiên (quên deck + trạng thái dở dang) và gửi 1 tin
# menu nút bấm để lần sau thao tác nhanh.
#
# Kiến trúc: long-polling (không cần mở port/domain/SSL). Mọi thao tác nặng
# (cào web, gọi AI, AnkiConnect) chạy qua asyncio.to_thread để không nghẽn bot.
# Logic thêm/sửa từ nằm ở anki_tools/pipeline.py - DÙNG CHUNG với main.py (CLI).
# ==============================================================================
import asyncio
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

from anki_tools.config import TELEGRAM_BOT_TOKEN, TELEGRAM_USER_ID
from anki_tools.utils import strip_accents_perfectly, hl_to_bracket
from anki_tools.ai_client import check_claude_ready
from anki_tools.pipeline import process_word, refine_note
from anki_tools.anki_client import (
    check_anki_ready,
    find_duplicate_notes,
    change_note_deck,
    delete_notes,
    ensure_deck_exists,
    get_deck_names,
    setup_anki_environment,
    trigger_sync,
)

IDLE_RESET_SECONDS = 180  # nghỉ 3 phút -> reset phiên + gửi menu

HELP_TEXT = (
    "🇷🇺 Bot Anki tiếng Nga\n"
    "───────────────────\n"
    "• Bắt đầu: chọn deck bằng nút (deck có sẵn / tạo mới) rồi gõ từ\n"
    "• Gõ 1 từ tiếng Nga → thêm thẻ mới\n"
    "• c → đổi bộ bài (mở bảng chọn deck)\n"
    "• /sua <từ> → sửa thẻ: chọn 1 Ngắn hơn / 2 Đổi ví dụ / 3 Dài hơn / Tự viết\n"
    "• /menu → menu nút bấm\n"
    "• /sync → đồng bộ AnkiWeb ngay\n"
    "• Nghỉ >3 phút → bot tự reset phiên (chọn lại deck)"
)


SYNC_OK_TEXT = "☁️ Đã sync AnkiWeb."
SYNC_FAIL_TEXT = "⚠️ SYNC ANKIWEB THẤT BẠI — thay đổi mới chỉ nằm trên VPS! Thử /sync hoặc xem log."


# ---------------------------------------------------------------------------
# Trạng thái phiên + tiện ích
# ---------------------------------------------------------------------------

def _current_deck(context):
    return context.bot_data.get("deck")


async def _sync_report_line():
    """Sync AnkiWeb ngay (chính sách: MỌI hành động sửa đổi đều sync liền)
    và trả về dòng text kết quả để nối vào tin nhắn trả lời."""
    ok = await asyncio.to_thread(trigger_sync)
    return SYNC_OK_TEXT if ok else SYNC_FAIL_TEXT


def _deck_choose_keyboard():
    """Bảng chọn cách lấy deck: dùng deck có sẵn hay tạo mới."""
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📂 Deck có sẵn", callback_data="deck:list"),
            InlineKeyboardButton("➕ Tạo deck mới", callback_data="deck:new"),
        ],
    ])


MAX_DECK_BUTTONS = 24  # tránh bảng nút quá dài nếu collection có rất nhiều deck


async def _show_deck_list(query, context):
    """Liệt kê toàn bộ deck trong Anki thành nút bấm để chọn."""
    names = await asyncio.to_thread(get_deck_names)
    if not names:
        context.bot_data["awaiting_deck"] = True
        await query.edit_message_text("📂 Chưa có deck nào trong Anki. Gõ tên deck mới để tạo:")
        return
    names = names[:MAX_DECK_BUTTONS]
    # Tên deck (Cyrillic) có thể vượt giới hạn 64 byte của callback_data
    # -> lưu danh sách vào user_data, nút chỉ mang chỉ số.
    context.user_data["deck_choices"] = names
    rows, row = [], []
    for i, name in enumerate(names):
        row.append(InlineKeyboardButton(name, callback_data=f"deckpick:{i}"))
        if len(row) == 2:
            rows.append(row)
            row = []
    if row:
        rows.append(row)
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
    deck_line = f"📦 Deck hiện tại: {deck}" if deck else "📦 Chưa chọn deck"
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
        user_data.pop("deck_choices", None)
    try:
        await context.bot.send_message(
            chat_id,
            "⏸ Đã reset phiên (nghỉ >3 phút). Deck đã xóa — bấm nút hoặc gõ tiếp:",
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


async def _do_add(status_msg, word, deck_name, is_forced):
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
    else:
        await status_msg.edit_text(f"❌ {error_msg}")


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
            f"{HELP_TEXT}\n\n📚 Chọn deck để bắt đầu:", reply_markup=_deck_choose_keyboard()
        )


async def cmd_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _reset_idle_timer(context, update.effective_chat.id)
    await update.message.reply_text(_menu_text(context), reply_markup=_menu_keyboard())


async def cmd_deck(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _reset_idle_timer(context, update.effective_chat.id)
    if not context.args:
        # Không có tham số -> hiện 2 tùy chọn (deck có sẵn / tạo mới) như menu khởi đầu
        deck = _current_deck(context)
        current = f"📦 Deck hiện tại: {deck}" if deck else "📦 Chưa chọn deck."
        await update.message.reply_text(
            f"{current}\n📚 Chọn deck:", reply_markup=_deck_choose_keyboard()
        )
        return
    deck_name = " ".join(context.args).strip()
    ok = await asyncio.to_thread(ensure_deck_exists, deck_name)
    if ok:
        context.bot_data["deck"] = deck_name
        context.bot_data["awaiting_deck"] = False
        sync_line = await _sync_report_line()  # deck mới tạo phải lên AnkiWeb ngay
        await update.message.reply_text(f"📦 Đã chuyển sang deck: {deck_name}\n{sync_line}")
    else:
        await update.message.reply_text("❌ Không tạo/kiểm tra được deck (AnkiConnect lỗi?).")


async def cmd_sync(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _reset_idle_timer(context, update.effective_chat.id)
    msg = await update.message.reply_text("⏳ Đang sync AnkiWeb...")
    ok = await asyncio.to_thread(trigger_sync)
    await msg.edit_text("☁️ Đã sync AnkiWeb." if ok else "❌ Sync thất bại (xem log trên VPS).")


async def cmd_sua(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _reset_idle_timer(context, update.effective_chat.id)
    if not context.args:
        await update.message.reply_text(
            "Cách dùng:\n"
            "• /sua <từ> → chọn nút 1 Ngắn hơn / 2 Đổi ví dụ / 3 Dài hơn / Tự viết\n"
            "• /sua <từ> 1 (hoặc 2, 3) → chạy thẳng lệnh sửa nhanh\n"
            "• /sua <từ> <yêu cầu tự do>\n"
            "vd: /sua хороший ví dụ về chủ đề ăn uống"
        )
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


async def on_word(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Tin nhắn text thường: tên deck (nếu đang chờ) / 'c' đổi deck / từ cần thêm."""
    text = update.message.text.strip()
    if not text:
        return
    _reset_idle_timer(context, update.effective_chat.id)

    # --- Đang chờ tên deck mới (sau khi bấm nút "Tạo deck mới") ---
    if context.bot_data.get("awaiting_deck"):
        deck_name = text
        ok = await asyncio.to_thread(ensure_deck_exists, deck_name)
        if ok:
            context.bot_data["deck"] = deck_name
            context.bot_data["awaiting_deck"] = False
            sync_line = await _sync_report_line()  # deck mới tạo phải lên AnkiWeb ngay
            await update.message.reply_text(
                f"📦 Deck: {deck_name} — giờ gõ từ tiếng Nga để thêm thẻ.\n{sync_line}"
            )
        else:
            await update.message.reply_text("❌ Không tạo được deck. Nhập tên khác thử:")
        return

    # --- Chưa chọn deck: hiện bảng chọn (deck có sẵn / tạo mới) ---
    if _current_deck(context) is None:
        await update.message.reply_text(
            "📚 Chưa chọn deck — chọn trước đã:", reply_markup=_deck_choose_keyboard()
        )
        return

    # --- 'c' = đổi deck (mở bảng chọn; deck cũ giữ nguyên đến khi chọn xong) ---
    if text.lower() == "c":
        await update.message.reply_text(
            f"📚 Đổi deck (đang ở: {_current_deck(context)}):",
            reply_markup=_deck_choose_keyboard(),
        )
        return

    # --- Còn lại: text là từ cần thêm ---
    word = text
    deck_name = _current_deck(context)
    status = await update.message.reply_text(f"🔍 Đang kiểm tra '{word}'...")

    clean_word = strip_accents_perfectly(word)
    duplicates = await asyncio.to_thread(find_duplicate_notes, clean_word)

    if duplicates:
        context.user_data["pending"] = {"word": word, "dups": duplicates, "sel": 0}
        dup_text, keyboard = _duplicate_text_and_keyboard(context.user_data["pending"])
        await status.edit_text(dup_text, reply_markup=keyboard)
        return

    await _do_add(status, word, deck_name, is_forced=False)


async def on_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Xử lý mọi nút bấm inline: menu:*, sua:*, và luồng từ trùng (sel:/act:)."""
    query = update.callback_query
    if query.from_user.id != TELEGRAM_USER_ID:
        await query.answer("Bạn không có quyền dùng bot này.")
        return
    await query.answer()
    _reset_idle_timer(context, query.message.chat_id)
    data = query.data

    # --- Chọn deck: 2 tùy chọn / liệt kê deck có sẵn / tạo mới ---
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
        context.bot_data["deck"] = deck_name
        context.bot_data["awaiting_deck"] = False
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
            await query.edit_message_text(
                "✏️ Gõ: /sua <từ> rồi chọn nút kiểu sửa.\nvd: /sua хороший"
            )
        elif action == "sync":
            await query.edit_message_text("⏳ Đang sync AnkiWeb...")
            ok = await asyncio.to_thread(trigger_sync)
            await query.edit_message_text("☁️ Đã sync AnkiWeb." if ok else "❌ Sync thất bại.")
        elif action == "help":
            await query.edit_message_text(HELP_TEXT)
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
            await query.edit_message_text(
                f"✏️ Gõ: /sua {word} <yêu cầu của bạn>\n"
                f"vd: /sua {word} ví dụ về chủ đề công việc"
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
        await _do_add(query.message, word, deck_name, is_forced=False)

    elif data == "act:trung":
        await _do_add(query.message, word, deck_name, is_forced=True)


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
        BotCommand("deck", "Đổi bộ bài: /deck <tên> (hoặc gõ c)"),
        BotCommand("sua", "Sửa thẻ: /sua <từ>"),
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
    app.add_handler(CommandHandler("sync", cmd_sync, filters=only_me))
    app.add_handler(CommandHandler("sua", cmd_sua, filters=only_me))
    app.add_handler(CallbackQueryHandler(on_callback))
    app.add_handler(MessageHandler(only_me & filters.TEXT & ~filters.COMMAND, on_word))

    print("🚀 Bot đang chạy (long polling). Sẽ hỏi tên deck khi bạn nhắn tin.")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
