# -*- coding: utf-8 -*-
"""k114 — places-position: 19 từ B1 lẫn chủ đề (cơ thể, nghề, trừu tượng) — soạn từng thẻ độc lập.

Tên topic không phải trục. Không khối hệ thống. Chỗ cần nhất quán trong lô:
(1) gốc giữ đúng cách chẻ của thẻ cũ: мёртвый ↔ смерть/умереть (-мерт-/-мер-),
    отношение ↔ носить (нос-/нош-), путь ↔ путешествовать, сторона ↔ страна, вокруг ↔ круг;
(2) giống động vật ăn vào cách 4: член, детектив — người thì cách 4 = cách 2, vật/sách thì = cách 1;
(3) где-то chỉ dẫn chiếu phép so -то ↔ -нибудь đã trải ở thẻ кто́-то (k110).
Họ hàng cố ý vắng: доктор (mượn Latinh đứng một mình; phái sinh duy nhất là thuật ngữ học vị).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa, ngăn bằng dấu phẩy.
V = {
    "взгляд": "cái nhìn, quan điểm",
    "мёртвый": "đã chết, vô hồn",
    "отношение": "quan hệ, thái độ",
    "советский": "Xô viết, thuộc Liên Xô",
    "детектив": "thám tử, truyện trinh thám, phim trinh thám",
    "труд": "lao động, công sức",
    "доктор": "bác sĩ, tiến sĩ",
    "операция": "ca mổ, ca phẫu thuật, chiến dịch, giao dịch",
    "сон": "giấc ngủ, giấc mơ",
    "область": "tỉnh, vùng, lĩnh vực",
    "сторона": "phía, bên, mặt",
    "обратно": "trở lại, ngược lại",
    "где-то": "ở đâu đó",
    "путь": "con đường, lối đi, hành trình",
}

# ------------------------------------------------------------------ взгляд
S["взгляд"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вз-</span>'
    '<span class="hd-gloss">LÊN, hướng tới</span></div>'
    '<div class="hd-row"><span class="hd-piece">-гляд</span>'
    '<span class="hd-gloss">NHÌN — gốc của <b>гляде́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đưa mắt hướng tới» ⇒ cái nhìn, ánh mắt. Rồi trượt sang «cách nhìn» ⇒ '
    'quan điểm — đúng như tiếng Anh <i>view</i> và tiếng Việt «góc nhìn».</div>'
    '<div class="hd-warn"><b>На мой взгля́д</b> = theo tôi (mở đầu ý kiến) · '
    '<b>с пе́рвого взгля́да</b> = ngay từ cái nhìn đầu tiên.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гляде́ть</b> nhìn · <b>взгляну́ть</b> liếc nhìn · '
    '<b>вы́глядеть</b> trông có vẻ · <b>огляну́ться</b> ngoái lại nhìn</div>'
)

# -------------------------------------------------------------------- тело
S["тело"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">тел-</span>'
    '<span class="hd-gloss">THÂN, khối cơ thể</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cả khối thân người; trong tin tức còn là «thi thể». Số nhiều trọng âm '
    'nhảy ra đuôi: <b>тела́</b>, cách 2 <b>тел</b>.</div>'
    '<div class="hd-warn">⚠️ <b>теле-</b> trong <b>телефо́н</b>, <b>телеви́зор</b> KHÔNG phải '
    '<b>те́ло</b> — đó là gốc Hy Lạp «xa». Chỉ trùng mặt chữ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>теле́сный</b> thuộc thân thể · <b>телосложе́ние</b> vóc dáng</div>'
)

# ------------------------------------------------------------------- кровь
S["кровь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc Slav trơn — không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giống CÁI đuôi <b>-ь</b> (như <b>ночь</b>). «Trong máu» có dạng riêng '
    'nhấn đuôi: <b>в крови́</b>, nhưng «về máu» vẫn là <b>о кро́ви</b>. Hầu như chỉ dùng số ít.</div>'
    '<div class="hd-warn">⚠️ Đừng nối với <b>крова́ть</b> (giường) — từ mượn Hy Lạp, chỉ trùng '
    'mặt chữ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>крова́вый</b> đẫm máu · <b>кровотече́ние</b> sự chảy máu '
    '(máu + <b>течь</b> chảy)</div>'
)

# ----------------------------------------------------------------- мёртвый
S["мёртвый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мёрт-</span>'
    '<span class="hd-gloss">CHẾT — gốc <b>мер-</b> của <b>умере́ть</b>, <b>смерть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-в-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Ở trạng thái đã chết». <b>ё</b> chỉ đứng được khi mang trọng âm; trọng '
    'âm rời đi là thành <b>е</b>. Dạng ngắn: <b>мёртв</b> · <b>мертва́</b> · <b>мёртвы</b> — '
    'riêng giống cái nhấn đuôi.</div>'
    '<div class="hd-warn">«Anh ấy chết rồi» người Nga nói bằng động từ: <b>Он у́мер</b>. '
    '<b>мёртвый</b> là tính từ tả trạng thái: <b>мёртвая тишина́</b> im lặng chết chóc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>смерть</b> cái chết · <b>умере́ть</b> / <b>умира́ть</b> chết · '
    '<b>мертве́ц</b> người chết</div>'
)

# --------------------------------------------------------------- отношение
S["отношение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">RỜI chỗ này, đưa sang chỗ khác</span></div>'
    '<div class="hd-row"><span class="hd-piece">-нош-</span>'
    '<span class="hd-gloss">MANG — gốc <b>нос-</b>/<b>нош-</b> của <b>носи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>относи́ться к</b> «đưa mình sang phía» ai ⇒ đối xử, có thái '
    'độ. Nên «thái độ VỚI» = <b>отноше́ние к</b> + cách 3: <b>отноше́ние к рабо́те</b>. Tiếng Anh '
    '<i>relation</i> cũng dựng từ «mang» (Latinh <i>re-latus</i> «mang về»).</div>'
    '<div class="hd-warn">Số nhiều <b>отноше́ния</b> = QUAN HỆ giữa người với người: '
    '<b>У нас хоро́шие отноше́ния</b>. Số ít thường là THÁI ĐỘ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>относи́ться</b> đối xử, có liên quan · <b>носи́ть</b> mang · '
    '<b>относи́тельно</b> tương đối</div>'
)

# --------------------------------------------------------------- советский
S["советский"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сове́т-</span>'
    '<span class="hd-gloss">HỘI ĐỒNG — chính là <b>сове́т</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ск-ий</span>'
    '<span class="hd-gloss">đuôi tính từ «thuộc về»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>сове́т</b> vừa là lời khuyên vừa là HỘI ĐỒNG (nơi ngồi lại bàn). Nhà nước '
    'sau 1917 dựng trên các hội đồng ⇒ «thuộc hội đồng» = Xô viết. Tiếng Anh <i>Soviet</i> mượn '
    'thẳng từ này.</div>'
    '<div class="hd-warn">Viết THƯỜNG giữa câu: <b>сове́тский фильм</b>. Chỉ hoa khi mở đầu tên '
    'riêng: <b>Сове́тский Сою́з</b> Liên Xô.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сове́т</b> lời khuyên, hội đồng · <b>сове́товать</b> / '
    '<b>посове́товать</b> khuyên</div>'
)

# -------------------------------------------------------------------- член
S["член"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc Slav trơn — không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc là CHI, KHỚP của cơ thể: bộ phận của thân → bộ phận của nhóm ⇒ '
    'thành viên. Tiếng Anh <i>member</i> đi đúng đường đó (Latinh <i>membrum</i> = chân tay). '
    'Thường kèm cách 2: <b>член кома́нды</b> thành viên đội.</div>'
    '<div class="hd-warn">Chỉ NGƯỜI thì cách 4 = cách 2 (<b>чле́на</b>, <b>чле́нов</b>); chỉ thành '
    'phần, bộ phận thì cách 4 = cách 1 (<b>член</b>). Đứng trơn một mình trong khẩu ngữ dễ bị '
    'hiểu là «của quý» — nên nói kèm nhóm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>чле́нство</b> tư cách thành viên · <b>чле́нский</b> thuộc thành viên '
    '(<b>чле́нский взнос</b> hội phí)</div>'
)

# ---------------------------------------------------------------- детектив
S["детектив"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn tiếng Anh <i>detective</i> (Latinh <i>detegere</i> «gỡ lớp che» → '
    'phát hiện). Không chẻ trong tiếng Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Như tiếng Anh, nhấn âm cuối: <b>детекти́в</b>. Nghĩa thứ hai rất hay gặp: '
    'TRUYỆN / PHIM TRINH THÁM — <b>люблю́ чита́ть детекти́вы</b>.</div>'
    '<div class="hd-warn">Hai nghĩa tách nhau ở cách 4: người thì <b>ви́жу детекти́ва</b> '
    '(= cách 2), sách thì <b>чита́ю детекти́в</b> (= cách 1).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>детекти́вный</b> trinh thám (<b>детекти́вный рома́н</b>)</div>'
)

# -------------------------------------------------------------------- труд
S["труд"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc Slav trơn — không chẻ được. Chính là mảnh <b>труд-</b> trong '
    '<b>тру́дный</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Việc đòi CÔNG SỨC ⇒ <b>тру́дный</b> khó. Khác <b>рабо́та</b> (việc làm, chỗ '
    'làm): <b>труд</b> là sức lao động bỏ ra, nghe trang trọng hơn. Mọi dạng có đuôi đều nhấn '
    'đuôi: <b>труда́</b>, <b>труду́</b>.</div>'
    '<div class="hd-warn"><b>с трудо́м</b> = khó khăn lắm mới: <b>Я с трудо́м по́нял</b> — tôi '
    'khó khăn lắm mới hiểu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тру́дный</b> khó · <b>тру́дно</b> khó (trạng từ) · <b>сотру́дник</b> '
    'nhân viên, đồng nghiệp (người CÙNG lao động) · <b>трудолюби́вый</b> chăm chỉ</div>'
)

# ------------------------------------------------------------------ доктор
S["доктор"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn Latinh <i>doctor</i> «người dạy» (<i>docēre</i> dạy) — cùng nguồn '
    'với <b>докуме́нт</b>. Không chẻ trong tiếng Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người học vị cao nhất ⇒ TIẾN SĨ (<b>до́ктор нау́к</b>); dân gian gọi luôn '
    'thầy thuốc như thế ⇒ bác sĩ. Số nhiều đuôi <b>-а́</b> nhấn cuối như <b>дом</b> → '
    '<b>дома́</b>: <b>доктора́</b>, <b>докторо́в</b>.</div>'
    '<div class="hd-warn">Gọi thẳng bác sĩ thì «<b>До́ктор</b>, …». Nói về NGHỀ thì dùng '
    '<b>врач</b>: <b>Она́ врач</b>.</div>'
)

# ---------------------------------------------------------------- операция
S["операция"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">опер-</span>'
    '<span class="hd-gloss">LÀM, công việc — Latinh <i>opus</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ация</span>'
    '<span class="hd-gloss">= <i>-ation</i> tiếng Anh, danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>operation</i>. Đuôi <b>-ация</b> ↔ <i>-ation</i> mở khoá cả lớp '
    'từ, luôn giống cái: <b>информа́ция</b>, <b>ситуа́ция</b>. Đời thường nghĩa đầu tiên là CA MỔ.</div>'
    '<div class="hd-warn">Mổ cho ai = <b>сде́лать опера́цию</b> + cách 3: <b>Ему́ сде́лали '
    'опера́цию</b> — anh ấy được mổ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>о́пера</b> nhạc kịch (cùng gốc <i>opus</i> «tác phẩm») · '
    '<b>опери́ровать</b> mổ · <b>опера́тор</b> người vận hành</div>'
)

# --------------------------------------------------------------------- сон
S["сон"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сон / сн-</span>'
    '<span class="hd-gloss">GIẤC NGỦ — <b>о</b> rụng khi có đuôi</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một từ hai nghĩa: giấc ngủ VÀ giấc mơ. Nguyên âm chạy: <b>сна</b>, '
    '<b>сну</b>, <b>во сне</b> (trong mơ), <b>пе́ред сном</b> trước khi ngủ. Theo từ nguyên cùng '
    'gốc xa với <b>спать</b> và Latinh <i>somnus</i> (<i>insomnia</i>).</div>'
    '<div class="hd-warn">«Tôi mơ thấy» = <b>мне сни́тся</b> (người mơ ở cách 3): <b>Мне сни́лся '
    'стра́нный сон</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>спать</b> ngủ · <b>сни́ться</b> hiện ra trong mơ · '
    '<b>бессо́нница</b> chứng mất ngủ</div>'
)

# ----------------------------------------------------------------- область
S["область"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">QUANH, bao trọn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ласть</span>'
    '<span class="hd-gloss">gốc của <b>власть</b> QUYỀN CAI QUẢN, đã rụng <b>в</b></span></div>'
    '<div class="hd-warn">⚠️ Mức tin: chẻ theo từ nguyên — mắt thường không còn thấy <b>в</b>, '
    'dùng để nhớ, không phải luật suy ra được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Vùng đất dưới một quyền cai quản» ⇒ tỉnh: <b>Моско́вская о́бласть</b>. '
    'Nghĩa bóng: lĩnh vực — <b>в о́бласти медици́ны</b>. Số nhiều từ cách 2 nhấn đuôi: '
    '<b>областе́й</b>, <b>областя́х</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>власть</b> quyền lực, chính quyền · <b>областно́й</b> thuộc tỉnh</div>'
)

# ------------------------------------------------------------------ тюрьма
S["тюрьма"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn rất cổ — không chẻ trong tiếng Nga.</div>'
    '<div class="hd-warn">⚠️ Mức tin: thường được cho là từ tiếng Đức cổ <i>turm</i> «tháp» '
    '(ngục xưa đặt trong tháp); đường mượn cụ thể chưa chắc.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giống cái, nhấn đuôi <b>тюрьма́</b>; sang số nhiều trọng âm lùi về thân '
    '<b>тю́рьмы</b>, cách 2 chen <b>е</b>: <b>тю́рем</b>. Ở tù = <b>сиде́ть в тюрьме́</b>, bị bỏ '
    'tù = <b>попа́сть в тюрьму́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тюре́мный</b> thuộc nhà tù</div>'
)

# ----------------------------------------------------------------- сторона
S["сторона"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сторон-</span>'
    '<span class="hd-gloss">PHÍA, BÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng một từ với <b>страна́</b>: <b>сторона́</b> là dạng Nga thuần, '
    '<b>страна́</b> là dạng Slav nhà thờ gọn lại — «phía bên kia» thành «xứ sở». Trọng âm chạy: '
    'cách 4 <b>сто́рону</b>, số nhiều <b>сто́роны</b>, <b>сторо́н</b>.</div>'
    '<div class="hd-warn"><b>с одно́й стороны́… с друго́й стороны́</b> = một mặt… mặt khác.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>страна́</b> đất nước · <b>сторо́нник</b> người ủng hộ (đứng về phía) · '
    '<b>посторо́нний</b> người ngoài</div>'
)

# ------------------------------------------------------------------ вокруг
S["вокруг"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">во-</span>'
    '<span class="hd-gloss">TRONG — giới từ <b>в</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-круг</span>'
    '<span class="hd-gloss">VÒNG — chính là <b>круг</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Trong một vòng» ⇒ xung quanh — y như tiếng Anh <i>a-round</i>. Làm giới '
    'từ thì đòi cách 2: <b>вокру́г до́ма</b> quanh nhà. Đứng một mình là trạng từ: '
    '<b>Посмотри́ вокру́г</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>круг</b> vòng tròn · <b>кру́глый</b> tròn</div>'
)

# ----------------------------------------------------------------- обратно
S["обратно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">обрат-</span>'
    '<span class="hd-gloss">XOAY LẠI — từ <b>обрати́ть</b> «quay về phía»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-но</span>'
    '<span class="hd-gloss">đuôi trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Xoay ngược lại ⇒ về ĐÚNG CHỖ CŨ: <b>Иди́ обра́тно</b> quay lại đi. Cụm '
    'phải thuộc: <b>туда́ и обра́тно</b> đi và về, <b>биле́т туда́-обра́тно</b> vé khứ hồi.</div>'
    '<div class="hd-warn">Khác <b>наза́д</b>: <b>наза́д</b> là hướng ra SAU, và cả «cách đây» '
    '(<b>два го́да наза́д</b>). <b>обра́тно</b> chỉ là về chỗ xuất phát, không bao giờ «cách đây».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обра́тный</b> ngược, chiều về · <b>обрати́ть внима́ние</b> chú ý '
    '(xoay sự chú ý về)</div>'
)

# ------------------------------------------------------------------ где-то
S["где-то"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">где</span>'
    '<span class="hd-gloss">Ở ĐÂU (từ hỏi)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-то</span>'
    '<span class="hd-gloss">«… nào đó» — có thật, chỉ là không biết chính xác</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng khuôn với <b>кто́-то</b> ai đó: <b>Ключи́ где́-то в су́мке</b> — chìa '
    'khoá ở đâu đó trong túi (chắc chắn có, chỉ không biết chỗ). Phép so <i>-то</i> ↔ '
    '<i>-нибудь</i> nằm ở thẻ <b>кто́-то</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>где</b> ở đâu · <b>кто́-то</b> ai đó · <b>что́-то</b> cái gì đó · '
    '<b>куда́-то</b> tới đâu đó</div>'
)

# -------------------------------------------------------------------- путь
S["путь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">путь</span>'
    '<span class="hd-gloss">ĐƯỜNG ĐI — gốc Slav trơn, không hậu tố</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giống ĐỰC (<b>мой путь</b>) nhưng biến cách như giống cái đuôi <b>-ь</b>: '
    '<b>пути́</b> ở cách 2, 3, 6; riêng cách 5 lại theo đực: <b>путём</b>. Khác <b>доро́га</b> '
    '(mặt đường cụ thể): <b>путь</b> là tuyến, hành trình, cả «cách» làm.</div>'
    '<div class="hd-warn"><b>Счастли́вого пути́!</b> = thượng lộ bình an · <b>по пути́</b> = tiện '
    'đường, trên đường đi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>путеше́ствие</b> chuyến du lịch · <b>путеше́ствовать</b> du lịch · '
    '<b>спу́тник</b> bạn đồng hành, vệ tinh (người CÙNG đường)</div>'
)
