# -*- coding: utf-8 -*-
"""VIỆC MỘT LẦN (18/11/2026) — dựng `data/sach_b2.json`: danh sách chờ B1→B2.

Nguồn (user chốt 18/11, đo đối chiếu trong commit):
- Sách *Лексический минимум по РКИ. Второй сертификационный уровень* (Златоуст 2014,
  5-е изд., МГУ, thuộc bộ tài liệu chính thức của hệ thống thi ТРКИ). Sách CỘNG DỒN:
  chứa 2 194/2 325 mục sách B1 làm mục riêng, 116 mục nữa gộp trong mục khác
  (trạng từ -о nằm trong tính từ), chỉ 8 từ vắng hẳn ⇒ cộng tay 8 từ đó (`THEM8`).
- Sách B1 (Первый уровень, 7-е изд. 2014) CHỈ dùng để gắn nhãn B1 ⇒ học trước.
- Thứ tự trong mỗi mức: hay NÓI trước (phụ đề OpenSubtitles `ru_50k.txt`, quy về
  từ gốc bằng bảng dạng của OpenRussian), rơi về tần suất viết (Ляшевская–Шаров
  `freqrnc2011.csv`). Cặp thể lấy hạng tốt nhất của cặp ⇒ đứng liền nhau.
Vì sao KHÔNG ros-edu (`data/rosedu_muc.json`): thiếu thể hoàn thành của động từ
(có `принимать`, không có `принять`) — sách ghi đủ cặp. Vì sao không thuần tần suất:
phần B1 là nền đề thi vào đại học Nga; tần suất còn đánh thấp đồ vật hằng ngày.

Đầu vào KHÔNG nằm trong repo (sách có bản quyền, CSV 22 MB) — tải lại khi cần:
  B2 PDF: plus.ac.at/wp-content/uploads/2021/06/Leksicheskii_minimum_po_russkomu_iazyku_kak_inostrannomu_2_uroven.pdf
  B1 PDF: portal.tpu.ru/SHARED/k/KLN/Studywork/studywork/Лексический минимум В1.pdf
  rồi `pdftotext -enc UTF-8 -layout` (B1: trang 11–154) · github.com/Badestrand/russian-dictionary
  (4 CSV) · github.com/hermitdave/FrequencyWords content/2018/ru/ru_50k.txt · dict.ruslang.ru/Freq2011.zip
Chạy:  python _daxong/_va_lap_ds_b2.py <thư mục chứa các file trên>
"""
import collections
import csv
import json
import os
import re
import sys

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, GOC)
from anki_tools.anki_client import get_known_words  # noqa: E402

THEM8 = ["мобильный", "пицца", "менеджер", "мюзикл", "бейсбол", "фигурное катание",
         "гимнастика", "покормить"]
# user duyệt 18/11: bỏ vật/tổ chức đã không còn; GIỮ từ lịch sử–chính trị (советский…)
LOI_THOI = {"видеомагнитофон", "дискета", "кассета", "гастроном", "бандероль",
            "милиция", "милиционер"}
# sửa tay sau khi đọc PDF: mảnh chữ do ngắt dòng / từ điển song ngữ (như lần A2)
RAC = {"заброни", "пожало", "пере", "ницы", "полюбо", "почув", "выдадим", "тельно",
       "петрушку", "политическая", "значит", "англо-русский", "испанско-русский",
       "китайско-русский", "немецко-русский", "французско-русский"}
# dạng NGẮN sách ghi riêng — thẻ là dạng đầy đủ, Hướng dẫn nhấn dạng ngắn (nếp lô A2)
NGAN = {"виден": "видный", "виноват": "виноватый", "доволен": "довольный",
        "похож": "похожий", "убеждён": "убеждённый", "достоин": "достойный",
        "обязан": "обязанный"}
CAT = (r" нсв| св\b| см\.|;|,| \+| \(| —| ж\.р| м\.р| ср\.р| с\.р| только| мн\.ч| ед\.ч"
       r"| I\b| II\b| кр\.ф| сравн| разг| [а-яё]+\?")


def khoa(x):
    x = re.sub(r"[\s\- ]", "", x.lower().replace("ё", "е").replace("'", "").replace("́", ""))
    return re.sub(r"(ть|ться|ти|тись|чь|чься)(н?св)$", r"\1", x)


def doc_sach(fn, a=0, b=10 ** 9):
    """-> ({khoá: chữ}, [(khoá chưa HT, khoá HT)]). Mục từ = dòng sát lề trái."""
    out, cap = {}, []
    L = open(fn, encoding="utf-8").read().splitlines()
    for i, ln in enumerate(L):
        if i < a or i > b or not ln or ln[0] == " " or not re.match(r"[А-Яа-яЁё]", ln) \
                or ln.startswith("Лексический минимум"):
            continue
        left = re.split(r"\s{2,}", ln)[0]
        if re.search(r"[а-яё]-$", left) and i + 1 < len(L):       # từ bị ngắt dòng
            left = left[:-1] + re.split(r"\s{2,}", L[i + 1].strip())[0]
        w = re.split(CAT, left)[0].strip()
        if re.fullmatch(r"[А-Яа-яЁё\- ]+", w) and not w.endswith("-") \
                and w not in ("нсв", "св") and (len(w) > 1 or w in "вкиоуяс"):
            out.setdefault(khoa(w), w)
            for p in re.findall(r"— ([а-яё\-]+)(?= \(| св|$)", left):
                out.setdefault(khoa(p), p)
                cap.append((khoa(w), khoa(p)))
    return out, cap


def main(D):
    b2, cap2 = doc_sach(f"{D}/b2_layout.txt", 405, 7880)   # Часть I của sách B2
    b1, cap1 = doc_sach(f"{D}/b1_layout.txt")
    tat = dict(b2)
    for w in THEM8:
        tat.setdefault(khoa(w), w)
    da = get_known_words()
    if da is None:
        sys.exit("AnkiConnect lỗi — KHÔNG được coi là kho trống (sẽ ra danh sách sai)")
    da = {khoa(x) for x in da}

    orr, f2l = set(), collections.defaultdict(set)    # OpenRussian: có trang + dạng -> gốc
    for fn in ("nouns", "verbs", "adjectives", "others"):
        with open(f"{D}/{fn}.csv", encoding="utf-8") as fh:
            r = csv.reader(fh, delimiter="\t")
            hdr = next(r)
            for row in r:
                if not row:
                    continue
                orr.add(khoa(row[0]))
                for h, v in zip(hdr, row):
                    if h.startswith(("sg_", "pl_", "short_")):
                        for p in re.split(r"[,;/]", v):
                            if khoa(p):
                                f2l[khoa(p)].add(khoa(row[0]))

    txt = open(f"{D}/b2_layout.txt", encoding="utf-8").read()
    con, ghi = {}, {}
    for k, w in tat.items():
        if k in da or " " in w.strip() or w in RAC or w in LOI_THOI:
            continue
        if f2l.get(k) and (f2l[k] & da) and k not in orr:
            continue                                   # dạng biến đổi của từ đã có thẻ
        if w in NGAN:
            if khoa(NGAN[w]) in da:
                continue
            k, ghi[khoa(NGAN[w])] = khoa(NGAN[w]), f"ngan:{w}"
            w = NGAN[w]
        elif k not in orr:                             # sách ghi số nhiều -> thẻ số ít
            m = re.search(r"(?m)^" + re.escape(w) + r" мн\.ч\.[^\n]*?ед\. ?ч\. ([а-яё]+)", txt)
            if m:
                if khoa(m.group(1)) in da:
                    continue
                k, w = khoa(m.group(1)), m.group(1)
            else:
                ghi[k] = "khong-OR"                    # OpenRussian không có trang
        con[k] = w

    fl = collections.Counter()
    for line in open(f"{D}/ru_50k.txt", encoding="utf-8"):
        w, c = line.split()
        w = khoa(w)
        L = f2l.get(w) or ({w} if w in orr else set())
        tg = [w] if w in L else sorted(L)
        for x in tg:
            fl[x] += int(c) / len(tg)
    noi = {w: i + 1 for i, (w, _) in enumerate(fl.most_common())}
    rnc = collections.Counter()
    for i, line in enumerate(open(f"{D}/freqrnc2011.csv", encoding="utf-8")):
        if i:
            p = line.split("\t")
            rnc[khoa(p[0])] += float(p[2])
    viet = {w: i + 1 for i, (w, _) in enumerate(rnc.most_common())}

    def hang(k):
        return min(noi.get(k, 99999), int(viet.get(k, 99999) * 1.5))

    nhom = {k: k for k in con}
    for a, b in cap1 + cap2:
        if a in con and b in con:
            nhom[b] = nhom[a]
    hn = collections.defaultdict(lambda: 99999)
    for k in con:
        hn[nhom[k]] = min(hn[nhom[k]], hang(k))
    # cả cặp chung MỘT mức (B1 nếu một vế B1) — tách mức là tách lô (`стать` ↔ `становиться`)
    b1nhom = {nhom[k] for k, w in con.items() if k in b1 or w in THEM8}
    ds = [[w, "B1" if nhom[k] in b1nhom else "B2", hn[nhom[k]],
           "" if nhom[k] == k and not any(nhom[o] == k for o in con if o != k) else con[nhom[k]],
           ghi.get(k, "")] for k, w in con.items()]
    ds.sort(key=lambda r: (r[1] != "B1", r[2], r[3] or r[0], r[0]))
    out = {
        "_nguon": "Лексический минимум ТРКИ-2 (Златоуст 2014) + 8 từ chỉ có ở sách B1; "
                  "dựng 18/11/2026 bằng _daxong/_va_lap_ds_b2.py",
        "_cot": "tu = [từ, mức B1|B2, hạng hay nói (nhỏ = hay gặp), cặp thể (từ đầu cặp, '' = "
                "không cặp), ghi chú: 'ngan:X' = sách ghi dạng ngắn X · 'khong-OR' = "
                "OpenRussian không có trang]. ĐÃ XẾP đúng thứ tự học. Từ đã có thẻ thì bỏ qua "
                "khi lấy đợt — trạng thái nằm ở Anki, file này không ghi.",
        "_bo": {"loi_thoi": sorted(LOI_THOI), "cum_nhieu_chu": "bỏ như lần A2"},
        "tu": ds,
    }
    with open(os.path.join(GOC, "data", "sach_b2.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=0)
    print(f"{len(ds)} từ | B1 {sum(r[1] == 'B1' for r in ds)} | B2 {sum(r[1] == 'B2' for r in ds)}"
          f" | ngan {sum(r[4].startswith('ngan') for r in ds)} | khong-OR {sum(r[4] == 'khong-OR' for r in ds)}")


if __name__ == "__main__":
    main(sys.argv[1])
