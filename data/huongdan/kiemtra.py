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
import json
import re
import sys
import urllib.request

ANKI = "http://127.0.0.1:8765"
NOUNS = r"d:\Desktop\ANKI\data\nouns.csv"
ACUTE = "\u0301"          # dấu trọng âm tổ hợp, đứng SAU nguyên âm
ZWSP = "\u200b"


def ac(action, **params):
    req = urllib.request.Request(
        ANKI, json.dumps({"action": action, "version": 6, "params": params}).encode())
    out = json.load(urllib.request.urlopen(req, timeout=180))
    if out.get("error"):
        raise RuntimeError(f"{action}: {out['error']}")
    return out["result"]


# Từ ĐỒNG TỰ: hai từ khác nhau viết giống hệt, từ điển chỉ giữ được một.
# Máy không thể phân biệt, nên phải miễn trừ TAY và ghi rõ lý do — một bộ soát
# kêu nhầm mãi thì rồi chính mình sẽ bỏ qua cả tiếng kêu thật.
MIEN_TRU = {
    "ви́на": "số nhiều của вино́ (rượu vang); từ điển chỉ có вина́ = lỗi lầm",
}


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
                chuan = nouns[b]
                # Từ điển KHÔNG ghi trọng âm cho nhiều tên riêng (Аме́рика, Кита́й,
                # Коре́я lưu trần). So với mục trần thì mọi dấu tôi đặt đều bị coi
                # là thừa -> báo nhầm hàng loạt. Không có dấu thì không so.
                if ACUTE not in chuan:
                    continue
                if token in MIEN_TRU:
                    continue
                if token.replace(ZWSP, "").lower().replace("ё", "е") != chuan.lower().replace("ё", "е"):
                    sai_trong_am.append((word, token, chuan))

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
