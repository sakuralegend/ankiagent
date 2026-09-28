# -*- coding: utf-8 -*-
"""k84 — tu-moi: 15 danh từ user vừa thêm, KHÔNG cùng họ nhau.

Mỗi thẻ soạn độc lập, không khối hệ thống. Chỗ cần nhất quán:
(1) bốn phương: юг (đã xong) giữ phần giải thích на + cách 6/cách 4, ba thẻ
    се́вер / восто́к / за́пад chỉ dẫn chiếu một dòng về nó;
(2) đuôi số nhiều -а́/-я́ mang trọng âm (ку́пол, се́вер, ла́герь, луг) — mỗi thẻ
    một câu, trỏ về từ đã học (дома́, города́, учителя́);
(3) khớp khuôn chẻ đã có: уч- HỌC/DẠY + -ен- "được dạy" (учёный), стро- + -и-тель
    (строи́тельный), лист- CHIẾC LÁ (листва́), кол- VÒNG (кольцо́, о́коло), пол- NỬA.
"""

S = {}

# -------------------------------------------------------- администратор
S["администратор"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">администр-</span>'
    '<span class="hd-gloss">gốc Latinh ĐIỀU HÀNH, TRÔNG COI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́тор</span>'
    '<span class="hd-gloss">NGƯỜI làm việc ấy = <i>-ator</i> tiếng Anh</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>administrator</i>. Nhưng ở Nga từ này gặp nhiều '
    'nhất tại quầy khách sạn, nhà hàng, salon: người đón khách, xếp chỗ — tức '
    'lễ tân. Trong tin học là quản trị viên hệ thống.</div>'
    '<div class="hd-warn">Trọng âm ở <b>-тра́-</b>: <b>администра́тор</b> — '
    'tiếng Anh nhấn ở <i>-min-</i>, đọc theo thói quen Anh là lệch.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>администра́ция</b> ban quản lý, chính quyền · '
    '<b>администрати́вный</b> hành chính</div>'
)

# ----------------------------------------------------------- архитектор
S["архитектор"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">архи-</span>'
    '<span class="hd-gloss">TRƯỞNG, ĐỨNG ĐẦU (Hy Lạp)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тектор</span>'
    '<span class="hd-gloss">THỢ XÂY, thợ mộc (Hy Lạp <i>téktōn</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen «thợ cả» — người đứng đầu đám thợ xây, đúng việc '
    'của kiến trúc sư. Cùng một từ với <i>architect</i> tiếng Anh.</div>'
    '<div class="hd-warn">Trọng âm ở <b>-те́-</b>: <b>архите́ктор</b>, không nhấn '
    'đầu như <i>ARchitect</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>архитекту́ра</b> kiến trúc · <b>архитекту́рный</b> '
    'thuộc kiến trúc</div>'
)

# --------------------------------------------------------------- восток
S["восток"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вос-</span>'
    '<span class="hd-gloss">LÊN (như <b>восхо́д</b> mặt trời mọc)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-то́к</span>'
    '<span class="hd-gloss">gốc CHẢY, TRÀO (<b>течь</b> chảy)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nơi mặt trời «trào lên» ⇒ phía đông. Dùng giới từ y như '
    '<b>юг</b>: <b>на восто́ке</b> ở phía đông / <b>на восто́к</b> về phía đông. '
    'Tính từ đổi <b>к → ч</b>: <b>восто́чный</b>. <b>Владивосто́к</b> = '
    '«cai quản phương Đông».</div>'
    '<div class="hd-warn">⚠️ Mức tin: cách chẻ <b>вос-</b> + <b>-ток</b> là từ '
    'nguyên, không phải luật suy ra được — người Nga ngày nay cảm nó như một gốc '
    'liền.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>восто́чный</b> thuộc phía đông · <b>ю́го-восто́к</b> '
    'đông nam · <b>Владивосто́к</b></div>'
)

# ---------------------------------------------------------------- запад
S["запад"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">RA SAU, KHUẤT ĐI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пад</span>'
    '<span class="hd-gloss">RƠI, NGÃ (<b>па́дать</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nơi mặt trời «rơi khuất» ⇒ phía tây — đối xứng với '
    '<b>восто́к</b> nơi nó trào lên. Cũng như <i>the West</i>, viết hoa '
    '<b>За́пад</b> là phương Tây (Âu–Mỹ). Giới từ như <b>юг</b>: <b>на за́паде</b> '
    'ở phía tây / <b>на за́пад</b> về phía tây.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>за́падный</b> thuộc phía tây · <b>па́дать</b> rơi, ngã · '
    '<b>листопа́д</b> mùa lá rụng</div>'
)

# --------------------------------------------------------------- колесо
S["колесо"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кол-</span>'
    '<span class="hd-gloss">từ cổ «ко́ло» — VÒNG TRÒN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-есо́</span>'
    '<span class="hd-gloss">phần đuôi, không mang nghĩa riêng; giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bánh xe = cái vòng lăn được. Cùng gốc với <b>кольцо́</b> '
    '(vòng nhỏ) và <b>о́коло</b> (vòng quanh ⇒ gần). Số nhiều trọng âm chạy về gốc '
    'và <b>е</b> hoá <b>ё</b>: <b>колёса</b>, <b>колёс</b> — y như '
    '<b>сестра́ → сёстры</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кольцо́</b> nhẫn, vòng · <b>о́коло</b> quanh, gần · '
    '<b>колёсный</b> có bánh xe</div>'
)

# ---------------------------------------------------------------- купол
S["купол"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn (tiếng Ý <i>cupola</i>, tiếng Anh cũng mượn y '
    'vậy) — không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mái vòm tròn, hình ảnh quen nhất là các mái vòm dát vàng '
    'của nhà thờ Nga. Số nhiều không đuôi <b>-ы</b> mà là <b>купола́</b>, trọng âm '
    'nhảy xuống đuôi và nằm đó suốt số nhiều (<b>куполо́в</b>) — cùng kiểu '
    '<b>дома́</b>, <b>города́</b>.</div>'
)

# --------------------------------------------------------------- лагерь
S["лагерь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn tiếng Đức <i>Lager</i> (trại; kho chứa) — không chẻ '
    'được. Chữ <i>lager</i> của bia lager («bia ủ trong kho») cũng chính là nó.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa hằng ngày là trại hè trẻ em (<b>де́тский ла́герь</b>), '
    'trại lều. Nghĩa nặng lịch sử: phần <b>ЛАГ</b> trong <b>ГУЛА́Г</b> là '
    '<b>лагере́й</b> — hệ thống trại cải tạo.</div>'
    '<div class="hd-why">Số nhiều đuôi <b>-я́</b> mang trọng âm: <b>лагеря́</b>, '
    '<b>лагере́й</b> — cùng kiểu <b>учителя́</b>, không phải <i>-и</i>.</div>'
)

# ----------------------------------------------------------------- лист
S["лист"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">лист</span>'
    '<span class="hd-gloss">CHIẾC LÁ — gốc trơn, cũng là gốc của '
    '<b>листва́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một chiếc lá rời; gom cả tán lá thì thành <b>листва́</b>. '
    'Số ít trọng âm ở đuôi (<b>листа́</b>, <b>листе́</b>), sang số nhiều lại về '
    'gốc.</div>'
    '<div class="hd-warn">🔴 Hai số nhiều, hai nghĩa: <b>ли́стья</b> = lá cây '
    '(đuôi lạ <b>-ья</b>, như <b>бра́тья</b>) · <b>листы́</b> = tờ giấy, tấm '
    '(kim loại). Số ít chung một vỏ, số nhiều mới tách nghĩa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>листва́</b> tán lá · <b>листо́к</b> lá nhỏ, tờ rơi · '
    '<b>листопа́д</b> mùa lá rụng · <b>листа́ть</b> lật trang</div>'
)

# ------------------------------------------------------------------ луг
S["луг"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn một âm tiết — không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đồng cỏ tự nhiên để cắt cỏ, thả bò — khác <b>по́ле</b> là '
    'cánh đồng trồng trọt. Số nhiều trọng âm ra đuôi: <b>луга́</b>, '
    '<b>луго́в</b>.</div>'
    '<div class="hd-warn">📍 «Trên đồng cỏ» là <b>на лугу́</b> — đuôi <b>-у́</b> riêng '
    'cho vị trí, như <b>в лесу́</b>, <b>в саду́</b>; nói VỀ đồng cỏ thì '
    '<b>о лу́ге</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лужа́йка</b> bãi cỏ nhỏ (<b>г → ж</b>) · '
    '<b>лугово́й</b> thuộc đồng cỏ</div>'
)

# ------------------------------------------------------------ медсестра
S["медсестра"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мед-</span>'
    '<span class="hd-gloss">viết tắt <b>медици́нская</b> Y TẾ — không phải '
    '<b>мёд</b> mật ong</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сестра́</span>'
    '<span class="hd-gloss">CHỊ / EM GÁI (thẻ <b>сестра́</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen «chị em y tế» — bệnh viện Anh cũng gọi y tá '
    'trưởng khoa là <i>Sister</i>. Y tá nam là <b>медбра́т</b> «anh em y tế». Số nhiều chia '
    'y hệt <b>сестра́</b>: <b>медсёстры</b>, cách 2/4 chèn <b>ё</b>: '
    '<b>медсестёр</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сестра́</b> chị, em gái · <b>медбра́т</b> y tá nam · '
    '<b>медици́на</b> y học · <b>медпу́нкт</b> trạm y tế</div>'
)

# -------------------------------------------------------------- полгода
S["полгода"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пол-</span>'
    '<span class="hd-gloss">NỬA (thẻ <b>пол</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-го́да</span>'
    '<span class="hd-gloss">cách 2 của <b>год</b>: «của năm»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Nửa của năm». <b>пол-</b> + danh từ cách 2 là khuôn đều: '
    '<b>полчаса́</b> nửa giờ, <b>полдня́</b> nửa ngày.</div>'
    '<div class="hd-warn">🔴 Ra khỏi cách 1 và cách 4 thì <b>пол-</b> đổi thành '
    '<b>полу-</b>: <b>в тече́ние полуго́да</b> trong vòng nửa năm, '
    '<b>полуго́дом</b>, <b>о полуго́де</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>полови́на</b> một nửa · <b>полчаса́</b> nửa giờ · '
    '<b>по́лдень</b> giữa trưa · <b>полуо́стров</b> bán đảo</div>'
)

# ---------------------------------------------------------------- север
S["север"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn — không chẻ được, phải thuộc.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giới từ y như <b>юг</b>: <b>на се́вере</b> ở miền Bắc / '
    '<b>на се́вер</b> về phía bắc. Số nhiều hiếm; gặp thì là <b>севера́</b> — đuôi '
    '<b>-а́</b> mang trọng âm, cùng kiểu <b>дома́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>се́верный</b> thuộc phía bắc · <b>се́веро-восто́к</b> '
    'đông bắc</div>'
)

# ------------------------------------------------------------ строитель
S["строитель"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">стро-</span>'
    '<span class="hd-gloss">XÂY, DỰNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-тель</span>'
    '<span class="hd-gloss">NGƯỜI làm việc ấy</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>стро́ить</b> xây + <b>-тель</b> người làm = người xây — '
    'đúng khuôn <b>учи́ть → учи́тель</b>. Trọng âm nhảy từ <b>о</b> sang <b>и</b> '
    'đúng một lần (<b>стро́ить → строи́тель</b>) rồi đứng yên suốt bảng chia.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>стро́ить</b> xây · <b>строи́тельный</b> thuộc xây dựng · '
    '<b>строи́тельство</b> việc xây dựng · <b>стро́йка</b> công trường</div>'
)

# ---------------------------------------------------------------- судно
S["судно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">су́дн-</span>'
    '<span class="hd-gloss">TÀU, THUYỀN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Như <i>vessel</i> tiếng Anh: từ chung, hơi trang trọng cho '
    'mọi con tàu (tin tức, hàng hải). Tàu máy chở khách cụ thể thì hay '
    'gọi <b>теплохо́д</b>.</div>'
    '<div class="hd-warn">🔴 Số nhiều rụng chữ <b>н</b>, trọng âm ra đuôi: '
    '<b>суда́</b>, <b>судо́в</b> (các con tàu) — đừng lẫn với <b>суды́</b> '
    '(các toà án, từ <b>суд</b>).</div>'
    '<div class="hd-warn">⚠️ Mức tin: từ nguyên, không phải luật — gốc cổ '
    '<i>суд-</i> «vật chứa», cùng họ xa với <b>сосу́д</b> bình chứa, '
    '<b>посу́да</b> bát đĩa (y như <i>vessel</i> vừa là bình vừa là tàu).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>судохо́дство</b> vận tải đường thủy · '
    '<b>судострое́ние</b> ngành đóng tàu</div>'
)

# --------------------------------------------------------------- ученик
S["ученик"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">уч-</span>'
    '<span class="hd-gloss">gốc HỌC / DẠY</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ен-</span>'
    '<span class="hd-gloss">đuôi phân từ bị động «ĐƯỢC dạy» (như <b>учёный</b>)'
    '</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́к</span>'
    '<span class="hd-gloss">NGƯỜI mang đặc điểm đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Người được dạy» — cặp đối với <b>учи́тель</b> người dạy. '
    'Học sinh phổ thông hoặc học trò của một thầy; sinh viên đại học là '
    '<b>студе́нт</b>. Có đuôi là trọng âm nằm trên đuôi: <b>ученика́</b>, '
    '<b>ученики́</b>, <b>ученико́в</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>учени́ца</b> nữ sinh · <b>учи́тель</b> giáo viên · '
    '<b>учи́ть</b> học, dạy · <b>учёный</b> nhà khoa học · <b>уче́бник</b> sách '
    'giáo khoa</div>'
)

V = {
    # "tên lửa" là nghĩa bịa (tên lửa = раке́та), gloss chỉ có vessel/ship/bedpan.
    "судно": "tàu thủy, thuyền lớn",
    # Bỏ "quản lý" (nới rộng, trùng менеджер cùng n + MASC); giữ hai nghĩa gloss xác nhận.
    "администратор": "nhân viên lễ tân, quản trị viên",
}
