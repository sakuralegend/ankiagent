# -*- coding: utf-8 -*-
"""k179 — nature::weather (lô trộn): thời tiết, địa hình, từ mượn Pháp/Latin, vài danh từ -ение.

Chỗ cần nhất quán trong lô:
(1) biến âm phụ âm trước hậu tố, mỗi thẻ một câu, không bảng: верх → верши́на (х→ш),
    знак → значо́к (к→ч), бе́рег → побере́жье (г→ж), изобрази́ть → изображе́ние (з→ж),
    учреди́ть → учрежде́ние (д→жд).
(2) -ина → danh từ: верши́на, доли́на — cùng khuôn, mỗi thẻ nói về chính nó.
(3) từ mượn KHÔNG chẻ: сеа́нс, мо́да, бриллиа́нт (Pháp), репети́ция (Latin), обезья́на (Ba Tư qua Thổ).
(4) трусы́ ↔ тру́сы (số nhiều của трус [đã có thẻ]) — một ô đỏ tách, vì user đã học трус.
(5) приро́дный ↔ есте́ственный [đã có thẻ] cùng «tự nhiên» — một ô đỏ tách nghĩa.
Họ hàng cố ý vắng: сеа́нс (từ mượn đứng một mình), доли́на (họ chỉ còn từ cổ дол / подо́л).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "ель": "cây vân sam, cây linh sam",
    "репетиция": "buổi diễn tập, sự tập dượt",   # rehearsal; «buổi tập» là трениро́вка [k134]; bỏ «tổng duyệt» (= dress rehearsal, hẹp hơn)
    "сеанс": "suất chiếu, buổi chiếu, buổi diễn, phiên",  # session/sitting; «ca» dễ lẫn ca làm việc (сме́на)
    "мода": "mốt, thời trang",                   # fashion/vogue; «xu hướng» là nới rộng (= тенде́нция)
}

# --------------------------------------------------------------------- плёнка
S["плёнка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">плён-</span>'
    '<span class="hd-gloss">MÀNG MỎNG — gốc không còn đứng riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">→ danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mọi nghĩa đều là <b>một lớp mỏng</b>: màng bọc thực phẩm '
    '(<i>пищева́я плёнка</i>), lớp váng, rồi cuộn phim — dải nhựa mỏng phủ thuốc ảnh. '
    'Số nhiều cách 2 chen <b>о</b> vào giữa <b>н</b> và <b>к</b>: <b>плёнок</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>плёночный</b> thuộc phim (<i>плёночный фотоаппара́т</i> máy ảnh phim)</div>'
)

# --------------------------------------------------------------------- изображение
S["изображение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">из-</span>'
    '<span class="hd-gloss">RA NGOÀI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ображ-</span>'
    '<span class="hd-gloss">HÌNH — <b>о́браз</b> (з → ж)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>изобрази́ть / изобража́ть</b> «đưa hình ra ngoài» = khắc họa: '
    'vừa là việc mô tả, vừa là chính cái hình làm ra. <b>з</b> của động từ thành <b>ж</b> '
    'trước <b>-ение</b>: <b>изобрази́ть → изображе́ние</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>изобража́ть</b> khắc họa · <b>о́браз</b> hình tượng · '
    '<b>образе́ц</b> mẫu, hình mẫu</div>'
)

# --------------------------------------------------------------------- сеанс
S["сеанс"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn tiếng Pháp <i>séance</i> «buổi ngồi» — không chẻ được trong tiếng Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một khoảng thời gian định sẵn mà người ta «ngồi vào» một việc: suất chiếu '
    'phim (<i>после́дний сеа́нс</i> suất cuối), buổi trị liệu, phiên liên lạc (<i>сеа́нс свя́зи</i>).</div>'
    '<div class="hd-warn">Tiếng Anh <i>seance</i> chỉ còn nghĩa gọi hồn — tiếng Nga phải nói rõ '
    '<b>спирити́ческий сеа́нс</b>. Đứng một mình, <b>сеа́нс</b> thường là suất chiếu.</div>'
)

# --------------------------------------------------------------------- репетиция
S["репетиция"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">репет-</span>'
    '<span class="hd-gloss">LẶP LẠI — Latin <i>repetere</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-иция</span>'
    '<span class="hd-gloss">= Anh <i>-ition</i>, danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Diễn đi diễn lại trước buổi thật ⇒ buổi diễn tập. '
    'Tổng duyệt là <b>генера́льная репети́ция</b>.</div>'
    '<div class="hd-warn">Bạn giả: «sự lặp lại» là <b>повторе́ние</b>, không phải <b>репети́ция</b>. '
    'Tập thể thao là <b>трениро́вка</b>; <b>репети́ция</b> là tập cho sân khấu, hoà nhạc, buổi lễ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>репети́ровать</b> diễn tập · <b>репети́тор</b> gia sư (người luyện bài cho học trò)</div>'
)

# --------------------------------------------------------------------- мода
S["мода"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn tiếng Pháp <i>mode</i> — gốc trơn, không chẻ. Cùng gốc tiếng Anh <i>mode</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hai cụm hằng ngày: <b>в мо́де</b> đang mốt · <b>вы́йти из мо́ды</b> lỗi mốt.</div>'
    '<div class="hd-warn"><b>после́дний крик мо́ды</b> — mốt mới nhất (nghĩa đen «tiếng thét cuối cùng của mốt»).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мо́дный</b> hợp mốt · <b>мо́дница</b> cô nàng sành mốt</div>'
)

# --------------------------------------------------------------------- значок
S["значок"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">знач-</span>'
    '<span class="hd-gloss">DẤU — <b>знак</b> (к → ч)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́к</span>'
    '<span class="hd-gloss">hậu tố nhỏ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cái dấu nhỏ» ⇒ huy hiệu cài áo, biểu tượng nhỏ trên màn hình. '
    'Chữ <b>о</b> của <b>-о́к</b> rơi khi thêm đuôi, trọng âm chuyển sang đuôi mới: '
    '<b>значо́к → значка́, значку́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>знак</b> dấu hiệu · <b>зна́чить</b> có nghĩa là · '
    '<b>значе́ние</b> ý nghĩa · <b>обозна́чить</b> đánh dấu</div>'
)

# --------------------------------------------------------------------- бриллиант
S["бриллиант"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn tiếng Pháp <i>brillant</i> «lấp lánh» — cùng gốc tiếng Anh <i>brilliant</i>, '
    'không chẻ. Chính tả giữ <b>hai л</b> như tiếng Anh.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Viên kim cương đã được mài giác để <i>lấp lánh</i>.</div>'
    '<div class="hd-warn"><b>алма́з</b> = kim cương thô; mài giác xong mới gọi là <b>бриллиа́нт</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бриллиа́нтовый</b> bằng kim cương, nạm kim cương</div>'
)

# --------------------------------------------------------------------- трусы
S["трусы"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được. <b>Chỉ có số nhiều</b>, như <b>брю́ки</b> — không có dạng số ít; '
    'trọng âm nằm ở đuôi suốt bảng: <b>трусо́в, труса́м</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: thường được cho là mượn tiếng Anh <i>trousers</i> — đó là từ nguyên, '
    'không phải luật suy ra được.</div>'
    '<div class="hd-warn">Khác gốc với <b>трус</b> kẻ nhát gan: số nhiều của nó giữ trọng âm ĐẦU '
    '(<b>тру́сов, тру́сам</b>) — chỉ dấu nhấn tách «những kẻ hèn» với «quần lót».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тру́сики</b> quần lót (dạng nhỏ)</div>'
)

# --------------------------------------------------------------------- обезьяна
S["обезьяна"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: <b>о-</b>, <b>без-</b> ở đây KHÔNG phải tiền tố, dù trông giống.</div>'
    '<div class="hd-warn">⚠️ Mức tin: từ nguyên thường nêu là mượn tiếng Ba Tư qua tiếng Thổ — '
    'không phải luật suy ra được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiếng Nga cũng dùng con khỉ cho việc bắt chước, giống tiếng Anh <i>to ape</i>: '
    '<b>обезья́нничать</b> = bắt chước như khỉ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обезья́нничать</b> bắt chước · <b>обезья́ний</b> thuộc khỉ</div>'
)

# --------------------------------------------------------------------- ель
S["ель"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được. Đuôi <b>-ь</b> mà là giống cái.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thêm <b>-ка</b> và <b>е</b> thành <b>ё</b> là ra <b>ёлка</b> — cây <b>ель</b> nhỏ, '
    'chính là cây thông Noel.</div>'
    '<div class="hd-warn">Cây thông Noel nói <b>ёлка</b>, không nói <b>ель</b>. '
    'Thông lá dài (<i>pine</i>) là từ khác: <b>сосна́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ёлка</b> cây thông Noel · <b>ело́вый</b> thuộc vân sam (<i>ело́вая ши́шка</i> quả thông)</div>'
)

# --------------------------------------------------------------------- природный
S["природный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">GẦN, KÈM THEO</span></div>'
    '<div class="hd-row"><span class="hd-piece">-род-</span>'
    '<span class="hd-gloss">SINH RA — như <b>род</b>, <b>роди́ться</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">→ tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tính từ của <b>приро́да</b>: cái có sẵn từ lúc sinh ra ⇒ thuộc thiên nhiên '
    '(<i>приро́дный газ</i> khí tự nhiên) hoặc bẩm sinh (<i>приро́дный тала́нт</i>).</div>'
    '<div class="hd-warn"><b>есте́ственный</b> cũng là «tự nhiên» nhưng theo nghĩa <i>hiển nhiên, '
    'không gượng ép</i>; <b>приро́дный</b> là <i>thuộc thiên nhiên, trời sinh</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>приро́да</b> thiên nhiên · <b>род</b> dòng họ · '
    '<b>роди́ться</b> được sinh ra · <b>наро́д</b> dân tộc</div>'
)

# --------------------------------------------------------------------- поток
S["поток"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng đáng nhớ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ток</span>'
    '<span class="hd-gloss">CHẢY — gốc của <b>течь</b> (е → о)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Động từ <b>течь</b> «chảy» thành danh từ thì <b>е</b> đổi <b>о</b>: <b>ток</b>. '
    'Cái gì chảy thành dòng đều là <b>пото́к</b>: dòng nước, dòng người, luồng thông tin.</div>'
    '<div class="hd-warn"><b>поста́вить на пото́к</b> — đưa vào sản xuất hàng loạt.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>течь</b> chảy · <b>тече́ние</b> dòng chảy · <b>ток</b> dòng điện · '
    '<b>исто́к</b> nguồn sông</div>'
)

# --------------------------------------------------------------------- дым
S["дым"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được. Cùng gốc Ấn–Âu với Latin <i>fūmus</i> → tiếng Anh <i>fume</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hai dạng giới cách: <b>о ды́ме</b> khi nói VỀ khói, nhưng <b>в дыму́</b> '
    'khi ở TRONG khói — đuôi <b>-у́</b> mang trọng âm, như <b>в лесу́</b>.</div>'
    '<div class="hd-warn"><b>Нет ды́ма без огня́.</b> — Không có lửa làm sao có khói.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дыми́ть</b> bốc khói · <b>ды́мка</b> làn sương mờ · <b>дымохо́д</b> ống khói</div>'
)

# --------------------------------------------------------------------- молния
S["молния"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc là tia chớp; từ đó mở rộng sang khoá kéo '
    '(<i>застёжка-мо́лния</i>), và sang điện tín, bản tin khẩn — tin đến nhanh như chớp.</div>'
    '<div class="hd-warn">Một cơn <b>гроза́</b> có hai phần: <b>мо́лния</b> là tia sáng, '
    'còn tiếng nổ (sấm) là <b>гром</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>молниено́сный</b> nhanh như chớp</div>'
)

# --------------------------------------------------------------------- буря
S["буря"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gió mạnh kèm mưa, tuyết hay cát: <i>сне́жная бу́ря</i> bão tuyết. '
    'Dùng cả nghĩa bóng: <i>бу́ря аплодисме́нтов</i> tràng vỗ tay như bão.</div>'
    '<div class="hd-warn"><b>бу́ря в стака́не воды́</b> — chuyện bé xé ra to (nghĩa đen «bão trong cốc nước»).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бу́рный</b> dữ dội, sôi nổi</div>'
)

# --------------------------------------------------------------------- долина
S["долина"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дол-</span>'
    '<span class="hd-gloss">THUNG, chỗ trũng — từ cổ, nay chỉ còn trong thơ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ина</span>'
    '<span class="hd-gloss">→ danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc Ấn–Âu với tiếng Anh <i>dale</i>, tiếng Đức <i>Tal</i>. '
    'Thung lũng Silicon là <b>Кре́мниевая доли́на</b>.</div>'
)

# --------------------------------------------------------------------- вершина
S["вершина"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">верш-</span>'
    '<span class="hd-gloss">PHẦN TRÊN — <b>верх</b> (х → ш)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ина</span>'
    '<span class="hd-gloss">→ danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỗ trên cùng của một vật: đỉnh núi, ngọn cây, đỉnh cao sự nghiệp, '
    'cả đỉnh tam giác trong toán. <b>х</b> của <b>верх</b> thành <b>ш</b> trước <b>-ина</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>верх</b> phần trên · <b>ве́рхний</b> ở trên · '
    '<b>наверху́</b> ở phía trên · <b>све́рху</b> từ trên</div>'
)

# --------------------------------------------------------------------- округ
S["округ"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">QUANH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-круг</span>'
    '<span class="hd-gloss">VÒNG TRÒN — <b>круг</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vùng được khoanh thành một vòng ⇒ khu hành chính, quận. '
    'Số nhiều cách 1 lấy đuôi <b>-а́</b> thay vì <b>-ы</b>, trọng âm ra đuôi suốt số nhiều: '
    '<b>округо́в, округа́м</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>круг</b> vòng tròn · <b>вокру́г</b> xung quanh · '
    '<b>окружа́ть</b> bao quanh</div>'
)

# --------------------------------------------------------------------- побережье
S["побережье"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">DỌC THEO</span></div>'
    '<div class="hd-row"><span class="hd-piece">-береж-</span>'
    '<span class="hd-gloss">BỜ — <b>бе́рег</b> (г → ж)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ье</span>'
    '<span class="hd-gloss">→ danh từ giống trung chỉ cả một vùng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cả dải đất chạy dọc bờ ⇒ vùng duyên hải. Cùng đuôi <b>-ье</b> chỉ vùng với '
    '<b>Подмоско́вье</b> vùng quanh Moskva. Số nhiều cách 2 ra <b>побере́жий</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бе́рег</b> bờ · <b>прибре́жный</b> ven bờ</div>'
)

# --------------------------------------------------------------------- региональный
S["региональный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">регион-</span>'
    '<span class="hd-gloss">VÙNG — <b>регио́н</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́льный</span>'
    '<span class="hd-gloss">→ tính từ (= Anh <i>-al</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiếng Anh <i>regional</i>: <i>-al</i> thành <b>-а́льный</b>, trọng âm luôn trên '
    '<b>-а́-</b>, như <b>национа́льный</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>регио́н</b> vùng, miền</div>'
)

# --------------------------------------------------------------------- учреждение
S["учреждение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng đáng nhớ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-чрежд-</span>'
    '<span class="hd-gloss">ĐẶT THEO THỨ TỰ (д → жд)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>учреди́ть</b> «lập ra»: vừa là việc thành lập, vừa là cái được '
    'lập ra ⇒ cơ quan. <b>д</b> thành <b>жд</b> trước <b>-ение</b>, như <b>роди́ть → рожде́ние</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: <b>чред-</b> là dạng Slavơ Nhà thờ của <b>черёд</b> «lượt», '
    'cùng gốc <b>о́чередь</b> — đó là từ nguyên, không phải luật suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>учреди́ть</b> thành lập · <b>учреди́тель</b> người sáng lập · '
    '<b>о́чередь</b> hàng chờ</div>'
)

B = {
    "docbangmat": 49,
    "loitubat": 2,
    "nguonsai": 2,
    "baolen": [
        "V репетиция: «buổi tập» (nằm gọn trong трениро́вка [k134]) -> «buổi diễn tập, sự tập dượt»; bỏ cả «tổng duyệt» vì đó là генера́льная репети́ция (hẹp hơn), đã đưa vào Cách nhớ. Sau khi nạp, va chạm này hết.",
        "Va chạm khác: không. Đã đối chiếu 3 dòng V với Vietnamese của 3255 thẻ — 0 nghĩa chung.",
        "Đồng tự, KHÔNG nới MIEN_TRU, đã sửa dữ liệu: (a) тру́сы (số nhiều của трус) khớp nhầm трусы́ — ô đỏ viết bằng тру́сов/тру́сам, cùng cách k167; (b) округа́ (số nhiều của о́круг) khớp nhầm окру́га «vùng xung quanh» — bỏ in đậm dạng cách 1, giữ округо́в/округа́м. Nếu luồng chính thêm (b) vào MIEN_TRU thì có thể in đậm lại округа́.",
        "Nguồn sai bác (nguonsai=2, đều là dòng Việt cũ): сеанс «ca» (dễ lẫn ca làm việc, gloss là session -> «phiên»); мода «xu hướng» (nới rộng, = тенде́нция). репетиция do luồng chính bắt, không tính.",
        "Lỗi tự bắt (loitubat=2): мода viết модни́ца -> đúng мо́дница (cửa soát bắt); изображение chẻ «-браж-» -> đúng «из- + -ображ-» (đọc lại tự thấy).",
        "Không chắc — đã hạ mức tin trên thẻ: трусы́ <- Anh trousers; обезья́на <- Ba Tư qua Thổ; учрежде́ние чред- = черёд/о́чередь. Viết như sự thật nhưng là từ nguyên (mức tin cao, chưa đối chiếu nguồn trong phiên): доли́на ~ Anh dale / Đức Tal; дым ~ Latin fūmus; плёнка «gốc плён- không còn đứng riêng» (плена chỉ còn là từ cổ). Sắc thái приро́дный vs есте́ственный là khái quát.",
        "Họ hàng cố ý vắng: сеа́нс (từ mượn Pháp đứng một mình), доли́на (họ chỉ còn дол/подо́л cổ). побере́жье cố ý KHÔNG nối бере́чь — khác gốc theo từ nguyên phổ biến, nối là sai.",
        "дым: câu chú ý dạy о ды́ме vs в дыму́ (đúng chỗ câu ví dụ trượt cổng máy 3 vòng).",
        "V cần duyệt (3 thẻ): репетиция, сеанс, мода. Các thẻ còn lại giữ dòng Việt cũ (đã đúng, chỉ nghĩa thật).",
    ],
}
