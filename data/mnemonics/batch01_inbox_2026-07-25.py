# -*- coding: utf-8 -*-
"""LÔ 1 — nội dung field `Mnemonic` ("Thầy nhắc") cho 271 thẻ RUSSIAN::0-inbox (25/07/2026).
Do Opus 5 soạn tay. File này là DỮ LIỆU, không phải module của anki_tools — giữ lại làm
CHUẨN VĂN PHONG cho các lô sau (các chuỗi *_TIP dùng chung được lấy lại nguyên văn).

Mỗi entry:  "từ": (phiên âm, thân bài, dòng "cách nhớ")
Bốn chiến lược, ưu tiên từ trên xuống — mẹo âm thanh là phương án CUỐI:
  1. ENG   — từ mượn quốc tế: chỉ mặt từ tiếng Anh (user B2/IELTS 6.5) + dạy trọng âm
  2. gốc   — chẻ gốc / nêu cả họ từ (вет-, ставить, уч-, род-, ъ, quốc tịch, số thứ tự...)
  3. COG   — họ hàng Ấn–Âu xa (дочь~daughter, мышь~mouse, хлеб~loaf)
  4. SND   — mẹo âm thanh, BẮT BUỘC dùng tiếng Việt CÓ THẬT

Phiên âm theo CÁCH ĐỌC THẬT: о không nhấn -> "a", е không nhấn -> "i",
г trong -ого/-его -> "v", phụ âm cuối điếc (б->p, в->f, з->s, д->t). VIẾT HOA âm tiết nhấn.

Cách dùng lại cho lô sau:
    from batch01... import M          # hoặc copy các hằng *_TIP
    html = f'<div class="mn-read">{read}</div>{body}<div class="mn-tip">{tip}</div>'
    ac("updateNoteFields", note={"id": note_id, "fields": {"Mnemonic": html}})
KHÔNG cần full sync lần nữa: field đã tồn tại, ghi nội dung chỉ là sửa note bình thường."""

M = {}

# ============================================================
# HỌ 1 — QUỐC TỊCH: một công thức duy nhất, lặp lại để thấm
# ============================================================
NAT_TIP = ('Bộ bốn cố định: <b>-ец</b> nam / <b>-ка</b> nữ / <b>-ский</b> tính từ / '
           '<b>по-…-ски</b> nói tiếng đó. Thuộc bộ này là mở khoá mọi quốc tịch.')
NAT = {
    "американец":   ("a-mi-ri-KA-nhets",  "Америк(а) + <b>-ец</b> → đàn ông nước đó"),
    "американка":   ("a-mi-ri-KAN-ka",    "Америк(а) + <b>-ка</b> → phụ nữ nước đó"),
    "американский": ("a-mi-ri-KAN-skiy",  "Америк(а) + <b>-ский</b> → tính từ"),
    "англичанин":   ("an-gli-CHA-nhin",   "Англи(я) + <b>-чанин</b> (biến thể của -ец) → đàn ông Anh"),
    "англичанка":   ("an-gli-CHAN-ka",    "Англи(я) + <b>-ка</b> → phụ nữ Anh"),
    "английский":   ("an-GLIY-skiy",      "Англи(я) + <b>-ский</b> → tính từ"),
    "английски":    ("an-GLIY-ski",       "Dạng trạng từ, hầu như luôn đi với <b>по-</b>"),
    "по-английски": ("pa-an-GLIY-ski",    "<b>по-</b> + англий + <b>-ски</b> → <i>bằng</i> tiếng Anh"),
    "араб":         ("a-RAP",             "Gốc Ả Rập. Cuối từ <b>б đọc thành “p”</b>"),
    "арабка":       ("a-RAP-ka",          "араб + <b>-ка</b> → phụ nữ Ả Rập"),
    "арабский":     ("a-RAP-skiy",        "араб + <b>-ский</b> → tính từ"),
    "испанец":      ("is-PA-nhets",       "Испани(я) + <b>-ец</b>"),
    "испанка":      ("is-PAN-ka",         "Испани(я) + <b>-ка</b>"),
    "испанский":    ("is-PAN-skiy",       "Испани(я) + <b>-ский</b>"),
    "по-испански":  ("pa-is-PAN-ski",     "<b>по-</b> + испан + <b>-ски</b> → <i>bằng</i> tiếng TBN"),
    "итальянец":    ("i-ta-LYA-nhets",    "Итали(я) + <b>-янец</b>"),
    "итальянка":    ("i-ta-LYAN-ka",      "Итали(я) + <b>-янка</b>"),
    "итальянский":  ("i-ta-LYAN-skiy",    "Итали(я) + <b>-янский</b>"),
    "китаец":       ("ki-TA-yets",        "Кита(й) + <b>-ец</b>"),
    "китаянка":     ("ki-ta-YAN-ka",      "Кита(й) + <b>-янка</b>"),
    "китайский":    ("ki-TAY-skiy",       "Кита(й) + <b>-ский</b>"),
    "китайски":     ("ki-TAY-ski",        "Dạng trạng từ, đi với <b>по-</b>"),
    "по-китайски":  ("pa-ki-TAY-ski",     "<b>по-</b> + китай + <b>-ски</b> → <i>bằng</i> tiếng Trung"),
    "кореец":       ("ka-RYE-yets",       "Коре(я) + <b>-ец</b>"),
    "кореянка":     ("ka-ri-YAN-ka",      "Коре(я) + <b>-янка</b>"),
    "француз":      ("fran-TSUS",         "Pháp. Cuối từ <b>з đọc thành “s”</b>"),
    "француженка":  ("fran-TSU-zhen-ka",  "француз + <b>-енка</b> → phụ nữ Pháp"),
    "французский":  ("fran-TSUS-kiy",     "француз + <b>-ский</b>"),
    "по-французски":("pa-fran-TSUS-ki",   "<b>по-</b> + французс + <b>-ки</b> → <i>bằng</i> tiếng Pháp"),
    "русский":      ("RUS-skiy",          "Рус(ь) + <b>-ский</b> → người Nga / tiếng Nga"),
    "русски":       ("RUS-ki",            "Dạng trạng từ, đi với <b>по-</b>"),
    "по-русски":    ("pa-RUS-ki",         "<b>по-</b> + рус + <b>-ски</b> → <i>bằng</i> tiếng Nga"),
    "вьетнамский":  ("vyet-NAM-skiy",     "Вьетнам + <b>-ский</b>"),
    "по-немецки":   ("pa-nhi-MYE-tski",   "<b>по-</b> + немец + <b>-ки</b> → <i>bằng</i> tiếng Đức"),
    "китай":        ("ki-TAY",            "Tên nước Trung Quốc — gốc của cả cụm китаец/китаянка/китайский"),
}
for w, (rd, body) in NAT.items():
    M[w] = (rd, body, NAT_TIP)

# немец có câu chuyện riêng, hay hơn công thức
M["немец"]    = ("NHE-mhets", "Gốc <b>немой</b> = <i>câm</i>. Người Slav xưa gọi người Đức là "
                 "“kẻ không biết nói (tiếng mình)”.", "Nhớ немой (câm) là ra cả немец/немка/немецкий. " + NAT_TIP)
M["немка"]    = ("NHEM-ka",   "немец + <b>-ка</b> → phụ nữ Đức (gốc <b>немой</b> = câm)", NAT_TIP)
M["немецкий"] = ("nhi-MHE-tskiy", "немец + <b>-кий</b> → tiếng Đức / thuộc Đức", NAT_TIP)

# ============================================================
# HỌ 2 — SỐ THỨ TỰ: số đếm + đuôi tính từ
# ============================================================
ORD_TIP = ('Số thứ tự = <b>số đếm + đuôi tính từ</b>. Thuộc số đếm là có luôn số thứ tự, '
           'khỏi học riêng 16 từ.')
ORD = {
    "второй":        ("fta-ROY",            "два (2)"),
    "третий":        ("TRYE-tiy",           "три (3)"),
    "четвёртый":     ("chit-VYOR-tyy",      "четыре (4)"),
    "пятый":         ("PYA-tyy",            "пять (5)"),
    "шестой":        ("shys-TOY",           "шесть (6)"),
    "седьмой":       ("sid-MOY",            "семь (7)"),
    "восьмой":       ("vas-MOY",            "восемь (8)"),
    "девятый":       ("di-VYA-tyy",         "девять (9)"),
    "десятый":       ("di-SYA-tyy",         "десять (10)"),
    "сороковой":     ("sa-ra-ka-VOY",       "сорок (40)"),
    "пятидесятый":   ("pya-ti-di-SYA-tyy",  "пятьдесят (50)"),
    "восьмидесятый": ("va-smi-di-SYA-tyy",  "восемьдесят (80)"),
    "девяностый":    ("di-vi-NOS-tyy",      "девяносто (90)"),
    "сотый":         ("SO-tyy",             "сто (100)"),
    "тысячный":      ("TY-sich-nyy",        "тысяча (1000)"),
    "двухтысячный":  ("dvukh-TY-sich-nyy",  "две тысячи (2000)"),
}
for w, (rd, src) in ORD.items():
    M[w] = (rd, f"Mọc thẳng từ <b>{src}</b>", ORD_TIP)

# ============================================================
# HỌ 3 — THỜI TIẾT: danh từ + -ный
# ============================================================
WEA_TIP = 'Thời tiết = <b>danh từ + -ный</b>. Biết danh từ là suy ra được tính từ.'
WEA = {
    "дождливый": ("dazhd-LI-vyy",  "дождь (mưa)"),
    "ветреный":  ("VYE-tri-nyy",   "ветер (gió)"),
    "снежный":   ("SNHEZH-nyy",    "снег (tuyết)"),
    "солнечный": ("SOL-nhich-nyy", "солнце (mặt trời)"),
    "облачный":  ("O-blach-nyy",   "облако (đám mây)"),
    "морозный":  ("ma-ROZ-nyy",    "мороз (băng giá)"),
}
for w, (rd, src) in WEA.items():
    M[w] = (rd, f"Từ <b>{src}</b> + <b>-ный</b>", WEA_TIP)

M["ветер"]   = ("VYE-tyer", "Gốc của <b>ветреный</b> (lộng gió) — và của cả “người hay thay đổi”.",
                "Gió thổi đâu ngả đó → nghĩa bóng: người nhẹ dạ.")
M["облако"]  = ("O-bla-ka", "<b>Ba</b> cầm <b>ô</b>, ngửa mặt <b>ca</b> hát với đám mây.",
                "Nhớ облако là có luôn <b>облачный</b> (nhiều mây / điện toán đám mây).")
M["пасмурный"] = ("PAS-mur-nyy", "Nghe như <b>“PẢ SƯƠNG MÙ”</b> — trời phủ sương mù, u ám.",
                  "Từ này không chẻ gốc được, đành dùng mẹo âm thanh.")

# ============================================================
# HỌ 4 — GỐC вет- (LỜI NÓI): mở khoá 6 từ một lúc
# ============================================================
VET_TIP = ('Gốc <b>-вет-</b> = <i>lời nói</i>. Nắm gốc này là có привет, ответ, ответить, '
           'отвечать, ответный cùng lúc.')
M["привет"]   = ("pri-VYET",       "<b>при-</b>(tới) + <b>вет</b>(lời) → “lời gửi tới bạn”", VET_TIP)
M["ответ"]    = ("at-VYET",        "<b>от-</b>(lại) + <b>вет</b>(lời) → “lời nói lại” = câu trả lời", VET_TIP)
M["ответить"] = ("at-VYE-tit",     "ответ + đuôi động từ (thể hoàn thành: trả lời <i>xong</i>)", VET_TIP)
M["отвечать"] = ("at-vi-CHAT",     "Cặp chưa hoàn thành của ответить (đang/thường trả lời)", VET_TIP)
M["ответный"] = ("at-VYET-nyy",    "ответ + <b>-ный</b> → mang tính đáp lại", VET_TIP)

# ============================================================
# HỌ 5 — DẤU ъ: tách tiền tố khỏi gốc
# ============================================================
HARD_TIP = ('Dấu cứng <b>ъ</b> chỉ làm một việc: <b>ngăn tiền tố khỏi gốc</b>, đọc tách ra. '
            'Thấy ъ là biết từ này ghép, cứ tách ra mà đoán nghĩa.')
M["подъезд"]  = ("pad-YEST",  "<b>под</b>(dưới/tới) + <b>езд</b>(đi xe) → chỗ xe đi tới = lối vào", HARD_TIP)
M["разъезд"]  = ("raz-YEST",  "<b>раз</b>(tản ra) + <b>езд</b>(đi) → đi tản mát khắp nơi", HARD_TIP)
M["подъём"]   = ("pad-YOM",   "<b>под</b>(lên) + <b>ём</b>(nâng) → sự nâng lên, thức dậy", HARD_TIP)
M["объём"]    = ("ab-YOM",    "<b>об</b>(bao quanh) + <b>ём</b>(chứa) → sức chứa = thể tích", HARD_TIP)
M["разъём"]   = ("raz-YOM",   "<b>раз</b>(tách) + <b>ём</b> → chỗ tách/nối = giắc cắm", HARD_TIP)
M["объявить"] = ("ab-yi-VIT", "<b>об</b> + <b>явить</b>(làm hiện ra) → làm cho ai cũng thấy = tuyên bố", HARD_TIP)
M["объявление"] = ("ab-yiv-LYE-nhiye", "объявить + <b>-ение</b> → cái được tuyên bố = thông báo, quảng cáo", HARD_TIP)

# ============================================================
# HỌ 6 — ставить (ĐẶT / ĐỨNG) + tiền tố
# ============================================================
STAV_TIP = 'Gốc <b>ставить</b> = đặt cho đứng. Đổi tiền tố là đổi nghĩa — học gốc, không học từng từ.'
M["поставить"]  = ("pa-STA-vit",  "<b>по-</b> + ставить → đặt xuống, dựng lên", STAV_TIP)
M["составить"]  = ("sa-STA-vit",  "<b>со-</b>(gom lại) + ставить → xếp các phần lại = soạn thảo", STAV_TIP)
M["вставить"]   = ("FSTA-vit",    "<b>в-</b>(vào trong) + ставить → cắm vào, chèn vào", STAV_TIP)

# ============================================================
# HỌ 7 — BỮA ĂN: danh từ bữa + -ать
# ============================================================
MEAL_TIP = 'Tên bữa ăn + <b>-ать</b> = động từ ăn bữa đó. Một luật, ba từ.'
M["завтракать"] = ("ZAF-tra-kat", "завтрак (bữa sáng) + <b>-ать</b>", MEAL_TIP)
M["обедать"]    = ("a-BYE-dat",   "обед (bữa trưa) + <b>-ать</b>", MEAL_TIP)
M["ужинать"]    = ("U-zhy-nat",   "ужин (bữa tối) + <b>-ать</b>", MEAL_TIP)

# ============================================================
# CẶP ĐỐI LẬP / CẶP DỄ LẪN — học theo cặp, đừng học lẻ
# ============================================================
M["почему"] = ("pa-chi-MU", "<b>по</b> + <b>чему</b> (theo cái gì) → “theo cái gì mà ra?” = tại sao",
               "Học <b>cặp</b>: почему (tại sao) hỏi — потому (bởi vì) đáp. Sai một cái là lẫn cả hai.")
M["потому"] = ("pa-ta-MU", "<b>по</b> + <b>тому</b> (theo cái đó) → “theo cái đó” = bởi vì",
               "Học <b>cặp</b>: почему hỏi — потому đáp. Thường đi đủ bộ <i>потому что</i>.")
M["узкий"]  = ("US-kiy",  "Miệng phải <b>khép hẹp</b> lại mới phát ra được âm “u” — hẹp.",
               "Học cặp đối lập với <b>широкий</b> (rộng): nhớ một là bật ra cái kia.")
M["широкий"]= ("shy-RO-kiy", "Miệng phải <b>há rộng</b> mới ra âm “shy-RO” — rộng.",
               "Học cặp đối lập với <b>узкий</b> (hẹp).")
M["жена"]   = ("zhy-NA", "Vợ. Gốc của <b>женатый</b> (đàn ông đã có vợ).",
                "Cặp giới tính: <b>женатый</b> = có vợ (nam) / <b>замужем</b> = có chồng (nữ). Nga phân biệt hai bên.")
M["женатый"]= ("zhy-NA-tyy", "<b>жена</b>(vợ) + đuôi → “đã có vợ” — chỉ dùng cho <b>nam</b>",
                "Cặp: женатый (nam) ↔ замужем (nữ). Dùng lộn giới là lỗi kinh điển.")
M["замужем"]= ("ZA-mu-zhem", "<b>за</b>(sau) + <b>муж</b>(chồng) → “ở sau lưng chồng” = đã lấy chồng (<b>nữ</b>)",
                "Cặp: замужем (nữ) ↔ женатый (nam).")
M["вина"]   = ("vi-NA", "Lỗi, tội. Nghe gần giống <b>вино</b> (rượu) — uống <b>вино</b> gây ra <b>вина</b>.",
                "Bẫy: <b>вина</b> (lỗi) vs <b>вино</b> (rượu) chỉ khác chữ cuối. Đọc kỹ đuôi.")
M["море"]   = ("MO-rye", "Biển.", "Học cặp vần với <b>поле</b> (cánh đồng): море–поле, biển–đồng, cùng đuôi -е.")
M["поле"]   = ("PO-lye", "Cánh đồng, sân, lĩnh vực.", "Học cặp vần với <b>море</b> (biển): море–поле.")

# ============================================================
# CHẺ GỐC — mở khoá cả họ từ
# ============================================================
M["конечно"]    = ("ka-NHESH-na", "Gốc <b>конец</b> (kết thúc) → “chuyện đã xong rồi” = tất nhiên.",
                   "⚠️ <b>чн đọc thành “shn”</b>, không đọc “ch”. Cùng luật với скучный.")
M["скучный"]    = ("SKUSH-nyy", "Gốc <b>скука</b> (sự chán).",
                   "⚠️ <b>чн đọc thành “shn”</b> — cùng luật với конечно. Chỉ vài từ có luật này, nhớ chung một mẻ.")
M["вместо"]     = ("VMYES-ta", "<b>в</b>(vào) + <b>место</b>(chỗ) → “vào chỗ của” = thay vì",
                   "Thấy место là ra nghĩa. Đừng học вместо như một từ mới.")
M["сначала"]    = ("s-na-CHA-la", "<b>с</b>(từ) + <b>начала</b>(khởi đầu) → từ đầu",
                   "Cùng gốc <b>начало</b> (bắt đầu) — biết một là biết hai.")
M["начало"]     = ("na-CHA-la", "Gốc <b>начать</b> (bắt đầu) → cái sự bắt đầu",
                   "Từ đây ra <b>сначала</b> (từ đầu). Học chùm.")
M["позавчера"]  = ("pa-za-fchi-RA", "<b>по-за-</b> + <b>вчера</b>(hôm qua) → “lùi quá hôm qua” = hôm kia",
                   "Cứ đếm lùi: вчера → позавчера. Tiếng Nga chồng tiền tố để lùi thêm một ngày.")
M["вечером"]    = ("VYE-chi-ram", "<b>вечер</b>(buổi tối) ở cách 5 → “vào buổi tối”",
                   "Đuôi <b>-ом</b> trên từ chỉ thời gian = “vào lúc đó”: утром, днём, вечером, ночью.")
M["современный"]= ("sa-vri-MHEN-nyy", "<b>со-</b>(cùng) + <b>время</b>(thời gian) → “cùng thời” = hiện đại",
                   "Thấy <b>-врем-</b> là nghĩ tới thời gian.")
M["иностранный"]= ("i-na-STRAN-nyy", "<b>ино</b>(khác) + <b>страна</b>(đất nước) → thuộc nước khác",
                   "Nhận ra <b>страна</b> nằm giữa từ là đoán được nghĩa ngay.")
M["небольшой"]  = ("nhi-bal-SHOY", "<b>не</b> + <b>большой</b>(lớn) → không lớn = nhỏ",
                   "Tiếng Nga rất hay dựng từ bằng <b>не + từ trái nghĩa</b>. Gặp не- là tách ra đọc.")
M["немного"]    = ("nhi-MNO-ga", "<b>не</b> + <b>много</b>(nhiều) → không nhiều = một chút",
                   "Cùng công thức <b>не + …</b> như небольшой, неинтересный.")
M["неинтересный"]=("nhi-in-ti-RYES-nyy", "<b>не</b> + interesting → không thú vị",
                   "Gốc là từ tiếng Anh bạn đã biết; chỉ cần nhớ <b>не-</b> = phủ định.")
M["домашний"]   = ("da-MASH-nhiy", "Gốc <b>дом</b> (nhà) → thuộc về nhà, tự làm ở nhà",
                   "Thấy <b>дом</b> là ra nghĩa — <i>домашнее задание</i> = bài tập về nhà.")
M["выходной"]   = ("vy-kha-DNOY", "<b>вы</b>(ra) + <b>ход</b>(đi) → “ngày được đi ra” = ngày nghỉ",
                   "Gốc <b>ход/ходить</b> (đi) có mặt trong rất nhiều từ — đáng thuộc.")
M["защита"]     = ("za-SHCHI-ta", "<b>за</b> + <b>щит</b>(cái khiên) → núp sau khiên = sự bảo vệ",
                   "Bạn đã học <b>щит</b> rồi — dùng lại nó, đừng học защита từ số 0.")
M["зачёт"]      = ("za-CHOT", "<b>за</b> + <b>счёт</b>(tính, đếm) → “được tính là đạt” = bài đánh giá",
                   "Bạn đã học <b>счёт</b> rồi. Nhận ra nó là xong.")
M["переводчик"] = ("pi-ri-VOT-chik", "<b>пере</b>(qua) + <b>вод</b>(dẫn) + <b>-чик</b>(người) → người dẫn nghĩa qua ngôn ngữ khác",
                   "Đuôi <b>-чик/-щик</b> = <i>người làm nghề đó</i>. Gặp là biết đang nói về người.")
M["повторять"]  = ("paf-ta-RYAT", "Gốc <b>второй</b> (thứ hai) → “làm lần thứ hai” = lặp lại, ôn tập",
                   "Bạn đã học второй. Đây đúng là từ mô tả việc bạn đang làm với Anki.")
M["записывать"] = ("za-PI-sy-vat", "<b>за</b> + <b>писать</b>(viết) → viết lại để giữ = ghi chép",
                   "Gốc <b>пис-</b> (viết): писать, записывать, письменно, письмо. Học chùm.")
M["письменно"]  = ("PIS-mhen-na", "Gốc <b>пис-</b>(viết) → bằng chữ viết",
                   "Cùng chùm <b>пис-</b> với писать, записывать.")
M["прослушать"] = ("pra-SLU-shat", "<b>про</b>(trọn) + <b>слушать</b>(nghe) → nghe hết từ đầu đến cuối",
                   "Tiền tố <b>про-</b> thường mang nghĩa “làm trọn vẹn”: прочитать, прослушать.")
M["прочитать"]  = ("pra-chi-TAT", "<b>про</b>(trọn) + <b>читать</b>(đọc) → đọc xong",
                   "Cặp thể: читать (đang đọc) → прочитать (đọc <i>xong</i>). Tiền tố про- đóng việc lại.")
M["написать"]   = ("na-pi-SAT", "<b>на</b> + <b>писать</b>(viết) → viết xong",
                   "Cặp thể: писать (đang viết) → написать (viết <i>xong</i>).")
M["рассказать"] = ("ra-ska-ZAT", "<b>рас</b>(trải ra) + <b>сказать</b>(nói) → trải câu chuyện ra = kể",
                   "Gốc <b>сказ-</b>: сказать (nói), рассказать (kể), рассказ (truyện).")
M["сказать"]    = ("ska-ZAT", "Gốc <b>сказ-</b> = nói ra một lần.",
                   "Cặp thể: говорить (đang nói) → сказать (nói <i>xong</i> một câu).")
M["поговорить"] = ("pa-ga-va-RIT", "<b>по</b> + <b>говорить</b> → nói <i>một lát</i> rồi thôi",
                   "Tiền tố <b>по-</b> trên động từ = làm một lúc: погулять, поговорить, поработать.")
M["говорить"]   = ("ga-va-RIT", "Gốc <b>говор</b> = tiếng nói, giọng.",
                   "Từ gốc này ra разговаривать (trò chuyện), поговорить, разговор.")
M["спросить"]   = ("spra-SIT", "Gốc <b>прос-</b> (hỏi xin).",
                   "Cặp thể: спрашивать (đang hỏi) → спросить (hỏi <i>xong</i> một câu). Học cả cặp.")
M["спрашивать"] = ("SPRA-shy-vat", "Cặp chưa hoàn thành của спросить.",
                   "Cặp thể: спрашивать (thường/đang hỏi) → спросить (hỏi xong).")
M["выполнить"]  = ("VY-pal-nhit", "<b>вы</b>(ra) + <b>полный</b>(đầy) → làm cho đầy đủ = hoàn thành",
                   "Thấy <b>полн-</b> là nghĩ “đầy/đủ”.")
M["использовать"]=("is-POL-za-vat", "Gốc <b>польза</b> (ích lợi) → lấy cái lợi ra = sử dụng",
                   "Thấy <b>польз-</b> là nghĩ “có ích”.")
M["проверять"]  = ("pra-vi-RYAT", "<b>про</b> + <b>вера</b>(niềm tin) → “thử xem có tin được không” = kiểm tra",
                   "Gốc <b>вер-</b> = tin: верить, проверять, уверенный.")
M["учиться"]    = ("u-CHI-tsa", "Gốc <b>уч-</b>(học) + <b>-ся</b>(tự mình) → tự học",
                   "Gốc <b>уч-</b> mở khoá cả chùm: учить, ученик, учебник, учёный.")
M["учёный"]     = ("u-CHO-nyy", "Gốc <b>уч-</b>(học) → “người đã được học” = nhà khoa học",
                   "Cùng chùm <b>уч-</b> với учиться, учебник.")
M["упражнение"] = ("u-prazh-NHE-nhiye", "Đuôi <b>-ение</b> = danh từ chỉ <i>việc làm gì đó</i> → bài tập",
                   "Đuôi <b>-ение/-ание</b> luôn là danh từ trừu tượng. Gặp là biết loại từ ngay.")
M["образование"]= ("a-bra-za-VA-nhiye", "<b>образ</b>(hình hài) + <b>-ание</b> → “sự tạo hình con người” = giáo dục",
                   "Đuôi <b>-ание</b> = danh từ chỉ quá trình. Gốc <b>образ</b> còn ra образец (mẫu).")
M["образец"]    = ("a-bra-ZYETS", "Gốc <b>образ</b> (hình ảnh, hình hài) → cái để nhìn theo = mẫu",
                   "Cùng gốc <b>образ</b> với образование.")
M["объяснение"] = ("ab-yis-NHE-nhiye", "", "")   # phòng khi có
M["особенность"]= ("a-SO-bhen-nast", "Gốc <b>особый</b> (riêng, đặc biệt) + <b>-ость</b> → tính chất riêng",
                   "Đuôi <b>-ость</b> biến tính từ thành danh từ trừu tượng, <b>luôn giống cái</b>.")
M["национальность"]=("na-tsy-a-NAL-nast", "Gốc tiếng Anh <i>national</i> + <b>-ость</b>",
                   "Chỉ cần nhớ đuôi <b>-ость</b> = danh từ trừu tượng, giống cái.")
M["множественный"]=("MNO-zhyst-vhen-nyy", "Gốc <b>много</b> (nhiều) → thuộc về số nhiều",
                   "Thấy <b>множ-</b> là nghĩ “nhiều”.")
M["положительный"]=("pa-la-ZHY-tyel-nyy", "Gốc <b>положить</b> (đặt vào) → “có đặt vào” = dương, tích cực",
                   "Cặp đối lập bắt buộc học chung: положительный ↔ <b>отрицательный</b>.")
M["отрицательный"]=("a-tri-TSA-tyel-nyy", "Gốc <b>отрицать</b> (phủ nhận) → phủ định, âm",
                   "Cặp đối lập: отрицательный ↔ <b>положительный</b>.")
M["вопросительный"]=("va-pra-SI-tyel-nyy", "Gốc <b>вопрос</b> (câu hỏi) → mang tính nghi vấn",
                   "Thấy <b>вопрос</b> nằm trong từ là ra nghĩa.")
M["прошедший"]  = ("pra-SHYED-shyy", "Gốc <b>пройти</b> (đi qua) → cái đã đi qua = đã qua",
                   "Cặp ngữ pháp: прошедшее время = <i>thì quá khứ</i>. Học nguyên cụm.")
M["прошедшее"]  = ("pra-SHYED-shy-ye", "Dạng giống trung của прошедший → dùng cho <i>время</i> (thì)",
                   "Học nguyên cụm <b>прошедшее время</b> = thì quá khứ.")
M["спряжение"]  = ("spri-ZHE-nhiye", "Gốc <b>прягать</b> (buộc ách vào) → “buộc động từ vào ngôi” = chia động từ",
                   "Cặp thuật ngữ: <b>спряжение</b> chia động từ ↔ <b>склонение</b> biến cách danh từ.")
M["спрягаться"] = ("spri-GA-tsa", "Cùng gốc спряжение + <b>-ся</b> → (động từ) tự chia",
                   "Nhớ cùng cặp với <b>спряжение</b>.")
M["сожаление"]  = ("sa-zhy-LYE-nhiye", "Gốc <b>жалеть</b> (thương xót, tiếc) + <b>-ение</b>",
                   "Hay gặp trong cụm <i>к сожалению</i> = tiếc là… Học nguyên cụm tiện hơn.")
M["правильно"]  = ("PRA-vil-na", "Gốc <b>право</b> (điều phải) → <b>правило</b> (quy tắc) → đúng quy tắc",
                   "Chùm <b>прав-</b> = phải/đúng: право, правило, правильно.")
M["отлично"]    = ("at-LICH-na", "Gốc <b>отличить</b> (phân biệt) → “nổi bật hẳn ra” = xuất sắc",
                   "Đây là điểm 5 (cao nhất) trong thang điểm Nga — nhớ như một lời khen.")
M["жительство"] = ("ZHY-tyel-stva", "Gốc <b>жить</b> (sống) → nơi sinh sống",
                   "Bạn đã học <b>жить</b>. Đuôi <b>-ство</b> = danh từ trừu tượng.")
M["звонить"]    = ("zva-NHIT", "Gốc <b>звон</b> = <i>tiếng chuông</i> → làm cho chuông reo = gọi điện",
                   "Hình dung điện thoại reo chuông. Trọng âm rơi vào <b>-нить</b>, đừng đọc ZVO-nit.")
M["родиться"]   = ("ra-DI-tsa", "Gốc <b>род</b> (dòng dõi) + <b>-ся</b> → “tự vào dòng họ” = ra đời",
                   "Bạn đã học <b>род</b>. Cùng chùm: родной, родители, родина.")
M["родной"]     = ("rad-NOY", "Gốc <b>род</b> (dòng dõi) → cùng huyết thống, ruột thịt, quê nhà",
                   "Cùng chùm <b>род</b> với родиться. <i>родной язык</i> = tiếng mẹ đẻ.")
M["малыш"]      = ("ma-LYSH", "Gốc <b>малый</b> (nhỏ) → nhỏ xíu = em bé",
                   "Thấy <b>мал-</b> là nghĩ “nhỏ”: маленький, малыш.")
M["рисовать"]   = ("ri-sa-VAT", "Vẽ.", "Học cặp: <b>рисовать</b> (vẽ) → <b>рисунок</b> (bức vẽ). Động từ ra danh từ.")
M["рисунок"]    = ("ri-SU-nak", "Từ <b>рисовать</b> (vẽ) → cái được vẽ ra",
                   "Học cặp với рисовать. Đuôi <b>-ок</b> hay chỉ kết quả của hành động.")
M["понимать"]   = ("pa-nhi-MAT", "Gốc <b>по-ня-</b> (nắm lấy) → “nắm được ý” = hiểu",
                   "Cặp thể: понимать (đang hiểu) → <b>понять</b> (hiểu ra). Cùng gốc: понятно, понятие.")
M["забыть"]     = ("za-BYT", "<b>за</b>(ra sau) + <b>быть</b>(tồn tại) → “đẩy ra sau tâm trí” = quên",
                   "Bạn đã biết <b>быть</b>. Tiền tố за- hay mang nghĩa “ra khỏi tầm”.")

# ============================================================
# MẸO ÂM THANH — chỉ dùng khi không chẻ gốc được
# ============================================================
SND_TIP = 'Từ này không chẻ gốc được nên phải dùng mẹo âm thanh — hình ảnh càng lố bịch càng dính.'
SND = {
    "капуста":   ("ka-PUS-ta",  "<b>CÁ PUỘT TA</b> — con cá trườn vào luống <b>bắp cải</b> nhà ta."),
    "картошка":  ("kar-TOSH-ka","Nghe như <b>“CẠO TÓC-ka”</b> — củ <b>khoai tây</b> gọt vỏ trọc lóc."),
    "блюдо":     ("BLYU-da",    "<b>“BLỬU-đa”</b> — bưng <b>món ăn</b> nóng quá phải kêu lên."),
    "чашка":     ("CHASH-ka",   "<b>“CHÁCH-ka”</b> — tiếng <b>cái tách</b> chạm đĩa."),
    "щётка":     ("SHCHOT-ka",  "<b>“SỌT-ka”</b> — cái <b>bàn chải</b> cọ soàn soạt."),
    "щепка":     ("SHCHEP-ka",  "<b>“SẺ-BÉ-ka”</b> — miếng gỗ bị sẻ ra bé xíu = <b>dằm gỗ</b>."),
    "щука":      ("SHCHU-ka",   "<b>“SÚC-ka”</b> — con <b>cá chó</b> đớp mồi cái “súc”."),
    "слеза":     ("sli-ZA",     "<b>“SLỊ-ZA”</b> — giọt <b>nước mắt</b> trượt (slide) xuống má."),
    "чудо":      ("CHU-da",     "<b>“CHÚ ĐÀ”</b> — chú làm được điều <b>kỳ diệu</b>, ai cũng ồ lên."),
    "земля":     ("zim-LYA",    "<b>“ZIM-LÁ”</b> — mùa đông (zima) lá rụng phủ kín <b>mặt đất</b>."),
    "хотеть":    ("kha-TYET",   "<b>“KHÁT-chết”</b> — khát <b>muốn</b> chết, thèm nước kinh khủng."),
    "видеть":    ("VI-dyet",    "Gần <i>video</i> — cái để <b>nhìn thấy</b>."),
    "думать":    ("DU-mat",     "<b>“ĐU-mát”</b> — đầu mát mẻ mới <b>nghĩ</b> ra được."),
    "гулять":    ("gu-LYAT",    "<b>“GÙ-LẾT”</b> — lưng gù, lết từng bước <b>đi dạo</b>."),
    "играть":    ("i-GRAT",     "Gần <i>game</i> — <b>chơi</b> trò chơi."),
    "целовать":  ("tsy-la-VAT", "<b>“XI-LA-VÁT”</b> — xi bé một cái rồi <b>hôn</b> lên má."),
    "ребёнок":   ("ri-BYO-nak", "<b>“RÍ-BÉ-nốc”</b> — <b>đứa bé</b> rí rí đòi bế."),
    "любовь":    ("lyu-BOF",    "Gốc <b>любить</b> (yêu) → <b>tình yêu</b>. Cuối từ <b>в đọc thành “f”</b>."),
    "счастье":   ("SHAS-tye",   "⚠️ <b>сч đọc thành “sh”</b>. <b>“SHÁT-chê”</b> — sướng phát chê = <b>hạnh phúc</b>."),
    "счастливый":("shas-LI-vyy","Từ <b>счастье</b> (hạnh phúc) + đuôi tính từ. <b>сч vẫn đọc “sh”</b>."),
    "помощь":    ("PO-mashch",  "Gốc <b>помочь</b> (giúp) → <b>sự giúp đỡ</b>."),
    "точка":     ("TOCH-ka",    "<b>“TÓT-ka”</b> — chấm bút một cái “tót” = <b>dấu chấm</b>."),
    "скобка":    ("SKOP-ka",    "<b>“SỎ-CÓP-ka”</b> — hai cái móc kẹp lấy chữ = <b>dấu ngoặc</b>."),
    "язык":      ("yi-ZYK",     "<b>“I-DZÍCH”</b> — thè <b>lưỡi</b> ra mới nói được <b>ngôn ngữ</b>."),
    "богатый":   ("ba-GA-tyy",  "<b>“BÁ GIÀ-tưi”</b> — ông bá hộ già, <b>giàu</b> nứt đố đổ vách."),
    "весёлый":   ("vi-SYO-lyy", "<b>“VI-XÔ-lưi”</b> — vui đến mức xô cả bàn = <b>vui vẻ</b>."),
    "острый":    ("OS-tryy",    "<b>“ỐT-trưi”</b> — cắn quả ớt, vừa <b>cay</b> vừa <b>nhọn</b> lưỡi."),
    "слабый":    ("SLA-byy",    "Gần <i>slack/slap</i> — lỏng lẻo, <b>yếu</b> ớt."),
    "нужный":    ("NUZH-nyy",   "<b>“NÚT-nhưi”</b> — cái nút bấm <b>cần thiết</b>, thiếu là hỏng việc."),
    "настоящий": ("nas-ta-YA-shchiy", "<b>“NÁT-TÀ-YÁ-shi”</b> — đập nát ra xem mới biết đồ <b>thật</b>."),
    "каждый":    ("KAZH-dyy",   "<b>“CẠ-ZI-đưi”</b> — cạ vai từng người, <b>mỗi</b> người một cái."),
    "другой":    ("dru-GOY",    "Gốc <b>друг</b> (bạn) → “người kia” = cái <b>khác</b>."),
    "какой":     ("ka-KOY",     "<b>“CA-CÓI”</b> — chỉ vào mà hỏi “cái coi nào?” = <b>cái nào</b>."),
    "некоторый": ("NHE-ka-ta-ryy", "<b>не</b> + <b>который</b>(cái mà) → “cái nào đó không rõ” = <b>một vài</b>."),
    "только":    ("TOL-ka",     "<b>“TỎN-ka”</b> — gọn lỏn có bấy nhiêu = <b>chỉ</b> thế thôi."),
    "между":     ("MYEZH-du",   "<b>“MẸ-ZỜ-đu”</b> — mẹ đứng <b>giữa</b> hai đứa con."),
    "себя":      ("si-BYA",     "<b>“XI-BIA”</b> — tự rót bia cho <b>chính mình</b>."),
    "они":       ("a-NHI",      "<b>“A-NHÍ”</b> — <i>anh + nị</i> = <b>họ</b>, mấy người kia."),
    "или":       ("I-li",       "<b>“Í-li”</b> — <i>ý này li kia</i>, chọn một = <b>hoặc</b>."),
    "его":       ("yi-VO",      "<b>của anh ấy</b>. ⚠️ <b>г đọc thành “v”</b>."),
    "часто":     ("CHAS-ta",    "<b>“CHẠY-TỚ”</b> — chạy tới chạy lui <b>thường xuyên</b>."),
    "дачка":     ("DACH-ka",    "Từ <b>дача</b> (nhà vườn ngoại ô) + <b>-ка</b> làm nhỏ đi → nhà vườn xinh xắn."),
    "пощада":    ("pa-SHCHA-da","<b>“PHA-SÁ-đa”</b> — tha cho một mạng = <b>lòng khoan dung</b>."),
    "будничный": ("BUD-nhich-nyy", "Gốc <b>будни</b> (ngày thường, ngày đi làm) → tẻ nhạt, thường ngày."),
    "воскресение":("vas-kri-SYE-nhiye", "Gốc <b>воскреснуть</b> (sống lại) → <b>sự phục sinh</b>."),
    "глагол":    ("gla-GOL",    "<b>“GÀ-GỌI”</b> — gà gáy gọi sáng, gáy là một <b>động từ</b>."),
}
for w, (rd, body) in SND.items():
    M[w] = (rd, body, SND_TIP)

# một số ca đặc biệt cần tip riêng, ghi đè lên SND_TIP ở trên
M["счастье"]     = M["счастье"][:2]     + ('⚠️ Luật <b>сч → “sh”</b>: счастье, счастливый, счёт. Nhớ luật, khỏi nhớ từng từ.',)
M["счастливый"]  = M["счастливый"][:2]  + ('⚠️ Luật <b>сч → “sh”</b>, và <b>т câm</b> giữa "с-т-л". Đọc "shas-LI-vyy".',)
M["его"]         = M["его"][:2]         + ('⚠️ Luật <b>г → “v”</b> ở đuôi -ого/-его: его, сегодня, всего, ничего. Một luật, nhiều từ.',)
M["любовь"]      = M["любовь"][:2]      + ('Cùng gốc <b>любить</b> (yêu). Phụ âm cuối luôn bị điếc: в→f, б→p, з→s, д→t.',)
M["воскресение"] = M["воскресение"][:2] + ('Đừng lẫn với <b>воскресенье</b> (Chủ nhật) — chỉ khác chữ ь, và Chủ nhật đúng là "ngày phục sinh".',)
M["видеть"]      = M["видеть"][:2]      + ('Cặp thể: <b>видеть</b> (nhìn thấy) → <b>увидеть</b> (thấy được, xong). Tiền tố у- đóng việc lại.',)

# ============================================================
# HỌ 8 — TỪ MƯỢN QUỐC TẾ: user có tiếng Anh B2, chỉ cần CHỈ MẶT từ tiếng Anh
# ============================================================
ENG_TIP = ('Nhóm từ mượn quốc tế: <b>bạn đã biết nghĩa sẵn qua tiếng Anh</b>. '
           'Việc duy nhất phải học là <b>cách đọc kiểu Nga và trọng âm</b> — đừng tốn công học nghĩa.')
ENG = {
    "актриса":     ("ak-TRI-sa",        "actress"),
    "аналогичный": ("a-na-la-GHICH-nyy","analogical / analogous"),
    "бизнесмен":   ("biz-nhes-MHEN",    "businessman"),
    "билет":       ("bi-LYET",          "billet → <i>ticket</i> (vé)"),
    "буфет":       ("bu-FYET",          "buffet (quầy ăn)"),
    "грамматика":  ("gra-MA-ti-ka",     "grammar"),
    "диалог":      ("di-a-LOK",         "dialogue"),
    "диктант":     ("dik-TANT",         "dictation (bài chính tả)"),
    "императив":   ("im-pi-ra-TIF",     "imperative (thức mệnh lệnh)"),
    "инженер":     ("in-zhy-NHER",      "engineer"),
    "конструкция": ("kan-STRUK-tsy-ya", "construction"),
    "конфета":     ("kan-FYE-ta",       "confection / <i>comfit</i> → cái kẹo"),
    "музей":       ("mu-ZYEY",          "museum"),
    "музыка":      ("MU-zy-ka",         "music"),
    "натуральный": ("na-tu-RAL-nyy",    "natural"),
    "нормальный":  ("nar-MAL-nyy",      "normal"),
    "помидор":     ("pa-mi-DOR",        "pomodoro (tiếng Ý) → quả cà chua"),
    "профессор":   ("pra-FYE-sar",      "professor"),
    "реплика":     ("RYE-pli-ka",       "replica / reply → lời thoại, lời nhận xét"),
    "салат":       ("sa-LAT",           "salad"),
    "спортивный":  ("spar-TIV-nyy",     "sportive → thuộc thể thao"),
    "физик":       ("FI-zik",           "physicist"),
    "физика":      ("FI-zi-ka",         "physics"),
    "фирма":       ("FIR-ma",           "firm (công ty)"),
    "форма":       ("FOR-ma",           "form"),
    "шоколад":     ("sha-ka-LAT",       "chocolate"),
    "шофёр":       ("sha-FYOR",         "chauffeur (tiếng Pháp) → tài xế"),
    "экономист":   ("e-ka-na-MIST",     "economist"),
    "юридический": ("yu-ri-DHI-chis-kiy","juridical (thuộc pháp lý)"),
    "юрист":       ("yu-RIST",          "jurist (luật sư)"),
    "центральный": ("tsyn-TRAL-nyy",    "central"),
    "танцевать":   ("tan-tsy-VAT",      "to dance"),
    "модный":      ("MOD-nyy",          "mode / modern → hợp mốt"),
    "спорт":       ("SPORT",            "sport"),
    "текст":       ("TYEKST",           "text"),
    "тест":        ("TYEST",            "test"),
    "тип":         ("TIP",              "type (kiểu, loại)"),
    "курс":        ("KURS",             "course (khoá học)"),
    "борщ":        ("BORSHCH",          "borscht — món canh củ dền Nga, tiếng Anh mượn ngược lại"),
}
for w, (rd, eng) in ENG.items():
    M[w] = (rd, f"Chính là <b>{eng}</b> trong tiếng Anh.", ENG_TIP)

# ============================================================
# HỌ 9 — TỪ NGẮN 1 ÂM TIẾT: nhiều từ là HỌ HÀNG XA của tiếng Anh
# ============================================================
COG_TIP = ('Nga và Anh cùng gốc Ấn–Âu nên nhiều từ cổ là <b>họ hàng xa</b>. '
           'Nhận ra họ hàng là nhớ được ngay mà không cần mẹo.')
M["дочь"]  = ("DOCH",  "Họ hàng với <b>daughter</b> (d–ch ↔ d–ght).", COG_TIP)
M["мышь"]  = ("MYSH",  "Họ hàng với <b>mouse</b> (mysh ↔ mouse).", COG_TIP)
M["хлеб"]  = ("KHLYEP","Họ hàng với <b>loaf</b> (gốc Giéc-manh <i>hlaif</i>). Cuối từ <b>б → “p”</b>.", COG_TIP)
M["лён"]   = ("LYON",  "Họ hàng với <b>linen</b> (cây lanh).", COG_TIP)
M["рожь"]  = ("ROSH",  "Họ hàng với <b>rye</b> (lúa mạch đen — làm bánh mì đen Nga).", COG_TIP)
M["лев"]   = ("LYEF",  "Họ hàng với <b>lion</b> / cung <b>Leo</b>. Cuối từ <b>в → “f”</b>.", COG_TIP)
M["дать"]  = ("DAT",   "Họ hàng với <b>donate</b> / cách <i>dative</i> (cách cho).", COG_TIP)

ROOT_TIP = 'Từ ngắn này là <b>gốc</b> của cả một chùm từ dài — thuộc nó là lời to.'
M["род"]  = ("ROT",   "Dòng dõi. Gốc của <b>родиться</b>(sinh ra), <b>родной</b>(ruột thịt), родина(quê hương).", ROOT_TIP)
M["щит"]  = ("SHCHIT","Cái khiên. Gốc của <b>защита</b> (sự bảo vệ = núp sau khiên).", ROOT_TIP)
M["счёт"] = ("SHCHOT","Sự đếm/tính. Gốc của <b>зачёт</b> (bài đánh giá). ⚠️ <b>сч → “sh”</b>.", ROOT_TIP)
M["жить"] = ("ZHYT",  "Sống. Gốc của <b>жительство</b> (nơi cư trú), жизнь(cuộc đời).", ROOT_TIP)
M["плач"] = ("PLACH", "Tiếng khóc — danh từ của <b>плакать</b> (khóc).", ROOT_TIP)
M["мочь"] = ("MOCH",  "Có thể. Gốc của <b>помощь</b> (sự giúp đỡ) và помочь (giúp).", ROOT_TIP)
M["цвет"] = ("TSVYET","Màu sắc. Cùng gốc với цветок (bông hoa) — hoa là thứ có màu.", ROOT_TIP)

SHORT_TIP = 'Từ một âm tiết: học bằng <b>hình ảnh</b> hoặc <b>cặp gần giống</b>, đừng chẻ gốc làm gì.'
M["врач"] = ("VRACH", "Gốc cổ <b>врать</b> (nói/đọc thần chú) — thầy lang xưa chữa bệnh bằng lời khấn.", SHORT_TIP)
M["час"]  = ("CHAS",  "Giờ. Học cặp vần với <b>чех</b> (người Séc): час–чех, chỉ khác nguyên âm.", SHORT_TIP)
M["чех"]  = ("CHEKH", "Người Séc (Czech). Học cặp vần với <b>час</b> (giờ).", SHORT_TIP)
M["луч"]  = ("LUCH",  "Tia sáng. Học cặp vần với <b>плач</b>(khóc), <b>грач</b>(quạ) — bộ ba đuôi -ч.", SHORT_TIP)
M["грач"] = ("GRACH", "Con quạ khoang — kêu “grách grách”. Cặp vần với <b>луч, плач</b>.", SHORT_TIP)
M["щи"]   = ("SHCHI", "Canh bắp cải Nga. Từ ngắn nhất tiếng Nga, chỉ 2 chữ cái.", SHORT_TIP)
M["плащ"] = ("PLASHCH","Áo mưa. Cặp vần với <b>борщ, хвощ</b> — bộ ba đuôi <b>-щ</b>.", SHORT_TIP)
M["хвощ"] = ("KHVOSHCH","Cỏ đuôi ngựa — gốc <b>хвост</b> (cái đuôi). Cặp vần với <b>плащ, борщ</b>.", SHORT_TIP)
M["вещь"] = ("VYESHCH","Đồ vật, thứ. Đuôi <b>-щь</b> → danh từ <b>giống cái</b>.", SHORT_TIP)
M["лёд"]  = ("LYOT",  "Băng, đá lạnh. Cặp vần với <b>лес</b>(rừng) — băng và rừng, cùng “lyo/lye”.", SHORT_TIP)
M["лес"]  = ("LYES",  "Rừng. Cặp vần với <b>лёд</b> (băng).", SHORT_TIP)
M["съезд"]= ("SYEST", "<b>с</b>(lại) + <b>езд</b>(đi) → đi tụ lại = đại hội. Cùng họ dấu <b>ъ</b> với подъезд/разъезд.", ROOT_TIP)

GRAM_TIP = 'Đây là <b>từ công cụ</b> (giới từ / liên từ). Học bằng <b>cụm mẫu</b>, đừng học nghĩa lẻ.'
M["и"]     = ("I",    "“và”. Cụm mẫu: <i>я и ты</i> = tôi và bạn.", GRAM_TIP)
M["а"]     = ("A",    "“còn / nhưng mà” — nối hai vế <b>đối nhau nhẹ</b>. <i>Я студент, а он врач.</i>", GRAM_TIP)
M["не"]    = ("NHE",  "Phủ định, đặt <b>ngay trước</b> từ bị phủ định. <i>Я не знаю</i> = tôi không biết.", GRAM_TIP)
M["по"]    = ("PA",   "“theo / dọc theo”. Có mặt trong почему, потому, по-русски.", GRAM_TIP)
M["у"]     = ("U",    "“ở chỗ ai”. Cụm mẫu <b>у меня есть</b> = tôi có (nghĩa đen: ở chỗ tôi có).", GRAM_TIP)
M["про"]   = ("PRA",  "“về, nói về”. <i>про меня</i> = về tôi. Cũng là tiền tố “làm trọn” (прочитать).", GRAM_TIP)
M["за"]    = ("ZA",   "“sau / vì / đổi lấy”. Có trong <b>замужем</b>(sau lưng chồng), <b>забыть</b>(đẩy ra sau).", GRAM_TIP)
M["вслух"] = ("FSLUKH","<b>в</b>(vào) + <b>слух</b>(thính giác) → “vào tai” = đọc thành tiếng.", ROOT_TIP)

M = {k: v for k, v in M.items() if v[1]}   # bỏ entry rỗng
