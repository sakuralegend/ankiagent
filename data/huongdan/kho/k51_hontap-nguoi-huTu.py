# -*- coding: utf-8 -*-
"""k51 — hontap-nguoi-huTu: bộ tên dân tộc/ngôn ngữ (-анин · -ский · по-…-и)
đứng cạnh nhóm hư từ và trạng từ hay dùng nhất.

Không dựng biến khối dùng chung — mỗi thẻ chỉ nói về chính từ của nó (README §3).
"""

S = {}

# ------------------------------------------------------------------ dân tộc
S["англичанин"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">англич-</span>'
    '<span class="hd-gloss">gốc А́нглия — nước Anh</span></div>'
    '<div class="hd-row"><span class="hd-piece">-анин</span>'
    '<span class="hd-gloss">hậu tố "người thuộc xứ…", chỉ nam giới</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">-анин là khuôn dựng tên cư dân theo xứ sở: '
    '<b>россия́нин</b>, <b>граждани́н</b>, <b>южа́нин</b>. Muốn nói phụ nữ thì '
    'thay bằng -анка: <b>англича́нка</b>.</div>'
    '<div class="hd-warn">⚠️ Số nhiều rụng hẳn -ин: <b>англича́не</b>; '
    'còn cách 2 số nhiều lại KHÔNG có đuôi — <b>пять англича́н</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>англи́йский</b> thuộc về Anh · '
    '<b>англича́нка</b> phụ nữ Anh · <b>по-англи́йски</b> bằng tiếng Anh</div>'
)

S["английский"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">А́нгли-</span>'
    '<span class="hd-gloss">gốc tên nước</span></div>'
    '<div class="hd-row"><span class="hd-piece">-йск-</span>'
    '<span class="hd-gloss">hậu tố dựng tính từ từ tên riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span>'
    '<span class="hd-gloss">đuôi tính từ giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tên nước + -ский = "thuộc về nước đó". Trọng âm rời gốc, '
    'nhảy về ngay trước hậu tố: А́нглия → англи́йский.</div>'
    '<div class="hd-warn">⚠️ Có danh từ theo sau thì dùng tính từ này '
    '(<b>англи́йский язы́к</b>); không có danh từ thì phải đổi sang trạng từ — '
    '<b>говорю́ по-англи́йски</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>англича́нин</b> người Anh · <b>англича́нка</b> phụ nữ Anh · '
    '<b>по-англи́йски</b> bằng tiếng Anh</div>'
)

S["немецкий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">нем-</span>'
    '<span class="hd-gloss">gốc "câm, không nói được"</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ец</span>'
    '<span class="hd-gloss">hậu tố người → не́мец</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-ий</span>'
    '<span class="hd-gloss">hậu tố tính từ -ск- co lại sau ц</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ghép <b>не́мец</b> với -ск-: chữ -е- của -ец rụng, ц nuốt luôn '
    'chữ с của hậu tố (ц + ск → цк), và trọng âm dịch một nấc sang phải — неме́цкий.</div>'
    '<div class="hd-warn">⚠️ Mức tin: nối неме́цкий với <b>немо́й</b> "câm" là TỪ NGUYÊN '
    '(người Slav xưa gọi kẻ không nói được tiếng mình như vậy), không phải luật suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>не́мец</b> người Đức · <b>не́мка</b> phụ nữ Đức · '
    '<b>по-неме́цки</b> bằng tiếng Đức</div>'
)

S["русский"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рус-</span>'
    '<span class="hd-gloss">gốc Русь — nước Rus cổ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ск-ий</span>'
    '<span class="hd-gloss">hậu tố + đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hai chữ с liền nhau là chỗ рус- gặp -ск-; tách được thành '
    'рус|ский thì không bao giờ viết thiếu một с.</div>'
    '<div class="hd-warn">⚠️ Tiếng Nga KHÔNG có từ riêng cho "người Nga": chính từ này '
    'làm luôn danh từ (<b>ру́сский</b> / <b>ру́сская</b>) — khác англича́нин, не́мец, '
    'францу́з vốn là danh từ riêng biệt.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>Русь</b> nước Rus cổ · <b>ру́сская</b> phụ nữ Nga · '
    '<b>по-ру́сски</b> bằng tiếng Nga</div>'
)

S["французский"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">францу́з-</span>'
    '<span class="hd-gloss">gốc = từ chỉ NGƯỜI Pháp</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ск-ий</span>'
    '<span class="hd-gloss">hậu tố + đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tính từ này mọc ra từ tên NGƯỜI (<b>францу́з</b>) chứ không '
    'thẳng từ tên nước Фра́нция — vì thế giữa từ mới có -уз-, và trọng âm đứng yên ở '
    '-у́- suốt cả họ.</div>'
    '<div class="hd-warn">⚠️ Viết đủ ba phụ âm -зск-: <b>францу́зский</b>. Đây là chỗ '
    'chữ з hay bị rơi mất.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>францу́з</b> người Pháp · <b>францу́женка</b> phụ nữ Pháp · '
    '<b>по-францу́зски</b> bằng tiếng Pháp</div>'
)

S["по-русски"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">"theo kiểu…", luôn có gạch nối</span></div>'
    '<div class="hd-row"><span class="hd-piece">ру́сск-</span>'
    '<span class="hd-gloss">gốc tính từ ру́сский</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и</span>'
    '<span class="hd-gloss">đuôi trạng từ — KHÔNG có й</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Khuôn по- + gốc tính từ dân tộc + -и dựng ra TRẠNG TỪ '
    '"bằng tiếng…/theo kiểu…": <b>по-англи́йски</b>, <b>по-неме́цки</b>, '
    '<b>по-францу́зски</b>.</div>'
    '<div class="hd-warn">⚠️ Chọn theo chỗ đứng: trước danh từ thì dùng tính từ '
    '(<b>ру́сский язы́к</b>), sau động từ nói/đọc/viết thì dùng dạng này — '
    '<b>говорю́ по-ру́сски</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ру́сский</b> thuộc về Nga · <b>по-англи́йски</b> bằng tiếng Anh · '
    '<b>по-неме́цки</b> bằng tiếng Đức</div>'
)

S["по-французски"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">"theo kiểu…"</span></div>'
    '<div class="hd-row"><span class="hd-piece">францу́зск-</span>'
    '<span class="hd-gloss">gốc tính từ францу́зский</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и</span>'
    '<span class="hd-gloss">đuôi trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng một khuôn với <b>по-ру́сски</b>. Điều duy nhất phải canh: '
    'đuôi trạng từ là -и trần, đừng kéo theo -ий của tính từ.</div>'
    '<div class="hd-warn">⚠️ <b>Она́ говори́т по-францу́зски</b> (sau động từ) ≠ '
    '<b>францу́зский язы́к</b> (trước danh từ).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>францу́зский</b> thuộc về Pháp · <b>францу́з</b> người Pháp · '
    '<b>по-ру́сски</b> bằng tiếng Nga</div>'
)

# ------------------------------------------------------- lớp học · ngữ pháp
S["грамматика"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">граммат-</span>'
    '<span class="hd-gloss">Hy Lạp gramma "chữ viết"</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ик-а</span>'
    '<span class="hd-gloss">hậu tố tên NGÀNH, luôn giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">-ика là khuôn tên ngành học, và trọng âm luôn rơi vào âm tiết '
    'ngay TRƯỚC nó: фи́зика, матема́тика, поли́тика — nên grammat + ика ra грамма́тика.</div>'
    '<div class="hd-warn">⚠️ Viết ĐÔI м (đúng như English grammar). Một м là sai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гра́мотный</b> biết chữ, thạo · <b>гра́мота</b> văn tự, chứng chỉ · '
    '<b>програ́мма</b> chương trình · <b>телегра́мма</b> điện tín</div>'
)

S["спряжение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">"cùng, gộp lại"</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пряж-</span>'
    '<span class="hd-gloss">gốc "buộc vào ách" (г → ж)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">hậu tố danh từ hành động, giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: "sự buộc chung vào một ách" — mọi dạng của một động từ '
    'bị buộc chung theo ngôi. Đuôi -ение cho biết ngay đây là danh từ giống trung.</div>'
    '<div class="hd-warn">⚠️ Cặp thuật ngữ luôn đi liền: <b>спряже́ние</b> là chia ĐỘNG TỪ '
    'theo ngôi, còn <b>склоне́ние</b> là biến cách DANH TỪ / tính từ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>супру́г</b> chồng (nghĩa đen "kẻ chung một ách") · '
    '<b>супру́га</b> vợ · <b>напряже́ние</b> sự căng thẳng, điện áp</div>'
)

S["спортивный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">спорт</span>'
    '<span class="hd-gloss">mượn thẳng English sport</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ив-</span>'
    '<span class="hd-gloss">hậu tố tính từ của lớp từ quốc tế</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ Nga</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi -и́вный gắn vào gốc mượn để ra nghĩa "có tính…": '
    '<b>акти́вный</b>, <b>масси́вный</b>, <b>эффекти́вный</b>. Nhận ra đuôi này là đoán '
    'được nghĩa cả những từ chưa gặp.</div>'
    '<div class="hd-warn">⚠️ Dạng ngắn giống đực chèn thêm -е- vào giữa cụm -вн- cho dễ '
    'đọc: <b>спорти́вен</b>; ba dạng còn lại đều đặn (<b>спорти́вна</b>, <b>спорти́вно</b>, '
    '<b>спорти́вны</b>), trọng âm không nhúc nhích.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>спорт</b> thể thao · <b>спортсме́н</b> vận động viên · '
    '<b>спортза́л</b> phòng tập</div>'
)

# --------------------------------------------------------------- trạng từ
S["близко"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">близ-</span>'
    '<span class="hd-gloss">gốc "gần"</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-</span>'
    '<span class="hd-gloss">phần thân của tính từ бли́зкий</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tính từ <b>бли́зкий</b> bỏ -ий thay bằng -о là thành trạng từ. '
    'Nó trả lời "ở đâu / thế nào" nên không bao giờ đứng trước danh từ.</div>'
    '<div class="hd-warn">⚠️ Nó đòi giới từ chứ không dùng trần: <b>бли́зко к до́му</b> '
    '(к + cách 3) hoặc <b>бли́зко от до́ма</b> (от + cách 2). Nghĩa bóng: '
    '<b>приня́ть бли́зко к се́рдцу</b> = để bụng, ghim vào lòng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бли́зкий</b> gần, thân thiết · <b>ближа́йший</b> gần nhất · '
    '<b>приближа́ться</b> tiến lại gần</div>'
)

S["отлично"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">"tách ra khỏi"</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лич-</span>'
    '<span class="hd-gloss">gốc "mặt, diện mạo" (như лицо́)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-о</span>'
    '<span class="hd-gloss">đuôi trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đi từ nghĩa đen "tách hẳn mặt mình ra khỏi số còn lại": '
    '<b>отлича́ться</b> khác biệt → <b>отли́чный</b> nổi trội hẳn → отли́чно.</div>'
    '<div class="hd-warn">⚠️ Thang điểm Nga chấm bằng đúng từ này: 5 = <b>отли́чно</b>. '
    'Trong hội thoại, отли́чно! là "tuyệt!".</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отлича́ться</b> khác biệt · <b>отли́чный</b> xuất sắc · '
    '<b>разли́чие</b> sự khác nhau · <b>лицо́</b> khuôn mặt</div>'
)

S["правильно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">прав-</span>'
    '<span class="hd-gloss">gốc "thẳng, phải, đúng"</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ил-</span>'
    '<span class="hd-gloss">lấy từ пра́вило "quy tắc"</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ьн-о</span>'
    '<span class="hd-gloss">đuôi trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen là "theo đúng <b>пра́вило</b> (quy tắc)" — nên nó nói về '
    'cách LÀM đúng, không phải sự thật đúng. Gốc прав- mở khoá cả cụm: <b>пра́вда</b> '
    'sự thật, <b>пра́вый</b> bên phải, <b>прави́тельство</b> chính phủ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пра́вило</b> quy tắc · <b>пра́вильный</b> đúng đắn · '
    '<b>исправля́ть</b> sửa cho đúng · <b>пра́вда</b> sự thật</div>'
)

S["часто"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">част-</span>'
    '<span class="hd-gloss">gốc "dày, khít, sít nhau"</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tính từ <b>ча́стый</b> vốn nói về khoảng cách: "dày, khít" '
    '(<b>ча́стый гре́бень</b> lược răng dày). Đem sang thời gian thì thành "các lần xảy ra '
    'khít nhau" = thường xuyên. Ngược lại là <b>ре́дко</b> (thưa → hiếm khi).</div>'
    '<div class="hd-warn">⚠️ ча́сто KHÔNG cùng gốc với <b>час</b> (giờ) — chỉ trùng mặt chữ. '
    'Đừng suy ra "часто = tính theo giờ".</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ча́стый</b> dày, hay xảy ra · <b>ча́ще</b> thường hơn · '
    '<b>частота́</b> tần số</div>'
)

# ------------------------------------------------------------------- hư từ
S["за"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: за là giới từ gốc, một âm tiết, không có mảnh nào '
    'mang nghĩa riêng.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một mặt chữ nhưng hai cách, và thứ quyết định là ĐỘNG hay TĨNH: '
    'đi RA phía sau → cách 4 (<b>сесть за стол</b>), đã Ở phía sau → cách 5 '
    '(<b>сиде́ть за столо́м</b>). Nghĩa "vì, đổi lấy" cũng là cách 4: '
    '<b>спаси́бо за по́мощь</b>.</div>'
    '<div class="hd-warn">⚠️ <b>не́ за что</b> = "không có gì đâu", câu đáp lại спаси́бо — '
    'trọng âm nhảy lên не́.</div>'
    '<div class="hd-warn">⚠️ Chỉ thời gian, за + cách 4 là "TRONG VÒNG, làm xong trong": '
    '<b>за два дня</b> = xong trong hai ngày, khác hẳn <b>че́рез два дня</b> = hai ngày nữa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>за́втра</b> ngày mai (за + у́тра "sau buổi sáng") · '
    '<b>за́пад</b> phía tây (nơi mặt trời ngã xuống)</div>'
)

S["или"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">и-</span>'
    '<span class="hd-gloss">"và"</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ли</span>'
    '<span class="hd-gloss">tiểu từ nghi vấn "liệu có chăng"</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ghép lại đúng là "và liệu…?" — tức nêu thêm một khả năng. Muốn nhấn '
    'thì lặp cả hai vế: <b>и́ли ко́фе, и́ли чай</b>.</div>'
    '<div class="hd-warn">⚠️ и́ли nối LỰA CHỌN trong câu kể. Còn câu hỏi "có… không" thì dùng '
    'tiểu từ <b>ли</b> đặt sau từ được hỏi: <b>Зна́ешь ли ты?</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ли́бо</b> hoặc (giọng văn viết, ли́бо… ли́бо…) · '
    '<b>неуже́ли</b> chẳng lẽ</div>'
)

S["про"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: про là giới từ gốc, một âm tiết.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">про + cách 4 = "về, nói về", đúng nghĩa của о/об nhưng про là giọng '
    'nói chuyện hằng ngày: <b>расска́зывать про шко́лу</b>. Viết lách hay nói trang trọng thì '
    'quay lại dùng о.</div>'
    '<div class="hd-warn">⚠️ <b>про себя́</b> = "thầm trong bụng": <b>чита́ть про себя́</b> '
    'là đọc thầm, không phải đọc về mình.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">про- làm tiền tố "xuyên suốt / cho hết": <b>прочита́ть</b> đọc xong · '
    '<b>пройти́</b> đi qua · <b>про́тив</b> chống lại (ở phía đối diện)</div>'
)

S["себя"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">себ-</span>'
    '<span class="hd-gloss">thân đại từ phản thân</span></div>'
    '<div class="hd-row"><span class="hd-piece">-я</span>'
    '<span class="hd-gloss">đuôi cách 2 / cách 4</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nó luôn trỏ ngược về chủ ngữ của chính câu đó, nên dùng chung cho '
    'mọi ngôi, mọi giống, mọi số — "tôi tự…", "nó tự…" đều là себя́. Đuôi <b>-ся</b> của '
    '<b>учи́ться</b>, <b>мы́ться</b> chính là себя́ co lại.</div>'
    '<div class="hd-warn">⚠️ KHÔNG có cách 1 — себя́ không bao giờ làm chủ ngữ. Cả bảng chỉ '
    'có себя́ / себе́ / собо́й.</div>'
    '<div class="hd-warn">⚠️ Đọc được biển ở Nga: <b>К СЕБЕ́</b> = kéo, <b>ОТ СЕБЯ́</b> = đẩy.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>со́бственный</b> của riêng mình · <b>осо́бенный</b> đặc biệt '
    '(ở riêng ra)</div>'
)

S["только"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">то-</span>'
    '<span class="hd-gloss">như тот / то "cái đó"</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лько</span>'
    '<span class="hd-gloss">khuôn chỉ lượng, như ско́лько</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng khuôn với <b>ско́лько</b> bao nhiêu và <b>сто́лько</b> chừng ấy, '
    'nên то́лько là "chỉ chừng đó, không hơn". Nghĩa thứ hai nằm ở thời gian: '
    '<b>Он то́лько пришёл</b> = anh ấy vừa mới đến.</div>'
    '<div class="hd-warn">⚠️ Hai cụm phải thuộc: <b>то́лько что</b> = vừa mới xong · '
    '<b>как то́лько</b> = ngay khi (mở mệnh đề thời gian).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ско́лько</b> bao nhiêu · <b>сто́лько</b> chừng ấy · '
    '<b>не́сколько</b> một vài</div>'
)

S["час"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: час- là gốc trơn, nghĩa "giờ, thời khắc".</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Số nhiều đổi hẳn nghĩa: <b>часы́</b> không phải "nhiều giờ" mà là '
    'CÁI ĐỒNG HỒ, và nghĩa đó chỉ tồn tại ở số nhiều. Hỏi giờ: <b>Кото́рый час?</b></div>'
    '<div class="hd-warn">⚠️ Trọng âm chạy ra đuôi khi đứng sau số đếm và sau в: '
    '<b>два часа́</b>, <b>в пе́рвом часу́</b>; còn cách 2 thường thì giữ ở gốc — '
    '<b>о́коло ча́са</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>часы́</b> đồng hồ · <b>сейча́с</b> bây giờ (сей + час "chính giờ này") · '
    '<b>полчаса́</b> nửa tiếng</div>'
)

# ---------------------------------------------------------------------------
# V — sửa field Vietnamese (đề bài của deck 1-go): phải chỉ có MỘT đáp án đúng.
# Không ghi từ loại/giống (mặt thẻ đã có badge), TRỪ từ có PoS = oth.
V = {
    'английский': 'thuộc về nước Anh, kiểu Anh',
    'немецкий': 'thuộc về nước Đức, kiểu Đức',
    'французский': 'thuộc về nước Pháp, kiểu Pháp',
    'русский': 'thuộc về nước Nga, người Nga, tiếng Nga',
    'по-русски': 'bằng tiếng Nga, theo kiểu Nga',
    'по-французски': 'bằng tiếng Pháp, theo kiểu Pháp',
    'за': 'đằng sau, phía sau, vì, đổi lấy, trong vòng',
    'или': 'hoặc, hay là',
    'про': 'về, nói về, dành cho',
    'только': 'chỉ, mỗi, vừa mới',
    'спортивный': 'thuộc về thể thao, kiểu thể thao',
    'спряжение': 'sự chia động từ theo ngôi',
    'близко': 'gần, ở gần',
    'отлично': 'xuất sắc, tuyệt vời, điểm 5',
    'правильно': 'đúng, chính xác',
    'себя': 'bản thân, chính mình',
    'час': 'giờ, một tiếng đồng hồ',
    'часто': 'thường xuyên, hay xảy ra',
}
