# ==============================================================================
# --- XÂY DỰNG EXAMPLES HTML (nhánh AI + nhánh fallback) ---
# Từ khi gỡ nút AI Refine khỏi thẻ, đây là NƠI DUY NHẤT dựng HTML khối ví dụ
# (cả lúc thêm thẻ mới lẫn lúc sửa thẻ qua /sua của bot đều đi qua đây).
# Đổi cấu trúc HTML/class CSS chỉ cần sửa ở file này (+ card.css nếu đổi class).
# ⚠️ Nửa dưới file là các hàm ĐỌC NGƯỢC (parse_*) HTML đã dựng để hiện lại thẻ cũ
# dưới dạng text (bot tra từ điển). Đổi cấu trúc ở nửa trên PHẢI sửa luôn nửa dưới.
# ==============================================================================
import html as html_lib
import json
import re

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
    """Trả về (examples_html, vi_meaning, simplified_examples_list, topic_slug).
    topic_slug: chủ đề AI chọn (slug trong topics.TOPICS) hoặc None ở các nhánh
    fallback không có AI — khi đó thẻ KHÔNG được gắn tag topic:: (gắn bù sau
    bằng: python tag_topics.py --missing).
    Thứ tự ưu tiên:
    1. Gọi call_claude_ai với raw examples (rewrite + dịch)
    2. Nếu thất bại hoặc không có raw examples -> call_claude_ai_freestyle (AI tự sinh)
    3. Nếu cả hai đều thất bại -> fallback raw examples gốc
    """
    # Nếu có raw examples, thử gọi AI rewrite trước
    if raw_examples:
        ai_result = call_claude_ai(word_clean, raw_examples, english_meanings)
        if ai_result:
            return _build_from_ai_result(ai_result) + (ai_result.get("topic"),)

    # Raw examples rỗng hoặc AI rewrite thất bại -> thử AI freestyle (tối đa 2 lần,
    # vì freestyle là phao cuối cùng có AI - trượt là thẻ mất hẳn ví dụ + nghĩa Việt)
    for attempt in range(2):
        if attempt == 1:
            log_warn("AI freestyle thất bại lần 1 -> thử lại lần 2...")
        ai_freestyle = call_claude_ai_freestyle(word_clean, english_meanings)
        if ai_freestyle:
            return _build_from_ai_result(ai_freestyle) + (ai_freestyle.get("topic"),)

    # Cả hai đều thất bại, nếu còn raw examples thì dùng tạm
    if raw_examples:
        return _build_fallback_from_raw(raw_examples, english_meanings) + (None,)

    # Hoàn toàn không có gì
    vi_meaning = ", ".join(english_meanings) if english_meanings else "N/A"
    return "", vi_meaning, [], None


# ==============================================================================
# --- ĐỌC NGƯỢC: HTML trong thẻ -> text thuần ---
# Bot tra từ điển (gõ từ đã có thẻ) cần hiện lại NGUYÊN NỘI DUNG thẻ cũ, mà thẻ
# chỉ lưu HTML. Các hàm dưới đây là hàm nghịch của _build_example_block() và của
# meaning_html trong anki_client.build_card_fields() — sửa cấu trúc HTML ở trên
# thì phải sửa regex ở đây, nếu không bot sẽ hiện thẻ cũ TRỐNG RỖNG.
# ==============================================================================

# <span class="hl">x</span> -> <hl>x</hl> để dùng lại utils.hl_to_bracket ([x])
_HL_SPAN_RE = re.compile(r'<span class="hl">(.*?)</span>', re.S)
# Bỏ mọi thẻ CÒN LẠI nhưng chừa <hl>/</hl> vừa dựng ở trên.
# ⚠️ Dấu / phải nằm TRONG lookahead: viết "</?(?!hl\b)..." thì regex vẫn khớp được
# </hl> bằng cách coi "/" là ký tự đầu tên thẻ -> nuốt mất thẻ đóng, câu ví dụ hiện
# ra thành "Trời [đẹp quá, đi dạo không?" (đã dính lỗi này và test bắt được).
_OTHER_TAG_RE = re.compile(r"<(?!/?hl\b)/?[a-zA-Z!][^>]*>")


def html_fragment_to_text(fragment):
    """1 mẩu HTML trong thẻ -> text thuần, giữ <hl>...</hl> đánh dấu từ đích."""
    if not fragment:
        return ""
    text = _HL_SPAN_RE.sub(r"<hl>\1</hl>", fragment)
    text = re.sub(r"<br\s*/?>", " ", text)
    text = _OTHER_TAG_RE.sub("", text)
    text = html_lib.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def parse_meaning_html(meaning_html):
    """Ô Meaning (<ol class="meaning-list"><li>..</li></ol>) -> list nghĩa tiếng Anh."""
    items = re.findall(r"<li[^>]*>(.*?)</li>", meaning_html or "", re.S)
    return [t for t in (html_fragment_to_text(i) for i in items) if t]


def parse_gender_badge(badge_html):
    """Ô GenderBadge (<div class="badge m">Masculine ♂</div>) -> 'Masculine ♂'."""
    return html_fragment_to_text(badge_html)


def parse_examples_html(examples_html):
    """Ô ExamplesHTML -> [{'ru','en','vi'}] (hàm nghịch của _build_example_block).

    Mỗi ví dụ nằm trong 1 khối <details>; cắt theo khối TRƯỚC rồi mới bóc từng
    ngôn ngữ, nhờ vậy câu tiếng Việt (bọc trong <span class="vi-text"> có thể
    chứa <span class="hl"> lồng bên trong) không bị lẫn sang ví dụ kế tiếp."""
    html_text = examples_html or ""
    blocks = re.findall(r"<details\b.*?</details>", html_text, re.S)
    if not blocks and html_text.strip():
        blocks = [html_text]  # thẻ đời cũ / cấu trúc lạ: cứ thử bóc nguyên khối
    examples = []
    for block in blocks:
        ru = re.search(r'<div class="ex-ru">(.*?)</div>', block, re.S)
        en = re.search(r'<div class="ex-en">(.*?)</div>', block, re.S)
        # THAM LAM cố ý: </span> đầu tiên có thể là của <span class="hl"> lồng trong
        vi = re.search(r'<span class="vi-text">(.*)</span>', block, re.S)
        ex = {
            "ru": html_fragment_to_text(ru.group(1) if ru else ""),
            "en": html_fragment_to_text(en.group(1) if en else ""),
            "vi": html_fragment_to_text(vi.group(1) if vi else ""),
        }
        if ex["ru"] or ex["en"] or ex["vi"]:
            examples.append(ex)
    return examples


def parse_raw_examples(raw_json):
    """Ô RawExamples (JSON câu gốc OpenRussian) -> list[dict] ([] nếu hỏng/trống)."""
    try:
        data = json.loads(raw_json or "[]")
        return data if isinstance(data, list) else []
    except (ValueError, TypeError):
        return []
