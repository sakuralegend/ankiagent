# ==============================================================================
# --- LUỒNG LÀM LẠI THẺ: /sua (1 thẻ) và /suadeck (cả deck).
# "Làm lại" = cào lại OpenRussian + AI sinh lại nghĩa/ví dụ GIỐNG lúc thêm thẻ
# mới, ghi đè lên note cũ nên TIẾN TRÌNH HỌC giữ nguyên (thống nhất 20/07/2026:
# bỏ preset 1/2/3 restyle vì gần như không dùng). /suadeck làm lại từng thẻ trong
# deck — tốn nhiều lượt AI nên vẫn có màn xác nhận, nút ⏹ Dừng, file resume.
# ==============================================================================
import asyncio
import json
import os
import time

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from anki_tools.utils import hl_to_bracket
from anki_tools.pipeline import redo_note, redo_note_id
from anki_tools.anki_client import get_deck_names, trigger_sync

from .core import (
    bao_ket_qua,
    chay_hang_loat,
    dang_chay_hang_loat,
    _PROJECT_ROOT,
    MAX_DECK_BUTTONS,
    SYNC_FAIL_TEXT,
    SYNC_OK_TEXT,
    _deck_buttons_rows,
    _reset_idle_timer,
)

SUADECK_QUOTA_WARN = 400   # gần trần ~500 lượt AI/ngày (làm lại tốn ~1 lượt/thẻ)


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


# ---------------------------------------------------------------------------
# /suadeck — làm lại TOÀN BỘ thẻ trong 1 deck (tốn nhiều lượt AI: có xác nhận,
# nút Dừng giữa chừng, file resume để bот restart vẫn làm tiếp)
# ---------------------------------------------------------------------------

# File lưu danh sách thẻ CHƯA làm lại xong của đợt /suadeck gần nhất (bị Dừng /
# lỗi giữa chừng / bot khởi động lại). /suadeck lần sau hỏi "Làm tiếp?" từ file này.
SUADECK_RESUME_FILE = os.path.join(_PROJECT_ROOT, "suadeck_resume.json")


def _sd_load_resume():
    """Đọc đợt làm lại dở (nếu có). Trả về dict {"deck", "note_ids", ...} hoặc None."""
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
    """Dọn trạng thái chọn dở của /suadeck."""
    for k in ("sd_deck_choices", "sd_deck", "sd_note_ids"):
        user_data.pop(k, None)


def _sd_confirm_text_keyboard(context):
    """Màn xác nhận cuối trước khi chạy batch: deck, số thẻ, ước tính."""
    deck = context.user_data["sd_deck"]
    total = len(context.user_data["sd_note_ids"])
    minutes = max(1, round(total * 11 / 60))  # ~8s (cào+AI) + 3s nghỉ mỗi thẻ
    lines = [
        "🛠 XÁC NHẬN LÀM LẠI TOÀN BỘ DECK",
        f"📦 Deck: {deck}",
        f"🃏 Số thẻ sẽ được LÀM LẠI (cào + AI, ghi đè nghĩa/ví dụ): {total}",
        "✅ Tiến trình học của từng thẻ được giữ nguyên.",
        f"⏱ Ước tính: ~{minutes} phút (mỗi thẻ 1 lượt AI)",
    ]
    if total > SUADECK_QUOTA_WARN:
        lines.append(
            f"🚨 {total} thẻ gần chạm hạn mức AI miễn phí (~500 lượt/ngày) — "
            "nên chia nhỏ hoặc chạy sang 2 ngày."
        )
    lines.append("Chạy chứ?")
    kb = InlineKeyboardMarkup([[
        InlineKeyboardButton("🚀 Bắt đầu", callback_data="sdgo"),
        InlineKeyboardButton("🚫 Hủy", callback_data="sdcancel"),
    ]])
    return "\n".join(lines), kb


async def _run_suadeck(context, chat_id, msg, deck, note_ids):
    """Task chạy nền làm lại cả deck. PHẢI chạy bằng asyncio.create_task: PTB xử lý
    update tuần tự, nếu chạy ngay trong handler thì nút ⏹ Dừng không bao giờ được
    xử lý. Tiến độ hiển thị trong ĐÚNG 1 tin nhắn edit tại chỗ."""
    total = len(note_ids)
    done, failed_words, failed_ids, homonym_words = 0, [], [], []

    async def lam(note_id):
        nonlocal done
        success, result, _ = await asyncio.to_thread(redo_note_id, note_id, False)
        word = hl_to_bracket((result or {}).get("word", "")) or f"note {note_id}"
        if success:
            done += 1
        else:
            # TỪ ĐỒNG TỰ: chạy hàng loạt thì không hỏi từng thẻ được, mà đoán
            # bừa là ghi đè thẻ đang học bằng nghĩa của TỪ KHÁC. Để thẻ nguyên
            # và tách riêng ra báo, kèm lời nhắc /sua thủ công — nếu gộp chung
            # "lỗi" thì user không biết vì sao và cứ bấm Làm tiếp mãi.
            if (result or {}).get("nhieu_muc"):
                homonym_words.append(word)
            failed_words.append(word)
            failed_ids.append(note_id)
        return f"{word} {'✅' if success else '❌'}", True

    def tien_do(lam_roi, tong, nhan):
        return (f"🔄 Làm lại deck '{deck}': thẻ {lam_roi}/{tong}\n"
                f"📝 Vừa xong: {nhan}\n"
                f"✅ xong {done} │ ❌ lỗi {len(failed_words)}")

    stopped, attempted = await chay_hang_loat(
        context, chat_id, msg, note_ids,
        co="sd", stop_data="sdstop", lam=lam, tien_do=tien_do)

    # Danh sách thẻ CHƯA xong (lỗi + chưa chạy tới) -> lưu để /suadeck hỏi "Làm tiếp"
    leftover_ids = failed_ids + list(note_ids[attempted:])
    if leftover_ids:
        _sd_save_resume(deck, leftover_ids)
    else:
        _sd_delete_resume()

    # Sync 1 lần cho cả đợt (chính sách: mọi sửa đổi đều lên AnkiWeb ngay)
    synced = await asyncio.to_thread(trigger_sync)

    title = "⏹ ĐÃ DỪNG làm lại deck" if stopped else "🏁 XONG làm lại deck"
    lines = [
        f"{title} '{deck}': ✅ {done} thẻ │ ❌ {len(failed_words)} lỗi │ tổng {total}",
    ]
    if failed_words:
        shown = ", ".join(failed_words[:10])
        more = f" (+{len(failed_words) - 10} từ nữa)" if len(failed_words) > 10 else ""
        lines.append(f"❌ Từ bị lỗi (thẻ giữ nguyên): {shown}{more}")
    if homonym_words:
        lines.append(
            f"⚠️ {len(homonym_words)} từ ĐỒNG CHÍNH TẢ nên bỏ qua có chủ đích "
            f"({', '.join(homonym_words[:6])}) — chạy hàng loạt thì không hỏi được "
            "nghĩa nào, mà đoán sai là ghi đè bằng nghĩa của từ khác. "
            "Làm lại từng từ bằng /sua để tự chọn."
        )
    if leftover_ids:
        lines.append(
            f"💾 Đã lưu {len(leftover_ids)} thẻ còn dở — gọi /suadeck sẽ có nút ▶️ Làm tiếp."
        )
    lines.append(SYNC_OK_TEXT if synced else SYNC_FAIL_TEXT)
    await bao_ket_qua(msg, lines)


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
        "🛠 LÀM LẠI TOÀN BỘ DECK — AI cào lại + sinh lại nghĩa/ví dụ MỌI thẻ.\n"
        "Chọn deck cần làm lại:"
    )
    return text, InlineKeyboardMarkup(rows)


async def cmd_suadeck(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Làm lại TOÀN BỘ thẻ trong 1 deck: chọn deck bằng nút -> xác nhận -> chạy.
    Nếu có đợt dở (bị Dừng / lỗi giữa chừng) thì hỏi Làm tiếp trước."""
    _reset_idle_timer(context, update.effective_chat.id)
    if context.bot_data.get("sd_running"):
        await update.message.reply_text(
            "⏳ Đang có một đợt làm lại deck chạy dở — chờ xong hoặc bấm ⏹ Dừng ở tin tiến độ nhé."
        )
        return
    ban = dang_chay_hang_loat(context, bo_qua="sd_running")
    if ban:
        await update.message.reply_text(
            f"⏳ Đang chạy đợt '{ban}' — chờ xong rồi gọi /suadeck lại nhé."
        )
        return

    state = _sd_load_resume()
    if state:
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton(
                f"▶️ Làm tiếp {len(state['note_ids'])} thẻ", callback_data="sdresume"
            )],
            [InlineKeyboardButton("📂 Chọn deck khác (bỏ đợt dở)", callback_data="sdfresh")],
            [InlineKeyboardButton("🚫 Hủy", callback_data="sdcancel")],
        ])
        await update.message.reply_text(
            f"🔁 Có đợt làm lại dở: deck '{state['deck']}' còn {len(state['note_ids'])} thẻ "
            f"(lưu lúc {state.get('saved_at', '?')}).",
            reply_markup=kb,
        )
        return

    text, kb = await _sd_deck_list_markup(context)
    if not text:
        await update.message.reply_text("📂 Chưa có deck nào trong Anki.")
        return
    await update.message.reply_text(text, reply_markup=kb)
