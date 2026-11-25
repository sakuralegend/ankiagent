# -*- coding: utf-8 -*-
"""k265 — life::food: đồ ăn, đồ nhà bếp + bốn từ nghề; trục là GỐC đã học (вар-, гранич-, груз-, сед-, веш-) + chỗ bảng chia lệch.

Chỗ cần nhất quán với lô đã nạp:
(1) грани́ч- BIÊN, ц → ч: khớp заграничный k248, ограничить k219. (2) груз- HÀNG CHỞ: khớp грузовик k165, груз k177.
(3) обо-зр- NHÌN KHẮP: khớp обзор k211. (4) -рабат- о → а: khớp зарабатывать k183. (5) вар- ĐUN SÔI: khớp варить k102.
(6) на-…-ся THOẢ, ĐÃ: khớp напиться k223. (7) кис-/квас- CHUA, LÊN MEN: khớp кислый k21. (8) бе- / -сед-: khớp беседа k135.
(9) веш- TREO: khớp вешать k131. (10) суш- KHÔ, х → ш: khớp сушить k253. (11) крупа ~ крупный: khớp k41.
Họ hàng cố ý vắng: không có (từ nào cũng có ít nhất một họ thật).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "грузчик": "người bốc xếp, người bốc vác",                 # «công nhân xếp hàng» đọc ra «đứng xếp hàng»
    "обозреватель": "nhà bình luận, người viết chuyên mục",    # «người quan sát» là наблюда́тель
    "сушка": "việc sấy, sự làm khô, bánh vòng khô",            # + dry bagel ring; «chế độ sấy» ngoài gloss
    "буханка": "ổ bánh mì",                        # UAZ van / minibus, không phải xe tải
}

# ---------------------------------------------------------------- пограничник
S["пограничник"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">DỌC THEO, sát bên</span></div>'
    '<div class="hd-row"><span class="hd-piece">-грани́ч-</span>'
    '<span class="hd-gloss">BIÊN — <b>грани́ца</b>, <i>ц → ч</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ник</span>'
    '<span class="hd-gloss">đuôi chỉ NGƯỜI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người đứng dọc biên giới ⇒ lính biên phòng. Đi qua tính từ '
    '<b>пограни́чный</b> «thuộc biên giới»: <b>пограни́чный контро́ль</b> chỗ soát hộ chiếu ở cửa khẩu. '
    'Trọng âm ở <i>-и́-</i> y như <b>грани́ца</b>, đứng yên cả bảng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>грани́ца</b> biên giới · <b>пограни́чный</b> thuộc biên giới · '
    '<b>грани́чить</b> giáp ranh · <b>заграни́чный</b> thuộc nước ngoài</div>'
)

# ------------------------------------------------------------------ граничить
S["граничить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">грани́ч-</span>'
    '<span class="hd-gloss">BIÊN — <b>грани́ца</b>, <i>ц → ч</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai: <b>грани́чу, грани́чишь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Có chung biên ⇒ giáp ranh. Giáp VỚI ai: <b>с</b> + cách 5 — '
    '<b>Росси́я грани́чит с Кита́ем</b>. Là trạng thái kéo dài nên không có cặp hoàn thành.</div>'
    '<div class="hd-warn">Nghĩa bóng «chỉ cách một đường biên» ⇒ gần như là: '
    '<b>сме́лость, кото́рая грани́чит с безу́мием</b> lòng can đảm gần như điên rồ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>грани́ца</b> biên giới · <b>пограни́чник</b> lính biên phòng · '
    '<b>ограни́чить</b> giới hạn lại · <b>безграни́чный</b> vô hạn</div>'
)

# -------------------------------------------------------------------- грузчик
S["грузчик"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">груз-</span>'
    '<span class="hd-gloss">HÀNG CHỞ, vật nặng — <b>груз</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-чик</span>'
    '<span class="hd-gloss">NGƯỜI làm nghề đó — như <b>перево́дчик, лётчик</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người làm việc với hàng nặng ⇒ người bốc vác, ở kho, ở cảng, hay đội chuyển nhà: '
    '<b>заказа́ть гру́зчиков</b> thuê người khuân đồ. Làm nghề gì thì cách 5: '
    '<b>рабо́тать гру́зчиком</b>.</div>'
    '<div class="hd-warn">Người lái xe nâng là nghề khác: <b>води́тель погру́зчика</b> — '
    '<b>погру́зчик</b> là chiếc xe nâng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>груз</b> hàng hoá · <b>грузови́к</b> xe tải · '
    '<b>грузи́ть</b> chất hàng · <b>загрузи́ть</b> chất đầy, tải xuống</div>'
)

# --------------------------------------------------------------- обозреватель
S["обозреватель"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">обо-</span>'
    '<span class="hd-gloss">= <i>об-</i> QUANH, khắp lượt (chen <i>о</i> trước <i>зр</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-зре-ва-</span>'
    '<span class="hd-gloss">NHÌN — <b>зре́ние</b>; <i>-ва-</i> là dấu thể chưa hoàn thành</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тель</span>'
    '<span class="hd-gloss">NGƯỜI làm việc đó — như <b>чита́тель</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người NHÌN KHẮP tình hình rồi viết lại ⇒ nhà bình luận, người giữ chuyên mục: '
    '<b>полити́ческий обозрева́тель</b>. Đuôi <i>-тель</i> chỉ người là giống ĐỰC; nữ làm nghề này '
    'cũng thường ghi <b>обозрева́тель</b>.</div>'
    '<div class="hd-warn">Trên Windows cũ, từ này là «trình duyệt»; ngày nay nói <b>бра́узер</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обзо́р</b> bài tổng quan · <b>обозре́ние</b> bài điểm lại, tạp chí điểm tin · '
    '<b>зре́ние</b> thị lực · <b>зри́тель</b> khán giả</div>'
)

# ------------------------------------------------------------- подрабатывать
S["подрабатывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span>'
    '<span class="hd-gloss">THÊM một ít — như <b>подли́ть</b> rót thêm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-рабат-</span>'
    '<span class="hd-gloss">LÀM VIỆC — <i>рабо́т-</i> của <b>рабо́тать</b>, <i>о → а</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành, chia đều: <b>подраба́тываю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm thêm một ít bên ngoài việc chính ⇒ làm thêm. Làm nghề gì thì cách 5: '
    '<b>подраба́тывать официа́нтом</b> chạy bàn kiếm thêm. Cặp HT: <b>подрабо́тать</b>.</div>'
    '<div class="hd-warn"><b>зараба́тывать</b> = kiếm tiền nói chung; <b>подраба́тывать</b> = chỉ phần kiếm '
    'THÊM, việc phụ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>подрабо́тка</b> việc làm thêm · <b>рабо́тать</b> làm việc · '
    '<b>зараба́тывать</b> kiếm tiền</div>'
)

# -------------------------------------------------------------------- буханка
S["буханка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Coi như một khối: thân <i>бухан-</i> nay không đứng riêng, <i>-ка</i> chỉ là đuôi '
    'danh từ giống cái.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ổ bánh nướng trong khuôn, hình viên gạch; thường là bánh đen. Bánh gì thì cách 2: '
    '<b>буха́нка хле́ба</b>. Ổ trắng dài là <b>бато́н</b>. Chiếc xe van UAZ được gọi đùa là '
    '<b>буха́нка</b> vì thùng xe trông y như ổ bánh.</div>'
    '<div class="hd-why">Chú ý bảng chia: cách 2 số nhiều chen <i>о</i> — <b>пять буха́нок</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>буха́ночка</b> ổ bánh nhỏ</div>'
)

# ---------------------------------------------------------------------- сушка
S["сушка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">суш-</span>'
    '<span class="hd-gloss">KHÔ — <b>сухо́й</b>, <i>х → ш</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">→ danh từ: việc làm đó, hoặc thứ làm ra</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Việc làm khô: <b>су́шка белья́</b> việc sấy quần áo. Thứ được làm khô: chiếc bánh '
    'vòng nhỏ, cứng giòn, ăn với trà — thường nói số nhiều: <b>чай с су́шками</b>.</div>'
    '<div class="hd-why">Chú ý bảng chia: cách 2 số nhiều chen <i>е</i> (sau <i>ш</i>) — <b>су́шек</b>.</div>'
    '<div class="hd-warn">Nói tắt ở nhà, <b>су́шка</b> còn là chế độ sấy hoặc cả cái máy sấy: '
    '<b>включи́ су́шку</b> bật sấy đi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>суши́ть</b> làm khô · <b>сухо́й</b> khô · '
    '<b>суши́лка</b> giá phơi, máy sấy · <b>за́суха</b> hạn hán</div>'
)

# --------------------------------------------------------------------- малина
S["малина"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — gốc Slav trơn.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Quả mâm xôi ĐỎ, cũng là cả cây. Như <b>клубни́ка</b>, dùng SỐ ÍT cho cả đống: '
    '<b>килогра́мм мали́ны</b>, <b>варе́нье из мали́ны</b>. Đếm từng quả thì thêm <b>я́года</b>: '
    '<b>одна́ я́года мали́ны</b>.</div>'
    '<div class="hd-warn"><b>Не жизнь, а мали́на!</b> — sướng như tiên (không phải cuộc đời, mà là quả '
    'mâm xôi ngọt).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мали́новый</b> vị mâm xôi; màu đỏ tím · <b>мали́нник</b> bụi mâm xôi</div>'
)

# ---------------------------------------------------------------------- крупа
S["крупа"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: gốc trơn <i>круп-</i> HẠT, mẩu vụn, cộng đuôi <i>-а́</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hạt khô đã xay, xát để nấu: <b>гре́чневая крупа́</b> hạt kiều mạch. Số ít chỉ cả '
    'khối; số nhiều là «các LOẠI hạt». Tuyết rơi thành hạt cũng gọi là <b>крупа́</b>.</div>'
    '<div class="hd-why">Chú ý bảng chia: số ít nhấn đuôi, số nhiều nhấn gốc — nên <b>крупы́</b> là cách 2 '
    'số ít, còn <b>кру́пы</b> là số nhiều.</div>'
    '<div class="hd-warn"><b>крупа́</b> là hạt KHÔ trong gói; nấu chín rồi thì thành <b>ка́ша</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>крупи́нка</b> một hạt nhỏ · <b>кру́пный</b> to, hạt to (từ nguyên: «như hạt»)</div>'
)

# -------------------------------------------------------------- кондитерский
S["кондитерский"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">конди́тер-</span>'
    '<span class="hd-gloss">THỢ BÁNH NGỌT — mượn tiếng Đức <i>Konditor</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ск-ий</span>'
    '<span class="hd-gloss">đuôi tính từ «thuộc về»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thuộc về thợ bánh ngọt» ⇒ bánh kẹo: <b>конди́терский магази́н</b>. Trên bao bì, '
    'tên chung của mọi loại bánh kẹo là <b>конди́терские изде́лия</b>.</div>'
    '<div class="hd-warn">Dạng giống cái đứng một mình thành danh từ: <b>конди́терская</b> = tiệm bánh ngọt; '
    'vẫn chia như tính từ: <b>в конди́терской</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>конди́тер</b> thợ bánh ngọt · <b>конди́терская</b> tiệm bánh ngọt</div>'
)

# -------------------------------------------------------------------- варёный
S["варёный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вар-</span>'
    '<span class="hd-gloss">ĐUN SÔI — <b>вари́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ён-</span>'
    '<span class="hd-gloss">«đã được» — như <b>солёный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đã được đun trong nước» ⇒ luộc: <b>варёное яйцо́</b>, <b>варёная карто́шка</b>. '
    '<b>варёная колбаса́</b> là loại xúc xích to, mềm như giò. Đối lập: <b>жа́реный</b> rán, '
    '<b>сыро́й</b> sống.</div>'
    '<div class="hd-warn">Một chữ <i>н</i>, nhấn <i>ё</i> = tính từ. <b>ва́ренный</b> hai <i>н</i> là phân '
    'từ, phải kèm phần bổ sung: <b>ва́ренный в молоке́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вари́ть</b> nấu, luộc · <b>варе́нье</b> mứt · <b>по́вар</b> đầu bếp · '
    '<b>завари́ть</b> pha, hãm</div>'
)

# ----------------------------------------------------------------------- квас
S["квас"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn <i>квас-</i> LÊN MEN, CHUA — mặt khác của <i>кис-</i> trong '
    '<b>ки́слый</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nước chua nhẹ lên men từ bánh mì đen, uống lạnh mùa hè; cũng là nước chan món '
    '<b>окро́шка</b> (canh nguội). Một cốc: <b>стака́н ква́са</b>, khẩu ngữ <b>стака́н ква́су</b>.</div>'
    '<div class="hd-why">Chú ý bảng chia: số ít nhấn gốc (<b>ква́са</b>), số nhiều đẩy hết ra đuôi '
    '(<b>квасы́, квасо́в</b>).</div>'
    '<div class="hd-warn">Cùng gốc, gặp ở mọi chợ Nga: <b>ква́шеная капу́ста</b> dưa bắp cải — '
    '<b>ква́сить</b> muối chua, <i>с → ш</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ки́слый</b> chua · <b>ква́сить</b> muối chua · <b>кисе́ль</b> chè quả sánh</div>'
)

# --------------------------------------------------------------------- кисель
S["кисель"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кис-</span>'
    '<span class="hd-gloss">CHUA, LÊN MEN — <b>ки́слый</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ль</span>'
    '<span class="hd-gloss">hậu tố danh từ cổ, ở đây giống ĐỰC</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Xưa là món yến mạch để lên men nên chua; nay là nước quả nấu với tinh bột cho '
    'sánh, thường ngọt: <b>клю́квенный кисе́ль</b>.</div>'
    '<div class="hd-why">Chú ý bảng chia: hễ thêm đuôi là trọng âm nhảy ra đuôi — <b>киселя́, киселю́, '
    'киселём, кисели́</b>.</div>'
    '<div class="hd-warn"><b>седьма́я вода́ на киселе́</b> — họ hàng xa lắc, «bắn đại bác không tới».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ки́слый</b> chua · <b>ки́снуть</b> chua đi · <b>кислота́</b> axit · '
    '<b>квас</b> nước kvas</div>'
)

# ----------------------------------------------------------------- заваривать
S["заваривать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">ở đây không tách được nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вар-</span>'
    '<span class="hd-gloss">ĐUN SÔI — <b>вари́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành, chia đều: <b>зава́риваю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dùng nước SÔI làm cho ngấm ⇒ pha, hãm; thứ được pha ở cách 4: '
    '<b>зава́ривать чай</b>. Cặp HT: <b>завари́ть</b> — thêm <i>-ива-</i> thì trọng âm lùi về gốc '
    '<i>-ва́р-</i>.</div>'
    '<div class="hd-warn"><b>вари́ть ко́фе</b> = đun trên bếp; <b>зава́ривать</b> = chỉ rót nước sôi vào '
    'rồi chờ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>завари́ть</b> (HT) · <b>зава́рка</b> trà khô; nước trà cốt · '
    '<b>вари́ть</b> nấu, luộc · <b>варёный</b> luộc</div>'
)

# ------------------------------------------------------------------- заварить
S["заварить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">ở đây không tách được nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вар-</span>'
    '<span class="hd-gloss">ĐUN SÔI — <b>вари́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dùng nước SÔI làm cho ngấm ⇒ pha, hãm (xong một ấm): '
    '<b>завари́ть чай</b>. Cặp CHT: <b>зава́ривать</b>.</div>'
    '<div class="hd-why">Chú ý bảng chia: trọng âm như <b>вари́ть</b> — chỉ ngôi «tôi» nhấn đuôi '
    '<b>заварю́</b>, còn lại lùi về gốc <b>зава́ришь, зава́рят</b>.</div>'
    '<div class="hd-warn"><b>завари́ть ка́шу</b> — «nấu lên nồi cháo» = gây ra chuyện rắc rối. Câu đi kèm: '
    '<b>Сам завари́л ка́шу, сам и расхлёбывай</b> tự gây ra thì tự gỡ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>зава́ривать</b> (CHT) · <b>зава́рка</b> trà khô; nước trà cốt · '
    '<b>вари́ть</b> nấu, luộc · <b>варёный</b> luộc</div>'
)

# ------------------------------------------------------------------- наесться
S["наесться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-…-ся</span>'
    '<span class="hd-gloss">đi thành cặp: làm cho THOẢ, cho ĐÃ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ес-ть</span>'
    '<span class="hd-gloss">ĂN — <b>есть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Ăn cho đã» ⇒ ăn no, cùng khuôn <b>напи́ться</b>. Ăn no CÁI GÌ thì cách 2: '
    '<b>нае́сться блино́в</b>. Được mời thêm thì đáp: <b>Спаси́бо, я нае́лся!</b> (nữ: <b>нае́лась</b>). '
    'Cặp CHT: <b>наеда́ться</b>.</div>'
    '<div class="hd-warn">Chú ý bảng chia: y như <b>есть</b> — số ít cụt <b>нае́мся, нае́шься, '
    'нае́стся</b>, số nhiều mọc <i>д</i> và nhấn đuôi <b>наеди́мся, наеди́тесь, наедя́тся</b>; quá khứ '
    '<b>нае́лся</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>есть</b> ăn · <b>съесть</b> ăn hết · <b>еда́</b> thức ăn · '
    '<b>объе́сться</b> ăn quá nhiều</div>'
)

# ------------------------------------------------------------------ сковорода
S["сковорода"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — từ Slav cổ, nay là một khối.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chảo nông để rán: <b>жа́рить на сковороде́</b> — tiếng Nga rán TRÊN chảo '
    '(<b>на</b>), nhưng nấu TRONG nồi (<b>в кастрю́ле</b>). Hằng ngày hay nói '
    '<b>сковоро́дка</b>.</div>'
    '<div class="hd-warn">Chú ý bảng chia: trọng âm chạy theo khuôn <b>голова́</b> — số nhiều '
    '<b>ско́вороды, сковоро́д, сковорода́м</b> (so <b>го́ловы, голо́в, голова́м</b>). Cách 4 số ít có hai '
    'lối, đều đúng: <b>ско́вороду</b> và <b>сковороду́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сковоро́дка</b> chảo (lời nói hằng ngày)</div>'
)

# -------------------------------------------------------------------- беседка
S["беседка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бесе́д-</span>'
    '<span class="hd-gloss">TRÒ CHUYỆN — <b>бесе́да</b> (trong đó <i>-сед-</i> là NGỒI)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">→ danh từ: ở đây là CHỖ để làm việc đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỗ để ngồi trò chuyện ⇒ chòi nghỉ có mái trong vườn, công viên: '
    '<b>сиде́ть в бесе́дке</b>. Trọng âm giữ đúng chỗ của <b>бесе́да</b>.</div>'
    '<div class="hd-why">Chú ý bảng chia: cách 2 số nhiều chen <i>о</i> — <b>бесе́док</b>.</div>'
    '<div class="hd-warn">Hai từ chỉ khác một chữ <i>к</i>: <b>бесе́да</b> là cuộc trò chuyện, '
    '<b>бесе́дка</b> là cái chòi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бесе́да</b> cuộc trò chuyện · <b>бесе́довать</b> trò chuyện · '
    '<b>собесе́дник</b> người cùng nói chuyện · <b>сосе́д</b> hàng xóm</div>'
)

# -------------------------------------------------------------------- вешалка
S["вешалка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">веш-а-</span>'
    '<span class="hd-gloss">TREO — <b>ве́шать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-лка</span>'
    '<span class="hd-gloss">ĐỒ để làm việc đó — như <b>суши́лка</b> giá phơi</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đồ để TREO áo ⇒ cái móc, cả cái giá đứng ở hành lang, lẫn vòng vải khâu ở cổ áo. '
    'Treo LÊN: <b>на</b> + cách 4 — <b>пове́сить пальто́ на ве́шалку</b>; đang treo: '
    '<b>виси́т на ве́шалке</b>.</div>'
    '<div class="hd-why">Chú ý bảng chia: cách 2 số nhiều chen <i>о</i> — <b>ве́шалок</b>.</div>'
    '<div class="hd-warn"><b>Теа́тр начина́ется с ве́шалки</b> — nhà hát bắt đầu từ chỗ gửi áo: câu cửa '
    'miệng về ấn tượng đầu tiên.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ве́шать</b> treo (CHT) · <b>пове́сить</b> treo lên (HT) · '
    '<b>висе́ть</b> đang treo</div>'
)

# --------------------------------------------------------------- видеокамера
S["видеокамера"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">видео-</span>'
    '<span class="hd-gloss">VIDEO — <b>ви́део</b>; đứng đầu từ ghép thì viết liền</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка́мера</span>'
    '<span class="hd-gloss">MÁY QUAY — Latin <i>camera</i> «căn buồng»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trùng hẳn <i>video camera</i>. Chỉ <i>-ка́мера</i> chia, <i>видео-</i> giữ nguyên: '
    '<b>снима́ть на видеока́меру</b> quay bằng máy quay. Nói gọn: <b>ка́мера</b>. Máy chụp ảnh thì là '
    '<b>фотоаппара́т</b>.</div>'
    '<div class="hd-warn"><b>ка́мера</b> còn giữ nghĩa gốc «căn buồng»: <b>ка́мера хране́ния</b> chỗ gửi '
    'hành lý ở nhà ga.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ви́део</b> video · <b>ка́мера</b> camera; buồng · '
    '<b>видеоза́пись</b> bản ghi hình · <b>ви́деть</b> thấy (họ xa)</div>'
)

# --------------------------------------------------------------------- люстра
S["люстра"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn tiếng Pháp <i>lustre</i> «vẻ sáng bóng; đèn chùm».</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng nguồn với tiếng Anh <i>lustre</i> vẻ bóng sáng. Đèn treo giữa trần nhà '
    'thường gọi là <b>лю́стра</b>, không cần có nhánh pha lê: <b>пове́сить лю́стру</b> treo đèn trần. '
    'Cách 2 số nhiều để nguyên cụm phụ âm, không chen gì: <b>люстр</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>иллюстра́ция</b> tranh minh hoạ (cùng gốc Latin «chiếu sáng»: rọi cho rõ)</div>'
)

# docbangmat 125 · loitubat 5: обозреватель chẻ -зр-ева- → -зре-ва-; варёная колбаса «không hun khói» sai; видео- «hình động» → video;
# люстра «bất cứ đèn treo nào» nói quá; thành ngữ Việt ở кисель tự chế → «bắn đại bác không tới».
# nguonsai 2: gloss «forklift operator» của грузчик; gloss «observer/viewer» của обозреватель.
B = {
    "docbangmat": 125,
    "loitubat": 5,
    "nguonsai": 2,
    "baolen": [
        "V cần duyệt (4 thẻ): грузчик (BỎ «công nhân xếp hàng» dễ đọc thành đứng xếp hàng; THÊM «người bốc vác») · обозреватель (BỎ «người quan sát», đó là наблюдатель) · сушка (BỎ «chế độ sấy» ngoài gloss; THÊM «bánh vòng khô») · буханка («xe tải nhỏ UAZ» → «xe van UAZ»).",
        "варёный — trùng «luộc, nấu chín» với ва́ренный (k21 đã nạp), cùng badge adj; варёный còn «đun chín» nên không trùng hết. Giữ nghĩa, không sửa; thẻ có ô đỏ phân biệt hai từ.",
        "грузчик — gloss EN «forklift operator» sai (đó là водитель погрузчика); nên là «loader / mover / stevedore».",
        "обозреватель — gloss EN «web browser / browser» là cách gọi Windows cũ, «observer / viewer» gần như không dùng; không đưa vào V.",
        "буханка — nghĩa xe UAZ là tiếng lóng; giữ vì gloss xác nhận (UAZ van). Muốn theo README §2c «bỏ nghĩa lóng» thì V = «ổ bánh mì».",
        "крупа — gloss có «snow pellets / graupel» (tuyết viên): thẻ nhắc một câu, không đưa vào V. Nối крупный ~ крупа: cùng gốc thật (từ nguyên), khớp k41. Ví dụ dịch «tấm ngũ cốc» gượng, nên là «hạt ngũ cốc» (cả ba câu).",
        "заваривать/заварить — V không đổi, hai thẻ đã chung dãy «pha, hãm, chế nước sôi»; nghĩa «hàn kim loại» ngoài gloss nên bỏ. Gloss EN thẻ заварить «to brew steep boil (tea)» dính chữ, thiếu dấu ngăn.",
        "малина — ví dụ 3 «Столько разных малин» không tự nhiên (số nhiều rất hiếm); nên «Столько разных сортов малины».",
        "сушка — ví dụ 3 dịch «máy sấy» là nghĩa khẩu ngữ không có trong V; thẻ có ô đỏ giải thích.",
        "сковорода — cách 4 hai trọng âm ско́вороду / сковороду́: cả hai đúng (nouns.csv ghi cả hai); không xem được ô bảng trên thẻ thật.",
        "Chỗ không chắc: từ nguyên буханка còn bàn cãi nên không nêu; за- của заварить khai «không tách được nghĩa riêng».",
        "Đã lỡ soạn một lệnh ĐỌC thẻ qua AnkiConnect; bị chặn trước khi chạy, không có gì chạm Anki.",
    ],
}
