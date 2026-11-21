# -*- coding: utf-8 -*-
"""k139 — people::professions: người (nghề, tầng lớp), dáng vẻ, cưới hỏi, món ăn.

Chỗ cần nhất quán trong lô:
(1) gốc лёт-/лет- = BAY (лётчик) — khớp лета́ть/лете́ть/самолёт (cũ), улете́ть (k141).
(2) gốc основ- = NỀN MÓNG (основа́тель) — khớp основа́ть (k142), основно́й (cũ).
(3) gốc жен- = VỢ (пожени́ться) — khớp жени́ться/жени́х/жена́ (cũ).
(4) gốc друг-/друж- = BẠN, г → ж (дружи́ть) — khớp дру́жный (cũ).
(5) корми́ть ↔ накорми́ть: cặp thể; м → мл ở ngôi «я».
Họ hàng cố ý vắng: балко́н (từ mượn đứng một mình).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "зарубежный": "hải ngoại, ở nước ngoài",   # trùng cả 2 nghĩa với иностра́нный (đã nạp); gloss «abroad»
    "деятель": "nhân vật, nhà hoạt động",     # bỏ ngoặc «(xã hội)»
    "накормить": "cho ăn, cho ăn no",          # bỏ ngoặc «(đã no)»; gloss «to satisfy (with food)»
}

# ----------------------------------------------------------------- седой
S["седой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сед-</span>'
    '<span class="hd-gloss">BẠC (tóc, râu)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́й</span>'
    '<span class="hd-gloss">đuôi tính từ mang trọng âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Màu của tóc người già: <b>седы́е во́лосы</b> tóc bạc, <b>седо́й '
    'стари́к</b> ông già tóc bạc. Dạng ngắn: giống cái trọng âm ra đuôi <b>седа́</b>, '
    'số nhiều lại về gốc <b>се́ды</b>.</div>'
    '<div class="hd-warn">Áo, trời màu xám là <b>се́рый</b> — <b>седо́й</b> chỉ dành cho '
    'tóc, râu, lông.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>седина́</b> tóc bạc, sợi bạc · <b>седе́ть</b> bạc dần · '
    '<b>поседе́ть</b> bạc tóc</div>'
)

# ----------------------------------------------------------------- худой
S["худой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">худ-</span>'
    '<span class="hd-gloss">GẦY, kém, tệ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́й</span>'
    '<span class="hd-gloss">đuôi tính từ mang trọng âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc là «kém» — vì thế <b>ху́же</b> (tệ hơn) là dạng so sánh '
    'của <b>плохо́й</b>. Thân «kém thịt» ⇒ gầy; đồ «kém» ⇒ rách, thủng: <b>худы́е '
    'сапоги́</b> ủng thủng. Dạng ngắn giống cái kéo trọng âm ra đuôi: <b>худа́</b>.</div>'
    '<div class="hd-warn">Người gầy là <b>худо́й</b>; vật mỏng (giấy, lát bánh) là '
    '<b>то́нкий</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>худе́ть</b> gầy đi · <b>похуде́ть</b> giảm cân · '
    '<b>ху́же</b> tệ hơn · <b>ху́дший</b> tệ nhất</div>'
)

# ----------------------------------------------------------------- бледный
S["бледный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бле́д-</span>'
    '<span class="hd-gloss">NHỢT, mất màu</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mặt mất màu ⇒ xanh xao; màu sắc mất độ đậm ⇒ nhạt. Dạng ngắn giống '
    'đực chèn <b>е</b> giữa <b>д</b> và <b>н</b>: <b>бле́ден</b>; trọng âm đứng yên ở gốc '
    'cả bảng.</div>'
    '<div class="hd-warn">Ghép trước màu = màu NHẠT: <b>бле́дно-голубо́й</b> xanh da trời '
    'nhạt.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бледне́ть</b> tái đi · <b>побледне́ть</b> tái mặt</div>'
)

# ----------------------------------------------------------------- усы
S["усы"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ус-</span>'
    '<span class="hd-gloss">RIA (một bên)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ы́</span>'
    '<span class="hd-gloss">đuôi số nhiều</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một <b>ус</b> là một bên ria (giống đực) ⇒ cả bộ râu mép là hai bên, '
    'nên từ này gần như luôn ở số nhiều. Râu mèo, râu tôm cũng gọi bằng chính nó. '
    'Số nhiều trọng âm nằm ở đuôi: <b>усо́в</b>, <b>уса́ми</b>.</div>'
    '<div class="hd-warn">Râu CẰM là <b>борода́</b> — khác gốc, thuộc riêng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уса́тый</b> có ria (khuôn <b>-атый</b> như <b>борода́тый</b> '
    'có râu)</div>'
)

# ----------------------------------------------------------------- пожениться
S["пожениться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố thể hoàn thành — không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-жен-</span>'
    '<span class="hd-gloss">VỢ (<b>жена́</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-ть-ся</span>'
    '<span class="hd-gloss">đuôi động từ + <b>-ся</b> «với nhau»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cả HAI người cưới nhau ⇒ chủ ngữ luôn số nhiều: <b>Они́ '
    'пожени́лись</b>, <b>Мы поже́нимся ле́том</b>. Trọng âm lùi về gốc ở thì tương lai: '
    '<b>поже́нимся</b>.</div>'
    '<div class="hd-warn">Một người thì đổi từ: đàn ông <b>жени́ться на</b> + cách 6, '
    'phụ nữ <b>вы́йти за́муж за</b> + cách 4.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>жени́ться</b> lấy vợ · <b>жена́</b> vợ · <b>жени́х</b> chú rể · '
    '<b>жена́тый</b> đã có vợ</div>'
)

# ----------------------------------------------------------------- зарубежный
S["зарубежный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">BÊN KIA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-рубе́ж-</span>'
    '<span class="hd-gloss">ranh giới, biên giới (<b>рубе́ж</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Ở bên kia biên giới» ⇒ hải ngoại: <b>зарубе́жные стра́ны</b>. '
    'Cùng khuôn với cụm <b>за рубежо́м</b> = ở nước ngoài (như <b>за грани́цей</b>).</div>'
    '<div class="hd-warn">Ngoại ngữ luôn là <b>иностра́нный язы́к</b>, người nước ngoài là '
    '<b>иностра́нец</b> — <b>зарубе́жный</b> dùng cho cái NẰM bên ngoài: nước, báo chí, '
    'đối tác.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рубе́ж</b> ranh giới · <b>за рубежо́м</b> ở nước ngoài · '
    '<b>из-за рубежа́</b> từ nước ngoài</div>'
)

# ----------------------------------------------------------------- дружить
S["дружить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">друж-</span>'
    '<span class="hd-gloss">BẠN (<b>друг</b>, г → ж)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-ть</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Làm <b>друг</b> của nhau» ⇒ là bạn, chơi thân. Trọng âm '
    '<b>дружу́</b> ở đuôi, các ngôi khác lùi về gốc: <b>дру́жишь</b>.</div>'
    '<div class="hd-warn">Thân VỚI AI: <b>с</b> + cách 5 — <b>Я дружу́ с Ма́шей</b>. '
    'Mới kết bạn (một lần) là <b>подружи́ться</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>друг</b> bạn · <b>дру́жба</b> tình bạn · <b>подру́га</b> bạn gái · '
    '<b>дру́жный</b> hoà thuận</div>'
)

# ----------------------------------------------------------------- лётчик
S["лётчик"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">лёт-</span>'
    '<span class="hd-gloss">gốc BAY (<b>лете́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-чик</span>'
    '<span class="hd-gloss">NGƯỜI làm việc đó (như <b>перево́дчик</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Người bay» ⇒ phi công. Gốc viết <b>ё</b> khi mang trọng âm '
    '(<b>лётчик</b>, <b>самолёт</b>, <b>полёт</b>), viết <b>е</b> khi không '
    '(<b>лета́ть</b>, <b>лете́ть</b>). Trọng âm đứng yên cả bảng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лета́ть</b> bay (nhiều chiều) · <b>лете́ть</b> bay (một chiều) · '
    '<b>самолёт</b> máy bay · <b>полёт</b> chuyến bay · <b>улете́ть</b> bay đi</div>'
)

# ----------------------------------------------------------------- моряк
S["моряк"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мор-</span>'
    '<span class="hd-gloss">BIỂN (<b>мо́ре</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́к</span>'
    '<span class="hd-gloss">NGƯỜI gắn với thứ đó (như <b>рыба́к</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Người của biển» ⇒ thuỷ thủ, người đi biển. Trọng âm nằm ở <b>-я́к</b>, '
    'hễ thêm đuôi là nhảy ra đuôi: <b>моряка́</b>, <b>моряки́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мо́ре</b> biển · <b>морско́й</b> thuộc về biển · '
    '<b>примо́рский</b> ven biển</div>'
)

# ----------------------------------------------------------------- крестьянин
S["крестьянин"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">крестья́н-</span>'
    '<span class="hd-gloss">dân quê (cả tầng lớp)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ин</span>'
    '<span class="hd-gloss">MỘT người — rụng ở số nhiều</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một người là <b>крестья́нин</b>, cả lớp người là <b>крестья́не</b> '
    '(rụng <b>-ин</b>, cùng khuôn <b>граждани́н</b> → <b>гра́ждане</b>); cách 2 số nhiều '
    'trụi hẳn đuôi: <b>крестья́н</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: đây là từ nguyên, không phải luật suy ra được — từ này '
    'tách ra từ <b>христиани́н</b> «tín đồ Cơ Đốc» (cùng họ với <b>крест</b> thánh giá).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>крестья́нка</b> nữ nông dân · <b>крестья́нский</b> thuộc nông dân · '
    '<b>крестья́нство</b> giai cấp nông dân</div>'
)

# ----------------------------------------------------------------- богатство
S["богатство"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бога́т-</span>'
    '<span class="hd-gloss">GIÀU (<b>бога́тый</b> = có của)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ств-о</span>'
    '<span class="hd-gloss">→ danh từ trừu tượng giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bỏ <b>-ый</b> của tính từ, thêm <b>-ство</b> ⇒ «cái giàu»: sự giàu '
    'có, của cải, cả sự phong phú — <b>бога́тство языка́</b>. Trọng âm đứng yên ở '
    '<b>-га́-</b>.</div>'
    '<div class="hd-warn">Số nhiều = tài nguyên: <b>приро́дные бога́тства</b> tài nguyên '
    'thiên nhiên.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бога́тый</b> giàu · <b>бога́ч</b> người giàu · '
    '<b>богате́ть</b> giàu lên</div>'
)

# ----------------------------------------------------------------- основатель
S["основатель"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">основ-</span>'
    '<span class="hd-gloss">NỀN MÓNG (<b>осно́ва</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́-тель</span>'
    '<span class="hd-gloss">NGƯỜI làm việc đó (như <b>писа́тель</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>основа́ть</b> = đặt nền → thành lập; bỏ <b>-ть</b>, thêm '
    '<b>-тель</b> ⇒ người đặt nền móng = người sáng lập: <b>основа́тель го́рода</b>, '
    '<b>основа́тель компа́нии</b>. Trọng âm đứng yên ở <b>-ва́-</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>основа́ть</b> thành lập · <b>осно́ва</b> nền tảng · '
    '<b>основно́й</b> cơ bản, chính · <b>основа́ние</b> sự thành lập, cơ sở</div>'
)

# ----------------------------------------------------------------- деятель
S["деятель"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">де́я-</span>'
    '<span class="hd-gloss">LÀM — động từ cổ <b>де́ять</b>, cùng gốc với <b>де́ло</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-тель</span>'
    '<span class="hd-gloss">NGƯỜI làm việc đó (như <b>учи́тель</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Người làm việc» — nhưng là việc lớn, việc chung, nên gần như luôn '
    'có từ đi kèm: <b>госуда́рственный де́ятель</b> chính khách, <b>де́ятель культу́ры</b> '
    'nhà hoạt động văn hoá.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>де́ятельность</b> hoạt động · <b>де́йствие</b> hành động · '
    '<b>де́ло</b> việc</div>'
)

# ----------------------------------------------------------------- закуска
S["закуска"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">KÈM sau (như <b>запи́ть</b> uống chiêu)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-кус-</span>'
    '<span class="hd-gloss">CẮN (<b>куса́ть</b>, <b>кусо́к</b> miếng)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-а</span>'
    '<span class="hd-gloss">→ danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Miếng cắn kèm sau ly rượu» ⇒ món nhắm; bày ra đầu bữa ⇒ món khai '
    'vị (thường số nhiều <b>заку́ски</b>). Cách 2 số nhiều chen <b>о</b>: '
    '<b>заку́сок</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>закуси́ть</b> ăn nhẹ, ăn nhắm · <b>кусо́к</b> miếng · '
    '<b>куса́ть</b> cắn</div>'
)

# ----------------------------------------------------------------- булочка
S["булочка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бу́л-</span>'
    '<span class="hd-gloss">ổ bánh mì trắng (<b>бу́лка</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-очк-а</span>'
    '<span class="hd-gloss">NHỎ, xinh — hậu tố giảm nhẹ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>бу́лка</b> → <b>бу́лочка</b>: chiếc bánh mì nhỏ, tròn, thường '
    'hơi ngọt. Cách 2 số nhiều chen <b>е</b>: <b>бу́лочек</b> (như <b>ка́рточка</b> → '
    '<b>ка́рточек</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бу́лка</b> ổ bánh mì trắng · <b>бу́лочная</b> tiệm bánh mì</div>'
)

# ----------------------------------------------------------------- свинина
S["свинина"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">свин-</span>'
    '<span class="hd-gloss">LỢN (<b>свинья́</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́н-а</span>'
    '<span class="hd-gloss">→ THỊT của con đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Con vật + <b>-ина</b> = thịt của nó — một khuôn mở khoá cả quầy thịt: '
    '<b>говя́дина</b> thịt bò, <b>бара́нина</b> thịt cừu. Trọng âm đứng yên ở '
    '<b>-и́н-</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>свинья́</b> con lợn · <b>свино́й</b> thuộc về lợn</div>'
)

# ----------------------------------------------------------------- кормить
S["кормить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">корм-</span>'
    '<span class="hd-gloss">THỨC ĂN (<b>корм</b> — thức ăn cho thú)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-ть</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đưa <b>корм</b> cho ai» ⇒ cho ăn, rồi nuôi. Ngôi «я» chen <b>л</b> '
    'sau <b>м</b>: <b>кормлю́</b>; các ngôi khác trọng âm lùi về gốc: <b>ко́рмишь</b>.</div>'
    '<div class="hd-warn">Cho AI ăn → cách 4, ăn GÌ → cách 5, không giới từ: '
    '<b>корми́ть ребёнка ка́шей</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>накорми́ть</b> cho ăn no (hoàn thành) · <b>покорми́ть</b> cho ăn '
    'một chút · <b>корми́лец</b> trụ cột nuôi nhà</div>'
)

# ----------------------------------------------------------------- накормить
S["накормить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">tạo thể hoàn thành, kèm chút nghĩa ĐỦ, NO (như <b>нае́сться</b> ăn no)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-корм-и-ть</span>'
    '<span class="hd-gloss">cho ăn (<b>корми́ть</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp hoàn thành của <b>корми́ть</b>: cho ăn xong, tới no — <b>накорми́ть '
    'дете́й обе́дом</b>. Chia y hệt: <b>накормлю́</b>, <b>нако́рмишь</b>; cách đòi cũng vậy '
    '(ai → cách 4, gì → cách 5).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>корми́ть</b> cho ăn · <b>покорми́ть</b> cho ăn một chút · '
    '<b>корм</b> thức ăn cho thú</div>'
)

# ----------------------------------------------------------------- балкон
S["балкон"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn, không chẻ được — qua tiếng Pháp <i>balcon</i>, cùng gốc với '
    'tiếng Anh <i>balcony</i>. Trọng âm đứng yên: <b>балко́на</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>балко́н</b> ≈ <i>balcony</i>, bỏ đuôi <i>-y</i>.</div>'
    '<div class="hd-warn">Ban công là mặt phẳng ⇒ dùng <b>на</b>, không dùng <b>в</b>: '
    '<b>на балко́не</b> trên ban công, <b>вы́йти на балко́н</b> ra ban công.</div>'
)

B = {
    "docbangmat": 89,
    "loitubat": 1,
    "nguonsai": 1,
    "baolen": [
        "V зарубежный: KHÔNG rút gọn được (cả 'nước ngoài' lẫn 'ngoại quốc' đều trùng иностра́нный) nên THAY bằng 'hải ngoại, ở nước ngoài' (gloss 'abroad') — cần duyệt.",
        "Nguồn sai: data/nouns.csv dòng pl_only 'усы' ghi accented у'сы, trái với chính cột pl_nom усы' của nó, dòng 'ус' và tudien.json (усы́). Không nới MIEN_TRU; tôi viết lại câu để không in đậm dạng cách 1 trần. Nên sửa nguồn.",
        "Trùng nghĩa để nguyên vì badge thể tách: 'cho ăn' кормить↔накормить, 'kết hôn' жениться↔пожениться.",
        "Mức tin: крестьянин ← христианин đã hạ mức tin bằng ô ⚠️; худой → хуже (so sánh của плохой) và деять cùng gốc дело viết thẳng vì tôi tin là chuẩn — nên soát.",
        "закуска: phân tích за- = 'kèm sau' (như запить) — mức tin vừa.",
        "балкон cố ý không có Họ hàng (từ mượn đứng một mình).",
        "Lỗi tự bắt: thẻ усы viết 'trọng âm ở đuôi cả bảng' — sai, số ít у́са ở gốc; đã sửa thành 'số nhiều'.",
    ],
}
