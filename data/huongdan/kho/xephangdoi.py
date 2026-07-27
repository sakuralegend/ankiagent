# -*- coding: utf-8 -*-
"""Xếp 703 từ còn lại thành hàng đợi các lô — CHẠY MỘT LẦN, rồi thôi.

Vì sao có file này: soạn 703 từ không thể xong trong một phiên chat. Trạng thái
phải nằm TRÊN ĐĨA chứ không nằm trong đầu tôi, để phiên sau đọc `hangdoi.json`
là biết chạy tiếp từ đâu, không phải dò lại.

Cách chia lô — theo README §3, gom theo HỌ TỪ chứ không chia đều:
  * khoá chính: topic (cùng chủ đề thì cùng trường nghĩa)
  * khoá phụ: TỪ VIẾT NGƯỢC — thủ thuật rẻ mà hiệu quả, vì tiếng Nga phái sinh
    bằng HẬU TỐ. Sắp xếp ngược thì -ение, -ость, -ский, -тель tự động nằm liền
    nhau, và một khối giải thích hệ thống dùng chung được cho cả cụm.

Chạy: python data/huongdan/kho/xephangdoi.py
"""
import io
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
CO = 15  # từ mỗi lô


def bare(w):
    return w.replace("́", "").replace("​", "").lower()


def main():
    words = json.load(io.open(os.path.join(HERE, "tudien.json"), encoding="utf-8"))
    # ngược chuỗi -> cùng hậu tố thì cạnh nhau
    words.sort(key=lambda x: (x["topic"], bare(x["wc"])[::-1]))

    lo, i = [], 0
    for t in sorted({w["topic"] for w in words}):
        nhom = [w for w in words if w["topic"] == t]
        for k in range(0, len(nhom), CO):
            i += 1
            lo.append({
                "id": f"k{i:02d}",
                "topic": t,
                "tu": [w["wc"] for w in nhom[k:k + CO]],
                "trangthai": "cho",   # cho | xong
                "file": None,
            })

    out = {"tong_tu": len(words), "tong_lo": len(lo), "lo": lo}
    io.open(os.path.join(HERE, "hangdoi.json"), "w", encoding="utf-8").write(
        json.dumps(out, ensure_ascii=False, indent=1))
    print(f"{len(lo)} lo / {len(words)} tu")
    for l in lo:
        print(f"  {l['id']}  {l['topic']:26s} {len(l['tu'])}")


if __name__ == "__main__":
    main()
