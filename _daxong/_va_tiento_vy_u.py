# -*- coding: utf-8 -*-
"""Chú thích вы-/у- cho 28 thẻ chuyển động (24/11/2026, user DUYỆT bảng). L2: chạy một lần.

User lẫn hai tiền tố vì đề đều đọc ra «đi khỏi». Đề chia hai khúc: chung (cùng hành động, chỉ khác
«ra»/«đi») + ngoặc, rồi nghĩa riêng; hai thể một dãy. «lúc xuất phát» chỉ ở cặp TỰ MÌNH đi.
угнать/угонять cố ý chừa. Dịch ví dụ: у- không được dịch «ra», вы- dịch «xuất phát/ra» cho khớp đề.
выехать câu 3 dùng mệnh lệnh của выезжать (Выезжай) -> Выедем."""
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
from anki_tools.html_builder import apply_hl, dung_cloze, thay_vi_du      # noqa: E402

X, R, U = "(ra ngoài, lúc xuất phát)", "(ra ngoài)", "(đi mất, không còn ở đây)"
VI = {
    "выйти выходить": f"đi ra, bước ra {X}, xuống xe, ra mắt, được xuất bản",
    "выехать выезжать": f"đi ra bằng xe, lái xe ra {X}",
    "вылететь вылетать": f"bay ra {X}, cất cánh, khởi hành, lao ra",
    "вывести выводить": f"dẫn ra, dắt ra, đưa ra {R}, rút ra",
    "вывезти вывозить": f"chở ra, đưa ra khỏi {R}",
    "вынести выносить": f"mang ra, đem ra, khiêng ra {R}, đưa ra, chịu đựng, chịu nổi",
    "выгнать выгонять": f"đuổi ra, xua ra, lùa ra {R}, tống cổ",
    "уйти уходить": f"rời đi, bỏ đi {U}, nghỉ việc",
    "уехать уезжать": f"đi khỏi bằng xe, lái xe đi {U}",
    "улететь улетать": f"bay đi {U}, bay mất",
    "увести уводить": f"dẫn đi, dắt đi, đưa đi {U}, cuỗm",
    "увезти увозить": f"chở đi, đưa đi bằng xe {U}",
    "унести уносить": f"mang đi, đem đi {U}, cuốn đi",
    "убежать убегать": f"chạy đi, bỏ chạy, trốn thoát {U}, trào ra",
}
DICH = {  # từ: {câu số: dịch Việt}
    "выйти": {1: "Tớ sắp [đi ra] khỏi nhà rồi, đợi tớ năm phút nhé."},
    "выходить": {1: "Tớ đang mang giày và chuẩn bị [đi ra] khỏi nhà đây."},
    "уйти": {3: "Nếu thời tiết xấu đi, chúng ta sẽ phải [rời đi] khỏi bãi biển gấp."},
    "уходить": {1: "Đến lúc tớ phải [rời đi] rồi, mai đi làm sớm.",
                2: "Xin lỗi, nhưng tôi [rời đi] về nhà đây.",
                3: "Lần nào cô ấy cũng buồn bã [bỏ đi] mà không nói một lời."},
    "выехать": {1: "Tôi sẽ [xuất phát] sáng sớm để không bị tắc đường.",
                2: "Anh ấy đã [xuất phát] cách đây một tiếng, sắp tới rồi."},
    "выезжать": {1: "Ngày nào tôi cũng [xuất phát] lúc bảy giờ sáng.",
                 2: "Trước đây cô ấy chỉ [lái xe ra] khỏi thành phố vào mùa hè.",
                 3: "Đừng [xuất phát] vào thứ Sáu, ai cũng mắc kẹt trong tắc đường."},
    "уехать": {2: "Chú mèo con đã lớn và đã [rời đi] về nhà chủ mới rồi.",
               3: "Sáng mai bọn tớ sẽ [đi khỏi] đây, đi nghỉ ở biển."},
    "уезжать": {2: "Lần nào cô ấy cũng [rời đi] trong nước mắt vì những chuyện nhỏ nhặt.",
                3: "Chúng tôi [đi khỏi] nhà vườn về nhà vì thời tiết xấu đi."},
    "улететь": {2: "Bố mẹ mình đã [bay đi] Sochi tối qua."},
    "улетать": {1: "Chim mùa thu nào cũng [bay đi] phương nam.",
                2: "Tháng nào anh ấy cũng [bay đi] Moskva vì công việc.",
                3: "Đừng [bay đi] sớm thế, ngồi với bọn mình thêm chút."},
    "увести": {1: "Tôi sẽ [dẫn] anh ấy [đi] vào bếp, còn cậu giấu quà đi.",
               2: "Người ta [dẫn] anh ấy [đi] sang phòng khác và hỏi rất lâu.",
               3: "[Dẫn] mấy đứa nhỏ [đi] khỏi phòng, sắp có chuyện rồi."},
    "уводить": {2: "Người ta luôn [đưa] chúng tôi [đi] khỏi sân chơi sau chín giờ."},
    "вывезти": {1: "Thứ Bảy bọn mình sẽ [chở] hết đồ bỏ [ra] khỏi nhà xe.",
                2: "Cuối cùng người ta cũng [chở] rác [ra] khỏi sân.",
                3: "[Chở] mấy cái thùng này [ra] nhà vườn giúp mình nhé."},
    "вывозить": {1: "Thứ Bảy nào mình cũng [chở] đồ cũ [ra] bãi rác.",
                 2: "Trước đây rác được [chở ra] bãi mỗi ngày, giờ thì ít lắm.",
                 3: "Người ta bắt đầu chỉ [chở] rác [ra] bãi vào thứ Ba."},
    "увезти": {3: "[Chở] mấy cái thùng này [đi] nhà vườn giúp tớ nhé."},
    "увозить": {1: "Sáng nào bố cũng [chở] các con [đi] nhà trẻ.",
                2: "Bà ấy luôn [chở] chúng tôi [đi] nhà vườn vào tháng Sáu."},
    "унести": {1: "Tớ sẽ [mang] mấy cái túi này [đi] lên trên, đừng động vào.",
               2: "Mấy người láng giềng [mang] cái thang của bọn tớ [đi] mà không trả.",
               3: "Giúp tớ [mang] mấy thùng này [đi] ra xe."},
    "уносить": {1: "Nhân viên [mang] đĩa [đi] nhanh quá.",
                2: "Tối nào anh ấy cũng [mang] cốc của mình [đi] về nhà.",
                3: "Đừng [mang] dép của tớ [đi] sang phòng khác."},
    "убежать": {1: "Nếu thấy nhện, tớ sẽ [bỏ chạy] ngay.",
                2: "Mấy con mèo nhà bên đã [trốn thoát] qua lỗ hàng rào.",
                3: "Nếu thấy nhạt, cứ [bỏ chạy] khỏi đó sớm."},
    "убегать": {1: "Xin lỗi, tớ [chạy đi] đây, xe buýt còn năm phút."},
    "выгнать": {},
}
kho = {n["noteId"]: {k: v["value"] for k, v in n["fields"].items()} for n in doc_notes_cua_model(MODEL_NAME)}
id_ = {}
for i, f in kho.items():
    id_.setdefault(f["WordClean"].strip(), []).append(i)
ghi = {}
for cap, vi in VI.items():
    for w in cap.split():
        assert len(id_[w]) == 1, w
        assert "(" not in kho[id_[w][0]]["Vietnamese"], w      # không đè chú thích user tự viết
        ghi[id_[w][0]] = {"Vietnamese": vi}
hl = lambda s: apply_hl(re.sub(r"\[(.*?)\]", r"<hl>\1</hl>", s))
for w, d in DICH.items():
    nid = id_[w][0]
    for i, vi in d.items():
        h = ghi[nid].get("ExamplesHTML", kho[nid]["ExamplesHTML"])
        m = list(re.finditer(r'(?<=<span class="vi-text">)(.*?)(?=</span></div>)', h))
        assert len(m) == 3, w
        ghi[nid]["ExamplesHTML"] = h[:m[i - 1].start()] + hl(vi) + h[m[i - 1].end():]
V = id_["выехать"][0]
assert "Выезжай" in ghi[V]["ExamplesHTML"]
ghi[V]["ExamplesHTML"] = thay_vi_du(ghi[V]["ExamplesHTML"], 2, {
    "ru": "<hl>Выедем</hl> пораньше, на дорогах сейчас ужас.",
    "en": "Let's <hl>set off</hl> early, the roads are terrible right now.",
    "vi": "Mình <hl>xuất phát</hl> sớm một chút nhé, đường giờ kinh khủng lắm."},
    gan_tieng=gan_tieng_vi_du if "--apply" in sys.argv else None)
for nid, o in ghi.items():
    f = kho[nid]
    if "ExamplesHTML" in o:
        o["ClozeHTML"] = dung_cloze(o["ExamplesHTML"], json.loads(f["GrammarJSON"]), f["WordClean"])
        assert bool(o["ClozeHTML"]) == bool(f["ClozeHTML"]), f["WordClean"]
        assert o["ExamplesHTML"].count("<audio") == f["ExamplesHTML"].count("<audio") or "--apply" not in sys.argv, f["WordClean"]
    print(f["WordClean"], "|", f["Vietnamese"], "->", o["Vietnamese"])
print(len(ghi), "thẻ")
if "--apply" not in sys.argv:
    raise SystemExit
run_backup()
if not sync_truoc_khi_ghi_lo("chú thích вы-/у-"):
    raise SystemExit("sync hỏng")
for nid, o in ghi.items():
    assert update_note_fields(nid, o), nid
print("sync:", sync_now())
