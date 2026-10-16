# -*- coding: utf-8 -*-
"""k95 — actions: 19 động từ mới (đợt A1-A2 TRKI), chín cặp thể chung lô + лета́ть.

Không khối hệ thống. Chỗ cần nhất quán:
(1) mỗi cặp: vế HT chẻ gốc + tiền tố, vế CHT chỉ nói phần đuôi (-ыва-/-ива-/-а-/-я́ть)
    rồi dẫn ngược — không chép nhau;
(2) gốc -каз- (доказа́ть, заказа́ть, каза́ться, показа́ться) giữ đúng khuôn k14/k54/k79:
    "đưa ra cho thấy / nói ra", -ыва- làm trọng âm nhảy về gốc;
(3) gốc -конч- khớp thẻ ко́нчить k87 (коне́ц, ц hoá ч);
(4) изменя́ть vs меня́ть: sửa đổi bản thân sự vật vs đổi cái này lấy cái khác;
(5) класть vs ста́вить: đặt NẰM vs đặt ĐỨNG — khớp thẻ ста́вить k80.
"""

S = {}

# -------------------------------------------------------- доказать
S["доказать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-</span>'
    '<span class="hd-gloss">TỚI tận đích</span></div>'
    '<div class="hd-row"><span class="hd-piece">-каз-</span>'
    '<span class="hd-gloss">gốc ĐƯA RA CHO THẤY — như <b>показа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đưa ra cho thấy TỚI TẬN CÙNG, đến khi người kia hết cãi ⇒ chứng minh. '
    'Chia như <b>сказа́ть</b>: <b>з</b> hoá <b>ж</b>, trọng âm lùi từ ngôi hai — '
    '<b>докажу́</b>, <b>дока́жешь</b>.</div>'
    '<div class="hd-warn">Chứng minh CHO AI (cách 3) ĐIỀU GÌ (cách 4): '
    '<b>Я докажу́ тебе́ э́то</b> = Tôi sẽ chứng minh cho cậu thấy điều đó.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дока́зывать</b> chứng minh (CHT) · <b>доказа́тельство</b> bằng chứng · '
    '<b>показа́ть</b> cho xem · <b>сказа́ть</b> nói ra</div>'
)

# -------------------------------------------------------- доказывать
S["доказывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">доказ-</span>'
    '<span class="hd-gloss">chứng minh — chính là <b>доказа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-</span>'
    '<span class="hd-gloss">hậu tố biến hoàn thành → CHƯA hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>-ыва-</b> kéo việc chứng minh dài ra: đang chứng minh, cố chứng minh '
    'mãi. Trọng âm nhảy về gốc y như <b>показа́ть → пока́зывать</b>: '
    '<b>доказа́ть → дока́зывать</b>. Chia đều: <b>дока́зываю</b>, <b>дока́зываешь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>доказа́ть</b> chứng minh (HT) · <b>доказа́тельство</b> bằng chứng · '
    '<b>пока́зывать</b> cho xem</div>'
)

# -------------------------------------------------------- заказать
S["заказать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">tiền tố, ở đây KHÔNG tách ra nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-каз-</span>'
    '<span class="hd-gloss">NÓI RA, chỉ ra — như <b>сказа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nói ra thứ mình muốn để người ta làm hoặc mang tới ⇒ đặt món, đặt chỗ, '
    'đặt hàng. Chia như <b>сказа́ть</b>: <b>закажу́</b>, <b>зака́жешь</b>.</div>'
    '<div class="hd-warn">Dùng ngay ở nhà hàng: <b>Я хочу́ заказа́ть сто́лик</b> = Tôi muốn đặt bàn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>зака́зывать</b> đặt (CHT) · <b>зака́з</b> đơn đặt hàng · '
    '<b>прика́з</b> mệnh lệnh · <b>сказа́ть</b> nói ra</div>'
)

# -------------------------------------------------------- заказывать
S["заказывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">заказ-</span>'
    '<span class="hd-gloss">đặt — chính là <b>заказа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-</span>'
    '<span class="hd-gloss">hậu tố biến hoàn thành → CHƯA hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>-ыва-</b> biến cú đặt một lần thành việc đang đặt / hay đặt. '
    'Trọng âm nhảy về gốc: <b>заказа́ть → зака́зывать</b>. Chia đều: <b>зака́зываю</b>.</div>'
    '<div class="hd-warn">Câu phục vụ hỏi khi bạn vừa ngồi xuống: '
    '<b>Что бу́дете зака́зывать?</b> = Quý khách gọi món gì ạ?</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>заказа́ть</b> đặt (HT) · <b>зака́з</b> đơn đặt hàng</div>'
)

# -------------------------------------------------------- закончить
S["закончить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">tiền tố thể, KHÔNG mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-конч-</span>'
    '<span class="hd-gloss">gốc KẾT THÚC — chính là <b>коне́ц</b>, <b>ц</b> hoá <b>ч</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đưa việc tới <b>коне́ц</b> ⇒ hoàn thành, làm xong. Trung tính, dùng an toàn '
    'hơn <b>ко́нчить</b>. Chia đều: <b>зако́нчу</b>, <b>зако́нчишь</b>. '
    '<b>Зако́нчить шко́лу</b> = học xong phổ thông.</div>'
    '<div class="hd-warn">Người LÀM xong thì không <b>-ся</b>: <b>Я зако́нчил рабо́ту</b>. '
    'Việc TỰ hết thì thêm <b>-ся</b>: <b>Уро́к зако́нчился</b> = Buổi học đã kết thúc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>зака́нчивать</b> làm xong (CHT) · <b>коне́ц</b> phần cuối · '
    '<b>ко́нчить</b> xong · <b>око́нчить</b> tốt nghiệp</div>'
)

# -------------------------------------------------------- заканчивать
S["заканчивать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">tiền tố, KHÔNG mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-канч-</span>'
    '<span class="hd-gloss">vẫn là gốc <b>конч-</b> (<b>коне́ц</b>), <b>о</b> hoá <b>а</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-</span>'
    '<span class="hd-gloss">hậu tố biến hoàn thành → CHƯA hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thêm <b>-ива-/-ыва-</b> thì <b>о</b> của gốc hoá <b>а</b>: '
    '<b>зако́нчить → зака́нчивать</b>, y như <b>спроси́ть → спра́шивать</b>. Thấy <b>а</b> '
    'đừng tìm gốc mới — vẫn là <b>коне́ц</b>. Chia đều: <b>зака́нчиваю</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>зако́нчить</b> làm xong (HT) · <b>коне́ц</b> phần cuối · '
    '<b>конча́ть</b> xong (CHT)</div>'
)

# -------------------------------------------------------- заметить
S["заметить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">tiền tố thể, KHÔNG mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мет-</span>'
    '<span class="hd-gloss">gốc DẤU, đánh dấu — như <b>заме́тка</b> ghi chú</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mắt "đánh một dấu" lên thứ vừa lướt qua ⇒ để ý thấy. Nói ra điều mình '
    'để ý ⇒ nhận xét. Ngôi «tôi» <b>т</b> hoá <b>ч</b>: <b>заме́чу</b>, nhưng '
    '<b>заме́тишь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>замеча́ть</b> để ý thấy (CHT) · <b>замеча́ние</b> lời nhận xét · '
    '<b>заме́тка</b> ghi chú · <b>замеча́тельный</b> tuyệt vời (đáng để ý)</div>'
)

# -------------------------------------------------------- замечать
S["замечать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">замеч-</span>'
    '<span class="hd-gloss">để ý — chính là <b>заме́тить</b>, <b>т</b> hoá <b>ч</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi CHƯA hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp thể đổi <b>т → ч</b> rồi thêm <b>-а-</b>: <b>заме́тить → замеча́ть</b>, '
    'y như <b>отве́тить → отвеча́ть</b>. Chia đều: <b>замеча́ю</b>, <b>замеча́ешь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>заме́тить</b> để ý thấy (HT) · <b>замеча́ние</b> lời nhận xét · '
    '<b>замеча́тельный</b> tuyệt vời</div>'
)

# -------------------------------------------------------- заплатить
S["заплатить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">tiền tố thể, KHÔNG mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-плати́ть</span>'
    '<span class="hd-gloss">trả tiền — chính là <b>плати́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>плати́ть</b> làm trọn một lần. Bảng chia y hệt: <b>т</b> hoá <b>ч</b> '
    'ở ngôi «tôi», trọng âm lùi từ ngôi hai — <b>заплачу́</b>, <b>запла́тишь</b>.</div>'
    '<div class="hd-warn">Trả cho CÁI GÌ phải có <b>за</b> + cách 4: <b>заплати́ть за ко́фе</b>. '
    'Trả cho AI thì cách 3, không giới từ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>плати́ть</b> trả tiền (CHT) · <b>пла́та</b> tiền phí · '
    '<b>зарпла́та</b> tiền lương · <b>беспла́тный</b> miễn phí</div>'
)

# -------------------------------------------------------- платить
S["платить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">плат-</span>'
    '<span class="hd-gloss">gốc TRẢ TIỀN — như <b>пла́та</b> tiền phí</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>плат-</b> có mặt trong mọi chữ về khoản phải trả: <b>зарпла́та</b> lương, '
    '<b>беспла́тный</b> không mất tiền. Trả cho cái gì: <b>за</b> + cách 4 — '
    '<b>плати́ть за кварти́ру</b>. Cặp HT: <b>заплати́ть</b>.</div>'
    '<div class="hd-warn">Ngôi «tôi» <b>т</b> hoá <b>ч</b>, trọng âm ở đuôi: <b>я плачу́</b> = tôi '
    'trả. Nhấn sai thành <b>я пла́чу</b> là «tôi khóc» (của <b>пла́кать</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>заплати́ть</b> trả tiền (HT) · <b>пла́та</b> tiền phí · '
    '<b>зарпла́та</b> tiền lương · <b>беспла́тный</b> miễn phí · <b>пла́тный</b> mất phí</div>'
)

# -------------------------------------------------------- изменить
S["изменить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">из-</span>'
    '<span class="hd-gloss">RA KHỎI (trạng thái cũ)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мен-</span>'
    '<span class="hd-gloss">ĐỔI — như <b>меня́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đổi cho nó ra khỏi dáng cũ ⇒ thay đổi CHÍNH sự vật đó (<b>измени́ть план</b>), '
    'khác <b>меня́ть</b> là bỏ cái này lấy cái khác. Trọng âm lùi từ ngôi hai: '
    '<b>изменю́</b>, <b>изме́нишь</b>.</div>'
    '<div class="hd-warn">Cách quyết định nghĩa: + cách 4 = thay đổi; + cách 3 = phản bội, ngoại '
    'tình — <b>Он измени́л жене́</b> = Anh ta phản bội vợ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>изменя́ть</b> thay đổi (CHT) · <b>измене́ние</b> sự thay đổi · '
    '<b>изме́на</b> sự phản bội · <b>меня́ть</b> đổi</div>'
)

# -------------------------------------------------------- изменять
S["изменять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">измен-</span>'
    '<span class="hd-gloss">thay đổi — chính là <b>измени́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́ть</span>'
    '<span class="hd-gloss">đuôi CHƯA hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp thể chỉ đổi đuôi <b>-и́ть → -я́ть</b>, chia đều: <b>изменя́ю</b>. '
    'Vẫn hai nghĩa theo cách: + cách 4 thay đổi, + cách 3 phản bội — '
    '<b>Он изменя́ет жене́</b> = Anh ta ngoại tình.</div>'
    '<div class="hd-warn">Tự mình thay đổi thì thêm <b>-ся</b>: <b>Он о́чень измени́лся</b> = '
    'Anh ấy thay đổi nhiều quá.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>измени́ть</b> thay đổi (HT) · <b>измене́ние</b> sự thay đổi · '
    '<b>изме́на</b> sự phản bội · <b>изме́нник</b> kẻ phản bội</div>'
)

# -------------------------------------------------------- менять
S["менять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мен-</span>'
    '<span class="hd-gloss">gốc ĐỔI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́ть</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cốt lõi là ĐỔI CHỖ: cái này đi, cái khác vào — <b>меня́ть ла́мпочку</b> thay '
    'bóng đèn, <b>меня́ть де́ньги</b> đổi tiền. Sửa đổi bản thân sự vật thì là '
    '<b>изменя́ть</b>. Chia đều: <b>меня́ю</b>, <b>меня́ешь</b>.</div>'
    '<div class="hd-warn">Đổi X LẤY Y: cách 4 + <b>на</b> + cách 4 — '
    '<b>меня́ть до́ллары на рубли́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поменя́ть</b> đổi (HT) · <b>обме́н</b> sự trao đổi · '
    '<b>изменя́ть</b> thay đổi</div>'
)

# -------------------------------------------------------- поменять
S["поменять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố thể, KHÔNG mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-меня́ть</span>'
    '<span class="hd-gloss">đổi — chính là <b>меня́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>меня́ть</b> làm trọn một lần, cùng ý đổi chỗ (cái này đi, cái khác vào). '
    'Chia đều: <b>поменя́ю</b>, <b>поменя́ешь</b>.</div>'
    '<div class="hd-warn">Đổi CHO NHAU thì thêm <b>-ся</b>: '
    '<b>Дава́й поменя́емся места́ми</b> = Mình đổi chỗ cho nhau nhé.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>меня́ть</b> đổi (CHT) · <b>обме́н</b> sự trao đổi · '
    '<b>измени́ть</b> thay đổi</div>'
)

# -------------------------------------------------------- казаться
S["казаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">каз-</span>'
    '<span class="hd-gloss">gốc ĐƯA RA CHO THẤY — như <b>показа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">CHÍNH MÌNH</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tự đưa mình ra cho người ta thấy ⇒ trông có vẻ. Tính chất đi sau ở cách 5: '
    '<b>Он ка́жется уста́лым</b> = Anh ấy trông có vẻ mệt. Chia như <b>сказа́ть</b>: '
    '<b>кажу́сь</b>, <b>ка́жешься</b>.</div>'
    '<div class="hd-warn">Hai câu dùng hằng ngày: <b>Мне ка́жется, что…</b> = Tôi nghĩ là… · '
    '<b>Ка́жется</b> đứng đầu câu = hình như…</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>показа́ться</b> có vẻ (HT) · <b>показа́ть</b> cho xem · '
    '<b>сказа́ть</b> nói ra</div>'
)

# -------------------------------------------------------- показаться
S["показаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">показа́-</span>'
    '<span class="hd-gloss">cho xem — chính là <b>показа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">CHÍNH MÌNH</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cho người khác thấy CHÍNH MÌNH ⇒ hai nghĩa: trông có vẻ (HT của '
    '<b>каза́ться</b>) — <b>Мне показа́лось…</b> = Tôi tưởng là…; và ló ra, hiện ra — '
    '<b>Показа́лось со́лнце</b>. Chia: <b>покажу́сь</b>, <b>пока́жешься</b>.</div>'
    '<div class="hd-warn"><b>Показа́ться врачу́</b> (cách 3) = đi khám bác sĩ — đưa mình cho bác sĩ xem.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>каза́ться</b> có vẻ (CHT) · <b>показа́ть</b> cho xem · '
    '<b>пока́зывать</b> cho xem (CHT)</div>'
)

# -------------------------------------------------------- класть
S["класть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">клад-</span>'
    '<span class="hd-gloss">gốc ĐẶT NẰM, xếp — lộ ra ở <b>кладу́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể; <b>д</b> đứng trước <b>т</b> thành <b>с</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đặt cho vật NẰM: sách lên bàn, ví vào túi, đường vào trà. Đặt ĐỨNG là '
    '<b>ста́вить</b>. Nguyên thể giấu chữ <b>д</b>, bảng chia lộ ra: <b>кладу́</b>, '
    '<b>кладёшь</b>; quá khứ rụng <b>д</b>: <b>клал</b>, <b>кла́ла</b> — y như '
    '<b>вести́ → веду́ → вёл</b>.</div>'
    '<div class="hd-warn">Cặp HT khác hẳn gốc: <b>положи́ть</b>. Dạng <i>ложи́ть</i> là SAI chuẩn — '
    'CHT luôn là <b>класть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>склад</b> kho hàng · <b>закла́дка</b> thẻ kẹp sách · '
    '<b>клад</b> kho báu</div>'
)

# -------------------------------------------------------- положить
S["положить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố thể, KHÔNG mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лож-</span>'
    '<span class="hd-gloss">gốc NẰM — họ với <b>лежа́ть</b>, <b>лечь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm cho vật NẰM xuống ⇒ đặt nằm, bỏ vào. Đặt tới đâu thì '
    '<b>в/на</b> + cách 4: <b>положи́ть кни́гу на стол</b>. Trọng âm lùi: <b>положу́</b>, '
    '<b>поло́жишь</b>. Cặp CHT khác gốc: <b>класть</b>.</div>'
    '<div class="hd-warn"><b>Положи́ть тру́бку</b> = cúp máy (đặt ống nghe xuống).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лежа́ть</b> nằm · <b>лечь</b> nằm xuống · <b>ложи́ться</b> đi nằm · '
    '<b>положе́ние</b> vị trí, tình hình</div>'
)

# -------------------------------------------------------- летать
S["летать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">лет-</span>'
    '<span class="hd-gloss">gốc BAY</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Động từ chuyển động NHIỀU CHIỀU: bay lượn, bay qua lại, hay bay đều đặn — '
    '<b>Я ча́сто лета́ю в Москву́</b>. Bay MỘT chiều, đang trên đường tới đâu là '
    '<b>лете́ть</b>; cặp y hệt <b>ходи́ть ↔ идти́</b>. Chia đều: <b>лета́ю</b>.</div>'
    '<div class="hd-warn">Quá khứ <b>лета́л</b> = đã bay đi VÀ đã về: <b>Я лета́л в Москву́</b> = '
    'Tôi đã có một chuyến bay đi Moskva.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лете́ть</b> bay (một chiều) · <b>самолёт</b> máy bay (tự bay) · '
    '<b>полёт</b> chuyến bay · <b>лётчик</b> phi công</div>'
)

# ============================================================ field Vietnamese
V = {
    # Bỏ "giải thích": nghĩa nới rộng, trùng объяснять (k96). Thêm "chứng tỏ" (demonstrate)
    # cho đủ đôi với доказывать — badge thể tách hai vế.
    "доказать": "chứng minh, chứng tỏ",
    "доказывать": "chứng minh, chứng tỏ",
    # Bỏ "kết thúc" và "xong" trơn: thuộc кончить/кончать (k85/k87). Giữ "hoàn thành".
    "закончить": "hoàn thành, làm xong",
    "заканчивать": "hoàn thành, làm xong",
    # Bỏ "nhận ra": trùng узнать (k81) / понимать (k54). "nhận xét" = to remark (gloss có).
    "заметить": "để ý thấy, chú ý thấy, nhận xét",
    "замечать": "để ý thấy, chú ý thấy",
    # Tách khỏi менять/поменять: изменить(-ять) = thay đổi chính sự vật + phản bội (cách 3).
    "изменить": "thay đổi, phản bội, ngoại tình",
    "изменять": "thay đổi, phản bội, ngoại tình",
    # менять/поменять = đổi cái này lấy cái khác (replace / exchange / swap). Bỏ "thay đổi"
    # (nhường изменить), bỏ "đổi mới" (renovate — gloss không có).
    "менять": "đổi, thay, trao đổi",
    "поменять": "đổi, thay, trao đổi",
    # Bỏ "đặt"/"để" trơn: trùng ставить (k80). Theo đối lập nằm/đứng với поставить.
    "класть": "đặt nằm, bỏ vào",
    "положить": "đặt nằm, bỏ vào",
    # Bỏ "xuất hiện": trùng найтись (k80) / появиться (k97).
    "показаться": "có vẻ, dường như",
    # Nhiều chiều; "bay" trơn để dành лететь (k107), như ходить "đi lại" vs идти.
    "летать": "bay lượn, bay qua lại",
}
