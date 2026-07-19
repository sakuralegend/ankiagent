# ==============================================================================
# --- LÕI PHIÊN BOT: deck hiện tại, menu, bàn phím chọn deck, đồng hồ idle,
# format tóm tắt thẻ. Các flow_* và dispatch đều import từ đây (một chiều:
# core <- flows <- dispatch <- app, không có import vòng).
# ==============================================================================
import asyncio
import json
import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from anki_tools.config import TELEGRAM_USER_ID, TOPIC_DECK_PARENT
from anki_tools.utils import hl_to_bracket
from anki_tools.anki_client import get_deck_names, trigger_sync

IDLE_RESET_SECONDS = 180  # nghỉ 3 phút -> reset phiên + gửi menu

HELP_TEXT = (
    "🇷🇺 Bot Anki tiếng Nga\n"
    "───────────────────\n"
    "• Gõ 1 từ tiếng Nga → thêm thẻ mới. Mặc định 🤖 TỰ ĐỘNG: AI chọn chủ đề\n"
    "  (gắn tag), thẻ vào 📥 RUSSIAN::0-inbox để học gom một chỗ trước\n"
    "• Thẻ học xong vòng đầu (tốt nghiệp learning) → 3h sáng bot tự chuyển về\n"
    "  deck chủ đề theo tag (vd RUSSIAN::life::food) để ôn; /don = chuyển ngay\n"
    "• Muốn deck cố định: /deck → nút (🤖 tự động / 🕘 gần nhất / 📂 có sẵn / ➕ mới)\n"
    "• Từ không có trên OpenRussian (biến cách/sai chính tả) → AI đoán từ nguyên mẫu, bấm nút xác nhận\n"
    "• Gửi 📷 ẢNH trang sách (dạng photo, không phải file) → AI quét từ tiếng Nga,\n"
    "  đưa về nguyên thể, lọc từ đã có thẻ — bạn DUYỆT danh sách rồi bot mới thêm\n"
    "• /deck → bảng chọn deck bằng nút\n"
    "• /sua → bot hỏi từ cần sửa, gõ từ xong chọn kiểu sửa bằng nút\n"
    "• /suadeck → sửa TOÀN BỘ thẻ trong 1 deck (ít dùng — có xác nhận + nút Dừng)\n"
    "• /menu → menu nút bấm\n"
    "• /thongke → phân bố thẻ theo chủ đề, cảnh báo khi cần tách deck\n"
    "• /don → chuyển ngay thẻ tốt nghiệp từ inbox về deck chủ đề\n"
    "• /sync → đồng bộ AnkiWeb ngay\n"
    "• Nghỉ >3 phút → bot tự reset phiên (về chế độ 🤖 tự động)"
)


SYNC_OK_TEXT = "☁️ Đã sync AnkiWeb."
SYNC_FAIL_TEXT = "⚠️ SYNC ANKIWEB THẤT BẠI — thay đổi mới chỉ nằm trên VPS! Thử /sync hoặc xem log."

# Gốc repo (cha của thư mục tgbot/) — các file trạng thái (last_deck.json,
# suadeck_resume.json) vẫn nằm ở đây như thời bot.py 1 file, khỏi migrate.
_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _current_deck(context):
    return context.bot_data.get("deck")


# File nhớ deck dùng gần nhất — để nút "🕘 Deck gần nhất" sống sót cả khi
# phiên bị reset (nghỉ >3 phút) LẪN khi bot restart trên VPS. Gitignore.
LAST_DECK_FILE = os.path.join(_PROJECT_ROOT, "last_deck.json")


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
        # Trạng thái CHỌN dở của /suadeck và quét ảnh (batch đang CHẠY không bị
        # ảnh hưởng: _run_suadeck/_run_scan_add tự đẩy đồng hồ idle mỗi thẻ)
        for k in ("sd_deck_choices", "sd_deck", "sd_note_ids", "sd_instruction", "sd_label",
                  "scan_words", "scan_msg"):
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
