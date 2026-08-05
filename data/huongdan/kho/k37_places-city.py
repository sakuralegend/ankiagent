# -*- coding: utf-8 -*-
"""k37 — places::city: thành phố và những chỗ trong nó.

Trục của lô: phần lớn các từ này CHẺ ĐƯỢC ra gốc còn sống trong tiếng Nga hôm nay
(го́род ← rào quây · больни́ца ← боль · заво́д ← води́ть · вход ← ход), nên mỗi thẻ
đi thẳng từ mảnh sang nghĩa. Bốn từ mượn (библиоте́ка, фа́брика, шко́ла, маши́на)
thì bắc cầu sang tiếng Anh/Hy Lạp, không bịa cấu trúc Nga cho chúng.
"""

S = {}
V = {}

# ---------------------------------------------------------------- phương hướng
S["справа"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">ở phía / từ phía</span></div>'
    '<div class="hd-row"><span class="hd-piece">-прав-</span>'
    '<span class="hd-gloss">PHẢI (bên phải; đúng)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi làm trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vỏ <b>с-</b>…<b>-а</b> trả lời “Ở ĐÂU”: <b>спра́ва</b> = ở phía bên '
    'phải, từ phía bên phải. Muốn nói “ĐI về phía nào” thì phải đổi vỏ thành '
    '<b>напра́во</b> (rẽ sang phải).</div>'
    '<div class="hd-warn">⚠️ Đừng lẫn với <b>напра́во</b>: <b>спра́ва</b> nói Ở ĐÂU '
    '(сиде́ть <b>спра́ва</b> = ngồi bên phải), <b>напра́во</b> nói ĐI VỀ ĐÂU '
    '(поверну́ть <b>напра́во</b> = rẽ sang phải).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пра́вый</b> bên phải; đúng · <b>пра́вда</b> sự thật · '
    '<b>пра́вило</b> quy tắc · <b>напра́во</b> sang phải</div>'
)
V['справа'] = 'ở bên phải, từ bên phải'

S["слева"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">ở phía / từ phía</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лев-</span>'
    '<span class="hd-gloss">TRÁI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi làm trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen “từ phía trái”, dùng cho chỗ ĐỨNG YÊN: cái gì nằm ở '
    'bên trái, tiếng động phát ra từ bên trái.</div>'
    '<div class="hd-warn">⚠️ Đừng lẫn với <b>нале́во</b>: <b>сле́ва</b> nói Ở ĐÂU '
    '(сиде́ть <b>сле́ва</b> = ngồi bên trái), <b>нале́во</b> nói ĐI VỀ ĐÂU '
    '(поверну́ть <b>нале́во</b> = rẽ sang trái).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ле́вый</b> bên trái · <b>нале́во</b> sang trái · '
    '<b>спра́ва</b> ở bên phải (cùng khuôn с-…-а)</div>'
)
V['слева'] = 'ở bên trái, từ bên trái'

# ---------------------------------------------------------------- tên riêng
S["москва"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Tên riêng, không chẻ ra mảnh có nghĩa được. Thành phố mang tên '
    'con sông <b>Москва́</b> chảy qua nó.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trọng âm bám chặt vào ĐUÔI ở mọi cách: <b>Москва́</b>, '
    'в <b>Москве́</b>, <b>Москву́</b>, из <b>Москвы́</b> — không bao giờ nhảy về đầu.</div>'
    '<div class="hd-warn">⚠️ Cột số nhiều trong bảng là do máy dựng máy móc, tên riêng này '
    'không dùng số nhiều. Ô cách 2 số nhiều <b>Москв</b> không có dấu vì nó mất sạch nguyên '
    'âm, chứ trọng âm KHÔNG dịch.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>москви́ч</b> người Moscow · <b>моско́вский</b> thuộc Moscow '
    '(chú ý: trọng âm lùi vào giữa)</div>'
)
V['москва'] = 'Moscow, sông Moskva'

S["киев"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">Ки-</span>'
    '<span class="hd-gloss">tên người lập thành: Кий</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ев</span>'
    '<span class="hd-gloss">hậu tố SỞ HỮU: “của ai”</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen “(thành) của Кий”. Đuôi <b>-ов</b>/<b>-ев</b> đúng là hậu '
    'tố sở hữu cổ vẫn còn thấy trong họ người Nga (Ивано́в = “của Ива́н”).</div>'
    '<div class="hd-warn">⚠️ Mức tin: chỗ “của Кий” là từ nguyên chép theo biên niên sử, '
    'không phải luật suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ки́евский</b> thuộc Kyiv (ки́евский торт — món bánh nổi tiếng)</div>'
)

# ---------------------------------------------------------------- đơn vị lãnh thổ
S["город"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">город-</span>'
    '<span class="hd-gloss">RÀO LẠI, quây tường bao</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc là khoảnh đất được RÀO kín — thấy rõ ở '
    '<b>огоро́д</b> (vườn rau có rào) và <b>огра́да</b> (hàng rào). Bản Slavơ-Nhà thờ của '
    'chính gốc này là <b>-гра́д</b>, nằm trong tên thành phố: Волгогра́д, Ленингра́д.</div>'
    '<div class="hd-warn">⚠️ Số nhiều lệch HAI mặt cùng lúc: đuôi là <b>-а́</b> chứ không phải '
    '<b>-ы</b>, và trọng âm nhảy hẳn ra đuôi — <b>го́род</b> → <b>города́</b>, '
    '<b>городо́в</b>, в <b>города́х</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>городско́й</b> thuộc thành phố · <b>горожа́нин</b> thị dân · '
    '<b>огоро́д</b> vườn rau có rào</div>'
)

S["страна"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">стран-</span>'
    '<span class="hd-gloss">VÙNG ĐẤT, phía bên kia</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>страна́</b> chính là <b>сторона́</b> (phía, bên) nói theo lối '
    'Slavơ-Nhà thờ: <b>-оро-</b> co lại thành <b>-ра-</b>. Nghĩa gốc “vùng đất ở phía kia” '
    '→ nước, quốc gia.</div>'
    '<div class="hd-warn">⚠️ Trọng âm nhảy về THÂN khi sang số nhiều: <b>страна́</b> → '
    '<b>стра́ны</b>, <b>стра́нам</b>, <b>стра́нах</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сторона́</b> phía, bên · <b>иностра́нец</b> người nước ngoài '
    '(ино- khác + стран-) · <b>иностра́нный</b> thuộc nước ngoài</div>'
)

S["улица"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ул-</span>'
    '<span class="hd-gloss">gốc, không tách thêm được</span></div>'
    '<div class="hd-row"><span class="hd-piece">-иц(а)</span>'
    '<span class="hd-gloss">hậu tố tạo danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi <b>-ица</b> hay nặn ra danh từ giống cái chỉ NƠI CHỐN — cùng '
    'khuôn: <b>больни́ца</b> (bệnh viện), <b>столи́ца</b> (thủ đô).</div>'
    '<div class="hd-warn">⚠️ Cụm phải thuộc: на <b>у́лице</b> = Ở NGOÀI TRỜI / ngoài nhà, '
    'không riêng gì “trên phố”. Де́ти игра́ют на <b>у́лице</b> = bọn trẻ chơi ở ngoài.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>у́личный</b> ngoài đường · <b>переу́лок</b> ngõ, hẻm</div>'
)
V['улица'] = 'đường phố, phố'

S["дорога"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дорог-</span>'
    '<span class="hd-gloss">CON ĐƯỜNG, lối đi lại</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>дорог-</b> ôm cả con đường lẫn CHUYẾN ĐI trên con đường đó: '
    'по <b>доро́ге</b> домо́й = trên đường về nhà; в <b>доро́ге</b> = đang đi đường.</div>'
    '<div class="hd-warn">⚠️ Đừng nhầm <b>доро́га</b> (con đường) với <b>дорого́й</b> '
    '(đắt; thân yêu) — hai từ khác hẳn nhau, chỉ tình cờ giống mặt chữ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>доро́жка</b> lối nhỏ, đường chạy (г→ж) · <b>доро́жный</b> thuộc '
    'đường sá · желе́зная <b>доро́га</b> đường sắt</div>'
)
V['дорога'] = 'con đường, đường đi, chuyến đi'

S["вход"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO (bên trong)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ход</span>'
    '<span class="hd-gloss">SỰ ĐI, lối đi — từ ходи́ть</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ghép thẳng “đi VÀO” → chỗ để đi vào. Đổi tiền tố là đổi hướng: '
    '<b>вы́ход</b> lối RA, <b>перехо́д</b> chỗ đi SANG (vạch/hầm qua đường).</div>'
    '<div class="hd-warn">⚠️ Trên biển hiệu <b>вход</b> còn nghĩa là VÉ VÀO CỬA: '
    '<b>вход</b> свобо́дный = vào tự do, <b>вход</b> 200 рубле́й.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>входи́ть</b> đi vào · <b>ход</b> nước đi, sự chạy · '
    '<b>вы́ход</b> lối ra · <b>похо́д</b> chuyến đi bộ đường dài</div>'
)
V['вход'] = 'cửa vào, lối vào, vé vào cửa'

# ---------------------------------------------------------------- chỗ làm, chỗ học
S["завод"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">đưa vào, cho bắt đầu chạy</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вод-</span>'
    '<span class="hd-gloss">DẪN, đưa — như води́ть</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ra thẳng từ <b>заводи́ть</b> “cho chạy, khởi động”: <b>заво́д</b> là '
    'chỗ máy móc được cho chạy. Nghĩa thứ hai — cái LÊN DÂY CÓT của đồng hồ — cũng ra từ '
    'đúng động từ đó.</div>'
    '<div class="hd-warn">⚠️ <b>заво́д</b> là nhà máy CÔNG NGHIỆP NẶNG (luyện kim, chế tạo '
    'máy, ô tô); hàng tiêu dùng thì dùng <b>фа́брика</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>заводи́ть</b> khởi động, lên dây · <b>води́ть</b> dẫn, lái · '
    '<b>заводско́й</b> thuộc nhà máy</div>'
)
V['завод'] = 'nhà máy, xí nghiệp'

S["фабрика"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">фабрик-</span>'
    '<span class="hd-gloss">Latin fabrica = xưởng thợ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mượn nguyên khối, cùng gốc với tiếng Anh <i>fabricate</i> / '
    '<i>fabric</i> — chỉ đổi vỏ chứ không chẻ ra mảnh Nga được.</div>'
    '<div class="hd-warn">⚠️ <b>фа́брика</b> làm HÀNG TIÊU DÙNG: dệt may, bánh kẹo, giấy, '
    'đồ gỗ. Nhà máy cơ khí nặng thì là <b>заво́д</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>фабри́чный</b> thuộc nhà máy · <b>фабрика́нт</b> chủ nhà máy</div>'
)
V['фабрика'] = 'nhà máy, xưởng sản xuất'

S["школа"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">школ-</span>'
    '<span class="hd-gloss">Hy Lạp scholē → Latin schola</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng một từ với <i>school</i> tiếng Anh, chỉ khác lớp vỏ. Nga hoá '
    'rồi thì nó đẻ tiếp bằng hậu tố Nga: <b>-ник</b> ra người, <b>-ный</b> ra tính từ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>шко́льник</b> học sinh · <b>шко́льный</b> thuộc trường học · '
    '<b>шко́льница</b> nữ sinh</div>'
)

S["библиотека"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">библио-</span>'
    '<span class="hd-gloss">SÁCH (Hy Lạp biblíon)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тек-</span>'
    '<span class="hd-gloss">CHỖ CẤT GIỮ (thēkē)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: KHO CHỨA SÁCH. Khuôn <b>-те́ка</b> mở ra cả một lớp từ '
    'quốc tế: <b>дискоте́ка</b> kho đĩa → sàn nhảy, <b>картоте́ка</b> kho phiếu, '
    '<b>апте́ка</b> kho thuốc → hiệu thuốc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>библиоте́карь</b> thủ thư · <b>библиоте́чный</b> thuộc thư viện</div>'
)

S["больница"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">боль-</span>'
    '<span class="hd-gloss">ĐAU (nỗi đau)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-</span>'
    '<span class="hd-gloss">mảnh nối, có sẵn ở больно́й</span></div>'
    '<div class="hd-row"><span class="hd-piece">-иц(а)</span>'
    '<span class="hd-gloss">nơi chốn, giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đọc ngược ba mảnh ra ngay nghĩa đen: NƠI dành cho người ĐAU ỐM. '
    'Trọng âm trôi ra sau theo hậu tố: <b>боль</b> → <b>больно́й</b> → '
    '<b>больни́ца</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>боль</b> nỗi đau · <b>больно́й</b> bị ốm; người bệnh · '
    '<b>боле́ть</b> bị ốm, bị đau · <b>бо́льно</b> đau quá</div>'
)

S["почта"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">почт-</span>'
    '<span class="hd-gloss">Latin posita = trạm ngựa ĐẶT sẵn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc với <i>post</i> tiếng Anh: chuỗi trạm đặt dọc đường để '
    'chuyền thư. Nghĩa lõi chỉ có hai: NHÀ BƯU ĐIỆN, và THƯ TỪ gửi qua đó.</div>'
    '<div class="hd-warn">⚠️ <b>по́чта</b> trần KHÔNG có nghĩa email — phải đủ cụm '
    'электро́нная <b>по́чта</b> mới là email.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>почтальо́н</b> người đưa thư · <b>почто́вый</b> thuộc bưu điện '
    '(почто́вый я́щик hòm thư) · <b>почта́мт</b> bưu điện trung tâm</div>'
)
V['почта'] = 'bưu điện, thư từ, bưu phẩm'

S["машина"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">машин-</span>'
    '<span class="hd-gloss">Pháp machine ← Hy Lạp mēkhanḗ: CỖ MÁY</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc là CỖ MÁY nói chung, nên tên máy đều ghép quanh nó: '
    'стира́льная <b>маши́на</b> máy giặt, шве́йная <b>маши́на</b> máy khâu. Nhưng khi đứng '
    'trơ một mình trong lời nói hằng ngày, <b>маши́на</b> mặc định là XE HƠI.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>маши́нка</b> máy nhỏ (пи́шущая маши́нка máy chữ) · '
    '<b>механи́зм</b> cơ cấu máy · <b>меха́ник</b> thợ máy</div>'
)
V['машина'] = 'xe hơi, ô tô, cỗ máy'

S["клуб"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn thẳng chữ <i>club</i> tiếng Anh, một khối, không chẻ ra mảnh '
    'có nghĩa được. Một âm tiết nên không cần đánh dấu trọng âm.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Che cả hai mặt như tiếng Anh: HỘI những người cùng sở thích '
    '(спорти́вный <b>клуб</b>) và NGÔI NHÀ của hội đó. Nghĩa “chốn ăn chơi” chỉ có khi có '
    'chữ đứng kèm: ночно́й <b>клуб</b> = hộp đêm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>клу́бный</b> thuộc câu lạc bộ</div>'
)
V['клуб'] = 'câu lạc bộ, nhà câu lạc bộ'
