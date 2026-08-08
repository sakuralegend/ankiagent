# -*- coding: utf-8 -*-
"""SOÁT nội dung field `HuongDan` bằng từ điển offline, thay vì bắt user tin.

Vì sao có file này: user học từ đầu, tự nói *"tôi không đủ kiến thức để kiểm tra
được độ tin cậy"*. Nên phần nào máy soát được thì phải để máy soát.

Soát hai thứ trên MỌI từ Nga in đậm trong khối "Họ hàng" (.hd-fam):
  1. Từ đó có THẬT không (đối chiếu data/nouns.csv — 26.983 danh từ).
  2. TRỌNG ÂM đặt đúng chỗ chưa (cột `accented` của từ điển là chuẩn).

⚠️ GIỚI HẠN PHẢI BIẾT: nouns.csv chỉ có DANH TỪ. Động từ/tính từ/trạng từ không
tra được, script báo "khong tra duoc" chứ KHÔNG phải "đúng". Đừng đọc nhầm.

🔴 **PHẢI ĐỌC BẰNG MẮT danh sách "khong tra duoc"** — đó không phải rác. Nó đã lộ
ra hai từ bịa sai dạng mà máy không cách nào bắt được: `мо́лодый` (đúng: молодо́й)
và `ра́дый` (không tồn tại trong tiếng Nga chuẩn). Cứ thấy tính từ trông lạ trong
danh sách đó thì kiểm lại thủ công trước khi báo là xong.

Chạy: python data/huongdan/kiemtra.py
"""
import csv
import io
import re
import sys
from pathlib import Path

# 3 dòng bootstrap: file này chạy thẳng bằng `python data/huongdan/kiemtra.py`
# nên gốc repo chưa có trong sys.path.
GOC = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(GOC))
sys.path.insert(0, str(GOC / "data" / "huongdan" / "kho"))

from anki_tools import goi_anki                                     # noqa: E402
from mientru import MIEN_TRU                                         # noqa: E402
from soatlo import lech_trong_am                                     # noqa: E402

NOUNS = Path(__file__).resolve().parent.parent / "nouns.csv"
ACUTE = "\u0301"          # dấu trọng âm tổ hợp, đứng SAU nguyên âm
ZWSP = "\u200b"


def ac(action, **params):
    """Vỏ mỏng quanh CỬA DUY NHẤT `anki_client` (L1) — giữ tên `ac` để ruột file
    không đổi. Trước 08/08 file này tự mở cổng AnkiConnect riêng; miễn trừ trong
    `soat_baseline.json` hẹn trả "sau 61 lô" và kho đóng 66/66 nên hạn đã tới."""
    return goi_anki(action, timeout=180, **params)


def bare(w):
    """Bỏ trọng âm + zero-width, về dạng tra cứu."""
    return w.replace(ACUTE, "").replace(ZWSP, "").replace("'", "").lower().replace("ё", "е")


def load_nouns():
    """bare -> dạng có trọng âm (từ điển ghi trọng âm bằng dấu ' SAU nguyên âm)."""
    d = {}
    with io.open(NOUNS, encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            b = (row.get("bare") or "").strip().lower().replace("ё", "е")
            acc = (row.get("accented") or "").strip()
            if b and acc and b not in d:
                d[b] = acc.replace("'", ACUTE)
    return d


def main():
    nouns = load_nouns()
    print(f"tu dien: {len(nouns)} danh tu\n")

    note_ids = ac("findNotes", query=r'note:RU_Word HuongDan:*hd-sec*')
    notes = ac("notesInfo", notes=note_ids)
    print(f"the kieu moi: {len(notes)}\n")

    sai_trong_am, khong_co, khong_tra_duoc = [], [], set()
    for n in notes:
        word = n["fields"]["WordClean"]["value"]
        html = n["fields"]["HuongDan"]["value"]
        # Soát TOÀN BỘ field, không chỉ khối Họ hàng. Bản đầu chỉ soát .hd-fam
        # nên bỏ lọt mọi từ Nga nằm trong phần "Cách nhớ" và ô cảnh báo — mà đó
        # cũng là chỗ tôi viết từ ra, cũng sai được y như vậy.
        for block in [html]:
            for m in re.findall(r"<b>(.*?)</b>", block):
                token = re.sub(r"<[^>]+>", "", m).strip()
                if not re.fullmatch(r"[А-Яа-яЁё\u0301\u200b-]+", token) or "-" in token:
                    continue          # bỏ phụ tố kiểu -ец, -ка
                b = bare(token)
                if b not in nouns:
                    khong_tra_duoc.add(b)
                    continue
                # Luật so nằm ở MỘT chỗ (`soatlo.lech_trong_am`): file này và
                # `congcu.py soat` từng giữ hai bản lệch nhau, và bản thiếu thì
                # kêu oan — đúng lý do `MIEN_TRU` phải gộp về một cửa (QD-03).
                if lech_trong_am(token, nouns[b]):
                    sai_trong_am.append((word, token, nouns[b]))

    print("=== TRONG AM LECH so voi tu dien ===")
    if not sai_trong_am:
        print("  (khong co)")
    seen = set()
    for w, mine, ref in sai_trong_am:
        key = (mine, ref)
        if key in seen:
            continue
        seen.add(key)
        print(f"  the {w:16s} toi viet {mine:20s} tu dien {ref}")

    # Bỏ mảnh phụ tố in đậm (ец, ский, ча…) khỏi danh sách phải đọc bằng mắt —
    # chúng luôn "không tra được" và làm loãng danh sách tới mức không ai đọc nữa.
    dai = sorted(w for w in khong_tra_duoc if len(w) >= 4)
    print(f"\n=== PHAI DOC BANG MAT: {len(dai)} tu (>=4 chu, khong co trong tu dien danh tu) ===")
    print("  " + ", ".join(dai))
    print(f"\n(bo qua {len(khong_tra_duoc) - len(dai)} manh phu to ngan)")
    print("⚠️ 'Khong tra duoc' KHONG co nghia la sai — chi la nouns.csv chi chua DANH TU.")
    print("   Nhung tinh tu/dong tu trong la trong danh sach nay thi PHAI kiem tay.")


if __name__ == "__main__":
    main()
