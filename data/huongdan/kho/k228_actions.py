# -*- coding: utf-8 -*-
"""k228 — actions: 10 cặp thể + vài động từ lẻ; trục là GỐC + TIỀN TỐ.

Chỗ cần nhất quán với lô đã nạp:
(1) разбирать: раз- TÁCH RA + -бир- LẤY — khớp разобрать k210, убирать k122; V y hệt разобрать.
(2) крас- ĐẸP rồi mới ĐỎ (k44, k186); у- LÀM CHO thành (k217, k225) trong украсить, усилить, укрепить.
(3) избить: бить GIÁNG XUỐNG, ĐÁNH — khớp бить k02, забить k219.
(4) унести/уносить: у- RỜI KHỎI (k98, k107) + нес-/нос- MANG — khớp k185, k201.
(5) укусить: кус- CẮN — khớp кусок k79, вкус k152. (6) обновить: об- LÀM CHO thành — khớp облегчить.
(7) обогнать/обгонять: об- VÒNG QUANH (обойти k137) + гн-/гон- ĐUỔI — khớp гнать, догнать k215.
Họ hàng cố ý vắng: không có (mọi từ đều có họ thật).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "хлопать": "vỗ tay, vỗ, đập, đóng sầm",                    # + to slam
    "хлопнуть": "vỗ tay, vỗ, đập, đóng sầm",                   # cặp thể, chung dãy
    "разбирать": "tháo rời, tháo dỡ, đọc ra, nghe ra, sắp xếp, phân tích, mua hết",   # y hệt разобрать k210
    "копить": "dành dụm, tiết kiệm, tích lũy, dồn lại",        # + build up
    "накопить": "dành dụm, tiết kiệm, tích lũy, dồn lại",      # bỏ «được» (badge thể đã in)
    "тонуть": "chết đuối, chìm, đắm, lún",                     # + be buried (in)
    "утонуть": "chết đuối, chìm, đắm, lún",
    "обновить": "cập nhật, làm mới, tân trang, thay mới",      # + renovate; replace with new
    "обновлять": "cập nhật, làm mới, tân trang, thay mới",
    "укрепить": "củng cố, tăng cường, gia cố, làm cho vững chắc, gắn chặt",   # + consolidate; fasten
    "укреплять": "củng cố, tăng cường, gia cố, làm cho vững chắc, gắn chặt",
}

# --------------------------------------------------------------------- хлопать
S["хлопать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">хлоп-</span>'
    '<span class="hd-gloss">tiếng ĐẬP «bộp», từ tượng thanh <b>хлоп!</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>хло́паю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm kêu «bộp, bộp» nhiều lần ⇒ vỗ tay, vỗ vai, đập cánh, đóng cửa sầm '
    'sầm. Một cú thì đổi sang <b>хло́пнуть</b>; vỗ một hồi thì HT là <b>похло́пать</b>.</div>'
    '<div class="hd-warn">Vật đem ra đập đứng cách 5: <b>хло́пать две́рью</b> đóng sầm cửa, '
    '<b>хло́пать кры́льями</b> đập cánh. Vỗ VÀO chỗ nào: <b>по</b> + cách 3 — <b>хло́пать по '
    'плечу́</b>. Riêng vỗ tay: <b>хло́пать в ладо́ши</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>хло́пнуть</b> (HT, một cú) · <b>похло́пать</b> vỗ một hồi (HT) · '
    '<b>захло́пнуть</b> đóng sầm lại</div>'
)

# -------------------------------------------------------------------- хлопнуть
S["хлопнуть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">хлоп-</span>'
    '<span class="hd-gloss">tiếng ĐẬP «bộp», như <b>хло́пать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ну-ть</span>'
    '<span class="hd-gloss">làm MỘT CÚ, đuôi HT</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một tiếng «bộp» duy nhất ⇒ sập cửa một cái, vỗ vai một cái: <b>хло́пнуть '
    'по плечу́</b>. Chia giữ <i>-н-</i>, trọng âm đứng yên: <b>хло́пну, хло́пнешь</b>. Cặp CHT: '
    '<b>хло́пать</b>.</div>'
    '<div class="hd-warn"><b>хло́пнуть две́рью</b> (cửa ở cách 5) = đóng sầm cửa; nghĩa bóng: giận '
    'dữ bỏ đi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>хло́пать</b> (CHT) · <b>захло́пнуть</b> đóng sầm lại · '
    '<b>захло́пнуться</b> tự đóng sầm</div>'
)

# ------------------------------------------------------------------- разбирать
S["разбирать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раз-</span>'
    '<span class="hd-gloss">TÁCH RA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бир-</span>'
    '<span class="hd-gloss">LẤY — gốc <i>бр-/бер-</i> của <b>брать</b>, mọc <i>и</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>разбира́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Lấy TÁCH RA từng phần ⇒ tháo máy, xếp đồ, mổ xẻ từng lỗi: '
    '<b>разбира́ть оши́бки</b> phân tích lỗi; tách ra từng chữ ⇒ đọc ra, nghe ra; mỗi người lấy '
    'một cái ⇒ mua hết. Cặp HT: <b>разобра́ть</b> (chêm <i>о</i>, mất <i>и</i>).</div>'
    '<div class="hd-warn">Thêm -ся là nghĩa khác: <b>разбира́ться в</b> + cách 6 = am hiểu cái gì. '
    'Không -ся thì kéo cách 4.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>разобра́ть</b> (HT) · <b>разбира́ться</b> am hiểu · <b>разбо́р</b> sự '
    'phân tích · <b>собира́ть</b> gom, lắp lại · <b>брать</b> lấy</div>'
)

# --------------------------------------------------------------------- красить
S["красить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">крас-</span>'
    '<span class="hd-gloss">ĐẸP (nghĩa cổ), sau mới thành ĐỎ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai; ngôi «tôi» <i>с → ш</i>: <b>кра́шу, '
    'кра́сишь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vốn là «làm cho đẹp» bằng màu ⇒ sơn tường, nhuộm tóc, tô son: '
    '<b>кра́сить гу́бы</b>. Đổi thành MÀU gì thì <b>в</b> + cách 4: <b>кра́сить сте́ны в бе́лый '
    'цвет</b>. Cặp HT: <b>покра́сить</b>.</div>'
    '<div class="hd-warn">Chỉ khác một chữ với <b>красть</b> ăn trộm, mà bảng chia khác hẳn: '
    '<b>кра́шу</b> tôi sơn ≠ <b>краду́</b> tôi ăn trộm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>покра́сить</b> (HT) · <b>кра́ска</b> sơn, màu vẽ · <b>краси́вый</b> '
    'đẹp · <b>кра́сный</b> đỏ</div>'
)

# ------------------------------------------------------------------- покрасить
S["покрасить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">chỉ làm thành thể hoàn thành, KHÔNG thêm nghĩa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-кра́сить</span>'
    '<span class="hd-gloss">SƠN, NHUỘM — gốc <i>крас-</i> ĐẸP</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Sơn xong, nhuộm xong: <b>покра́сить забо́р</b> sơn hàng rào, '
    '<b>покра́сить во́лосы</b> nhuộm tóc. Trọng âm đứng yên, ngôi «tôi» <i>с → ш</i>: '
    '<b>покра́шу, покра́сишь</b>. Cặp CHT: <b>кра́сить</b>.</div>'
    '<div class="hd-warn">Tiền tố đổi là nghĩa đổi: <b>покра́сить</b> sơn, nhuộm · '
    '<b>укра́сить</b> trang trí.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кра́сить</b> (CHT) · <b>покра́ска</b> việc sơn · <b>кра́ска</b> sơn, '
    'màu vẽ · <b>краси́вый</b> đẹp</div>'
)

# -------------------------------------------------------------------- украсить
S["украсить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">LÀM CHO thành</span></div>'
    '<div class="hd-row"><span class="hd-piece">-кра́с-</span>'
    '<span class="hd-gloss">ĐẸP — <b>краси́вый</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai; ngôi «tôi» <i>с → ш</i>: <b>укра́шу, '
    'укра́сишь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm cho ĐẸP ⇒ trang trí. Bằng thứ gì thì cách 5: <b>укра́сить ёлку '
    'игру́шками</b> trang trí cây thông bằng đồ chơi. Cặp CHT: <b>украша́ть</b>.</div>'
    '<div class="hd-warn">Đừng lẫn với <b>укра́сть</b> ăn trộm: quá khứ <b>укра́сил</b> đã trang '
    'trí ≠ <b>укра́л</b> đã ăn trộm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>украша́ть</b> (CHT) · <b>украше́ние</b> đồ trang trí, trang sức · '
    '<b>краси́вый</b> đẹp · <b>красота́</b> vẻ đẹp</div>'
)

# -------------------------------------------------------------------- украшать
S["украшать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">LÀM CHO thành</span></div>'
    '<div class="hd-row"><span class="hd-piece">-краш-</span>'
    '<span class="hd-gloss">ĐẸP — gốc <i>крас-</i>, с đổi thành ш</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>украша́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đang trang trí, hay vẫn làm đẹp cho: <b>Карти́ны украша́ют ко́мнату</b> '
    'Tranh làm đẹp căn phòng. Chữ <i>ш</i> này chính là <i>ш</i> của <b>укра́шу</b> và '
    '<b>украше́ние</b>. Cặp HT: <b>укра́сить</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>укра́сить</b> (HT) · <b>украше́ние</b> đồ trang trí, trang sức · '
    '<b>краси́вый</b> đẹp · <b>красота́</b> vẻ đẹp</div>'
)

# ---------------------------------------------------------------------- избить
S["избить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">из-</span>'
    '<span class="hd-gloss">tới CẠN, khắp chỗ, quá mức</span></div>'
    '<div class="hd-row"><span class="hd-piece">-би́ть</span>'
    '<span class="hd-gloss">GIÁNG XUỐNG, ĐÁNH — chính là <b>бить</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đánh khắp người tới thậm tệ ⇒ đánh nhừ tử. Người bị đánh đứng cách 4: '
    '<b>Его́ изби́ли</b> Anh ta bị đánh (ngôi 3 số nhiều, không chủ ngữ = «bị»). Cặp CHT: '
    '<b>избива́ть</b>.</div>'
    '<div class="hd-warn">Chia như <b>бить</b>, <i>и</i> rút thành <i>ь</i>, và chêm <i>о</i> sau '
    '<i>из</i>: <b>изобью́, изобьёшь</b>; mệnh lệnh <b>избе́й</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>избива́ть</b> (CHT) · <b>избие́ние</b> vụ đánh đập · <b>бить</b> đánh · '
    '<b>уби́ть</b> giết · <b>разби́ть</b> đập vỡ</div>'
)

# --------------------------------------------------------------------- усилить
S["усилить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">LÀM CHO thành</span></div>'
    '<div class="hd-row"><span class="hd-piece">-си́л-</span>'
    '<span class="hd-gloss">SỨC — <b>си́ла</b>, <b>си́льный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai: <b>уси́лю, уси́лишь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm cho có SỨC hơn ⇒ tăng cường, làm mạnh lên: <b>уси́лить охра́ну</b> '
    'tăng cường bảo vệ, <b>уси́лить звук</b> khuếch đại âm thanh. Trọng âm đứng yên ở <i>си́</i>. '
    'Cặp CHT: <b>уси́ливать</b>.</div>'
    '<div class="hd-warn">Cái TỰ mạnh lên thì phải thêm -ся: <b>Ве́тер уси́лился</b> Gió mạnh '
    'lên.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уси́ливать</b> (CHT) · <b>усиле́ние</b> sự tăng cường · '
    '<b>усили́тель</b> máy khuếch đại · <b>уси́лие</b> nỗ lực · <b>си́ла</b> sức</div>'
)

# ---------------------------------------------------------------------- копить
S["копить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">коп-</span>'
    '<span class="hd-gloss">GOM THÀNH ĐỐNG — như <b>копна́</b> đống cỏ khô</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gom dần thành đống ⇒ dành dụm, tích lũy. Ngôi «tôi» chèn <i>л</i>, từ ngôi '
    '«bạn» trọng âm lùi: <b>коплю́, ко́пишь</b>. Cặp HT: <b>накопи́ть</b>.</div>'
    '<div class="hd-warn">Dành tiền ĐỂ MUA gì: <b>на</b> + cách 4 — <b>копи́ть (де́ньги) на '
    'маши́ну</b> dành tiền mua xe.</div>'
    '<div class="hd-warn">Chỉ giống mặt chữ, không họ hàng: <b>ко́пия</b> bản sao (mượn, như Anh '
    '<i>copy</i>) và <b>пить</b> uống.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>накопи́ть</b> (HT) · <b>накопле́ния</b> tiền tiết kiệm · '
    '<b>скопи́ться</b> dồn lại, tụ lại</div>'
)

# -------------------------------------------------------------------- накопить
S["накопить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">DỒN cho ĐẦY, được một lượng — như <b>набра́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-коп-</span>'
    '<span class="hd-gloss">GOM THÀNH ĐỐNG — <b>копи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dồn tới khi được một đống ⇒ tích lũy được, dành dụm đủ: <b>накопи́ть на '
    'кварти́ру</b> dành đủ tiền mua nhà. Chia như <b>копи́ть</b>, trọng âm lùi từ ngôi «bạn»: '
    '<b>накоплю́, нако́пишь</b>. Cặp CHT: <b>копи́ть</b>, <b>нака́пливать</b>.</div>'
    '<div class="hd-warn">Việc tự dồn lại thì thêm -ся: <b>Накопи́лось мно́го дел</b> Dồn lại cả đống '
    'việc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>копи́ть</b> (CHT) · <b>накопи́ться</b> dồn lại · <b>накопле́ния</b> '
    'tiền tiết kiệm</div>'
)

# ---------------------------------------------------------------------- унести
S["унести"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">RỜI KHỎI, ra xa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-нес-ти́</span>'
    '<span class="hd-gloss">MANG, VÁC — chính là <b>нести́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mang RA XA ⇒ đem đi; gió, nước mang đi ⇒ cuốn đi: <b>Ве́тер унёс '
    'шля́пу</b> Gió cuốn mất cái mũ. Trái chiều: <b>принести́</b> mang đến. Cặp CHT: '
    '<b>уноси́ть</b>.</div>'
    '<div class="hd-warn">Chia như <b>нести́</b>: <b>унесу́, унесёшь</b>. Quá khứ giống đực KHÔNG '
    'có -л, các dạng kia nhấn đuôi: <b>унёс, унесла́, унесли́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уноси́ть</b> (CHT) · <b>нести́</b> mang · <b>принести́</b> mang đến · '
    '<b>отнести́</b> đem tới · <b>вы́нести</b> mang ra</div>'
)

# --------------------------------------------------------------------- уносить
S["уносить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">RỜI KHỎI, ra xa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-нос-и́ть</span>'
    '<span class="hd-gloss">MANG, VÁC — <b>носи́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đang mang đi, hay mang đi nhiều lần: <b>Официа́нт уно́сит таре́лки</b> Bồi '
    'bàn mang đĩa đi. Cả họ: tiền tố + <b>носи́ть</b> → CHT, tiền tố + <b>нести́</b> → HT '
    '(<b>унести́</b>).</div>'
    '<div class="hd-warn">Chia như <b>носи́ть</b>: ngôi «tôi» <i>с → ш</i>, sau đó trọng âm lùi — '
    '<b>уношу́, уно́сишь, уно́сят</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>унести́</b> (HT) · <b>носи́ть</b> mang, mặc · <b>приноси́ть</b> mang '
    'đến · <b>выноси́ть</b> mang ra</div>'
)

# -------------------------------------------------------------------- укусить
S["укусить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">chỉ làm thành thể hoàn thành, KHÔNG thêm nghĩa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-кус-</span>'
    '<span class="hd-gloss">CẮN — như <b>куса́ть</b>, <b>кусо́к</b> miếng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cắn một phát; ong, muỗi «cắn» cũng là từ này ⇒ đốt. Nạn nhân đứng cách 4, '
    'con vật làm chủ ngữ: <b>Меня́ укуси́ла соба́ка</b> Tôi bị chó cắn. Cặp CHT: '
    '<b>куса́ть</b>.</div>'
    '<div class="hd-warn">Ngôi «tôi» <i>с → ш</i>, từ ngôi «bạn» trọng âm lùi: <b>укушу́, '
    'уку́сишь, уку́сят</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>куса́ть</b> (CHT) · <b>уку́с</b> vết cắn · <b>кусо́к</b> miếng · '
    '<b>заку́ска</b> món nhắm, khai vị</div>'
)

# ---------------------------------------------------------------------- тонуть
S["тонуть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">то(п)-</span>'
    '<span class="hd-gloss">CHÌM — <i>п</i> rụng trước <i>н</i>, còn thấy trong '
    '<b>утопи́ть</b> dìm chết</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ну́-ть</span>'
    '<span class="hd-gloss">đuôi động từ, giữ <i>-н-</i> khi chia</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đang chìm xuống nước ⇒ chết đuối, đắm. Chìm TRONG gì thì <b>в</b> + cách '
    '6: <b>тону́ть в снегу́</b> lún trong tuyết, <b>тону́ть в дела́х</b> ngập đầu trong việc. Cặp '
    'HT: <b>утону́ть</b>.</div>'
    '<div class="hd-warn">Từ ngôi «bạn» trọng âm lùi: <b>тону́, то́нешь, то́нут</b>. Đuôi <i>-ну-</i> '
    'ở đây KHÔNG phải «một cú» — từ này là CHƯA hoàn thành.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>утону́ть</b> (HT) · <b>утопи́ть</b> dìm chết, đánh chìm · '
    '<b>уто́пленник</b> người chết đuối · <b>пото́п</b> trận đại hồng thủy</div>'
)

# --------------------------------------------------------------------- утонуть
S["утонуть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">RỜI KHỎI, mất hẳn — như trong <b>уби́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-тону́ть</span>'
    '<span class="hd-gloss">CHÌM — chính là <b>тону́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chìm MẤT HẲN ⇒ chết đuối, chìm nghỉm: <b>Он утону́л в реке́</b> Anh ấy '
    'chết đuối dưới sông; chìm vào thứ mềm ⇒ lún: <b>утону́ть в снегу́</b>. Chia như '
    '<b>тону́ть</b>: <b>утону́, уто́нешь</b>.</div>'
    '<div class="hd-warn">Tự chìm là <b>утону́ть</b>; dìm người khác, đánh chìm tàu là '
    '<b>утопи́ть</b> + cách 4.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тону́ть</b> (CHT) · <b>утопи́ть</b> dìm chết, đánh chìm · '
    '<b>уто́пленник</b> người chết đuối</div>'
)

# -------------------------------------------------------------------- обновить
S["обновить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">LÀM CHO thành — như <b>облегчи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-нов-</span>'
    '<span class="hd-gloss">MỚI — <b>но́вый</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai; ngôi «tôi» chèn <i>л</i>: <b>обновлю́, '
    'обнови́шь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm cho MỚI ⇒ cập nhật, làm mới, tân trang — cùng ý với Anh '
    '<i>renew</i>: <b>обнови́ть програ́мму</b> cập nhật phần mềm. Trọng âm ở đuôi suốt bảng. Cặp '
    'CHT: <b>обновля́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обновля́ть</b> (CHT) · <b>обновле́ние</b> bản cập nhật · <b>но́вый</b> '
    'mới · <b>но́вость</b> tin tức · <b>сно́ва</b> lại lần nữa</div>'
)

# ------------------------------------------------------------------- обновлять
S["обновлять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">LÀM CHO thành</span></div>'
    '<div class="hd-row"><span class="hd-piece">-новл-</span>'
    '<span class="hd-gloss">MỚI — <b>но́вый</b>; <i>в</i> thêm <i>л</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>обновля́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đang làm mới, làm mới thường xuyên: <b>обновля́ть сайт ка́ждый день</b> '
    'cập nhật trang web mỗi ngày. Chữ <i>л</i> này chính là <i>л</i> của <b>обновлю́</b>. Cặp HT: '
    '<b>обнови́ть</b>.</div>'
    '<div class="hd-warn">Máy tự cập nhật thì thêm -ся: <b>Телефо́н обновля́ется</b> Điện thoại '
    'đang cập nhật.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обнови́ть</b> (HT) · <b>обновле́ние</b> bản cập nhật · <b>но́вый</b> '
    'mới · <b>но́вость</b> tin tức</div>'
)

# -------------------------------------------------------------------- укрепить
S["укрепить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">LÀM CHO thành</span></div>'
    '<div class="hd-row"><span class="hd-piece">-креп-</span>'
    '<span class="hd-gloss">CHẮC, VỮNG — <b>кре́пкий</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai; ngôi «tôi» chèn <i>л</i>: <b>укреплю́, '
    'укрепи́шь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm cho CHẮC ⇒ củng cố, gia cố: <b>укрепи́ть сте́ну</b> gia cố tường; nghĩa '
    'bóng: <b>укрепи́ть здоро́вье</b> tăng cường sức khoẻ; làm cho chắc vào chỗ ⇒ gắn chặt. Trọng '
    'âm ở đuôi suốt bảng. Cặp CHT: <b>укрепля́ть</b>.</div>'
    '<div class="hd-warn"><b>укрепи́ть</b> làm cho CHẮC, khó lay · <b>уси́лить</b> làm cho MẠNH '
    'hơn (âm thanh, áp lực).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>укрепля́ть</b> (CHT) · <b>укрепле́ние</b> sự củng cố · <b>кре́пкий</b> '
    'chắc, đậm · <b>кре́пость</b> pháo đài</div>'
)

# ------------------------------------------------------------------- укреплять
S["укреплять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">LÀM CHO thành</span></div>'
    '<div class="hd-row"><span class="hd-piece">-крепл-</span>'
    '<span class="hd-gloss">CHẮC, VỮNG — <b>кре́пкий</b>; <i>п</i> thêm <i>л</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>укрепля́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đang củng cố, làm cho vững dần: <b>Спорт укрепля́ет здоро́вье</b> Thể thao '
    'tăng cường sức khoẻ. Chữ <i>л</i> này chính là <i>л</i> của <b>укреплю́</b> và '
    '<b>укрепле́ние</b>. Cặp HT: <b>укрепи́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>укрепи́ть</b> (HT) · <b>укрепле́ние</b> sự củng cố · <b>кре́пкий</b> '
    'chắc, đậm · <b>кре́пость</b> pháo đài</div>'
)

# ------------------------------------------------------------------- обгонять
S["обгонять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">VÒNG QUANH, vòng qua bên — như <b>обойти́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-гон-</span>'
    '<span class="hd-gloss">ĐUỔI, PHÓNG — gốc <i>гн-/гон-</i> của <b>гнать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>обгоня́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Phóng vòng qua bên xe trước ⇒ vượt; nghĩa bóng: giỏi hơn, bỏ xa. Kẻ bị vượt '
    'đứng cách 4: <b>обгоня́ть авто́бус</b> vượt xe buýt. Cặp HT: <b>обогна́ть</b>.</div>'
    '<div class="hd-warn">Biển báo, lỗi giao thông dùng danh từ <b>обго́н</b>: <b>Обго́н '
    'запрещён</b> Cấm vượt.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обогна́ть</b> (HT) · <b>обго́н</b> sự vượt xe · <b>догоня́ть</b> đuổi '
    'theo · <b>гнать</b> lùa, phóng · <b>го́нка</b> cuộc đua</div>'
)

# ------------------------------------------------------------------- обогнать
S["обогнать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">обо-</span>'
    '<span class="hd-gloss">VÒNG QUA — <b>об-</b> chêm <i>о</i> trước cụm <i>гн</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-гн-а́ть</span>'
    '<span class="hd-gloss">ĐUỔI, PHÓNG — chính là <b>гнать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Phóng vòng qua mặt, vượt xong. Vượt AI cách 4: <b>обогна́ть '
    'грузови́к</b> vượt xe tải, <b>обогна́ть сопе́рника</b> vượt đối thủ. Mới bắt KỊP thì là '
    '<b>догна́ть</b>. Cặp CHT: <b>обгоня́ть</b>.</div>'
    '<div class="hd-warn">Chia như <b>гнать</b>: hiện <i>о</i> trong gốc thì <i>о</i> chêm biến mất — '
    '<b>обгоню́, обго́нишь</b>. Quá khứ chỉ giống cái nhấn đuôi: <b>обогна́л, обогнала́, '
    'обогна́ли</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обгоня́ть</b> (CHT) · <b>обго́н</b> sự vượt xe · <b>догна́ть</b> đuổi '
    'kịp · <b>гнать</b> lùa, phóng · <b>го́нка</b> cuộc đua</div>'
)

B = {
    "docbangmat": 145,
    "loitubat": 2,
    "nguonsai": 1,
    "baolen": [
        "V cần duyệt (11 thẻ): хлопать/хлопнуть chung dãy «vỗ tay, vỗ, đập, đóng sầm» (gloss hai thẻ đều có clap, slap, pat, slam; bỏ nghĩa suồng sã «nốc cạn»); разбирать y hệt разобрать; копить/накопить chung «dành dụm, tiết kiệm, tích lũy, dồn lại»; тонуть/утонуть chung «chết đuối, chìm, đắm, lún»; обновить/обновлять + «tân trang, thay mới» (renovate, replace with new; bỏ «mặc/dùng lần đầu» vì hẹp); укрепить/укреплять + «củng cố, gắn chặt». 11 thẻ còn lại giữ đề cũ.",
        "усилить giữ đề cũ có «khuếch đại»: gloss trên thẻ chỉ ghi to strengthen, nhưng nghĩa này có thật (усилить звук, усилитель) nên không cắt.",
        "THẺ ĐÃ NẠP SAI, chưa sửa vì ngoài lô: красный k44, mục Họ hàng ghi «краси́ть», đúng là кра́сить.",
        "THẺ ĐÃ NẠP thiếu dấu nhấn, chưa sửa vì ngoài lô: прекрасный k42 in «Красная площадь» (đúng: Кра́сная пло́щадь).",
        "Chỗ không chắc: копить nối копна «đống cỏ khô» theo từ điển từ nguyên, không phải luật suy ra được; cố ý không nối копать «đào». утонуть: у- ghi «mất hẳn», có sách coi là tiền tố thể thuần tuý.",
        "Nguồn sai đã bác (1): bỏ «được» trong đề накопить (tích lũy được, dành dụm được): đó là nhãn thể, badge đã in.",
        "loitubat (2): накопить viết -ся «đi với cách 2» (cách 2 là do много); обновить viết «khuôn y hệt renew» (об- không phải «lại», đổi thành «cùng ý»).",
    ],
}
