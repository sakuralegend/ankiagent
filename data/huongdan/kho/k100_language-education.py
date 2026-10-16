# -*- coding: utf-8 -*-
"""k100 — language-education: 21 từ A1–A2 TRKI (trường lớp, giấy tờ, tin tức) — phần lớn KHÔNG cùng họ.

Mỗi thẻ soạn độc lập, không khối hệ thống. Chỗ cần nhất quán:
(1) họ био-/психо- + -лог/-ло́гия: dạy CHUNG một khuôn với k89 (геогра́фия/гео́граф):
    -ия = môn · bỏ -ия = người · trọng âm nhảy (био́лог ↔ биоло́гия).
(2) сообща́ть/сообщи́ть/сообще́ние soạn như một họ, gốc о́бщий (cùng k50 общежи́тие).
(3) khớp lời giải thích đã có: зада́ние/зада́ча (k85), перево́д (k96), звони́ть (k54),
    око́нчить/зако́нчить (k87/k95), преподава́тель (k36).
"""

S = {}

# ----------------------------------------------------------------- анкета
S["анкета"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn tiếng Pháp <i>enquête</i> (cuộc điều tra) — trong tiếng Nga '
    'không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tờ giấy có sẵn câu hỏi để mình điền vào: phiếu khai lý lịch khi xin '
    'việc, xin visa, hay bảng khảo sát. Đuôi <b>-а</b> nên là giống cái.</div>'
    '<div class="hd-warn">Cụm phải thuộc: <b>запо́лнить анке́ту</b> = điền phiếu, điền tờ khai.'
    '</div>'
)

# --------------------------------------------------------------- аспирант
S["аспирант"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">аспир-</span>'
    '<span class="hd-gloss">KHAO KHÁT, NHẮM TỚI (Latin <i>aspirare</i> — Anh <i>aspire</i>)'
    '</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ант</span>'
    '<span class="hd-gloss">đuôi NGƯỜI đang làm việc đó (như <b>эмигра́нт</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người đang nhắm tới học vị khoa học ⇒ nghiên cứu sinh.</div>'
    '<div class="hd-warn">Không phải «học viên cao học» kiểu thạc sĩ: ở Nga <b>аспира́нт</b> '
    'học để lấy học vị <b>кандида́т нау́к</b> (≈ tiến sĩ). Học viên thạc sĩ là '
    '<b>магистра́нт</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>аспиранту́ра</b> bậc nghiên cứu sinh</div>'
)

# ------------------------------------------------------------ аспирантура
S["аспирантура"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">аспира́нт-</span>'
    '<span class="hd-gloss">thẻ <b>аспира́нт</b> — nghiên cứu sinh</span></div>'
    '<div class="hd-row"><span class="hd-piece">-у́ра</span>'
    '<span class="hd-gloss">đuôi = cả một bậc, một ngạch (như <b>магистрату́ра</b> bậc thạc sĩ)'
    '</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người là <b>аспира́нт</b>, còn chương trình họ theo học là '
    '<b>аспиранту́ра</b>. Trọng âm dời sang đuôi: <b>-ту́-</b>. Học ở đó thì dùng <b>в</b>: '
    '<b>учи́ться в аспиранту́ре</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>аспира́нт</b> nghiên cứu sinh</div>'
)

# -------------------------------------------------------------- биография
S["биография"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">био-</span>'
    '<span class="hd-gloss">SỰ SỐNG (Hy Lạp <i>bios</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-граф-</span>'
    '<span class="hd-gloss">VIẾT, MÔ TẢ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ия</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Viết về một cuộc đời» — chính là <i>biography</i>. Cùng khuôn '
    '<b>-гра́фия</b> với <b>геогра́фия</b>, <b>фотогра́фия</b>: trọng âm luôn ở <b>-гра́-</b>.'
    '</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>биоло́гия</b> sinh học · <b>био́лог</b> nhà sinh học · '
    '<b>геогра́фия</b> địa lý · <b>фотогра́фия</b> bức ảnh</div>'
)

# ----------------------------------------------------------------- биолог
S["биолог"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">био-</span>'
    '<span class="hd-gloss">SỰ SỐNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лог</span>'
    '<span class="hd-gloss">NGƯỜI NGHIÊN CỨU (Hy Lạp <i>logos</i> lời, học thuyết)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Môn <b>биоло́гия</b> bỏ đuôi <b>-ия</b> ⇒ người làm môn đó. Trọng âm '
    'lùi một âm tiết: <b>биоло́гия → био́лог</b>, y như <b>геогра́фия → гео́граф</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>биоло́гия</b> sinh học · <b>психо́лог</b> nhà tâm lý học · '
    '<b>биогра́фия</b> tiểu sử</div>'
)

# ---------------------------------------------------------------- биология
S["биология"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">био-</span>'
    '<span class="hd-gloss">SỰ SỐNG (Hy Lạp <i>bios</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ло́г-</span>'
    '<span class="hd-gloss">LỜI, HỌC THUYẾT (Hy Lạp <i>logos</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ия</span>'
    '<span class="hd-gloss">đuôi = môn, ngành (giống cái)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Học thuyết về sự sống» — <i>biology</i>. Đuôi <b>-ло́гия</b> = '
    'tiếng Anh <i>-logy</i>, và trọng âm luôn nằm ở <b>-ло́-</b>: <b>биоло́гия</b>, '
    '<b>психоло́гия</b>. Bỏ <b>-ия</b> là ra người: <b>био́лог</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>био́лог</b> nhà sinh học · <b>психоло́гия</b> tâm lý học · '
    '<b>биогра́фия</b> tiểu sử</div>'
)

# ----------------------------------------------------------------- задание
S["задание"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">tiền tố của <b>зада́ть</b> — giao, đặt ra</span></div>'
    '<div class="hd-row"><span class="hd-piece">-да-</span>'
    '<span class="hd-gloss">CHO, TRAO — như <b>дать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ние</span>'
    '<span class="hd-gloss">đuôi danh từ → giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thứ được <b>зада́ть</b> (giao) cho mình ⇒ phần việc được giao: '
    '<b>дома́шнее зада́ние</b> = bài tập về nhà.</div>'
    '<div class="hd-warn">Đừng lẫn với <b>зада́ча</b>: <b>зада́ние</b> là phần việc CỤ THỂ '
    'người khác giao; <b>зада́ча</b> là vấn đề cần nghĩ để giải, là mục tiêu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>зада́ть</b> giao, đặt (câu hỏi) · <b>задава́ть</b> giao (CHT) · '
    '<b>зада́ча</b> bài toán, nhiệm vụ · <b>дать</b> cho</div>'
)

# ------------------------------------------------------------------ звонок
S["звонок"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">звон-</span>'
    '<span class="hd-gloss">TIẾNG CHUÔNG, tiếng ngân</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́к</span>'
    '<span class="hd-gloss">đuôi danh từ giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái làm ra tiếng <b>звон</b> ⇒ cái chuông (chuông cửa, chuông báo '
    'hết giờ); chuông điện thoại reo ⇒ cuộc gọi. Danh từ của <b>звони́ть</b>.</div>'
    '<div class="hd-why">Chú ý bảng chia: chữ <b>о</b> trong <b>-о́к</b> rơi mất khi thêm '
    'đuôi, trọng âm dồn ra đuôi — <b>звонка́</b>, <b>звонку́</b>, <b>звонки́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>звони́ть</b> gọi điện · <b>позвони́ть</b> gọi một cuộc (HT) · '
    '<b>звон</b> tiếng chuông</div>'
)

# ------------------------------------------------------------- оканчивать
S["оканчивать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không tách ra nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка́нч-</span>'
    '<span class="hd-gloss">gốc KẾT THÚC — <b>конч-</b> của <b>коне́ц</b>, о hoá а</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ть</span>'
    '<span class="hd-gloss">hậu tố → thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>око́нчить</b> tốt nghiệp. Thêm <b>-ива-</b> thì '
    '<b>о</b> của gốc hoá <b>а</b>, trọng âm vẫn đứng đó: <b>око́нчить → ока́нчивать</b>, '
    'y như <b>зако́нчить → зака́нчивать</b>. Trường nào: cách 4, không giới từ — '
    '<b>ока́нчивать университе́т</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>око́нчить</b> tốt nghiệp (HT) · <b>зака́нчивать</b> làm xong · '
    '<b>коне́ц</b> phần cuối</div>'
)

# ----------------------------------------------------------------- перевод
S["перевод"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пере-</span>'
    '<span class="hd-gloss">QUA, từ bên này sang bên kia</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вод</span>'
    '<span class="hd-gloss">DẪN, đưa đi — gốc của <b>води́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>переводи́ть / перевести́</b>: dẫn ý sang tiếng khác '
    '⇒ bản dịch; dẫn tiền sang tài khoản khác ⇒ khoản chuyển tiền. Cùng cặp giới từ như '
    'động từ: <b>перево́д с ру́сского на вьетна́мский</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>переводи́ть</b> dịch (CHT) · <b>перевести́</b> dịch (HT) · '
    '<b>перево́дчик</b> phiên dịch viên · <b>води́ть</b> dẫn</div>'
)

# ----------------------------------------------------------------- предмет
S["предмет"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пред-</span>'
    '<span class="hd-gloss">TRƯỚC, phía trước</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мет</span>'
    '<span class="hd-gloss">NÉM, đặt ra (gốc của <b>мета́ть</b> ném)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thứ được ném ra trước mặt» — dịch từng mảnh từ Latin '
    '<i>objectum</i>, nên trùng khớp tiếng Anh <i>object</i>: vật, đồ vật. Rồi mở sang '
    '«thứ mình học» ⇒ môn học, như <i>subject</i>: <b>Како́й твой люби́мый предме́т?</b> = '
    'Môn bạn thích nhất là gì?</div>'
)

# ------------------------------------------------------------- преподавать
S["преподавать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пре-по-</span>'
    '<span class="hd-gloss">truyền qua, chuyển sang</span></div>'
    '<div class="hd-row"><span class="hd-piece">-да-ва-</span>'
    '<span class="hd-gloss">CHO, TRAO — chính là <b>дава́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trao kiến thức sang cho người khác ⇒ giảng dạy; người làm việc đó '
    'là <b>преподава́тель</b>. Dạy môn gì: cách 4, dạy ai: cách 3 — '
    '<b>преподава́ть ру́сский студе́нтам</b>.</div>'
    '<div class="hd-why">Chú ý bảng chia: chia y hệt <b>дава́ть</b>, <b>-ва-</b> rơi mất ở '
    'hiện tại — <b>преподаю́</b>, <b>преподаёшь</b>, <b>преподаю́т</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>преподава́тель</b> giảng viên · <b>дава́ть</b> cho · '
    '<b>задава́ть</b> giao, đặt (câu hỏi)</div>'
)

# ---------------------------------------------------------------- психолог
S["психолог"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">психо-</span>'
    '<span class="hd-gloss">TÂM HỒN, tâm trí (Hy Lạp <i>psychē</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лог</span>'
    '<span class="hd-gloss">NGƯỜI NGHIÊN CỨU — như trong <b>био́лог</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Môn <b>психоло́гия</b> bỏ <b>-ия</b> ⇒ người làm môn đó; trọng âm '
    'lùi một âm tiết: <b>психоло́гия → психо́лог</b>, cùng khuôn <b>биоло́гия → био́лог</b>.'
    '</div>'
    '<div class="hd-warn"><b>психо́лог</b> không phải bác sĩ, không kê đơn thuốc. Bác sĩ '
    'chữa bệnh tâm thần là <b>психиа́тр</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>психоло́гия</b> tâm lý học · <b>био́лог</b> nhà sinh học</div>'
)

# -------------------------------------------------------------- психология
S["психология"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">психо-</span>'
    '<span class="hd-gloss">TÂM HỒN, tâm trí (Hy Lạp <i>psychē</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ло́гия</span>'
    '<span class="hd-gloss">MÔN HỌC VỀ… = tiếng Anh <i>-logy</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Môn học về tâm trí» — <i>psychology</i>. Cùng khuôn với '
    '<b>биоло́гия</b>: trọng âm ở <b>-ло́-</b>, bỏ <b>-ия</b> là ra người — '
    '<b>психо́лог</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>психо́лог</b> nhà tâm lý học · <b>биоло́гия</b> sinh học</div>'
)

# ----------------------------------------------------------------- система
S["система"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn Hy Lạp <i>systēma</i> (cái ghép lại thành một khối) — '
    'trong tiếng Nga không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>system</i>, chỉ khác chỗ nhấn: tiếng Anh nhấn đầu, '
    'tiếng Nga nhấn giữa — <b>систе́ма</b>. Đuôi <b>-а</b> nên là giống cái.</div>'
)

# ---------------------------------------------------------------- собрание
S["собрание"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">CÙNG, gom lại một chỗ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бра-</span>'
    '<span class="hd-gloss">LẤY — gốc của <b>брать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ние</span>'
    '<span class="hd-gloss">đuôi danh từ → giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>собра́ть</b> gom lại: gom NGƯỜI ⇒ cuộc họp; gom '
    'VẬT ⇒ bộ sưu tập. Đi họp là <b>на</b>: <b>быть на собра́нии</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>собра́ть</b> gom, thu thập (HT) · <b>собира́ть</b> gom (CHT) · '
    '<b>брать</b> lấy</div>'
)

# ---------------------------------------------------------------- сообщать
S["сообщать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">CÙNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-общ-</span>'
    '<span class="hd-gloss">CHUNG — gốc của <b>о́бщий</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành, chia lớp 1</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Biến điều mình biết thành cái CHUNG cho người khác cùng biết ⇒ báo '
    'tin, cho biết. Cặp thể: <b>сообщи́ть</b>. Chia đều: <b>сообща́ю</b>, '
    '<b>сообща́ешь</b>.</div>'
    '<div class="hd-warn">Báo cho AI: cách 3; báo VỀ cái gì: <b>о</b> + cách 6 — '
    '<b>сообща́ть дру́гу о встре́че</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сообщи́ть</b> báo tin (HT) · <b>сообще́ние</b> tin nhắn · '
    '<b>о́бщий</b> chung · <b>общежи́тие</b> ký túc xá</div>'
)

# --------------------------------------------------------------- сообщение
S["сообщение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сообщ-</span>'
    '<span class="hd-gloss">từ <b>сообщи́ть</b> — làm cho mọi người cùng biết</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ние</span>'
    '<span class="hd-gloss">đuôi danh từ → giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thứ được <b>сообщи́ть</b> ⇒ tin, tin nhắn: <b>написа́ть '
    'сообще́ние</b> = nhắn một tin. Nghĩa «làm cho hai nơi thông nhau» còn trong '
    '<b>сообще́ние</b> = đường liên lạc, tuyến giao thông giữa hai nơi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сообщи́ть</b> báo tin (HT) · <b>сообща́ть</b> báo tin (CHT) · '
    '<b>о́бщий</b> chung</div>'
)

# ---------------------------------------------------------------- сообщить
S["сообщить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">CÙNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-общ-</span>'
    '<span class="hd-gloss">CHUNG — gốc của <b>о́бщий</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi thể hoàn thành, chia lớp 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Báo tin một lần, xong — cặp HT của <b>сообща́ть</b>, cùng cách đòi: '
    'người nghe cách 3, nội dung <b>о</b> + cách 6. Trọng âm ở đuôi suốt bảng: '
    '<b>сообщу́</b>, <b>сообщи́шь</b>, <b>сообща́т</b>.</div>'
    '<div class="hd-warn">Cụm hay gặp trên báo: <b>как сообщи́ли…</b> = theo tin đưa, theo '
    'thông tin từ…</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сообща́ть</b> báo tin (CHT) · <b>сообще́ние</b> tin nhắn · '
    '<b>о́бщий</b> chung</div>'
)

# ----------------------------------------------------------------- справка
S["справка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không tách ra nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-прав-</span>'
    '<span class="hd-gloss">ĐÚNG — gốc của <b>пра́вильно</b>, <b>пра́вда</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tờ giấy xác nhận một điều là ĐÚNG ⇒ giấy chứng nhận (đi học, nghỉ '
    'ốm, nơi ở); rộng ra là thông tin tra cứu. Số nhiều cách 2 chen thêm <b>о</b>: '
    '<b>спра́вок</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пра́вильно</b> đúng · <b>пра́вда</b> sự thật · '
    '<b>спра́вочник</b> sách tra cứu</div>'
)

# ---------------------------------------------------------------- ударение
S["ударение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">удар-</span>'
    '<span class="hd-gloss">CÚ ĐÁNH — chính là <b>уда́р</b>, <b>уда́рить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ние</span>'
    '<span class="hd-gloss">đuôi danh từ → giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cú đánh» giáng vào một âm tiết ⇒ trọng âm — y như tiếng Anh gọi là '
    '<i>stress</i>. Âm tiết mang nó gọi là <b>уда́рный</b>.</div>'
    '<div class="hd-warn">Cụm phải thuộc: <b>ударе́ние па́дает на</b> + cách 4 = trọng âm rơi '
    'vào… — <b>на пе́рвый слог</b> (âm tiết đầu).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уда́р</b> cú đánh · <b>уда́рить</b> đánh · <b>уда́рный</b> mang '
    'trọng âm</div>'
)


# ---------------------------------------------------------------------------
# V — đề bài deck 1-go. Chỉ những từ cần sửa.
V = {
    # Luồng chính: 'bài tập' thuộc упражнение (k57). 'giao việc' là động từ, không phải
    # nghĩa của danh từ — đổi thành 'việc được giao' (task / assignment).
    "задание": "nhiệm vụ, việc được giao",
    # Luồng chính: 'thông báo' thuộc объявлять/объявить/объявление (k77/k52).
    "сообщать": "báo tin, cho biết",
    "сообщить": "báo tin, cho biết",
    "сообщение": "tin nhắn, tin báo, sự liên lạc",
    # Trục lô: 'hoàn thành' thuộc закончить/заканчивать (k95); окончить đã rút về 'tốt nghiệp'.
    "оканчивать": "tốt nghiệp",
    # 'học viên cao học' là học viên thạc sĩ = магистрант; аспирант là nghiên cứu sinh.
    "аспирант": "nghiên cứu sinh",
    # Cũ trùng 'nghiên cứu sinh' với аспирант — đó là NGƯỜI, còn từ này là BẬC HỌC.
    "аспирантура": "bậc nghiên cứu sinh",
    # 'bác sĩ tâm lý' sai nghề: психолог không phải bác sĩ (bác sĩ là психиатр).
    "психолог": "nhà tâm lý học, chuyên gia tâm lý",
    # Tiếng Anh có bell / doorbell mà đề bài chỉ có 'tiếng chuông'.
    "звонок": "cuộc gọi, cái chuông, tiếng chuông",
}
