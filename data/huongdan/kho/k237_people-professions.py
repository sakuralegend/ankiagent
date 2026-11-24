# -*- coding: utf-8 -*-
"""k237 — people::professions: dáng vẻ (dáng đi, nếp nhăn, lông mi), sống tới, đạo – nước, người theo nghề và vai.

Chỗ cần nhất quán trong lô:
(1) дожива́ть / дожи́ть: до- TỚI TẬN ĐÍCH (khớp дойти́ [k49]) + -жи- SỐNG; khuôn прожи́ть [k127], выжива́ть [k168].
(2) правосла́вие: mảnh y hệt правосла́вный [k181]; сооте́чественник: со- + оте́чественный [k168] + -ик, khuôn совреме́нник [k220].
(3) -ница / -щица NGƯỜI NỮ: домрабо́тница, убо́рщица; -ент NGƯỜI: оппоне́нт, интеллиге́нт (khớp конкуре́нт [k202]).
(4) -лог NGƯỜI NGHIÊN CỨU: гинеко́лог khớp стомато́лог [k233]; -ин MỘT người: дворяни́н khớp граждани́н [k121].
(5) прее́мник: gốc ём/ня/ним LẤY (приня́ть [k113]); оппоне́нт: оп- khớp оппози́ция [k231].
Họ hàng không vắng ở thẻ nào.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "походка": "dáng đi, cách đi",                                       # «bước đi» là шаг / шагать
    "зрительный": "thuộc thị giác, thuộc thị lực, bằng mắt",             # «thị giác» trơ là danh từ зрение
    "доживать": "sống đến, sống đủ lâu để thấy, sống nốt, sống cho hết",  # gloss hai thể như nhau, đề cũ mỗi thể một nửa
    "дожить": "sống đến, sống đủ lâu để thấy, sống nốt, sống cho hết",    # cặp thể cùng dãy
    "латинский": "La Tinh, thuộc tiếng La Tinh",                         # «thuộc vùng Latin» không có trong gloss
    "соотечественник": "đồng bào, người cùng nước, người đồng hương",    # compatriot = cùng NƯỚC; «cùng quê hương» là земляк
    "оппонент": "đối thủ, đối thủ tranh luận, người phản biện",          # «người tranh luận đối lập» là diễn giải
    "уборщица": "cô lao công, chị dọn dẹp, nữ tạp vụ",                   # «người phụ nữ làm vệ sinh» là diễn giải
    "гинеколог": "bác sĩ phụ khoa",                                      # sản khoa là акушер, gloss không có
    "преемник": "người kế nhiệm, người nối nghiệp",                      # «thừa kế chức vụ» là diễn giải
}

# --------------------------------------------------------------------- походка
S["походка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ход-</span>'
    '<span class="hd-gloss">ĐI — gốc của <b>ходи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">→ danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái cách một người <b>хо́дит</b> ⇒ dáng đi: <b>лёгкая похо́дка</b> dáng đi nhẹ nhàng. '
    'Nhận ra ai NHỜ dáng đi → <b>по</b> + cách 3: <b>узна́ть по похо́дке</b>. Cách 2 số nhiều chen <b>о</b>: '
    '<b>похо́док</b>.</div>'
    '<div class="hd-warn">Anh <i>walk</i> có hai nghĩa, tiếng Nga tách đôi: dáng đi là <b>похо́дка</b>, cuộc dạo chơi là '
    '<b>прогу́лка</b>. Còn <b>похо́д</b> là chuyến đi dài ngày.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ходи́ть</b> đi lại · <b>похо́д</b> chuyến đi dã ngoại · <b>ход</b> sự chuyển động, nước đi · '
    '<b>вход</b> lối vào</div>'
)

# --------------------------------------------------------------------- морщина
S["морщина"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">морщ-</span>'
    '<span class="hd-gloss">NHĂN — như <b>мо́рщить</b> làm nhăn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́на</span>'
    '<span class="hd-gloss">một VẾT trên bề mặt, như <b>цара́пина</b> vết xước, <b>тре́щина</b> vết nứt</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Một vết nhăn» ⇒ nếp nhăn. Nhăn Ở ĐÂU → <b>на</b> + cách 6: <b>морщи́на на лбу</b> '
    '(<b>лоб</b> mất <b>о</b>). Trọng âm ở <b>-и́-</b>, khác <b>мо́рщить</b> và <b>цара́пина</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мо́рщить</b> làm nhăn (trán, mũi) · <b>мо́рщиться</b> nhăn mặt · '
    '<b>морщи́нка</b> nếp nhăn nhỏ · <b>морщи́нистый</b> nhăn nheo</div>'
)

# --------------------------------------------------------------------- ресница
S["ресница"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Với người học thì không chẻ được: <b>-ница</b> ở đây trông như đuôi người nữ của '
    '<b>учи́тельница</b>, nhưng từ này chỉ một sợi lông.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bộ ba quanh mắt: <b>ве́ко</b> mí mắt, trên mí mọc <b>ресни́цы</b> lông mi, cao hơn nữa là '
    '<b>бровь</b> lông mày. Một <b>ресни́ца</b> là một sợi; nói chung thì dùng số nhiều: '
    '<b>дли́нные ресни́цы</b>.</div>'
    '<div class="hd-warn">Mascara = <b>тушь для ресни́ц</b>; chải mascara = <b>кра́сить ресни́цы</b> (nghĩa đen «sơn lông '
    'mi»).</div>'
    '<div class="hd-warn">⚠️ Mức tin: từ nguyên, không suy ra được — từ điển nối với chữ cổ nghĩa «tua rua».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ресни́чка</b> sợi mi nhỏ (nói thân mật)</div>'
)

# --------------------------------------------------------------------- зрительный
S["зрительный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">зри-</span>'
    '<span class="hd-gloss">gốc NHÌN — như <b>зре́ние</b> thị lực</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тель-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ <b>-тельный</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thuộc việc NHÌN» ⇒ thuộc thị giác, bằng mắt: <b>зри́тельная па́мять</b> trí nhớ hình ảnh, '
    '<b>зри́тельный конта́кт</b> tiếp xúc bằng mắt. Trạng từ: <b>зри́тельно</b>.</div>'
    '<div class="hd-warn"><b>зри́тельный зал</b> = khán phòng — ở cụm này <b>зри́тельный</b> đi với <b>зри́тель</b>: '
    'gian của KHÁN GIẢ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>зри́тель</b> khán giả · <b>зре́ние</b> thị lực · <b>зрачо́к</b> con ngươi · '
    '<b>прозра́чный</b> trong suốt</div>'
)

# --------------------------------------------------------------------- вдовец
S["вдовец"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вдов-</span>'
    '<span class="hd-gloss">GÓA — <b>вдова́</b> bà góa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ц</span>'
    '<span class="hd-gloss">NGƯỜI (nam), như <b>продаве́ц</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc Ấn–Âu với Anh <i>widow</i>: <i>w-d-w</i> ↔ <b>в-д-в</b>. Tiếng Anh thêm <i>-er</i> cho '
    'người nam (<i>widower</i>), tiếng Nga thêm <b>-е́ц</b>.</div>'
    '<div class="hd-warn">Chữ <b>е</b> của <b>-ец</b> rụng ngay khi thêm đuôi, trọng âm ra cuối: <b>вдовца́, вдовцу́, '
    'вдовцо́м, вдовцы́</b> — cùng khuôn <b>продаве́ц → продавца́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вдова́</b> bà góa · <b>овдове́ть</b> góa vợ / góa chồng (HT)</div>'
)

# --------------------------------------------------------------------- доживать
S["доживать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-</span>'
    '<span class="hd-gloss">TỚI TẬN ĐÍCH — như <b>дойти́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-жи-</span>'
    '<span class="hd-gloss">SỐNG — như <b>жить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва́-ть</span>'
    '<span class="hd-gloss">hậu tố thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dạng CHT của <b>дожи́ть</b>. Đang đi nốt đoạn cuối ⇒ sống nốt, sống cho hết (+ cách 4); '
    'nói chung, hay lặp lại thì «sống đến»: <b>Здесь ча́сто дожива́ют до ста лет.</b> Chia đều: <b>дожива́ю</b>, '
    'y như <b>выжива́ть</b>.</div>'
    '<div class="hd-warn"><b>дожива́ть свой век</b> = sống nốt quãng đời cuối (<b>век</b> ở đây là «cả đời»).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дожи́ть</b> (HT) · <b>жить</b> sống · <b>жизнь</b> cuộc sống · <b>выжива́ть</b> sống sót '
    '(CHT)</div>'
)

# --------------------------------------------------------------------- дожить
S["дожить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-</span>'
    '<span class="hd-gloss">TỚI TẬN ĐÍCH — như <b>дойти́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-жи́-ть</span>'
    '<span class="hd-gloss">SỐNG — như <b>жить</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Sống và TỚI được mốc ⇒ sống đến. Mốc luôn là <b>до</b> + cách 2, y như <b>дойти́ до</b>: '
    '<b>дожи́ть до ста лет</b>, <b>дожи́ть до побе́ды</b>. Cặp CHT: <b>дожива́ть</b>.</div>'
    '<div class="hd-warn">Chia y như <b>жить</b>, mọc <b>в</b>: <b>доживу́, доживёшь</b>. Quá khứ giống cái dồn trọng âm '
    'ra cuối: <b>дожила́</b>; các dạng kia thì không.</div>'
    '<div class="hd-warn"><b>не дожи́ть до</b> = mất trước lúc đó: <b>Он не до́жил до пе́нсии.</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>жить</b> sống · <b>жизнь</b> cuộc sống · <b>прожи́ть</b> sống qua · <b>вы́жить</b> sống '
    'sót</div>'
)

# --------------------------------------------------------------------- православие
S["православие"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">право-</span>'
    '<span class="hd-gloss">ĐÚNG — như <b>пра́вый</b>, <b>пра́во</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-сла́в-</span>'
    '<span class="hd-gloss">TÔN VINH — như <b>сла́ва</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ие</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Sự tôn vinh (Chúa) cho đúng» — dịch từng mảnh <i>ortho-doxy</i> ⇒ đạo Chính Thống, '
    'một nhánh của <b>христиа́нство</b>. Viết chữ thường, chỉ dùng số ít.</div>'
    '<div class="hd-warn"><b>приня́ть правосла́вие</b> = theo, cải sang đạo này. Tín đồ là <b>правосла́вный</b>, tính từ '
    'dùng như danh từ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>правосла́вный</b> Chính Thống giáo, tín đồ · <b>сла́ва</b> vinh quang · '
    '<b>пра́вый</b> đúng; bên phải · <b>пра́вда</b> sự thật</div>'
)

# --------------------------------------------------------------------- латинский
S["латинский"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">лати́н-</span>'
    '<span class="hd-gloss">LA TINH — Anh <i>Latin</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ск-ий</span>'
    '<span class="hd-gloss">đuôi tính từ, như <b>ру́сский</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng chữ <i>Latin</i> thêm đuôi tính từ: <b>лати́нский алфави́т</b> bảng chữ cái La Tinh. '
    'Nói TÊN thứ tiếng thì <b>лати́нский язы́к</b>, gọn hơn là <b>латы́нь</b>.</div>'
    '<div class="hd-warn">Bẫy chính tả: <b>лати́нский</b> viết <b>и</b>, mà <b>латы́нь</b> lại viết <b>ы</b>.</div>'
    '<div class="hd-warn"><b>Лати́нская Аме́рика</b> Mỹ La Tinh — trong tên riêng thì viết hoa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>латы́нь</b> tiếng La Tinh · <b>лати́ница</b> chữ La Tinh (đối với <b>кири́ллица</b> chữ '
    'Kirin)</div>'
)

# --------------------------------------------------------------------- соотечественник
S["соотечественник"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">CÙNG — như <b>совреме́нник</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-оте́ч-еств-</span>'
    '<span class="hd-gloss">«đất của CHA» — <b>оте́чество</b> tổ quốc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-енн-ик</span>'
    '<span class="hd-gloss">NGƯỜI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người CÙNG tổ quốc ⇒ đồng bào. Dựng y khuôn <b>совреме́нник</b> người cùng thời: '
    '<b>оте́чественный</b> bỏ <b>-ый</b>, thêm <b>-ик</b>, nên giữ hai chữ <b>н</b>. Đầu từ có hai chữ <b>о</b>: một của '
    '<b>со-</b>, một của <b>оте́ц</b>.</div>'
    '<div class="hd-warn">Cùng NƯỚC là <b>сооте́чественник</b>; cùng tỉnh, cùng làng là <b>земля́к</b> '
    '(từ <b>земля́</b> đất).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оте́ц</b> cha · <b>оте́чество</b> tổ quốc · <b>оте́чественный</b> trong nước, nội địa · '
    '<b>сооте́чественница</b> nữ đồng bào</div>'
)

# --------------------------------------------------------------------- оппонент
S["оппонент"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">оп-</span>'
    '<span class="hd-gloss">ĐỐI LẠI (Latin <i>ob- → op-</i>) — như <b>оппози́ция</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-пон-</span>'
    '<span class="hd-gloss">ĐẶT (Latin <i>ponere</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́нт</span>'
    '<span class="hd-gloss">NGƯỜI đang làm — như <b>студе́нт</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chẻ theo Latin: «người đặt mình ở phía đối lại» = <i>opponent</i>. Hai chữ <b>п</b>: một của '
    '<b>оп-</b>, một của <b>-пон-</b>.</div>'
    '<div class="hd-warn">Chủ yếu là đối thủ TRANH LUẬN: <b>оппоне́нт на деба́тах</b>; trong trường là người phản biện '
    'luận án. Đối thủ trên sân thì thường nói <b>сопе́рник</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оппони́ровать</b> phản biện · <b>оппози́ция</b> phe đối lập · <b>пози́ция</b> lập trường · '
    '<b>компоне́нт</b> thành phần</div>'
)

# --------------------------------------------------------------------- стюардесса
S["стюардесса"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">стюард-</span>'
    '<span class="hd-gloss">TIẾP VIÊN — mượn Anh <i>steward</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́сс-а</span>'
    '<span class="hd-gloss">NGƯỜI NỮ = Anh <i>-ess</i>, như <b>принце́сса</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng chữ <i>stewardess</i>: trọng âm dồn vào đuôi nữ <b>-е́сс-</b>, hai chữ <b>с</b> như '
    '<i>-ess</i>. Anh <i>stew-</i> ở đây thành <b>стю-</b>.</div>'
    '<div class="hd-warn">Tên nghề chính thức: <b>бортпроводни́ца</b> — <b>борт</b> khoang máy bay, mạn tàu + '
    '<b>проводни́к</b> người đi theo phục vụ khách; nói chuyện thì <b>стюарде́сса</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>стю́ард</b> tiếp viên nam</div>'
)

# --------------------------------------------------------------------- домработница
S["домработница"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дом-</span>'
    '<span class="hd-gloss">NHÀ — rút từ <b>дома́шняя</b> (thuộc) nhà</span></div>'
    '<div class="hd-row"><span class="hd-piece">-рабо́т-</span>'
    '<span class="hd-gloss">LÀM VIỆC — <b>рабо́та</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ниц-а</span>'
    '<span class="hd-gloss">NGƯỜI NỮ, như <b>учи́тельница</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nói tắt của <b>дома́шняя рабо́тница</b> ⇒ người giúp việc nhà. Vì là từ rút gọn nên '
    '<b>дом</b> dính thẳng, không có <b>о</b> nối như <b>домохозя́йка</b>. Trọng âm giữ chỗ của '
    '<b>рабо́та</b>.</div>'
    '<div class="hd-warn"><b>домрабо́тница</b> được trả lương, làm ở nhà người khác; <b>домохозя́йка</b> lo việc nhà của '
    'chính mình (nội trợ).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рабо́та</b> công việc · <b>рабо́тник</b> người làm · <b>дом</b> nhà · '
    '<b>дома́шний</b> thuộc về nhà</div>'
)

# --------------------------------------------------------------------- уборщица
S["уборщица"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">RỜI KHỎI, ra xa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бо́р-</span>'
    '<span class="hd-gloss">LẤY — gốc <i>бр-/бер-</i> của <b>брать</b>, mặt <i>о</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-щиц-а</span>'
    '<span class="hd-gloss">NGƯỜI NỮ làm việc đó, như <b>продавщи́ца</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người làm <b>убо́рка</b> («lấy đi cho khỏi chỗ» ⇒ dọn dẹp) ⇒ cô lao công. Cắt là '
    '<b>убо́р-щица</b>, đừng thấy <b>борщ</b> trong đó: chữ <b>щ</b> thuộc về đuôi.</div>'
    '<div class="hd-warn"><b>убо́рщица</b> dọn công sở, trường học; <b>домрабо́тница</b> lo việc trong nhà riêng; '
    '<b>го́рничная</b> dọn phòng khách sạn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>убо́рка</b> sự dọn dẹp · <b>убира́ть</b> dọn (CHT) · <b>убра́ть</b> dọn (HT) · '
    '<b>убо́рщик</b> người dọn (nam)</div>'
)

# --------------------------------------------------------------------- гинеколог
S["гинеколог"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">гинеко-</span>'
    '<span class="hd-gloss">PHỤ NỮ (Hy Lạp <i>gynē, gynaiko-</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лог</span>'
    '<span class="hd-gloss">NGƯỜI NGHIÊN CỨU — như <b>био́лог</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chuyên gia về phụ nữ ⇒ bác sĩ phụ khoa. <b>гинеколо́гия</b> bỏ <b>-ия</b>, trọng âm lùi một âm: '
    '<b>гинеко́лог</b>, cùng khuôn <b>стоматоло́гия → стомато́лог</b>. Đi khám: <b>к гинеко́логу</b> '
    '(к + cách 3).</div>'
    '<div class="hd-warn">⚠️ Mức tin: từ nguyên, không suy ra được — Hy Lạp <i>gynē</i> cùng gốc Ấn–Âu với '
    '<b>жена́</b>, <b>же́нщина</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гинеколо́гия</b> phụ khoa · <b>гинекологи́ческий</b> thuộc phụ khoa · '
    '<b>стомато́лог</b> nha sĩ (cùng <b>-лог</b>)</div>'
)

# --------------------------------------------------------------------- акционерный
S["акционерный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">акци-</span>'
    '<span class="hd-gloss">CỔ PHIẾU — <b>а́кция</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-оне́р-</span>'
    '<span class="hd-gloss">NGƯỜI có thứ đó → <b>акционе́р</b> cổ đông</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vốn chia thành cổ phiếu, chủ là các <b>акционе́ры</b> ⇒ (thuộc) cổ phần. <b>-оне́р</b> như '
    '<b>пенсионе́р</b> người hưởng lương hưu. Dạng ngắn giống đực chen <b>е</b> (<b>акционе́рен</b>), nhưng thực tế hầu như '
    'không ai dùng.</div>'
    '<div class="hd-warn"><b>акционе́рное о́бщество</b> = công ty cổ phần, viết tắt <i>АО</i> — hai chữ đứng trước tên rất '
    'nhiều công ty Nga.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>а́кция</b> cổ phiếu; đợt khuyến mãi · <b>акционе́р</b> cổ đông · <b>акти́вный</b> năng động '
    '(cùng gốc Latin)</div>'
)

# --------------------------------------------------------------------- ботаник
S["ботаник"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бота́н-</span>'
    '<span class="hd-gloss">CÂY CỎ (Hy Lạp <i>botanē</i>) — Anh <i>botany</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ик</span>'
    '<span class="hd-gloss">NGƯỜI theo ngành, như <b>хи́мик</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>бота́ника</b> là ngành, bỏ <b>-а</b> ra người: <b>бота́ник</b> nhà thực vật học. Trọng âm đứng '
    'yên. Hai từ trùng nhau ở cách 6: <b>о бота́нике</b> = về môn, hoặc về người.</div>'
    '<div class="hd-warn">Tiếng lóng học trò: <b>бота́ник</b> (nói gọn <b>бота́н</b>) = mọt sách, hơi chế giễu — ngoài '
    'đời nghe nghĩa này nhiều hơn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бота́ника</b> thực vật học · <b>ботани́ческий сад</b> vườn bách thảo</div>'
)

# --------------------------------------------------------------------- преемник
S["преемник"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пре-</span>'
    '<span class="hd-gloss">CHUYỂN SANG — dạng sách vở của <b>пере-</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́м-</span>'
    '<span class="hd-gloss">LẤY — gốc <i>ём/ня/ним</i>, như <b>приня́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ник</span>'
    '<span class="hd-gloss">NGƯỜI, như <b>сотру́дник</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người NHẬN LẤY khi việc chuyển sang tay mình ⇒ người kế nhiệm. Kế nhiệm AI là cách 2: '
    '<b>прее́мник дире́ктора</b>. Hai chữ <b>е</b> liền: một của <b>пре-</b>, một của gốc.</div>'
    '<div class="hd-warn">Đừng lẫn <b>прее́мник</b> (<b>пре-е</b>, người kế nhiệm) với <b>приёмник</b> (<b>при-ё</b>, '
    'máy thu thanh) — cùng gốc LẤY, chỉ khác tiền tố.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>прее́мственность</b> tính kế thừa · <b>приём</b> sự tiếp đón · <b>приня́ть</b> nhận · '
    '<b>взять</b> lấy</div>'
)

# --------------------------------------------------------------------- дворянин
S["дворянин"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">двор-</span>'
    '<span class="hd-gloss">SÂN, và cả TRIỀU ĐÌNH — <b>двор</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ян-</span>'
    '<span class="hd-gloss">người thuộc về</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́н</span>'
    '<span class="hd-gloss">MỘT người — rụng ở số nhiều</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Người của triều đình» ⇒ nhà quý tộc.</div>'
    '<div class="hd-warn">Số nhiều rụng <b>-ин</b>, trọng âm lùi về <b>я</b>: <b>дворя́не</b>, cách 2 trụi đuôi: '
    '<b>дворя́н</b> — rụng y như <b>граждани́н → гра́ждане</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>двор</b> sân; triều đình · <b>дворе́ц</b> cung điện · <b>дворя́нка</b> nữ quý tộc · '
    '<b>дворя́нство</b> tầng lớp quý tộc · <b>дво́рник</b> người quét sân</div>'
)

# --------------------------------------------------------------------- интеллигент
S["интеллигент"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">интеллиг-</span>'
    '<span class="hd-gloss">HIỂU (Latin <i>intellegere</i>) — như <b>интелле́кт</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́нт</span>'
    '<span class="hd-gloss">NGƯỜI đang làm — như <b>студе́нт</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chẻ theo Latin: «người hiểu biết» ⇒ người trí thức. Gộp cả lớp người là '
    '<b>интеллиге́нция</b>. Tiếng Nga đòi thêm cả cách cư xử: <b>настоя́щий интеллиге́нт</b> thì phải nhã nhặn.</div>'
    '<div class="hd-warn">Bạn giả của Anh <i>intelligent</i>: người thông minh là <b>у́мный челове́к</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>интеллиге́нция</b> giới trí thức · <b>интеллиге́нтный</b> có học thức, lịch thiệp · '
    '<b>интелле́кт</b> trí tuệ</div>'
)

B = {
    "docbangmat": 71,
    "loitubat": 4,   # стюардесса: «Anh ste- thành стю-» sai mảnh -> stew-; проводник dịch «người đưa đường» lạc nghĩa -> người phục vụ khách
                     # дворянин: «cùng khuôn гражданин» nói quá (chỗ trọng âm lùi khác nhau) -> chỉ «rụng y như»
                     # оппонент: câu «mảnh trước một chữ, mảnh sau một chữ» khó hiểu -> nói rõ оп- và -пон-
    "nguonsai": 1,   # акционерный: bảng chia in dạng ngắn акционерен như bình thường; thực tế không dùng -> thẻ nói thẳng
    "baolen": [
        "V cần duyệt (10): походка (BỎ bước đi) · зрительный (thị giác trơ -> thuộc thị giác; THÊM bằng mắt) · доживать, дожить (gộp một dãy) · латинский (BỎ thuộc vùng Latin) · соотечественник (THÊM người cùng nước; BỎ người cùng quê hương = земляк) · оппонент (người tranh luận đối lập -> đối thủ tranh luận) · уборщица (THÊM cô lao công; người phụ nữ làm vệ sinh -> nữ tạp vụ) · гинеколог (BỎ sản phụ khoa, gloss không có) · преемник (BỎ người thừa kế chức vụ).",
        "Ví dụ GƯỢNG — походка câu 3 «В их походках» (số nhiều không ai nói). Thay: «В их походке сразу видна военная выправка.» / You can immediately see military bearing in their <b>gait</b>. / Trong <b>dáng đi</b> của họ thấy ngay phong thái quân nhân.",
        "Ví dụ GƯỢNG — зрительный câu 3 «Пользуйся зрительным контактом» (chuẩn là поддерживать). Thay: «С хорошей зрительной памятью учить слова легко.» / With a good <b>visual</b> memory it's easy to learn words. / Có trí nhớ <b>thị giác</b> tốt thì học từ rất dễ.",
        "зрительный câu 1 bôi đậm «Khán phòng / auditorium» là nghĩa của CẢ CỤM зрительный зал, không có trong V (cụm nằm ở ô đỏ của thẻ). Thay nếu muốn khớp đề: «Зрительный контакт очень важен на собеседовании.» / <b>Eye</b> contact is very important at an interview. / Tiếp xúc <b>bằng mắt</b> rất quan trọng khi phỏng vấn.",
        "ботаник: cả 3 câu dùng nghĩa lóng, nghĩa chính nhà thực vật học không có câu nào; câu 2 «шутить о ботанике» còn đọc lẫn với ботаника (môn học). Thay câu 2: «Мой дед был ботаником и изучал редкие цветы.» / My grandfather was a <b>botanist</b> and studied rare flowers. / Ông tớ là <b>nhà thực vật học</b>, chuyên nghiên cứu hoa quý hiếm.",
        "латинский câu 2 «Латинская музыка» là lối nói sao từ Anh (chuẩn: латиноамериканская). Thay: «Напиши своё имя латинскими буквами.» / Write your name in <b>Latin</b> letters. / Viết tên cậu bằng chữ cái <b>La Tinh</b> đi.",
        "Cả 3 câu соотечественник dịch «người đồng hương» — vẫn nằm trong V (đứng cuối); câu 1 nên đổi dịch thành «một <b>người cùng nước</b>» cho đúng nghĩa chính.",
        "доживать: «sống đến», «sống đủ lâu để thấy» có trong gloss nhưng cả 3 câu chỉ dùng «sống nốt»; дожить ngược lại — hệ quả của gộp dãy cặp thể.",
        "домработница ↔ горничная [k183, «nữ giúp việc»]: gần nghĩa nhưng không trùng hết; không đổi V.",
        "Không chắc / hạ mức tin bằng ô đỏ: ресница (từ nguyên «tua rua»); гинеколог ↔ жена (từ nguyên Ấn–Âu). стюард nhấn стю́ард theo từ điển, khẩu ngữ hay nghe стюа́рд — thẻ chỉ ghi dạng từ điển. дожить: quá khứ giống đực có hai chuẩn до́жил / дожи́л, thẻ ghi до́жил.",
        "Trùng hết nghĩa trong lô chỉ có cặp доживать/дожить — badge thể tách. Không gặp lỗi trọng âm ở thẻ cũ đã đọc.",
    ],
}
