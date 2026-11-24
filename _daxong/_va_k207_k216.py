"""Vá sau đợt k207–k216 (24/11/2026, user duyệt từng việc). L2: chạy một lần.

завязать: OpenRussian gộp завяза́ть (завяжу́, HT «buộc») với завяза́ть (завяза́ю, CHT
«sa lầy») ⇒ thể "both" + tương lai «бу́ду завяза́ть». призвать: призва́ла → призвала́.
красть: + «đánh cắp» (đề cũ nằm gọn trong воровать). подвести/подводить: câu 3 đổi
sang nghĩa «phụ lòng» — nghĩa hay gặp nhất mà ba câu cũ không có.
Mọi chỗ so bản cũ trước khi ghi."""
import copy
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from anki_tools import grammar                                            # noqa: E402
from anki_tools.anki_client import (doc_notes_cua_model, gan_tieng_vi_du, sync_now,   # noqa: E402
                                    sync_truoc_khi_ghi_lo, update_note_fields)
from anki_tools.backup import run_backup                                  # noqa: E402
from anki_tools.config import MODEL_NAME                                  # noqa: E402

CAU = {
    1795456301974: ([
        ('Не <span class="hl">подводи</span> собаку близко к дороге.',
         'Пожалуйста, не <span class="hl">подводи</span> меня в этот раз.'),
        ('Don\'t <span class="hl">bring</span> the dog <span class="hl">up</span> close to the road.',
         'Please don\'t <span class="hl">let</span> me <span class="hl">down</span> this time.'),
        ('Đừng <span class="hl">dắt</span> con chó <span class="hl">lại</span> gần đường.',
         'Lần này làm ơn đừng <span class="hl">làm</span> tôi <span class="hl">thất vọng</span> nhé.')]),
    1795456308119: ([
        ('<span class="hl">Подведи</span> машину ближе к воротам, пожалуйста.',
         'Не <span class="hl">подведи</span> меня завтра, я на тебя рассчитываю.'),
        ('<span class="hl">Bring</span> the car <span class="hl">up</span> closer to the gate, please.',
         'Don\'t <span class="hl">let</span> me <span class="hl">down</span> tomorrow, I\'m counting on you.'),
        ('<span class="hl">Đưa</span> xe <span class="hl">lại</span> gần cổng hơn đi.',
         'Mai đừng <span class="hl">làm</span> tôi <span class="hl">thất vọng</span>, tôi trông cậy vào bạn đấy.')]),
}
ZAV, PRI, KRA = 1795456855515, 1795456869257, 1795312194758

kho = {n["noteId"]: n["fields"] for n in doc_notes_cua_model(MODEL_NAME)}
ex = {}
for nid, doi in CAU.items():
    h = kho[nid]["ExamplesHTML"]["value"]
    for cu, moi in doi:
        assert h.count(cu) == 1, (nid, cu)
        h = h.replace(cu, moi)
    ex[nid] = h
z = json.loads(kho[ZAV]["GrammarJSON"]["value"])
assert z["acc"] == "завяза́ть" and z["aspect"] == "both"
z = copy.deepcopy(z)
z.update(aspect="perfective", partners=["завя́зывать"], present=[""] * 6, future=list(z["presfut"]))
z["parts"].pop("activePresent")
p = json.loads(kho[PRI]["GrammarJSON"]["value"])
assert p["past"][1] == "призва́ла"
p = copy.deepcopy(p)
p["past"][1] = "призвала́"
assert kho[KRA]["Vietnamese"]["value"] == "ăn cắp, trộm"

if "--apply" not in sys.argv:
    print("KHAN: mọi bản cũ khớp.")
    raise SystemExit
run_backup()
print("sync truoc:", sync_truoc_khi_ghi_lo())
for nid, h in ex.items():
    h = gan_tieng_vi_du(h)
    assert h.count("<audio") == 3, nid
    assert update_note_fields(nid, {"ExamplesHTML": h})
grammar.remember("завязать", z, note_id=ZAV)
grammar.remember("призвать", p, note_id=PRI)
assert update_note_fields(ZAV, {"AspectBadge": grammar.aspect_badge_html("perfective", "завязать")})
assert update_note_fields(KRA, {"Vietnamese": "ăn cắp, trộm, đánh cắp"})
print("sync:", sync_now())
