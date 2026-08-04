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


# ------------------------------------------------------------------ LÕI CHUNG
# 🔴 THÊM THẺ MỚI và LÀM LẠI THẺ (/sua) là CÙNG MỘT CƠ CHẾ — user chốt 29/07:
# *"nút /sua cơ chế giống y như thêm một thẻ mới, hãy gom chúng với luồng tạo thẻ
# mới; phần hướng dẫn kia nếu có thì không đụng vào"*.
#
# `/sua` dùng để VÁ khi một lỗi bất định làm thẻ mất field nào đó (bảng chia,
# nghĩa, audio…). Muốn vá được thì nó phải dựng ra ĐÚNG thứ mà luồng thêm mới
# dựng, nếu không thì thẻ vá xong vẫn khác thẻ mới — mà lệch chỗ nào thì không
# ai biết. Nên phần cào + hỏi từ đồng tự nằm ở đây, cả hai bên gọi vào.
#
# CHỈ CÓ BA CHỖ KHÁC NHAU, và cả ba đều cố ý:
#   1. `HuongDan` — làm lại thì GIỮ phần chữ, chỉ thay bảng chia. Đó là phần
#      soạn tay qua Claude (README §2), máy không dựng lại được.
#   2. `Stage` + deck + note_id — làm lại thì KHÔNG đụng, để giữ tiến trình học.
#   3. `Audio` — làm lại chỉ tải khi thẻ ĐANG THIẾU tiếng, vì `/suadeck` chạy cả
#      deck mà tải lại toàn bộ audio là vô ích và rất chậm.
# Thêm chỗ khác thứ tư thì phải ghi vào danh sách này, đừng để nó lặng lẽ trôi.


def cao_mot_tu(word, chon_id=None):
    """Cào OpenRussian cho 1 từ, có chốt HỎI khi gặp từ đồng tự.

    Trả `(data, dung_lai)`:
      · `data` != None            -> cào xong, chạy tiếp được
      · `dung_lai = {"nhieu_muc"}`-> PHẢI hỏi user chọn mục rồi gọi lại kèm `chon_id`
      · `dung_lai = {"not_found"}`-> không có từ này trên OpenRussian

    🔴 Chốt từ đồng tự phải nằm ở lõi chung, KHÔNG nằm riêng bên luồng thêm mới.
    Trước 29/07 nó chỉ có ở `process_word`, nên `/sua` trên `мочь` lặng lẽ lấy mục
    có bảng chia dày nhất — đoán sai là ghi đè thẻ đang học bằng nghĩa của TỪ KHÁC
    (nghĩa, badge thể/giống và bảng chia đều đi theo mục đã chọn).
    """
    if chon_id is None:
        muc = cac_muc_dong_tu(fetch_page(word), word)
        if len(muc) > 1:
            return None, {"nhieu_muc": [tom_tat_muc(m) for m in muc]}
    data = process_pure_next_data(word, chon_id=chon_id)
    if not data:
        return None, {"not_found": True}
    return data, None


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
    extracted_data, dung_lai = cao_mot_tu(word, chon_id)
    if dung_lai is not None:
        if dung_lai.get("nhieu_muc"):
            return False, dung_lai, None
        # card_info mang cờ not_found để giao diện (bot) nhận ra tình huống
        # "từ không có trên OpenRussian" và kích hoạt luồng AI đoán từ nguyên mẫu.
        return False, dung_lai, (
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


def redo_note_id(note_id, do_sync=False, chon_id=None):
    """LÀM LẠI 1 thẻ đã có — CÙNG LÕI với luồng thêm thẻ mới (xem khối comment
    "LÕI CHUNG" ở trên để biết ba chỗ cố ý khác nhau).

    Cào lại OpenRussian + AI sinh lại nghĩa/ví dụ y như lúc thêm thẻ MỚI, rồi GHI
    ĐÈ lên đúng note đó (giữ note_id -> tiến trình học không đổi). Cũng làm mới
    tag chủ đề, và vá audio nếu thẻ đang thiếu tiếng.
    Dùng chung cho /sua (1 thẻ) và /suadeck (cả deck).

    Trả về (success, result, error_msg).
    - success=True  -> result = {"word","vi","examples","ai_degraded","topic",
      "audio_source"} (+ "synced" nếu do_sync).
    - success=False -> result cố mang {"word": ...} nếu đã đọc được thẻ, để giao
      diện batch báo được TỪ NÀO lỗi. Thẻ KHÔNG bị thay đổi khi lỗi.
    - success=False + result["nhieu_muc"] -> TỪ ĐỒNG TỰ, giao diện phải hỏi rồi
      gọi lại kèm `chon_id`. Thẻ chưa bị đụng gì.
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

    data, dung_lai = cao_mot_tu(clean_word, chon_id)
    if dung_lai is not None:
        if dung_lai.get("nhieu_muc"):
            return False, {**word_info, **dung_lai}, None
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
    new_fields["HuongDan"] = grammar.go_bang(fields.get("HuongDan") or "")

    # 🔴 GIỮ nghĩa tiếng Việt user đã sửa TAY (QD-27). Cùng lý lẽ với ô Hướng dẫn
    # ngay trên: `build_card_fields()` dựng lại `Vietnamese` bằng một lượt dịch
    # AI mới, nên ghi thẳng là user bấm "làm lại thẻ" rồi mất bản mình tự chữa —
    # mà đây là ĐỀ BÀI của deck 1-gõ, tức mất đúng câu hỏi chứ không phải mất
    # phần trang trí. Thẻ chưa có nghĩa Việt thì vẫn điền bản mới như cũ.
    if (fields.get("Vietnamese") or "").strip():
        new_fields["Vietnamese"] = fields["Vietnamese"]

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


def redo_note(word, do_sync=True, chon_id=None):
    """Làm lại 1 thẻ theo TỪ (luồng /sua của bot). Tìm note theo từ (nhiều note
    trùng -> chọn note mới nhất) rồi gọi redo_note_id.

    `chon_id` đi thẳng xuống `redo_note_id` — dùng khi user vừa chọn mục cho một
    TỪ ĐỒNG TỰ; xem `cao_mot_tu`."""
    clean_word = strip_accents_perfectly(word)
    dups = find_duplicate_notes(clean_word)
    if not dups:
        return False, None, f"Không tìm thấy thẻ nào cho từ '{word}'."

    note_id = max(d["note_id"] for d in dups)
    success, result, error_msg = redo_note_id(note_id, do_sync=do_sync, chon_id=chon_id)
    if result is not None and not result.get("word"):
        result["word"] = word
    return success, result, error_msg
