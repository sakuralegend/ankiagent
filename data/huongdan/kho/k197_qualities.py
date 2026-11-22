# -*- coding: utf-8 -*-
"""k197 — qualities (lô trộn): 15 tính từ/trạng từ chỉ tính chất + 5 danh từ, phần lớn là từ quốc tế.

Chỗ cần nhất quán trong lô:
(1) -лож- dùng ĐÚNG câu khuôn k95/k155/k195: «gốc NẰM — làm cho NẰM ⇒ đặt, họ với лежа́ть, лечь».
(2) без-/бес-: бесконе́чный (бес- trước к vô thanh) ↔ безнадёжный (без- trước н) — dẫn chiếu chéo.
(3) krinein Hy Lạp «phán xét»: кри́тика ↔ крите́рий, hai thẻ trỏ nhau, khớp критикова́ть (k147).
(4) Hậu tố tính từ quốc tế: -ичн- (типи́чный ~ -ic/-ical), -ивн- (объекти́вный ~ -ive).
(5) коне́ц/коне́чно (k19, k85), дробь (k31), дви́гаться (k123), наде́яться (k117), объе́кт (k156):
    giữ đúng cách giải thích của thẻ cũ.
Họ hàng cố ý vắng: không có — kể cả từ mượn (арома́т, фрагме́нт, станда́рт, крите́рий) đều có
phái sinh Nga thật nên vẫn giữ mục này, chỉ ngắn.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "тесный": "chật, chật chội, bó sát, thân thiết, mật thiết",   # gỡ va chạm у́зкий (k61): bỏ «hẹp» (narrow = nghĩa phụ, ý quần áo bó), thêm close/intimate
    "типичный": "điển hình, tiêu biểu, thường gặp",                # gỡ va chạm характе́рный (k189): bỏ «đặc trưng» (characteristic = lõi của характе́рный), thêm typical = hay gặp
    "старинный": "cổ, cổ xưa, lâu đời",                            # «đồ cổ» là danh từ; age-old/time-honoured = lâu đời
}

# --------------------------------------------------------------------- противоположный
S["противоположный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">противо-</span>'
    '<span class="hd-gloss">CHỐNG LẠI, đối diện — như <b>про́тив</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-лож-</span>'
    '<span class="hd-gloss">gốc NẰM — làm cho NẰM ⇒ đặt, họ với <b>лежа́ть</b>, <b>лечь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Được đặt ở phía chống lại» ⇒ đối diện, trái ngược. Khớp từng mảnh với tiếng Anh '
    '<i>op-posite</i> (op- chống + posit- đặt). <b>противополо́жный бе́рег</b> bờ bên kia · '
    '<b>противополо́жное мне́ние</b> ý kiến trái ngược.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>про́тив</b> chống lại · <b>напро́тив</b> đối diện · '
    '<b>противополо́жность</b> sự đối lập · <b>положе́ние</b> vị trí · <b>предложе́ние</b> lời đề nghị</div>'
)

# --------------------------------------------------------------------- разнообразный
S["разнообразный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">разн-</span>'
    '<span class="hd-gloss">KHÁC NHAU — như <b>ра́зный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-о-</span>'
    '<span class="hd-gloss">nguyên âm nối hai gốc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-образ-</span>'
    '<span class="hd-gloss">HÌNH DẠNG, kiểu — như <b>о́браз</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Nhiều kiểu khác nhau» ⇒ đa dạng, phong phú: <b>разнообра́зная еда́</b> đồ ăn '
    'phong phú. Thay <i>разн-</i> bằng <i>одн-</i> (một) là ra từ ngược nghĩa <b>однообра́зный</b> đơn điệu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ра́зный</b> khác nhau · <b>разнообра́зие</b> sự đa dạng · '
    '<b>однообра́зный</b> đơn điệu · <b>о́браз</b> hình ảnh</div>'
)

# --------------------------------------------------------------------- взаимный
S["взаимный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">взаим-</span>'
    '<span class="hd-gloss">gốc cổ «LẤY, vay» — cùng gốc <b>взаймы́</b> vay, cho vay</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Lấy qua lấy lại, có đi có lại ⇒ lẫn nhau, từ hai phía: '
    '<b>взаи́мная по́мощь</b> giúp đỡ lẫn nhau · <b>взаи́мная любо́вь</b> tình yêu được đáp lại.</div>'
    '<div class="hd-warn"><b>Взаи́мно!</b> = «Tôi cũng vậy!» — câu đáp chuẩn khi ai đó nói '
    '<b>Прия́тно познако́миться</b> (rất vui được làm quen).</div>'
    '<div class="hd-warn">⚠️ Mức tin: nối với <b>взаймы́</b> là từ nguyên theo sách, không phải luật suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>взаймы́</b> vay, cho vay · <b>взаи́мность</b> sự đáp lại (tình cảm) · '
    '<b>взаимоде́йствие</b> sự tương tác</div>'
)

# --------------------------------------------------------------------- старинный
S["старинный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">стар-</span>'
    '<span class="hd-gloss">GIÀ, CŨ — như <b>ста́рый</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ин-</span>'
    '<span class="hd-gloss">từ <b>старина́</b> «thời xưa»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thuộc về thời xưa» ⇒ cổ, có từ lâu đời: <b>стари́нный за́мок</b> lâu đài cổ · '
    '<b>стари́нная пе́сня</b> bài hát cổ.</div>'
    '<div class="hd-warn"><b>ста́рый</b> = già, cũ (người, đồ dùng lâu) · <b>стари́нный</b> = cổ, mang giá trị '
    'thời xưa (đồ vật, phong tục). Người già thì KHÔNG nói <b>стари́нный</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ста́рый</b> già, cũ · <b>старина́</b> thời xưa · <b>ста́рость</b> tuổi già · '
    '<b>стари́к</b> ông già</div>'
)

# --------------------------------------------------------------------- тесный
S["тесный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">тесн-</span>'
    '<span class="hd-gloss">ÉP SÁT, chật — gốc trơn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một ý «ép sát nhau»: phòng ép sát ⇒ chật (<b>те́сная ко́мната</b>); giày ép chân ⇒ '
    'chật (<b>те́сные ту́фли</b>); người gắn sát ⇒ thân thiết (<b>те́сная дру́жба</b>). Dạng ngắn giống cái '
    'nhảy trọng âm ra đuôi: <b>те́сен, тесна́, те́сно</b>.</div>'
    '<div class="hd-warn"><b>у́зкий</b> = hẹp BỀ NGANG (<b>у́зкая у́лица</b>) · <b>те́сный</b> = chật vì '
    'THIẾU CHỖ, đông, bó.</div>'
    '<div class="hd-warn"><b>Мир те́сен!</b> = «Trái đất tròn thật!» — khi tình cờ gặp người quen ở chỗ không ngờ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>те́сно</b> chật; khăng khít · <b>теснота́</b> sự chật chội · '
    '<b>тесни́ть</b> chèn ép</div>'
)

# --------------------------------------------------------------------- квадратный
S["квадратный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">квадра́т-</span>'
    '<span class="hd-gloss">HÌNH VUÔNG — Latin <i>quadratus</i>, từ <i>quattuor</i> «bốn»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">danh từ → tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc tiếng Anh <i>quadrant, quadratic</i>. Hai cụm hay gặp nhất: '
    '<b>квадра́тный метр</b> mét vuông (м²) · <b>квадра́тный ко́рень</b> căn bậc hai. '
    'Bình phương là <b>в квадра́те</b>: <i>три в квадра́те</i> = 3².</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>квадра́т</b> hình vuông; bình phương · <b>квадра́тик</b> ô vuông nhỏ</div>'
)

# --------------------------------------------------------------------- прозрачный
S["прозрачный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">XUYÊN QUA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-зрач-</span>'
    '<span class="hd-gloss">NHÌN — gốc <i>зр-</i> như <b>зре́ние</b> thị lực, <b>зрачо́к</b> con ngươi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Nhìn xuyên qua được» ⇒ trong suốt: <b>прозра́чная вода́</b> nước trong veo. '
    'Nghĩa bóng: <b>прозра́чный намёк</b> lời bóng gió lộ liễu, ai nghe cũng hiểu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>зре́ние</b> thị lực · <b>зри́тель</b> khán giả · <b>зрачо́к</b> con ngươi · '
    '<b>прозра́чность</b> độ trong suốt</div>'
)

# --------------------------------------------------------------------- бесконечный
S["бесконечный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бес-</span>'
    '<span class="hd-gloss">KHÔNG CÓ — <i>без-</i> viết thành <i>бес-</i> trước phụ âm vô thanh (к)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-кон-</span>'
    '<span class="hd-gloss">TẬN CÙNG — như <b>коне́ц</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-еч-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ, <i>ц → ч</i> như <b>коне́чный</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Không có điểm cuối» ⇒ vô tận, dài lê thê: <b>бесконе́чный разгово́р</b>. '
    'Trước <i>н</i> thì giữ <i>без-</i>: <b>безнадёжный</b> (cùng lô).</div>'
    '<div class="hd-warn"><b>коне́чно</b> đọc [шн], nhưng <b>бесконе́чный</b> đọc đúng mặt chữ [чн].</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>коне́ц</b> kết thúc · <b>коне́чный</b> cuối cùng · <b>коне́чно</b> tất nhiên · '
    '<b>наконе́ц</b> cuối cùng thì · <b>бесконе́чность</b> vô cực</div>'
)

# --------------------------------------------------------------------- типичный
S["типичный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">тип-</span>'
    '<span class="hd-gloss">KIỂU, LOẠI — <b>тип</b>, tiếng Anh <i>type</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ичн-ый</span>'
    '<span class="hd-gloss">= đuôi <i>-ic/-ical</i> của từ quốc tế</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>typical</i>. Đuôi <i>-ичный</i> mở khoá cả loạt: <b>логи́чный</b> '
    '<i>logical</i>, <b>практи́чный</b> <i>practical</i>. Điển hình CỦA ai: <b>для</b> + cách 2 — '
    '<b>Э́то типи́чно для него́</b> đúng kiểu anh ta.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тип</b> kiểu, loại; gã (khẩu ngữ) · <b>типи́чно</b> điển hình là · '
    '<b>прототи́п</b> nguyên mẫu</div>'
)

# --------------------------------------------------------------------- стабильный
S["стабильный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">стаби́ль-</span>'
    '<span class="hd-gloss">Latin <i>stabilis</i> «đứng vững»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>stable</i>: <b>стаби́льная рабо́та</b> việc làm ổn định. '
    'Dạng ngắn giống đực rụng <i>ь</i>: <b>стаби́лен</b>, nhưng <b>стаби́льна, стаби́льно</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>стаби́льность</b> sự ổn định · <b>стабилиза́ция</b> sự bình ổn · '
    '<b>нестаби́льный</b> bất ổn</div>'
)

# --------------------------------------------------------------------- подробно
S["подробно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дроб-</span>'
    '<span class="hd-gloss">ĐẬP VỤN — như <b>дробь</b>, <b>дроби́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-о</span>'
    '<span class="hd-gloss">đuôi trạng từ (tính từ <b>подро́бный</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chẻ vụn câu chuyện ra từng mảnh nhỏ ⇒ kể tỉ mỉ: <b>Расскажи́ подро́бно!</b> '
    'Kể chi tiết đi!</div>'
    '<div class="hd-warn"><b>Подро́бнее</b> (chi tiết hơn) là chữ trên nút «Xem thêm» ở hầu hết trang web Nga.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>подро́бный</b> chi tiết · <b>подро́бность</b> chi tiết nhỏ · '
    '<b>дробь</b> phân số · <b>дроби́ть</b> nghiền nhỏ</div>'
)

# --------------------------------------------------------------------- аромат
S["аромат"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn gốc Hy Lạp <i>arōma</i>, không chẻ ra mảnh Nga được. Chính là <i>aroma</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>арома́т ко́фе</b> hương cà phê · <b>арома́т цвето́в</b> hương hoa.</div>'
    '<div class="hd-warn"><b>арома́т</b> chỉ mùi DỄ CHỊU · <b>за́пах</b> là mùi nói chung, thơm hay hôi đều được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>аромати́чный</b> thơm phức · <b>ароматерапи́я</b> liệu pháp hương thơm</div>'
)

# --------------------------------------------------------------------- фрагмент
S["фрагмент"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn Latin <i>fragmentum</i> «mảnh vỡ» (<i>frangere</i> «đập vỡ»), không chẻ ra '
    'mảnh Nga được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>fragment</i>. Đoạn CỦA cái gì thì cách 2: <b>фрагме́нт фи́льма</b> '
    'đoạn phim · <b>фрагме́нт пе́сни</b> đoạn bài hát.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>фрагмента́рный</b> rời rạc, từng mảnh</div>'
)

# --------------------------------------------------------------------- стандарт
S["стандарт"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn tiếng Anh <i>standard</i>, không chẻ ra mảnh Nga được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trọng âm KHÁC tiếng Anh — rơi vào âm tiết sau: <b>станда́рт</b>. '
    'Ngoài «tiêu chuẩn» còn nghĩa chê: khuôn sáo, rập khuôn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>станда́ртный</b> tiêu chuẩn; rập khuôn · <b>нестанда́ртный</b> khác thường '
    '(<b>нестанда́ртное реше́ние</b> giải pháp độc đáo)</div>'
)

# --------------------------------------------------------------------- рыжий
S["рыжий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn <i>рыж-</i>, không chẻ được. Đuôi <i>-ий</i> chứ không <i>-ый</i> chỉ vì sau '
    '<i>ж</i> phải viết <i>и</i> (luật ЖИ ШИ); giống cái vẫn là <b>ры́жая</b>, không phải <i>-яя</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Màu cam-đỏ của tóc, lông: <b>ры́жая лиса́</b> cáo lông hung · <b>ры́жий кот</b> mèo vàng cam.</div>'
    '<div class="hd-warn">Tóc đỏ là <b>ры́жие во́лосы</b>, KHÔNG nói <b>кра́сные во́лосы</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рыжева́тый</b> hơi hung · <b>ры́жик</b> một loại nấm màu cam; biệt danh người tóc đỏ</div>'
)

# --------------------------------------------------------------------- критика
S["критика"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">крит-</span>'
    '<span class="hd-gloss">PHÁN XÉT — Hy Lạp <i>krinein</i>, như <i>critic</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ика</span>'
    '<span class="hd-gloss">hoạt động, ngành (khác <i>-ик</i> = người)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>кри́тик</b> nhà phê bình ↔ <b>кри́тика</b> sự phê bình — cùng khuôn '
    '<b>фи́зик ↔ фи́зика</b>. Dùng cho cả chê bai lẫn phê bình văn học.</div>'
    '<div class="hd-warn"><b>Ни́же вся́кой кри́тики</b> = tệ đến mức không còn gì để chê.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>критикова́ть</b> phê bình · <b>кри́тик</b> nhà phê bình · '
    '<b>крити́ческий</b> phê phán; nguy kịch · <b>крите́рий</b> tiêu chí</div>'
)

# --------------------------------------------------------------------- подвиг
S["подвиг"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-двиг-</span>'
    '<span class="hd-gloss">ĐẨY, XÊ DỊCH — như <b>дви́гаться</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một cú dấn lên vượt sức mình ⇒ chiến công, kỳ tích. Trọng âm ở đầu: <b>по́двиг</b>. '
    'Lập chiến công là <b>соверши́ть по́двиг</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: nối với <b>дви́гать</b> là từ nguyên — nghĩa đã trôi xa, không suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дви́гаться</b> di chuyển · <b>движе́ние</b> chuyển động · '
    '<b>подви́жный</b> linh hoạt, hiếu động</div>'
)

# --------------------------------------------------------------------- критерий
S["критерий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn Hy Lạp <i>kritērion</i>, không chẻ ra mảnh Nga được. Cùng gốc <i>krinein</i> '
    '«phán xét» với <b>кри́тика</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>criterion</i> — thước để phán xét. Đuôi <i>-ий</i> nên số nhiều và '
    'cách 6 đều là <i>-ии</i>: <b>крите́рии</b>, <b>в крите́рии</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кри́тика</b> sự phê bình · <b>критикова́ть</b> phê bình · '
    '<b>крити́ческий</b> phê phán</div>'
)

# --------------------------------------------------------------------- объективный
S["объективный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">объе́кт-</span>'
    '<span class="hd-gloss">ĐỐI TƯỢNG — như <b>объе́кт</b>, <i>object</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ивн-ый</span>'
    '<span class="hd-gloss">= đuôi <i>-ive</i> của từ quốc tế</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dựa vào chính sự vật, không vào cảm xúc người nói ⇒ khách quan. Chính là '
    '<i>objective</i>; ngược nghĩa <b>субъекти́вный</b> chủ quan.</div>'
    '<div class="hd-warn"><b>объекти́в</b> (danh từ) = ỐNG KÍNH máy ảnh, không phải «mục tiêu».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>объе́кт</b> đối tượng · <b>объекти́вность</b> tính khách quan · '
    '<b>субъекти́вный</b> chủ quan</div>'
)

# --------------------------------------------------------------------- безнадёжный
S["безнадёжный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">без-</span>'
    '<span class="hd-gloss">KHÔNG CÓ (trước <i>н</i> giữ <i>без-</i>; trước <i>к</i> thành <i>бес-</i>: <b>бесконе́чный</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-надёж-</span>'
    '<span class="hd-gloss">HY VỌNG — như <b>наде́жда</b>, <b>наде́яться</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Không còn hy vọng» ⇒ vô vọng: <b>безнадёжная ситуа́ция</b> tình thế tuyệt vọng.</div>'
    '<div class="hd-warn">Bỏ <i>без-</i> đi thì <b>надёжный</b> = ĐÁNG TIN CẬY, không phải «có hy vọng».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>наде́жда</b> hy vọng · <b>наде́яться</b> hy vọng · <b>надёжный</b> đáng tin cậy · '
    '<b>безнадёжность</b> sự vô vọng</div>'
)

B = {
    "docbangmat": 79,
    "loitubat": 3,
    "nguonsai": 2,
    "baolen": [
        "VA CHẠM тесный ↔ у́зкий[k61 đã nạp] — ĐÃ GỠ từ phía lô này, CẦN DUYỆT: V тесный = «chật, chật chội, bó sát, thân thiết, mật thiết». Bỏ «hẹp» vì narrow chỉ là nghĩa phụ của те́сный (ý quần áo bó; nghĩa gốc là chật vì thiếu chỗ), «hẹp» bề ngang là lõi của у́зкий. Thêm close/intimate (те́сная дру́жба, те́сная связь). Nếu user muốn giữ «hẹp» thì đề «chật, hẹp» của у́зкий lại nằm gọn trong те́сный — khi đó phải sửa у́зкий (mồ côi, tôi không đụng).",
        "VA CHẠM типичный ↔ характе́рный[k189 đã nạp] — ĐÃ GỠ cả hai chiều, CẦN DUYỆT: hai đề cũ trùng HẾT («điển hình, tiêu biểu, đặc trưng»). V типичный = «điển hình, tiêu biểu, thường gặp»: bỏ «đặc trưng» (characteristic = lõi của характе́рный, nghĩa chính của типи́чный là typical), thêm «thường gặp» (typical = hay gặp: типи́чная оши́бка lỗi thường gặp). Không chắc: «thường gặp» có bị coi là nới rộng không — gloss chỉ ghi typical/characteristic/model; «model» tôi không đưa vào vì không thấy nghĩa này dùng thật.",
        "V старинный: «cổ, cổ xưa, đồ cổ» → «cổ, cổ xưa, lâu đời» — «đồ cổ» là danh từ, không phải nghĩa của tính từ; age-old/time-honoured = lâu đời.",
        "Nguồn sai (đã bác, 2): (1) BAT THUONG gắn cho dạng ngắn chèn -ен của 9 tính từ (противополо́жен, разнообра́зен, взаи́мен, стари́нен, прозра́чен, бесконе́чен, типи́чен, объекtíвен→объекти́вен, безнадёжен) — đó là quy tắc chung của đuôi -нный/-ный, KHÔNG bất thường, nên tôi không viết câu chú ý; chỉ viết cho chỗ lệch thật: те́сный (giống cái nhảy trọng âm тесна́), стаби́льный (giống đực rụng ь: стаби́лен). ры́жий có рыжа́ nhưng dạng ngắn của nó hiếm dùng — bỏ. (2) CACH DUNG của прозра́чный chứa chữ Ả Rập «شفاف» — rác, bỏ.",
        "Tự sửa 3 lỗi: (1) подро́бно ban đầu chẻ «под- + (д)роб-, hai д nhập một» kèm ô Mức tin — phân tích đó tôi không chắc; đổi thành по- + -дроб- (дробь hiện rõ mặt chữ, khớp k31), bỏ ô Mức tin; (2) арома́т viết «mượn qua tiếng Pháp» — không chắc đường đi, đổi thành «gốc Hy Lạp arōma»; (3) ры́жий viết «vẫn biến cách cứng: ры́жая, ры́жее» — ры́жее trông như đuôi mềm, dễ gây hiểu sai, chỉ giữ ры́жая.",
        "Không chắc (đã hạ mức tin trên thẻ): взаи́мный ↔ взаймы́ (gốc «lấy, vay» — từ nguyên Vasmer); по́двиг ↔ дви́гать (nghĩa trôi xa). Không đặt Mức tin nhưng là từ nguyên: противополо́жный «khớp từng mảnh» với op-posite — tôi chỉ khẳng định cấu trúc song song, không khẳng định là dịch sao (calque). ры́жик tôi viết «một loại nấm màu cam» thay vì tên nấm tiếng Việt vì không chắc tên.",
        "Họ hàng: KHÔNG thẻ nào vắng — kể cả 4 từ mượn (арома́т, фрагме́нт, станда́рт, крите́рий) vì đều có phái sinh Nga thật (аромати́чный, фрагмента́рный, станда́ртный) hoặc cùng gốc Hy Lạp trong bộ sưu tập (крите́рий ↔ кри́тика). -лож- ở противополо́жный dùng NGUYÊN VĂN câu khuôn k95/k195.",
    ],
}
