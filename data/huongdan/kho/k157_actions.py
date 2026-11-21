# -*- coding: utf-8 -*-
"""k157 — actions (lô trộn): nhìn/thấy, rơi/trúng, cho phép, cú đánh, nhổ.

Chỗ cần nhất quán trong lô:
(1) gốc вид- THẤY (ви́деть): вид · ви́дный — khớp khuôn thẻ cũ ви́деть.
(2) gốc гляд- NHÌN (взгляд): гляде́ть · погляде́ть — д→ж chỉ ở ngôi «tôi», đúng khuôn ви́деть → ви́жу.
(3) gốc пад- RƠI (па́дать): попада́ть / попа́сть — nguyên thể -сть che mất д (д+т→ст).
(4) cặp thể позво́лить / позволя́ть: gốc вол- (во́ля), KHÔNG phải зва- (позва́ть) — báo oan của máy.
(5) cặp thể плева́ть / плю́нуть: thân hiện tại плю-, -ну- = một cái.
Họ hàng cố ý vắng: до́ллар (mượn, đứng một mình).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "шаг": "bước, bước chân, nhịp bước",                     # bỏ «(chân)», «(giai đoạn)»
    "плевать": "nhổ, khạc nhổ, mặc kệ",                       # «;» -> «,»
    "плюнуть": "nhổ, khạc nhổ, mặc kệ, buông bỏ",             # bỏ «một cái» (nhãn thể trá hình); give up on
    "попадать": "đến được, vào được, rơi vào, trúng",         # bỏ «(đích)», «;»; khớp cặp попасть, badge thể tách
    "попасть": "đến được, vào được, rơi vào, trúng",          # bỏ «(nơi nào)»; bỏ «tới được» — trùng достигнуть
    "глядеть": "nhìn, nhìn chăm chú, trông chừng, hướng ra",  # bỏ «ngắm» — trùng смотреть; gaze/look after/face
    "деятельность": "hoạt động, sự vận hành",                 # bỏ «công việc» — trùng работа; functioning
    "позволить": "cho phép, để cho, tạo điều kiện, có khả năng chi trả",   # bỏ «(hoàn thành)»; let/enable/afford
    "позволять": "cho phép, để cho, tạo điều kiện, có khả năng chi trả",   # bỏ «(chưa hoàn thành)»
    "структура": "cấu trúc, cơ cấu",                          # bỏ «kết cấu» — trùng конструкция; «cấu trúc» là lõi, giữ
    "черта": "đường vạch, nét, đặc điểm, ranh giới",                     # thiếu trait/feature; «ranh giới», «đặc điểm» trùng граница/особенность nên dùng «nét»
    "вид": "vẻ ngoài, quang cảnh, tầm nhìn, loại, loài, thể",       # «;» -> «,»; thiếu species/aspect; «loại», «dạng» trùng тип nên bỏ
    "похожий": "giống, tương tự",                                       # bỏ «tương tự» — trùng аналогичный; «giống nhau» trùng одинаковый
    "прямой": "thẳng, thẳng đứng, trực tiếp, thẳng thắn",     # «;» -> «,»; thiếu upright/frank
    "видный": "dễ thấy, có tiếng, lỗi lạc, đường bệ",         # bỏ «nổi bật» — trùng яркий; eminent/stately
}

# --------------------------------------------------------------------- доллар
S["доллар"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga — mượn tiếng Anh <i>dollar</i>, gốc là tên '
    'đồng <i>Thaler</i> của Đức.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đọc gần như tiếng Anh, nhấn âm đầu. Giá tiền luôn đi với số nên thuộc '
    'ba dạng: <b>оди́н до́ллар</b> · <b>два до́ллара</b> · <b>пять до́лларов</b>.</div>'
)

# --------------------------------------------------------------------- попытка
S["попытка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố, không mang nghĩa riêng (lấy theo <b>попыта́ться</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пыт-</span>'
    '<span class="hd-gloss">THỬ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">→ danh từ: MỘT lần làm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>попыта́ться</b> «cố thử» = một lần thử. Số nhiều cách 2 '
    'chêm <b>о</b>: <b>попы́ток</b> (như <b>оши́бка</b> → <b>оши́бок</b>).</div>'
    '<div class="hd-warn"><b>с пе́рвой попы́тки</b> — ngay lần thử đầu tiên.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>попыта́ться</b> cố thử · <b>пыта́ться</b> cố gắng · <b>о́пыт</b> kinh '
    'nghiệm, thí nghiệm · <b>испыта́ние</b> sự thử thách · <b>пы́тка</b> tra tấn</div>'
)

# --------------------------------------------------------------------- шаг
S["шаг"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Số nhiều nhấn đuôi: <b>шаги́</b>, <b>шаго́в</b>. Động từ cùng gốc '
    '<b>шага́ть</b> «bước đi».</div>'
    '<div class="hd-warn">Cách 2 có hai dạng: <b>шага́</b> nhấn đuôi chỉ dùng sau 2, 3, 4 — '
    '<b>два шага́</b> (như <b>два часа́</b>); chỗ khác là <b>ша́га</b>.</div>'
    '<div class="hd-warn"><b>шаг за ша́гом</b> — từng bước một.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>шага́ть</b> bước đi · <b>шажо́к</b> bước nhỏ (г→ж)</div>'
)

# --------------------------------------------------------------------- участие
S["участие"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-част-</span>'
    '<span class="hd-gloss">PHẦN — <b>часть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ие</span>'
    '<span class="hd-gloss">→ danh từ trừu tượng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Có PHẦN của mình trong việc gì = tham gia — y như tiếng Anh '
    '<i>take <b>part</b></i>.</div>'
    '<div class="hd-warn"><b>приня́ть</b> (<b>принима́ть</b>) <b>уча́стие в</b> + cách 6 — tham '
    'gia vào: <b>приня́ть уча́стие в рабо́те</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уча́ствовать</b> tham gia · <b>уча́стник</b> người tham gia · '
    '<b>часть</b> phần · <b>уча́сток</b> mảnh đất, khu vực</div>'
)

# --------------------------------------------------------------------- удар
S["удар"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">удар-</span>'
    '<span class="hd-gloss">CÚ ĐÁNH</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>уда́рить</b> «đánh». Cũng họ này ra <b>ударе́ние</b> = '
    'trọng âm, nghĩa đen «cú đánh» vào một âm tiết — dấu nhấn trên mọi thẻ chính là nó.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уда́рить</b> · <b>ударя́ть</b> đánh · <b>ударе́ние</b> trọng âm · '
    '<b>уда́рник</b> tay trống</div>'
)

# --------------------------------------------------------------------- плевать
S["плевать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">плев- / плю-</span>'
    '<span class="hd-gloss">NHỔ — nguyên thể <b>плев-</b>, hiện tại <b>плю-</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thân hiện tại đổi <b>-ева- → -ю-</b>: <b>плюю́, плюёшь</b>, cùng khuôn '
    '<b>танцева́ть → танцу́ю</b>. Cặp thể: <b>плю́нуть</b> — nhổ MỘT cái.</div>'
    '<div class="hd-warn"><b>Мне плева́ть</b> (<b>на</b> + cách 4) — tôi cóc cần, mặc kệ. '
    'Khẩu ngữ, khá thô.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>плю́нуть</b> nhổ một cái · <b>плево́к</b> bãi nước bọt · '
    '<b>плёвый</b> dễ ợt (khẩu ngữ)</div>'
)

# --------------------------------------------------------------------- плюнуть
S["плюнуть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">плю-</span>'
    '<span class="hd-gloss">NHỔ — thân hiện tại của <b>плева́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ну-ть</span>'
    '<span class="hd-gloss">làm MỘT cái, hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>-ну-</b> = hành động chớp nhoáng một lần, như <b>гля́нуть</b> liếc '
    'một cái. Chia đều: <b>плю́ну, плю́нешь</b>.</div>'
    '<div class="hd-warn"><b>плю́нуть на</b> + cách 4 — bỏ mặc, buông hẳn: '
    '<b>Плюнь на него́!</b> Kệ nó đi!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>плева́ть</b> nhổ · <b>плево́к</b> bãi nước bọt</div>'
)

# --------------------------------------------------------------------- попадать
S["попадать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố, không mang nghĩa riêng rõ ràng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пад-</span>'
    '<span class="hd-gloss">RƠI — gốc của <b>па́дать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen «rơi trúng vào» → trúng đích, lọt vào, tới được. Đòi '
    '<b>в/на</b> + cách 4 (hướng tới): <b>попада́ть в цель</b> trúng đích.</div>'
    '<div class="hd-warn">Chỉ khác trọng âm: <b>попа́дать</b> (hoàn thành) = lần lượt đổ rạp, '
    'rơi hết. Thẻ này là <b>попада́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>попа́сть</b> cặp hoàn thành · <b>па́дать</b> rơi · <b>упа́сть</b> ngã</div>'
)

# --------------------------------------------------------------------- попасть
S["попасть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố, như ở <b>попада́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-пас-ть</span>'
    '<span class="hd-gloss">RƠI — thật ra là <b>пад-</b> + <b>-ть</b>: д + т thành ст</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nguyên thể che mất <b>д</b>; nó lộ lại ở thân tương lai <b>попаду́, '
    'попадёшь</b>, còn quá khứ rụng <b>д</b> trước <b>л</b>: <b>попа́л</b> — y như '
    '<b>упа́сть → упаду́, упа́л</b>.</div>'
    '<div class="hd-warn"><b>Как попа́сть в/на</b> …? — Làm sao tới được …? · '
    '<b>попа́сть под дождь</b> — bị mắc mưa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>попада́ть</b> cặp chưa hoàn thành · <b>па́дать</b> rơi · '
    '<b>упа́сть</b> ngã</div>'
)

# --------------------------------------------------------------------- глядеть
S["глядеть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">гляд-</span>'
    '<span class="hd-gloss">NHÌN — gốc của <b>взгляд</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ть</span>'
    '<span class="hd-gloss">đuôi động từ, chia đuôi <b>-и-</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng khuôn <b>ви́деть → ви́жу</b>: <b>д→ж</b> chỉ ở ngôi «tôi» — '
    '<b>гляжу́</b>, còn lại <b>гляди́шь, гляди́т</b>. Nghĩa gần <b>смотре́ть</b> nhưng khẩu ngữ, '
    'nhiều cảm xúc hơn: <b>Гляди́!</b> Nhìn kìa!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>взгляд</b> cái nhìn · <b>вы́глядеть</b> trông có vẻ · '
    '<b>погляде́ть</b> nhìn một chút · <b>гля́нуть</b> liếc một cái</div>'
)

# --------------------------------------------------------------------- поглядеть
S["поглядеть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">làm MỘT LÚC, một chút</span></div>'
    '<div class="hd-row"><span class="hd-piece">-гляд-е́ть</span>'
    '<span class="hd-gloss">NHÌN — <b>гляде́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>по-</b> thêm sắc «một chốc», như <b>погуля́ть</b> dạo một lát. Chia '
    'y hệt <b>гляде́ть</b>: <b>погляжу́, погляди́шь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гляде́ть</b> nhìn · <b>взгляд</b> cái nhìn · <b>вы́глядеть</b> '
    'trông có vẻ</div>'
)

# --------------------------------------------------------------------- деятельность
S["деятельность"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">де́я-</span>'
    '<span class="hd-gloss">LÀM — động từ cổ <b>де́ять</b>, cùng gốc <b>де́ло</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-тель-</span>'
    '<span class="hd-gloss">NGƯỜI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-</span>'
    '<span class="hd-gloss">→ tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ость</span>'
    '<span class="hd-gloss">→ danh từ trừu tượng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Xây từng tầng: <b>де́ятель</b> người hoạt động → <b>де́ятельный</b> năng '
    'nổ → <b>де́ятельность</b> hoạt động. Trọng âm đứng yên ở <b>де́-</b> suốt cả chuỗi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>де́ятель</b> nhân vật hoạt động · <b>де́ятельный</b> năng nổ · '
    '<b>де́ло</b> việc · <b>де́йствие</b> hành động</div>'
)

# --------------------------------------------------------------------- позволить
S["позволить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-з-</span>'
    '<span class="hd-gloss"><b>по-</b> + <b>из-</b> dính liền</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вол-</span>'
    '<span class="hd-gloss">Ý MUỐN — <b>во́ля</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thuận theo ý muốn» → cho phép. Cặp thể: <b>позво́лить</b> (chia '
    '<b>позво́лю, позво́лишь</b>) / <b>позволя́ть</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: phần chẻ <b>по-</b> + <b>из-</b> + <b>вол-</b> là từ nguyên, '
    'không nhìn mặt chữ ra được. <b>позва́ть</b> «gọi» trông giống nhưng KHÁC gốc.</div>'
    '<div class="hd-warn"><b>Позво́льте</b> …! — Cho phép tôi …: <b>Позво́льте предста́виться</b> '
    '— xin tự giới thiệu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>позволя́ть</b> · <b>позволе́ние</b> sự cho phép · <b>во́ля</b> ý chí, '
    'tự do · <b>дово́льный</b> hài lòng</div>'
)

# --------------------------------------------------------------------- позволять
S["позволять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">позвол-</span>'
    '<span class="hd-gloss">CHO PHÉP — gốc <b>вол-</b> ý muốn, xem thẻ <b>позво́лить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp của <b>позво́лить</b>: đổi <b>-ить → -я́ть</b>, trọng âm nhảy ra '
    'đuôi; chia đều: <b>позволя́ю, позволя́ешь</b>.</div>'
    '<div class="hd-warn">Người được phép ở cách 3 + nguyên thể: <b>Ма́ма не позволя́ет мне '
    'гуля́ть</b>. Thêm <b>себе́</b> = dám, có điều kiện: <b>Я не могу́ себе́ э́то позво́лить</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>позво́лить</b> · <b>позволе́ние</b> sự cho phép · <b>во́ля</b> ý chí</div>'
)

# --------------------------------------------------------------------- структура
S["структура"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga — mượn Latin <i>structura</i>, chính là tiếng '
    'Anh <i>structure</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi <b>-у́ра</b> ứng với <i>-ure</i>, thường mang trọng âm: '
    '<b>культу́ра</b> <i>culture</i>, <b>температу́ра</b> <i>temperature</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">Cùng gốc Latin <i>struct-</i>: <b>структу́рный</b> thuộc cấu trúc · '
    '<b>констру́кция</b> kết cấu · <b>инстру́кция</b> bản hướng dẫn</div>'
)

# --------------------------------------------------------------------- черта
S["черта"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">черт-</span>'
    '<span class="hd-gloss">NÉT KẺ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́</span>'
    '<span class="hd-gloss">đuôi danh từ, nhấn đuôi</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ «nét kẻ» mở ra «ranh giới» (<b>в черте́ го́рода</b> trong địa giới '
    'thành phố) và «nét» của người: <b>черты́ лица́</b> đường nét khuôn mặt, <b>черта́ '
    'хара́ктера</b> nét tính cách. Trọng âm bám đuôi cả bảng: <b>черты́</b>, <b>черта́м</b>.</div>'
    '<div class="hd-warn">Đừng lẫn với <b>чёрт</b> «con quỷ». Cụm hay gặp: <b>в о́бщих '
    'черта́х</b> — nói đại thể.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>черти́ть</b> kẻ, vẽ kỹ thuật · <b>чертёж</b> bản vẽ</div>'
)

# --------------------------------------------------------------------- вид
S["вид"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вид-</span>'
    '<span class="hd-gloss">THẤY — gốc của <b>ви́деть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cái được thấy»: vẻ ngoài, cảnh trước mắt; rồi «dạng, loại». Chữ «thể» '
    'trên badge cũng là nó: <b>соверше́нный вид</b> thể hoàn thành.</div>'
    '<div class="hd-warn">Cách 6 có hai dạng: <b>в ви́де</b> + cách 2 = dưới dạng · nhưng '
    '<b>име́ть в виду́</b> = ý muốn nói: <b>Что ты име́ешь в виду́?</b> Ý bạn là gì?</div>'
    '<div class="hd-warn"><b>де́лать вид, что</b> … — giả vờ, làm ra vẻ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ви́деть</b> thấy · <b>ви́дный</b> dễ thấy · <b>свида́ние</b> cuộc hẹn · '
    '<b>до свида́ния</b> tạm biệt («tới lần gặp»)</div>'
)

# --------------------------------------------------------------------- похожий
S["похожий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố</span></div>'
    '<div class="hd-row"><span class="hd-piece">-хож-</span>'
    '<span class="hd-gloss">= <b>ход-</b> (д→ж), gốc của <b>ходи́ть</b> — nghĩa không suy thẳng '
    'ra được</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhớ qua động từ đi cặp: <b>походи́ть на</b> = giống ai. Dạng ngắn '
    '<b>похо́ж, похо́жа, похо́жи</b>; <b>похо́же, что</b> … = có vẻ như …</div>'
    '<div class="hd-warn">Giống AI: <b>на</b> + cách 4 — <b>Он похо́ж на отца́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>походи́ть</b> giống · <b>схо́дство</b> sự giống nhau · '
    '<b>схо́дный</b> tương tự</div>'
)

# --------------------------------------------------------------------- прямой
S["прямой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">прям-</span>'
    '<span class="hd-gloss">THẲNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́й</span>'
    '<span class="hd-gloss">đuôi tính từ, nhấn đuôi</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thẳng» → «trực tiếp» → «thẳng thắn». Trọng âm rời đuôi ở dạng ngắn và '
    'trạng từ: <b>прям, пряма́, пря́мо, пря́мы</b> — chỉ giống cái nhấn đuôi. Trạng từ '
    '<b>пря́мо</b>: thẳng, ngay — <b>пря́мо сейча́с</b> ngay bây giờ.</div>'
    '<div class="hd-warn"><b>прямо́й эфи́р</b> — truyền hình trực tiếp · <b>прямо́й у́гол</b> — '
    'góc vuông.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пря́мо</b> thẳng, ngay · <b>прямоуго́льник</b> hình chữ nhật · '
    '<b>напряму́ю</b> trực tiếp</div>'
)

# --------------------------------------------------------------------- видный
S["видный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вид-</span>'
    '<span class="hd-gloss">THẤY — gốc của <b>ви́деть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thấy được» → «dễ thấy» → người ai cũng để ý: <b>ви́дный учёный</b> nhà '
    'khoa học lỗi lạc. Dạng ngắn nhấn được cả hai chỗ: <b>ви́дна / видна́</b>, '
    '<b>ви́дны / видны́</b>.</div>'
    '<div class="hd-warn"><b>ви́дно</b> dùng một mình rất nhiều: <b>Отсю́да ви́дно мо́ре</b> — từ '
    'đây thấy được biển · <b>Ви́дно, он уста́л</b> — xem ra anh ấy mệt.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вид</b> vẻ ngoài · <b>ви́деть</b> thấy · <b>очеви́дный</b> hiển nhiên '
    '(<b>о́чи</b> mắt + <b>вид-</b>)</div>'
)

B = {
    "docbangmat": 111,
    "loitubat": 1,
    "nguonsai": 1,
    "baolen": [
        "Va chạm còn lại KHÔNG gỡ được bằng rút gọn vì là nghĩa lõi: «cho phép» позволять/позволить ↔ разрешать/разрешить/дать · «nhìn» глядеть ↔ смотреть · «cấu trúc» структура ↔ конструкция. Danh sách đầy đủ hai bên đã khác nhau (vd позволять có «để cho, tạo điều kiện, có khả năng chi trả»; разрешать chỉ «cho phép, cấp phép»), nên theo §2c là phân biệt được — cần luồng chính xác nhận.",
        "V đã rút gọn để né va chạm mới chính mình tạo ra khi bổ sung nghĩa: вид bỏ «loại, dạng» (trùng тип) · черта dùng «nét» thay «ranh giới, đặc điểm» (trùng граница, особенность) · похожий chỉ còn «giống» (bỏ «giống nhau» trùng одинаковый) · структура bỏ «tổ chức» (trùng организация). Đổi lại вид mất nghĩa «loại» (вид спорта) trên đề bài — cần duyệt.",
        "V cặp thể trùng nguyên văn, chỉ badge thể tách: позволить = позволять; попадать = попасть («đến được, vào được, rơi vào, trúng»; попасть bỏ «tới được» vì trùng достигнуть).",
        "Nguồn sai bác: BAT THUONG của черта ghi «trọng âm dịch trong số nhiều» — bảng thật nhấn đuôi suốt (черты́, черта́м), chỉ cách 2 số nhiều черт không có đuôi; không viết câu chú ý theo nó.",
        "Không chắc (đã hạ mức tin hoặc tránh khẳng định): позволить = по- + из- + вол- (từ nguyên, có ô ⚠️ Mức tin); похожий ← ход- qua походить на (ghi rõ nghĩa không suy thẳng); дово́льный, схо́дство, де́йствие xếp vào họ theo từ nguyên — nếu luồng chính muốn chặt hơn thì bỏ ba từ đó khỏi Họ hàng.",
        "Thẻ cũ không thấy khai sai; удар giữ chẻ một khối «удар- CÚ ĐÁNH» như уда́рить/ударе́ние, không tách у-/дар- vì không chắc từ nguyên.",
    ],
}
