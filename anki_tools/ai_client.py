# ==============================================================================
# --- GIAO TIẾP VỚI AI (Gemini qua endpoint OpenAI-compatible) ---
# CỬA DUY NHẤT gọi AI (L1). Lời dặn đặt CÂU VÍ DỤ không còn ở đây: nó nằm ở
# `vi_du.py` cùng bộ chọn dạng + cổng kiểm, vì ba thứ đó phải sửa cùng nhau (QD-47).
# ==============================================================================
import json
import re
import time
import requests

from .config import CLAUDE_API_URL, CLAUDE_API_KEY, CLAUDE_MODEL, CLAUDE_FALLBACK_MODELS
from .topics import normalize_topic, topics_prompt_block, normalize_pos, pos_prompt_block
from .utils import log_fail, log_warn

# ==============================================================================
# --- KHUÔN JSON BẮT BUỘC (đo 12/08/2026) ---
# Gửi kèm `response_format` thì Google KHÔNG cho model đẻ ra chữ lệch khuôn nữa —
# nó ép ngay lúc sinh chữ, chứ không phải nhắc suông trong prompt rồi cầu may.
#
# VÌ SAO PHẢI LÀM: prompt đã dặn "Return ONLY a valid JSON object" mà model vẫn
# sai, hai kiểu bắt được thật trên VPS 12/08:
#   1. thừa dấu phẩy trước `}` / `]`  (`красивый`)
#   2. QUÊN DẤU NHÁY MỞ ở câu tiếng Nga (`думать`: `"ru": Я сижу и ...`) — kiểu
#      này vá tay là đoán mò, vì không biết câu bắt đầu từ đâu.
# Cả hai đều bị `json.loads` từ chối ⇒ code tưởng "AI hỏng" ⇒ gọi lại freestyle
# 1–2 lượt nữa. Đo trước khi vá: 4/16 từ phải gọi AI nhiều lượt. Sau khi ép
# khuôn: 0/16, và mỗi lượt chỉ chậm thêm ~0,1s.
#
# Trần 3 ví dụ đặt luôn trong khuôn: ép sẵn thì khỏi phải quay lại hỏi.
# ==============================================================================
# Khuôn thẻ NGỮ PHÁP (`grammar_forms/ai.py`): nghĩa Việt + đúng 3 ví dụ. Không hỏi
# chủ đề/từ loại — model thẻ ngữ pháp không có ô đó, ép hỏi là ép AI bịa field
# không ai đọc. (Thẻ từ vựng dùng khuôn riêng ở `vi_du.py`, QD-47.)
_KHUON_THE_KHONG_TOPIC = {
    "type": "object",
    "properties": {
        "vietnamese_meaning": {"type": "string"},
        "simplified_examples": {
            "type": "array", "minItems": 3, "maxItems": 3,
            "items": {
                "type": "object",
                "properties": {"ru": {"type": "string"}, "en": {"type": "string"},
                               "vi": {"type": "string"}},
                "required": ["ru", "en", "vi"],
            },
        },
    },
    "required": ["vietnamese_meaning", "simplified_examples"],
}

_KHUON_LEMMA = {
    "type": "object",
    "properties": {
        "lemma": {"type": "string"},
        "reason_vi": {"type": "string"},
        "alternatives": {"type": "array", "maxItems": 2, "items": {"type": "string"}},
    },
    "required": ["lemma", "reason_vi", "alternatives"],
}

_KHUON_POS = {
    "type": "object",
    "properties": {
        "ket_qua": {
            "type": "array",
            "items": {
                "type": "object",
                # null hợp lệ, y như `topic`: "chưa xếp được" là câu trả lời THẬT,
                # không phải lỗi. Ép buộc string là ép AI bịa (QD-38, QD-41).
                "properties": {"tu": {"type": "string"},
                               "pos": {"type": ["string", "null"]}},
                "required": ["tu", "pos"],
            },
        }
    },
    "required": ["ket_qua"],
}

_KHUON_TOPIC = {
    "type": "object",
    "properties": {
        "ket_qua": {
            "type": "array",
            "items": {
                "type": "object",
                # topic cho phép null: "chưa xếp được" là câu trả lời HỢP LỆ, không
                # phải lỗi. Bắt buộc phải là string là ép AI bịa (QD-38).
                "properties": {"tu": {"type": "string"},
                               "topic": {"type": ["string", "null"]}},
                "required": ["tu", "topic"],
            },
        }
    },
    "required": ["ket_qua"],
}


def _response_format(khuon):
    """Bọc khuôn thành field `response_format` kiểu OpenAI. None -> không ép."""
    if not khuon:
        return None
    return {"type": "json_schema",
            "json_schema": {"name": "khuon", "schema": khuon, "strict": True}}


def _parse_ai_response(raw_response):
    """Tách JSON từ raw response, xử lý markdown code block. Trả về dict hoặc None.

    THA THỨ DẤU PHẨY THỪA (đo 12/08/2026). Gemini thỉnh thoảng trả JSON kiểu
    JavaScript — thừa một dấu phẩy trước `}` hoặc `]`:
        {"vi": "...",
        }
    `json.loads` từ chối thẳng, và trước bản vá này nó bị hiểu nhầm thành "AI
    hỏng" ⇒ `build_examples_html` gọi lại freestyle 1–2 lượt nữa. Một từ tốn 3–4
    lượt AI thay vì 1: log VPS 12/08 có ca 07:53:18 → 07:53:44 = 26 GIÂY cho một
    từ, trong khi một lượt AI chỉ 1,8s. Tỉ lệ đo được: 1/12 từ dính.

    Vá bằng cách xoá ĐÚNG dấu phẩy mà trình đọc vấp phải, không phải regex quét
    cả chuỗi: `json.loads` cho biết vị trí lỗi, ta lùi lại tìm dấu phẩy ngay
    trước đó và chỉ xoá khi giữa hai chỗ toàn khoảng trắng. Nhờ vậy dấu phẩy nằm
    TRONG câu tiếng Việt/tiếng Nga không bao giờ bị đụng — một regex quét cả
    chuỗi thì có thể nuốt nhầm dấu phẩy trong chính câu, kiểu "chào, ]".
    """
    raw_content = raw_response.strip()
    if raw_content.startswith("```json"):
        raw_content = raw_content[7:]
    if raw_content.startswith("```"):
        raw_content = raw_content[3:]
    if raw_content.endswith("```"):
        raw_content = raw_content[:-3]
    raw_content = raw_content.strip()

    # Tối đa 8 vòng: đủ cho JSON 3 ví dụ (mỗi ví dụ 1 dấu + 2 dấu bao ngoài),
    # có trần để một câu trả lời rác không quay vòng mãi.
    for _ in range(8):
        try:
            return json.loads(raw_content)
        except json.JSONDecodeError as e:
            # e.pos có thể trỏ VÀO chính dấu phẩy ("Illegal trailing comma")
            # hoặc trỏ vào `}`/`]` đứng sau nó -> tìm cả tại chỗ lẫn lùi về trước.
            vi_tri_phay = raw_content.rfind(",", 0, e.pos + 1)
            if vi_tri_phay == -1 or raw_content[vi_tri_phay + 1:e.pos].strip():
                return None  # không phải lỗi phẩy thừa -> chịu, để caller lo
            raw_content = raw_content[:vi_tri_phay] + raw_content[vi_tri_phay + 1:]
    return None


def _model_chain():
    """Danh sách model theo thứ tự ưu tiên: model chính -> các model dự phòng."""
    chain = [CLAUDE_MODEL]
    for m in CLAUDE_FALLBACK_MODELS:
        if m not in chain:
            chain.append(m)
    return chain


def _call_model_once(model, system_prompt, user_prompt, use_reasoning=True, rpm_waits=2,
                     max_tokens=900, reasoning_effort="minimal", timeout=60, khuon=None):
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
    rf = _response_format(khuon)
    if rf:
        payload["response_format"] = rf
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

    if res.status_code == 400:
        # XUỐNG BẬC TỪNG NẤC, bỏ thứ ÍT QUAN TRỌNG TRƯỚC — để một model kén field
        # vẫn dùng được, mà không vứt luôn thứ đang giữ cho JSON khỏi hỏng.
        if use_reasoning:
            # Model có thể không hỗ trợ reasoning_effort (hoặc không nhận đúng mức
            # được yêu cầu) -> thử lại chính model đó, bỏ field này. GIỮ khuôn.
            return _call_model_once(model, system_prompt, user_prompt, use_reasoning=False,
                                    max_tokens=max_tokens, timeout=timeout, khuon=khuon)
        if khuon:
            # Nấc cuối: model không nhận `response_format`. Bỏ khuôn thì chạy tiếp
            # được, nhưng MẤT bảo đảm JSON đúng dạng -> nói ra, đừng im lặng: im
            # lặng đúng là thứ đã làm bot chậm gấp 2-3 lần mà không ai biết vì sao.
            log_warn(f"Model '{model}' không nhận khuôn JSON bắt buộc -> chạy KHÔNG khuôn "
                     f"(có thể lại gặp JSON hỏng — xem khối `_KHUON_*`).")
            return _call_model_once(model, system_prompt, user_prompt, use_reasoning=False,
                                    max_tokens=max_tokens, timeout=timeout, khuon=None)

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
                     reasoning_effort="minimal", timeout=60, khuon=None):
    """Gửi request AI, tự động chuyển model dự phòng khi hết quota/lỗi.
    Trả về raw text response hoặc None.

    khuon: khuôn JSON bắt buộc — MỌI lời gọi sinh dữ liệu có cấu trúc đều phải
    truyền, xem khối `_KHUON_*` để biết vì sao."""
    for model in _model_chain():
        content, try_next = _call_model_once(
            model, system_prompt, user_prompt, max_tokens=max_tokens,
            reasoning_effort=reasoning_effort, timeout=timeout, khuon=khuon,
        )
        if content:
            return content
        if not try_next:
            return None
    log_fail("Tất cả model AI đều thất bại (hết quota hoặc lỗi).")
    return None


def call_claude_vi_du(system_prompt, user_prompt, khuon):
    """Một lượt đặt câu ví dụ. Lời dặn + khuôn do `vi_du.py` dựng (QD-47) — hàm này
    chỉ là CỬA: gửi, bóc JSON, trả dict hoặc None. Kiểm câu đúng/sai là việc của
    cổng bên `vi_du.py`, KHÔNG làm ở đây, để mọi đường đặt câu đi qua cùng một cổng."""
    raw_response = _send_ai_request(system_prompt, user_prompt, khuon=khuon)
    if not raw_response:
        return None
    parsed = _parse_ai_response(raw_response)
    if not isinstance(parsed, dict):
        log_fail("AI trả về JSON không hợp lệ khi đặt câu ví dụ.")
        return None
    return parsed


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

    raw_response = _send_ai_request(system_prompt, user_prompt, khuon=_KHUON_LEMMA)
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


def call_claude_topic(cac_tu):
    """Phân loại CHỦ ĐỀ cho MỘT LÔ từ — dùng bởi scripts/tag_topics.py.

    `cac_tu`: list các cặp (từ Nga, nghĩa tiếng Anh). Trả về dict {từ: slug},
    slug là None khi AI không xếp được — người gọi PHẢI để trống tag, đừng ép rọ.

    Nhận cả lô chứ không phải từng từ (đổi 23/08/2026): xếp lại toàn bộ kho là
    ~1200 từ, mỗi từ một request thì phần cố định (danh sách 35 chủ đề, ~2K token)
    bị gửi lại 1200 lần. Gộp 25 từ/lượt ⇒ còn ~49 lượt, cùng một danh sách chủ đề
    được trả tiền một lần cho 25 từ.

    🔴 KHÔNG có nhánh "không hợp thì dùng other" trong prompt nữa (QD-38): câu đó
    mời AI đổ rác vào một rọ, và rọ đó chính là thứ vừa phải dọn."""
    if not cac_tu:
        return {}
    system_prompt = (
        "You classify Russian vocabulary words into EXACTLY ONE topic slug each, "
        "from this list, based on the word's most common meaning:\n"
        f"{topics_prompt_block()}\n\n"
        "Rules: use ONLY slugs from the list above. If a word genuinely fits none "
        'of them, return null for that word — do NOT force it into a loose fit. '
        "Keep semantic pairs in the same topic (mother with father, wife with husband).\n"
        'Return ONLY valid JSON, no markdown: '
        '{"ket_qua": [{"tu": "...", "topic": "..." or null}, ...]} '
        "with one entry per input word, in the same order."
    )
    dong = [f'{i + 1}. [{w}] = {en or "N/A"}' for i, (w, en) in enumerate(cac_tu)]
    user_prompt = "Classify these words:\n" + "\n".join(dong) + "\n\nReturn ONLY the JSON."

    raw_response = _send_ai_request(system_prompt, user_prompt, khuon=_KHUON_TOPIC)
    ra = {w: None for w, _en in cac_tu}
    if not raw_response:
        return ra
    parsed = _parse_ai_response(raw_response)
    if not isinstance(parsed, dict):
        return ra
    for muc in parsed.get("ket_qua") or []:
        if isinstance(muc, dict) and muc.get("tu") in ra:
            ra[muc["tu"]] = normalize_topic(muc.get("topic"))
    return ra


def call_claude_pos(cac_tu, co_lo=25):
    """Xếp TỪ LOẠI cho một danh sách từ — dùng bởi `scripts/backfill_badge.py`.

    `cac_tu`: list các cặp (từ Nga, nghĩa tiếng Anh). Trả về dict {từ: mã ngắn};
    mã là None khi AI không xếp được — người gọi PHẢI để ô PoS TRỐNG, đừng ép về
    "other". Danh sách mã hợp lệ ở `topics.TU_LOAI`, và ở đó CỐ Ý không có
    "other"/"unknown" (QD-41): một rọ chứa "phần còn lại" làm thẻ TRÔNG NHƯ đã
    xếp xong nên không ai đi tìm lại — đúng cái bẫy đã phải dọn 93 thẻ.

    🔴 Hàm này TỰ CHIA LÔ, khác `call_claude_topic()` (bắt người gọi tự chia).
    Vì sao lệch: vòng chia lô ở `tag_topics.py` dài ~10 dòng, chép sang
    `backfill_badge.py` là dựng bản thứ hai của cùng một vòng — đúng bệnh
    "10 wrapper AnkiConnect" repo đã trả học phí. Cỡ lô 25 lấy y `tag_topics.CO_LO`:
    to hơn thì model bắt đầu trả thiếu mục, phải gọi lại, mất luôn cái vừa tiết kiệm.
    """
    ra = {w: None for w, _en in cac_tu}
    if not cac_tu:
        return ra
    system_prompt = (
        "You are a Russian linguist. Classify each Russian word into EXACTLY ONE "
        "part-of-speech code from this list:\n"
        f"{pos_prompt_block()}\n\n"
        "Rules: use ONLY codes from the list above. If a word belongs to two classes "
        "(когда = adverb + conjunction), return the PRIMARY one — the one matching the "
        "meaning given for that word. If you genuinely cannot tell, return null for that "
        "word; never invent 'other' or 'unknown'.\n"
        'Return ONLY valid JSON, no markdown: '
        '{"ket_qua": [{"tu": "...", "pos": "..." or null}, ...]} '
        "with one entry per input word, in the same order."
    )
    for i in range(0, len(cac_tu), co_lo):
        lo = cac_tu[i:i + co_lo]
        dong = [f'{j + 1}. [{w}] = {en or "N/A"}' for j, (w, en) in enumerate(lo)]
        user_prompt = ("Classify these words:\n" + "\n".join(dong)
                       + "\n\nReturn ONLY the JSON.")
        raw_response = _send_ai_request(system_prompt, user_prompt, khuon=_KHUON_POS)
        if not raw_response:
            log_warn(f"AI khong tra loi lo tu loai {i}-{i + len(lo)} — de trong, chay lai sau")
            continue
        parsed = _parse_ai_response(raw_response)
        if not isinstance(parsed, dict):
            log_warn(f"AI tra JSON hong o lo tu loai {i}-{i + len(lo)} — de trong")
            continue
        for muc in parsed.get("ket_qua") or []:
            if isinstance(muc, dict) and muc.get("tu") in ra:
                ra[muc["tu"]] = normalize_pos(muc.get("pos"))
    return ra


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


# ==============================================================================
# --- HỢP ĐỒNG PUBLIC (G4, 31/07/2026) ---
# `grammar_forms/ai.py` đang import hai tên private này xuyên gói. Tuyên bố tên
# public để caller đổi dần; THUẦN CỘNG THÊM, tên cũ giữ nguyên. Xem QD-02 và
# mục S2 của `soatkientruc.py`.
# ==============================================================================
parse_ai_response = _parse_ai_response      # bóc JSON từ câu trả lời thô của AI
send_ai_request = _send_ai_request          # gọi API, tự chuyển model khi 429
KHUON_THE_KHONG_TOPIC = _KHUON_THE_KHONG_TOPIC   # khuôn JSON cho thẻ ngữ pháp
