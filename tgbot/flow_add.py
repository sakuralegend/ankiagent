# ==============================================================================
# --- LUỒNG THÊM TỪ: gõ từ -> dò trùng -> pipeline (cào OpenRussian -> AI -> Anki).
# Hai nhánh rẽ:
#  • Từ ĐÃ CÓ thẻ -> không báo "bị trùng" suông mà đọc lại nguyên nội dung thẻ đó
#    ra như một mục TỪ ĐIỂN (_duplicate_text_and_keyboard).
#  • Từ không có trên OpenRussian -> từ điển hình thái (hoặc AI) đoán từ nguyên
#    mẫu, user bấm nút xác nhận mới thêm.
# ==============================================================================
import asyncio
import time

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from anki_tools.utils import strip_accents_perfectly
from anki_tools.ai_client import call_claude_lemma
from anki_tools.lemma import guess_lemma_offline
from anki_tools.pipeline import process_word
from anki_tools.anki_client import find_duplicate_notes, note_to_card_info

from .core import _current_deck, _degraded_fix_keyboard
from .hienthi import format_card_summary, format_dictionary_entry


async def _do_add(status_msg, word, deck_name, is_forced, context=None, chon_id=None):
    """Chạy pipeline thêm từ (trong thread) rồi cập nhật tin nhắn trạng thái."""
    t0 = time.time()
    await status_msg.edit_text(f"⏳ Đang xử lý '{word}' (cào OpenRussian → AI → Anki)...")
    success, card_info, error_msg = await asyncio.to_thread(
        process_word, word, deck_name, is_forced, True, chon_id  # do_sync=True trên VPS
    )
    if success:
        markup = None
        if card_info.get("ai_degraded"):
            markup = _degraded_fix_keyboard(card_info.get("clean_word", ""))
        await status_msg.edit_text(
            format_card_summary(card_info, time.time() - t0), reply_markup=markup
        )
    elif (card_info or {}).get("nhieu_muc") and context is not None:
        # TỪ ĐỒNG TỰ -> hỏi user, chưa bấm thì CHƯA thẻ nào được thêm.
        await _show_homonym_buttons(status_msg, context, word,
                                    card_info["nhieu_muc"], deck_name, is_forced)
    elif (card_info or {}).get("not_found") and context is not None:
        # Từ không có trên OpenRussian: có thể sai chính tả hoặc là dạng biến cách
        # -> nhờ AI đoán từ nguyên mẫu rồi hỏi user xác nhận trước khi cào lại.
        await _suggest_lemma(status_msg, word, context)
    else:
        await status_msg.edit_text(f"❌ {error_msg}")


async def _suggest_lemma(status_msg, word, context):
    """Từ không tìm thấy -> đề xuất từ nguyên mẫu cho user bấm xác nhận.

    Hỏi TỪ ĐIỂN HÌNH THÁI trước (pymorphy3, offline): nếu nó nhận ra từ này thì
    đáp án chắc chắn đúng, khỏi tốn lượt AI và khỏi chờ. Chỉ khi từ điển bó tay —
    tức là gõ sai chính tả, thứ mà từ điển không xử lý được nhưng AI thì có — mới
    gọi AI đoán."""
    clean = strip_accents_perfectly(word)
    offline = await asyncio.to_thread(guess_lemma_offline, clean)
    if offline and offline != clean:
        await _show_lemma_buttons(status_msg, context, [offline], [
            f"⚠️ Không tìm thấy '{word}' trên OpenRussian.",
            f"📚 Từ điển hình thái: đây là dạng biến cách của '{offline}'.",
        ])
        return

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
    lines = [
        f"⚠️ Không tìm thấy '{word}' trên OpenRussian.",
        f"🤖 AI đoán từ nguyên mẫu: {guess['lemma']}",
    ]
    if guess["reason_vi"]:
        lines.append(f"💬 {guess['reason_vi']}")
    await _show_lemma_buttons(status_msg, context, [guess["lemma"]] + guess["alternatives"], lines)


async def _show_homonym_buttons(status_msg, context, word, muc, deck_name=None,
                                is_forced=False, che_do="them"):
    """Từ ĐỒNG TỰ -> hiện từng mục thành nút để user chọn nghĩa nào.

    Dùng chung cho CẢ HAI luồng (`che_do="them"` và `"sua"`) vì chúng chạy cùng
    một lõi cào (`pipeline.cao_mot_tu`). Hai bộ nút riêng thì sớm muộn một bên
    được vá còn bên kia không — mà bên không vá lại là bên GHI ĐÈ thẻ đang học.

    `мочь` là động từ *có thể* hay danh từ *sức lực*? Máy không đoán được, mà
    đoán sai thì SAI CẢ THẺ: nghĩa, badge thể/giống, và cả bảng chia. User chốt
    29/07: *"nếu tìm ra nhiều từ đồng chính tả, cho tôi chọn"*.

    Nút mang CHỈ SỐ chứ không mang tên từ — `callback_data` trần 64 byte, chữ
    Cyrillic ăn 2 byte mỗi ký tự nên tên từ dễ vượt (bẫy đã dính, xem
    `_show_lemma_buttons`).
    """
    context.user_data["homonym"] = {"word": word, "muc": muc, "deck": deck_name,
                                    "forced": is_forced, "che_do": che_do}
    rows = [[InlineKeyboardButton(f"{m['pos']} — {m['en'][:40]}",
                                  callback_data=f"dongtu:{i}")]
            for i, m in enumerate(muc)]
    rows.append([InlineKeyboardButton("🚫 Hủy", callback_data="dongtu:cancel")])
    dau = ("Chọn nghĩa bạn muốn học — thẻ sẽ lấy nghĩa, badge và bảng chia "
           "theo đúng mục đó:") if che_do == "them" else (
          "Chọn nghĩa đúng của thẻ ĐANG CÓ — chọn sai là ghi đè thẻ bằng nghĩa "
          "của từ khác. Chưa bấm thì thẻ chưa bị đụng gì:")
    await status_msg.edit_text(
        "\n".join([f"⚠️ '{word}' có {len(muc)} mục ĐỒNG CHÍNH TẢ trên OpenRussian.", dau]),
        reply_markup=InlineKeyboardMarkup(rows),
    )


async def _show_lemma_buttons(status_msg, context, candidates, lines):
    """Hiện các từ nguyên mẫu ứng viên thành nút bấm (dùng chung cho đề xuất của
    từ điển hình thái lẫn của AI). Chưa bấm nút thì KHÔNG thẻ nào được thêm."""
    # Tên từ (Cyrillic) có thể vượt 64 byte callback_data -> nút chỉ mang chỉ số
    context.user_data["lemma_choices"] = candidates
    rows = [
        [InlineKeyboardButton(f"✅ Thêm '{c}'", callback_data=f"lemma:{i}")]
        for i, c in enumerate(candidates)
    ]
    rows.append([InlineKeyboardButton("🚫 Hủy", callback_data="lemma:cancel")])
    await status_msg.edit_text(
        "\n".join(lines + ["Bấm từ đúng để thêm thẻ, hoặc hủy:"]),
        reply_markup=InlineKeyboardMarkup(rows),
    )


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
    """Từ đã có thẻ -> TRA TỪ ĐIỂN: đọc nguyên nội dung thẻ cũ ra (nghĩa, từ loại,
    chủ đề, 3 ví dụ, audio, trạng thái học) thay vì chỉ báo 'bị trùng'. Nút bấm cũ
    (chuyển deck / xóa / thêm trùng) vẫn giữ nguyên bên dưới."""
    dups = pending["dups"]
    sel = pending["sel"]
    card_info = note_to_card_info(dups[sel])
    text = format_dictionary_entry(card_info, index=sel, total=len(dups))

    rows = []
    if len(dups) > 1:
        # Nhiều note cùng từ: bấm để xem chi tiết note khác (bảng vẽ lại tại chỗ)
        rows.append([
            InlineKeyboardButton(
                f"{'👉 ' if i == sel else ''}Note [{i + 1}] {dups[i]['deck'].split('::')[-1]}",
                callback_data=f"sel:{i}",
            )
            for i in range(min(len(dups), 4))
        ])
    # Nút làm lại thẻ (cào + AI lại, giữ tiến trình học). Hai điều kiện:
    # - chỉ khi có ĐÚNG 1 note: redo_note() làm lại note MỚI NHẤT theo từ, nên khi
    #   có nhiều note trùng thì nút sẽ sửa nhầm cái đang xem -> thà đừng hiện;
    # - từ phải nằm gọn trong trần 64 byte của callback_data (còn /sua gõ tay).
    redo_data = f"fix:{card_info.get('clean_word', '')}"
    if len(dups) == 1 and card_info.get("clean_word") and len(redo_data.encode("utf-8")) <= 64:
        rows.append([InlineKeyboardButton("🔄 Làm lại thẻ này", callback_data=redo_data)])
    rows.append([
        InlineKeyboardButton("🚫 Xong", callback_data="act:huy"),
        InlineKeyboardButton("📦 Chuyển deck", callback_data="act:chuyen"),
    ])
    rows.append([
        InlineKeyboardButton("🗑 Xóa cũ + thêm mới", callback_data="act:xoa"),
        InlineKeyboardButton("➕ Vẫn thêm trùng", callback_data="act:trung"),
    ])
    return text, InlineKeyboardMarkup(rows)
