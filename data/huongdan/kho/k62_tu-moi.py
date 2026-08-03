# -*- coding: utf-8 -*-
"""k62 — tu-moi: 16 danh từ user thêm 03/08 (đồ ăn · quần áo · đồ vật trong nhà).
CỐ Ý KHÔNG có trục chung — mỗi thẻ đứng một mình. Hai chỗ dùng chung duy nhất
được trải đầy đủ ở ĐÚNG MỘT thẻ rồi thôi: luật nguyên âm chạy của đuôi -ка đặt ở
ку́ртка (từ hay gặp nhất), danh sách các loại giày đặt ở о́бувь (từ tập hợp).
Không khối hệ thống dùng chung, tối đa 2 ô đỏ, nhắm dưới một màn hình iPhone.
Chuẩn v3."""

# 🔴 KHÔNG dựng biến khối dùng chung rồi cộng vào mọi thẻ — xem README §3.

S = {}
V = {}

S["банан"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — từ mượn quốc tế nguyên khối, mặt chữ '
    'trùng khít với <b>banana</b> của tiếng Anh.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa thì bạn biết sẵn rồi, nên thứ duy nhất phải học ở từ này '
    'là <b>chỗ nhấn</b>: tiếng Anh nhấn giữa (ba-<b>NA</b>-na), tiếng Nga nhấn '
    '<b>âm cuối</b> — <b>бана́н</b>. Nhấn sai chỗ là người Nga không nhận ra từ, '
    'dù mọi chữ cái đều đúng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бана́новый</b> thuộc chuối, vị chuối</div>'
)

S["банка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ба́нк-</span>'
    '<span class="hd-gloss">thân từ mượn: cái đồ đựng miệng rộng có nắp</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một từ ôm cả hai thứ mà tiếng Việt gọi tên riêng: <b>lọ</b> thuỷ '
    'tinh có nắp vặn và <b>lon</b> kim loại. Điểm chung là đồ đựng kín để cất đồ ăn, '
    'đồ uống — nên hễ thấy thứ gì đóng kín cầm vừa tay thì dùng từ này.</div>'
    '<div class="hd-why"><b>Đọc cả bảng bằng một câu:</b> mọi cách đều đặn, riêng số nhiều '
    'cách 2 chèn thêm một <b>-о-</b> cho đỡ vấp cụm phụ âm: <b>ба́нок</b>.</div>'
    '<div class="hd-warn"><b>Bỏ đuôi -а ra là một từ KHÁC hẳn:</b> <b>банк</b> = ngân hàng. '
    'Hai từ vào tiếng Nga bằng hai con đường riêng, không suy từ nọ ra từ kia được — '
    'chỉ trùng mặt chữ thôi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ба́ночка</b> lọ nhỏ, hũ nhỏ · <b>ба́ночный</b> đóng lon</div>'
)

S["блузка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">блу́з-</span>'
    '<span class="hd-gloss">mượn tiếng Pháp <b>blouse</b> — áo choàng rộng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">đuôi giống cái, nhập tịch từ mượn và cho sắc thái gọn nhỏ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng một từ với <b>blouse</b> tiếng Anh, nhưng tiếng Nga đã thu hẹp '
    'nghĩa lại: <b>блу́зка</b> chỉ là áo của <b>phụ nữ</b>, mặc với váy hoặc quần âu. '
    'Cái đuôi <b>-ка</b> ở đây làm đúng việc nó vẫn làm với từ mượn — biến chúng thành '
    'danh từ giống cái chia được bình thường.</div>'
    '<div class="hd-why"><b>Đọc cả bảng bằng một câu:</b> đều đặn hết, chỉ số nhiều cách 2 '
    'mọc thêm nguyên âm chạy: <b>блу́зок</b>.</div>'
    '<div class="hd-warn"><b>Đừng lẫn với áo sơ mi:</b> <b>руба́шка</b> là áo có cổ bẻ, '
    'cài khuy suốt, chủ yếu của nam. блу́зка là đồ nữ, kiểu dáng tự do.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>блу́за</b> áo choàng rộng, áo bảo hộ (dạng gốc, không thu nhỏ)</div>'
)

S["ветчина"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ветч-</span>'
    '<span class="hd-gloss">biến dạng của lõi <b>ве́тх-</b> — CŨ, để lâu</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ина́</span>'
    '<span class="hd-gloss">đuôi gọi tên một loại thịt / một chất</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen là <b>thịt để lâu</b> — thịt muối, hun khói, cất được '
    'lâu ngày, đặt đối lại với thịt mới mổ. Nhớ được cái ý "để dành" là nhớ đúng thứ '
    'giăm bông trong tủ lạnh.</div>'
    '<div class="hd-why"><b>Đọc cả bảng bằng một câu:</b> ở số ít trọng âm nằm hết ngoài '
    'đuôi (<b>ветчина́</b>, <b>ветчины́</b>), sang số nhiều thì rút về thân '
    '(<b>ветчи́ны</b>) — nhưng đây là thứ đong bằng lát, số nhiều hầu như không dùng.</div>'
    '<div class="hd-warn">⚠️ <b>Mức tin:</b> mối nối với <b>ве́тхий</b> (cũ nát) là '
    '<b>từ nguyên</b>, không phải luật bạn suy ra được — phép đổi <b>х → ч</b> ở đây là '
    'trường hợp lẻ, đừng đem áp cho từ khác.</div>'
)

S["джинсы"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">джинс-</span>'
    '<span class="hd-gloss">mượn thẳng tiếng Anh <b>jeans</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ы</span>'
    '<span class="hd-gloss">đuôi SỐ NHIỀU — và từ này chỉ có số nhiều</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiếng Anh <b>jeans</b> vốn đã là số nhiều, tiếng Nga giữ nguyên '
    'tính đó: <b>джи́нсы</b> <b>không có dạng số ít</b>. Đúng như mọi thứ mặc có hai ống — '
    '<b>брю́ки</b> (quần dài), <b>шо́рты</b> (quần soóc). Vì vậy tính từ đi kèm cũng luôn ở '
    'số nhiều: <b>но́вые джи́нсы</b> (quần jean mới).</div>'
    '<div class="hd-warn"><b>Không đếm bằng số thường được:</b> một cái quần là '
    '<b>одни́ джи́нсы</b> (nghĩa đen "một bộ"), hai cái là <b>дво́е джи́нсов</b> — dùng số từ '
    'tập hợp, không nói "два…".</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>джи́нсовый</b> bằng vải bò (<b>джи́нсовая ку́ртка</b> áo khoác bò)</div>'
)

S["йогурт"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — mượn từ tiếng Thổ Nhĩ Kỳ (<b>yoğurt</b>) qua '
    'đường châu Âu, y hệt con đường mà tiếng Việt và tiếng Anh đã đi.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hai chi tiết đáng nhớ, cả hai đều nằm ở mặt chữ chứ không ở nghĩa: '
    '① trọng âm rơi vào <b>âm đầu</b> — <b>йо́гурт</b>, giống tiếng Anh; ② nó mở đầu bằng '
    'chữ <b>й</b>, thứ gần như không có ở từ Nga gốc — chỉ vài từ mượn làm thế '
    '(<b>йо́га</b>, <b>йод</b>). Thấy từ bắt đầu bằng <b>й</b> thì gần như chắc chắn đó là '
    'từ nước ngoài.</div>'
)

S["куртка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ку́рт-</span>'
    '<span class="hd-gloss">lõi mượn, gốc xa là Latin <b>curtus</b> = NGẮN, cụt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nếu đúng theo từ nguyên thì lõi của nó là <b>ngắn</b> — cùng ổ với '
    '<b>curt</b>, <b>curtail</b> tiếng Anh. Và đó cũng chính là nghĩa dùng thật: '
    '<b>ку́ртка</b> là áo khoác <b>ngắn</b>, dừng ở ngang hông, thường có khoá kéo.</div>'
    '<div class="hd-why"><b>Đọc cả bảng bằng một câu:</b> đều đặn, chỉ số nhiều cách 2 chèn '
    'thêm <b>-о-</b> vào giữa cụm phụ âm: <b>ку́рток</b>. Đây là <b>nguyên âm chạy</b>, luật '
    'chung cho mọi danh từ đuôi <b>-ка</b> có phụ âm chồng phụ âm đứng trước — trong lô này '
    'bạn gặp lại y hệt ở <b>ба́нок</b>, <b>блу́зок</b>, <b>соси́сок</b>.</div>'
    '<div class="hd-warn"><b>Ba từ đều dịch là "áo khoác", chọn theo độ dài:</b> '
    '<b>ку́ртка</b> ngắn tới hông (áo phao, áo gió) · <b>пальто́</b> dài quá gối, vải dạ · '
    '<b>плащ</b> mỏng, che mưa hoặc choàng ngoài.</div>'
)

S["матрёшка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">матрёш-</span>'
    '<span class="hd-gloss">từ <b>Матрёша</b>, tên gọi thân mật của <b>Матрёна</b> — '
    'tên phụ nữ nông thôn Nga rất phổ biến thời xưa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">đuôi giống cái, sắc thái thân mật</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây không phải từ chỉ đồ vật mà là một <b>cái tên người</b> đem đặt '
    'cho con búp bê. Tên <b>Матрёна</b> đi lên từ <b>matrona</b> Latin ("bà mẹ trong nhà") — '
    'cùng lõi <b>mat-</b> với <b>мать</b>, và với <b>matron</b>, <b>maternal</b> tiếng Anh. '
    'Búp bê mẹ ôm cả đàn con trong bụng: cái tên đã nói đúng nội dung.</div>'
    '<div class="hd-why"><b>Đọc cả bảng bằng một câu:</b> đều đặn, chỉ số nhiều cách 2 chèn '
    'nguyên âm — và vì đứng ngay sau <b>ш</b> mà không mang trọng âm nên viết <b>-е-</b> chứ '
    'không phải <b>-о-</b>: <b>матрёшек</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">Cùng lõi Ấn–Âu <b>mat-</b> (mẹ), không phải phái sinh trực tiếp: '
    '<b>мать</b> mẹ · <b>ма́ма</b> mẹ (thân mật) · <b>матери́нский</b> thuộc về mẹ</div>'
)

S["морковь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ ra mảnh có nghĩa được: <b>морк-</b> là lõi Slav cổ, còn '
    '<b>-овь</b> ngày nay chỉ còn làm mỗi việc đánh dấu giống cái.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thứ đáng nhớ ở từ này không phải nghĩa mà là <b>giống</b>: nó kết '
    'thúc bằng <b>-ь</b> nhưng là giống <b>cái</b>, nên chia theo lối riêng của nhóm '
    'giống cái đuôi mềm (cách 2, 3, 6 đều là <b>морко́ви</b>). Chữ <b>в</b> đứng trước '
    '<b>-ь</b> đọc điếc đi thành âm "f".</div>'
    '<div class="hd-warn"><b>Trong bếp, người Nga để từ này ở SỐ ÍT như một thứ đong được:</b> '
    'mua cả kilô vẫn nói <b>купи́ть морко́вь</b>. Muốn nói <b>một củ</b> thì đổi sang '
    '<b>морко́вка</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>морко́вка</b> một củ cà rốt (lối nói hằng ngày) · '
    '<b>морко́вный</b> thuộc cà rốt (<b>морко́вный сок</b> nước ép cà rốt)</div>'
)

S["обувь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">BAO LẤY, trùm quanh</span></div>'
    '<div class="hd-row"><span class="hd-piece">-у(в)-</span>'
    '<span class="hd-gloss">lõi cổ "xỏ vào chân" — thấy nguyên hình trong <b>обу́ть</b>; '
    'chữ <b>в</b> chỉ chèn vào cho dễ đọc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ь</span>'
    '<span class="hd-gloss">đuôi làm danh từ giống cái, gọi tên cả một loại đồ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>cái trùm lấy bàn chân</b>. Cặp động từ đáng học kèm '
    'ngay: <b>обу́ть</b> (xỏ giày vào) ↔ <b>разу́ть</b> (tháo giày ra) — đúng cặp tiền tố '
    '"trùm vào / gỡ ra" mà bạn đã thấy ở <b>оде́ть</b> ↔ <b>разде́ть</b> với quần áo.</div>'
    '<div class="hd-warn"><b>Từ TẬP HỢP, không có số nhiều:</b> một chữ <b>о́бувь</b> đã là '
    '"giày dép nói chung". Muốn nói một đôi cụ thể thì phải gọi tên riêng: '
    '<b>ту́фли</b> giày da lịch sự · <b>боти́нки</b> giày cao cổ · <b>кроссо́вки</b> giày thể '
    'thao · <b>та́почки</b> dép đi trong nhà.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обу́ть</b> xỏ giày vào · <b>обува́ться</b> tự đi giày · '
    '<b>разу́ться</b> cởi giày ra · <b>обувно́й</b> thuộc giày dép</div>'
)

S["продукт"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">RA PHÍA TRƯỚC, ra ngoài</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дукт</span>'
    '<span class="hd-gloss">DẪN, đưa đi — lõi Latin <b>duct-</b> như trong '
    '<b>conduct</b>, <b>duct</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cộng hai mảnh: <b>cái được dẫn ra ngoài</b> = thứ làm ra được, '
    'đúng nghĩa <b>product</b> tiếng Anh. Đây là mảnh Latin chứ không phải mảnh Nga, nhưng '
    'nhận ra chúng là mở khoá được cả loạt từ quốc tế đang nằm sẵn trong tiếng Nga.</div>'
    '<div class="hd-warn"><b>Số ít và số nhiều lệch nghĩa nhau — chỗ đáng thuộc nhất:</b> '
    'dạng số ít nói về <b>sản phẩm</b>, thứ được làm ra (dùng cả nghĩa bóng). Còn '
    '<b>thực phẩm</b> đi chợ mua về thì người Nga luôn để ở số nhiều: '
    '<b>проду́кты</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>продукти́вный</b> hiệu quả, cho ra nhiều · '
    '<b>проду́кция</b> sản lượng, hàng làm ra</div>'
)

S["сосиска"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">соси́с-</span>'
    '<span class="hd-gloss">mượn tiếng Pháp <b>saucisse</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">đuôi giống cái, nhập tịch từ mượn</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng lò với <b>sausage</b> và <b>sauce</b> tiếng Anh: gốc xa là '
    'Latin <b>salsus</b> = "đã ướp muối" (từ <b>sal</b> = muối, cũng là gốc của '
    '<b>salad</b>, <b>salary</b>). Trên bàn ăn Nga từ này gần như luôn ở số nhiều — '
    '<b>соси́ски</b>; số nhiều cách 2 chèn nguyên âm chạy: <b>соси́сок</b>.</div>'
    '<div class="hd-warn"><b>Ba thứ đều dịch là "xúc xích", phân theo hình dáng:</b> '
    '<b>соси́ска</b> nhỏ bằng ngón tay, luộc ăn nóng · <b>сарде́лька</b> ngắn và mập hơn · '
    '<b>колбаса́</b> cây to, cắt lát ăn nguội.</div>'
)

S["сувенир"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Trong tiếng Nga không chẻ được — mượn nguyên khối từ tiếng Pháp '
    '<b>souvenir</b>, y như tiếng Anh đã mượn.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>Souvenir</b> tiếng Pháp nghĩa đen là <b>nhớ lại</b> (Latin '
    '<b>sub-venire</b> = "trồi lên" trong trí). Vì vậy <b>сувени́р</b> không phải món quà '
    'bất kỳ, mà là <b>vật để nhớ một nơi đã đến</b> — nghĩa nằm sẵn trong từ.</div>'
    '<div class="hd-warn"><b>Đừng dùng thay cho quà tặng nói chung:</b> <b>пода́рок</b> là '
    'quà sinh nhật, quà lễ tết; <b>сувени́р</b> gắn với chuyến đi, mua ở nơi du lịch.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сувени́рный</b> thuộc quà lưu niệm '
    '(<b>сувени́рная ла́вка</b> quầy bán đồ lưu niệm)</div>'
)

S["творог"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">твор-</span>'
    '<span class="hd-gloss">LÀM RA, kết lại — lõi của <b>твори́ть</b> (tạo ra)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ог</span>'
    '<span class="hd-gloss">đuôi danh từ cổ, nay không còn đẻ ra từ mới</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Theo từ nguyên đây là <b>cái được làm ra</b> từ sữa: sữa chua lại '
    'rồi <b>kết</b> thành hạt, vắt ráo nước là xong. Nhớ ý "sữa đông kết lại" là nhớ đúng '
    'thứ trắng lổn nhổn ăn bằng thìa này.</div>'
    '<div class="hd-warn"><b>Ba thứ trắng đừng lẫn:</b> <b>творо́г</b> là hạt sữa đông ăn '
    'bằng thìa · <b>сыр</b> là phô mai miếng cắt lát · <b>смета́на</b> là kem chua để rưới '
    'và nấu.</div>'
    '<div class="hd-warn"><b>Đọc cả bảng bằng một câu:</b> trọng âm chạy ra <b>đuôi</b> ở '
    'mọi cách trừ cách 1 và cách 4 — <b>творо́г</b> nhưng <b>творога́</b>, <b>творого́м</b>. '
    'Người Nga còn nói cả kiểu dồn trọng âm về đầu từ, từ điển chấp nhận cả hai; nghe kiểu '
    'kia đừng tưởng mình học sai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">Cùng gốc theo từ nguyên: <b>твори́ть</b> tạo ra · '
    '<b>творо́жный</b> thuộc phô mai tươi · <b>тво́рчество</b> sự sáng tạo</div>'
)

S["туфля"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ту́фл-</span>'
    '<span class="hd-gloss">lõi mượn (tiếng Đức <b>Pantoffel</b>) — không chẻ nhỏ hơn '
    'được</span></div>'
    '<div class="hd-row"><span class="hd-piece">-я</span>'
    '<span class="hd-gloss">đuôi giống cái, loại mềm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Là giày <b>da đế cứng đi với đồ lịch sự</b>: giày tây của nam, '
    'giày cao gót của nữ — không dùng cho giày thể thao hay giày cao cổ. Vì giày đi thành '
    'đôi nên dạng hay gặp là số nhiều <b>ту́фли</b>.</div>'
    '<div class="hd-warn"><b>Dạng gốc là số ít giống cái</b> — <b>ту́фля</b>. Chớ lấy số '
    'nhiều cách 2 <b>ту́фель</b> làm dạng gốc (lỗi này người Nga cũng mắc). Nó chỉ đúng trong '
    '<b>па́ра ту́фель</b> = một đôi giày — chỗ chèn <b>-е-</b> cho đỡ vấp cụm <b>фл</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ту́фелька</b> giày nhỏ xinh (giày trẻ con, giày búp bê)</div>'
)

S["ёрш"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được — một tiếng duy nhất, không tiền tố '
    'cũng không hậu tố.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc là một loài <b>cá sông nhỏ mình tua tủa vây gai</b>. '
    'Chính hình ảnh "xù gai" đó đẻ ra hai nghĩa còn lại: <b>cây cọ</b> rửa chai lọ, bồn cầu '
    '(lông xù y hệt con cá), và món <b>bia pha vodka</b> — thứ "gai góc" hạ gục người uống '
    'rất nhanh.</div>'
    '<div class="hd-warn"><b>Đọc cả bảng bằng một câu:</b> chữ <b>ё</b> chỉ tồn tại khi nó '
    '<b>mang trọng âm</b>. Trọng âm vừa nhảy ra đuôi là <b>ё</b> tụt xuống thành <b>е</b>: '
    '<b>ёрш</b> nhưng <b>ерша́</b>, <b>ершу́</b>, <b>ерши́</b>. Luật này đúng cho từ Nga '
    'gốc — thấy <b>ё</b> là biết trọng âm nằm ở đó, khỏi phải tra.</div>'
    '<div class="hd-warn">⚠️ <b>Dòng nghĩa tiếng Việt cũ thiếu nghĩa GỐC:</b> từ điển Anh '
    'xếp "ruff" (con cá) đứng đầu, và bảng chia bên dưới là bảng của <b>vật sống</b> '
    '(cách 4 mượn dạng cách 2: <b>ерша́</b>) — tức bảng của con cá, không phải của cây cọ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ёршик</b> cây cọ nhỏ (cọ bồn cầu, cọ cốc) · '
    '<b>ерши́ться</b> xù lông lên, cãi lại</div>'
)

# ── Field Vietnamese ─────────────────────────────────────────────────────────
# Chỉ sửa chỗ dòng tiếng Việt TỰ NÓ mơ hồ hoặc sai. Không ghi từ loại / giống —
# mặt đề bài đã in badge (README §2c). Bốn chỗ đầu là VA CHẠM NỘI BỘ với thẻ đã
# có trong kho (пальто, колбаса, сыр) mà phép quét chuỗi không thấy vì chữ khác
# nhau; ba chỗ sau là thứ không badge nào chứa (số nhiều-only, tập hợp, số ít).
V["куртка"] = "áo khoác ngắn ngang hông (áo phao, áo gió — không phải áo khoác dài)"
V["сосиска"] = "xúc xích nhỏ cỡ ngón tay, luộc ăn nóng (không phải cây giò cắt lát)"
V["творог"] = "phô mai tươi dạng hạt vón, ăn bằng thìa (không phải phô mai miếng)"
V["продукт"] = "sản phẩm, thứ được làm ra (nghĩa 'thực phẩm' là khi từ này ở số nhiều)"
V["обувь"] = "giày dép nói chung (từ tập hợp, không có số nhiều)"
V["джинсы"] = "quần jean (từ chỉ dùng ở số nhiều)"
V["туфля"] = "giày da đế cứng đi với đồ lịch sự: giày tây, giày cao gót (ghi ở dạng một chiếc)"
# Dòng cũ bỏ mất nghĩa GỐC: từ điển Anh ghi "ruff" (con cá) đứng đầu, và bảng
# chia là bảng danh từ chỉ vật sống -> bảng của con cá. Xem ô đỏ trên thẻ.
V["ёрш"] = "cá ruff — cá sông nhỏ tua tủa vây gai; cũng là tên cây cọ rửa chai lọ, bồn cầu"
