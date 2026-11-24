# -*- coding: utf-8 -*-
"""k206 — actions: 10 cặp thể + отрезать; trục là GỐC + TIỀN TỐ.

Chỗ cần nhất quán trong lô:
(1) отражать/отразить: -раз-/-раж- ĐÁNH (khớp выразить k135, поразить k188); от- = bật ngược lại.
(2) отрезать (HT, отре́зать, OpenRussian 2713): khớp резать k142 («от- rời ra»); bẫy là cặp CHT
    отреза́ть cùng mặt chữ.
(3) нажать/нажимать: -жа- (жм-) / -жим- BÓP, ÉP — khớp пожать k185.
(4) обнимать/обнять, вынимать/вынуть: -ним-/-ня- LẤY — khớp снять/снимать k122, отнимать k142.
(5) набрать: -бр- (бер-) = брать.
(6) махать/махнуть: -ну- MỘT LẦN.
(7) исключать/исключить, отключать/отключить: -ключ- MÓC, KHOÁ — khớp исключение k161,
    выключать/включить k94.
(8) владеть: влад- CAI QUẢN — khớp власть k115, владелец k163.
(9) увести/уводить: khuôn вести k113 «вес- (вед-) DẪN» / водить k107 «вод- DẪN»; у- RỜI KHỎI
    khớp увезти/увозить k143.
Họ hàng cố ý vắng: không có (mọi từ đều có họ thật).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "отражать": "phản chiếu, phản ánh, thể hiện, đẩy lui",                 # + repel / fend off
    "отразить": "phản chiếu, dội lại, phản ánh, thể hiện, đẩy lui",        # + convey, repel
    "нажать": "ấn, bấm, nhấn, gây áp lực",                                  # hai thể cùng gloss
    "нажимать": "ấn, bấm, nhấn, gây áp lực",                                # + put pressure on
    "набрать": "bấm số, gõ, gom, thu được, tích luỹ, tăng, tuyển",               # gather, accumulate, recruit
    "махать": "vẫy, vung, đập cánh, khoát",                                 # + to swing
    "исключать": "loại trừ, loại ra, trừ ra, khai trừ",                     # «bỏ ra» không phải nghĩa; + expel
    "исключить": "loại trừ, loại bỏ, loại ra, khai trừ",
    "отключать": "ngắt kết nối, cắt",                                       # gỡ ⊇ выключа́ть[k94]; gloss chỉ cut off / disconnect, «tắt» là nới rộng
    "отключить": "ngắt kết nối, cắt, tắt",                                  # gỡ ⊇ вы́ключить[k94]; «tắt» = turn off, gloss có
    "грабить": "cướp, cướp bóc, trấn lột",                                  # «trấn cướp» không phải từ; «bóc lột» = exploit, sai nghĩa
    "ограбить": "cướp, cướp bóc, trấn lột",
    "увести": "dẫn đi, đưa đi, dắt đi, cuỗm",                               # + steal / walk off with
    "уводить": "dẫn đi, đưa đi, dắt đi, cuỗm",
}

# --------------------------------------------------------------------- отражать
S["отражать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">NGƯỢC LẠI, bật ra khỏi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-раж-</span>'
    '<span class="hd-gloss">= <i>-раз-</i> ĐÁNH (з → ж), như <b>выража́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>отража́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đánh bật NGƯỢC LẠI ⇒ đẩy lui đòn: <b>отража́ть ата́ку</b>. Ánh sáng bị '
    'bật ngược ⇒ phản chiếu; đời thật hiện lại trong sách, tranh ⇒ phản ánh. Cặp HT: '
    '<b>отрази́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отрази́ть</b> (HT) · <b>отраже́ние</b> hình phản chiếu, sự phản ánh · '
    '<b>выража́ть</b> diễn đạt · <b>поража́ть</b> làm sửng sốt</div>'
)

# --------------------------------------------------------------------- отразить
S["отразить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">NGƯỢC LẠI, bật ra khỏi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-раз-</span>'
    '<span class="hd-gloss">ĐÁNH, giáng — như <b>порази́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp HT của <b>отража́ть</b> — nghĩa xem ở thẻ đó. Ở thể này gốc giữ '
    'đúng <i>з</i>, chỉ «tôi» hoá <i>ж</i>: <b>я отражу́</b>, <b>ты отрази́шь</b> — y như '
    '<b>порази́ть → поражу́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отража́ть</b> (CHT) · <b>отраже́ние</b> sự phản chiếu · '
    '<b>вы́разить</b> diễn đạt · <b>порази́ть</b> đánh trúng, làm sửng sốt</div>'
)

# --------------------------------------------------------------------- отрезать
S["отрезать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">RỜI RA, tách khỏi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ре́з-а-ть</span>'
    '<span class="hd-gloss">CẮT — chính là <b>ре́зать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cắt cho một phần RỜI ra: <b>отре́зать кусо́к хле́ба</b>. Nghĩa bóng: cắt '
    'đứt đường đi; cắt ngang bằng một câu cộc lốc. Như <b>ре́зать</b>, <i>з → ж</i> ở mọi ngôi '
    'tương lai, trọng âm đứng yên: <b>отре́жу, отре́жешь</b>.</div>'
    '<div class="hd-warn">Cặp CHT cùng mặt chữ, chỉ khác chỗ nhấn: <b>отре́зать</b> (HT, cắt xong) · '
    '<b>отреза́ть</b> (CHT, chia đều <b>отреза́ю</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ре́зать</b> cắt · <b>поре́зать</b> cắt (HT) · '
    '<b>наре́зать</b> thái ra · <b>ре́зкий</b> gắt, đột ngột</div>'
)

# --------------------------------------------------------------------- нажать
S["нажать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">LÊN trên bề mặt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-жа-ть (жм-)</span>'
    '<span class="hd-gloss">BÓP, ÉP — như <b>пожа́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ép LÊN một chỗ ⇒ ấn, bấm một cái; ép lên người ⇒ gây áp lực. Nguyên thể '
    'giấu mất <i>м</i>, tương lai mới lộ gốc thật <b>жм-</b>: <b>нажму́, нажмёшь</b>. Cặp CHT: '
    '<b>нажима́ть</b>.</div>'
    '<div class="hd-warn">Bấm VÀO cái gì thường đi với <b>на</b> + cách 4: <b>Нажми́ на кно́пку!</b> '
    'Bấm nút đi! · <b>нажа́ть на газ</b> đạp ga.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>нажима́ть</b> (CHT) · <b>пожа́ть</b> bắt tay · '
    '<b>сжать</b> siết chặt · <b>нажи́м</b> sức ép</div>'
)

# --------------------------------------------------------------------- нажимать
S["нажимать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">LÊN trên bề mặt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-жим-</span>'
    '<span class="hd-gloss">BÓP, ÉP — mặt khác của <i>жм-</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>нажима́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>нажа́ть</b> — nghĩa xem ở thẻ đó. Hai thể chia hai kiểu '
    'khác hẳn: <b>нажима́ю</b> (đều) ↔ <b>нажму́</b> (thân <i>жм-</i>). Cùng khuôn '
    '<b>пожима́ть : пожа́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>нажа́ть</b> (HT) · <b>пожима́ть</b> bắt tay (CHT) · '
    '<b>нажи́м</b> sức ép</div>'
)

# --------------------------------------------------------------------- обнимать
S["обнимать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">VÒNG QUANH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ним-</span>'
    '<span class="hd-gloss">NẮM, LẤY — như <b>снима́ть</b>, <b>понима́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>обнима́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đưa tay VÒNG QUANH mà nắm lấy ⇒ ôm. Cặp HT: <b>обня́ть</b>.</div>'
    '<div class="hd-warn"><b>Обнима́ю!</b> — câu chào cuối tin nhắn, thư gửi người thân: «ôm bạn», '
    'như tiếng Anh <i>hugs</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обня́ть</b> (HT) · <b>снима́ть</b> cởi, tháo · '
    '<b>понима́ть</b> hiểu · <b>отнима́ть</b> lấy đi</div>'
)

# --------------------------------------------------------------------- обнять
S["обнять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">VÒNG QUANH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ня-ть</span>'
    '<span class="hd-gloss">NẮM, LẤY — như <b>снять</b>, <b>подня́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ôm choàng lấy một cái; nghĩa bóng: bao trùm, thu cả vào tầm mắt. Tương '
    'lai lộ <i>-ним-</i> và trọng âm lùi sau «tôi»: <b>обниму́, обни́мешь</b>; quá khứ giống cái '
    'nhấn đuôi: <b>обняла́</b>. Cặp CHT: <b>обнима́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обнима́ть</b> (CHT) · <b>снять</b> cởi, tháo · '
    '<b>поня́ть</b> hiểu · <b>взять</b> lấy</div>'
)

# --------------------------------------------------------------------- вынимать
S["вынимать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span>'
    '<span class="hd-gloss">RA ngoài</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ним-</span>'
    '<span class="hd-gloss">NẮM, LẤY — như <b>снима́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>вынима́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">LẤY RA khỏi chỗ chứa, chỗ chứa đứng sau <b>из</b> + cách 2: '
    '<b>вынима́ть ключи́ из карма́на</b> lấy chìa khoá ra khỏi túi. Cặp HT: <b>вы́нуть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вы́нуть</b> (HT) · <b>снима́ть</b> cởi, tháo · '
    '<b>отнима́ть</b> lấy đi · <b>понима́ть</b> hiểu</div>'
)

# --------------------------------------------------------------------- вынуть
S["вынуть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы́-</span>'
    '<span class="hd-gloss">RA ngoài — ở thể HT luôn mang trọng âm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ну-ть</span>'
    '<span class="hd-gloss">gốc LẤY đã mòn — nhìn qua cặp <b>вынима́ть</b> mới thấy</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Lấy ra một lần cho xong: <b>вы́нуть письмо́ из я́щика</b>. Chia như '
    'động từ <i>-нуть</i> thường, trọng âm không rời <b>вы́</b>: <b>вы́ну, вы́нешь, вы́нул</b>. '
    'Mệnh lệnh: <b>вы́нь!</b></div>'
    '<div class="hd-warn">⚠️ Mức tin: coi <i>-ну-</i> là mảnh mòn của gốc «lấy» (dạng cổ '
    '<i>вы́нять</i>) là từ nguyên, không phải luật suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вынима́ть</b> (CHT) · <b>снять</b> cởi, tháo · <b>взять</b> lấy</div>'
)

# --------------------------------------------------------------------- набрать
S["набрать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">DỒN cho ĐẦY, cho nhiều</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бр-а-ть (бер-)</span>'
    '<span class="hd-gloss">LẤY — chính là <b>брать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Lấy dồn cho đủ ⇒ gom, thu: <b>набра́ть воды́</b> (cách 2 = một lượng). Gom '
    'từng chữ số ⇒ bấm số: <b>набра́ть но́мер</b>; gom từng chữ ⇒ gõ văn bản. Chia như '
    '<b>брать</b>: <b>наберу́, наберёшь</b>; quá khứ giống cái <b>набрала́</b>.</div>'
    '<div class="hd-warn"><b>набра́ть вес</b> = lên cân · <b>набра́ть ско́рость</b> = tăng tốc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>набира́ть</b> (CHT) · <b>брать</b> lấy · <b>собра́ть</b> thu gom · '
    '<b>вы́брать</b> chọn · <b>набо́р</b> bộ, đợt tuyển</div>'
)

# --------------------------------------------------------------------- махать
S["махать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мах-</span>'
    '<span class="hd-gloss">VUNG, vẫy — gốc trơn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vung đi vung lại ⇒ vẫy tay, đập cánh, vẫy đuôi. Thứ đem ra vẫy đứng ở '
    'cách 5: <b>маха́ть руко́й</b>, <b>маха́ть кры́льями</b>; vẫy chào ai thì + cách 3. Vẫy một '
    'cái: <b>махну́ть</b>.</div>'
    '<div class="hd-warn"><i>х → ш</i> ở MỌI ngôi hiện tại, trọng âm lùi sau «tôi»: <b>машу́, '
    'ма́шешь, ма́шут</b> (như <b>писа́ть → пишу́</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>махну́ть</b> vẫy một cái (HT) · <b>разма́х</b> tầm vung, quy mô · '
    '<b>взмах</b> cú vung</div>'
)

# --------------------------------------------------------------------- махнуть
S["махнуть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мах-</span>'
    '<span class="hd-gloss">VUNG, vẫy</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ну́-ть</span>'
    '<span class="hd-gloss">MỘT LẦN — như <b>кри́кнуть</b> hét một tiếng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vẫy MỘT cái là xong. Chia đều theo <i>-нуть</i>: <b>махну́, махнёшь</b> — '
    'không biến âm như <b>маха́ть → машу́</b>. Khẩu ngữ còn là «phóng đi»: <b>махну́ть на '
    'мо́ре</b>.</div>'
    '<div class="hd-warn"><b>махну́ть руко́й на</b> + cách 4 = buông xuôi, mặc kệ: <b>Он махну́л '
    'руко́й на учёбу.</b> Nó bỏ mặc chuyện học.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>маха́ть</b> vẫy (CHT) · <b>разма́х</b> tầm vung, quy mô</div>'
)

# --------------------------------------------------------------------- исключать
S["исключать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ис-</span>'
    '<span class="hd-gloss">= из- RA KHỎI (з → с trước к)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ключ-</span>'
    '<span class="hd-gloss">MÓC, KHOÁ — như trong <b>включа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>исключа́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>включа́ть</b> móc vào ↔ <b>исключа́ть</b> móc ra khỏi ⇒ loại ra, loại '
    'trừ; khỏi trường, khỏi đảng ⇒ khai trừ: <b>исключа́ть из</b> + cách 2. Cặp HT: '
    '<b>исключи́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>исключи́ть</b> (HT) · <b>исключе́ние</b> ngoại lệ · '
    '<b>исключи́тельно</b> chỉ riêng; đặc biệt · <b>включа́ть</b> bật, gộp vào</div>'
)

# --------------------------------------------------------------------- исключить
S["исключить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ис-</span>'
    '<span class="hd-gloss">= из- RA KHỎI (з → с trước к)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ключ-</span>'
    '<span class="hd-gloss">MÓC, KHOÁ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Móc ra khỏi một lần cho xong ⇒ loại bỏ, khai trừ: <b>Его́ исключи́ли из '
    'шко́лы.</b> Nó bị đuổi học. Trọng âm ở ĐUÔI suốt bảng như <b>включи́ть</b>: <b>исключу́, '
    'исключи́шь</b>.</div>'
    '<div class="hd-warn"><b>Не исключено́, что…</b> = không loại trừ khả năng là…, có thể là…</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>исключа́ть</b> (CHT) · <b>исключе́ние</b> ngoại lệ · '
    '<b>включи́ть</b> bật · <b>ключ</b> chìa khoá</div>'
)

# --------------------------------------------------------------------- отключать
S["отключать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">TÁCH RỜI ra</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ключ-</span>'
    '<span class="hd-gloss">MÓC, KHOÁ — như <b>включа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>отключа́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tháo móc cho RỜI khỏi nguồn ⇒ ngắt kết nối, cắt điện, nước, mạng: '
    '<b>Ле́том отключа́ют горя́чую во́ду.</b> Mùa hè bị cắt nước nóng. Cặp HT: '
    '<b>отключи́ть</b>.</div>'
    '<div class="hd-warn"><b>вы́ключить свет</b> = tự tay tắt đèn ở công tắc · <b>отключи́ть '
    'свет</b> = cắt điện, ngắt khỏi nguồn — thường là bên điện lực cắt.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отключи́ть</b> (HT) · <b>выключа́ть</b> tắt · '
    '<b>включа́ть</b> bật · <b>ключ</b> chìa khoá</div>'
)

# --------------------------------------------------------------------- отключить
S["отключить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">TÁCH RỜI ra</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ключ-</span>'
    '<span class="hd-gloss">MÓC, KHOÁ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp HT của <b>отключа́ть</b> — phép so với <b>вы́ключить</b> ở thẻ đó. '
    'Ngắt cho xong: <b>отключи́ть телефо́н</b> tắt máy, ngắt khỏi mạng. Trọng âm ở ĐUÔI suốt '
    'bảng như <b>включи́ть</b>: <b>отключу́, отключи́шь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отключа́ть</b> (CHT) · <b>вы́ключить</b> tắt · '
    '<b>исключи́ть</b> loại trừ · <b>ключ</b> chìa khoá</div>'
)

# --------------------------------------------------------------------- владеть
S["владеть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">влад-</span>'
    '<span class="hd-gloss">CAI QUẢN, nắm giữ — như <b>власть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́-ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ nhất, chia đều: <b>владе́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nắm trong tay ⇒ sở hữu; nắm vững ⇒ thông thạo. Tiếng Anh <i>wield</i> '
    '(cầm, nắm quyền) là họ hàng Ấn–Âu xa.</div>'
    '<div class="hd-warn">Thứ được nắm đứng ở cách 5: <b>владе́ть до́мом</b> làm chủ căn nhà · '
    '<b>владе́ть ру́сским языко́м</b> thông thạo tiếng Nga.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>владе́лец</b> chủ sở hữu · <b>власть</b> quyền lực · '
    '<b>о́бласть</b> tỉnh, vùng · <b>завладе́ть</b> chiếm lấy</div>'
)

# --------------------------------------------------------------------- грабить
S["грабить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">граб-</span>'
    '<span class="hd-gloss">VỒ LẤY, cào về mình</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vồ lấy của người khác ⇒ cướp, cướp bóc; người, nhà, ngân hàng bị cướp '
    'đứng cách 4. Tiếng Anh <i>grab</i> (vồ lấy) là họ hàng Ấn–Âu xa. Cặp HT: '
    '<b>огра́бить</b>.</div>'
    '<div class="hd-warn">«Tôi» chèn thêm <b>л</b> sau <i>б</i>: <b>гра́блю</b>, còn <b>гра́бишь</b> '
    '— như <b>люби́ть → люблю́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>огра́бить</b> (HT) · <b>граби́тель</b> kẻ cướp · '
    '<b>грабёж</b> vụ cướp · <b>гра́бли</b> cái cào</div>'
)

# --------------------------------------------------------------------- ограбить
S["ограбить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">tiền tố làm HT, không thêm nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-граб-и-ть</span>'
    '<span class="hd-gloss">VỒ LẤY — chính là <b>гра́бить</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cướp xong một vụ: <b>огра́бить банк</b>. Câu cần nhất: <b>Меня́ '
    'огра́били!</b> Tôi bị cướp rồi! (người bị cướp ở cách 4). «Tôi» cũng chèn <b>л</b>: '
    '<b>огра́блю</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гра́бить</b> (CHT) · <b>ограбле́ние</b> vụ cướp · '
    '<b>граби́тель</b> kẻ cướp</div>'
)

# --------------------------------------------------------------------- увести
S["увести"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">RỜI KHỎI, đi mất (như <b>уйти́</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вес-ти́ (вед-)</span>'
    '<span class="hd-gloss">DẪN — chính là <b>вести́</b>, gốc thật là <i>вед-</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dẫn đi khỏi đây, dắt đi mất. Chia như <b>вести́</b>: <b>уведу́, '
    'уведёшь</b>; quá khứ rơi <i>д</i>: <b>увёл, увела́</b>. Cặp CHT: <b>уводи́ть</b>.</div>'
    '<div class="hd-warn">Dắt đi MẤT ⇒ cuỗm: <b>увести́ маши́ну</b> trộm xe · <b>увести́ му́жа</b> '
    'cướp chồng người khác.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уводи́ть</b> (CHT) · <b>вести́</b> dẫn · '
    '<b>привести́</b> dẫn tới · <b>увезти́</b> chở đi mất</div>'
)

# --------------------------------------------------------------------- уводить
S["уводить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">RỜI KHỎI, đi mất</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вод-и́ть</span>'
    '<span class="hd-gloss">DẪN — chính là <b>води́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>увести́</b> — nghĩa xem ở thẻ đó. Có tiền tố rồi thì hết '
    'nghĩa «nhiều chiều»: chỉ còn là đang / hay dẫn đi. Chia như <b>води́ть</b>: «tôi» '
    '<i>д → ж</i>, trọng âm lùi — <b>увожу́, уво́дишь</b>.</div>'
    '<div class="hd-warn"><b>я увожу́</b> vừa là «tôi dẫn đi» (<b>уводи́ть</b>) vừa là «tôi chở đi» '
    '(<b>увози́ть</b>). Ngôi khác mới tách: <b>уво́дишь</b> / <b>уво́зишь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>увести́</b> (HT) · <b>води́ть</b> dẫn · '
    '<b>увози́ть</b> chở đi · <b>уходи́ть</b> đi khỏi</div>'
)

B = {
    "docbangmat": 131,
    "loitubat": 0,
    "nguonsai": 4,
    "baolen": [
        "Va chạm отключа́ть/отключи́ть ⊇ выключа́ть/вы́ключить[k94 đã nạp] «ngắt, tắt»: gỡ phía mình bằng V — отключа́ть «ngắt kết nối, cắt» (gloss chỉ có cut off / disconnect; «tắt» là nới rộng nên bỏ), отключи́ть «ngắt kết nối, cắt, tắt» (gloss có turn off). Thẻ k94 không đụng. Đã chạy thử do_va_cham (chỉ đọc Anki) với V mới thay vào: 0 va chạm dính từ của lô.",
        "V cần duyệt (14 thẻ): отража́ть/отрази́ть + «đẩy lui» (repel); нажа́ть/нажима́ть thống nhất «ấn, bấm, nhấn, gây áp lực»; набра́ть «bấm số, gõ, gom, thu được, tích luỹ, tuyển»; маха́ть + «vung»; исключа́ть/исключи́ть bỏ «bỏ ra», thêm «loại ra, khai trừ»; гра́бить/огра́бить «cướp, cướp bóc, trấn lột» (bỏ «trấn cướp» — không phải từ — và «bóc lột» — nghĩa khác, exploit; bỏ «trộm cướp»); увести́/уводи́ть «dẫn đi, đưa đi, dắt đi, cuỗm». 7 thẻ còn lại giữ đề cũ.",
        "Nguồn sai đã bác (4): гра́бить «bóc lột» và «trấn cướp» (cả огра́бить); исключа́ть «bỏ ra»; CACH DUNG của владе́ть ghi завладе́ть là cặp HT — thực ra khác nghĩa (chiếm lấy), chỉ để vào Họ hàng, không gọi là cặp thể.",
        "Chỗ KHÔNG chắc: (1) вы́нуть — -ну- là mảnh mòn của gốc «lấy» (dạng cổ вы́нять) là từ nguyên, đã ghi ô ⚠️ Mức tin. (2) Bắc cầu tiếng Anh wield ↔ владе́ть và grab ↔ гра́бить: theo từ nguyên phổ biến là cùng gốc Ấn–Âu xa, viết mềm «họ hàng Ấn–Âu xa», không khẳng định chặt. (3) гра́бли (cái cào) nối với гра́бить theo Vasmer.",
        "loitubat = 0 là thật: hai chỗ dễ nói quá (вы́нуть, о- của огра́бить «không thêm nghĩa riêng») đã hạ mức ngay lúc soạn, không phải sửa sau khi đọc lại.",
    ],
}
