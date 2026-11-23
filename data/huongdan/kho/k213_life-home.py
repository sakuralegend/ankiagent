# -*- coding: utf-8 -*-
"""k213 — life::home: bếp núc, đồ gia dụng, sức khoẻ; trục là NỐI VỀ GỐC ĐÃ HỌC.

Chỗ cần nhất quán trong lô:
(1) чист- SẠCH, thuần (чи́стый k42): чистить / почистить / химчистка.
(2) бы- TỒN TẠI (быть k03): быт / бытовой.
(3) -ли-/-лив- ĐỔ, RÓT (залив, сливки): наливать / налить; на- DỒN cho ĐẦY khớp набрать k206.
(4) осложнение = о- + сложный (с- LẠI VỚI NHAU + -лож- ĐẶT, k123).
(5) кушать: -кус- NẾM khớp вкус k152, искусство. жирный ← жир k205. пирожок ← пирог k74.
(6) зажигалка: gốc жг-/жег-/жог- khớp ожог. бритва: бри- CẠO khớp бриться k150.
Họ hàng cố ý vắng: омлет (từ mượn, không có từ phái sinh đáng học).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "пирожок": "bánh nhỏ có nhân, bánh bao nướng",            # «bánh nhân» không phải từ; «bánh nướng nhân» lẫn пиро́г
    "омлет": "trứng ốp lết, trứng tráng",                     # «trứng chiên» gồm cả trứng ốp la (яи́чница)
    "изба": "nhà gỗ, nhà gỗ nông thôn Nga",                   # изба là nhà ở kiên cố, không phải «lều»
    "зажигалка": "bật lửa, hộp quẹt",                         # «bom cháy»: nghĩa thời chiến, không thông dụng
    "бытовой": "thường ngày, sinh hoạt, đời thường, gia dụng",  # + household / for home use
    "уютный": "ấm cúng, dễ chịu",                             # «thoải mái» = comfortable, gloss chỉ cozy / snug
    "кран": "vòi nước, vòi, van, cần cẩu",                    # + crane
    "быт": "cuộc sống thường ngày, sinh hoạt hàng ngày, nếp sống",  # «chuyện nhà cửa» gloss không xác nhận
    "почистить": "làm sạch, chải, chà, đánh bóng, gọt vỏ",    # + brush; «đánh răng» là nghĩa của cả cụm với зу́бы
    "чистить": "làm sạch, chải, chà, đánh bóng, gọt vỏ",
    "витамин": "vitamin",                                     # «sinh tố» nay hiểu là nước xay
}

# --------------------------------------------------------------------- кукуруза
S["кукуруза"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ mượn (đi qua vùng Balkan), không chẻ được. Giống cái theo đuôi '
    '<b>-а</b>. Chỉ dùng SỐ ÍT, kể cả khi nói cả đống: <b>варёная кукуру́за</b> ngô luộc, '
    '<b>по́ле кукуру́зы</b> ruộng ngô.</div>'
    '<div class="hd-warn">Muốn đếm từng BẮP thì phải mượn từ khác: <b>поча́ток кукуру́зы</b> '
    '— một bắp ngô.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кукуру́зный</b> thuộc về ngô: <b>кукуру́зные хло́пья</b> ngô '
    'mảnh ăn sáng</div>'
)

# --------------------------------------------------------------------- жирный
S["жирный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">жир-</span>'
    '<span class="hd-gloss">MỠ, chất béo — <b>жир</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ный</span>'
    '<span class="hd-gloss">đuôi tính từ: có, nhiều thứ đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Có mỡ ⇒ béo, ngấy; dính mỡ ⇒ nhờn: <b>жи́рное мя́со</b> thịt mỡ, '
    '<b>жи́рная ко́жа</b> da dầu. Dạng ngắn giống đực chen <b>е</b>, giống cái nhảy xuống '
    'đuôi: <b>жи́рен, жирна́, жи́рно</b>.</div>'
    '<div class="hd-warn">Nói về NGƯỜI thì rất thô — dùng <b>по́лный</b> (lịch sự) hoặc '
    '<b>то́лстый</b>.</div>'
    '<div class="hd-warn"><b>жи́рный шрифт</b> = chữ in ĐẬM.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>жир</b> mỡ, chất béo · <b>нежи́рный</b> ít béo · '
    '<b>обезжи́ренный</b> tách béo</div>'
)

# --------------------------------------------------------------------- пирожок
S["пирожок"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пирож-</span>'
    '<span class="hd-gloss"><b>пиро́г</b> bánh nướng có nhân (г → ж)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ок</span>'
    '<span class="hd-gloss">hậu tố NHỎ, giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«<b>пиро́г</b> nhỏ» — cái bánh cầm tay bọc nhân thịt, bắp cải, '
    'táo… nướng hoặc rán. Nhân gì thì <b>с</b> + cách 5: <b>пирожо́к с мя́сом</b>.</div>'
    '<div class="hd-warn">NGUYÊN ÂM CHẠY: <b>о</b> của <b>-ок</b> rơi khi thêm đuôi, trọng âm '
    'dồn ra cuối: <b>пирожо́к → пирожка́, пирожки́, пирожко́в</b> (như <b>кусо́к → '
    'куска́</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пиро́г</b> bánh nướng to có nhân · <b>пиро́жное</b> bánh ngọt '
    'kiểu Âu, không bọc nhân</div>'
)

# --------------------------------------------------------------------- омлет
S["омлет"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ mượn tiếng Pháp <i>omelette</i> (Anh cũng <i>omelette</i>), '
    'không chẻ được. Tiếng Nga bỏ đuôi, kết thúc bằng phụ âm ⇒ giống ĐỰC: <b>вку́сный '
    'омле́т</b>. Thêm gì thì <b>с</b> + cách 5: <b>омле́т с сы́ром</b>.</div>'
    '<div class="hd-warn"><b>омле́т</b> = trứng đánh tan rồi tráng · <b>яи́чница</b> = thường '
    'là trứng đập thẳng vào chảo (ốp la).</div>'
)

# --------------------------------------------------------------------- наливать
S["наливать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">DỒN cho ĐẦY</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ли-</span>'
    '<span class="hd-gloss">ĐỔ, RÓT — <b>лить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>налива́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Rót cho đầy cốc, đầy bình: rót VÀO đâu thì <b>в</b> + cách 4, rót CHO ai '
    'thì cách 3 — <b>налива́ть го́стю чай в ча́шку</b>. Cặp HT <b>нали́ть</b> chia lệch hẳn, '
    'còn thể này thì đều.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>нали́ть</b> (HT) · <b>лить</b> đổ, rót · <b>зали́в</b> vịnh · '
    '<b>сли́вки</b> kem sữa · <b>ли́вень</b> mưa rào</div>'
)

# --------------------------------------------------------------------- налить
S["налить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">DỒN cho ĐẦY</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ли-ть</span>'
    '<span class="hd-gloss">ĐỔ, RÓT — <b>лить</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp HT của <b>налива́ть</b>. Rót MỘT ÍT thì dùng cách 2: <b>нале́й мне '
    'воды́</b> rót cho tôi ít nước; rót cả phần đã xác định thì cách 4.</div>'
    '<div class="hd-warn"><i>и</i> của gốc biến thành <i>ь</i>, y như <b>пить → пью</b>: '
    '<b>налью́, нальёшь, налью́т</b>; sai khiến <b>нале́й</b> (như <b>пей</b>). Quá khứ giống '
    'cái nhảy ra đuôi: <b>нали́л</b> nhưng <b>налила́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>налива́ть</b> (CHT) · <b>лить</b> đổ, rót · <b>вы́лить</b> đổ đi · '
    '<b>проли́ть</b> làm đổ</div>'
)

# --------------------------------------------------------------------- кушать
S["кушать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">куш-</span>'
    '<span class="hd-gloss">= <i>-кус-</i> NẾM (с → ш), như <b>вкус</b> vị</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>ку́шаю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Nếm» ⇒ ăn, nói cho lịch sự: lời mời khách và lời với trẻ con — '
    '<b>Ку́шайте, пожа́луйста!</b> Mời bác xơi ạ. Cặp HT: <b>поку́шать</b> ăn một chút, '
    '<b>ску́шать</b> ăn hết.</div>'
    '<div class="hd-warn">Đừng nói <b>я ку́шаю</b> về CHÍNH MÌNH — nghe kiểu cách. Người lớn nói '
    'về mình thì dùng <b>есть</b>: <b>я ем</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: nối <i>куш-</i> với <i>-кус-</i> là từ nguyên, không phải '
    'luật suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вкус</b> vị · <b>вку́сный</b> ngon · <b>иску́сство</b> nghệ '
    'thuật (nghĩa gốc: tài khéo qua thử, nếm)</div>'
)

# --------------------------------------------------------------------- изба
S["изба"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không chẻ được. Nhà bằng gỗ súc của nông dân Nga, trong nhà có cái lò '
    'lớn <b>печь</b>: <b>жить в избе́</b>. Trọng âm ở đuôi suốt số ít, sang số nhiều lùi hết '
    'về đầu: <b>изба́ → и́збы</b>, cách 2 trơ thân <b>изб</b>.</div>'
    '<div class="hd-warn"><b>Не выноси́ть сор из избы́</b> («đừng đem rác ra khỏi nhà») = đừng '
    'vạch áo cho người xem lưng.</div>'
    '<div class="hd-warn">⚠️ Mức tin: thường được coi là từ mượn rất cổ, cùng gốc với Đức '
    '<i>Stube</i> (phòng), Anh <i>stove</i> (lò) — từ nguyên, chưa ngã ngũ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>избу́шка</b> nhà gỗ nhỏ — nhà chân gà của Baba Yaga là '
    '<b>избу́шка на ку́рьих но́жках</b></div>'
)

# --------------------------------------------------------------------- бритва
S["бритва"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бри-</span>'
    '<span class="hd-gloss">CẠO — <b>брить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-тв-а</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái gắn vào động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thứ để cạo» ⇒ dao cạo, máy cạo. Cạo BẰNG dao thì cách 5: '
    '<b>бри́ться бри́твой</b>. Cùng khuôn <b>-тва</b>: <b>моли́ться</b> cầu nguyện → '
    '<b>моли́тва</b> lời cầu nguyện.</div>'
    '<div class="hd-warn"><b>о́стрый как бри́тва</b> = sắc như dao cạo. Máy cạo điện: '
    '<b>электробри́тва</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>брить</b> cạo · <b>бри́ться</b> tự cạo râu · '
    '<b>побри́ться</b> cạo râu xong</div>'
)

# --------------------------------------------------------------------- зажигалка
S["зажигалка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">BẮT ĐẦU</span></div>'
    '<div class="hd-row"><span class="hd-piece">-жиг-а-</span>'
    '<span class="hd-gloss">ĐỐT — cùng gốc <i>жг-/жег-/жог-</i> của <b>жечь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-лка</span>'
    '<span class="hd-gloss">đồ vật LÀM việc đó, giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>зажига́ть</b> = châm lửa, thắp ⇒ cái để châm lửa. Thay <i>-ть</i> '
    'bằng <b>-лка</b> là ra đồ dùng: <b>открыва́ть</b> mở → <b>открыва́лка</b> cái mở nắp. '
    'Cách 2 số nhiều chen <b>о</b>: <b>зажига́лок</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>зажига́ть</b> / <b>заже́чь</b> châm, thắp · <b>жечь</b> đốt · '
    '<b>ожо́г</b> vết bỏng</div>'
)

# --------------------------------------------------------------------- бытовой
S["бытовой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">быт-</span>'
    '<span class="hd-gloss"><b>быт</b> đời sống thường ngày — từ <i>бы-</i> TỒN TẠI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ово́й</span>'
    '<span class="hd-gloss">đuôi tính từ, tự mang trọng âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thuộc về <b>быт</b> ⇒ sinh hoạt, đời thường; đồ dùng cho sinh hoạt ⇒ '
    'gia dụng. Không có dạng ngắn, không so sánh: <b>бытовы́е пробле́мы</b> chuyện '
    'vặt đời thường.</div>'
    '<div class="hd-warn">Cụm hay gặp nhất: <b>бытова́я те́хника</b> = đồ điện gia dụng (biển '
    'hiệu cửa hàng).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>быт</b> đời sống thường ngày · <b>быть</b> là, có · '
    '<b>собы́тие</b> sự kiện</div>'
)

# --------------------------------------------------------------------- уютный
S["уютный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ую́т-</span>'
    '<span class="hd-gloss">danh từ <b>ую́т</b>: sự ấm cúng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ный</span>'
    '<span class="hd-gloss">đuôi tính từ: có thứ đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Có <b>ую́т</b> ⇒ ấm cúng: <b>ую́тная кварти́ра</b>. Khác '
    '<b>удо́бный</b> (tiện, vừa người): ghế ngồi êm thì <b>удо́бный</b>, căn phòng ấm áp thì '
    '<b>ую́тный</b>. Trọng âm đứng yên, dạng ngắn giống đực chen <b>е</b>: <b>ую́тен</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: <b>ую́т</b> và <b>прию́т</b> (nơi nương thân) cùng gốc '
    '<i>-ют-</i> «chỗ trú» — là từ nguyên, không phải luật suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ую́т</b> sự ấm cúng · <b>ую́тно</b> thật ấm cúng · '
    '<b>неую́тный</b> lạnh lẽo, thiếu ấm cúng · <b>прию́т</b> nơi nương thân</div>'
)

# --------------------------------------------------------------------- лак
S["лак"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ mượn, không chẻ được — cùng gốc với Anh <i>lacquer</i>: chất phủ '
    'BÓNG. Dùng cho cái gì thì <b>для</b> + cách 2 chỉ rõ: <b>лак для '
    'ногте́й</b> sơn móng tay · <b>лак для ме́бели</b> véc ni đồ gỗ.</div>'
    '<div class="hd-warn"><b>лак</b> là lớp bóng (thường trong suốt); sơn MÀU quét tường, quét '
    'cửa là <b>кра́ска</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ла́ковый</b> thuộc sơn bóng, bóng loáng · <b>лакирова́ть</b> đánh '
    'véc ni</div>'
)

# --------------------------------------------------------------------- кран
S["кран"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ mượn (Hà Lan <i>kraan</i>), không chẻ được. Hai nghĩa là hai đồ vật '
    'khác hẳn: VÒI nước và CẦN CẨU — nghĩa sau gặp lại ở Anh <i>crane</i>. Muốn rõ là cần cẩu '
    'thì thêm tính từ: <b>подъёмный кран</b> («vòi» để NÂNG).</div>'
    '<div class="hd-warn">Vòi nước thì «mở/đóng» như cửa: <b>откры́ть кран</b>, <b>закры́ть '
    'кран</b>. Nước máy = <b>вода́ из-под кра́на</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>крановщи́к</b> người lái cần cẩu (<i>-щик</i> = người làm nghề)</div>'
)

# --------------------------------------------------------------------- кондиционер
S["кондиционер"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кондицион-</span>'
    '<span class="hd-gloss">gốc mượn ≈ Anh <i>condition</i>: đưa về TRẠNG THÁI đúng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ер</span>'
    '<span class="hd-gloss">≈ Anh <i>-er</i>: người / máy làm việc đó, giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>conditioner</i>, và giữ đủ hai nghĩa: thứ chỉnh KHÔNG KHÍ '
    'về độ dễ chịu ⇒ máy điều hoà; thứ chỉnh TÓC cho mềm ⇒ dầu xả (<b>нанести́ кондиционе́р '
    'на во́лосы</b> bôi dầu xả lên tóc). Trọng âm rơi vào đuôi <b>-е́р</b>.</div>'
    '<div class="hd-warn">Bật/tắt máy: <b>включи́ть</b> / <b>вы́ключить кондиционе́р</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кондициони́рование</b> sự điều hoà (không khí)</div>'
)

# --------------------------------------------------------------------- быт
S["быт"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бы-</span>'
    '<span class="hd-gloss">TỒN TẠI — <b>быть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-т</span>'
    '<span class="hd-gloss">biến động từ thành danh từ, giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cách người ta «tồn tại» mỗi ngày ⇒ ăn ở, cơm nước, nếp sinh hoạt. Hẹp '
    'hơn <b>жизнь</b> (cả cuộc đời): <b>семе́йный быт</b> nếp sinh hoạt gia đình. Không có số '
    'nhiều.</div>'
    '<div class="hd-warn">Cách 6 có hai dạng: <b>о бы́те</b> (nói VỀ) nhưng <b>в быту́</b> '
    '(TRONG đời thường) — đuôi <b>-у́</b> mang trọng âm, như <b>в саду́, в лесу́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бытово́й</b> đời thường, gia dụng · <b>быть</b> là, có · '
    '<b>собы́тие</b> sự kiện · <b>бытие́</b> sự tồn tại</div>'
)

# --------------------------------------------------------------------- почистить
S["почистить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố thể, KHÔNG mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-чист-</span>'
    '<span class="hd-gloss">SẠCH, thuần — <b>чи́стый</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai: LÀM CHO như thế</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp HT của <b>чи́стить</b> — làm sạch XONG: <b>почи́стить зу́бы</b> '
    'đánh răng xong, <b>почи́стить карто́шку</b> gọt xong khoai. Chỉ «tôi» biến âm '
    '<b>ст → щ</b>: <b>я почи́щу</b>, <b>ты почи́стишь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>чи́стить</b> (CHT) · <b>чи́стый</b> sạch · <b>очи́стить</b> tẩy '
    'sạch, lọc sạch · <b>чистота́</b> sự sạch sẽ</div>'
)

# --------------------------------------------------------------------- чистить
S["чистить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">чист-</span>'
    '<span class="hd-gloss">SẠCH, thuần — <b>чи́стый</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai: LÀM CHO như thế</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm cho sạch bằng cách CỌ hoặc BỎ lớp ngoài — nên tiếng Việt đổi theo '
    'đồ vật: <b>чи́стить зу́бы</b> đánh răng · <b>о́бувь</b> đánh giày · <b>карто́шку</b> gọt '
    'khoai · <b>ры́бу</b> đánh vảy cá. Rửa bằng NƯỚC thì là <b>мыть</b>.</div>'
    '<div class="hd-warn">Chỉ «tôi» biến âm <b>ст → щ</b>: <b>я чи́щу</b>, <b>ты '
    'чи́стишь</b> — đúng phép biến âm của <b>чи́стый → чи́ще</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>почи́стить</b> (HT) · <b>чи́стый</b> sạch · <b>чи́стка</b> sự làm '
    'sạch · <b>химчи́стка</b> giặt khô</div>'
)

# --------------------------------------------------------------------- химчистка
S["химчистка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">хим-</span>'
    '<span class="hd-gloss">viết tắt của <b>хими́ческая</b> HOÁ HỌC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-чист-</span>'
    '<span class="hd-gloss">SẠCH, thuần — <b>чи́стить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">→ danh từ chỉ việc (rồi chỉ nơi), giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Làm sạch bằng hoá chất» (không dùng nước) ⇒ giặt khô, rồi gọi luôn '
    'cửa hiệu. Ghép cắt đầu kiểu <b>зарпла́та</b> (= <b>за́работная пла́та</b>). Cách 2 số '
    'nhiều chen <b>о</b>: <b>химчи́сток</b>.</div>'
    '<div class="hd-warn">Cụm dùng thật: <b>отда́ть пальто́ в химчи́стку</b> = đem áo khoác đi '
    'giặt khô.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>чи́стка</b> sự làm sạch · <b>чи́стить</b> làm sạch · '
    '<b>хи́мия</b> hoá học · <b>хими́ческий</b> thuộc hoá học</div>'
)

# --------------------------------------------------------------------- осложнение
S["осложнение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">làm cho TRỞ NÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-слож-н-</span>'
    '<span class="hd-gloss"><b>сло́жный</b> phức tạp (<i>с-</i> LẠI VỚI NHAU + <i>-лож-</i> '
    'ĐẶT)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ chỉ việc, giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Việc trở nên phức tạp» ⇒ rắc rối thêm; trong y khoa: bệnh đẻ thêm bệnh '
    '⇒ biến chứng, hay dùng số nhiều: <b>осложне́ния по́сле гри́ппа</b> biến chứng sau '
    'cúm.</div>'
    '<div class="hd-warn">Biến chứng VÀO đâu thì <b>на</b> + cách 4: <b>осложне́ние на '
    'се́рдце</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>осложни́ть</b> làm phức tạp thêm · <b>сло́жный</b> phức tạp · '
    '<b>сло́жность</b> độ phức tạp · <b>сложи́ть</b> gộp, cộng</div>'
)

# --------------------------------------------------------------------- инфаркт
S["инфаркт"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ин-</span>'
    '<span class="hd-gloss">VÀO (Latin <i>in-</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-фаркт</span>'
    '<span class="hd-gloss">NHỒI (Latin <i>farcire</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là Anh <i>infarct</i>; tiếng Việt «NHỒI máu» dịch đúng từng mảnh. '
    'Tên đủ: <b>инфа́ркт миока́рда</b> nhồi máu cơ tim, nhưng nói trống <b>инфа́ркт</b> là hiểu '
    'ngay tim: <b>у него́ инфа́ркт</b>.</div>'
    '<div class="hd-warn">Thứ tự chữ là <i>-арк-</i>: viết hay đọc thành <i>-рак-</i> là lỗi '
    'kinh điển.</div>'
    '<div class="hd-warn">Đừng lẫn <b>инсу́льт</b> = đột quỵ, tai biến NÃO.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>фарш</b> thịt băm, nhân nhồi (họ xa, từ <i>farcire</i> qua tiếng '
    'Pháp <i>farce</i>)</div>'
)

# --------------------------------------------------------------------- витамин
S["витамин"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вит-</span>'
    '<span class="hd-gloss">SỰ SỐNG (Latin <i>vita</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-амин</span>'
    '<span class="hd-gloss">amin, tên một nhóm chất hoá học</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ ghép của nhà khoa học đầu thế kỷ 20: «chất amin cần cho sự sống». '
    'Giống đực, hay dùng số nhiều: <b>пить витами́ны</b> uống vitamin, <b>витами́н C</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: Latin <i>vita</i> và <b>жить</b> (sống, <b>живу́</b>) cùng '
    'gốc Ấn–Âu xa — từ nguyên, không phải luật suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>витами́нный</b> thuộc vitamin, giàu vitamin · '
    '<b>авитамино́з</b> chứng thiếu vitamin</div>'
)

B = {
    "docbangmat": 118, "loitubat": 4, "nguonsai": 8,
    "baolen": [
        "V cần duyệt (11 thẻ): пирожо́к «bánh nhỏ có nhân, bánh bao nướng»; омле́т bỏ «trứng chiên», thêm «trứng tráng»; изба́ bỏ «lều»; зажига́лка bỏ «bom cháy» (có trong gloss nhưng không thông dụng); бытово́й + «gia dụng»; ую́тный bỏ «thoải mái»; кран + «cần cẩu»; быт bỏ «chuyện nhà cửa»; чи́стить/почи́стить «làm sạch, chải, chà, đánh bóng, gọt vỏ» (bỏ «đánh răng» vì là nghĩa của cụm с зу́бы — đã dạy ở Hướng dẫn); витами́н chỉ còn «vitamin». 11 thẻ còn lại giữ đề cũ.",
        "Nguồn sai đã bác (8 đề tiếng Việt cũ): пирожок, омлет, изба, уютный, быт, чистить, почистить, витамин — lý do ở chú thích dict V.",
        "Va chạm nghĩa: máy báo 0 với đề CŨ; chưa chạy lại với V mới (không đụng Anki). ку́шать giữ «ăn, dùng cơm»; chung «ăn» với есть/съесть là bình thường.",
        "Bỏ cụm «для воло́с» ở лак và кондиционе́р: cách 2 số nhiều воло́с là ĐÚNG nhưng nouns.csv chỉ có cách 1 во́лос nên cửa kêu oan; đổi ví dụ, không nới MIEN_TRU.",
        "Chỗ KHÔNG chắc: ку́шать ↔ вкус, изба́ ↔ Stube/stove, ую́т ↔ прию́т, vita ↔ жить là từ nguyên, đã ghi ⚠️ Mức tin. Quá khứ нали́ть: bảng ghi нали́л, chuẩn cũng nhận на́лил; trên thẻ theo bảng.",
        "Lệch khuôn cũ có sẵn: -лож- là ĐẶT ở сло́жный (k123) nhưng NẰM ở положи́ть (k95)/сложи́ть; осложне́ние theo k123 như bối cảnh giao. Không sửa thẻ cũ.",
    ],
}
