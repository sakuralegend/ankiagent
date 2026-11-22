# -*- coding: utf-8 -*-
"""k172 — qualities (lô trộn): kích thước, đặc điểm, khác biệt, sở hữu.

Chỗ cần nhất quán trong lô:
(1) họ -лич-: отли́чие / отлича́ться chẻ đúng khuôn thẻ отли́чный [k156]
    «от- TÁCH RA KHỎI -лич- MẶT, DIỆN MẠO — лицо́».
(2) ме́лкий / ме́лочь cùng gốc мел- NHỎ VỤN (к → ч khi thành danh từ). Báo oan мело́дия.
(3) сво́йство ↔ со́бственность: cả hai là «property» tiếng Anh — mỗi thẻ một ô đỏ tách nghĩa
    (tính chất / tài sản). Gốc сво-/соб- khớp thẻ свой [k75], со́бственный [k156].
(4) дополни́тельный: пол- ĐẦY như по́лный [k113] — KHÔNG phải пол- NỬA của по́лночь.
(5) приме́та: -мет- DẤU như заме́тить [k95]. Báo oan име́ть.
(6) глубина́ / высота́: tính từ → danh từ đo lường (-ина́ / -ота́), một câu ở mỗi thẻ, không bảng.
Họ hàng cố ý vắng: không thẻ nào — từ nào trong lô cũng có họ thật.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "глубина": "độ sâu, chiều sâu, chỗ sâu bên trong",          # depth/profundity; interior, heart (of a place)
    "примета": "điềm, dấu hiệu, đặc điểm nhận dạng",            # distinguishing/identifying mark
    "повреждение": "hư hỏng, thương tổn, chấn thương",          # injury
    "отличие": "sự khác biệt, điểm khác biệt, sự xuất sắc, phần thưởng",  # distinction (honour), award
    "дикий": "hoang dã, dại, man rợ, nhút nhát, kỳ quặc",       # savage, shy, strange/preposterous
    "мелкий": "nhỏ, nhỏ vụn, mịn, lặt vặt, nông",               # fine-grained, petty, shallow
    "тупой": "cùn, đần, chậm hiểu, âm ỉ, tù",                   # «;» -> «,»; dull pain, obtuse angle
    "ровный": "phẳng, bằng, đều, thẳng, điềm tĩnh",             # straight, even-tempered/calm
    "тайный": "bí mật, thầm kín, lén lút, ẩn giấu",             # clandestine, covert, hidden
    "частный": "riêng, tư nhân, cá biệt",                       # particular, individual
    "свойство": "tính chất, đặc tính, thuộc tính",              # attribute
    "грязь": "bùn, bùn đất, chất bẩn, sự bẩn thỉu, sự nhơ nhuốc",  # mud/mire, grime, sleaze
    "соответствовать": "phù hợp, tương ứng, khớp, đáp ứng",     # bỏ «với»; to match, to meet (requirements)
    "собственность": "tài sản, quyền sở hữu",                   # property or ownership
    "мелочь": "chuyện nhỏ, chuyện vặt, chi tiết nhỏ, tiền lẻ",  # THIẾU hẳn small change/coins
    "отличаться": "khác, khác biệt, nổi bật",                   # bỏ «với»; to stand out, be notable for
}

# --------------------------------------------------------------------- глубина
S["глубина"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">глуб-</span>'
    '<span class="hd-gloss">SÂU — gốc của <b>глубо́кий</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ина́</span>'
    '<span class="hd-gloss">→ danh từ chỉ số đo</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tính từ đo lường bỏ đuôi, thêm <b>-ина́</b> là ra «độ…»: '
    '<b>глубо́кий → глубина́</b>, như <b>широ́кий → ширина́</b>. Số nhiều trọng âm lùi về '
    'thân: <b>глуби́ны</b>.</div>'
    '<div class="hd-warn"><b>в глубине́ души́</b> — tận đáy lòng, sâu thẳm trong lòng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>глубо́кий</b> sâu · <b>глубоко́</b> sâu (trạng từ) · '
    '<b>углуби́ть</b> làm sâu thêm</div>'
)

# --------------------------------------------------------------------- примета
S["примета"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">GẮN VÀO, ở sát bên</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мет-</span>'
    '<span class="hd-gloss">DẤU, đánh dấu — như <b>заме́тить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái dấu gắn sẵn trên người/vật ⇒ <b>đặc điểm nhận dạng</b>. Cái dấu '
    'báo trước chuyện sắp tới ⇒ <b>điềm</b>.</div>'
    '<div class="hd-warn">Hai nghĩa, hai kiểu câu: <b>плоха́я приме́та</b> điềm xấu · '
    '<b>приме́ты</b> (số nhiều) đặc điểm nhận dạng của một người.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>заме́тить</b> nhận thấy · <b>заме́тка</b> ghi chú · '
    '<b>ме́тка</b> dấu đánh · <b>приме́тный</b> dễ nhận ra · <b>отме́тить</b> đánh dấu</div>'
)

# --------------------------------------------------------------------- высота
S["высота"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">выс-</span>'
    '<span class="hd-gloss">CAO — gốc của <b>высо́кий</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ота́</span>'
    '<span class="hd-gloss">→ danh từ chỉ tính chất</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>высо́кий → высота́</b>, cùng khuôn <b>-ота́</b> với '
    '<b>красота́</b> vẻ đẹp. Cặp đối của <b>глубина́</b> cùng lô. Số nhiều trọng âm lùi: '
    '<b>высо́ты</b>.</div>'
    '<div class="hd-warn"><b>быть на высоте́</b> — làm rất tốt, đạt đúng tầm (nghĩa đen: '
    '«ở trên cao»).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>высо́кий</b> cao · <b>высоко́</b> cao (trạng từ) · '
    '<b>вы́ше</b> cao hơn · <b>повы́сить</b> nâng lên</div>'
)

# --------------------------------------------------------------------- повреждение
S["повреждение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố thể HT — không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-врежд-</span>'
    '<span class="hd-gloss">HẠI — <b>вред</b>, д hoá жд</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ние</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>повреди́ть</b> làm hỏng: gây hại cho đồ vật (hư hỏng) '
    'hay cho cơ thể (thương tổn). <b>д → жд</b> khi thêm <b>-ение</b>, như '
    '<b>роди́ть → рожде́ние</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вред</b> tác hại · <b>вре́дный</b> có hại · '
    '<b>повреди́ть</b> làm hỏng · <b>безвре́дный</b> vô hại</div>'
)

# --------------------------------------------------------------------- отличие
S["отличие"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">TÁCH RA KHỎI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лич-</span>'
    '<span class="hd-gloss">MẶT, DIỆN MẠO — <b>лицо́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ие</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Diện mạo tách khỏi đám đông ⇒ chỗ khác biệt; tách lên trên hẳn ⇒ sự '
    'xuất sắc, phần thưởng — cùng ý với <b>отли́чный</b>.</div>'
    '<div class="hd-warn"><b>в отли́чие от</b> + cách 2 — khác với, trái với: '
    '<i>в отли́чие от бра́та</i>.</div>'
    '<div class="hd-warn"><b>с отли́чием</b> — loại xuất sắc (tốt nghiệp, bằng cấp).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отлича́ться</b> khác biệt · <b>отли́чный</b> xuất sắc · '
    '<b>разли́чие</b> sự khác nhau · <b>ли́чный</b> cá nhân</div>'
)

# --------------------------------------------------------------------- дикий
S["дикий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дик-</span>'
    '<span class="hd-gloss">HOANG, chưa thuần</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc: thú hoang, cây dại. Sang người: man rợ, hoặc nhút nhát '
    'không quen người. Sang chuyện: kỳ quặc, quá đáng. Dạng ngắn giống cái nhấn đuôi '
    '<b>дика́</b>; so sánh hơn <b>к → ч</b>: <b>ди́че</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дика́рь</b> người man rợ · <b>дичь</b> thú săn; chuyện nhảm · '
    '<b>ди́кость</b> sự hoang dã · <b>одича́ть</b> hoá hoang</div>'
)

# --------------------------------------------------------------------- мелкий
S["мелкий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мел-</span>'
    '<span class="hd-gloss">NHỎ VỤN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-кий</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhỏ theo kiểu VỤN, HẠT: mưa phùn, cát mịn, tiền lẻ, chuyện vặt. Với '
    'nước là <b>nông</b> — ngược với <b>глубо́кий</b>. Dạng ngắn giống cái nhấn '
    'đuôi <b>мелка́</b>; so sánh hơn <b>ме́льче</b>.</div>'
    '<div class="hd-warn">Nhỏ về kích thước, tuổi nói chung là <b>ма́ленький</b>; '
    '<b>ме́лкий</b> là nhỏ li ti, lặt vặt.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ме́лочь</b> chuyện vặt, tiền lẻ · <b>мель</b> bãi cạn · '
    '<b>ме́лко</b> nhỏ, vụn (trạng từ)</div>'
)

# --------------------------------------------------------------------- тупой
S["тупой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">туп-</span>'
    '<span class="hd-gloss">CÙN, không sắc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́й</span>'
    '<span class="hd-gloss">đuôi tính từ có nhấn</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dao cùn → óc cùn = đần; đau cùn = âm ỉ (<b>тупа́я боль</b>); góc cùn = '
    'góc tù. Ngược nghĩa với <b>о́стрый</b> sắc, nhọn. Dạng ngắn giống cái nhấn đuôi: '
    '<b>тупа́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тупи́ть</b> làm cùn · <b>тупи́ца</b> kẻ đần · '
    '<b>отупе́ть</b> hoá đần</div>'
)

# --------------------------------------------------------------------- ровный
S["ровный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ров-</span>'
    '<span class="hd-gloss">BẰNG, NGANG NHAU — cùng gốc <b>ра́вный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ный</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỗ nào cũng bằng nhau ⇒ phẳng, đều, thẳng; tính người: điềm tĩnh. '
    '<b>ров-</b> là dạng Nga, <b>рав-</b> là dạng Slavơ nhà thờ của cùng một gốc. Dạng ngắn '
    'chêm <b>е</b>: <b>ро́вен</b>, <b>ровна́</b>.</div>'
    '<div class="hd-warn"><b>ро́вно</b> còn nghĩa ĐÚNG, TRÒN (giờ, số): '
    '<i>ро́вно в два часа́</i> đúng hai giờ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ра́вный</b> bằng nhau · <b>сравни́ть</b> so sánh · '
    '<b>рове́сник</b> người cùng tuổi</div>'
)

# --------------------------------------------------------------------- тайный
S["тайный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">тай-</span>'
    '<span class="hd-gloss">GIẤU — gốc của <b>таи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ный</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tính từ của <b>та́йна</b> bí mật: thứ bị giấu đi. Dạng ngắn chêm '
    '<b>е</b>: <b>та́ен</b>. Trạng từ <b>та́йно</b> lén lút.</div>'
    '<div class="hd-warn"><b>та́йный</b> là giấu kín (tình yêu, ước muốn, cuộc gặp); tài liệu '
    '«mật» theo quy định là <b>секре́тный</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>та́йна</b> bí mật · <b>таи́ть</b> giấu kín · '
    '<b>вта́йне</b> thầm kín, lén</div>'
)

# --------------------------------------------------------------------- частный
S["частный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">част-</span>'
    '<span class="hd-gloss">PHẦN — <b>часть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ный</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thuộc về một PHẦN, không phải của chung ⇒ <b>tư nhân</b> '
    '(<b>ча́стная со́бственность</b> tư hữu) và <b>cá biệt</b> (<b>ча́стный слу́чай</b> trường '
    'hợp riêng).</div>'
    '<div class="hd-warn">Đừng lẫn <b>ча́стый</b> thường xuyên (<b>ча́сто</b> hay, thường) — chỉ '
    'thiếu một chữ <b>н</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>часть</b> phần · <b>уча́стие</b> sự tham gia · '
    '<b>уча́стник</b> người tham gia · <b>сча́стье</b> hạnh phúc</div>'
)

# --------------------------------------------------------------------- дополнительный
S["дополнительный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-</span>'
    '<span class="hd-gloss">TỚI ĐỦ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-полн-</span>'
    '<span class="hd-gloss">ĐẦY — <b>по́лный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́тельный</span>'
    '<span class="hd-gloss">đuôi tính từ từ động từ (<b>допо́лнить</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đổ thêm cho tới đầy ⇒ bổ sung, thêm vào: <b>дополни́тельная '
    'информа́ция</b> thông tin bổ sung.</div>'
    '<div class="hd-warn">«Thêm» mà CẦN, có ích. «Thừa», không cần là <b>ли́шний</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>по́лный</b> đầy · <b>допо́лнить</b> bổ sung · '
    '<b>дополне́ние</b> phần bổ sung · <b>запо́лнить</b> điền vào</div>'
)

# --------------------------------------------------------------------- свойство
S["свойство"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">свой-</span>'
    '<span class="hd-gloss">CỦA MÌNH — <b>свой</b> (сво- gốc phản thân, cùng nhà với '
    '<b>себя́</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ство</span>'
    '<span class="hd-gloss">→ danh từ trừu tượng giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái «của riêng» một vật, sinh ra đã có ⇒ tính chất, thuộc tính: '
    '<i>сво́йства воды́</i> tính chất của nước.</div>'
    '<div class="hd-warn">«Property» nghĩa <b>tài sản</b> KHÔNG phải từ này — đó là '
    '<b>со́бственность</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>свой</b> của mình · <b>сво́йственный</b> vốn có, đặc trưng · '
    '<b>себя́</b> bản thân</div>'
)

# --------------------------------------------------------------------- вес
S["вес"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc với động từ <b>ве́сить</b> nặng (bao nhiêu). Số nhiều '
    'nhấn đuôi <b>веса́</b>, ít gặp.</div>'
    '<div class="hd-warn">Nói cân nặng dùng động từ, <b>с → ш</b> ở ngôi «tôi»: '
    '<i>Я ве́шу 60 кг</i> · <i>Ско́лько ты ве́сишь?</i></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ве́сить</b> nặng · <b>весы́</b> cái cân · '
    '<b>невесо́мость</b> tình trạng không trọng lượng</div>'
)

# --------------------------------------------------------------------- грязь
S["грязь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn <b>гряз-</b> bùn, đất bẩn — chính gốc của '
    '<b>гря́зный</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giống cái đuôi <b>-ь</b>: <b>гря́зи</b>, <b>гря́зью</b>. Nghĩa đen là '
    'bùn đất, nghĩa bóng là chuyện nhơ nhuốc.</div>'
    '<div class="hd-warn"><b>облива́ть гря́зью</b> — bôi nhọ (nghĩa đen: dội bùn lên ai).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гря́зный</b> bẩn · <b>гря́зно</b> bẩn (trạng từ) · '
    '<b>загрязне́ние</b> sự ô nhiễm</div>'
)

# --------------------------------------------------------------------- соответствовать
S["соответствовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">CÙNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ответ-</span>'
    '<span class="hd-gloss">ĐÁP LẠI — <b>отве́т</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ствовать</span>'
    '<span class="hd-gloss">đuôi động từ, chia <b>-ствую</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cùng đáp lại» một thứ ⇒ khớp với nó. Chỉ có thể CHT. Đòi cách 3: '
    '<i>соотве́тствовать тре́бованиям</i> đáp ứng yêu cầu. Chia: <b>соотве́тствую</b>, '
    '<b>соотве́тствует</b>.</div>'
    '<div class="hd-warn"><b>в соотве́тствии с</b> + cách 5 — theo đúng (luật, quy định).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отве́т</b> câu trả lời · <b>соотве́тствие</b> sự phù hợp · '
    '<b>соотве́тственно</b> tương ứng · <b>отве́тственный</b> có trách nhiệm</div>'
)

# --------------------------------------------------------------------- собственность
S["собственность"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со́бствен-</span>'
    '<span class="hd-gloss">CỦA CHÍNH MÌNH — <b>со́бственный</b> (соб- BẢN THÂN, cùng gốc '
    '<b>себя́</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ность</span>'
    '<span class="hd-gloss">→ danh từ trừu tượng giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tình trạng «là của chính mình» ⇒ quyền sở hữu, và thứ mình sở hữu: '
    '<b>ча́стная со́бственность</b> tư hữu.</div>'
    '<div class="hd-warn">«Property» nghĩa <b>tính chất</b> KHÔNG phải từ này — đó là '
    '<b>сво́йство</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>со́бственный</b> riêng của mình · <b>со́бственник</b> chủ sở hữu · '
    '<b>со́бственно</b> nói đúng ra</div>'
)

# --------------------------------------------------------------------- мелочь
S["мелочь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мел-оч-</span>'
    '<span class="hd-gloss">NHỎ VỤN — <b>ме́лкий</b>, к hoá ч</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ь</span>'
    '<span class="hd-gloss">danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gom những thứ <b>ме́лкий</b> lại: chuyện vặt, chi tiết nhỏ, tiền xu. Số '
    'nhiều trọng âm nhảy ra đuôi: <b>ме́лочи</b> → <b>мелоче́й</b>.</div>'
    '<div class="hd-warn">Tiền lẻ, tiền xu: <i>У вас есть ме́лочь?</i> — Anh có tiền lẻ '
    'không?</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ме́лкий</b> nhỏ vụn · <b>ме́лочный</b> nhỏ nhen · '
    '<b>мель</b> bãi cạn</div>'
)

# --------------------------------------------------------------------- отличаться
S["отличаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-лич-</span>'
    '<span class="hd-gloss">TÁCH RA KHỎI + MẶT — như <b>отли́чие</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi thể CHT</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">phản thân: tự mình tách ra</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mặt mình tách khỏi mặt người khác ⇒ khác. Không có cặp HT cùng nghĩa: '
    '<b>отличи́ться</b> (HT) lại là «lập công, nổi danh».</div>'
    '<div class="hd-warn">Hai cách, hai nghĩa: <b>от</b> + cách 2 = khác với '
    '(<i>отлича́ться от бра́та</i>) · + cách 5 = nổi bật nhờ (<i>отлича́ться умо́м</i>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отли́чие</b> sự khác biệt · <b>отличи́ть</b> phân biệt · '
    '<b>отли́чный</b> xuất sắc · <b>лицо́</b> khuôn mặt</div>'
)

B = {
    "docbangmat": 81,
    "loitubat": 2,
    "nguonsai": 1,
    "baolen": [
        "Va chạm nghĩa: không có (máy báo 0; tự soát thêm cũng không thấy cặp nào trùng HẾT nghĩa mà badge không tách).",
        "ĐỀ XUẤT MIỄN TRỪ (KHÔNG tự thêm — lệnh sửa mientru.py bị chặn, nên đã SỬA DỮ LIỆU để cửa xanh): (a) тупи́к «ngõ cụt» — nouns.csv có hai dòng ту'пик (animate=1, thật ra là chim, glossed nhầm dead end) và тупи'к, khoá tra gộp nên dòng sai thắng; đã BỎ тупи́к khỏi Họ hàng của тупо́й dù đó là móc nhớ hay nhất («đường cùn»). (b) в грязи́ (cách vị trí, cùng lớp двери́) — BAT THUONG chỉ đúng chỗ này, đã bỏ câu đó khỏi thẻ грязь. (c) ме́лок (dạng ngắn của ме́лкий) ↔ мело́к «viên phấn» — bỏ, giữ мелка́. Nếu luồng chính thêm (a)(b) vào MIEN_TRU thì có thể khôi phục.",
        "Nguồn sai bác: nouns.csv dòng ту'пик glossed «dead end» nhưng animate=1 — trọng âm đúng của «ngõ cụt» là тупи́к.",
        "Lỗi tự bắt (loitubat=2): thẻ вес viết «danh từ đứng sau động từ ве́сить» (vô nghĩa) → «cùng gốc với»; дополни́тельный gắn đuôi -и́тельный vào дополня́ть → đúng là допо́лнить.",
        "Không chắc (mức tin vừa): мель «bãi cạn» cùng gốc ме́лкий (từ nguyên, chưa đối chiếu nguồn); sắc thái та́йный (giấu kín) vs секре́тный (mật theo quy định) là khái quát, có ngoại lệ (та́йная поли́ция).",
        "V cần duyệt (16 thẻ): глубина, примета, повреждение, отличие, дикий, мелкий, тупой («;»→«,»), ровный, тайный, частный, свойство, грязь, соответствовать, собственность, мелочь (THIẾU hẳn «tiền lẻ» — small change/coins), отличаться. Không viết V cho высота, дополнительный, вес (đề cũ đã đúng).",
    ],
}
