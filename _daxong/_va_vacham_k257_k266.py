# -*- coding: utf-8 -*-
"""Bốn va chạm nghĩa đợt k257–k266, user duyệt 25/11/2026. L2: chạy một lần. File lô sửa kèm cho `nap --tatca` khớp."""
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
from anki_tools.config import MODEL_NAME                                  # noqa: E402
from anki_tools.html_builder import dung_cloze, thay_vi_du                # noqa: E402

VI = {"активный": ("năng động", "tích cực, năng động"),
      "демократичный": ("dân chủ, bình dân, giản dị, gần gũi, phải chăng", "bình dân, giản dị, gần gũi, phải chăng"),
      "варенный": ("luộc, nấu chín", "được luộc, được nấu"),
      "отчего-то": ("không hiểu sao, chẳng rõ vì sao, vì lý do nào đó", "chẳng rõ vì sao, chẳng hiểu sao")}
CAU = {("демократичный", 2): ("Она очень <hl>демократичная</hl>, общается со всеми на равных.",
                              "She's very <hl>down-to-earth</hl>, she talks to everyone as an equal.",
                              "Cô ấy rất <hl>gần gũi</hl>, nói chuyện ngang hàng với mọi người."),
       ("отчего-то", 1): (None, None, "<hl>Chẳng hiểu sao</hl> hôm nay tôi buồn suốt cả ngày."),
       ("отчего-то", 3): (None, None, "<hl>Chẳng hiểu sao</hl> điện thoại không sạc được, lạ thật."),
       ("варенный", 1): (None, None, "Bữa tối có khoai tây <hl>được luộc</hl> nguyên vỏ."),
       ("варенный", 2): (None, None, "Chúng tôi ăn bắp <hl>được luộc</hl> trong nước muối."),
       ("варенный", 3): (None, None, "Bà dọn ra trứng <hl>được luộc</hl> chín kỹ.")}
K = os.path.join(ROOT, "data", "huongdan", "kho")
TEP = [("k93_qualities.py", '    # Bỏ "tích cực" (trùng положительный k53, cùng adj); gloss chỉ "active".\n'
        '    # Giữ "năng động" — lô k99 tự rút phía энергичный.\n    "активный": "năng động",',
        '    # «tích cực» user duyệt 25/11: «năng động» trơ nằm gọn trong динамичный (k264).\n    "активный": "tích cực, năng động",'),
       ("k21_life-food.py", "V['варенный'] = 'luộc, nấu chín'", "V['варенный'] = 'được luộc, được nấu'"),
       ("k258_concepts-state.py", '"демократичный": "dân chủ, bình dân', '"демократичный": "bình dân'),
       ("k261_language-communication.py", "\nV = {\n", '\nV = {\n    "отчего-то": "chẳng rõ vì sao, chẳng hiểu sao",\n')]

kho = {n["fields"]["WordClean"]["value"].strip(): (n["noteId"], {k: v["value"] for k, v in n["fields"].items()})
       for n in doc_notes_cua_model(MODEL_NAME)}
ghi = {}
for w, (cu, moi) in VI.items():
    assert kho[w][1]["Vietnamese"] == cu, (w, kho[w][1]["Vietnamese"])
    ghi[w] = {"Vietnamese": moi}
for (w, i), moi in CAU.items():
    h = ghi[w].get("ExamplesHTML", kho[w][1]["ExamplesHTML"])
    k = re.findall(r"<details\b.*?</details>", h, re.S)[i - 1]
    cu = [re.sub(r'<span class="hl">(.*?)</span>', r"<hl>\1</hl>", re.search(p, k, re.S).group(1)) for p in (
        r'<div class="ex-ru">(.*?)(?:<span class="nghe"|</div>)', r'<div class="ex-en">(.*?)</div>',
        r'<span class="vi-text">(.*?)</span></div>')]
    ghi[w]["ExamplesHTML"] = thay_vi_du(h, i - 1, dict(zip(("ru", "en", "vi"), [m or c for m, c in zip(moi, cu)])))
for t, cu, _moi in TEP:
    assert io.open(os.path.join(K, t), encoding="utf-8").read().count(cu) == 1, t
print("KHAN khớp")
if "--apply" not in sys.argv:
    raise SystemExit
if not sync_truoc_khi_ghi_lo("va chạm k257-k266"):
    raise SystemExit("sync hỏng")
for w, o in ghi.items():
    nid, f = kho[w]
    if "ExamplesHTML" in o:
        o["ExamplesHTML"] = gan_tieng_vi_du(o["ExamplesHTML"])
        assert o["ExamplesHTML"].count("<audio") == 3, w
        o["ClozeHTML"] = dung_cloze(o["ExamplesHTML"], json.loads(f["GrammarJSON"]), w)
    assert update_note_fields(nid, o), w
    print("ok", w, list(o), bool(o.get("ClozeHTML", 1)), bool(f["ClozeHTML"]))
for t, cu, moi in TEP:
    p = os.path.join(K, t)
    s = io.open(p, encoding="utf-8").read().replace(cu, moi)
    io.open(p, "w", encoding="utf-8", newline="\n").write(s)
print("sync:", sync_now())
