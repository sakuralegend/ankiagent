# ==============================================================================
# --- PIPELINE DÙNG CHUNG: xử lý trọn vẹn 1 từ (cào -> AI -> đẩy lên Anki) ---
# Cả main.py (CLI trên PC) lẫn bot.py (Telegram trên VPS) đều gọi vào đây,
# nhờ vậy logic chỉ tồn tại MỘT nơi. Hàm này KHÔNG dùng input()/print tương tác
# nên gọi được từ bất kỳ giao diện nào.
# ==============================================================================
import json
import re

from .scraper import process_pure_next_data
from .utils import strip_accents_perfectly
from .ai_client import call_claude_refine, REFINE_PRESETS
from .html_builder import build_html_from_ai_result
from .anki_client import (
    push_to_anki,
    trigger_sync,
    find_duplicate_notes,
    get_note_fields,
    update_note_refined,
)


def process_word(word, deck_name, is_forced=False, do_sync=False):
    """Xử lý trọn vẹn 1 từ: cào OpenRussian -> AI dịch/tạo ví dụ -> đẩy lên Anki.

    Trả về (success: bool, card_info: dict | None, error_msg: str | None).
    - success=True  -> card_info có đủ dữ liệu để hiển thị tóm tắt.
    - success=False -> error_msg mô tả lỗi ngắn gọn (để in ra CLI hoặc gửi Telegram).

    do_sync=True: sau khi thêm thành công sẽ gọi AnkiConnect sync để đẩy lên
    AnkiWeb ngay (dùng trên VPS; trên PC để False vì Anki desktop tự sync).
    """
    extracted_data = process_pure_next_data(word)
    if not extracted_data:
        # card_info mang cờ not_found để giao diện (bot) nhận ra tình huống
        # "từ không có trên OpenRussian" và kích hoạt luồng AI đoán từ nguyên mẫu.
        return False, {"not_found": True}, (
            "Không tìm thấy từ trên OpenRussian (sai chính tả, hoặc là dạng biến cách?)."
        )

    success, card_info = push_to_anki(word, extracted_data, deck_name, is_forced=is_forced)
    if not success:
        err = (card_info or {}).get("error", "")
        if "duplicate" in err.lower():
            return False, card_info, (
                "Anki báo thẻ này ĐÃ TỒN TẠI (trùng mặt trước) dù bước dò trùng không thấy "
                "— thường do thẻ cũ được tạo từ phiên bản trước, thiếu ô WordClean.\n"
                "Cách xử lý: sửa thẻ cũ bằng /sua <từ> <yêu cầu>, hoặc xóa thẻ cũ trong app Anki rồi thêm lại."
            )
        return False, card_info, f"AnkiConnect từ chối thêm note: {err or 'không rõ nguyên nhân'}"

    if do_sync:
        # Ghi lại kết quả sync để giao diện (bot) BÁO RÕ khi thất bại,
        # tránh tình trạng thẻ chỉ nằm trên VPS mà người dùng không biết.
        card_info["synced"] = trigger_sync()

    return True, card_info, None


def refine_note_id(note_id, instruction, do_sync=False):
    """Lõi sửa 1 note theo note_id — dùng chung cho /sua (1 thẻ) và /suadeck (cả deck).

    Trả về (success: bool, result: dict | None, error_msg: str | None).
    - success=True  -> result = {"word", "vi", "examples"} (+ "synced" nếu do_sync).
    - success=False -> result vẫn cố mang {"word": ...} nếu đã đọc được thẻ,
      để giao diện batch báo được TỪ NÀO bị lỗi.

    instruction có thể là "1"/"2"/"3" (lệnh sửa nhanh - xem REFINE_PRESETS
    trong ai_client.py) hoặc yêu cầu tự do.
    """
    instruction = REFINE_PRESETS.get(instruction.strip(), instruction.strip())

    fields = get_note_fields(note_id)
    if fields is None:
        return False, None, "Không đọc được nội dung thẻ từ Anki."

    word_info = {"word": fields.get("Word", "")}
    clean_word = fields.get("WordClean") or strip_accents_perfectly(fields.get("Word", ""))

    current_vi = fields.get("Vietnamese", "")
    # Bóc text thô từ HTML ví dụ hiện tại để AI biết thẻ đang có gì
    current_ex_text = re.sub(r"<[^>]+>", " ", fields.get("ExamplesHTML", ""))
    current_ex_text = re.sub(r"\s+", " ", current_ex_text).strip()[:1500]

    try:
        raw_examples = json.loads(fields.get("RawExamples") or "[]")
    except (json.JSONDecodeError, TypeError):
        raw_examples = []

    ai_result = call_claude_refine(clean_word, current_vi, current_ex_text, raw_examples, instruction)
    if not ai_result:
        return False, word_info, "AI trả thiếu dữ liệu 2 lần liên tiếp — thẻ KHÔNG bị thay đổi. Thử lại nhé."

    examples_html, vi_meaning, simplified = build_html_from_ai_result(ai_result)

    if not update_note_refined(note_id, vi_meaning, examples_html):
        return False, word_info, "Ghi thẻ mới vào Anki thất bại."

    result = {"word": word_info["word"], "vi": vi_meaning, "examples": simplified}
    if do_sync:
        result["synced"] = trigger_sync()

    return True, result, None


def refine_note(word, instruction, do_sync=True):
    """Sửa/làm lại 1 thẻ đã có theo yêu cầu người dùng (luồng /sua của bot).
    Tìm note theo từ (nhiều note trùng -> chọn note mới nhất) rồi gọi refine_note_id."""
    clean_word = strip_accents_perfectly(word)
    dups = find_duplicate_notes(clean_word)
    if not dups:
        return False, None, f"Không tìm thấy thẻ nào cho từ '{word}'."

    note_id = max(d["note_id"] for d in dups)
    success, result, error_msg = refine_note_id(note_id, instruction, do_sync=do_sync)
    if success and not result.get("word"):
        result["word"] = word
    return success, result, error_msg
