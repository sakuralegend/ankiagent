# -*- coding: utf-8 -*-
"""k46 — time: tính từ thời gian dựng bằng hậu tố -н- (mềm -ний vs cứng -о́й),
trạng từ thời gian là cách 5 đông cứng lại, và tên hai ngày đầu tuần."""

S = {}
V = {}

S["зимний"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">зим-</span>'
    '<span class="hd-gloss">mùa đông (<b>зима́</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-</span>'
    '<span class="hd-gloss">hậu tố biến danh từ thành tính từ quan hệ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span>'
    '<span class="hd-gloss">đuôi MỀM</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen là “thuộc về mùa đông”: <b>зи́мняя оде́жда</b> '
    'quần áo mùa đông. Trọng âm rời đuôi về gốc: <b>зима́</b> → <b>зи́мний</b>. '
    'Đuôi <b>-ний</b> mềm nên biến cách theo mẫu <b>си́ний</b> (зи́мнего, зи́мней) — '
    'cả nhóm <b>ле́тний · весе́нний · осе́нний · у́тренний · вече́рний</b> đều thế.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>зима́</b> mùa đông · <b>зимо́й</b> vào mùa đông · '
    '<b>зимова́ть</b> trú đông</div>'
)

S["ранний"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ран-</span>'
    '<span class="hd-gloss">sớm (như <b>ра́но</b>, <b>ра́ньше</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-</span>'
    '<span class="hd-gloss">hậu tố tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span>'
    '<span class="hd-gloss">đuôi mềm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tính từ “sớm”: <b>ра́ннее у́тро</b> sáng sớm, '
    '<b>ра́нняя весна́</b> đầu xuân. Trạng từ đi kèm là <b>ра́но</b>, so sánh hơn '
    '<b>ра́ньше</b>; trái nghĩa <b>по́здний</b>. Hai chữ н là do gốc ран- đã tận cùng '
    'bằng н rồi mới lắp hậu tố -н- vào, y như <b>о́сень</b> → <b>осе́нний</b>.</div>'
    '<div class="hd-warn">⚠️ Bảng dạng ngắn không suy thẳng từ dạng dài: giống đực '
    'rụng bớt một н → <b>ра́нен</b>; ba dạng còn lại (ра́ння · ра́нне · ра́нни) '
    'gần như không ai dùng.</div>'
    '<div class="hd-warn">⚠️ Gặp <b>ра́нен</b> trong câu thì thường là dạng ngắn của '
    '<b>ра́неный</b> (bị thương), không phải của từ này.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ра́но</b> sớm · <b>ра́ньше</b> sớm hơn, trước đây · '
    '<b>рань</b> lúc tinh mơ</div>'
)

S["утренний"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у́тр-</span>'
    '<span class="hd-gloss">buổi sáng (<b>у́тро</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-енн-</span>'
    '<span class="hd-gloss">hậu tố tính từ, chèn thêm chữ е</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span>'
    '<span class="hd-gloss">đuôi mềm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dùng cho mọi thứ “của buổi sáng”: <b>у́тренний ко́фе</b> '
    'cà phê sáng, <b>у́тренняя газе́та</b> báo buổi sáng. Trọng âm đứng yên ở у́- '
    'đúng chỗ của <b>у́тро</b> — khác <b>вече́рний</b>, nơi trọng âm dịch khỏi '
    '<b>ве́чер</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>у́тро</b> buổi sáng · <b>у́тром</b> vào buổi sáng · '
    '<b>у́тренник</b> buổi diễn ban sáng cho trẻ</div>'
)

S["весенний"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вес-</span>'
    '<span class="hd-gloss">gốc “mùa xuân”</span></div>'
    '<div class="hd-row"><span class="hd-piece">-енн-</span>'
    '<span class="hd-gloss">hậu tố tính từ, chèn chữ е vào giữa gốc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span>'
    '<span class="hd-gloss">đuôi mềm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc của <b>весна́</b> là весн-, nhưng khi lắp hậu tố thì một '
    'chữ е chen vào giữa: вес-е-нний. Đúng chữ е đó cũng hiện ra ở cách 2 số nhiều '
    '<b>вёсен</b> — viết ё vì ở đó nó mang trọng âm. Trọng âm dời khỏi đuôi: '
    '<b>весна́</b> → <b>весе́нний</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>весна́</b> mùa xuân · <b>весно́й</b> vào mùa xuân</div>'
)

S["осенний"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">осен-</span>'
    '<span class="hd-gloss">gốc của <b>о́сень</b> (mùa thu)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-</span>'
    '<span class="hd-gloss">hậu tố tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span>'
    '<span class="hd-gloss">đuôi mềm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc осен- đã tận cùng bằng н, cộng thêm hậu tố -н- ⇒ viết '
    'HAI chữ н: осе-н-н-ий. Trọng âm dịch từ <b>о́сень</b> vào âm giữa: '
    '<b>осе́нний</b>, y như <b>ве́чер</b> → <b>вече́рний</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>о́сень</b> mùa thu · <b>о́сенью</b> vào mùa thu</div>'
)

S["вечерний"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вечер-</span>'
    '<span class="hd-gloss">buổi tối (<b>ве́чер</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-</span>'
    '<span class="hd-gloss">hậu tố tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span>'
    '<span class="hd-gloss">đuôi mềm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thêm -н- thì trọng âm nhảy vào âm giữa: <b>ве́чер</b> → '
    '<b>вече́рний</b> (còn <b>у́тро</b> → <b>у́тренний</b> giữ nguyên chỗ cũ). Dùng cho '
    'mọi thứ diễn ra buổi tối: <b>вече́рнее пла́тье</b> váy dạ hội, '
    '<b>вече́рние но́вости</b> bản tin tối.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ве́чер</b> buổi tối · <b>ве́чером</b> vào buổi tối · '
    '<b>вечери́нка</b> bữa tiệc tối</div>'
)

S["летний"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">лет-</span>'
    '<span class="hd-gloss">mùa hè (<b>ле́то</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-</span>'
    '<span class="hd-gloss">hậu tố tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span>'
    '<span class="hd-gloss">đuôi mềm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trọng âm đứng yên ở gốc: <b>ле́то</b> → <b>ле́тний</b>. Vì số '
    'nhiều <b>лета́</b> còn mang nghĩa “năm”, nên -ле́тний trong từ ghép lại có nghĩa '
    '“…tuổi / …năm”: <b>пятиле́тний</b> 5 tuổi, <b>двухле́тний</b> 2 năm.</div>'
    '<div class="hd-warn">⚠️ <b>ле́тний</b> (mùa hè) chỉ khác <b>лётный</b> (thuộc về '
    'bay, gốc <b>лета́ть</b>) đúng một chữ ё — đọc kỹ mặt chữ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ле́то</b> mùa hè · <b>ле́том</b> vào mùa hè</div>'
)

S["вчерашний"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вчера́</span>'
    '<span class="hd-gloss">hôm qua (trạng từ)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-шн-ий</span>'
    '<span class="hd-gloss">đuôi biến trạng từ thời gian thành TÍNH TỪ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Khuôn -шний lắp thẳng vào trạng từ và giữ nguyên trọng âm của '
    'nó: <b>вчера́</b> → <b>вчера́шний</b>, <b>за́втра</b> → <b>за́втрашний</b>, '
    '<b>сего́дня</b> → <b>сего́дняшний</b>, <b>тогда́</b> → <b>тогда́шний</b> (thời đó). '
    'Bản thân <b>вчера́</b> cùng gốc với <b>ве́чер</b> — “buổi tối vừa qua”.</div>'
    '<div class="hd-warn">⚠️ Bảng dạng ngắn (giống đực chèn thêm е: '
    '<b>вчера́шен</b>) chỉ có trên giấy — tính từ loại này thực tế chỉ dùng dạng '
    'đầy đủ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вчера́</b> hôm qua · <b>позавчера́</b> hôm kia</div>'
)

S["завтрашний"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за́втра</span>'
    '<span class="hd-gloss">ngày mai (trạng từ)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-шн-ий</span>'
    '<span class="hd-gloss">đuôi biến trạng từ thành tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng khuôn -шний như <b>вчера́шний</b>, trọng âm ở nguyên chỗ '
    'за́-. Chính <b>за́втра</b> là hai chữ “за у́тра” dính lại — “sau buổi sáng [này]”; <b>за́втрак</b> (bữa sáng) cũng mọc ra từ đúng gốc <b>у́тро</b> đó.</div>'
    '<div class="hd-warn">⚠️ Dạng ngắn <b>за́втрашен</b> · за́втрашня… có trong bảng '
    'nhưng hầu như không gặp trong lời nói; cứ dùng dạng đầy đủ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>за́втра</b> ngày mai · <b>послеза́втра</b> ngày kia · '
    '<b>за́втрак</b> bữa sáng</div>'
)

S["сегодняшний"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сего́</span>'
    '<span class="hd-gloss">“của cái này” (cách 2 của <b>сей</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">дня</span>'
    '<span class="hd-gloss">“ngày” (cách 2 của <b>день</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-шн-ий</span>'
    '<span class="hd-gloss">đuôi biến trạng từ thành tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>сего́дня</b> vốn là hai chữ “сего́ дня” = “của ngày này”, '
    'dính lại thành một; thêm -шний ra tính từ. Chữ г ở đó đọc thành в, đúng luật đọc '
    'của đuôi -ого.</div>'
    '<div class="hd-warn">⚠️ Cụm hay gặp trên báo: <b>на сего́дняшний день</b> = tính '
    'đến hôm nay, ở thời điểm hiện tại.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сего́дня</b> hôm nay · <b>сейча́с</b> bây giờ (cũng từ '
    '<b>сей</b> + <b>час</b>) · <b>день</b> ngày</div>'
)

S["прошедший"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">qua, xuyên qua</span></div>'
    '<div class="hd-row"><span class="hd-piece">-шед-</span>'
    '<span class="hd-gloss">gốc quá khứ của <b>идти́</b> (<b>шёл</b> đã đi)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ш-ий</span>'
    '<span class="hd-gloss">đuôi phân từ quá khứ chủ động</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ <b>пройти́</b> / <b>прошёл</b> “đã đi qua” ⇒ '
    '<b>проше́дший</b> “đã trôi qua, vừa qua”: <b>проше́дшая неде́ля</b> tuần vừa qua. '
    'Đây là phân từ đem dùng như tính từ; trong lời nói thường ngày người ta hay chọn '
    '<b>про́шлый</b> cho gọn.</div>'
    '<div class="hd-warn">⚠️ <b>проше́дшее вре́мя</b> = “thì quá khứ” — thuật ngữ ngữ '
    'pháp sẽ gặp suốt.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пройти́</b> đi qua · <b>про́шлый</b> trước, vừa qua · '
    '<b>прохо́жий</b> người qua đường</div>'
)

S["зимой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">зим-</span>'
    '<span class="hd-gloss">mùa đông</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́й</span>'
    '<span class="hd-gloss">đuôi cách 5 số ít của <b>зима́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không phải một từ riêng: đây là dạng cách 5 của <b>зима́</b> '
    'đông cứng lại thành trạng từ “vào mùa đông”, dùng không cần giới từ. Cả bộ thời '
    'gian làm y hệt: <b>весно́й · ле́том · о́сенью · у́тром · днём · ве́чером · '
    'но́чью</b>. Trọng âm ở đuôi đúng như <b>зима́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>зима́</b> mùa đông · <b>зи́мний</b> thuộc về mùa đông</div>'
)

S["дневной"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дн-</span>'
    '<span class="hd-gloss">gốc cụt của <b>день</b> (như <b>дня</b>, <b>днём</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ев-н-</span>'
    '<span class="hd-gloss">hậu tố tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́й</span>'
    '<span class="hd-gloss">đuôi CỨNG, mang trọng âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>день</b> có nguyên âm chạy — cách 2 là <b>дня</b>, chữ е '
    'rơi mất — và tính từ dựng thẳng trên cái gốc cụt дн- đó. Đuôi -о́й cứng và có '
    'trọng âm (như <b>ночно́й</b>), khác hẳn nhóm mềm <b>зи́мний / ле́тний</b>: '
    '<b>дневно́й свет</b> ánh sáng ban ngày.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>день</b> ngày · <b>днём</b> vào ban ngày · '
    '<b>по́лдень</b> giữa trưa · <b>ежедне́вный</b> hằng ngày</div>'
)

S["весной"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">весн-</span>'
    '<span class="hd-gloss">mùa xuân</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́й</span>'
    '<span class="hd-gloss">đuôi cách 5 số ít của <b>весна́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cách 5 của <b>весна́</b> dùng làm trạng từ thời gian “vào mùa '
    'xuân”, không cần giới từ: <b>Весно́й тепло́</b> = Mùa xuân thì ấm. Cùng bộ với '
    '<b>зимо́й</b> — xem thẻ đó. Trọng âm ở đuôi như từ gốc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>весна́</b> mùa xuân · <b>весе́нний</b> thuộc về mùa xuân</div>'
)

S["ночной"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ноч-</span>'
    '<span class="hd-gloss">đêm (<b>ночь</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-</span>'
    '<span class="hd-gloss">hậu tố tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́й</span>'
    '<span class="hd-gloss">đuôi CỨNG, mang trọng âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đi thành cặp với <b>дневно́й</b>: cùng lấy đuôi cứng có trọng '
    'âm, chứ không vào nhóm mềm -ний. Dùng cho mọi thứ “về đêm”: <b>ночно́й по́езд</b> '
    'tàu đêm, <b>ночна́я сме́на</b> ca đêm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ночь</b> đêm · <b>но́чью</b> vào ban đêm · '
    '<b>по́лночь</b> nửa đêm · <b>ночева́ть</b> ngủ qua đêm</div>'
)

S["вторник"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">втор-</span>'
    '<span class="hd-gloss">thứ hai (<b>второ́й</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ник</span>'
    '<span class="hd-gloss">hậu tố tạo danh từ giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tuần Nga mở đầu bằng <b>понеде́льник</b>, nên “ngày số hai” '
    'chính là <b>вто́рник</b>. Thêm -ник thì trọng âm lùi về gốc: <b>второ́й</b> → '
    '<b>вто́рник</b>.</div>'
    '<div class="hd-warn">⚠️ Con số trong tên ngày Nga lệch một bậc so với tiếng Việt: '
    '<b>вто́рник</b> gốc “hai” nhưng là thứ BA, <b>четве́рг</b> gốc “bốn” là thứ '
    'NĂM.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>второ́й</b> thứ hai · <b>втори́чный</b> lần hai, thứ cấp</div>'
)

S["понедельник"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">sau, tiếp theo</span></div>'
    '<div class="hd-row"><span class="hd-piece">-недель-</span>'
    '<span class="hd-gloss">gốc của <b>неде́ля</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ник</span>'
    '<span class="hd-gloss">hậu tố tạo danh từ giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>неде́ля</b> nay nghĩa là “tuần”, nhưng gốc của nó là '
    '“не + <b>де́лать</b>” — ngày KHÔNG làm việc, tức ngày chủ nhật thời xưa. '
    '<b>Понеде́льник</b> = ngày ngay SAU ngày nghỉ ấy, nên nó mở đầu tuần.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>неде́ля</b> tuần · <b>де́лать</b> làm · <b>де́ло</b> việc</div>'
)

S["утром"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у́тр-</span>'
    '<span class="hd-gloss">buổi sáng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ом</span>'
    '<span class="hd-gloss">đuôi cách 5 số ít của <b>у́тро</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cách 5 của <b>у́тро</b> hoá thành trạng từ “vào buổi sáng”, '
    'cùng bộ với <b>зимо́й</b> (xem thẻ đó). Nhưng trọng âm ở GỐC: <b>у́тром</b>, vì '
    'bản thân <b>у́тро</b> vốn trọng âm gốc — khác <b>зимо́й · весно́й</b> lấy trọng '
    'âm ở đuôi.</div>'
    '<div class="hd-warn">⚠️ Nói giờ cụ thể thì không dùng từ này mà dùng cách 2: '
    '<b>де́сять часо́в утра́</b> = 10 giờ sáng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>у́тро</b> buổi sáng · <b>у́тренний</b> thuộc về buổi sáng</div>'
)

S["потом"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по</span>'
    '<span class="hd-gloss">giới từ “по” (theo, sau)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-то́м</span>'
    '<span class="hd-gloss">cách 6 của <b>то</b> (cái đó)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen “по то́м” = sau cái đó ⇒ <b>пото́м</b> “sau đó, rồi '
    'thì”. Cùng lối ghép giới từ + đại từ: <b>потому́</b> (vì thế), <b>зате́м</b> '
    '(tiếp đó).</div>'
    '<div class="hd-warn">⚠️ Trọng âm tách hai từ chẳng liên quan gì nhau: '
    '<b>пото́м</b> sau đó — còn <b>по́том</b> là cách 5 của <b>пот</b> (mồ hôi).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>то</b> cái đó · <b>потому́</b> vì thế · <b>зате́м</b> '
    'tiếp sau đó</div>'
)

S["утро"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у́тр-</span>'
    '<span class="hd-gloss">gốc, không chẻ nhỏ hơn được</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi ⇒ danh từ giống TRUNG</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi -о cho biết giống trung, nên lời chào phải là '
    '<b>до́брое у́тро</b> với tính từ ở dạng trung, không phải “до́брый”.</div>'
    '<div class="hd-warn">⚠️ Đứng một mình thì trọng âm ở gốc (<b>у́тро</b>), nhưng '
    'trong cụm cố định có giới từ nó chạy xuống đuôi: <b>с утра́</b> từ sáng · '
    '<b>к утру́</b> về sáng · <b>по утра́м</b> vào các buổi sáng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>у́тренний</b> thuộc về buổi sáng · <b>у́тром</b> vào buổi '
    'sáng</div>'
)

S["лето"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">лет-</span>'
    '<span class="hd-gloss">gốc, không chẻ nhỏ hơn được</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi ⇒ danh từ giống TRUNG</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi -о ⇒ giống trung. Sang số nhiều thì trọng âm dịch xuống '
    'đuôi: <b>ле́то</b> → <b>лета́</b> — và chính dạng số nhiều này còn mang nghĩa '
    '“năm”.</div>'
    '<div class="hd-warn">⚠️ Cách 2 số nhiều <b>лет</b> chính là chữ mà <b>год</b> '
    'mượn để đếm: <b>ско́лько тебе́ лет?</b> bạn bao nhiêu tuổi · <b>пять лет</b> '
    '5 năm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ле́тний</b> thuộc về mùa hè · <b>ле́том</b> vào mùa hè · '
    '<b>лета́</b> năm tháng, tuổi tác</div>'
)

# --- Việc thứ hai: đề bài tiếng Việt (README §2c) — chỉ những từ cần sửa ---
# потом: bỏ "lát nữa" vì trùng nguyên cụm với попозже (k66, cả hai PoS=oth,
#        không badge nào tách được); thay bằng các nghĩa gloss Anh xác nhận
#        (afterwards / then / later on).
V["потом"] = "sau đó, rồi thì, về sau"
# прошедший: "trước" quá rộng (nới rộng), cắt.
V["прошедший"] = "đã qua, vừa qua"
# дневной: "diễn ra vào ban ngày" là lời chú thích, không phải một nghĩa rời.
V["дневной"] = "thuộc về ban ngày, ban ngày"
# осенний: "thu" đứng một mình mơ hồ; viết cho khớp khuôn các tính từ mùa khác.
V["осенний"] = "thuộc về mùa thu, mùa thu"
