# ==============================================================================
# --- XÂY DỰNG EXAMPLES HTML (nhánh AI + nhánh fallback) ---
# Từ khi gỡ nút AI Refine khỏi thẻ, đây là NƠI DUY NHẤT dựng HTML khối ví dụ
# (cả lúc thêm thẻ mới lẫn lúc sửa thẻ qua /sua của bot đều đi qua đây).
# Đổi cấu trúc HTML/class CSS chỉ cần sửa ở file này (+ card.css nếu đổi class).
# ==============================================================================
from .utils import log_warn, apply_hl
from .ai_client import call_claude_ai, call_claude_ai_freestyle


def _build_example_block(index, ru_text, en_text, vi_text):
    """Tạo 1 khối <details> ví dụ dùng chung cho cả nhánh AI và nhánh fallback."""
    open_attr = " open" if index == 0 else ""
    label_suffix = " (Xem ngay)" if index == 0 else " (Bấm để mở rộng)"
    return (
        f'<details class="example-toggle"{open_attr}>'
        f'<summary class="example-summary">💡 Example {index + 1}{label_suffix}</summary>'
        f'<div class="example-content">'
        f'<div class="ex-ru">{ru_text}</div>'
        f'<div class="ex-en">{en_text}</div>'
        f'<div class="ex-vi"><span class="arrow">➔</span><span class="vi-text">{vi_text}</span></div>'
        f'</div>'
        f'</details>'
    )


def _build_from_ai_result(ai_result):
    """Từ ai_result dict, tạo examples_html và simplified list. Trả về (examples_html, vi_meaning, simplified)."""
    vi_meaning = ai_result.get("vietnamese_meaning", "")
    ai_examples = ai_result.get("simplified_examples", [])
    simplified = ai_examples[:3]
    examples_html = ""
    for i, ex in enumerate(simplified):
        ru_text = apply_hl(ex.get("ru", "").strip())
        en_text = apply_hl(ex.get("en", "").strip())
        vi_text = apply_hl((ex.get("vi") or ex.get("vietnamese") or "").strip())
        examples_html += _build_example_block(i, ru_text, en_text, vi_text)
    return examples_html, vi_meaning, simplified


def _build_fallback_from_raw(raw_examples, english_meanings):
    """Fallback cuối cùng: dùng raw examples thô, không AI."""
    log_warn("🔄 Fallback: dùng raw examples gốc (không qua AI).")
    vi_meaning = ", ".join(english_meanings) if english_meanings else "N/A"
    examples_html = ""
    simplified = []
    for i, ex in enumerate(raw_examples[:3]):
        ru_text = ex.get("ru", "").strip()
        en_text = ex.get("en", "").strip()
        simplified.append({"ru": ru_text, "en": en_text, "vi": ""})
        examples_html += _build_example_block(i, ru_text, en_text, "")
    return examples_html, vi_meaning, simplified


def build_html_from_ai_result(ai_result):
    """Public wrapper cho _build_from_ai_result — dùng ở luồng sửa thẻ (/sua của bot).
    Nhận dict {"vietnamese_meaning", "simplified_examples"} từ AI,
    trả về (examples_html, vi_meaning, simplified)."""
    return _build_from_ai_result(ai_result)


def build_examples_html(word_clean, raw_examples, english_meanings):
    """Trả về (examples_html, vi_meaning, simplified_examples_list).
    Thứ tự ưu tiên:
    1. Gọi call_claude_ai với raw examples (rewrite + dịch)
    2. Nếu thất bại hoặc không có raw examples -> call_claude_ai_freestyle (AI tự sinh)
    3. Nếu cả hai đều thất bại -> fallback raw examples gốc
    """
    # Nếu có raw examples, thử gọi AI rewrite trước
    if raw_examples:
        ai_result = call_claude_ai(word_clean, raw_examples, english_meanings)
        if ai_result:
            return _build_from_ai_result(ai_result)

    # Raw examples rỗng hoặc AI rewrite thất bại -> thử AI freestyle (tối đa 2 lần,
    # vì freestyle là phao cuối cùng có AI - trượt là thẻ mất hẳn ví dụ + nghĩa Việt)
    for attempt in range(2):
        if attempt == 1:
            log_warn("AI freestyle thất bại lần 1 -> thử lại lần 2...")
        ai_freestyle = call_claude_ai_freestyle(word_clean, english_meanings)
        if ai_freestyle:
            return _build_from_ai_result(ai_freestyle)

    # Cả hai đều thất bại, nếu còn raw examples thì dùng tạm
    if raw_examples:
        return _build_fallback_from_raw(raw_examples, english_meanings)

    # Hoàn toàn không có gì
    vi_meaning = ", ".join(english_meanings) if english_meanings else "N/A"
    return "", vi_meaning, []
