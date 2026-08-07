# -*- coding: utf-8 -*-
"""k45 — time: mốc thời gian đời thường (hôm qua/mai/kia · thứ trong tuần ·
mùa · năm · lần) + bốn hư từ neo trục thời gian (когда́ · никогда́ · уже́ ·
ра́ньше · снача́ла).
Trục thật của lô: gần như mỗi từ TỰ KHAI thời điểm của nó bằng một mảnh có
nghĩa — сред- giữa, пят- năm, четвер- bốn, крес- sống lại, за-утра sau sáng.
Mỗi thẻ phải chỉ ra ĐÚNG cái mảnh đó, chứ không dạy lại cả bộ lịch.
"""

# 🔴 KHÔNG dựng biến khối dùng chung (HE/LUAT/THE…) rồi cộng vào mọi thẻ.

S = {}
V = {}

# ------------------------------------------------------------------- когда́
S["когда"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ко-</span>'
    '<span class="hd-gloss">mảnh HỎI, y như đầu <b>кто</b>, <b>како́й</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-гда́</span>'
    '<span class="hd-gloss">mảnh chỉ THỜI ĐIỂM</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ghép hai mảnh ra đúng nghĩa đen «thời điểm nào?». '
    'Giữ nguyên <b>-гда</b> rồi thay mảnh đầu là được cả họ: <b>всегда́</b> '
    'luôn luôn · <b>иногда́</b> đôi khi · <b>никогда́</b> không bao giờ.</div>'
    '<div class="hd-warn">⚠️ <b>когда́</b> nối vào MỘT thời điểm («khi tôi đến»); '
    'còn muốn nói suốt một quãng đang diễn ra thì tiếng Nga dùng <b>пока́</b> '
    '(trong khi). Hai từ này rất dễ đổi chỗ cho nhau.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>всегда́</b> luôn luôn · <b>иногда́</b> đôi khi · '
    '<b>никогда́</b> không bao giờ</div>'
)

# ----------------------------------------------------------------- никогда́
S["никогда"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ни-</span>'
    '<span class="hd-gloss">tiền tố PHỦ ĐỊNH gắn vào từ hỏi</span></div>'
    '<div class="hd-row"><span class="hd-piece">когда́</span>'
    '<span class="hd-gloss">khi nào</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Khi nào» bị <b>ни-</b> dập tắt ⇒ «không khi nào». '
    'Cùng khuôn đó: <b>кто</b> ai → <b>никто́</b> không ai; <b>где</b> ở đâu → '
    '<b>нигде́</b> không đâu.</div>'
    '<div class="hd-warn">🔴 Tiếng Nga bắt buộc PHỦ ĐỊNH HAI LẦN: có '
    '<b>никогда́</b> thì trước động từ vẫn phải có <b>не</b> — '
    '<b>Я никогда́ не был в Москве́</b> (Tôi chưa bao giờ ở Moskva). '
    'Bỏ <b>не</b> là câu sai, không phải câu gọn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>когда́</b> khi nào · <b>всегда́</b> luôn luôn · '
    '<b>иногда́</b> đôi khi</div>'
)

# ------------------------------------------------------------------- среда́
S["среда"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сред-</span>'
    '<span class="hd-gloss">gốc GIỮA (<b>сре́дний</b> ở giữa, trung bình)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một gốc «giữa» đỡ cả hai nghĩa: tuần Nga mở đầu bằng '
    'thứ Hai nên <b>среда́</b> là ngày nằm GIỮA tuần; còn «môi trường» là cái '
    'vây quanh, ta ở GIỮA nó.</div>'
    '<div class="hd-warn">⚠️ Đúng MỘT ô của bảng chia tách hai nghĩa ra: cách 4 '
    'số ít là <b>сре́ду</b> khi nói thứ Tư (<b>в сре́ду</b> vào thứ Tư), nhưng '
    '<b>среду́</b> khi nói môi trường. Các cách còn lại hai nghĩa dùng chung.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сре́дний</b> ở giữa, trung bình · <b>середи́на</b> '
    'phần giữa · <b>среди́</b> giữa (đám, nhóm)</div>'
)

# ---------------------------------------------------------------- снача́ла
S["сначала"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">giới từ TỪ, kéo theo cách 2</span></div>'
    '<div class="hd-row"><span class="hd-piece">-нача́л-</span>'
    '<span class="hd-gloss">gốc BẮT ĐẦU (<b>нача́ло</b> sự bắt đầu)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi cách 2 đã đông cứng lại trong từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen là «từ chỗ bắt đầu», nên nó ôm luôn hai '
    'nghĩa ta thấy: «thoạt tiên, trước hết» và «làm lại từ đầu».</div>'
    '<div class="hd-warn">⚠️ Viết LIỀN <b>снача́ла</b> là trạng từ «trước tiên». '
    'Viết RỜI <b>с нача́ла</b> là giới từ + danh từ, phải có cái gì đó đi sau: '
    '<b>с нача́ла го́да</b> từ đầu năm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>нача́ло</b> sự bắt đầu · <b>начина́ть</b> bắt đầu · '
    '<b>нача́льник</b> thủ trưởng, người đứng đầu</div>'
)

# -------------------------------------------------------------------- зима́
S["зима"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">зим-</span>'
    '<span class="hd-gloss">gốc MÙA ĐÔNG, không chẻ nhỏ hơn được</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc rất cổ, cùng nhà Ấn–Âu với <b>hiems</b> (Latin: '
    'mùa đông) — nhánh tiếng Anh của nó là <i>hibernate</i> «ngủ đông». '
    'Muốn nói «vào mùa đông» thì dùng cách 5: <b>зимо́й</b>.</div>'
    '<div class="hd-warn">⚠️ Trọng âm nhảy đúng MỘT ô: cách 4 số ít lùi về gốc '
    '<b>зи́му</b> (<b>всю зи́му</b> suốt mùa đông), còn các cách khác giữ trọng '
    'âm ở đuôi — <b>зимы́</b>, <b>зиме́</b>, <b>зимо́й</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>зи́мний</b> thuộc mùa đông · <b>зимо́й</b> vào mùa '
    'đông · <b>зимо́вка</b> kỳ trú đông</div>'
)

# ------------------------------------------------------------------- весна́
S["весна"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">весн-</span>'
    '<span class="hd-gloss">gốc MÙA XUÂN, không chẻ nhỏ hơn được</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng nhà Ấn–Âu với <b>ver</b> (Latin: mùa xuân), nhánh '
    'tiếng Anh là <i>vernal</i> «thuộc mùa xuân». «Vào mùa xuân» cũng đi cách 5 '
    'như mùa đông: <b>весно́й</b>.</div>'
    '<div class="hd-warn">⚠️ Sang số nhiều gốc đổi hai chỗ cùng lúc: trọng âm '
    'lùi về gốc và <b>е</b> hoá thành <b>ё</b> ⇒ <b>вёсны</b>; riêng cách 2 số '
    'nhiều còn chèn thêm một <b>е</b> cho đọc được ⇒ <b>вёсен</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>весе́нний</b> thuộc mùa xuân · <b>весно́й</b> vào '
    'mùa xuân</div>'
)

# ------------------------------------------------------------------- вчера́
S["вчера"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: <b>вчера́</b> là một khối cứng, mảnh '
    '<b>в-</b> ở đầu không còn là giới từ <b>в</b> nữa.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đừng học lẻ, học theo trục ngày — nó dựng đối xứng '
    'hoàn toàn: <b>позавчера́</b> ← <b>вчера́</b> ← <b>сего́дня</b> → '
    '<b>за́втра</b> → <b>послеза́втра</b>. Cả năm từ đều là trạng từ, không '
    'biến cách.</div>'
    '<div class="hd-warn">⚠️ Muốn biến mốc ngày thành TÍNH TỪ thì thêm '
    '<b>-шний</b>: <b>вчера́шний</b> (của) hôm qua, <b>за́втрашний</b> (của) '
    'ngày mai, <b>сего́дняшний</b> (của) hôm nay. Đó là cách duy nhất nói '
    '«bánh mì hôm qua» — <b>вчера́шний хлеб</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вчера́шний</b> (của) hôm qua · <b>позавчера́</b> '
    'hôm kia</div>'
)

# ------------------------------------------------------------------ за́втра
S["завтра"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">SAU, quá bên kia</span></div>'
    '<div class="hd-row"><span class="hd-piece">-втра</span>'
    '<span class="hd-gloss">dạng cổ của <b>у́тро</b> buổi sáng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen «sau buổi sáng (tới)». Nhớ một lần được hai '
    'từ: đúng cái ghép đó cho <b>за́втрак</b> — bữa ăn sau khi trời sáng.</div>'
    '<div class="hd-warn">⚠️ Trọng âm ở âm đầu: <b>за́втра</b>, và giữ nguyên '
    'chỗ đó khi thêm đuôi — <b>за́втрак</b>, <b>за́втрашний</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>за́втрак</b> bữa sáng · <b>за́втрашний</b> (của) '
    'ngày mai · <b>послеза́втра</b> ngày kia</div>'
)

# ------------------------------------------------------------- послеза́втра
S["послезавтра"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по́сле</span>'
    '<span class="hd-gloss">SAU</span></div>'
    '<div class="hd-row"><span class="hd-piece">-за́втра</span>'
    '<span class="hd-gloss">ngày mai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ghép thẳng hai từ «sau» + «ngày mai», chỉ một thứ đổi: '
    'cả khối dồn về MỘT trọng âm ở <b>послеза́втра</b>. Phía quá khứ dựng y hệt '
    'kiểu chồng tiền tố: <b>по-</b> + <b>за-</b> + <b>вчера́</b> = '
    '<b>позавчера́</b> hôm kia. Cả hai đều là trạng từ, không biến cách.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>за́втра</b> ngày mai · <b>позавчера́</b> hôm kia · '
    '<b>по́сле</b> sau</div>'
)

# ----------------------------------------------------------------- суббо́та
S["суббота"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — đây là từ mượn, vào tiếng Nga qua '
    'tiếng Hy Lạp từ chữ Hebrew <i>shabbat</i> «ngày nghỉ» (cùng nguồn với '
    '<i>Sabbath</i> tiếng Anh).</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vì đi mượn nên nó KHÔNG tự khai vị trí trong tuần '
    'như <b>четве́рг</b> (bốn) hay <b>пя́тница</b> (năm): nghĩa gốc của nó là '
    '«ngày nghỉ», không dính gì tới việc đếm ngày.</div>'
    '<div class="hd-warn">⚠️ Viết HAI chữ <b>б</b>: <b>суббо́та</b> — chỗ sai '
    'chính tả thường gặp nhất của từ này, và trọng âm rơi đúng vào âm tiết có '
    'cặp <b>бб</b> đó.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>суббо́тний</b> (của) thứ Bảy · <b>суббо́тник</b> '
    'buổi lao động tập thể tự nguyện ngày nghỉ</div>'
)

# ----------------------------------------------------------------- пя́тница
S["пятница"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пя́т-</span>'
    '<span class="hd-gloss">gốc NĂM (5), từ <b>пять</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ниц-а</span>'
    '<span class="hd-gloss">đuôi tạo danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tuần Nga mở đầu bằng thứ Hai, nên đếm từ đó ra thì '
    '«thứ Sáu» của ta chính là ngày thứ NĂM của họ. Thấy mảnh <b>пят-</b> là '
    'nghĩ ngay tới <b>пять</b>.</div>'
    '<div class="hd-warn">⚠️ «Vào thứ mấy» thì dùng <b>в</b> + cách 4, không '
    'phải cách 6: <b>в пя́тницу</b>, <b>в суббо́ту</b>, <b>в сре́ду</b>, '
    '<b>в четве́рг</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пять</b> năm (5) · <b>пя́тый</b> thứ năm · '
    '<b>пятна́дцать</b> mười lăm</div>'
)

# ----------------------------------------------------------------- четве́рг
S["четверг"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">четвер-</span>'
    '<span class="hd-gloss">gốc BỐN (4), từ <b>четы́ре</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-г</span>'
    '<span class="hd-gloss">đuôi đã đông cứng, nay không mang nghĩa riêng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đếm từ thứ Hai thì «thứ Năm» của ta là ngày thứ BỐN '
    'của họ. Cùng mảnh <b>четвер-</b> còn có <b>че́тверть</b> (một phần tư) — '
    'nhận ra mảnh này là mở được cả nhóm từ chỉ số bốn.</div>'
    '<div class="hd-warn">⚠️ Cách 1 và cách 4 không có đuôi nên trọng âm nằm '
    'ngay trong thân từ (<b>четве́рг</b>, <b>в четве́рг</b>); mọi dạng còn lại '
    'đẩy trọng âm ra đuôi — <b>четверга́</b>, <b>четвергу́</b>, số nhiều '
    '<b>четверги́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>четы́ре</b> bốn · <b>четвёртый</b> thứ tư · '
    '<b>че́тверть</b> một phần tư</div>'
)

# --------------------------------------------------------------------- год
S["год"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn một âm tiết, không chẻ được. Cái phải học ở '
    'từ này không phải nghĩa mà là cách ĐẾM và một đuôi lệch.</div>'
    '<div class="hd-warn">🔴 Đếm năm phải đổi dạng theo số đứng trước: '
    '<b>оди́н год</b> · <b>два/три/четы́ре го́да</b> · <b>пять…два́дцать лет</b>. '
    'Dạng <b>лет</b> mượn hẳn của <b>ле́то</b> (mùa hè), không phải đuôi của '
    '<b>год</b> — đó là lý do nhìn nó lạ hoắc.</div>'
    '<div class="hd-warn">⚠️ «Trong năm» có đuôi riêng, trọng âm ra cuối: '
    '<b>в году́</b> (<b>в про́шлом году́</b> năm ngoái), chứ không nói '
    '<b>в го́де</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ле́то</b> mùa hè · <b>годово́й</b> (thuộc) cả năm · '
    '<b>годовщи́на</b> ngày kỷ niệm tròn năm</div>'
)

# -------------------------------------------------------------- проше́дшее
S["прошедшее"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">tiền tố QUA, đi hết chiều dài</span></div>'
    '<div class="hd-row"><span class="hd-piece">-шед-</span>'
    '<span class="hd-gloss">gốc ĐI ở nhánh quá khứ của <b>идти́</b> (<b>шёл</b> đã đi)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-шее</span>'
    '<span class="hd-gloss">đuôi phân từ, dạng giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen «cái đã đi qua». Vì thân nó là PHÂN TỪ chứ '
    'không phải danh từ thật, nó biến cách theo mẫu TÍNH TỪ giống trung — '
    '<b>проше́дшего</b>, <b>проше́дшему</b>, <b>проше́дшим</b> — và không có số '
    'nhiều. Một câu đó đủ giải thích cả bảng chia.</div>'
    '<div class="hd-warn">⚠️ Đời thường người Nga nói «quá khứ» là '
    '<b>про́шлое</b>; <b>проше́дшее</b> hay gặp nhất trong thuật ngữ ngữ pháp '
    '<b>проше́дшее вре́мя</b> = thì quá khứ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пройти́</b> đi qua · <b>про́шлый</b> vừa qua '
    '(<b>в про́шлом году́</b> năm ngoái) · <b>про́шлое</b> quá khứ</div>'
)

# -------------------------------------------------------------------- уже́
S["уже"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: hư từ một khối, không có mảnh nào mang '
    'nghĩa riêng.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhớ nó bằng cặp đối: <b>уже́</b> đánh dấu việc ĐÃ xảy '
    'ra rồi, phía ngược lại là <b>ещё не</b> «vẫn chưa». Ghép với <b>не</b> thì '
    'nó đổi vai thành «không còn… nữa»: <b>уже́ не рабо́тает</b> không làm việc '
    'nữa.</div>'
    '<div class="hd-warn">🔴 Đồng tự — chỉ trọng âm phân biệt: <b>уже́</b> '
    '(trọng âm cuối) là «đã, rồi»; <b>у́же</b> (trọng âm đầu) là «hẹp hơn», dạng '
    'so sánh hơn của <b>у́зкий</b>. Cả hai từ đều có trong bộ thẻ này.</div>'
)

# ----------------------------------------------------------------- ра́ньше
S["раньше"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ра́н-</span>'
    '<span class="hd-gloss">gốc SỚM (<b>ра́нний</b> sớm)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ьше</span>'
    '<span class="hd-gloss">đuôi SO SÁNH HƠN</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nó là dạng so sánh hơn của <b>ра́нний</b> / '
    '<b>ра́но</b>, nên gánh hai việc: «sớm hơn» khi đem ra so, và «trước đây, '
    'hồi trước» khi chỉ một quãng đã qua. Phía đối xứng là <b>по́зже</b> muộn '
    'hơn.</div>'
    '<div class="hd-warn">⚠️ Cái đem ra so đứng ở CÁCH 2, không cần <b>чем</b>: '
    '<b>Он пришёл ра́ньше меня́</b> (Anh ấy đến sớm hơn tôi) — cùng khuôn với '
    '<b>по́зже меня́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ра́нний</b> sớm · <b>ра́но</b> sớm (trạng từ) · '
    '<b>зара́нее</b> trước, từ sớm</div>'
)

# ------------------------------------------------------------ воскресе́нье
S["воскресенье"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вос-</span>'
    '<span class="hd-gloss">tiền tố LÊN, TRỞ LẠI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-крес-</span>'
    '<span class="hd-gloss">gốc SỐNG LẠI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-енье</span>'
    '<span class="hd-gloss">đuôi danh từ, cho biết đây là giống TRUNG</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen «sự sống lại» — chủ nhật là ngày Chúa phục '
    'sinh, nên ngày này cũng không mang số như <b>четве́рг</b> hay '
    '<b>пя́тница</b>. Số nhiều cách 2 rụng <b>-ье</b> thành <b>-ий</b>: '
    '<b>воскресе́ний</b>.</div>'
    '<div class="hd-warn">🔴 Hai từ chỉ khác nhau một chữ và cả hai đều có '
    'trong bộ thẻ: <b>воскресе́нье</b> là chủ nhật, <b>воскресе́ние</b> là sự '
    'phục sinh.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>воскресе́ние</b> sự phục sinh · <b>воскре́снуть</b> '
    'sống lại · <b>воскре́сный</b> (của) chủ nhật</div>'
)

# --------------------------------------------------------------------- раз
S["раз"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn một âm tiết, không chẻ được. Thứ phải học ở '
    'từ này không phải nghĩa mà là cách ĐẾM và một ô bảng chia rỗng đuôi.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa dùng nhiều nhất là đơn vị đếm LẦN, và nó đếm '
    'đúng cái khuôn ba dạng của <b>год</b>: <b>оди́н раз</b> một lần · '
    '<b>два ра́за</b> hai lần · <b>пять раз</b> năm lần.</div>'
    '<div class="hd-warn">🔴 Số nhiều cách 2 KHÔNG có đuôi, trùng khít dạng '
    'gốc: <b>мно́го раз</b> nhiều lần. Hai cụm phải thuộc: <b>как раз</b> (vừa '
    'đúng, vừa vặn) và <b>ни ра́зу</b> (chưa một lần nào).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ра́зный</b> khác nhau · <b>однора́зовый</b> dùng một '
    'lần rồi bỏ</div>'
)

# --------------------------------------------------------------------- май
S["май"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — mượn thẳng từ Latin <i>Maius</i>, y '
    'như cả 12 tên tháng của tiếng Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vì đều đi mượn cùng một nguồn nên tên tháng Nga nghe '
    'gần tiếng Anh (<b>май</b> May, <b>апре́ль</b> April, <b>ию́нь</b> June) và '
    'cả 12 tháng đều là giống ĐỰC.</div>'
    '<div class="hd-warn">⚠️ «Vào tháng Năm» đi <b>в</b> + cách 6, khác hẳn tên '
    'ngày trong tuần (cách 4): <b>в ма́е</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ма́йский</b> thuộc tháng Năm · <b>Первома́й</b> '
    'ngày 1 tháng Năm</div>'
)

# ---------------------------------------------------------------- ма́йский
S["майский"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ма́й-</span>'
    '<span class="hd-gloss">tháng Năm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ск-ий</span>'
    '<span class="hd-gloss">đuôi tính từ QUAN HỆ: «thuộc về, dính tới»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng khuôn với <b>ру́сский</b>: <b>-ский</b> chỉ nói '
    'thứ này THUỘC VỀ cái gì, không nói nhiều hay ít. Vì thế nó không có dạng '
    'ngắn và không có so sánh hơn — không thể «tháng Năm hơn».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>май</b> tháng Năm</div>'
)

# ---------------------------------------------------------------- по́здний
S["поздний"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по́зд-</span>'
    '<span class="hd-gloss">gốc MUỘN, TRỄ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ий</span>'
    '<span class="hd-gloss">đuôi tính từ (biến thể mềm)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một gốc <b>позд-</b> đỡ cả bộ: tính từ '
    '<b>по́здний</b>, trạng từ <b>по́здно</b>, so sánh hơn <b>по́зже</b>. Cả bộ '
    'này đối xứng đúng với <b>ра́нний / ра́но / ра́ньше</b> ở phía «sớm».</div>'
    '<div class="hd-warn">⚠️ Có HAI dạng so sánh hơn cùng đúng: <b>по́зже</b> '
    'dùng hằng ngày, <b>поздне́е</b> trang trọng hơn. Riêng dạng ngắn thì từ này '
    'không có.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>по́здно</b> muộn (trạng từ) · <b>по́зже</b> muộn '
    'hơn · <b>опозда́ть</b> đến muộn, lỡ</div>'
)

# ------------------------------------------------ VIỆC 2: field Vietnamese
# когда: bỏ "trong khi" — đó là chỗ nó đè lên пока (cũng PoS=oth, không badge
# nào tách được). "khi" đã phủ hết nghĩa when/while/as của когда.
V["когда"] = "khi nào, khi, lúc"
# раньше: đang thiếu hẳn nghĩa so sánh "earlier" mà gloss tiếng Anh có.
V["раньше"] = "trước đây, hồi trước, sớm hơn"
# майский: vế "mang không khí của tháng Năm" là ghi chú sắc thái, không phải
# một nghĩa — §2c cấm.
V["майский"] = "thuộc về tháng Năm"
