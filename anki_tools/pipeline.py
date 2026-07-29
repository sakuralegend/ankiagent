# ==============================================================================
# --- PIPELINE DÙNG CHUNG: xử lý trọn vẹn 1 từ (cào -> AI -> đẩy lên Anki) ---
# Cả main.py (CLI trên PC) lẫn bot.py (Telegram trên VPS) đều gọi vào đây,
# nhờ vậy logic chỉ tồn tại MỘT nơi. Hàm này KHÔNG dùng input()/print tương tác
# nên gọi được từ bất kỳ giao diện nào.
# ==============================================================================
import re

from . import grammar
from .grammar import cac_muc_dong_tu, fetch_page, tom_tat_muc
from .scraper import process_pure_next_data
from .utils import strip_accents_perfectly
from .anki_client import (
    build_card_fields,
    find_duplicate_notes,
    get_note_full,
    push_to_anki,
    set_topic_tag,
    store_word_audio,
    trigger_sync,
    update_note_fields,
)


def process_word(word, deck_name, is_forced=False, do_sync=False, chon_id=None):
    """Xử lý trọn vẹn 1 từ: cào OpenRussian -> AI dịch/tạo ví dụ -> đẩy lên Anki.

    deck_name=None -> chế độ TỰ ĐỘNG: thẻ vào deck con theo chủ đề AI chọn
    (xem push_to_anki). card_info["deck"] luôn là deck THẬT thẻ được thêm vào.

    Trả về (success: bool, card_info: dict | None, error_msg: str | None).
    - success=True  -> card_info có đủ dữ liệu để hiển thị tóm tắt.
    - success=False -> error_msg mô tả lỗi ngắn gọn (để in ra CLI hoặc gửi Telegram).

    do_sync=True: sau khi thêm thành công sẽ gọi AnkiConnect sync để đẩy lên
    AnkiWeb ngay (dùng trên VPS; trên PC để False vì Anki desktop tự sync).

    TỪ ĐỒNG TỰ: nếu trang có >1 mục đúng chính tả (`мочь` động từ *có thể* /
    danh từ *sức lực*) và `chon_id=None`, hàm DỪNG LẠI và trả
    `(False, {"nhieu_muc": [...]}, None)` để giao diện hỏi user chọn — máy không
    có cách nào biết user định học nghĩa nào. Gọi lại với `chon_id` để chạy tiếp.
    """
    if chon_id is None:
        info = fetch_page(word)
        muc = cac_muc_dong_tu(info, word)
        if len(muc) > 1:
            return False, {"nhieu_muc": [tom_tat_muc(m) for m in muc]}, None

    extracted_data = process_pure_next_data(word, chon_id=chon_id)
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
                "Cách xử lý: làm lại thẻ cũ bằng /sua, hoặc xóa thẻ cũ trong app Anki rồi thêm lại."
            )
        return False, card_info, f"AnkiConnect từ chối thêm note: {err or 'không rõ nguyên nhân'}"

    if do_sync:
        # Ghi lại kết quả sync để giao diện (bot) BÁO RÕ khi thất bại,
        # tránh tình trạng thẻ chỉ nằm trên VPS mà người dùng không biết.
        card_info["synced"] = trigger_sync()

    return True, card_info, None


def redo_note_id(note_id, do_sync=False):
    """LÀM LẠI 1 thẻ đã có: cào lại OpenRussian + AI sinh lại nghĩa/ví dụ giống hệt
    lúc thêm thẻ MỚI, rồi GHI ĐÈ lên đúng note đó (giữ nguyên note_id -> tiến trình
    học không đổi). Cũng làm mới tag chủ đề, và VÁ audio nếu thẻ đang thiếu tiếng.
    Dùng chung cho /sua (1 thẻ) và /suadeck (cả deck).

    Trả về (success, result, error_msg).
    - success=True  -> result = {"word","vi","examples","ai_degraded","topic",
      "audio_source"} (+ "synced" nếu do_sync).
    - success=False -> result cố mang {"word": ...} nếu đã đọc được thẻ, để giao
      diện batch báo được TỪ NÀO lỗi. Thẻ KHÔNG bị thay đổi khi lỗi.
    """
    info = get_note_full(note_id)
    if info is None:
        return False, None, "Không đọc được nội dung thẻ từ Anki."

    fields = info["fields"]
    tags = info["tags"]
    word_info = {"word": fields.get("Word", "")}
    clean_word = fields.get("WordClean") or strip_accents_perfectly(fields.get("Word", ""))
    if not clean_word:
        return False, word_info, "Thẻ không có từ (WordClean rỗng) để làm lại."

    data = process_pure_next_data(clean_word)
    if not data:
        return False, word_info, (
            f"Không cào lại được '{clean_word}' trên OpenRussian (từ hiếm hoặc trang đổi cấu trúc). "
            "Thẻ giữ nguyên, không thay đổi gì."
        )

    built = build_card_fields(clean_word, data)
    new_fields = dict(built["fields"])

    # 🔴 GIỮ phần chữ của ô Hướng dẫn. `build_card_fields()` dựng `HuongDan` chỉ
    # gồm BẢNG CHIA (đúng cho thẻ mới tinh), nhưng ở đây thẻ đã tồn tại và có thể
    # đã được soạn kỹ phần chẻ từ / cách nhớ / họ hàng. Ghi thẳng là user bấm
    # "làm lại thẻ" rồi mất trắng nội dung mà không ai báo. `attach_table` chỉ
    # thay đúng cái bảng, chừa nguyên phần chữ.
    new_fields["HuongDan"] = grammar.attach_table(
        fields.get("HuongDan") or "", data.get("grammar") or {})

    # Audio: chỉ tải khi thẻ ĐANG THIẾU tiếng. "Thiếu" = ô Audio không có tag
    # [sound:...] hợp lệ — gồm cả thẻ trống LẪN thẻ mà AnkiConnect từng ghi câu
    # lỗi "...download failed with return code 500" vào ô Audio (bug cũ). Khi đó
    # ghi đè ô Audio bằng tiếng mới, hoặc "" để ít nhất xóa câu lỗi rác.
    audio_source = ""
    if not re.search(r"\[sound:[^\]]+\]", fields.get("Audio") or ""):
        audio_field, audio_source = store_word_audio(clean_word)
        new_fields["Audio"] = audio_field

    if not update_note_fields(note_id, new_fields):
        return False, word_info, "Ghi thẻ mới vào Anki thất bại (thẻ giữ nguyên)."

    # Làm mới tag chủ đề theo phân loại AI mới (không đụng tiến trình học)
    set_topic_tag(note_id, tags, built["topic_slug"])

    result = {
        "word": built["fields"]["Word"],
        "vi": built["vi_meaning"],
        "examples": built["simplified_examples"],
        "ai_degraded": built["ai_degraded"],
        "topic": built["topic_slug"] or "",
        "audio_source": audio_source,   # "google_tts" nếu vừa vá bằng TTS dự phòng
    }
    if do_sync:
        result["synced"] = trigger_sync()

    return True, result, None


def redo_note(word, do_sync=True):
    """Làm lại 1 thẻ theo TỪ (luồng /sua của bot). Tìm note theo từ (nhiều note
    trùng -> chọn note mới nhất) rồi gọi redo_note_id."""
    clean_word = strip_accents_perfectly(word)
    dups = find_duplicate_notes(clean_word)
    if not dups:
        return False, None, f"Không tìm thấy thẻ nào cho từ '{word}'."

    note_id = max(d["note_id"] for d in dups)
    success, result, error_msg = redo_note_id(note_id, do_sync=do_sync)
    if success and not result.get("word"):
        result["word"] = word
    return success, result, error_msg
