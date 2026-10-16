# -*- coding: utf-8 -*-
"""k93 — qualities: 19 từ mới (đợt A1 TRKI), KHÔNG cùng một trục — soạn từng thẻ độc lập.

Chỗ cần nhất quán trong lô:
(1) закры́тый / откры́тый / до́лжный / пра́вый: TRKI dạy DẠNG NGẮN (закры́т, откры́т, до́лжен,
    прав) ⇒ dạng ngắn đứng ĐẦU thẻ, trước cả phần chẻ từ;
(2) истори́ческий / экономи́ческий: cùng đuôi -и́ческий, trọng âm luôn nằm ở и́ đó;
(3) khớp lô cũ: -кры- CHE, ĐẬY (k85/k87), на- + -род- (k33), прав- THẲNG, ĐÚNG (k04/k49),
    ни- + từ hỏi (k45), -вяз- buộc (k05), гость (k74), эко- + -ном- (k89).
Bẫy họ hàng đã gạt: гора́ ≠ го́род; ле́вый ≠ лев (sư tử); до́лжен ≠ до́лгий (không nêu);
век ≠ ве́чер; челове́к KHÔNG nêu dưới век (từ nguyên tranh cãi, k33 đã nói thế).
"""

S = {}

# -------------------------------------------------------------- активный
S["активный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">акти́в-</span>'
    '<span class="hd-gloss">mượn Latin <i>activus</i> — HOẠT ĐỘNG (Anh <i>active</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi biến thành tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>active</i>, chỉ gắn thêm đuôi tính từ <b>-ный</b>. '
    'Trạng từ bỏ <b>-ый</b> lấy <b>-о</b>: <b>акти́вно</b>. Dạng ngắn giống đực chèn '
    '<b>е</b>: <b>акти́вен</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>акти́вность</b> sự năng động · <b>активи́ст</b> nhà hoạt '
    'động</div>'
)

# --------------------------------------------------------------- будущий
S["будущий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бу́д-</span>'
    '<span class="hd-gloss">SẼ LÀ — gốc của <b>бу́ду</b> (tôi sẽ là)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ущ-ий</span>'
    '<span class="hd-gloss">«đang / sẽ …» — đuôi phân từ, như <b>веду́щий</b> người dẫn</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cái sẽ có» của <b>быть</b> ⇒ tương lai, sắp tới: <b>бу́дущая '
    'неде́ля</b> tuần tới.</div>'
    '<div class="hd-warn">Đứng một mình ở giống trung thì thành danh từ: <b>бу́дущее</b> = '
    'tương lai · <b>в бу́дущем</b> = trong tương lai, sau này.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>быть</b> là, có · <b>бу́ду</b> tôi sẽ · <b>бу́дущее</b> '
    'tương lai</div>'
)

# ------------------------------------------------------------------- век
S["век"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn Slav cổ, không chẻ được — nghĩa cũ là «một đời người» (còn trong '
    'nghĩa «đời người»), sau mới thành «trăm năm».</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Số ít trọng âm ở gốc (<b>ве́ка</b>, <b>в ве́ке</b>), sang số nhiều '
    'nhảy ra đuôi: <b>века́</b>, <b>веко́в</b>.</div>'
    '<div class="hd-warn">Thế kỷ viết số La Mã nhưng đọc bằng số THỨ TỰ: <b>XXI век</b> = '
    '<b>два́дцать пе́рвый век</b>.</div>'
    '<div class="hd-warn"><b>сре́дние века́</b> = thời Trung cổ (nghĩa đen «các thế kỷ '
    'giữa»).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ве́чный</b> vĩnh cửu (<b>к → ч</b>) · <b>ве́чно</b> mãi mãi · '
    '<b>веково́й</b> trăm năm, lâu đời</div>'
    '<div class="hd-why"><b>ве́чер</b> buổi tối trông giống mà KHÁC gốc.</div>'
)

# --------------------------------------------------------------- великий
S["великий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вели́к-</span>'
    '<span class="hd-gloss">LỚN, có TẦM VÓC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>большо́й</b> là to về kích thước; <b>вели́кий</b> là lớn về tầm '
    'vóc: <b>Пётр Вели́кий</b> Pyotr Đại đế, <b>Вели́кая Оте́чественная война́</b> Chiến tranh Vệ quốc.</div>'
    '<div class="hd-warn">Dạng NGẮN đổi hẳn nghĩa thành «QUÁ to» (quần áo, giày): '
    '<b>Пальто́ мне велико́</b> = áo khoác rộng quá. Trọng âm nhảy ra đuôi: '
    '<b>вели́к · велика́ · велико́ · велики́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>велика́н</b> người khổng lồ · <b>увели́чить</b> phóng to · '
    '<b>Великобрита́ния</b> <i>Great Britain</i></div>'
)

# ------------------------------------------------------------------ виза
S["виза"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được trong tiếng Nga: mượn nguyên khối <i>visa</i> — Latin '
    '«(giấy) đã được XEM», tức đã được duyệt.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giống cái vì đuôi <b>-а</b>, chia như mọi từ đuôi <b>-а</b>: '
    '<b>получи́ть ви́зу</b> được cấp visa · <b>без ви́зы</b> miễn visa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>визи́т</b> chuyến thăm (cùng gốc Latin «xem, thăm»)</div>'
)

# ------------------------------------------------------------------ гора
S["гора"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được. Trông giống <b>го́род</b> nhưng KHÁC gốc.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trọng âm phải thuộc: đuôi ở hầu hết số ít (<b>горы́</b>, <b>горо́й</b>), nhưng cách 4 lùi về đầu — <b>на го́ру</b> lên núi.</div>'
    '<div class="hd-warn">Chỉ trọng âm tách hai dạng: <b>горы́</b> = của ngọn núi (cách 2) · '
    '<b>го́ры</b> = những ngọn núi. Đi núi: <b>в го́ры</b>, ở vùng núi: <b>в гора́х</b>.</div>'
    '<div class="hd-warn"><b>не за гора́ми</b> = sắp tới rồi, chẳng còn xa (nghĩa đen '
    '«không ở sau núi»).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>го́рный</b> thuộc núi (<b>го́рные лы́жи</b> trượt tuyết đổ dốc) '
    '· <b>гори́стый</b> nhiều núi</div>'
)

# ------------------------------------------------------------- гостиница
S["гостиница"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">гост-</span>'
    '<span class="hd-gloss">KHÁCH — như <b>гость</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ин-</span>'
    '<span class="hd-gloss">«dành cho» — như <b>гости́ная</b> phòng khách</span></div>'
    '<div class="hd-row"><span class="hd-piece">-иц-а</span>'
    '<span class="hd-gloss">đuôi chỉ NƠI CHỐN — như <b>больни́ца</b> bệnh viện</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Nơi dành cho khách» ⇒ khách sạn. Trọng âm đứng yên ở <b>-и́-</b> '
    'khắp bảng: <b>жить в гости́нице</b> ở khách sạn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гость</b> khách · <b>гости́ная</b> phòng khách · '
    '<b>гостеприи́мный</b> hiếu khách · <b>оте́ль</b> khách sạn (từ mượn, khác gốc)</div>'
)

# --------------------------------------------------------------- должный
S["должный"] = (
    '<div class="hd-why"><b>Dạng hay dùng là dạng NGẮN: до́лжен · должна́ · должно́ · '
    'должны́</b> = phải. <b>Я до́лжен рабо́тать</b> tôi phải làm việc.</div>'
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">долж-</span>'
    '<span class="hd-gloss">= <b>долг</b> NỢ, BỔN PHẬN (<b>г → ж</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ен / -ный</span>'
    '<span class="hd-gloss">đuôi tính từ (ngắn / đầy đủ)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đang mắc nợ» ⇒ phải làm. Đuôi theo GIỐNG của người phải làm: '
    '<b>Она́ должна́</b>. Nghĩa gốc vẫn sống: <b>Ты мне до́лжен сто рубле́й</b> = bạn nợ tôi '
    '100 rúp. Dạng đầy đủ <b>до́лжный</b> chỉ còn nghĩa sách vở «thích đáng».</div>'
    '<div class="hd-warn">Chủ ngữ ở cách 1: <b>Я до́лжен</b>. Đừng lẫn với <b>Мне на́до</b> '
    '(cách 3) — cùng nghĩa «phải», khác khung câu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>долг</b> món nợ, bổn phận · <b>должни́к</b> con nợ · '
    '<b>до́лжность</b> chức vụ</div>'
)

# -------------------------------------------------------------- закрытый
S["закрытый"] = (
    '<div class="hd-why"><b>Dạng hay dùng là dạng NGẮN: закры́т · закры́та · закры́то · '
    'закры́ты</b>. <b>Магази́н закры́т</b> cửa hàng (đang) đóng cửa.</div>'
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-кры́-</span>'
    '<span class="hd-gloss">= <b>закры́ть</b> đóng, đậy (gốc <b>-кры-</b> CHE)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-т-ый</span>'
    '<span class="hd-gloss">«đã bị …» — biến động từ thành tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đã bị đóng lại» ⇒ đóng, kín. Nói trạng thái sau «là» thì dùng dạng '
    'ngắn (<b>Дверь закры́та</b>); đứng trước danh từ thì dạng đầy đủ (<b>закры́тая '
    'дверь</b>).</div>'
    '<div class="hd-warn">Biển treo cửa: <b>Закры́то</b> = đóng cửa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>закры́ть</b> đóng · <b>закрыва́ть</b> đóng (CHT) · '
    '<b>откры́тый</b> mở</div>'
)

# --------------------------------------------------------- исторический
S["исторический"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">истор-</span>'
    '<span class="hd-gloss"><b>исто́рия</b> lịch sử</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ческ-ий</span>'
    '<span class="hd-gloss">đuôi tính từ cho từ mượn <b>-ия / -ика</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thay <b>-ия</b> bằng <b>-и́ческий</b> ⇒ «thuộc lịch sử» — y như '
    '<i>history → historical</i>. Trọng âm luôn bị đuôi này kéo về <b>-и́-</b>: '
    '<b>исто́рия → истори́ческий</b>, giống <b>эконо́мика → экономи́ческий</b>.</div>'
    '<div class="hd-warn"><b>истори́ческий факульте́т</b> = khoa Lịch sử.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>исто́рия</b> lịch sử, câu chuyện · <b>исто́рик</b> nhà sử '
    'học</div>'
)

# ----------------------------------------------------------------- левый
S["левый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">лев-</span>'
    '<span class="hd-gloss">TRÁI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>ле́вая рука́</b> tay trái. Muốn nói «ở bên trái / sang trái» thì '
    'KHÔNG dùng tính từ này mà dùng <b>сле́ва</b> / <b>нале́во</b>. Trùng mặt chữ với '
    '<b>лев</b> (sư tử) nhưng khác gốc hẳn.</div>'
    '<div class="hd-warn"><b>ле́вая рабо́та</b> = việc làm thêm «chui», ngoài sổ sách — '
    '«trái» ở đây là trái phép.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сле́ва</b> ở bên trái · <b>нале́во</b> sang trái · '
    '<b>левша́</b> người thuận tay trái</div>'
)

# ------------------------------------------------------------ московский
S["московский"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">моско́в-</span>'
    '<span class="hd-gloss"><b>Москва́</b>, giữa <b>к</b> và <b>в</b> mọc thêm <b>о</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ск-ий</span>'
    '<span class="hd-gloss">đuôi «thuộc về nơi …»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trọng âm rời đuôi <b>Москва́</b> về đúng chữ <b>о</b> mới mọc: '
    '<b>моско́вский</b>. Viết THƯỜNG, khác tiếng Anh <i>Moscow</i>.</div>'
    '<div class="hd-warn"><b>по моско́вскому вре́мени</b> = theo giờ Moskva — câu quen trên '
    'đài, bảng giờ tàu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>Москва́</b> Moskva · <b>москви́ч</b> người Moskva · '
    '<b>Подмоско́вье</b> vùng quanh Moskva</div>'
)

# --------------------------------------------------------------- народный
S["народный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-ро́д-</span>'
    '<span class="hd-gloss"><b>наро́д</b> nhân dân (<b>-род-</b> SINH RA)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi biến danh từ thành tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hai nghĩa: dân gian (<b>наро́дная пе́сня</b> dân ca) và của nhân dân '
    '(<b>наро́дный арти́ст</b> Nghệ sĩ Nhân dân). Ở hai nghĩa này gần như không gặp dạng '
    'ngắn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>наро́д</b> nhân dân · <b>междунаро́дный</b> quốc tế (giữa các '
    'dân tộc) · <b>ро́дина</b> quê hương</div>'
)

# ---------------------------------------------------------------- никуда
S["никуда"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ни-</span>'
    '<span class="hd-gloss">tiền tố PHỦ ĐỊNH gắn vào từ hỏi</span></div>'
    '<div class="hd-row"><span class="hd-piece">куда́</span>'
    '<span class="hd-gloss">tới đâu</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Tới đâu» bị <b>ни-</b> dập tắt ⇒ không tới đâu cả. Vẫn phải có '
    '<b>не</b> trước động từ: <b>Я никуда́ не иду́</b> tôi không đi đâu cả.</div>'
    '<div class="hd-warn">Đi đâu (có chuyển động) → <b>никуда́</b>; ở đâu (đứng yên) → '
    '<b>нигде́</b>: <b>Я нигде́ не был</b> tôi chưa từng ở đâu cả.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>куда́</b> tới đâu · <b>нигде́</b> không ở đâu · '
    '<b>никогда́</b> không bao giờ · <b>никто́</b> không ai</div>'
)

# ----------------------------------------------------------- обязательно
S["обязательно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-(в)яз-</span>'
    '<span class="hd-gloss"><b>об-</b> quanh + gốc <b>вяз-</b> BUỘC (<b>вяза́ть</b>), <b>в</b> rụng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-тельн-о</span>'
    '<span class="hd-gloss"><b>-тельный</b> tính từ → <b>-о</b> trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Bị buộc vào» ⇒ bắt buộc; buộc chính mình ⇒ nhất định sẽ làm: '
    '<b>Я обяза́тельно приду́</b> tôi nhất định sẽ đến.</div>'
    '<div class="hd-warn"><b>не обяза́тельно</b> = không cần, không bắt buộc — KHÔNG phải '
    '«nhất định không».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обяза́тельный</b> bắt buộc · <b>обя́занность</b> nghĩa vụ · '
    '<b>связь</b> mối liên hệ · <b>вяза́ть</b> buộc, đan</div>'
)

# ------------------------------------------------------------- осторожно
S["осторожно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">quanh mình</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сторож-</span>'
    '<span class="hd-gloss">CANH GÁC — như <b>сто́рож</b> người gác</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-о</span>'
    '<span class="hd-gloss">đuôi trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Canh chừng quanh mình» ⇒ cẩn thận, thận trọng. Đứng một mình là '
    'lời cảnh báo: <b>Осторо́жно!</b> Cẩn thận!</div>'
    '<div class="hd-warn"><b>Осторо́жно, две́ри закрыва́ются!</b> = Chú ý, cửa đang đóng! — '
    'câu loa ở mọi ga tàu điện ngầm Moskva.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>осторо́жный</b> cẩn thận · <b>осторо́жность</b> sự thận trọng · '
    '<b>сто́рож</b> người gác</div>'
)

# -------------------------------------------------------------- открытый
S["открытый"] = (
    '<div class="hd-why"><b>Dạng hay dùng là dạng NGẮN: откры́т · откры́та · откры́то · '
    'откры́ты</b>. <b>Магази́н откры́т</b> cửa hàng (đang) mở cửa.</div>'
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-кры́-</span>'
    '<span class="hd-gloss">= <b>откры́ть</b> mở (gỡ cái <b>-кры-</b> CHE ra)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-т-ый</span>'
    '<span class="hd-gloss">«đã được …» — biến động từ thành tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đã được gỡ cái che» ⇒ mở, hở; nói về người ⇒ cởi mở: '
    '<b>откры́тый челове́к</b>. Trạng thái sau «là» dùng dạng ngắn: <b>Окно́ откры́то</b>.</div>'
    '<div class="hd-warn"><b>на откры́том во́здухе</b> = ngoài trời (nghĩa đen «trên '
    'không khí mở»).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>откры́ть</b> mở · <b>закры́тый</b> đóng · <b>откры́тка</b> '
    'bưu thiếp · <b>откры́тие</b> khám phá, khai trương</div>'
)

# ----------------------------------------------------------------- правый
S["правый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">прав-</span>'
    '<span class="hd-gloss">THẲNG, ĐÚNG, NGAY — như <b>пра́вда</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một gốc, hai nghĩa — y hệt <i>right</i> tiếng Anh: bên phải '
    '(<b>пра́вая рука́</b>) và đúng.</div>'
    '<div class="hd-warn">Nghĩa «đúng, có lý» sống ở dạng NGẮN: <b>Я прав</b> tôi đúng · '
    '<b>Ты права́</b> (nói với nữ) · <b>Вы пра́вы</b> anh/chị nói đúng. Dạng ngắn không bao '
    'giờ mang nghĩa «bên phải».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пра́вда</b> sự thật · <b>пра́вильно</b> đúng · '
    '<b>спра́ва</b> ở bên phải · <b>напра́во</b> sang phải · <b>пра́во</b> quyền</div>'
)

# ---------------------------------------------------------- экономический
S["экономический"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">эко-ном-</span>'
    '<span class="hd-gloss"><b>эконо́мика</b> — «phép quản cái nhà»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ческ-ий</span>'
    '<span class="hd-gloss">đuôi tính từ cho từ mượn <b>-ика / -ия</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thay <b>-ика</b> bằng <b>-и́ческий</b> ⇒ «thuộc kinh tế»; trọng âm '
    'bị kéo về <b>-и́-</b>, giống <b>исто́рия → истори́ческий</b>.</div>'
    '<div class="hd-warn">Đừng lẫn với <b>эконо́мный</b> = tiết kiệm, chi tiêu dè sẻn — y như '
    'tiếng Anh tách <i>economic</i> và <i>economical</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>эконо́мика</b> kinh tế · <b>экономи́ст</b> nhà kinh tế học · '
    '<b>эконо́мить</b> tiết kiệm</div>'
)

V = {
    # Bỏ "tích cực" (trùng положительный k53, cùng adj); gloss chỉ "active".
    # Giữ "năng động" — lô k99 tự rút phía энергичный.
    "активный": "năng động",
    # Bỏ ngoặc "(dùng với phủ định)" (cấm) và bỏ "ở đâu cả" — đó là нигде́, không phải
    # никуда́ (gloss "nowhere" theo hướng chuyển động).
    "никуда": "không đi đâu cả, không tới đâu cả",
    # "nhẹ nhàng" (gently) gloss không xác nhận; gloss: carefully/cautiously/guardedly/warily.
    "осторожно": "cẩn thận, thận trọng, dè dặt",
    # Bỏ "thành thật" (nới rộng, trùng честный k99) — gloss "frank/candid" đã là "cởi mở".
    "открытый": "mở, cởi mở",
    # Bỏ "phải" trơn (trùng должный cùng lô, cùng adj).
    "правый": "bên phải, đúng",
}
