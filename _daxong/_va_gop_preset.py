# -*- coding: utf-8 -*-
"""VIỆC MỘT LẦN — gộp 4 preset deck thành 1, bỏ trần thẻ mới/ngày.

Vì sao: đo 23/08/2026 cho thấy 3 trong 4 preset đang cai quản **0 thẻ**
(`0-quen`, `1-go` chỉ là trạm trung chuyển, thẻ chảy qua rồi về deck chủ đề),
và 21 tham số FSRS + bước học của cả 4 GIỐNG HỆT nhau. Khác biệt còn lại đúng
2 khoá: trần thẻ mới (Default 20, ba cái kia 9999) và thứ tự lấy thẻ mới.
User chốt 23/08: bỏ trần, và lấy "thẻ vừa thêm lên trước" làm chuẩn chung vì
từ nay mỗi ngày sẽ bơm 10 từ mới vào.

Chạy:  python _va_gop_preset.py           -> chỉ IN, không đụng gì
       python _va_gop_preset.py --apply   -> làm thật
Xong thì chuyển vào `_daxong/` NGAY trong cùng commit (L2).
"""
import json
import sys

from anki_tools.anki_client import _ac

GIU = 1                       # preset "Default" — Anki dựng sẵn, KHÔNG xoá được
GATHER_MOI_TRUOC = 2          # thẻ vừa thêm lên trước
KHONG_TRAN = 9999


def main():
    apply = "--apply" in sys.argv
    decks = _ac("deckNames")
    truoc = {}
    for d in decks:
        c = _ac("getDeckConfig", deck=d)
        truoc.setdefault((c["id"], c["name"]), []).append(d)

    print("=== TRƯỚC ===")
    for (i, n), ds in sorted(truoc.items()):
        so = sum(len(_ac("findCards", query=f'deck:"{d}"')) for d in ds)
        print(f"  preset {i} {n!r}: {len(ds)} deck, {so} thẻ")
    print("\nBản ghi để LÙI LẠI (chép vào thân commit):")
    print(json.dumps({f"{i}|{n}": {"decks": ds} for (i, n), ds in truoc.items()},
                     ensure_ascii=False)[:1500])

    if not apply:
        print("\n(NHÁP — chưa đụng gì. Chạy lại với --apply để làm thật.)")
        return

    # KHÔNG hỏi theo tên deck "Default": ở máy user deck đó tên "Mặc định",
    # AnkiConnect trả về False chứ không báo lỗi -> vỡ im lặng (bắt 23/08).
    # Hỏi qua một deck CHẮC CHẮN có và đang dùng preset cần sửa.
    deck_mau = next(d for (i, _n), ds in truoc.items() if i == GIU for d in ds)
    cfg = _ac("getDeckConfig", deck=deck_mau)
    assert cfg["id"] == GIU, f"deck {deck_mau} không dùng preset {GIU}"
    cfg["new"]["perDay"] = KHONG_TRAN
    cfg["newGatherPriority"] = GATHER_MOI_TRUOC
    _ac("saveDeckConfig", config=cfg)
    print(f"\n✓ Preset {GIU}: trần thẻ mới -> {KHONG_TRAN}, thứ tự -> thẻ mới thêm trước")

    _ac("setDeckConfigId", decks=decks, configId=GIU)
    print(f"✓ Đã chuyển {len(decks)} deck về preset {GIU}")

    for (i, n) in truoc:
        if i != GIU:
            _ac("removeDeckConfigId", configId=i)
            print(f"✓ Đã xoá preset {i} {n!r} (đang cai quản 0 thẻ)")

    print("\n=== SAU ===")
    sau = {}
    for d in decks:
        c = _ac("getDeckConfig", deck=d)
        sau.setdefault((c["id"], c["name"]), []).append(d)
    for (i, n), ds in sorted(sau.items()):
        c = _ac("getDeckConfig", deck=ds[0])
        print(f"  preset {i} {n!r}: {len(ds)} deck | trần thẻ mới "
              f"{c['new']['perDay']} | thứ tự {c['newGatherPriority']}")


if __name__ == "__main__":
    main()
