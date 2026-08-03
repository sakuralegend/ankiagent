# ==============================================================================
# --- QUÉT ẢNH TRANG SÁCH: Gemini ĐỌC chữ, pymorphy3 CHỐT dạng từ điển ---
# Tách từ ai_client.py (03/08/2026). Vẫn đi qua MỘT CỬA AI duy nhất (L1):
# mọi request đều gửi bằng ai_client._send_ai_request, file này không gọi mạng.
# ==============================================================================
import base64
import re
import unicodedata

from .ai_client import _parse_ai_response, _send_ai_request
from .lemma import reconcile_lemma
from .utils import log_fail

# Prompt quét ảnh — viết lại 21/07/2026 sau khi soi lỗi thật (bỏ sót từ; trả về
# "проверяем"/"дети" thay vì проверять/ребёнок). Ba thay đổi cốt lõi:
# (1) Chia rõ 2 việc ĐỌC rồi mới ĐƯA VỀ NGUYÊN THỂ, và bắt liệt kê cả tiêu đề,
#     số bài tập, chú thích, bảng biểu — chỗ mắt AI hay lướt qua.
# (2) Bắt trả về CẶP {seen, lemma} chứ không phải mỗi lemma: model buộc phải nghĩ
#     "từ này biến đổi từ đâu ra", và bot có dạng gốc để đối chiếu + hiện cho user.
# (3) Nêu đích danh các ca hay trượt (suppletive: дети→ребёнок, шёл→идти).
_SCAN_SYSTEM_PROMPT = (
    "You are a Russian OCR + morphology assistant. The user sends a PHOTO of a page "
    "from a Russian book or textbook.\n\n"
    "STEP 1 — READ EVERYTHING. Work through the page line by line, top to bottom. Read "
    "every Russian word you can see: body text, titles and headings, exercise numbers "
    "and their instructions, words inside tables, boxes, captions, footnotes and margins. "
    "Do not stop early, do not summarise, do not keep only the 'interesting' words — a "
    "word you skip is a word the learner never gets to study. If a word is split across "
    "two lines with a hyphen (ко-\\nторый), join it back into one word.\n\n"
    "STEP 2 — LEMMATIZE. For each word give its DICTIONARY FORM:\n"
    "- noun -> nominative singular: детей -> ребёнок, людьми -> человек, времена -> время\n"
    "- verb -> infinitive: проверяем -> проверять, шёл -> идти, возьми -> взять, ем -> есть\n"
    "- adjective -> masculine nominative singular: хорошая -> хороший, лучше -> хороший, "
    "умнее -> умный\n"
    "- pronoun -> nominative: нас -> мы, его -> он\n"
    "NEVER output a conjugated, declined, plural or comparative form as the lemma. Be "
    "especially careful with words whose dictionary form looks nothing like the form on "
    "the page (дети -> ребёнок, люди -> человек, шла -> идти, лучше -> хороший).\n"
    "Use the surrounding sentence to choose the right lemma when a form is ambiguous "
    "(стали -> сталь in 'из стали', but стали -> стать in 'они стали').\n\n"
    "STEP 3 — CLEAN UP. Deduplicate by lemma, keeping the first form you saw. EXCLUDE: "
    "proper names of people and places (Анна, Иван, Москва), single letters, "
    "abbreviations, numbers, and anything that is not a real Russian word. KEEP "
    "everything else, including prepositions, pronouns and conjunctions.\n\n"
    "Return ONLY a valid JSON object, no markdown, no commentary:\n"
    '{"words": [{"seen": "детей", "lemma": "ребёнок"}, '
    '{"seen": "проверяем", "lemma": "проверять"}, '
    '{"seen": "хорошая", "lemma": "хороший"}]}\n'
    "- seen: the word exactly as printed on the page (lowercase, no stress marks)\n"
    "- lemma: its dictionary form (lowercase, no stress marks, keep ё where it belongs)\n"
    "- Cyrillic only; order = first appearance on the page"
)

_CYRILLIC_WORD_RE = re.compile(r"[а-яё]+(-[а-яё]+)*")


def image_mime_type(image_bytes):
    """Đoán định dạng ảnh từ mấy byte đầu (magic bytes), trả về mime hoặc None nếu
    Gemini không nhận dạng đó.
    Cần từ 21/07/2026, khi bot bắt đầu nhận ảnh gửi dạng FILE: ảnh nén của Telegram
    luôn là JPEG nên trước đây khai cứng "image/jpeg" cũng không sao, còn file thì
    có thể là PNG (ảnh chụp màn hình) hoặc HEIC (iPhone) — khai sai định dạng thì
    AI trả lỗi khó hiểu thay vì đọc ảnh."""
    if image_bytes[:3] == b"\xff\xd8\xff":
        return "image/jpeg"
    if image_bytes[:8] == b"\x89PNG\r\n\x1a\n":
        return "image/png"
    if image_bytes[:4] == b"RIFF" and image_bytes[8:12] == b"WEBP":
        return "image/webp"
    if image_bytes[4:8] == b"ftyp" and image_bytes[8:12] in (b"heic", b"heix", b"mif1", b"heim"):
        return None  # HEIC của iPhone: Gemini không đọc được
    return None


def _clean_scan_word(value):
    """Chuẩn hóa 1 từ AI trả về; None nếu không phải từ Cyrillic thuần."""
    if not isinstance(value, str):
        return None
    # ё viết dạng tổ hợp (е + dấu) -> 1 ký tự, nếu không sẽ lệch khi so chuỗi
    word = unicodedata.normalize("NFC", value.strip().lower()).replace("́", "")
    # cho phép dấu gạch nối kiểu "кто-то"
    return word if _CYRILLIC_WORD_RE.fullmatch(word) else None


def call_claude_scan_words(image_bytes):
    """Quét ẢNH trang sách: Gemini ĐỌC chữ, pymorphy3 CHỐT dạng từ điển.

    Trả về list[dict] {"lemma", "seen", "fixed"} theo thứ tự xuất hiện, đã dedupe
    theo lemma; hoặc None nếu AI không đọc được gì.
      lemma : dạng từ điển cuối cùng (thứ dùng để cào OpenRussian + tạo thẻ)
      seen  : dạng chữ đúng như in trên trang sách (để user đối chiếu khi duyệt)
      fixed : True nếu pymorphy3 đã sửa lại đáp án của AI (bot hiện dấu 🔧)
    ⚠️ Hàm CHỈ quét thô — việc lọc từ đã có thẻ và quyết định thêm là của bot/user."""
    mime = image_mime_type(image_bytes)
    if not mime:
        log_fail("Ảnh không phải JPEG/PNG/WEBP nên AI không đọc được.")
        return None
    b64 = base64.b64encode(image_bytes).decode("ascii")
    user_content = [
        {"type": "text", "text": "Extract and lemmatize all Russian words from this photo. Return ONLY the JSON."},
        {"type": "image_url", "image_url": {"url": f"data:{mime};base64,{b64}"}},
    ]
    # Khác hẳn lượt sinh thẻ: đây là việc ĐỌC TỈ MỈ cả trang nên cho model nghĩ
    # kỹ ("low" thay vì "minimal"), nới max_tokens (1 trang có thể ra hàng trăm
    # cặp từ) và nới trần chờ HTTP cho tương xứng — hết 60s giữa chừng thì công
    # đọc cả trang đổ sông đổ biển mà không có gì để thử lại.
    raw_response = _send_ai_request(_SCAN_SYSTEM_PROMPT, user_content,
                                    max_tokens=6000, reasoning_effort="low", timeout=180)
    if not raw_response:
        return None
    parsed = _parse_ai_response(raw_response)
    if not isinstance(parsed, dict) or not isinstance(parsed.get("words"), list):
        log_fail("AI quét ảnh trả về JSON không hợp lệ.")
        return None

    seen_lemmas, words = set(), []
    for item in parsed["words"]:
        # Nhận cả kiểu cũ (chuỗi trần) phòng khi model lười theo schema
        if isinstance(item, str):
            seen_form, ai_lemma = _clean_scan_word(item), _clean_scan_word(item)
        elif isinstance(item, dict):
            seen_form = _clean_scan_word(item.get("seen"))
            ai_lemma = _clean_scan_word(item.get("lemma"))
        else:
            continue
        if not (seen_form or ai_lemma):
            continue
        seen_form = seen_form or ai_lemma

        # TRỌNG TÀI: từ điển hình thái chốt lại, nhưng nhường AI khi AI có lý
        lemma, fixed = reconcile_lemma(seen_form, ai_lemma or seen_form)
        if not lemma or lemma in seen_lemmas:
            continue
        seen_lemmas.add(lemma)
        words.append({"lemma": lemma, "seen": seen_form, "fixed": fixed})
    return words or None
