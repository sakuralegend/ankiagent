# -*- coding: utf-8 -*-
"""Vá sau đợt k227–k236 (24/11/2026, user giao tự quyết). L2: chạy một lần.

Câu ví dụ gượng (số nhiều của từ chỉ có số ít) hoặc thiếu nghĩa hay gặp; chữ dịch trong câu
không có trong đề; trọng âm sai/thiếu ở 5 thẻ cũ; стройный: dạng ngắn trung/trạng từ là стро́йно."""
import copy
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
ROOT = ROOT if os.path.exists(os.path.join(ROOT, "bot.py")) else os.path.dirname(ROOT)
sys.path.insert(0, ROOT)
from anki_tools import grammar                                            # noqa: E402
from anki_tools.anki_client import (doc_notes_cua_model, gan_tieng_vi_du, sync_now,   # noqa: E402
                                    sync_truoc_khi_ghi_lo, update_note_fields)
from anki_tools.backup import run_backup                                  # noqa: E402
from anki_tools.config import MODEL_NAME                                  # noqa: E402
from anki_tools.html_builder import dung_cloze, thay_vi_du                # noqa: E402

VI = {"стройный": ("thon thả, mảnh mai, dong dỏng, cân đối, hài hoà, mạch lạc",
                   "thanh mảnh, mảnh mai, cân đối, hài hoà, mạch lạc")}
CAU = {  # từ: (câu số mấy, ru, en, vi)
    "тайга": (3, "Он всю жизнь прожил в <hl>тайге</hl>.", "He has lived in the <hl>taiga</hl> all his life.",
              "Ông ấy sống cả đời trong <hl>rừng taiga</hl>."),
    "загрязнение": (3, "На уроке мы говорили о <hl>загрязнении</hl> океана.",
                    "In class we talked about ocean <hl>pollution</hl>.",
                    "Trong giờ học bọn tớ nói về <hl>sự ô nhiễm</hl> đại dương."),
    "разбирать": (3, "Я с трудом <hl>разбираю</hl> его почерк.", "I can barely <hl>make out</hl> his handwriting.",
                  "Tớ khó lắm mới <hl>đọc ra</hl> chữ anh ấy."),
    "оптимизм": (3, "Мне бы хоть немного твоего <hl>оптимизма</hl>!", "I wish I had a bit of your <hl>optimism</hl>!",
                 "Giá mà tôi có được chút <hl>lạc quan</hl> của bạn!"),
    "траур": (3, "Во время <hl>траура</hl> флаги опускают наполовину.",
              "During <hl>mourning</hl> the flags are lowered to half-mast.",
              "Trong <hl>thời gian để tang</hl>, cờ được hạ xuống nửa cột."),
    "солидарность": (3, "Мы тоже не пошли на работу из <hl>солидарности</hl>.",
                     "We didn't go to work either, out of <hl>solidarity</hl>.",
                     "Bọn tôi cũng không đi làm vì <hl>tình đoàn kết</hl>."),
    "расстроиться": (3, "Из-за дождя <hl>расстроились</hl> все наши планы.",
                     "All our plans <hl>fell through</hl> because of the rain.",
                     "Vì mưa mà mọi kế hoạch của bọn tớ <hl>đổ bể</hl> hết."),
    "специфика": (3, "Без опыта трудно понять <hl>специфику</hl> этого рынка.",
                  "Without experience it's hard to understand the <hl>specifics</hl> of this market.",
                  "Không có kinh nghiệm thì khó hiểu <hl>đặc thù</hl> của thị trường này."),
    "глина": (3, "Эта ваза сделана из белой <hl>глины</hl>.", "This vase is made of white <hl>clay</hl>.",
              "Cái bình này làm bằng <hl>đất sét</hl> trắng."),
    "оппозиция": (3, "Он много лет был в <hl>оппозиции</hl>.", "He was in the <hl>opposition</hl> for many years.",
                  "Ông ấy ở <hl>phe đối lập</hl> nhiều năm."),
    "инспекция": (3, "Во время <hl>инспекции</hl> наш начальник всегда нервничает.",
                  "Our boss is always nervous during an <hl>inspection</hl>.",
                  "Trong <hl>cuộc thanh tra</hl>, sếp chúng tôi luôn căng thẳng."),
    "отстать": (3, "<hl>Отстань</hl> от меня, я занят!", "<hl>Leave</hl> me <hl>alone</hl>, I'm busy!",
                "<hl>Để yên</hl> cho tớ, tớ đang bận!"),
    "ислам": (2, "Моя подруга изучает <hl>ислам</hl> и арабский язык.", "My friend studies <hl>Islam</hl> and Arabic.",
              "Bạn tớ nghiên cứu <hl>Hồi giáo</hl> và tiếng Ả Rập."),
    "христианство": (3, "Рождество — главный праздник в <hl>христианстве</hl>.",
                     "Christmas is a major holiday in <hl>Christianity</hl>.",
                     "Giáng sinh là ngày lễ lớn trong <hl>Kitô giáo</hl>."),
    "спирт": (2, "Протри руки <hl>спиртом</hl> перед уколом.", "Wipe your hands with <hl>alcohol</hl> before the injection.",
              "Lau tay bằng <hl>cồn</hl> trước khi tiêm nhé."),
    "отопление": (3, "Зимой мы платим за <hl>отопление</hl> очень много.",
                  "In winter we pay a lot for <hl>heating</hl>.",
                  "Mùa đông bọn tớ trả tiền <hl>sưởi ấm</hl> rất nhiều."),
    "гладить": (3, "Терпеть не могу <hl>гладить</hl> рубашки.", "I can't stand <hl>ironing</hl> shirts.",
                "Tớ ghét nhất là <hl>ủi</hl> áo sơ mi."),
    "пневмония": (3, "Врач подозревает у неё <hl>пневмонию</hl>.", "The doctor suspects she has <hl>pneumonia</hl>.",
                  "Bác sĩ nghi cô ấy bị <hl>viêm phổi</hl>."),
    "поправиться": (2, "За зиму я <hl>поправилась</hl> на три кило.", "I've <hl>put on</hl> three kilos over the winter.",
                    "Qua mùa đông tớ <hl>lên cân</hl>, tận ba ký."),
    "финиш": (3, "На <hl>финише</hl> он всегда делает рывок.", "He always makes a spurt at the <hl>finish</hl>.",
              "Gần <hl>đích</hl> anh ấy luôn bứt tốc."),
    "расписаться": (2, "Мы <hl>расписались</hl> в мае, а свадьба летом.",
                    "We <hl>registered our marriage</hl> in May, and the wedding is in summer.",
                    "Bọn tớ <hl>đăng ký kết hôn</hl> hồi tháng Năm, còn đám cưới thì mùa hè."),
}
H = '<span class="hl">%s</span>'
DICH = {  # chữ dịch không có trong đề
    "сердитый": [("tức tối", "tức giận", 2)], "кривой": [("méo", "vẹo", 1)],
    "познавать": [("khám phá", "tìm hiểu", 1)],
    "познать": [("biết đến", "trải qua", 1), ("biết", "nếm trải", 1)],
    "престижный": [("sang trọng", "danh giá", 1)], "криминальный": [("đầy tệ nạn", "đầy tội phạm", 1)],
    "напрасно": [("toi công", "uổng công", 1)], "характеризовать": [("đánh giá", "nhận xét", 1)],
    "остывать": [("nguội lạnh", "mất hứng thú", 1)], "траур": [("lễ tưởng niệm", "sự để tang", 1)],
}
HD = {
    "служить": [("<b>служа́щий</b>", "<b>слу́жащий</b>")],
    "красный": [("<b>краси́ть</b>", "<b>кра́сить</b>")],
    "прекрасный": [("<i>Красная площадь</i>", "<i>Кра́сная пло́щадь</i>")],
    "сильный": [("<i>сильный дождь</i>", "<i>си́льный дождь</i>"), ("<i>сильный ветер</i>", "<i>си́льный ве́тер</i>")],
    "настаивать": [("<b>насто́ять</b> (<b>насто́ю</b>)", "<b>настоя́ть</b> (<b>настою́</b>)"),
                   ("<b>насто́ять</b> (HT)", "<b>настоя́ть</b> (HT)")],
}

notes = doc_notes_cua_model(MODEL_NAME)
kho = {n["noteId"]: {k: v["value"] for k, v in n["fields"].items()} for n in notes}
id_ = {}
for i, f in kho.items():
    id_.setdefault(f["WordClean"].strip(), []).append(i)
ghi = {}


def mot(w):
    assert len(id_[w]) == 1, (w, id_[w])
    return id_[w][0]


for w, (cu, moi) in VI.items():
    assert kho[mot(w)]["Vietnamese"] == cu, w
    ghi.setdefault(mot(w), {})["Vietnamese"] = moi
for w, ds in DICH.items():
    h = kho[mot(w)]["ExamplesHTML"]
    for cu, moi, so in ds:
        assert h.count(H % cu) == so, (w, cu, h.count(H % cu))
        h = h.replace(H % cu, H % moi)
    ghi.setdefault(mot(w), {})["ExamplesHTML"] = h
for w, ds in HD.items():
    h = kho[mot(w)]["HuongDan"]
    for cu, moi in ds:
        assert h.count(cu) == 1, (w, cu, h.count(cu))
        h = h.replace(cu, moi)
    ghi.setdefault(mot(w), {})["HuongDan"] = h
for w, (i, ru, en, vi) in CAU.items():
    nid = mot(w)
    h = ghi.get(nid, {}).get("ExamplesHTML", kho[nid]["ExamplesHTML"])
    assert len(re.findall(r"<details\b", h)) == 3, w
    ghi.setdefault(nid, {})["ExamplesHTML"] = thay_vi_du(h, i - 1, {"ru": ru, "en": en, "vi": vi})
S = mot("стройный")
g = copy.deepcopy(json.loads(kho[S]["GrammarJSON"]))
assert g["shorts"][2] == g["adverb"] == "стройно́"
g["shorts"][2] = g["adverb"] = "стро́йно"
for nid, o in ghi.items():
    if "ExamplesHTML" in o:
        f = kho[nid]
        cz = dung_cloze(o["ExamplesHTML"], json.loads(f["GrammarJSON"]), f["WordClean"])
        if not cz:
            sys.exit(f"cloze hỏng: {f['WordClean']}")
print("KHAN: mọi bản cũ khớp —", len(ghi), "thẻ")
if "--apply" not in sys.argv:
    raise SystemExit
run_backup()
if not sync_truoc_khi_ghi_lo("vá k227-k236"):
    raise SystemExit("sync hỏng")
for nid, o in ghi.items():
    f = kho[nid]
    if "ExamplesHTML" in o:
        h = gan_tieng_vi_du(o["ExamplesHTML"])
        assert h.count("<audio") == 3 == h.count('class="nghe"'), nid
        o["ExamplesHTML"], o["ClozeHTML"] = h, dung_cloze(h, json.loads(f["GrammarJSON"]), f["WordClean"])
    assert update_note_fields(nid, o), nid
    print("ok", f["WordClean"], list(o))
grammar.remember("стройный", g, note_id=S)
print("sync:", sync_now())
