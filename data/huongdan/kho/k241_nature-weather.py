# -*- coding: utf-8 -*-
"""k241 — nature::weather (lô trộn): chim thú, rét và hoa, vườn phố, chỗ nào đó, đi xe vào.

Chỗ cần nhất quán trong lô:
(1) -ей → -ь- (воробе́й/воробья́, солове́й/соловья́): một câu như nhau; nguyên âm chạy của като́к theo цвето́к [k91].
(2) мёрз- BĂNG GIÁ = мороз- (моро́з k27): мёрзнуть / замёрзнуть cùng móc, quá khứ rụng -ну- như привы́кнуть [k128].
(3) цвет- NỞ HOA theo цвет [k58], цвето́к [k91] (расцве́т do k242 soạn cùng nghĩa gốc).
(4) кое- theo кое-что́ [k154], кое-кто́ [k173], кое-куда́ [k224]; ở кое-ка́к nghĩa «người nói biết» đã mờ — nói thẳng.
(5) въ- VÀO TRONG, có ъ vì е đứng sau — khuôn съе́хать [k225], подъе́хать [k143].
(6) вдаль (куда́?) đối lại вдали́ [k199] (где?); досто- ĐÁNG theo досто́йный [k182], -меч-/-мет- DẤU theo приме́та [k172].
Họ hàng cố ý vắng: сквер, алле́я (từ mượn đứng một mình).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "соловей": "chim hoạ mi, chim dạ oanh",               # «sơn ca» là жаворонок (lark), sai loài
    "баран": "cừu đực, kẻ ngốc, kẻ cứng đầu",             # «con cừu» trơn = овца; THIẾU stubborn fool
    "цвести": "nở hoa, ra hoa",                           # «tươi tốt» = lush, gloss chỉ bloom
    "град": "mưa đá, loạt dồn dập, trận tới tấp",         # «trận như trút» tối nghĩa; gloss torrent / volley
    "замёрзнуть": "bị lạnh, lạnh cóng, đóng băng, chết rét",   # cặp thể chung dãy; THIẾU freeze over / freeze to death
    "мёрзнуть": "bị lạnh, lạnh cóng, đóng băng, chết rét",     # cặp thể chung dãy; THIẾU freeze / be killed by frost
    "вдаль": "ra xa, về phía xa",                         # «xa xa» = вдали (đứng yên)
    "ориентироваться": "định hướng, tìm đường, dựa theo, nắm được tình hình, am hiểu",  # THIẾU go by / be well versed
    "въезжать": "lái xe vào, đi xe vào, dọn vào ở",           # «vào bằng xe» lặp; THIẾU move in
    "въехать": "lái xe vào, đi xe vào, dọn vào ở, đâm vào",   # như въезжать + crash into / ram (chỉ gloss HT có)
    "кое-как": "chật vật lắm mới, qua loa, cẩu thả, tạm bợ",  # «loay hoay mãi mới» lặp; THIẾU carelessly / sloppily
}

# --------------------------------------------------------------------- бильярд
S["бильярд"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn, không chẻ theo tiếng Nga: Pháp <i>billard</i>, cùng chữ với '
    'tiếng Anh <i>billiards</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiếng Việt «bi-a» cũng từ chữ Pháp này. Nói môn chơi thì chỉ dùng số ít. '
    'Gõ đủ <b>ль + я</b>: chữ <b>ь</b> ngăn <b>л</b> với <b>я</b>.</div>'
    '<div class="hd-warn">Chơi môn gì thì <b>игра́ть в</b> + cách 4: <b>игра́ть в билья́рд</b> — '
    'như <b>игра́ть в футбо́л</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>билья́рдный</b> thuộc bi-a (<b>билья́рдный стол</b> bàn bi-a) · '
    '<b>билья́рдная</b> phòng bi-a</div>'
)

# --------------------------------------------------------------------- каток
S["каток"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кат-</span><span class="hd-gloss">LĂN, cho chạy '
    'trên bánh/lưỡi trượt — như <b>ката́ться</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́к</span><span class="hd-gloss">hậu tố danh từ, '
    'chữ <b>о</b> chạy</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỗ để <b>ката́ться на конька́х</b> ⇒ sân trượt băng. Cái để LĂN cho phẳng '
    '⇒ xe lu. Hễ thêm đuôi là <b>о</b> rơi mất, trọng âm ra đuôi: <b>катка́, катко́м</b>, '
    '<b>катки́</b> — khuôn <b>цвето́к → цветка́</b>.</div>'
    '<div class="hd-warn">Ở sân, ra sân trượt đều dùng <b>на</b>: <b>на катке́</b>, '
    '<b>идти́ на като́к</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ката́ться</b> đi chơi bằng xe, trượt · <b>кати́ться</b> lăn · '
    '<b>ката́ние</b> sự trượt, việc đi chơi bằng xe</div>'
)

# --------------------------------------------------------------------- воробей
S["воробей"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Khuôn <b>-ей → -ь-</b>: hễ thêm đuôi là <b>е</b> co lại thành <b>ь</b>, '
    'trọng âm ra đuôi: <b>воробья́, воробьём</b>, số nhiều <b>воробьи́, воробьёв</b>. '
    '<b>солове́й</b> chia y hệt.</div>'
    '<div class="hd-warn"><b>стре́ляный воробе́й</b> «chim sẻ từng bị bắn» = người từng trải, khó '
    'lừa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>воро́бушек</b> chim sẻ nhỏ · <b>воробьи́ный</b> thuộc chim sẻ</div>'
)

# --------------------------------------------------------------------- соловей
S["соловей"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Con chim nhỏ hót hay về đêm — <i>nightingale</i>. Khuôn <b>-ей → -ь-</b>: '
    'hễ thêm đuôi là <b>е</b> co lại thành <b>ь</b>, trọng âm ra đuôi: <b>соловья́, соловьём</b>, '
    'số nhiều <b>соловьи́, соловьёв</b>. <b>воробе́й</b> chia y hệt.</div>'
    '<div class="hd-warn"><b>Соловья́ ба́снями не ко́рмят</b> «không nuôi hoạ mi bằng truyện kể» = '
    'nói suông không no, mời khách ăn đi đã.</div>'
    '<div class="hd-warn">Đừng lẫn <b>жа́воронок</b> chim sơn ca — hót từ sáng sớm, nên người quen '
    'dậy sớm cũng gọi là <b>жа́воронок</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>соловьи́ный</b> thuộc hoạ mi (<b>соловьи́ное пе́ние</b> tiếng hoạ mi '
    'hót)</div>'
)

# --------------------------------------------------------------------- баран
S["баран"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Con ĐỰC; con cái (và cừu nói chung) là <b>овца́</b>. Cừu đực nổi tiếng lì '
    '⇒ mắng người ngốc mà cứng đầu. Trọng âm đứng yên: <b>бара́на, бара́ны</b>.</div>'
    '<div class="hd-warn"><b>смотре́ть как бара́н на но́вые воро́та</b> «nhìn như cừu đực nhìn cổng '
    'mới» = ngơ ngác, đần mặt ra.</div>'
    '<div class="hd-warn"><b>Вернёмся к на́шим бара́нам</b> «quay lại với lũ cừu» = trở lại chuyện '
    'chính.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бара́нина</b> thịt cừu · <b>бара́ний</b> thuộc cừu · '
    '<b>бара́шек</b> cừu non</div>'
)

# --------------------------------------------------------------------- цвести
S["цвести"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">цвес-</span><span class="hd-gloss">NỞ HOA — chính '
    'là <b>цвет-</b> (thẻ <b>цвет</b>), <b>т</b> hoá <b>с</b> trước <b>-ти</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ти́</span><span class="hd-gloss">đuôi nguyên thể, '
    'như <b>расти́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhớ gốc <b>цвет-</b> là ra hiện tại: <b>цвету́, цветёт, цвету́т</b>. Quá '
    'khứ thì <b>т</b> rụng trước <b>л</b>, trọng âm ra đuôi: <b>цвёл, цвела́, цвели́</b>. Bắt đầu nở: '
    '<b>расцвести́</b>, <b>зацвести́</b> (HT).</div>'
    '<div class="hd-warn"><b>Цветём и па́хнем</b> «đang nở và toả hương» — câu đùa đáp lại '
    '<b>Как дела́?</b> = vẫn tươi roi rói.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>цвет</b> màu · <b>цвето́к</b> bông hoa · <b>цветно́й</b> có màu · '
    '<b>расцве́т</b> thời nở rộ</div>'
)

# --------------------------------------------------------------------- град
S["град"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn rất cổ, không chẻ được; cùng gốc với Latin <i>grando</i> '
    '«mưa đá».</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đá trút xuống rào rào ⇒ bất cứ thứ gì dồn dập ập tới, kèm cách 2 số nhiều: '
    '<b>град вопро́сов</b> câu hỏi tới tấp, <b>град пуль</b> mưa đạn. Đang có mưa đá: '
    '<b>идёт град</b>. Chỉ dùng số ít.</div>'
    '<div class="hd-warn"><b>-град</b> trong <b>Волгогра́д</b> là từ KHÁC: bản Slavơ cổ của '
    '<b>го́род</b>. <b>награ́да, виногра́д, гра́дус</b> cũng không dính gì tới mưa đá.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гра́дина</b> viên mưa đá · <b>гра́дом</b> tới tấp (<b>слёзы гра́дом</b> '
    'nước mắt tuôn như mưa)</div>'
)

# --------------------------------------------------------------------- замёрзнуть
S["замёрзнуть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span><span class="hd-gloss">tiền tố thể hoàn '
    'thành, không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мёрз-</span><span class="hd-gloss">BĂNG GIÁ — cùng '
    'gốc <b>моро́з</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ну-ть</span><span class="hd-gloss">đuôi động từ, '
    '<i>-ну-</i> rụng ở quá khứ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">HT của <b>мёрзнуть</b>: băng giá đã ngấm xong — người thì lạnh cóng, '
    'sông thì đóng băng (<b>река́ замёрзла</b>). Quá khứ rụng <i>-ну-</i>, giống đực rụng luôn '
    '<i>-л</i>: <b>замёрз, замёрзла, замёрзли</b>.</div>'
    '<div class="hd-warn"><b>Я замёрз</b> (quá khứ) = tôi đang lạnh cóng đây — kết quả còn tới bây '
    'giờ, như <b>я привы́к</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мёрзнуть</b> (CHT) · <b>замерза́ть</b> đóng băng dần (CHT, chữ '
    '<b>е</b>) · <b>моро́з</b> rét đóng băng · <b>моро́женое</b> kem</div>'
)

# --------------------------------------------------------------------- мёрзнуть
S["мёрзнуть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мёрз-</span><span class="hd-gloss">BĂNG GIÁ — cùng '
    'gốc <b>моро́з</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ну-ть</span><span class="hd-gloss">đuôi động từ, '
    '<i>-ну-</i> rụng ở quá khứ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bị <b>моро́з</b> ngấm vào người ⇒ chịu lạnh. Có <i>-ну-</i> mà vẫn là CHT. '
    'Quá khứ rụng <i>-ну-</i>, giống đực rụng luôn <i>-л</i>: <b>мёрз, мёрзла, мёрзли</b>; dạng '
    '<b>мёрзнул</b> có nhưng hiếm. Cặp HT: <b>замёрзнуть</b>.</div>'
    '<div class="hd-warn"><b>Мне хо́лодно</b> tôi thấy lạnh ↔ <b>я мёрзну</b> tôi đang chịu rét. '
    'Nói được cả bộ phận: <b>У меня́ мёрзнут ру́ки</b> = Tay tôi lạnh.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>замёрзнуть</b> (HT) · <b>моро́з</b> rét đóng băng · <b>моро́зный</b> '
    'giá rét · <b>ве́чная мерзлота́</b> tầng đất đóng băng vĩnh cửu</div>'
)

# --------------------------------------------------------------------- провинциальный
S["провинциальный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">провинци-</span><span class="hd-gloss">TỈNH, tỉnh '
    'lẻ — <b>прови́нция</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-альн-ый</span><span class="hd-gloss">đuôi tính từ '
    'quốc tế, Anh <i>-al</i> (<i>provincial</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thuộc tỉnh lẻ» ⇒ không phải thủ đô; nói về lối ăn mặc, cách nghĩ thì thành '
    'chê: quê mùa. Trọng âm luôn ở <b>-а́льн-</b>; dạng ngắn giống đực chen <b>е</b>: '
    '<b>провинциа́лен</b>, còn lại giữ nguyên: <b>провинциа́льна</b>.</div>'
    '<div class="hd-warn">Đối lại là <b>столи́чный</b> thuộc thủ đô. Nói về Nga, từ này là «tỉnh '
    'lẻ»; «của tỉnh» (hành chính) là <b>областно́й</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>прови́нция</b> tỉnh, tỉnh lẻ · <b>провинциа́л</b> người tỉnh lẻ</div>'
)

# --------------------------------------------------------------------- сквер
S["сквер"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn, không chẻ theo tiếng Nga: chính là Anh <i>square</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Khu phố Anh có <i>square</i> là ô đất trồng cây giữa các dãy nhà ⇒ tiếng '
    'Nga chỉ giữ phần CÂY: mảnh vườn công cộng nhỏ giữa phố, có ghế ngồi. Lớn hơn là <b>парк</b>. '
    'Ở đó: <b>в скве́ре</b>.</div>'
    '<div class="hd-warn">Quảng trường (<i>Red Square</i>) KHÔNG phải <b>сквер</b> mà là '
    '<b>пло́щадь</b>.</div>'
    '<div class="hd-warn"><b>скве́рный</b> tồi tệ chỉ giống mặt chữ, không cùng gốc.</div>'
)

# --------------------------------------------------------------------- аллея
S["аллея"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn, không chẻ theo tiếng Nga: Pháp <i>allée</i> «lối đi», từ '
    '<i>aller</i> «đi».</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Lối đi có hai hàng cây hai bên, trong công viên hay dọc phố: '
    '<b>ли́повая алле́я</b> lối đi trồng cây đoan. Dạo dọc lối đó: <b>гуля́ть по алле́е</b>.</div>'
    '<div class="hd-warn">Anh <i>alley</i> cùng gốc Pháp nhưng lệch nghĩa: ngõ hẻm tiếng Nga là '
    '<b>переу́лок</b>, không phải <b>алле́я</b>.</div>'
    '<div class="hd-warn"><b>аллерги́я</b> dị ứng là gốc Hy Lạp, không liên quan.</div>'
)

# --------------------------------------------------------------------- кое-где
S["кое-где"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кое-</span><span class="hd-gloss">người nói BIẾT là '
    'chỗ nào, chỉ chưa nói ra</span></div>'
    '<div class="hd-row"><span class="hd-piece">где</span><span class="hd-gloss">Ở ĐÂU (từ '
    'hỏi)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Ở những chỗ biết đấy, khỏi kể hết» ⇒ đôi chỗ, chỗ này chỗ kia: '
    '<b>Кое-где́ лежи́т снег</b> = Đôi chỗ còn tuyết. Thường là VÀI chỗ rải rác.</div>'
    '<div class="hd-warn"><b>где́-то</b> = MỘT chỗ, chính người nói không rõ (<b>Ключи́ где́-то в '
    'су́мке</b>) · <b>где́-нибудь</b> = chỗ nào cũng được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>где</b> ở đâu · <b>кое-куда́</b> tới vài chỗ · <b>кое-что́</b> một thứ · '
    '<b>кое-кто́</b> có người · <b>кое-ка́к</b> qua loa</div>'
)

# --------------------------------------------------------------------- вдаль
S["вдаль"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span><span class="hd-gloss">VÀO, hướng '
    'tới</span></div>'
    '<div class="hd-row"><span class="hd-piece">-даль</span><span class="hd-gloss">KHOẢNG XA '
    '(<b>даль</b>), dạng cách 4</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Vào khoảng xa» ⇒ ra xa, trả lời <b>куда́?</b>: <b>смотре́ть вдаль</b> nhìn '
    'ra xa, <b>доро́га ухо́дит вдаль</b> con đường chạy hút ra xa.</div>'
    '<div class="hd-warn">Đứng yên ở đằng xa (<b>где?</b>) là <b>вдали́</b> — cách 6, trọng âm ra '
    'đuôi.</div>'
    '<div class="hd-warn">Có từ bổ nghĩa thì tách rời: <b>в голубу́ю даль</b> vào cõi xa xanh.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>даль</b> khoảng xa · <b>вдали́</b> ở đằng xa · <b>далеко́</b> xa · '
    '<b>да́льний</b> ở phía xa · <b>да́льше</b> xa hơn</div>'
)

# --------------------------------------------------------------------- ориентироваться
S["ориентироваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ориент-</span><span class="hd-gloss">PHƯƠNG ĐÔNG — '
    'Latin <i>oriens</i>, Anh <i>orient</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ирова-ть</span><span class="hd-gloss">đuôi động từ '
    'mượn, chia <b>-иру-</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span><span class="hd-gloss">TỰ mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Tự tìm ra phía đông» ⇒ định hướng, biết mình đang ở đâu; rộng ra là nắm rõ '
    'một lĩnh vực. Hiện tại: <b>ориенти́руюсь</b>. Cặp HT: <b>сориенти́роваться</b>.</div>'
    '<div class="hd-warn"><b>в</b> + cách 6 = thạo, biết đường: <b>ориенти́роваться в '
    'го́роде</b>, <b>в зако́нах</b> · <b>по</b> + cách 3 = dựa theo: <b>по со́лнцу, по ка́рте</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ориенти́р</b> mốc định hướng · <b>ориента́ция</b> sự định hướng · '
    '<b>ориентиро́вочный</b> phỏng chừng</div>'
)

# --------------------------------------------------------------------- достопримечательность
S["достопримечательность"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">досто-</span><span class="hd-gloss">ĐÁNG — như '
    '<b>досто́йный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-при-меч-а-</span><span class="hd-gloss">ĐỂ Ý — gốc '
    '<b>-мет-</b> DẤU (<b>приме́та</b>), <b>т</b> hoá <b>ч</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-тельн-ость</span><span class="hd-gloss">→ danh từ '
    'giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cái ĐÁNG ĐỂ Ý» ⇒ nơi đáng xem của một thành phố. Từ dài thì gõ theo mảnh: '
    '<i>досто + примечательность</i>; khúc giữa giống hệt <b>замеча́тельный</b> tuyệt vời '
    '(đáng để ý).</div>'
    '<div class="hd-warn">Hay gặp số nhiều: <b>осма́тривать достопримеча́тельности</b> đi tham quan '
    'danh thắng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>досто́йный</b> xứng đáng · <b>примеча́тельный</b> đáng chú ý · '
    '<b>примеча́ние</b> lời chú thích · <b>заме́тить</b> nhận thấy</div>'
)

# --------------------------------------------------------------------- въезжать
S["въезжать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">въ-</span><span class="hd-gloss">VÀO TRONG — có '
    '<i>ъ</i> vì <i>е</i> đứng ngay sau</span></div>'
    '<div class="hd-row"><span class="hd-piece">-езж-</span><span class="hd-gloss">gốc ĐI XE, như '
    '<b>приезжа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́-ть</span><span class="hd-gloss">đuôi CHT, chia '
    'đều: <b>въезжа́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Xe đi VÀO: <b>въезжа́ть в го́род</b> vào thành phố (<b>в</b> + cách 4). Chở '
    'đồ vào nhà mới ⇒ dọn vào ở: <b>въезжа́ть в кварти́ру</b>. Cặp HT: <b>въе́хать</b>.</div>'
    '<div class="hd-warn">Đi vào bằng CHÂN là <b>входи́ть</b>. Ngược hướng: <b>выезжа́ть</b> đi xe '
    'ra, <b>съезжа́ть</b> dọn khỏi nhà.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>въе́хать</b> (HT) · <b>въезд</b> lối xe vào · <b>приезжа́ть</b> đến bằng '
    'xe · <b>выезжа́ть</b> đi xe ra</div>'
)

# --------------------------------------------------------------------- въехать
S["въехать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">въ-</span><span class="hd-gloss">VÀO TRONG — có '
    '<i>ъ</i> vì <i>е</i> đứng ngay sau</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́х-ать</span><span class="hd-gloss">gốc ĐI XE — '
    'chính là <b>е́хать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp HT của <b>въезжа́ть</b>, cũng đi với <b>в</b> + cách 4: <b>въе́хать во '
    'двор</b> vào sân · <b>въе́хать в но́вую кварти́ру</b> dọn vào nhà mới. Thân tương lai lấy '
    '<i>е́д-</i> như <b>е́ду</b>: <b>въе́ду, въе́дешь, въе́дут</b>.</div>'
    '<div class="hd-warn">«Đi vào» cả thứ không có lối vào ⇒ đâm vào: <b>Он въе́хал в столб</b> = '
    'Anh ta đâm xe vào cột.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>въезжа́ть</b> (CHT) · <b>въезд</b> lối xe vào · <b>е́хать</b> đi xe · '
    '<b>вы́ехать</b> đi xe ra</div>'
)

# --------------------------------------------------------------------- кое-какой
S["кое-какой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кое-</span><span class="hd-gloss">người nói BIẾT là '
    'cái nào, chỉ chưa nói ra</span></div>'
    '<div class="hd-row"><span class="hd-piece">како́й</span><span class="hd-gloss">NÀO</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cái nào thì biết đấy, mà chẳng nhiều nhặn gì» ⇒ một vài, chút ít: '
    '<b>У меня́ есть кое-каки́е вопро́сы</b> = Tôi có vài câu hỏi. Còn <b>како́й-то</b> là chính '
    'người nói cũng không rõ. Chỉ phần <b>како́й</b> đổi đuôi: <b>кое-кака́я, кое-каки́х</b>.</div>'
    '<div class="hd-warn">Có giới từ thì nó chen vào GIỮA, gạch nối biến mất: кое <b>о каки́х</b>, '
    'кое <b>с каки́ми</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>како́й</b> nào · <b>како́й-то</b> nào đó · <b>кое-что́</b> một thứ · '
    '<b>кое-кто́</b> có người</div>'
)

# --------------------------------------------------------------------- кое-как
S["кое-как"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кое-</span><span class="hd-gloss">«… này … kia» — ở '
    'từ này nghĩa «người nói BIẾT» đã mờ</span></div>'
    '<div class="hd-row"><span class="hd-piece">как</span><span class="hd-gloss">THẾ NÀO</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cách này cách kia, sao cũng được» ⇒ hai nghĩa. Làm qua loa: <b>Он всё '
    'де́лает кое-ка́к</b> = Nó làm gì cũng cẩu thả. Xoay đủ cách mới được: <b>Мы кое-ка́к '
    'дое́хали</b> = Chúng tôi chật vật lắm mới tới nơi.</div>'
    '<div class="hd-warn">Nghĩa nào? Chê thái độ làm ⇒ «qua loa»; động từ HT kể việc khó mà cuối '
    'cùng xong ⇒ «chật vật lắm mới». <b>ка́к-то</b> chỉ là «bằng cách nào đó».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>как</b> thế nào · <b>ка́к-то</b> bằng cách nào đó · <b>кое-где́</b> đôi '
    'chỗ · <b>кое-что́</b> một thứ</div>'
)

# --------------------------------------------------------------------- báo cáo
B = {
    "docbangmat": 127,
    "loitubat": 5,   # воробей: nghĩa đen «từng bị bắn» gán chung cho cả старый lẫn стреляный -> chỉ giữ стреляный
                     # воробей/соловей: «ngoài cách 1 số ít» rối -> «hễ thêm đuôi»
                     # кое-где/кое-какой: mảnh кое- viết lệch khuôn k154 -> chép lại đúng khuôn
                     # мёрзнуть: «tay hay bị lạnh» sai sắc thái -> «Tay tôi lạnh»
                     # достопримечательность: «gần y замечательный» nói quá -> chỉ khúc giữa giống
    "nguonsai": 4,   # соловей «chim sơn ca» (sai loài) · аллея gloss «alley» (bạn giả) · град gloss «city» (từ khác)
                     # кое-как: nguồn ghi hai trọng âm ко́е-ка́к -> dạy кое-ка́к, khớp k154/k173
    "baolen": [
        "V cần duyệt (11 thẻ): соловей (BỎ sơn ca — loài khác, lark = жаворонок; THÊM hoạ mi) · баран (BỎ con cừu trơn = овца; THÊM kẻ cứng đầu) · цвести (BỎ tươi tốt) · град (viết lại hai nghĩa bóng) · мёрзнуть + замёрзнуть (cùng dãy; BỎ rét run / rét; THÊM đóng băng, chết rét) · вдаль (BỎ xa xa = вдали) · ориентироваться (THÊM dựa theo, am hiểu) · въезжать + въехать (BỎ «vào bằng xe» lặp; THÊM dọn vào ở) · кое-как (BỎ «cho xong», «loay hoay mãi mới»; THÊM qua loa, cẩu thả).",
        "въехать lệch въезжать đúng một nghĩa «đâm vào» (crash into / ram chỉ có trong gloss HT) — cố ý. мёрзнуть trùng hết nghĩa замёрзнуть — badge thể tách.",
        "соловей câu 1, 2, 3: bản dịch «chim sơn ca» -> «chim hoạ mi» (đề V không còn sơn ca). Câu 1: Под окном всю ночь пел соловей. / A <b>nightingale</b> was singing under the window all night. / Suốt đêm có con <b>chim hoạ mi</b> hót dưới cửa sổ. Câu 2: … Tôi chưa bao giờ nghe <b>chim hoạ mi</b> hót trực tiếp. Câu 3: … Mùa xuân ở đây <b>chim hoạ mi</b> hót tới sáng.",
        "цвести câu 1 (цветём и пахнем, dịch «tươi roi rói») dùng nghĩa bóng không có trong V; ô đỏ của thẻ đã dạy câu này. Nên thay bằng: В нашем саду уже цветут вишни. / The cherry trees are already <b>blooming</b> in our garden. / Trong vườn nhà tôi anh đào đã <b>nở hoa</b>.",
        "баран câu 3 «Хватит о баранах, расскажи про себя» gượng và dịch «cừu» trơn (V bỏ). Nên thay: Не упирайся как баран, послушай меня. / Don't be as stubborn as a <b>ram</b>, listen to me. / Đừng có bướng như <b>cừu đực</b>, nghe tớ nói này. (Cả 3 câu chưa câu nào dùng nghĩa «kẻ ngốc»; nếu muốn: Вот баран, опять забыл ключи! / What an <b>idiot</b>, he forgot his keys again! / Đúng là <b>kẻ ngốc</b>, lại quên chìa khoá!)",
        "град câu 2 «Не удивляйся граду» hơi gượng. Nên thay: Град побил все яблони в саду. / The <b>hail</b> damaged all the apple trees in the garden. / <b>Mưa đá</b> làm dập nát hết mấy cây táo trong vườn.",
        "мёрзнуть câu 2: «chúng tôi <b>lạnh</b> kinh khủng» -> «chúng tôi <b>bị lạnh</b> kinh khủng» cho khớp V.",
        "кое-как câu 2: «<b>cố lắm mới</b> mặc được» -> «<b>chật vật lắm mới</b> mặc được» cho khớp V.",
        "аллея: gloss Anh «alley» và cả 3 câu dịch «alley» là bạn giả (Anh alley = ngõ hẻm = переулок). Nên đổi English thành «tree-lined path, avenue»; câu 1: A long linden <b>avenue</b> starts behind the house; câu 2: We strolled along the <b>avenue</b>…; câu 3: This park has so many <b>tree-lined paths</b> that you can get lost.",
        "въезжать / въехать / ориентироваться: cả 3 câu của mỗi thẻ chỉ minh hoạ «lái xe vào» / «định hướng, tìm đường»; nghĩa thêm chưa có câu. Nên đổi một câu mỗi thẻ — въезжать câu 3 (dịch «lái xe LÊN vỉa hè» cũng lệch đề): Мы въезжаем в новую квартиру в субботу. / We're <b>moving into</b> the new flat on Saturday. / Thứ Bảy chúng tôi <b>dọn vào ở</b> căn hộ mới. въехать câu 1: Он задумался и въехал в столб. / He got lost in thought and <b>crashed into</b> a pole. / Anh ấy mải nghĩ nên <b>đâm vào</b> cột. ориентироваться câu 2: Она отлично ориентируется в законах. / She <b>is well versed</b> in the law. / Cô ấy rất <b>am hiểu</b> luật.",
        "Trọng âm trên mặt thẻ кое-как ghi hai dấu ко́е-ка́к (Wiktionary, trọng âm phụ); thẻ k154, k173 và lô này đều dạy кое-ка́к — nên đổi field Word về кое-ка́к cho khớp кое-где́ / кое-како́й.",
        "KHÔNG đưa lên vì không chắc: соловей ← соловый (vàng xám); баранка (bánh vòng) không cùng gốc баран. «chết rét» ở мёрзнуть dựa vào gloss «be killed by frost» (cây cối) — nếu thấy rộng thì bỏ ở CẢ HAI thẻ cặp.",
    ],
}
