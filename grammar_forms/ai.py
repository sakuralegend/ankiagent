# ==============================================================================
# --- AI SINH NỘI DUNG CHO THẺ SỐ NHIỀU BẤT QUY TẮC ---
# Dùng LẠI hạ tầng gọi AI của anki_tools/ai_client.py (_send_ai_request đã lo sẵn
# việc đổi model dự phòng khi hết quota, chờ khi chạm giới hạn mỗi phút, parse
# JSON lẫn trong markdown) — nhưng PROMPT thì hoàn toàn riêng, nằm ở file này.
# Sửa văn phong ví dụ của thẻ biến cách chỉ cần sửa ở đây.
#
# Khác biệt cốt lõi so với thẻ từ vựng: ví dụ phải chứa ĐÚNG dạng SỐ NHIỀU CÁCH 1
# (nominative), không phải dạng biến cách khác. AI rất hay trả về "много друзей"
# (genitive) thay vì "мои друзья" — nên có bước HẬU KIỂM bắt làm lại.
# ==============================================================================
import re

from anki_tools.ai_client import _parse_ai_response, _send_ai_request
from anki_tools.utils import log_fail, log_warn, strip_accents_perfectly

_SYSTEM_PROMPT = (
    "You are a native Russian speaker and friendly tutor helping a learner memorise "
    "IRREGULAR PLURAL forms of Russian nouns.\n\n"
    "You are given a noun in the singular and its irregular plural form.\n\n"
    "TASK:\n"
    "1) Give a short, natural Vietnamese meaning of the noun (the word itself, not the plural).\n"
    "2) Write 3 short Russian example sentences in DIFFERENT everyday situations "
    "(family, work, travel, shopping, weather, phone calls...). Casual and natural — "
    "like texting a friend, not a textbook.\n"
    "3) Translate each sentence naturally into English and Vietnamese.\n\n"
    "CRITICAL RULE — every sentence MUST contain the EXACT plural form given to you, "
    "spelled letter-for-letter, as the SUBJECT or in the NOMINATIVE case.\n"
    "Do NOT use any other case of the plural. Examples of what is FORBIDDEN when the "
    "given plural is 'друзья':\n"
    "  BAD:  У меня много друзей.        (genitive plural — WRONG FORM)\n"
    "  BAD:  Я пишу письмо друзьям.      (dative plural — WRONG FORM)\n"
    "  GOOD: Мои <hl>друзья</hl> уже ждут внизу.\n"
    "  GOOD: <hl>Друзья</hl> приехали раньше, чем я думал.\n"
    "The learner is memorising this one specific form, so seeing any other ending "
    "defeats the whole purpose of the card.\n\n"
    "HIGHLIGHT RULE: wrap the plural word with <hl>...</hl> in the ru sentence, and wrap "
    "the corresponding word(s) with <hl>...</hl> in the en AND vi sentences too. "
    "Only the word itself, never the whole sentence. All three languages must have a "
    "highlighted word in every sentence.\n\n"
    "Return ONLY a valid JSON object, no markdown, no commentary:\n"
    '{"vietnamese_meaning": "...", "simplified_examples": ['
    '{"ru": "...","en": "...","vi": "..."},'
    '{"ru": "...","en": "...","vi": "..."},'
    '{"ru": "...","en": "...","vi": "..."}]}'
)


def _contains_form(sentence, form_clean):
    """Câu RU có chứa ĐÚNG dạng số nhiều (tính cả khi câu có dấu nhấn) không?
    So theo TỪ trọn vẹn, không phải chuỗi con: 'дома' không được khớp 'домашний'."""
    plain = strip_accents_perfectly(sentence.replace("<hl>", "").replace("</hl>", ""))
    return re.search(rf"(?<![а-яё]){re.escape(form_clean)}(?![а-яё])", plain) is not None


def _validate(parsed, plural_clean):
    """Kiểm tra AI trả đủ schema VÀ cả 3 câu đều dùng đúng dạng số nhiều.
    Trả về dict đã chuẩn hóa, hoặc (None, lý do) để quyết định có thử lại không."""
    if not isinstance(parsed, dict):
        return None, "không phải JSON object"

    vi = parsed.get("vietnamese_meaning")
    if not isinstance(vi, str) or not vi.strip():
        return None, "thiếu nghĩa tiếng Việt"

    examples = parsed.get("simplified_examples")
    if not isinstance(examples, list) or len(examples) < 3:
        return None, "không đủ 3 ví dụ"

    cleaned = []
    for ex in examples[:3]:
        if not isinstance(ex, dict):
            return None, "ví dụ sai định dạng"
        ru = (ex.get("ru") or "").strip()
        en = (ex.get("en") or "").strip()
        vi_ex = (ex.get("vi") or ex.get("vietnamese") or "").strip()
        if not ru or not en or not vi_ex:
            return None, "ví dụ thiếu ngôn ngữ"
        if not _contains_form(ru, plural_clean):
            return None, f"câu không dùng đúng dạng '{plural_clean}': {ru[:60]}"
        cleaned.append({"ru": ru, "en": en, "vi": vi_ex})

    return {"vietnamese_meaning": vi.strip(), "simplified_examples": cleaned}, ""


def generate_plural_content(word_clean, plural, plural_clean, english_meanings,
                            raw_examples=None, attempts=3):
    """Sinh nghĩa Việt + 3 ví dụ dùng đúng dạng số nhiều.

    Thử tối đa `attempts` lần: AI hay lỡ dùng genitive ('много друзей') nên lần
    thử sau được nhắc thẳng lỗi vừa mắc. Trả về dict hoặc None.
    """
    en_str = ", ".join(english_meanings) if english_meanings else "N/A"
    raw_text = ""
    for i, ex in enumerate((raw_examples or [])[:4]):
        raw_text += f"[{i + 1}] RU: {ex.get('ru', '')} | EN: {ex.get('en', '')} --- "

    base_prompt = (
        f"Noun (singular): [{word_clean}]. "
        f"IRREGULAR PLURAL you must use: [{plural_clean}] (written with stress: {plural}). "
        f"English meanings (reference only): [{en_str}]. "
    )
    if raw_text:
        base_prompt += (
            f"Dictionary examples for inspiration only — most use OTHER cases, do NOT copy "
            f"them as-is, rewrite so the noun appears as [{plural_clean}]: {raw_text} "
        )
    base_prompt += "Return ONLY the JSON."

    last_reason = ""
    for attempt in range(attempts):
        prompt = base_prompt
        if attempt:
            prompt = (
                f"{base_prompt}\n\nYour previous answer was REJECTED ({last_reason}). "
                f"Every single ru sentence must contain the exact word '{plural_clean}' "
                f"in the nominative plural. Try again."
            )
        raw = _send_ai_request(_SYSTEM_PROMPT, prompt)
        if not raw:
            return None

        result, last_reason = _validate(_parse_ai_response(raw), plural_clean)
        if result:
            return result
        log_warn(f"AI lần {attempt + 1} bị loại ({last_reason}) — bắt làm lại.")

    log_fail(f"AI không sinh được ví dụ đúng dạng '{plural_clean}' sau {attempts} lần.")
    return None
