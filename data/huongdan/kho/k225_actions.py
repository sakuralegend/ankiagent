# -*- coding: utf-8 -*-
"""k225 — actions: 10 cặp thể + набирать, сэкономить; trục là GỐC + TIỀN TỐ.

Chỗ cần nhất quán với lô đã nạp:
(1) зажечь/зажигать: за- BẮT ĐẦU + жг-/жег-/жог-/жиг- ĐỐT — khớp зажигалка k213, ожог k203.
(2) съехать/съезжать: с- XUỐNG, RỜI KHỎI + е́х-/езж- ĐI XE — khớp съезд k52, съездить k82.
(3) впустить/впускать: пуск-/пуст- THẢ, BUÔNG — khớp отпустить k171, выпустить k185.
(4) уступить/уступать: у- RỜI KHỎI, ra xa (như уезжать k107) + -ступ- BƯỚC CHÂN (k97, k185).
(5) набирать: на- DỒN cho ĐẦY + -бир- LẤY — khớp набрать k206; V y hệt набрать.
(6) вручить: руч- TAY (к → ч) — khớp рука k32. (7) осветить: о- PHỦ KHẮP — khớp освещение k205.
(8) поправить: прав- THẲNG, ĐÚNG — khớp исправить k125, править k202.
(9) усложнить: у- làm cho TRỞ NÊN… — khớp улучшить k137, увеличить k195.
(10) расширить: рас- TRẢI RA KHẮP (k126) + шир- RỘNG — khớp широкий k61.
Họ hàng cố ý vắng: không có (mọi từ đều có họ thật).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "зажечь": "thắp, đốt, châm lửa, bật, truyền cảm hứng",              # + to inspire
    "зажигать": "thắp, đốt, châm lửa, bật, truyền cảm hứng",            # «bật lửa» đọc ra danh từ зажигалка
    "съезжать": "đi xuống, lái xuống, trượt xuống, dọn nhà đi, rời khỏi đường",   # + move out; turn off a road
    "съехать": "đi xuống, lái xuống, trượt xuống, dọn nhà đi, rời khỏi đường",    # + move out; come off the road
    "толкать": "đẩy, xô, huých, xúi giục, thúc đẩy",                    # + shove; incite / urge on
    "толкнуть": "đẩy, xô, huých, xúi giục, thúc đẩy",
    "впускать": "cho vào, cho phép vào, để cho vào",                    # «để vào» đọc ra «đặt vào»; «cho vô» lặp
    "впустить": "cho vào, cho phép vào, để cho vào",
    "уступать": "nhường, nhượng bộ, nhường chỗ, thua kém, bớt giá",     # + be inferior; come down in price
    "уступить": "nhường, nhượng bộ, nhường chỗ, thua kém, bớt giá",
    "набирать": "bấm số, gõ, gom, thu được, tích luỹ, tăng, tuyển",           # y hệt набрать k206
    "вручать": "trao, trao tận tay, giao, giao phó",                    # + entrust
    "вручить": "trao, trao tận tay, giao, giao phó",
    "осветить": "chiếu sáng, thắp sáng, soi sáng, làm sáng tỏ, đưa tin",   # + shed light on; cover
    "освещать": "chiếu sáng, thắp sáng, soi sáng, làm sáng tỏ, đưa tin",
}

# ---------------------------------------------------------------------- зажечь
S["зажечь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">BẮT ĐẦU</span></div>'
    '<div class="hd-row"><span class="hd-piece">-же́чь</span>'
    '<span class="hd-gloss">ĐỐT — chính là <b>жечь</b>, gốc <i>жг-/жег-/жог-/жиг-</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bắt đầu đốt ⇒ thắp, châm lửa; nghĩa bóng: «châm lửa» trong lòng người ⇒ '
    'truyền cảm hứng. Cặp CHT: <b>зажига́ть</b>.</div>'
    '<div class="hd-warn">Gốc lộ <i>г</i> ở hai đầu bảng chia: <b>зажгу́, зажгу́т</b>; ở giữa '
    '<i>г</i> → <i>ж</i> nên thành hai chữ ж: <b>зажжёшь, зажжёт</b>. Quá khứ: <b>зажёг, зажгла́, '
    'зажгли́</b>.</div>'
    '<div class="hd-warn"><b>заже́чь свет</b> = bật đèn; với máy móc thì dùng '
    '<b>включи́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>зажига́ть</b> (CHT) · <b>зажига́лка</b> bật lửa · <b>жечь</b> đốt · '
    '<b>ожо́г</b> vết bỏng</div>'
)

# -------------------------------------------------------------------- зажигать
S["зажигать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">BẮT ĐẦU</span></div>'
    '<div class="hd-row"><span class="hd-piece">-жиг-</span>'
    '<span class="hd-gloss">ĐỐT — gốc của <b>жечь</b>, chen <i>и</i> khi thành CHT</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>зажига́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là động từ nằm trong <b>зажига́лка</b> bật lửa = cái để châm lửa. '
    'Thứ được thắp đứng cách 4: <b>зажига́ть све́чи</b> thắp nến. Cặp HT: <b>заже́чь</b> — chia '
    'khó hơn hẳn, xem thẻ đó.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>заже́чь</b> (HT) · <b>зажига́лка</b> bật lửa · <b>зажига́ние</b> bộ '
    'đánh lửa (xe) · <b>жечь</b> đốt · <b>ожо́г</b> vết bỏng</div>'
)

# ------------------------------------------------------------------- съезжать
S["съезжать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">съ-</span>'
    '<span class="hd-gloss">XUỐNG, RỜI KHỎI — có <i>ъ</i> vì <i>е</i> đứng ngay sau</span></div>'
    '<div class="hd-row"><span class="hd-piece">-езж-</span>'
    '<span class="hd-gloss">gốc ĐI XE, như <b>приезжа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>съезжа́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Xe chạy XUỐNG dốc, hay RỜI khỏi đường, khỏi nhà. Luôn là с + cách 2: '
    '<b>съезжа́ть с горы́</b> xuống dốc · <b>съезжа́ть с доро́ги</b> rẽ khỏi đường · '
    '<b>съезжа́ть с кварти́ры</b> dọn khỏi căn hộ. Cặp HT: <b>съе́хать</b>.</div>'
    '<div class="hd-warn">Đừng lẫn <b>съезжа́ю</b> (từ này) với <b>съе́зжу</b> — ngôi «tôi» của '
    '<b>съе́здить</b> đi một chuyến rồi về.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>съе́хать</b> (HT) · <b>съезд</b> lối rẽ xuống; đại hội · '
    '<b>приезжа́ть</b> đến bằng xe · <b>уезжа́ть</b> đi khỏi bằng xe</div>'
)

# -------------------------------------------------------------------- съехать
S["съехать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">съ-</span>'
    '<span class="hd-gloss">XUỐNG, RỜI KHỎI — có <i>ъ</i> vì <i>е</i> đứng ngay sau</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́х-ать</span>'
    '<span class="hd-gloss">ĐI XE — chính là <b>е́хать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp HT của <b>съезжа́ть</b>, cũng đi với с + cách 2: <b>съе́хать с го́рки</b> '
    'trượt xuống đồi · <b>Он съе́хал с кварти́ры</b> Anh ấy đã dọn khỏi căn hộ. Thân tương lai lấy '
    '<i>е́д-</i> như <b>е́ду</b>: <b>съе́ду, съе́дешь, съе́дут</b>.</div>'
    '<div class="hd-warn">Nghe kỹ trọng âm: <b>съе́дем</b> ta sẽ đi xuống, dọn đi ↔ <b>съеди́м</b> '
    'ta sẽ ăn hết (của <b>съесть</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>съезжа́ть</b> (CHT) · <b>съезд</b> lối rẽ xuống; đại hội · '
    '<b>е́хать</b> đi xe · <b>перее́хать</b> chuyển nhà</div>'
)

# -------------------------------------------------------------------- толкать
S["толкать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">толк-</span>'
    '<span class="hd-gloss">ĐẨY, XÔ — gốc trơn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>толка́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đẩy, huých hoài; nghĩa bóng: «đẩy» người ta vào việc gì ⇒ xúi giục, thúc '
    'đẩy, dùng на + cách 4: <b>толка́ть на преступле́ние</b> xúi phạm tội. Đối nghĩa: '
    '<b>тяну́ть</b> kéo. Cặp HT: <b>толкну́ть</b>.</div>'
    '<div class="hd-warn">Chữ dán trên cửa hay không dùng động từ này: <b>От себя́</b> = ĐẨY · '
    '<b>На себя́</b> = KÉO.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>толкну́ть</b> (HT) · <b>толчо́к</b> cú đẩy, cú xóc · '
    '<b>толка́ться</b> chen lấn, xô nhau · <b>столкну́ться</b> đâm vào nhau</div>'
)

# ------------------------------------------------------------------- толкнуть
S["толкнуть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">толк-</span>'
    '<span class="hd-gloss">ĐẨY, XÔ — gốc trơn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ну́-ть</span>'
    '<span class="hd-gloss">MỘT LẦN rồi thôi — như <b>кивну́ть</b> gật một cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đẩy MỘT cái, huých MỘT cái — cặp HT của <b>толка́ть</b>. Trọng âm ở đuôi '
    'suốt bảng: <b>толкну́, толкнёшь, толкну́т</b>. Đẩy bằng gì đứng cách 5: <b>толкну́ть '
    'плечо́м</b> huých bằng vai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>толка́ть</b> (CHT) · <b>толчо́к</b> cú đẩy, cú xóc · '
    '<b>столкну́ться</b> đâm vào nhau · <b>столкнове́ние</b> vụ va chạm</div>'
)

# ------------------------------------------------------------------- впускать
S["впускать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO TRONG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пуск-</span>'
    '<span class="hd-gloss">THẢ, BUÔNG — như <b>отпуска́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>впуска́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thả cho đi VÀO ⇒ cho vào. Cho ai (cách 4) vào đâu (в + cách 4): '
    '<b>впуска́ть соба́ку в дом</b>. Ngược chiều hẳn là <b>выпуска́ть</b> thả RA. Cặp HT: '
    '<b>впусти́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>впусти́ть</b> (HT) · <b>выпуска́ть</b> thả ra · <b>отпуска́ть</b> thả, '
    'buông · <b>пропуска́ть</b> cho qua · <b>о́тпуск</b> nghỉ phép</div>'
)

# ------------------------------------------------------------------- впустить
S["впустить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO TRONG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пуст-и́ть</span>'
    '<span class="hd-gloss">THẢ, BUÔNG — như <b>отпусти́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cho vào MỘT lần, mở cửa cho ai đó: <b>Впусти́ меня́!</b> Cho tôi vào! Cặp '
    'CHT: <b>впуска́ть</b>. Chia y như <b>отпусти́ть</b>: ngôi «tôi» ст → щ và nhấn đuôi '
    '<b>впущу́</b>; các ngôi khác nhấn lùi về gốc <b>впу́стишь, впу́стят</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>впуска́ть</b> (CHT) · <b>пусти́ть</b> thả, cho vào · <b>вы́пустить</b> '
    'thả ra · <b>пропусти́ть</b> cho qua, bỏ lỡ</div>'
)

# ------------------------------------------------------------------- уступать
S["уступать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">RỜI KHỎI, ra xa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ступ-</span>'
    '<span class="hd-gloss">BƯỚC CHÂN — như <b>поступа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>уступа́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bước tránh RA cho người khác ⇒ nhường, nhượng bộ; người bán «lùi» giá ⇒ bớt '
    'giá. Nhường CHO AI đứng cách 3: <b>уступа́ть ме́сто ба́бушке</b>. Cặp HT: '
    '<b>уступи́ть</b>.</div>'
    '<div class="hd-warn">Thua kém AI (cách 3) VỀ CÁI GÌ (в + cách 6): <b>Он не уступа́ет бра́ту в '
    'си́ле</b> Nó không kém anh nó về sức.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уступи́ть</b> (HT) · <b>усту́пка</b> sự nhượng bộ · <b>вступа́ть</b> '
    'gia nhập · <b>поступа́ть</b> thi vào, cư xử</div>'
)

# ------------------------------------------------------------------- уступить
S["уступить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">RỜI KHỎI, ra xa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ступ-и́ть</span>'
    '<span class="hd-gloss">BƯỚC CHÂN — như <b>поступи́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bước tránh ra một lần ⇒ nhường, chịu nhượng bộ. Chia y như <b>вступи́ть</b>: '
    'ngôi «tôi» chèn л và nhấn đuôi <b>уступлю́</b>; các ngôi khác nhấn lùi về gốc <b>усту́пишь, '
    'усту́пят</b>. Cặp CHT: <b>уступа́ть</b>.</div>'
    '<div class="hd-warn"><b>Уступи́те доро́гу</b> = biển báo «nhường đường» · <b>уступи́ть '
    'ме́сто</b> = nhường chỗ ngồi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уступа́ть</b> (CHT) · <b>усту́пка</b> sự nhượng bộ · <b>вступи́ть</b> '
    'gia nhập · <b>поступи́ть</b> vào học, cư xử</div>'
)

# ------------------------------------------------------------------- набирать
S["набирать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">DỒN cho ĐẦY, cho nhiều</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бир-</span>'
    '<span class="hd-gloss">LẤY — gốc của <b>брать</b> (бр/бир/бер)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>набира́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Lấy dồn dần cho đủ ⇒ gom, tích luỹ; từng chữ số ⇒ bấm số; từng chữ cái ⇒ gõ; '
    'từng người ⇒ tuyển: <b>набира́ть сотру́дников</b> tuyển nhân viên. Khuôn -бира́ть (CHT) ↔ '
    '-бра́ть (HT) y như <b>выбира́ть ↔ вы́брать</b>. Cặp HT: <b>набра́ть</b>.</div>'
    '<div class="hd-warn"><b>набира́ть вес</b> = lên cân · <b>набира́ть ско́рость</b> = tăng tốc — '
    'đều đứng cách 4.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>набра́ть</b> (HT) · <b>брать</b> lấy · <b>собира́ть</b> gom, thu thập · '
    '<b>выбира́ть</b> chọn · <b>набо́р</b> bộ, đợt tuyển</div>'
)

# -------------------------------------------------------------------- вручать
S["вручать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO</span></div>'
    '<div class="hd-row"><span class="hd-piece">-руч-</span>'
    '<span class="hd-gloss">TAY — <b>рука́</b>, к → ч</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>вруча́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đặt VÀO TAY ⇒ trao tận tay. Trao cái gì (cách 4) cho ai (cách 3): '
    '<b>вруча́ть награ́ды победи́телям</b> trao giải cho người thắng. Trang trọng hơn '
    '<b>дава́ть</b> đưa. Cặp HT: <b>вручи́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вручи́ть</b> (HT) · <b>вруче́ние</b> lễ trao · <b>рука́</b> tay · '
    '<b>ру́чка</b> cái bút; tay nắm · <b>поруча́ть</b> giao việc cho ai</div>'
)

# -------------------------------------------------------------------- вручить
S["вручить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO</span></div>'
    '<div class="hd-row"><span class="hd-piece">-руч-</span>'
    '<span class="hd-gloss">TAY — <b>рука́</b>, к → ч</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai: <b>вручу́, вручи́шь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đặt VÀO TAY một lần, xong: <b>вручи́ть дипло́м студе́нту</b> trao bằng cho '
    'sinh viên — cái gì cách 4, cho ai cách 3. Trọng âm nằm ở đuôi suốt bảng. Cặp CHT: '
    '<b>вруча́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вруча́ть</b> (CHT) · <b>вруче́ние</b> lễ trao · <b>рука́</b> tay · '
    '<b>ручно́й</b> bằng tay · <b>поручи́ть</b> giao việc cho ai</div>'
)

# ------------------------------------------------------------------- осветить
S["осветить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">PHỦ KHẮP, quanh</span></div>'
    '<div class="hd-row"><span class="hd-piece">-свет-</span>'
    '<span class="hd-gloss">ÁNH SÁNG — <b>свет</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai, nhấn đuôi</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cho ánh sáng phủ khắp ⇒ chiếu sáng; «rọi sáng» một vấn đề ⇒ làm sáng tỏ, đưa '
    'tin: <b>освети́ть вопро́с</b>. Ngôi «tôi» т → щ: <b>освещу́, освети́шь</b> — chữ щ ấy là thân '
    'của cặp CHT <b>освеща́ть</b>.</div>'
    '<div class="hd-warn">Nghe y hệt <b>освяти́ть</b> làm phép thánh — khác một chữ: <b>свет</b> sáng '
    '↔ <b>свято́й</b> thánh.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>освеща́ть</b> (CHT) · <b>освеще́ние</b> sự chiếu sáng · <b>све́тлый</b> '
    'sáng · <b>свети́ть</b> chiếu sáng · <b>свеча́</b> nến</div>'
)

# ------------------------------------------------------------------- освещать
S["освещать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">PHỦ KHẮP, quanh</span></div>'
    '<div class="hd-row"><span class="hd-piece">-свещ-</span>'
    '<span class="hd-gloss">ÁNH SÁNG — <b>свет</b>, т → щ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>освеща́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đang soi, vẫn soi: <b>Ла́мпа освеща́ет стол</b> Đèn soi sáng cái bàn. Báo '
    'chí «rọi sáng» sự kiện ⇒ đưa tin: <b>освеща́ть собы́тия</b>. Thứ được soi luôn đứng cách 4, '
    'không giới từ. Cặp HT: <b>освети́ть</b>.</div>'
    '<div class="hd-warn"><b>свети́ть</b> = TOẢ sáng, không kéo theo cách 4 (<b>Со́лнце '
    'све́тит</b>); <b>освеща́ть</b> = soi sáng CÁI GÌ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>освети́ть</b> (HT) · <b>освеще́ние</b> sự chiếu sáng, sự đưa tin · '
    '<b>свет</b> ánh sáng · <b>све́тлый</b> sáng</div>'
)

# ----------------------------------------------------------------- сэкономить
S["сэкономить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">chỉ làm thể hoàn thành, không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-эконо́м-</span>'
    '<span class="hd-gloss">như <b>эконо́мика</b> (эко- NHÀ + -ном- QUẢN)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Khéo quản việc nhà ⇒ tiết kiệm được — <i>economize</i>. Ngôi «tôi» chèn л: '
    '<b>сэконо́млю, сэконо́мишь</b>; trọng âm đứng yên. Cặp CHT: <b>эконо́мить</b>.</div>'
    '<div class="hd-warn">Tiết kiệm ĐƯỢC cái gì: cách 4 — <b>сэконо́мить вре́мя</b>. Bớt tiền Ở '
    'KHOẢN nào: на + cách 6 — <b>сэконо́мить на такси́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>эконо́мить</b> (CHT) · <b>эконо́мика</b> kinh tế · <b>эконо́мный</b> '
    'tiết kiệm (tính từ) · <b>эконо́мия</b> sự tiết kiệm</div>'
)

# ------------------------------------------------------------------ поправить
S["поправить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пра́в-</span>'
    '<span class="hd-gloss">THẲNG, ĐÚNG — như <b>пра́вый</b>, <b>пра́вильно</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nắn lại cho THẲNG ⇒ chỉnh lại (<b>попра́вить шарф</b>); cho ĐÚNG ⇒ sửa lời, '
    'sửa lỗi. Ngôi «tôi» chèn л: <b>попра́влю, попра́вишь</b>. Cặp CHT: <b>поправля́ть</b>.</div>'
    '<div class="hd-why">Khác <b>испра́вить</b>: cổ áo lệch, khăn xô thì chỉ <b>попра́вить</b>.</div>'
    '<div class="hd-warn"><b>Попра́вь меня́, е́сли я ошиба́юсь.</b> Sửa giúp tôi nếu tôi nói '
    'sai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поправля́ть</b> (CHT) · <b>попра́вка</b> sự sửa đổi · <b>испра́вить</b> '
    'sửa · <b>пра́вить</b> cai trị; biên tập · <b>пра́вило</b> quy tắc</div>'
)

# ----------------------------------------------------------------- поправлять
S["поправлять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-прав-</span>'
    '<span class="hd-gloss">nắn cho THẲNG, ĐÚNG — như <b>попра́вить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-л-я́ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>поправля́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hay chỉnh, hay sửa: <b>поправля́ть очки́</b> đẩy lại kính · <b>поправля́ть '
    'ученика́</b> sửa lời học trò. Chữ вл là từ ngôi «tôi» <b>попра́влю</b> của cặp HT '
    '<b>попра́вить</b> — cùng khuôn <b>испра́влю → исправля́ть</b>.</div>'
    '<div class="hd-warn">Thêm <b>-ся</b> là từ khác: khoẻ lại, hoặc lên cân. <b>Поправля́йся!</b> = '
    'Chóng khoẻ nhé!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>попра́вить</b> (HT) · <b>исправля́ть</b> sửa · <b>попра́вка</b> sự sửa '
    'đổi · <b>пра́вильно</b> đúng</div>'
)

# ------------------------------------------------------------------ усложнить
S["усложнить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">làm cho TRỞ NÊN…</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сложн-</span>'
    '<span class="hd-gloss">PHỨC TẠP — <b>сло́жный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai: <b>усложню́, усложни́шь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng khuôn у- + gốc tính từ + -ить với <b>увели́чить</b> làm cho lớn: làm cho '
    'PHỨC TẠP. Trái nghĩa dựng y hệt từ <b>просто́й</b>: <b>упрости́ть</b> đơn giản hoá. Trọng âm ở '
    'đuôi suốt bảng. Cặp CHT: <b>усложня́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>усложня́ть</b> (CHT) · <b>сло́жный</b> phức tạp · <b>сло́жность</b> độ '
    'phức tạp · <b>усложне́ние</b> sự phức tạp hoá</div>'
)

# ------------------------------------------------------------------ усложнять
S["усложнять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">làm cho TRỞ NÊN…</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сложн-</span>'
    '<span class="hd-gloss">PHỨC TẠP — <b>сло́жный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>усложня́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cứ làm cho phức tạp thêm, rối thêm. Hai thể chỉ khác đuôi: -и́ть (HT) ↔ -я́ть '
    '(CHT). Thứ bị làm rối đứng cách 4: <b>усложня́ть жизнь</b> làm đời thêm rắc rối.</div>'
    '<div class="hd-warn"><b>Не усложня́й!</b> = Đừng làm rối chuyện lên! — sau <b>не</b>, lời bảo '
    'đừng dùng thể CHT này.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>усложни́ть</b> (HT) · <b>сло́жный</b> phức tạp · <b>сло́жно</b> phức tạp, '
    'khó (trạng từ) · <b>сло́жность</b> độ phức tạp</div>'
)

# ------------------------------------------------------------------ расширить
S["расширить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рас-</span>'
    '<span class="hd-gloss">= раз- : trải RA KHẮP</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ши́р-</span>'
    '<span class="hd-gloss">RỘNG — <b>широ́кий</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai: <b>расши́рю, расши́ришь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm cho RỘNG ra mọi phía ⇒ mở rộng, nới rộng — cả nghĩa bóng: <b>расши́рить '
    'слова́рный запа́с</b> mở rộng vốn từ. Trọng âm đứng yên ở <i>ши́</i>. Cặp CHT: '
    '<b>расширя́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>расширя́ть</b> (CHT) · <b>расшире́ние</b> sự mở rộng · <b>широ́кий</b> '
    'rộng · <b>ширина́</b> chiều rộng</div>'
)

# ------------------------------------------------------------------ расширять
S["расширять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рас-</span>'
    '<span class="hd-gloss">= раз- : trải RA KHẮP</span></div>'
    '<div class="hd-row"><span class="hd-piece">-шир-</span>'
    '<span class="hd-gloss">RỘNG — <b>широ́кий</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>расширя́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đang mở rộng, mở rộng dần: <b>расширя́ть доро́гу</b> nới rộng con đường. '
    'Trọng âm tách hai thể: CHT ở đuôi <b>расширя́ю</b>, HT ở gốc <b>расши́рю</b>.</div>'
    '<div class="hd-warn">Có người làm cho cái gì (cách 4) rộng ra thì không -ся; cái tự rộng ra phải '
    'thêm -ся: <b>Го́род расширя́ется</b> Thành phố đang mở rộng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>расши́рить</b> (HT) · <b>расшире́ние</b> sự mở rộng · <b>широко́</b> '
    'rộng rãi (trạng từ) · <b>ширина́</b> chiều rộng</div>'
)

B = {
    "docbangmat": 147,
    "loitubat": 3,
    "nguonsai": 4,
    "baolen": [
        "V cần duyệt (15 thẻ): зажечь/зажигать + «châm lửa, truyền cảm hứng», bỏ «bật lửa»; съезжать/съехать + «dọn nhà đi, rời khỏi đường»; толкать/толкнуть «thúc» → «xô, xúi giục, thúc đẩy»; впускать/впустить «cho vào, cho phép vào, để cho vào» (bỏ «cho vô» lặp, «để vào» đọc ra «đặt vào»); уступать/уступить + «thua kém, bớt giá»; набирать lấy y hệt набрать; вручать/вручить + «giao phó»; осветить/освещать + «làm sáng tỏ, đưa tin» (khớp освещение). 7 thẻ còn lại giữ đề cũ.",
        "набирать: V y hệt набрать nên KHÔNG có «tăng», trong khi câu ví dụ trên thẻ набирать dùng «tăng cân / tăng tốc» và «nhồi». Gloss to gain phủ bằng «thu được»; ô đỏ của thẻ dạy набирать вес / скорость. Muốn có «tăng» thì phải thêm ở CẢ набрать (đã nạp, không sửa từ lô này).",
        "Cặp thể: câu ví dụ впускать dịch «Đừng để khí lạnh vào» — đề mới ghi «để cho vào», vẫn khớp.",
        "Nguồn sai đã bác (4): CACH DUNG của съехать «съехать с этой темой» sai ngữ pháp (с + cách 2: с этой темы); bảng ghi светить là cặp của осветить (cặp thật: освещать); «bật lửa» của зажигать đọc ra danh từ зажигалка; «lấy thêm» của набирать không có trong gloss.",
        "Chỗ không chắc: толк- ghi gốc trơn, cố ý không nối толпа (đúng thẻ толпа: gốc trơn) và толк «ý nghĩa». Bỏ nghĩa lóng зажигать «quẩy», съехать с темы «đánh trống lảng», толкать «bán».",
        "Va chạm: bản tiep in (khong co); V mới trùng hoàn toàn chỉ trong từng cặp thể, badge PERF/IMPF tách. Nên chạy vacham sau khi nạp.",
        "loitubat (3): зажечь viết «máy móc CHỈ dùng включить» (quá tay); освещать viết светить «không cần gì theo sau» (светить nhận cách 3/5, đổi thành không kéo cách 4); толкать viết chữ trên cửa «không dùng» động từ này (có cửa ghi Толкать, đổi thành «hay không dùng»).",
    ],
}
