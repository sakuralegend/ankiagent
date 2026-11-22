# -*- coding: utf-8 -*-
"""k162 — people::professions (lô gộp hai trục): thân thể · đức tin/đời sống · người theo nghề.

Chỗ cần nhất quán trong lô:
(1) đuôi -ник = NGƯỜI gắn với việc/vật ấy — nói một câu ở уча́стник; сотру́дник, охра́нник,
    свяще́нник, полко́вник chỉ ghi mảnh, không lặp lời giảng.
(2) gốc хран-/хорон- = CẤT GIỮ: охра́нник (khớp охра́на, храни́ть — thẻ cũ) và по́хороны
    (хорон- là dạng Nga «оро» của хран-, như го́род ↔ -град).
(3) gốc стро- «XÂY, DỰNG» khớp стро́ить/строи́тель (thẻ cũ); -ство khớp прави́тельство.
(4) свяще́нник khớp thẻ свято́й (т→щ). зре́ние khớp зри́тель. ве́ра khớp ве́рить.
(5) коле́но → коле́ни: số nhiều -и của bộ phận đi đôi, như плечо́ → пле́чи, у́хо → у́ши.
Họ hàng cố ý vắng: карье́ра (mượn Pháp, đứng một mình).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "кожа": "da, da thuộc",                   # «;» -> «,»
    "зрение": "thị lực, thị giác",            # «mắt» là nghĩa của глаз; gloss sight/eyesight/vision
    "услуга": "dịch vụ, sự giúp đỡ",          # «;» -> «,»
}

# --------------------------------------------------------------------- губа
S["губа"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc Slav trơn — không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Số ít nhấn đuôi (<b>губа́</b>, <b>губу́</b>), nhưng số nhiều lùi lên đầu: '
    '<b>гу́бы</b>, <b>губ</b> — rồi từ cách 3 lại về đuôi: <b>губа́м</b>, <b>губа́х</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>губно́й</b> thuộc môi · <b>губна́я пома́да</b> son môi · '
    '<b>губна́я гармо́шка</b> kèn harmonica</div>'
)

# --------------------------------------------------------------------- кожа
S["кожа"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga hiện đại — coi như gốc trơn.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một từ cho cả da người lẫn da thuộc: <b>ко́жаная ку́ртка</b> áo khoác da.</div>'
    '<div class="hd-warn">⚠️ Mức tin: từ nguyên (nhiều khả năng, không phải luật) — '
    '<b>коза́</b> con dê + <b>з→ж</b> ⇒ «da dê».</div>'
    '<div class="hd-warn"><b>гуси́ная ко́жа</b> — nổi da gà (tiếng Nga nói «da NGỖNG»).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ко́жаный</b> bằng da · <b>ко́жный</b> thuộc da (bệnh da)</div>'
)

# --------------------------------------------------------------------- зрение
S["зрение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">зр-</span>'
    '<span class="hd-gloss">gốc NHÌN — như <b>зри́тель</b> khán giả</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ние</span>'
    '<span class="hd-gloss">→ danh từ: việc, khả năng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Khả năng NHÌN ⇒ thị lực: <b>плохо́е зре́ние</b> mắt kém.</div>'
    '<div class="hd-warn"><b>то́чка зре́ния</b> — quan điểm; đúng từng chữ như Anh '
    '<i>point of view</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>зри́тель</b> khán giả · <b>зри́тельный зал</b> khán phòng · '
    '<b>зре́лище</b> cảnh tượng</div>'
)

# --------------------------------------------------------------------- колено
S["колено"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc Slav trơn — không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi <b>-о</b> ⇒ giống trung, trọng âm đứng yên ở <b>-ле́-</b>.</div>'
    '<div class="hd-warn">Số nhiều (đầu gối) là <b>коле́ни</b>, cách 2 <b>коле́ней</b> — '
    'bộ phận đi đôi giữ đuôi <b>-и</b>, như <b>плечо́ → пле́чи</b>, <b>у́хо → у́ши</b>.</div>'
    '<div class="hd-warn"><b>встать на коле́ни</b> — quỳ xuống · <b>на коле́нях</b> — đang quỳ, '
    'hoặc ngồi trên đùi ai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>наколе́нник</b> miếng bảo vệ đầu gối (<b>на-</b> trên + <b>-ник</b>)</div>'
)

# --------------------------------------------------------------------- выглядеть
S["выглядеть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы́-</span>'
    '<span class="hd-gloss">RA NGOÀI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-гляд-</span>'
    '<span class="hd-gloss">NHÌN — như <b>гляде́ть</b>, <b>взгляд</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е-ть</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái phô ra ngoài cho người ta nhìn ⇒ trông có vẻ. <b>д→ж</b> chỉ ở ngôi «tôi»: '
    '<b>вы́гляжу</b>, còn lại <b>вы́глядишь</b>; <b>вы́-</b> giữ trọng âm suốt bảng.</div>'
    '<div class="hd-warn">Có <b>вы́-</b> mà vẫn là CHƯA hoàn thành, không có cặp thể.</div>'
    '<div class="hd-warn">Trông THẾ NÀO → trạng từ hoặc cách 5: <b>Ты хорошо́ вы́глядишь</b>, '
    '<b>Он вы́глядит уста́лым</b>. Trông NHƯ ai → <b>как</b>: <b>вы́глядит как врач</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гляде́ть</b> nhìn · <b>взгляд</b> cái nhìn</div>'
)

# --------------------------------------------------------------------- кость
S["кость"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc Slav trơn — không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi <b>-ь</b> ở đây là giống CÁI. Số nhiều nhảy trọng âm y hệt <b>часть</b>: '
    '<b>ко́сти</b>, nhưng <b>косте́й</b>, <b>костя́м</b>. Số nhiều <b>ко́сти</b> còn là xúc xắc.</div>'
    '<div class="hd-warn"><b>слоно́вая кость</b> — ngà voi (nghĩa đen «xương voi»).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ко́стный</b> thuộc xương · <b>ко́стный мозг</b> tủy xương</div>'
)

# --------------------------------------------------------------------- похороны
S["похороны"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố, lấy theo <b>похорони́ть</b>; không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-хорон-</span>'
    '<span class="hd-gloss">CHÔN, CẤT GIỮ — dạng Nga của <b>хран-</b> (<b>храни́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ы</span>'
    '<span class="hd-gloss">đuôi số nhiều</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cất người đã khuất vào đất ⇒ đám tang. <b>хорон-</b> ↔ <b>хран-</b> như '
    '<b>го́род</b> ↔ <b>Ленингра́д</b>: tiếng Nga chêm <b>о</b> vào cụm <b>ра</b>.</div>'
    '<div class="hd-warn">CHỈ có số nhiều: <b>По́хороны бы́ли вчера́</b>. Trọng âm nhảy: '
    '<b>по́хороны</b> → <b>похоро́н</b>, <b>похорона́м</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>хорони́ть</b> chôn cất · <b>храни́ть</b> cất giữ · '
    '<b>охра́нник</b> bảo vệ</div>'
)

# --------------------------------------------------------------------- вера
S["вера"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вер-</span>'
    '<span class="hd-gloss">TIN, THẬT — như <b>ве́рить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>ве́рить</b> tin. Cũng là tên nữ <b>Ве́ра</b> «Đức Tin».</div>'
    '<div class="hd-warn">Tin VÀO → <b>в</b> + cách 4, như động từ: <b>ве́ра в Бо́га</b>, '
    '<b>ве́ра в себя́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ве́рить</b> tin · <b>ве́рный</b> trung thành, đúng · '
    '<b>уве́ренный</b> chắc chắn · <b>дове́рие</b> sự tin cậy</div>'
)

# --------------------------------------------------------------------- участник
S["участник"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-част-</span>'
    '<span class="hd-gloss">PHẦN — <b>часть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ник</span>'
    '<span class="hd-gloss">NGƯỜI gắn với việc ấy</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người có PHẦN trong việc chung ⇒ người tham gia. Đuôi <b>-ник</b> dựng '
    'người từ một việc/vật (<b>сотру́дник</b>, <b>охра́нник</b>…); nữ thì <b>-ница</b>: '
    '<b>уча́стница</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уча́ствовать</b> tham gia · <b>уча́стие</b> sự tham gia · '
    '<b>часть</b> phần</div>'
)

# --------------------------------------------------------------------- ангел
S["ангел"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga — mượn Hy Lạp <i>ángelos</i> «sứ giả», '
    'cùng nguồn với Anh <i>angel</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhấn âm đầu như tiếng Anh: <b>а́нгел</b>. <b>а́нгел-храни́тель</b> = thiên thần '
    'hộ mệnh (<b>храни́ть</b> giữ gìn).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>а́нгельский</b> thuộc thiên thần</div>'
)

# --------------------------------------------------------------------- дьявол
S["дьявол"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga — mượn Hy Lạp <i>diábolos</i>, cùng nguồn với Anh '
    '<i>devil</i>, <i>diabolic</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>ди-</b> Hy Lạp thành <b>дья-</b>: viết <b>ь</b> trước <b>я</b>. Nghe sách vở, '
    'tôn giáo; câu chửi hằng ngày dùng <b>чёрт</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дья́вольский</b> quỷ quái</div>'
)

# --------------------------------------------------------------------- грех
S["грех"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc Slav trơn — không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thêm đuôi là trọng âm dồn xuống đuôi: <b>греха́</b>, <b>грехо́м</b>, '
    '<b>грехи́</b>. Sang tính từ thì <b>х→ш</b>: <b>гре́шный</b>.</div>'
    '<div class="hd-warn"><b>Грех жа́ловаться</b> — chẳng có gì phải than (đáp «Как дела́?»).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гре́шный</b> có tội · <b>гре́шник</b> kẻ có tội · '
    '<b>согреши́ть</b> phạm tội</div>'
)

# --------------------------------------------------------------------- услуга
S["услуга"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố, nghĩa đã mờ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-слуг-</span>'
    '<span class="hd-gloss">PHỤC VỤ — <b>слуга́</b> đầy tớ; <b>г→ж</b> trong <b>служи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một việc làm hộ người khác ⇒ sự giúp đỡ; số nhiều <b>услу́ги</b> là dịch vụ: '
    '<b>услу́ги свя́зи</b> dịch vụ viễn thông.</div>'
    '<div class="hd-warn"><b>оказа́ть услу́гу</b> — giúp một việc · <b>к ва́шим услу́гам</b> — '
    'sẵn sàng phục vụ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>служи́ть</b> phục vụ · <b>слуга́</b> đầy tớ · <b>слу́жба</b> công việc, '
    'sự phục vụ</div>'
)

# --------------------------------------------------------------------- карьера
S["карьера"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga — mượn Pháp <i>carrière</i>, cùng nguồn với Anh '
    '<i>career</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhấn <b>-ье́-</b>. Có đuôi <b>-а</b> ⇒ giống cái; khác <b>карье́р</b> '
    '(giống đực) là mỏ đá lộ thiên.</div>'
    '<div class="hd-warn"><b>сде́лать карье́ру</b> — thăng tiến, thành đạt.</div>'
)

# --------------------------------------------------------------------- полковник
S["полковник"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">полк-</span>'
    '<span class="hd-gloss">TRUNG ĐOÀN — <b>полк</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ов-ник</span>'
    '<span class="hd-gloss">NGƯỜI gắn với nó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người cầm một <b>полк</b> ⇒ đại tá. Thêm <b>под-</b> «dưới» là bậc ngay dưới: '
    '<b>подполко́вник</b> trung tá.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>полк</b> trung đoàn · <b>подполко́вник</b> trung tá</div>'
)

# --------------------------------------------------------------------- сотрудник
S["сотрудник"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">CÙNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-труд-</span>'
    '<span class="hd-gloss">LAO ĐỘNG — <b>труд</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ник</span>'
    '<span class="hd-gloss">NGƯỜI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người CÙNG lao động trong một tổ chức ⇒ nhân viên: <b>сотру́дник '
    'поли́ции</b> cán bộ cảnh sát. <b>со-</b> như trong <b>совреме́нный</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>труд</b> lao động · <b>тру́дный</b> khó · <b>сотру́дничество</b> sự hợp tác '
    '· <b>сотру́дница</b> nữ nhân viên</div>'
)

# --------------------------------------------------------------------- охранник
S["охранник"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-хран-</span>'
    '<span class="hd-gloss">CANH GIỮ — <b>охра́на</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ник</span>'
    '<span class="hd-gloss">NGƯỜI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một người của <b>охра́на</b> ⇒ nhân viên bảo vệ. Cả đội bảo vệ thì gọi '
    '<b>охра́на</b>, một người là <b>охра́нник</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>охра́на</b> sự canh gác · <b>охраня́ть</b> canh gác · '
    '<b>храни́ть</b> cất giữ · <b>сохрани́ть</b> lưu lại</div>'
)

# --------------------------------------------------------------------- священник
S["священник"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">свящ-</span>'
    '<span class="hd-gloss">THÁNH — <b>свят-</b>, <b>т→щ</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ен-</span>'
    '<span class="hd-gloss">như <b>свяще́нный</b> thiêng liêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ник</span>'
    '<span class="hd-gloss">NGƯỜI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người lo việc thiêng liêng ⇒ linh mục. Nhìn khác <b>свято́й</b> chỉ vì '
    '<b>т→щ</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>свято́й</b> thánh · <b>свяще́нный</b> thiêng liêng</div>'
)

# --------------------------------------------------------------------- строительство
S["строительство"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">стро-</span>'
    '<span class="hd-gloss">gốc XÂY, DỰNG, sắp đặt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-тель-</span>'
    '<span class="hd-gloss">NGƯỜI làm — <b>строи́тель</b> thợ xây</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ство</span>'
    '<span class="hd-gloss">→ danh từ: việc, ngành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Việc của thợ xây ⇒ việc xây dựng, ngành xây dựng. Cùng khuôn '
    '<b>прави́тель</b> người cai trị → <b>прави́тельство</b> chính phủ. Trọng âm đứng yên ở '
    '<b>-и́-</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>стро́ить</b> xây · <b>строи́тель</b> thợ xây · <b>строи́тельный</b> '
    'thuộc xây dựng · <b>стро́йка</b> công trường</div>'
)

# --------------------------------------------------------------------- лидер
S["лидер"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga — mượn thẳng Anh <i>leader</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đọc gần như tiếng Anh, nhấn âm đầu. Giống đực, nhưng dùng cho cả phụ nữ: '
    '<b>Она́ ли́дер па́ртии</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ли́дерство</b> vai trò dẫn đầu · <b>лиди́ровать</b> dẫn đầu</div>'
)

B = {
    "docbangmat": 69,   # đọc hết 69 dạng bằng mắt, đối chiếu bảng chia trên thẻ: không lệch
    "loitubat": 1,      # колено: viết «không phải коле́на» — sai một phần (коле́на là số nhiều đúng ở nghĩa «thế hệ/chi tộc») ⇒ bỏ mệnh đề
    "nguonsai": 1,      # выглядеть: từ điển ghi «+accusative if как» — sai, sau как là cách 1 (вы́глядит как врач) ⇒ không chép
    "baolen": [
        "кожа: từ nguyên коза́ → ко́жа «da dê» là của Vasmer («по-видимому»), đã gắn ⚠️ Mức tin — luồng chính duyệt có giữ không",
        "похороны: nối хорон- ↔ хран- (полногласие, như го́род ↔ -град) — chắc theo Vasmer, nhưng là từ nguyên chứ không phải luật",
        "колено: BAT THUONG của máy KHÔNG bắt số nhiều коле́ни (đuôi -и lệch quy tắc -а) — đã tự viết câu chú ý; máy có thể đang mù ca này ở thẻ khác (плечо́, у́хо)",
        "V cần duyệt: зрение «thị lực, mắt» → «thị lực, thị giác» (bỏ «mắt» vì đó là nghĩa của глаз, không có trong gloss); кожа, услуга chỉ đổi «;» → «,»",
        "карьера: cố ý bỏ mục Họ hàng (mượn Pháp, đứng một mình)",
    ],
}
