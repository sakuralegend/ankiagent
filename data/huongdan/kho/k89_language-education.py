# -*- coding: utf-8 -*-
"""k89 — language-education: 22 từ A1 TRKI (trường học, sách vở, nhà nước) — phần lớn KHÔNG cùng họ.

Mỗi thẻ soạn độc lập, không khối hệ thống. Chỗ cần nhất quán:
(1) ba họ kéo về chung lô: геогра́фия/гео́граф/географи́ческий, матема́тика/матема́тик,
    эконо́мика — dạy chung MỘT khuôn: -ия/-ика = môn · bỏ đuôi = người · -и́ческий = tính từ,
    và trọng âm nhảy ở mỗi dạng; bản trải đủ nằm ở thẻ географи́ческий, thẻ khác chỉ nói về mình.
(2) khớp khuôn đã có: на- + -ук-/уч- (k86 нау́ка), уч- + -ен- + đuôi người (k84 учени́к).
"""

S = {}

# ------------------------------------------------------------- география
S["география"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">гео-</span>'
    '<span class="hd-gloss">ĐẤT, TRÁI ĐẤT (Hy Lạp)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-граф-</span>'
    '<span class="hd-gloss">VIẾT, MÔ TẢ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ия</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái = môn, ngành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Mô tả trái đất» — chính là <i>geography</i>. Cùng khuôn với '
    '<b>фотогра́фия</b>: bỏ <b>-ия</b> ra là được NGƯỜI làm nghề đó, và trọng âm nhảy '
    'lùi: <b>геогра́фия → гео́граф</b> y như <b>фотогра́фия → фото́граф</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гео́граф</b> nhà địa lý học · <b>географи́ческий</b> thuộc địa lý'
    '</div>'
)

# ---------------------------------------------------------------- географ
S["географ"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">гео-</span>'
    '<span class="hd-gloss">ĐẤT, TRÁI ĐẤT</span></div>'
    '<div class="hd-row"><span class="hd-piece">-граф</span>'
    '<span class="hd-gloss">NGƯỜI VIẾT, người mô tả</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Môn <b>геогра́фия</b> bỏ đuôi <b>-ия</b> ⇒ người làm môn đó. '
    'Trọng âm lùi về <b>гео́-</b> — y như <b>фото́граф</b> nhiếp ảnh gia.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>геогра́фия</b> địa lý · <b>географи́ческий</b> thuộc địa lý · '
    '<b>фото́граф</b> nhiếp ảnh gia</div>'
)

# --------------------------------------------------------- географический
S["географический"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">геогра́ф-</span>'
    '<span class="hd-gloss">thẻ <b>геогра́фия</b> — địa lý</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ческий</span>'
    '<span class="hd-gloss">đuôi tính từ = tiếng Anh <i>-ic, -ical</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi <b>-и́ческий</b> mở khoá cả lớp từ: thấy môn <b>-ия/-ика</b> là '
    'đoán được tính từ, và trọng âm LUÔN rơi vào <b>-и́-</b> ngay trước <b>-ческий</b>: '
    '<b>матема́тика → математи́ческий</b>, <b>эконо́мика → экономи́ческий</b>, '
    '<b>исто́рия → истори́ческий</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>геогра́фия</b> địa lý · <b>гео́граф</b> nhà địa lý học</div>'
)

# ------------------------------------------------------------- математика
S["математика"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">матема́т-</span>'
    '<span class="hd-gloss">ĐIỀU HỌC ĐƯỢC (Hy Lạp <i>máthēma</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ика</span>'
    '<span class="hd-gloss">đuôi = môn, ngành (tiếng Anh <i>-ics</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>mathematics</i>; trọng âm ở <b>-ма́-</b>. Môn <b>-ика</b> '
    'bỏ <b>-а</b> là ra NGƯỜI: <b>матема́тика → матема́тик</b>, như '
    '<b>фи́зика → фи́зик</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>матема́тик</b> nhà toán học · <b>математи́ческий</b> thuộc toán '
    'học</div>'
)

# -------------------------------------------------------------- математик
S["математик"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">матема́тик-</span>'
    '<span class="hd-gloss">thẻ <b>матема́тика</b> bỏ đuôi <b>-а</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Môn và người chỉ cách nhau một chữ <b>-а</b>: <b>матема́тика</b> '
    'là môn (giống cái), <b>матема́тик</b> là người (giống đực) — cùng cặp với '
    '<b>фи́зика / фи́зик</b>. Trọng âm đứng yên ở <b>-ма́-</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>матема́тика</b> môn toán · <b>математи́ческий</b> thuộc toán học'
    '</div>'
)

# --------------------------------------------------------------- экономика
S["экономика"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">эко-</span>'
    '<span class="hd-gloss">NHÀ (Hy Lạp <i>oîkos</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ном-</span>'
    '<span class="hd-gloss">QUẢN, phép tắc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ика</span>'
    '<span class="hd-gloss">đuôi = môn, ngành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Phép quản cái nhà» ⇒ kinh tế — <i>economy, economics</i>. Một '
    'từ gánh cả hai: nền kinh tế lẫn môn kinh tế học. Trọng âm nhảy khắp họ: '
    '<b>эконо́мика</b> · <b>экономи́ст</b> · <b>экономи́ческий</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>экономи́ст</b> nhà kinh tế học · <b>экономи́ческий</b> thuộc '
    'kinh tế</div>'
)

# ------------------------------------------------------------ государство
S["государство"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">госуда́р-</span>'
    '<span class="hd-gloss">VUA, đấng quân chủ (<b>госуда́рь</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ство</span>'
    '<span class="hd-gloss">đuôi danh từ trừu tượng / tập thể, giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cõi của đấng quân chủ» ⇒ nhà nước, quốc gia với tư cách bộ máy '
    'chính trị. Tính từ: <b>госуда́рственный</b> — <b>госуда́рственный язы́к</b> = ngôn ngữ '
    'chính thức.</div>'
    '<div class="hd-warn">Đừng lẫn với <b>страна́</b>: <b>страна́</b> là đất nước (lãnh thổ, '
    'con người — đi du lịch tới một <b>страна́</b>); <b>госуда́рство</b> là bộ máy nhà nước '
    '(có luật, có biên giới, có <b>прави́тельство</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>госуда́рственный</b> thuộc nhà nước</div>'
    '<div class="hd-warn">⚠️ Mức tin: <b>госуда́рь</b> bắt nguồn từ <b>господа́рь</b>, cùng '
    'gốc với <b>господи́н</b> ngài, ông — đây là từ nguyên, không phải luật suy ra được.</div>'
)

# ----------------------------------------------------------- правительство
S["правительство"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">прав-</span>'
    '<span class="hd-gloss">THẲNG, ĐÚNG → điều khiển cho đúng (<b>пра́вить</b> cai trị)'
    '</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́тель-</span>'
    '<span class="hd-gloss">NGƯỜI làm việc đó, như <b>учи́тель</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ство</span>'
    '<span class="hd-gloss">bộ máy, tập thể (như <b>госуда́рство</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>прави́тель</b> = người cai trị ⇒ <b>прави́тельство</b> = cả bộ máy '
    'cai trị = chính phủ. Gốc <b>прав-</b> «thẳng, đúng» là gốc bạn đã gặp ở '
    '<b>пра́вильно</b> và <b>пра́вда</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пра́вильно</b> đúng · <b>пра́вда</b> sự thật · <b>пра́вый</b> '
    'bên phải, đúng · <b>пра́вило</b> quy tắc</div>'
)

# --------------------------------------------------------------- документ
S["документ"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga — mượn nguyên khối từ Latin '
    '<i>documentum</i>, cùng gốc với <i>document</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giống hệt tiếng Anh, chỉ cần nhớ trọng âm ở cuối: '
    '<b>докуме́нт</b>.</div>'
    '<div class="hd-warn">Số nhiều <b>докуме́нты</b> thường là GIẤY TỜ TUỲ THÂN: '
    '<b>Ва́ши докуме́нты!</b> = Xuất trình giấy tờ!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>документа́льный</b> tài liệu, phim tài liệu</div>'
)

# --------------------------------------------------------------------- из
S["из"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Giới từ gốc trơn, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Luôn kéo <b>cách 2</b>. «Từ TRONG ra»: là chiều ngược của '
    '<b>в</b> — vào <b>в шко́лу</b>, ra <b>из шко́лы</b>. Còn chỗ nào dùng <b>на</b> '
    '(<b>на рабо́ту</b>) thì chiều ra là <b>с</b> (<b>с рабо́ты</b>), không phải '
    '<b>из</b>. Nghĩa thứ hai: làm bằng — <b>из де́рева</b> = bằng gỗ.</div>'
    '<div class="hd-warn"><b>Я из Вьетна́ма</b> = Tôi đến từ Việt Nam — câu đầu tiên '
    'bạn sẽ dùng với <b>из</b>.</div>'
)

# ---------------------------------------------------------------- книжный
S["книжный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">книж-</span>'
    '<span class="hd-gloss">SÁCH (<b>кни́га</b>, <b>г</b> hoá <b>ж</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ «thuộc về»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trước <b>-н-</b>, <b>г</b> hoá <b>ж</b>: <b>кни́га → кни́жный</b> — '
    'cùng phép với <b>друг → дру́жба</b>. Hay gặp nhất: <b>кни́жный магази́н</b> = hiệu '
    'sách, nói tắt chỉ còn <b>кни́жный</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кни́га</b> sách · <b>кни́жка</b> cuốn sách nhỏ, sổ</div>'
)

# --------------------------------------------------------------- например
S["например"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на</span>'
    '<span class="hd-gloss">TRÊN, theo</span></div>'
    '<div class="hd-row"><span class="hd-piece">-при́мер</span>'
    '<span class="hd-gloss">VÍ DỤ (<b>приме́р</b>, gốc <b>мер-</b> ĐO, «đem ra so»)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vốn là <b>на приме́р</b> «lấy làm ví dụ» viết dính lại; trọng âm '
    'giữ nguyên ở <b>-ме́-</b>. Chen vào giữa câu, hai bên có dấu phẩy: <b>Я люблю́ '
    'фру́кты, наприме́р, я́блоки</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>приме́р</b> ví dụ · <b>приме́рно</b> khoảng chừng · '
    '<b>разме́р</b> kích cỡ (cùng gốc <b>мер-</b> đo)</div>'
)

# ----------------------------------------------------------------- научный
S["научный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">нау́ч-</span>'
    '<span class="hd-gloss">thẻ <b>нау́ка</b> — khoa học (<b>к</b> hoá <b>ч</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ «thuộc về»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trước <b>-н-</b>, <b>к</b> hoá <b>ч</b>: <b>нау́ка → нау́чный</b>, như '
    '<b>река́ → речно́й</b>. Hay đi với: <b>нау́чный институ́т</b> viện nghiên cứu. Dạng '
    'ngắn giống đực chèn thêm <b>е</b>: <b>нау́чен</b> (ít dùng).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>нау́ка</b> khoa học · <b>учёный</b> nhà khoa học · '
    '<b>учи́ть</b> học, dạy</div>'
)

# ------------------------------------------------------------------ после
S["после"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ theo nghĩa hiện đại được — học nguyên khối.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Kéo <b>cách 2</b>: <b>по́сле обе́да</b> = sau bữa trưa. Trước cả một '
    'mệnh đề thì dùng <b>по́сле того́ как</b>: <b>по́сле того́ как он ушёл</b> = sau khi anh ấy '
    'đi.</div>'
    '<div class="hd-warn">Đừng lẫn với <b>че́рез</b>: <b>по́сле</b> + MỘT VIỆC (sau giờ học), '
    '<b>че́рез</b> + MỘT KHOẢNG thời gian tính từ bây giờ — <b>че́рез час</b> = một tiếng '
    'nữa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>послеза́втра</b> ngày kia · <b>после́дний</b> cuối cùng</div>'
)

# ----------------------------------------------------------------- спасибо
S["спасибо"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">спаси́</span>'
    '<span class="hd-gloss">HÃY CỨU (lệnh của <b>спасти́</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бо</span>'
    '<span class="hd-gloss">CHÚA (<b>Бог</b>, rụng <b>г</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc là lời chúc «Chúa phù hộ (bạn)», mòn dần thành «cảm ơn». Cảm ơn '
    'VÌ cái gì thì <b>за</b> + cách 4: <b>спаси́бо за по́мощь</b>.</div>'
    '<div class="hd-warn">Nó cư xử như danh từ giống trung — nên mới nói '
    '<b>большо́е спаси́бо</b> (đuôi <b>-ое</b>) = cảm ơn nhiều. Đáp lại: '
    '<b>пожа́луйста</b>.</div>'
)

# ------------------------------------------------------------------ статья
S["статья"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ hữu ích cho người học — học nguyên khối.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hai nghĩa đều là «một phần viết tách riêng»: bài trên báo '
    '(<b>статья́ в газе́те</b>) và một điều trong văn bản luật (<b>статья́ зако́на</b>). '
    'Số nhiều cách 2 chèn <b>-е́-</b>: <b>стате́й</b> — đúng như <b>семья́ → семе́й</b>.</div>'
)

# ---------------------------------------------------------------- страница
S["страница"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">стран-</span>'
    '<span class="hd-gloss">MẶT, PHÍA (nghĩa cổ của <b>страна́</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ц-а</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Một mặt của tờ giấy» ⇒ trang. Trang web cũng là '
    '<b>страни́ца</b>.</div>'
    '<div class="hd-warn">Trên trang dùng <b>на</b>, không dùng <b>в</b>: '
    '<b>на страни́це пять</b> = ở trang 5.</div>'
    '<div class="hd-warn">⚠️ Mức tin: nối với <b>страна́</b> là từ nguyên (xưa '
    '<b>страна́</b> nghĩa là «phía»), không phải luật suy ra được.</div>'
)

# ------------------------------------------------------------ студенческий
S["студенческий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">студе́н-</span>'
    '<span class="hd-gloss">thẻ <b>студе́нт</b> — rụng mất <b>т</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ческий</span>'
    '<span class="hd-gloss">đuôi tính từ «thuộc về»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chữ <b>т</b> của <b>студе́нт</b> biến mất khi gắn đuôi — gõ là '
    '<b>студе́нческий</b>, không phải *студентческий. Trọng âm giữ nguyên ở <b>-де́-</b>.'
    '</div>'
    '<div class="hd-warn"><b>студе́нческий биле́т</b> = thẻ sinh viên — cụm hay gặp nhất.'
    '</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>студе́нт</b> sinh viên · <b>студе́нтка</b> nữ sinh viên</div>'
)

# ------------------------------------------------------------- телеграмма
S["телеграмма"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">теле-</span>'
    '<span class="hd-gloss">XA (Hy Lạp)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-грамм-а</span>'
    '<span class="hd-gloss">CHỮ VIẾT</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Chữ gửi đi xa» — <i>telegram</i>. <b>теле-</b> «xa» như '
    '<b>телефо́н</b>, <b>телеви́зор</b>; <b>-грамм-</b> «chữ viết» như '
    '<b>грамма́тика</b>, <b>програ́мма</b>.</div>'
    '<div class="hd-warn">Gõ HAI chữ <b>м</b>: <b>телегра́мма</b> — giống '
    '<b>програ́мма</b>, <b>грамма́тика</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>телефо́н</b> điện thoại · <b>телеви́зор</b> tivi · '
    '<b>програ́мма</b> chương trình · <b>грамма́тика</b> ngữ pháp</div>'
)

# ----------------------------------------------------------------- ученица
S["ученица"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">уч-</span>'
    '<span class="hd-gloss">gốc HỌC / DẠY</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ен-</span>'
    '<span class="hd-gloss">«ĐƯỢC dạy» (như <b>учёный</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ц-а</span>'
    '<span class="hd-gloss">NGƯỜI NỮ — bản giống cái của <b>-и́к</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đổi <b>-и́к → -и́ца</b> là ra người nữ: <b>учени́к → учени́ца</b>. '
    'Khác <b>учени́к</b> (trọng âm chạy xuống đuôi: <b>ученика́</b>), ở đây trọng âm đứng '
    'yên trên <b>-ни́-</b>: <b>учени́цы</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>учени́к</b> học sinh · <b>учи́тельница</b> cô giáo · '
    '<b>учи́ть</b> học, dạy · <b>нау́ка</b> khoa học</div>'
)

# --------------------------------------------------------------- факультет
S["факультет"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga — mượn Latin <i>facultas</i>, như '
    '<i>faculty</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một khoa trong <b>университе́т</b>, trọng âm ở cuối: '
    '<b>факульте́т</b>.</div>'
    '<div class="hd-warn">Học ở khoa nào dùng <b>на</b>, không dùng <b>в</b>: '
    '<b>учи́ться на факульте́те</b> = học ở khoa.</div>'
)

# ------------------------------------------------------------------ фраза
S["фраза"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ — mượn Hy Lạp, như <i>phrase</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa rộng hơn <i>phrase</i>: <b>фра́за</b> thường là cả một CÂU NÓI '
    'trọn vẹn, câu ai đó vừa thốt ra.</div>'
    '<div class="hd-warn">Câu theo nghĩa NGỮ PHÁP (có chủ ngữ, vị ngữ) là '
    '<b>предложе́ние</b>, không phải <b>фра́за</b>.</div>'
)

V = {
    "после": "sau khi",
    "факультет": "khoa",
    "из": "từ, ra khỏi, làm bằng",
    "научный": "thuộc về khoa học, học thuật",
    "географ": "nhà địa lý học",
}
