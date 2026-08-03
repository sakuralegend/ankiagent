# ==============================================================================
# --- ĐẾM THẺ: trạng thái học (Card Counts) + phân bố chủ đề (/thongke của bot).
# Tách từ anki_client.py (03/08/2026, QD-18). Caller vẫn import anki_client.
# ==============================================================================
import requests

from .config import ANKI_CONNECT_URL, MODEL_NAME
from .topics import TOPICS, normalize_topic
from .utils import log_warn

# --- Đếm thẻ theo TRẠNG THÁI HỌC (bản Telegram của màn "Card Counts" trong Anki) ---
# Mốc 21 ngày là hằng số của chính Anki để tách thẻ "trẻ" khỏi thẻ "trưởng thành".
MATURE_IVL_DAYS = 21

# Thẻ TẠM NGƯNG/TẠM ẨN phải được tách ra TRƯỚC rồi phần còn lại mới chia theo trạng
# thái học — đúng thứ tự Anki làm, nhờ vậy các nhóm không chồng lấn nhau.
_ACTIVE = "-is:suspended -is:buried"

# (slug, nhãn hiển thị, truy vấn Anki). Thứ tự này cũng là thứ tự hiện trong báo cáo:
# đi theo vòng đời một tấm thẻ — mới -> đang học -> trẻ -> trưởng thành.
CARD_STATES = [
    ("new", "🆕 Mới (chưa học)", f"is:new {_ACTIVE}"),
    ("learning", "📖 Đang học", f"is:learn {_ACTIVE}"),
    ("young", f"🌱 Trẻ (dưới {MATURE_IVL_DAYS} ngày)",
     f"is:review prop:ivl<{MATURE_IVL_DAYS} {_ACTIVE}"),
    ("mature", f"🌳 Trưởng thành (từ {MATURE_IVL_DAYS} ngày)",
     f"is:review prop:ivl>={MATURE_IVL_DAYS} {_ACTIVE}"),
    ("suspended", "⏸ Tạm ngưng", "is:suspended"),
    ("buried", "🫥 Tạm ẩn", f"is:buried -is:suspended"),
]


def get_card_state_stats(deck=None):
    """Đếm thẻ theo trạng thái học, chia nhóm y như màn "Card Counts" của Anki.
    deck=None -> cả collection; deck="RUSSIAN" -> deck đó và mọi deck con của nó.
    Trả về (counts: dict slug->số thẻ, total) hoặc (None, 0) nếu AnkiConnect lỗi.

    Lọc theo DECK chứ không theo model (user chốt 22/07/2026: "đừng lẫn 2 deck lớn
    vào nhau"). Lọc theo model thì mảng ngữ pháp GRAMMAR:: — vốn dùng model RU_Plural
    riêng — sẽ biến mất khỏi báo cáo mà không ai hay.

    CỐ Ý đếm bằng findCards (chỉ trả về danh sách id) thay vì cardsInfo: cardsInfo
    kèm theo cả HTML mặt trước/sau ĐÃ DỰNG của từng thẻ — với ~700 thẻ là vài MB
    tải về chỉ để đọc hai con số queue/type.

    Nhóm "Đang học" gộp cả thẻ học lại (lapse). Anki tách riêng Relearning, nhưng đã
    đo trên chính collection này: `is:learn` và `is:review` KHÔNG giao nhau nên không
    có cách tách bằng truy vấn — mà bốn nhóm chính mới là thứ cần nhìn hằng ngày."""
    # Thoát dấu " trong tên deck y như get_deck_note_ids() — tên deck do user đặt
    safe_deck = (deck or "").replace('"', '\\"')
    scope = f'deck:"{safe_deck}"' if deck else ""

    def count(query):
        res = requests.post(ANKI_CONNECT_URL, json={
            "action": "findCards", "version": 6,
            "params": {"query": f"{scope} {query}".strip()}
        }, timeout=20)
        out = res.json()
        if out.get("error"):
            raise RuntimeError(out["error"])
        return len(out.get("result") or [])

    try:
        counts = {slug: count(query) for slug, _, query in CARD_STATES}
        total = count("")
    except Exception as e:
        log_warn(f"Không đếm được trạng thái thẻ của deck '{deck or 'toàn bộ'}': {e}")
        return None, 0
    return counts, total


def get_topic_stats():
    """Đếm thẻ theo từng chủ đề topic:: (cho lệnh /thongke của bot).
    Đọc tag của TỪNG note rồi đếm phía Python — KHÔNG query tag:"topic::X" từng
    chủ đề, vì Anki coi tag cha khớp cả tag con (cây lồng cấp sẽ bị đếm đúp).
    Tag tên cũ (LEGACY_ALIASES) được quy về slug mới.
    Trả về (stats: dict slug->số thẻ, untagged: số note chưa có tag topic::)
    hoặc (None, 0) nếu AnkiConnect lỗi."""
    try:
        res = requests.post(ANKI_CONNECT_URL, json={
            "action": "findNotes", "version": 6,
            "params": {"query": f'note:"{MODEL_NAME}"'}
        }, timeout=15)
        note_ids = res.json().get("result") or []
        res_info = requests.post(ANKI_CONNECT_URL, json={
            "action": "notesInfo", "version": 6, "params": {"notes": note_ids}
        }, timeout=60)
        notes = res_info.json().get("result") or []

        stats = {slug: 0 for slug in TOPICS}
        untagged = 0
        for n in notes:
            tags = [t for t in n.get("tags", []) if t.startswith("topic::")]
            if not tags:
                untagged += 1
                continue
            slug = normalize_topic(tags[0])
            stats[slug] = stats.get(slug, 0) + len(n.get("cards", []))
        return stats, untagged
    except Exception as e:
        log_warn(f"Không đếm được thống kê chủ đề: {e}")
        return None, 0
