# -*- coding: utf-8 -*-
"""k202 — people::professions (lô trộn): nghề nghiệp, kinh doanh, tang lễ, họ hàng.

Chỗ cần nhất quán trong lô:
(1) хорони́ть / похорони́ть soạn THÀNH ĐÔI; хорон- ↔ хран- chẻ đúng như thẻ по́хороны đã có
    (tiếng Nga chêm о vào ра). Bảng chia (trọng âm lùi) nói ở cả hai, ngắn.
(2) Gốc Latin «chạy» (currere) chung cho курье́р và конкуре́нт — khớp thẻ ко́нкурс đã có
    («-курс CHẠY», mượn Latin, chẻ theo Latin chứ không theo Nga).
(3) инве́стор / инвести́ция dẫn chiếu nhau; trọng âm đổi chỗ giữa hai từ.
(4) потреби́тель chẻ -треб- CẦN, khớp thẻ потре́бность và употребля́ть.
(5) пра́вить chẻ прав- THẲNG, ĐÚNG — khớp thẻ пра́вило («nắn cho đúng»).
(6) христиани́н: dòng крестья́нин giữ đúng mức tin như thẻ крестья́нин đã có.
Họ hàng cố ý vắng: бровь (gốc trơn), жюри́ (từ mượn đứng một mình).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "курьер": "người giao hàng, người chuyển phát",          # bỏ «người đưa thư» = почтальо́н; gloss courier/delivery person
    "потребитель": "người tiêu dùng, người sử dụng",           # bỏ «khách hàng» = клие́нт; gloss consumer/user
    "похоронить": "chôn, mai táng, chôn vùi, che giấu",        # «dập tắt» không có trong gloss; thiếu hide/conceal
    "пра": "cụ, cố, nguyên thủy, nguyên sơ",                  # «tằng tổ» là danh từ = пра́дед, không phải tiền tố great-
    "править": "cai trị, trị vì, thống trị, cầm quyền, lái, điều khiển, sửa, biên tập",  # THIẾU steer/drive, edit/correct
    "дежурный": "trực, đang trực, thường trực, người trực, trực nhật, chiếu lệ",          # THIẾU person on duty, monitor, perfunctory
    "банкир": "chủ ngân hàng, nhà ngân hàng",                 # «nhà tài phiệt» nới rộng; gloss chỉ banker
}

# --------------------------------------------------------------------- стрижка
S["стрижка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">стриж-</span>'
    '<span class="hd-gloss">CẮT (tóc, lông) — từ <b>стричь</b>, <i>г → ж</i> trước hậu tố</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-а</span>'
    '<span class="hd-gloss">→ danh từ giống cái chỉ việc làm và kết quả của nó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Việc cắt» ⇒ cắt tóc, và cái còn lại trên đầu ⇒ kiểu tóc; với cừu ⇒ xén lông. '
    'Gốc <i>г/ж</i> lộ ngay trong bảng chia: <b>стригу́</b> tôi cắt — <b>стрижёшь</b> bạn cắt. '
    'Cách 2 số nhiều chèn <i>е</i>: <b>стри́жек</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>стричь</b> cắt (tóc) · <b>стри́чься</b> đi cắt tóc · '
    '<b>подстри́чь</b> tỉa ngắn</div>'
)

# --------------------------------------------------------------------- бровь
S["бровь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc Ấn–Âu với tiếng Anh <i>brow</i>: <i>b-r-ow</i> ↔ <i>б-р-овь</i>. '
    'Đuôi <b>-ь</b>, giống cái. Số nhiều trọng âm nhảy ra đuôi từ cách 2: '
    '<b>бро́ви</b> → <b>брове́й</b>, <b>бровя́м</b>.</div>'
    '<div class="hd-warn"><b>не в бровь, а в глаз</b> = «không trúng lông mày mà trúng mắt» ⇒ '
    'nói trúng phóc chỗ đau.</div>'
)

# --------------------------------------------------------------------- пожилой
S["пожилой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">MỘT QUÃNG — như <b>пожи́ть</b> sống một thời gian</span></div>'
    '<div class="hd-row"><span class="hd-piece">-жил-</span>'
    '<span class="hd-gloss">SỐNG — <b>жить</b>, quá khứ <b>жил</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́й</span>'
    '<span class="hd-gloss">đuôi tính từ, trọng âm ở đuôi</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đã sống được một quãng dài» ⇒ cao tuổi: <b>пожило́й челове́к</b> '
    'người lớn tuổi, <b>пожилы́е лю́ди</b> người cao tuổi.</div>'
    '<div class="hd-warn">Nói về NGƯỜI thì <b>пожило́й</b> là cách nói tế nhị; <b>ста́рый</b> '
    'nói thẳng «già», dễ chạm lòng người nghe.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>жить</b> sống · <b>жизнь</b> cuộc sống · <b>пожи́ть</b> sống một thời gian</div>'
)

# --------------------------------------------------------------------- хоронить
S["хоронить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">хорон-</span>'
    '<span class="hd-gloss">CHÔN, CẤT GIỮ — dạng Nga của <i>хран-</i> (<b>храни́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cất người đã khuất vào đất ⇒ chôn; nghĩa gốc «cất giấu» còn sống trong '
    'nghĩa che giấu. <i>хорон-</i> ↔ <i>хран-</i> như đã chẻ ở <b>по́хороны</b>. Chôn AI ở cách 4: '
    '<b>хорони́ть дру́га</b>. Trọng âm lùi từ ngôi «bạn»: <b>хороню́</b>, <b>хоро́нишь</b>, '
    '<b>хоро́нят</b>. Cặp HT: <b>похорони́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>по́хороны</b> đám tang · <b>храни́ть</b> cất giữ · '
    '<b>похорони́ть</b> (HT)</div>'
)

# --------------------------------------------------------------------- похоронить
S["похоронить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố chỉ đổi thể — không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-хорон-и́ть</span>'
    '<span class="hd-gloss">CHÔN, CẤT GIỮ — chính là <b>хорони́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vế hoàn thành của <b>хорони́ть</b>: chôn xong, trọn một lần. Chia y hệt, '
    'trọng âm lùi: <b>похороню́</b>, <b>похоро́нишь</b>. Nghĩa bóng: <b>похорони́ть наде́жды</b> '
    'chôn vùi hy vọng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>по́хороны</b> đám tang (giữ cả <i>по-</i>) · <b>хорони́ть</b> (CHT) · '
    '<b>храни́ть</b> cất giữ</div>'
)

# --------------------------------------------------------------------- христианин
S["христианин"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">Христ-</span>'
    '<span class="hd-gloss">CHÚA KITÔ — <b>Христо́с</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-иан-</span>'
    '<span class="hd-gloss">người theo — như <i>-ian</i> trong <i>Christian</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́н</span>'
    '<span class="hd-gloss">MỘT người — rụng ở số nhiều</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng khuôn <b>крестья́нин</b>: số nhiều rụng <b>-ин</b> và trọng âm lùi về '
    '<i>а</i>: <b>христиа́не</b>, cách 2 trụi đuôi: <b>христиа́н</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>Христо́с</b> Chúa Kitô · <b>христиа́нство</b> Kitô giáo · '
    '<b>христиа́нка</b> nữ tín đồ · <b>крестья́нин</b> nông dân (từ nguyên: tách ra từ chính từ này)</div>'
)

# --------------------------------------------------------------------- жюри
S["жюри"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn tiếng Pháp <i>jury</i>, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không biến cách, giống trung — như <b>кафе́</b>: <b>член жюри́</b> thành viên '
    'ban giám khảo. Sau <i>ж</i> thường viết <i>у</i>; <b>жюри́</b> là từ mượn hiếm hoi giữ <i>ю</i> '
    '(như <b>парашю́т</b>), đọc như <i>жу</i>.</div>'
    '<div class="hd-warn"><b>жюри́</b> chỉ chấm cuộc thi, liên hoan (<b>жюри́ ко́нкурса</b>). Bồi thẩm '
    'đoàn ở toà án là <b>прися́жные</b> — khác tiếng Anh <i>jury</i>.</div>'
)

# --------------------------------------------------------------------- дежурный
S["дежурный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дежу́р-</span>'
    '<span class="hd-gloss">TRỰC — mượn Pháp <i>de jour</i> «của ngày»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Người của ngày hôm nay» ⇒ trực — đúng như chữ <i>trực nhật</i> (nhật = ngày). '
    'Hay dùng thẳng làm danh từ: <b>дежу́рный</b> người trực, <b>дежу́рная</b> cô trực. Nghĩa bóng '
    '«làm cho có lệ»: <b>дежу́рная улы́бка</b> nụ cười xã giao.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дежу́рить</b> trực · <b>дежу́рство</b> ca trực, phiên trực</div>'
)

# --------------------------------------------------------------------- дизайнер
S["дизайнер"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">диза́йн</span>'
    '<span class="hd-gloss">THIẾT KẾ — mượn Anh <i>design</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ер</span>'
    '<span class="hd-gloss">NGƯỜI làm — chính là <i>-er</i> tiếng Anh</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mượn nguyên <i>designer</i>, trọng âm đúng chỗ tiếng Anh: <i>de-SIGN-er</i> → '
    '<b>диза́йнер</b>; đuôi <b>-ер</b> mượn y như <b>ме́неджер</b>. Nói về phụ nữ vẫn dùng '
    '<b>диза́йнер</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>диза́йн</b> thiết kế · <b>диза́йнерский</b> thuộc thiết kế</div>'
)

# --------------------------------------------------------------------- курьер
S["курьер"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кур-</span>'
    '<span class="hd-gloss">CHẠY — Latin <i>currere</i>, như <b>курс</b>, <b>ко́нкурс</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ьер</span>'
    '<span class="hd-gloss">NGƯỜI làm — đuôi Pháp <i>-ier</i> (<i>courrier</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mượn Latin, chẻ theo Latin: «người chạy» mang đồ đến tận tay ⇒ người giao '
    'hàng; tiếng Anh <i>courier</i> cùng gốc. Có <b>ь</b> giữa <i>р</i> và <i>е</i>: đọc tách '
    '<i>р</i> ra khỏi <i>е</i>.</div>'
    '<div class="hd-warn"><b>курье́р</b> ≠ <b>почтальо́н</b>: người đưa thư của bưu điện là '
    '<b>почтальо́н</b>; <b>курье́р</b> giao hàng, giấy tờ theo đơn — <b>курье́рская доста́вка</b> '
    'chuyển phát nhanh.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>курс</b> khoá học, hướng đi · <b>ко́нкурс</b> cuộc thi · '
    '<b>конкуре́нт</b> đối thủ cạnh tranh</div>'
)

# --------------------------------------------------------------------- банкир
S["банкир"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">банк</span>'
    '<span class="hd-gloss">NGÂN HÀNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́р</span>'
    '<span class="hd-gloss">NGƯỜI làm nghề — như <b>пассажи́р</b>, <b>команди́р</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Người của ngân hàng» theo nghĩa chủ, người cầm vốn — không phải nhân viên '
    'quầy (đó là <b>сотру́дник ба́нка</b>). Trọng âm luôn ở đuôi: <b>банки́р</b>, <b>банки́ра</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>банк</b> ngân hàng · <b>ба́нковский</b> thuộc ngân hàng · '
    '<b>банкно́та</b> tờ tiền giấy</div>'
)

# --------------------------------------------------------------------- спонсор
S["спонсор"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn tiếng Anh <i>sponsor</i>, không chẻ trong tiếng Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giữ trọng âm âm đầu như tiếng Anh: <b>спо́нсор</b>. Đuôi <b>-ор</b> giống '
    'đực, như <b>а́втор</b>. Nhà tài trợ CỦA cái gì → cách 2: <b>спо́нсор конце́рта</b> nhà tài trợ buổi hoà nhạc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>спо́нсорство</b> sự tài trợ · <b>спонси́ровать</b> tài trợ</div>'
)

# --------------------------------------------------------------------- инвестор
S["инвестор"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">инвест-</span>'
    '<span class="hd-gloss">ĐẦU TƯ — mượn <i>invest</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ор</span>'
    '<span class="hd-gloss">NGƯỜI làm — như <b>а́втор</b>, <b>дире́ктор</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><i>invest</i> + <i>-or</i> ⇒ <i>investor</i>. Trọng âm đứng ở <i>-ве́-</i>: '
    '<b>инве́стор</b>; sang <b>инвести́ция</b> thì nhảy ra <i>-ти́-</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>инвести́ция</b> khoản đầu tư · <b>инвести́ровать</b> đầu tư</div>'
)

# --------------------------------------------------------------------- конкурент
S["конкурент"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кон-</span>'
    '<span class="hd-gloss">CÙNG (Latin <i>con-</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-кур-</span>'
    '<span class="hd-gloss">CHẠY — như <b>ко́нкурс</b>, <b>курье́р</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́нт</span>'
    '<span class="hd-gloss">NGƯỜI đang làm — như <b>студе́нт</b>, <b>клие́нт</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mượn Latin, chẻ theo Latin: «người cùng chạy đua» ⇒ đối thủ cạnh tranh, '
    'nhất là trên thị trường: <b>гла́вный конкуре́нт</b> đối thủ chính.</div>'
    '<div class="hd-warn"><b>ко́нкурс</b> cuộc thi ≠ <b>конкуре́нция</b> sự cạnh tranh — cùng gốc, '
    'khác nghĩa, khác cả chỗ trọng âm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>конкуре́нция</b> sự cạnh tranh · <b>конкури́ровать</b> cạnh tranh · '
    '<b>ко́нкурс</b> cuộc thi</div>'
)

# --------------------------------------------------------------------- потребитель
S["потребитель"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố — ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-треб-</span>'
    '<span class="hd-gloss">CẦN — gốc của <b>тре́бовать</b>, <b>потре́бность</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́тель</span>'
    '<span class="hd-gloss">NGƯỜI làm việc đó — như <b>учи́тель</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ <b>потребля́ть</b> tiêu thụ: người dùng hết cái mình cần ⇒ người tiêu dùng: '
    '<b>права́ потреби́телей</b> quyền người tiêu dùng.</div>'
    '<div class="hd-warn">Khách của một cửa hàng, công ty cụ thể là <b>клие́нт</b> hay '
    '<b>покупа́тель</b>; <b>потреби́тель</b> là người tiêu dùng nói chung.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>потребля́ть</b> tiêu thụ · <b>потребле́ние</b> sự tiêu dùng · '
    '<b>потре́бность</b> nhu cầu · <b>употребля́ть</b> dùng</div>'
)

# --------------------------------------------------------------------- компенсация
S["компенсация"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">компенс-</span>'
    '<span class="hd-gloss">BÙ — Latin <i>compensare</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ция</span>'
    '<span class="hd-gloss">= <i>-ation</i> tiếng Anh → danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><i>compensation</i> → <b>компенса́ция</b>: đổi <i>-ation</i> thành <b>-ация</b>, '
    'trọng âm rơi đúng vào <i>а</i>. Bù cho CÁI GÌ: <b>за</b> + cách 4 — <b>компенса́ция за '
    'уще́рб</b> đền bù thiệt hại; trả tiền đền bù là <b>вы́платить компенса́цию</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>компенси́ровать</b> bù đắp, đền bù</div>'
)

# --------------------------------------------------------------------- инвестиция
S["инвестиция"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">инвест-</span>'
    '<span class="hd-gloss">ĐẦU TƯ — như <b>инве́стор</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ция</span>'
    '<span class="hd-gloss">→ danh từ giống cái (như <b>поли́ция</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hay dùng ở số nhiều. Đầu tư VÀO đâu: <b>в</b> + cách 4 — '
    '<b>инвести́ции в эконо́мику</b> đầu tư vào kinh tế. Trọng âm khác <b>инве́стор</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>инве́стор</b> nhà đầu tư · <b>инвести́ровать</b> đầu tư</div>'
)

# --------------------------------------------------------------------- сирота
S["сирота"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn với vốn từ hiện nay, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi <b>-а</b> nhưng là danh từ GIỐNG CHUNG: nói về con trai thì tính từ '
    'đi theo giống đực — <b>он кру́глый сирота́</b>. Số nhiều trọng âm lùi: <b>сиро́ты</b>, '
    '<b>сиро́т</b>.</div>'
    '<div class="hd-warn"><b>кру́глый сирота́</b> = mồ côi cả cha lẫn mẹ (nghĩa đen «mồ côi '
    'tròn»).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сиро́тский</b> của trẻ mồ côi · <b>осироте́ть</b> thành mồ côi</div>'
)

# --------------------------------------------------------------------- пра
S["пра"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пра-</span>'
    '<span class="hd-gloss">TIỀN TỐ: lùi thêm một đời; hoặc «gốc, đầu tiên» — không đứng một mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gắn trước từ họ hàng ⇒ lùi thêm một thế hệ: <b>ба́бушка</b> bà → '
    '<b>праба́бушка</b> cụ bà; <b>внук</b> cháu → <b>пра́внук</b> chắt. Gắn trước từ khác ⇒ '
    'nguyên thủy: <b>праязы́к</b> ngôn ngữ gốc.</div>'
    '<div class="hd-warn"><b>пра́внук</b> = <b>пра-</b> + <b>внук</b>, KHÔNG phải <i>прав-</i> '
    '(đúng, phải) + <i>-нук</i>. <i>прав-</i> của <b>пра́вда</b> là gốc khác hẳn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пра́дед</b> cụ ông · <b>пра́внучка</b> chắt gái · '
    '<b>пра́родина</b> quê tổ</div>'
)

# --------------------------------------------------------------------- править
S["править"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">прав-</span>'
    '<span class="hd-gloss">THẲNG, ĐÚNG — như <b>пра́вило</b>, <b>пра́вый</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Nắn cho thẳng, cho đúng»: nắn câu chữ ⇒ sửa, biên tập (+ cách 4: '
    '<b>пра́вить текст</b>); nắn hướng đi ⇒ lái; nắn cả nước ⇒ cai trị (+ cách 5: '
    '<b>пра́вить страно́й</b>). Ngôi «tôi» chèn <i>л</i>: <b>пра́влю</b>, <b>пра́вишь</b>. '
    'Sửa xong (HT) thì dùng <b>испра́вить</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>прави́тельство</b> chính phủ · <b>управля́ть</b> điều hành · '
    '<b>испра́вить</b> sửa cho đúng · <b>отпра́вить</b> gửi đi</div>'
)

B = {
    "docbangmat": 64,
    "loitubat": 5,
    "nguonsai": 5,
    "baolen": [
        "NGUỒN CÓ VẤN ĐỀ — пра: không phải một từ mà là TIỀN TỐ (chỉ sống trong праба́бушка, пра́внук, праязы́к…); thẻ không có từ loại (pos rỗng ⇒ mặt đề không có badge); gloss trộn thêm «Pra (river)» là tên riêng một con sông, không liên quan. Tôi soạn thẻ như một thẻ tiền tố + V «cụ, cố, nguyên thủy, nguyên sơ» (bỏ «tằng tổ» — đó là danh từ = пра́дед). User quyết có giữ thẻ này không.",
        "Va chạm đã gỡ từ phía k202, không cắt nghĩa chính: курье́р bỏ «người đưa thư» (= почтальо́н k67) ⇒ «người giao hàng, người chuyển phát»; потреби́тель bỏ «khách hàng» (= клие́нт k71) ⇒ «người tiêu dùng, người sử dụng». Hai thẻ đã nạp không đụng. Mô phỏng do_va_cham với V áp vào (đọc Anki, không ghi): 0 va chạm dính từ k202.",
        "V cần duyệt (7): курьер, потребитель (dòng trên) · похоронить («dập tắt» không có trong gloss ⇒ thay bằng «che giấu» — gloss hide/conceal; giờ trùng y хоронить, badge thể tách) · пра (dòng 1) · править (THIẾU lái, điều khiển — steer/drive; sửa, biên tập — edit/correct/proofread) · дежурный (THIẾU người trực, trực nhật, chiếu lệ — person on duty / school monitor / perfunctory) · банкир («nhà tài phiệt ngân hàng» nới rộng ⇒ «nhà ngân hàng»).",
        "Nguồn sai đã bác (5): (a) пра vi «tằng tổ»; (b) CACH DUNG компенсация viết sai chính tả «компенсанцию» — thẻ dùng đúng компенса́цию; (c) BAT THUONG дежурный gọi dạng ngắn дежу́рен là bất thường — thật ra chèn е đúng khuôn ва́жный→ва́жен, và dạng ngắn từ này gần như không dùng ⇒ không viết câu chú ý; (d) похоронить vi «dập tắt»; (e) банкир vi «tài phiệt». (курьер/потребитель luồng chính đã chỉ sẵn, không đếm.)",
        "Lỗi tự bắt (5): пожило́й ô đỏ nói quá «ста́рый nghe như già khọm, để dành cho đồ vật» ⇒ hạ xuống «nói thẳng, dễ chạm lòng»; христиани́н mảnh chẻ đánh dấu trọng âm -иа́н- sai với dạng số ít ⇒ bỏ dấu; диза́йнер câu «giữ trọng âm như tiếng Anh, cùng khuôn ме́неджер» lẫn lộn (ме́неджер nhấn âm đầu) ⇒ viết lại; курье́р chẻ sai курь-/-е́р ⇒ кур- (Latin currere) + -ьер (đuôi Pháp -ier); инвести́ция «hầu như chỉ số nhiều» nói quá ⇒ «hay dùng số nhiều».",
        "Không chắc (đã viết, mức tin vừa–cao): дежу́рный ← Pháp de jour (từ nguyên chuẩn, không ghi Mức tin); бровь ↔ brow cùng gốc Ấn–Âu; dòng họ hàng крестья́нин ở thẻ христиани́н ghi «(từ nguyên: …)» khớp mức tin ⚠️ trên thẻ крестья́нин đã có; trọng âm пра́родина (theo trí nhớ, nouns.csv không có từ này nên chưa máy nào kiểm).",
        "Họ hàng cố ý vắng: бровь (gốc trơn), жюри́ (từ mượn Pháp đứng một mình). Máy báo oan đã bỏ qua: жило́й, ба́нка, вести́, пе́нсия.",
    ],
}
