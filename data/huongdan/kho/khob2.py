# -*- coding: utf-8 -*-
"""🧹 CODE TẠM — kho chờ `B2-pending` cho từ sách B2. HẾT HẠN KHI: `chon N` báo "HẾT sách"
VÀ deck `B2-pending` rỗng ⇒ XOÁ file này + mọi dòng `khob2` (grep `khob2` ra đủ) + dòng
nợ trong `SONO.md` + cụm "/ chuyển từ B2 sang học" ở dòng rẽ lô của `CLAUDE.md`. `xephangdoi.py` (chạy khan) TỰ NHẮC khi kho rỗng; `SONO.md` có hạn
chót, quá hạn thì cửa S18 chặn deploy — user dặn 21/11 "để nó không trở thành rác".

User chốt 21/11/2026: từ B2 (sau B1) chỉ để làm KHO, chưa học. Thẻ tạo vào deck gốc
`B2-pending` (NGOÀI `RUSSIAN` ⇒ bấm học RUSSIAN không lôi chúng ra; bot đêm 3h và
`soat_giaidoan` chỉ quét `RUSSIAN::*`, đo 21/11), mặt 1-go (Stage="type"). Hướng dẫn
soạn NGAY như mọi lô. Muốn học ⇒ user nhờ AI: `xephangdoi.py chuyen N --apply` đưa N
từ LÔ ĐẦU về `RUSSIAN::0-quen`, Stage rỗng, `forgetCards` (user muốn RESET trạng thái).
Thứ tự ra học giữ nguyên: Anki đặt vị trí thẻ mới lúc TẠO, `changeDeck` không đổi.
Cố ý tách file riêng: code tạm gom một chỗ thì xoá sạch được; rải vào xephangdoi.py
(sát trần 400 dòng) là để lại mảnh vụn.
"""
from anki_tools import goi_anki
from anki_tools.anki_client import cham_vao_kho, sync_truoc_khi_ghi_lo
from anki_tools.config import MODEL_NAME, STAGE1_DECK

DECK = "B2-pending"
_THE = f'note:"{MODEL_NAME}" deck:"{DECK}"'      # 🔴 luôn lọc note: (bẫy CLAUDE.md)


def tao_deck(dot):
    """Trước khi tạo thẻ: deck phải có sẵn, addNote vào deck chưa có là bị từ chối."""
    if any(l.get("deck") == DECK for l in dot):
        goi_anki("createDeck", deck=DECK)


def gan_mat_go():
    """Thẻ trong kho chưa mang Stage="type" ⇒ gắn (mặt 1-go). Idempotent, tự vá lần sau."""
    nids = goi_anki("findNotes", query=f"{_THE} -Stage:_*")
    for nid in nids:
        goi_anki("updateNoteFields", note={"id": nid, "fields": {"Stage": "type"}})
    if nids:
        print(f"gắn mặt 1-go cho {len(nids)} thẻ {DECK}")
        sync_truoc_khi_ghi_lo("gắn mặt gõ B2")


def chon_chuyen(q, trong_kho, n=None, ids=()):
    """PHẦN THUẦN: từ nào chuyển, theo thứ tự LÔ (số nhỏ trước) rồi thứ tự từ trong lô.
    `trong_kho`: {WordClean đang nằm ở DECK} — Anki là nguồn sự thật, hàng đợi không
    ghi gì thêm nên không có sổ thứ hai để lệch."""
    lo = sorted((l for l in q["lo"] if l.get("deck") == DECK and (not ids or l["id"] in ids)),
                key=lambda l: int(l["id"][1:]))
    tu = [w for l in lo for w in l["tu"] if w in trong_kho]
    return tu[:n] if n else tu


def cmd_chuyen(q, n, ids, apply):
    notes = goi_anki("notesInfo", notes=goi_anki("findNotes", query=_THE))
    theo = {x["fields"]["WordClean"]["value"].strip(): x["noteId"] for x in notes}
    tu = chon_chuyen(q, set(theo), n, ids)
    print(f"{DECK}: {len(theo)} thẻ · chuyển {len(tu)} về {STAGE1_DECK}: {' '.join(tu[:30])}"
          f"{' …' if len(tu) > 30 else ''}")
    if not tu or not apply:
        return print("" if apply else "(CHẠY KHAN — thêm --apply)")
    if not sync_truoc_khi_ghi_lo("chuyển B2 sang học"):
        return
    nids = [theo[w] for w in tu]
    cards = goi_anki("findCards", query=f'{_THE} ({" OR ".join(f"nid:{x}" for x in nids)})')
    for nid in nids:                                  # cùng ba bước với thang_cap_gd2, chiều ngược
        goi_anki("updateNoteFields", note={"id": nid, "fields": {"Stage": ""}})
    goi_anki("forgetCards", timeout=120, cards=cards)
    goi_anki("createDeck", deck=STAGE1_DECK)
    goi_anki("changeDeck", timeout=120, cards=cards, deck=STAGE1_DECK)
    cham_vao_kho(nids[0])                             # changeDeck một mình KHÔNG lên sync (QD-34)
    sync_truoc_khi_ghi_lo("đẩy B2 vừa chuyển")
    print(f"đã chuyển {len(nids)} note / {len(cards)} thẻ về {STAGE1_DECK}")


def nhac(q):
    """Dòng nhắc XOÁ code tạm khi kho đã dùng mà nay rỗng — in ở `xephangdoi.py` khan."""
    if not any(l.get("deck") == DECK for l in q["lo"]):
        return None
    try:
        if goi_anki("findCards", query=_THE):
            return None
    except Exception:
        return None                                   # không có Anki thì thôi nhắc, khỏi kêu oan
    return (f"🧹 Kho {DECK} đang RỖNG. Nếu `chon 1` báo 'HẾT sách' ⇒ code tạm đã xong việc: "
            "xoá data/huongdan/kho/khob2.py + mọi dòng `khob2` + dòng nợ SONO.md.")
