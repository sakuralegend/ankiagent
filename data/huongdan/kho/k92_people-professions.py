# -*- coding: utf-8 -*-
"""k92 — people-professions: 17 từ mới (đợt A1 TRKI), KHÔNG cùng một trục — soạn từng thẻ độc lập.

Chỗ cần nhất quán trong lô:
(1) khớp lô cũ: го́род «RÀO lại» (k37) · па́мять gốc мн- (k83) · преподава́тель пре-по-да-ва-тель (k36)
    · фут-/-бол (k08) · экску́рсия экс-/курс (k73) · хозя́йка/хозя́ин -ин (k91) · -ме́н = man (k91 бизнесме́н);
(2) фило́лог / фило́соф: chung mảnh фило- «yêu», khác mảnh sau (-лог lời · -соф minh triết);
(3) -и́ст (футболи́ст) là khuôn NGƯỜI mượn, -тель (преподава́тельница) là khuôn thuần Nga.
Bẫy họ hàng đã gạt: -во́д của экскурсово́д KHÔNG phải вода́ «nước»; кафе́ ≠ ко́фе (giống khác nhau).
"""

S = {}

# ---------------------------------------------------------------- аптека
S["аптека"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ bằng phụ tố Nga: mượn Hy Lạp <i>apothḗkē</i> «kho cất đồ» '
    '(qua tiếng Đức <i>Apotheke</i>) — cùng gốc tiếng Anh <i>apothecary</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mảnh <b>-те́ка</b> = KHO, chỗ cất — gặp lại trong <b>библиоте́ка</b> '
    '(kho sách), <b>дискоте́ка</b>. Hiệu thuốc là «kho thuốc». Đuôi <b>-а</b> ⇒ giống cái: '
    '<b>в апте́ке</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>апте́чка</b> hộp thuốc cấp cứu, tủ thuốc gia đình · '
    '<b>апте́карь</b> dược sĩ (cổ)</div>'
)

# ------------------------------------------------------------- городской
S["городской"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">город-</span>'
    '<span class="hd-gloss">THÀNH PHỐ (gốc: khoảnh đất RÀO lại)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ск-</span>'
    '<span class="hd-gloss">THUỘC VỀ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́й</span>'
    '<span class="hd-gloss">đuôi tính từ mang trọng âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>го́род</b> + <b>-ск-</b> = «thuộc thành phố»: <b>городско́й '
    'тра́нспорт</b> giao thông công cộng trong thành phố. Trọng âm rời <b>го́-</b>, nhảy ra '
    'đuôi <b>-о́й</b> và nằm đó suốt bảng.</div>'
    '<div class="hd-why">Tính từ «thuộc về» kiểu <b>-ский</b> chỉ phân loại, không đo mức độ ⇒ '
    'không có dạng ngắn, không có so sánh hơn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>го́род</b> thành phố · <b>горожа́нин</b> thị dân · '
    '<b>при́город</b> ngoại ô</div>'
)

# ----------------------------------------------------------- домохозяйка
S["домохозяйка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дом-о-</span>'
    '<span class="hd-gloss">NHÀ + nguyên âm nối</span></div>'
    '<div class="hd-row"><span class="hd-piece">-хозя́й-</span>'
    '<span class="hd-gloss">CHỦ (như <b>хозя́ин</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">người NỮ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ghép nguyên hai từ: <b>дом</b> + <b>хозя́йка</b> = «bà chủ của cái '
    'nhà» → người ở nhà lo việc nhà, không đi làm. Trọng âm giữ đúng chỗ của <b>хозя́йка</b>.</div>'
    '<div class="hd-why">Số nhiều cách 2 (và cách 4) <b>й</b> biến thành <b>е</b>: '
    '<b>домохозя́ек</b> — y như <b>хозя́йка → хозя́ек</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>хозя́йка</b> bà chủ · <b>хозя́ин</b> ông chủ · '
    '<b>хозя́йство</b> việc nhà · <b>дом</b> nhà</div>'
)

# --------------------------------------------------------------- историк
S["историк"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">истор-</span>'
    '<span class="hd-gloss">LỊCH SỬ (gốc Hy Lạp, như <b>исто́рия</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ик</span>'
    '<span class="hd-gloss">NGƯỜI làm ngành đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cắt đuôi ngành <b>-ия</b>, gắn đuôi người <b>-ик</b>: '
    '<b>исто́рия → исто́рик</b>, y như <b>хи́мия → хи́мик</b>. Trọng âm đứng yên ở '
    '<b>-то́-</b>. Giống đực, dùng cho cả phụ nữ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>исто́рия</b> lịch sử, câu chuyện · <b>истори́ческий</b> thuộc '
    'lịch sử (trọng âm nhảy sang <b>-ри́-</b>)</div>'
)

# ------------------------------------------------------------------ кафе
S["кафе"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn thẳng tiếng Pháp <i>café</i>, trọng âm cuối '
    'như tiếng Pháp.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giống trung và KHÔNG biến cách — mọi cách, cả số nhiều, đều là '
    '<b>кафе́</b>: <b>в кафе́</b>, <b>из кафе́</b>, <b>два кафе́</b>.</div>'
    '<div class="hd-warn">Đừng lẫn với <b>ко́фе</b> = cà phê (đồ uống): trọng âm ĐẦU, và là '
    'giống ĐỰC — <b>чёрный ко́фе</b>. Quán là <b>кафе́</b>, thứ uống là <b>ко́фе</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ко́фе</b> cà phê (cùng gốc xa) · <b>кафете́рий</b> quán ăn tự '
    'phục vụ</div>'
)

# -------------------------------------------------------------- памятник
S["памятник"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">па́мят-</span>'
    '<span class="hd-gloss">TRÍ NHỚ (<b>па́мять</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ник</span>'
    '<span class="hd-gloss">VẬT gắn với cái đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Vật dựng lên để giữ trí nhớ» → tượng đài, đài tưởng niệm, cả bia '
    'mộ. Trọng âm giữ nguyên chỗ của <b>па́мять</b>.</div>'
    '<div class="hd-warn">Tượng đài của AI thì người đó ở cách 3 (dựng «cho» ai): '
    '<b>па́мятник Пу́шкину</b>. Còn cách 2 là «di tích»: <b>па́мятник архитекту́ры</b> di tích '
    'kiến trúc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>па́мять</b> trí nhớ, kỷ niệm · <b>по́мнить</b> nhớ · '
    '<b>па́мятный</b> đáng nhớ</div>'
)

# ----------------------------------------------------------- поликлиника
S["поликлиника"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">поли-</span>'
    '<span class="hd-gloss">nay hiểu là NHIỀU (nhiều chuyên khoa)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-кли́ник-а</span>'
    '<span class="hd-gloss">PHÒNG KHÁM (<b>кли́ника</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Phòng khám nhiều khoa» — khớp đúng chữ «đa khoa». Trọng âm giữ chỗ '
    'của <b>кли́ника</b>: <b>в поликли́нике</b>.</div>'
    '<div class="hd-warn">Khám xong rồi VỀ. Nằm lại điều trị là <b>больни́ца</b> (bệnh '
    'viện).</div>'
    '<div class="hd-warn">⚠️ Mức tin: từ nguyên. Tiếng Đức <i>Poliklinik</i> được cho là từ '
    'Hy Lạp <i>polis</i> «thành phố» (phòng khám của thành phố); cách hiểu «nhiều» đến sau.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кли́ника</b> phòng khám, bệnh viện chuyên khoa</div>'
)

# --------------------------------------------------------------- полиция
S["полиция"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">полиц-</span>'
    '<span class="hd-gloss">gốc Hy Lạp <i>polis</i> «thành bang» → việc giữ trật tự</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ия</span>'
    '<span class="hd-gloss">đuôi danh từ mượn ⇒ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc tiếng Anh <i>police</i>, <i>politics</i>. Đuôi <b>-ия</b>: '
    'cách 3 và cách 6 là <b>-ии</b> — <b>в поли́ции</b>. Từ 1917 tới 2011 lực lượng này ở '
    'Nga tên là <b>мили́ция</b>.</div>'
    '<div class="hd-warn"><b>поли́ция</b> là cả LỰC LƯỢNG. Một viên cảnh sát là '
    '<b>полице́йский</b> — biến cách như tính từ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>полице́йский</b> viên cảnh sát; thuộc cảnh sát · '
    '<b>поли́тика</b> chính trị</div>'
)

# ----------------------------------------------------- преподавательница
S["преподавательница"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">преподава́тель-</span>'
    '<span class="hd-gloss">GIẢNG VIÊN (пре-по- truyền sang · -да- trao · -ва- đều đặn · '
    '-тель người)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ниц-а</span>'
    '<span class="hd-gloss">bản NỮ của đuôi <b>-тель</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>-тель → -тельница</b> là khuôn cố định: <b>учи́тель → '
    'учи́тельница</b>, <b>писа́тель → писа́тельница</b>. Trọng âm giữ ở <b>-ва́-</b>.</div>'
    '<div class="hd-why">Như <b>преподава́тель</b>: dạy ở đại học, hoặc dạy một môn cho người '
    'lớn; cô giáo phổ thông là <b>учи́тельница</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>преподава́тель</b> giảng viên · <b>преподава́ть</b> giảng dạy · '
    '<b>учи́тельница</b> cô giáo</div>'
)

# ----------------------------------------------------------------- район
S["район"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn tiếng Pháp <i>rayon</i> «tia, bán kính» — cùng '
    'gốc tiếng Anh <i>ray</i>, <i>radius</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Vùng trong một bán kính» → quận, khu vực. Giống đực, trọng âm đứng '
    'yên ở <b>-о́н</b>: <b>в райо́не</b>, <b>райо́ны</b>.</div>'
    '<div class="hd-warn"><b>в райо́не</b> + cách 2 = «quanh khu, gần»: <b>в райо́не '
    'вокза́ла</b> quanh khu nhà ga.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>микрорайо́н</b> tiểu khu dân cư · <b>райо́нный</b> thuộc quận</div>'
)

# ------------------------------------------------------------- спортсмен
S["спортсмен"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">спорт-с-</span>'
    '<span class="hd-gloss">THỂ THAO (mượn <i>sport-s-</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ме́н</span>'
    '<span class="hd-gloss"><i>man</i> — người (như <b>бизнесме́н</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mượn nguyên cụm tiếng Anh <i>sportsman</i>, giữ cả chữ <b>с</b> ở '
    'giữa. Trọng âm nằm ở <b>-ме́н</b> suốt bảng: <b>спортсме́ны</b>.</div>'
    '<div class="hd-warn">Vận động viên là người THI ĐẤU. Người đi cổ vũ là '
    '<b>боле́льщик</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>спортсме́нка</b> nữ vận động viên · <b>спорт</b> thể thao · '
    '<b>спорти́вный</b> thuộc thể thao</div>'
)

# ----------------------------------------------------------- талантливый
S["талантливый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">тала́нт-</span>'
    '<span class="hd-gloss">TÀI NĂNG (<b>тала́нт</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лив-</span>'
    '<span class="hd-gloss">CÓ NHIỀU, mang đặc tính đó</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Mang đầy tài năng». Cùng khuôn <b>-ливый</b> với '
    '<b>счастли́вый</b> (hạnh phúc), <b>терпели́вый</b> (kiên nhẫn). Tiếng Anh <i>talent</i> '
    'cùng gốc.</div>'
    '<div class="hd-why">Đều đặn, trọng âm đứng yên: dạng ngắn <b>тала́нтлив</b>, '
    '<b>тала́нтлива</b>; trạng từ <b>тала́нтливо</b> một cách tài tình.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тала́нт</b> tài năng, người có tài</div>'
)

# --------------------------------------------------------------- филолог
S["филолог"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">фило-</span>'
    '<span class="hd-gloss">YÊU (Hy Lạp <i>phílos</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лог</span>'
    '<span class="hd-gloss">LỜI, chữ → người nghiên cứu</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Người yêu chữ nghĩa» → người nghiên cứu ngôn ngữ và văn học. '
    '<b>-лог</b> là NGƯỜI, <b>-ло́гия</b> là NGÀNH: <b>био́лог / биоло́гия</b>, '
    '<b>психо́лог / психоло́гия</b>.</div>'
    '<div class="hd-warn">Trọng âm nhảy khi đổi người ↔ ngành: <b>фило́лог</b> nhưng '
    '<b>филоло́гия</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>филоло́гия</b> ngữ văn học · <b>филологи́ческий</b> thuộc ngữ '
    'văn · <b>фило́соф</b> triết gia (cùng <b>фило-</b>)</div>'
)

# --------------------------------------------------------------- философ
S["философ"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">фило-</span>'
    '<span class="hd-gloss">YÊU (Hy Lạp <i>phílos</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-соф</span>'
    '<span class="hd-gloss">MINH TRIẾT (Hy Lạp <i>sophía</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Người yêu sự minh triết» — y hệt tiếng Anh <i>philosopher</i>. '
    'Cùng mảnh đầu với <b>фило́лог</b>, khác mảnh sau: <b>-лог</b> chữ nghĩa, <b>-соф</b> '
    'minh triết.</div>'
    '<div class="hd-warn">Trọng âm nhảy khi sang ngành: <b>фило́соф</b> nhưng '
    '<b>филосо́фия</b>, <b>филосо́фский</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>филосо́фия</b> triết học · <b>филосо́фский</b> thuộc triết học</div>'
)

# ------------------------------------------------------------ футболист
S["футболист"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">фут-бол-</span>'
    '<span class="hd-gloss">BÓNG ĐÁ (<i>foot</i> + <i>ball</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ст</span>'
    '<span class="hd-gloss">NGƯỜI theo môn/nghề đó (khuôn mượn)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>футбо́л</b> + <b>-и́ст</b>; trọng âm rời <b>-бо́л</b>, nhảy sang '
    '<b>-и́ст</b>. Cùng khuôn: <b>хоккеи́ст</b>, <b>тенниси́ст</b>, <b>программи́ст</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>футбо́л</b> bóng đá · <b>футбо́льный</b> thuộc bóng đá · '
    '<b>футболи́стка</b> nữ cầu thủ</div>'
)

# --------------------------------------------------------------- чемпион
S["чемпион"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn tiếng Pháp/Anh <i>champion</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trọng âm ở <b>-о́н</b> và đứng yên: <b>чемпио́на</b>, '
    '<b>чемпио́ны</b>. <b>чемпио́н ми́ра</b> = nhà vô địch thế giới.</div>'
    '<div class="hd-warn">Người thắng là <b>чемпио́н</b>; còn GIẢI ĐẤU là '
    '<b>чемпиона́т</b> — <b>чемпиона́т ми́ра</b> giải vô địch thế giới.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>чемпиона́т</b> giải vô địch · <b>чемпио́нка</b> nữ vô địch</div>'
)

# ----------------------------------------------------------- экскурсовод
S["экскурсовод"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">экскурс-о-</span>'
    '<span class="hd-gloss">CHUYẾN THAM QUAN (<b>экску́рсия</b>) + nguyên âm nối</span></div>'
    '<div class="hd-row"><span class="hd-piece">-во́д</span>'
    '<span class="hd-gloss">người DẪN (<b>води́ть</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Người dẫn chuyến tham quan». Trọng âm dồn về <b>-во́д</b> và đứng '
    'yên: <b>экскурсово́ды</b>. Nói ngắn hơn thì là <b>гид</b>.</div>'
    '<div class="hd-warn">Mảnh <b>-во́д</b> ở đây là DẪN, không dính gì tới <b>вода́</b> '
    '(nước).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>экску́рсия</b> chuyến tham quan · <b>води́ть</b> dẫn, lái xe</div>'
)

V = {
    # Bỏ «cô giáo» — trùng учительница (k35, cùng n FEM); phía mình rút gọn. Gloss teacher/lecturer.
    "преподавательница": "giáo viên nữ, giảng viên nữ",
    # Thêm nghĩa tombstone/headstone/gravestone mà gloss có (памятник trên mộ).
    "памятник": "tượng đài, đài tưởng niệm",
}
