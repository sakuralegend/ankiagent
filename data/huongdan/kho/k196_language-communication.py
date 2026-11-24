# -*- coding: utf-8 -*-
"""k196 — language::communication (lô trộn): gọi lại, thuyết phục, giấy tờ, vài từ mượn.

Chỗ cần nhất quán trong lô:
(1) о → а khi thêm -ива- chạy qua BA thẻ: настоя́ть → наста́ивать, звон- → перезва́нивать,
    уговори́ть → угова́ривать (giống разгово́р → разгова́ривать). Mỗi thẻ nói một câu, không bảng.
(2) перезвони́ть khớp звони́ть [k54]: trọng âm ở đuôi suốt bảng, gọi CHO AI = cách 3.
(3) угова́ривать / уговори́ть ↔ убежда́ть / убеди́ть [k124]: уговори́ть ai LÀM (+ nguyên thể),
    убеди́ть ai TIN (в + cách 6). Câu «mãi mà không được» chép khuôn thẻ убежда́ть.
(4) отчего́ khớp почему́ [k17] / заче́м: giới từ + một cách của что.
(5) Chẻ khớp thẻ cũ: безусло́вно ← усло́вие [k113]; по-ви́димому ← ви́димо [k165];
    визи́тка ← визи́т [k169]; дипло́м ← диплома́т [k148]; выпускни́к ← вы́пуск [k177];
    иссле́дователь ← иссле́дование [k120]; утвержде́ние ← утвержда́ть [k169].
Họ hàng cố ý vắng: không thẻ nào.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "коляска": "xe đẩy em bé, xe đẩy, xe lăn",                        # gloss: wheelchair
    "безусловно": "chắc chắn, hẳn nhiên, dĩ nhiên, vô điều kiện",     # gloss: unconditionally
    "визитка": "danh thiếp, card visit",                              # «áo đuôi tôm» (morning coat) cổ, dễ lẫn фрак
    "диплом": "bằng tốt nghiệp, bằng cấp, giấy chứng nhận, bằng khen",  # gloss: award / prize
    "исследователь": "nhà nghiên cứu, nhà thám hiểm",                 # «người điều tra» = сле́дователь
    "утверждение": "lời khẳng định, lời tuyên bố, luận điểm, sự phê duyệt",  # gloss: approval / ratification
    "перезванивать": "gọi lại, gọi điện lại",                         # «nhiều lần» không có trong gloss
}

# --------------------------------------------------------------------- коляска
S["коляска"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кол-</span>'
    '<span class="hd-gloss">BÁNH XE — cùng gốc <b>колесо́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́ска</span>'
    '<span class="hd-gloss">đuôi mượn qua tiếng Ba Lan, không tách tiếp</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Xe nhỏ có bánh» ⇒ xe đẩy em bé; xe cho người ngồi ⇒ <b>инвали́дная '
    'коля́ска</b> xe lăn. Số nhiều cách 2 chèn <b>о</b>: <b>коля́сок</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>колесо́</b> bánh xe</div>'
)

# --------------------------------------------------------------------- отчего
S["отчего"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от</span>'
    '<span class="hd-gloss">TỪ, do (từ đâu mà ra)</span></div>'
    '<div class="hd-row"><span class="hd-piece">чего́</span>'
    '<span class="hd-gloss">cách 2 của <b>что</b> (cái gì)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen «từ cái gì mà ra» ⇒ do đâu, vì sao — hỏi NGUYÊN NHÂN y như '
    '<b>почему́</b>, chỉ mềm và văn nói hơn: <b>Отчего́ ты не спишь?</b> Cùng khuôn giới từ + '
    '<b>что</b> với <b>почему́</b>, <b>заче́м</b>.</div>'
    '<div class="hd-warn">Đáp đúng cặp: <b>Отчего́?</b> → <b>Оттого́ что…</b> (bởi vì…), như '
    '<b>Почему́?</b> → <b>Потому́ что…</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>почему́</b> tại sao · <b>заче́м</b> để làm gì · <b>оттого́</b> vì thế '
    '· <b>что</b> cái gì</div>'
)

# --------------------------------------------------------------------- безусловно
S["безусловно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">без-</span>'
    '<span class="hd-gloss">KHÔNG CÓ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-услов-</span>'
    '<span class="hd-gloss">ĐIỀU KIỆN — <b>усло́вие</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-о</span>'
    '<span class="hd-gloss">→ tính từ, rồi → trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Không kèm điều kiện nào» ⇒ vô điều kiện ⇒ chắc chắn, dĩ nhiên. Hay đứng '
    'đầu câu, ngăn bằng phẩy: <b>Безусло́вно, ты прав.</b> Hoặc đáp gọn một từ: '
    '<b>Безусло́вно!</b> = Chắc chắn rồi!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>усло́вие</b> điều kiện · <b>усло́вный</b> có điều kiện, quy ước · '
    '<b>безусло́вный</b> tuyệt đối</div>'
)

# --------------------------------------------------------------------- по-видимому
S["по-видимому"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">THEO</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ви́дим-</span>'
    '<span class="hd-gloss">THẤY ĐƯỢC — <b>ви́димый</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ому</span>'
    '<span class="hd-gloss">đuôi cách 3 của tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Theo những gì thấy được» ⇒ xem ra, hình như — đoán từ dấu hiệu, gần y '
    '<b>ви́димо</b>, nghe sách vở hơn chút. Cùng khuôn <b>по-</b> + <b>-ому</b> với '
    '<b>по-мо́ему</b> theo tôi, <b>по-но́вому</b> theo kiểu mới.</div>'
    '<div class="hd-warn">Gạch nối là bắt buộc: <b>по-ви́димому</b>, không viết liền.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ви́димо</b> hình như · <b>ви́димый</b> thấy được · <b>ви́деть</b> thấy</div>'
)

# --------------------------------------------------------------------- визитка
S["визитка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">визи́т-</span>'
    '<span class="hd-gloss">CUỘC THĂM — <b>визи́т</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">đuôi rút gọn cả cụm thành một từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gọn của <b>визи́тная ка́рточка</b> «tấm thẻ đi thăm» — xưa đến thăm thì để '
    'lại thẻ ⇒ danh thiếp. Khuôn rút gọn tính từ + danh từ → <b>-ка</b> rất hay gặp: '
    '<b>маршру́тка</b> ← <b>маршру́тное такси́</b>. Số nhiều cách 2 chèn <b>о</b>: '
    '<b>визи́ток</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>визи́т</b> cuộc thăm · <b>визи́тная ка́рточка</b> danh thiếp</div>'
)

# --------------------------------------------------------------------- диплом
S["диплом"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn Hy Lạp <i>diplōma</i> «tờ gấp đôi» — văn thư chính thức; không chẻ '
    'trong tiếng Nga. Chính là <i>diploma</i> tiếng Anh.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tờ văn thư chứng nhận ⇒ bằng tốt nghiệp, bằng khen: <b>дипло́м пе́рвой '
    'сте́пени</b> giải nhất. Danh từ giống đực, biến cách đều.</div>'
    '<div class="hd-warn">Sinh viên nói <b>писа́ть дипло́м</b>, <b>защища́ть дипло́м</b> = viết, bảo '
    'vệ KHOÁ LUẬN tốt nghiệp — không phải tấm bằng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дипло́мный</b> thuộc khoá luận · <b>диплома́т</b> nhà ngoại giao · '
    '<b>диплома́тия</b> ngoại giao</div>'
)

# --------------------------------------------------------------------- издательство
S["издательство"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">из-</span>'
    '<span class="hd-gloss">RA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-да-</span>'
    '<span class="hd-gloss">ĐƯA, CHO — <b>дать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-тель-</span>'
    '<span class="hd-gloss">người làm — như <b>писа́тель</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ство</span>'
    '<span class="hd-gloss">→ danh từ giống trung: cơ quan, nghề</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Xây từng tầng: <b>изда́ть</b> đưa (sách) RA = xuất bản (đúng «xuất» = ra) → '
    '<b>изда́тель</b> người xuất bản → <b>изда́тельство</b> nhà xuất bản. Cùng khuôn '
    '<b>-тельство</b> với <b>прави́тельство</b> chính phủ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>изда́ть</b> / <b>издава́ть</b> xuất bản · <b>изда́ние</b> ấn phẩm, lần '
    'xuất bản · <b>изда́тель</b> người xuất bản</div>'
)

# --------------------------------------------------------------------- выпускник
S["выпускник"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span>'
    '<span class="hd-gloss">RA NGOÀI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пуск-</span>'
    '<span class="hd-gloss">THẢ, CHO ĐI — như <b>вы́пуск</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ни́к</span>'
    '<span class="hd-gloss">người gắn với việc đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người được trường «thả ra» ⇒ người tốt nghiệp. Trọng âm đứng ở đuôi suốt '
    'bảng: <b>выпускника́</b>, <b>выпускники́</b>. Nữ: <b>выпускни́ца</b>.</div>'
    '<div class="hd-warn"><b>выпускно́й</b> (<b>ве́чер</b>) = lễ / dạ hội tốt nghiệp — học sinh Nga '
    'nói gọn một từ <b>выпускно́й</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вы́пуск</b> khoá tốt nghiệp · <b>выпуска́ть</b> / <b>вы́пустить</b> thả '
    'ra · <b>о́тпуск</b> kỳ nghỉ phép</div>'
)

# --------------------------------------------------------------------- исследователь
S["исследователь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ис-след-ова-</span>'
    '<span class="hd-gloss">thân của <b>иссле́довать</b> — lần theo DẤU VẾT cho ra</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тель</span>'
    '<span class="hd-gloss">NGƯỜI LÀM việc đó — như <b>писа́тель</b>, <b>учи́тель</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bỏ <b>-ть</b> của động từ, gắn <b>-тель</b>: <b>иссле́дова-ть</b> → '
    '<b>иссле́дова-тель</b> người nghiên cứu, thám hiểm. Trọng âm đứng yên.</div>'
    '<div class="hd-warn">Đuôi <b>-тель</b> luôn GIỐNG ĐỰC dù tận cùng <b>-ь</b>: '
    '<b>изве́стный иссле́дователь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>иссле́довать</b> nghiên cứu · <b>иссле́дование</b> công trình nghiên '
    'cứu · <b>сле́дователь</b> điều tra viên · <b>след</b> dấu vết</div>'
)

# --------------------------------------------------------------------- цитата
S["цитата"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn Latin <i>citāta</i> «điều được dẫn ra», không chẻ trong tiếng Nga — '
    'cùng gốc <i>cite</i>, <i>citation</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Lời người khác được dẫn lại ⇒ câu trích dẫn. Động từ: <b>цити́ровать</b> '
    'trích dẫn, <b>-ова-</b> → <b>-у-</b>: <b>цити́рую</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>цити́ровать</b> trích dẫn · <b>цити́рование</b> sự trích dẫn</div>'
)

# --------------------------------------------------------------------- утверждение
S["утверждение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">làm cho thành</span></div>'
    '<div class="hd-row"><span class="hd-piece">-твержд-</span>'
    '<span class="hd-gloss">CỨNG, CHẮC — <b>твёрд-</b> của <b>твёрдый</b>, <b>д→жд</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ние</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>утверди́ть</b> / <b>утвержда́ть</b> «làm cho chắc»: nói chắc ⇒ '
    'lời khẳng định; đóng dấu chắc ⇒ sự phê duyệt (<b>утвержде́ние пла́на</b>). <b>д→жд</b> y như '
    '<b>убеди́ть</b> → <b>убежде́ние</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>утвержда́ть</b> khẳng định · <b>твёрдый</b> cứng · <b>твёрдо</b> dứt '
    'khoát</div>'
)

# --------------------------------------------------------------------- сотовый
S["сотовый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со́т-</span>'
    '<span class="hd-gloss">Ô TỔ ONG — <b>со́ты</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ов-ый</span>'
    '<span class="hd-gloss">đuôi tính từ «thuộc về»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mạng di động chia vùng thành từng ô như tổ ong — đúng hình ảnh '
    '<i>cellular</i> (<i>cell</i> = ô). <b>со́товый телефо́н</b> điện thoại di động; nói tắt chỉ '
    '<b>со́товый</b>: <b>Позвони́ мне на со́товый</b>.</div>'
    '<div class="hd-warn">Đừng lẫn <b>со́тый</b> = thứ một trăm (gốc <b>сто</b>), khác gốc hẳn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>со́ты</b> tổ ong · <b>со́товая связь</b> mạng di động</div>'
)

# --------------------------------------------------------------------- аргумент
S["аргумент"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn Latin <i>argūmentum</i>, không chẻ trong tiếng Nga — mặt chữ y '
    '<i>argument</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thứ đưa ra để chứng minh ⇒ lý lẽ, luận cứ: <b>приводи́ть аргуме́нты</b> '
    'đưa ra lý lẽ; <b>аргуме́нт в по́льзу</b> + cách 2 = luận cứ ủng hộ điều gì.</div>'
    '<div class="hd-warn">Chỉ là LÝ LẼ, không bao giờ là «cuộc cãi nhau» như <i>argument</i> tiếng '
    'Anh — cãi nhau là <b>спор</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>аргументи́ровать</b> lập luận, dẫn chứng · <b>аргумента́ция</b> lối lập '
    'luận</div>'
)

# --------------------------------------------------------------------- настаивать
S["настаивать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">LÊN TRÊN, đè lên</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ста́-</span>'
    '<span class="hd-gloss">ĐỨNG — <b>стоя́ть</b>, <b>о→а</b> khi thêm <b>-ива-</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành, chia đều: <b>наста́иваю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đứng lì trên» một ý ⇒ khăng khăng, nhất quyết đòi. Để lá, thuốc «đứng» '
    'lâu trong nước ⇒ ngâm, hãm. Cặp HT: <b>настоя́ть</b> (<b>настою́</b>).</div>'
    '<div class="hd-warn">Khăng khăng VỀ cái gì: <b>на</b> + cách 6 — <b>наста́ивать на своём</b> = '
    'khăng khăng giữ ý mình.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>настоя́ть</b> (HT) · <b>стоя́ть</b> đứng · <b>насто́йчивый</b> kiên trì · '
    '<b>насто́йка</b> rượu ngâm</div>'
)

# --------------------------------------------------------------------- перезванивать
S["перезванивать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пере-</span>'
    '<span class="hd-gloss">LẠI LẦN NỮA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-зва́н-</span>'
    '<span class="hd-gloss">= <b>звон</b> tiếng chuông, <b>о→а</b> khi thêm <b>-ива-</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành, chia đều: <b>перезва́ниваю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Làm chuông reo lại» ⇒ gọi lại. Thể CHT của <b>перезвони́ть</b>: dùng cho '
    'thói quen, việc lặp — <b>Он никогда́ не перезва́нивает</b> anh ta chẳng bao giờ gọi lại. '
    '<b>о→а</b> y như <b>разгово́р</b> → <b>разгова́ривать</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>перезвони́ть</b> (HT) · <b>звони́ть</b> gọi điện · <b>звоно́к</b> cuộc '
    'gọi</div>'
)

# --------------------------------------------------------------------- перезвонить
S["перезвонить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пере-</span>'
    '<span class="hd-gloss">LẠI LẦN NỮA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-звон-и́ть</span>'
    '<span class="hd-gloss">làm chuông reo — chính là <b>звони́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thể HOÀN THÀNH: gọi lại một cuộc. Câu nghe hằng ngày: <b>Я вам '
    'перезвоню́</b> = Tôi sẽ gọi lại cho anh/chị. Gọi CHO AI = cách 3, như <b>звони́ть</b>: '
    '<b>Перезвони́ ма́ме!</b></div>'
    '<div class="hd-warn">Trọng âm ở ĐUÔI suốt bảng chia, y <b>звони́ть</b>: <b>перезвони́шь</b>, '
    '<b>перезвоня́т</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>перезва́нивать</b> (CHT) · <b>звони́ть</b> gọi điện · <b>позвони́ть</b> '
    'gọi một cuộc</div>'
)

# --------------------------------------------------------------------- уговаривать
S["уговаривать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">ở đây: làm cho ĐƯỢC việc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-гова́р-</span>'
    '<span class="hd-gloss">NÓI — <b>говор-</b>, <b>о→а</b> khi thêm <b>-ива-</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành, chia đều: <b>угова́риваю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Nói mãi cho tới khi người ta chịu» ⇒ dỗ, nài, thuyết phục. Thể CHT: đang '
    'cố, chưa chắc được. Cặp HT: <b>уговори́ть</b>.</div>'
    '<div class="hd-warn">Hai thể tách rõ: <b>Он до́лго угова́ривал её, но не уговори́л</b> — anh '
    'ấy nài mãi mà cô ấy không chịu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уговори́ть</b> (HT) · <b>говори́ть</b> nói · <b>разгова́ривать</b> trò '
    'chuyện · <b>договори́ться</b> thoả thuận</div>'
)

# --------------------------------------------------------------------- уговорить
S["уговорить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">ở đây: làm cho ĐƯỢC việc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-говор-и́ть</span>'
    '<span class="hd-gloss">NÓI — chính là <b>говори́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thể HOÀN THÀNH: nói tới khi người ta chịu ⇒ thuyết phục được. Người ở '
    'cách 4 + việc ở nguyên thể: <b>Я уговори́л его́ пойти́ в кино́.</b></div>'
    '<div class="hd-warn">Khác <b>убеди́ть</b>: <b>уговори́ть</b> ai LÀM (+ nguyên thể) · '
    '<b>убеди́ть</b> ai TIN (<b>в</b> + cách 6).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>угова́ривать</b> (CHT) · <b>говори́ть</b> nói · <b>договори́ться</b> '
    'thoả thuận · <b>разгово́р</b> cuộc trò chuyện</div>'
)

B = {
    "docbangmat": 78,
    "loitubat": 0,
    "nguonsai": 2,
    "baolen": [
        "VA CHẠM KHÔNG GỠ ĐƯỢC TỪ PHÍA LÔ NÀY (thẻ đã nạp, không sửa): đề убежда́ть/убеди́ть[k124] chỉ «thuyết phục» nằm gọn trong đề угова́ривать {thuyết phục, dỗ dành, năn nỉ} / уговори́ть {thuyết phục, dỗ cho đồng ý, nói cho chịu}. Phía thẻ của tôi đã có nghĩa riêng (gloss talk into) nên nhìn đề của nó là ra; còn nhìn «thuyết phục» trơn thì cả hai đều hợp. Không cắt «thuyết phục» (nghĩa chính). Muốn gỡ hẳn thì phải thêm nghĩa cho убежда́ть/убеди́ть (vd «làm cho tin» — gloss convince) — user quyết.",
        "VA CHẠM tương tự: đề почему́[k17, đã nạp] {tại sao, vì sao} nằm gọn trong отчего́ {tại sao, vì sao, do đâu}. Gloss của отчего́ chỉ có «why», không còn nghĩa nào để thêm; giữ nguyên, không viết V.",
        "Nguồn sai đã bác (2): иссле́дователь «người điều tra» (gloss investigator theo nghĩa khoa học; người điều tra vụ án là сле́дователь) → bỏ; перезва́нивать «gọi điện lại nhiều lần» (gloss không có nghĩa lặp nhiều lần, chỉ có call back / phone round) → bỏ.",
        "V cần duyệt (7): коля́ска +xe lăn (gloss wheelchair) · безусло́вно +vô điều kiện (gloss unconditionally) · визи́тка bỏ «áo đuôi tôm» (morning coat — nghĩa cổ, dễ lẫn фрак) · дипло́м +bằng khen (gloss award) · иссле́дователь bỏ «người điều tra» · утвержде́ние +sự phê duyệt (gloss approval) · перезва́нивать bỏ «nhiều lần». Chưa tự chạy `vacham` cho V mới.",
        "Không chắc (đã viết, không gắn Mức tin): коля́ска ← Ba Lan kolaska, gốc kolo «bánh xe» (Vasmer, như tôi nhớ); по-ви́димому «sách vở hơn ви́димо một chút» là sắc thái, không phải luật; у- trong уговори́ть = «làm cho được việc» là cách giải nghĩa tiền tố, không phải nghĩa tách bạch.",
        "Thẻ дипло́м có ô đỏ «писать/защищать диплом = khoá luận tốt nghiệp» — nghĩa có thật trong khẩu ngữ sinh viên nhưng gloss tiếng Anh không ghi, nên KHÔNG đưa vào V.",
    ],
}
