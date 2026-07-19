# ==============================================================================
# --- LUỒNG THÊM TỪ: gõ từ -> dò trùng -> pipeline (cào OpenRussian -> AI ->
# Anki); từ không có trên OpenRussian -> AI đoán từ nguyên mẫu, user bấm nút.
# ==============================================================================
import asyncio
import time

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from anki_tools.utils import strip_accents_perfectly
from anki_tools.ai_client import call_claude_lemma
from anki_tools.pipeline import process_word
from anki_tools.anki_client import find_duplicate_notes

from .core import _current_deck, _degraded_fix_keyboard, format_card_summary


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
