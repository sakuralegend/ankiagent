# -*- coding: utf-8 -*-
"""k242 — qualities::eval: tính từ mượn -ный/-и́вный/-а́рный (song song, chủ quan, vô lý, thô tục…); đỏ lên; nở rộ; từ chính trị (tư bản, độc tài, thuế quan).

Chỗ cần nhất quán trong lô:
(1) красне́ть / покрасне́ть: красн- ĐỎ + -е́ть «trở nên» — khớp кра́сный [k44], khuôn бледне́ть.
(2) -и́вн-ый = -ive: прогресси́вный, примити́вный, субъекти́вный — khớp объекти́вный [k197]; прогресс- khớp прогре́сс [k128].
(3) расцве́т: -цвет NỞ, RA HOA — khớp цвет [k58], цвето́к [k91]; рас- TOẢ RA như рассве́т [k176] (nhưng свет ≠ цвет).
(4) бе́режно: береж- GIỮ GÌN — khớp бере́чь [k149], убере́чь [k212].
(5) дипломати́ческий ← диплома́т [k148]; дикта́тор: дикт- khớp ди́ктор [k35], дикта́нт [k11]; капитали́зм: -и́зм khớp социали́зм [k145], капита́л/caput khớp капита́н [k152].
(6) по́шлина = «lệ» (custom → customs), phân biệt нало́г [k167].
Họ hàng không vắng ở thẻ nào.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "параллельный": "song song, diễn ra cùng lúc",              # «cùng lúc» trơ là trạng từ; «lớp song song» là cụm riêng, không phải nghĩa
    "дефект": "khuyết tật, lỗi, vết lỗi",                       # «khuyết điểm» là недоста́ток (shortcoming); gloss defect / blemish
    "краснеть": "đỏ lên, ửng đỏ, đỏ mặt",                       # giữ nguyên, khai để cặp thể cùng dãy
    "покраснеть": "đỏ lên, ửng đỏ, đỏ mặt",                     # như trên
    "вульгарный": "thô tục, dung tục, kém thẩm mỹ",             # «tục tĩu» = obscene, gloss không có
    "адекватный": "phù hợp, thoả đáng, hợp lý, bình thường, tỉnh táo",   # «tỉnh táo bình thường» gộp hai gloss normal + sane
    "расцвет": "sự nở rộ, sự nở hoa, thời kỳ hưng thịnh, thời kỳ đỉnh cao",   # THIẾU blossoming; «đỉnh cao» trơ là верши́на
    "буржуазный": "tư sản, kiểu tư sản",                        # «sang trọng kiểu tư sản» là nới rộng
    "протестовать": "phản đối, kháng nghị, biểu tình phản đối",  # «phản kháng» = resist, gloss không có
}

# --------------------------------------------------------------------- параллельный
S["параллельный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">паралле́ль-</span>'
    '<span class="hd-gloss">ĐƯỜNG SONG SONG — Hy Lạp <i>para</i> «cạnh» + <i>allēlōn</i> «nhau»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cạnh nhau» ⇒ song song, rồi sang thời gian: diễn ra cùng lúc. Chính là <i>parallel</i>, '
    'chữ l cũng đôi trước đơn sau: <i>лл</i> rồi <i>ль</i>. Dạng ngắn giống đực bỏ <b>ь</b>, chen <b>е</b>: '
    '<b>паралле́лен</b>; còn lại giữ <b>ь</b>: <b>паралле́льна</b>.</div>'
    '<div class="hd-warn"><b>паралле́льный класс</b> = lớp khác CÙNG KHỐI (8А và 8Б).</div>'
    '<div class="hd-warn">Song song VỚI cái gì → cách 3, không giới từ: <b>у́лица, паралле́льная реке́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>паралле́льно</b> song song, cùng lúc (trạng từ) · <b>паралле́ль</b> đường song song, vĩ tuyến</div>'
)

# --------------------------------------------------------------------- пыльный
S["пыльный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пыль-</span>'
    '<span class="hd-gloss">BỤI — chính là <b>пыль</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Có bụi» ⇒ bụi bặm, đầy bụi; chữ <b>ь</b> của <b>пыль</b> giữ nguyên trước <b>н</b>. Dạng ngắn '
    'lệch hai chỗ: giống đực bỏ <b>ь</b>, chen <b>е</b> — <b>пы́лен</b>; giống cái trọng âm ra đuôi — <b>пыльна́</b>.</div>'
    '<div class="hd-warn"><b>пы́льный</b> chỉ là phủ BỤI (kệ, đường, sách cũ). Bẩn nói chung (bùn, vết ố) là '
    '<b>гря́зный</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пыль</b> bụi · <b>пыли́нка</b> hạt bụi · <b>пылесо́с</b> máy hút bụi · '
    '<b>запыли́ться</b> bị bám bụi</div>'
)

# --------------------------------------------------------------------- бережно
S["бережно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бе́реж-</span>'
    '<span class="hd-gloss">GIỮ GÌN — <b>бере́чь</b>, г → ж như <b>бережёшь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-о</span>'
    '<span class="hd-gloss">đuôi trạng từ, từ <b>бе́режный</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm với ý GIỮ GÌN món đồ ⇒ nhẹ nhàng, nâng niu. Trọng âm lùi hẳn về đầu: '
    '<b>бере́чь</b> nhưng <b>бе́режно</b>.</div>'
    '<div class="hd-warn"><b>осторо́жно</b> là cẩn thận vì sợ NGUY HIỂM (đi chậm kẻo ngã); <b>бе́режно</b> là nhẹ tay '
    'vì QUÝ món đồ đang cầm.</div>'
    '<div class="hd-warn"><b>бе́режно относи́ться к</b> + cách 3 = nâng niu, giữ gìn (cái gì): '
    '<b>бе́режно относи́ться к приро́де</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бе́режный</b> nâng niu · <b>бере́чь</b> giữ gìn · <b>убере́чь</b> che chở được · '
    '<b>бережли́вый</b> tiết kiệm, biết giữ của</div>'
)

# --------------------------------------------------------------------- дефект
S["дефект"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">де-</span>'
    '<span class="hd-gloss">Latin <i>de-</i> «hụt đi, thiếu»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-фе́кт</span>'
    '<span class="hd-gloss">Latin <i>-fectum</i> «được làm», như <b>эффе́кт</b>, <i>effect</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Làm mà hụt» ⇒ chỗ lỗi trên món đồ, khuyết tật. Chính là <i>defect</i>, trọng âm ở cuối. '
    'Lỗi ở ĐÂU thì <b>на</b> hoặc <b>в</b> + cách 6: <b>дефе́кт на рукаве́</b>.</div>'
    '<div class="hd-warn">Lỗi của ĐỒ VẬT, cơ thể: <b>дефе́кт ре́чи</b> tật nói. Khuyết điểm trong tính nết là '
    '<b>недоста́ток</b>; lỗi do làm sai là <b>оши́бка</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дефе́ктный</b> bị lỗi · <b>эффе́кт</b> hiệu ứng, hiệu quả · <b>эффекти́вный</b> hiệu quả '
    '(tính từ) · <b>дефици́т</b> sự thiếu hụt</div>'
)

# --------------------------------------------------------------------- краснеть
S["краснеть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">красн-</span>'
    '<span class="hd-gloss">ĐỎ — <b>кра́сный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ть</span>'
    '<span class="hd-gloss">TRỞ NÊN như thế</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Trở nên đỏ» ⇒ đỏ lên; với người ⇒ đỏ mặt. Tính từ màu + <i>-е́ть</i> = tự đổi sang màu đó: '
    '<b>бле́дный → бледне́ть</b> tái đi. Chia đều, giữ <b>е</b>: <b>красне́ю, красне́ешь</b>. '
    'Cặp HT: <b>покрасне́ть</b>.</div>'
    '<div class="hd-warn">Đỏ mặt VÌ gì → <b>от</b> + cách 2: <b>красне́ть от стыда́</b>. Xấu hổ THAY cho ai → '
    '<b>за</b> + cách 4: <b>Мне прихо́дится за тебя́ красне́ть</b>.</div>'
    '<div class="hd-warn">Tự đỏ lên, không có tân ngữ. Sơn, nhuộm (cái gì) là <b>кра́сить</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кра́сный</b> đỏ · <b>краснота́</b> vết đỏ, sắc đỏ · <b>кра́ска</b> sơn, thuốc màu · '
    '<b>краси́вый</b> đẹp</div>'
)

# --------------------------------------------------------------------- покраснеть
S["покраснеть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">chỉ báo hoàn thành, không thêm nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">красн-</span>'
    '<span class="hd-gloss">ĐỎ — <b>кра́сный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ть</span>'
    '<span class="hd-gloss">TRỞ NÊN như thế</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đã trở nên đỏ» ⇒ đỏ lên, đỏ mặt (một lần, thành kết quả). Cùng khuôn '
    '<b>бледне́ть → побледне́ть</b> tái mặt. Chia như cặp CHT <b>красне́ть</b>: <b>покрасне́ю, покрасне́ешь</b>.</div>'
    '<div class="hd-warn">Quá khứ tả bộ phận đang đỏ lúc này, phải hợp với nó: <b>У меня́ глаза́ покрасне́ли</b> mắt '
    'tôi đỏ lên rồi · <b>Ко́жа покрасне́ла</b> da bị đỏ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>красне́ть</b> (CHT) · <b>покрасне́ние</b> chỗ tấy đỏ · <b>кра́сный</b> đỏ</div>'
)

# --------------------------------------------------------------------- прогрессивный
S["прогрессивный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">прогре́сс-</span>'
    '<span class="hd-gloss">BƯỚC TỚI TRƯỚC — <b>прогре́сс</b> (<i>про-</i> tới trước + <i>-гресс</i> bước)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́вн-ый</span>'
    '<span class="hd-gloss">= đuôi <i>-ive</i> của từ quốc tế</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Hay bước tới trước» ⇒ tiến bộ, cấp tiến = <i>progressive</i>. Trọng âm rời gốc sang đuôi: '
    '<b>прогре́сс → прогресси́вный</b>. Dạng ngắn giống đực chen <b>е</b>: <b>прогресси́вен</b>, còn lại đều.</div>'
    '<div class="hd-warn"><b>прогресси́вный нало́г</b> = thuế LUỸ TIẾN (thu nhập càng cao, thuế suất càng «bước lên»), '
    'không phải «thuế tiến bộ».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>прогре́сс</b> sự tiến bộ · <b>прогресси́ровать</b> tiến triển · <b>регре́сс</b> sự thoái bộ · '
    '<b>агресси́вный</b> hung hăng</div>'
)

# --------------------------------------------------------------------- примитивный
S["примитивный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">примит-</span>'
    '<span class="hd-gloss">ĐẦU TIÊN — Latin <i>primus</i>, như <i>prime</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́вн-ый</span>'
    '<span class="hd-gloss">= đuôi <i>-ive</i> của từ quốc tế</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thuộc buổi đầu tiên» ⇒ nguyên thuỷ, sơ khai = <i>primitive</i>. '
    'Dạng ngắn giống đực chen <b>е</b>: <b>примити́вен</b>, còn lại đều: <b>примити́вна</b>.</div>'
    '<div class="hd-warn">Đời thường hay là lời CHÊ — quá thô sơ, nông cạn: <b>примити́вная шу́тка</b> câu đùa rẻ tiền, '
    '<b>примити́вный челове́к</b> người đầu óc đơn giản.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>примити́вно</b> một cách thô sơ · <b>примити́в</b> thứ thô sơ, đơn giản · '
    '<b>премье́ра</b> buổi ra mắt (lần ĐẦU)</div>'
)

# --------------------------------------------------------------------- субъективный
S["субъективный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">субъе́кт-</span>'
    '<span class="hd-gloss">CHỦ THỂ, người đang xét — như <b>субъе́кт</b>, <i>subject</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́вн-ый</span>'
    '<span class="hd-gloss">= đuôi <i>-ive</i> của từ quốc tế</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dựa vào cảm nhận của chính người nói, không vào sự vật ⇒ chủ quan. Chính là '
    '<i>subjective</i>; ngược nghĩa <b>объекти́вный</b> khách quan. Dạng ngắn giống đực chen <b>е</b>: '
    '<b>субъекти́вен</b>, còn lại đều.</div>'
    '<div class="hd-warn">Có <b>ъ</b> giữa <b>б</b> và <b>е</b>, đúng chỗ như <b>объе́кт</b>: tách phụ âm khỏi <b>е</b>.</div>'
    '<div class="hd-warn">Chỉ là «theo cảm nhận riêng», không phải «chủ quan khinh địch» (<b>самоуве́ренный</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>субъе́кт</b> chủ thể · <b>субъекти́вность</b> tính chủ quan · '
    '<b>объе́кт</b> đối tượng · <b>объекти́вный</b> khách quan</div>'
)

# --------------------------------------------------------------------- абсурдный
S["абсурдный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">абсу́рд-</span>'
    '<span class="hd-gloss">SỰ VÔ LÝ — <b>абсу́рд</b>, Latin <i>absurdus</i> «chối tai»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Nghe chối tai» ⇒ vô lý, phi lý, ngớ ngẩn. Tiếng Anh <i>absurd</i> đã là tính từ; tiếng Nga '
    'phải thêm <i>-н-</i> vì <b>абсу́рд</b> là danh từ. Dạng ngắn giống đực chen <b>е</b>: <b>абсу́рден</b>, '
    'còn lại đều: <b>абсу́рдна</b>.</div>'
    '<div class="hd-warn">Câu cảm thán dùng danh từ <b>Э́то абсу́рд!</b> hoặc dạng ngắn <b>Э́то абсу́рдно!</b> = '
    'Thật vô lý!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>абсу́рд</b> sự vô lý · <b>абсу́рдно</b> thật vô lý · <b>абсу́рдность</b> tính vô lý</div>'
)

# --------------------------------------------------------------------- вульгарный
S["вульгарный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вульг-</span>'
    '<span class="hd-gloss">ĐÁM ĐÔNG — Latin <i>vulgus</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́рн-ый</span>'
    '<span class="hd-gloss">= đuôi <i>-ar</i> của từ quốc tế, như <b>популя́рный</b> <i>popular</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Kiểu đám đông, chợ búa» ⇒ thô tục, dung tục, ăn mặc thì kém thẩm mỹ = <i>vulgar</i>. '
    'Có <b>ь</b> sau <b>л</b>. Dạng ngắn giống đực chen <b>е</b>: <b>вульга́рен</b>, còn lại đều.</div>'
    '<div class="hd-warn">Hợp với gu và cách nói: <b>вульга́рное пла́тье</b>, <b>вульга́рный анекдо́т</b>. Thô lỗ với '
    'người khác (cộc cằn, xẵng) thì là <b>гру́бый</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вульга́рно</b> một cách thô tục · <b>вульга́рность</b> sự thô tục</div>'
)

# --------------------------------------------------------------------- адекватный
S["адекватный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ад-</span>'
    '<span class="hd-gloss">Latin <i>ad-</i> «tới»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-екват-</span>'
    '<span class="hd-gloss">Latin <i>aequus</i> «BẰNG», như <b>эква́тор</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Ngang bằng với điều cần» ⇒ phù hợp, thoả đáng, hợp lý; người cư xử đúng mực ⇒ bình thường, '
    'tỉnh táo. Dạng ngắn giống đực chen <b>е</b>: <b>адеква́тен</b>, còn lại đều.</div>'
    '<div class="hd-warn">Anh <i>adequate</i> nghiêng về «vừa ĐỦ», tiếng Nga thì không: đủ là <b>доста́точный</b>.</div>'
    '<div class="hd-warn"><b>неадеква́тный</b> (nói về người) = cư xử không bình thường, mất kiểm soát.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>адеква́тно</b> một cách phù hợp · <b>неадеква́тный</b> không bình thường · '
    '<b>эква́тор</b> xích đạo (đường chia BẰNG nhau)</div>'
)

# --------------------------------------------------------------------- расцвет
S["расцвет"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рас-</span>'
    '<span class="hd-gloss">TOẢ, BUNG ra</span></div>'
    '<div class="hd-row"><span class="hd-piece">-цве́т</span>'
    '<span class="hd-gloss">NỞ, RA HOA — <b>цвето́к</b>, <b>цвести́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Hoa bung nở hết» ⇒ sự nở rộ; nghĩa bóng: thời kỳ hưng thịnh, đỉnh cao của nghệ thuật, thành '
    'phố, đời người. Nở rộ CỦA cái gì → cách 2: <b>расцве́т культу́ры</b>.</div>'
    '<div class="hd-warn">Khác đúng một chữ: <b>расцве́т</b> (<b>цвет</b>, hoa nở) ≠ <b>рассве́т</b> '
    '(<b>свет</b>, ánh sáng) bình minh.</div>'
    '<div class="hd-warn"><b>в расцве́те сил</b> = ở độ sung sức nhất.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>расцвести́</b> nở rộ (HT) · <b>цвести́</b> nở hoa · <b>цвето́к</b> bông hoa · '
    '<b>цвет</b> màu</div>'
)

# --------------------------------------------------------------------- пошлина
S["пошлина"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по́шл-</span>'
    '<span class="hd-gloss">«đã ĐI», đã thành lệ — như <b>пошла́</b> của <b>пойти́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ин-а</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Xưa nay vẫn đi như thế» = lệ ⇒ khoản nộp theo lệ: thuế quan, lệ phí. Tiếng Anh đi đúng đường '
    'ấy: <i>custom</i> tục lệ → <i>customs</i> thuế hải quan. Đánh vào hàng gì → <b>на</b> + cách 4: '
    '<b>по́шлина на таба́к</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: nối với <b>пойти́</b> là từ nguyên, không phải luật suy ra được.</div>'
    '<div class="hd-warn"><b>нало́г</b> = thuế nói chung (thu nhập, nhà đất); <b>по́шлина</b> = thu khi hàng qua biên '
    'giới hoặc khi làm giấy tờ, kiện tụng (<b>госпо́шлина</b> lệ phí nhà nước).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>беспо́шлинный</b> miễn thuế · <b>пойти́</b> đi · <b>про́шлый</b> trước, đã qua '
    '(«đã ĐI qua»)</div>'
)

# --------------------------------------------------------------------- дипломатический
S["дипломатический"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">диплома́т-</span>'
    '<span class="hd-gloss">NHÀ NGOẠI GIAO — <b>диплома́т</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ческ-ий</span>'
    '<span class="hd-gloss">đuôi tính từ = tiếng Anh <i>-ic</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><i>diplomat-ic</i> ⇒ thuộc ngoại giao. Trọng âm dời về đúng chữ <b>и́</b> trước '
    '<i>-ческий</i>: <b>диплома́тия → дипломати́ческий</b>, như <b>демокра́тия → демократи́ческий</b>.</div>'
    '<div class="hd-warn">Khen ai KHÉO LÉO, tế nhị thì hay dùng <b>дипломати́чный</b>: '
    '<b>дипломати́чный отве́т</b> câu trả lời khéo. <b>дипломати́ческий</b> là của NGÀNH ngoại giao: '
    '<b>дипломати́ческий па́спорт</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>диплома́т</b> nhà ngoại giao · <b>диплома́тия</b> ngoại giao · '
    '<b>дипло́м</b> bằng tốt nghiệp</div>'
)

# --------------------------------------------------------------------- буржуазный
S["буржуазный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">буржуа́з-</span>'
    '<span class="hd-gloss">GIAI CẤP TƯ SẢN — <b>буржуази́я</b> (Pháp <i>bourgeoisie</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Pháp <i>bourgeois</i> vốn là dân sống trong <i>bourg</i> «thị trấn» — cùng gốc <i>-бург</i> '
    'của <b>Петербу́рг</b>. Dân thành thị có của ⇒ tư sản. '
    'Dạng ngắn giống đực chen <b>е</b>: <b>буржуа́зен</b>, còn lại đều.</div>'
    '<div class="hd-warn">Ngoài sách sử thường có ý mỉa: lối sống sang, ham tiện nghi — <b>буржуа́зные привы́чки</b> '
    'thói quen tư sản.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>буржуази́я</b> giai cấp tư sản · <b>буржуа́</b> nhà tư sản (không biến cách) · '
    '<b>буржу́й</b> tên tư sản (khinh)</div>'
)

# --------------------------------------------------------------------- капитализм
S["капитализм"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">капитал-</span>'
    '<span class="hd-gloss">VỐN — <b>капита́л</b> (Latin <i>caput</i> «cái đầu»)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́зм</span>'
    '<span class="hd-gloss">CHỦ NGHĨA (= <i>-ism</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chế độ lấy VỐN làm gốc ⇒ chủ nghĩa tư bản = <i>capitalism</i>. Cùng khuôn với từ đối lập '
    '<b>социали́зм</b>: giống đực, trọng âm ở <i>-и́зм</i>, dùng số ít. Người thì đổi sang <i>-и́ст</i>: '
    '<b>капитали́ст</b>.</div>'
    '<div class="hd-warn">DƯỚI chế độ nào → <b>при</b> + cách 6: <b>при капитали́зме</b> dưới thời tư bản.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>капита́л</b> vốn · <b>капитали́ст</b> nhà tư bản · <b>капиталисти́ческий</b> tư bản chủ nghĩa · '
    '<b>капита́н</b> thuyền trưởng (cũng từ <i>caput</i>)</div>'
)

# --------------------------------------------------------------------- диктатор
S["диктатор"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дикт-</span>'
    '<span class="hd-gloss">ĐỌC RA, ĐỌC CHO CHÉP (Latin <i>dictare</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́тор</span>'
    '<span class="hd-gloss">NGƯỜI làm, như <b>организа́тор</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người ĐỌC lệnh, cả nước phải chép theo ⇒ nhà độc tài = <i>dictator</i>. Số nhiều đều, trọng âm '
    'đứng yên: <b>дикта́торы</b>.</div>'
    '<div class="hd-warn">Cùng gốc, khác người: <b>ди́ктор</b> (ngắn, trọng âm đầu) chỉ là phát thanh viên.</div>'
    '<div class="hd-warn"><b>диктова́ть</b> cũng giữ cả hai nghĩa: đọc cho chép · áp đặt '
    '(<b>диктова́ть усло́вия</b> áp đặt điều kiện).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>диктату́ра</b> chế độ độc tài · <b>дикта́торский</b> kiểu độc tài · '
    '<b>дикта́нт</b> bài chính tả · <b>ди́ктор</b> phát thanh viên</div>'
)

# --------------------------------------------------------------------- протестовать
S["протестовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">протест-</span>'
    '<span class="hd-gloss">SỰ PHẢN ĐỐI = <i>protest</i> (Latin <i>pro-</i> ra trước + <i>testari</i> làm chứng)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова́-ть</span>'
    '<span class="hd-gloss">đuôi động từ, chia đổi <i>-ова-</i> → <i>-у-</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đứng ra trước mọi người mà lên tiếng» ⇒ phản đối, biểu tình. Chia như <b>голосова́ть</b>: '
    '<b>протесту́ю, протесту́ешь</b>.</div>'
    '<div class="hd-warn">Phản đối CÁI GÌ → <b>про́тив</b> + cách 2, không dùng cách 4 trần: '
    '<b>протестова́ть про́тив войны́</b>.</div>'
    '<div class="hd-warn"><b>возража́ть</b> là cãi lại bằng lời trong câu chuyện; <b>протестова́ть</b> mạnh và công khai '
    'hơn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>проте́ст</b> sự phản đối · <b>проте́стный</b> mang tính phản đối · '
    '<b>протеста́нт</b> tín đồ Tin Lành</div>'
)

B = {
    "docbangmat": 96,
    "loitubat": 5,   # примити́вный: mảnh đánh trọng âm giả «прими́т-» -> примит- (cả протест- cùng kiểu)
                     # про́шлый: dịch «năm ngoái» (chỉ đúng khi đi với год) -> «trước, đã qua»
                     # покрасне́ть: «hợp số» thiếu hợp giống -> «hợp với nó»
                     # буржуа́зный: bourg «thành thị» nói quá -> «thị trấn»
                     # эффе́кт: gloss «ấn tượng» -> «hiệu ứng»
    "nguonsai": 0,
    "baolen": [
        "V cần duyệt (7 thẻ đổi thật): параллельный (BỎ lớp song song; cùng lúc trơ -> diễn ra cùng lúc) · дефект (khuyết điểm -> khuyết tật) · вульгарный (tục tĩu -> dung tục) · адекватный (tách «tỉnh táo bình thường» thành bình thường, tỉnh táo) · расцвет (THÊM sự nở hoa; phồn thịnh -> hưng thịnh; đỉnh cao trơ -> thời kỳ đỉnh cao) · буржуазный (BỎ «sang trọng kiểu tư sản») · протестовать (BỎ phản kháng). краснеть, покраснеть khai trong V nhưng không đổi.",
        "примитивный: gloss thẻ bị bó vào nghĩa «xã hội sơ khai» nên V giữ nguyên thuỷ, sơ khai; nghĩa đời thường hay gặp hơn là «thô sơ, quá đơn giản» — thẻ dạy ở ô đỏ, user muốn thì thêm «thô sơ» vào đề.",
        "Câu GƯỢNG капитализм câu 3 («национальных капитализмах», số nhiều) -> Профессор полтора часа говорил об истории капитализма. / The professor talked about the history of <b>capitalism</b> for an hour and a half. / Giáo sư nói về lịch sử <b>chủ nghĩa tư bản</b> suốt tiếng rưỡi.",
        "Câu GƯỢNG расцвет câu 3 («расцветы пионов», số nhiều) -> При этом царе начался расцвет русской культуры. / Under this tsar the <b>flourishing</b> of Russian culture began. / Dưới thời sa hoàng này, <b>thời kỳ hưng thịnh</b> của văn hoá Nga bắt đầu.",
        "Dịch расцвет câu 1: «đang <b>nở rộ</b> đồ ăn đường phố» (động từ) -> «Thành phố tôi giờ đang có <b>sự nở rộ</b> thật sự của đồ ăn đường phố.»; câu 2 «độ sung sức nhất» không có trong đề -> «Bà bảo tôi đang ở đúng <b>thời kỳ đỉnh cao</b> của sức lực.»",
        "Câu GƯỢNG пошлина câu 2 («Благодаря» cho chuyện xấu) -> После введения новой пошлины телефоны сразу подорожали. / After the new <b>duty</b> was introduced, phones immediately got more expensive. / Sau khi áp <b>thuế nhập khẩu</b> mới, điện thoại đắt lên ngay. Câu 1 dịch «Thuế hải quan» không có trong đề -> <b>Thuế nhập khẩu</b>.",
        "Câu GƯỢNG примитивный câu 2 («какая была примитивная жизнь тогда») -> В музее показывают примитивную жизнь древних людей. / The museum shows the <b>primitive</b> life of ancient people. / Bảo tàng cho thấy đời sống <b>nguyên thuỷ</b> của người cổ đại.",
        "Dịch lệch đề: адекватный câu 1 «bình thường tử tế» -> <b>bình thường</b> · вульгарный câu 3 «thô kệch» -> <b>kém thẩm mỹ</b> · дефект câu 2 «lỗi sản phẩm» -> <b>lỗi</b> · протестовать câu 3 Anh «argue» -> Don't <b>protest</b>.",
        "Thẻ cũ диктор [k35]: V lô ghi «người đọc bản tin trên đài/TV» là lời giải thích kèm dấu gạch chéo (trái §2c) — nếu trên thẻ vẫn thế thì nên là «phát thanh viên, người đọc bản tin». Ngoài ra không gặp lỗi trọng âm ở thẻ cũ nào.",
        "Mức tin ghi ô đỏ: по́шлина ← пойти (từ nguyên). Cố ý KHÔNG đưa по́шлый «tầm thường» vào họ dù cùng nguồn: nghĩa đã trôi xa, chỉ gây rối.",
        "Trùng hết nghĩa trong lô chỉ có краснеть/покраснеть — badge thể tách. протестовать không khai cặp thể (không có cặp HT chuẩn). Câu ví dụ đọc từ _opus_k242.json, không đọc Anki.",
    ],
}
