# ==============================================================================
# --- LUỒNG SỬA THẺ: /sua (1 thẻ, 3 preset + tự viết yêu cầu) và /suadeck
# (sửa TOÀN BỘ thẻ trong 1 deck — có màn xác nhận, nút ⏹ Dừng, file resume).
# ==============================================================================
import asyncio
import json
import os
import time

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from anki_tools.utils import hl_to_bracket
from anki_tools.pipeline import refine_note, refine_note_id
from anki_tools.anki_client import get_deck_names, get_deck_note_ids, trigger_sync

from .core import (
    _PROJECT_ROOT,
    MAX_DECK_BUTTONS,
    SYNC_FAIL_TEXT,
    SYNC_OK_TEXT,
    _deck_buttons_rows,
    _reset_idle_timer,
)


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


def _sua_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("1️⃣ Ngắn hơn", callback_data="sua:1"),
            InlineKeyboardButton("2️⃣ Đổi ví dụ", callback_data="sua:2"),
            InlineKeyboardButton("3️⃣ Dài hơn", callback_data="sua:3"),
        ],
        [InlineKeyboardButton("✏️ Tự viết yêu cầu", callback_data="sua:custom")],
    ])


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


# ---------------------------------------------------------------------------
# /suadeck — sửa TOÀN BỘ thẻ trong 1 deck (ít dùng; ghi đè hàng loạt nên có
# màn xác nhận trước khi chạy + nút Dừng giữa chừng)
# ---------------------------------------------------------------------------

SUADECK_QUOTA_WARN = 450  # gần trần 500 lượt Gemini free/ngày thì cảnh báo đậm
SUADECK_DELAY_SECONDS = 3  # nghỉ giữa 2 thẻ để không dồn dập chạm giới hạn RPM

_SD_LABELS = {"1": "1️⃣ Ngắn hơn", "2": "2️⃣ Đổi ví dụ", "3": "3️⃣ Dài hơn"}

# File lưu danh sách thẻ CHƯA sửa xong của đợt /suadeck gần nhất (bị Dừng /
# lỗi giữa chừng / bot restart). /suadeck lần sau sẽ hỏi "Sửa tiếp?" từ file này.
SUADECK_RESUME_FILE = os.path.join(_PROJECT_ROOT, "suadeck_resume.json")


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
