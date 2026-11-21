# -*- coding: utf-8 -*-
"""k144 — life::leisure: nghỉ ngơi, thể thao, thời tiết, địa danh.

Chỗ cần nhất quán trong lô:
(1) gốc гор- = CHÁY (загорать/загореть) — khớp горе́ть/сгоре́ть (k133): rám nắng = «bị nắng đốt».
(2) gốc ши-/шь- = MAY (шить/сшить) — ши- → шь- khi chia, y khuôn пить → пью.
(3) gốc бол- (болельщик) — khớp боле́ть (k48) «боле́ть за = cổ vũ»; баскетболист: -бо́л là «ball», KHÔNG phải бол- (khớp k72).
(4) увлечение — khớp увле́чься (k73): у- không nghĩa riêng, -влеч- = KÉO.
(5) tính từ từ địa danh viết THƯỜNG: сибирский, азиатский.
Họ hàng cố ý vắng: салют (từ mượn đứng một mình), туча (gốc trơn, không chắc họ).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "кроссовка": "giày thể thao",                 # bỏ «(một chiếc)»
    "сшить": "may, khâu",                         # bỏ «xong», «(hoàn thành)» — badge thể tách với шить
    "увлечение": "niềm say mê",                   # RÚT «sở thích» — trùng хо́бби (k73, n, cùng giống trung)
    "загореть": "rám nắng",                       # bỏ «(xong)»
    "купаться": "đi bơi, tắm biển, tắm sông",     # RÚT «tắm» trơn — nhường мы́ться (luồng chính phân xử); gloss go swimming / bathe
    "туча": "mây đen, đám dày đặc",               # «;» → «,»
    "сибирский": "thuộc Siberia",                 # bỏ ngoặc «(thuộc)»
    "азиатский": "thuộc châu Á",                  # bỏ «Á Đông» — hẹp hơn gloss Asian (Trung Á cũng là азиа́тский)
}

# -------------------------------------------------------------- кроссовка
S["кроссовка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кросс-</span>'
    '<span class="hd-gloss"><b>кросс</b> — cuộc chạy việt dã, mượn tiếng Anh <i>cross(-country)</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́вк-а</span>'
    '<span class="hd-gloss">đuôi «đồ dùng cho việc đó», giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đồ để chạy việt dã» ⇒ giày thể thao. Một chữ là MỘT chiếc; đôi giày nói số nhiều '
    '<b>кроссо́вки</b>.</div>'
    '<div class="hd-warn">Sinh cách số nhiều chèn <b>о</b>: <b>па́ра кроссо́вок</b> = một đôi giày thể thao.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кросс</b> chạy việt dã · <b>ветро́вка</b> áo gió (cùng đuôi <i>-овка</i>, gốc <b>ве́тер</b>)</div>'
)

# ------------------------------------------------------------------- шить
S["шить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ши-</span>'
    '<span class="hd-gloss">MAY — gốc trơn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc Ấn–Âu với tiếng Anh <i>sew</i> (và <i>suture</i> — đường khâu). '
    'Cặp thể HT: <b>сшить</b>.</div>'
    '<div class="hd-warn">Khi chia, <b>ши-</b> co thành <b>шь-</b>: <b>шью, шьёшь, шьют</b> — y khuôn '
    '<b>пить → пью, пьёшь</b> và <b>бить → бью</b>. Mệnh lệnh: <b>шей</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сшить</b> may (HT) · <b>шов</b> đường may · <b>шве́йная маши́на</b> máy may · '
    '<b>швея́</b> thợ may nữ</div>'
)

# ------------------------------------------------------------------ сшить
S["сшить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">thể hoàn thành, kèm nghĩa «GHÉP LẠI với nhau»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-шить</span>'
    '<span class="hd-gloss">MAY — chính là <b>шить</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">May cho xong một món: <b>сшить пла́тье</b> = may xong cái váy. Vì <b>с-</b> còn nghĩa '
    '«ghép lại», nó cũng là khâu nối hai mảnh: <b>сшить два куска́</b>.</div>'
    '<div class="hd-warn">Khi chia, tiền tố chèn thêm <b>о</b> để dễ đọc: <b>сошью́, сошьёшь, сошью́т</b> '
    '(quá khứ thì không: <b>сшил</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>шить</b> may (CHT) · <b>шов</b> đường may · <b>шве́йный</b> (thuộc) may vá</div>'
)

# -------------------------------------------------------------- увлечение
S["увлечение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố — ở từ này không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-влеч-</span>'
    '<span class="hd-gloss">gốc KÉO <i>влек-</i>, <i>к</i> đổi thành <i>ч</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">đuôi danh từ, giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>увлека́ться</b>: «sự bị cuốn theo» ⇒ niềm say mê, cũng là sở thích. '
    'Say mê CÁI GÌ thì cái đó ở cách 5: <b>увлече́ние му́зыкой</b>.</div>'
    '<div class="hd-warn">Cùng nghĩa «sở thích» với <b>хо́бби</b> (mượn Anh): <b>увлече́ние</b> là từ Nga gốc, '
    'đậm hơn — còn dùng cho cả một mối say nắng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>увлека́ться</b> say mê (CHT) · <b>увле́чься</b> đâm ra say mê (HT) · '
    '<b>увлека́тельный</b> cuốn hút, hấp dẫn</div>'
)

# ------------------------------------------------------------- новогодний
S["новогодний"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">нов-о-</span>'
    '<span class="hd-gloss">MỚI — <b>но́вый</b>, <i>-о-</i> là nguyên âm nối</span></div>'
    '<div class="hd-row"><span class="hd-piece">-год-</span>'
    '<span class="hd-gloss">NĂM — <b>год</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ний</span>'
    '<span class="hd-gloss">đuôi tính từ MỀM, như <b>зи́мний</b>, <b>ле́тний</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hai chữ <b>Но́вый год</b> (Tết dương lịch) dính lại thành một tính từ. Đuôi mềm nên đổi '
    'đuôi là <b>нового́дняя</b>, <b>нового́днее</b>. Dạng ngắn trong bảng gần như không ai dùng — bỏ qua.</div>'
    '<div class="hd-warn"><b>нового́дняя ёлка</b> = cây thông của TẾT DƯƠNG LỊCH — người Nga dựng cây thông '
    'cho năm mới, không phải cho Giáng sinh.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>но́вый</b> mới · <b>год</b> năm · <b>ежего́дный</b> hằng năm</div>'
)

# ------------------------------------------------------------------ салют
S["салют"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mượn tiếng Pháp <i>salut</i> = lời chào (tiếng Anh <i>salute</i>), một khối, không chẻ. '
    'Gốc là bắn súng CHÀO MỪNG ⇒ màn pháo hoa ngày lễ (<b>Но́вый год</b>, ngày 9/5).</div>'
    '<div class="hd-warn">Cả màn pháo hoa là MỘT <b>салю́т</b>, số ít: <b>смотре́ть салю́т</b> = xem bắn pháo hoa '
    '(tiếng Anh lại dùng số nhiều <i>fireworks</i>).</div>'
    '<div class="hd-why">Nói suồng sã, <b>Салю́т!</b> còn là câu chào «Hi!» giữa bạn bè.</div>'
)

# --------------------------------------------------------------- загорать
S["загорать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">tiền tố — ở từ này không mang nghĩa riêng rõ ràng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-гор-</span>'
    '<span class="hd-gloss">CHÁY — như <b>горе́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>загора́ю, загора́ешь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nằm cho nắng «đốt» da ⇒ tắm nắng: <b>загора́ть на пля́же</b>. Cặp HT: <b>загоре́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>загоре́ть</b> rám nắng (HT) · <b>зага́р</b> làn da rám nắng (<i>о</i> đổi <i>а</i>) · '
    '<b>горе́ть</b> cháy · <b>сгоре́ть</b> cháy rụi</div>'
)

# --------------------------------------------------------------- загореть
S["загореть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">tiền tố thể hoàn thành</span></div>'
    '<div class="hd-row"><span class="hd-piece">-гор-е́ть</span>'
    '<span class="hd-gloss">CHÁY — chính là <b>горе́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Kết quả của <b>загора́ть</b>: da đã sạm lại. <b>Ты хорошо́ загоре́л!</b> = Bạn rám nắng đẹp '
    'quá! Chia y như <b>горе́ть</b>: <b>загорю́, загори́шь</b>.</div>'
    '<div class="hd-warn">Ba từ gần nhau, đừng lẫn: <b>загоре́ть</b> rám nắng (tốt) · <b>сгоре́ть на со́лнце</b> '
    'cháy nắng (bỏng) · <b>загоре́ться</b> (thêm <b>-ся</b>) bắt lửa, bùng cháy.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>загора́ть</b> tắm nắng (CHT) · <b>зага́р</b> làn da rám nắng · <b>горе́ть</b> cháy</div>'
)

# --------------------------------------------------------------- купаться
S["купаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">куп-а́-ть</span>'
    '<span class="hd-gloss"><b>купа́ть</b> — dầm cho ai xuống nước, tắm cho (em bé)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">phản thân — dầm CHÍNH MÌNH xuống nước</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Xuống biển, sông, hồ cho vui: <b>купа́ться в мо́ре</b>. Khác <b>пла́вать</b> = động tác bơi '
    '(biết bơi, bơi bao xa), và khác <b>мы́ться</b> = tắm rửa cho sạch. Cặp HT: <b>искупа́ться</b>.</div>'
    '<div class="hd-warn">⚠️ <b>куп-</b> ở đây KHÔNG dính gì tới <b>купи́ть</b>, <b>покупа́ть</b> (mua) — hai gốc '
    'khác nhau, chỉ trùng mặt chữ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>купа́ть</b> tắm cho (ai) · <b>купа́льник</b> đồ bơi nữ · <b>искупа́ться</b> đi bơi (HT)</div>'
)

# ----------------------------------------------------------------- коньки
S["коньки"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кон-</span>'
    '<span class="hd-gloss">NGỰA — <b>конь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ёк / -ьк-и́</span>'
    '<span class="hd-gloss">đuôi «nhỏ»: <b>конёк</b> = con ngựa nhỏ; số nhiều <b>коньки́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một chiếc giày trượt là <b>конёк</b> «ngựa con» — thứ chở mình lướt đi; vì sao gọi thế '
    'thì chỉ có giả thuyết. Thường dùng số nhiều vì đi cả đôi.</div>'
    '<div class="hd-warn"><b>ё</b> rơi mất khi đổi đuôi: <b>конёк → конька́ → коньки́</b>. Trượt băng là '
    '<b>ката́ться на конька́х</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>конь</b> con ngựa · <b>конькобе́жец</b> vận động viên trượt băng tốc độ</div>'
)

# -------------------------------------------------------------- болельщик
S["болельщик"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">боле́-</span>'
    '<span class="hd-gloss"><b>боле́ть</b> — đau; ở đây nghĩa «cổ vũ»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-льщик</span>'
    '<span class="hd-gloss">đuôi «người làm việc đó»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người «đau cùng đội» ⇒ cổ động viên. Nữ: <b>боле́льщица</b>.</div>'
    '<div class="hd-warn">Cổ vũ CHO ai là <b>за</b> + cách 4: <b>Я боле́ю за «Спарта́к»</b> = Tôi là fan '
    'của Spartak.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>боле́ть</b> ốm; cổ vũ · <b>боль</b> cơn đau · <b>боле́знь</b> căn bệnh</div>'
)

# ----------------------------------------------------------- баскетболист
S["баскетболист"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">баскетбол-</span>'
    '<span class="hd-gloss"><b>баскетбо́л</b> — bóng rổ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ст</span>'
    '<span class="hd-gloss">người chơi / theo nghề đó — như <i>-ist</i> tiếng Anh</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng khuôn <b>футболи́ст</b>, <b>хоккеи́ст</b>: tên môn + <b>-и́ст</b>. Trọng âm nhảy sang '
    '<b>-и́ст</b> và đứng yên ở đó. Nữ: <b>баскетболи́стка</b>.</div>'
    '<div class="hd-why"><i>-бол-</i> ở đây là <i>ball</i>, không cùng gốc với <b>боле́льщик</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>баскетбо́л</b> bóng rổ · <b>баскетбо́льный</b> (thuộc) bóng rổ · '
    '<b>футболи́ст</b> cầu thủ bóng đá</div>'
)

# ----------------------------------------------------------------- берёза
S["берёза"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc Ấn–Âu với tiếng Anh <i>birch</i>: <i>b-r</i> ↔ <b>б-р</b>. Cây biểu tượng của '
    'nước Nga. Trọng âm luôn ở <b>ё</b>, kể cả số nhiều <b>берёзы</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>берёзовый</b> (thuộc) bạch dương · <b>берёзка</b> cây bạch dương nhỏ · '
    '<b>подберёзовик</b> nấm «mọc dưới bạch dương»</div>'
)

# ------------------------------------------------------------------- туча
S["туча"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mây NẶNG: đen, sắp mưa giông. Còn mây thường (trắng, nhẹ) là <b>о́блако</b>. '
    'Từ hình ảnh «khối dày đặc» ra nghĩa thứ hai: <b>ту́ча комаро́в</b> = cả đám muỗi.</div>'
    '<div class="hd-warn"><b>Ту́чи сгуща́ются</b> = mây đen kéo đến — cũng dùng nghĩa bóng: sắp có chuyện '
    'chẳng lành.</div>'
)

# ----------------------------------------------------------------- климат
S["климат"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mượn gốc Hy Lạp <i>klima</i> «độ nghiêng (so với mặt trời)», cùng gốc tiếng Anh '
    '<i>climate</i>, một khối, không chẻ. Trọng âm ở đầu như tiếng Anh: <b>кли́мат</b>.</div>'
    '<div class="hd-why">Cũng dùng nghĩa bóng y tiếng Anh: <b>психологи́ческий кли́мат</b> = bầu không khí '
    '(trong tập thể).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>климати́ческий</b> (thuộc) khí hậu — trọng âm nhảy sang <i>-ти́-</i></div>'
)

# -------------------------------------------------------------- сибирский
S["сибирский"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сибир-</span>'
    '<span class="hd-gloss"><b>Сиби́рь</b> — Siberia (bỏ <b>ь</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ск-ий</span>'
    '<span class="hd-gloss">đuôi tính từ «thuộc về nơi đó»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tên đất + <b>-ский</b>, trọng âm giữ nguyên chỗ: <b>сиби́рский моро́з</b> = cái rét '
    'Siberia.</div>'
    '<div class="hd-warn">Tính từ từ địa danh viết THƯỜNG: <b>сиби́рский</b>, dù <b>Сиби́рь</b> viết hoa '
    '(tiếng Anh thì <i>Siberian</i> vẫn hoa).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>Сиби́рь</b> Siberia · <b>сибиря́к</b> người Siberia</div>'
)

# -------------------------------------------------------------- азиатский
S["азиатский"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ази-а́т-</span>'
    '<span class="hd-gloss"><b>А́зия</b> — châu Á, chèn <i>-ат-</i> theo Latin <i>asiaticus</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ск-ий</span>'
    '<span class="hd-gloss">đuôi tính từ «thuộc về nơi đó»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đoạn <i>-ат-</i> chính là <i>-at-</i> trong tiếng Anh <i>Asiatic</i>. Trọng âm dời từ '
    '<b>А́зия</b> sang <b>азиа́тский</b>. Viết thường như mọi tính từ địa danh: <b>азиа́тская ку́хня</b> = món ăn châu Á.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>А́зия</b> châu Á · <b>Евра́зия</b> lục địa Á–Âu · <b>европе́йский</b> châu Âu '
    '(cùng đuôi <i>-ский</i>)</div>'
)

B = {
    "docbangmat": 65,
    "loitubat": 1,
    "nguonsai": 1,
    "baolen": [
        "увлечение: V rút còn MỘT nghĩa 'niềm say mê' (bỏ «sở thích» vì trùng хобби k73, cùng n + giống trung) — đề bài mất hẳn nghĩa hobby, cần duyệt",
        "купаться: V 'đi bơi, tắm biển, tắm sông' (bỏ «tắm» trơn theo phân xử, nhường мыться k150). Chưa đối chiếu field thật của плавать — nếu плавать cũng ghi «đi bơi» thì chỉ còn badge phản thân tách; tôi KHÔNG đọc Anki",
        "шить (giữ 'may, khâu') và сшить (V 'may, khâu') trùng hết chữ — chỉ badge thể (IMPF/PERF) tách; đúng luật §2c nhưng báo để biết",
        "сибирский 'thuộc Siberia', азиатский 'thuộc châu Á': bỏ ngoặc «(thuộc)» và bỏ «Á Đông» (hẹp hơn gloss Asian) — cần duyệt cách viết",
        "nguonsai=1: field Vietnamese cũ của азиатский có «Á Đông» (= Đông Á), hẹp hơn gloss Asian/Asiatic — đã bỏ thay vì chép theo",
        "loitubat=1: климат — đã viết «độ nghiêng (của mặt trời)», sửa thành «so với mặt trời» (κλίμα là độ nghiêng của mặt đất so với mặt trời)",
        "коньки: конёк ← конь (chắc), nhưng VÌ SAO giày trượt gọi là «ngựa con» chỉ là giả thuyết — đã hạ mức tin ngay trong câu",
        "Họ hàng cố ý vắng: салют (từ mượn đứng một mình; салютовать quá hiếm), туча (gốc trơn, không chắc họ từ nào)",
        "новогодний: giữ field 'của năm mới, dịp năm mới' (không ngoặc, không cần sửa); BAT THUONG dạng ngắn нового́ден… ghi là gần như không dùng",
        "Va chạm chỉ soát offline (_vacham_vi.txt + tudien.json), không chạm Anki — luồng chính nên chạy congcu.py vacham sau khi nạp",
    ],
}
