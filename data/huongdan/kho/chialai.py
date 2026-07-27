# -*- coding: utf-8 -*-
"""Chia lại các lô CHƯA soạn cho đều — chạy khi hàng đợi còn nhiều lô lẻ.

Vì sao cần: đo thật phiên 27/07 cho thấy **chi phí tính theo LÔ, không theo từ**.
Mỗi lô dù to hay nhỏ đều phải đọc lại spec, xem mẫu, tra từ điển, chạy soát —
phần cố định đó áp đảo:

    lô 15 từ -> 116-165K token ->  7,8-11,0K token/từ
    lô  6 từ -> 125K token     -> 20,9K token/từ
    lô  4 từ -> 107K token     -> 26,7K token/từ   (đắt gấp 3,4 lần)

Cách chia: mỗi topic tách thành `ceil(n/16)` phần **đều nhau** thay vì cắt 15
rồi bỏ mẩu thừa. 67 từ -> 14+13+13+13+14, chứ không phải 15+15+15+15+7.
Mẩu dưới 10 từ của các topic nhỏ được gom lại thành lô "gộp" — mất một chút
tính thuần họ từ, nhưng rẻ hơn nhiều so với chạy một lô 4 từ riêng.

Lô ĐÃ SOẠN không bị đụng tới.

Chạy: python data/huongdan/kho/chialai.py [--apply]
"""
import io
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TRAN = 16     # cỡ lô nhắm tới
TOI_DA = 18   # không lô nào vượt quá — lớn hơn thì agent dễ hụt hơi
SAN = 10    # dưới mức này thì gom sang lô "gộp"


def chia_deu(xs, k):
    """Chia list thành k phần chênh nhau nhiều nhất 1 phần tử."""
    n, out, i = len(xs), [], 0
    for j in range(k):
        co = n // k + (1 if j < n % k else 0)
        out.append(xs[i:i + co])
        i += co
    return out


def main():
    apply = "--apply" in sys.argv
    q = json.load(io.open(os.path.join(HERE, "hangdoi.json"), encoding="utf-8"))
    xong = [l for l in q["lo"] if l["trangthai"] == "xong"]
    cho = [l for l in q["lo"] if l["trangthai"] != "xong"]

    # gom lại theo topic, GIỮ NGUYÊN thứ tự từ (đã sắp theo hậu tố ở xephangdoi.py)
    theo_topic = {}
    for l in cho:
        theo_topic.setdefault(l["topic"], []).extend(l["tu"])

    lo_moi, le = [], []
    for t in sorted(theo_topic):
        tu = theo_topic[t]
        if len(tu) < SAN:
            le.append((t, tu))       # cả topic ít từ -> để dành gộp
            continue
        # Chia đều quanh mức TRAN, KHÔNG cắt 16 rồi bỏ mẩu thừa.
        # `round` chứ không `ceil`: 17 từ -> MỘT lô 17, không phải 9+8.
        # Một topic thuần chia đều thì mọi mẩu đều hợp lệ, kể cả khi nhỏ hơn SAN —
        # SAN chỉ dùng để quyết định có GỘP TOPIC KHÁC vào hay không.
        k = max(1, round(len(tu) / TRAN))
        while len(tu) / k > TOI_DA:
            k += 1
        lo_moi.extend((t, phan) for phan in chia_deu(tu, k))

    # mẩu lẻ của các topic nhỏ -> gom thành lô "gộp"
    if le:
        goi, dem = [], 0
        for t, phan in le:
            if dem + len(phan) > TRAN and goi:
                lo_moi.append(("gop:" + "+".join(sorted({x for x, _ in goi})),
                               [w for _, p in goi for w in p]))
                goi, dem = [], 0
            goi.append((t, phan))
            dem += len(phan)
        if goi:
            lo_moi.append(("gop:" + "+".join(sorted({x for x, _ in goi})),
                           [w for _, p in goi for w in p]))

    i = len(xong)
    ra = list(xong)
    for topic, tu in lo_moi:
        i += 1
        ra.append({"id": f"k{i:02d}", "topic": topic, "tu": tu,
                   "trangthai": "cho", "file": None})

    cu = sum(len(l["tu"]) for l in cho)
    moi = sum(len(l["tu"]) for l in ra if l["trangthai"] == "cho")
    print(f"lo chua soan: {len(cho)} -> {len(ra) - len(xong)}   (tu: {cu} -> {moi})")
    nho = [l for l in ra if l["trangthai"] == "cho" and len(l["tu"]) < SAN]
    print(f"lo con duoi {SAN} tu: {len(nho)}")
    for l in ra[len(xong):]:
        print(f"  {l['id']}  {l['topic']:34s} {len(l['tu']):3d}")

    assert cu == moi, "MAT TU khi chia lai!"
    if apply:
        q["lo"] = ra
        q["tong_lo"] = len(ra)
        io.open(os.path.join(HERE, "hangdoi.json"), "w", encoding="utf-8").write(
            json.dumps(q, ensure_ascii=False, indent=1))
        print("da ghi hangdoi.json")
    else:
        print("(chua ghi — them --apply)")


if __name__ == "__main__":
    main()
