# -*- coding: utf-8 -*-
"""k214 — qualities (lô trộn): tính chất, chất liệu, danh từ chỉ phẩm chất.

Chỗ cần nhất quán trong lô:
(1) ко́жаный một н / стекля́нный hai н — hai thẻ nhắc nhau, khuôn theo деревя́нный, стекло́ đã có.
(2) Từ mượn -альный: принципиа́льный, потенциа́льный, актуа́льный — mỗi thẻ chỉ nói bẫy nghĩa riêng.
(3) -год- của вы́годный giữ đúng lời thẻ пого́да («lúc thuận, hợp»); -чёт- của почётный nối предпочита́ть.
(4) схо́дство: -ход- như похо́жий, đã in trên thẻ похо́жий.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "пена": "bọt, váng",                                       # «bong bóng» = пузы́рь, gloss không có
    "гигантский": "khổng lồ, đồ sộ",                           # gỡ bao trùm огро́мный; «vĩ đại» là вели́кий, gloss không có
    "коллективный": "tập thể, chung",                          # «cộng đồng» gloss không có
    "качественный": "chất lượng cao, có chất lượng, về chất",  # «tốt» gloss không có; qualitative thì có (cụm cố định)
    "искусственный": "nhân tạo, giả, tổng hợp, gượng gạo",     # gloss affected/forced; «không tự nhiên» là lời phủ định
    "стеклянный": "bằng thủy tinh, bằng kính",                 # «đờ đẫn» nghĩa bóng, gloss không có
    "выгодный": "có lợi, hời, thuận lợi, sinh lời",            # «lợi nhiều» lủng củng; gloss profitable/lucrative
}

# ---------------------------------------------------------------------- пена
S["пена"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — <i>пен-</i> BỌT là gốc trơn, chỉ thêm đuôi giống cái <i>-а</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mọi thứ bọt nổi trên mặt: bọt bia, bọt xà phòng, váng khi nấu súp. '
    'Trọng âm luôn ở gốc. Gặp hằng ngày: <b>пе́на для бритья́</b> bọt cạo râu.</div>'
    '<div class="hd-warn">Bong bóng (từng quả tròn) là <b>пузы́рь</b>, không phải <b>пе́на</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пе́нка</b> lớp váng (sữa nóng, cà phê) · <b>пе́ниться</b> sủi bọt</div>'
)

# ----------------------------------------------------------------- укрепление
S["укрепление"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">LÀM CHO thành ra thế</span></div>'
    '<div class="hd-row"><span class="hd-piece">-креп-л-</span>'
    '<span class="hd-gloss">CHẮC, VỮNG — như <b>кре́пкий</b>; <i>п</i> thêm <i>л</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ chỉ việc, giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Việc làm cho vững chắc» ⇒ sự củng cố, tăng cường: '
    '<b>укрепле́ние здоро́вья</b> tăng cường sức khoẻ. Số nhiều <b>укрепле́ния</b> '
    'thường là công sự phòng thủ — thứ đã được làm cho vững.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>укрепи́ть</b> / <b>укрепля́ть</b> củng cố · <b>кре́пкий</b> chắc, đậm · '
    '<b>кре́пость</b> pháo đài</div>'
)

# ----------------------------------------------------------------- гигантский
S["гигантский"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">гига́нт-</span>'
    '<span class="hd-gloss">NGƯỜI KHỔNG LỒ — mượn gốc Hy Lạp, = <i>giant</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ск-ий</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cỡ người khổng lồ» = tiếng Anh <i>gigantic</i>. Mạnh và giàu hình ảnh hơn '
    '<b>огро́мный</b> — từ «rất to» dùng hằng ngày. '
    '<b>гига́нтскими шага́ми</b> = bằng những bước khổng lồ (tiến rất nhanh).</div>'
    '<div class="hd-warn">✍️ Giữ chữ <i>т</i> của <b>гига́нт</b> trước <i>-ск-</i>: gõ <i>-нтск-</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гига́нт</b> người khổng lồ, «ông lớn»</div>'
)

# -------------------------------------------------------------------- кожаный
S["кожаный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ко́ж-</span>'
    '<span class="hd-gloss">DA — <b>ко́жа</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ан-ый</span>'
    '<span class="hd-gloss">đuôi tính từ chất liệu «làm bằng»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Da + «làm bằng» ⇒ bằng da: <b>ко́жаная ку́ртка</b> áo khoác da, '
    '<b>ко́жаный дива́н</b> ghế sofa da. Đuôi <i>-ан-/-ян-</i> chất liệu viết MỘT <i>н</i>, '
    'như <b>сере́бряный</b> bằng bạc.</div>'
    '<div class="hd-warn"><b>ко́жаный</b> = làm từ da thuộc; <b>ко́жный</b> = thuộc về da người: '
    '<b>ко́жный врач</b> bác sĩ da liễu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ко́жа</b> da · <b>ко́жный</b> thuộc da người</div>'
)

# --------------------------------------------------------------- коллективный
S["коллективный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">коллекти́в-</span>'
    '<span class="hd-gloss">TẬP THỂ — từ mượn <b>коллекти́в</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ứng đúng với tính từ <i>collective</i> tiếng Anh: '
    '<b>коллекти́вная рабо́та</b> việc làm tập thể, <b>коллекти́вный догово́р</b> thoả ước tập thể. '
    'Trạng từ <b>коллекти́вно</b>. Dạng ngắn giống đực chen <i>е</i>: <b>коллекти́вен</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>коллекти́в</b> tập thể · <b>колле́кция</b> bộ sưu tập</div>'
)

# --------------------------------------------------------------- качественный
S["качественный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ка́ч-еств-</span>'
    '<span class="hd-gloss">CHẤT LƯỢNG — <b>ка́чество</b>, từ <i>как</i> «thế nào» (<i>к→ч</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-енн-ый</span>'
    '<span class="hd-gloss">đuôi tính từ, hai <i>н</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nói về hàng hoá, công việc thì tự nó đã là khen: '
    '<b>ка́чественные това́ры</b> hàng chất lượng cao. Trạng từ <b>ка́чественно</b> '
    '(làm) kỹ, tốt.</div>'
    '<div class="hd-warn">Nghĩa thứ hai: «về CHẤT» (đối lại <b>коли́чественный</b> về lượng) — '
    '<b>ка́чественный скачо́к</b> bước nhảy vọt về chất.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ка́чество</b> chất lượng · <b>нека́чественный</b> kém chất lượng · '
    '<b>како́й</b> thế nào</div>'
)

# -------------------------------------------------------------- искусственный
S["искусственный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ис-кус-ств-</span>'
    '<span class="hd-gloss">TÀI KHÉO — <b>иску́сство</b>: <i>ис-</i> RA + <i>-кус-</i> THỬ, NẾM</span></div>'
    '<div class="hd-row"><span class="hd-piece">-енн-ый</span>'
    '<span class="hd-gloss">đuôi tính từ, hai <i>н</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Do tay khéo con người làm chứ không mọc tự nhiên ⇒ nhân tạo. Tiếng Anh y hệt: '
    '<i>art</i> → <i>artificial</i>. Trái nghĩa: <b>есте́ственный</b> tự nhiên. Với nụ cười, '
    'cử chỉ ⇒ gượng gạo. Dạng ngắn giống đực chen <i>е</i>: <b>иску́сственен</b>.</div>'
    '<div class="hd-warn"><b>иску́сственный интелле́кт</b> (ИИ) = trí tuệ nhân tạo, AI.</div>'
    '<div class="hd-warn">✍️ Hai chữ <i>с</i> (như <b>иску́сство</b>), rồi hai chữ <i>н</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>иску́сство</b> nghệ thuật · <b>иску́сный</b> khéo tay, lành nghề · '
    '<b>вкус</b> vị</div>'
)

# ----------------------------------------------------------------- стеклянный
S["стеклянный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">стекл-</span>'
    '<span class="hd-gloss">KÍNH, THUỶ TINH — <b>стекло́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́нн-ый</span>'
    '<span class="hd-gloss">đuôi tính từ chất liệu «làm bằng»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Kính + «làm bằng»: <b>стекля́нная буты́лка</b> chai thuỷ tinh, '
    '<b>стекля́нная дверь</b> cửa kính. Trọng âm rơi vào đuôi <i>-я́нн-</i>. '
    'Dạng ngắn (<b>стекля́нен</b>, chen <i>е</i>) hầu như không dùng.</div>'
    '<div class="hd-warn">✍️ HAI chữ <i>н</i> — ngoại lệ phải thuộc, cùng <b>деревя́нный</b> bằng gỗ; '
    'còn <b>ко́жаный</b>, <b>сере́бряный</b> chỉ một.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>стекло́</b> kính, thuỷ tinh · <b>стеко́льщик</b> thợ lắp kính</div>'
)

# ------------------------------------------------------------------- оригинал
S["оригинал"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga — mượn quốc tế (Latin <i>originalis</i> '
    '«thuộc nguồn gốc»), = <i>original</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái có từ nguồn ⇒ bản gốc, đối lại <b>ко́пия</b> bản sao. Trọng âm ở cuối: '
    '<b>оригина́л</b>. Nghĩa thứ hai: người chẳng giống ai ⇒ người lập dị.</div>'
    '<div class="hd-warn"><b>в оригина́ле</b> = bằng nguyên tác: <b>чита́ть Че́хова в оригина́ле</b> '
    'đọc Chekhov bằng tiếng Nga gốc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оригина́льный</b> độc đáo · <b>оригина́льно</b> một cách độc đáo</div>'
)

# ------------------------------------------------------------------- сходство
S["сходство"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">LẠI MỘT CHỖ, nhập vào nhau</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ход-</span>'
    '<span class="hd-gloss">ĐI — gốc của <b>ходи́ть</b>, cũng là <i>-хож-</i> trong <b>похо́жий</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ство</span>'
    '<span class="hd-gloss">danh từ trừu tượng, giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>сходи́ться</b> = đi lại một chỗ, khớp nhau. Hai thứ «khớp vào nhau» '
    '⇒ nét giống nhau.</div>'
    '<div class="hd-warn">Giống VỚI ai: <i>с</i> + cách 5 — <b>схо́дство с отцо́м</b>; giống GIỮA hai bên: '
    '<b>схо́дство ме́жду бра́тьями</b>. (Tính từ <b>похо́жий</b> thì lại đi với <i>на</i> + cách 4.)</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>схо́дный</b> tương tự · <b>похо́жий</b> giống · '
    '<b>сходи́ться</b> gặp nhau, khớp nhau</div>'
)

# ----------------------------------------------------------------------- сорт
S["сорт"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — từ mượn châu Âu, cùng gốc tiếng Anh <i>sort</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Loại hàng hoá, giống cây trồng: <b>сорт я́блок</b> giống táo, <b>сорт сы́ра</b> '
    'loại phô mai — danh từ theo sau ở cách 2. Từ «loại» thành «hạng»: '
    '<b>пе́рвый сорт</b> hạng nhất, <b>вы́сший сорт</b> thượng hạng.</div>'
    '<div class="hd-warn">Số nhiều bất thường, trọng âm ra đuôi <i>-а́</i>: <b>сорта́</b>, <b>сорто́в</b>.</div>'
    '<div class="hd-warn">Chủ yếu cho HÀNG và GIỐNG CÂY; loại nói chung (môn thể thao, loài vật…) là '
    '<b>вид</b>: <b>вид спо́рта</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сортирова́ть</b> phân loại · <b>ассортиме́нт</b> các mặt hàng có bán</div>'
)

# ------------------------------------------------------------------ по-разному
S["по-разному"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">THEO (kiểu)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ра́зн-</span>'
    '<span class="hd-gloss">KHÁC NHAU — <b>ра́зный</b> (<i>раз-</i> tản ra mỗi hướng)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ому</span>'
    '<span class="hd-gloss">đuôi cách 3 của tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Theo kiểu khác nhau» ⇒ mỗi người, mỗi lúc một kiểu. Cùng khuôn '
    '<b>по-друго́му</b>, <b>по-пре́жнему</b> — luôn có gạch nối. '
    '<b>Все ду́мают по-ра́зному.</b> Mỗi người nghĩ một kiểu.</div>'
    '<div class="hd-warn"><b>по-ра́зному</b> = nhiều kiểu, so với NHAU; <b>по-друго́му</b> = '
    'theo một kiểu KHÁC, không phải kiểu này.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ра́зный</b> khác nhau · <b>ра́зница</b> sự chênh lệch · '
    '<b>разнообра́зный</b> đa dạng</div>'
)

# -------------------------------------------------------------- перспективный
S["перспективный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">перспекти́в-</span>'
    '<span class="hd-gloss">TRIỂN VỌNG — <b>перспекти́ва</b> (Latin «nhìn xuyên ra xa»)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhìn ra xa thấy còn đường đi tới ⇒ có triển vọng: '
    '<b>перспекти́вный сотру́дник</b> nhân viên nhiều hứa hẹn, <b>перспекти́вный план</b> '
    'kế hoạch dài hạn. Dạng ngắn giống đực chen <i>е</i>: <b>перспекти́вен</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>перспекти́ва</b> triển vọng, viễn cảnh · '
    '<b>бесперспекти́вный</b> không có tương lai</div>'
)

# ------------------------------------------------------------------- выгодный
S["выгодный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span>'
    '<span class="hd-gloss">tiền tố (nghĩa thường là RA)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-год-</span>'
    '<span class="hd-gloss">gốc cổ: lúc thuận, HỢP — như <b>пого́да</b>, <b>го́дный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dựng từ <b>вы́года</b> «cái lợi» (thứ thuận cho mình) ⇒ có lợi, hời: '
    '<b>вы́годная цена́</b> giá hời. Trọng âm đứng yên ở <i>вы́-</i>; dạng ngắn giống đực '
    'chen <i>е</i>: <b>вы́годен</b>. Có lợi CHO AI: cách 3 — <b>Мне э́то вы́годно.</b></div>'
    '<div class="hd-warn">⚠️ Mức tin: nối <i>-год-</i> với «lúc thuận, hợp» là từ nguyên, '
    'không phải luật suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вы́года</b> cái lợi · <b>вы́годно</b> có lợi · '
    '<b>невы́годный</b> bất lợi, không lời · <b>го́дный</b> dùng được, hợp</div>'
)

# ------------------------------------------------------------------- почётный
S["почётный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-чёт-</span>'
    '<span class="hd-gloss">COI TRỌNG — cùng gốc <b>честь</b> danh dự, '
    '<i>-чит-</i> trong <b>предпочита́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ <b>почёт</b> «sự kính trọng» ⇒ được kính trọng, danh dự: '
    '<b>почётный гость</b> khách danh dự, <b>почётное ме́сто</b> chỗ ngồi trang trọng. '
    'Dạng ngắn giống đực chen <i>е</i>: <b>почётен</b>.</div>'
    '<div class="hd-warn">Đừng lẫn với <b>че́стный</b>: cùng gốc nhưng là «trung thực». '
    'Và không liên quan <b>по́чта</b> bưu điện.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>почёт</b> sự kính trọng · <b>честь</b> danh dự · '
    '<b>че́стный</b> trung thực</div>'
)

# ------------------------------------------------------------- принципиальный
S["принципиальный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">принцип-и-</span>'
    '<span class="hd-gloss">NGUYÊN TẮC — <b>при́нцип</b> (Latin <i>principium</i> «khởi đầu»)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́льн-ый</span>'
    '<span class="hd-gloss">đuôi tính từ của từ quốc tế (<i>-al</i>), kéo trọng âm về nó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thuộc về nguyên tắc». Nói người ⇒ có nguyên tắc: <b>принципиа́льный челове́к</b>. '
    'Nói việc ⇒ đụng tới nền tảng, mấu chốt: <b>принципиа́льный вопро́с</b>, '
    '<b>принципиа́льная ра́зница</b> khác biệt cơ bản. '
    'Dạng ngắn giống đực: <i>ь</i> được thay bằng <i>е</i> — <b>принципиа́лен</b>.</div>'
    '<div class="hd-warn">Không phải tiếng Anh <i>principal</i> «chủ yếu, chính» — cái đó là <b>гла́вный</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>при́нцип</b> nguyên tắc · <b>принципиа́льно</b> về nguyên tắc · '
    '<b>беспринци́пный</b> vô nguyên tắc</div>'
)

# -------------------------------------------------------------- потенциальный
S["потенциальный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">потенци-</span>'
    '<span class="hd-gloss">KHẢ NĂNG còn ẩn — Latin <i>potentia</i> «sức, khả năng»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́льн-ый</span>'
    '<span class="hd-gloss">đuôi tính từ của từ quốc tế (<i>-al</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= tiếng Anh <i>potential</i>: chưa thành nhưng có thể thành — '
    '<b>потенциа́льный покупа́тель</b> khách hàng tiềm năng, <b>потенциа́льная опа́сность</b> '
    'mối nguy tiềm ẩn. Dạng ngắn giống đực: <i>ь</i> được thay bằng <i>е</i> — <b>потенциа́лен</b>.</div>'
    '<div class="hd-warn">Tiếng Anh một chữ <i>potential</i> cho cả hai; tiếng Nga tách: danh từ là '
    '<b>потенциа́л</b> tiềm năng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>потенциа́л</b> tiềm năng (danh từ) · <b>потенциа́льно</b> một cách tiềm tàng</div>'
)

# ---------------------------------------------------------------- актуальный
S["актуальный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">акту-</span>'
    '<span class="hd-gloss">ĐANG DIỄN RA — Latin <i>actualis</i>, từ <i>actus</i> hành động '
    '(như <b>актёр</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́льн-ый</span>'
    '<span class="hd-gloss">đuôi tính từ của từ quốc tế (<i>-al</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đang diễn ra ngay lúc này ⇒ thời sự, cấp thiết, còn giá trị: '
    '<b>актуа́льная те́ма</b> đề tài thời sự, <b>актуа́льная информа́ция</b> thông tin còn mới. '
    'Dạng ngắn giống đực: <i>ь</i> được thay bằng <i>е</i> — <b>актуа́лен</b>; '
    '<b>Э́то ещё актуа́льно?</b> Cái này còn hiệu lực không?</div>'
    '<div class="hd-warn">BẠN GIẢ: không phải <i>actual</i> «thực sự» tiếng Anh — cái đó là '
    '<b>настоя́щий</b>, <b>факти́ческий</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>актуа́льность</b> tính thời sự · <b>акт</b> hành động; màn kịch · '
    '<b>акти́вный</b> tích cực, năng động</div>'
)

# --------------------------------------------------------------------- идеал
S["идеал"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga — từ mượn, = <i>ideal</i>; cùng ổ với <b>иде́я</b> ý tưởng.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thứ hoàn hảo tồn tại trong «ý tưởng» ⇒ lý tưởng, hình mẫu. Trọng âm ở cuối: '
    '<b>идеа́л</b>. <b>идеа́л красоты́</b> hình mẫu của cái đẹp; số nhiều <b>идеа́лы</b> = những lý tưởng sống.</div>'
    '<div class="hd-warn">Đây là DANH TỪ; «hoàn hảo» (tính từ) là <b>идеа́льный</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>идеа́льный</b> hoàn hảo · <b>иде́я</b> ý tưởng</div>'
)

# ------------------------------------------------------------------- BÁO CÁO
B = {
    "docbangmat": 87,
    "loitubat": 4,      # trọng âm «некаче́ственный» -> нека́чественный · dạng ngắn -альный viết «bỏ ь» -> ь thay bằng е (3 thẻ) · вы- của вы́годный gán nghĩa «thu được ra» (bịa) · сорт «chỉ dùng cho hàng» (quá tay)
    "nguonsai": 1,      # tiep in dạng ngắn стекля́нен như dạng sống; thực tế hầu như không dùng — thẻ nói rõ
    "baolen": [
        "Va chạm гигантский / огромный: gỡ bằng V гигантский «khổng lồ, đồ sộ» (bỏ «to lớn, vĩ đại»; «vĩ đại» là вели́кий, gloss không có). Vẫn chung «khổng lồ» — nghĩa chính, không cắt. Huge/enormous trong gloss cũng đọc được là «to lớn», nên CẦN DUYỆT việc bỏ chữ đó.",
        "V cần duyệt (6 thẻ còn lại): пена bỏ «bong bóng» · коллективный bỏ «cộng đồng» · качественный bỏ «tốt», thêm «về chất» (cụm ка́чественный скачо́к) · искусственный «không tự nhiên» -> «gượng gạo» (gloss affected/forced) · стеклянный bỏ «đờ đẫn» (nghĩa bóng, gloss không có) · выгодный «lợi nhiều» -> «sinh lời».",
        "укрепление giữ «công sự phòng thủ» dù gloss thẻ chỉ có strengthening: nouns.csv xác nhận fortification.",
        "KHÔNG CHẮC (từ nguyên, theo trí nhớ, không tra được trong repo): -год- của вы́годный (đã có ô Mức tin, giữ khớp thẻ пого́да) · сорт mượn châu Âu không chỉ rõ Pháp hay Đức.",
    ],
}
