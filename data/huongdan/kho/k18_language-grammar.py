# -*- coding: utf-8 -*-
"""k18 — language::grammar: tám giới từ, trục là CÁCH mà mỗi giới từ chi phối.

Phần lớn là hư từ gốc trơn (không chẻ được, nói thẳng ra), nhưng chúng sống lại
làm TIỀN TỐ động từ cùng nghĩa — đó là chỗ mục "Họ hàng" trả về nhiều nhất.
"""

# 🔴 KHÔNG dựng biến khối dùng chung (HE/LUAT/THE…) rồi cộng vào mọi thẻ (README §3).

S = {}

# ---------------------------------------------------------------- к (+ cách 3)
S["к"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Hư từ một chữ cái, không chẻ được — đừng tìm mảnh.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mũi tên chạy <b>tới GẦN</b> rồi dừng lại ở bên ngoài: '
    '<b>к до́му</b> tới sát nhà (chưa vào trong), <b>к пяти́</b> tới trước 5 giờ. '
    'Chỉ đi với <b>cách 3</b>, không có cách thứ hai — dễ nhất trong nhóm giới từ.</div>'
    '<div class="hd-warn">⚠️ Đi tới chỗ NGƯỜI thì bắt buộc <b>к</b>, không dùng в/на: '
    '<b>идти́ к врачу́</b> đi khám bác sĩ.</div>'
    '<div class="hd-warn">⚠️ Thuộc nguyên cụm: <b>к сожале́нию</b> tiếc là… · '
    '<b>к сло́ву</b> nhân tiện. Trước мне thì dài ra thành <b>ко</b>: <b>ко мне</b> tới chỗ tôi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">Không có động từ nào lấy к làm tiền tố, nhưng có mấy trạng từ '
    'đông cứng từ đúng công thức к + cách 3: <b>кста́ти</b> nhân tiện · '
    '<b>кве́рху</b> lên phía trên · <b>кни́зу</b> xuống phía dưới.</div>'
)

# ------------------------------------------------ о / об / обо (+ cách 6, 4)
S["о"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Hư từ một chữ cái, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hình gốc là <b>đi vòng quanh</b> một vật. Vòng quanh bằng lời '
    'chính là nói VỀ nó: <b>ду́мать о рабо́те</b> nghĩ về công việc — <b>cách 6</b>.</div>'
    '<div class="hd-warn">⚠️ Đập VÀO bề mặt thì cùng chữ đó nhảy sang <b>cách 4</b>: '
    '<b>уда́риться о сте́ну</b> đâm vào tường. Cách nào là nghĩa nấy.</div>'
    '<div class="hd-warn">⚠️ Trước nguyên âm phải viết <b>об</b>: <b>об э́том</b> về chuyện này; '
    'riêng trước мне thì dài thêm một chữ — обо мне về tôi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">Làm tiền tố thì <b>о-/об-</b> giữ nguyên nghĩa vòng quanh: '
    '<b>обойти́</b> đi vòng qua · <b>осмотре́ть</b> xem xét khắp lượt · <b>обду́мать</b> nghĩ kỹ mọi mặt.</div>'
)

# --------------------------------------------------------------- до (+ cách 2)
S["до"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Hư từ một âm tiết, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chạy tới <b>vạch giới hạn rồi dừng</b>, không vượt qua: '
    '<b>до до́ма</b> tới tận nhà, <b>до пяти́</b> trước 5 giờ. Luôn <b>cách 2</b>.</div>'
    '<div class="hd-warn">⚠️ <b>до свида́ния</b> nghĩa đen là “cho tới lúc gặp lại” — '
    '<b>свида́ния</b> đứng ở cách 2, đúng luật trên chứ không phải cụm học vẹt.</div>'
    '<div class="hd-warn">⚠️ Đừng lẫn với перед: <b>до обе́да</b> bất kỳ lúc nào trước bữa trưa · '
    '<b>пе́ред обе́дом</b> ngay sát bữa trưa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">Tiền tố <b>до-</b> = làm TỚI HẾT, tới đích: <b>дойти́</b> đi tới nơi · '
    '<b>дочита́ть</b> đọc nốt đến cuối · <b>доде́лать</b> làm cho xong.</div>'
)

# --------------------------------------------------------------- по (+ cách 3)
S["по"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Hư từ một âm tiết, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vẽ cái gì đó <b>trải trên bề mặt</b>: <b>идти́ по у́лице</b> đi dọc phố. '
    'Từ hình đó ra hai nghĩa hay gặp — qua phương tiện <b>по телефо́ну</b> và lặp theo lịch '
    '<b>по понеде́льникам</b> các thứ hai. Cả ba đều <b>cách 3</b>.</div>'
    '<div class="hd-warn">⚠️ Chỗ hiếm hoi по đổi cách: khoảng “từ… đến hết” thì lấy '
    '<b>cách 4</b> — <b>с пе́рвого по пя́тое</b> từ mùng 1 đến hết mùng 5.</div>'
    '<div class="hd-warn">⚠️ Thuộc nguyên cụm: <b>по кра́йней ме́ре</b> ít nhất là… · '
    '<b>по-мо́ему</b> theo tôi thấy.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">Tiền tố <b>по-</b> thêm nét “một lát”: <b>погуля́ть</b> đi dạo một lát · '
    '<b>поговори́ть</b> nói chuyện một lúc. Còn <b>по-</b> + trạng từ cho kiểu cách: <b>по-ру́сски</b> theo lối Nga.</div>'
)

# ------------------------------------------------------- с / со (+ cách 5, 2)
S["с"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Hư từ một chữ cái, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hai nghĩa hay gặp ngược hẳn nhau, phân biệt hoàn toàn bằng CÁCH: '
    '<b>cách 5</b> = cùng với (<b>ко́фе с молоко́м</b> cà phê sữa) · '
    '<b>cách 2</b> = từ trên xuống, rời khỏi (<b>с рабо́ты</b> từ chỗ làm về).</div>'
    '<div class="hd-warn">⚠️ Cặp đối xứng đáng thuộc: đi bằng <b>на</b> thì về bằng <b>с</b>, '
    'đi bằng <b>в</b> thì về bằng <b>из</b> — <b>на рабо́ту</b> → <b>с рабо́ты</b>.</div>'
    '<div class="hd-warn">⚠️ Trước cụm phụ âm thì dài ra thành <b>со</b>: <b>со мной</b> với tôi · '
    '<b>со стола́</b> khỏi mặt bàn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">Tiền tố <b>с-</b> giữ cả hai nghĩa: <b>сойти́</b> bước xuống khỏi · '
    '<b>снять</b> gỡ ra, cởi ra · <b>собра́ть</b> gom lại một chỗ.</div>'
)

# ---------------------------------------------------------------- у (+ cách 2)
S["у"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Hư từ một chữ cái, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đặt vật <b>sát cạnh</b> ai/cái gì: <b>у окна́</b> cạnh cửa sổ. '
    'Luôn <b>cách 2</b>, không có cách thứ hai.</div>'
    '<div class="hd-warn">⚠️ Tiếng Nga không nói “tôi có” mà nói “ở chỗ tôi có”: '
    '<b>у меня́ есть маши́на</b>. Phủ định đổi sang нет + cách 2: <b>у меня́ нет маши́ны</b>.</div>'
    '<div class="hd-warn">⚠️ Lấy/hỏi TỪ ai cũng là у: <b>спроси́ть у дру́га</b> hỏi bạn · '
    '<b>взять у бра́та</b> mượn của anh. Ngược với <b>к дру́гу</b> = đi tới chỗ bạn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">Tiền tố <b>у-</b> = rời đi cho khuất: <b>уйти́</b> bỏ đi · '
    '<b>уе́хать</b> rời đi bằng xe · <b>убра́ть</b> dọn đi chỗ khác.</div>'
)

# ----------------------------------------------------------- между (+ cách 5)
S["между"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">меж-</span>'
    '<span class="hd-gloss">KHOẢNG GIỮA, ranh giới</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ду</span>'
    '<span class="hd-gloss">đuôi cũ, nay không mang nghĩa riêng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đứng ở khoảng giữa hai bên và bắt cả hai bên vào <b>cách 5</b>, nối bằng и: '
    '<b>ме́жду до́мом и шко́лой</b> giữa nhà và trường.</div>'
    '<div class="hd-warn">⚠️ Giữa một đám nhiều thứ thì phải đổi từ: <b>среди́</b> + cách 2 — '
    '<b>среди́ друзе́й</b> trong đám bạn bè. <b>ме́жду</b> chỉ dùng cho hai bên.</div>'
    '<div class="hd-warn">⚠️ Vài cụm cổ còn giữ cách 2, học nguyên cụm đừng suy: '
    '<b>ме́жду строк</b> giữa hai dòng chữ · <b>ме́жду двух огне́й</b> tiến thoái lưỡng nan.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>междунаро́дный</b> quốc tế, nghĩa đen “giữa các dân tộc” · '
    '<b>промежу́ток</b> khoảng trống giữa hai điểm.</div>'
)

# ---------------------------------------------------------- вместо (+ cách 2)
S["вместо"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ме́сто</span>'
    '<span class="hd-gloss">CHỖ, vị trí</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen là bước <b>vào chỗ</b> của cái khác ⇒ thay cho nó. '
    'Thứ bị thay đứng ở <b>cách 2</b>: <b>вме́сто меня́</b> thay cho tôi · '
    '<b>вме́сто ча́я</b> thay vì trà.</div>'
    '<div class="hd-warn">⚠️ Lệch một chữ cái là lệch hẳn nghĩa lẫn cách: '
    '<b>вме́сто нас</b> thay cho chúng tôi (cách 2) ≠ <b>вме́сте с на́ми</b> cùng với chúng tôi '
    '(с + cách 5).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ме́сто</b> chỗ, nơi · <b>вме́сте</b> cùng nhau · '
    '<b>ме́стный</b> thuộc địa phương.</div>'
)


# ============================================================================
# V — sửa field `Vietnamese` (README §2c).
# Cả 8 từ đều mang PoS = oth ⇒ badge chỉ hiện "oth", vô dụng ⇒ VẪN phải ghi
# "giới từ". Và CÁCH mà giới từ chi phối thì không field nào chứa — mà chính nó
# là thứ tách được các nghĩa Việt trùng nhau ("đến", "về", "ở", "với", "giữa").
V = {}

V['к'] = 'đến chỗ, tới, hướng về phía'
V['о'] = 'về, nói về, va vào'
V['до'] = 'cho tới, đến, trước lúc'
V['по'] = 'theo, dọc theo, qua, vào'
V['с'] = 'cùng với, từ chỗ, khỏi'
V['у'] = 'ở chỗ, cạnh, bên'
V['между'] = 'ở giữa, giữa'
V['вместо'] = 'thay cho, thay vì'
