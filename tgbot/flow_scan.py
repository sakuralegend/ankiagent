# ==============================================================================
# --- 📷 LUỒNG QUÉT ẢNH trang sách: OCR từ tiếng Nga -> lemma -> lọc từ đã có ->
# user DUYỆT danh sách (bắt buộc) -> bot mới thêm hàng loạt vào inbox.
# NGUYÊN TẮC user chốt 19/07/2026: bot CHỈ xử lý thô, KHÔNG BAO GIỜ tự thêm —
# mọi lần thêm đều phải qua nút ✅ xác nhận.
# ==============================================================================
import asyncio
import re

from telegram import Update
from telegram.error import TimedOut
from telegram.ext import ContextTypes

from anki_tools.utils import strip_accents_perfectly
from anki_tools.ai_scan import call_claude_scan_words, image_mime_type
from anki_tools.anki_client import get_known_words

from .core import danh_sach_cho_duyet, them_loat_tu, _reset_idle_timer


def _scan_clear(user_data):
    user_data.pop("scan_words", None)
    user_data.pop("scan_msg", None)



def _scan_line(word):
    """1 dòng trong danh sách duyệt: 'lemma ← dạng in trên sách' (chỉ hiện dạng
    gốc khi nó KHÁC lemma, và 🔧 khi pymorphy3 phải sửa lại đáp án của AI).
    Số thứ tự do `danh_sach_cho_duyet` đánh."""
    lemma, seen = word["lemma"], word.get("seen", "")
    line = lemma
    if seen and seen != lemma:
        line += f" ← {seen}"
    if word.get("fixed"):
        line += " 🔧"
    return line


def _scan_list_text_keyboard(words, scanned_total=None):
    """Màn duyệt của luồng QUÉT ẢNH. Phần khung (đánh số, cắt theo trần tin nhắn,
    nút ✅/🚫, lời nhắc 'bỏ 3 7') dùng chung ở `core.danh_sach_cho_duyet`."""
    header = f"📷 {len(words)} từ MỚI chưa có thẻ"
    if scanned_total is not None and scanned_total > len(words):
        header += f" (quét được {scanned_total}, đã lọc {scanned_total - len(words)} từ có thẻ rồi)"
    duoi = (["🔧 = từ điển hình thái đã sửa lại dạng nguyên thể AI đọc được."]
            if any(w.get("fixed") for w in words) else [])
    return danh_sach_cho_duyet([_scan_line(w) for w in words], tieu_de=header,
                               cb_them="scanadd", cb_huy="scancancel", duoi=duoi)


# Ảnh gửi dạng FILE giữ nguyên độ nét, nhưng nhét nguyên bản vào request AI thì
# base64 phình ~33% -> quá nặng. Trần này để bot từ chối sớm với lời khuyên rõ ràng
# thay vì treo rồi lỗi khó hiểu.
_MAX_IMAGE_BYTES = 8 * 1024 * 1024


async def _download_image(message, status):
    """Tải ảnh từ Telegram (nhận cả photo nén lẫn document ảnh gốc).
    Trả về bytes, hoặc None nếu đã báo lỗi cho user."""
    getter = (message.photo[-1] if message.photo else message.document)
    for attempt in (1, 2):
        try:
            tg_file = await getter.get_file()
            return bytes(await tg_file.download_as_bytearray())
        except TimedOut:
            if attempt == 1:
                await asyncio.sleep(3)  # mạng chững thoáng qua -> thử lại 1 lần
                continue
            await status.edit_text("❌ Mạng Telegram đang chậm, tải ảnh thất bại — gửi lại ảnh thử nhé.")
            return None
        except Exception:
            await status.edit_text("❌ Không tải được ảnh từ Telegram, gửi lại thử nhé.")
            return None


def _already_has_card(word, known):
    """Từ coi như ĐÃ CÓ THẺ khi dạng từ điển HOẶC dạng in trên trang sách trùng
    một thẻ sẵn có.

    Phải xét cả hai vì bước đưa về nguyên thể có thể đổi từ sang một mục từ điển
    KHÁC mà vẫn hợp lệ: ca thật 21/07/2026 — trang sách có 'это' (đã có thẻ),
    AI đưa về 'этот' (chưa có thẻ) nên bot báo là TỪ MỚI, dù người học chẳng học
    thêm được gì. Chỉ so mỗi lemma là còn nguyên cái bẫy đó cho những cặp khác."""
    forms = {word.get("lemma", ""), word.get("seen", "")}
    return any(strip_accents_perfectly(f).lower() in known for f in forms if f)


async def on_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Nhận ảnh trang sách: quét từ mới rồi CHỜ user duyệt (không tự thêm).

    Nhận CẢ HAI kiểu gửi: ảnh thường (Telegram nén còn ~1280px) và ảnh gửi dạng
    FILE/document (giữ nguyên độ nét máy ảnh). Sách chữ nhỏ nên gửi dạng file:
    chữ càng nét thì AI càng ít bỏ sót từ."""
    _reset_idle_timer(context, update.effective_chat.id)
    try:
        status = await update.message.reply_text("📷 Đang tải ảnh về...")
    except TimedOut:
        # Mạng VPS<->Telegram chững một nhịp (19/07/2026: từng chết ở đây với
        # trần 5s cũ, user kẹt ở "Đang tải ảnh"). Tin đầu có thể ĐÃ tới user dù
        # client báo lỗi -> thử lại 1 lần rồi đi tiếp; lỗi nữa thì bó tay thật.
        status = await update.message.reply_text("📷 Đang tải ảnh về... (mạng chậm)")

    image_bytes = await _download_image(update.message, status)
    if image_bytes is None:
        return
    if len(image_bytes) > _MAX_IMAGE_BYTES:
        await status.edit_text(
            f"❌ Ảnh nặng {len(image_bytes) / 1024 / 1024:.1f}MB, quá cỡ gửi cho AI (trần 8MB).\n"
            "Gửi lại dạng ẢNH thường (Telegram tự nén) hoặc chụp lại ở độ phân giải thấp hơn."
        )
        return
    if not image_mime_type(image_bytes):
        # Hay gặp khi gửi ảnh dạng FILE từ iPhone: file gốc là HEIC
        await status.edit_text(
            "❌ Định dạng ảnh này AI không đọc được (chỉ nhận JPEG/PNG/WEBP — file iPhone\n"
            "gửi nguyên bản thường là HEIC).\nGửi lại dạng ẢNH thường là được ngay."
        )
        return

    await status.edit_text("🔍 AI đang đọc từ tiếng Nga trong ảnh (1 lượt AI, có thể hơi lâu)...")
    words = await asyncio.to_thread(call_claude_scan_words, image_bytes)
    if not words:
        await status.edit_text(
            "❌ AI không đọc được từ tiếng Nga nào trong ảnh.\n"
            "Thử chụp gần hơn / rõ nét hơn, hoặc gửi ảnh dạng FILE để giữ nguyên độ nét."
        )
        return

    known = await asyncio.to_thread(get_known_words)
    if known is None:
        await status.edit_text("❌ Không đọc được danh sách từ đã có từ Anki — thử gửi lại ảnh sau nhé.")
        return
    new_words = [w for w in words if not _already_has_card(w, known)]
    if not new_words:
        await status.edit_text(f"✅ Cả {len(words)} từ quét được đều ĐÃ có thẻ — không có từ mới.")
        return

    context.user_data["scan_words"] = new_words
    context.user_data["scan_msg"] = status
    text, kb = _scan_list_text_keyboard(new_words, scanned_total=len(words))
    await status.edit_text(text, reply_markup=kb)


async def _scan_exclude(update, context, text):
    """Xử lý tin nhắn 'bỏ 3 7 12': loại từ khỏi danh sách quét rồi vẽ lại."""
    idxs = {int(x) for x in re.findall(r"\d+", text)}
    words = context.user_data["scan_words"]
    kept = [w for i, w in enumerate(words, 1) if i not in idxs]
    if not kept:
        _scan_clear(context.user_data)
        await update.message.reply_text("🚫 Đã loại hết từ — hủy đợt quét này.")
        return
    context.user_data["scan_words"] = kept
    list_text, kb = _scan_list_text_keyboard(kept)
    old_msg = context.user_data.get("scan_msg")
    try:
        # Vẽ lại danh sách ngay trên tin nhắn cũ (gỡ luôn nút cũ cho khỏi bấm nhầm)
        await old_msg.edit_text(list_text, reply_markup=kb)
        await update.message.reply_text(f"✂️ Đã loại {len(words) - len(kept)} từ (danh sách ở tin trên).")
    except Exception:
        # Tin cũ quá xa/lỗi edit -> gửi danh sách thành tin mới
        new_msg = await update.message.reply_text(list_text, reply_markup=kb)
        context.user_data["scan_msg"] = new_msg


async def _run_scan_add(context, chat_id, msg, words):
    """Thêm loạt từ user ĐÃ DUYỆT từ ảnh. Việc thật nằm ở `core.them_loat_tu` —
    ở đây chỉ còn phần RIÊNG của luồng quét: lấy dạng từ điển pymorphy3 đã chốt,
    và lời khuyên khi user bấm ⏹ Dừng giữa chừng."""
    await them_loat_tu(
        context, chat_id, msg, [w["lemma"] for w in words],
        co="scan", stop_data="scanstop", nhan="từ quét ảnh",
        con_lai="gửi lại ảnh để quét lại (từ đã thêm sẽ tự bị lọc).")
