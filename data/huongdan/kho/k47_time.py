# -*- coding: utf-8 -*-
"""k47 — time: mốc thời gian Nga bản địa (вечер, ночь, день, осень, время)
đứng cạnh 11 tên tháng mượn thẳng từ Latin qua đường Hy Lạp."""

S = {}
V = {}

S["вечер"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ве́чер-</span>'
    '<span class="hd-gloss">BUỔI TỐI — gốc trơn, không chẻ nhỏ hơn được</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ Ấn–Âu rất cổ: cùng gốc với Latin <i>vesper</i> (sao Hôm), '
    'tiếng Anh <i>vespers</i> là buổi kinh chiều.</div>'
    '<div class="hd-why">Số ít trọng âm đứng yên, nhưng số nhiều nhảy hẳn ra đuôi: '
    '<b>вечера́</b>, đúng kiểu <b>дом</b> → <b>дома́</b>.</div>'
    '<div class="hd-warn"><b>до́брый ве́чер</b> = chào buổi tối, dùng từ chập tối trở đi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ве́чером</b> vào buổi tối · <b>вече́рний</b> thuộc buổi tối '
    '(trọng âm dịch vào giữa) · <b>вечери́нка</b> buổi tiệc tối</div>'
)

S["ночь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ночь</span>'
    '<span class="hd-gloss">ĐÊM — gốc trơn, không chẻ được</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một trong những từ Ấn–Âu còn nguyên hình rõ nhất: Latin '
    '<i>nox</i>, Anh <i>night</i>, Đức <i>Nacht</i>. Đuôi <b>-ь</b> ở đây là giống cái.</div>'
    '<div class="hd-why">Số ít trọng âm nằm yên; sang số nhiều nó nhảy ra đuôi từ cách 2 '
    'trở đi: <b>но́чи</b> nhưng <b>ноче́й</b>, <b>ноча́ми</b>.</div>'
    '<div class="hd-warn"><b>споко́йной но́чи</b> = chúc ngủ ngon; nghĩa đen là chúc một '
    'đêm yên bình, cả cụm nằm ở cách 2.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>но́чью</b> vào ban đêm · <b>ночно́й</b> thuộc về đêm · '
    '<b>по́лночь</b> nửa đêm</div>'
)

S["день"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дн-</span>'
    '<span class="hd-gloss">NGÀY — thân từ thật chỉ có hai chữ này</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">NGUYÊN ÂM CHẠY: chữ <b>е</b> chỉ mọc ra để đỡ dạng trần '
    '<b>день</b>; thêm bất cứ đuôi nào là nó rơi mất — <b>дня</b>, <b>дню</b>, '
    '<b>днём</b>, <b>дне</b>.</div>'
    '<div class="hd-warn"><b>до́брый день</b> = chào ban ngày, dùng từ khoảng trưa tới '
    'chiều muộn.</div>'
    '<div class="hd-warn"><b>день рожде́ния</b> = sinh nhật, nghĩa đen là ngày của sự ra '
    'đời (<b>рожде́ния</b> ở cách 2).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>днём</b> vào ban ngày · <b>дневно́й</b> thuộc ban ngày · '
    '<b>по́лдень</b> giữa trưa · <b>сего́дня</b> hôm nay</div>'
)

S["сегодня"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сего́</span>'
    '<span class="hd-gloss">CỦA CÁI NÀY — cách 2 của <b>сей</b>, đại từ cổ</span></div>'
    '<div class="hd-row"><span class="hd-piece">дня</span>'
    '<span class="hd-gloss">CỦA NGÀY — cách 2 của <b>день</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hai từ cách 2 dính lại thành một khối: của ngày này. Vì vốn là một '
    'dạng đã chia rồi đông cứng lại nên <b>сего́дня</b> không biến đổi gì thêm.</div>'
    '<div class="hd-warn">Đọc là <i>сево́дня</i>: chữ <b>г</b> trong đuôi cách 2 '
    '<i>-ого / -его</i> luôn phát âm thành <b>в</b> — như <b>его́</b>, <b>кра́сного</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сего́дняшний</b> của ngày hôm nay · <b>сейча́с</b> bây giờ '
    '(cũng chứa <b>сей</b>) · <b>день</b> ngày</div>'
)

S["сейчас"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сей</span>'
    '<span class="hd-gloss">NÀY — đại từ cổ, nay gần như chết</span></div>'
    '<div class="hd-row"><span class="hd-piece">ча́с</span>'
    '<span class="hd-gloss">GIỜ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen là giờ này, tức lúc này. Từ <b>сей</b> chỉ còn sống '
    'trong vài khối đông cứng như <b>сейча́с</b> và <b>сего́дня</b>.</div>'
    '<div class="hd-why">Nó nhìn được cả hai chiều quanh hiện tại: vừa mới xong, hoặc '
    'ngay bây giờ, hoặc ngay lát nữa.</div>'
    '<div class="hd-warn"><b>сейча́с</b> là đúng khoảnh khắc này. <b>тепе́рь</b> cũng dịch '
    'là bây giờ nhưng mang ý từ nay trở đi, khác với trước kia.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>час</b> giờ · <b>часы́</b> đồng hồ · <b>сего́дня</b> hôm nay</div>'
)

S["месяц"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ме́с-</span>'
    '<span class="hd-gloss">TRĂNG / THÁNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-яц</span>'
    '<span class="hd-gloss">hậu tố danh từ, không mang nghĩa riêng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc Ấn–Âu với tiếng Anh <i>moon</i> và <i>month</i>, Latin '
    '<i>mensis</i>: người xưa đếm tháng bằng tuần trăng, nên một từ ôm cả hai nghĩa.</div>'
    '<div class="hd-warn">Nghĩa trăng của <b>ме́сяц</b> là vầng trăng lưỡi liềm nhìn thấy '
    'trên trời; còn thiên thể Mặt Trăng nói chung thì gọi là <b>луна́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ме́сячный</b> hàng tháng, kéo dài một tháng · '
    '<b>полуме́сяц</b> vầng trăng khuyết</div>'
)

S["осень"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о́сень</span>'
    '<span class="hd-gloss">MÙA THU — gốc trơn, không chẻ được</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc cổ này được cho là mang nghĩa mùa gặt (họ với Đức '
    '<i>Ernte</i> vụ thu hoạch): mùa thu là mùa gom lúa về.</div>'
    '<div class="hd-why">Cả số ít lẫn số nhiều đều đặn, trọng âm không rời chữ '
    '<b>о́</b> đầu từ, kể cả <b>о́сеней</b>.</div>'
    '<div class="hd-warn">Đuôi <b>-ь</b> KHÔNG cho biết giống: <b>о́сень</b> và '
    '<b>ночь</b> giống cái, còn <b>день</b> cùng đuôi lại giống đực. Phải nhớ theo từng từ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>осе́нний</b> thuộc mùa thu (trọng âm dịch vào giữa) · '
    '<b>о́сенью</b> vào mùa thu</div>'
)

S["осенью"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о́сень-</span>'
    '<span class="hd-gloss">MÙA THU</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ю</span>'
    '<span class="hd-gloss">đuôi cách 5 của danh từ giống cái đuôi <b>-ь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiếng Nga trả lời câu hỏi vào lúc nào bằng CÁCH 5 trần, không '
    'cần giới từ: <b>о́сенью</b> vào mùa thu, <b>но́чью</b> ban đêm, <b>днём</b> ban ngày, '
    '<b>ве́чером</b> buổi tối.</div>'
    '<div class="hd-why">Dạng này đã đông cứng thành trạng từ nên không chia nữa, và '
    'trọng âm giữ nguyên chỗ cũ của <b>о́сень</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>о́сень</b> mùa thu · <b>осе́нний</b> thuộc mùa thu</div>'
)

S["время"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">врем-</span>'
    '<span class="hd-gloss">THỜI GIAN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-я</span>'
    '<span class="hd-gloss">đuôi danh từ giống trung nhóm <b>-мя</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiếng Nga chỉ có 10 danh từ trung đuôi <b>-мя</b>, và cả nhóm '
    'chèn thêm <b>-ен-</b> trước mọi đuôi: <b>вре́мени</b>, <b>вре́менем</b>. Số nhiều '
    '<b>времена́</b> còn đẩy trọng âm ra tận cuối.</div>'
    '<div class="hd-warn">Viết liền hay tách là hai từ khác hẳn: <b>во вре́мя</b> + cách 2 '
    'nghĩa là trong lúc, còn <b>во́время</b> một chữ nghĩa là đúng giờ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вре́менный</b> tạm thời · <b>совреме́нный</b> hiện đại '
    '(<b>со-</b> cùng + <b>вре́мя</b>, dựng y hệt <i>contemporary</i>)</div>'
)

S["март"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn nguyên khối từ Latin <i>Martius</i>, tiếng '
    'Nga không cắt ra mảnh nào có nghĩa riêng.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><i>Martius</i> là tháng của <b>Mars</b>, thần chiến tranh — mùa '
    'mở màn chiến dịch. Tiếng Anh cho ra <i>March</i> và <i>martial</i> (thuộc quân sự).</div>'
    '<div class="hd-why">Mốc quan trọng nhất của cả lô nằm ở đây: năm La Mã cổ BẮT ĐẦU từ '
    'tháng này. Nhớ nó là hiểu vì sao bốn tháng cuối năm mang số đếm lệch đúng 2.</div>'
    '<div class="hd-why">Một âm tiết nên trọng âm đứng yên. Ngày tháng luôn ở cách 2: '
    '<b>пе́рвое ма́рта</b> = mồng 1 tháng 3.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ма́ртовский</b> thuộc tháng 3 — mọi tên tháng đều đẻ tính từ '
    'theo khuôn này, thêm <b>-ский</b> hoặc <b>-овский</b>.</div>'
)

S["январь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn nguyên khối từ Latin <i>Januarius</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đặt theo <b>Janus</b>, thần của cửa ra vào và của mọi khởi đầu. '
    'Thần này có hai mặt: một mặt nhìn về năm cũ, một mặt nhìn sang năm mới — đúng chỗ '
    'đứng của tháng 1. Tiếng Anh <i>January</i>.</div>'
    '<div class="hd-why">Trọng âm rời thân ngay khi thêm đuôi: <b>янва́рь</b> nhưng '
    '<b>января́</b>, <b>январе́</b>. Vì ngày tháng luôn ở cách 2 nên dạng gặp nhiều nhất '
    'chính là <b>пе́рвое января́</b>.</div>'
)

S["февраль"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: Latin <i>Februarius</i>, từ <i>februa</i> — lễ '
    'tẩy uế.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trong lịch La Mã cũ (bắt đầu từ <b>март</b>) đây là tháng CUỐI '
    'năm, dành cho lễ tẩy uế trước khi sang năm mới. Đứng chót hàng nên nó cũng là tháng '
    'bị cắt ngắn còn 28 ngày. Tiếng Anh <i>February</i>.</div>'
    '<div class="hd-why">Trọng âm dịch ra đuôi khi chia: <b>февра́ль</b> nhưng '
    '<b>февраля́</b>, <b>феврале́</b>.</div>'
)

S["апрель"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: Latin <i>Aprilis</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tên này thường được nối với Latin <i>aperire</i> mở ra — tháng '
    'chồi non bật mở. Tiếng Anh <i>April</i>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: chỗ nối với <i>aperire</i> là giả thuyết từ nguyên '
    'còn tranh cãi, không phải luật suy ra được.</div>'
    '<div class="hd-why">Đây là chỗ <b>апре́ль</b> tách khỏi <b>янва́рь</b> và '
    '<b>февра́ль</b>: trọng âm của nó ĐỨNG YÊN khi chia — <b>апре́ля</b>, <b>апре́ле</b>. '
    'Trong chín tháng đuôi mềm <b>-рь</b> hay <b>-ль</b>, chỉ ba tháng đứng yên như vậy: <b>апре́ль</b>, <b>ию́нь</b>, <b>ию́ль</b>.</div>'
)

S["июнь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: Latin <i>Junius</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đặt theo nữ thần <b>Juno</b>, vợ của Jupiter và là thần bảo trợ '
    'hôn nhân — nên tháng 6 là tháng cưới của người La Mã. Tiếng Anh <i>June</i>.</div>'
    '<div class="hd-warn">Khác <b>ию́ль</b> đúng MỘT chữ cuối. Bám vào tiếng Anh cho chắc: '
    '<b>ию́нь</b> tận cùng <b>нь</b> như ju<i>n</i>e, còn <b>ию́ль</b> tận cùng <b>ль</b> '
    'như ju<i>l</i>y.</div>'
    '<div class="hd-why">Trọng âm đứng yên khi chia: <b>ию́ня</b>, <b>ию́не</b>.</div>'
)

S["июль"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: Latin <i>Julius</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tháng sinh của <b>Julius Caesar</b>; Viện nguyên lão đổi tên '
    'tháng để tôn ông. Ít lâu sau hoàng đế Augustus bắt chước đúng chiêu đó với '
    '<b>а́вгуст</b>. Tiếng Anh <i>July</i>.</div>'
    '<div class="hd-warn">Đừng lẫn với <b>ию́нь</b> tháng 6: chữ cuối của tháng 7 là '
    '<b>ль</b>, như chữ l trong ju<i>l</i>y.</div>'
    '<div class="hd-why">Trọng âm đứng yên khi chia: <b>ию́ля</b>, <b>ию́ле</b>.</div>'
)

S["август"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn nguyên khối từ Latin <i>Augustus</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hoàng đế <b>Augustus</b> lấy chính tên mình đặt cho tháng này, '
    'đúng như Julius Caesar đã làm với <b>ию́ль</b>. Tiếng Anh giữ cả hai: danh từ '
    '<i>August</i> tháng 8 và tính từ <i>august</i> uy nghi.</div>'
    '<div class="hd-why">Trong các tên tháng nhiều âm tiết, đây là tên DUY NHẤT có trọng âm ở âm tiết đầu, và nó không '
    'nhúc nhích khi chia: <b>пе́рвое а́вгуста</b>.</div>'
)

S["сентябрь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сент-</span>'
    '<span class="hd-gloss">BẢY — Latin <i>septem</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́брь</span>'
    '<span class="hd-gloss">đuôi tên tháng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Số 7 mà lại là tháng 9, vì năm La Mã bắt đầu từ <b>март</b>: mọi '
    'số ở đây đều lệch đúng 2. Tiếng Anh <i>September</i>, <i>septet</i> bản nhạc bảy bè.</div>'
    '<div class="hd-why">Đuôi <b>-брь</b> đi vòng qua tiếng Hy Lạp trước khi vào tiếng '
    'Nga, nên bị bóp còn một cụm phụ âm chứ không giữ dạng <i>-ber</i> như tiếng Anh.</div>'
    '<div class="hd-why">Trọng âm dịch ra đuôi: <b>сентября́</b> — dạng gặp nhiều nhất là '
    '<b>пе́рвое сентября́</b>, ngày khai giảng của cả nước Nga.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">Bốn tháng cùng đuôi <b>-брь</b>: <b>сентя́брь</b> · <b>октя́брь</b> · '
    '<b>ноя́брь</b> · <b>дека́брь</b> — đều mang số đếm La Mã, đều dịch trọng âm khi chia.</div>'
)

S["октябрь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">окт-</span>'
    '<span class="hd-gloss">TÁM — Latin <i>octo</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́брь</span>'
    '<span class="hd-gloss">đuôi tên tháng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng con số 8 với <i>octopus</i> tám chân và <i>octave</i> quãng '
    'tám. Nó rơi xuống ô thứ 10 vì cả dãy lệch 2, mốc gốc nằm ở thẻ <b>март</b>.</div>'
    '<div class="hd-why">Trọng âm dịch ra đuôi khi chia: <b>октя́брь</b> nhưng '
    '<b>октября́</b>, <b>октябре́</b>.</div>'
)

S["ноябрь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ноя́-</span>'
    '<span class="hd-gloss">CHÍN — Latin <i>novem</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-брь</span>'
    '<span class="hd-gloss">đuôi tên tháng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Số 9 đứng ở ô thứ 11, vẫn đúng độ lệch 2 của cả dãy. Chữ '
    '<b>в</b> của <i>novem</i> rụng mất trên đường vòng qua tiếng Hy Lạp, nên chỉ còn '
    '<b>ноя́-</b>; tiếng Anh <i>November</i> giữ lại nó.</div>'
    '<div class="hd-why">Trọng âm dịch ra đuôi khi chia: <b>ноя́брь</b> nhưng '
    '<b>ноября́</b>, <b>ноябре́</b>.</div>'
)

S["декабрь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дек-</span>'
    '<span class="hd-gloss">MƯỜI — Latin <i>decem</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-абрь</span>'
    '<span class="hd-gloss">đuôi tên tháng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Số 10 khép dãy ở ô thứ 12. Cùng gốc đếm với <i>decade</i> mười '
    'năm và <i>decimal</i> thập phân.</div>'
    '<div class="hd-why">Trọng âm dịch ra đuôi khi chia: <b>дека́брь</b> nhưng '
    '<b>декабря́</b>, <b>декабре́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>декабри́ст</b> người Tháng Chạp — nhóm sĩ quan khởi nghĩa '
    'tháng 12 năm 1825; đây là chỗ hiếm hoi tiếng Nga tự đẻ một từ mới ra từ tên tháng đi mượn.</div>'
)

# --- field Vietnamese (đề bài deck 1-go) — README §2c -----------------------
# 11 tên tháng trước đây ghi bằng 4 kiểu lẫn lộn (tháng Ba / tháng sáu /
# tháng 7 / tháng Mười Hai). Thống nhất DẠNG SỐ cho cả 11: không lẫn với
# cách gọi tháng âm lịch trong tiếng Việt (tháng Một = tháng 11 âm).
V["январь"] = "tháng 1"
V["февраль"] = "tháng 2"
V["март"] = "tháng 3"
V["апрель"] = "tháng 4"
V["июнь"] = "tháng 6"
V["июль"] = "tháng 7"
V["август"] = "tháng 8"
V["сентябрь"] = "tháng 9"
V["октябрь"] = "tháng 10"
V["ноябрь"] = "tháng 11"
V["декабрь"] = "tháng 12"

V["сейчас"] = "bây giờ, ngay lúc này, ngay lập tức, sắp"
V["время"] = "thời gian, thời điểm, thời đại"
