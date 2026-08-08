# -*- coding: utf-8 -*-
"""k58 — nature-plants: tên topic chỉ là nhãn xếp kho, bên trong KHÔNG đồng nhất.

Có bốn nhóm rời nhau: danh từ thiên nhiên (земля, лес, лён, море, поле, цвет,
ветер, мышь, слеза), ba tên người làm nghề/ngành (переводчик, учёный, физик),
ba trạng từ – hư từ thời gian và cách thức (вечером, позавчера, вслух), ba tính
từ (выходной, американский, множественный). Mỗi thẻ soạn độc lập, KHÔNG ép trục
chung. Trục nhỏ duy nhất được phép nhắc chéo: hiện tượng "cách 6 thứ hai"
(в лесу́ ↔ о ле́се, на ветру́ ↔ о ве́тре) nói đủ ở thẻ лес, thẻ ветер dẫn chiếu.
"""

# 🔴 KHÔNG dựng biến khối dùng chung (HE/LUAT/THE…) rồi cộng vào mọi thẻ.
# Đó là cách cũ, đã bỏ 28/07 — xem README §3.

S = {}
V = {}

# --------------------------------------------------- người làm nghề / làm ngành
S["переводчик"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пере-</span>'
    '<span class="hd-gloss">QUA, từ bên này sang bên kia</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вод-</span>'
    '<span class="hd-gloss">gốc DẪN, đưa đi (của <b>води́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-чик</span>'
    '<span class="hd-gloss">đuôi chỉ NGƯỜI làm nghề đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: người <i>dẫn</i> ý nghĩa <i>qua</i> phía bên kia — '
    'đúng việc của người dịch. Đuôi <b>-чик</b> mở khoá cả một lớp tên nghề: '
    '<b>лётчик</b> phi công, <b>разве́дчик</b> trinh sát viên.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>переводи́ть</b> dịch, chuyển · <b>перево́д</b> bản dịch, '
    'khoản chuyển tiền · <b>води́ть</b> dẫn, lái xe</div>'
)

S["учёный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">уч-</span>'
    '<span class="hd-gloss">gốc HỌC / DẠY (của <b>учи́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ённ-</span>'
    '<span class="hd-gloss">đuôi phân từ bị động: "đã ĐƯỢC dạy"</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen "người đã được dạy" → có học → nhà khoa học. '
    'Badge trên thẻ ghi <i>adj</i> là đúng: từ này vẫn chia y hệt tính từ '
    '(<b>учёного</b>, <b>учёному</b>) nhưng đứng một mình đã đủ nghĩa là NGƯỜI — '
    'gọi là tính từ danh-từ-hoá.</div>'
    '<div class="hd-warn">⚠️ Chữ <b>ё</b> luôn tự mang trọng âm, nên bảng chia của từ '
    'này không có dấu nhọn nào: cứ thấy <b>ё</b> là đọc nhấn ở đó.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>учи́ть</b> học, dạy · <b>учи́тель</b> thầy giáo · '
    '<b>учёба</b> việc học · <b>уче́бник</b> sách giáo khoa</div>'
)

S["физик"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">физ-</span>'
    '<span class="hd-gloss">Hy Lạp <i>physis</i> — TỰ NHIÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ик</span>'
    '<span class="hd-gloss">đuôi chỉ NGƯỜI làm ngành đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp đuôi phải thuộc: <b>-ик</b> là NGƯỜI, <b>-ика</b> là NGÀNH — '
    '<b>фи́зик</b> nhà vật lý ↔ <b>фи́зика</b> môn vật lý, và trọng âm đứng yên ở cả hai. '
    'Cùng khuôn: <b>матема́тик</b> ↔ <b>матема́тика</b>. Bảng chia đều tăm tắp, '
    'không có chỗ nào bất thường.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>фи́зика</b> môn vật lý · <b>физи́ческий</b> thuộc về thể chất, '
    'thuộc về vật lý · <b>физкульту́ра</b> thể dục</div>'
)

# ------------------------------------------------------------- thiên nhiên: đất
S["земля"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">земл-</span>'
    '<span class="hd-gloss">gốc ĐẤT</span></div>'
    '<div class="hd-row"><span class="hd-piece">-я</span>'
    '<span class="hd-gloss">đuôi danh từ giống CÁI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một câu gói cả bảng chia: <b>số ít trọng âm nằm ở ĐUÔI</b> '
    '(<b>земли́</b>, <b>земле́</b>) — trừ đúng cách 4 <b>зе́млю</b>; <b>số nhiều nó lùi '
    'lên GỐC</b> (<b>зе́мли</b>, <b>зе́млям</b>) — trừ đúng cách 2 <b>земе́ль</b>, ô này '
    'còn chèn thêm một chữ <b>е</b> vào giữa cụm <i>-мл-</i> cho đọc được.</div>'
    '<div class="hd-warn">⚠️ Viết hoa <b>Земля́</b> là hành tinh Trái Đất; viết thường '
    '<b>земля́</b> là đất, mặt đất.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>земно́й</b> thuộc về trái đất · <b>землетрясе́ние</b> động đất · '
    '<b>земля́к</b> người đồng hương</div>'
)

S["лес"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn một âm tiết, không chẻ được: <b>лес</b> đã là toàn bộ '
    'cái gốc, mọi thứ khác trong họ đều mọc ra từ nó.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hai chỗ lệch của bảng chia, nhớ chung một câu: cách 6 có '
    '<b>HAI dạng</b> — <b>о ле́се</b> khi chỉ NÓI VỀ rừng, còn <b>в лесу́</b> khi ở '
    'BÊN TRONG rừng, lúc đó trọng âm tụt xuống đuôi <i>-у́</i>. Và số nhiều đổi hẳn đuôi '
    'sang <i>-а́</i>: <b>леса́</b> — cùng khuôn với <b>дом → дома́</b>.</div>'
    '<div class="hd-warn">⚠️ Lối <b>в лесу́</b> chỉ đi với <b>в</b> và <b>на</b>. Cùng lớp: '
    '<b>на берегу́</b> trên bờ, <b>в саду́</b> trong vườn, <b>в углу́</b> trong góc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лесно́й</b> thuộc về rừng · <b>лесни́к</b> người gác rừng · '
    '<b>переле́сок</b> rừng thưa nối hai cánh rừng</div>'
)

S["лён"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn một âm tiết, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc Ấn–Âu với tiếng Anh <i>linen</i> (vải lanh) và <i>line</i> '
    '(sợi, đường) — nhìn <i>l–n</i> là nhận ra. Chỗ bất thường của bảng chia: <b>ё '
    'BIẾN MẤT</b> ngay khi thêm đuôi, gốc rút còn <i>льн-</i> và trọng âm dời xuống đuôi: '
    '<b>льна́</b>, <b>льну́</b>, <b>льно́м</b>. Đúng khuôn nguyên âm chạy của '
    '<b>лёд → льда́</b>, <b>пёс → пса́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>льняно́й</b> bằng vải lanh, thuộc về cây lanh</div>'
)

S["море"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мор-</span>'
    '<span class="hd-gloss">gốc BIỂN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е</span>'
    '<span class="hd-gloss">đuôi danh từ giống TRUNG</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc Ấn–Âu với Latin <i>mare</i> → tiếng Anh <i>marine</i>, '
    '<i>maritime</i>. Bảng chia lệch đúng một chỗ: <b>số ít trọng âm đứng yên ở gốc</b> '
    '(<b>мо́ре</b>, <b>мо́ря</b>), nhưng <b>cả số nhiều nhảy hết xuống đuôi</b>: '
    '<b>моря́</b>, <b>море́й</b>, <b>моря́м</b>.</div>'
    '<div class="hd-warn">⚠️ Cặp chỉ khác nhau ở dấu trọng âm: <b>мо́ря</b> = của biển '
    '(cách 2 số ít) ↔ <b>моря́</b> = những biển (số nhiều).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>морско́й</b> thuộc về biển · <b>моря́к</b> thuỷ thủ · '
    '<b>примо́рский</b> ven biển</div>'
)

S["поле"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пол-</span>'
    '<span class="hd-gloss">gốc: khoảng đất BẰNG, trống trải</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е</span>'
    '<span class="hd-gloss">đuôi danh từ giống TRUNG</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chia y hệt <b>мо́ре</b> trong lô này, kể cả chỗ lệch: số ít yên ở '
    'gốc (<b>по́ле</b>, <b>по́ля</b>), số nhiều dồn hết xuống đuôi (<b>поля́</b>, '
    '<b>поле́й</b>). Từ nghĩa gốc "khoảng trống" mà ra nghĩa trừu tượng <i>lĩnh vực</i>: '
    '<b>по́ле де́ятельности</b> lĩnh vực hoạt động.</div>'
    '<div class="hd-warn">⚠️ Riêng số nhiều <b>поля́</b> còn hai nghĩa mà số ít không có: '
    'LỀ trang giấy và VÀNH mũ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поля́на</b> trảng trống giữa rừng · <b>полево́й</b> thuộc về '
    'đồng ruộng, ngoài thực địa</div>'
)

# ------------------------------------------- trạng từ / hư từ: thời gian, cách thức
S["вечером"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ве́чер-</span>'
    '<span class="hd-gloss">danh từ: buổi chiều tối</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ом</span>'
    '<span class="hd-gloss">đuôi CÁCH 5 giống đực, đông cứng lại</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là danh từ <b>ве́чер</b> bị đóng băng ở cách 5 rồi thành hẳn '
    'một trạng từ — không chia nữa. Cả bộ giờ giấc đi cùng một khuôn ấy: <b>у́тром</b> vào '
    'buổi sáng, <b>днём</b> vào ban ngày, <b>но́чью</b> vào ban đêm, <b>зимо́й</b> vào mùa '
    'đông. Cách 5 ở đây trả lời câu hỏi "vào lúc nào".</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ве́чер</b> buổi tối · <b>вече́рний</b> thuộc về buổi tối · '
    '<b>вечери́нка</b> bữa tiệc tối</div>'
)

S["позавчера"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-за-</span>'
    '<span class="hd-gloss">hai tiền tố chồng nhau: lùi thêm MỘT nấc nữa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вчера́</span>'
    '<span class="hd-gloss">hôm qua</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Lấy <b>вчера́</b> hôm qua rồi lùi thêm một ngày = hôm kia. '
    'Chiều ngược lại dựng y hệt: <b>за́втра</b> ngày mai → <b>послеза́втра</b> ngày kia. '
    'Là hư từ nên không chia, không biến hình gì cả.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вчера́</b> hôm qua · <b>вчера́шний</b> của hôm qua · '
    '<b>послеза́втра</b> ngày kia</div>'
)

S["вслух"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">giới từ <b>в</b> VÀO, dính liền vào từ sau</span></div>'
    '<div class="hd-row"><span class="hd-piece">-слух</span>'
    '<span class="hd-gloss">thính giác, cái tai nghe được</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen "đưa VÀO tai" — tức là nói ra cho nghe thấy được, '
    'thành tiếng. Khuôn giới từ dính liền danh từ rồi hoá trạng từ gặp lại nhiều: '
    '<b>вме́сте</b> cùng nhau, <b>вокру́г</b> xung quanh, <b>вниз</b> xuống dưới.</div>'
    '<div class="hd-warn">⚠️ Cặp phải thuộc: <b>чита́ть вслух</b> đọc to lên ↔ '
    '<b>чита́ть про себя́</b> đọc thầm trong đầu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>слух</b> thính giác, tin đồn · <b>слу́шать</b> nghe, lắng nghe · '
    '<b>слы́шать</b> nghe thấy</div>'
)

# ------------------------------------------------------------------- tính từ
S["выходной"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span>'
    '<span class="hd-gloss">tiền tố RA, ra khỏi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ход-</span>'
    '<span class="hd-gloss">gốc ĐI bộ (của <b>ходи́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-но́й</span>'
    '<span class="hd-gloss">đuôi tính từ, trọng âm rơi đúng vào nó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen "thuộc về việc đi RA" → ngày người ta đi ra khỏi chỗ làm '
    '= ngày nghỉ. Từ này đã danh-từ-hoá: nói trống <b>выходно́й</b> là đủ hiểu '
    '<b>выходно́й день</b>, và số nhiều <b>выходны́е</b> chính là hai ngày cuối tuần.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вы́ход</b> lối ra · <b>выходи́ть</b> đi ra · <b>ходи́ть</b> đi lại · '
    '<b>вход</b> lối vào</div>'
)

S["американский"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">америка́н-</span>'
    '<span class="hd-gloss">thân từ của <b>Аме́рика</b> + <i>-ан</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ский</span>'
    '<span class="hd-gloss">đuôi tính từ quan hệ: THUỘC VỀ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trọng âm DỊCH khi thêm đuôi: <b>Аме́рика</b> nhấn ở <i>ме</i>, sang '
    '<b>америка́нский</b> nó chạy sang chữ <i>а</i> của <i>-ан-</i> rồi đứng yên suốt bảng. '
    'Bộ ba cùng khuôn: <b>америка́нец</b> người Mỹ · <b>америка́нка</b> người phụ nữ Mỹ · '
    '<b>америка́нский</b> thuộc về Mỹ.</div>'
    '<div class="hd-warn">⚠️ <b>америка́нские го́рки</b> nghĩa đen là "những ngọn đồi Mỹ" '
    'nhưng dùng để gọi TÀU LƯỢN siêu tốc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>Аме́рика</b> nước Mỹ · <b>америка́нец</b> người Mỹ · '
    '<b>америка́нка</b> người phụ nữ Mỹ</div>'
)

S["множественный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">множ-</span>'
    '<span class="hd-gloss">gốc NHIỀU (của <b>мно́го</b>), г đổi thành ж</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ественн-</span>'
    '<span class="hd-gloss">đuôi dựng tính từ từ danh từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dây chuyền: <b>мно́го</b> nhiều → <b>мно́жество</b> một tập rất nhiều '
    'cái → <b>мно́жественный</b> "gồm nhiều cái", tức là SỐ NHIỀU. Biến âm <i>г→ж</i> là '
    'khuôn quen. Chỗ lệch duy nhất của bảng: <b>dạng ngắn giống đực có hai bản song song</b> — '
    '<b>мно́жествен</b> và bản chèn thêm <i>е</i> cho dễ đọc <b>мно́жественен</b>.</div>'
    '<div class="hd-warn">⚠️ Chỗ user gặp từ này nhiều nhất là thuật ngữ ngữ pháp: '
    '<b>мно́жественное число́</b> = số nhiều (đối lại <b>еди́нственное число́</b> số ít).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мно́го</b> nhiều · <b>мно́жество</b> số lượng lớn, tập hợp · '
    '<b>умножа́ть</b> nhân lên (toán)</div>'
)

# ------------------------------------------- thiên nhiên: màu, gió, chuột, nước mắt
S["цвет"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn <b>цвет-</b>, không chẻ được. Gốc này vốn có nghĩa "nở, ra '
    'hoa"; màu sắc là cái mà bông hoa khoe ra, nên một gốc đẻ ra hai nhánh nghĩa.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bảng chia lệch đúng một chỗ: số ít trọng âm ở gốc (<b>цве́та</b>, '
    '<b>цве́том</b>), sang số nhiều thì đổi đuôi sang <i>-а́</i> và trọng âm nhảy theo — '
    '<b>цвета́</b>. Cùng khuôn <b>дом → дома́</b>, <b>лес → леса́</b> trong lô này.</div>'
    '<div class="hd-warn">⚠️ Hai số nhiều đừng lẫn: <b>цвета́</b> = các MÀU, còn '
    '<b>цветы́</b> = các BÔNG HOA (số nhiều của <b>цвето́к</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>цвето́к</b> bông hoa · <b>цветно́й</b> có màu, màu mè · '
    '<b>цвести́</b> nở hoa</div>'
)

S["ветер"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вет-</span>'
    '<span class="hd-gloss">gốc THỔI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ер</span>'
    '<span class="hd-gloss">đuôi danh từ, chữ <i>е</i> này sẽ rụng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc Ấn–Âu với tiếng Anh <i>wind</i> và Latin <i>ventus</i>. '
    'Bảng chia lệch hai chỗ, cùng một câu là đủ: <b>chữ е trong -ер RỤNG</b> ngay khi thêm '
    'đuôi (<b>ве́тра</b>, <b>ве́тром</b>), và cách 6 có dạng thứ hai <b>на ветру́</b> khi ở '
    'ngoài trời lộng gió — đúng hiện tượng của <b>в лесу́</b> ở thẻ <b>лес</b> lô này.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ве́треный</b> lộng gió, nhẹ dạ · <b>ветеро́к</b> làn gió nhẹ · '
    '<b>прове́тривать</b> thông gió cho phòng</div>'
)

S["мышь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мыш-</span>'
    '<span class="hd-gloss">gốc CHUỘT</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ь</span>'
    '<span class="hd-gloss">dấu mềm khép từ; ở đây từ là giống CÁI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc Ấn–Âu với tiếng Anh <i>mouse</i>, Latin <i>mus</i>. '
    'Chỗ lệch của bảng: <b>số nhiều tách làm hai nửa</b> — riêng cách 1 giữ trọng âm ở gốc '
    '<b>мы́ши</b>, còn tất cả các cách kia tụt xuống đuôi: <b>мыше́й</b>, <b>мыша́м</b>, '
    '<b>мыша́ми</b>.</div>'
    '<div class="hd-warn">⚠️ Đuôi <b>-ь</b> KHÔNG tự nó cho biết giống. <b>мышь</b> giống cái, '
    'nhưng <b>день</b> và <b>роди́тель</b> cũng đuôi <b>-ь</b> mà giống đực — phải nhớ từng từ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мы́шка</b> con chuột nhắt, con chuột máy tính · '
    '<b>мыши́ный</b> thuộc về chuột, màu xám chuột</div>'
)

S["слеза"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">слез-</span>'
    '<span class="hd-gloss">gốc NƯỚC MẮT</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi danh từ giống CÁI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trọng âm chạy vòng, nhưng nhìn mặt chữ là biết: số ít nhấn ở đuôi '
    '(<b>слеза́</b>, <b>слезы́</b>, <b>слезе́</b>); lên đầu bảng số nhiều nó nhảy về gốc và '
    'chữ <b>е</b> của gốc <b>đổi luôn thành ё</b> — <b>слёзы</b>, <b>слёз</b>; các cách sau '
    'của số nhiều lại tụt xuống đuôi nên <b>ё</b> biến mất: <b>слеза́м</b>, <b>слеза́ми</b>. '
    'Chiều ngược lại thì luôn đúng ở mọi từ: hễ thấy <b>ё</b> là trọng âm nằm ngay đó.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>слёзный</b> thuộc về nước mắt · <b>слезли́вый</b> mau nước mắt, '
    'hay khóc · <b>прослези́ться</b> rơm rớm nước mắt</div>'
)

# ------------------------------------------------------------------------------
# V — sửa field Vietnamese (đề bài deck 1-go). CHỈ những từ thật sự cần sửa.
# Xem báo cáo: 16/18 từ giữ nguyên vì đề bài hiện tại đã là danh sách nghĩa thuần.

# «sân chơi» KHÔNG có trong gloss Anh (a field / margins / brim) — đúng khuôn
# "nới rộng" README §2c cảnh báo; bỏ. Bù lại hai nghĩa gloss có mà đề bài đang
# thiếu hẳn: margins = lề trang giấy, brim = vành mũ (cả hai chỉ dùng số nhiều
# поля́). "lĩnh vực chuyên môn" rút còn "lĩnh vực" cho đúng mức rộng của gloss.
V["поле"] = "cánh đồng, lĩnh vực, lề trang giấy, vành mũ"

# Khuôn tính từ quan hệ đã đo trên chính bộ sưu tập: англи́йский = "thuộc về nước
# Anh, kiểu Anh", неме́цкий / францу́зский y hệt. Mỹ không phải một ngôn ngữ nên
# lấy nhánh "kiểu X" chứ không phải "tiếng X".
V["американский"] = "thuộc về nước Mỹ, kiểu Mỹ"
