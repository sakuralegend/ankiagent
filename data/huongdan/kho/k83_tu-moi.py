# -*- coding: utf-8 -*-
"""k83 — tu-moi: 7 từ user vừa thêm, KHÔNG cùng họ nhau.

Mỗi thẻ soạn độc lập, không trục chung, không khối hệ thống. Hai chỗ cần
nhất quán trong lô: (1) cặp thể мять ↔ помять — cùng cách chẻ gốc мя-/мн-;
(2) bẫy mặt chữ мн- của мну (мять) ≠ мн- của по́мню (память): hai gốc khác
nhau, nói ở мять và помять, память chỉ nhắc một vế. Họ đã có trong kho
(по́мнить, вспо́мнить, смотре́ть, посмотре́ть, кольцо́) chỉ trỏ về.
"""

S = {}

# ----------------------------------------------------------------- мять
S["мять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мя-</span>'
    '<span class="hd-gloss">gốc ÉP, BÓP, GIẪM — cả nghĩa nằm ở đây; thân hiện '
    'tại rút thành <b>мн-</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ép một thứ mềm bằng tay hay chân: nhào bột '
    '(<b>мять те́сто</b>), vò nhàu áo (<b>мять руба́шку</b>), giẫm nát cỏ. '
    'Thể chưa hoàn thành; cặp hoàn thành là <b>помя́ть</b> (thẻ riêng, cùng '
    'lô) hoặc <b>смять</b> khi vò nát hẳn thành cục.</div>'
    '<div class="hd-warn">Thân hiện tại KHÔNG suy được từ nguyên thể: '
    '<b>мну, мнёшь, мнёт… мнут</b>, quá khứ lại về <b>мял</b>. Cùng kiểu với '
    '<b>жать → жму</b> (ép).</div>'
    '<div class="hd-warn">Chữ <b>мн-</b> của <b>мну</b> không họ hàng gì với '
    '<b>мн-</b> của <b>по́мню</b> / <b>па́мять</b> (cùng lô): hai gốc khác nhau '
    'trùng mặt chữ. <b>мя́та</b> (bạc hà) cũng không cùng gốc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>помя́ть</b> làm nhàu (HT) · <b>смять</b> vò nát · '
    '<b>размя́ть</b> nhào kỹ, khởi động cơ · <b>разми́нка</b> bài khởi động · '
    '<b>мя́тый</b> bị nhàu</div>'
)

# --------------------------------------------------------------- помять
S["помять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố tạo thể hoàn thành — ở đây không mang nghĩa '
    'riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мя-</span>'
    '<span class="hd-gloss">gốc ÉP, BÓP (thẻ <b>мять</b>); thân hiện tại '
    '<b>-мн-</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thể hoàn thành của <b>мять</b>: nhìn vào KẾT QUẢ — áo '
    'đã nhàu (<b>помя́ть руба́шку</b>), xe đã móp (<b>помя́ть маши́ну</b>, nghĩa '
    '«làm bẹp»). Thân tương lai cũng bất thường y như gốc: <b>помну́, '
    'помнёшь… помну́т</b>, trọng âm rơi trên đuôi; quá khứ <b>помя́л</b>.</div>'
    '<div class="hd-warn">Cặp chỉ khác trọng âm: <b>помну́</b> = tôi sẽ vò '
    'nhàu (từ <b>помя́ть</b>) ≠ <b>по́мню</b> = tôi nhớ (từ <b>по́мнить</b>). '
    'Khác gốc, chỉ trùng mặt chữ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мять</b> vò, nhào (CHT) · <b>смять</b> vò nát · '
    '<b>разми́нка</b> bài khởi động</div>'
)

# ---------------------------------------------------------------- около
S["около"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">quanh, vòng quanh</span></div>'
    '<div class="hd-row"><span class="hd-piece">-коло</span>'
    '<span class="hd-gloss">gốc cổ VÒNG, BÁNH XE — còn thấy ở <b>кольцо́</b>, '
    '<b>колесо́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Ở vòng quanh» ⇒ gần (<b>о́коло до́ма</b>) và ⇒ khoảng '
    'chừng (<b>о́коло пяти́ часо́в</b>) — đúng hai nghĩa của <i>around</i> '
    'tiếng Anh: <i>around the house</i> / <i>around five</i>. Là giới từ, luôn '
    'kéo cách 2 theo sau.</div>'
    '<div class="hd-warn">Ba từ «gần» trong kho khác vai: <b>о́коло</b> + cách 2 '
    'là giới từ; <b>ря́дом</b> và <b>бли́зко</b> là trạng từ, muốn thêm danh từ '
    'phải nói <b>ря́дом с</b> + cách 5.</div>'
    '<div class="hd-warn">⚠️ Mức tin: từ nguyên, không phải luật. '
    '<i>коло</i> «vòng» là từ Nga cổ, nay chỉ còn sống trong các từ phái sinh.'
    '</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кольцо́</b> nhẫn, vòng · <b>колесо́</b> bánh xe · '
    '<b>око́льный</b> (đường) vòng, quanh co</div>'
)

# ---------------------------------------------------------------- орден
# Từ mượn đứng một mình (Đức Orden ← Latin ordo); từ phái sinh Nga hiếm ⇒ BỎ
# mục Họ hàng, cầu sang tiếng Anh order thay thế.
S["орден"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn từ Đức <i>Orden</i> ← Latin '
    '<i>ordo</i> «hàng ngũ, trật tự» — chính là <i>order</i> tiếng Anh. Đường '
    'nghĩa: hội hiệp sĩ / dòng tu (<i>order</i>) → huy hiệu của hội → huân '
    'chương nhà nước.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa «hội, dòng» vẫn còn (<b>о́рден иезуи́тов</b>) '
    'và hai nghĩa chia hai số nhiều: huân chương → <b>ордена́</b>, hội → '
    '<b>о́рдены</b>. Khác <b>меда́ль</b>: <b>о́рден</b> bậc cao hơn, có hạng '
    '(1-й, 2-й сте́пени).</div>'
    '<div class="hd-warn">Số nhiều nghĩa «huân chương» ném trọng âm ra đuôi: '
    '<b>о́рден → ордена́, ордено́в</b> — như <b>дом → дома́</b>.</div>'
    '<div class="hd-warn">Trao thì dùng cách 5: <b>награди́ть о́рденом</b>; '
    'nhận thì cách 4: <b>получи́ть о́рден</b>.</div>'
)

# ---------------------------------------------------------- осматривать
S["осматривать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">khắp, vòng quanh (cùng <b>о-</b> của <b>о́коло</b>)'
    '</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сматр-</span>'
    '<span class="hd-gloss">gốc NHÌN của <b>смотре́ть</b>, <b>о</b> đổi thành '
    '<b>а</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-</span>'
    '<span class="hd-gloss">hậu tố tạo thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Nhìn khắp một lượt» để đánh giá: bác sĩ khám '
    '(<b>осма́тривать больно́го</b>), khách tham quan (<b>осма́тривать '
    'го́род</b>), thanh tra rà một chỗ. Cặp hoàn thành: <b>осмотре́ть</b>.</div>'
    '<div class="hd-warn">Luật lặp khắp nơi: <b>-ива-</b> kéo <b>о</b> của gốc '
    'thành <b>а</b> và hút trọng âm về đó — <b>осмотре́ть → осма́тривать</b>, '
    'y như <b>спроси́ть → спра́шивать</b>.</div>'
    '<div class="hd-warn">Khác <b>смотре́ть на</b> + cách 4: '
    '<b>осма́тривать</b> đi thẳng với cách 4, không giới từ — '
    '<b>осма́тривать музе́й</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>смотре́ть</b> nhìn, xem · <b>посмотре́ть</b> xem '
    'thử · <b>осмотре́ть</b> khám, xem kỹ (HT) · <b>осмо́тр</b> cuộc khám, đợt '
    'kiểm tra · <b>осмотре́ться</b> ngó quanh · <b>рассма́тривать</b> xem xét, '
    'cân nhắc</div>'
)

# --------------------------------------------------------------- память
S["память"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">па-</span>'
    '<span class="hd-gloss">tiền tố danh từ cổ, ít gặp — không cần nhớ nghĩa '
    'riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мять</span>'
    '<span class="hd-gloss">gốc NGHĨ, NHỚ <b>мн-</b> của <b>по́мню</b>, '
    '<b>мне́ние</b> — KHÔNG phải <b>мять</b> «vò nhàu» cùng lô</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái «giữ trong đầu» của <b>по́мнить</b>: trí nhớ, kỷ '
    'vật để nhớ, và bộ nhớ máy tính. Đuôi <b>-ь</b> giống cái, biến cách 3: '
    '<b>в па́мяти</b>, <b>па́мятью</b>; trọng âm đứng yên.</div>'
    '<div class="hd-warn">Hai cụm hay gặp: <b>на па́мять</b> = để làm kỷ niệm '
    '(<b>подари́ть на па́мять</b>) · <b>по па́мяти</b> = theo trí nhớ, không '
    'nhìn giấy.</div>'
    '<div class="hd-warn">⚠️ Mức tin: từ nguyên. Gốc <b>мн-</b> «nghĩ» được '
    'cho là cùng gốc Ấn-Âu với <i>mind</i>, <i>mental</i> tiếng Anh.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>по́мнить</b> nhớ · <b>вспо́мнить</b> nhớ lại · '
    '<b>запо́мнить</b> ghi nhớ · <b>напо́мнить</b> nhắc · <b>па́мятник</b> '
    'tượng đài · <b>мне́ние</b> ý kiến</div>'
)

# --------------------------------------------------------------- сердце
S["сердце"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">серд-</span>'
    '<span class="hd-gloss">gốc TIM — chữ <b>д</b> không đọc nhưng phải viết, '
    'vì nó vang lên ở <b>серде́чный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-це</span>'
    '<span class="hd-gloss">đuôi danh từ giống trung, như <b>со́лнце</b>'
    '</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giống trung dù kết bằng <b>-е</b>. Nghĩa mở rộng '
    '«nóng giận» (<i>temper</i>) chính là thứ đẻ ra <b>серди́ться</b> «giận»: '
    'tim nổi lên. Cùng gốc Ấn-Âu với <i>heart</i>, <i>cordial</i>.</div>'
    '<div class="hd-warn">Số nhiều lệch hai chỗ: trọng âm nhảy ra đuôi '
    '<b>сердца́</b>, và cách 2 số nhiều chèn <b>е</b>: <b>серде́ц</b>.</div>'
    '<div class="hd-warn"><b>принима́ть бли́зко к се́рдцу</b> = để tâm quá, '
    'lấy làm buồn · <b>от всего́ се́рдца</b> = từ tận đáy lòng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>серде́чный</b> thuộc tim; chân thành · '
    '<b>серди́ться</b> giận · <b>серди́тый</b> cáu, giận · '
    '<b>рассерди́ться</b> nổi giận · <b>сердцебие́ние</b> nhịp tim</div>'
)

# ------------------------------------------------ VIỆC THỨ HAI: field V
# осматривать: gỡ va chạm với проверять ở nghĩa "kiểm tra" (cùng v/IMPF) —
# rút gọn, giữ nghĩa lõi "nhìn kỹ".
# память: thêm "bộ nhớ" — gloss Anh có "memory / storage", nghĩa máy tính thông dụng.
V = {
    "осматривать": "khám, tham quan, ngắm nghía",
    "память": "trí nhớ, kỷ niệm, bộ nhớ",
}
