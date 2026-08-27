# -*- coding: utf-8 -*-
"""k79 — ăn uống + đời sống: từ mới user vừa thêm, các từ KHÔNG cùng một họ.

Mỗi thẻ soạn độc lập, không ép trục chung. Ba chỗ phải nhất quán với thẻ đã có
trong kho: bộ ba `мыть / помы́ть / вы́мыть` (thẻ `мыть` giữ luật `стира́ть` vs
`мыть`, hai thẻ hoàn thành chỉ nói phần khác nhau của mình); lớp danh từ giống
đực số nhiều `-а́` nói KỸ ở thẻ `го́лос`, thẻ `па́спорт` chỉ dẫn chiếu một dòng;
và bộ `род` đã dạy ở `роди́ться / рожде́ние / ро́дина`.
"""

S = {}

# ------------------------------------------------------------------ варенье
S["варенье"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вар-</span>'
    '<span class="hd-gloss">gốc ĐUN, LUỘC — như <b>вари́ть</b> nấu</span></div>'
    '<div class="hd-row"><span class="hd-piece">-енье</span>'
    '<span class="hd-gloss">hậu tố → danh từ giống trung, chỉ KẾT QUẢ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Quả đun (<b>вар-</b>) với đường tới khi sánh lại thì '
    'thành mứt. Nhìn đuôi <b>-енье</b> là biết ngay danh từ giống trung.</div>'
    '<div class="hd-warn">Đuôi <b>-енье</b> chỉ KẾT QUẢ, còn <b>-ение</b> chỉ VIỆC '
    'ĐANG LÀM: <b>варе́нье</b> là hũ mứt, <b>варе́ние</b> là việc đun nấu.</div>'
    '<div class="hd-warn">Cách 2 số nhiều nuốt mất <b>-ь-</b>: <b>варе́нье → '
    'варе́ний</b>. Mọi danh từ đuôi <b>-нье</b> đều thế.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вари́ть</b> nấu, luộc · <b>по́вар</b> đầu bếp · '
    '<b>варёный</b> đã luộc</div>'
)

# ------------------------------------------------------------------- десерт
S["десерт"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn nguyên khối từ tiếng Pháp '
    '<i>dessert</i>, tiếng Nga không tách ra mảnh nào có nghĩa riêng.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiếng Pháp <i>desservir</i> là DỌN BÀN — món ăn lúc bàn '
    'chính đã dọn xong. Tiếng Anh <i>dessert</i> cùng gốc đó, nên chỉ còn phải nhớ '
    'mặt chữ Nga.</div>'
    '<div class="hd-warn">Tiếng Nga viết MỘT chữ <b>с</b>: <b>десе́рт</b>, không '
    'gấp đôi như <i>dessert</i> tiếng Anh.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>десе́ртный</b> thuộc món tráng miệng — '
    '<b>десе́ртная ло́жка</b> thìa tráng miệng</div>'
)

# --------------------------------------------------------------- мороженое
S["мороженое"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">морож-</span>'
    '<span class="hd-gloss">gốc <b>моро́з</b> băng giá, з đổi thành ж</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ен-</span>'
    '<span class="hd-gloss">đuôi phân từ «bị làm cho…»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ое</span>'
    '<span class="hd-gloss">đuôi TÍNH TỪ, giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen là «cái đã bị làm cho đông lại». Nó vốn là tính '
    'từ nên chia y như tính từ: <b>моро́женого, моро́женым</b> — không có đuôi danh '
    'từ nào cả.</div>'
    '<div class="hd-warn">Trước hậu tố <b>-ен-</b> thì <b>з → ж</b>: <b>моро́з → '
    'моро́женое</b>. Cùng phép biến âm với <b>сказа́ть → скажу́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>моро́з</b> băng giá · <b>моро́зить</b> làm đông · '
    '<b>моро́женый</b> đã đông lạnh</div>'
)

# -------------------------------------------------------------------- овощи
S["овощи"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">овощ-</span>'
    '<span class="hd-gloss">gốc RAU CỦ, không phụ tố</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и</span>'
    '<span class="hd-gloss">đuôi SỐ NHIỀU</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Rau củ gần như luôn nói ở số nhiều — mua rau là mua nhiều '
    'thứ một lúc. Dạng số ít <b>о́вощ</b> có thật nhưng hiếm, chỉ dùng khi nói về '
    'đúng MỘT loại.</div>'
    '<div class="hd-warn">Trọng âm chạy sang đuôi ở mọi cách gián tiếp: <b>о́вощи</b> '
    'nhưng <b>овоще́й, овоща́м, овоща́ми</b>. Nhớ một cặp là ra cả bảng.</div>'
    '<div class="hd-warn">Đừng lẫn với <b>фру́кты</b>: <b>о́вощи</b> là thứ ăn với '
    'cơm, <b>фру́кты</b> là thứ ăn tráng miệng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>о́вощ</b> một loại rau · <b>овощно́й</b> thuộc rau — '
    '<b>овощно́й магази́н</b> cửa hàng rau</div>'
)

# --------------------------------------------------------------------- суши
S["суши"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn thẳng tiếng Nhật <i>sushi</i>, vào '
    'tiếng Nga nguyên một khối.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ mượn kết thúc bằng <b>-и</b> nên tiếng Nga không xếp '
    'được nó vào kiểu chia nào — đành để nguyên, y như <b>метро́</b> và '
    '<b>кино́</b>.</div>'
    '<div class="hd-warn">KHÔNG biến cách: mọi cách đều viết <b>су́ши</b>. Chính '
    'giới từ đứng trước mới cho biết đang ở cách nào.</div>'
    '<div class="hd-warn">Sách phiên âm chuẩn ghi <b>су́си</b>, nhưng đời thường và '
    'mọi thực đơn đều viết <b>су́ши</b>. Cứ dùng <b>су́ши</b>.</div>'
)

# ----------------------------------------------------------------- нарезать
S["нарезать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">tiền tố: làm ra MỘT LƯỢNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-рез-</span>'
    '<span class="hd-gloss">gốc CẮT — như <b>ре́зать</b> cắt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cắt (<b>-рез-</b>) ra thành một lượng (<b>на-</b>) miếng '
    'nhỏ — đúng việc thái thịt, thái rau xếp lên đĩa.</div>'
    '<div class="hd-warn">Cặp thể này khác nhau CHỈ ở trọng âm, mặt chữ y hệt: '
    '<b>наре́зать</b> thái xong một lượt · <b>нареза́ть</b> đang, thường thái.</div>'
    '<div class="hd-warn">Thân tương lai đổi <b>з → ж</b>: <b>наре́жу, '
    'наре́жешь</b> — không suy thẳng từ nguyên thể được, phải nhớ riêng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ре́зать</b> cắt · <b>отре́зать</b> cắt rời · '
    '<b>разре́зать</b> cắt đôi</div>'
)

# -------------------------------------------------------------------- кусок
S["кусок"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кус-</span>'
    '<span class="hd-gloss">gốc CẮN — như <b>куса́ть</b> cắn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ок</span>'
    '<span class="hd-gloss">hậu tố giống đực; chữ о sẽ rơi</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái mình cắn (<b>кус-</b>) một phát ra được = một miếng. '
    'Hậu tố <b>-ок</b> làm nó thành vật đếm được, giống đực.</div>'
    '<div class="hd-warn">NGUYÊN ÂM CHẠY: chữ <b>о</b> trong <b>-ок</b> rơi ngay '
    'khi thêm đuôi — <b>кусо́к → куска́, куску́, куски́</b>.</div>'
    '<div class="hd-warn">«Một miếng CỦA cái gì» đi với cách 2: <b>кусо́к хле́ба</b> '
    'miếng bánh mì · <b>кусо́к са́хара</b> viên đường.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кусо́чек</b> miếng nhỏ · <b>куса́ть</b> cắn · '
    '<b>заку́ска</b> món khai vị</div>'
)

# ------------------------------------------------------------------ новость
S["новость"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">нов-</span>'
    '<span class="hd-gloss">gốc MỚI — như <b>но́вый</b> mới</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ость</span>'
    '<span class="hd-gloss">hậu tố → danh từ trừu tượng, LUÔN giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>-ость</b> biến tính từ thành tên gọi của chính tính '
    'chất đó: mới → «cái mới» → tin mới. Thấy đuôi <b>-ость</b> là biết giống cái, '
    'biến cách theo lối <b>-ь</b>.</div>'
    '<div class="hd-warn">Số nhiều gián tiếp dịch trọng âm ra đuôi: <b>но́вости</b> '
    'nhưng <b>новосте́й, новостя́м, новостя́ми</b>.</div>'
    '<div class="hd-warn">Số nhiều <b>но́вости</b> còn là bản tin thời sự: '
    '<b>смотре́ть но́вости</b> = xem thời sự.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>но́вый</b> mới · <b>обнови́ть</b> làm mới, cập nhật</div>'
)

# ------------------------------------------------------------------ паспорт
S["паспорт"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được trong tiếng Nga: mượn nguyên khối, gốc xa '
    'là tiếng Ý <i>passaporto</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiếng Ý <i>passare</i> ĐI QUA + <i>porto</i> CỬA CẢNG — tờ '
    'giấy để đi qua cửa cảng. Tiếng Anh <i>passport</i> cùng gốc, nên chỉ còn phải '
    'nhớ mặt chữ Nga.</div>'
    '<div class="hd-warn">Số nhiều đổi hẳn đuôi và dịch trọng âm: <b>па́спорт → '
    'паспорта́</b>. Cùng lớp với <b>дом → дома́</b> — thẻ <b>го́лос</b> trong lô này '
    'nói kỹ lớp đó.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>па́спортный</b> thuộc hộ chiếu — <b>па́спортный '
    'контро́ль</b> kiểm tra hộ chiếu</div>'
)

# ------------------------------------------------------------------ секунда
S["секунда"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">секунд-</span>'
    '<span class="hd-gloss">gốc Latin <i>secunda</i> — THỨ HAI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiếng Latin thời trung cổ chia nhỏ giờ lần MỘT được phút, '
    'chia nhỏ lần HAI được giây — nên «giây» mang đúng nghĩa «thứ hai». Tiếng Anh <i>second</i> '
    'cùng một chữ đó.</div>'
    '<div class="hd-warn">Muốn bảo «chờ chút» thì dùng dạng nhỏ: '
    '<b>Секу́ндочку!</b> = chờ một giây nhé. Rất hay gặp khi nói chuyện.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>секу́ндный</b> kéo dài một giây · <b>секу́ндочка</b> '
    'một giây thôi</div>'
)

# -------------------------------------------------------------- заболевать
S["заболевать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">tiền tố: BẮT ĐẦU rơi vào một trạng thái</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бол-</span>'
    '<span class="hd-gloss">gốc ĐAU, ỐM — như <b>боле́ть</b> bị ốm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ева-</span>'
    '<span class="hd-gloss">hậu tố KÉO DÀI → thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>за-</b> đánh dấu lúc BƯỚC VÀO cơn ốm, còn <b>-ева-</b> '
    'kéo cái lúc ấy dài ra thành quá trình — đang chớm ốm, hoặc hay ốm.</div>'
    '<div class="hd-warn">Ba từ ba việc: <b>боле́ть</b> đang ốm · '
    '<b>заболева́ть</b> đang chớm ốm, hay ốm · <b>заболе́ть</b> đổ bệnh một lần.</div>'
    '<div class="hd-warn">Ốm bệnh gì thì để bệnh đó ở cách 5: '
    '<b>заболе́ть гри́ппом</b> = mắc cúm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>боле́ть</b> ốm · <b>заболе́ть</b> đổ bệnh · <b>боль</b> '
    'cơn đau · <b>больни́ца</b> bệnh viện</div>'
)

# ---------------------------------------------------------------- рождаться
S["рождаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рожд-</span>'
    '<span class="hd-gloss">gốc <b>род</b> DÒNG GIỐNG, д đổi thành жд</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-</span>'
    '<span class="hd-gloss">hậu tố kéo dài → thể chưa hoàn thành</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">đuôi phản thân: xảy ra với CHÍNH MÌNH</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bước vào dòng giống (<b>род</b>) của mình — việc ấy xảy ra '
    'với chính mình nên phải có <b>-ся</b>.</div>'
    '<div class="hd-warn">Vào nhóm từ này thì <b>д</b> của gốc <b>род</b> hoá <b>жд</b>: '
    '<b>род → рожде́ние, рожда́ться</b> — dấu vết tiếng Slav Nhà thờ.</div>'
    '<div class="hd-warn">Cặp thể: <b>роди́ться</b> cho một lần chào đời — '
    '<b>Я роди́лся в 2000 году́</b>; <b>рожда́ться</b> cho việc lặp lại hay nghĩa '
    'bóng — <b>рожда́ются иде́и</b> ý tưởng nảy sinh.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>род</b> dòng họ · <b>роди́ться</b> chào đời · '
    '<b>рожде́ние</b> sự ra đời · <b>ро́дина</b> quê hương</div>'
)

# ---------------------------------------------------------------- отдохнуть
S["отдохнуть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">tiền tố: RỜI RA, tách khỏi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дох-</span>'
    '<span class="hd-gloss">gốc THỞ — như <b>дыша́ть</b> thở, <b>во́здух</b> không '
    'khí</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ну-</span>'
    '<span class="hd-gloss">hậu tố MỘT LẦN, chốc lát → thể hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: thở ra một cái cho RỜI khỏi công việc. Hậu tố '
    '<b>-ну-</b> đóng gói việc đó thành một lần dứt điểm, nên đây là thể hoàn '
    'thành.</div>'
    '<div class="hd-warn">Cặp thể: <b>отдыха́ть</b> đang nghỉ, hay nghỉ — '
    '<b>отдохну́ть</b> nghỉ một lát rồi thôi. Câu hay dùng: <b>Отдохни́!</b> = '
    'Nghỉ đi!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отдыха́ть</b> nghỉ ngơi · <b>о́тдых</b> sự nghỉ ngơi · '
    '<b>дыша́ть</b> thở · <b>во́здух</b> không khí</div>'
)

# ------------------------------------------------------------------ сыграть
S["сыграть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">tiền tố: gói việc lại thành MỘT lần trọn vẹn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыгра-</span>'
    '<span class="hd-gloss">chính là <b>игра́ть</b> chơi, и đã đổi thành ы</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>с-</b> không thêm nghĩa mới, chỉ biến «đang chơi» thành '
    '«chơi xong một ván». Vì thế <b>сыгра́ть</b> luôn nói về một trận, một bản nhạc '
    'cụ thể.</div>'
    '<div class="hd-warn">Sau tiền tố kết thúc bằng phụ âm, chữ <b>и</b> đầu gốc '
    'đổi thành <b>ы</b>: <b>с + игра́ть → сыгра́ть</b>.</div>'
    '<div class="hd-warn">Chơi TRÒ thì <b>в</b> + cách 4, chơi NHẠC CỤ thì <b>на</b> '
    '+ cách 6: <b>сыгра́ть в ша́хматы</b> · <b>сыгра́ть на гита́ре</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>игра́ть</b> chơi · <b>игра́</b> trò chơi · '
    '<b>игру́шка</b> đồ chơi · <b>игро́к</b> người chơi</div>'
)

# --------------------------------------------------------------------- мыть
S["мыть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мы-</span>'
    '<span class="hd-gloss">gốc RỬA, đứng trơn không phụ tố</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ thêm được. Nhận ra nó ở <b>мы́ло</b> '
    'xà phòng — thứ dùng để <b>мыть</b>.</div>'
    '<div class="hd-warn">Nguyên thể có <b>ы</b>, nhưng thân hiện tại đổi sang '
    '<b>о</b>: <b>мыть → мо́ю, мо́ешь, мо́ют</b>. Nhớ một dạng là ra cả bảng.</div>'
    '<div class="hd-warn"><b>мыть</b> chỉ dùng cho ĐỒ VẬT và BỀ MẶT — tay, bát, xe, '
    'sàn. Giặt quần áo là <b>стира́ть</b>, không bao giờ là <b>мыть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мы́ло</b> xà phòng · <b>помы́ть</b>, <b>вы́мыть</b> rửa '
    'xong · <b>умы́ться</b> rửa mặt</div>'
)

# ------------------------------------------------------------------- вымыть
S["вымыть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span>'
    '<span class="hd-gloss">tiền tố: RA HẾT, làm cho cạn sạch</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мы-</span>'
    '<span class="hd-gloss">gốc RỬA — <b>мыть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>вы-</b> vốn nghĩa «ra ngoài», ở đây thành «làm cho sạch '
    'tới hết» — rửa đến khi không còn gì bẩn, sạch bong.</div>'
    '<div class="hd-warn">Trong động từ hoàn thành, tiền tố <b>вы-</b> luôn kéo '
    'trọng âm về mình và giữ yên đó: <b>вы́мыть, вы́мою, вы́мыл</b>.</div>'
    '<div class="hd-warn">Khác <b>помы́ть</b>: <b>помы́ть</b> là rửa xong một lượt '
    'bình thường, còn <b>вы́мыть</b> nhấn KẾT QUẢ sạch bong.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мыть</b> rửa · <b>помы́ть</b> rửa xong · '
    '<b>вымыва́ть</b> rửa trôi · <b>мы́ло</b> xà phòng</div>'
)

# ------------------------------------------------------------------- помыть
S["помыть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố: làm XONG một lượt, không thêm nghĩa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мы-</span>'
    '<span class="hd-gloss">gốc RỬA — <b>мыть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>по-</b> ở đây là tiền tố rỗng nghĩa: nó chỉ đóng việc '
    'rửa lại thành một lượt đã xong. <b>помы́ть</b> = <b>мыть</b> ở thể hoàn '
    'thành.</div>'
    '<div class="hd-warn">Thân tương lai đổi <b>ы → о</b> y như <b>мыть</b>: '
    '<b>помо́ю, помо́ешь, помо́ют</b>. Mệnh lệnh: <b>Помо́й ру́ки!</b></div>'
    '<div class="hd-warn">Đây là cặp thể thường ngày của <b>мыть</b>; còn '
    '<b>вы́мыть</b> để dành cho lúc muốn nhấn «sạch bong».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мыть</b> rửa · <b>вы́мыть</b> rửa sạch bong · '
    '<b>мы́ло</b> xà phòng</div>'
)

# -------------------------------------------------------------- показывать
S["показывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố đã dính chặt, không còn nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-каз-</span>'
    '<span class="hd-gloss">gốc ĐƯA RA CHO THẤY — như <b>сказа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-</span>'
    '<span class="hd-gloss">hậu tố biến hoàn thành → CHƯA hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>-ыва-</b> kéo việc «đưa ra cho thấy» dài ra: từ '
    '<b>показа́ть</b> cho xem một lần thành <b>пока́зывать</b> đang, thường cho '
    'xem.</div>'
    '<div class="hd-warn">Thêm <b>-ыва-</b> thì trọng âm nhảy về trước: '
    '<b>показа́ть → пока́зывать</b>, y như <b>рассказа́ть → расска́зывать</b>.</div>'
    '<div class="hd-warn">Cho AI (cách 3) xem CÁI GÌ (cách 4): <b>Покажи́те мне '
    'па́спорт</b> = Cho tôi xem hộ chiếu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>показа́ть</b> cho xem · <b>сказа́ть</b> nói · '
    '<b>рассказа́ть</b> kể lại · <b>ука́зывать</b> chỉ trỏ</div>'
)

# -------------------------------------------------------------- передавать
S["передавать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пере-</span>'
    '<span class="hd-gloss">tiền tố: QUA, từ bên này sang bên kia</span></div>'
    '<div class="hd-row"><span class="hd-piece">-да-</span>'
    '<span class="hd-gloss">gốc CHO — như <b>дать</b>, <b>дава́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва-</span>'
    '<span class="hd-gloss">hậu tố kéo dài → thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cho (<b>-да-</b>) một thứ đi QUA (<b>пере-</b>) tay người '
    'khác. Nghĩa «phát sóng» cũng là chuyển đi xa — <b>переда́ча</b> buổi phát.</div>'
    '<div class="hd-warn">Hậu tố <b>-ва-</b> RƠI MẤT ở thì hiện tại: '
    '<b>передава́ть → передаю́, передаёшь</b>. Cùng lối với <b>дава́ть → даю́</b>, '
    '<b>встава́ть → встаю́</b>.</div>'
    '<div class="hd-warn">Cụm phải thuộc: <b>Переда́й приве́т</b> + cách 3 = cho gửi '
    'lời chào tới…</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дать</b>, <b>дава́ть</b> cho · <b>переда́ть</b> trao '
    'lại · <b>переда́ча</b> buổi phát sóng</div>'
)

# -------------------------------------------------------------------- голос
S["голос"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">голос-</span>'
    '<span class="hd-gloss">gốc trơn — âm phát ra từ miệng người</span></div>'
    '<div class="hd-row"><span class="hd-piece">глас-</span>'
    '<span class="hd-gloss">biến thể Slav Nhà thờ của cùng gốc ấy</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một gốc, hai mặt chữ: kiểu Nga <b>го́лос</b> và kiểu Slav '
    'Nhà thờ <b>глас</b> — đúng cặp <b>-оло-</b> / <b>-ла-</b> đã thấy ở '
    '<b>го́род</b> / <b>град</b>.</div>'
    '<div class="hd-warn">Số nhiều đổi đuôi sang <b>-а́</b> và dịch trọng âm: '
    '<b>го́лос → голоса́, голосо́в</b>. Cả lớp danh từ giống đực này đều thế: '
    '<b>дом → дома́</b>, <b>го́род → города́</b>, <b>па́спорт → паспорта́</b>.</div>'
    '<div class="hd-warn">Nghĩa «lá phiếu» sinh ra từ chỗ xưa bỏ phiếu bằng cách '
    'CẤT TIẾNG: <b>голосова́ть за</b> + cách 4 = bỏ phiếu ủng hộ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>голосова́ть</b> bỏ phiếu · <b>гла́сный</b> nguyên âm · '
    '<b>согла́сный</b> phụ âm; đồng ý</div>'
)

# ============================================================ field Vietnamese
# Chỉ sửa dòng thật sự hỏng: có ngoặc chú thích (README §2c cấm ③), va chạm nghĩa
# với thẻ ĐÃ CÓ trong kho, hoặc nghĩa sai mà chính từ điển của thẻ bác lại.
# 🔴 KHÔNG có V["нарезать"]: bộ sưu tập có HAI note cùng WordClean `нарезать`
# (наре́зать PERF và нареза́ть IMPF), mà `nap` ghi vào MỌI note khớp khoá — đặt V
# ở đây là san phẳng đúng cái badge đang tách hai thẻ đó. Đã báo lên luồng chính.
V = {
    # va chạm với болеть (v/IMPF) = "bị ốm, đau nhức, cổ vũ" — thẻ CÓ SẴN, mồ côi.
    # Gỡ bằng RÚT GỌN phía mình: bỏ "bị ốm", giữ đúng sắc thái BẮT ĐẦU của за-.
    "заболевать": "đổ bệnh, ngả bệnh",
    # va chạm với давать (v/IMPF) = "đưa, cho, trao" — thẻ CÓ SẴN, mồ côi.
    # Bỏ "đưa"; hai nghĩa còn lại đã đủ và khớp lối phân biệt của передать.
    "передавать": "chuyển, truyền tải",
    # va chạm với звук "âm thanh, tiếng, âm" và язык "ngôn ngữ, tiếng, cái lưỡi"
    # (cùng n/MASC) — cả hai CÓ SẴN, mồ côi. Bỏ "tiếng" ở phía mình.
    # Thêm "lá phiếu": gloss tiếng Anh của CHÍNH thẻ này ghi "vote", đây là nghĩa
    # thông dụng đang thiếu hẳn (đúng ca `пол` thiếu "nửa" mà README §2c nêu).
    "голос": "giọng nói, lá phiếu",
    # bỏ ngoặc chú thích "(món ăn)" — README §2c cấm ③. "kem" không đụng ai:
    # сметана là "kem chua", торт là "bánh kem", không cụm nào trùng nguyên vẹn.
    "мороженое": "kem",
    # bỏ ngoặc "(trò chơi, nhạc cụ)"; phần trong ngoặc vốn là hai nghĩa thật nên
    # trả chúng về dạng nghĩa rời thay vì vứt đi.
    "сыграть": "chơi, chơi nhạc, diễn xuất",
    # BỎ "giặt": chính từ điển của thẻ này ghi стирать = giặt quần áo, còn мыть chỉ
    # dùng cho đồ vật/bề mặt. Đây là nghĩa SAI, không phải nghĩa thừa.
    "мыть": "rửa, lau chùi",
    # BỎ "giặt" (cùng lý do trên) và bỏ "sạch": вымыть/помыть cùng badge PERF nên
    # "rửa sạch" đứng cạnh "rửa cho sạch bong" của вымыть là hai đáp án cho một đề.
    # "rửa, gội" tách sạch khỏi вымыть, và khác мыть nhờ badge IMPF/PERF.
    "помыть": "rửa, gội",
}
