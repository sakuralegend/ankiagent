# ==============================================================================
# --- 📷 LUỒNG QUÉT ẢNH trang sách: OCR từ tiếng Nga -> lemma -> lọc từ đã có ->
# user DUYỆT danh sách (bắt buộc) -> bot mới thêm hàng loạt vào inbox.
# NGUYÊN TẮC user chốt 19/07/2026: bot CHỈ xử lý thô, KHÔNG BAO GIỜ tự thêm —
# mọi lần thêm đều phải qua nút ✅ xác nhận.
# ==============================================================================
import asyncio
import re

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.error import TimedOut
from telegram.ext import ContextTypes

from anki_tools.config import INBOX_DECK
from anki_tools.utils import strip_accents_perfectly
from anki_tools.ai_client import call_claude_scan_words, image_mime_type
from anki_tools.pipeline import process_word
from anki_tools.anki_client import find_duplicate_notes, get_known_words, trigger_sync

from .core import SYNC_FAIL_TEXT, SYNC_OK_TEXT, _reset_idle_timer
from .flow_edit import SUADECK_DELAY_SECONDS


def _scan_clear(user_data):
    user_data.pop("scan_words", None)
    user_data.pop("scan_msg", None)


def _join_words(words, limit=30):
    shown = ", ".join(words[:limit])
    more = f" (+{len(words) - limit} từ nữa)" if len(words) > limit else ""
    return shown + more


# Trần 1 tin nhắn Telegram là 4096 ký tự — trang sách dày có thể ra hàng trăm từ,
# vượt trần thì Telegram TỪ CHỐI cả tin, user không thấy gì để duyệt.
_LIST_TEXT_BUDGET = 3500


def _scan_line(index, word):
    """1 dòng trong danh sách duyệt: 'stt. lemma ← dạng in trên sách' (chỉ hiện
    dạng gốc khi nó KHÁC lemma, và 🔧 khi pymorphy3 phải sửa lại đáp án của AI)."""
    lemma, seen = word["lemma"], word.get("seen", "")
    line = f"{index}. {lemma}"
    if seen and seen != lemma:
        line += f" ← {seen}"
    if word.get("fixed"):
        line += " 🔧"
    return line


def _scan_list_text_keyboard(words, scanned_total=None):
    """Danh sách từ mới chờ user duyệt + nút xác nhận. Đây là CHỐT AN TOÀN:
    không bấm ✅ thì không có gì được thêm vào Anki."""
    minutes = max(1, round(len(words) * 11 / 60))  # ~8s AI + 3s nghỉ mỗi từ
    header = f"📷 {len(words)} từ MỚI chưa có thẻ"
    if scanned_total is not None and scanned_total > len(words):
        header += f" (quét được {scanned_total}, đã lọc {scanned_total - len(words)} từ có thẻ rồi)"

    lines, used, hidden = [header + ":"], len(header), 0
    for i, w in enumerate(words, 1):
        line = _scan_line(i, w)
        if used + len(line) > _LIST_TEXT_BUDGET:
            hidden = len(words) - i + 1
            break
        lines.append(line)
        used += len(line) + 1
    if hidden:
        lines.append(f"… và {hidden} từ nữa (không hiện hết được trong 1 tin nhắn).")

    lines.append("")
    if any(w.get("fixed") for w in words):
        lines.append("🔧 = từ điển hình thái đã sửa lại dạng nguyên thể AI đọc được.")
    lines.append(f"⏱ Thêm hết tốn ~{minutes} phút, {len(words)} lượt AI.")
    lines.append("Muốn loại từ nào: nhắn 'bỏ 3 7 12'. Chưa bấm ✅ thì chưa thêm gì.")
    kb = InlineKeyboardMarkup([[
        InlineKeyboardButton(f"✅ Thêm cả {len(words)} từ", callback_data="scanadd"),
        InlineKeyboardButton("🚫 Hủy", callback_data="scancancel"),
    ]])
    return "\n".join(lines), kb


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
    """Task nền thêm loạt từ user ĐÃ DUYỆT từ ảnh. Mỗi từ đi qua đúng pipeline
    thêm từ thường (cào OpenRussian -> AI -> Anki; deck None = tự động -> inbox),
    nghỉ giữa 2 từ chống chạm giới hạn mỗi-phút. Chạy bằng create_task để nút
    ⏹ Dừng vẫn được xử lý (PTB xử lý update tuần tự — giống /suadeck)."""
    context.bot_data["scan_running"] = True
    context.bot_data["scan_stop"] = False
    total = len(words)
    added, skipped_dup, failed = [], [], []
    stop_kb = InlineKeyboardMarkup([[InlineKeyboardButton("⏹ Dừng", callback_data="scanstop")]])
    stopped = False
    attempted = 0

    try:
        for i, item in enumerate(words):
            if context.bot_data.get("scan_stop"):
                stopped = True
                break
            _reset_idle_timer(context, chat_id)
            attempted = i + 1
            word = item["lemma"]  # dạng từ điển đã qua tay pymorphy3 — thứ dùng để cào

            # Dò trùng lần cuối ngay trước khi thêm (rẻ, không tốn AI) — phòng
            # trường hợp từ vừa được thêm tay giữa lúc quét và lúc bấm ✅
            dups = await asyncio.to_thread(find_duplicate_notes, strip_accents_perfectly(word))
            if dups:
                skipped_dup.append(word)
                mark = "⏭ đã có"
            else:
                success, card_info, error_msg = await asyncio.to_thread(
                    process_word, word, None, False, False  # sync 1 lần cuối đợt
                )
                if success:
                    added.append(word)
                    mark = "✅"
                else:
                    failed.append(word)
                    mark = "❌"
                # Nghỉ chống RPM — chỉ cần sau lượt có gọi AI thật
                if attempted < total and not context.bot_data.get("scan_stop"):
                    await asyncio.sleep(SUADECK_DELAY_SECONDS)

            progress = (
                f"🔄 Thêm từ quét ảnh: {attempted}/{total}\n"
                f"📝 Vừa xong: {word} {mark}\n"
                f"✅ thêm {len(added)} │ ⏭ trùng {len(skipped_dup)} │ ❌ lỗi {len(failed)}"
            )
            try:
                await msg.edit_text(progress, reply_markup=stop_kb)
            except Exception:
                pass  # nội dung trùng / mạng chớp — vòng sau edit tiếp
    finally:
        context.bot_data["scan_running"] = False
        context.bot_data["scan_stop"] = False

    synced = await asyncio.to_thread(trigger_sync) if added else True

    title = "⏹ ĐÃ DỪNG thêm từ quét ảnh" if stopped else "🏁 XONG thêm từ quét ảnh"
    lines = [f"{title}: ✅ {len(added)} │ ⏭ trùng {len(skipped_dup)} │ ❌ lỗi {len(failed)} │ tổng {total}"]
    if added:
        lines.append(f"📥 Đã vào {INBOX_DECK}: {_join_words(added)}")
    if skipped_dup:
        lines.append(f"⏭ Đã có thẻ từ trước: {_join_words(skipped_dup)}")
    if failed:
        lines.append(f"❌ Chưa tạo được thẻ: {_join_words(failed)}")
        lines.append("   → gõ tay từng từ lỗi: bot sẽ dò OpenRussian + đoán từ nguyên mẫu như thường.")
    if stopped and attempted < total:
        lines.append(
            f"💤 Còn {total - attempted} từ chưa chạy tới — gửi lại ảnh để quét lại "
            "(từ đã thêm sẽ tự bị lọc)."
        )
    lines.append(SYNC_OK_TEXT if synced else SYNC_FAIL_TEXT)
    try:
        await msg.edit_text("\n".join(lines))
    except Exception:
        pass
