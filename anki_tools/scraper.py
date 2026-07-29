# ==============================================================================
# --- CÀO DỮ LIỆU TỪ OPENRUSSIAN ---
# File này lo phần BÓC FIELD CỦA THẺ (nghĩa, từ loại, giống, ví dụ) từ mục từ.
# Phần gọi mạng + chọn mục từ nằm ở `grammar.fetch_word_object()` — nơi duy nhất
# chạm tới OpenRussian, để hai luồng (tạo thẻ / cào hàng loạt) không bao giờ
# chọn hai mục khác nhau cho cùng một từ.
# ==============================================================================
from . import grammar
from .utils import log_fail, convert_stress_to_combining_accent


def process_pure_next_data(word):
    """Cào dữ liệu từ vựng từ OpenRussian.
    Trả về dict với các khóa cố định (được push_to_anki() sử dụng):
      word, english_meanings, part_of_speech, pos_full, gender, aspect,
      reflexive, raw_dictionary_examples
    ⚠️ Nếu đổi tên bất kỳ khóa nào ở đây, phải sửa luôn anki_client.push_to_anki().
    """
    clean_word = word.strip()
    try:
        # Gọi mạng + chọn mục từ nằm ở grammar.fetch_word_object() — NƠI DUY NHẤT.
        # File này trước đây tự GET và tự có luật chọn mục riêng; hai luật thì với
        # từ ĐỒNG TỰ (`мочь` động từ / danh từ) có thể chọn hai mục khác nhau,
        # thành ra một thẻ mà nghĩa lấy ở mục này, bảng chia lấy ở mục kia.
        main_word_obj = grammar.fetch_word_object(clean_word, timeout=15)
        if not main_word_obj:
            log_fail(f"Từ '{clean_word}' không tồn tại trên OpenRussian.")
            return None

        pos_full = main_word_obj.get("type", "unknown")
        pos_short_map = {"noun": "n", "adjective": "adj", "verb": "v", "adverb": "adv", "pronoun": "pron", "conjunction": "conj"}
        pos_short = pos_short_map.get(pos_full, pos_full[:3] if pos_full else "unk")

        gender_code = main_word_obj.get("gender")
        if not gender_code and isinstance(main_word_obj.get("noun"), dict):
            gender_code = main_word_obj["noun"].get("gender")
        gender_map = {"m": "Masculine", "f": "Feminine", "n": "Neuter", "pl": "Plural"}
        gender = gender_map.get(gender_code, "None")

        # Thể động từ (вид) — nguồn cho badge HOÀN THÀNH / CHƯA HOÀN THÀNH.
        # Chỉ có ở mục động từ; danh từ/tính từ trả về "" và badge biến mất.
        verb_obj = main_word_obj.get("verb")
        aspect = verb_obj.get("aspect") or "" if isinstance(verb_obj, dict) else ""
        reflexive = bool(verb_obj.get("isReflexive")) if isinstance(verb_obj, dict) else False

        # Toàn bộ dữ liệu ngữ pháp (bảng chia, họ từ...) -> field GrammarJSON.
        # Dùng ĐÚNG `main_word_obj` mà các field khác của thẻ vừa lấy ra, nên
        # KHÔNG tốn thêm một lượt gọi mạng nào và nội dung trong một thẻ luôn
        # nhất quán với nhau (không có chuyện nghĩa lấy ở mục này, bảng chia lấy
        # ở mục đồng tự khác).
        try:
            # `bo_sung` vá nốt chỗ OpenRussian thiếu (số từ chỉ có dạng gốc ->
            # hỏi Wiktionary). Hỏng ở bước này KHÔNG được làm hỏng cả việc tạo
            # thẻ: thà thẻ thiếu bảng còn hơn không có thẻ.
            grammar_rec = grammar.bo_sung(grammar.normalize(main_word_obj), clean_word)
        except Exception as e:
            log_fail(f"khong dung duoc GrammarJSON cho '{clean_word}': {e}")
            grammar_rec = {}

        meanings = []
        trans_data = main_word_obj.get("translations")
        if isinstance(trans_data, dict) and "en" in trans_data:
            meanings = trans_data["en"] if isinstance(trans_data["en"], list) else [str(trans_data["en"])]
        elif isinstance(trans_data, list):
            for trans in trans_data:
                if isinstance(trans, dict) and "tls" in trans:
                    meanings.extend(trans["tls"])
        if not meanings:
            meanings = ["N/A"]

        raw_examples = []
        for s in main_word_obj.get("sentences", []):
            if isinstance(s, dict):
                raw_examples.append({"ru": convert_stress_to_combining_accent(s.get("ru", "")), "en": s.get("tl", "")})

        return {
            "word": convert_stress_to_combining_accent(main_word_obj.get("accented", word)),
            "english_meanings": meanings,
            "part_of_speech": pos_short,
            "pos_full": pos_full,
            "gender": gender,
            "aspect": aspect,
            "reflexive": reflexive,
            "grammar": grammar_rec,
            "raw_dictionary_examples": raw_examples
        }
    except Exception as e:
        log_fail(f"Lỗi cào dữ liệu: {e}")
        return None
