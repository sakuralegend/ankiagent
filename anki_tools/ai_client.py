# ==============================================================================
# --- GIAO TIẾP VỚI AI (Gemini qua endpoint OpenAI-compatible) ---
# _CORE_SYSTEM_PROMPT là "NGUỒN CHÂN LÝ DUY NHẤT" cho phong cách viết câu ví dụ.
# Từ khi gỡ nút AI Refine khỏi thẻ Anki (chuyển sang /sua của bot Telegram),
# prompt CHỈ tồn tại ở file này — muốn đổi văn phong AI, sửa ở đây là đủ.
# ==============================================================================
import base64
import json
import re
import time
import unicodedata
import requests

from .config import CLAUDE_API_URL, CLAUDE_API_KEY, CLAUDE_MODEL, CLAUDE_FALLBACK_MODELS
from .lemma import reconcile_lemma
from .topics import TOPICS, normalize_topic, topics_prompt_block
from .utils import log_fail, log_warn

_FEWSHOT_EXAMPLES = [
    # (loại từ, target word, JSON mẫu) — mỗi entry chỉ giữ câu nào thể hiện RÕ biến đổi
    # ngữ pháp (khác dạng từ điển), để prompt ngắn mà vẫn dạy đủ highlight rule.
    (
        "adjective",
        "хороший",
        '{"vietnamese_meaning": "tốt, ngon, hay", "topic": "qualities", "simplified_examples": ['
        '{"ru": "У нас <hl>хорошая</hl> погода, пойдём гулять?", "en": "The weather\'s <hl>nice</hl>, wanna go for a walk?", "vi": "Trời <hl>đẹp</hl> quá, đi dạo không?"},'
        '{"ru": "Ты молодец, получилось <hl>лучше</hl>, чем в прошлый раз.", "en": "Nice job, that turned out <hl>better</hl> than last time.", "vi": "Giỏi lắm, lần này làm <hl>tốt hơn</hl> lần trước đó."}'
        ']}'
    ),
    (
        "verb",
        "говорить",
        '{"vietnamese_meaning": "nói, trò chuyện", "topic": "actions", "simplified_examples": ['
        '{"ru": "Она <hl>говорит</hl> по-английски свободно.", "en": "She <hl>speaks</hl> English fluently.", "vi": "Cô ấy <hl>nói</hl> tiếng Anh lưu loát lắm."},'
        '{"ru": "Прости, я не то <hl>сказал</hl>, не обижайся.", "en": "Sorry, I didn\'t mean what I <hl>said</hl>, don\'t be mad.", "vi": "Xin lỗi, tại tớ lỡ lời, đừng giận nha."}'
        ']}'
    ),
]


def _build_fewshot_block():
    """Ghép các few-shot example thành text để nhét vào system prompt."""
    lines = []
    for pos, word, json_example in _FEWSHOT_EXAMPLES:
        lines.append(f"# Example ({pos}: {word})")
        lines.append(json_example)
    return "\n".join(lines)


_CORE_SYSTEM_PROMPT = (
    "You are a native Russian speaker and friendly tutor. Write natural, casual, everyday Russian — "
    "like texting a friend, not a textbook. Avoid stiff, word-by-word translations.\n\n"
    "TASK: 1) Give a short, natural Vietnamese meaning of the target word. "
    "2) Write 3 short Russian example sentences, each in a DIFFERENT everyday situation "
    "(food, weather, work, friends, family, phone calls, etc — don't repeat contexts). "
    "3) Translate each sentence naturally (meaning-for-meaning, not word-for-word) into English and Vietnamese. "
    "4) Classify the target word into EXACTLY ONE topic slug from the TOPIC LIST below "
    "(based on the word's most common meaning; if nothing fits, use \"other\").\n\n"
    "TOPIC LIST:\n"
    f"{topics_prompt_block()}\n\n"
    "HIGHLIGHT RULE: wrap the target word AND any of its grammatical forms (conjugated, declined, plural, "
    "comparative, short form, etc.) with <hl>...</hl> in the ru, en, AND vi sentence — only the word itself, "
    "never the whole sentence. Every sentence MUST have a highlighted word in ALL THREE languages: if a fully "
    "idiomatic translation would drop the word entirely (e.g. \"быстрее\" -> \"Hurry up!\" has nothing to highlight), "
    "pick a more literal-but-still-natural phrasing instead (e.g. \"Come on, faster!\") so en and vi always keep a "
    "clear <hl> word too.\n\n"
    "Examples below show only 2 sentences each for brevity, but your actual output must always contain "
    "exactly 3 sentences in simplified_examples:\n\n"
    f"{_build_fewshot_block()}\n\n"
    "Return ONLY a valid JSON object, no markdown, no commentary, matching this schema:\n"
    '{"vietnamese_meaning": "...", "topic": "...", "simplified_examples": '
    '[{"ru": "...","en": "...","vi": "..."},{"ru": "...","en": "...","vi": "..."},{"ru": "...","en": "...","vi": "..."}]}'
)


def _parse_ai_response(raw_response):
    """Tách JSON từ raw response, xử lý markdown code block. Trả về dict hoặc None."""
    raw_content = raw_response.strip()
    if raw_content.startswith("```json"):
        raw_content = raw_content[7:]
    if raw_content.startswith("```"):
        raw_content = raw_content[3:]
    if raw_content.endswith("```"):
        raw_content = raw_content[:-3]
    try:
        parsed = json.loads(raw_content.strip())
        return parsed
    except json.JSONDecodeError:
        return None


def _validate_ai_result(parsed):
    """Lưới an toàn: kiểm tra dict AI trả về đủ schema thẻ.
    Trả về dict đã chuẩn hóa {"vietnamese_meaning", "simplified_examples"(=3, đủ ru/en/vi)}
    hoặc None nếu thiếu bất kỳ thứ gì (KHÔNG được dùng dữ liệu thiếu để ghi đè thẻ)."""
    if not isinstance(parsed, dict):
        return None
    vi_meaning = parsed.get("vietnamese_meaning")
    if not isinstance(vi_meaning, str) or not vi_meaning.strip():
        return None
    examples = parsed.get("simplified_examples")
    if not isinstance(examples, list) or len(examples) < 3:
        return None
    cleaned = []
    for ex in examples[:3]:
        if not isinstance(ex, dict):
            return None
        ru = (ex.get("ru") or "").strip()
        en = (ex.get("en") or "").strip()
        vi = (ex.get("vi") or ex.get("vietnamese") or "").strip()
        if not ru or not en or not vi:
            return None
        cleaned.append({"ru": ru, "en": en, "vi": vi})
    # topic là trường PHỤ: sai/thiếu chỉ bị ép về "other", KHÔNG làm hỏng cả kết quả
    # (luồng refine /sua không dùng topic nên cũng vô hại).
    return {
        "vietnamese_meaning": vi_meaning.strip(),
        "simplified_examples": cleaned,
        "topic": normalize_topic(parsed.get("topic")),
    }


def _model_chain():
    """Danh sách model theo thứ tự ưu tiên: model chính -> các model dự phòng."""
    chain = [CLAUDE_MODEL]
    for m in CLAUDE_FALLBACK_MODELS:
        if m not in chain:
            chain.append(m)
    return chain


def _call_model_once(model, system_prompt, user_prompt, use_reasoning=True, rpm_waits=2,
                     max_tokens=900, reasoning_effort="minimal", timeout=60):
    """Gọi 1 model đúng 1 lần. Trả về (content | None, nên_thử_model_khác: bool).

    user_prompt: str, hoặc list content parts kiểu OpenAI (để gửi kèm ảnh).

    reasoning_effort: mặc định "minimal" cho việc sinh thẻ (chỉ cần viết câu, nghĩ
    nhiều chỉ tổ ăn hết max_tokens). Riêng QUÉT ẢNH thì nâng lên vì đó là việc đọc
    tỉ mỉ cả trang — xem call_claude_scan_words().

    rpm_waits: số lần được phép CHỜ khi dính 429 loại "giới hạn mỗi phút" (RPM).
    RPM chỉ là tạm thời (sửa deck hàng loạt bắn request nhanh quá) — chờ rồi thử
    lại CHÍNH model đó tốt hơn nhiều so với nhảy sang model dự phòng vốn có quota
    ngày rất thấp. Chỉ 429 loại hết quota NGÀY (PerDay) mới chuyển model."""
    payload = {
        "model": model,
        "messages": [{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}],
        "temperature": 0.7,
        "max_tokens": max_tokens,
    }
    if use_reasoning:
        # Model "thinking" (vd gemini-3.5-flash) mặc định ngốn max_tokens vào suy nghĩ ẩn
        # -> reasoning_effort thấp để dồn token cho câu trả lời JSON.
        payload["reasoning_effort"] = reasoning_effort

    try:
        res = requests.post(CLAUDE_API_URL, headers={
            "Authorization": f"Bearer {CLAUDE_API_KEY}",
            "Content-Type": "application/json",
        }, json=payload, timeout=timeout)
    except Exception as e:
        log_fail(f"AI lỗi mạng: {e}")
        return None, False  # mạng đứt thì model khác cũng vô ích

    try:
        data = res.json()
    except ValueError:
        log_fail(f"AI ({model}) trả về không phải JSON (status {res.status_code}).")
        return None, True

    # Google đôi khi bọc lỗi trong list: [{"error": {...}}]
    if isinstance(data, list):
        data = data[0] if data and isinstance(data[0], dict) else {}

    if res.status_code == 429:
        err_text = json.dumps(data, ensure_ascii=False)
        if "PerDay" not in err_text and rpm_waits > 0:
            # 429 mỗi phút (hoặc không rõ loại): chờ theo retryDelay Google gợi ý
            m = re.search(r'retryDelay"?\s*:?\s*"?(\d+)', err_text)
            delay = min(int(m.group(1)) + 2, 65) if m else 30
            log_warn(f"Model '{model}' chạm giới hạn MỖI PHÚT (RPM) -> chờ {delay}s rồi thử lại...")
            time.sleep(delay)
            return _call_model_once(model, system_prompt, user_prompt, use_reasoning,
                                    rpm_waits - 1, max_tokens, reasoning_effort, timeout)
        log_warn(f"Model '{model}' hết hạn mức miễn phí trong NGÀY (429) -> thử model dự phòng...")
        return None, True

    if res.status_code == 400 and use_reasoning:
        # Model có thể không hỗ trợ reasoning_effort (hoặc không nhận đúng mức được
        # yêu cầu) -> thử lại chính model đó, bỏ hẳn field này
        return _call_model_once(model, system_prompt, user_prompt, use_reasoning=False,
                                max_tokens=max_tokens, timeout=timeout)

    if res.status_code != 200 or not data.get("choices"):
        err_msg = ""
        if isinstance(data.get("error"), dict):
            err_msg = data["error"].get("message", "")
        log_fail(f"AI ({model}) lỗi {res.status_code}: {err_msg[:200]}")
        return None, True

    content = (data["choices"][0].get("message") or {}).get("content") or ""
    content = content.strip()
    if not content:
        log_warn(f"AI ({model}) trả về nội dung rỗng.")
        return None, True
    return content, False


def _send_ai_request(system_prompt, user_prompt, max_tokens=900,
                     reasoning_effort="minimal", timeout=60):
    """Gửi request AI, tự động chuyển model dự phòng khi hết quota/lỗi.
    Trả về raw text response hoặc None."""
    for model in _model_chain():
        content, try_next = _call_model_once(
            model, system_prompt, user_prompt, max_tokens=max_tokens,
            reasoning_effort=reasoning_effort, timeout=timeout,
        )
        if content:
            return content
        if not try_next:
            return None
    log_fail("Tất cả model AI đều thất bại (hết quota hoặc lỗi).")
    return None


def call_claude_ai(word_clean, raw_examples, english_meanings):
    """Gửi raw examples cho AI, nhờ rewrite + dịch. Trả về dict hoặc None."""
    raw_text = ""
    for i, ex in enumerate(raw_examples):
        raw_text += f"[Example {i + 1}] RU: {ex.get('ru', '')} | EN: {ex.get('en', '')} --- "
    en_meanings_str = ", ".join(english_meanings) if english_meanings else "N/A"

    system_prompt = _CORE_SYSTEM_PROMPT

    user_prompt = (
        f"Target word: [{word_clean}]. "
        f"English meanings (reference only, don't translate literally): [{en_meanings_str}]. "
        f"Raw dictionary examples (use as inspiration, but REWRITE into natural, casual, everyday sentences — "
        f"don't keep their stiff textbook phrasing): {raw_text} "
        "Return ONLY the JSON."
    )

    raw_response = _send_ai_request(system_prompt, user_prompt)
    if not raw_response:
        return None

    parsed = _parse_ai_response(raw_response)
    if not parsed:
        log_fail("AI trả về JSON không hợp lệ, thử lại với chế độ tự sinh...")
        return None

    valid = _validate_ai_result(parsed)
    if not valid:
        log_fail("AI trả về thiếu dữ liệu (không đủ 3 ví dụ hoặc thiếu ngôn ngữ).")
        return None
    return valid


def call_claude_ai_freestyle(word_clean, english_meanings):
    """AI tự sinh ví dụ từ chính trí tuệ của nó (không có raw examples). Dùng khi raw_examples rỗng hoặc parse lỗi."""
    log_warn("🔄 Chuyển sang chế độ AI TỰ SINH ví dụ (freestyle) - AI dùng kiến thức riêng để tạo câu.")
    en_meanings_str = ", ".join(english_meanings) if english_meanings else "N/A"

    system_prompt = _CORE_SYSTEM_PROMPT

    user_prompt = (
        f"Target word: [{word_clean}]. "
        f"English meanings (reference only): [{en_meanings_str}]. "
        "There are no raw examples provided — invent 3 fresh, natural, everyday Russian sentences yourself "
        "using your own knowledge of the word. "
        "Return ONLY the JSON."
    )

    raw_response = _send_ai_request(system_prompt, user_prompt)
    if not raw_response:
        return None

    parsed = _parse_ai_response(raw_response)
    if not parsed:
        log_fail("AI freestyle cũng trả về JSON không hợp lệ.")
        return None

    valid = _validate_ai_result(parsed)
    if not valid:
        log_fail("AI freestyle trả về thiếu dữ liệu (không đủ 3 ví dụ hoặc thiếu ngôn ngữ).")
        return None
    return valid


def call_claude_lemma(word):
    """Từ không có trên OpenRussian (sai chính tả hoặc là dạng biến cách):
    nhờ AI đoán DẠNG TỪ ĐIỂN (lemma) để cào lại. Bot sẽ hỏi user xác nhận
    trước khi dùng — hàm này chỉ đoán, không tự quyết.
    Trả về {"lemma": str, "reason_vi": str, "alternatives": [str, ...]} hoặc None."""
    system_prompt = (
        "You are a Russian morphology expert. The user typed a Russian word that was NOT found "
        "in the dictionary. Two possible causes: (a) it is an INFLECTED form (conjugated verb, "
        "declined noun/adjective, plural, comparative, participle, short form...), or (b) it "
        "contains a TYPO.\n"
        "Find the most likely DICTIONARY FORM (lemma): nominative singular for nouns, "
        "infinitive for verbs, masculine nominative singular for adjectives.\n"
        "Return ONLY one valid JSON object, no markdown:\n"
        '{"lemma": "...", "reason_vi": "...", "alternatives": ["..."]}\n'
        "- lemma: the single most likely dictionary form (Russian, no stress marks)\n"
        "- reason_vi: ONE short Vietnamese sentence explaining the guess "
        "(e.g. 'дома là dạng số nhiều của дом' or 'có thể gõ nhầm từ хорошо')\n"
        "- alternatives: 0-2 OTHER plausible lemmas if ambiguous, else []"
    )
    user_prompt = f"Word as typed: [{word}]. Return ONLY the JSON."

    raw_response = _send_ai_request(system_prompt, user_prompt)
    if not raw_response:
        return None
    parsed = _parse_ai_response(raw_response)
    if not isinstance(parsed, dict):
        log_fail("AI đoán lemma trả về JSON không hợp lệ.")
        return None
    lemma = (parsed.get("lemma") or "").strip()
    if not lemma:
        return None
    alts = []
    for a in parsed.get("alternatives") or []:
        if isinstance(a, str) and a.strip() and a.strip() != lemma:
            alts.append(a.strip())
    return {
        "lemma": lemma,
        "reason_vi": (parsed.get("reason_vi") or "").strip(),
        "alternatives": alts[:2],
    }


def call_claude_topic(word, english_meanings):
    """Phân loại CHỦ ĐỀ cho 1 từ (không sinh ví dụ) — dùng cho script tag_topics.py
    khi gặp thẻ chưa có tag topic:: (vd thẻ tạo lúc AI hỏng nên thiếu topic).
    Trả về slug hợp lệ trong TOPICS, hoặc None nếu AI không trả lời được."""
    en_str = ", ".join(english_meanings) if english_meanings else "N/A"
    system_prompt = (
        "You classify a Russian vocabulary word into EXACTLY ONE topic slug from this list "
        "(based on the word's most common meaning; if nothing fits, use \"other\"):\n"
        f"{topics_prompt_block()}\n\n"
        'Return ONLY a valid JSON object, no markdown: {"topic": "..."}'
    )
    user_prompt = f"Word: [{word}]. English meanings: [{en_str}]. Return ONLY the JSON."

    raw_response = _send_ai_request(system_prompt, user_prompt)
    if not raw_response:
        return None
    parsed = _parse_ai_response(raw_response)
    if not isinstance(parsed, dict):
        return None
    slug = normalize_topic(parsed.get("topic"))
    return slug


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


def check_claude_ready():
    """Kiểm tra API key hợp lệ bằng endpoint liệt kê model.
    ⚠️ Cố tình KHÔNG gửi request sinh nội dung: gói free chỉ có vài chục
    lượt/ngày, ping kiểu cũ đốt 1 lượt mỗi lần bot khởi động lại."""
    try:
        base_url = CLAUDE_API_URL.split("/chat/completions")[0]
        res = requests.get(f"{base_url}/models", headers={
            "Authorization": f"Bearer {CLAUDE_API_KEY}",
        }, timeout=15)
        return res.status_code == 200
    except Exception:
        return False
