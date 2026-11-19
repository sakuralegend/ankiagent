# -*- coding: utf-8 -*-
"""k123 — actions: động từ -ся theo CẶP THỂ + vài tính từ/danh từ trừu tượng; trục là khuôn -ся.

Chỗ cần nhất quán trong lô:
(1) Khuôn -ся «CHÍNH MÌNH»: động từ gốc tác động LÊN cái gì, thêm -ся thì tác động quay về chủ
    ngữ, hết tân ngữ. Trải một lần ở остана́вливаться; двигаться/подниматься/собираться trỏ lại.
    -ся GẮN CHẾT (không tách ra nghĩa «tự mình»): удаваться, пользоваться, бороться — nói thẳng.
(2) Cặp k122 (останови́ть, поднима́ть/подня́ть) là phía «làm CÁI GÌ dừng/lên»; lô này là phía tự.
(3) о- trong остановиться: tiền tố KHÔNG mang nghĩa riêng (như k113, остано́вка k49).
Họ hàng cố ý vắng: không thẻ nào (cả 21 từ đều có họ từ chắc chắn).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa, ngăn bằng dấu phẩy.
V = {
    "остановиться": "dừng lại, nghỉ lại",            # THÊM «nghỉ lại» — gloss stay/put up; khớp cặp IMPF
    "подниматься": "đi lên, leo lên, tăng lên",       # đồng bộ cặp; gloss rise/climb/go up
    "подняться": "đi lên, leo lên, tăng lên",         # THÊM «tăng lên» — gloss increase
    "собираться": "dự định, tụ họp",                  # THÊM «tụ họp» (gloss gather); bỏ «định» thừa, trùng хоте́ть
    "собраться": "tụ họp, dự định",                   # bỏ «lại»; THÊM «dự định» (gloss intend, be about to)
    "пустой": "rỗng, trống rỗng, bỏ trống",           # RÚT «trống» — trùng свобо́дный (cùng adj)
    "сложный": "phức tạp, rắc rối, phức hợp",         # RÚT «khó» — trùng тру́дный, тяжёлый; gloss compound
    "единый": "thống nhất, đồng lòng",                # RÚT «duy nhất» — trùng еди́нственный; gloss of one mind
    "естественный": "tự nhiên, hiển nhiên, đương nhiên",  # KHÔNG rút được «tự nhiên» (nghĩa lõi) — tách натура́льный bằng THÊM (xem báo cáo)
    "состоять": "gồm, nằm ở chỗ",                     # RÚT «bao gồm» — trùng включа́ть; gloss consist in
}

# ---------------------------------------------------------------- удаваться
S["удаваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-да(ва)-</span>'
    '<span class="hd-gloss">CHO — gốc của <b>дать</b> / <b>дава́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">gắn chết, không tách ra nghĩa «tự mình»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Việc «cho ra» kết quả ⇒ thành công. Chủ ngữ là VIỆC, người làm được '
    'đứng cách 3: <b>Мне удаётся</b>. Hiện tại <i>-ва-</i> rơi mất y như <b>дава́ть</b> → '
    '<b>даёт</b>: <b>удаётся</b>.</div>'
    '<div class="hd-warn">«Tôi đã làm được…» = <b>Мне удало́сь</b> + nguyên thể '
    '(<b>Мне удало́сь сдать экза́мен</b>) — đừng đặt <i>я</i> làm chủ ngữ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уда́ча</b> may mắn, thành công · <b>Уда́чи!</b> chúc may mắn · '
    '<b>неуда́ча</b> thất bại · <b>дать</b> cho</div>'
)

# ---------------------------------------------------------------- удаться
S["удаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố, không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-да-</span>'
    '<span class="hd-gloss">CHO — gốc của <b>дать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">gắn chết</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp hoàn thành của <b>удава́ться</b>, cùng khuôn <b>Мне удало́сь…</b> '
    'Chia y hệt <b>дать</b> (bất quy tắc): <b>уда́стся</b>, <b>удаду́тся</b> — thực tế gần như '
    'chỉ gặp ngôi 3. Quá khứ nhấn đuôi: <b>удала́сь</b>, <b>удало́сь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уда́ча</b> may mắn · <b>неуда́ча</b> thất bại</div>'
)

# ---------------------------------------------------------------- останавливаться
S["останавливаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-стан(ов)-</span>'
    '<span class="hd-gloss">ĐỨNG — như <b>стать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-авлива-</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành (о của gốc đổi thành а)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">CHÍNH MÌNH</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Khuôn <i>-ся</i> của cả lô: động từ gốc tác động LÊN cái gì '
    '(<b>останови́ть маши́ну</b> dừng xe), thêm <i>-ся</i> thì tác động quay về chủ ngữ: '
    '<b>Маши́на остана́вливается</b> — xe tự dừng. Dừng lại qua đêm ⇒ nghỉ lại, trọ.</div>'
    '<div class="hd-warn">«Thôi, ngừng LÀM gì» không dùng từ này mà dùng <b>переста́ть</b> + '
    'nguyên thể: <b>Он переста́л кури́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>останови́ть</b> dừng (cái gì) · <b>остано́вка</b> bến xe, sự dừng · '
    '<b>стать</b> trở thành (gốc «đứng»)</div>'
)

# ---------------------------------------------------------------- остановиться
S["остановиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">tiền tố, không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-станов-</span>'
    '<span class="hd-gloss">ĐỨNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">CHÍNH MÌNH — khuôn ở thẻ <b>остана́вливаться</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp hoàn thành của <b>остана́вливаться</b>: tự làm mình đứng lại. '
    'Ngôi «tôi» chen <i>л</i> (в → вл): <b>остановлю́сь</b>; từ ngôi 2 trọng âm lùi: '
    '<b>остано́вишься</b>.</div>'
    '<div class="hd-warn"><b>Где вы останови́лись?</b> = Anh chị đang nghỉ (trọ) ở đâu? — '
    'nghĩa «ở lại khách sạn» gặp liên tục khi đi du lịch.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>останови́ть</b> dừng (cái gì) · <b>остано́вка</b> bến xe</div>'
)

# ---------------------------------------------------------------- пользоваться
S["пользоваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по́льз-</span>'
    '<span class="hd-gloss">LỢI ÍCH — gốc của <b>по́льза</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-</span>'
    '<span class="hd-gloss">đuôi động từ, hiện tại thành <i>-у-</i>: <b>по́льзуюсь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">gắn chết, không tách ra nghĩa «tự mình»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Lấy lợi ích cho mình TỪ cái gì ⇒ dùng; cái được dùng đứng cách 5: '
    '<b>по́льзоваться телефо́ном</b>. Cùng hình ảnh «hưởng»: <b>по́льзоваться успе́хом</b> '
    '= được ưa chuộng.</div>'
    '<div class="hd-warn">Cùng nghĩa «dùng» nhưng khác cách: <b>испо́льзовать</b> + cách 4 '
    '(<b>испо́льзовать телефо́н</b>) · <b>по́льзоваться</b> + cách 5.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>по́льза</b> lợi ích · <b>поле́зный</b> có ích · '
    '<b>бесполе́зный</b> vô ích · <b>испо́льзовать</b> sử dụng</div>'
)

# ---------------------------------------------------------------- двигаться
S["двигаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дви́г-</span>'
    '<span class="hd-gloss">ĐẨY, XÊ DỊCH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">CHÍNH MÌNH — khuôn ở thẻ <b>остана́вливаться</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><i>дви́гать</i> xê dịch CÁI GÌ + <i>-ся</i> = tự di chuyển. Hiện tại '
    'г → ж (biến âm г/к/х → ж/ч/ш): <b>дви́жусь</b>, <b>дви́жется</b>.</div>'
    '<div class="hd-warn">Hiện tại có hai dạng: <b>дви́жется</b> = đang chuyển động '
    '(<b>По́езд дви́жется</b>) · <b>дви́гается</b> = cử động, nhúc nhích (khẩu ngữ). '
    'Không chắc thì dùng <b>дви́жется</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>движе́ние</b> chuyển động, giao thông · <b>дви́гатель</b> động cơ · '
    '<b>дви́нуться</b> bắt đầu chuyển (HT)</div>'
)

# ---------------------------------------------------------------- подниматься
S["подниматься"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span>'
    '<span class="hd-gloss">TỪ DƯỚI LÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ним-</span>'
    '<span class="hd-gloss">LẤY — như <b>понима́ть</b>, <b>принима́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">CHÍNH MÌNH — khuôn ở thẻ <b>остана́вливаться</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Lấy» mình từ dưới lên ⇒ đi lên. <b>поднима́ть</b> nhấc CÁI GÌ + '
    '<i>-ся</i> = tự lên: người leo cầu thang, giá cả tăng — <b>Це́ны поднима́ются</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поднима́ть</b> nhấc, nâng · <b>подъём</b> sự đi lên, dốc · '
    '<b>понима́ть</b> hiểu · <b>принима́ть</b> nhận</div>'
)

# ---------------------------------------------------------------- подняться
S["подняться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span>'
    '<span class="hd-gloss">TỪ DƯỚI LÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ня-</span>'
    '<span class="hd-gloss">LẤY (hiện tại thành <i>-ним-</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">CHÍNH MÌNH</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp hoàn thành của <b>поднима́ться</b>. Gốc <i>-ня-</i> sang hiện tại '
    'thành <i>-ним-</i>: <b>подниму́сь</b>, <b>подни́мешься</b> (trọng âm lùi từ ngôi 2); quá '
    'khứ giống cái nhấn đuôi: <b>подняла́сь</b>.</div>'
    '<div class="hd-warn">Lên ĐẾN đâu: на + cách 4 — <b>подня́ться на пя́тый эта́ж</b>. Nghĩa '
    '«nổi lên»: <b>Подняла́сь бу́ря</b> = bão nổi lên.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>подня́ть</b> nâng lên (HT) · <b>подъём</b> sự đi lên</div>'
)

# ---------------------------------------------------------------- собираться
S["собираться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">CÙNG, gom lại một chỗ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бир-</span>'
    '<span class="hd-gloss">LẤY, NHẶT — gốc бр/бир của <b>брать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">CHÍNH MÌNH — khuôn ở thẻ <b>остана́вливаться</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>собира́ть</b> gom CÁI GÌ + <i>-ся</i> = gom chính mình lại ⇒ '
    '(1) tụ họp: <b>Мы собира́емся в во́семь</b>; (2) «gom mình» sẵn cho một việc ⇒ định làm.</div>'
    '<div class="hd-warn">Nghĩa «định» luôn kèm nguyên thể: <b>Что ты собира́ешься де́лать?</b> '
    '= Bạn định làm gì?</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>собира́ть</b> gom, thu thập · <b>собра́ние</b> cuộc họp · '
    '<b>брать</b> lấy</div>'
)

# ---------------------------------------------------------------- собраться
S["собраться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">CÙNG, gom lại</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бр-</span>'
    '<span class="hd-gloss">LẤY — gốc của <b>брать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">CHÍNH MÌNH</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp hoàn thành của <b>собира́ться</b>, cùng hai nghĩa. Hiện tại gốc '
    '<i>бр</i> chen <i>е</i> y như <b>брать</b> → <b>беру́</b>: <b>соберу́сь</b>, '
    '<b>соберёшься</b>; quá khứ giống cái nhấn đuôi: <b>собрала́сь</b>.</div>'
    '<div class="hd-warn"><b>Собери́сь!</b> = Tập trung vào! — «gom mình lại», nói với người '
    'đang rối.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>собира́ть</b> gom · <b>собра́ние</b> cuộc họp</div>'
)

# ---------------------------------------------------------------- относиться
S["относиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">RỜI ĐI, đưa ra chỗ khác</span></div>'
    '<div class="hd-row"><span class="hd-piece">-нос-</span>'
    '<span class="hd-gloss">MANG — gốc của <b>носи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">CHÍNH MÌNH</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><i>относи́ть</i> = mang cái gì về đúng chỗ, quy về; <i>-ся</i> ⇒ quy '
    'mình về ai/cái gì, luôn với к + cách 3 ⇒ (1) có thái độ với; (2) thuộc về: '
    '<b>Э́то не отно́сится к де́лу</b>. Ngôi «tôi» с → ш: <b>отношу́сь</b>.</div>'
    '<div class="hd-warn"><b>Как вы отно́ситесь к…?</b> = Anh chị nghĩ sao về…? — câu hỏi ý '
    'kiến rất hay gặp.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отноше́ние</b> thái độ, quan hệ · <b>носи́ть</b> mang · '
    '<b>относи́тельно</b> tương đối</div>'
)

# ---------------------------------------------------------------- бороться
S["бороться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бор-</span>'
    '<span class="hd-gloss">ĐẤU, VẬT — gốc của <b>борьба́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">gắn chết — không có dạng thiếu <i>-ся</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hình ảnh gốc là hai người vật nhau ⇒ đấu tranh. Hiện tại rơi <i>о</i> '
    'giữa: <b>борю́сь</b>, <b>бо́решься</b> (trọng âm lùi từ ngôi 2).</div>'
    '<div class="hd-warn">Chống AI/CÁI GÌ: с + cách 5 (<b>боро́ться с корру́пцией</b>) · VÌ cái '
    'gì: за + cách 4 (<b>боро́ться за свобо́ду</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>борьба́</b> cuộc đấu tranh, môn vật</div>'
)

# ---------------------------------------------------------------- разница
S["разница"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ра́зн-</span>'
    '<span class="hd-gloss">KHÁC NHAU — gốc của <b>ра́зный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ица</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái làm hai thứ <b>ра́зный</b> ⇒ sự khác biệt. Giữa hai thứ: '
    'ме́жду + cách 5 — <b>ра́зница ме́жду ни́ми</b>.</div>'
    '<div class="hd-warn"><b>Кака́я ра́зница?</b> = Có khác gì đâu? / Sao cũng được — câu đáp '
    'gặp hằng ngày.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ра́зный</b> khác nhau · <b>по-ра́зному</b> theo cách khác nhau · '
    '<b>разнообра́зный</b> đa dạng</div>'
)

# ---------------------------------------------------------------- высший
S["высший"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы́с-</span>'
    '<span class="hd-gloss">CAO — gốc của <b>высо́кий</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ш-</span>'
    '<span class="hd-gloss">dấu so sánh cổ, như <b>лу́чший</b>, <b>ху́дший</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dạng so sánh «đông cứng» của <b>высо́кий</b> ⇒ cao nhất về THỨ BẬC, '
    'chất lượng. Không có dạng ngắn.</div>'
    '<div class="hd-warn">Chỉ dùng cho bậc, hạng: <b>вы́сшее образова́ние</b> = học vấn đại '
    'học. Toà nhà cao nhất là <b>са́мое высо́кое зда́ние</b>, không dùng <b>вы́сший</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>высо́кий</b> cao · <b>вы́ше</b> cao hơn · <b>высота́</b> độ cao</div>'
)

# ---------------------------------------------------------------- чужой
S["чужой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn <i>чуж-</i>, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhớ theo cặp đối: <b>свой</b> của mình ↔ <b>чужо́й</b> của người khác. '
    'Áp vào người ⇒ xa lạ: <b>чужо́й челове́к</b> người lạ. Dùng như danh từ thì là «người '
    'ngoài».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>чужби́на</b> đất khách · <b>чу́ждый</b> xa lạ, không hợp (sách vở)</div>'
)

# ---------------------------------------------------------------- пустой
S["пустой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn <i>пуст-</i>, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không có gì bên trong: <b>пуста́я буты́лка</b>. Dạng ngắn trọng âm '
    'nhảy: <b>пуст</b>, <b>пуста́</b>, <b>пу́сто</b>, <b>пусты́</b>; <b>пу́сто</b> còn là trạng '
    'từ: <b>В ко́мнате пу́сто</b> = phòng trống trơn.</div>'
    '<div class="hd-warn">Chỗ ngồi «còn trống» (chưa ai lấy) là <b>свобо́дный</b>: '
    '<b>Здесь свобо́дно?</b> — không dùng <b>пусто́й</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пусты́ня</b> sa mạc · <b>пустя́к</b> chuyện vặt</div>'
)

# ---------------------------------------------------------------- сложный
S["сложный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">LẠI VỚI NHAU</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лож-</span>'
    '<span class="hd-gloss">ĐẶT — gốc của <b>положи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ный</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đặt nhiều phần chồng lại với nhau ⇒ phức tạp, ghép — đúng hình ảnh '
    '<i>complex</i> «đan vào nhau»: <b>сло́жное сло́во</b> = từ ghép. Dạng ngắn giống cái nhấn '
    'đuôi: <b>сложна́</b>; trạng từ <b>сло́жно</b>.</div>'
    '<div class="hd-warn">Nghiêng khác <b>тру́дный</b>: <b>сло́жный</b> rối vì NHIỀU PHẦN · '
    '<b>тру́дный</b> nặng vì tốn SỨC (<b>тру́дная рабо́та</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сложи́ть</b> gộp, cộng · <b>сложе́ние</b> phép cộng · '
    '<b>сло́жность</b> độ phức tạp · <b>положи́ть</b> đặt</div>'
)

# ---------------------------------------------------------------- единый
S["единый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">еди́н-</span>'
    '<span class="hd-gloss">MỘT — dạng cổ của <b>оди́н</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhiều cái gộp lại thành MỘT ⇒ thống nhất: <b>еди́ное це́лое</b> một '
    'khối liền.</div>'
    '<div class="hd-warn">Đừng lẫn <b>еди́нственный</b> = CHỈ CÓ MỘT (cơ hội duy nhất). '
    '<b>еди́ный</b> = NHIỀU cái hợp thành một.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>еди́нство</b> sự thống nhất · <b>едини́ца</b> đơn vị, số một · '
    '<b>объедини́ть</b> hợp nhất · <b>еди́нственный</b> duy nhất</div>'
)

# ---------------------------------------------------------------- естественный
S["естественный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">есте́ств-</span>'
    '<span class="hd-gloss">BẢN CHẤT, cái vốn có — từ <b>есть</b> «là, có»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-енн-</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thuộc về cái VỐN CÓ, không do người làm ra ⇒ tự nhiên, hiển nhiên. '
    'Dạng ngắn giống đực chen <i>е</i>: <b>есте́ственен</b>. Trạng từ <b>есте́ственно</b> = '
    'tất nhiên! — dùng như <b>коне́чно</b>.</div>'
    '<div class="hd-warn">Khác <b>натура́льный</b> = thật, không nhân tạo (<b>натура́льный '
    'сок</b>). <b>есте́ственный</b> = theo lẽ tự nhiên: <b>есте́ственный отбо́р</b> chọn lọc tự '
    'nhiên.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>естество́</b> bản chất (sách vở) · <b>есть</b> là, có</div>'
)

# ---------------------------------------------------------------- скорость
S["скорость"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">скор-</span>'
    '<span class="hd-gloss">NHANH — gốc của <b>ско́рый</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ость</span>'
    '<span class="hd-gloss">đuôi danh từ trừu tượng, giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Sự nhanh ⇒ tốc độ. Trên xe còn là «số»: <b>переключи́ть ско́рость</b> '
    '= sang số.</div>'
    '<div class="hd-warn"><b>ско́ро</b> thường là SẮP, chẳng bao lâu (<b>Ско́ро ле́то</b>) — '
    '«nhanh» là <b>бы́стро</b>. <b>ско́рая</b> = xe cấp cứu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ско́рый</b> nhanh · <b>ско́ро</b> sắp · <b>скоре́е</b> mau lên</div>'
)

# ---------------------------------------------------------------- состоять
S["состоять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">CÙNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-стоя-</span>'
    '<span class="hd-gloss">ĐỨNG — gốc của <b>стоя́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Các phần ĐỨNG CÙNG nhau ⇒ hợp thành, gồm: из + cách 2 — '
    '<b>Кварти́ра состои́т из трёх ко́мнат</b>. в + cách 6 = nằm ở chỗ: '
    '<b>Пробле́ма состои́т в том, что…</b> Chia như <b>стоя́ть</b>: <b>состою́</b>.</div>'
    '<div class="hd-warn">Thêm <i>-ся</i> là ra từ KHÁC: <b>состоя́ться</b> (HT) = diễn ra — '
    '<b>Конце́рт состои́тся за́втра</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>состоя́ние</b> trạng thái · <b>соста́в</b> thành phần · '
    '<b>стоя́ть</b> đứng</div>'
)
