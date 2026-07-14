# ==============================================================================
# --- GIAO TIẾP VỚI AI (Gemini qua endpoint OpenAI-compatible) ---
# _CORE_SYSTEM_PROMPT là "NGUỒN CHÂN LÝ DUY NHẤT" cho phong cách viết câu ví dụ.
# Từ khi gỡ nút AI Refine khỏi thẻ Anki (chuyển sang /sua của bot Telegram),
# prompt CHỈ tồn tại ở file này — muốn đổi văn phong AI, sửa ở đây là đủ.
# ==============================================================================
import json
import requests

from .config import CLAUDE_API_URL, CLAUDE_API_KEY, CLAUDE_MODEL, CLAUDE_FALLBACK_MODELS
from .utils import log_fail, log_warn

_FEWSHOT_EXAMPLES = [
    # (loại từ, target word, JSON mẫu) — mỗi entry chỉ giữ câu nào thể hiện RÕ biến đổi
    # ngữ pháp (khác dạng từ điển), để prompt ngắn mà vẫn dạy đủ highlight rule.
    (
        "adjective",
        "хороший",
        '{"vietnamese_meaning": "tốt, ngon, hay", "simplified_examples": ['
        '{"ru": "У нас <hl>хорошая</hl> погода, пойдём гулять?", "en": "The weather\'s <hl>nice</hl>, wanna go for a walk?", "vi": "Trời <hl>đẹp</hl> quá, đi dạo không?"},'
        '{"ru": "Ты молодец, получилось <hl>лучше</hl>, чем в прошлый раз.", "en": "Nice job, that turned out <hl>better</hl> than last time.", "vi": "Giỏi lắm, lần này làm <hl>tốt hơn</hl> lần trước đó."}'
        ']}'
    ),
    (
        "verb",
        "говорить",
        '{"vietnamese_meaning": "nói, trò chuyện", "simplified_examples": ['
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
    "3) Translate each sentence naturally (meaning-for-meaning, not word-for-word) into English and Vietnamese.\n\n"
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
    '{"vietnamese_meaning": "...", "simplified_examples": '
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


def _model_chain():
    """Danh sách model theo thứ tự ưu tiên: model chính -> các model dự phòng."""
    chain = [CLAUDE_MODEL]
    for m in CLAUDE_FALLBACK_MODELS:
        if m not in chain:
            chain.append(m)
    return chain


def _call_model_once(model, system_prompt, user_prompt, use_reasoning=True):
    """Gọi 1 model đúng 1 lần. Trả về (content | None, nên_thử_model_khác: bool)."""
    payload = {
        "model": model,
        "messages": [{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}],
        "temperature": 0.7,
        "max_tokens": 900,
    }
    if use_reasoning:
        # Model "thinking" (vd gemini-3.5-flash) mặc định ngốn max_tokens vào suy nghĩ ẩn
        # -> reasoning_effort minimal để dồn token cho câu trả lời JSON.
        payload["reasoning_effort"] = "minimal"

    try:
        res = requests.post(CLAUDE_API_URL, headers={
            "Authorization": f"Bearer {CLAUDE_API_KEY}",
            "Content-Type": "application/json",
        }, json=payload, timeout=60)
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
        log_warn(f"Model '{model}' hết hạn mức miễn phí (429) -> thử model dự phòng...")
        return None, True

    if res.status_code == 400 and use_reasoning:
        # Model có thể không hỗ trợ reasoning_effort -> thử lại chính model đó, bỏ field này
        return _call_model_once(model, system_prompt, user_prompt, use_reasoning=False)

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


def _send_ai_request(system_prompt, user_prompt):
    """Gửi request AI, tự động chuyển model dự phòng khi hết quota/lỗi.
    Trả về raw text response hoặc None."""
    for model in _model_chain():
        content, try_next = _call_model_once(model, system_prompt, user_prompt)
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

    vi_meaning = parsed.get("vietnamese_meaning", "")
    examples = parsed.get("simplified_examples", [])
    if not examples:
        log_fail("AI trả về danh sách simplified_examples rỗng.")
        return None
    return {"vietnamese_meaning": vi_meaning, "simplified_examples": examples}


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

    vi_meaning = parsed.get("vietnamese_meaning", "")
    examples = parsed.get("simplified_examples", [])
    if not examples:
        log_fail("AI freestyle trả về danh sách simplified_examples rỗng.")
        return None
    return {"vietnamese_meaning": vi_meaning, "simplified_examples": examples}


def call_claude_refine(word_clean, current_vi, current_examples_text, raw_examples, instruction):
    """Sửa/làm lại thẻ theo yêu cầu người dùng (luồng /sua của bot Telegram).
    Đây là bản Python của đúng prompt mà nút "AI Refine" trong thẻ đang dùng
    (back_template.html) — giữ 2 nơi cùng văn phong.
    Trả về dict {"vietnamese_meaning", "simplified_examples"} hoặc None."""
    raw_text = ""
    for i, ex in enumerate(raw_examples or []):
        raw_text += f"[RawEx{i + 1}] RU:{ex.get('ru', '')} | EN:{ex.get('en', '')} --- "

    user_prompt = (
        f"Target word: [{word_clean}]. "
        f"CURRENT CARD -> Meaning: [{current_vi}]. CurrentExamples: {current_examples_text} "
        f"FULL DICTIONARY EXAMPLES (from OpenRussian, for reference): {raw_text} "
        f"USER INSTRUCTION: [{instruction}]. "
        f"Wrap the target word [{word_clean}] and its inflected forms in <hl>...</hl> tags "
        "in ALL THREE languages: Russian (ru), English (en), AND Vietnamese (vi). "
        "Return ONLY the JSON."
    )

    raw_response = _send_ai_request(_CORE_SYSTEM_PROMPT, user_prompt)
    if not raw_response:
        return None

    parsed = _parse_ai_response(raw_response)
    if not parsed:
        log_fail("AI refine trả về JSON không hợp lệ.")
        return None

    vi_meaning = parsed.get("vietnamese_meaning", "")
    examples = parsed.get("simplified_examples", [])
    if not examples:
        log_fail("AI refine trả về danh sách simplified_examples rỗng.")
        return None
    return {"vietnamese_meaning": vi_meaning, "simplified_examples": examples}


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
