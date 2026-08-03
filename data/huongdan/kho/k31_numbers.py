# -*- coding: utf-8 -*-
"""k31 — numbers: số đếm được vs số đo được — chữ số, con số, phân số, và ba đơn vị đo."""

# 🔴 KHÔNG dựng biến khối dùng chung (HE/LUAT/THE…) rồi cộng vào mọi thẻ (README §3).
# Luật "sau số đếm danh từ đi cách 2" chỉ trải đầy đủ ở ĐÚNG thẻ метр; килограмм
# dẫn chiếu một dòng, дюйм không nhắc lại.

S = {}

# ---------------------------------------------------------------- цифра
S["цифра"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — mượn nguyên khối: tiếng Ả Rập '
    '<i>ṣifr</i> «số không, trống rỗng» → Latin <i>cifra</i> → Đức '
    '<i>Ziffer</i> → Nga <b>ци́фра</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính gốc Ả Rập ấy đẻ ra cả <i>cipher</i> (mật mã) '
    'lẫn <i>zero</i> trong tiếng Anh: «chữ số» và «số không» vốn là một chữ.</div>'
    '<div class="hd-warn"><b>ци́фра</b> là KÝ HIỆU viết ra (0–9), '
    '<b>число́</b> là GIÁ TRỊ. 25 là một <b>число́</b> viết bằng hai '
    '<b>ци́фры</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>цифрово́й</b> thuộc chữ số → kỹ thuật số · '
    '<b>оцифрова́ть</b> số hoá</div>'
)

# ---------------------------------------------------------------- число
S["число"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">чис-</span>'
    '<span class="hd-gloss">ĐẾM — biến thể của gốc чёт-/счит-</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ло</span>'
    '<span class="hd-gloss">đuôi tạo danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cái đếm ra được» → con số. Cùng ổ với '
    '<b>счита́ть</b> (đếm) và <b>счёт</b> (hoá đơn, tỉ số).</div>'
    '<div class="hd-why">⚠️ Số nhiều kéo trọng âm về đầu VÀ chèn thêm một '
    'nguyên âm: <b>число́</b> → <b>чи́сла</b>, cách 2 số nhiều <b>чи́сел</b>.</div>'
    '<div class="hd-warn"><b>в том числе́</b> = «kể cả, trong đó có» — cụm '
    'gặp liên tục trong văn viết.</div>'
    '<div class="hd-warn"><b>число́</b> còn là NGÀY trong tháng: '
    '<b>Како́е сего́дня число́?</b> «Hôm nay ngày mấy?»</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>счита́ть</b> đếm · <b>счёт</b> hoá đơn, tỉ số · '
    '<b>чётный</b> chẵn · <b>числи́тельное</b> số từ</div>'
)

# ---------------------------------------------------------------- дробь
S["дробь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дроб-</span>'
    '<span class="hd-gloss">ĐẬP VỤN, nghiền nhỏ (<b>дроби́ть</b> = nghiền)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ь</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cái bị đập vụn ra»: một đơn vị vỡ thành phần nhỏ → '
    'phân số. Cùng chữ ấy còn là đạn ghém (chì vụn) và tiếng trống dồn.</div>'
    '<div class="hd-why">⚠️ Số nhiều: cách 1 và 4 giữ trọng âm gốc '
    '(<b>дро́би</b>), các cách còn lại đẩy trọng âm ra đuôi — <b>дробе́й</b>, '
    '<b>дробя́м</b>, <b>дробя́ми</b>.</div>'
    '<div class="hd-warn">Đọc phân số bằng số thứ tự giống cái: ½ là '
    '<b>одна́ втора́я</b>, 5/8 là <b>пять восьмы́х</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дроби́ть</b> nghiền nhỏ · <b>дро́бный</b> lẻ, '
    'thuộc phân số · <b>раздроби́ть</b> đập vỡ vụn</div>'
)

# ---------------------------------------------------------------- метр
S["метр"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">метр</span>'
    '<span class="hd-gloss">CÁI ĐO — Hy Lạp <i>métron</i> «thước đo», vào Nga '
    'qua tiếng Pháp <i>mètre</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính mảnh này đứng cuối cả một dãy từ quốc tế: '
    '<b>термо́метр</b> (đo nhiệt), <b>баро́метр</b> (đo áp suất), '
    '<b>киломе́тр</b> (nghìn mét) — thấy phần đuôi ấy là biết «cái đo».</div>'
    '<div class="hd-why">Nghĩa «bậc thầy» mà từ điển gắn kèm thuộc về một từ '
    'KHÁC: <b>мэтр</b> (mượn Pháp <i>maître</i>) — cùng âm, khác mặt chữ.</div>'
    '<div class="hd-warn">Sau số đếm, đơn vị đi cách 2: 2–4 → số ít '
    '<b>два ме́тра</b>; từ 5 trở lên → số nhiều <b>пять ме́тров</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сантиме́тр</b> xăng-ti-mét · <b>киломе́тр</b> '
    'ki-lô-mét · <b>метри́ческий</b> thuộc hệ mét</div>'
)

# ---------------------------------------------------------------- килограмм
S["килограмм"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кило-</span>'
    '<span class="hd-gloss">MỘT NGHÌN (Hy Lạp <i>chilioi</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-грамм</span>'
    '<span class="hd-gloss">gam, đơn vị khối lượng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen «nghìn gam» = 1 kg. Nắm được mảnh кило- là '
    'mở luôn <b>киломе́тр</b> «nghìn mét»: một mảnh, cả bộ đơn vị.</div>'
    '<div class="hd-why">Cách đếm sau số giống hệt <b>метр</b> — xem thẻ đó.</div>'
    '<div class="hd-warn">Nói miệng người Nga rút gọn thành <b>кило́</b>, '
    'không biến cách: <b>два кило́ я́блок</b> «hai cân táo».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>грамм</b> gam · <b>килограммо́вый</b> nặng một '
    'ki-lô (trọng âm nhảy ra đuôi) · <b>киломе́тр</b> ki-lô-mét</div>'
)

# ---------------------------------------------------------------- дюйм
S["дюйм"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — mượn thẳng tiếng Hà Lan <i>duim</i> '
    '«ngón tay cái», theo đám thợ đóng tàu vào Nga thời Pyotr I.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bề ngang đốt ngón cái ≈ 2,54 cm, đúng một '
    '<b>дюйм</b>. Tiếng Anh <i>inch</i> đi đường khác (Latin <i>uncia</i> '
    '«một phần mười hai») nhưng ra cùng cỡ.</div>'
    '<div class="hd-warn">Nga dùng hệ mét, nên <b>дюйм</b> chỉ còn sống ở màn '
    'hình, ống nước và cỡ nòng: <b>экра́н</b> 15 <b>дю́ймов</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дюймо́вый</b> dày một inch · <b>Дюймо́вочка</b> '
    '«Cô bé tí hon» của Andersen, đúng nghĩa «bé bằng một дюйм»</div>'
)

# ---------------------------------------------------------------- сколько
S["сколько"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Hư từ, không chẻ ra mảnh mang nghĩa riêng được. Nhưng '
    'nó nằm trong một cặp: hỏi bằng к-, trỏ lại bằng т-.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đổi к- thành т- là đi từ CÂU HỎI sang CÂU TRẢ LỜI: '
    '<b>ско́лько</b> bao nhiêu ↔ <b>сто́лько</b> bấy nhiêu, y như <b>как</b> ↔ '
    '<b>так</b>, <b>кто</b> ↔ <b>тот</b>, <b>когда́</b> ↔ <b>тогда́</b>.</div>'
    '<div class="hd-warn"><b>ско́лько</b> luôn kéo danh từ sang cách 2: đếm '
    'được thì số nhiều — <b>ско́лько книг</b>; không đếm được thì số ít — '
    '<b>ско́лько воды́</b>.</div>'
    '<div class="hd-warn"><b>Ско́лько сто́ит?</b> «Giá bao nhiêu?» và '
    '<b>Ско́лько тебе́ лет?</b> «Bạn bao nhiêu tuổi?» — hai câu phải thuộc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>не́сколько</b> một vài · <b>сто́лько</b> bấy nhiêu '
    '· <b>коли́чество</b> số lượng · <b>поско́льку</b> bởi vì</div>'
)


# ====================================================================
# V — sửa field Vietnamese (đề bài deck 1-go, README §2c).
# KHÔNG ghi từ loại / giống / thể / phản thân: mặt đề bài đã có badge.
# ====================================================================
V = {}

# цифра "chữ số, con số, số liệu" và число "số, con số, ngày" cùng có "con số"
# -> đề bài không tách được hai từ. Tách bằng KÝ HIỆU vs GIÁ TRỊ.
V["цифра"] = "chữ số (một ký hiệu 0–9)"
V["число"] = "số (giá trị, số lượng); ngày trong tháng"

# vi cũ: "mét (đơn vị đo chiều dài), thước kẻ, người đứng đầu".
# "người đứng đầu" là nghĩa của TỪ KHÁC — мэтр (Pháp maître). Bỏ.
V["метр"] = "mét (đơn vị đo chiều dài)"

# vi cũ: "ki-lô-gam (cân)" — "(cân)" chỉ làm đề bài rối, không tách thêm gì.
V["килограмм"] = "ki-lô-gam"

# vi cũ: "inch (đơn vị đo chiều dài), một inch, không nhượng bộ chút nào"
# — vế sau là nghĩa của thành ngữ "не уступить ни дюйма" lọt vào, không phải
# nghĩa của từ. Bỏ, thay bằng con số giúp nhận ra ngay.
V["дюйм"] = "inch (đơn vị đo chiều dài, 2,54 cm)"

# сколько chi phối cách của danh từ đi sau — không badge nào in ra thứ đó.
V["сколько"] = "bao nhiêu (hỏi số lượng, danh từ theo sau ở cách 2)"
