# ==============================================================================
# --- LÕI PHIÊN BOT: deck hiện tại, menu, bàn phím chọn deck, đồng hồ idle,
# bộ chạy hàng loạt. (Format nội dung thẻ nằm ở hienthi.py.) Các flow_* và
# dispatch đều import từ đây (một chiều: core <- flows <- dispatch <- app).
# ==============================================================================
import asyncio
import json
import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from anki_tools.config import TELEGRAM_USER_ID, TOPIC_DECK_PARENT
from anki_tools.anki_client import get_deck_names, trigger_sync
from anki_tools.utils import log_debug, log_warn

IDLE_RESET_SECONDS = 180  # nghỉ 3 phút -> reset phiên + gửi menu

HELP_TEXT = (
    "🇷🇺 Bot Anki tiếng Nga\n"
    "═══ DÙNG HẰNG NGÀY ═══\n"
    "• Gõ 1 từ tiếng Nga → xong. AI chọn chủ đề (gắn tag), thẻ vào\n"
    "  📥 RUSSIAN::0-quen (LÀM QUEN: chỉ nhìn chữ Nga, chưa phải gõ)\n"
    "• Làm quen xong (~15 phút) → thẻ thành thẻ GÕ mới tinh ở ⌨️ RUSSIAN::1-go\n"
    "• Gõ xong vòng đầu → thẻ về deck chủ đề theo tag\n"
    "• Học xong gõ /don một phát: sync về → dọn cả hai chặng → sync lên\n"
    "• Gõ từ ĐÃ CÓ thẻ → bot đọc lại nguyên nội dung thẻ đó như một mục TỪ ĐIỂN\n"
    "  (nghĩa, từ loại, 3 ví dụ, audio, lịch ôn) — vẫn có nút xóa/chuyển deck\n"
    "• Gửi 📷 ẢNH trang sách → AI đọc từ, lọc từ đã có thẻ, bạn DUYỆT rồi bot mới\n"
    "  thêm. Sách chữ nhỏ thì gửi ảnh dạng FILE (không nén) để AI đỡ đọc sót\n"
    "• Gõ nhầm / gõ dạng biến cách → từ điển hình thái (hoặc AI) đoán từ nguyên\n"
    "  mẫu, bấm nút xác nhận\n"
    "• ⭐ /dacbiet → thẻ NGỮ PHÁP (số nhiều bất quy tắc), deck GRAMMAR:: riêng.\n"
    "  Một từ có CẢ thẻ từ vựng lẫn thẻ ngữ pháp là bình thường, không phải trùng\n"
    "\n"
    "═══ KHI CẦN SỬA (nút 🛠 trong /menu) ═══\n"
    "• 🔄 /sua → làm lại 1 thẻ TỪ VỰNG (cào lại + AI + audio), giữ tiến trình học\n"
    "  (thẻ ngữ pháp thì sửa trong /dacbiet)\n"
    "• 📚 /suadeck → làm lại toàn bộ thẻ 1 deck (có xác nhận + nút Dừng)\n"
    "• 📊 /thongke → trạng thái học (mới/đang học/trẻ/trưởng thành) TÁCH RIÊNG từng\n"
    "  kho, + phân bố theo chủ đề và cảnh báo khi cần tách deck\n"
    "• 🧹 /don → chuyển ngay thẻ tốt nghiệp từ inbox về deck chủ đề\n"
    "• ☁️ /sync → đồng bộ AnkiWeb ngay\n"
    "• 💾 /backup → sao lưu ngay (nên bấm TRƯỚC khi làm gì mạo hiểm)\n"
    "• 📚 /deck → đổi deck cố định (mặc định là 🤖 tự động theo chủ đề)\n"
    "\n"
    "🛡 Tự động: sync 2 chiều mỗi 30 phút, sao lưu 3h30 sáng (giữ 7 bản gần nhất).\n"
    "Nghỉ >3 phút → bot tự reset phiên (về chế độ 🤖 tự động)."
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
    except Exception as e:
        # nhớ deck chỉ là tiện ích, lỗi ghi file không được làm gãy luồng chính —
        # nhưng phải để lại vết, vì "bot quên deck sau mỗi lần khởi động" nhìn từ
        # ngoài giống hệt lỗi logic, mà nguyên nhân thật là quyền ghi file.
        log_warn(f"khong ghi duoc {LAST_DECK_FILE} ({e}) — bot van chay, chi mat tri nho deck")


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
    """2 nút cho thẻ AI tạo bị thiếu nội dung: làm lại thẻ (như /sua) hoặc bỏ qua.
    Trả về None nếu từ quá dài so với giới hạn 64 byte của callback_data (khi đó
    tin nhắn vẫn còn dòng gợi ý /sua)."""
    data = f"fix:{word}"
    if not word or len(data.encode("utf-8")) > 64:
        return None
    return InlineKeyboardMarkup([[
        InlineKeyboardButton("🔄 Làm lại thẻ", callback_data=data),
        InlineKeyboardButton("⏭ Bỏ qua", callback_data="fix:"),
    ]])


# --- MENU 2 TẦNG (user chốt 20/07/2026) ---------------------------------------
# Việc dùng hằng ngày (gõ từ -> thẻ vào inbox + AI gắn nhãn) KHÔNG cần nút nào,
# nên mặt tiền phải nhường đường cho nó: chỉ 3 nút. Mọi công cụ sửa chữa (dùng
# lúc có sự cố) gom sau nút 🛠 để không gây nhiễu.
def _menu_keyboard():
    """Tầng 1: chỉ những thứ dùng thường xuyên."""
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📚 Đổi deck", callback_data="menu:deck"),
            InlineKeyboardButton("⭐ Ngữ pháp", callback_data="sp:menu"),
        ],
        [InlineKeyboardButton("🛠 Sửa chữa & công cụ", callback_data="menu:tools")],
    ])


def _tools_keyboard():
    """Tầng 2: công cụ ít dùng, chủ yếu khi cần sửa lỗi."""
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🔄 Làm lại 1 thẻ", callback_data="menu:sua"),
            InlineKeyboardButton("📚 Cả deck", callback_data="menu:suadeck"),
        ],
        [
            InlineKeyboardButton("📊 Thống kê", callback_data="menu:thongke"),
            InlineKeyboardButton("🧹 Dọn inbox", callback_data="menu:don"),
        ],
        [
            InlineKeyboardButton("☁️ Sync", callback_data="menu:sync"),
            InlineKeyboardButton("💾 Sao lưu ngay", callback_data="menu:backup"),
        ],
        [
            InlineKeyboardButton("❓ Hướng dẫn", callback_data="menu:help"),
            InlineKeyboardButton("◀️ Quay lại", callback_data="menu:back"),
        ],
    ])


TOOLS_TEXT = (
    "🛠 SỬA CHỮA & CÔNG CỤ\n"
    "Mấy thứ này chỉ cần khi có sự cố — dùng hằng ngày thì chỉ việc gõ từ."
)


def _menu_text(context):
    deck = _current_deck(context)
    deck_line = (f"📦 Deck hiện tại: {deck}" if deck
                 else f"📦 Deck: 🤖 tự động theo chủ đề ({TOPIC_DECK_PARENT}::<topic>)")
    return (f"🎛 MENU\n{deck_line}\n"
            "👉 Gõ từ tiếng Nga là xong — không cần bấm gì.")


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
        user_data.pop("awaiting", None)
        user_data.pop("deck_choices", None)
        user_data.pop("lemma_choices", None)
        # Trạng thái CHỌN dở của /suadeck và quét ảnh (batch đang CHẠY không bị
        # ảnh hưởng: _run_suadeck/_run_scan_add tự đẩy đồng hồ idle mỗi thẻ)
        for k in ("sd_deck_choices", "sd_deck", "sd_note_ids", "scan_words", "scan_msg",
                  "sp_rows"):
            user_data.pop(k, None)
    try:
        # 1 tin duy nhất: báo đã reset + menu y hệt /menu để lần vào tới bấm luôn
        await context.bot.send_message(
            chat_id,
            f"⏸ Nghỉ >3 phút — đã reset phiên, về chế độ 🤖 tự động theo chủ đề (thẻ trong Anki không mất gì).\n\n{_menu_text(context)}",
            reply_markup=_menu_keyboard(),
        )
    except Exception as e:
        # Nhắn "hết phiên" mà hụt thì không có gì để cứu (user sẽ tự thấy khi gõ
        # tiếp), nhưng hụt LIÊN TỤC là dấu hiệu token/chat_id hỏng — cần thấy được.
        log_warn(f"khong gui duoc thong bao het phien cho {chat_id} ({e})")


def _reset_idle_timer(context, chat_id):
    """Mỗi tương tác gọi hàm này 1 lần: hủy đồng hồ cũ, đặt đồng hồ 3 phút mới."""
    old_task = context.bot_data.get("idle_task")
    if old_task and not old_task.done():
        old_task.cancel()
    context.bot_data["idle_task"] = asyncio.create_task(_idle_reset_job(context, chat_id))


# --------------------------------------------------------------------------
# CHỐT CHỐNG HAI ĐỢT HÀNG LOẠT CHẠY CHỒNG NHAU
#
# Bot có BA luồng chạy nền dài, cả ba đều ghi vào Anki, đều gọi AI và đều
# `trigger_sync()`:
#     `sd_*`   /suadeck   — làm lại cả deck
#     `scan_*` quét ảnh   — thêm loạt từ đã duyệt
#     `sp_*`   /dacbiet   — thêm loạt thẻ số nhiều
#
# 🔴 Trước 29/07 mỗi luồng tự kiểm một tập cờ KHÁC NHAU, và bảng kiểm chéo bị
# thủng: `/dacbiet` kiểm cả ba · quét ảnh kiểm hai (quên `sp_`) · `/suadeck`
# **chỉ kiểm chính nó**. Nên bấm `/suadeck` giữa lúc đang quét ảnh thì hai đợt
# cùng ghi Anki, cùng đốt hạn mức AI, cùng sync, và hai tin nhắn tiến độ đè nhau.
#
# Gom về MỘT hàm để không thể thủng lại: thêm luồng nền thứ tư thì chỉ cần thêm
# một dòng vào `_LUONG_NEN` là mọi lối vào có nó, khỏi phải nhớ đi vá ba chỗ.
# --------------------------------------------------------------------------

_LUONG_NEN = (("sd_running", "làm lại deck"),
              ("scan_running", "thêm từ đã quét từ ảnh"),
              ("sp_running", "thêm thẻ số nhiều"))


def dang_chay_hang_loat(context, bo_qua=None):
    """Tên đợt hàng loạt đang chạy (str) — None nếu đang rảnh.

    `bo_qua` = cờ của chính luồng đang hỏi, khi nó muốn báo riêng một câu khác.
    """
    for co, ten in _LUONG_NEN:
        if co != bo_qua and context.bot_data.get(co):
            return ten
    return None


NGHI_GIAY = 3   # nghỉ giữa hai mục — chống chạm giới hạn mỗi-phút (RPM) của AI


async def chay_hang_loat(context, chat_id, msg, items, *, co, stop_data, lam, tien_do,
                         nghi=NGHI_GIAY):
    """BỘ CHẠY NỀN DÙNG CHUNG cho mọi đợt hàng loạt. Trả `(stopped, attempted)`.

    🔴 User chốt 29/07: *"cùng 1 chức năng chỉ có đúng 1 script nhận nhiệm vụ,
    không được có 2 cái cùng làm 1 thứ. Nếu xảy ra thì phải quy về mô hình nhiều
    tầng, cái gì làm chung thì là 1 script, khi khác nhau thì tách ra."*
    Trước đó `_run_suadeck` (87 dòng) · `_run_scan_add` (76) · `_run_batch` (72)
    **đều có đủ 11 bước giống hệt nhau**, và ba bản đã trôi lệch nhau thật: chỉ
    `_run_scan_add` nghỉ TRƯỚC khi hiện tiến độ, nên user phải chờ thêm 3 giây
    mới thấy từ vừa xong.

    PHẦN CHUNG (ở đây): bật cờ · vòng lặp · kiểm nút ⏹ Dừng · đẩy đồng hồ idle ·
    hiện tiến độ · nuốt lỗi `edit_text` · nghỉ chống RPM · `finally` hạ cờ.

    PHẦN RIÊNG (người gọi truyền vào):
      `co`        tiền tố cờ, ví dụ "sd" -> dùng `sd_running` / `sd_stop`
      `stop_data` `callback_data` của nút ⏹ Dừng
      `lam(item)` **async**, làm việc thật với một mục. Trả `(nhan, co_nghi)`:
                  `nhan` = chữ hiện ở dòng "Vừa xong"; `co_nghi=False` khi lượt
                  đó KHÔNG gọi AI (quét ảnh bỏ qua từ trùng) nên khỏi phải nghỉ.
                  Người gọi tự cộng sổ thắng/thua trong closure của mình.
      `tien_do(attempted, total, nhan)` -> chữ của tin nhắn tiến độ.

    Việc dựng câu TÓM TẮT CUỐI vẫn để người gọi tự làm — ba luồng tóm tắt ba kiểu
    khác hẳn nhau (suadeck có danh sách thẻ còn dở, quét ảnh có mục "đã có thẻ
    từ trước", số nhiều có "vá thẻ cũ"), gom vào đây là ép chung một khuôn rồi
    lại phải đẻ tham số cho từng ngoại lệ.
    """
    co_run, co_stop = f"{co}_running", f"{co}_stop"
    context.bot_data[co_run] = True
    context.bot_data[co_stop] = False
    total = len(items)
    stop_kb = InlineKeyboardMarkup([[InlineKeyboardButton("⏹ Dừng", callback_data=stop_data)]])
    stopped, attempted = False, 0
    try:
        for i, item in enumerate(items):
            if context.bot_data.get(co_stop):
                stopped = True
                break
            # Đẩy đồng hồ idle mỗi mục để menu reset 3 phút không chen giữa đợt
            _reset_idle_timer(context, chat_id)
            attempted = i + 1

            nhan, co_nghi = await lam(item)

            try:
                await msg.edit_text(tien_do(attempted, total, nhan), reply_markup=stop_kb)
            except Exception as e:
                # nội dung trùng / mạng chớp — bỏ qua, vòng sau edit tiếp. Mức
                # DEBUG chứ không WARN: cái này kêu mỗi vòng lặp khi Telegram trả
                # "message is not modified", mà đó là chuyện thường, không phải lỗi.
                log_debug(f"edit tien do {attempted}/{total} hut: {e}")

            if co_nghi and attempted < total and not context.bot_data.get(co_stop):
                await asyncio.sleep(nghi)
    finally:
        context.bot_data[co_run] = False
        context.bot_data[co_stop] = False
    return stopped, attempted


async def bao_ket_qua(msg, lines):
    """In tóm tắt cuối đợt. Nuốt lỗi edit y như trong vòng lặp — mạng chớp ở
    đúng dòng cuối không được phép làm nổ task nền."""
    try:
        await msg.edit_text("\n".join(lines))
    except Exception as e:
        # Đây là dòng TÓM TẮT CUỐI ĐỢT — hụt là user không biết đợt chạy ra sao,
        # nên WARN chứ không DEBUG như dòng tiến độ giữa chừng.
        log_warn(f"khong in duoc tom tat cuoi dot ({e}) — ket qua van da ghi vao Anki")
