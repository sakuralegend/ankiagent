# -*- coding: utf-8 -*-
"""k40 — qualities: 19 tính từ chỉ tính chất cơ bản. Trục của lô là DẠNG NGẮN —
chỗ duy nhất tính từ Nga không suy thẳng từ dạng dài được (chèn nguyên âm ở giống
đực, trọng âm chạy ra đuôi ở giống cái), cộng với các so sánh hơn đổi thân.

Không có khối dùng chung: mỗi thẻ chỉ nói dạng ngắn CỦA CHÍNH NÓ, bằng đúng các
dạng của nó (README §3). So sánh hơn cũng chỉ nêu FORM, không dựng luật chung —
mỗi từ biến âm một kiểu (з→ж, т→ч, х→ш, hoặc thay hẳn gốc).
"""

S = {}
V = {}

# --------------------------------------------------- nhóm -к-: mềm / dẻo / nhẹ
S["гибкий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">гиб-</span>'
    '<span class="hd-gloss">UỐN, gập lại</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-ий</span>'
    '<span class="hd-gloss">đuôi dựng tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>гиб-</b> là gốc của <b>сгиба́ть</b> «gập lại» và '
    '<b>изги́б</b> «chỗ uốn cong». Cái gì uốn được mà không gãy thì <b>ги́бкий</b> — '
    'từ cành cây, thân người cho tới nghĩa bóng «biết xoay xở».</div>'
    '<div class="hd-why">Dạng ngắn giống đực chèn thêm <b>о</b> cho đỡ vướng cụm '
    '<i>-бк</i>: <b>ги́бок</b>; giống cái đẩy trọng âm ra đuôi: <b>гибка́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ги́бкость</b> sự dẻo, sự linh hoạt · '
    '<b>сгиба́ть</b> gập lại · <b>изги́б</b> chỗ uốn cong</div>'
)
V['гибкий'] = 'dẻo, uốn cong được, linh hoạt'

S["мягкий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мягк-</span>'
    '<span class="hd-gloss">MỀM — gốc liền một khối, không tách nhỏ hơn được</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một gốc ôm cả nghĩa sờ vào (<b>мя́гкий</b> хлеб bánh mì mềm) '
    'lẫn nghĩa tính tình (<b>мя́гкий</b> хара́ктер tính dịu dàng). Hễ thêm đuôi thì cụm '
    '<b>-гк-</b> thành <b>-гч-</b>: <b>мя́гче</b> mềm hơn, <b>смягчи́ть</b> làm dịu bớt.</div>'
    '<div class="hd-warn">📌 <b>мя́гкий знак</b> chính là tên gọi của chữ <b>ь</b> — '
    '«dấu mềm», thứ làm mềm phụ âm đứng trước nó.</div>'
    '<div class="hd-why">Dạng ngắn: giống đực chèn <b>о</b> (<b>мя́гок</b>), giống cái '
    'dồn trọng âm ra đuôi (<b>мягка́</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мя́гкость</b> sự mềm mại · <b>мя́гко</b> nhẹ nhàng, êm · '
    '<b>смягчи́ть</b> làm dịu bớt</div>'
)
V['мягкий'] = 'mềm, dịu, êm'

S["лёгкий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">лёгк-</span>'
    '<span class="hd-gloss">NHẸ — gốc liền một khối, không tách nhỏ hơn được</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một gốc, hai hướng: nhẹ về CÂN NẶNG (<b>лёгкая</b> су́мка túi '
    'nhẹ) và nhẹ về CÔNG SỨC, tức là dễ (<b>лёгкий</b> вопро́с câu hỏi dễ). Cùng gốc có '
    '<b>облегчи́ть</b> «làm nhẹ bớt».</div>'
    '<div class="hd-warn">⚠️ Chữ <b>ё</b> chỉ sống khi CÓ trọng âm. Trọng âm rời đi là '
    'nó thành <b>е</b>: <b>лёгок</b> nhưng <b>легка́</b>, <b>легко́</b>, <b>ле́гче</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>легко́</b> dễ dàng, nhẹ nhàng · <b>ле́гче</b> nhẹ hơn, dễ hơn · '
    '<b>лёгкие</b> phổi (nghĩa đen: «những cái nhẹ», bộ phận nổi được trên nước)</div>'
)
V['лёгкий'] = 'nhẹ, dễ'

S["низкий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">низ-</span>'
    '<span class="hd-gloss">PHÍA DƯỚI, phần đáy (<b>низ</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-ий</span>'
    '<span class="hd-gloss">đuôi dựng tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ <b>низ</b> là «phần dưới»; thêm <b>-к-</b> thành tính từ '
    '«nằm ở phía dưới» = thấp. Dùng cho chiều cao (<b>ни́зкий</b> стол bàn thấp), cho mức '
    'độ (<b>ни́зкая</b> цена́ giá thấp) và cho giọng trầm.</div>'
    '<div class="hd-why">Dạng ngắn: <b>ни́зок</b> (chèn <b>о</b>) · <b>низка́</b> (trọng âm '
    'ra đuôi). So sánh hơn vứt hẳn <b>-к-</b> rồi đổi <b>з→ж</b>: <b>ни́же</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>низ</b> phía dưới · <b>сни́зу</b> từ dưới lên · '
    '<b>пони́зить</b> hạ xuống (giá, giọng)</div>'
)
V['низкий'] = 'thấp, trầm, hèn hạ'

S["громкий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">гром-</span>'
    '<span class="hd-gloss">TIẾNG SẤM (<b>гром</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-ий</span>'
    '<span class="hd-gloss">đuôi dựng tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>гром</b> là tiếng sấm — âm to nhất trời cho. Cái gì to như '
    'sấm thì <b>гро́мкий</b>. Nên từ này chỉ nói về ÂM THANH, không bao giờ nói về kích '
    'thước.</div>'
    '<div class="hd-why">Dạng ngắn: <b>гро́мок</b> (chèn <b>о</b>) · <b>громка́</b> (trọng '
    'âm ra đuôi). So sánh hơn: <b>гро́мче</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гром</b> sấm · <b>гро́мко</b> to tiếng · '
    '<b>гро́мкость</b> âm lượng</div>'
)
V['громкий'] = 'to, vang, ầm ĩ'

# ------------------------------------------------------- kích thước, kích cỡ
S["высокий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">выс-</span>'
    '<span class="hd-gloss">CAO</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ок-ий</span>'
    '<span class="hd-gloss">đuôi dựng tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>выс-</b> đẻ ra <b>высота́</b> «chiều cao» và <b>вы́сший</b> '
    '«cao nhất». Nghĩa lõi là cái ĐO ĐƯỢC theo chiều cao hoặc theo mức: <b>высо́кий</b> дом '
    'nhà cao, <b>высо́кая</b> температу́ра sốt cao.</div>'
    '<div class="hd-warn">⚠️ So sánh hơn vứt hẳn <b>-ок-</b> và kéo trọng âm về đầu từ: '
    '<b>высо́кий</b> → <b>вы́ше</b> (<b>с→ш</b>).</div>'
    '<div class="hd-why">Dạng ngắn không chèn nguyên âm, chỉ chạy trọng âm: <b>высо́к</b> · '
    '<b>высока́</b> · <b>высоки́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>высота́</b> chiều cao, độ cao · <b>вы́сший</b> cao nhất, tối cao · '
    '<b>повы́сить</b> nâng lên, tăng</div>'
)
V['высокий'] = 'cao'

S["короткий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">корот-</span>'
    '<span class="hd-gloss">NGẮN, cụt — gốc của <b>укороти́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-ий</span>'
    '<span class="hd-gloss">đuôi dựng tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ này đo theo CHIỀU DÀI hoặc THỜI GIAN: <b>коро́ткие</b> во́лосы '
    'tóc ngắn, <b>коро́ткий</b> разгово́р cuộc nói chuyện ngắn.</div>'
    '<div class="hd-warn">⚠️ Không dùng cho CHIỀU CAO. Bàn thấp là <b>ни́зкий</b> стол; còn '
    'người thấp phải nói <b>невысо́кий</b> — <b>ни́зкий</b> gán cho người lại thành «hèn hạ, '
    'đê tiện».</div>'
    '<div class="hd-why">Dạng ngắn: <b>коро́ток</b> (chèn <b>о</b>) · <b>коротка́</b>. So sánh '
    'hơn mất <b>-к-</b> và đổi <b>т→ч</b>: <b>коро́че</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>коро́тко</b> ngắn, gọn · <b>коро́че</b> ngắn hơn; «nói gọn lại là…» · '
    '<b>укороти́ть</b> làm ngắn lại</div>'
)
V['короткий'] = 'ngắn'

S["маленький"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мал-</span>'
    '<span class="hd-gloss">NHỎ, ít</span></div>'
    '<div class="hd-row"><span class="hd-piece">-еньк-</span>'
    '<span class="hd-gloss">hậu tố vốn dùng để làm dịu giọng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>мал-</b> cũng là gốc của <b>ма́ло</b> «ít». Hậu tố '
    '<b>-еньк-</b> vốn để làm dịu giọng, nhưng ở từ này sắc thái đó đã mòn hết: '
    '<b>ма́ленький</b> nay là chữ «nhỏ» thông dụng nhất, hoàn toàn trung tính.</div>'
    '<div class="hd-warn">⚠️ Dạng ngắn KHÔNG dựng từ <b>ма́леньк-</b> mà quay về gốc trần: '
    '<b>мал</b> · <b>мала́</b> · <b>мало́</b> · <b>малы́</b>. So sánh hơn cũng là từ khác '
    'hẳn: <b>ме́ньше</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ма́ло</b> ít · <b>ме́ньше</b> nhỏ hơn, ít hơn · '
    '<b>уме́ньшить</b> làm giảm bớt</div>'
)
V['маленький'] = 'nhỏ, bé'

S["средний"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сред-</span>'
    '<span class="hd-gloss">PHẦN GIỮA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ий</span>'
    '<span class="hd-gloss">thuộc về</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc với <b>середи́на</b> «chính giữa» và <b>среда́</b> «thứ Tư» '
    '— ngày nằm giữa tuần làm việc. Từ «ở giữa» ra thẳng nghĩa «trung bình», và ra cả tên '
    'giống thứ ba trong ngữ pháp: <b>сре́дний род</b> giống trung, giống đứng giữa đực và '
    'cái.</div>'
    '<div class="hd-warn">📌 <b>в сре́днем</b> = «tính trung bình thì…» — cụm cố định, luôn '
    'ở dạng cách 6.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>середи́на</b> chính giữa · <b>среда́</b> thứ Tư; môi trường · '
    '<b>сре́дство</b> phương tiện, cách thức</div>'
)
V['средний'] = 'ở giữa, trung bình, giống trung'

# ------------------------------------------------- cảm nhận: tiếng, nhiệt, giá
S["тихий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">тих-</span>'
    '<span class="hd-gloss">gốc trơn: LẶNG, ít tiếng động</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa lõi là ÍT TIẾNG ĐỘNG: <b>ти́хий</b> го́лос giọng khẽ, '
    '<b>ти́хая</b> у́лица phố vắng. Từ đó mới nới ra nghĩa «êm ả, không xáo động». Dạng '
    'ngắn không chèn nguyên âm, chỉ chạy trọng âm: <b>тих</b> · <b>тиха́</b>; so sánh hơn '
    'đổi <b>х→ш</b>: <b>ти́ше</b>.</div>'
    '<div class="hd-warn">📌 <b>Ти́хий океа́н</b> = Thái Bình Dương, đúng nghĩa đen «đại '
    'dương lặng sóng». Còn <b>Ти́ше!</b> đứng một mình là «Khẽ thôi!».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ти́хо</b> khẽ, lặng lẽ · <b>тишина́</b> sự yên lặng · '
    '<b>зати́хнуть</b> lặng đi, ngớt dần</div>'
)
V['тихий'] = 'yên tĩnh, khẽ, êm ả'

S["горячий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">гор-</span>'
    '<span class="hd-gloss">CHÁY — gốc của <b>горе́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-яч-ий</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái gì còn giữ hơi lửa thì <b>горя́чий</b>: <b>горя́чий</b> чай, '
    '<b>горя́чая</b> вода́. Nghĩa bóng đi thẳng từ đó — <b>горя́чий</b> спор cuộc tranh cãi '
    'nảy lửa. Dạng ngắn chạy trọng âm ra đuôi: <b>горя́ч</b> · <b>горяча́</b> · '
    '<b>горячо́</b>.</div>'
    '<div class="hd-warn">⚠️ <b>горя́чий</b> là nóng KHI CHẠM VÀO (đồ ăn, nước, bếp). Trời '
    'nóng thì phải nói <b>жа́рко</b>, không dùng từ này.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>горе́ть</b> cháy · <b>горячо́</b> nóng bỏng; sôi nổi · '
    '<b>загора́ть</b> phơi nắng cho rám da</div>'
)
V['горячий'] = 'nóng, nồng nhiệt, nóng tính'

S["хороший"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">хорош-</span>'
    '<span class="hd-gloss">gốc trơn: TỐT — không chẻ nhỏ hơn được</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không có mảnh nào mang nghĩa riêng để bám vào, phải thuộc thẳng. '
    'Bù lại nó đẻ ra <b>хорошо́</b> — tiếng «tốt / được / ổn» người Nga nói suốt ngày, và '
    'chính là dạng ngắn giống trung của từ này.</div>'
    '<div class="hd-warn">⚠️ So sánh hơn KHÔNG dựng từ <b>хорош-</b> mà thay hẳn gốc: '
    '<b>лу́чше</b> «tốt hơn» (đúng kiểu <i>good → better</i>).</div>'
    '<div class="hd-warn">📌 <b>Всего́ хоро́шего!</b> = «Chúc mọi sự tốt lành!» — câu chào '
    'lúc chia tay, để nguyên cách 2.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>хорошо́</b> tốt, được, ổn · <b>лу́чше</b> tốt hơn · '
    '<b>хороше́ть</b> đẹp ra, tươi ra</div>'
)
V['хороший'] = 'tốt, giỏi, khá, hay'

S["настоящий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">tại, ngay trên</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сто-</span>'
    '<span class="hd-gloss">ĐỨNG — gốc của <b>стоя́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ящ-ий</span>'
    '<span class="hd-gloss">đuôi «đang…», kiểu phân từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen là «đang đứng ngay đây», và hai nghĩa mọc thẳng ra từ '
    'đó: cái đang có mặt LÚC NÀY (<b>настоя́щее вре́мя</b> thì hiện tại) và cái CÓ THẬT, '
    'không phải đồ giả (<b>настоя́щий</b> друг bạn thật sự).</div>'
    '<div class="hd-warn">📌 <b>в настоя́щее вре́мя</b> / <b>в настоя́щий моме́нт</b> = '
    '«hiện nay, ngay lúc này» — giọng văn viết, trang trọng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>стоя́ть</b> đứng · <b>настоя́щее вре́мя</b> thì hiện tại · '
    '<b>постоя́нный</b> thường xuyên, liên tục</div>'
)
V['настоящий'] = 'thật, đích thực, hiện tại'

# ---------------------------------------- đuôi -о́й có trọng âm: giá, tuổi, nết
S["дорогой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дорог-</span>'
    '<span class="hd-gloss">CÓ GIÁ TRỊ CAO</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́й</span>'
    '<span class="hd-gloss">đuôi tính từ, tự mang trọng âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một gốc, hai loại «giá»: giá tiền cao (<b>дорого́й</b> пода́рок '
    'món quà đắt) và giá tình cảm cao (<b>дорого́й</b> друг bạn thân yêu) — y hệt chữ '
    '<i>dear</i> tiếng Anh vừa là «đắt» vừa là «thân mến» ở đầu thư.</div>'
    '<div class="hd-warn">⚠️ Đừng nhầm với <b>доро́га</b> (con đường): hai từ khác hẳn '
    'nhau, chỉ tình cờ giống mặt chữ.</div>'
    '<div class="hd-why">Dạng dài để trọng âm ở đuôi, nhưng dạng ngắn kéo nó về đầu: '
    '<b>до́рог</b> · <b>до́рого</b> · <b>до́роги</b>. Riêng giống cái <b>дорога́</b> vẫn ra '
    'đuôi — viết y hệt <b>доро́га</b> «con đường», chỉ khác chỗ trọng âm. So sánh hơn '
    '<b>доро́же</b> (<b>г→ж</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>до́рого</b> đắt (trạng từ) · <b>доро́же</b> đắt hơn · '
    '<b>дорожа́ть</b> lên giá</div>'
)
V['дорогой'] = 'đắt, đắt tiền, quý giá, thân mến'

S["молодой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">молод-</span>'
    '<span class="hd-gloss">TRẺ, non</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́й</span>'
    '<span class="hd-gloss">đuôi tính từ, tự mang trọng âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>молод-</b> có một bản song sinh kiểu Slav cổ là '
    '<b>млад-</b>, nên «em, ít tuổi hơn» lại là <b>мла́дший</b>. Cùng ổ còn '
    '<b>молоде́ц</b> — lời khen «giỏi lắm!», nghĩa gốc là «chàng trai cừ».</div>'
    '<div class="hd-why">Dạng ngắn kéo trọng âm về đầu: <b>мо́лод</b> · <b>мо́лодо</b> · '
    '<b>мо́лоды</b> (riêng giống cái <b>молода́</b> ra đuôi). So sánh hơn <b>моло́же</b> '
    '(<b>д→ж</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мо́лодость</b> tuổi trẻ · <b>молоде́ц</b> giỏi lắm! · '
    '<b>мла́дший</b> em, ít tuổi hơn</div>'
)
V["молодой"] = "trẻ, ít tuổi"

S["злой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">зл-</span>'
    '<span class="hd-gloss">CÁI ÁC, điều xấu (<b>зло</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ой</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ <b>зло</b> là «cái ác», nên <b>злой</b> đúng nghĩa là '
    '«mang cái ác trong người». Nhưng đời thường nó hay chỉ có nghĩa nhẹ hơn nhiều: '
    'đang cáu — <b>он сего́дня злой</b> hôm nay ông ấy đang quạu.</div>'
    '<div class="hd-why">Gốc <b>зл-</b> trơ trọi không đứng cuối từ được, nên dạng ngắn '
    'giống đực phải chèn <b>о</b>: <b>зол</b> (<b>я зол</b> = tôi đang giận). Các dạng còn '
    'lại vẫn trần: <b>зла</b> · <b>зло</b> · <b>злы</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>зло</b> điều ác · <b>зло́сть</b> cơn tức giận · '
    '<b>зли́ться</b> nổi cáu, bực mình</div>'
)
V['злой'] = 'hung dữ, độc ác, đang cáu giận'

S["плохой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">плох-</span>'
    '<span class="hd-gloss">gốc trơn: TỒI, kém</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́й</span>'
    '<span class="hd-gloss">đuôi tính từ, tự mang trọng âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là từ trái nghĩa của <b>хоро́ший</b> trong lô này, và cả hai '
    'đều «trái tính» y như nhau: so sánh hơn của <b>плохо́й</b> cũng không dựng từ gốc của '
    'nó mà mượn hẳn từ khác — <b>ху́же</b>.</div>'
    '<div class="hd-warn">⚠️ Từ này chê CHẤT LƯỢNG (<b>плоха́я</b> пого́да thời tiết xấu, '
    '<b>плохо́й</b> врач bác sĩ tồi), không dùng để chê ngoại hình.</div>'
    '<div class="hd-why">Dạng ngắn: <b>плох</b> · <b>плоха́</b> · <b>пло́хо</b>. Dạng giống '
    'trung <b>пло́хо</b> chính là chữ trong câu <b>мне пло́хо</b> «tôi thấy khó chịu, '
    'trong người không ổn».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пло́хо</b> tệ, không tốt · <b>ху́же</b> tệ hơn · '
    '<b>ху́дший</b> tệ nhất</div>'
)
V['плохой'] = 'tồi, kém, dở, xấu'

# ------------------------------------------------------------ cặp -ский: nam/nữ
S["женский"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">жен-</span>'
    '<span class="hd-gloss">PHỤ NỮ; vợ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ск-</span>'
    '<span class="hd-gloss">thuộc về</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng khuôn <b>-ский</b> «thuộc về» đã gặp ở tên nước '
    '(<b>ру́сский</b>). Gốc <b>жен-</b> cho <b>жена́</b> «vợ» và <b>же́нщина</b> «phụ nữ», '
    'nên <b>же́нский</b> = thuộc về phái nữ: <b>же́нская о́бувь</b> giày nữ, '
    '<b>же́нский род</b> giống cái trong ngữ pháp.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>жена́</b> vợ · <b>же́нщина</b> phụ nữ · '
    '<b>жени́ться</b> cưới vợ (chỉ nói về đàn ông) · <b>мужско́й</b> nam (từ đối lập)</div>'
)

S["мужской"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">муж-</span>'
    '<span class="hd-gloss">ĐÀN ÔNG; chồng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ск-</span>'
    '<span class="hd-gloss">thuộc về</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́й</span>'
    '<span class="hd-gloss">đuôi tính từ, tự mang trọng âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng một khuôn với <b>же́нский</b>, chỉ đổi gốc. <b>муж-</b> vừa '
    'là «chồng» (<b>муж</b>) vừa là «đàn ông» (<b>мужчи́на</b>), nên <b>мужско́й</b> = dành '
    'cho nam: <b>мужска́я руба́шка</b> áo sơ mi nam, <b>мужско́й род</b> giống đực.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>муж</b> chồng · <b>мужчи́на</b> đàn ông · '
    '<b>му́жество</b> lòng dũng cảm</div>'
)
