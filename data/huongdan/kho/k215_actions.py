# -*- coding: utf-8 -*-
"""k215 — actions: 8 cặp thể + бродить, тащить, гнать, течь; trục là GỐC + TIỀN TỐ.

Chỗ cần nhất quán trong lô:
(1) гнать / догнать / выгнать: гон-/гн- ĐUỔI, PHÓNG — khớp гонка k174; CHT -гон-я́ть chia đều.
(2) повысить/повышать: выс- (с → ш) CAO — khớp высокий k40.
(3) сократить/сокращать: со- mờ nghĩa + крат-/кращ- NGẮN — khớp сокращение k200, прекратить k160.
(4) возглавить/возглавлять: глав- CÁI ĐẦU — khớp главный k109.
(5) освободиться/-ждаться: о- LÀM CHO + свобод- TỰ DO — khớp освободить k131.
(6) подчиниться: чин- CẤP BẬC — khớp чиновник k178; KHÔNG phải -чин- BẮT ĐẦU của начинать k85.
(7) тащить: -тащ- KÉO LÊ — khớp вытащить k171. (8) течь: тек-/ток CHẢY — khớp поток k179.
Họ hàng cố ý vắng: không có (mọi từ đều có họ thật).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "нарушать": "vi phạm, làm trái, phá vỡ, làm xáo trộn",            # hai thể cùng gloss; + disrupt / disturb
    "нарушить": "vi phạm, làm trái, phá vỡ, làm xáo trộn",
    "повысить": "nâng lên, tăng lên, cải thiện, thăng chức",          # + improve / enhance
    "сократить": "rút ngắn, cắt giảm, viết tắt, cho thôi việc",       # «tinh gọn» là nới rộng; + abbreviate, lay off
    "сокращать": "rút ngắn, cắt giảm, viết tắt, cho thôi việc",
    "бродить": "lang thang, đi lông bông, lên men",                    # + to ferment
    "тащить": "kéo, lôi, kéo lê, khuân",                              # «mang nặng» không ai nói; lug = khuân
    "возглавить": "lên đứng đầu, đứng ra lãnh đạo, dẫn đầu",          # «nhận lãnh đạo» không thành câu
    "возглавлять": "đứng đầu, lãnh đạo, phụ trách, dẫn đầu",          # + to top / be at the top of
    "течь": "chảy, tuôn, rò rỉ, trôi qua",                            # + to pass / elapse
    "освободиться": "được rảnh, thoát khỏi, giải phóng bản thân, trống chỗ",    # + become available
    "освобождаться": "được rảnh, thoát khỏi, giải phóng bản thân, trống chỗ",   # + become vacant
}

# --------------------------------------------------------------------- нарушать
S["нарушать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-руш-</span>'
    '<span class="hd-gloss">SỤP ĐỔ — gốc của <b>ру́шить</b> làm sụp</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>наруша́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm «sụp» một trật tự đang yên ⇒ phá vỡ luật (vi phạm), phá vỡ sự yên '
    'tĩnh (làm xáo trộn). Thứ bị phá đứng cách 4, không cần giới từ: <b>наруша́ть зако́н</b>, '
    '<b>наруша́ть тишину́</b>. Cặp HT: <b>нару́шить</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>нару́шить</b> (HT) · <b>наруше́ние</b> sự vi phạm · '
    '<b>наруши́тель</b> kẻ vi phạm · <b>разру́шить</b> phá huỷ</div>'
)

# --------------------------------------------------------------------- нарушить
S["нарушить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ру́ш-ить</span>'
    '<span class="hd-gloss">làm SỤP ĐỔ — chính là <b>ру́шить</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp HT của <b>наруша́ть</b> — nghĩa xem ở thẻ đó. Trọng âm tách hai thể: '
    'HT đứng yên ở gốc <b>нару́шу, нару́шишь</b>, CHT ở đuôi <b>наруша́ю</b>.</div>'
    '<div class="hd-warn"><b>нару́шить пра́вила</b> phạm quy · <b>нару́шить обеща́ние</b> thất hứa · '
    '<b>нару́шить молча́ние</b> phá tan im lặng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>наруша́ть</b> (CHT) · <b>наруше́ние</b> sự vi phạm · '
    '<b>разру́шить</b> phá huỷ · <b>ру́хнуть</b> đổ sập</div>'
)

# --------------------------------------------------------------------- повысить
S["повысить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вы́с-</span>'
    '<span class="hd-gloss">CAO — gốc của <b>высо́кий</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm cho CAO lên ⇒ tăng (giá, lương), nâng (chất lượng), thăng chức. '
    '<i>вы</i> ở đây là của gốc, không phải tiền tố RA NGOÀI. Chỉ ngôi «tôi» đổi <i>с → ш</i>: '
    '<b>повы́шу, повы́сишь</b>. Cặp CHT: <b>повыша́ть</b>.</div>'
    '<div class="hd-warn"><b>повы́сить го́лос</b> lên giọng, to tiếng · '
    '<b>повы́сить в до́лжности</b> thăng chức cho ai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>повыша́ть</b> (CHT) · <b>повыше́ние</b> sự tăng, sự thăng chức · '
    '<b>высо́кий</b> cao · <b>высота́</b> chiều cao</div>'
)

# --------------------------------------------------------------------- повышать
S["повышать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-выш-</span>'
    '<span class="hd-gloss">CAO — <i>выс-</i> với с → ш, như <b>вы́ше</b> cao hơn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>повыша́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>повы́сить</b> — nghĩa xem ở thẻ đó. Cặp HT <i>-сить</i> → '
    'CHT <i>-шать</i> là khuôn lặp: <b>пригласи́ть → приглаша́ть</b>. Dùng khi tăng dần hay tăng '
    'nhiều lần: <b>повыша́ть це́ны</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>повы́сить</b> (HT) · <b>повыше́ние</b> sự tăng · '
    '<b>вы́ше</b> cao hơn · <b>вы́сший</b> cao nhất</div>'
)

# --------------------------------------------------------------------- сократить
S["сократить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-крат-</span>'
    '<span class="hd-gloss">NGẮN — gốc của <b>кра́ткий</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm cho NGẮN lại: đường, bài viết ⇒ rút ngắn; chi phí ⇒ cắt giảm; từ ngữ '
    '⇒ viết tắt; nhân viên ⇒ cho thôi việc. Ngôi «tôi» <i>т → щ</i>: <b>сокращу́, сократи́шь</b> — '
    'như <b>прекращу́</b>. Cặp CHT: <b>сокраща́ть</b>.</div>'
    '<div class="hd-warn">Giảm ĐI bao nhiêu: <b>на</b> + cách 4; giảm XUỐNG CÒN: <b>до</b> + cách 2 — '
    '<b>сократи́ть на час</b> bớt một tiếng · <b>сократи́ть до ча́са</b> còn một tiếng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сокраща́ть</b> (CHT) · <b>сокраще́ние</b> sự cắt giảm, chữ viết tắt · '
    '<b>кра́ткий</b> ngắn gọn · <b>прекрати́ть</b> chấm dứt</div>'
)

# --------------------------------------------------------------------- сокращать
S["сокращать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-кращ-</span>'
    '<span class="hd-gloss">NGẮN — <i>крат-</i> với т → щ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>сокраща́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>сократи́ть</b> — nghĩa xem ở thẻ đó. Chữ <i>щ</i> đi suốt '
    'mọi ngôi; ở HT trong bảng chia nó chỉ ló ra ở «tôi». Cùng khuôn '
    '<b>прекрати́ть → прекраща́ть</b>. Hay gặp: <b>сокраща́ть расхо́ды</b> cắt giảm chi tiêu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сократи́ть</b> (HT) · <b>сокраще́ние</b> sự cắt giảm · '
    '<b>прекраща́ть</b> chấm dứt (CHT) · <b>коро́ткий</b> ngắn</div>'
)

# --------------------------------------------------------------------- бродить
S["бродить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">брод-</span>'
    '<span class="hd-gloss">LÊ BƯỚC — gốc của <b>брести́</b> (<b>бреду́</b>), е → о</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>брести́ : броди́ть</b> đúng khuôn <b>вести́ : води́ть</b>: <i>е</i> là lê '
    'bước về một hướng, <i>о</i> là nhiều hướng ⇒ lang thang. Đi KHẮP nơi nào: <b>по</b> + cách 3 — '
    '<b>броди́ть по го́роду</b>. «Tôi» đổi <i>д → ж</i>, trọng âm lùi từ ngôi 2: '
    '<b>брожу́, бро́дишь</b>.</div>'
    '<div class="hd-warn">Chủ ngữ là bột, rượu vang thì là nghĩa khác: LÊN MEN — '
    '<b>вино́ бро́дит</b>; danh từ <b>броже́ние</b> sự lên men.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>брести́</b> lê bước · <b>бродя́га</b> kẻ lang thang · '
    '<b>брод</b> chỗ cạn lội qua được</div>'
)

# --------------------------------------------------------------------- тащить
S["тащить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">тащ-</span>'
    '<span class="hd-gloss">KÉO LÊ — <i>таск-</i> của <b>таска́ть</b> với ск → щ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Kéo thứ nặng lê đi, hay khuân một cách ì ạch: <b>тащи́ть чемода́н</b>. '
    'Trọng âm lùi từ ngôi 2: <b>тащу́, та́щишь, та́щат</b>.</div>'
    '<div class="hd-warn">Cặp chuyển động, cả hai đều CHT: <b>тащи́ть</b> MỘT hướng, đang kéo · '
    '<b>таска́ть</b> kéo đi kéo lại, nhiều lần.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>таска́ть</b> kéo đi kéo lại · <b>вы́тащить</b> lôi ra · '
    '<b>тащи́ться</b> lê bước</div>'
)

# --------------------------------------------------------------------- гнать
S["гнать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">гн- / гон-</span>'
    '<span class="hd-gloss">ĐUỔI, PHÓNG — nguyên thể giấu <i>о</i>, hiện tại lộ ra</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bắt CHẠY phía trước mình ⇒ lùa (đàn bò), xua đuổi; bắt xe chạy hết '
    'sức ⇒ phóng: <b>Не гони́!</b> Đừng phóng nhanh thế! Quá khứ chỉ giống cái dịch trọng âm: '
    '<b>гнал, гнала́, гна́ло, гна́ли</b>.</div>'
    '<div class="hd-warn">Đuôi <i>-ать</i> mà chia lớp HAI, lại thêm <i>о</i>: <b>гоню́, го́нишь, '
    'го́нят</b> — cùng nhóm ngoại lệ với <b>держа́ть, дыша́ть, слы́шать</b>.</div>'
    '<div class="hd-warn">Cặp chuyển động, cả hai đều CHT: <b>гнать</b> MỘT hướng · <b>гоня́ть</b> '
    'nhiều hướng, đuổi qua đuổi lại.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>го́нка</b> cuộc đua · <b>догна́ть</b> đuổi kịp · '
    '<b>вы́гнать</b> đuổi ra · <b>пого́ня</b> cuộc truy đuổi</div>'
)

# --------------------------------------------------------------------- возглавить
S["возглавить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">воз-</span>'
    '<span class="hd-gloss">LÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-глав-</span>'
    '<span class="hd-gloss">CÁI ĐẦU — dạng Slav nhà thờ của <b>голова́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">LÊN làm cái ĐẦU ⇒ lên đứng đầu, đứng ra lãnh đạo. «Tôi» chen <i>л</i>: '
    '<b>возгла́влю, возгла́вишь</b>. Cặp CHT: <b>возглавля́ть</b>.</div>'
    '<div class="hd-warn">Đi thẳng cách 4, không giới từ: <b>возгла́вить компа́нию</b> lên đứng đầu '
    'công ty · <b>возгла́вить спи́сок</b> đứng đầu danh sách.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>возглавля́ть</b> (CHT) · <b>глава́</b> người đứng đầu, chương sách · '
    '<b>гла́вный</b> chính · <b>голова́</b> cái đầu</div>'
)

# --------------------------------------------------------------------- возглавлять
S["возглавлять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">воз-</span>'
    '<span class="hd-gloss">LÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-главл-</span>'
    '<span class="hd-gloss">CÁI ĐẦU — <i>глав-</i> chen thêm <i>л</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>возглавля́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>возгла́вить</b>: HT là lúc LÊN nắm, CHT là đang đứng đầu — '
    '<b>Он возглавля́ет институ́т</b> Ông ấy đứng đầu viện. Chữ <i>л</i> (в → вл) ở HT chỉ có '
    'ở «tôi», ở CHT đi suốt; cùng khuôn <b>испра́вить → исправля́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>возгла́вить</b> (HT) · <b>глава́</b> người đứng đầu · '
    '<b>гла́вный</b> chính · <b>заголо́вок</b> đầu đề</div>'
)

# --------------------------------------------------------------------- догнать
S["догнать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-</span>'
    '<span class="hd-gloss">TỚI NƠI, tới tận — như <b>дойти́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-гн-а́ть</span>'
    '<span class="hd-gloss">ĐUỔI — chính là <b>гнать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuổi TỚI NƠI ⇒ đuổi kịp. Chia đúng như <b>гнать</b>: <b>догоню́, '
    'дого́нишь</b>; quá khứ giống cái dịch trọng âm: <b>догна́л, догнала́</b>. Người bị đuổi kịp '
    'đứng cách 4: <b>догна́ть дру́га</b>.</div>'
    '<div class="hd-warn"><b>догна́ть</b> là KỊP; vượt qua là <b>обогна́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>догоня́ть</b> (CHT) · <b>гнать</b> lùa, đuổi · '
    '<b>обогна́ть</b> vượt qua · <b>го́нка</b> cuộc đua</div>'
)

# --------------------------------------------------------------------- догонять
S["догонять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-</span>'
    '<span class="hd-gloss">TỚI NƠI, tới tận</span></div>'
    '<div class="hd-row"><span class="hd-piece">-гон-</span>'
    '<span class="hd-gloss">ĐUỔI — mặt đủ nguyên âm của <i>гн-</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>догоня́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>догна́ть</b>: HT là đã kịp, CHT là đang rượt theo, chưa chắc '
    'kịp — <b>Я догоня́л его́, но не догна́л</b> Tôi đuổi theo mà không kịp.</div>'
    '<div class="hd-warn">Nhìn giống nhau nhưng hai thể: <b>догоня́ю</b> đang đuổi (CHT) · '
    '<b>догоню́</b> sẽ đuổi kịp (HT, của <b>догна́ть</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>догна́ть</b> (HT) · <b>гоня́ть</b> đuổi qua đuổi lại · '
    '<b>выгоня́ть</b> đuổi ra · <b>пого́ня</b> cuộc truy đuổi</div>'
)

# --------------------------------------------------------------------- выгнать
S["выгнать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы́-</span>'
    '<span class="hd-gloss">RA NGOÀI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-гн-ать</span>'
    '<span class="hd-gloss">ĐUỔI — chính là <b>гнать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuổi RA NGOÀI ⇒ tống cổ. Chia như <b>гнать</b> (lộ <i>о</i>), nhưng '
    '<b>вы́-</b> của HT giữ trọng âm ở mọi dạng: <b>вы́гоню, вы́гонишь, вы́гнала</b>. Cặp CHT: '
    '<b>выгоня́ть</b>.</div>'
    '<div class="hd-warn">Đuổi khỏi chỗ nào: <b>из</b> hoặc <b>с</b> + cách 2 — '
    '<b>вы́гнать из до́ма</b> đuổi khỏi nhà · <b>вы́гнать с рабо́ты</b> đuổi việc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>выгоня́ть</b> (CHT) · <b>гнать</b> lùa, đuổi · '
    '<b>догна́ть</b> đuổi kịp · <b>изгна́ние</b> sự trục xuất, lưu đày</div>'
)

# --------------------------------------------------------------------- выгонять
S["выгонять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span>'
    '<span class="hd-gloss">RA NGOÀI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-гон-</span>'
    '<span class="hd-gloss">ĐUỔI — mặt đủ nguyên âm của <i>гн-</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>выгоня́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>вы́гнать</b> — nghĩa xem ở thẻ đó. Khuôn cặp: HT '
    '<i>-гнать</i> → CHT <i>-гонять</i>, y như <b>догна́ть → догоня́ть</b>; sang CHT thì <i>вы-</i> '
    'nhả trọng âm cho đuôi. Lùa gia súc ra đồng cũng là từ này: <b>выгоня́ть коро́в</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вы́гнать</b> (HT) · <b>догоня́ть</b> đuổi theo · '
    '<b>гоня́ть</b> đuổi qua đuổi lại · <b>го́нка</b> cuộc đua</div>'
)

# --------------------------------------------------------------------- течь
S["течь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">тек- / теч-</span>'
    '<span class="hd-gloss">CHẢY — nguyên thể kiểu <i>-чь</i> đã nuốt <i>к</i> của gốc</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nước chảy; mái, vòi «chảy» ⇒ dột, rò: <b>Кры́ша течёт</b>; thời gian chảy ⇒ '
    'trôi qua. Chia như <b>печь</b>: <i>к</i> ở hai đầu, <i>ч</i> ở giữa — <b>теку́, течёшь, '
    'течёт… теку́т</b>. Quá khứ: <b>тёк, текла́, текло́, текли́</b>.</div>'
    '<div class="hd-warn">Cùng mặt chữ còn có danh từ giống cái <b>течь</b> «chỗ rò»: '
    '<b>ло́дка дала́ течь</b> thuyền bị rò.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тече́ние</b> dòng chảy · <b>пото́к</b> dòng, luồng (е → о) · '
    '<b>ток</b> dòng điện · <b>уте́чка</b> sự rò rỉ</div>'
)

# --------------------------------------------------------------------- освободиться
S["освободиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">LÀM CHO thành</span></div>'
    '<div class="hd-row"><span class="hd-piece">-свобод-и́ть-</span>'
    '<span class="hd-gloss">TỰ DO — <b>освободи́ть</b> là giải phóng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">chính MÌNH</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mình thành <b>свобо́дный</b> «tự do, rảnh, trống» ⇒ người: thoát ra, xong '
    'việc mà rảnh; chỗ ngồi: trống ra. «Tôi» <i>д → ж</i>: <b>освобожу́сь, освободи́шься</b>. '
    'Cặp CHT: <b>освобожда́ться</b>.</div>'
    '<div class="hd-warn"><b>Когда́ ты освободи́шься?</b> Bao giờ bạn rảnh? · Thoát KHỎI: <b>от</b> + '
    'cách 2 — <b>освободи́ться от долго́в</b> thoát nợ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>освобожда́ться</b> (CHT) · <b>освободи́ть</b> giải phóng · '
    '<b>свобо́да</b> tự do · <b>свобо́дный</b> tự do, rảnh</div>'
)

# --------------------------------------------------------------------- освобождаться
S["освобождаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-свобожд-</span>'
    '<span class="hd-gloss">làm cho TỰ DO — <i>д</i> hoá <i>жд</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́-ть-</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>освобожда́юсь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">chính MÌNH</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>освободи́ться</b> — nghĩa xem ở thẻ đó. Dùng cho việc lặp '
    'lại hay đang diễn ra: <b>Я обы́чно освобожда́юсь в шесть</b> Tôi thường rảnh lúc sáu giờ. '
    'HT ngôi «tôi» đổi <i>ж</i>, CHT đổi <i>жд</i> — đừng lẫn: <b>освобожу́сь</b> ↔ '
    '<b>освобожда́юсь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>освободи́ться</b> (HT) · <b>освобожда́ть</b> giải phóng (CHT) · '
    '<b>освобожде́ние</b> sự giải phóng</div>'
)

# --------------------------------------------------------------------- подчиниться
S["подчиниться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span>'
    '<span class="hd-gloss">DƯỚI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-чин-и́ть-</span>'
    '<span class="hd-gloss">CẤP BẬC, thứ bậc — <b>чин</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">chính MÌNH</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đặt mình DƯỚI một cấp bậc ⇒ tuân theo, khuất phục. Ghép giống tiếng Anh '
    '<i>sub-ordin-ate</i> (<i>sub</i> dưới + <i>order</i> thứ bậc). Trọng âm đứng yên ở đuôi: '
    '<b>подчиню́сь, подчини́шься</b>. Cặp CHT: <b>подчиня́ться</b>.</div>'
    '<div class="hd-warn">Tuân theo ai/cái gì đứng cách 3, không giới từ: <b>подчини́ться '
    'прика́зу</b> chấp hành mệnh lệnh.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>подчиня́ться</b> (CHT) · <b>подчини́ть</b> bắt phải phục tùng · '
    '<b>подчинённый</b> cấp dưới · <b>чино́вник</b> quan chức</div>'
)

# --------------------------------------------------------------------- подчиняться
S["подчиняться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span>'
    '<span class="hd-gloss">DƯỚI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-чин-</span>'
    '<span class="hd-gloss">CẤP BẬC, thứ bậc — <b>чин</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́-ть-ся</span>'
    '<span class="hd-gloss">đuôi CHT + chính MÌNH, chia đều: <b>подчиня́юсь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>подчини́ться</b>, cũng đòi cách 3. HT là một lần chịu nghe '
    'theo, CHT là thường xuyên phục tùng hay ở dưới quyền ai: <b>подчиня́ться зако́ну</b> tuân theo '
    'pháp luật · <b>Он подчиня́ется дире́ктору</b> Anh ấy dưới quyền giám đốc.</div>'
    '<div class="hd-why">Đừng nối với <b>-чин-</b> BẮT ĐẦU của <b>начина́ть</b>: chỉ trùng mặt chữ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>подчини́ться</b> (HT) · <b>подчине́ние</b> sự phục tùng · '
    '<b>чин</b> cấp bậc · <b>чино́вник</b> quan chức</div>'
)

B = {
    "docbangmat": 124,
    "loitubat": 3,
    "nguonsai": 4,
    "baolen": [
        "V cần duyệt (12 thẻ): нарушать/нарушить thống nhất + «làm xáo trộn»; повысить + «cải thiện»; сократить/сокращать thống nhất «rút ngắn, cắt giảm, viết tắt, cho thôi việc» (bỏ «tinh gọn», «giảm»); бродить + «lên men»; тащить «mang nặng» → «khuân», + «kéo lê»; возглавить «nhận lãnh đạo» → «đứng ra lãnh đạo»; возглавлять + «dẫn đầu»; течь + «trôi qua», «rỉ nước» → «rò rỉ»; освободиться/освобождаться thống nhất «được rảnh, thoát khỏi, giải phóng bản thân, trống chỗ» (bỏ «xong việc»). 8 thẻ còn lại giữ đề cũ.",
        "Va chạm: đối chiếu ngoại tuyến (_input + V các lô, KHÔNG gọi Anki nên không phủ hết thẻ): chỉ trùng trong 3 cặp thể của chính lô, badge thể tách được. Nên chạy vacham thật sau khi nạp.",
        "Nguồn sai đã bác (4): CACH DUNG của догонять dẫn «догонит» — đó là dạng của догнать; сократить «tinh gọn» (nới rộng); тащить «mang nặng»; освободиться «xong việc» (gloss không có).",
        "Chỗ không chắc: (1) подчиниться chẻ чин- CẤP BẬC; gốc này cùng чинить/причина (làm, gây ra) theo k184, thẻ chỉ nói nghĩa cấp bậc và chặn nối với начинать. So với subordinate là so cấu tạo, không khẳng định vay. (2) бродить «lên men» ghi là «nghĩa khác», không khẳng định có cùng gốc với «lang thang» hay không.",
        "Cố ý bỏ nghĩa lóng/hiếm khỏi đề: гнать «nói nhảm, chưng cất, bức hại»; догнать/догонять «hiểu ra», «overtake» (vượt là обогнать — thẻ догнать có ô đỏ); cụm гнать порожняк.",
        "loitubat (3): thẻ течь lúc đầu chẻ thêm mảnh «-ь» vô nghĩa; сокращать nói «щ ở HT chỉ có ở ngôi tôi» mà quên сокращённый (đã giới hạn «trong bảng chia»); догнать dẫn автобус sau câu «người bị đuổi kịp» (đổi друга).",
    ],
}
