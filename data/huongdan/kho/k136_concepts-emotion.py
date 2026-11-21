# -*- coding: utf-8 -*-
"""k136 — concepts::emotion: 20 từ cảm xúc / phẩm chất, phần lớn là CẶP THỂ đi đôi.

Không khối hệ thống. Chỗ cần nhất quán trong lô:
(1) Cặp thể: thẻ gốc (сравнить, обидеть, обидеться, радоваться, целоваться) giải gốc đầy đủ,
    thẻ cặp kia dẫn chiếu + nói đúng một chỗ khác.
(2) Gốc оби́д- = об- + вид- (từ nguyên, hạ mức tin) — khớp оби́да (k04); д→ж (оби́жу, обижа́ть).
(3) Phụ tố mở lớp: -тельный (решительный ↔ удивительный), -лив- (вежливый ↔ счастливый),
    -ота́ (доброта), -ество (мужество ↔ детство).
(4) -ова- co thành -у- khi chia: интересу́ет, ра́дуюсь, целу́юсь.
Họ hàng: không thẻ nào cố ý vắng.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa, ngăn bằng dấu phẩy.
V = {
    "сравнить": "so sánh",                              # bỏ «(xong)» — nhãn thể trá hình
    "интересовать": "làm quan tâm, làm hứng thú",       # «thấy hứng thú» là nghĩa của интересоваться
    "нервный": "bồn chồn, căng thẳng, dễ kích động, thuộc thần kinh",  # thiếu nghĩa gốc nerve-/neural
    "скромный": "khiêm tốn",                            # RÚT «giản dị» — trùng простой (đã nạp)
    "решительный": "quyết đoán",                        # RÚT «dứt khoát» — trùng твёрдый (đã nạp)
    "стыдно": "xấu hổ, hổ thẹn",                        # «thấy nhục» quá nặng — đó là унижение
    "обидеть": "làm tổn thương, xúc phạm",              # bỏ «(một lần)»
    "обижать": "làm tổn thương, xúc phạm",              # bỏ «ai» chen giữa
    "обрадоваться": "vui mừng, mừng rỡ",                # «lên» là nhãn thể trá hình
    "поцеловаться": "hôn nhau",                         # bỏ «(một lần)»
    "обидеться": "tự ái, cảm thấy bị xúc phạm",         # bỏ «(một lần)»; «bị chạm lòng» không phải tiếng Việt thường
}

# ------------------------------------------------------------- сравнить
S["сравнить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">tiền tố, ở đây: đặt CẠNH NHAU</span></div>'
    '<div class="hd-row"><span class="hd-piece">-равн-</span>'
    '<span class="hd-gloss">BẰNG NHAU — <b>ра́вный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đặt cạnh nhau xem có bằng không» ⇒ so sánh. So sánh cái gì (cách 4) '
    'VỚI cái gì → <b>с</b> + cách 5: <b>сравни́ть ко́шку с соба́кой</b>. Cặp chưa hoàn thành là '
    '<b>сра́внивать</b>.</div>'
    '<div class="hd-warn"><b>по сравне́нию с</b> + cách 5 = so với: '
    '<b>по сравне́нию с про́шлым го́дом</b> = so với năm ngoái.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ра́вный</b> bằng nhau · <b>всё равно́</b> sao cũng được · '
    '<b>сравне́ние</b> sự so sánh · <b>сра́внивать</b> so sánh (CHT)</div>'
)

# ----------------------------------------------------------- сравнивать
S["сравнивать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сравн-</span>'
    '<span class="hd-gloss">đặt cạnh nhau xem có BẰNG không — như <b>сравни́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ть</span>'
    '<span class="hd-gloss">đuôi tạo thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp chưa hoàn thành của <b>сравни́ть</b> (gốc giải ở thẻ đó). '
    '<b>-ива-</b> kéo trọng âm lùi lên đầu: <b>сра́внивать</b>, <b>сра́вниваю</b> — y như '
    '<b>пока́зывать</b>. Vẫn <b>с</b> + cách 5: <b>Не сра́внивай меня́ с ним!</b> = Đừng so sánh '
    'tôi với anh ta!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сравни́ть</b> so sánh (HT) · <b>сравне́ние</b> sự so sánh · '
    '<b>ра́вный</b> bằng nhau</div>'
)

# --------------------------------------------------------- интересовать
S["интересовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">интере́с-</span>'
    '<span class="hd-gloss">mối quan tâm — chính <b>интере́с</b> (Anh <i>interest</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-ть</span>'
    '<span class="hd-gloss">biến danh từ thành động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Gây ra mối quan tâm» ⇒ làm (ai) quan tâm. <b>-ова-</b> co thành '
    '<b>-у-</b> khi chia: <b>интересу́ет</b>.</div>'
    '<div class="hd-warn">Chủ ngữ là CÁI gây hứng thú, người đứng ở cách 4: '
    '<b>Меня́ интересу́ет исто́рия</b> = Tôi quan tâm tới lịch sử. Thêm <b>-ся</b> là đảo vai: '
    '<b>Я интересу́юсь исто́рией</b> (cách 5).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>интере́с</b> mối quan tâm · <b>интере́сный</b> thú vị · '
    '<b>интересова́ться</b> quan tâm tới</div>'
)

# ---------------------------------------------------------- сомневаться
S["сомневаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">tiền tố, không mang nghĩa rõ ở đây</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мн-</span>'
    '<span class="hd-gloss">gốc NGHĨ (từ nguyên) — cùng nhà <b>мне́ние</b> ý kiến</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ева́-ть-ся</span>'
    '<span class="hd-gloss">đuôi động từ + <b>-ся</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Động từ của <b>сомне́ние</b> sự nghi ngờ: «mang mối nghi trong đầu». '
    'Chia đều, giữ nguyên <b>-ва-</b>: <b>сомнева́юсь</b>, <b>сомнева́ешься</b>.</div>'
    '<div class="hd-warn">Nghi VỀ cái gì → <b>в</b> + cách 6: <b>Я сомнева́юсь в э́том</b> = '
    'Tôi không chắc chuyện đó lắm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сомне́ние</b> sự nghi ngờ · <b>без сомне́ния</b> chắc chắn · '
    '<b>несомне́нно</b> không nghi ngờ gì · <b>мне́ние</b> ý kiến</div>'
)

# -------------------------------------------------------------- доброта
S["доброта"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">добр-</span>'
    '<span class="hd-gloss">TỐT LÀNH, tấm lòng — <b>до́брый</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ота́</span>'
    '<span class="hd-gloss">→ danh từ chỉ TÍNH CHẤT (như <b>красота́</b> vẻ đẹp)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Tính tốt lành của tấm lòng» ⇒ lòng tốt. Trọng âm nhảy ra đuôi: '
    '<b>до́брый</b> → <b>доброта́</b>. Đuôi <b>-а</b> ⇒ giống cái.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>до́брый</b> tốt bụng · <b>добро́</b> điều thiện · '
    '<b>Добро́ пожа́ловать!</b> hoan nghênh</div>'
)

# ------------------------------------------------------------ удивление
S["удивление"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố, không mang nghĩa riêng ở đây</span></div>'
    '<div class="hd-row"><span class="hd-piece">-див-</span>'
    '<span class="hd-gloss">ĐIỀU LẠ — <b>ди́во</b> (từ cổ)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-л-е́ние</span>'
    '<span class="hd-gloss">→ danh từ giống trung; <b>л</b> chèn sau <b>в</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>удиви́ться</b>: «gặp điều lạ» ⇒ sự ngạc nhiên. Chữ '
    '<b>л</b> chính là chữ trong <b>удивлю́сь</b>, <b>удивля́ться</b>.</div>'
    '<div class="hd-warn"><b>к моему́ удивле́нию</b> = trước sự ngạc nhiên của tôi — khuôn '
    '<b>к</b> + cách 3 y như <b>к сожале́нию</b>. Còn <b>на удивле́ние</b> = đến bất ngờ: '
    '<b>на удивле́ние бы́стро</b> = nhanh đến bất ngờ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>удиви́ться</b> ngạc nhiên · <b>удиви́ть</b> làm ngạc nhiên · '
    '<b>удиви́тельный</b> đáng kinh ngạc</div>'
)

# ------------------------------------------------------------- вежливый
S["вежливый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">веж-</span>'
    '<span class="hd-gloss">gốc cổ: BIẾT, hiểu lễ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лив-ый</span>'
    '<span class="hd-gloss">→ tính từ «có tính…» (như <b>счастли́вый</b>, '
    '<b>тала́нтливый</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Người biết phép tắc» ⇒ lịch sự. Trạng từ <b>ве́жливо</b>; phủ định chỉ '
    'cần thêm <b>не-</b>: <b>неве́жливый</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: nối <b>веж-</b> với «biết» là từ nguyên, không phải luật. '
    'Nó giải thích vì sao <b>неве́жество</b> (cùng gốc, thêm <b>не-</b>) lại là «sự dốt nát».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ве́жливость</b> sự lịch sự · <b>ве́жливо</b> một cách lịch sự · '
    '<b>неве́жливый</b> bất lịch sự</div>'
)

# -------------------------------------------------------------- нервный
S["нервный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">нерв-</span>'
    '<span class="hd-gloss">DÂY THẦN KINH (Anh <i>nerve</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">→ tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thuộc thần kinh» (<b>не́рвная систе́ма</b> hệ thần kinh) ⇒ nghĩa rộng: '
    'thần kinh dễ bị kích, hay bồn chồn. Dạng ngắn chen <b>е</b>, giống cái đẩy trọng âm ra '
    'đuôi: <b>не́рвен</b>, <b>нервна́</b>.</div>'
    '<div class="hd-warn"><b>Он не́рвный</b> thường nói về TÍNH KHÍ (người dễ kích động). Đang hồi hộp '
    'lúc này thì dùng động từ: <b>Я не́рвничаю</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>нерв</b> dây thần kinh · <b>не́рвничать</b> bồn chồn · '
    '<b>не́рвный срыв</b> suy sụp thần kinh</div>'
)

# ------------------------------------------------------------- скромный
S["скромный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">скром-</span>'
    '<span class="hd-gloss">gốc mượn (nhiều khả năng qua tiếng Ba Lan), không chẻ tiếp được</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">→ tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trục nghĩa là «không phô ra»: người không khoe ⇒ khiêm tốn; vật không '
    'phô ⇒ giản dị, ít ỏi: <b>скро́мная зарпла́та</b> lương khiêm tốn. Dạng ngắn chen <b>е</b>, '
    'giống cái đẩy trọng âm ra đuôi: <b>скро́мен</b>, <b>скромна́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>скро́мность</b> sự khiêm tốn · <b>скро́мно</b> một cách khiêm tốn · '
    '<b>нескро́мный</b> thiếu khiêm tốn</div>'
)

# ---------------------------------------------------------- решительный
S["решительный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">реш-и-</span>'
    '<span class="hd-gloss">QUYẾT, gỡ nút — <b>реши́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-тельный</span>'
    '<span class="hd-gloss">→ tính từ «có tính/khả năng làm việc đó» (như '
    '<b>удиви́тельный</b>, <b>внима́тельный</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Người hay quyết, quyết là làm» ⇒ quyết đoán, dứt khoát. Nói về sự việc: '
    '<b>реши́тельный моме́нт</b> = thời khắc quyết định. Dạng ngắn chỉ chen <b>е</b>, trọng âm '
    'đứng yên: <b>реши́телен</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>реши́ть</b> quyết định · <b>реше́ние</b> quyết định, lời giải · '
    '<b>реши́тельно</b> dứt khoát · <b>нереши́тельный</b> do dự</div>'
)

# -------------------------------------------------------------- мужество
S["мужество"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">муж-</span>'
    '<span class="hd-gloss">ĐÀN ÔNG (nghĩa rộng cũ của <b>муж</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ество</span>'
    '<span class="hd-gloss">→ danh từ chỉ PHẨM CHẤT, trạng thái (đuôi -ство, như <b>де́тство</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Phẩm chất của người đàn ông» ⇒ lòng dũng cảm — cùng đường với Latin '
    '<i>vir</i> «đàn ông» → <i>virtue</i>. Nay dùng cho mọi người, cả phụ nữ. Trọng âm ở gốc: '
    '<b>му́жество</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>муж</b> chồng · <b>мужчи́на</b> đàn ông · <b>мужско́й</b> thuộc nam '
    'giới · <b>му́жественный</b> dũng cảm</div>'
)

# --------------------------------------------------------------- стыдно
S["стыдно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">стыд-</span>'
    '<span class="hd-gloss">NỖI XẤU HỔ — <b>стыд</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-о</span>'
    '<span class="hd-gloss">→ trạng từ làm vị ngữ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Khuôn «người ở cách 3 + <b>сты́дно</b>», như <b>мне хо́лодно</b>: '
    '<b>Мне сты́дно</b> = tôi xấu hổ; quá khứ <b>Мне бы́ло сты́дно</b>. Xấu hổ VÌ ai → '
    '<b>за</b> + cách 4: <b>Мне сты́дно за тебя́</b>.</div>'
    '<div class="hd-warn"><b>Как тебе́ не сты́дно!</b> = Không biết xấu hổ à! — câu mắng dùng '
    'hằng ngày.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>стыд</b> nỗi xấu hổ · <b>стыди́ться</b> xấu hổ (động từ) · '
    '<b>бессты́дный</b> vô liêm sỉ</div>'
)

# -------------------------------------------------------------- обидеть
S["обидеть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">QUANH, LƯỚT QUA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ид-</span>'
    '<span class="hd-gloss">gốc NHÌN — <b>ви́деть</b>, chữ <b>в</b> rụng sau <b>об-</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е-ть</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2 (như <b>ви́деть</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Nhìn lướt qua, coi như không có» ⇒ làm ai tủi, xúc phạm (từ nguyên, '
    'không phải luật). Ngôi «tôi» <b>д→ж</b>: <b>оби́жу</b>, <b>оби́дишь</b> — chính chữ '
    '<b>ж</b> ấy làm nên cặp <b>обижа́ть</b>.</div>'
    '<div class="hd-warn">Người bị xúc phạm → cách 4: <b>Я не хоте́л тебя́ оби́деть</b> = '
    'Anh không cố ý làm em buồn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оби́да</b> nỗi tủi thân · <b>оби́деться</b> tự ái · '
    '<b>оби́дно</b> thật tủi · <b>обижа́ть</b> (CHT)</div>'
)

# -------------------------------------------------------------- обижать
S["обижать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">обиж-</span>'
    '<span class="hd-gloss"><b>оби́д-</b> với <b>д→ж</b> — như <b>оби́деть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi tạo thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp chưa hoàn thành của <b>оби́деть</b> (gốc giải ở thẻ đó). Chia đều '
    'lớp 1, <b>ж</b> giữ suốt bảng: <b>обижа́ю</b>, <b>обижа́ешь</b>.</div>'
    '<div class="hd-warn">Làm tổn thương lặp đi lặp lại ⇒ bắt nạt: '
    '<b>Не обижа́й мла́дшего бра́та!</b> = Đừng bắt nạt em trai!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оби́деть</b> (HT) · <b>обижа́ться</b> giận dỗi · '
    '<b>оби́да</b> nỗi tủi thân</div>'
)

# ------------------------------------------------------------ обидеться
S["обидеться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">оби́де-ть</span>'
    '<span class="hd-gloss">làm ai tủi — <b>оби́деть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">quay việc về CHÍNH MÌNH</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Tự thấy mình bị làm tủi» ⇒ tự ái, phật lòng. Chia như '
    '<b>оби́деть</b>, ngôi «tôi» <b>д→ж</b>: <b>оби́жусь</b>, <b>оби́дишься</b>. Cặp chưa hoàn '
    'thành: <b>обижа́ться</b>.</div>'
    '<div class="hd-warn">Giận AI → <b>на</b> + cách 4: <b>Ты на меня́ оби́делась?</b> = '
    'Em giận anh à?</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оби́да</b> nỗi tủi thân · <b>оби́деть</b> làm ai tủi · '
    '<b>оби́дчивый</b> hay tự ái</div>'
)

# ------------------------------------------------------------ обижаться
S["обижаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">обижа́-ть</span>'
    '<span class="hd-gloss">làm ai tủi (CHT) — <b>обижа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">quay việc về CHÍNH MÌNH</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp chưa hoàn thành của <b>оби́деться</b> (gốc giải ở thẻ đó). Vẫn '
    '<b>на</b> + cách 4: <b>обижа́ться на дру́га</b> = giận bạn.</div>'
    '<div class="hd-warn"><b>Не обижа́йся!</b> = Đừng giận nhé! — câu cửa miệng; lời «đừng…» '
    'thông thường dùng thể chưa hoàn thành.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оби́да</b> nỗi tủi thân · <b>оби́дчивый</b> hay tự ái · '
    '<b>оби́деться</b> (HT)</div>'
)

# ----------------------------------------------------------- радоваться
S["радоваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рад-</span>'
    '<span class="hd-gloss">VUI — <b>рад</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-ть-ся</span>'
    '<span class="hd-gloss">khuôn động từ + <b>-ся</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thấy vui trong lòng» ⇒ vui mừng. <b>-ова-</b> co thành <b>-у-</b>, '
    'trọng âm đứng ở gốc: <b>ра́дуюсь</b>, <b>ра́дуешься</b>.</div>'
    '<div class="hd-warn">Mừng VÌ cái gì → cách 3, không giới từ (y như <b>рад тебе́</b>): '
    '<b>ра́доваться пода́рку</b> = mừng vì món quà.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рад</b> vui · <b>ра́дость</b> niềm vui · <b>ра́достный</b> hân hoan · '
    '<b>обра́доваться</b> (HT)</div>'
)

# --------------------------------------------------------- обрадоваться
S["обрадоваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">chỉ làm thành thể hoàn thành, KHÔNG thêm nghĩa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ра́доваться</span>'
    '<span class="hd-gloss">vui mừng — <b>ра́доваться</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp hoàn thành của <b>ра́доваться</b>: khoảnh khắc BỪNG vui khi nghe, '
    'thấy gì. Vẫn cách 3: <b>Она́ обра́довалась письму́</b> = Cô ấy mừng vì lá thư. Chia: '
    '<b>обра́дуюсь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рад</b> vui · <b>ра́дость</b> niềm vui · <b>ра́доваться</b> (CHT)</div>'
)

# ----------------------------------------------------------- целоваться
S["целоваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">целова́-ть</span>'
    '<span class="hd-gloss">hôn — <b>целова́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">ở đây: LẪN NHAU (như <b>встреча́ться</b> gặp nhau)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hai người cùng làm với nhau ⇒ hôn nhau. <b>-ова-</b> co thành <b>-у-</b>: '
    '<b>целу́юсь</b>, <b>целу́ешься</b>. Người kia → <b>с</b> + cách 5: '
    '<b>целова́ться с ней</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>целова́ть</b> hôn · <b>поцелу́й</b> nụ hôn · '
    '<b>поцелова́ться</b> (HT)</div>'
)

# --------------------------------------------------------- поцеловаться
S["поцеловаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">làm thành thể hoàn thành: trọn MỘT lần</span></div>'
    '<div class="hd-row"><span class="hd-piece">-целова́ться</span>'
    '<span class="hd-gloss">hôn nhau — <b>целова́ться</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp hoàn thành của <b>целова́ться</b> (giải ở thẻ đó): hôn nhau một cái. '
    'Chia: <b>поцелу́емся</b>; vẫn <b>с</b> + cách 5.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поцелова́ть</b> hôn một cái · <b>поцелу́й</b> nụ hôn · '
    '<b>целова́ть</b> hôn</div>'
)

B = {
    "docbangmat": 101,
    "loitubat": 2,
    "nguonsai": 1,
    "baolen": [
        "V скромный 'khiêm tốn' và решительный 'quyết đoán': RÚT còn một nghĩa để gỡ va chạm với простой/твёрдый — cần duyệt.",
        "V có chuỗi nghĩa MỚI chưa đối chiếu toàn bộ sưu tập (agent bị chặn đọc Anki): нервный 'bồn chồn, dễ kích động, thuộc thần kinh', стыдно 'hổ thẹn', обрадоваться 'vui mừng, mừng rỡ', интересовать 'làm quan tâm, làm hứng thú' — luồng chính nên chạy congcu.py vacham.",
        "nguonsai: gloss Anh của интересовать ghi 'to be interested in' — đó là nghĩa của интересоваться, đã bỏ khỏi V.",
        "Không chắc: сравнить — nghĩa 'đặt cạnh nhau' của с- là suy diễn; скромный mượn qua Ba Lan (đã hạ: 'nhiều khả năng'); сомневаться nối -мн- với мнение và вежливый nối веж- với 'biết' là từ nguyên (đã ghi mức tin).",
        "Giữ nguyên V cũ của сравнивать, сомневаться, доброта, удивление, вежливый, мужество, радоваться, целоваться, обижаться — không thấy lỗi.",
    ],
}
