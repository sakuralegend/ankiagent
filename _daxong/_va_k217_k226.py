# -*- coding: utf-8 -*-
"""Vá sau đợt k217–k226 (24/11/2026, user duyệt từng việc). L2: chạy một lần.

Đề lọt trong đề (наврать, ель, из-за/вследствие), đề thiếu nghĩa có trong câu ví dụ
(набрать/набирать «tăng»), câu ví dụ gượng/thiếu nghĩa hay gặp, dịch lệch, Пасха/Евангелие
viết thường, gloss của từ khác (бомж, высыпаться), увольнять sót -н-. Mọi chỗ so bản cũ trước."""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
ROOT = ROOT if os.path.exists(os.path.join(ROOT, "bot.py")) else os.path.dirname(ROOT)
sys.path.insert(0, ROOT)
from anki_tools.anki_client import (doc_notes_cua_model, gan_tieng_vi_du, sync_now,   # noqa: E402
                                    sync_truoc_khi_ghi_lo, update_note_fields)
from anki_tools.backup import run_backup                                  # noqa: E402
from anki_tools.config import MODEL_NAME                                  # noqa: E402
from anki_tools.html_builder import dung_cloze, thay_vi_du                # noqa: E402

VI = {  # id: (cũ, mới)
    1795312472922: ("nói dối", "nói dối, bịa chuyện, nói sai"),
    1795336908040: ("cây thông, vân sam, cây linh sam", "cây vân sam, cây linh sam"),
    1795020154609: ("do", "vì, tại, do, từ đằng sau"),
    "вследствие": ("vì, bởi, do hậu quả của", "do, do hậu quả của"),
    1795358272495: ("bấm số, gõ, gom, thu được, tích luỹ, tuyển",
                    "bấm số, gõ, gom, thu được, tích luỹ, tăng, tuyển"),
    1795489416300: ("bấm số, gõ, gom, thu được, tích luỹ, tuyển",
                    "bấm số, gõ, gom, thu được, tích luỹ, tăng, tuyển"),
    1792083818951: ("thuốc lá", "điếu thuốc lá, thuốc lá"),
    1795240396806: ("tập dượt, rèn luyện", "tập luyện, rèn luyện"),
    1792084572811: ("đổi, thay, trao đổi (lấy cái khác)", "đổi, thay, trao đổi"),
}
CAU = {  # id: câu 3 mới
    1795489780437: ("Без <hl>зелени</hl> салат какой-то скучный.",
                    "Without <hl>greens</hl> the salad is kind of boring.",
                    "Không có <hl>rau thơm</hl>, món salad cứ nhạt nhẽo thế nào ấy."),
    1795489795568: ("Мне нужна рубашка из <hl>хлопка</hl>.", "I need a <hl>cotton</hl> shirt.",
                    "Tớ cần một cái áo sơ mi bằng <hl>vải bông</hl>."),
    1795489905619: ("Мы давно мечтаем о <hl>возрождении</hl> этого парка.",
                    "We've long dreamed of the <hl>revival</hl> of this park.",
                    "Bọn tớ từ lâu mơ về <hl>sự hồi sinh</hl> của công viên này."),
    1795489802731: ("Вся его куртка пахнет <hl>табаком</hl>.",
                    "His whole jacket smells of <hl>tobacco</hl>.",
                    "Cả cái áo khoác của anh ấy toàn mùi <hl>thuốc lá</hl>."),
    1795490238760: ("Я совсем не разбираюсь в корейской <hl>косметике</hl>.",
                    "I know nothing about Korean <hl>cosmetics</hl>.",
                    "Tôi chẳng hiểu gì về <hl>mỹ phẩm</hl> Hàn Quốc."),
    1795490429465: ("Опять получил <hl>тройку</hl> по химии, мама расстроится.",
                    "I got a <hl>C</hl> in chemistry again, Mum will be upset.",
                    "Lại bị <hl>điểm 3</hl> môn hoá, mẹ sẽ buồn lắm."),
    1795490437116: ("Мы <hl>приветствуем</hl> любую критику и новые идеи.",
                    "We <hl>welcome</hl> any criticism and new ideas.",
                    "Chúng tôi <hl>hoan nghênh</hl> mọi lời phê bình và ý tưởng mới."),
    1795489468495: ("Соседи хотят <hl>съехать</hl> до конца месяца.",
                    "The neighbours want to <hl>move out</hl> by the end of the month.",
                    "Hàng xóm muốn <hl>dọn đi</hl> trước cuối tháng."),
    1795489475906: ("Нам придётся <hl>съезжать</hl>, хозяин продаёт квартиру.",
                    "We'll have to <hl>move out</hl>, the landlord is selling the flat.",
                    "Bọn mình phải <hl>dọn đi</hl> thôi, chủ nhà bán căn hộ rồi."),
}
H = '<span class="hl">%s</span>'
THAY = {  # id: (ô, [(cũ, mới, số lần)])
    1795489853811: [(H % "пасху", H % "Пасху", 1), (H % "пасхой", H % "Пасхой", 1)],
    1795490209614: [(H % "евангелие", H % "Евангелие", 1), (H % "евангелий", H % "Евангелий", 1),
                    (H % "евангелии", H % "Евангелии", 1)],
    1795490565792: [(H % "chính thức", H % "trang trọng", 1)],
    1795490589918: [(H % "đá quý", H % "quý", 1)],
    1795336908040: [(H % "thông", H % "vân sam", 3)],
}
MEANING = {1795490143194: ["good catch", "eligible bachelor", "Prince Charming"],
           1795489644221: ["to spill out", "to trickle out", "to pour out"]}
HD = [('<span class="hd-piece">-воль-</span><span class="hd-gloss">TỰ DO — <i>вол-</i> của <b>во́ля</b>, л mềm trước я</span>',
       '<span class="hd-piece">-вольн-</span><span class="hd-gloss">TỰ DO — như <b>во́льный</b> tự do, cùng gốc <b>во́ля</b></span>'),
      ]
HD_UVOLIT = ('Cặp CHT: <b>увольня́ть</b> — đúng khuôn <b>позво́лить → позволя́ть</b>.',
             'Cặp CHT: <b>увольня́ть</b> — chèn thêm <b>н</b>, khác <b>позво́лить → позволя́ть</b>.')

notes = doc_notes_cua_model(MODEL_NAME)
kho = {n["noteId"]: {k: v["value"] for k, v in n["fields"].items()} for n in notes}
theo_chu = {f["WordClean"].strip(): i for i, f in kho.items()}
ghi = {}


def dat(nid, o, v):
    ghi.setdefault(nid, {})[o] = v


for k, (cu, moi) in VI.items():
    nid = theo_chu[k] if isinstance(k, str) else k
    assert kho[nid]["Vietnamese"] == cu, (k, kho[nid]["Vietnamese"])
    dat(nid, "Vietnamese", moi)
for nid, ds in THAY.items():
    h = kho[nid]["ExamplesHTML"]
    for cu, moi, so in ds:
        assert h.count(cu) == so, (nid, cu, h.count(cu))
        h = h.replace(cu, moi)
    dat(nid, "ExamplesHTML", h)
for nid, ds in MEANING.items():
    h = kho[nid]["Meaning"]
    for g in ds:
        assert h.count(f"<li>{g}</li>") == 1, (nid, g)
        h = h.replace(f"<li>{g}</li>", "")
    dat(nid, "Meaning", h)
u, u2 = 1795336363169, theo_chu["уволить"]
for nid, ds in ((u, HD), (u2, [HD_UVOLIT])):
    h = kho[nid]["HuongDan"]
    for cu, moi in ds:
        assert h.count(cu) == 1, (nid, cu)
        h = h.replace(cu, moi)
    dat(nid, "HuongDan", h)
for nid in CAU:
    assert len(re.findall(r"<details\b", kho[nid]["ExamplesHTML"])) == 3, nid
print("KHAN: mọi bản cũ khớp —", len(ghi) + len(CAU), "thẻ")
if "--apply" not in sys.argv:
    raise SystemExit
run_backup()
if not sync_truoc_khi_ghi_lo("vá k217-k226"):
    raise SystemExit("sync hỏng")
for nid, (ru, en, vi) in CAU.items():
    dat(nid, "ExamplesHTML", thay_vi_du(kho[nid]["ExamplesHTML"], 2, {"ru": ru, "en": en, "vi": vi}))
for nid, o in ghi.items():
    if "ExamplesHTML" in o:
        h = gan_tieng_vi_du(o["ExamplesHTML"])
        assert h.count("<audio") == 3 == h.count('class="nghe"'), nid
        f = kho[nid]
        o["ExamplesHTML"], o["ClozeHTML"] = h, dung_cloze(h, json.loads(f["GrammarJSON"]), f["WordClean"])
        assert o["ClozeHTML"], nid
    assert update_note_fields(nid, o), nid
    print("ok", kho[nid]["WordClean"], list(o))
print("sync:", sync_now())
