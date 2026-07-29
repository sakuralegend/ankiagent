# ==============================================================================
# --- CÀO DỮ LIỆU TỪ OPENRUSSIAN ---
# ==============================================================================
import json
import urllib.parse
import requests
from bs4 import BeautifulSoup

from .utils import log_fail, convert_stress_to_combining_accent


def process_pure_next_data(word):
    """Cào dữ liệu từ vựng từ OpenRussian.
    Trả về dict với các khóa cố định (được push_to_anki() sử dụng):
      word, english_meanings, part_of_speech, pos_full, gender, aspect,
      reflexive, raw_dictionary_examples
    ⚠️ Nếu đổi tên bất kỳ khóa nào ở đây, phải sửa luôn anki_client.push_to_anki().
    """
    clean_word = word.strip()
    url = f"https://en.openrussian.org/ru/{urllib.parse.quote(clean_word, safe='')}"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        res = requests.get(url, headers=headers, timeout=15)
        if res.status_code != 200:
            log_fail(f"Server trả về status {res.status_code}.")
            return None

        soup = BeautifulSoup(res.text, "html.parser")
        script_tag = soup.find("script", id="__NEXT_DATA__")
        if not script_tag:
            log_fail("Không tìm thấy dữ liệu từ vựng (trang có thể đã đổi cấu trúc).")
            return None

        json_data = json.loads(script_tag.get_text(strip=True))
        pageProps = json_data.get("props", {}).get("pageProps", {})

        def find_word_object(data):
            if isinstance(data, dict):
                if 'type' in data and 'translations' in data:
                    return data
                for val in data.values():
                    result = find_word_object(val)
                    if result:
                        return result
            elif isinstance(data, list):
                for item in data:
                    result = find_word_object(item)
                    if result:
                        return result
            return None

        main_word_obj = find_word_object(pageProps)
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
            "raw_dictionary_examples": raw_examples
        }
    except Exception as e:
        log_fail(f"Lỗi cào dữ liệu: {e}")
        return None
