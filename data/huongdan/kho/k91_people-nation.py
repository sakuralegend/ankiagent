# -*- coding: utf-8 -*-
"""k91 — people-nation: 19 từ mới (đợt A1 TRKI), KHÔNG cùng một trục — soạn từng thẻ độc lập.

Chỗ cần nhất quán trong lô:
(1) господи́н / госпожа́ / хозя́ин: đuôi -ин «MỘT người» chỉ sống ở số ít (господа́, хозя́ева);
(2) господи́н ↔ това́рищ: hai lối xưng hô đổi chỗ cho nhau sau 1917 và sau 1991;
(3) khớp lô cũ: жи- SỐNG + -тель NGƯỜI (k38), кило- + метр (k31), цвета́ ≠ цветы́ (k58),
    часы́ = số nhiều của час (k51), Росс- ← Русь (k39), бизнес- (k35).
Bẫy họ hàng đã gạt: ча́шка KHÔNG cùng gốc чай (nó từ ча́ша); плане́та KHÔNG cùng gốc план.
"""

S = {}

# ---------------------------------------------------------------- автор
S["автор"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được trong tiếng Nga: mượn nguyên khối từ Latin '
    '<i>auctor</i> — cùng gốc với tiếng Anh <i>author</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người làm ra một tác phẩm, không chỉ sách: <b>а́втор пе́сни</b> = '
    'tác giả bài hát. Giống đực, nhưng dùng cho cả phụ nữ: <b>Она́ а́втор кни́ги</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>а́вторский</b> của tác giả (<b>а́вторское пра́во</b> bản quyền) · '
    '<b>соа́втор</b> đồng tác giả (<b>со-</b> = cùng)</div>'
)

# ---------------------------------------------------------------- бизнес
S["бизнес"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn thẳng tiếng Anh <i>business</i>, trọng âm '
    'cũng ở âm đầu như tiếng Anh.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giống đực, gần như chỉ dùng số ít: <b>ма́лый би́знес</b> = doanh '
    'nghiệp nhỏ. «Làm kinh doanh» là <b>занима́ться би́знесом</b> (cách 5).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бизнесме́н</b> doanh nhân (<b>-ме́н</b> = <i>man</i>)</div>'
)

# -------------------------------------------------------------- господин
S["господин"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">госпо́д-</span>'
    '<span class="hd-gloss">CHỦ, BỀ TRÊN (như <b>Госпо́дь</b> = Chúa)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́н</span>'
    '<span class="hd-gloss">MỘT người (như <b>граждани́н</b> một công dân)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi <b>-ин</b> chỉ sống ở số ít, sang số nhiều rụng mất: '
    '<b>господа́</b>, <b>госпо́д</b> — y như <b>граждани́н → гра́ждане</b>. Đứng trước họ '
    'như «ngài»: <b>господи́н Ивано́в</b>.</div>'
    '<div class="hd-warn"><b>Да́мы и господа́!</b> = Thưa quý bà và quý ông! — '
    '<b>господа́</b> một mình là «thưa quý vị».</div>'
    '<div class="hd-why">Sau 1917 từ này bị bỏ, thay bằng <b>това́рищ</b>; sau 1991 mới '
    'trở lại trong văn phong trang trọng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>госпожа́</b> quý bà · <b>Госпо́дь</b> Chúa · '
    '<b>Го́споди!</b> Trời ơi!</div>'
)

# --------------------------------------------------------------- госпожа
S["госпожа"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">госпо́ж-</span>'
    '<span class="hd-gloss">= <b>госпо́д-</b> CHỦ, BỀ TRÊN, chữ <b>д</b> hoá <b>ж</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́</span>'
    '<span class="hd-gloss">đuôi giống cái, mang trọng âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bản giống cái của <b>господи́н</b>. Phép <b>д → ж</b> là phép đã '
    'gặp ở động từ: <b>ходи́ть → хожу́</b>. Đứng trước họ như «bà»: '
    '<b>госпожа́ Ивано́ва</b>.</div>'
    '<div class="hd-why">Trọng âm ở đuôi khắp bảng, trừ đúng cách 2 số nhiều — hết đuôi '
    'nên lùi về gốc: <b>госпо́ж</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>господи́н</b> quý ông, ngài · <b>господа́</b> quý vị · '
    '<b>Госпо́дь</b> Chúa</div>'
)

# --------------------------------------------------------------- детский
S["детский"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дет-</span>'
    '<span class="hd-gloss">TRẺ EM (gốc của <b>де́ти</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ск-ий</span>'
    '<span class="hd-gloss">«thuộc về» + đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thuộc về trẻ em». Tính từ lấy gốc của SỐ NHIỀU <b>де́ти</b>, '
    'vì số ít <b>ребёнок</b> là một gốc khác hẳn — đừng tìm <b>реб-</b> ở đây.</div>'
    '<div class="hd-warn"><b>де́тский сад</b> = nhà trẻ, mẫu giáo (nghĩa đen «vườn trẻ '
    'em»), nói tắt <b>детса́д</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>де́ти</b> trẻ em, con cái · <b>де́тство</b> tuổi thơ</div>'
)

# --------------------------------------------------------------- женщина
S["женщина"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">жен-</span>'
    '<span class="hd-gloss">ĐÀN BÀ, VỢ (như <b>жена́</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-щин-а</span>'
    '<span class="hd-gloss"><b>-ск-</b> của <b>же́нский</b> hoá <b>щ</b> + đuôi <b>-ина</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Về từ nguyên: «người thuộc giới nữ» = <b>же́нский</b> + <b>-ина</b>, '
    'chỗ gặp nhau <b>ск → щ</b> (như <b>иска́ть → ищу́</b>). Từ đôi của nó dựng y hệt: '
    '<b>мужчи́на</b> đàn ông ← <b>мужско́й</b>.</div>'
    '<div class="hd-why">Trọng âm đứng yên ở <b>же́н-</b> trong mọi cách.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>жена́</b> vợ · <b>же́нский</b> của phụ nữ · '
    '<b>жени́ться</b> lấy vợ · <b>мужчи́на</b> đàn ông</div>'
)

# ---------------------------------------------------------------- житель
S["житель"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">жи-</span>'
    '<span class="hd-gloss">SỐNG — gốc của <b>жить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-тель</span>'
    '<span class="hd-gloss">NGƯỜI làm việc đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Người sống (ở đâu đó)» = cư dân. Cùng khuôn <b>-тель</b> với '
    '<b>учи́тель</b> người dạy, <b>писа́тель</b> người viết. Nơi chốn đứng sau ở '
    'cách 2: <b>жи́тель Москвы́</b> = cư dân Moscow.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>жить</b> sống · <b>жизнь</b> cuộc sống · '
    '<b>жи́тельство</b> sự cư trú · <b>живо́й</b> sống, còn sống</div>'
)

# -------------------------------------------------------------- километр
S["километр"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кило-</span>'
    '<span class="hd-gloss">NGHÌN (Hy Lạp <i>khílioi</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ме́тр</span>'
    '<span class="hd-gloss">thẻ <b>метр</b> — mét</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghìn mét — ghép y như tiếng Anh <i>kilometre</i>. Trọng âm nằm '
    'trên <b>-ме́-</b>, đúng chỗ của <b>метр</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>метр</b> mét · <b>сантиме́тр</b> xăng-ti-mét · '
    '<b>килогра́мм</b> ki-lô-gam</div>'
)

# --------------------------------------------------------------- копейка
S["копейка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">коп-</span>'
    '<span class="hd-gloss">← <b>копьё</b> CÂY GIÁO</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́йк-а</span>'
    '<span class="hd-gloss">hậu tố + đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cách giải thích phổ biến: đồng tiền đúc năm 1535 in hình kỵ sĩ '
    'cầm giáo. 100 <b>копе́ек</b> = 1 <b>рубль</b>.</div>'
    '<div class="hd-warn">Cách 2 số nhiều: <b>-йк-</b> thành <b>-ек-</b> — <b>копе́ек</b> '
    '(không phải «копейк»). Đếm tiền: <b>одна́ копе́йка</b> · <b>две копе́йки</b> · '
    '<b>пять копе́ек</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>копьё</b> cây giáo · <b>копе́ечка</b> đồng xu nhỏ (thân mật)</div>'
)

# --------------------------------------------------------------- москвич
S["москвич"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">москв-</span>'
    '<span class="hd-gloss"><b>Москва́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ч</span>'
    '<span class="hd-gloss">NGƯỜI ở thành phố đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người Moscow; nữ là <b>москви́чка</b>. Trọng âm nhảy ra đuôi ngay '
    'khi đổi cách: <b>москвича́</b>, <b>москвичу́</b>, số nhiều <b>москвичи́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>Москва́</b> Moscow · <b>моско́вский</b> thuộc Moscow · '
    '<b>москви́чка</b> phụ nữ Moscow</div>'
)

# ------------------------------------------------------------- несколько
S["несколько"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не́-</span>'
    '<span class="hd-gloss">«NÀO ĐÓ» — không phải phủ định, và luôn mang trọng âm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сколько</span>'
    '<span class="hd-gloss">thẻ <b>ско́лько</b> — bao nhiêu</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Bao nhiêu đó» không rõ số = vài. Cùng <b>не́-</b> bất định với '
    '<b>не́который</b> (nào đó).</div>'
    '<div class="hd-warn">Đi với vật ĐẾM ĐƯỢC ở cách 2 số nhiều: <b>не́сколько дней</b>. '
    'Vật không đếm được thì dùng <b>немно́го</b>: <b>немно́го воды́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ско́лько</b> bao nhiêu · <b>сто́лько</b> bấy nhiêu · '
    '<b>не́который</b> nào đó</div>'
)

# ------------------------------------------------------------------ план
S["план"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: từ mượn châu Âu, gốc Latin <i>planum</i> «mặt '
    'phẳng» — cùng chữ với tiếng Anh <i>plan</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hai nghĩa đều từ «hình vẽ trên mặt phẳng»: kế hoạch, và bản vẽ '
    'mặt bằng — <b>план го́рода</b> = sơ đồ thành phố.</div>'
    '<div class="hd-warn"><b>плане́та</b> trông giống nhưng KHÔNG cùng gốc (Hy Lạp «kẻ lang '
    'thang»).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>плани́ровать</b> lên kế hoạch · <b>планиро́вка</b> cách bố trí '
    'mặt bằng</div>'
)

# ------------------------------------------------------------ российский
S["российский"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">росси́-</span>'
    '<span class="hd-gloss"><b>Росси́я</b> (chữ <b>я</b> hoá <b>й</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-йск-ий</span>'
    '<span class="hd-gloss">«thuộc về» + đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thuộc về QUỐC GIA Nga — nhà nước, lãnh thổ, công dân mọi dân tộc: '
    '<b>Росси́йская Федера́ция</b>.</div>'
    '<div class="hd-warn">Còn dân tộc, tiếng nói, văn hoá Nga là <b>ру́сский</b>: '
    '<b>ру́сский язы́к</b>, không phải «российский язык».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>Росси́я</b> nước Nga · <b>россия́нин</b> công dân Nga · '
    '<b>ру́сский</b> người Nga, tiếng Nga</div>'
)

# ---------------------------------------------------------------- собака
S["собака"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được — học nguyên khối.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giống cái nhưng là từ chung cho mọi con chó, cả chó đực. '
    'Muốn nói rõ «con chó đực» thì dùng <b>пёс</b>.</div>'
    '<div class="hd-warn">Ký hiệu <b>@</b> trong email người Nga gọi là <b>соба́ка</b> '
    '(hoặc <b>соба́чка</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>соба́чка</b> chó nhỏ · <b>соба́чий</b> của chó '
    '(<b>к → ч</b>)</div>'
)

# --------------------------------------------------------------- товарищ
S["товарищ"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được theo tiếng Nga hiện đại — học nguyên khối.</div>'
    '<div class="hd-warn">⚠️ Mức tin: đây là từ nguyên, không phải luật — nhiều nhà ngôn '
    'ngữ cho là mượn tiếng Turk, nghĩa gốc «bạn cùng buôn hàng», họ hàng với '
    '<b>това́р</b> hàng hoá.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thời Xô Viết là lối xưng hô chung «đồng chí», thay cho '
    '<b>господи́н</b>. Nay hay gặp nhất nghĩa «bạn cùng làm/cùng học»: '
    '<b>това́рищ по рабо́те</b> = bạn đồng nghiệp.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>това́рищество</b> hội, tình bạn bè · <b>това́р</b> hàng hoá '
    '(theo từ nguyên trên)</div>'
)

# ---------------------------------------------------------------- хозяин
S["хозяин"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">хозя́-</span>'
    '<span class="hd-gloss">CHỦ — gốc học nguyên khối</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ин</span>'
    '<span class="hd-gloss">MỘT người (như <b>господи́н</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ai làm chủ cái gì thì là <b>хозя́ин</b> của nó: chủ nhà, chủ quán, '
    'chủ con chó — <b>хозя́ин соба́ки</b>.</div>'
    '<div class="hd-warn">Số nhiều phải thuộc: <b>-ин</b> rụng, thay bằng <b>-ева</b> — '
    '<b>хозя́ева</b>, cách 2 <b>хозя́ев</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>хозя́йка</b> bà chủ, nữ chủ nhà · <b>хозя́йство</b> việc nhà; '
    'kinh tế (<b>се́льское хозя́йство</b> nông nghiệp)</div>'
)

# --------------------------------------------------------------- цветок
S["цветок"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">цвет-</span>'
    '<span class="hd-gloss">NỞ, RA HOA (thẻ <b>цвет</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́к</span>'
    '<span class="hd-gloss">hậu tố danh từ, chữ <b>о</b> chạy</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Số ít: <b>о</b> rơi mất và trọng âm ra đuôi — <b>цветка́</b>, '
    '<b>цветко́м</b>. Số nhiều thay hẳn mặt: <b>цветы́</b>, <b>цвето́в</b>.</div>'
    '<div class="hd-warn">⚠️ Hai số nhiều đừng lẫn: <b>цветы́</b> = các BÔNG HOA, còn '
    '<b>цвета́</b> = các MÀU (số nhiều của <b>цвет</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>цвет</b> màu · <b>цвести́</b> nở hoa · <b>цвето́чный</b> '
    'thuộc hoa (<b>цвето́чный магази́н</b> tiệm hoa)</div>'
)

# --------------------------------------------------------------- чайник
S["чайник"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ча́й-</span>'
    '<span class="hd-gloss">thẻ <b>чай</b> — trà</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ник</span>'
    '<span class="hd-gloss">ĐỒ VẬT dành cho thứ đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đồ dành cho trà» = cái ấm, cả ấm đun nước lẫn ấm pha. Cùng khuôn: '
    '<b>кофе́йник</b> bình pha cà phê.</div>'
    '<div class="hd-warn">Tiếng lóng: <b>ча́йник</b> = người mới, gà mờ — sách '
    '<b>для ча́йников</b> = «cho người mới bắt đầu».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>чай</b> trà · <b>ча́йный</b> thuộc trà (<b>ча́йная ло́жка</b> '
    'thìa nhỏ). <b>ча́шка</b> KHÔNG cùng gốc — nó từ <b>ча́ша</b>.</div>'
)

# ------------------------------------------------------------------ часы
S["часы"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">час-</span>'
    '<span class="hd-gloss">GIỜ (thẻ <b>час</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ы́</span>'
    '<span class="hd-gloss">đuôi số nhiều</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Những cái giờ» = đồng hồ. Nghĩa này chỉ có ở số nhiều, nên một '
    'cái đồng hồ vẫn là số nhiều: <b>Где мои́ часы́?</b> = đồng hồ của tôi đâu?</div>'
    '<div class="hd-warn">Cùng mặt chữ còn là số nhiều thường «các giờ»: <b>часы́ '
    'рабо́ты</b> = giờ làm việc. Đọc ngữ cảnh mà phân.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>час</b> giờ · <b>сейча́с</b> bây giờ · <b>часовщи́к</b> thợ '
    'đồng hồ</div>'
)

V = {
    # Bỏ ngoặc (cấm) và bỏ "ông" (trùng дедушка, cùng n MASC); gloss mister/gentleman.
    "господин": "ngài, quý ông",
    # Bỏ "bà" (trùng бабушка, cùng n FEM); "tiểu thư" là con nhà giàu, không phải
    # Miss/Mademoiselle — gloss lady/Miss/Madame.
    "госпожа": "quý bà, quý cô",
    # "dân cư" là cả dân số (население), không phải một người; gloss inhabitant/resident.
    "житель": "cư dân, người dân",
    # "người thủ đô" là nới rộng — gloss chỉ Muscovite/inhabitant of Moscow.
    "москвич": "người Moskva",
    # Bỏ ngoặc (cấm) và bỏ "thuộc về nước Nga" (trùng русский, cùng adj); gloss
    # "Russian (related to the state)".
    "российский": "thuộc quốc gia Nga, thuộc Liên bang Nga",
    # "xu nhỏ" không phải nghĩa; thêm tên đồng tiền mà gloss copeck/kopek xác nhận.
    "копейка": "cô-pếch, đồng xu",
    # Thêm nghĩa map/layout/ground plan mà gloss có (план города).
    "план": "kế hoạch, sơ đồ",
}
