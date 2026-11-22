# -*- coding: utf-8 -*-
"""k199 — places::position (lô trộn): lễ hội, săn bắn, thời tiết, địa hình, vị trí.

Chỗ cần nhất quán trong lô:
(1) Động từ gắn với danh từ đã có thẻ: пра́здновать ← пра́здник, весели́ться ← весёлый,
    охо́титься ← охо́та. Cả ba nói "danh từ + -овать/-иться ⇒ làm việc đó".
(2) Ba trạng từ chỗ chốn: ниотку́да (ни- + отку́да), вдали́ (в + даль), наскво́зь (на + сквозь)
    — chẻ ra là thấy ngay từ đã học bên trong.
(3) Bỏ Họ hàng có chủ ý: гол, урага́н, тонне́ль (từ mượn đứng một mình), ста́я (gốc trơn).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "гол": "bàn thắng",                                    # «gôn» = khung thành (воро́та), không phải гол
    "насквозь": "xuyên qua, thấu suốt, hoàn toàn",          # «ướt sũng» là промо́кнуть наскво́зь, không phải nghĩa của từ
}

# --------------------------------------------------------------------- парад
S["парад"] = (
    '<div class="hd-why">Không chẻ được: mượn thẳng tiếng Pháp <i>parade</i> — cùng gốc với '
    'tiếng Anh <i>parade</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc là cuộc diễu hành, lễ duyệt binh: <b>пара́д Побе́ды</b> lễ duyệt '
    'binh Ngày Chiến thắng. Từ đó ra nghĩa «bộ đồ mặc cho lễ»: <b>при пара́де</b> = ăn diện chỉnh '
    'tề. Trọng âm ở âm cuối: <b>пара́д</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пара́дный</b> thuộc nghi lễ, trang trọng · '
    '<b>пара́дный вход</b> cửa chính</div>'
)

# --------------------------------------------------------------------- праздновать
S["праздновать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пра́здн-</span>'
    '<span class="hd-gloss">NGÀY LỄ — gốc của <b>пра́здник</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-ть</span>'
    '<span class="hd-gloss">→ động từ; chia -ую, -уешь</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>пра́здник</b> ngày lễ → <b>пра́здновать</b> làm lễ, ăn mừng. Đuôi '
    '-ова- đổi thành -у- khi chia: <b>я пра́здную</b>, <b>ты пра́зднуешь</b>. Bắt thẳng cách 4: '
    '<b>пра́здновать день рожде́ния</b>. Thể hoàn thành: <b>отпра́здновать</b>.</div>'
    '<div class="hd-warn">Cụm -здн- đọc như [зн] — chữ д câm nhưng VẪN PHẢI VIẾT, gõ đề rất dễ '
    'sót (cùng kiểu <b>по́здно</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пра́здник</b> ngày lễ · <b>пра́здничный</b> thuộc ngày lễ · '
    '<b>отпра́здновать</b> ăn mừng (xong)</div>'
)

# --------------------------------------------------------------------- веселиться
S["веселиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">весел-</span>'
    '<span class="hd-gloss">VUI — như <b>весёлый</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-ть-ся</span>'
    '<span class="hd-gloss">→ động từ, -ся: làm cho CHÍNH MÌNH vui</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Tự làm mình vui» ⇒ vui chơi, vui đùa: <b>де́ти веселя́тся</b> bọn trẻ '
    'vui chơi. Chia kiểu -ить: <b>я веселю́сь</b>, <b>ты весели́шься</b>.</div>'
    '<div class="hd-warn">Chữ ё chỉ đứng dưới trọng âm: <b>весёлый</b> có ё, nhưng trọng âm dời '
    'sang đuôi thì về е — gõ <b>весели́ться</b>, không có ё.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>весёлый</b> vui · <b>ве́село</b> vui vẻ · '
    '<b>весе́лье</b> niềm vui, cuộc vui · <b>развесели́ть</b> làm cho vui lên</div>'
)

# --------------------------------------------------------------------- охотиться
S["охотиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">охо́т-</span>'
    '<span class="hd-gloss">CUỘC SĂN — như <b>охо́та</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-ть-ся</span>'
    '<span class="hd-gloss">→ động từ; -ся không mang nghĩa «tự mình», chỉ đi kèm sẵn</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>охо́та</b> cuộc săn → <b>охо́титься</b> đi săn. Riêng ngôi «tôi» '
    'т đổi thành ч: <b>я охо́чусь</b>, nhưng <b>ты охо́тишься</b> — cùng luật với '
    '<b>плати́ть → я плачу́</b>.</div>'
    '<div class="hd-warn">Săn CON GÌ: <b>на</b> + cách 4 — <b>охо́титься на волко́в</b> săn sói. '
    'Ráo riết tìm ai/cái gì: <b>за</b> + cách 5 — <b>охо́титься за ним</b> săn lùng hắn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>охо́та</b> cuộc săn · <b>охо́тник</b> thợ săn · '
    '<b>охо́тно</b> sẵn lòng (<b>охо́та</b> còn nghĩa «ham muốn»)</div>'
)

# --------------------------------------------------------------------- гол
S["гол"] = (
    '<div class="hd-why">Không chẻ được: mượn tiếng Anh <i>goal</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>гол</b> là BÀN THẮNG, điểm ghi được; cái khung thành thì là '
    '<b>воро́та</b>. Cụm phải thuộc: <b>заби́ть гол</b> ghi bàn. Số nhiều trọng âm nhảy ra đuôi: '
    '<b>голы́</b>, <b>два го́ла</b> nhưng <b>пять голо́в</b>.</div>'
)

# --------------------------------------------------------------------- бокс
S["бокс"] = (
    '<div class="hd-why">Không chẻ được: mượn tiếng Anh <i>box</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hai nghĩa đều từ chữ Anh: <i>boxing</i> ⇒ môn quyền anh '
    '(<b>занима́ться бо́ксом</b> tập quyền anh); <i>box</i> «hộp» ⇒ buồng ngăn riêng — buồng cách '
    'ly trong bệnh viện, ô đỗ trong gara.</div>'
    '<div class="hd-warn">Võ sĩ là <b>боксёр</b> — có chữ ё, gõ đề đừng viết е.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>боксёр</b> võ sĩ quyền anh · <b>боксёрский</b> thuộc quyền anh</div>'
)

# --------------------------------------------------------------------- котёнок
S["котёнок"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кот-</span>'
    '<span class="hd-gloss">CON MÈO (<b>кот</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ёнок</span>'
    '<span class="hd-gloss">→ CON NON của loài vật</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi -ёнок mở khoá cả lớp «con non»: <b>утёнок</b> vịt con, '
    '<b>телёнок</b> bê con. Số ít: о của -ёнок rơi khi thêm đuôi — <b>котёнка</b>.</div>'
    '<div class="hd-warn">Số nhiều KHÔNG giữ -ёнок mà đổi hẳn sang -я́та: <b>котя́та</b>, '
    '<b>котя́т</b> — cả lớp đều thế (<b>утя́та</b>, <b>теля́та</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кот</b> mèo (đực) · <b>ко́шка</b> mèo (cái), mèo nói chung</div>'
)

# --------------------------------------------------------------------- стая
S["стая"] = (
    '<div class="hd-why">Không chẻ được — gốc trơn, học nguyên khối.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đàn con vật TỰ KẾT BẦY mà đi: <b>ста́я птиц</b> đàn chim, '
    '<b>ста́я волко́в</b> bầy sói, <b>ста́я рыб</b> đàn cá. Đàn gia súc do người chăn '
    '(bò, cừu) thì lại là <b>ста́до</b>.</div>'
)

# --------------------------------------------------------------------- ветка
S["ветка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вет-</span>'
    '<span class="hd-gloss">CÀNH — từ <b>ветвь</b> (văn viết), mất chữ в</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-а</span>'
    '<span class="hd-gloss">đuôi thu nhỏ → cành con</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cành cây toả nhánh ⇒ mọi thứ rẽ nhánh: đường ray nhánh, tuyến tàu điện '
    'ngầm (<b>ве́тка метро́</b>), luồng thảo luận. Số nhiều cách 2 chèn о: <b>ве́ток</b>, như '
    'mọi danh từ -ка sau phụ âm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ветвь</b> cành (văn viết) · <b>ве́точка</b> cành nhỏ</div>'
)

# --------------------------------------------------------------------- прогноз
S["прогноз"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">TRƯỚC (Hy Lạp)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-гноз</span>'
    '<span class="hd-gloss">BIẾT (Hy Lạp <i>gnosis</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Biết trước» ⇒ dự báo — chính là tiếng Anh <i>prognosis</i>, mượn nguyên '
    'khối. Hay gặp nhất: <b>прогно́з пого́ды</b> dự báo thời tiết.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>прогнози́ровать</b> dự báo · <b>диа́гноз</b> chẩn đoán '
    '(cùng -гноз «biết»)</div>'
)

# --------------------------------------------------------------------- гром
S["гром"] = (
    '<div class="hd-why">Không chẻ được — gốc trơn.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>гром</b> là SẤM, cái tiếng ầm; tia chớp, tia sét là <b>мо́лния</b>. '
    'Gốc гром- = «tiếng ầm ầm» ⇒ <b>гро́мкий</b> to tiếng là «như sấm».</div>'
    '<div class="hd-warn">Cụm phải thuộc: <b>гром среди́ я́сного не́ба</b> = sét đánh ngang tai '
    '(nghĩa đen: sấm giữa trời quang).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гро́мкий</b> to tiếng · <b>гро́мко</b> to, lớn tiếng · '
    '<b>греме́ть</b> vang rền (о↔е)</div>'
)

# --------------------------------------------------------------------- ураган
S["ураган"] = (
    '<div class="hd-why">Không chẻ được: từ mượn, cùng gốc với tiếng Anh <i>hurricane</i> '
    '(gốc từ thổ dân vùng Caribe).</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không phải bão thường mà là bão cực mạnh, gió phá nhà — bão nói chung '
    'là <b>бу́ря</b>. Trọng âm cuối: <b>урага́н</b>.</div>'
)

# --------------------------------------------------------------------- залив
S["залив"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">VÀO SÂU, tràn lấp</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лив</span>'
    '<span class="hd-gloss">ĐỔ, RÓT — như <b>лить</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Chỗ nước đổ tràn vào đất liền» ⇒ vịnh. Cùng hình với động từ '
    '<b>залива́ть</b> đổ ngập. Tên riêng hay gặp: <b>Фи́нский зали́в</b> vịnh Phần Lan.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лить</b> đổ, rót · <b>залива́ть</b> đổ ngập · '
    '<b>ли́вень</b> mưa rào · <b>разли́в</b> nước lũ tràn</div>'
)

# --------------------------------------------------------------------- распродажа
S["распродажа"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рас-</span>'
    '<span class="hd-gloss">TOẢ RA, cho HẾT</span></div>'
    '<div class="hd-row"><span class="hd-piece">-прода́жа</span>'
    '<span class="hd-gloss">SỰ BÁN — từ <b>прода́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Bán toả ra cho hết sạch» ⇒ đợt bán tháo, hạ giá, thanh lý. Trọng âm '
    'giữ y như <b>прода́жа</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>прода́ть</b> bán · <b>прода́жа</b> sự bán · '
    '<b>продаве́ц</b> người bán · <b>распрода́ть</b> bán hết sạch</div>'
)

# --------------------------------------------------------------------- тоннель
S["тоннель"] = (
    '<div class="hd-why">Không chẻ được: mượn tiếng Anh <i>tunnel</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi -ь nhưng là giống đực: <b>дли́нный тонне́ль</b>. Trọng âm cuối: '
    '<b>тонне́ль</b>.</div>'
    '<div class="hd-warn">Có hai cách viết đều đúng: <b>тонне́ль</b> và <b>тунне́ль</b>. Thẻ '
    'này dùng <b>тонне́ль</b> — chữ о sau т.</div>'
)

# --------------------------------------------------------------------- баня
S["баня"] = (
    '<div class="hd-why">Không chẻ được — gốc trơn, học nguyên khối.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhà tắm hơi kiểu Nga — hơi nóng, quất chổi lá bạch dương: '
    '<b>ходи́ть в ба́ню</b> đi tắm hơi.</div>'
    '<div class="hd-warn">Đừng lẫn với <b>ва́нна</b> bồn tắm, <b>ва́нная</b> phòng tắm '
    'trong nhà — chữ đầu б khác в.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ба́нный</b> thuộc nhà tắm hơi</div>'
)

# --------------------------------------------------------------------- ниоткуда
S["ниоткуда"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ни-</span>'
    '<span class="hd-gloss">KHÔNG … NÀO CẢ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-отку́да</span>'
    '<span class="hd-gloss">TỪ ĐÂU (<b>отку́да</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Không từ đâu cả». Cùng khuôn ни- + từ hỏi: <b>никуда́</b> không đi đâu, '
    '<b>нигде́</b> không ở đâu.</div>'
    '<div class="hd-warn">Động từ đi kèm vẫn phải có <b>не</b> — tiếng Nga phủ định hai lần: '
    '<b>Я ниотку́да не получа́л пи́сем</b> tôi chẳng nhận thư từ đâu cả.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отку́да</b> từ đâu · <b>куда́</b> đi đâu · '
    '<b>никуда́</b> không đi đâu cả</div>'
)

# --------------------------------------------------------------------- вдали
S["вдали"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">Ở TRONG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дал-и́</span>'
    '<span class="hd-gloss">KHOẢNG XA (<b>даль</b>), dạng cách 6</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Ở trong khoảng xa» ⇒ đằng xa, đứng yên một chỗ, trả lời <b>где?</b>: '
    '<b>вдали́ видны́ го́ры</b> đằng xa thấy núi.</div>'
    '<div class="hd-warn">Hướng nhìn/đi RA xa (<b>куда́?</b>) là <b>вдаль</b>: '
    '<b>смотре́ть вдаль</b> nhìn ra xa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>даль</b> khoảng xa · <b>далёкий</b> xa · <b>далеко́</b> xa · '
    '<b>издалека́</b> từ xa</div>'
)

# --------------------------------------------------------------------- насквозь
S["насквозь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">biến giới từ thành trạng từ — không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сквозь</span>'
    '<span class="hd-gloss">XUYÊN QUA (<b>сквозь</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>сквозь</b> là giới từ, phải có danh từ theo sau: <b>сквозь стекло́</b> '
    'xuyên qua kính. <b>наскво́зь</b> đứng một mình: <b>промо́кнуть наскво́зь</b> ướt sũng '
    '(ướt xuyên qua).</div>'
    '<div class="hd-warn">Nghĩa bóng hay gặp: <b>ви́жу тебя́ наскво́зь</b> tôi nhìn thấu bạn rồi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сквозь</b> xuyên qua · <b>сквозня́к</b> gió lùa</div>'
)

# --------------------------------------------------------------------- отсутствовать
S["отсутствовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">RỜI XA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-су́тств-</span>'
    '<span class="hd-gloss">SỰ CÓ MẶT (gốc cổ của «là, có»)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-ть</span>'
    '<span class="hd-gloss">→ động từ; chia -ую, -уешь</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Rời xa chỗ có mặt» ⇒ vắng mặt; đối nghĩa với при- «ở cạnh»: '
    '<b>прису́тствовать</b> có mặt. Ai vắng thì đứng làm chủ ngữ: <b>Он отсу́тствует</b>; vắng ở '
    'đâu: <b>на</b> + cách 6 — <b>отсу́тствовать на уро́ке</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отсу́тствие</b> sự vắng mặt · <b>прису́тствовать</b> có mặt · '
    '<b>прису́тствие</b> sự hiện diện</div>'
)

B = {
    "docbangmat": 79,
    "loitubat": 2,      # весе́лятся -> веселя́тся (trọng âm sai); тонне́ль/тунне́ль: viết nhầm "khác ở hai chữ н" (cả hai đều нн, khác ở о/у)
    "nguonsai": 2,      # V гол: «gôn» = khung thành, không phải bàn thắng; V насквозь: «ướt sũng» là nghĩa của cả cụm промо́кнуть наскво́зь
    "baolen": [
        "V cần duyệt: гол «bàn thắng, gôn» -> «bàn thắng» (gôn là khung thành = воро́та).",
        "V cần duyệt: насквозь bỏ «ướt sũng» (chỉ đúng trong cụm промо́кнуть наскво́зь).",
        "Không chắc: охо́тно nối với охо́та qua nghĩa cổ «ham muốn» — từ nguyên phổ biến, nhưng là từ nguyên, không phải luật.",
        "Không chắc: -су́тств- trong отсу́тствовать khai là «sự có mặt, gốc cổ của là/có» — đúng theo từ nguyên chuẩn, chưa đánh Mức tin trên thẻ.",
        "Không chắc: урага́н ghi «gốc thổ dân vùng Caribe» (Taíno qua Tây Ban Nha) — chưa đối chiếu nguồn.",
        "Họ hàng cố ý vắng: гол, ста́я, урага́н, тонне́ль (từ mượn/gốc trơn đứng một mình).",
        "Từ điển ghi гром số nhiều nom «гро́мы, гро́ма» — không dùng trên thẻ (số nhiều hiếm), không xác minh dạng гро́ма.",
    ],
}
