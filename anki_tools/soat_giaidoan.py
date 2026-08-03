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


def _doc_the():
    """Đọc deck + nhãn của mọi thẻ trong bộ sưu tập. 3 lời gọi, ~4,8s/976 thẻ."""
    cids = _ac("findCards", query=f'deck:"{TOPIC_DECK_PARENT}::*"')
    if not cids:
        return [], set()
    cards = _ac("cardsInfo", timeout=300, cards=cids)
    notes = _ac("notesInfo", timeout=300,
                notes=sorted({c["note"] for c in cards if c.get("note")}))
    stage, mod, tu = {}, {}, {}
    for n in notes:
        f = n.get("fields", {})
        stage[n["noteId"]] = f.get("Stage", {}).get("value") or ""
        mod[n["noteId"]] = n.get("mod", 0)
        tu[n["noteId"]] = f.get("Word", {}).get("value") or "?"
    the = [{"cardId": c["cardId"], "noteId": c.get("note"), "deck": c.get("deckName"),
            "stage": stage.get(c.get("note"), ""), "note_mod": mod.get(c.get("note"), 0),
            "tu": tu.get(c.get("note"), "?")}
           for c in cards if isinstance(c, dict)]
    tot_nghiep = set(_ac("findCards",
                         query=f'deck:"{STAGE1_DECK}" is:review -is:suspended'))
    return the, tot_nghiep


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
    lech = tim_lech(the, tot_nghiep, time.time())
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
