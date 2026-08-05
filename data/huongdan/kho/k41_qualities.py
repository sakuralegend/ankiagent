# -*- coding: utf-8 -*-
"""k41 — qualities: tính từ chỉ tính chất, trục chính là DANH TỪ + hậu tố -н-
thành TÍNH TỪ, và luật "ё luôn mang trọng âm" lộ ra ở dạng ngắn.

Không có khối dùng chung: mỗi luật được nói bằng MỘT câu về chính từ đó
(README §3). Câu 📋 về dạng ngắn CHỈ viết khi bảng chia thật sự lệch — từ nào
chỉ chèn -е- giống đực mà trọng âm đứng yên thì đó là quy tắc, không ghi.
"""

S = {}
V = {}

# --------------------------------------------------------------- to / nhỏ
S["большой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">больш-</span>'
    '<span class="hd-gloss">lớn — cũng là gốc của <b>бо́льше</b> (hơn)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́й</span>'
    '<span class="hd-gloss">đuôi tính từ, trọng âm rơi vào đuôi</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một gốc <b>больш-</b> dùng cho cả ba từ hay gặp: <b>большо́й</b> to, '
    '<b>бо́льше</b> hơn, <b>большинство́</b> đa số. Đây là từ mặc định cho mọi thứ to — cỡ, '
    'số lượng, tuổi: <b>большо́й го́род</b>, <b>больша́я семья́</b>.</div>'
    '<div class="hd-warn">🔴 <b>большо́й</b> nói cỡ NÓI CHUNG; <b>кру́пный</b> chỉ dùng khi '
    'ngầm so với cái cùng loại nhỏ hơn (hạt to, tờ tiền lớn, nhân vật tầm cỡ).</div>'
    '<div class="hd-warn">⚠️ Dạng ngắn đổi nghĩa thành "quá to so với người dùng": '
    '<b>э́ти ту́фли мне велики́</b> = đôi giày này rộng quá với chân tôi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бо́льше</b> hơn, nhiều hơn · <b>большинство́</b> đa số · '
    '<b>вели́кий</b> vĩ đại (cho <b>большо́й</b> mượn dạng ngắn)</div>'
    '<div class="hd-why">📋 Không có dạng ngắn riêng, mượn của <b>вели́кий</b>: '
    '<b>вели́к · велика́ · велико́ · велики́</b>.</div>'
)
V["большой"] = "to, lớn (cỡ lớn nói chung)"

S["небольшой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не-</span>'
    '<span class="hd-gloss">không</span></div>'
    '<div class="hd-row"><span class="hd-piece">больш-</span>'
    '<span class="hd-gloss">lớn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́й</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Viết LIỀN một chữ vì đây là một tính từ riêng chứ không phải câu '
    'phủ định. Nghĩa đúng là "không lớn lắm, vừa vừa" — <b>небольша́я кварти́ра</b> căn hộ '
    'không rộng, vẫn ở tốt.</div>'
    '<div class="hd-warn">🔴 <b>небольшо́й</b> nhẹ hơn <b>ма́ленький</b>: cái gì bé HẲN thì '
    'dùng <b>ма́ленький</b>, cái gì chỉ "không to lắm" mới là <b>небольшо́й</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>большо́й</b> to, lớn · <b>бо́льше</b> hơn · '
    '<b>большинство́</b> đa số</div>'
)
V["небольшой"] = "không lớn lắm, nho nhỏ (phủ định của to)"

# ------------------------------------------------------------- đẹp / xấu
S["красивый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">крас-</span>'
    '<span class="hd-gloss">đẹp (nghĩa cổ) — cũng là gốc của <b>кра́сный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ив-</span>'
    '<span class="hd-gloss">có phẩm chất đó</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thời cổ <b>крас-</b> nghĩa là ĐẸP, mãi sau mới chuyển sang màu đỏ '
    '— nên <b>Кра́сная пло́щадь</b> ban đầu là "Quảng trường ĐẸP". Hậu tố <b>-ив-</b> gắn '
    'vào gốc để nói "có phẩm chất đó".</div>'
    '<div class="hd-warn">🔴 <b>краси́вый</b> chỉ nói về VẺ NGOÀI nhìn thấy được. "Tốt, hay, '
    'ổn" là <b>хоро́ший</b> — hai từ không thay nhau được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>красота́</b> vẻ đẹp · <b>кра́сный</b> đỏ · '
    '<b>укра́сить</b> trang trí · <b>краси́во</b> đẹp (trạng từ)</div>'
)
V["красивый"] = "đẹp, xinh (đẹp mắt, về vẻ ngoài)"

S["некрасивый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не-</span>'
    '<span class="hd-gloss">không</span></div>'
    '<div class="hd-row"><span class="hd-piece">крас-</span>'
    '<span class="hd-gloss">đẹp</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ивый</span>'
    '<span class="hd-gloss">có phẩm chất đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ghép thẳng từ <b>краси́вый</b>. Tiếng Nga hay chê bằng cách phủ '
    'định cho nhẹ đi, nên <b>некраси́вый</b> là "không đẹp, khó coi" chứ chưa tới mức chửi. '
    'Dùng được cả cho hành vi: <b>некраси́вый посту́пок</b> việc làm không đẹp.</div>'
    '<div class="hd-warn">🔴 Ba từ "xấu" khác nhau: <b>некраси́вый</b> xấu về NHÌN · '
    '<b>плохо́й</b> tồi về CHẤT LƯỢNG · <b>ужа́сный</b> tệ tới mức kinh khủng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>краси́вый</b> đẹp · <b>красота́</b> vẻ đẹp · '
    '<b>некраси́во</b> (làm) không đẹp</div>'
)
V["некрасивый"] = "không đẹp, khó coi (phủ định của đẹp)"

# ------------------- dạng ngắn có trọng âm chạy (và ё chạy theo trọng âm)
S["новый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">нов-</span>'
    '<span class="hd-gloss">mới</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc Ấn–Âu với <i>new</i> / <i>novel</i> tiếng Anh, nên mặt '
    'chữ tự nhắc nghĩa. Nhận ra gốc <b>нов-</b> là đọc được cả họ nhà nó.</div>'
    '<div class="hd-warn">⚠️ <b>Но́вый год</b> = Tết dương lịch, viết hoa chữ đầu và là ngày '
    'lễ lớn nhất của người Nga.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>но́вость</b> tin tức · <b>новичо́к</b> người mới · '
    '<b>обнови́ть</b> làm mới, cập nhật · <b>сно́ва</b> lại một lần nữa</div>'
    '<div class="hd-why">📋 Dạng ngắn <b>нов · нова́ · но́во · но́вы</b>: chỉ giống cái dồn '
    'trọng âm ra đuôi, các dạng kia nhấn gốc.</div>'
)

S["дешёвый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дешёв-</span>'
    '<span class="hd-gloss">rẻ — gốc trơn, không chẻ nhỏ hơn được</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Học theo cặp đối: <b>дешёвый</b> ↔ <b>дорого́й</b> (đắt). Chữ '
    '<b>ё</b> trong tiếng Nga LUÔN mang trọng âm, nên hễ trọng âm rời chỗ thì <b>ё</b> tự '
    'hạ xuống thành <b>е</b> — dạng ngắn cho thấy rõ.</div>'
    '<div class="hd-warn">🔴 Nghĩa xấu đi kèm: <b>дешёвый</b> còn là "rẻ tiền, kém giá trị" '
    '(<b>дешёвый трюк</b> trò rẻ tiền).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дёшево</b> rẻ (trạng từ) · <b>дешеви́зна</b> sự rẻ · '
    '<b>подешеве́ть</b> rẻ đi</div>'
    '<div class="hd-why">📋 Dạng ngắn <b>дёшев · дешева́ · дёшево · дёшевы</b>: trọng âm '
    'chạy lên đầu thì <b>ё</b> chạy theo, còn khi trọng âm ra đuôi (<b>дешева́</b>) thì '
    'không còn <b>ё</b> nào.</div>'
)

S["твёрдый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">твёрд-</span>'
    '<span class="hd-gloss">cứng, chắc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một gốc dùng cho cả nghĩa đen lẫn nghĩa bóng: cứng về vật chất '
    '(bóp không lún) và cứng về ý chí (<b>твёрдо реши́ть</b> quyết định dứt khoát).</div>'
    '<div class="hd-warn">🔴 <b>твёрдый</b> ↔ <b>мя́гкий</b> chính là tên gọi hai loại phụ âm '
    'Nga, và tên hai chữ cái: <b>твёрдый знак ъ</b> / <b>мя́гкий знак ь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>твёрдость</b> độ cứng · <b>твёрдо</b> chắc chắn, dứt khoát · '
    '<b>утвержда́ть</b> khẳng định (<b>д</b> hoá <b>жд</b> lối Slav cổ)</div>'
    '<div class="hd-why">📋 Dạng ngắn <b>твёрд · тверда́ · твёрдо · тверды́</b>: giống cái và '
    'số nhiều dồn trọng âm ra đuôi nên mất <b>ё</b>.</div>'
)
V["твёрдый"] = "cứng, rắn (trái với mềm); dứt khoát, kiên định"

S["тяжёлый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">тяж-</span>'
    '<span class="hd-gloss">sức nặng — gốc của <b>тя́жесть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ёлый</span>'
    '<span class="hd-gloss">đuôi tính từ, trọng âm rơi vào <b>ё</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc là NẶNG CÂN — cái kéo tay xuống. Nghĩa bóng đi thẳng từ '
    'đó: <b>тяжёлая рабо́та</b> việc nặng nhọc, <b>тяжёлый день</b> ngày vất vả.</div>'
    '<div class="hd-warn">🔴 Nặng hay khó: cân nặng thì luôn là <b>тяжёлый</b>, còn bài toán '
    'khó (khó về đầu óc) thì luôn là <b>тру́дный</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тя́жесть</b> sức nặng · <b>тяжело́</b> nặng nề, vất vả (trạng '
    'từ) · <b>тя́жкий</b> nặng nề (giọng trang trọng)</div>'
    '<div class="hd-why">📋 Dạng ngắn <b>тяжёл · тяжела́ · тяжело́ · тяжелы́</b>: chỉ giống '
    'đực giữ <b>ё</b>, ba dạng kia trọng âm ra đuôi nên <b>ё</b> thành <b>е</b>.</div>'
)
V["тяжёлый"] = "nặng (về trọng lượng); nặng nề, vất vả"

# ------------------------------------------------ DANH TỪ + -н- thành TÍNH TỪ
S["коммуникативный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">коммуника-</span>'
    '<span class="hd-gloss">Latin <i>communicare</i> truyền đạt, chia sẻ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тивн-</span>'
    '<span class="hd-gloss">ứng với đuôi <i>-ative/-ive</i> tiếng Anh</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thấy <b>-тивный</b> là gần như chắc chắn có một từ Anh '
    '<i>-ative/-ive</i> tương ứng (<b>акти́вный</b> active, <b>эффекти́вный</b> effective). '
    'Nghĩa là "thuộc về việc giao tiếp": <b>коммуникати́вные на́выки</b> kỹ năng giao '
    'tiếp.</div>'
    '<div class="hd-warn">🔴 Đừng dùng cho người. "Anh ấy cởi mở, dễ bắt chuyện" là '
    '<b>коммуника́бельный</b>; <b>коммуникати́вный</b> là từ sách vở nói về BẢN THÂN sự giao '
    'tiếp (chức năng, kỹ năng).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>коммуника́ция</b> sự giao tiếp, truyền thông · '
    '<b>коммуника́бельный</b> dễ gần, hoà đồng</div>'
)
V["коммуникативный"] = "thuộc về giao tiếp (chức năng, kỹ năng giao tiếp)"

S["трудный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">труд-</span>'
    '<span class="hd-gloss">lao động, công sức (<b>труд</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-</span>'
    '<span class="hd-gloss">biến danh từ thành tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen là "đòi hỏi <b>труд</b>" ⇒ khó. Nên từ này luôn nói về '
    'cái khó phải bỏ CÔNG SỨC hoặc ĐẦU ÓC ra: <b>тру́дный вопро́с</b> câu hỏi khó, '
    '<b>тру́дный язы́к</b> thứ tiếng khó học.</div>'
    '<div class="hd-warn">🔴 Đừng đổi chỗ với <b>тяжёлый</b>: <b>тяжёлый</b> là nặng cân, '
    '<b>тру́дный</b> là khó nghĩ. Việc vừa mệt vừa hóc thì mới dùng cả hai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>труд</b> lao động · <b>тру́дно</b> khó (trạng từ) · '
    '<b>тру́дность</b> khó khăn · <b>трудолюби́вый</b> chăm chỉ</div>'
    '<div class="hd-why">📋 Dạng ngắn <b>тру́ден</b> (chèn <b>-е-</b> cho đọc được) · '
    '<b>трудна́</b> (giống cái nhấn đuôi) · <b>тру́дно · тру́дны</b>.</div>'
)
V["трудный"] = "khó, hóc búa (đòi hỏi công sức, đầu óc)"

S["грязный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">гряз-</span>'
    '<span class="hd-gloss">bùn, đất bẩn (<b>грязь</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-</span>'
    '<span class="hd-gloss">biến danh từ thành tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đi thẳng từ danh từ <b>грязь</b>: dính <b>грязь</b> thì bẩn. Mùa '
    'thu và mùa tan tuyết ở Nga đường đầy bùn nên đây là từ hằng ngày.</div>'
    '<div class="hd-warn">⚠️ Nghĩa bóng dùng y như tiếng Việt: <b>гря́зные де́ньги</b> tiền '
    'bẩn, <b>гря́зная игра́</b> trò chơi bẩn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>грязь</b> bùn, đất bẩn · <b>гря́зно</b> bẩn (trạng từ) · '
    '<b>загрязне́ние</b> sự ô nhiễm</div>'
    '<div class="hd-why">📋 Dạng ngắn <b>гря́зен</b> (chèn <b>-е-</b>) · <b>грязна́</b> — '
    'chỉ giống cái đẩy trọng âm ra đuôi, <b>гря́зно · гря́зны</b> vẫn nhấn gốc.</div>'
)
V["грязный"] = "bẩn, dơ (dính bùn đất, cần rửa)"

S["умный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ум-</span>'
    '<span class="hd-gloss">trí óc, đầu óc (<b>ум</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-</span>'
    '<span class="hd-gloss">biến danh từ thành tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Có <b>ум</b> thì <b>у́мный</b>. Gốc ngắn này mở khoá cả một chùm, '
    'kể cả nghĩa ngược: <b>безу́мный</b> = <b>без</b> (không có) + <b>ум</b> = mất '
    'trí.</div>'
    '<div class="hd-warn">🔴 <b>у́мный</b> là nhanh trí, học giỏi. Còn "khôn ngoan, từng '
    'trải" là <b>му́дрый</b> — người trẻ có thể <b>у́мный</b> chứ khó <b>му́дрый</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ум</b> trí óc · <b>у́мница</b> người giỏi giang · '
    '<b>умне́ть</b> khôn ra · <b>безу́мный</b> điên rồ</div>'
    '<div class="hd-why">📋 Dạng ngắn <b>умён</b> — chỗ chèn nguyên âm chính là chỗ nhấn nên '
    'viết <b>ё</b> chứ không phải <b>е</b>; <b>умна́ · умно́ · умны́</b> đều nhấn đuôi.</div>'
)
V["умный"] = "thông minh, nhanh trí"

S["медленный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">медл-</span>'
    '<span class="hd-gloss">chần chừ, kéo dài — gốc của <b>ме́длить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-енн-</span>'
    '<span class="hd-gloss">mang tính chất đó</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Động từ <b>ме́длить</b> là "chần chừ, để thời gian trôi"; cái gì '
    'mang tính đó thì chậm. Trọng âm bám chặt <b>ме́-</b> ở mọi dạng, kể cả trạng từ.</div>'
    '<div class="hd-warn">✍️ Viết HAI chữ <b>н</b> vì hậu tố là <b>-енн-</b>: '
    '<b>ме́дленный</b>, <b>ме́дленно</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ме́дленно</b> chậm (trạng từ) · <b>ме́длить</b> chần chừ · '
    '<b>заме́длить</b> làm chậm lại</div>'
)

S["длинный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">длин-</span>'
    '<span class="hd-gloss">chiều dài (<b>длина́</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-</span>'
    '<span class="hd-gloss">biến danh từ thành tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc đã có sẵn <b>н</b>, hậu tố thêm một <b>н</b> nữa — đó là lý do '
    'phải viết <b>дли́нный</b> hai chữ <b>н</b>, không phải ngoại lệ cần học thuộc.</div>'
    '<div class="hd-warn">🔴 Dài trong KHÔNG GIAN mới là <b>дли́нный</b> (<b>дли́нная '
    'доро́га</b>). Dài về THỜI GIAN là <b>до́лгий</b> (<b>до́лгий разгово́р</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>длина́</b> chiều dài · <b>дли́ться</b> kéo dài (về thời gian) · '
    '<b>дли́тельный</b> lâu dài</div>'
    '<div class="hd-why">📋 Dạng ngắn <b>дли́нен</b> (giống đực chèn <b>-е-</b> và chỉ còn '
    'một <b>н</b>) · <b>длинна́ · длинно́ · длинны́</b> đều nhấn đuôi.</div>'
)
V["длинный"] = "dài (chiều dài của vật, của đường — không dùng cho thời gian)"

S["деревянный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дерев-</span>'
    '<span class="hd-gloss">cây; gỗ (<b>де́рево</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-янн-</span>'
    '<span class="hd-gloss">làm bằng chất liệu đó</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hậu tố <b>-ян-/-ан-</b> nghĩa là "làm bằng", và thường viết MỘT '
    'chữ <b>н</b>: <b>ко́жаный</b> bằng da, <b>сере́бряный</b> bằng bạc.</div>'
    '<div class="hd-warn">✍️ Đúng ba từ viết HAI <b>н</b>, phải thuộc lòng: '
    '<b>деревя́нный</b> · <b>стекля́нный</b> (bằng thuỷ tinh) · <b>оловя́нный</b> (bằng '
    'thiếc).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>де́рево</b> cây; gỗ · <b>дере́вья</b> những cái cây (số nhiều '
    'bất quy tắc) · <b>деревя́шка</b> mẩu gỗ</div>'
)

S["крупный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">круп-</span>'
    '<span class="hd-gloss">hạt to — gốc của <b>крупа́</b> (tấm, hạt ngũ cốc)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-</span>'
    '<span class="hd-gloss">biến danh từ thành tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc là "hạt to", đối lập với <b>ме́лкий</b> (vụn, mịn). Từ đó '
    'lên nghĩa tầm cỡ: <b>кру́пная компа́ния</b> công ty lớn, <b>кру́пный учёный</b> nhà '
    'khoa học tầm cỡ.</div>'
    '<div class="hd-warn">🔴 Không thay được <b>большо́й</b>: <b>большо́й</b> nói cỡ nói '
    'chung, còn <b>кру́пный</b> luôn ngầm so với cái cùng loại nhỏ hơn.</div>'
    '<div class="hd-warn">⚠️ <b>кру́пные де́ньги</b> không phải "nhiều tiền" mà là tiền tờ '
    'mệnh giá lớn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>крупа́</b> hạt ngũ cốc, tấm · <b>кру́пно</b> ở cỡ lớn · '
    '<b>крупне́йший</b> lớn nhất</div>'
    '<div class="hd-why">📋 Dạng ngắn <b>кру́пен</b> (chèn <b>-е-</b>) · <b>крупна́</b> — chỉ '
    'giống cái nhấn đuôi, <b>кру́пно · кру́пны</b> nhấn gốc.</div>'
)
V["крупный"] = "cỡ lớn, hạt to (so với cái cùng loại); tầm cỡ, quy mô lớn"

S["серный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сер-</span>'
    '<span class="hd-gloss">lưu huỳnh (<b>се́ра</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-</span>'
    '<span class="hd-gloss">biến danh từ thành tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ hoá học hẹp, hầu như chỉ gặp trong vài cụm cố định: <b>се́рная '
    'кислота́</b> axit sunfuric, <b>се́рный исто́чник</b> suối nước lưu huỳnh. Nó nói "thuộc '
    'về <b>се́ра</b>", không phải "có mùi khó chịu".</div>'
    '<div class="hd-warn">🔴 Chỉ hơn kém một chữ <b>н</b> so với <b>се́рый</b> (màu xám), mà '
    'nghĩa thì khác hẳn — đọc kỹ trước khi dịch.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>се́ра</b> lưu huỳnh · <b>серни́стый</b> chứa lưu huỳnh</div>'
)
V["серный"] = "thuộc về lưu huỳnh (axit sunfuric, suối lưu huỳnh)"

S["ужасный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ужас-</span>'
    '<span class="hd-gloss">nỗi kinh hoàng (<b>у́жас</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-</span>'
    '<span class="hd-gloss">biến danh từ thành tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái gì gây <b>у́жас</b> thì <b>ужа́сный</b>. Đời thường dùng nhẹ đi '
    'thành "tệ quá" cho mọi thứ khó chịu: <b>ужа́сная пого́да</b> thời tiết kinh '
    'khủng.</div>'
    '<div class="hd-warn">⚠️ Trạng từ <b>ужа́сно</b> hay đứng trước tính từ với nghĩa "cực '
    'kỳ", kể cả điều tốt: <b>ужа́сно рад</b> = mừng kinh khủng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>у́жас</b> nỗi kinh hoàng · <b>ужа́сно</b> khủng khiếp; cực kỳ · '
    '<b>ужасну́ться</b> hoảng sợ</div>'
)
V["ужасный"] = "khủng khiếp, kinh hoàng (tệ tới mức gây sốc)"
