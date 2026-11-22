# -*- coding: utf-8 -*-
"""k174 — life::home (lô trộn): đồ trong nhà, chỗ ở, vài danh từ trừu tượng.

Chỗ cần nhất quán trong lô:
(1) труба́: chẻ khớp thẻ тру́бка [k166] «труб- ỐNG».
(2) холоди́льник: холод- LẠNH khớp thẻ хо́лод/холо́дный [k27]; -льник «đồ dùng» như буди́льник.
(3) воро́та: họ «đóng/mở» (отвори́ть, затвори́ть) + вра́та/врата́рь. KHÔNG ghép поворо́т (họ QUAY).
(4) бельё ← бе́лый [k44] «бел- TRẮNG» (Шанский: «vải tẩy trắng»). Máy ghép ме́бель = báo oan.
(5) расте́ние: рас-/рос- khớp расти́ [k97], во́зраст [k119]. Máy ghép красть/стена = báo oan.
(6) аге́нтство: аге́нт [k152] + -ство. со́весть: со- + вед-/вес- BIẾT (calque Hy Lạp, = con-science).
(7) приключе́ние: chẻ theo приключи́ться «xảy đến», KHÔNG ghép ключ «chìa khoá» (xem B).
Họ hàng cố ý vắng: бока́л, бере́т (từ mượn đứng một mình).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
# бока́л, бельё đang có ngoặc = chú thích của USER ⇒ không viết V.
V = {
    "труба": "ống, đường ống, ống khói, kèn",                # thiếu chimney, trumpet
    "ворота": "cổng, khung thành",                           # dấu ; -> dấu phẩy
    "подвал": "tầng hầm, hầm chứa",                          # thiếu cellar
    "стекло": "kính, thuỷ tinh, tấm kính, cửa kính xe",      # thiếu chất liệu glass, car window
    "палата": "phòng bệnh, viện quốc hội",                   # thiếu chamber/house
    "гонка": "cuộc đua, sự hối hả",                          # thiếu rush/haste
    "отделение": "chi nhánh, phòng ban, khoa, khoang, sự tách ra",  # thiếu ward, compartment, separation
    "агентство": "hãng, đại lý, cơ quan",                    # bỏ «công ty» (nới rộng), thêm agency nhà nước
}

# --------------------------------------------------------------------- труба
S["труба"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">труб-</span>'
    '<span class="hd-gloss">ỐNG — như trong <b>тру́бка</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mọi thứ hình ống dài: ống nước, ống khói, cả cây kèn trumpet. '
    'Số nhiều trọng âm lùi lên gốc: <b>труба́ → тру́бы</b>.</div>'
    '<div class="hd-warn"><b>вы́лететь в трубу́</b> — phá sản (bay ra ống khói).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тру́бка</b> ống nhỏ, ống nghe điện thoại, tẩu · '
    '<b>трубопрово́д</b> đường ống dẫn · <b>труба́ч</b> người thổi kèn</div>'
)

# --------------------------------------------------------------------- ворота
S["ворота"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được bằng mắt thường — gốc <b>вор-</b> «chắn, đóng lối» '
    'chỉ còn thấy trong vài động từ ở mục Họ hàng.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỉ có SỐ NHIỀU: một cái cổng vẫn là <b>воро́та</b>, đi với dạng số nhiều: '
    '<b>воро́та откры́ты</b> cổng đang mở.</div>'
    '<div class="hd-warn"><b>врата́</b> là dạng cổ của <b>воро́та</b> ⇒ <b>врата́рь</b> '
    '«người giữ cổng» = thủ môn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отвори́ть</b> mở (cửa, cổng) · <b>затвори́ть</b> đóng lại · '
    '<b>врата́рь</b> thủ môn</div>'
    '<div class="hd-warn">⚠️ Mức tin: nối <b>воро́та</b> với <b>отвори́ть</b> là từ nguyên '
    '(tiếng Litva <i>atverti</i> mở / <i>užverti</i> đóng), không phải luật suy ra được.</div>'
)

# --------------------------------------------------------------------- помещение
S["помещение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">đặt vào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мещ-</span>'
    '<span class="hd-gloss">CHỖ — chính là <b>мест-</b> của <b>ме́сто</b>, <b>ст → щ</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>помести́ть</b> đặt vào chỗ ⇒ <b>помеще́ние</b> chỗ để đặt người, đồ '
    '⇒ phòng, mặt bằng. Từ hơi trang trọng (văn phòng, kho, toà nhà); phòng trong nhà ở '
    'thì nói <b>ко́мната</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ме́сто</b> chỗ · <b>помести́ть</b> đặt vào · '
    '<b>вмести́ть</b> chứa vừa · <b>ме́стный</b> địa phương</div>'
)

# --------------------------------------------------------------------- холодильник
S["холодильник"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">холод-</span>'
    '<span class="hd-gloss">LẠNH — gốc của <b>хо́лод</b>, <b>холо́дный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-</span>'
    '<span class="hd-gloss">thân động từ <b>холоди́ть</b> làm lạnh</span></div>'
    '<div class="hd-row"><span class="hd-piece">-льник</span>'
    '<span class="hd-gloss">«đồ dùng để làm việc đó»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái máy làm lạnh. Đuôi <b>-льник</b> gắn vào động từ ra đồ vật: '
    '<b>буди́ть</b> đánh thức → <b>буди́льник</b> đồng hồ báo thức.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>хо́лод</b> cái lạnh · <b>холо́дный</b> lạnh · '
    '<b>морози́льник</b> ngăn đá (cùng đuôi) · <b>буди́льник</b> đồng hồ báo thức (cùng đuôi)</div>'
)

# --------------------------------------------------------------------- подвал
S["подвал"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span>'
    '<span class="hd-gloss">DƯỚI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вал</span>'
    '<span class="hd-gloss">phần còn lại — không cần chẻ tiếp</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tầng nằm DƯỚI ngôi nhà ⇒ tầng hầm, hầm chứa đồ. Chỉ cần nhớ <b>под-</b>, '
    'nghĩa đã ra.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">cùng tiền tố <b>под-</b> «dưới»: <b>подзе́мный</b> ngầm dưới đất · '
    '<b>подоко́нник</b> bậu cửa sổ (dưới cửa sổ)</div>'
)

# --------------------------------------------------------------------- бокал
S["бокал"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn châu Âu, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ly có chân, cho vang, sâm panh. Đừng lẫn: <b>стака́н</b> cốc không chân '
    '(nước, trà) · <b>рю́мка</b> ly nhỏ cho rượu mạnh.</div>'
    '<div class="hd-warn"><b>подня́ть бока́л за</b> + cách 4 — nâng ly chúc mừng ai/điều gì.</div>'
)

# --------------------------------------------------------------------- стекло
S["стекло"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">стекл-</span>'
    '<span class="hd-gloss">KÍNH, THUỶ TINH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́</span>'
    '<span class="hd-gloss">đuôi giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vừa là chất liệu, vừa là tấm kính (cửa sổ, kính xe). Số nhiều trọng âm '
    'lên gốc và <b>е</b> thành <b>ё</b>: <b>стёкла</b>, cách 2 <b>стёкол</b> (chen <b>о</b>).</div>'
    '<div class="hd-warn"><b>стекля́нный</b> bằng kính — viết <b>-нн-</b>, một trong ba ngoại lệ '
    'phải thuộc cùng <b>деревя́нный</b> bằng gỗ, <b>оловя́нный</b> bằng thiếc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>стекля́нный</b> bằng kính · <b>стёклышко</b> mảnh kính nhỏ · '
    '<b>стеко́льщик</b> thợ lắp kính</div>'
)

# --------------------------------------------------------------------- палата
S["палата"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn (Hy Lạp–Latin <i>palatium</i>), không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc tiếng Anh <i>palace</i>: gian phòng lớn ⇒ nay là phòng bệnh '
    'và «viện» của quốc hội. Phòng trong bệnh viện là <b>пала́та</b>, không phải <b>ко́мната</b>.</div>'
    '<div class="hd-warn"><b>Пала́та представи́телей</b> — Hạ viện (Mỹ).</div>'
)

# --------------------------------------------------------------------- легенда
S["легенда"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn Latin, không chẻ trong tiếng Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>legend</i> tiếng Anh — Latin <i>legenda</i> «điều để đọc». '
    'Chỉ lệch trọng âm: <b>леге́нда</b> nhấn giữa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>легенда́рный</b> huyền thoại, lừng danh</div>'
)

# --------------------------------------------------------------------- бельё
S["бельё"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бел-</span>'
    '<span class="hd-gloss">TRẮNG — gốc của <b>бе́лый</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ьё</span>'
    '<span class="hd-gloss">danh từ tập hợp, không đếm được</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen «đồ vải trắng» (vải tẩy trắng) ⇒ đồ lót, ga gối, đồ đem giặt. '
    'Tập hợp nên KHÔNG có số nhiều; trọng âm luôn ở cuối: <b>белья́</b>.</div>'
    '<div class="hd-warn"><b>ни́жнее бельё</b> đồ lót · <b>посте́льное бельё</b> ga gối.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бе́лый</b> trắng · <b>бели́ть</b> quét vôi, tẩy trắng · '
    '<b>сырьё</b> nguyên liệu (cùng đuôi <b>-ьё</b>)</div>'
)

# --------------------------------------------------------------------- берет
S["берет"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn Pháp <i>béret</i>, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mũ nồi, nhấn âm cuối như tiếng Pháp: <b>бере́т</b>.</div>'
    '<div class="hd-warn">Đừng nhầm với <b>берёт</b> «(nó) lấy» của <b>брать</b> — sách báo '
    'bỏ dấu <b>ё</b> thì hai chữ viết y hệt, nhìn câu mà đoán.</div>'
)

# --------------------------------------------------------------------- кукла
S["кукла"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Số nhiều cách 2 chen <b>о</b> vào giữa: <b>ку́кол</b> (như '
    '<b>ло́дка → ло́док</b>).</div>'
    '<div class="hd-warn"><b>ку́кольный теа́тр</b> — nhà hát múa rối.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ку́колка</b> búp bê nhỏ, con nhộng · <b>ку́кольный</b> thuộc búp bê, rối</div>'
)

# --------------------------------------------------------------------- приключение
S["приключение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">TỚI, đến với mình</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ключ-</span>'
    '<span class="hd-gloss">gốc của <b>приключи́ться</b> «xảy đến»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Điều bất ngờ xảy đến với mình ⇒ cuộc phiêu lưu. '
    '<b>Что с тобо́й приключи́лось?</b> — Có chuyện gì xảy ra với cậu vậy?</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>приключи́ться</b> xảy đến · <b>приключе́нческий</b> phiêu lưu '
    '(<b>приключе́нческий фильм</b> phim phiêu lưu)</div>'
)

# --------------------------------------------------------------------- бал
S["бал"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn Pháp <i>bal</i>, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= <i>ball</i> «dạ hội» tiếng Anh. Số nhiều trọng âm nhảy ra đuôi: '
    '<b>балы́</b>, <b>бало́в</b>.</div>'
    '<div class="hd-warn"><b>на балу́</b> — ở dạ hội: sau <b>на</b> chỉ chỗ thì đuôi <b>-у́</b>, '
    'không phải <b>-е</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бале́т</b> múa ba lê · <b>ба́льный</b> thuộc dạ hội '
    '(<b>ба́льные та́нцы</b> khiêu vũ dạ hội)</div>'
)

# --------------------------------------------------------------------- гонка
S["гонка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">гон-</span>'
    '<span class="hd-gloss">ĐUỔI, PHÓNG — gốc của <b>гнать</b> (<b>гн/гон</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-а</span>'
    '<span class="hd-gloss">→ danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đua nhau phóng, đuổi nhau ⇒ cuộc đua; nghĩa rộng: sự hối hả. '
    'Số nhiều cách 2 chen <b>о</b>: <b>го́нок</b>.</div>'
    '<div class="hd-warn"><b>го́нка вооруже́ний</b> — cuộc chạy đua vũ trang.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гнать</b> đuổi, lùa, phóng nhanh · <b>догна́ть</b> đuổi kịp · '
    '<b>пого́ня</b> cuộc truy đuổi · <b>го́нщик</b> tay đua</div>'
)

# --------------------------------------------------------------------- растение
S["растение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раст-</span>'
    '<span class="hd-gloss">MỌC, LỚN LÊN — gốc của <b>расти́</b> (<b>рас/рос</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cái mọc lên» ⇒ cây, thực vật.</div>'
    '<div class="hd-warn"><b>ко́мнатное расте́ние</b> — cây trồng trong nhà.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>расти́</b> mọc, lớn lên · <b>вы́расти</b> lớn lên · '
    '<b>расти́тельность</b> thảm thực vật · <b>рост</b> chiều cao · <b>во́зраст</b> tuổi</div>'
)

# --------------------------------------------------------------------- отделение
S["отделение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">TÁCH RA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дел-</span>'
    '<span class="hd-gloss">CHIA — gốc của <b>дели́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>отдели́ть</b> tách ra ⇒ phần được tách ra: chi nhánh, khoa (bệnh viện), '
    'khoang, và cả chính sự tách ra.</div>'
    '<div class="hd-warn"><b>отделе́ние ба́нка</b> chi nhánh ngân hàng · '
    '<b>отделе́ние поли́ции</b> đồn công an.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дели́ть</b> chia · <b>отдели́ть</b> tách ra · <b>отде́л</b> phòng, ban · '
    '<b>отде́льный</b> riêng biệt · <b>разде́л</b> phần, mục</div>'
)

# --------------------------------------------------------------------- агентство
S["агентство"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">аге́нт-</span>'
    '<span class="hd-gloss">người đại diện — mượn Latin <i>agens</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ство</span>'
    '<span class="hd-gloss">→ danh từ giống trung: tổ chức, hoạt động</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Y như tiếng Anh <i>agent → agency</i>. Cùng khuôn người + <b>-ство</b> '
    '→ tổ chức: <b>мини́стр → министе́рство</b> bộ.</div>'
    '<div class="hd-warn"><b>туристи́ческое аге́нтство</b> công ty du lịch · '
    '<b>аге́нтство недви́жимости</b> văn phòng bất động sản.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>аге́нт</b> người đại diện, điệp viên · <b>министе́рство</b> bộ (cùng đuôi)</div>'
)

# --------------------------------------------------------------------- совесть
S["совесть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">CÙNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вес-ть</span>'
    '<span class="hd-gloss">BIẾT — gốc <b>вед-/вес-</b> của <b>ве́дать</b>, <b>весть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cái cùng biết» với mình — y hệt tiếng Anh <i>con-science</i> '
    '(<i>con-</i> cùng + <i>science</i> biết).</div>'
    '<div class="hd-warn"><b>угрызе́ния со́вести</b> — cắn rứt lương tâm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>со́вестно</b> thấy ngượng, áy náy · <b>бессо́вестный</b> vô liêm sỉ · '
    '<b>весть</b> tin tức · <b>изве́стный</b> nổi tiếng</div>'
)

B = {
    "docbangmat": 58,
    "loitubat": 1,   # ворота: gọi откры́ты là «động từ» (thực ra là dạng ngắn) -> sửa câu
    "nguonsai": 1,   # агентство: bỏ «công ty» trong đề bài cũ (nới rộng, gloss Anh chỉ là agency)
    "baolen": [
        "Máy bắt 2 lỗi trọng âm CỦA TÔI, đã sửa: вра́та -> врата́, подо́конник -> подоко́нник (không tính vào loitubat vì không tự thấy).",
        "ворота: máy kêu воро́т (cách 2 số nhiều, đúng) lệch во́рот «cổ áo» = đồng tự; đã BỎ câu đó (dạng đúng quy tắc) thay vì nới MIEN_TRU.",
        "приключение: KHÔNG ghép ключ «chìa khoá» — chẻ theo приключи́ться «xảy đến»; cùng gốc xa với ключ có thật nhưng không dạy được.",
        "ворота <-> отвори́ть/затвори́ть: ghi ô ⚠️ Mức tin (từ nguyên, Litva atverti/užverti). врата́/врата́рь là dạng Slavơ Nhà thờ — chắc.",
        "бельё <- бе́лый: theo từ điển từ nguyên (Шанский) «vải tẩy trắng»; khá chắc nên không gắn Mức tin — cần duyệt nếu muốn chặt hơn.",
        "подвал: không chẻ -вал (từ nguyên không chắc), chỉ dạy под- «dưới».",
        "бокал, бельё: đề tiếng Việt đang có ngoặc = chú thích của user -> không viết V.",
        "V cần duyệt: агентство bỏ «công ty» (đụng компания/фирма); палата thêm «viện quốc hội»; стекло thêm «thuỷ tinh, cửa kính xe»; отделение thêm «khoa, khoang, sự tách ra»; гонка thêm «sự hối hả».",
    ],
}
