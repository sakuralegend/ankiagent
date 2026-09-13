# -*- coding: utf-8 -*-
"""Soi thẻ LỆCH GIỮA DECK VÀ Ô `Stage` — thẻ hiện sai mặt.

Vì sao có file này (SONO.md 03/08/2026, QD-17): việc thăng cấp GĐ1→GĐ2 ghi vào
HAI CHỖ KHÁC NHAU — ô `Stage` nằm trên **note**, còn deck + lịch nằm trên **thẻ**.
Anki xử xung đột sync **riêng cho note và riêng cho card**, nên một nửa thắng một
nửa thua. Đã nổ hai lần, HAI CHIỀU NGƯỢC NHAU:
  · 31/07 — mất nhãn, giữ deck ⇒ 23 thẻ ở GĐ2 hiện mặt làm quen
  · 03/08 — mất deck, giữ nhãn ⇒ 21 thẻ ở GĐ1 hiện mặt gõ
Cả hai lần đều IM LẶNG tuyệt đối: không lỗi nào bật ra ở bất kỳ đâu, user phát
hiện bằng mắt. Nguyên nhân gốc (xung đột sync) **không sửa được** — chỉ dò rồi vá
lại được, nên đây là cửa canh chứ không phải bản vá.

🔴 DECK LÀ BÊN ĐÚNG. Deck là thứ user nhìn thấy và điều khiển; `Stage` chỉ là cái
nhãn quyết định mặt thẻ. Nên mọi phép sửa ở đây đều kéo trạng thái về cho khớp
DECK, không bao giờ ngược lại.

⚠️ Ngoại lệ có chủ ý — thẻ ĐÃ tốt nghiệp mà bị đá ngược về GĐ1 thì **đẩy tiếp
sang GĐ2** chứ không gỡ nhãn. Vì `forgetCards` của việc thăng cấp là MỤC ĐÍCH:
GĐ1 là chặng user bấm Again rất nhiều nên độ khó tích lại, GĐ2 phải bắt đầu sạch
(user chốt 03/08). Gỡ nhãn cho "lành" là phá đúng thứ hệ thống được dựng để làm.
Và nó gọi lại `anki_client.thang_cap_gd2()` — KHÔNG dựng bản thứ hai của ba bước.
"""
import time

from .anki_client import _ac, sync_truoc_khi_ghi_lo, thang_cap_gd2
from .config import STAGE1_DECK, TOPIC_DECK_PARENT
from .utils import log_warn

# Lệch mới dưới ngần này giây thì BỎ QUA. Lúc `thang_cap_gd2` đang chạy dở, thẻ
# lệch vài giây là bình thường (nó ghi nhãn trước, đổi deck sau) — cửa canh nhảy
# vào giữa là giẫm chân nhau. 10 phút đủ rộng cho mọi đợt thăng cấp thật (đợt to
# nhất từng đo: 36 thẻ, vài giây), vẫn đủ nhanh để user thấy trong 1 nhịp sync.
HOAN_GIAY = 600


def tim_lech(the, da_tot_nghiep, bay_gio, hoan_giay=HOAN_GIAY):
    """PHẦN THUẦN — không mạng, không Anki, nên test offline được.

    `the`: list dict {cardId, noteId, deck, stage, note_mod}
    `da_tot_nghiep`: set cardId mà Anki trả về cho truy vấn `is:review` (dùng
        CHÍNH truy vấn của `promote_stage1_to_stage2` để hai bên không thể lệch
        định nghĩa "đã pass Good 2 lần" — đừng tự suy từ `type`/`queue`).
    `bay_gio`: epoch giây.

    Trả về dict 3 rổ: thang_cap · go_nhan · gan_nhan."""
    ra = {"thang_cap": [], "go_nhan": [], "gan_nhan": []}
    for t in the:
        deck = t.get("deck") or ""
        # Thẻ bị kéo vào deck LỌC mang tên deck lọc, không nằm dưới RUSSIAN:: —
        # bỏ qua, đừng động vào lịch của nó (cùng lý do `promote` lọc `at_home`).
        if not deck.startswith(TOPIC_DECK_PARENT + "::"):
            continue
        if bay_gio - t.get("note_mod", 0) < hoan_giay:
            continue
        stage = (t.get("stage") or "").strip()
        if deck == STAGE1_DECK:
            if not stage:
                continue                       # đúng: GĐ1 thì nhãn phải rỗng
            if t["cardId"] in da_tot_nghiep:
                ra["thang_cap"].append(t)      # đã pass 2 lần -> đẩy tiếp sang GĐ2
            else:
                ra["go_nhan"].append(t)        # chưa pass -> "để nguyên đấy"
        elif stage != "type":
            ra["gan_nhan"].append(t)           # GĐ2/kho thì CẤM mang mặt GĐ1
    return ra


def ghep_the(theo_deck, co_nhan, la_type):
    """PHẦN THUẦN — dựng bảng thẻ từ ba câu trả lời NHẸ của Anki (test offline được).

    `theo_deck`: `getDecks` → {tên deck: [cardId]} · `co_nhan`: set cardId mà ô
    `Stage` KHÁC rỗng · `la_type`: set cardId mà `Stage` = "type". Nhãn khác rỗng
    mà không phải "type" ghi "?" — `tim_lech` chỉ hỏi *rỗng hay không* và *có phải
    "type" không*, nên "?" cho ra cùng phán quyết với giá trị thật.

    `noteId`/`note_mod`/`tu` cố ý để TRỐNG ở bước này: tra ba thứ đó cho cả kho là
    tải 14 MB, mà chỉ thẻ NGHI lệch mới cần — xem `_bo_sung_note`."""
    the = []
    for deck, cids in (theo_deck or {}).items():
        for cid in cids:
            stage = "type" if cid in la_type else ("?" if cid in co_nhan else "")
            the.append({"cardId": cid, "noteId": None, "deck": deck,
                        "stage": stage, "note_mod": 0, "tu": "?"})
    return the


def _doc_the():
    """Đọc deck + nhãn của mọi thẻ trong bộ sưu tập. 5 lời gọi, ~0,4 s / 1 295 thẻ.

    🔴 CẤM `cardsInfo` cho cả kho ở đây (đo 13/09/2026: 127 MB/lần vì nó kèm HTML
    mặt trước/sau + CSS ĐÃ DỰNG của từng thẻ, Python tốn 613 MB RAM để đọc, cửa
    canh gọi 48 lần/ngày ⇒ bot chiếm 1 GB + 930 MB swap trên VPS 2 GB, các dự án
    cùng máy kêu). Ba lệnh dưới trả đúng thứ cần (deck, nhãn) — tổng 0,14 MB.
    `anki_thongke.py` đã tránh `cardsInfo` cùng lý do; test canh cả hai."""
    goc = f'deck:"{TOPIC_DECK_PARENT}::*"'
    cids = _ac("findCards", query=goc)
    if not cids:
        return [], set()
    theo_deck = _ac("getDecks", cards=cids)
    co_nhan = set(_ac("findCards", query=f"{goc} Stage:_*"))
    la_type = set(_ac("findCards", query=f"{goc} Stage:type"))
    tot_nghiep = set(_ac("findCards",
                         query=f'deck:"{STAGE1_DECK}" is:review -is:suspended'))
    return ghep_the(theo_deck, co_nhan, la_type), tot_nghiep


def _bo_sung_note(the):
    """Tra note id · thời điểm sửa · chữ `Word` — CHỈ cho các thẻ nghi lệch (thường
    0, đợt to nhất từng đo 36), không phải cả kho. `cardsToNotes` trả danh sách
    KHÔNG theo thứ tự nên phải hỏi từng thẻ một."""
    for t in the:
        t["noteId"] = _ac("cardsToNotes", cards=[t["cardId"]])[0]
    nids = sorted({t["noteId"] for t in the})
    mod = {m["noteId"]: m["mod"] for m in _ac("notesModTime", notes=nids)}
    tu = {n["noteId"]: n.get("fields", {}).get("Word", {}).get("value") or "?"
          for n in _ac("notesInfo", notes=nids)}
    for t in the:
        t["note_mod"] = mod.get(t["noteId"], 0)
        t["tu"] = tu.get(t["noteId"], "?")
    return the


def soat_va_va(apply=True, da_sync=False):
    """Soát toàn bộ, vá chỗ lệch. Trả về (số thẻ đã vá, báo cáo dạng chữ).

    `apply=False` = CHẠY KHAN: chỉ báo, không ghi gì. Dùng để nghiệm thu.
    `da_sync=True` = người gọi vừa kéo AnkiWeb về xong (nhịp sync 30′), khỏi kéo
        lần hai. Mặc định False thì tự kéo — QD-16: ghi hàng loạt lên note mà
        chưa kéo về là ghi đè lên bản chép cũ, đúng cái đẻ ra sự cố 31/07.

    Sạch thì trả (0, "") để người gọi IM LẶNG — không nhắn tin rỗng mỗi 30 phút."""
    if apply and not da_sync and not sync_truoc_khi_ghi_lo("vá thẻ lệch giai đoạn"):
        return 0, ""
    the, tot_nghiep = _doc_the()
    bay_gio = time.time()
    # Lượt 1 chưa có `note_mod` (=0, coi như cũ) → ra danh sách NGHI lệch, thường
    # rỗng. Lượt 2 tra note cho đúng các thẻ đó rồi lọc lại theo HOAN_GIAY —
    # kết quả y hệt soát một lượt trên đủ dữ liệu, chỉ khác là không tải cả kho.
    nghi = [t for r in tim_lech(the, tot_nghiep, bay_gio).values() for t in r]
    if not nghi:
        return 0, ""
    lech = tim_lech(_bo_sung_note(nghi), tot_nghiep, bay_gio)
    tong = sum(len(v) for v in lech.values())
    if not tong:
        return 0, ""

    dong = []
    for t in lech["thang_cap"]:
        dong.append(f"⬆️ {t['tu']}: ở GĐ1 mà đã tốt nghiệp → đẩy sang GĐ2 (reset lịch)")
    for t in lech["go_nhan"]:
        dong.append(f"↩️ {t['tu']}: ở GĐ1 mà chưa tốt nghiệp → gỡ nhãn về mặt làm quen")
    for t in lech["gan_nhan"]:
        dong.append(f"🏷️ {t['tu']}: ở {t['deck']} mà thiếu nhãn → gắn lại mặt gõ")
    # Log TỪNG thẻ: đây là dấu vết duy nhất để lùi tay nếu cửa này vá sai.
    for d in dong:
        log_warn(f"[soat_giaidoan] {d}")

    if apply:
        thang_cap_gd2([t["cardId"] for t in lech["thang_cap"]],
                      sorted({t["noteId"] for t in lech["thang_cap"]}))
        for t in lech["go_nhan"]:
            _ac("updateNoteFields", note={"id": t["noteId"], "fields": {"Stage": ""}})
        for t in lech["gan_nhan"]:
            _ac("updateNoteFields", note={"id": t["noteId"], "fields": {"Stage": "type"}})

    dau = "Đã vá" if apply else "CHẠY KHAN — sẽ vá"
    return tong, f"{dau} {tong} thẻ hiện sai mặt:\n" + "\n".join(dong)
