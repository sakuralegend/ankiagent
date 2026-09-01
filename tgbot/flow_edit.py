# ==============================================================================
# --- LUỒNG LÀM LẠI THẺ: /sua (MỘT thẻ) ---
# "Làm lại" = cào lại OpenRussian + AI sinh lại nghĩa/ví dụ GIỐNG lúc thêm thẻ
# mới, ghi đè lên note cũ nên TIẾN TRÌNH HỌC giữ nguyên (thống nhất 20/07/2026:
# bỏ preset 1/2/3 restyle vì gần như không dùng).
#
# 🔴 ĐÃ XOÁ `/suadeck` (01/09/2026, QD-42) — đừng dựng lại. Nó làm lại CẢ deck
# bằng một nút trên điện thoại, không xem trước, ghi đè mọi thẻ từ một nguồn đã
# đo được là sai (`тут` OpenRussian xếp là DANH TỪ). Ra đời 15/07 cho deck-theo-
# ngày, mà cây deck theo CHỦ ĐỀ ra đời 18/07 — nó chết từ lúc đó, `VPS_SETUP.md`
# đã ghi "ít dùng". Cần sửa hàng loạt thì dùng script có chạy khan xem trước
# (`scripts/backfill_badge.py`), đừng dùng nút không hoàn tác được.
# ==============================================================================
import asyncio
import time

from telegram import Update
from telegram.ext import ContextTypes

from anki_tools.utils import hl_to_bracket, log_debug, log_warn
from anki_tools.pipeline import redo_note

from .core import SYNC_FAIL_TEXT, SYNC_OK_TEXT, _reset_idle_timer


async def _do_redo(status_msg, word, context=None, chon_id=None):
    """Làm lại 1 thẻ (trong thread) rồi cập nhật tin nhắn trạng thái.

    Dừng lại HỎI khi từ đồng tự, y như luồng thêm thẻ mới — vì `/sua` chạy đúng
    lõi đó (xem `pipeline.cao_mot_tu`). Trước 29/07 `/sua` tự chọn mục có bảng
    chia dày nhất, tức có thể ghi đè thẻ đang học bằng nghĩa của TỪ KHÁC.
    """
    t0 = time.time()
    await status_msg.edit_text(f"⏳ Đang làm lại thẻ '{word}' (cào lại → AI → audio)...")
    success, result, error_msg = await asyncio.to_thread(redo_note, word, True, chon_id)
    if not success:
        if (result or {}).get("nhieu_muc") and context is not None:
            # KHÔNG có vòng import ở đây (`flow_add` chỉ import `core`) — comment
            # cũ ghi "tránh import vòng" là nói dối, đã xoá 31/07/2026. Import
            # vẫn để trong hàm vì đây là chỗ DUY NHẤT hai flow chạm nhau, để nó
            # ở đây thì `soatkientruc.py` S3 chỉ đúng một dòng khi tới lượt dọn.
            from .flow_add import _show_homonym_buttons
            await _show_homonym_buttons(status_msg, context, word,
                                        result["nhieu_muc"], che_do="sua")
            return
        await status_msg.edit_text(f"❌ {error_msg}")
        return
    lines = [f"🔄 ĐÃ LÀM LẠI THẺ: {hl_to_bracket(result['word'])}", f"🇻🇳 {result['vi']}"]
    for i, ex in enumerate(result["examples"][:3]):
        lines.append(f"💡 {i + 1}. {hl_to_bracket(ex.get('ru', ''))}")
        en = hl_to_bracket(ex.get("en", ""))
        vi = hl_to_bracket(ex.get("vi") or ex.get("vietnamese") or "")
        if en:
            lines.append(f"     🇬🇧 {en}")
        if vi:
            lines.append(f"     🇻🇳 {vi}")
    if result.get("audio_source") == "google_tts":
        lines.append("🔊 OpenRussian lỗi audio nên đã dùng Google TTS (giọng máy).")
    if result.get("ai_degraded"):
        lines.append("⚠️ AI không tạo được ví dụ/nghĩa Việt lần này — thử /sua lại lần nữa.")
    lines.append(f"✅ Tiến trình học giữ nguyên. ⏱ {time.time() - t0:.1f}s")
    lines.append(SYNC_FAIL_TEXT if result.get("synced") is False else SYNC_OK_TEXT)
    await status_msg.edit_text("\n".join(lines))


async def cmd_sua(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/sua [từ] — làm lại thẻ. Không có từ -> bot hỏi từ (để gõ bàn phím Nga)."""
    _reset_idle_timer(context, update.effective_chat.id)
    if not context.args:
        context.user_data["awaiting"] = "sua_word"
        await update.message.reply_text("🔄 Gõ từ cần làm lại thẻ (chỉ cần gõ từ):")
        return
    word = context.args[0]
    msg = await update.message.reply_text("⏳ Chuẩn bị làm lại thẻ...")
    await _do_redo(msg, word, context)
