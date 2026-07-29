# -*- coding: utf-8 -*-
"""k48 — tu-moi: 20 từ user vừa thêm, KHÔNG cùng một họ. Mỗi thẻ đứng một mình
(README §2b, §3): không có khối hệ thống dùng chung, tối đa 2 ô đỏ, nhắm dưới
một màn hình iPhone. Hai cụm nhỏ có liên hệ khi tiện tay: bộ đuôi -гда
(всегда́ · иногда́, kèm когда́/тогда́/никогда́) và thang tần suất đặt gọn ở ре́дко."""

# 🔴 KHÔNG dựng biến khối dùng chung rồi cộng vào mọi thẻ — xem README §3.

S = {}
V = {}

S["бассейн"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — từ mượn nguyên khối từ tiếng Pháp '
    '<i>bassin</i> (cái chậu, cái bồn), cùng nguồn với tiếng Anh <i>basin</i>. '
    'Trong tiếng Nga nó giữ cả hai nghĩa của bản gốc: <b>bồn nước lớn</b> (bể bơi) '
    'và <b>vùng trũng chứa nước</b> — <i>бассе́йн реки́</i> = lưu vực sông.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giống nhiều từ mượn Pháp, trọng âm rơi vào âm cuối và '
    'đứng yên ở mọi cách: <b>бассе́йн</b>. Danh từ giống đực đuôi phụ âm, biến cách '
    'đều tăm tắp nên không có gì phải nhớ thêm.</div>'
    '<div class="hd-warn"><b>Hai cách, hai việc:</b> đi tới bể bơi thì '
    '<i>ходи́ть <b>в бассе́йн</b></i> (cách 4 — có chuyển động); còn đang ở đó thì '
    '<i>пла́вать <b>в бассе́йне</b></i> (cách 6 — đứng yên một chỗ).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">Không có họ hàng gốc Nga — từ mượn đứng một mình. Chỗ bắc cầu '
    'duy nhất là tiếng Anh <i>basin</i>, cùng một từ gốc Pháp.</div>'
)

S["болеть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бол-</span>'
    '<span class="hd-gloss">ĐAU — chính là danh từ <b>боль</b> (cơn đau)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-еть</span>'
    '<span class="hd-gloss">đuôi nguyên thể; thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cứ thấy <b>бол-</b> là thấy chuyện đau ốm — cả nhà thương, '
    'người bệnh, cơn bệnh đều mọc ra từ mảnh này.</div>'
    '<div class="hd-warn"><b>Một từ nhưng HAI cách chia, đừng trộn:</b><br>'
    '① <b>người</b> ốm → chia đủ sáu ngôi: <i>я боле́ю</i> = tôi đang ốm.<br>'
    '② <b>bộ phận cơ thể</b> đau → chỉ có ngôi thứ ba, và chính chỗ đau làm chủ ngữ: '
    '<i>у меня́ боли́т голова́</i> = tôi đau đầu (nghĩa đen: cái đầu nó đau).</div>'
    '<div class="hd-warn"><b>Nghĩa thứ ba, rất hay gặp:</b> <b>боле́ть за</b> + cách 4 '
    '= cổ vũ cho (đội bóng) — "đau cùng đội". Từ đó ra <b>боле́льщик</b> = cổ động viên.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>боль</b> cơn đau · <b>больно́й</b> ốm; người bệnh · '
    '<b>больни́ца</b> bệnh viện · <b>боле́знь</b> căn bệnh · <b>бо́льно</b> đau (thấy đau)</div>'
)

S["весь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Đại từ gốc trơn, không chẻ được. Nó đi kèm danh từ và '
    'đổi đuôi theo giống/số/cách như một tính từ: <i>весь день</i> cả ngày · '
    '<i>вся семья́</i> cả nhà · <i>всё вре́мя</i> suốt thời gian.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>весь</b> gom mọi thứ lại thành MỘT KHỐI nguyên vẹn — '
    'khác hẳn <b>ка́ждый</b> là xét từng cái riêng lẻ. <i>Весь класс</i> = cả lớp '
    '(một khối) ↔ <i>ка́ждый учени́к</i> = từng học sinh một.</div>'
    '<div class="hd-warn"><b>Bẫy ё/е đổi hẳn nghĩa:</b> <b>всё</b> (giống trung) = '
    'mọi <b>THỨ</b> — <i>всё хорошо́</i> = mọi sự đều ổn. Còn <b>все</b> (số nhiều) = '
    'mọi <b>NGƯỜI</b> — <i>все здесь</i> = mọi người đều ở đây. Viết sai một dấu chấm '
    'là đổi sang câu khác.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>всегда́</b> luôn luôn · <b>вся́кий</b> bất kỳ, mọi loại · '
    '<b>всеми́рный</b> toàn thế giới · <b>всё равно́</b> dù sao cũng thế</div>'
)

S["всегда"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">все-</span>'
    '<span class="hd-gloss">TOÀN BỘ — chính là <b>весь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-гда</span>'
    '<span class="hd-gloss">mảnh chỉ THỜI ĐIỂM (nằm trong <b>когда́</b>, <b>тогда́</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen là "vào TOÀN BỘ mọi lúc" = luôn luôn. Mảnh '
    '<b>-гда</b> khoá lại một họ nhỏ đóng kín, thuộc một lượt là xong cả bộ: '
    '<b>когда́</b> khi nào · <b>тогда́</b> khi đó · <b>иногда́</b> đôi khi · '
    '<b>никогда́</b> không bao giờ.</div>'
    '<div class="hd-warn"><b>Vị trí trong câu thoải mái</b> — đứng trước động từ là '
    'chỗ tự nhiên nhất: <i>Я <b>всегда́</b> встаю́ ра́но</i> = tôi luôn dậy sớm. Đưa lên '
    'đầu câu cũng đúng, chỉ là nhấn mạnh hơn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>весь</b> toàn bộ · <b>когда́</b> khi nào · '
    '<b>тогда́</b> khi đó · <b>иногда́</b> đôi khi · <b>никогда́</b> không bao giờ</div>'
)

S["встретиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">встре́т-</span>'
    '<span class="hd-gloss">GẶP — chính là danh từ <b>встре́ча</b> (cuộc gặp)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">phản thân, ở đây mang nghĩa LẪN NHAU</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính mảnh <b>-ся</b> biến "gặp ai đó" thành "gặp NHAU" — '
    'nên bên kia không còn là tân ngữ nữa mà thành người cùng làm, đi với '
    '<b>с</b> + cách 5. Chia thì ngôi "tôi" biến âm <b>т→ч</b>: <b>встре́чусь</b>, '
    'các ngôi còn lại giữ nguyên <b>т</b>.</div>'
    '<div class="hd-warn"><b>Chọn đúng cái cần dùng:</b> '
    '<b>встре́тить</b> + cách 4 = gặp/đón ai (một phía chủ động — <i>встре́тить друга́ '
    'в аэропорту́</i>) ↔ <b>встре́титься</b> <b>с</b> + cách 5 = hẹn gặp nhau (hai phía).</div>'
    '<div class="hd-warn"><b>Thể:</b> <b>встре́титься</b> là HOÀN THÀNH (một cuộc gặp, '
    'xong việc); muốn nói "vẫn hay gặp nhau" thì dùng <b>встреча́ться</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>встре́ча</b> cuộc gặp · <b>встреча́ться</b> gặp nhau (chưa HT) · '
    '<b>встре́тить</b> gặp, đón ai · <b>навстре́чу</b> đi ngược lại phía ai</div>'
)

S["для"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Giới từ gốc trơn, không chẻ được và cũng không đẻ ra từ '
    'phái sinh nào. Thứ phải thuộc ở đây không phải cấu tạo mà là <b>cách nó đòi</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>для</b> luôn kéo theo <b>cách 2</b>, không có ngoại lệ, và '
    'nghĩa lõi là <b>VÌ LỢI ÍCH CỦA</b> ai/cái gì: <i>пода́рок <b>для</b> ма́мы</i> = quà '
    'cho mẹ · <i><b>для</b> меня́</i> cho tôi · <i><b>для</b> чего́?</i> để làm gì?</div>'
    '<div class="hd-warn"><b>Lỗi kinh điển của người mới:</b> "để làm gì đó" KHÔNG dùng '
    '<b>для</b> + động từ. Sau <b>для</b> chỉ được đứng danh từ; muốn nối một hành động '
    'thì phải dùng <b>что́бы</b>: <i>Я чита́ю, <b>что́бы</b> учи́ть слова́</i> = tôi đọc để '
    'học từ (không nói <i>для чита́ть</i>).</div>'
    '<div class="hd-warn"><b>Đừng lẫn với за:</b> <b>для</b> + cách 2 = vì lợi ích ai '
    '(<i>для тебя́</i> — dành cho bạn) ↔ <b>за</b> + cách 4 = đổi lấy, trả giá '
    '(<i>за сто рубле́й</i> — với giá 100 rúp).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">Không có — giới từ này không sinh ra từ phái sinh nào. Thứ đáng '
    'gom cùng nó là nhóm giới từ cũng đòi <b>cách 2</b>: <b>у</b> (ở chỗ), <b>от</b> (từ), '
    '<b>до</b> (đến tận), <b>без</b> (không có).</div>'
)

S["ждать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">жд-</span>'
    '<span class="hd-gloss">gốc CHỜ — hiện ra nguyên vẹn khi chia: <b>жду</b>, <b>ждёшь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">đuôi nguyên thể; thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nguyên thể <b>ждать</b> có chữ <b>а</b>, nhưng thân hiện tại '
    'lại là <b>жд-</b> trơn với trọng âm rơi hẳn vào đuôi. Cặp thể: <b>ждать</b> (chưa '
    'hoàn thành) ↔ <b>подожда́ть</b> (chờ một lát, hoàn thành) — câu <i>Подожди́те!</i> '
    '= "chờ chút!" chính là từ này.</div>'
    '<div class="hd-warn"><b>Cách nó đòi — chỗ đắt nhất của từ này, tiếng Nga tách hai:</b><br>'
    '• Chờ người/vật <b>cụ thể, chắc chắn có</b> → <b>cách 4</b>: <i>жду ма́му</i>, '
    '<i>жду авто́бус</i>.<br>'
    '• Chờ điều <b>trừu tượng, chưa chắc tới</b> → <b>cách 2</b>: <i>ждать по́мощи</i> '
    '(chờ sự giúp đỡ), <i>ждать отве́та</i> (chờ hồi âm).</div>'
    '<div class="hd-warn"><b>Quá khứ nhảy trọng âm ở giống cái:</b> <i>ждал</i> · '
    '<i>ждала́</i> · <i>жда́ло</i> · <i>жда́ли</i>. Đây là nết chung của nhóm động từ một '
    'âm tiết, giống <i>был / была́</i> và <i>брал / брала́</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>подожда́ть</b> chờ một lát (HT) · <b>ожида́ть</b> trông đợi · '
    '<b>ожида́ние</b> sự chờ đợi · <b>неожи́данный</b> bất ngờ (không ai chờ)</div>'
)

S["иногда"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ин-о-</span>'
    '<span class="hd-gloss">KHÁC — như <b>ино́й</b> (khác), <b>иностра́нный</b> (nước ngoài)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-гда</span>'
    '<span class="hd-gloss">mảnh chỉ THỜI ĐIỂM (như trong <b>когда́</b>, <b>всегда́</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: "vào những lúc KHÁC" — tức là ngoài lệ thường, '
    'thỉnh thoảng. Ghép <b>ин-</b> (khác) với <b>-гда</b> (lúc) là ra nghĩa, không phải '
    'học thuộc suông.</div>'
    '<div class="hd-warn"><b>Đừng lẫn với ре́дко:</b> <b>иногда́</b> = có lúc có, có lúc '
    'không (không nói ít hay nhiều) ↔ <b>ре́дко</b> = nhấn mạnh rằng <b>ít lần</b>. '
    '<i>Иногда́ я гото́влю до́ма</i> = thỉnh thoảng tôi nấu ăn ↔ <i>Ре́дко</i> = họa hoằn lắm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ино́й</b> khác · <b>иностра́нный</b> nước ngoài · '
    '<b>когда́</b> khi nào · <b>тогда́</b> khi đó · <b>никогда́</b> không bao giờ</div>'
)

S["кататься"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кат-</span>'
    '<span class="hd-gloss">LĂN, cho chạy trên bánh/lưỡi trượt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ся</span>'
    '<span class="hd-gloss">đuôi lớp 1 + phản thân: TỰ lăn đi</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">"Tự lăn đi lòng vòng" — nên nó là đi cho <b>vui</b>, không nhằm '
    'tới đâu cả. Phương tiện luôn đứng sau <b>на</b> + cách 6: '
    '<i><b>на</b> велосипе́де</i> đạp xe · <i><b>на</b> конька́х</i> trượt băng · '
    '<i><b>на</b> лы́жах</i> trượt tuyết · <i><b>на</b> ло́дке</i> chèo thuyền.</div>'
    '<div class="hd-warn"><b>Cặp một chiều / nhiều chiều, y hệt идти́ ↔ ходи́ть:</b> '
    '<b>кати́ться</b> = lăn một mạch về một hướng (<i>мяч ка́тится с горы́</i> — quả bóng '
    'lăn xuống dốc) ↔ <b>ката́ться</b> = đi đi lại lại cho vui.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кати́ться</b> lăn · <b>ката́ние</b> việc đi dạo/trượt · '
    '<b>прока́т</b> dịch vụ cho thuê (xe, ván) · <b>самока́т</b> xe trượt scooter '
    '(nghĩa đen: tự lăn)</div>'
)

S["любить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">люб-</span>'
    '<span class="hd-gloss">YÊU, thấy hợp ý — chính là <b>любо́вь</b> (tình yêu)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-ть</span>'
    '<span class="hd-gloss">đuôi lớp 2: <b>лю́бишь, лю́бит… лю́бят</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cấu trúc thẳng như tiếng Việt: <b>NGƯỜI</b> làm chủ ngữ, cái '
    'được yêu ở cách 4 — <i>Я люблю́ тебя́</i>, <i>Я люблю́ ко́фе</i>. Dùng được cho cả '
    'tình yêu lẫn "khoái, thích lâu dài".</div>'
    '<div class="hd-warn"><b>Ngôi "tôi" chèn thêm л:</b> <b>люблю́</b> (б→бл), rồi trọng '
    'âm lùi về gốc ở các ngôi sau: <b>лю́бишь</b>. Luật chèn <b>л</b> này lặp ở mọi động '
    'từ có thân kết bằng môi <b>б п в ф м</b>: <i>купи́ть → куплю́</i>, '
    '<i>гото́вить → гото́влю</i>.</div>'
    '<div class="hd-warn"><b>люби́ть hay нра́виться?</b> <b>люби́ть</b> = tình cảm bền, '
    'người là chủ ngữ (<i>Я люблю́ тебя́</i> = tỏ tình thật) ↔ <b>нра́виться</b> = thấy '
    'ưng, nhẹ hơn nhiều (<i>Ты мне нра́вишься</i> = tôi thấy mến bạn).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>любо́вь</b> tình yêu · <b>люби́мый</b> yêu quý; ưa thích nhất · '
    '<b>влюби́ться</b> phải lòng · <b>любо́й</b> bất kỳ ai/cái nào · '
    '<b>полюби́ть</b> đâm ra yêu (HT)</div>'
)

S["неделя"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не-</span>'
    '<span class="hd-gloss">KHÔNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дел-</span>'
    '<span class="hd-gloss">LÀM VIỆC — cùng gốc <b>де́ло</b>, <b>де́лать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>ngày KHÔNG LÀM việc</b> — thuở xưa <b>неде́ля</b> '
    'chính là ngày nghỉ, rồi mới lan ra thành cả tuần. Bằng chứng còn nguyên trong tên '
    'thứ Hai: <b>понеде́льник</b> = <i>по + неде́ля</i> = "ngày SAU ngày nghỉ".</div>'
    '<div class="hd-warn"><b>Nói "tuần này" phải dùng на, không dùng в:</b> '
    '<i><b>на</b> э́той неде́ле</i> tuần này · <i><b>на</b> про́шлой неде́ле</i> tuần trước · '
    '<i><b>на</b> сле́дующей неде́ле</i> tuần sau — tất cả ở cách 6. (Trong khi tháng thì '
    'lại là <i><b>в</b> э́том ме́сяце</i>.)</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>понеде́льник</b> thứ Hai · <b>неде́льный</b> hằng tuần · '
    '<b>де́ло</b> việc · <b>де́лать</b> làm</div>'
)

S["нравиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">нрав-</span>'
    '<span class="hd-gloss">TÍNH NẾT, ý thích — danh từ <b>нрав</b> = tính khí</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-ся</span>'
    '<span class="hd-gloss">lớp 2 + phản thân; ngôi "tôi" chèn л: <b>нра́влюсь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen là "hợp với tính ý của ai" — nên câu Nga đảo ngược so '
    'với tiếng Việt: <i>Мне нра́вится э́та кни́га</i> = "với tôi, quyển sách này làm vừa '
    'lòng". Dịch thô ra tiếng Anh cho dễ nắm: <i>it pleases me</i>.</div>'
    '<div class="hd-warn"><b>Ai thích thì KHÔNG phải chủ ngữ — đây là chỗ sai kinh điển:</b><br>'
    'Người thích đứng ở <b>cách 3</b> (<i>мне, тебе́, ему́</i>), còn <b>cái được thích mới '
    'là chủ ngữ</b> và động từ chia theo nó: <i>Мне нра́вится фильм</i> (số ít) ↔ '
    '<i>Мне нра́вятся фи́льмы</i> (số nhiều).</div>'
    '<div class="hd-warn"><b>Thể hoàn thành понра́виться = ưng ngay lần đầu:</b> '
    '<i>Мне понра́вился э́тот фильм</i> = tôi (xem rồi và) thấy thích bộ phim đó.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>нрав</b> tính khí · <b>понра́виться</b> đâm ra ưng (HT) · '
    '<b>нра́вственный</b> thuộc về đạo đức</div>'
)

S["помнить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố dính chết, ở đây KHÔNG thêm nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мн-</span>'
    '<span class="hd-gloss">gốc GIỮ TRONG ĐẦU — cũng nằm trong <b>па́мять</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi lớp 2, trọng âm đứng yên ở <b>по́-</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhận ra gốc <b>-мн-</b> là mở luôn được <b>па́мять</b> (trí nhớ) '
    'và <b>па́мятник</b> (đài tưởng niệm — vật giữ ký ức).</div>'
    '<div class="hd-warn"><b>Đây là TRẠNG THÁI, không phải hành động</b> — nên nó không '
    'có thể hoàn thành đi kèm. Muốn nói "chợt nhớ ra" thì phải đổi hẳn từ: '
    '<b>по́мнить</b> = vẫn còn nhớ (kéo dài) ↔ <b>вспо́мнить</b> = nhớ ra (một khoảnh '
    'khắc) ↔ <b>запо́мнить</b> = ghi vào đầu để nhớ về sau.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>па́мять</b> trí nhớ · <b>па́мятник</b> đài tưởng niệm · '
    '<b>вспо́мнить</b> nhớ ra (HT) · <b>запо́мнить</b> ghi nhớ (HT) · '
    '<b>напо́мнить</b> nhắc ai nhớ (HT)</div>'
)

S["портрет"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được trong tiếng Nga — mượn nguyên khối từ tiếng Pháp '
    '<i>portrait</i>, chính là chữ <i>portrait</i> của tiếng Anh. Gốc xa hơn là Latin '
    '<i>pro-trahere</i> = "kéo nét ra", tức vẽ lại khuôn mặt ai đó lên mặt giấy.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ mượn Pháp vào tiếng Nga gần như luôn giữ trọng âm ở âm cuối, '
    'và giữ nguyên chỗ đó khi biến cách: <b>портре́т</b> — cùng nhịp với <b>биле́т</b> (vé), '
    '<b>буке́т</b> (bó hoa), <b>паке́т</b> (gói, túi).</div>'
    '<div class="hd-warn"><b>Chân dung CỦA ai thì để cách 2:</b> <i>портре́т ма́мы</i> = '
    'bức chân dung mẹ · <i>портре́т худо́жника</i> = chân dung người hoạ sĩ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>портре́тный</b> thuộc về chân dung · <b>портрети́ст</b> hoạ sĩ '
    'vẽ chân dung · <b>автопортре́т</b> chân dung tự hoạ</div>'
)

S["регулярно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">регуля́рн-</span>'
    '<span class="hd-gloss">tính từ <b>регуля́рный</b> = đều đặn, có quy luật</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi biến tính từ thành TRẠNG TỪ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Lõi là Latin <i>regula</i> = cây thước, quy tắc — đúng chữ '
    '<i>regular</i> của tiếng Anh. Làm việc gì <b>регуля́рно</b> là làm "đúng theo thước", '
    'tức lặp lại <b>đều theo chu kỳ</b>.</div>'
    '<div class="hd-warn"><b>Không đồng nghĩa với ча́сто:</b> <b>ча́сто</b> = nhiều lần '
    '(chẳng cần đều) ↔ <b>регуля́рно</b> = đúng nhịp, đúng lịch. <i>Я ча́сто пью ко́фе</i> '
    '(uống nhiều) ↔ <i>Я регуля́рно хожу́ в спортза́л</i> (tuần nào cũng đi).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>регуля́рный</b> đều đặn · <b>регули́ровать</b> điều chỉnh, '
    'điều tiết · <b>нерегуля́рный</b> thất thường</div>'
)

S["редко"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ре́дк-</span>'
    '<span class="hd-gloss">tính từ <b>ре́дкий</b> = thưa, hiếm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi biến tính từ thành TRẠNG TỪ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc của <b>ре́дкий</b> là thưa trong <b>không gian</b> '
    '(<i>ре́дкий лес</i> = rừng thưa, cây cách xa nhau). Đem cái "thưa" đó áp vào '
    '<b>thời gian</b> thì thành thưa thớt về số lần = hiếm khi.</div>'
    '<div class="hd-warn"><b>Thang tần suất — học một lượt là xong cả nhóm:</b><br>'
    '<b>всегда́</b> luôn luôn → <b>ча́сто</b> hay, nhiều lần → <b>иногда́</b> thỉnh thoảng '
    '→ <b>ре́дко</b> hiếm khi → <b>никогда́</b> không bao giờ (nhớ kèm <b>не</b>: '
    '<i>я никогда́ <b>не</b> был там</i>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ре́дкий</b> hiếm; thưa · <b>ре́дкость</b> của hiếm · '
    '<b>и́зредка</b> thảng hoặc, năm thì mười hoạ</div>'
)

S["самый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сам-</span>'
    '<span class="hd-gloss">CHÍNH NÓ, tự thân — cùng thân với <b>сам</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ: đổi theo giống/số/cách của danh từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Việc chính của nó: đặt trước tính từ là ra <b>so sánh nhất</b> — '
    '<i>са́мый большо́й</i> lớn nhất · <i>са́мая краси́вая</i> đẹp nhất · '
    '<i>са́мое лу́чшее</i> tốt nhất. Đây là cách nói bậc nhất dễ nhất, dùng được với '
    'mọi tính từ mà không phải đổi đuôi tính từ.</div>'
    '<div class="hd-warn"><b>са́мый ≠ сам, đừng lẫn:</b> <b>сам / сама́ / са́ми</b> = '
    'TỰ MÌNH (<i>Я сам сде́лал</i> = tôi tự làm lấy) ↔ <b>са́мый</b> = NHẤT, chính là cái '
    'đó. Cùng một thân từ nhưng hai việc khác hẳn.</div>'
    '<div class="hd-warn"><b>Hai cụm phải thuộc:</b> <i>на са́мом де́ле</i> = thật ra, '
    'thực tế là… · <i>тот же са́мый</i> = đúng cái đó, y hệt cái đó.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сам</b> tự mình · <b>самолёт</b> máy bay (tự bay) · '
    '<b>самова́р</b> ấm samovar (tự đun) · <b>самостоя́тельный</b> tự lập</div>'
)

S["слышать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">слыш-</span>'
    '<span class="hd-gloss">NGHE — biến thể của gốc <b>слух</b> (thính giác)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">đuôi nguyên thể — nhưng chia theo LỚP 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhận ra gốc <b>слух</b> là nắm luôn cả cụm: '
    '<b>слух</b> = thính giác, và cũng là <b>tin đồn</b> (thứ chỉ nghe được chứ không '
    'thấy).</div>'
    '<div class="hd-warn"><b>Cặp dễ lẫn nhất — đúng như hear ↔ listen:</b> '
    '<b>слы́шать</b> = nghe THẤY, âm tự lọt vào tai (<i>Я слы́шу шум</i> = tôi nghe thấy '
    'tiếng ồn) ↔ <b>слу́шать</b> = LẮNG nghe, có chủ ý (<i>Я слу́шаю му́зыку</i> = tôi '
    'đang nghe nhạc).</div>'
    '<div class="hd-warn"><b>Đuôi -ать nhưng chia LỚP 2:</b> <b>слы́шу, слы́шишь… '
    'слы́шат</b> — không phải <i>слыша́ю</i>. Cùng nhóm ngoại lệ với <b>держа́ть</b>, '
    '<b>дыша́ть</b>, <b>гнать</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>слух</b> thính giác; tin đồn · <b>слу́шать</b> lắng nghe · '
    '<b>слы́шно</b> nghe được, nghe rõ · <b>услы́шать</b> nghe thấy (HT) · '
    '<b>слу́шатель</b> thính giả</div>'
)

S["тот"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Đại từ chỉ định gốc trơn, không chẻ được. Nó đổi đuôi theo '
    'giống/số/cách của danh từ đi kèm, y như một tính từ.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Học theo cặp đối lập thì không bao giờ nhầm: <b>э́тот</b> = cái '
    'NÀY, ở gần, trước mặt ↔ <b>тот</b> = cái KIA, ở xa hơn, hoặc cái vừa được nhắc tới '
    'trong câu chuyện. <i>Не э́та кни́га, а та</i> = không phải quyển này, mà quyển kia.</div>'
    '<div class="hd-warn"><b>то, что… — bộ nối câu dùng hằng ngày:</b> nó là "điều mà", '
    'và phần <b>то</b> mới là chỗ mang cách do động từ đòi: <i>Я ду́маю о том, что…</i> = '
    'tôi nghĩ về điều mà… (<b>о</b> + cách 6 nên <b>то</b> thành <b>том</b>).</div>'
    '<div class="hd-warn"><b>Hai cụm phải thuộc:</b> <i>с тех пор</i> = từ dạo đó, kể từ '
    'khi ấy · <i>тот же</i> = vẫn cái đó, cùng một cái.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тогда́</b> khi đó · <b>пото́м</b> sau đó · <b>то́же</b> cũng · '
    '<b>тако́й</b> như thế, loại như vậy</div>'
)

S["устать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố làm nên thể HOÀN THÀNH (đi tới hết mức)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ста-ть</span>'
    '<span class="hd-gloss">cùng thân với <b>стать</b> (trở nên) — kéo theo cả kiểu chia</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhìn nguyên thể <b>уста́ть</b> không đoán ra được chữ <b>н</b> ở '
    'thì tương lai — nhưng nếu nhớ nó đi cùng thân với <b>стать</b> thì có ngay: '
    '<b>ста́ну</b> → <b>уста́ну</b>, <b>ста́нешь</b> → <b>уста́нешь</b>. Cặp thể: '
    '<b>уста́ть</b> (HT) ↔ <b>устава́ть</b> (chưa HT, mệt dần).</div>'
    '<div class="hd-warn"><b>"Tôi mệt" nói bằng thì QUÁ KHỨ</b> — vì đây là thể hoàn '
    'thành, nghĩa của nó là "đã đi tới chỗ mệt": <i>Я уста́л</i> (nam) / <i>Я уста́ла</i> '
    '(nữ) = tôi mệt rồi. Nói <i>я устаю́</i> là "tôi đang mệt dần", nghĩa khác.</div>'
    '<div class="hd-warn"><b>Mệt VÌ cái gì thì dùng от + cách 2:</b> '
    '<i>Я уста́л <b>от</b> рабо́ты</i> = tôi mệt vì công việc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уста́лый</b> mệt mỏi (dáng vẻ) · <b>уста́лость</b> sự mệt mỏi · '
    '<b>устава́ть</b> mệt dần (chưa HT)</div>'
)

# ----------------------------------------------------------- field Vietnamese
# Đề bài của deck 1-go: user nhìn dòng này rồi GÕ từ Nga. Chỉ sửa từ nào mơ hồ.
# Không ghi từ loại (badge đã có) — TRỪ từ có PoS = oth: для, всегда́, иногда́.

V["болеть"]      = "bị ốm; (bộ phận cơ thể) bị đau nhức; cổ vũ cho đội nào (chưa hoàn thành)"
V["весь"]        = "toàn bộ, cả (nguyên một khối — không phải \"mỗi/từng cái\")"
V["всегда"]      = "trạng từ: luôn luôn, lúc nào cũng vậy (100% số lần)"
V["встретиться"] = "gặp nhau, hẹn gặp (HOÀN THÀNH — phản thân -ся, đi với с + cách 5)"
V["для"]         = "giới từ, đi với cách 2: cho, dành cho (vì lợi ích của ai/việc gì)"
V["ждать"]       = "đợi, chờ, trông đợi (chưa hoàn thành — không tiền tố)"
V["иногда"]      = "trạng từ: thỉnh thoảng, đôi khi (lúc có lúc không)"
V["кататься"]    = "đi lòng vòng cho vui bằng xe/thuyền, trượt băng, trượt tuyết (chưa hoàn thành, phản thân -ся)"
V["любить"]      = "yêu; thích lâu dài (chưa hoàn thành — NGƯỜI làm chủ ngữ: я люблю́ + cách 4)"
V["нравиться"]   = "làm cho ai thấy ưng, hợp ý (chưa hoàn thành — VẬT làm chủ ngữ: мне нра́вится…)"
V["помнить"]     = "nhớ, vẫn còn giữ trong đầu (chưa hoàn thành — trạng thái, không có thể hoàn thành)"
V["регулярно"]   = "đều đặn, lặp lại đúng nhịp theo lịch (không phải \"nhiều lần\" nói chung)"
V["редко"]       = "hiếm khi, ít khi (ít lần hơn hẳn \"thỉnh thoảng\")"
V["самый"]       = "…nhất (đặt trước tính từ để tạo bậc nhất); chính là cái đó — không phải \"tự mình\""
V["слышать"]     = "nghe thấy, âm lọt vào tai (chưa hoàn thành — không chủ ý, không phải \"lắng nghe\")"
V["тот"]         = "cái kia, cái đó (ở xa hoặc đã nhắc tới — đối lập với э́тот \"cái này\")"
V["устать"]      = "mệt, đuối sức (HOÀN THÀNH — я уста́л = tôi mệt rồi)"
