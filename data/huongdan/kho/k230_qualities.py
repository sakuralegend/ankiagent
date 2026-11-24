# -*- coding: utf-8 -*-
"""k230 — qualities: 3 cặp thể + мчаться, помыться + tính từ tính chất; trục là GỐC + TIỀN TỐ.

Chỗ cần nhất quán trong lô:
(1) измерить / измерять: ме́р- ĐO — khớp мерить k149, размер k14, và примерить k235.
(2) помыться: мы- RỬA — khớp мыть, мыться, вымыться, помыть.
(3) объединиться / объединяться: объ- QUANH + един- MỘT — khớp объединение k178, присоединиться.
(4) наклониться / наклоняться: -клон- CÚI, NGHIÊNG — khớp поклонник k181.
(5) специфика: специ- = species — khớp специальный. жидкий: жидк- LỎNG — khớp жидкость k182.
(6) бумажный: бумаг-/бумаж- — khớp бумага, бумажник. неподвижный: движ- — khớp движение, подвиг k197.
(7) непрерывный: рыв- XÉ, ĐỨT — khớp перерыв k04. автономный: авто- TỰ, -ном- phép tắc (экономика).
(8) интенсивный: -ивн- ~ -ive — khớp объективный k197. глина: -ян- chất liệu — khớp деревянный.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "измерить": "đo, đo lường, đo đạc",                 # «đo xong» là nhãn thể; một dãy với измерять
    "измерять": "đo, đo lường, đo đạc",                 # gloss «survey» = đo đạc
    "объединяться": "hợp nhất, liên kết lại, chung sức",  # một dãy với объединиться; «kết hợp» là việc của соединять
    "наклониться": "cúi xuống, khom người, nghiêng",    # gloss «lean to one side, tilt»: vật cũng nghiêng
    "наклоняться": "cúi xuống, khom người, nghiêng",    # một dãy với наклониться
    "мчаться": "lao nhanh, phóng vun vút, chạy vội, trôi vùn vụt",  # THIẾU nghĩa thời gian (fly by, race by)
    "глина": "đất sét",                                 # «đất thịt» (loam) = суглинок, từ khác
    "жидкий": "lỏng, loãng, thưa",                      # THIẾU sparse (tóc thưa); «thể lỏng» là danh từ
    "неподвижный": "bất động, không nhúc nhích, cố định",  # «tĩnh lặng» nghiêng sang im tiếng (тихий); gloss có fixed
}

# --------------------------------------------------------------------- измерить
S["измерить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">из-</span>'
    '<span class="hd-gloss">RA — đo cho ra con số</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ме́р-</span>'
    '<span class="hd-gloss">gốc ĐO — như <b>ме́рить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi lớp 2, trọng âm đứng yên: <b>изме́рю, изме́ришь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đo ra một CON SỐ: <b>изме́рить температу́ру</b> đo nhiệt độ, <b>изме́рить '
    'ко́мнату</b> đo căn phòng. Khác <b>ме́рить</b>: không có nghĩa thử quần áo. Cặp CHT: '
    '<b>измеря́ть</b>.</div>'
    '<div class="hd-warn">Lệch một chữ với <b>измени́ть</b> thay đổi: gốc <i>мер-</i> đo ↔ '
    '<i>мен-</i> đổi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>измеря́ть</b> (CHT) · <b>измере́ние</b> phép đo; chiều (3D) · '
    '<b>ме́ра</b> thước đo, mức · <b>разме́р</b> cỡ</div>'
)

# --------------------------------------------------------------------- измерять
S["измерять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">из-</span>'
    '<span class="hd-gloss">RA — đo cho ra con số</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мер-</span>'
    '<span class="hd-gloss">gốc ĐO — như <b>ме́рить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành, chia lớp 1</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>изме́рить</b>, đổi <i>-ить → -я́ть</i> và trọng âm nhảy ra đuôi: '
    '<b>измеря́ю, измеря́ешь</b>. Đo đều đặn: <b>ка́ждый день измеря́ть давле́ние</b> đo huyết áp hằng '
    'ngày.</div>'
    '<div class="hd-warn">Đo BẰNG đơn vị gì → <b>в</b> + cách 6 số nhiều: <b>измеря́ть в ме́трах</b> '
    'đo bằng mét.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>изме́рить</b> (HT) · <b>измере́ние</b> phép đo · '
    '<b>примеря́ть</b> mặc thử (cùng khuôn <i>-я́ть</i>) · <b>ме́ра</b> thước đo, mức</div>'
)

# --------------------------------------------------------------------- мчаться
S["мчаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мч-</span>'
    '<span class="hd-gloss">LAO VÚT — gốc trơn, của <b>мчать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть-ся</span>'
    '<span class="hd-gloss">đuôi + <i>-ся</i>: tự mình lao đi</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Lao đi hết tốc lực, về MỘT hướng: <b>мча́ться на вокза́л</b> lao ra ga. Thời gian '
    'cũng lao: <b>Вре́мя мчи́тся</b>. Vừa cất đi là <b>помча́ться</b> (HT).</div>'
    '<div class="hd-warn">Đuôi <i>-ать</i> mà chia LỚP 2, nhấn đuôi: <b>мчусь, мчи́шься, мча́тся</b>. '
    'Vì thế <b>мча́тся</b> «họ lao» nghe y hệt nguyên thể, viết khác đúng một chữ <i>ь</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>помча́ться</b> lao đi (HT) · <b>промча́ться</b> lao vụt qua (HT) · '
    '<b>мчать</b> phóng, chở đi vun vút</div>'
)

# --------------------------------------------------------------------- помыться
S["помыться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">làm XONG một lượt, không thêm nghĩa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мы-</span>'
    '<span class="hd-gloss">RỬA — <b>мыть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть-ся</span>'
    '<span class="hd-gloss">đuôi nguyên thể + phản thân: rửa CHÍNH MÌNH</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tắm xong một lượt — cặp HT thường ngày của <b>мы́ться</b>. Thân đổi '
    '<i>ы → о</i> y như <b>мыть</b>: <b>помо́юсь, помо́ешься</b>; quá khứ giữ <i>ы</i>: <b>помы́лся</b>. '
    'Muốn nhấn SẠCH BONG thì <b>вы́мыться</b>.</div>'
    '<div class="hd-warn">Bỏ <i>-ся</i> là phải có CÁI bị rửa: <b>помы́ть ру́ки</b> rửa tay ↔ '
    '<b>Я помы́лся</b> tôi tắm rồi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мы́ться</b> tắm (CHT) · <b>помы́ть</b> rửa · <b>умы́ться</b> rửa mặt · '
    '<b>мы́ло</b> xà phòng</div>'
)

# --------------------------------------------------------------------- объединиться
S["объединиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">объ-</span>'
    '<span class="hd-gloss">об- QUANH, gom lại; <i>ъ</i> giữ <i>е</i> đọc tách «ye»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-един-</span>'
    '<span class="hd-gloss">MỘT — như <b>еди́ный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть-ся</span>'
    '<span class="hd-gloss">đuôi lớp 2 + <i>-ся</i>: tự mình gom lại</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tự gom quanh thành MỘT khối ⇒ hợp nhất, liên kết. Tương lai: <b>объединю́сь, '
    'объедини́шься</b>. Cặp CHT: <b>объединя́ться</b>.</div>'
    '<div class="hd-warn">Với AI → <b>с</b> + cách 5: <b>объедини́ться с друзья́ми</b>. Thành CÁI GÌ → '
    '<b>в</b> + cách 4: <b>объедини́ться в кома́нду</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>объедине́ние</b> sự hợp nhất · <b>присоедини́ться</b> gia nhập (cái có sẵn) · '
    '<b>еди́ный</b> thống nhất · <b>оди́н</b> một</div>'
)

# --------------------------------------------------------------------- объединяться
S["объединяться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">объ-</span>'
    '<span class="hd-gloss">об- QUANH, gom lại; <i>ъ</i> giữ <i>е</i> đọc tách «ye»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-един-</span>'
    '<span class="hd-gloss">MỘT — như <b>еди́ный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́ть-ся</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành + <i>-ся</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng hình ảnh với <b>объедини́ться</b>: <i>-и́ть → -я́ть</i> là đổi sang CHT, '
    'chia đều lớp 1: <b>объединя́юсь, объединя́ешься</b>. Dùng khi đang hoặc vẫn hay liên kết.</div>'
    '<div class="hd-warn"><b>объединя́ться</b> (с + cách 5) = các bên gom thành một khối; '
    '<b>присоединя́ться</b> (к + cách 3) = một bên nhập VÀO cái đã có.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>объедини́ться</b> (HT) · <b>объедине́ние</b> sự hợp nhất · '
    '<b>соединя́ть</b> nối lại · <b>еди́ный</b> thống nhất</div>'
)

# --------------------------------------------------------------------- наклониться
S["наклониться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">hướng VÀO, tới phía cái gì</span></div>'
    '<div class="hd-row"><span class="hd-piece">-клон-</span>'
    '<span class="hd-gloss">CÚI, NGHIÊNG — như <b>покло́нник</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть-ся</span>'
    '<span class="hd-gloss">đuôi lớp 2 + <i>-ся</i>: nghiêng chính mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghiêng mình về phía trước ⇒ cúi xuống; cây, cột cũng nghiêng được. Trọng âm lùi '
    'từ ngôi «bạn»: <b>наклоню́сь</b>, nhưng <b>накло́нишься</b>; mệnh lệnh <b>Наклони́сь!</b> Cặp CHT: '
    '<b>наклоня́ться</b>.</div>'
    '<div class="hd-warn">Cúi TỚI ai/cái gì → <b>к</b> + cách 3: <b>наклони́ться к ребёнку</b>. Cúi TRÊN '
    'cái gì → <b>над</b> + cách 5: <b>наклони́ться над столо́м</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>накло́н</b> độ nghiêng · <b>поклони́ться</b> cúi chào · '
    '<b>склоне́ние</b> biến cách · <b>наклоне́ние</b> thức (ngữ pháp)</div>'
)

# --------------------------------------------------------------------- наклоняться
S["наклоняться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">hướng VÀO, tới phía cái gì</span></div>'
    '<div class="hd-row"><span class="hd-piece">-клон-</span>'
    '<span class="hd-gloss">CÚI, NGHIÊNG — như <b>покло́нник</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́ть-ся</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành + <i>-ся</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>наклони́ться</b>: cúi nhiều lần, hay đang cúi. Chia đều lớp 1, '
    'trọng âm đứng yên: <b>наклоня́юсь, наклоня́ешься</b>.</div>'
    '<div class="hd-warn">Cúi nhặt đồ, khom lưng còn hay nói <b>нагиба́ться</b> '
    '(HT <b>нагну́ться</b>), gốc <i>гиб-</i> UỐN của <b>ги́бкий</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>наклони́ться</b> (HT) · <b>накло́н</b> độ nghiêng · '
    '<b>накло́нный</b> nghiêng, dốc · <b>покло́н</b> cái cúi chào</div>'
)

# --------------------------------------------------------------------- специфика
S["специфика"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">специ́-</span>'
    '<span class="hd-gloss">Latin <i>species</i> loại riêng — như <b>специа́льный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-фик-а</span>'
    '<span class="hd-gloss">Latin <i>-ficus</i> «làm nên» + đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cái làm nên một loại riêng» ⇒ nét đặc thù; Anh cùng gốc: <i>specific</i>. Của '
    'CÁI GÌ → cách 2: <b>специ́фика рабо́ты</b> đặc thù công việc. Hầu như chỉ dùng số ít. Trọng âm: '
    '<b>специ́фика</b> → <b>специфи́ческий</b>.</div>'
    '<div class="hd-warn"><b>осо́бенность</b> = MỘT nét riêng, đếm được; <b>специ́фика</b> = TOÀN BỘ cái '
    'làm nó khác những cái cùng loại.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>специфи́ческий</b> đặc thù · <b>специа́льный</b> chuyên dụng · '
    '<b>специали́ст</b> chuyên gia · <b>специа́льность</b> chuyên ngành</div>'
)

# --------------------------------------------------------------------- глина
S["глина"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn <i>глин-</i> ĐẤT SÉT, không chẻ được; <i>-а</i> là đuôi giống cái.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chất liệu nên thường chỉ dùng số ít. Làm BẰNG đất sét → <b>из</b> + cách 2: '
    '<b>лепи́ть из гли́ны</b> nặn bằng đất sét. Tính từ lấy đuôi chất liệu <i>-ян-</i>, một chữ <i>н</i>: '
    '<b>гли́няный горшо́к</b> cái nồi đất.</div>'
    '<div class="hd-warn"><b>глинтве́йн</b> rượu vang nóng KHÔNG liên quan: mượn nguyên tiếng Đức '
    '<i>Glühwein</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гли́няный</b> bằng đất sét · <b>гли́нистый</b> (đất) pha sét · '
    '<b>сугли́нок</b> đất thịt</div>'
)

# --------------------------------------------------------------------- жидкий
S["жидкий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">жи́дк-</span>'
    '<span class="hd-gloss">LỎNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một ý «không đặc»: chất lỏng, súp loãng (<b>жи́дкий суп</b>), rồi tóc thưa '
    '(<b>жи́дкие во́лосы</b>). Trái nghĩa ở cả súp lẫn tóc là <b>густо́й</b>; trái với thể lỏng là '
    '<b>твёрдый</b> rắn.</div>'
    '<div class="hd-warn">So sánh hơn vứt <i>к</i>, đổi <i>д → ж</i>: <b>жи́же</b>. Dạng ngắn giống '
    'đực chen <i>о</i> trước <i>к</i>; riêng giống cái nhấn đuôi: <b>жидка́</b>, nhưng <b>жи́дко</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>жи́дкость</b> chất lỏng · <b>жи́жа</b> chất sền sệt, bùn loãng · '
    '<b>разжиди́ть</b> làm loãng</div>'
)

# --------------------------------------------------------------------- кривой
S["кривой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">крив-</span>'
    '<span class="hd-gloss">CONG, LỆCH — gốc trơn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́й</span>'
    '<span class="hd-gloss">đuôi tính từ, nhấn đuôi</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trái nghĩa thẳng của <b>прямо́й</b>, và chạy trọng âm y như nó: dạng ngắn <b>крив, '
    'крива́, кри́во</b>, chỉ giống cái nhấn đuôi. <b>криво́е зе́ркало</b> gương méo, <b>крива́я '
    'улы́бка</b> nụ cười méo xệch.</div>'
    '<div class="hd-warn"><b>крива́я</b> đứng một mình là DANH TỪ: đường cong, đường biểu đồ (hiểu ngầm '
    '<b>ли́ния</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кри́во</b> xiên xẹo · <b>кривизна́</b> độ cong · '
    '<b>искриви́ть</b> làm cong, làm méo</div>'
)

# --------------------------------------------------------------------- интенсивный
S["интенсивный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">интенс-</span>'
    '<span class="hd-gloss">Latin <i>intens-</i> CĂNG ra — Anh <i>intense</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́вн-ый</span>'
    '<span class="hd-gloss">đuôi tính từ quốc tế, = Anh <i>-ive</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>intensive</i>: dồn nhiều trong ít thời gian — <b>интенси́вный курс</b> '
    'khoá cấp tốc, <b>интенси́вное движе́ние</b> xe cộ dày đặc. Sức mạnh của người thì là '
    '<b>си́льный</b>. Dạng ngắn chèn <i>е</i>: <b>интенси́вен</b>.</div>'
    '<div class="hd-warn"><b>интенси́вная терапи́я</b> = chăm sóc đặc biệt, hồi sức (ICU).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>интенси́вно</b> dồn dập · <b>интенси́вность</b> cường độ · '
    '<b>интенси́в</b> khoá cấp tốc</div>'
)

# --------------------------------------------------------------------- непрерывный
S["непрерывный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не-</span>'
    '<span class="hd-gloss">KHÔNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пре-</span>'
    '<span class="hd-gloss">dạng sách vở của <i>пере-</i>: cắt ngang giữa chừng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ры́в-</span>'
    '<span class="hd-gloss">XÉ, ĐỨT — như <b>переры́в</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Không có chỗ đứt» ⇒ liên tục: <b>непреры́вный дождь</b> mưa không ngớt. Dạng ngắn '
    'chèn <i>е</i>: <b>непреры́вен</b>.</div>'
    '<div class="hd-warn"><b>постоя́нный</b> = lúc nào cũng có, lâu dài (<b>постоя́нный а́дрес</b>); '
    '<b>непреры́вный</b> = chạy liền một mạch, không quãng nghỉ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>непреры́вно</b> liên tục · <b>прерыва́ть</b> ngắt, ngắt lời · '
    '<b>переры́в</b> giờ nghỉ · <b>рвать</b> xé</div>'
)

# --------------------------------------------------------------------- бумажный
S["бумажный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бума́ж-</span>'
    '<span class="hd-gloss">GIẤY — <b>бума́га</b>, г → ж</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi biến danh từ thành tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm bằng giấy: <b>бума́жный стака́н</b> cốc giấy, <b>бума́жные де́ньги</b> tiền '
    'giấy; <b>бума́жная кни́га</b> là sách in, đối với sách điện tử. Tính từ chất liệu: dạng ngắn có in '
    'trong bảng nhưng thực tế không dùng.</div>'
    '<div class="hd-warn"><b>хлопчатобума́жный</b> là bằng vải BÔNG (cotton), không phải bằng giấy — trên '
    'nhãn áo viết tắt <i>х/б</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бума́га</b> giấy · <b>бума́жник</b> ví · <b>бума́жка</b> mảnh giấy</div>'
)

# --------------------------------------------------------------------- неподвижный
S["неподвижный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не-</span>'
    '<span class="hd-gloss">KHÔNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-по-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дви́ж-</span>'
    '<span class="hd-gloss">ĐẨY, XÊ DỊCH — <i>двиг-</i>, г → ж, như <b>движе́ние</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Không xê dịch» ⇒ bất động: <b>неподви́жный взгляд</b> cái nhìn đờ ra. Bỏ '
    '<i>не-</i> là ngược lại: <b>подви́жный</b> linh hoạt, hiếu động. Dạng ngắn chèn <i>е</i>: '
    '<b>неподви́жен</b>.</div>'
    '<div class="hd-warn">Cùng gốc, rất hay gặp: <b>недви́жимость</b> BẤT ĐỘNG SẢN — «thứ không dời đi '
    'được».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>неподви́жно</b> bất động (trạng từ) · <b>дви́гаться</b> di chuyển · '
    '<b>движе́ние</b> chuyển động</div>'
)

# --------------------------------------------------------------------- автономный
S["автономный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">авто-</span>'
    '<span class="hd-gloss">TỰ (Hy Lạp, như Anh <i>auto-</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-но́м-</span>'
    '<span class="hd-gloss">PHÉP TẮC, quản (Hy Lạp) — như trong <b>эконо́мика</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Tự đặt phép tắc cho mình» ⇒ tự trị — Anh <i>autonomous</i>: <b>автоно́мная '
    'о́бласть</b> tỉnh tự trị. Máy móc thì là tự chạy một mình, không cần nguồn ngoài: <b>автоно́мный '
    'режи́м</b>. Dạng ngắn chèn <i>е</i>: <b>автоно́мен</b>.</div>'
    '<div class="hd-warn">Nước độc lập hẳn là <b>незави́симый</b>; vùng <b>автоно́мный</b> là tự quản '
    'BÊN TRONG một nước.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>автоно́мия</b> quyền tự trị · <b>автоно́мно</b> một cách độc lập · '
    '<b>автома́т</b> máy tự động</div>'
)

# --------------------------------------------------------------------- просторный
S["просторный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">просто́р-</span>'
    '<span class="hd-gloss">KHOẢNG RỘNG MỞ — danh từ <b>просто́р</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhiều khoảng trống để cựa: phòng rộng, áo rộng. Trái nghĩa <b>те́сный</b> chật; còn '
    '<b>широ́кий</b> trước hết là rộng bề NGANG. Dạng ngắn chèn <i>е</i>: <b>просто́рен</b>. Câu không chủ '
    'ngữ: <b>Здесь просто́рно</b> ở đây rộng rãi.</div>'
    '<div class="hd-warn">Không dính gì tới <b>просто́й</b> đơn giản hay <b>проси́ть</b> xin.</div>'
    '<div class="hd-warn">⚠️ Mức tin: từ nguyên — <b>просто́р</b> = <i>про-</i> + <i>стор-</i> «trải ra», '
    'cùng gốc <b>сторона́</b> phía.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>просто́р</b> khoảng rộng mở · <b>простра́нство</b> không gian · '
    '<b>просто́рно</b> rộng rãi</div>'
)

# --------------------------------------------------------------------- изящный
S["изящный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">изя́щ-</span>'
    '<span class="hd-gloss">THANH NHÃ — ngày nay không chẻ nhỏ hơn được</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đẹp vì thanh, nhẹ, gọn: <b>изя́щная фигу́ра</b> dáng thanh mảnh, <b>изя́щный '
    'по́черк</b> nét chữ thanh thoát. Đẹp chung chung chỉ cần <b>краси́вый</b>. Dạng ngắn chèn <i>е</i>: '
    '<b>изя́щен</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: từ nguyên — tiếng Slav cổ <i>из-</i> RA + gốc LẤY (của <b>взять</b>) '
    '= «được chọn ra», đúng kiểu Anh <i>elegant</i> từ Latin <i>eligere</i> «chọn ra».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>изя́щество</b> sự thanh lịch · <b>изя́щно</b> một cách duyên dáng · '
    '<b>изя́щные иску́сства</b> mỹ thuật</div>'
)

B = {
    "docbangmat": 120,
    "loitubat": 3,   # интенсивный: viết sức gió không dùng интенси́вный (gió, mưa vẫn dùng được) -> chỉ giữ sức người
                     # просторный: «широ́кий chỉ nói bề ngang» nói quá (còn nghĩa bóng) -> «trước hết là»
                     # автономный: gán незави́симый cho «người tự lập» (đó là самостоя́тельный) -> bỏ vế đó
    "nguonsai": 2,   # глина «loam / đất thịt» = сугли́нок, từ khác -> bỏ khỏi V
                     # бумажный: dạng ngắn бума́жен / бума́жена / бумажены máy tự sinh -> thẻ nói thực tế không dùng
    "baolen": [
        "V cần duyệt (9 thẻ): измерить / измерять (cùng dãy; BỎ «đo xong», «lấy số đo», THÊM «đo đạc») · объединяться (cùng dãy với объединиться, BỎ «kết hợp») · наклониться / наклоняться (cùng dãy) · мчаться (THÊM trôi vùn vụt) · глина (BỎ đất thịt) · жидкий (THÊM thưa, BỎ thể lỏng) · неподвижный (BỎ tĩnh lặng, THÊM cố định).",
        "Trùng hết nghĩa trong lô chỉ có 3 cặp thể (измер-, объедин-, наклон-) — badge thể tách. Chưa chạy lại vacham với V mới (không đọc Anki).",
        "неподвижный: V bỏ «tĩnh lặng» nhưng câu ví dụ mặt hồ trong _opus_k230 vẫn dịch «tĩnh lặng» (hợp văn cảnh hồ, không sửa).",
        "специфика: ví dụ _opus «о спецификах разных рынков» dùng số nhiều, không tự nhiên (từ này hầu như chỉ số ít) — nên đổi câu ví dụ.",
        "кривой: ví dụ _opus «Стол какой-то кривой» dịch «hơi méo»; hợp cảnh cốc trượt là «vẹo, nghiêng» — nên sửa bản dịch.",
        "жидкий: từ điển chỉ có DANH TỪ nên so nhầm dạng ngắn жи́док với danh từ đồng tự (nhấn cuối). Không thêm MIEN_TRU: thẻ tả dạng này bằng lời («chen о trước к»), bảng chia trên thẻ vẫn in đủ.",
        "Mức tin ghi trên thẻ: просторный (про- + стор- ~ сторона), изящный (из- + LẤY; elegant ~ eligere). Từ nguyên theo trí nhớ, không tra được trong repo; thêm: специфика -фик- ~ Latin -ficus, глинтвейн < Glühwein.",
        "Không chắc: на- trong наклониться «hướng vào» là cách hiểu theo nghĩa; из- trong измерить «RA con số» cũng vậy.",
    ],
}
