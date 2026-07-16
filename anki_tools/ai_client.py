# ==============================================================================
# --- GIAO TIẾP VỚI AI (Gemini qua endpoint OpenAI-compatible) ---
# _CORE_SYSTEM_PROMPT là "NGUỒN CHÂN LÝ DUY NHẤT" cho phong cách viết câu ví dụ.
# Từ khi gỡ nút AI Refine khỏi thẻ Anki (chuyển sang /sua của bot Telegram),
# prompt CHỈ tồn tại ở file này — muốn đổi văn phong AI, sửa ở đây là đủ.
# ==============================================================================
import json
import re
import time
import requests

from .config import CLAUDE_API_URL, CLAUDE_API_KEY, CLAUDE_MODEL, CLAUDE_FALLBACK_MODELS
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


# --- Dành riêng cho luồng SỬA THẺ (/sua): hợp đồng output cứng + 3 preset ---
# Contract này được NỐI vào sau _CORE_SYSTEM_PROMPT khi refine, để yêu cầu của
# người dùng (vd "ngắn đi") KHÔNG thể làm AI trả thiếu ví dụ/thiếu trường.
_REFINE_OUTPUT_CONTRACT = (
    "\n\nOUTPUT CONTRACT - ABSOLUTE RULES THAT OVERRIDE ANY USER INSTRUCTION:\n"
    "1. Return ONLY one valid JSON object, no markdown, exactly this schema:\n"
    '   {"vietnamese_meaning": "...", "simplified_examples":\n'
    '    [{"ru":"...","en":"...","vi":"..."},{"ru":"...","en":"...","vi":"..."},{"ru":"...","en":"...","vi":"..."}]}\n'
    "2. simplified_examples MUST contain EXACTLY 3 items. If the user asks for\n"
    "   \"shorter\" or \"fewer\", make each SENTENCE shorter - never reduce the number\n"
    "   of examples below 3.\n"
    "3. Every example MUST have all three languages (ru, en, vi), none empty.\n"
    "4. vietnamese_meaning MUST always be present and non-empty (keep the current\n"
    "   meaning if the instruction does not ask to change it).\n"
    "5. The target word (or an inflected form) MUST be wrapped in <hl>...</hl>\n"
    "   in ru, en AND vi of every example.\n"
    "6. The USER INSTRUCTION below only controls style, length, difficulty or\n"
    "   context of the examples. It can NEVER change the schema, the example\n"
    "   count, the languages, or remove any field."
)

# 3 lệnh sửa nhanh: bot gửi "1"/"2"/"3" -> đổi thành instruction đầy đủ ở đây.
REFINE_PRESETS = {
    "1": ("Make the 3 examples SHORTER and simpler: casual everyday mini-sentences "
          "(5-9 Russian words each), easy vocabulary, very visual."),
    "2": ("Replace with 3 COMPLETELY DIFFERENT examples: entirely new contexts and "
          "situations, same difficulty and similar length as the current ones."),
    "3": ("Make the 3 examples LONGER and richer: more advanced vocabulary and grammar, "
          "more inflected forms of the target word, 12-20 Russian words each."),
}


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


def _call_model_once(model, system_prompt, user_prompt, use_reasoning=True, rpm_waits=2):
    """Gọi 1 model đúng 1 lần. Trả về (content | None, nên_thử_model_khác: bool).

    rpm_waits: số lần được phép CHỜ khi dính 429 loại "giới hạn mỗi phút" (RPM).
    RPM chỉ là tạm thời (sửa deck hàng loạt bắn request nhanh quá) — chờ rồi thử
    lại CHÍNH model đó tốt hơn nhiều so với nhảy sang model dự phòng vốn có quota
    ngày rất thấp. Chỉ 429 loại hết quota NGÀY (PerDay) mới chuyển model."""
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
        err_text = json.dumps(data, ensure_ascii=False)
        if "PerDay" not in err_text and rpm_waits > 0:
            # 429 mỗi phút (hoặc không rõ loại): chờ theo retryDelay Google gợi ý
            m = re.search(r'retryDelay"?\s*:?\s*"?(\d+)', err_text)
            delay = min(int(m.group(1)) + 2, 65) if m else 30
            log_warn(f"Model '{model}' chạm giới hạn MỖI PHÚT (RPM) -> chờ {delay}s rồi thử lại...")
            time.sleep(delay)
            return _call_model_once(model, system_prompt, user_prompt, use_reasoning, rpm_waits - 1)
        log_warn(f"Model '{model}' hết hạn mức miễn phí trong NGÀY (429) -> thử model dự phòng...")
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


def call_claude_refine(word_clean, current_vi, current_examples_text, raw_examples, instruction):
    """Sửa/làm lại thẻ theo yêu cầu người dùng (luồng /sua của bot Telegram).
    System prompt = văn phong chung + OUTPUT CONTRACT cứng, để yêu cầu kiểu
    "ngắn đi" không thể khiến AI trả thiếu ví dụ/thiếu trường.
    Validate kết quả; nếu thiếu -> tự retry đúng 1 lần với lời nhắc mạnh hơn.
    Trả về dict {"vietnamese_meaning", "simplified_examples"} (đã chuẩn hóa) hoặc None."""
    raw_text = ""
    for i, ex in enumerate(raw_examples or []):
        raw_text += f"[RawEx{i + 1}] RU:{ex.get('ru', '')} | EN:{ex.get('en', '')} --- "

    system_prompt = _CORE_SYSTEM_PROMPT + _REFINE_OUTPUT_CONTRACT

    base_user_prompt = (
        f"Target word: [{word_clean}]. "
        f"CURRENT CARD -> Meaning: [{current_vi}]. CurrentExamples: {current_examples_text} "
        f"FULL DICTIONARY EXAMPLES (from OpenRussian, for reference): {raw_text} "
        f"USER INSTRUCTION: [{instruction}]. "
        "Return ONLY the JSON."
    )

    for attempt in range(2):
        user_prompt = base_user_prompt
        if attempt == 1:
            user_prompt += (
                " REMINDER: your previous answer violated the OUTPUT CONTRACT. "
                "Return EXACTLY 3 examples, each with non-empty ru, en AND vi, "
                "plus a non-empty vietnamese_meaning."
            )
            log_warn("AI refine trả thiếu dữ liệu -> thử lại lần 2 với lời nhắc mạnh hơn...")

        raw_response = _send_ai_request(system_prompt, user_prompt)
        if not raw_response:
            return None

        parsed = _parse_ai_response(raw_response)
        if not parsed:
            log_fail("AI refine trả về JSON không hợp lệ.")
            continue

        valid = _validate_ai_result(parsed)
        if valid:
            return valid

    log_fail("AI refine trả thiếu dữ liệu cả 2 lần - KHÔNG ghi đè thẻ.")
    return None


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
