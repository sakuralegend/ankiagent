# -*- coding: utf-8 -*-
"""k142 — language::communication: cặp thể động từ «nói chuyện, gửi, in, cắt, lấy đi» + 3 danh từ.

Chỗ cần nhất quán trong lô:
(1) gốc -сед- = NGỒI (беседовать/побеседовать) — khớp thẻ беседа (k135): бе- hạ mức tin.
(2) gốc сл-/сыл- = GỬI (прислать/присылать) — khớp послать/посылать; сл → шл ở tương lai (пришлю́).
(3) gốc печат- = IN, ĐÓNG DẤU (печатать/напечатать) — khớp впечатление.
(4) gốc знаком- = QUEN: bản không -ся = giới thiệu NGƯỜI KHÁC; м → мл ở ngôi «я».
(5) gốc здоров- = KHOẺ (здороваться): chào = chúc khoẻ, như здравствуйте.
(6) gốc основ- = NỀN MÓNG (основать/основывать) — khớp основатель (k139), основной.
(7) gốc рез- = CẮT: з → ж ở mọi ngôi (ре́жу, поре́жу).
(8) gốc -ним-/-ня- = LẤY (отнимать/отнять) — khớp занять, понять, снять.
(9) -ыва-/-ива- kéo trọng âm lùi: догова́риваться, осно́вывать.
Họ hàng: không thẻ nào cố ý vắng.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "беседовать": "đàm thoại, đàm đạo",           # RÚT «trò chuyện» — trùng говори́ть, разгова́ривать (đã nạp)
    "прислать": "gửi tới, gửi đến",               # bỏ «(xong)»; «gửi» trơn trùng посла́ть
    "присылать": "gửi tới, gửi đến",              # bỏ «(đến đây)»; «gửi» trơn trùng посыла́ть
    "напечатать": "in, đánh máy, đăng báo",       # bỏ «xong»; «;» → «,»; gloss có publish / run an article
    "печатать": "in, đánh máy, đăng báo",         # «;» → «,»; gloss có publish
    "замолчать": "im bặt, nín thinh, ngừng nói",  # «im lặng» là trạng thái (молча́ть); gloss fall silent / stop speaking
    "познакомить": "giới thiệu làm quen",         # bỏ «(ai với ai)»; «giới thiệu» trơn trùng посове́товать
    "дискуссия": "cuộc tranh luận, cuộc thảo luận",  # «thảo luận» trơn là động từ (обсужда́ть)
    "договариваться": "thoả thuận, thương lượng, hẹn",  # gloss arrange / make arrangements
    "договориться": "thoả thuận, thương lượng, hẹn",    # bỏ «xong», «được»; gloss có negotiate
    "поздороваться": "chào hỏi",                  # bỏ «(một lần)»
    "пятёрка": "điểm 5, điểm xuất sắc",           # bỏ ngoặc; tờ 5 rúp là nghĩa cũ, bỏ
    "основать": "sáng lập, lấy làm cơ sở",        # RÚT «thành lập», «lập ra» — trùng созда́ть, соста́вить (đã nạp)
    "основывать": "sáng lập, lấy làm cơ sở",      # «;» → «,»; «dựa trên» → nghĩa ngoại động của to base
    "порезать": "cắt, xắt",                       # bỏ «(xong)»; «cắt» vẫn trùng наре́зать — xem B.baolen
    "отнять": "lấy đi, tước đi",                  # bỏ «(xong)», đồng bộ với отнима́ть
}

# -------------------------------------------------------------- беседовать
S["беседовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бе-сед-</span>'
    '<span class="hd-gloss"><b>-сед-</b> NGỒI — như <b>бесе́да</b>, <b>сосе́д</b> '
    '(phần <b>бе-</b> chưa chắc nghĩa)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-ть</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Động từ của <b>бесе́да</b>: «NGỒI lại nói với nhau» ⇒ trò chuyện từ tốn, '
    'trao đổi nghiêm túc. Đi với <b>с</b> + cách 5, <b>о</b> + cách 6. Cặp HT: <b>побесе́довать</b>.</div>'
    '<div class="hd-warn"><b>-ова-</b> biến thành <b>-у-</b> khi chia: <b>я бесе́дую, ты бесе́дуешь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бесе́да</b> cuộc trò chuyện · <b>собесе́дник</b> người cùng nói chuyện · '
    '<b>собесе́дование</b> buổi phỏng vấn xin việc</div>'
)

# ------------------------------------------------------------ побеседовать
S["побеседовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">làm thành HOÀN THÀNH, kèm sắc thái «MỘT LÚC»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бесе́довать</span>'
    '<span class="hd-gloss">trò chuyện (gốc <b>-сед-</b> NGỒI)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ngồi nói chuyện MỘT buổi rồi thôi — y khuôn <b>поговори́ть</b>. '
    'Chia như <b>бесе́довать</b>: <b>я побесе́дую</b> (tương lai).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бесе́довать</b> trò chuyện · <b>бесе́да</b> cuộc trò chuyện · '
    '<b>собесе́дник</b> người cùng nói chuyện</div>'
)

# ---------------------------------------------------------------- прислать
S["прислать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">TỚI (về phía người nói)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сл-а́ть</span>'
    '<span class="hd-gloss">gốc GỬI — như <b>посла́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>посла́ть</b> = gửi ĐI; <b>присла́ть</b> = gửi TỚI, và món đồ đã đến nơi: '
    '<b>Пришли́ мне фо́то</b> = Gửi ảnh cho tôi nhé. Cặp CHT: <b>присыла́ть</b>.</div>'
    '<div class="hd-warn">Tương lai đổi <b>сл → шл</b>: <b>пришлю́, пришлёшь</b> — giống <b>пошлю́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>присыла́ть</b> gửi tới (CHT) · <b>посла́ть</b> gửi đi · '
    '<b>посы́лка</b> bưu kiện · <b>посо́л</b> đại sứ</div>'
)

# --------------------------------------------------------------- присылать
S["присылать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">TỚI (về phía người nói)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сыл-а́ть</span>'
    '<span class="hd-gloss">gốc GỬI, dạng <b>сыл</b> của <b>сл</b> (như <b>посыла́ть</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gửi TỚI, lặp lại hoặc đang diễn ra: <b>Он ча́сто присыла́ет пи́сьма</b> = '
    'Anh ấy hay gửi thư về. Chia đều: <b>присыла́ю</b>. Cặp HT: <b>присла́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>присла́ть</b> gửi tới (HT) · <b>посыла́ть</b> gửi đi · '
    '<b>посы́лка</b> bưu kiện</div>'
)

# -------------------------------------------------------------- напечатать
S["напечатать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">tiền tố thể — KHÔNG mang nghĩa riêng ở đây</span></div>'
    '<div class="hd-row"><span class="hd-piece">-печа́т-ать</span>'
    '<span class="hd-gloss">IN — từ <b>печа́ть</b> con dấu, ngành in</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng <b>печа́тать</b>, chỉ thêm <b>на-</b> để thành HOÀN THÀNH: in ra xong, '
    'gõ xong, cho đăng. Chia đều: <b>напеча́таю</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>печа́тать</b> in (CHT) · <b>печа́ть</b> con dấu, báo chí · '
    '<b>впечатле́ние</b> ấn tượng · <b>опеча́тка</b> lỗi in</div>'
)

# ---------------------------------------------------------------- печатать
S["печатать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">печа́т-</span>'
    '<span class="hd-gloss">IN, ĐÓNG DẤU — <b>печа́ть</b> con dấu</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">đuôi động từ, chia đều: <b>печа́таю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ấn con dấu chữ lên giấy ⇒ in; nay cả gõ phím: <b>печа́тать на компью́тере</b> '
    '= đánh máy. <b>впечатле́ние</b> «dấu in vào lòng» = ấn tượng, đúng hình ảnh <i>im-press-ion</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>напеча́тать</b> in (HT) · <b>печа́ть</b> con dấu, báo chí · '
    '<b>впечатле́ние</b> ấn tượng · <b>опеча́тка</b> lỗi in</div>'
)

# --------------------------------------------------------------- замолчать
S["замолчать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">BẮT ĐẦU một trạng thái</span></div>'
    '<div class="hd-row"><span class="hd-piece">-молч-а́ть</span>'
    '<span class="hd-gloss">IM LẶNG — <b>молча́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«BẮT ĐẦU im» ⇒ im bặt, ngừng nói. <b>молча́ть</b> là đang im (trạng thái), '
    '<b>замолча́ть</b> là khoảnh khắc chuyển sang im. Câu quát quen: <b>Замолчи́!</b> = Im đi!</div>'
    '<div class="hd-warn">Đuôi <b>-ать</b> nhưng chia kiểu <b>-ишь</b> như <b>молча́ть</b>: '
    '<b>замолчу́, замолчи́шь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>молча́ть</b> im lặng · <b>молча́ние</b> sự im lặng · '
    '<b>мо́лча</b> lặng lẽ, không nói gì</div>'
)

# --------------------------------------------------------------- знакомить
S["знакомить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">знако́м-</span>'
    '<span class="hd-gloss">QUEN — <b>знако́мый</b>, gốc xa là <b>знать</b> biết</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi động từ «LÀM CHO»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Làm cho QUEN» ⇒ giới thiệu NGƯỜI KHÁC: <b>знако́мить</b> ai (cách 4) '
    '<b>с</b> ai (cách 5). Thêm <b>-ся</b> thành <b>знако́миться</b> = chính mình làm quen.</div>'
    '<div class="hd-warn">Ngôi «я» chen <b>л</b>: <b>я знако́млю</b>, nhưng <b>ты знако́мишь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>познако́мить</b> giới thiệu (HT) · <b>знако́миться</b> làm quen · '
    '<b>знако́мый</b> quen biết · <b>знако́мство</b> sự quen biết</div>'
)

# ------------------------------------------------------------- познакомить
S["познакомить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố thể — KHÔNG mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-знако́м-ить</span>'
    '<span class="hd-gloss">làm cho QUEN (xem <b>знако́мить</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giới thiệu xong một lần: <b>Я познако́мил дру́га с сестро́й</b> = '
    'Tôi giới thiệu bạn với em gái. Ngôi «я» chen <b>л</b>: <b>я познако́млю</b>.</div>'
    '<div class="hd-warn">Có <b>-ся</b> là đổi người làm: <b>Я познако́мился с сестро́й</b> = '
    'TÔI làm quen với cô ấy, không ai giới thiệu cả.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>знако́мить</b> giới thiệu (CHT) · <b>познако́миться</b> làm quen · '
    '<b>знако́мый</b> quen biết · <b>знако́мство</b> sự quen biết</div>'
)

# --------------------------------------------------------------- дискуссия
S["дискуссия"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn Latin <i>discussio</i>, không chẻ theo gốc Nga. Chỉ đuôi đáng nhớ: '
    '<i>-ion</i> → <b>-ия</b>, nên danh từ giống cái.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>discussion</i>: cuộc thảo luận, tranh luận có trao đổi ý kiến. '
    'Cùng khuôn <i>-ion</i> → <b>-ия</b>: <b>ми́ссия</b>, <b>ве́рсия</b>.</div>'
    '<div class="hd-warn">Viết HAI chữ <b>с</b> như tiếng Anh <i>ss</i>: <b>диску́ссия</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дискути́ровать</b> thảo luận, tranh luận</div>'
)

# ---------------------------------------------------------- договариваться
S["договариваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-</span>'
    '<span class="hd-gloss">TỚI ĐÍCH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-говар-</span>'
    '<span class="hd-gloss">NÓI — <b>говори́ть</b> (о → а trước <b>-ива-</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ть-ся</span>'
    '<span class="hd-gloss">chưa hoàn thành + phản thân (nói VỚI NHAU)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Nói với nhau cho TỚI ĐÍCH» ⇒ thương lượng, đang dàn xếp. Cặp HT: '
    '<b>договори́ться</b>. Chia đều: <b>догова́риваюсь</b>.</div>'
    '<div class="hd-warn">Thêm <b>-ива-</b> thì trọng âm lùi và <b>о → а</b>: '
    '<b>договори́ться → догова́риваться</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>говори́ть</b> nói · <b>разгово́р</b> cuộc nói chuyện · '
    '<b>перегово́ры</b> cuộc đàm phán</div>'
)

# ------------------------------------------------------------ договориться
S["договориться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-</span>'
    '<span class="hd-gloss">TỚI ĐÍCH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-говор-и́ть</span>'
    '<span class="hd-gloss">NÓI — <b>говори́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">VỚI NHAU</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nói với nhau tới đích ⇒ đã chốt được: <b>договори́ться с дру́гом о встре́че</b> '
    '= hẹn được với bạn (<b>с</b> + cách 5, <b>о</b> + cách 6). Chia như <b>говори́ть</b>.</div>'
    '<div class="hd-warn"><b>Договори́лись!</b> = Chốt vậy nhé! — câu kết thúc mọi cuộc hẹn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>догова́риваться</b> thoả thuận (CHT) · <b>говори́ть</b> nói · '
    '<b>перегово́ры</b> cuộc đàm phán</div>'
)

# ------------------------------------------------------------- здороваться
S["здороваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">здоро́в-</span>'
    '<span class="hd-gloss">KHOẺ — <b>здоро́вый</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть-ся</span>'
    '<span class="hd-gloss">đuôi động từ + phản thân (VỚI NHAU)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chào nhau = chúc nhau KHOẺ. <b>Здра́вствуйте</b> cũng cùng gốc: '
    '<b>здрав-</b> là dạng cổ của <b>здоров-</b> (như <b>град</b> ↔ <b>го́род</b>).</div>'
    '<div class="hd-warn">Chào AI thì dùng <b>с</b> + cách 5, không phải cách 4: '
    '<b>здоро́ваться с сосе́дом</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поздоро́ваться</b> chào (HT) · <b>здоро́вый</b> khoẻ mạnh · '
    '<b>здоро́вье</b> sức khoẻ</div>'
)

# ----------------------------------------------------------- поздороваться
S["поздороваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố thể — KHÔNG mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-здоро́ваться</span>'
    '<span class="hd-gloss">chào nhau, gốc <b>здоров-</b> KHOẺ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chào một lần rồi xong: <b>Он поздоро́вался со мной</b> = Anh ấy chào tôi. '
    'Vẫn <b>с</b> + cách 5 như <b>здоро́ваться</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>здоро́ваться</b> chào (CHT) · <b>здоро́вый</b> khoẻ mạnh · '
    '<b>здоро́вье</b> sức khoẻ · <b>здра́вствуйте</b> xin chào</div>'
)

# --------------------------------------------------------------- календарь
S["календарь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn Latin <i>calendarium</i> (sổ ghi theo <i>kalendae</i> — ngày đầu tháng), '
    'không chẻ theo gốc Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>calendar</i>. Đuôi <b>-арь</b> là giống ĐỰC, như <b>слова́рь</b> '
    'từ điển.</div>'
    '<div class="hd-warn">Trọng âm nhảy xuống đuôi khi biến cách: <b>календа́рь → календаря́, '
    'календари́</b> — y như <b>слова́рь → словаря́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>календа́рный</b> thuộc lịch (<b>календа́рный год</b> năm dương lịch)</div>'
)

# ----------------------------------------------------------------- пятёрка
S["пятёрка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пят-</span>'
    '<span class="hd-gloss">NĂM — <b>пять</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ёрк-а</span>'
    '<span class="hd-gloss">đuôi gọi tên CON SỐ như một vật (điểm, số xe buýt…)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trường Nga chấm thang 5: <b>пятёрка</b> là loại <b>оце́нка</b> / '
    '<b>отме́тка</b> CAO NHẤT, <b>дво́йка</b> là trượt. <b>получи́ть пятёрку</b> = được điểm 5.</div>'
    '<div class="hd-warn">Số nhiều cách 2 chen <b>о</b>: <b>пятёрок</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пять</b> năm · <b>четвёрка</b> điểm 4 · <b>тро́йка</b> điểm 3 · '
    '<b>дво́йка</b> điểm 2</div>'
)

# ---------------------------------------------------------------- основать
S["основать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">осно́в-</span>'
    '<span class="hd-gloss">NỀN MÓNG — <b>осно́ва</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">ĐẶT NỀN MÓNG ⇒ thành lập: người làm việc đó là <b>основа́тель</b>. '
    'Nghĩa bóng: <b>основа́ть на</b> + cách 6 = lấy làm nền, dựa vào. Cặp CHT: <b>осно́вывать</b>.</div>'
    '<div class="hd-warn">Gần như chỉ gặp ở quá khứ và bị động: <b>Москва́ была́ осно́вана</b> '
    '= Moskva được thành lập. Tương lai <b>осную́</b> rất hiếm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>осно́ва</b> nền tảng · <b>основно́й</b> cơ bản · '
    '<b>основа́тель</b> người sáng lập · <b>основа́ние</b> sự thành lập, căn cứ</div>'
)

# -------------------------------------------------------------- основывать
S["основывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">осно́в-</span>'
    '<span class="hd-gloss">NỀN MÓNG — <b>осно́ва</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-ть</span>'
    '<span class="hd-gloss">hậu tố biến hoàn thành → CHƯA hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đặt nền, lấy làm nền — đang diễn ra hoặc lặp lại. Hay gặp nhất ở dạng '
    '<b>-ся</b>: <b>Фильм осно́вывается на фа́ктах</b> = Phim dựa trên sự thật.</div>'
    '<div class="hd-warn">Thêm <b>-ыва-</b> thì trọng âm lùi: <b>основа́ть → осно́вывать</b>, '
    'chia đều <b>осно́вываю</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>основа́ть</b> thành lập (HT) · <b>осно́ва</b> nền tảng · '
    '<b>основно́й</b> cơ bản · <b>основа́тель</b> người sáng lập</div>'
)

# ---------------------------------------------------------------- порезать
S["порезать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố thể (thêm sắc thái «cắt cho hết, cắt phải»)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ре́з-ать</span>'
    '<span class="hd-gloss">CẮT — <b>ре́зать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp HT của <b>ре́зать</b>: <b>поре́зать хлеб</b> = cắt bánh mì ra. '
    'Tương lai <b>з → ж</b> như gốc: <b>поре́жу, поре́жешь</b>.</div>'
    '<div class="hd-warn"><b>поре́зать па́лец</b> = cắt phải ngón tay, bị đứt tay. '
    'Tự cắt phải mình: <b>поре́заться</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ре́зать</b> cắt (CHT) · <b>наре́зать</b> thái ra từng miếng · '
    '<b>отре́зать</b> cắt rời ra · <b>ре́зкий</b> gắt, đột ngột</div>'
)

# ------------------------------------------------------------------ резать
S["резать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ре́з-</span>'
    '<span class="hd-gloss">CẮT</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>рез-</b> = vết cắt; thêm tiền tố là đổi kiểu cắt: <b>от-</b> rời ra, '
    '<b>на-</b> thành nhiều miếng. Cũng là giết mổ: <b>ре́зать кур</b>. Cặp HT: <b>поре́зать</b>.</div>'
    '<div class="hd-warn"><b>з → ж</b> ở MỌI ngôi hiện tại: <b>ре́жу, ре́жешь, ре́жут</b> '
    '(như <b>писа́ть → пишу́</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поре́зать</b> cắt (HT) · <b>наре́зать</b> thái ra · '
    '<b>отре́зать</b> cắt rời · <b>ре́зкий</b> gắt, đột ngột</div>'
)

# ---------------------------------------------------------------- отнимать
S["отнимать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">RA KHỎI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ним-</span>'
    '<span class="hd-gloss">LẤY — như <b>снима́ть</b>, <b>понима́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">chưa hoàn thành, chia đều: <b>отнима́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">LẤY RA KHỎI tay ai ⇒ tước đi; trong toán là trừ. Người bị lấy đi với '
    '<b>у</b> + cách 2: <b>отнима́ть игру́шку у ребёнка</b>. Cặp HT: <b>отня́ть</b>.</div>'
    '<div class="hd-warn"><b>отнима́ть вре́мя</b> = ngốn thời gian (của ai).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отня́ть</b> lấy đi (HT) · <b>снима́ть</b> cởi, tháo · '
    '<b>занима́ть</b> chiếm · <b>понима́ть</b> hiểu</div>'
)

# ------------------------------------------------------------------ отнять
S["отнять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">RA KHỎI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ня́-ть</span>'
    '<span class="hd-gloss">LẤY — như <b>снять</b>, <b>поня́ть</b>, <b>заня́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Lấy ra khỏi tay ai, xong một lần: <b>отня́ть у</b> + cách 2. '
    'Trong toán: <b>от пяти́ отня́ть два</b> = năm trừ hai.</div>'
    '<div class="hd-warn">Tương lai lộ lại <b>м</b> của gốc <b>-ним-</b>, trọng âm lùi từ ngôi 2: '
    '<b>отниму́, отни́мешь</b> — y như <b>сниму́, сни́мешь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отнима́ть</b> lấy đi (CHT) · <b>снять</b> cởi, tháo · '
    '<b>заня́ть</b> chiếm · <b>поня́ть</b> hiểu</div>'
)

B = {
    "docbangmat": 101,
    "loitubat": 2,   # беседовать: gloss gộp «бе-сед-» = NGỒI (khẳng định quá mức về бе-) → tách, hạ mức tin
                     # дискуссия: viết «-sion → -ссия» rồi lấy ве́рсия làm ví dụ (sai: chỉ một с) → đổi «-ion → -ия»
    "nguonsai": 0,
    "baolen": [
        "VA CHAM KHONG GO DUOC: порезать (PERF) 'cắt, xắt' vẫn trùng «cắt» với наре́зать PERF 'cắt, thái, thái nhỏ' — «cắt» là nghĩa lõi, rút không được",
        "VA CHAM MAY CHUA BAO: резать (IMPF, giữ nguyên 'cắt, xắt') nằm TRỌN trong нареза́ть IMPF 'cắt, thái, xắt' — đề xuất thêm «giết mổ» cho резать (gloss có slaughter/butcher) nếu user cho phép thêm chữ; tôi KHÔNG tự thêm",
        "беседовать: rút «trò chuyện» (trùng говорить/разговаривать), thay bằng 'đàm thoại, đàm đạo' — hơi sách vở, cần duyệt",
        "основать/основывать: bỏ «thành lập, lập ra» (trùng создать/составить) → 'sáng lập, lấy làm cơ sở'; «lấy làm cơ sở» dịch nghĩa to base (on) — cần duyệt",
        "печатать/напечатать: thêm «đăng báo» theo gloss publish / run an article — nghĩa thật nhưng là chữ mới so với field cũ, cần duyệt",
        "замолчать: đổi 'im lặng, nín thinh' → 'im bặt, nín thinh, ngừng nói' (im lặng là trạng thái của молчать; gloss fall silent / stop speaking)",
        "Đã đọc field Vietnamese thật qua AnkiConnect (CHỈ ĐỌC, findNotes+notesInfo lọc note:RU_Word) để đo va chạm; không ghi gì",
    ],
}
