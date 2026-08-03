# ==============================================================================
# --- FORMAT NỘI DUNG THẺ cho tin nhắn Telegram: thẻ vừa thêm + mục từ điển.
# Tách từ core.py (03/08/2026); chỉ flow_add dùng. Một chiều: core <- hienthi.
# ==============================================================================
from anki_tools.utils import hl_to_bracket

from .core import SYNC_FAIL_TEXT


def _card_body_lines(card_info):
    """Phần RUỘT của thẻ (nghĩa, từ loại, chủ đề, 3 ví dụ) — dùng CHUNG cho thẻ vừa
    thêm (format_card_summary) và thẻ đã có sẵn (format_dictionary_entry), để hai
    nơi không bao giờ trình bày lệch nhau."""
    lines = [
        f"🇬🇧 {', '.join(card_info['en_meanings'])}",
        f"🇻🇳 {card_info['vi_meaning']}",
    ]
    # Thể động từ đứng chung ngoặc với giống: hai thứ này loại trừ nhau (danh từ
    # có giống, động từ có thể) nên không bao giờ chen nhau trên cùng một dòng.
    phu = [x for x in (card_info.get("gender"), card_info.get("aspect")) if x]
    lines.append(f"🏷️ {card_info['pos']}" + (f" ({', '.join(phu)})" if phu else ""))
    if card_info.get("topic"):
        lines.append(f"📂 {card_info['topic']}")

    for i, ex in enumerate(card_info.get("simplified_examples", [])[:3]):
        ru = hl_to_bracket(ex.get("ru", ""))
        en = hl_to_bracket(ex.get("en", ""))
        vi = hl_to_bracket(ex.get("vi") or ex.get("vietnamese") or "")
        lines.append(f"💡 {i + 1}. {ru}")
        if en:
            lines.append(f"     🇬🇧 {en}")
        if vi:
            lines.append(f"     🇻🇳 {vi}")
    return lines


def format_card_summary(card_info, elapsed):
    """Bản Telegram của print_card_summary() - text thuần, không markdown."""
    w = hl_to_bracket(card_info["word"])
    forced = " ⚠️ FORCE" if card_info.get("is_forced") else ""
    lines = [f"✅ THẺ MỚI{forced}: {w}"]
    lines += _card_body_lines(card_info)

    if card_info.get("ai_degraded"):
        lines.append(
            "⚠️ AI không tạo được ví dụ/nghĩa Việt lần này — thẻ vẫn được thêm nhưng THIẾU nội dung."
        )
        lines.append(
            f"👉 Bấm nút bên dưới, hoặc gõ /sua {card_info.get('clean_word', '')} để AI làm lại."
        )

    lines.append(f"📦 {card_info['deck']} | ⏱ {elapsed:.1f}s")
    if card_info.get("synced") is False:
        lines.append(SYNC_FAIL_TEXT)
    else:
        lines.append("☁️ Đã sync AnkiWeb — mở app Anki bấm sync để thấy thẻ.")
    return "\n".join(lines)


def format_dictionary_entry(card_info, index=0, total=1):
    """Gõ một từ ĐÃ CÓ thẻ -> bot trả về nguyên nội dung thẻ đó như một mục TỪ ĐIỂN
    (user chốt 21/07/2026: báo 'bị trùng' suông là phí — thẻ đã có sẵn đủ nghĩa,
    ví dụ, audio thì cứ đọc ra). Dùng chung _card_body_lines() với thẻ mới thêm nên
    bố cục y hệt, chỉ khác phần đuôi: trạng thái học + audio + deck thay cho ⏱/sync.

    index/total: khi 1 từ có nhiều note trùng, cho biết đang xem note thứ mấy."""
    w = hl_to_bracket(card_info["word"])
    which = f" (note {index + 1}/{total})" if total > 1 else ""
    lines = [f"📖 {w} — ĐÃ CÓ THẺ{which}"]
    lines += _card_body_lines(card_info)

    lines.append("─────────────")
    lines.append("🔊 Có audio" if card_info.get("has_audio") else "🔇 Thẻ chưa có audio")
    if card_info.get("image"):
        lines.append("🖼 Thẻ có ảnh minh họa")
    if card_info.get("raw_count"):
        lines.append(f"📄 Kèm {card_info['raw_count']} câu gốc OpenRussian (ô RawExamples)")
    lines.append(f"📦 {card_info['deck']}")
    if card_info.get("status_text"):
        lines.append(f"📈 {card_info['status_text']}")

    if card_info.get("ai_degraded"):
        lines.append("⚠️ Thẻ này THIẾU ví dụ/nghĩa Việt — nên bấm 🔄 Làm lại thẻ.")
    return "\n".join(lines)
