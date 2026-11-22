# -*- coding: utf-8 -*-
"""k161 — qualities::eval: danh từ trừu tượng + tính từ đánh giá, phần lớn chẻ được ra gốc đã học.

Chỗ cần nhất quán trong lô:
(1) Đuôi danh từ: -ение/-ие (исключе́ние, разреше́ние, сомне́ние, созна́ние, наси́лие) ·
    -ость (необходи́мость, глу́пость) · -от-а (красота́, như доброта́).
(2) Gốc khớp thẻ cũ: -ход- (необходи́мо, приходи́ть) · -реш- (реше́ние, разреши́ть) ·
    -зна- (знать, зна́ние) · -мн- (мне́ние) · -сил- (си́ла) · -ключ- (включи́ть, ключ) ·
    -рыв-/-рв- (переры́в).
(3) Từ mượn đứng gần như một mình: риск, бюдже́т, аре́ст — không chẻ, chỉ bắc sang tiếng Anh.
Dạng ngắn: чуде́сный, сро́чный, идеа́льный đều chèn -е- đúng quy tắc ⇒ bỏ, chỉ nêu trạng từ -о.
Họ hàng cố ý vắng: зря (trạng từ đứng một mình; gốc cổ зр- chỉ nêu trong ô Mức tin).
кро́ме KHÔNG cùng gốc исключе́ние — chỉ là đồng nghĩa của за исключе́нием, không đưa vào Họ hàng.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "красота": "vẻ đẹp, cái đẹp, cảnh đẹp",
    "исключение": "ngoại lệ, sự loại trừ, sự khai trừ",
    "потрясающий": "tuyệt vời, đáng kinh ngạc, gây choáng ngợp, gây sửng sốt",
    "чудесный": "tuyệt vời, tuyệt diệu, kỳ diệu",
    "срочный": "gấp, khẩn cấp, có kỳ hạn",
    "необходимость": "sự cần thiết, nhu cầu",
    "приходиться": "phải, buộc phải, đành phải, rơi vào, trùng vào",
    "взрыв": "vụ nổ, sự bùng nổ, cơn bộc phát",
    "насилие": "bạo lực, sự cưỡng bức, sự ép buộc",
    "разрешение": "sự cho phép, giấy phép, sự giải quyết, độ phân giải",
    "арест": "sự bắt giữ, sự giam giữ",
    "сознание": "ý thức, nhận thức, sự tỉnh táo",
    "глупость": "sự ngốc nghếch, sự ngu ngốc, điều ngớ ngẩn",
}

# ----------------------------------------------------------------- польза
S["польза"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không dịch riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-льз-</span>'
    '<span class="hd-gloss">gốc cổ DỄ, ĐƯỢC PHÉP</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái làm việc dễ đi ⇒ ích lợi. Tính từ: <b>поле́зный</b> có ích '
    '(<b>льз</b> → <b>лез</b>, chèn nguyên âm).</div>'
    '<div class="hd-warn">⚠️ Mức tin: từ nguyên — <b>нельзя́</b> cũng từ gốc này '
    '(«không dễ, không được phép»).</div>'
    '<div class="hd-warn"><b>в по́льзу</b> + cách 2 = có lợi cho, nghiêng về phía: '
    '<b>Э́то в на́шу по́льзу.</b> Điều đó có lợi cho ta.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поле́зный</b> có ích · <b>бесполе́зный</b> vô ích · '
    '<b>по́льзоваться</b> sử dụng · <b>испо́льзовать</b> sử dụng</div>'
)

# ----------------------------------------------------------------- красота
S["красота"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">крас-</span>'
    '<span class="hd-gloss">ĐẸP</span></div>'
    '<div class="hd-row"><span class="hd-piece">-от-а</span>'
    '<span class="hd-gloss">tính từ → danh từ «tính chất», như <b>доброта́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc <b>краси́вый</b>, <b>прекра́сный</b>. <b>кра́сный</b> thời xưa '
    'nghĩa là «đẹp», về sau mới thành «đỏ». Số nhiều trọng âm lùi: <b>красо́ты</b> = những cảnh '
    'đẹp.</div>'
    '<div class="hd-warn">Câu cảm thán hay dùng: <b>Кака́я красота́!</b> Đẹp quá!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>краси́вый</b> đẹp · <b>прекра́сный</b> tuyệt đẹp · '
    '<b>кра́сный</b> đỏ</div>'
)

# ----------------------------------------------------------------- исключение
S["исключение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ис-</span>'
    '<span class="hd-gloss">= из- RA KHỎI (з → с trước к)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ключ-</span>'
    '<span class="hd-gloss">MÓC, KHOÁ — như trong <b>включи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>включи́ть</b> móc vào (bật) ↔ <b>исключи́ть</b> móc ra khỏi '
    '(loại ra) ⇒ cái bị loại ra khỏi luật = ngoại lệ.</div>'
    '<div class="hd-warn"><b>за исключе́нием</b> + cách 2 = ngoại trừ, giống <b>кро́ме</b>: '
    '<b>все, за исключе́нием Ива́на</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>исключи́ть</b> loại trừ · <b>включи́ть</b> bật, gộp vào · '
    '<b>вы́ключить</b> tắt · <b>ключ</b> chìa khoá</div>'
)

# ----------------------------------------------------------------- потрясающий
S["потрясающий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố thể, không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тряс-</span>'
    '<span class="hd-gloss">RUNG, LẮC — gốc của <b>трясти́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ющ-ий</span>'
    '<span class="hd-gloss">«đang làm» — đuôi phân từ hiện tại</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đang làm rung chuyển» ⇒ làm choáng váng — y như tiếng Anh '
    '<i>stunning</i>, <i>shocking</i>. Đuôi <b>-ющий/-ащий</b> = «đang …», dấu hiệu phân từ hiện tại. '
    'Trạng từ: <b>потряса́юще</b> tuyệt quá.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>трясти́</b> rung, lắc · <b>потрясти́</b> làm chấn động · '
    '<b>потрясе́ние</b> cú sốc</div>'
)

# ----------------------------------------------------------------- чудесный
S["чудесный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">чуд-ес-</span>'
    '<span class="hd-gloss">PHÉP MÀU — thân số nhiều của <b>чу́до</b>: <b>чудеса́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Như phép màu» ⇒ tuyệt diệu. Phần <b>-ес-</b> chính là đoạn chèn vào ở số '
    'nhiều <b>чу́до → чудеса́</b>. Trạng từ: <b>чуде́сно</b> tuyệt quá.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>чу́до</b> phép màu · <b>чудо́вище</b> quái vật · '
    '<b>чуда́к</b> người kỳ quặc</div>'
)

# ----------------------------------------------------------------- срочный
S["срочный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сроч-</span>'
    '<span class="hd-gloss">THỜI HẠN — <b>срок</b> (к → ч)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Dính hạn chót» ⇒ gấp: <b>сро́чное де́ло</b> việc gấp. Nghĩa thứ hai: có '
    'kỳ hạn — <b>сро́чный вклад</b> tiền gửi có kỳ hạn.</div>'
    '<div class="hd-warn">Trạng từ <b>сро́чно</b> = gấp! — dùng rất nhiều: '
    '<b>Мне сро́чно ну́жно…</b> Tôi cần gấp…</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>срок</b> thời hạn · <b>сро́чно</b> gấp · '
    '<b>просро́чить</b> để quá hạn</div>'
)

# ----------------------------------------------------------------- идеальный
S["идеальный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">идеа́л-</span>'
    '<span class="hd-gloss">LÝ TƯỞNG — từ mượn, = <i>ideal</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ьн-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiếng Anh <i>ideal</i> + đuôi tính từ. Thường dịch là «hoàn hảo»: '
    '<b>идеа́льный вариа́нт</b> phương án hoàn hảo. Trạng từ: <b>идеа́льно</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>идеа́л</b> lý tưởng · <b>иде́я</b> ý tưởng</div>'
)

# ----------------------------------------------------------------- риск
S["риск"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ mượn, không chẻ được — y như tiếng Anh <i>risk</i>. Giống đực, '
    'biến cách đều.</div>'
    '<div class="hd-warn"><b>на свой страх и риск</b> = tự chịu rủi ro (nghĩa đen «trên nỗi sợ '
    'và rủi ro của mình»).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рискова́ть</b> liều, mạo hiểm · <b>риско́ванный</b> liều lĩnh</div>'
)

# ----------------------------------------------------------------- необходимость
S["необходимость"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не-об-</span>'
    '<span class="hd-gloss">KHÔNG + VÒNG QUANH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ход-им-</span>'
    '<span class="hd-gloss">ĐI → «có thể đi được»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ость</span>'
    '<span class="hd-gloss">tính từ → danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>необходи́мый</b>: «không đi vòng qua được» ⇒ sự cần '
    'thiết, điều tất yếu.</div>'
    '<div class="hd-warn"><b>в слу́чае необходи́мости</b> = khi cần thiết.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>необходи́мо</b> cần thiết · <b>необходи́мый</b> cần thiết · '
    '<b>обходи́ть</b> đi vòng · <b>ходи́ть</b> đi</div>'
)

# ----------------------------------------------------------------- зря
S["зря"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trạng từ đứng một mình, không chẻ được trong tiếng Nga ngày nay. Hai '
    'nghĩa: «uổng công» — <b>Я зря пришёл.</b> Tôi đến uổng công; và «lẽ ra đừng» — '
    '<b>Зря ты э́то сказа́л.</b> Cậu không nên nói thế.</div>'
    '<div class="hd-warn"><b>не зря</b> = không phải vô cớ, đáng công: '
    '<b>Я не зря учи́л.</b> Tôi học không uổng.</div>'
    '<div class="hd-warn">⚠️ Mức tin: từ nguyên — gốc cổ <b>зр-</b> «nhìn» (như '
    '<b>зре́ние</b> thị lực): «chỉ đứng nhìn» ⇒ không được gì.</div>'
)

# ----------------------------------------------------------------- приходиться
S["приходиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">TỚI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ход-и-ть-ся</span>'
    '<span class="hd-gloss">ĐI + đuôi phản thân</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Hoàn cảnh tự tìm tới» ⇒ đành phải. Dùng vô nhân xưng: người ở '
    'cách 3 + nguyên mẫu — <b>Мне прихо́дится рабо́тать.</b> Tôi đành phải làm. '
    'Cặp thể: <b>прийти́сь</b>.</div>'
    '<div class="hd-warn">Quá khứ hay gặp nhất: <b>Мне пришло́сь</b> + nguyên mẫu = '
    'tôi đã buộc phải.</div>'
    '<div class="hd-warn"><b>на</b> + cách 4 = rơi vào (ngày): '
    '<b>Пра́здник прихо́дится на суббо́ту.</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>приходи́ть</b> đến · <b>ходи́ть</b> đi</div>'
)

# ----------------------------------------------------------------- реформа
S["реформа"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ре-</span>'
    '<span class="hd-gloss">LẠI — tiền tố Latin, như <i>re-</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-фо́рм-а</span>'
    '<span class="hd-gloss">HÌNH DẠNG — <b>фо́рма</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ mượn, nhưng hai mảnh nhìn thấy được: «nặn lại hình dạng» ⇒ cải cách, '
    'y như tiếng Anh <i>reform</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>фо́рма</b> hình dạng · <b>реформи́ровать</b> cải cách</div>'
)

# ----------------------------------------------------------------- взрыв
S["взрыв"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вз-</span>'
    '<span class="hd-gloss">BẬT LÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-рыв</span>'
    '<span class="hd-gloss">XÉ, GIẬT — cùng gốc <b>рвать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Xé tung lên» ⇒ vụ nổ. Gốc chạy <b>рыв/рв</b>: động từ là '
    '<b>взорва́ть</b> cho nổ. Nghĩa bóng: <b>взрыв сме́ха</b> tràng cười bùng lên.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>взорва́ть</b> cho nổ · <b>взрыва́ть</b> cho nổ · '
    '<b>переры́в</b> giờ nghỉ · <b>рвать</b> xé</div>'
)

# ----------------------------------------------------------------- насилие
S["насилие"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">ĐÈ LÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сил-</span>'
    '<span class="hd-gloss">SỨC MẠNH — <b>си́ла</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ие</span>'
    '<span class="hd-gloss">danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đè sức lên người khác» ⇒ bạo lực, cưỡng bức.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>си́ла</b> sức mạnh · <b>си́льный</b> mạnh · '
    '<b>наси́льно</b> bằng vũ lực, cưỡng ép</div>'
)

# ----------------------------------------------------------------- разрешение
S["разрешение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раз-</span>'
    '<span class="hd-gloss">TÁCH RA, GỠ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-реш-</span>'
    '<span class="hd-gloss">gốc của <b>реши́ть</b> quyết, giải</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>разреши́ть</b>: «gỡ nút» ⇒ cho phép, hoặc giải quyết. '
    '<b>С ва́шего разреше́ния</b> = nếu anh cho phép.</div>'
    '<div class="hd-warn"><b>разреше́ние экра́на</b> = độ phân giải màn hình — y như tiếng Anh '
    '<i>resolution</i>, cũng vừa «giải quyết» vừa «độ phân giải».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>разреши́ть</b> cho phép · <b>разреша́ть</b> cho phép · '
    '<b>реше́ние</b> quyết định, lời giải · <b>реши́ть</b> quyết định</div>'
)

# ----------------------------------------------------------------- бюджет
S["бюджет"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ mượn, không chẻ được — chính là tiếng Anh <i>budget</i>. Giống đực, '
    'biến cách đều: <b>в бюдже́те</b> trong ngân sách.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бюдже́тный</b> thuộc ngân sách; giá rẻ</div>'
)

# ----------------------------------------------------------------- арест
S["арест"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ mượn, không chẻ được — y như tiếng Anh <i>arrest</i>. Giống đực, '
    'biến cách đều.</div>'
    '<div class="hd-warn"><b>под аре́стом</b> = đang bị giam giữ · <b>дома́шний аре́ст</b> = '
    'quản thúc tại gia.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>арестова́ть</b> bắt giữ</div>'
)

# ----------------------------------------------------------------- сознание
S["сознание"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">CÙNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-зна-</span>'
    '<span class="hd-gloss">BIẾT — <b>знать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ние</span>'
    '<span class="hd-gloss">danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ráp từng mảnh y như tiếng Anh <i>con-sci-ousness</i> (<i>con-</i> cùng + '
    '<i>sci-</i> biết) ⇒ ý thức. Bỏ <b>со-</b> là ra <b>зна́ние</b> kiến thức.</div>'
    '<div class="hd-warn"><b>потеря́ть созна́ние</b> = ngất, bất tỉnh · '
    '<b>прийти́ в созна́ние</b> = tỉnh lại.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>знать</b> biết · <b>зна́ние</b> kiến thức · '
    '<b>созна́тельный</b> có ý thức, tự giác</div>'
)

# ----------------------------------------------------------------- сомнение
S["сомнение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không dịch riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мн-</span>'
    '<span class="hd-gloss">NGHĨ — gốc của <b>мне́ние</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc <b>мне́ние</b> ý kiến: nghĩ mà chưa ngả hẳn ⇒ nghi ngờ. '
    'Động từ: <b>сомнева́ться в</b> + cách 6 nghi ngờ điều gì.</div>'
    '<div class="hd-warn"><b>без сомне́ния</b> = chắc chắn, không nghi ngờ gì.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сомнева́ться</b> nghi ngờ · <b>мне́ние</b> ý kiến · '
    '<b>несомне́нно</b> chắc chắn · <b>сомни́тельный</b> đáng ngờ</div>'
)

# ----------------------------------------------------------------- глупость
S["глупость"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">глуп-</span>'
    '<span class="hd-gloss">NGỐC — <b>глу́пый</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ость</span>'
    '<span class="hd-gloss">tính từ → danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Sự ngốc, và một việc ngốc cụ thể: <b>Э́то глу́пость.</b> '
    'Thế là ngớ ngẩn.</div>'
    '<div class="hd-warn">Số nhiều <b>глу́пости!</b> = vớ vẩn! · '
    '<b>Не говори́ глу́постей!</b> Đừng nói nhảm!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>глу́пый</b> ngốc · <b>глу́по</b> ngốc nghếch · '
    '<b>глупе́ц</b> kẻ ngốc</div>'
)

B = {
    "docbangmat": 76,
    "loitubat": 3,   # польза: viết «з → з» cho поле́зный — sai, thật là льз → лез · ví dụ «Спартака́» sai trọng âm (Спарта́ка) — thay câu khác · потрясающий: «-ющий gặp ở MỌI phân từ hiện tại» — nói quá (còn -ущ/-ящ), đã viết lại
    "nguonsai": 3,   # cờ BAT THUONG dạng ngắn của чудесный, идеальный (chèn -е-, trọng âm đứng yên = đúng quy tắc) và срочный (chỉ thêm biến thể срочна́) — không chép
    "baolen": [
        "Không chắc vừa: исключе́ние chẻ -ключ- «móc, khoá» cùng gốc включи́ть/ключ (Vasmer nối ключить ← ключ «móc») — viết thẳng, không gắn Mức tin; luồng chính muốn chặt thì hạ.",
        "Đã gắn Mức tin (từ nguyên, không suy ra được): по́льза ↔ нельзя́ (gốc льз-) · зря ← gốc cổ зр- «nhìn» (зре́ние).",
        "Gợi ý của luồng chính «исключе́ние ← кро́ме» KHÔNG cùng gốc — кро́ме chỉ được nhắc làm đồng nghĩa của за исключе́нием, không vào Họ hàng.",
        "зря cố ý không có mục Họ hàng (trạng từ đứng một mình). риск/бюдже́т/аре́ст: từ mượn, không chẻ, Họ hàng chỉ là phái sinh Nga trực tiếp.",
        "V cần duyệt: 13 dòng, chủ yếu đổi «;» thành «,» và thêm nghĩa gloss xác nhận (разрешение + «sự giải quyết, độ phân giải»; срочный + «có kỳ hạn»; приходиться + «đành phải»; потрясающий + «đáng kinh ngạc, gây sửng sốt»). Không cắt nghĩa nào. Không gặp trùng nghĩa không gỡ được.",
    ],
}
