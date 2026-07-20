# ==============================================================================
# --- PIPELINE THẺ SỐ NHIỀU BẤT QUY TẮC ---
# Xử lý trọn vẹn 1 từ: cào -> AI -> audio -> đẩy Anki. Không dùng input()/print
# tương tác nên gọi được từ cả bot Telegram lẫn script chạy loạt.
#
# Song song với anki_tools/pipeline.py nhưng ĐỘC LẬP hoàn toàn — sửa ở đây không
# đụng gì đến luồng thêm thẻ từ vựng.
# ==============================================================================
import csv
import os

from anki_tools.anki_client import trigger_sync
from anki_tools.utils import strip_accents_perfectly

from . import cards
from .ai import generate_plural_content
from .config import PLURAL_DECK
from .irregular_plurals import OUT_TSV
from .scraper import fetch_noun

# Tag gắn cho mọi thẻ của mảng này — để lọc/tìm trong Anki không lẫn thẻ từ vựng
PLURAL_TAG = "grammar::plural-irregular"


def load_word_list(path=OUT_TSV):
    """Đọc danh sách từ bất quy tắc đã dựng sẵn (data/irregular_plurals.tsv).
    Trả về list dict, hoặc [] nếu chưa chạy bước dựng danh sách."""
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def _kind_of(word_clean, word_list=None):
    """Tra kiểu bất quy tắc của từ trong danh sách (để in nhãn lên thẻ)."""
    for row in (word_list if word_list is not None else load_word_list()):
        if row.get("bare") == word_clean:
            return row.get("kind", "")
    return ""


def process_word(word, deck=PLURAL_DECK, do_sync=False, word_list=None):
    """Tạo 1 thẻ số nhiều bất quy tắc.

    Trả về (success, info, error_msg):
      success=True  -> info có word/plural/vi/examples/audio để hiện tóm tắt
      success=False -> error_msg mô tả lỗi ngắn gọn cho bot/CLI in ra
    """
    clean = strip_accents_perfectly(word)

    existing = cards.find_existing(clean)
    if existing:
        return False, {"note_ids": existing}, (
            f"Từ '{word}' đã có thẻ số nhiều rồi (dùng lệnh vá/làm lại nếu muốn cập nhật)."
        )

    data = fetch_noun(clean)
    if not data:
        return False, None, (
            f"Không cào được '{word}' trên OpenRussian — sai chính tả, không phải danh từ, "
            "hoặc danh từ này không có dạng số nhiều."
        )

    plural_clean = strip_accents_perfectly(data["plural"])
    if plural_clean == clean:
        return False, None, (
            f"'{word}' có số nhiều trùng số ít ({data['plural']}) — không cần thẻ loại này."
        )

    ai_result = generate_plural_content(
        clean, data["plural"], plural_clean, data["english"], data["raw_examples"]
    )
    if not ai_result:
        return False, None, (
            f"AI không viết được ví dụ dùng đúng dạng '{plural_clean}' (đã thử 3 lần). "
            "Thẻ KHÔNG được tạo — thử lại sau."
        )

    fields = cards.build_fields(data, ai_result, kind=_kind_of(clean, word_list))

    # Audio: số ít và số nhiều tải riêng. OpenRussian đọc được cả hai; hụt thì
    # rơi về Google TTS (fetch_audio_bytes lo sẵn).
    fields["Audio"], audio_src = cards.store_audio(data["word"], "ru_audio")
    fields["PluralAudio"], plural_audio_src = cards.store_audio(data["plural"], "ru_plural")

    note_id, err = cards.add_note(fields, deck=deck, tags=[PLURAL_TAG])
    if not note_id:
        return False, None, f"AnkiConnect từ chối thêm thẻ: {err or 'không rõ nguyên nhân'}"

    info = {
        "note_id": note_id,
        "word": data["word"],
        "plural": data["plural"],
        "vi": ai_result["vietnamese_meaning"],
        "en": data["english"],
        "examples": ai_result["simplified_examples"],
        "kind": fields["KindLabel"],
        "deck": deck,
        "audio_source": audio_src,
        "plural_audio_source": plural_audio_src,
        "missing_audio": not fields["Audio"] or not fields["PluralAudio"],
    }
    if do_sync:
        info["synced"] = trigger_sync()
    return True, info, None


def redo_word(word, do_sync=True, word_list=None):
    """LÀM LẠI thẻ số nhiều theo TỪ (luồng 🔄 của mục ⭐ đặc biệt).

    Tìm note theo từ gốc rồi gọi redo_note. Nhiều note trùng -> lấy note mới nhất.
    Cố ý tách khỏi /sua của thẻ từ vựng: một từ (vd дом) có thể có CẢ hai loại
    thẻ, gộp chung thì không biết user muốn làm lại thẻ nào.
    """
    clean = strip_accents_perfectly(word)
    note_ids = cards.find_existing(clean)
    if not note_ids:
        return False, None, (
            f"Không tìm thấy thẻ số nhiều nào cho '{word}' trong {PLURAL_DECK}.\n"
            "(Thẻ TỪ VỰNG thì dùng /sua như thường.)"
        )
    success, result, error = redo_note(max(note_ids), do_sync=do_sync, word_list=word_list)
    if success and not result.get("word"):
        result["word"] = word
    return success, result, error


def redo_note(note_id, do_sync=False, word_list=None):
    """LÀM LẠI 1 thẻ đã có: cào lại + AI sinh lại ví dụ + vá audio còn thiếu,
    GHI ĐÈ lên đúng note đó (giữ note_id -> tiến trình học không đổi).

    Dùng cho việc vá 26 thẻ cũ (thiếu ví dụ, thiếu PluralAudio).
    """
    info = cards.get_note(note_id)
    if info is None:
        return False, None, "Không đọc được nội dung thẻ từ Anki."

    old = info["fields"]
    clean = old.get("WordClean") or strip_accents_perfectly(old.get("Word", ""))
    if not clean:
        return False, None, "Thẻ không có từ gốc (WordClean rỗng) để làm lại."

    data = fetch_noun(clean)
    if not data:
        return False, {"word": clean}, (
            f"Không cào lại được '{clean}' trên OpenRussian. Thẻ giữ nguyên, không đổi gì."
        )

    plural_clean = strip_accents_perfectly(data["plural"])
    ai_result = generate_plural_content(
        clean, data["plural"], plural_clean, data["english"], data["raw_examples"]
    )
    if not ai_result:
        return False, {"word": clean}, (
            f"AI không viết được ví dụ đúng dạng '{plural_clean}'. Thẻ giữ nguyên."
        )

    fields = cards.build_fields(data, ai_result, kind=_kind_of(clean, word_list))

    # Audio: chỉ tải lại ô nào ĐANG THIẾU, để không tốn quota TTS vô ích
    # (26 thẻ cũ có Audio rồi nhưng PluralAudio rỗng hết).
    for field, text, prefix in (("Audio", data["word"], "ru_audio"),
                                ("PluralAudio", data["plural"], "ru_plural")):
        if "[sound:" in (old.get(field) or ""):
            fields[field] = old[field]
        else:
            fields[field], _ = cards.store_audio(text, prefix)

    if not cards.update_note(note_id, fields):
        return False, {"word": clean}, "Ghi thẻ mới vào Anki thất bại (thẻ giữ nguyên)."

    result = {
        "note_id": note_id,
        "word": data["word"],
        "plural": data["plural"],
        "vi": ai_result["vietnamese_meaning"],
        "examples": ai_result["simplified_examples"],
        "kind": fields["KindLabel"],
        "missing_audio": not fields["Audio"] or not fields["PluralAudio"],
    }
    if do_sync:
        result["synced"] = trigger_sync()
    return True, result, None
