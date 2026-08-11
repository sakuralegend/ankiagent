# -*- coding: utf-8 -*-
"""k73 — tu-moi-giaitri: 19 từ giải trí / văn hoá / thể thao, KHÔNG cùng một họ.

Cố ý không có khối hệ thống dùng chung: mỗi thẻ chỉ nói phần của chính từ đó.
Ba chỗ giao nhau nằm trọn trong lô nên được xử lý cả hai phía:
увлека́ться ↔ увле́чься (cặp thể, cùng gốc влек-/влеч- — mỗi thẻ nói rõ mình khác
bạn ở đâu), интересова́ться (cùng đòi cách 5 nhưng KHÁC GỐC hẳn — nói ở cả hai
thẻ đúng một câu), волейбо́л ↔ хокке́й ↔ матч (nhóm tên môn thể thao mượn: cách
nói «chơi môn này» trải đủ ở ĐÚNG thẻ волейбо́л, thẻ хокке́й chỉ dẫn chiếu một dòng).
"""

# 🔴 KHÔNG dựng biến khối dùng chung (HE/LUAT/THE…) rồi cộng vào mọi thẻ.

S = {}
V = {}

# ----------------------------------------------------------------- бале́т
S["балет"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mượn nguyên khối từ tiếng Pháp <i>ballet</i>, trong tiếng '
    'Nga không chẻ ra mảnh nào — đừng cố tìm tiền tố. Nhưng cái gốc Ý <i>ballo</i> '
    '(nhảy múa) thì vẫn nhìn thấy được: nó nằm luôn trong <b>бал</b> (dạ hội khiêu '
    'vũ) và <b>балери́на</b>. Giống đực, trọng âm ở đuôi và đứng yên cả bảng: '
    '<b>бале́та</b>, <b>бале́ты</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бал</b> dạ hội khiêu vũ · <b>балери́на</b> nữ diễn viên '
    'ba lê · <b>балетме́йстер</b> biên đạo múa</div>'
)

# -------------------------------------------------------------- бараба́н
S["барабан"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бараба́н</span>'
    '<span class="hd-gloss">một khối liền — không chẻ nhỏ được</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ này được coi là mượn từ các thứ tiếng Turkic, mô phỏng '
    'tiếng gõ; trong tiếng Nga nó không còn mảnh nào mang nghĩa riêng. Cái đáng học '
    'là hậu tố dựng thêm phía sau: <b>бараба́нщик</b> = trống + <i>-щик</i> (người '
    'làm nghề đó), cùng khuôn với <b>перево́дчик</b> người phiên dịch. Giống đực, '
    'trọng âm ở đuôi và đứng yên: <b>бараба́на</b>, <b>бараба́ны</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бараба́нщик</b> người đánh trống · <b>бараба́нить</b> '
    'đánh trống, gõ liên hồi</div>'
)
V["барабан"] = "cái trống"

# ------------------------------------------------------------ волейбо́л
S["волейбол"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">волей-</span>'
    '<span class="hd-gloss">volley — cú đánh khi bóng còn đang bay</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бо́л</span>'
    '<span class="hd-gloss">ball — quả bóng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mượn nguyên khối tiếng Anh <i>volleyball</i>: bóng đánh '
    'trên không, không cho chạm đất. Cùng khuôn <i>-бо́л</i> với <b>футбо́л</b> và '
    '<b>баскетбо́л</b> — gặp đuôi này là biết đang gọi tên một môn bóng. Là tên một '
    'môn nên chỉ dùng số ít.</div>'
    '<div class="hd-warn">⚠️ «Chơi môn thể thao» là <b>игра́ть в</b> + cách 4: '
    '<b>игра́ть в волейбо́л</b>, <b>в футбо́л</b>, <b>в хокке́й</b>. Tên môn giữ '
    'nguyên hình vì đây là danh từ bất động vật.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>футбо́л</b> bóng đá · <b>баскетбо́л</b> bóng rổ · '
    '<b>волейболи́ст</b> vận động viên bóng chuyền</div>'
)

# --------------------------------------------------------- гимна́стика
S["гимнастика"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">гимнаст-</span>'
    '<span class="hd-gloss">Hy Lạp <i>gymnastes</i> — người tập luyện</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ика</span>'
    '<span class="hd-gloss">tên một NGÀNH, một bộ môn</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi <i>-ика</i> là cái đã gặp ở <b>фи́зика</b>, '
    '<b>поли́тика</b>, <b>грамма́тика</b>: nó gọi tên bộ môn, còn người làm bộ môn '
    'đó thì mang đuôi khác — <b>гимна́ст</b>. Giống cái, trọng âm nằm ở '
    '<i>-на́-</i> và đứng yên cả bảng.</div>'
    '<div class="hd-warn">⚠️ KHÔNG cùng gốc với <b>гимн</b> (quốc ca). '
    '<b>гимн</b> là Hy Lạp <i>hymnos</i> — bài ca; <b>гимна́стика</b> là '
    '<i>gymnos</i> — trần mình mà tập. Trùng mặt chữ thôi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гимна́ст</b> vận động viên thể dục · '
    '<b>гимна́стка</b> nữ vận động viên thể dục</div>'
)

# --------------------------------------------------- интересова́ться
S["интересоваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">интере́с-</span>'
    '<span class="hd-gloss">mối quan tâm — chính từ <b>интере́с</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-ть</span>'
    '<span class="hd-gloss">biến danh từ thành động từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">phản thân — hướng việc vào chính mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dựng thẳng từ <b>интере́с</b>: «tự đặt mối quan tâm của '
    'mình vào cái gì». Đuôi <i>-овать</i> khi chia thì co lại thành <i>-у-</i>: '
    '<b>интересу́юсь</b>, <b>интересу́ешься</b>. Cái đi kèm phải để cách 5: '
    '<b>интересова́ться му́зыкой</b>.</div>'
    '<div class="hd-warn">⚠️ Cùng đòi cách 5 với <b>увлека́ться</b> nhưng KHÁC GỐC '
    'hẳn và nhẹ hơn: từ này là để tâm tìm hiểu, còn <b>увлека́ться</b> là mê đắm, '
    'dồn cả thời gian vào.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>интере́с</b> sự quan tâm · <b>интере́сный</b> thú vị · '
    '<b>интере́сно</b> một cách thú vị · <b>неинтере́сный</b> không thú vị</div>'
)

# ------------------------------------------------------ класси́ческий
S["классический"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">класс-</span>'
    '<span class="hd-gloss">hạng, lớp — chính từ <b>класс</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ческ-</span>'
    '<span class="hd-gloss">khuôn biến từ quốc tế thành tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span>'
    '<span class="hd-gloss">đuôi tính từ giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc Latin của <b>класс</b> là «hạng», nên '
    '<b>класси́ческий</b> = thuộc hạng mẫu mực, đã được thời gian xếp hạng → cổ '
    'điển. Thêm <i>-ический</i> thì trọng âm bị kéo về đúng âm ngay trước nó: '
    '<b>класс → класси́ческий</b>. Là tính từ quan hệ nên nó không có dạng ngắn, '
    'chỉ dùng nguyên hình đứng trước danh từ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>класс</b> lớp học, hạng · <b>кла́ссика</b> dòng cổ điển '
    '· <b>кла́ссик</b> tác giả kinh điển</div>'
)

# --------------------------------------------------------------- кома́нда
S["команда"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кома́нд-</span>'
    '<span class="hd-gloss">mệnh lệnh (Latin <i>com-</i> cùng + <i>mandare</i> '
    'giao phó)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hai nghĩa của từ này nối với nhau bằng một sợi dây, nhớ '
    'sợi dây thì khỏi nhớ hai thứ: <b>mệnh lệnh</b> → nhóm người cùng nhận một '
    'mệnh lệnh → <b>đội, ê-kíp</b>. Vì thế cùng một từ vừa là lệnh gõ cho máy tính '
    'vừa là đội bóng. Trọng âm ở <i>-ма́н-</i> và đứng yên cả bảng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>команди́р</b> người chỉ huy · <b>кома́ндовать</b> chỉ '
    'huy, ra lệnh · <b>командиро́вка</b> chuyến đi công tác</div>'
)
V["команда"] = "đội, ê-kíp, đội ngũ, mệnh lệnh, khẩu lệnh"

# ---------------------------------------------------------- компози́тор
S["композитор"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ком-</span>'
    '<span class="hd-gloss">Latin <i>com-</i> — cùng nhau, lại với nhau</span></div>'
    '<div class="hd-row"><span class="hd-piece">-позит-</span>'
    '<span class="hd-gloss">đặt, để (Latin <i>positum</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ор</span>'
    '<span class="hd-gloss">người làm nghề đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: «người ĐẶT các phần LẠI VỚI NHAU» — đúng chữ '
    '<i>compose</i> của tiếng Anh, ở đây là đặt các nốt nhạc lại thành bản nhạc. '
    'Đuôi <i>-ор</i> gọi tên người làm nghề, đã gặp ở <b>дире́ктор</b>, '
    '<b>профе́ссор</b>. Trọng âm ở <i>-зи́-</i> và đứng yên cả bảng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>компози́ция</b> bố cục, tác phẩm · <b>пози́ция</b> vị '
    'trí, tư thế</div>'
)

# --------------------------------------------------------- литерату́ра
S["литература"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">литер-</span>'
    '<span class="hd-gloss">chữ cái (Latin <i>littera</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-атур-</span>'
    '<span class="hd-gloss">khuôn danh từ trừu tượng mượn từ Latin</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen là «cái được viết ra bằng chữ cái» — cùng ổ với '
    'tiếng Anh <i>letter</i>, <i>literature</i>, nên mặt chữ đọc là đoán được nghĩa. '
    'Trọng âm ở <i>-ту́-</i>; đổi sang tên người thì nó nhảy chỗ: '
    '<b>литерату́ра → литера́тор</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>литерату́рный</b> thuộc về văn học · '
    '<b>литера́тор</b> người viết văn</div>'
)

# ------------------------------------------------------------------ матч
S["матч"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mượn thẳng tiếng Anh <i>match</i>, một khối, không chẻ ra '
    'mảnh nào. Thứ đáng học ở đây là GIỐNG: danh từ kết thúc bằng <i>ч</i> mà '
    'KHÔNG có <i>ь</i> đằng sau thì là giống đực — <b>матч</b>, <b>мяч</b>, '
    '<b>врач</b>. Trọng âm bám gốc và đứng yên khi biến cách: <b>ма́тча</b>, '
    '<b>ма́тчи</b>. Đừng dùng thay <b>игра́</b>: <b>игра́</b> là trò chơi, cuộc '
    'chơi nói chung, còn <b>матч</b> chỉ một trận đấu thể thao giữa hai bên.</div>'
    '<div class="hd-warn">⚠️ Có <i>ь</i> sau <i>ч</i> thì lật ngược sang giống '
    'cái: <b>ночь</b>, <b>дочь</b>. Một chữ <i>ь</i> đổi cả giống của từ.</div>'
)
V["матч"] = "trận đấu"

# ---------------------------------------------------------------- о́пера
S["опера"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mượn nguyên khối từ tiếng Ý <i>opera</i> — nghĩa gốc là '
    '«tác phẩm» (Latin <i>opus</i> công trình), nên không chẻ được. Khác với phần '
    'lớn từ mượn dồn trọng âm ra cuối (<b>бале́т</b>, <b>хокке́й</b>), từ này '
    'trọng âm ở âm ĐẦU và đứng yên cả bảng: <b>о́перы</b>, <b>о́пере</b>, '
    '<b>о́пер</b>. Nghĩa «nhà hát opera» chỉ là nói tắt của <b>о́перный '
    'теа́тр</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>о́перный</b> thuộc về opera · <b>опере́тта</b> nhạc '
    'kịch vui</div>'
)

# ------------------------------------------------------------ переда́ча
S["передача"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пере-</span>'
    '<span class="hd-gloss">qua, sang phía bên kia</span></div>'
    '<div class="hd-row"><span class="hd-piece">-да́ч-</span>'
    '<span class="hd-gloss">gốc <i>да-</i> CHO, TRAO (trong <b>дать</b>) cộng hậu '
    'tố dựng danh từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen «sự trao QUA», và mọi nghĩa đều mọc ra từ đó: '
    'trao đồ cho ai → sự chuyển giao; trao tín hiệu qua sóng → buổi phát, chương '
    'trình truyền hình. Khuôn dựng từ này gặp lại nguyên xi ở <b>сда́ча</b> (tiền '
    'trả lại) — cũng là tiền tố + <i>-да́ч-</i> + <i>-а</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>переда́ть</b> trao lại, chuyển hộ · '
    '<b>передава́ть</b> trao, truyền · <b>дать</b> đưa, cho · <b>сда́ча</b> tiền '
    'thừa trả lại</div>'
)
V["передача"] = "chương trình truyền hình, buổi phát sóng, sự truyền tải, sự chuyển giao"

# ------------------------------------------------------------ пла́вание
S["плавание"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пла́в-</span>'
    '<span class="hd-gloss">gốc BƠI, TRÔI — trong <b>пла́вать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ание</span>'
    '<span class="hd-gloss">biến động từ thành danh từ chỉ HÀNH ĐỘNG</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cứ <b>пла́вать</b> + <i>-ание</i> là ra «việc bơi». Đuôi '
    '<i>-ание/-ение</i> luôn cho danh từ giống TRUNG, đã gặp ở <b>зда́ние</b>, '
    '<b>объявле́ние</b>. Nghĩa thứ hai «chuyến đi đường biển» cũng chỉ là cái sự '
    'trôi trên nước ấy, kéo dài ra. Trọng âm không nhúc nhích khỏi '
    '<i>пла́-</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пла́вать</b> bơi · <b>плове́ц</b> người bơi, vận động '
    'viên bơi</div>'
)

# ------------------------------------------------------------------ поэ́т
S["поэт"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">поэ́т</span>'
    '<span class="hd-gloss">mượn nguyên khối Hy Lạp <i>poietes</i> = «người làm '
    'ra» (<i>poieo</i> tôi làm ra + đuôi chỉ người); trong tiếng Nga đã dính liền, '
    'không tách được nữa</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc Hy Lạp không phải «người mơ mộng» mà là «người '
    'LÀM RA» — người làm ra bài thơ. Chính tả cần để ý: sau nguyên âm <i>о</i> thì '
    'viết <i>э</i> chứ không viết <i>е</i>, để giữ âm [e] cứng — <b>поэ́т</b>, '
    '<b>поэ́зия</b>, <b>поэ́ма</b>. Giống đực, trọng âm ở <i>-э́-</i> và đứng '
    'yên.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поэ́зия</b> thơ ca · <b>поэ́ма</b> trường ca · '
    '<b>поэти́ческий</b> thuộc về thơ</div>'
)

# -------------------------------------------------------- увлека́ться
S["увлекаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố — ở từ này không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-влек-</span>'
    '<span class="hd-gloss">gốc KÉO, LÔI — chính từ <b>влечь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-</span>'
    '<span class="hd-gloss">dấu hiệu thể CHƯA HOÀN THÀNH, việc kéo dài</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">phản thân — để chính mình bị kéo</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: «để cho mình bị KÉO theo cái gì» → say mê. Cái '
    'mình mê phải để cách 5: <b>Я увлека́юсь спо́ртом</b>. Mảnh <i>-а-</i> cho biết '
    'đây là thể chưa hoàn thành, dùng cho sở thích kéo dài; bạn thể của nó là '
    '<b>увле́чься</b>, cùng gốc, chỉ đổi <i>к</i> thành <i>ч</i>.</div>'
    '<div class="hd-warn">⚠️ Cùng đòi cách 5 với <b>интересова́ться</b> nhưng KHÁC '
    'GỐC hẳn và mạnh hơn: <b>интересова́ться</b> là để tâm tìm hiểu, còn từ này là '
    'mê đắm, dồn cả thời gian vào.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>увле́чься</b> bạn thể hoàn thành · <b>увлече́ние</b> '
    'niềm đam mê · <b>развлече́ние</b> trò giải trí · <b>влечь</b> kéo, lôi '
    'cuốn</div>'
)
V["увлекаться"] = "đam mê, say mê, bị cuốn hút"

# ------------------------------------------------------------ увле́чься
S["увлечься"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố — ở từ này không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-влеч-</span>'
    '<span class="hd-gloss">vẫn là gốc KÉO <i>влек-</i>, đứng trước <i>ь/ё</i> thì '
    '<i>к</i> đổi thành <i>ч</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">phản thân — để chính mình bị kéo</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng nghĩa đen «bị kéo theo cái gì» và cùng gốc với '
    '<b>увлека́ться</b>; khác đúng một chỗ: đây là thể HOÀN THÀNH, chỉ khoảnh khắc '
    'đâm ra say mê, không phải trạng thái kéo dài. Cũng đòi cách 5: <b>Он увлёкся '
    'хокке́ем</b>.</div>'
    '<div class="hd-warn">⚠️ Thân từ đổi qua lại <i>к/ч</i> ngay trong một bảng: '
    '<b>увлеку́сь</b> · <b>увлечёшься</b> · <b>увлеку́тся</b>. Và quá khứ dịch '
    'trọng âm: <b>увлёкся</b> nhưng <b>увлекла́сь</b>, <b>увлекли́сь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>увлека́ться</b> bạn thể chưa hoàn thành · '
    '<b>увлече́ние</b> niềm đam mê · <b>влечь</b> kéo, lôi cuốn</div>'
)

# ---------------------------------------------------------------- хо́бби
S["хобби"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mượn thẳng tiếng Anh <i>hobby</i>, một khối, không chẻ. '
    'Hai điều phải thuộc. Một: nó KHÔNG biến cách — mọi cách đều viết y hệt '
    '<b>хо́бби</b>, chỉ nhìn từ đứng cạnh mới biết đang ở cách nào. Hai: nó là '
    'giống TRUNG, nên nói <b>моё хо́бби</b> chứ không phải <i>мой</i> — đúng khuôn '
    'của từ mượn kết thúc bằng nguyên âm đã học: <b>кино́</b>, <b>метро́</b>, '
    '<b>такси́</b>. Trọng âm ở âm đầu. Từ Nga bản địa cùng nghĩa là '
    '<b>увлече́ние</b> (xem thẻ <b>увлека́ться</b>); <b>хо́бби</b> là cách nói mượn, '
    'hiện đại và thông dụng hơn trong đời thường.</div>'
)

# --------------------------------------------------------------- хокке́й
S["хоккей"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mượn thẳng tiếng Anh <i>hockey</i>, không chẻ ra mảnh nào, '
    'và giữ nguyên hai chữ <i>кк</i> của bản gốc. Đuôi <i>-й</i> làm nó thành giống '
    'đực và biến cách rất êm, trọng âm bám <i>-ке́й</i> cả bảng: <b>хокке́я</b>, '
    '<b>хокке́ем</b>. Người chơi môn này là <b>хоккеи́ст</b> — cùng khuôn '
    '<i>-и́ст</i> với <b>журнали́ст</b>, <b>тури́ст</b> đã học.</div>'
    '<div class="hd-why">Cách nói «chơi môn này» (<b>игра́ть в</b> + cách 4) nằm ở '
    'thẻ <b>волейбо́л</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>хоккеи́ст</b> vận động viên khúc côn cầu</div>'
)

# ------------------------------------------------------------ экску́рсия
S["экскурсия"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">экс-</span>'
    '<span class="hd-gloss">RA NGOÀI (Latin <i>ex-</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ку́рс-</span>'
    '<span class="hd-gloss">chạy, đường đi — chính từ <b>курс</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ия</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái, mượn theo Latin</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen «cuộc CHẠY RA NGOÀI» → chuyến ra khỏi nhà để đi '
    'xem ngắm. Đã biết <b>курс</b> (hướng đi, khoá học) thì nhận ra ngay cái ruột '
    'của từ này, không phải học thuộc mù. Trọng âm ở <i>-ку́р-</i> và đứng '
    'yên.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>курс</b> hướng đi, khoá học · <b>экскурсово́д</b> '
    'hướng dẫn viên du lịch</div>'
)
