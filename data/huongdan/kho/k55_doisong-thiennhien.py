# -*- coding: utf-8 -*-
"""k55 — doisong-thiennhien: 14 danh từ đồ ăn/đời sống + 5 danh từ đuôi mềm
(вещь дочь любовь рожь giống cái · лёд giống NAM) — trục thật của lô là
"chữ cuối quyết định giống, và chỗ nào nguyên âm rơi khi thêm đuôi".
"""

# 🔴 KHÔNG dựng biến khối dùng chung (HE/LUAT/THE…) rồi cộng vào mọi thẻ.
# Đó là cách cũ, đã bỏ 28/07 — xem README §3.

S = {}
V = {}

# --------------------------------------------------------------- đồ ăn, món ăn
S["блюдо"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">блюд-</span>'
    '<span class="hd-gloss">đồ đựng thức ăn → món ăn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đi từ VẬT ĐỰNG sang THỨ ĐƯỢC ĐỰNG: đầu tiên là cái '
    'khay bày thức ăn, sau thành chính món bày trên đó — hệt tiếng Việt "gọi một '
    'đĩa". Nghĩa cũ còn nguyên trong <b>блю́дце</b>.</div>'
    '<div class="hd-warn"><b>блю́до</b> là MỘT MÓN trong thực đơn (đếm được: '
    'три блю́да), không phải "thức ăn" nói chung.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>блю́дце</b> đĩa lót dưới tách</div>'
)
V["блюдо"] = "món ăn (một món trong thực đơn, trong bữa)"

S["борщ"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn một âm tiết, <b>không chẻ được</b>: bốn chữ cái là '
    'trọn cả từ.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Kết bằng <b>щ</b> TRẦN, không có <b>ь</b> ⇒ giống nam '
    '(thêm <b>ь</b> vào là sang giống cái: <b>вещь</b>, <b>рожь</b> cùng lô). '
    'Trọng âm ở đuôi nên cách 5 viết chữ <b>о</b>: <b>борщо́м</b> — luật chung sau '
    'ж ш ч щ: có trọng âm viết о, không trọng âm viết е.</div>'
    '<div class="hd-warn">Dạng trần chỉ có một nguyên âm nên chưa thấy gì, nhưng vừa '
    'thêm đuôi là trọng âm rời gốc ra đuôi, và ra HẾT MỌI CÁCH: <b>борща́</b>, '
    '<b>борщу́</b>, <b>борщо́м</b>, <b>борщи́</b>.</div>'
)
# Họ hàng: BỎ CÓ Ý THỨC — tên món ăn gốc trơn, không có từ phái sinh nào user gặp.

S["буфет"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn nguyên tiếng Pháp <i>buffet</i>, <b>không chẻ được</b> '
    'bằng phụ tố Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng một chữ với "buffet" tiếng Anh nhưng nghĩa Nga rẽ sang '
    'hai thứ CÓ QUẦY: quầy bán đồ ăn nhẹ (ở trường, nhà hát) và cái tủ búp phê đựng '
    'bát đĩa.</div>'
    '<div class="hd-warn"><b>буфе́т</b> KHÔNG phải "buffet ăn tự chọn". Ăn tự chọn '
    'là <b>шве́дский стол</b> (bàn kiểu Thuỵ Điển).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>буфе́тчик</b> người đứng quầy</div>'
)
V["буфет"] = "quầy bán đồ ăn nhẹ (ở trường, nhà hát); tủ búp phê"

S["дачка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дач-</span>'
    '<span class="hd-gloss">nhà vườn ngoại ô</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-</span>'
    '<span class="hd-gloss">hậu tố nhỏ, thân mật</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>да́ча</b> nghĩa gốc là "thứ được BAN cho" (từ '
    '<b>дать</b> cho) — miếng đất nhà nước cấp; thêm <b>-ка</b> thành căn nhà vườn '
    'nho nhỏ nói bằng giọng thương mến.</div>'
    '<div class="hd-warn">Cách 2 số nhiều mọc thêm chữ <b>е</b> chen giữa ч và к: '
    '<b>да́чек</b> (không phải "дачк").</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>да́ча</b> nhà vườn ngoại ô · <b>да́чник</b> người ra nhà '
    'vườn nghỉ · <b>да́чный</b> thuộc nhà vườn</div>'
)

S["капуста"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">капуст-</span>'
    '<span class="hd-gloss">gốc mượn, không chẻ nhỏ hơn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bắp cải là những lá cuộn thành CÁI ĐẦU — và cả '
    '<b>капу́ста</b> lẫn "cabbage" tiếng Anh đều được truy về chữ Latin '
    '<i>caput</i> "đầu". Trọng âm đứng yên ở <b>-пу́-</b> suốt bảng chia.</div>'
    '<div class="hd-warn">⚠️ Mức tin: chỗ nối với <i>caput</i> là TỪ NGUYÊN (còn giả '
    'thuyết khác: <i>composita</i> "đồ ghép"), không phải luật suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>капу́стный</b> làm bằng / thuộc bắp cải</div>'
)

S["картошка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">картош-</span>'
    '<span class="hd-gloss">← карто́ф-, ф đổi thành ш</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-а</span>'
    '<span class="hd-gloss">hậu tố thân mật + giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>карто́фель</b> mượn từ tiếng Đức <i>Kartoffel</i>; người '
    'Nga cắt đuôi <b>-фель</b>, đổi ф thành ш rồi thêm <b>-ка</b> ⇒ '
    '<b>карто́шка</b>, từ của bàn ăn.</div>'
    '<div class="hd-warn">Nói hằng ngày luôn là <b>карто́шка</b>; '
    '<b>карто́фель</b> là chữ của sách vở, thực đơn, nhãn hàng.</div>'
    '<div class="hd-warn">Cách 2 số nhiều chen thêm chữ <b>е</b>: '
    '<b>карто́шек</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>карто́фель</b> khoai tây (chữ chuẩn) · '
    '<b>карто́фельный</b> làm bằng khoai tây</div>'
)
V["картошка"] = "khoai tây — cách nói thông tục, thân mật hằng ngày"

S["конфета"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">конфет-</span>'
    '<span class="hd-gloss">← Ý <i>confetto</i> đồ chế biến</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng ổ với "confection" và "confetti" tiếng Anh: '
    '<i>confetti</i> ban đầu chính là những viên KẸO nhỏ ném trong lễ hội, mãi sau '
    'mới thành giấy vụn. Trọng âm đứng yên ở <b>-фе́-</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>конфе́тка</b> viên kẹo nho nhỏ · <b>конфе́тный</b> '
    'thuộc bánh kẹo</div>'
)

S["музей"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">музе-</span>'
    '<span class="hd-gloss">← Му́за, nữ thần nghệ thuật</span></div>'
    '<div class="hd-row"><span class="hd-piece">-й</span>'
    '<span class="hd-gloss">đuôi giống nam</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiếng Hy Lạp <i>mouseion</i> = "đền của các nàng Muse". Cùng '
    'một nàng Muse đó sinh ra <b>му́зыка</b> — hai từ user đã học nằm chung một ổ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>му́за</b> nàng thơ · <b>му́зыка</b> âm nhạc · '
    '<b>музе́йный</b> thuộc bảo tàng</div>'
)

S["помидор"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">поми-</span>'
    '<span class="hd-gloss">← Ý <i>pomo</i> quả</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дор</span>'
    '<span class="hd-gloss">← Ý <i>d\'oro</i> bằng vàng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giống cà chua đầu tiên vào châu Âu có quả VÀNG, người Ý gọi '
    '<i>pomo d\'oro</i> "quả vàng"; tiếng Nga bê cả cụm thành một từ. Vậy hai mảnh '
    'trên là chữ Ý, không phải phụ tố Nga — trọng âm ở mảnh cuối: <b>помидо́р</b>.</div>'
    '<div class="hd-warn">Quả trên bàn là <b>помидо́р</b>; còn nước ép và sốt thì '
    'dùng gốc khác — <b>тома́тный сок</b>, <b>тома́тная па́ста</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>помидо́рный</b> thuộc quả cà chua</div>'
)

S["салат"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">салат-</span>'
    '<span class="hd-gloss">← Ý <i>salata</i> đồ đã muối</span></div>'
    '<div class="hd-row"><span class="hd-piece">-∅</span>'
    '<span class="hd-gloss">đuôi trần ⇒ giống nam</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng ổ chữ Latin <i>sal</i> "muối" với salad, salami, sauce '
    'tiếng Anh: món rau trộn nguyên nghĩa là "rau đã nêm muối".</div>'
    '<div class="hd-warn"><b>сала́т</b> gọi cả hai thứ: MÓN trộn và chính CÂY xà lách '
    '— <b>сала́т</b> trong rổ rau là lá xà lách, không phải món đã trộn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сала́тница</b> bát đựng salad · <b>сала́тный</b> thuộc '
    'salad, (màu) xanh lá non</div>'
)

S["фирма"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">фирм-</span>'
    '<span class="hd-gloss">← Latin <i>firmus</i> chắc, vững</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vào tiếng Nga qua tiếng Đức <i>Firma</i>, nghĩa gốc là CHỮ KÝ '
    'xác nhận — cái tên hãng đóng chắc lên hàng. Cùng gốc với "firm" và "confirm" '
    'tiếng Anh.</div>'
    '<div class="hd-warn"><b>фи́рма</b> nghiêng về hãng CÓ THƯƠNG HIỆU, nên '
    '<b>фи́рменный</b> nghĩa là "chính hãng" (<b>фи́рменный магази́н</b> cửa hàng '
    'chính hãng).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>фи́рменный</b> chính hãng, của hãng</div>'
)
V["фирма"] = "hãng, doanh nghiệp (cái tên hãng in trên sản phẩm)"

S["чашка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">чаш-</span>'
    '<span class="hd-gloss">← ча́ша chén lớn, cúp</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-а</span>'
    '<span class="hd-gloss">hậu tố nhỏ + giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thu nhỏ <b>ча́ша</b> (cái chén lớn, cái cúp) lại bằng '
    '<b>-ка</b> thì ra cái tách con có tai. Trọng âm ở gốc, đứng yên cả bảng: '
    '<b>ча́шки</b>, <b>ча́шками</b>.</div>'
    '<div class="hd-warn">KHÔNG dính gì tới <b>чай</b> (trà): <b>чай</b> mượn từ '
    'tiếng Trung, còn <b>ча́ша</b> là từ Slav cổ — ba chữ đầu giống nhau chỉ là '
    'tình cờ.</div>'
    '<div class="hd-warn">Cách 2 số nhiều chen chữ <b>е</b> để khỏi có ba phụ âm '
    'liền: <b>ча́шек</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ча́ша</b> chén lớn, cúp · <b>ча́шечка</b> tách bé xíu</div>'
)
V["чашка"] = "cái tách (chén nhỏ có tai, uống trà/cà phê, kèm đĩa lót)"

S["шоколад"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn đi vòng: Nahuatl (tiếng Aztec) <i>xocolatl</i> → Tây '
    'Ban Nha → Pháp/Đức → Nga. <b>Không chẻ được</b> bằng phụ tố Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa thì user đã biết sẵn; việc cần nhớ là MẶT CHỮ Nga: mở '
    'bằng <b>ш</b>, đóng bằng <b>д</b>, trọng âm ở âm cuối <b>-ла́д</b>.</div>'
    '<div class="hd-warn"><b>д</b> ở cuối từ bị đọc cứng thành "t", nhưng viết thì '
    'vẫn là <b>д</b> — kiểm bằng cách thêm đuôi: <b>шокола́да</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>шокола́дка</b> thanh/viên sô-cô-la · <b>шокола́дный</b> '
    'màu, vị sô-cô-la</div>'
)

S["шофёр"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">шоф-</span>'
    '<span class="hd-gloss">← Pháp <i>chauffer</i> làm nóng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ёр</span>'
    '<span class="hd-gloss">đuôi mượn chỉ NGƯỜI LÀM NGHỀ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Pháp <i>chauffeur</i> nghĩa gốc là "người đốt lò" — thời xe '
    'còn chạy bằng hơi nước. Đuôi <b>-ёр</b> luôn hút trọng âm, và <b>ё</b> thì '
    'không bao giờ đứng ở chỗ không có trọng âm.</div>'
    '<div class="hd-warn"><b>шофёр</b> là người LÀM NGHỀ lái xe, giọng hơi cũ; người '
    'đang lái xe nói chung là <b>води́тель</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">Cùng đuôi <b>-ёр</b> chỉ nghề, đều mượn Pháp: <b>актёр</b> '
    'diễn viên · <b>дирижёр</b> nhạc trưởng</div>'
)
V["шофёр"] = "tài xế, người làm nghề lái xe"

# --------------------------------------- bốn danh từ đuôi mềm giống CÁI + лёд NAM
S["вещь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вещ-</span>'
    '<span class="hd-gloss">vật, đồ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ь</span>'
    '<span class="hd-gloss">dấu mềm: biển báo giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ kết bằng ж ш ч щ mà CÓ thêm <b>ь</b> thì luôn giống '
    'cái — <b>ь</b> ở đây không đọc thành gì, nó chỉ làm biển báo. Bỏ <b>ь</b> đi là '
    'sang giống nam: <b>борщ</b>, <b>нож</b>.</div>'
    '<div class="hd-warn">Trọng âm ở gốc suốt số ít (<b>ве́щи</b>), sang số nhiều chỉ '
    'còn <b>ве́щи</b> giữ được, các cách khác đẩy hết ra đuôi: <b>веще́й</b>, '
    '<b>веща́м</b>, <b>веща́ми</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ве́щи</b> (số nhiều dùng như từ riêng) đồ đạc, hành lý · '
    '<b>вещество́</b> chất, vật chất</div>'
)

S["дочь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">доч-</span>'
    '<span class="hd-gloss">gốc Ấn–Âu "con gái"</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ь</span>'
    '<span class="hd-gloss">dấu mềm: biển báo giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc Ấn–Âu với "daughter" tiếng Anh và <i>Tochter</i> '
    'tiếng Đức. Cái <b>-r</b> của daughter chính là mảnh <b>-ер-</b> mà từ Nga mọc '
    'lại khi thêm đuôi.</div>'
    '<div class="hd-warn">Chỉ dạng trần <b>дочь</b> là ngắn; mọi cách khác chèn '
    '<b>-ер-</b> vào giữa — <b>до́чери</b>, <b>до́черью</b> — rồi số nhiều đẩy trọng '
    'âm ra đuôi: <b>дочере́й</b>, <b>дочеря́м</b>. Đúng khuôn <b>мать</b> → '
    '<b>ма́тери</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>до́чка</b> con gái (thân mật) · <b>доче́рний</b> con, '
    'trực thuộc (<b>доче́рняя компа́ния</b> công ty con)</div>'
)
V["дочь"] = "con gái (con của cha mẹ)"

S["любовь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">люб-</span>'
    '<span class="hd-gloss">yêu, thích</span></div>'
    '<div class="hd-row"><span class="hd-piece">-овь</span>'
    '<span class="hd-gloss">đuôi cũ, tạo danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>люб-</b> cùng ổ Ấn–Âu với "love" tiếng Anh, và nó có '
    'mặt trong cả họ từ user gặp hằng ngày: <b>люби́ть</b>, <b>люби́мый</b>.</div>'
    '<div class="hd-warn">Chữ <b>о</b> trong đuôi là о CHẠY: rơi mất ở cách 2/3/6 — '
    '<b>любви́</b> — và chỉ trụ lại ở cách 5: <b>любо́вью</b>.</div>'
    '<div class="hd-warn">"Yêu cái gì" thì dùng <b>к</b> + cách 3: '
    '<b>любо́вь к му́зыке</b> tình yêu âm nhạc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>люби́ть</b> yêu · <b>люби́мый</b> yêu thích nhất · '
    '<b>любо́вный</b> thuộc tình yêu</div>'
)

S["лёд"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">лёд</span>'
    '<span class="hd-gloss">gốc trơn, một âm tiết</span></div>'
    '<div class="hd-row"><span class="hd-piece">льд- / лед-</span>'
    '<span class="hd-gloss">hai mặt của cùng gốc đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>ё</b> chỉ tồn tại ở chỗ CÓ trọng âm; trọng âm rời đi thì '
    'gốc lộ chữ <b>е</b> — <b>ледяно́й</b>, <b>ледоко́л</b>. Kết bằng phụ âm trần '
    '(không có <b>ь</b>) ⇒ giống NAM, đừng để đuôi mềm của lô này kéo sai.</div>'
    '<div class="hd-warn">Thêm đuôi là nguyên âm rơi hẳn, còn <b>льд-</b>: '
    '<b>льда</b>, <b>льду</b>, <b>льдом</b>. Cách 6 có hai dạng khác việc: '
    '<b>на льду</b> (ở TRÊN mặt băng) nhưng <b>о льде</b> (nói VỀ băng).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ледяно́й</b> bằng băng, lạnh băng · <b>гололёд</b> băng '
    'đóng trên đường · <b>ледоко́л</b> tàu phá băng</div>'
)

S["рожь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рож-</span>'
    '<span class="hd-gloss">lúa mạch đen</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ь</span>'
    '<span class="hd-gloss">dấu mềm: biển báo giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc Ấn–Âu với "rye" tiếng Anh và <i>Roggen</i> tiếng '
    'Đức. Là hạt ngũ cốc nên không có số nhiều đúng nghĩa: một loại cây, một khối '
    'hạt.</div>'
    '<div class="hd-warn">Chữ <b>о</b> rơi sạch khi thêm đuôi: <b>ржи</b> (cách '
    '2/3/6), chỉ cách 5 giữ lại — <b>ро́жью</b>. Y hệt khuôn <b>любо́вь</b> → '
    '<b>любви́</b> cùng lô.</div>'
    '<div class="hd-warn">Thứ user gặp thật ở tiệm bánh: <b>ржано́й хлеб</b> — bánh '
    'mì đen làm từ lúa mạch đen.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ржано́й</b> làm bằng lúa mạch đen</div>'
)
