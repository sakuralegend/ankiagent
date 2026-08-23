# -*- coding: utf-8 -*-
"""VIỆC MỘT LẦN — chụp Лексический минимум của ros-edu.ru ra `data/rosedu_muc.json`.

QD-A (23/08/2026): lấy ẢNH CHỤP, KHÔNG cào lúc chạy.
Vì Лексический минимум là chuẩn ТРКИ **đã xuất bản** — nó không đổi. Cào lại mỗi
lần dùng chỉ thêm một chỗ hỏng im lặng trên VPS (bot sống ở đó, mạng sang Nga
chập chờn), đổi lại 0 lợi ích. 130 KB, bằng 1,6% `data/nouns.csv`.

Nguồn: https://www.ros-edu.ru/basic-dictionary — bảng từ nạp bằng AJAX vào `/380`.
Mức CỘNG DỒN: level_id=4 trả về cả A1+A2+B1+B2, nên chỉ cần gọi một mức là đủ;
mức thật của mỗi từ = SỐ NHỎ NHẤT trong `level_ids` của nó.

Chạy: python _va_tai_rosedu.py
Xong thì chuyển vào `_daxong/` NGAY trong cùng commit (L2).
"""
import json
import re
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

GOC = "https://www.ros-edu.ru"
MUC_ROI = 4          # B2 cộng dồn = phủ hết A1/A2/B1
MOI_TRANG = 40
DICH = "data/rosedu_muc.json"
UA = {"User-Agent": "Mozilla/5.0", "X-Requested-With": "XMLHttpRequest"}


def _post(**data):
    req = urllib.request.Request(f"{GOC}/380", data=urllib.parse.urlencode(data).encode(),
                                 headers=UA)
    return json.load(urllib.request.urlopen(req, timeout=60))


def trang(p):
    return _post(level_id=MUC_ROI, category_id=0, action="getPublications",
                 collection_id=0, page=p)


def main():
    dau = trang(1)
    tong = dau["count"]
    so_trang = -(-tong // MOI_TRANG)
    print(f"Nguồn khai {tong} từ, {so_trang} trang")
    with ThreadPoolExecutor(8) as ex:
        phan = list(ex.map(lambda p: trang(p)["data"], range(1, so_trang + 1)))
    dong = [r for tr in phan for r in tr]
    assert len(dong) == tong, f"tải về {len(dong)} != {tong} nguồn khai"

    # Tên chủ đề nằm trong HTML trang mẹ, không có trong JSON.
    html = urllib.request.urlopen(
        urllib.request.Request(f"{GOC}/basic-dictionary", headers=UA), timeout=60
    ).read().decode("utf-8")
    chu_de = {m[0]: m[1].strip() for m in
              re.findall(r'id="theme-id-(\d+)"[^>]*>([^<]*)<', html) if m[0] != "0"}
    print(f"{len(chu_de)} chủ đề")

    tu = []
    for r in dong:
        muc = [int(x) for x in r["level_ids"].split(",") if x.strip()]
        cat = [c.strip() for c in r["categories"].split(",") if c.strip()]
        if not muc:
            continue
        tu.append([r["word_rus"].strip(), min(muc), cat])

    ra = {
        "_nguon": f"{GOC}/basic-dictionary — Лексический минимум ТРКИ, chụp 23/08/2026",
        "_cot": "tu = [chữ Nga CÓ DẤU NHẤN, mức nhỏ nhất 1=A1 2=A2 3=B1 4=B2, [id chủ đề]]",
        "chu_de": chu_de,
        "tu": tu,
    }
    with open(DICH, "w", encoding="utf-8") as f:
        json.dump(ra, f, ensure_ascii=False, separators=(",", ":"))
    import os
    print(f"✓ {DICH}: {len(tu)} từ, {os.path.getsize(DICH) / 1024:.0f} KB")
    for m, ten in [(1, "A1"), (2, "A2"), (3, "B1"), (4, "B2")]:
        print(f"   {ten}: {sum(1 for t in tu if t[1] <= m)} từ (cộng dồn)")


if __name__ == "__main__":
    main()
