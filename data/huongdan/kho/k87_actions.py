# -*- coding: utf-8 -*-
"""k87 — actions: 19 động từ user vừa thêm, phần lớn là bản HOÀN THÀNH của thẻ cũ.

Mỗi thẻ soạn độc lập, không khối hệ thống. Chỗ cần nhất quán:
(1) bốn cặp thể soạn như một họ (задава́ть/зада́ть, конча́ться/ко́нчиться,
    начина́ться/нача́ться, открыва́ться/откры́ться): thẻ CHT nói chuyện thường lệ,
    thẻ HT nói chuyện một lần; -ся = sự việc TỰ xảy ra, chủ ngữ là sự việc;
(2) khớp khuôn chẻ của k85: -кры- CHE (от- gỡ ra / за- đậy vào), -чин-/-чн- BẮT ĐẦU,
    конч- = коне́ц (ц→ч), -мог- SỨC, прос- XIN, по-луч- học nguyên khối, -позд- MUỘN,
    -да- CHO (зада́ча).
"""

S = {}

# -------------------------------------------------------- задавать
S["задавать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không tách ra nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дава́-</span>'
    '<span class="hd-gloss">chính là <b>дава́ть</b> — CHO</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">"Cho ra" một câu hỏi, một bài tập ⇒ đặt câu hỏi, giao bài. Chia y như '
    '<b>дава́ть</b>: <b>-ва-</b> rơi mất ở hiện tại — <b>я задаю́, ты задаёшь</b>. '
    'Cặp thể: <b>зада́ть</b>.</div>'
    '<div class="hd-warn">Hỏi AI thì dùng <b>спра́шивать</b>; còn "đặt câu hỏi" là cụm cố định '
    '<b>задава́ть вопро́с</b>, người được hỏi ở cách 3: <i>задава́ть вопро́с учи́телю</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дава́ть</b> cho · <b>зада́ть</b> đặt, giao (HT) · '
    '<b>зада́ние</b> bài tập, nhiệm vụ · <b>зада́ча</b> bài toán, nhiệm vụ</div>'
)

# -------------------------------------------------------- задать
S["задать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không tách ra nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-да́ть</span>'
    '<span class="hd-gloss">chính là <b>дать</b> — CHO</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp HT của <b>задава́ть</b>: đặt xong một câu hỏi, giao xong một bài. '
    'Bảng chia lạ vì nó chia Y HỆT <b>дать</b> — thuộc <b>дать</b> là thuộc luôn từ này: '
    '<b>зада́м, зада́шь, зада́ст, задади́м, задади́те, зададу́т</b>; quá khứ '
    '<b>за́дал</b> nhưng <b>задала́</b>.</div>'
    '<div class="hd-warn">Cụm phải thuộc: <b>зада́ть вопро́с</b> = đặt câu hỏi · '
    '<b>зада́ть дома́шнее зада́ние</b> = giao bài tập về nhà.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дать</b> cho · <b>задава́ть</b> đặt, giao (CHT) · '
    '<b>зада́ние</b> bài tập · <b>зада́ча</b> bài toán, nhiệm vụ</div>'
)

# -------------------------------------------------------- закрыть
S["закрыть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">che kín, chắn lại</span></div>'
    '<div class="hd-row"><span class="hd-piece">-кры-</span>'
    '<span class="hd-gloss">gốc CHE, ĐẬY</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đậy kín lại ⇒ đóng, che. Đối của <b>откры́ть</b>: cùng gốc, chỉ đổi '
    '<b>от-</b> (gỡ ra) thành <b>за-</b> (đậy vào). Khi chia, <b>ы</b> đổi thành <b>о</b>: '
    '<b>я закро́ю, ты закро́ешь</b>. Cặp CHT: <b>закрыва́ть</b>.</div>'
    '<div class="hd-warn">Nhắm mắt cũng là "đậy" mắt lại: <b>закры́ть глаза́</b>. '
    'Đã đóng sẵn rồi → dạng ngắn: <b>Дверь закры́та.</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>закрыва́ть</b> đóng (CHT) · <b>откры́ть</b> mở · '
    '<b>закры́тый</b> đóng, kín · <b>кры́ша</b> mái nhà (cái che)</div>'
)

# -------------------------------------------------------- кончаться
S["кончаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">конч-</span>'
    '<span class="hd-gloss">gốc KẾT THÚC — chính là <b>коне́ц</b>, <b>ц</b> hoá <b>ч</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">TỰ nó — không ai làm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>конча́ть</b> là ai đó làm xong; thêm <b>-ся</b> thì sự việc TỰ đi tới '
    '<b>коне́ц</b>: <i>Уро́к конча́ется в два.</i> Cặp HT là <b>ко́нчиться</b> — để ý trọng âm: '
    'bản CHT nhấn đuôi, bản HT nhấn gốc.</div>'
    '<div class="hd-warn">Đang cạn dần: <b>У меня́ конча́ются де́ньги.</b> Tiền mình sắp hết — '
    'TIỀN là chủ ngữ, không phải "tôi".</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>конча́ть</b> làm xong · <b>ко́нчиться</b> hết (HT) · '
    '<b>коне́ц</b> phần cuối · <b>наконе́ц</b> cuối cùng thì</div>'
)

# -------------------------------------------------------- кончить
S["кончить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">конч-</span>'
    '<span class="hd-gloss">gốc KẾT THÚC — chính là <b>коне́ц</b>, <b>ц</b> hoá <b>ч</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đưa việc tới <b>коне́ц</b> một lần ⇒ làm xong. Cặp CHT là '
    '<b>конча́ть</b>. Nguyên thể theo sau ở thể chưa hoàn thành: <i>ко́нчить рабо́тать</i>.</div>'
    '<div class="hd-warn">Dùng trống không, nói về người thì mang nghĩa tục (lên đỉnh). Nói '
    '"làm xong việc" an toàn hơn với <b>зако́нчить</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>коне́ц</b> phần cuối · <b>ко́нчиться</b> hết, kết thúc · '
    '<b>зако́нчить</b> làm xong · <b>око́нчить</b> tốt nghiệp</div>'
)

# -------------------------------------------------------- кончиться
S["кончиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ко́нчи-ть</span>'
    '<span class="hd-gloss">chính là <b>ко́нчить</b> — làm xong</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">TỰ nó — không ai làm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Sự việc tự đi tới <b>коне́ц</b>, một lần là xong: '
    '<i>Фильм ко́нчился.</i> Phim hết rồi. Cặp CHT: <b>конча́ться</b>.</div>'
    '<div class="hd-warn">Hết sạch cái gì: cái bị hết làm chủ ngữ — <b>У меня́ ко́нчились '
    'де́ньги.</b> Mình hết tiền rồi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ко́нчить</b> làm xong · <b>конча́ться</b> hết dần (CHT) · '
    '<b>коне́ц</b> phần cuối · <b>наконе́ц</b> cuối cùng thì</div>'
)

# -------------------------------------------------------- называться
S["называться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không tách ra nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-зыва́-</span>'
    '<span class="hd-gloss">gốc GỌI — biến thể của <b>звать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть-ся</span>'
    '<span class="hd-gloss">đuôi nguyên thể + "được, bị"</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>называ́ть</b> = gọi là, đặt tên; thêm <b>-ся</b> ⇒ được gọi là. '
    'Tên đứng ở cách 1: <i>Э́тот го́род называ́ется Москва́.</i></div>'
    '<div class="hd-warn">Hỏi tên ĐỒ VẬT, nơi chốn: <b>Как называ́ется…?</b> Hỏi tên NGƯỜI '
    'thì không dùng từ này mà nói <b>Как тебя́ зову́т?</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>звать</b> gọi · <b>назва́ние</b> tên gọi · '
    '<b>называ́ть</b> gọi là · <b>позва́ть</b> gọi tới</div>'
)

# -------------------------------------------------------- начать
S["начать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">tiền tố, ở đây KHÔNG mang nghĩa riêng tách ra được</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ча-</span>'
    '<span class="hd-gloss">gốc BẮT ĐẦU — cùng gốc <b>-чин-</b> của <b>начина́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc này đổi mặt liên tục: <b>-ча-</b> ở nguyên thể, <b>-чн-</b> khi chia '
    '(<b>я начну́, ты начнёшь</b>), <b>-чин-</b> ở cặp CHT <b>начина́ть</b>. Quá khứ: '
    '<b>на́чал</b> nhưng <b>начала́</b>.</div>'
    '<div class="hd-warn">Nguyên thể đứng sau luôn ở thể CHƯA hoàn thành: <b>нача́ть чита́ть</b>. '
    'Ai bắt đầu việc → <b>нача́ть</b>; việc tự bắt đầu → <b>нача́ться</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>начина́ть</b> bắt đầu (CHT) · <b>нача́ло</b> sự bắt đầu · '
    '<b>снача́ла</b> lúc đầu · <b>нача́льник</b> thủ trưởng</div>'
)

# -------------------------------------------------------- начаться
S["начаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">нача́-ть</span>'
    '<span class="hd-gloss">chính là <b>нача́ть</b> — bắt đầu</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">TỰ nó — không ai làm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Sự việc TỰ bắt đầu, một lần: chủ ngữ là buổi học, bộ phim, cơn mưa — '
    'không phải người. Chia như <b>нача́ть</b>, gốc lộ <b>-чн-</b>; hay gặp nhất là ngôi 3: '
    '<i>Уро́к начнётся в де́вять.</i> Cặp CHT: <b>начина́ться</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>нача́ть</b> bắt đầu · <b>начина́ться</b> bắt đầu (CHT) · '
    '<b>нача́ло</b> sự bắt đầu · <b>снача́ла</b> lúc đầu</div>'
)

# -------------------------------------------------------- начинаться
S["начинаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">начина́-ть</span>'
    '<span class="hd-gloss">chính là <b>начина́ть</b> — bắt đầu</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">TỰ nó — không ai làm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Sự việc tự bắt đầu, nói về giờ giấc thường lệ hoặc đang diễn ra: '
    '<i>Уро́к начина́ется в де́вять.</i> Buổi học (hằng ngày) bắt đầu lúc chín giờ. '
    'Cặp HT: <b>нача́ться</b>.</div>'
    '<div class="hd-warn">Người bắt đầu việc thì KHÔNG có <b>-ся</b>: <b>Я начина́ю рабо́ту.</b> '
    'Việc tự bắt đầu mới có: <b>Рабо́та начина́ется.</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>начина́ть</b> bắt đầu · <b>нача́ться</b> bắt đầu (HT) · '
    '<b>нача́ло</b> sự bắt đầu · <b>снача́ла</b> lúc đầu</div>'
)

# -------------------------------------------------------- окончить
S["окончить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không tách ra nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-конч-</span>'
    '<span class="hd-gloss">gốc KẾT THÚC — chính là <b>коне́ц</b>, <b>ц</b> hoá <b>ч</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đi trọn tới <b>коне́ц</b> — sắc trang trọng hơn <b>ко́нчить</b>, nên là từ '
    'dùng cho trường lớp: học xong cả khoá ⇒ tốt nghiệp. Cặp CHT: <b>ока́нчивать</b>.</div>'
    '<div class="hd-warn">Tốt nghiệp trường nào: cách 4, KHÔNG giới từ — <b>око́нчить '
    'университе́т</b>, <b>око́нчить шко́лу</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>коне́ц</b> phần cuối · <b>ко́нчить</b> làm xong · '
    '<b>оконча́ние</b> phần kết; đuôi từ (ngữ pháp)</div>'
)

# -------------------------------------------------------- опоздать
S["опоздать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">tiền tố</span></div>'
    '<div class="hd-row"><span class="hd-piece">-позд-</span>'
    '<span class="hd-gloss">gốc MUỘN — của <b>по́здно</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thành ra <b>по́здно</b> một lần ⇒ đến muộn; muộn tới mức xe chạy mất ⇒ '
    'lỡ chuyến. Cặp CHT <b>опа́здывать</b> đổi <b>о</b> thành <b>а</b>.</div>'
    '<div class="hd-warn">Cả hai thứ đều đi với <b>на</b> + cách 4: muộn CÁI GÌ — '
    '<b>опозда́ть на по́езд</b> (lỡ tàu); muộn BAO LÂU — <b>опозда́ть на пять мину́т</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>по́здно</b> muộn · <b>по́здний</b> muộn, khuya · '
    '<b>опа́здывать</b> đến muộn (CHT) · <b>опозда́ние</b> sự đến trễ</div>'
)

# -------------------------------------------------------- осмотреть
S["осмотреть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">VÒNG QUANH, phủ khắp mặt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-смотре́-</span>'
    '<span class="hd-gloss">chính là <b>смотре́ть</b> — nhìn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhìn quanh khắp lượt ⇒ xem xét kỹ: bác sĩ khám bệnh nhân, khách tham '
    'quan thành phố. Trọng âm dịch y như <b>смотре́ть</b>: <b>я осмотрю́, ты осмо́тришь</b>. '
    'Cặp CHT: <b>осма́тривать</b>.</div>'
    '<div class="hd-warn"><b>смотре́ть на</b> + cách 4, nhưng <b>осмотре́ть</b> đi thẳng cách 4, '
    'không giới từ: <b>осмотре́ть музе́й</b>, <b>осмотре́ть больно́го</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>смотре́ть</b> nhìn, xem · <b>посмотре́ть</b> xem (HT) · '
    '<b>осма́тривать</b> xem xét (CHT) · <b>осмо́тр</b> sự khám, kiểm tra</div>'
)

# -------------------------------------------------------- открываться
S["открываться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">открыва́-ть</span>'
    '<span class="hd-gloss">chính là <b>открыва́ть</b> — mở</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">TỰ nó — không ai làm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái gì tự mở ra, nói về giờ giấc thường lệ: <i>Магази́н открыва́ется в '
    'де́вять.</i> Cửa hàng (hằng ngày) mở cửa lúc chín giờ. Cặp HT: <b>откры́ться</b>.</div>'
    '<div class="hd-warn">Cụm hay gặp: <b>Из окна́ открыва́ется вид на мо́ре.</b> Từ cửa sổ '
    'nhìn ra biển — cảnh "mở ra" trước mắt.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>открыва́ть</b> mở · <b>откры́ться</b> mở ra (HT) · '
    '<b>закрыва́ться</b> đóng lại · <b>откры́тка</b> bưu thiếp</div>'
)

# -------------------------------------------------------- открыть
S["открыть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">tách ra, rời khỏi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-кры-</span>'
    '<span class="hd-gloss">gốc CHE, ĐẬY — như trong <b>откры́тка</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gỡ cái che ra ⇒ mở; gỡ màn bí mật ⇒ phát hiện — y như tiếng Anh '
    '<i>dis-cover</i>. Khi chia, <b>ы</b> đổi thành <b>о</b>: <b>я откро́ю, ты откро́ешь</b>. '
    'Cặp CHT: <b>открыва́ть</b>.</div>'
    '<div class="hd-warn">Bật đèn, bật TV thì KHÔNG dùng từ này mà dùng <b>включи́ть</b>. '
    '<b>откры́ть</b> là mở thứ có nắp, có cửa: cửa, sách, hộp, cửa hàng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>открыва́ть</b> mở (CHT) · <b>закры́ть</b> đóng · '
    '<b>откры́тка</b> bưu thiếp · <b>откры́тие</b> sự khám phá, khai trương</div>'
)

# -------------------------------------------------------- открыться
S["открыться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">откры́-ть</span>'
    '<span class="hd-gloss">chính là <b>откры́ть</b> — mở</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">TỰ nó — không ai làm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tự mở ra, một lần: <i>Дверь откры́лась.</i> Cửa bật mở. Một lần đó có '
    'thể là lần đầu tiên ⇒ khai trương: <i>Откры́лся но́вый магази́н.</i> Chia như '
    '<b>откры́ть</b>: <b>откро́ется</b>. Cặp CHT: <b>открыва́ться</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>откры́ть</b> mở · <b>открыва́ться</b> mở ra (CHT) · '
    '<b>закры́ться</b> đóng lại · <b>откры́тие</b> sự khai trương</div>'
)

# -------------------------------------------------------- получить
S["получить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-луч-</span>'
    '<span class="hd-gloss">tiền tố + gốc cổ, nay không đứng riêng — học như một khối</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp HT của <b>получа́ть</b>: nhận xong một lần — <i>получи́ть письмо́</i>. '
    'Trọng âm: chỉ ngôi "tôi" nhấn đuôi <b>я получу́</b>, các ngôi khác lùi về gốc: '
    '<b>ты полу́чишь</b>.</div>'
    '<div class="hd-warn">Thêm <b>-ся</b> = ra được, thành công: <b>Получи́лось!</b> Được rồi! · '
    '<b>Не получи́лось.</b> Không thành.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>получа́ть</b> nhận (CHT) · <b>получи́ться</b> thành, ra được · '
    '<b>получа́тель</b> người nhận</div>'
)

# -------------------------------------------------------- помочь
S["помочь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мочь</span>'
    '<span class="hd-gloss">chính là <b>мочь</b> — CÓ SỨC, có thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Góp sức mình cho người khác, một lần. Chia y như <b>мочь</b>: <b>г</b> ở '
    'ngôi "tôi" và "họ", <b>ж</b> ở giữa — <b>помогу́, помо́жешь, помо́гут</b>; quá khứ '
    '<b>помо́г, помогла́</b>. Cặp CHT: <b>помога́ть</b>.</div>'
    '<div class="hd-warn">Người được giúp ở CÁCH 3, không phải cách 4: <b>Помоги́ мне!</b> · '
    '<b>помо́чь ма́ме</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мочь</b> có thể · <b>по́мощь</b> sự giúp đỡ · '
    '<b>помога́ть</b> giúp (CHT) · <b>помо́щник</b> người trợ giúp</div>'
)

# -------------------------------------------------------- попросить
S["попросить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố thể hoàn thành, không thêm nghĩa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-прос-</span>'
    '<span class="hd-gloss">gốc XIN, THỈNH CẦU — của <b>вопро́с</b>, <b>спроси́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bản HT của <b>проси́ть</b>: xin, nhờ một lần. Ngôi "tôi" <b>с</b> hoá '
    '<b>ш</b> — <b>я попрошу́</b>; các ngôi khác trọng âm lùi về gốc — '
    '<b>ты попро́сишь</b>.</div>'
    '<div class="hd-warn">Cùng gốc mà khác việc: <b>спроси́ть</b> = hỏi để BIẾT; '
    '<b>попроси́ть</b> = nhờ ai LÀM — người ở cách 4 + nguyên thể: '
    '<b>попроси́ть дру́га помо́чь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>проси́ть</b> xin, nhờ (CHT) · <b>про́сьба</b> lời thỉnh cầu · '
    '<b>вопро́с</b> câu hỏi · <b>спроси́ть</b> hỏi</div>'
)

V = {
    # Ngoặc "(câu hỏi)", "(bài tập)" vi phạm §2c — gỡ ngoặc thành nghĩa trọn cụm.
    # Gloss: ask/pose a question, assign/set homework, give a task, set (standard/goal).
    # Bỏ "đặt" trơn vì đụng положить "đặt".
    "задавать": "đặt câu hỏi, giao bài tập, giao nhiệm vụ, đề ra",
    "задать": "đặt câu hỏi, giao bài tập, giao nhiệm vụ, đề ra",
    # Ba PERF tranh "hoàn thành" (закончить k95, окончить lô này). Rút "hoàn thành"
    # khỏi кончить — gloss finish/end; окончить giữ vì có "tốt nghiệp" tách riêng.
    "кончить": "xong, kết thúc",
    # Ngoặc "(xe)" vi phạm §2c; gloss "to miss (a bus or train)" = lỡ chuyến.
    "опоздать": "đến muộn, trễ, lỡ chuyến",
    # Thiếu nghĩa "discover" mà gloss có; thêm thì cũng tách khỏi включить "mở"
    # và khỏi открыться (bản -ся không có nghĩa phát hiện).
    "открыть": "mở, khai trương, hé lộ, phát hiện",
}
