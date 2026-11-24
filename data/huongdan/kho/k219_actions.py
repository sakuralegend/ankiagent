# -*- coding: utf-8 -*-
"""k219 — actions: 9 cặp thể + сформировать, формироваться, продемонстрировать, отрывок; trục là GỐC + TIỀN TỐ.

Chỗ cần nhất quán trong lô:
(1) раздавать/раздать: раз- RA CÁC PHÍA + да- CHO — khớp разбить k80, выдавать/выдать k187.
(2) забивать/забить: за- VÀO SÂU, LẤP KÍN + би-/бь- ĐÁNH — khớp бить k02.
(3) обменивать/обменять: об- VÒNG QUA + мен- ĐỔI — khớp обмен k131, менять k95.
(4) ограничивать/ограничить: о- BAO QUANH + гранич- BIÊN — khớp ограничение k189.
(5) сформировать/формироваться: форм- HÌNH, KHUÔN — khớp форма k07, формирование k169.
(6) вкладывать/вложить, укладывать/уложить: клад- / лож- hai gốc khác nhau — khớp складывать/сложить k195.
(7) оторвать/отрывать/отрывок: от- RỜI RA + рв-/рыв- XÉ, GIẬT — khớp сорвать/срывать k212.
(8) выписать/выписывать: вы- RA + пис- VIẾT — luật вы́- mang nhấn khớp вытащить k171.
Họ hàng cố ý vắng: không có (mọi từ đều có họ thật).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "забивать": "đóng vào, ghi bàn, làm tắc, bịt kín, nhồi đầy",      # + clog, board up, cram; «đập vào» mơ hồ
    "забить": "đóng vào, ghi bàn, làm tắc, bịt kín, nhồi đầy",
    "обменивать": "đổi, trao đổi, đổi lấy",                           # khớp обменять; gỡ luôn va chạm менять
    "ограничивать": "hạn chế, giới hạn",                              # «đặt giới hạn» lặp ý
    "ограничить": "hạn chế, giới hạn",                                # «giảm bớt» là nới rộng
    "реагировать": "phản ứng, đáp lại",                               # «hồi đáp» lặp «đáp lại»
    "продемонстрировать": "trình diễn, giới thiệu, thể hiện",         # khớp демонстрировать k207
    "вложить": "đầu tư, bỏ vào, cho vào, kèm vào",                    # khớp вкладывать
    "укладывать": "cho đi ngủ, dỗ ngủ, đặt xuống, xếp vào",
    "уложить": "cho đi ngủ, dỗ ngủ, đặt xuống, xếp vào",
    "отрывать": "xé ra, bóc ra, làm đứt, tách ra",                    # khớp оторвать
    "выписать": "chép ra, ghi ra, trích ra, kê đơn, cho xuất viện, đặt mua",   # + make out, discharge, subscribe
    "выписывать": "chép ra, ghi ra, trích ra, kê đơn, cho xuất viện, đặt mua",
    "отрывок": "đoạn trích, đoạn",                                    # «mẩu» là обрывок; «trích đoạn» lặp
}

# ------------------------------------------------------------------- раздавать
S["раздавать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раз-</span>'
    '<span class="hd-gloss">RA CÁC PHÍA — như <b>разби́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-да-</span>'
    '<span class="hd-gloss">CHO — như <b>дать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва́-ть</span>'
    '<span class="hd-gloss">hậu tố «đang / hay làm» → CHT</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cho ra các phía, mỗi người một phần ⇒ phát, chia. Vật phát ở cách 4, '
    'người nhận ở cách 3: <b>раздава́ть де́тям кни́ги</b>. Như <b>дава́ть</b>, hiện tại BỎ '
    '<i>-ва-</i>: <b>раздаю́, раздаёшь</b>. Cặp HT: <b>разда́ть</b>.</div>'
    '<div class="hd-warn"><b>раздава́ть интерне́т</b> = phát mạng từ điện thoại mình cho máy '
    'khác dùng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>разда́ть</b> (HT) · <b>разда́ча</b> sự phân phát · '
    '<b>дава́ть</b> cho · <b>выдава́ть</b> cấp, phát</div>'
)

# --------------------------------------------------------------------- раздать
S["раздать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раз-</span>'
    '<span class="hd-gloss">RA CÁC PHÍA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-да́ть</span>'
    '<span class="hd-gloss">CHO — chính là <b>дать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Phát xong, chia hết: <b>разда́ть ка́рты</b> chia bài, <b>разда́ть '
    'тетра́ди</b> phát vở. Cặp CHT: <b>раздава́ть</b>.</div>'
    '<div class="hd-why">Bảng bất quy tắc, chép y <b>дать</b>: <b>разда́м · разда́шь · разда́ст</b>, '
    'số nhiều nhấn đuôi <b>раздади́м · раздади́те · раздаду́т</b>; quá khứ giống cái '
    '<b>раздала́</b>.</div>'
    '<div class="hd-warn">Thêm <i>-ся</i> là nghĩa khác: <b>разда́ться</b> = (tiếng động) vang lên — '
    '<b>Разда́лся звоно́к.</b> Chuông reo lên.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>раздава́ть</b> (CHT) · <b>разда́ча</b> sự phân phát · '
    '<b>отда́ть</b> đưa lại · <b>переда́ть</b> chuyển, trao lại</div>'
)

# -------------------------------------------------------------------- забивать
S["забивать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">VÀO SÂU, LẤP KÍN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-би-</span>'
    '<span class="hd-gloss">ĐÁNH, ĐẬP — như <b>бить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва́-ть</span>'
    '<span class="hd-gloss">hậu tố «đang / hay làm» → CHT</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đánh cho VÀO ⇒ đóng đinh, đưa bóng vào lưới: <b>забива́ть гво́зди</b>, '
    '<b>забива́ть голы́</b>. Đánh cho KÍN ⇒ bịt, làm tắc, nhồi đầy. Khác <b>дава́ть</b>, ở đây '
    '<i>-ва-</i> Ở LẠI khi chia: <b>забива́ю, забива́ешь</b>. Cặp HT: <b>заби́ть</b>.</div>'
    '<div class="hd-warn">Chỉ lệch một chữ với <b>забыва́ть</b> (quên): <i>би</i> ĐÁNH ↔ '
    '<i>бы</i> của <b>забы́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>заби́ть</b> (HT) · <b>бить</b> đánh · <b>убива́ть</b> giết · '
    '<b>разбива́ть</b> đập vỡ</div>'
)

# ---------------------------------------------------------------------- забить
S["забить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">VÀO SÂU, LẤP KÍN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-би́ть</span>'
    '<span class="hd-gloss">ĐÁNH, ĐẬP — chính là <b>бить</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đánh cho VÀO, cho KÍN xong: <b>заби́ть гол</b> ghi bàn, <b>заби́ть '
    'гвоздь</b> đóng đinh, <b>заби́ть холоди́льник</b> nhét đầy tủ lạnh. Chia như <b>бить</b>, '
    '<i>и</i> rút thành <i>ь</i>: <b>забью́, забьёшь</b>; mệnh lệnh <b>забе́й</b>. '
    'Cặp CHT: <b>забива́ть</b>.</div>'
    '<div class="hd-warn">Khẩu ngữ, suồng sã: <b>заби́ть на</b> + cách 4 = mặc kệ, bỏ bê — '
    '<b>Забе́й!</b> Kệ đi!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>забива́ть</b> (CHT) · <b>бить</b> đánh · <b>уби́ть</b> giết · '
    '<b>разби́ть</b> đập vỡ</div>'
)

# ------------------------------------------------------------------ обменивать
S["обменивать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">VÒNG QUA — như <b>обме́н</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ме́н-</span>'
    '<span class="hd-gloss">ĐỔI — gốc của <b>меня́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ть</span>'
    '<span class="hd-gloss">thể chưa hoàn thành, chia đều: <b>обме́ниваю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đưa một thứ đi, lấy thứ khác về: <b>обме́нивать де́ньги</b> đổi tiền. '
    'Cặp HT: <b>обменя́ть</b>. Nhìn <i>-ива-</i> là biết thể CHT; trọng âm lùi về gốc '
    '<i>-ме́н-</i>.</div>'
    '<div class="hd-warn">Hai bên đổi cho nhau thì thêm <i>-ся</i>, vật đổi ở cách 5: '
    '<b>обме́ниваться пи́сьмами</b> trao đổi thư từ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обменя́ть</b> (HT) · <b>обме́н</b> sự trao đổi · '
    '<b>обме́нник</b> quầy đổi tiền · <b>меня́ть</b> đổi</div>'
)

# -------------------------------------------------------------------- обменять
S["обменять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">VÒNG QUA — như <b>обме́н</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-меня́ть</span>'
    '<span class="hd-gloss">ĐỔI — chính là <b>меня́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đổi xong một vụ. <b>меня́ть</b> là CHT, nhưng gắn <i>об-</i> vào thì thành '
    'HT; chiều CHT phải dựng thêm <i>-ива-</i>: <b>обме́нивать</b>. Chia đều: <b>обменя́ю, '
    'обменя́ешь</b>.</div>'
    '<div class="hd-warn">Đổi X LẤY Y: cách 4 + <b>на</b> + cách 4 — <b>обменя́ть рубли́ на '
    'до́ллары</b>.</div>'
    '<div class="hd-warn">Đừng lẫn <b>обману́ть</b> (lừa): <i>мен</i> ĐỔI ↔ <i>ман</i> LỪA.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обме́нивать</b> (CHT) · <b>обме́н</b> sự trao đổi · '
    '<b>поменя́ть</b> đổi · <b>замени́ть</b> thay thế</div>'
)

# ---------------------------------------------------------------- ограничивать
S["ограничивать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">BAO QUANH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-грани́ч-</span>'
    '<span class="hd-gloss">BIÊN, MÉP — <b>грани́ца</b>, <i>ц → ч</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ть</span>'
    '<span class="hd-gloss">thể chưa hoàn thành, chia đều: <b>ограни́чиваю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vạch một đường biên bao quanh ⇒ giới hạn, hạn chế. Thứ bị hạn chế ở '
    'cách 4: <b>ограни́чивать ско́рость</b> hạn chế tốc độ. Trọng âm đứng yên ở <i>-ни́-</i>. '
    'Cặp HT: <b>ограни́чить</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ограни́чить</b> (HT) · <b>ограниче́ние</b> sự hạn chế · '
    '<b>грани́ца</b> biên giới · <b>безграни́чный</b> vô bờ bến</div>'
)

# ------------------------------------------------------------------ ограничить
S["ограничить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">BAO QUANH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-грани́ч-</span>'
    '<span class="hd-gloss">BIÊN, MÉP — <b>грани́ца</b>, <i>ц → ч</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai: <b>ограни́чу, ограни́чишь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vạch biên cho xong ⇒ đặt ra mức hạn chế. Cặp CHT <b>ограни́чивать</b> chỉ '
    'khác khúc <i>-ива-</i>, trọng âm hai bên cùng chỗ.</div>'
    '<div class="hd-warn">Hạn chế AI ở khoản gì: người ở cách 4, khoản đó <b>в</b> + cách 6 — '
    '<b>ограни́чить себя́ в сла́дком</b> bớt ăn ngọt.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ограни́чивать</b> (CHT) · <b>ограниче́ние</b> sự hạn chế · '
    '<b>ограни́ченный</b> hạn hẹp · <b>грани́ца</b> biên giới</div>'
)

# --------------------------------------------------------------- отреагировать
S["отреагировать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">tiền tố thể, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-реаги́ровать</span>'
    '<span class="hd-gloss">PHẢN ỨNG — chính là <b>реаги́ровать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một lần phản ứng đã xảy ra: <b>Как он отреаги́ровал?</b> Anh ta phản ứng '
    'ra sao? Chia y <b>реаги́ровать</b>, <i>-ова-</i> thành <i>-у-</i>: <b>отреаги́рую, '
    'отреаги́руешь</b>.</div>'
    '<div class="hd-warn">Phản ứng TRƯỚC cái gì: <b>на</b> + cách 4 — <b>отреаги́ровать на '
    'шу́тку</b> phản ứng trước câu đùa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>реаги́ровать</b> (CHT) · <b>реа́кция</b> phản ứng · '
    '<b>реакти́вный</b> thuộc phản lực</div>'
)

# ----------------------------------------------------------------- реагировать
S["реагировать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ре-</span>'
    '<span class="hd-gloss">= Anh <i>re-</i>, ĐÁP LẠI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-аг-</span>'
    '<span class="hd-gloss">LÀM — Latin <i>agere</i>, Anh là <i>act</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ровать</span>'
    '<span class="hd-gloss">đuôi động từ mượn</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng là <i>re-act</i>: làm đáp lại ⇒ phản ứng. Khi chia, <i>-ова-</i> thành '
    '<i>-у-</i>: <b>реаги́рую, реаги́руешь</b>. Cặp HT: <b>отреаги́ровать</b>.</div>'
    '<div class="hd-warn">Đi với <b>на</b> + cách 4: <b>Не реаги́руй на него́!</b> Đừng phản ứng '
    'lại hắn!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отреаги́ровать</b> (HT) · <b>реа́кция</b> phản ứng · '
    '<b>реа́ктор</b> lò phản ứng</div>'
)

# ---------------------------------------------------------------- сформировать
S["сформировать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">tiền tố thể, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-форм-</span>'
    '<span class="hd-gloss">HÌNH, KHUÔN — chính là <b>фо́рма</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ирова́ть</span>'
    '<span class="hd-gloss">đuôi động từ mượn</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúc cho thành hình, như Anh <i>form</i>: <b>сформирова́ть кома́нду</b> lập '
    'đội, <b>сформирова́ть привы́чку</b> tạo thói quen. Nguyên thể nhấn đuôi, khi chia nhấn '
    '<i>-у́-</i>: <b>сформиру́ю, сформиру́ешь</b>. Cặp CHT: <b>формирова́ть</b>.</div>'
    '<div class="hd-warn">Đừng lẫn <b>сформули́ровать</b>: gốc là <i>formula</i> — phát biểu, diễn '
    'đạt thành lời.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>формирова́ть</b> (CHT) · <b>формирова́ние</b> sự hình thành · '
    '<b>фо́рма</b> hình dạng · <b>рефо́рма</b> cải cách</div>'
)

# ---------------------------------------------------------- продемонстрировать
S["продемонстрировать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">tiền tố thể, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-демонстр-</span>'
    '<span class="hd-gloss">= Anh <i>demonstr-</i> (Latin «chỉ ra»)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ровать</span>'
    '<span class="hd-gloss">= Anh <i>-ate</i>, đuôi động từ mượn</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp HT của <b>демонстри́ровать</b>: cho người ta THẤY xong một lần. '
    'Chia y hệt, <i>-ова-</i> thành <i>-у-</i>: <b>продемонстри́рую, продемонстри́руешь</b>.</div>'
    '<div class="hd-warn">Cho AI xem: người xem ở cách 3 — <b>продемонстри́ровать това́р '
    'покупа́телям</b> giới thiệu hàng với khách.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>демонстри́ровать</b> (CHT) · <b>демонстра́ция</b> sự trình diễn; '
    'cuộc biểu tình</div>'
)

# ------------------------------------------------------------------ вкладывать
S["вкладывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO TRONG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-кла́д-</span>'
    '<span class="hd-gloss">ĐẶT — gốc của <b>класть</b>, <b>кладу́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-ть</span>'
    '<span class="hd-gloss">thể chưa hoàn thành, chia đều: <b>вкла́дываю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đặt VÀO TRONG ⇒ bỏ vào, kèm vào; đặt tiền vào ⇒ đầu tư. Cặp HT '
    '<b>вложи́ть</b> dùng gốc KHÁC (<i>-лож-</i>) — y như <b>класть / положи́ть</b>.</div>'
    '<div class="hd-warn">Vào đâu thì lặp lại <b>в</b> + cách 4: <b>вкла́дывать де́ньги в '
    'би́знес</b> đầu tư vào kinh doanh; <b>вкла́дывать ду́шу в рабо́ту</b> dồn tâm huyết '
    'vào công việc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вложи́ть</b> (HT) · <b>вклад</b> sự đóng góp, tiền gửi · '
    '<b>вкла́дка</b> thẻ (trình duyệt) · <b>скла́дывать</b> xếp, gấp</div>'
)

# --------------------------------------------------------------------- вложить
S["вложить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO TRONG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лож-</span>'
    '<span class="hd-gloss">làm cho NẰM ⇒ ĐẶT — gốc của <b>положи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đặt vào trong xong: <b>вложи́ть письмо́ в конве́рт</b> cho thư vào phong bì, '
    '<b>вложи́ть де́ньги</b> đầu tư. Cặp CHT <b>вкла́дывать</b> mang gốc khác.</div>'
    '<div class="hd-why">Trọng âm lùi y <b>положи́ть</b>: «tôi» nhấn đuôi <b>вложу́</b>, các ngôi sau '
    'nhấn gốc <b>вло́жишь, вло́жат</b>.</div>'
    '<div class="hd-warn"><b>вложе́ние</b> trong email = tệp đính kèm; trong tiền bạc = khoản '
    'đầu tư.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вкла́дывать</b> (CHT) · <b>вложе́ние</b> khoản đầu tư, tệp kèm · '
    '<b>положи́ть</b> đặt · <b>отложи́ть</b> hoãn</div>'
)

# ------------------------------------------------------------------ укладывать
S["укладывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">ở đây: cho YÊN CHỖ, gọn vào — không phải RỜI KHỎI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-кла́д-</span>'
    '<span class="hd-gloss">ĐẶT NẰM — gốc của <b>класть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-ть</span>'
    '<span class="hd-gloss">thể chưa hoàn thành, chia đều: <b>укла́дываю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đặt nằm cho yên, cho gọn: đặt trẻ xuống ⇒ cho ngủ; đặt đồ vào vali ⇒ xếp '
    'gọn. Cặp HT <b>уложи́ть</b> dùng gốc khác (<i>-лож-</i>) — như <b>класть / '
    'положи́ть</b>.</div>'
    '<div class="hd-warn"><b>укла́дывать дете́й спать</b> cho bọn trẻ đi ngủ · <b>укла́дывать '
    'ве́щи в чемода́н</b> xếp đồ vào vali · <b>укла́дывать во́лосы</b> làm tóc, tạo kiểu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уложи́ть</b> (HT) · <b>укла́дка</b> việc xếp, lát; kiểu tóc · '
    '<b>класть</b> đặt nằm · <b>вкла́дывать</b> bỏ vào</div>'
)

# --------------------------------------------------------------------- уложить
S["уложить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">ở đây: cho YÊN CHỖ, gọn vào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лож-</span>'
    '<span class="hd-gloss">làm cho NẰM ⇒ ĐẶT — gốc của <b>положи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đặt nằm cho yên xong: <b>уложи́ть ребёнка</b> cho bé ngủ, <b>уложи́ть '
    'чемода́н</b> xếp xong vali. Trọng âm lùi y <b>положи́ть</b>: <b>уложу́</b> nhưng <b>уло́жишь, '
    'уло́жат</b>. Cặp CHT: <b>укла́дывать</b>.</div>'
    '<div class="hd-warn">Thêm <i>-ся</i> có nghĩa «gọn vừa trong»: <b>уложи́ться в срок</b> = xong '
    'kịp hạn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>укла́дывать</b> (CHT) · <b>ложи́ться</b> nằm xuống · '
    '<b>сложи́ть</b> xếp, gấp · <b>вложи́ть</b> cho vào</div>'
)

# -------------------------------------------------------------------- оторвать
S["оторвать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ото-</span>'
    '<span class="hd-gloss">= <i>от-</i> RỜI RA; thêm <i>о</i> đệm trước <i>рв</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-рв-</span>'
    '<span class="hd-gloss">XÉ, GIẬT — chính là <b>рвать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi động từ; <i>а</i> rơi khi chia: <b>оторву́, оторвёшь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giật cho RỜI khỏi chỗ đang dính ⇒ xé ra, bóc ra, làm đứt: '
    '<b>оторва́ть пу́говицу</b> làm đứt cúc. Quá khứ chỉ giống cái nhấn đuôi: <b>оторвала́</b>. '
    'Cặp CHT: <b>отрыва́ть</b>.</div>'
    '<div class="hd-warn"><b>Глаз не оторва́ть!</b> Đẹp không rời mắt được!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отрыва́ть</b> (CHT) · <b>отры́вок</b> đoạn trích · <b>рвать</b> xé · '
    '<b>сорва́ть</b> giật ra, hái</div>'
)

# -------------------------------------------------------------------- отрывать
S["отрывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">RỜI RA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-рыв-</span>'
    '<span class="hd-gloss">XÉ, GIẬT — thân dài của <b>рвать</b>, như <b>взрыв</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành, chia đều: <b>отрыва́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>оторва́ть</b>: xé tờ lịch, bóc nhãn khỏi hộp. Gốc giãn '
    '<i>рв → рыв</i> nên hết cần <i>о</i> đệm. Rời khỏi đâu thì <b>от</b> + cách 2: '
    '<b>отрыва́ть ярлы́к от игру́шки</b> bóc nhãn khỏi đồ chơi.</div>'
    '<div class="hd-warn">Nghĩa bóng, «giật» ai khỏi việc đang làm: <b>Не отрыва́й меня́ от '
    'рабо́ты!</b> Đừng làm gián đoạn việc của tôi!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оторва́ть</b> (HT) · <b>отры́вок</b> đoạn trích · '
    '<b>срыва́ть</b> giật ra · <b>переры́в</b> giờ nghỉ</div>'
)

# -------------------------------------------------------------------- выписать
S["выписать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы́-</span>'
    '<span class="hd-gloss">RA NGOÀI — ở thể HT luôn mang trọng âm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пис-ать</span>'
    '<span class="hd-gloss">VIẾT — chính là <b>писа́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Viết RA: chép từ sách ra sổ; viết ra tờ giấy đưa cho ai ⇒ kê đơn; viết giấy '
    'cho RA khỏi viện ⇒ cho xuất viện; viết phiếu đặt báo ⇒ đặt mua. <i>с → ш</i> ở mọi ngôi như '
    '<b>писа́ть</b>, nhấn đứng yên ở <i>вы́-</i>: <b>вы́пишу, вы́пишешь</b>. '
    'Cặp CHT: <b>выпи́сывать</b>.</div>'
    '<div class="hd-warn"><b>вы́писать реце́пт</b> kê đơn thuốc · <b>Его́ вы́писали из '
    'больни́цы.</b> Anh ấy được xuất viện.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>выпи́сывать</b> (CHT) · <b>вы́писка</b> bản trích, sao kê; sự xuất viện · '
    '<b>писа́ть</b> viết · <b>подписа́ть</b> ký</div>'
)

# ------------------------------------------------------------------ выписывать
S["выписывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span>'
    '<span class="hd-gloss">RA NGOÀI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пи́с-</span>'
    '<span class="hd-gloss">VIẾT — gốc của <b>писа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-ть</span>'
    '<span class="hd-gloss">thể chưa hoàn thành, chia đều: <b>выпи́сываю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>вы́писать</b> — các nghĩa xem ở thẻ đó. Thêm <i>-ыва-</i> thì '
    'nhấn rời <i>вы-</i> sang <i>-пи́-</i>, và <i>с</i> giữ nguyên, không thành <i>ш</i>. Chép RA TỪ '
    'đâu: <b>из</b> + cách 2 — <b>выпи́сывать слова́ из те́кста</b>.</div>'
    '<div class="hd-warn"><b>Врач выпи́сывает лека́рство.</b> Bác sĩ đang kê thuốc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вы́писать</b> (HT) · <b>вы́писка</b> bản trích, sao kê · '
    '<b>запи́сывать</b> ghi lại · <b>опи́сывать</b> mô tả</div>'
)

# --------------------------------------------------------------- формироваться
S["формироваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">форм-</span>'
    '<span class="hd-gloss">HÌNH, KHUÔN — chính là <b>фо́рма</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ирова́ть</span>'
    '<span class="hd-gloss">đuôi động từ mượn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">việc xảy ra với chính nó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>формирова́ть</b> là tạo ra cái khác; thêm <i>-ся</i> là tự nó thành hình: '
    '<b>Хара́ктер формиру́ется в де́тстве.</b> Tính cách hình thành từ bé. <i>-ова-</i> thành '
    '<i>-у́-</i>: <b>формиру́юсь, формиру́ешься</b>. Cặp HT: <b>сформирова́ться</b>.</div>'
    '<div class="hd-warn"><b>формирова́ться под влия́нием</b> + cách 2 = hình thành dưới ảnh hưởng '
    'của…</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сформирова́ть</b> tạo thành (HT) · <b>формирова́ние</b> sự hình thành · '
    '<b>фо́рма</b> hình dạng · <b>рефо́рма</b> cải cách</div>'
)

# --------------------------------------------------------------------- отрывок
S["отрывок"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">RỜI RA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ры́в-</span>'
    '<span class="hd-gloss">XÉ, GIẬT — như <b>отрыва́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ок</span>'
    '<span class="hd-gloss">đuôi danh từ giống đực, <i>о</i> rơi khi biến cách</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Miếng «xé rời» khỏi cả cuốn ⇒ đoạn trích. Trích từ đâu: <b>из</b> + cách 2 — '
    '<b>отры́вок из рома́на</b>. Nguyên âm chạy: <i>о</i> mất ở mọi dạng có thêm đuôi — '
    '<b>отры́вка, отры́вком, отры́вки</b>.</div>'
    '<div class="hd-warn">Mẩu giấy bị xé thì là <b>обры́вок</b>; <b>отры́вок</b> là đoạn văn, đoạn '
    'phim, đoạn nhạc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оторва́ть</b> xé ra (HT) · <b>отрыва́ть</b> xé ra (CHT) · '
    '<b>переры́в</b> giờ nghỉ · <b>взрыв</b> vụ nổ</div>'
)

B = {
    "docbangmat": 150,
    "loitubat": 2,
    "nguonsai": 4,
    "baolen": [
        "V cần duyệt (14 thẻ): забивать/забить thống nhất + «làm tắc, bịt kín, nhồi đầy» (bỏ «đập vào», «sút vào»); обменивать + «đổi lấy»; ограничивать/ограничить «hạn chế, giới hạn»; реагировать bỏ «hồi đáp»; продемонстрировать theo демонстрировать k207; вложить theo вкладывать; укладывать/уложить «cho đi ngủ, dỗ ngủ, đặt xuống, xếp vào»; отрывать theo оторвать; выписать/выписывать + «kê đơn, cho xuất viện, đặt mua»; отрывок «đoạn trích, đoạn». 8 thẻ còn lại giữ đề cũ.",
        "Va chạm обменивать ⊂ менять: gỡ bằng «đổi lấy» (vốn có sẵn ở обменять, gloss exchange). Đối chiếu ngoại tuyến (_input + V các lô, KHÔNG gọi Anki) — nên chạy vacham thật.",
        "KHÔNG chắc: «kê đơn» của выписать/выписывать — gloss ghi make out / issue / write out, không có chữ prescribe; nghĩa rất thông dụng (выписать рецепт) nên đưa vào. «xuất hoá đơn» và «xoá tên, xoá hộ khẩu» (deregister, strike off) cố ý bỏ khỏi đề; «cho xuất viện», «đặt mua» gloss xác nhận cả hai thể.",
        "KHÔNG chắc: tiền tố у- của укладывать/уложить ghi «cho YÊN CHỖ, gọn vào» — là cách diễn giải theo nghĩa, gloss không nói.",
        "Cố ý bỏ khỏi đề: забить/забивать «đánh chết, giết mổ, nện»; забить на (lóng, chỉ ở ô đỏ); укладывать/уложить «bắn gục, giết»; «tạo kiểu tóc» (gloss chỉ có ở укладывать, để trong ô đỏ); вкладывать «góp, dồn vào»; отрывать от работы (ô đỏ).",
        "Nguồn sai đã bác (4): забить/забивать «đập vào» (gloss là đóng vào, đánh vào lỗ); ограничить «giảm bớt»; продемонстрировать «biểu diễn»; отрывок «mẩu» (là обрывок). «trích đoạn» bỏ vì lặp, không tính.",
        "loitubat (2): ограничить nói cặp CHT «chỉ dài hơn khúc -ива-» (HT còn có -ить riêng, đổi «chỉ khác»); отрывать dẫn ли́стик от календаря́ — câu tự nhiên là листо́к с календаря́, đổi sang ярлы́к от игру́шки.",
    ],
}
