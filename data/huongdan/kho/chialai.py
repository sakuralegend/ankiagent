# -*- coding: utf-8 -*-
"""Chia lại các lô CHƯA soạn cho đều — chạy khi hàng đợi còn nhiều lô lẻ.

Vì sao cần: đo thật phiên 27/07 cho thấy **chi phí tính theo LÔ, không theo từ**.
Mỗi lô dù to hay nhỏ đều phải đọc lại spec, xem mẫu, tra từ điển, chạy soát —
phần cố định đó áp đảo:

    lô 15 từ -> 116-165K token ->  7,8-11,0K token/từ
    lô  6 từ -> 125K token     -> 20,9K token/từ
    lô  4 từ -> 107K token     -> 26,7K token/từ   (đắt gấp 3,4 lần)

Cách chia: mỗi topic tách thành `round(n/TRAN)` phần **đều nhau** thay vì cắt
đủ cỡ rồi bỏ mẩu thừa. 67 từ -> 14+13+13+13+14, chứ không phải 15+15+15+15+7.

--------------------------------------------------------------------- 28/07
**Nâng cỡ lô 16 -> 20, và BỎ HẲN việc gộp topic khác nhau.**

Cỡ 20 đã đo thật ở k49 (19 từ) + k50 (20 từ): 39 từ hết 75% hạn mức = 1,9%/từ,
so với 2,5%/từ của các phiên lô 15-17 từ. Rẻ hơn vì phần cố định (đọc spec, xem
mẫu, dựng khung) chia cho nhiều từ hơn. Không có dấu hiệu hụt hơi: đo độ dày thẻ
theo thứ tự soạn thì k50 phẳng lì (nửa đầu 5.874 / nửa sau 5.918), k49 tụt là do
nửa sau toàn trạng từ vốn ít chữ, không phải mỏi.

Nhưng **20 là mức nhắm, không phải khuôn ép** (user chốt 28/07: *"nếu từ khác
nhau quá, bạn đừng ngại cho riêng 1 lô, đừng ép phải khuôn cứng 20"*). Vì vậy
lô "gộp" trộn nhiều topic đã bị bỏ: nó tiết kiệm token bằng cách hi sinh đúng thứ
làm nên giá trị của một lô — **các từ trong lô phải cùng họ thì khối dùng chung
mới gánh được nhiều thẻ**. Topic nhỏ nay giữ nguyên thành lô riêng, dù chỉ 7 từ.
Chi phí mỗi từ của lô nhỏ cao gấp 3-4 lần, và đó là cái giá đã được cân nhắc
rồi chấp nhận, không phải sơ suất.

Lô ĐÃ SOẠN không bị đụng tới.

Chạy: python data/huongdan/kho/chialai.py [--apply]
"""
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TRAN = 20     # cỡ lô nhắm tới
TOI_DA = 22   # không lô nào vượt quá — lớn hơn thì agent dễ hụt hơi
SAN = 10      # chỉ để CẢNH BÁO khi in, không còn dùng để gộp


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

    # ------------------------------------------------------------ chốt chặn
    # Lô có `thucong` là lô ĐÃ GHÉP TAY THEO NGHĨA, không theo hậu tố. Chạy lại
    # file này sẽ gom hết từ của topic đó rồi chia lại bằng máy — xoá sạch công
    # ghép mà không báo gì. Đã suýt mất `language::grammar` và `numbers` (28/07).
    tay = [l for l in cho if l.get("thucong")]
    if tay and "--ep" not in sys.argv:
        print(f"DUNG: {len(tay)} lo da ghep tay theo nghia, chia lai bang may se xoa sach:")
        for l in tay:
            print(f"  {l['id']}  {l['topic']:22} {len(l['tu']):3}   [{l['thucong']}]")
        print("\nHau to KHONG phai ho hang voi hu tu va so tu — do la ly do chung"
              "\nduoc ghep tay. Chi thuc su muon xoa thi them --ep.")
        return

    # gom lại theo topic, GIỮ NGUYÊN thứ tự từ (đã sắp theo hậu tố ở xephangdoi.py)
    theo_topic = {}
    for l in cho:
        theo_topic.setdefault(l["topic"], []).extend(l["tu"])

    lo_moi = []
    for t in sorted(theo_topic):
        tu = theo_topic[t]
        # Chia đều quanh mức TRAN, KHÔNG cắt đủ cỡ rồi bỏ mẩu thừa.
        # `round` chứ không `ceil`: 22 từ -> MỘT lô 22, không phải 11+11.
        # Topic nhỏ hơn TRAN thì k=1 -> nguyên topic thành MỘT lô, dù chỉ 7 từ.
        # Không gộp sang topic khác: xem phần 28/07 ở đầu file.
        k = max(1, round(len(tu) / TRAN))
        while len(tu) / k > TOI_DA:
            k += 1
        lo_moi.extend((t, phan) for phan in chia_deu(tu, k))

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
