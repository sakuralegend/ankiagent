# -*- coding: utf-8 -*-
"""k63 — tu-moi: 16 từ user thêm 03/08. CỐ Ý KHÔNG có trục chung — ba nhóm rời
nhau: tính từ phẩm chất (крепкий, толстый, тонкий, редкий, разный, удобный,
оригинальный, далёкий, долгий), hai dạng so sánh hơn đuôi -ше (больше, меньше),
và hư từ / trạng từ (так, теперь, домой, здравствуйте, интересно). Mỗi thẻ đứng
một mình — không khối hệ thống dùng chung, tối đa 2 ô đỏ, nhắm dưới một màn hình
iPhone. Chuẩn v3."""

# 🔴 KHÔNG dựng biến khối dùng chung rồi cộng vào mọi thẻ — xem README §3.

S = {}
V = {}

S["больше"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бо́ль-</span>'
    '<span class="hd-gloss">LỚN, NHIỀU — chính là thân của <b>большо́й</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ше</span>'
    '<span class="hd-gloss">đuôi SO SÁNH HƠN, đứng yên một dạng cho mọi giống</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vẫn là thân của <b>большо́й</b>, chỉ thay đuôi tính từ bằng '
    '<b>-ше</b> ⇒ "to hơn, nhiều hơn". Cùng bộ với <b>лу́чше</b> (tốt hơn), <b>ху́же</b> (tệ hơn): '
    'nhóm đuôi <b>-ше</b> này <i>không biến cách</i>, nên không phải nhớ bảng nào cả.</div>'
    '<div class="hd-warn"><b>Thứ đem ra so đứng ở CÁCH 2:</b> '
    '<i>Он зна́ет бо́льше меня́</i>. Muốn giữ cách 1 thì phải thêm <b>чем</b> — '
    '<i>бо́льше, чем я</i>.</div>'
    '<div class="hd-warn"><b>Cụm phải thuộc:</b> <b>бо́льше не</b> = "không còn… nữa" — '
    '<i>Я бо́льше не курю́</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>большо́й</b> to, lớn · <b>большинство́</b> đa số · '
    '<b>бо́льший</b> lớn hơn (tính từ, biến cách được) · <b>побо́льше</b> nhiều hơn một chút</div>'
)

S["далёкий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дал-</span>'
    '<span class="hd-gloss">XA — chính là <b>даль</b> (cõi xa, phía chân trời)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ёк-ий</span>'
    '<span class="hd-gloss">đuôi tính từ, cùng bộ với <b>высо́кий</b>, <b>широ́кий</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>даль</b> là danh từ chỉ khoảng không mãi tít đằng kia; '
    'thêm đuôi tính từ ⇒ "thuộc về chốn xa đó". Dạng ngắn dồn trọng âm ra đuôi '
    '(<i>далёк · далека́ · далеко́ · далеки́</i>), và hễ trọng âm rời khỏi <b>ё</b> '
    'thì <b>ё</b> tự thành <b>е</b> — vì trong tiếng Nga <b>ё</b> luôn phải mang trọng âm.</div>'
    '<div class="hd-warn"><b>Đừng lẫn với trạng từ:</b> <b>далёкий</b> đứng trước danh từ '
    '(<i>далёкая страна́</i>), còn <b>далеко́</b> đi với động từ (<i>Он живёт далеко́</i>). '
    'Dạng ngắn giống trung trùng mặt chữ với trạng từ, đó là chỗ dễ nhìn nhầm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>даль</b> cõi xa · <b>далеко́</b> ở xa · '
    '<b>да́льний</b> xa (chuyến đi, vùng đất) · <b>вдали́</b> ở đằng xa</div>'
)

S["долгий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до́лг-</span>'
    '<span class="hd-gloss">LÂU, kéo dài trong thời gian</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thân này chỉ đo THỜI GIAN: <i>до́лгий день</i> là ngày dài dằng dặc. '
    'Dạng gặp nhiều nhất của gốc lại là trạng từ <b>до́лго</b> "lâu". Dạng ngắn giống đực '
    'mọc thêm nguyên âm chạy: <i>до́лог · долга́ · до́лго · до́лги</i>.</div>'
    '<div class="hd-warn"><b>Cặp dễ chọn nhầm:</b> dài về THỜI GIAN là <b>до́лгий</b>, '
    'dài về KÍCH THƯỚC là <b>дли́нный</b> — <i>дли́нная доро́га</i> là con đường dài, '
    '<i>до́лгая доро́га</i> là chuyến đi mất nhiều giờ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>до́лго</b> lâu · <b>продолжа́ть</b> tiếp tục (thân đổi <b>г → ж</b>) · '
    '<b>продолже́ние</b> phần tiếp theo · <b>продолжи́тельный</b> kéo dài</div>'
)

S["домой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дом-</span>'
    '<span class="hd-gloss">NHÀ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́й</span>'
    '<span class="hd-gloss">đuôi cổ đã đông cứng, nay chỉ còn dùng cho riêng từ này</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một gốc đẻ ra ba từ phải tách bạch: <b>дом</b> là ngôi nhà (danh từ), '
    '<b>до́ма</b> là ĐANG Ở nhà, <b>домо́й</b> là ĐI VỀ nhà. Cứ có chuyển động hướng về nhà '
    'thì dùng <b>домо́й</b>.</div>'
    '<div class="hd-warn"><b>Hai mặt chữ chỉ khác nhau ở trọng âm:</b> <b>до́ма</b> là '
    '"ở nhà", còn <b>дома́</b> là số nhiều của <b>дом</b> (những ngôi nhà).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дом</b> nhà · <b>до́ма</b> ở nhà · '
    '<b>дома́шний</b> (thuộc) về nhà, việc nhà · <b>домохозя́йка</b> người nội trợ</div>'
)

S["здравствуйте"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">здра́в-</span>'
    '<span class="hd-gloss">KHỎE MẠNH — cùng thân với <b>здоро́вье</b> (sức khỏe)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ствуй-</span>'
    '<span class="hd-gloss">dạng mệnh lệnh của <b>здра́вствовать</b> (sống khỏe)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-те</span>'
    '<span class="hd-gloss">đuôi LỊCH SỰ, cũng là đuôi nói với nhiều người</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen là một câu chúc: "chúc ngài mạnh khỏe" — lời chúc dùng '
    'mãi thành lời chào. Chữ <b>в</b> ở giữa không phát âm, nhưng viết thì bắt buộc phải có.</div>'
    '<div class="hd-warn"><b>Bỏ -те là đổi vai:</b> <b>здра́вствуй</b> chào MỘT người thân quen; '
    'với người lạ, người trên, hay nhiều người thì phải đủ <b>здра́вствуйте</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>здоро́вье</b> sức khỏe · <b>здоро́вый</b> khỏe mạnh · '
    '<b>здра́вствовать</b> sống khỏe · <b>здра́вый</b> (đầu óc) tỉnh táo, lành mạnh</div>'
)

S["интересно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">интерес-</span>'
    '<span class="hd-gloss">SỰ QUAN TÂM — mượn quốc tế, cùng gốc với <i>interest</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-</span>'
    '<span class="hd-gloss">đuôi biến danh từ thành tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi biến tính từ thành TRẠNG TỪ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dây chuyền ba bước: <b>интере́с</b> → <b>интере́сный</b> → thay đuôi '
    'giống bằng <b>-о</b> ⇒ <b>интере́сно</b>. Nó không đứng trước danh từ mà làm vị ngữ cho '
    'cả sự việc: <i>Э́то о́чень интере́сно</i>.</div>'
    '<div class="hd-warn"><b>Người thấy hay đứng ở CÁCH 3:</b> <i>Мне интере́сно</i> = '
    'tôi thấy cuốn hút. Không nói <i>я интере́сно</i>.</div>'
    '<div class="hd-warn"><b>Nghĩa thứ hai, rất hay gặp:</b> đứng đầu câu nó thành '
    '"không biết là…, tự hỏi liệu…" — <i>Интере́сно, где он?</i></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>интере́с</b> sự quan tâm · <b>интере́сный</b> hay, hấp dẫn · '
    '<b>интересова́ться</b> quan tâm tới (đi với cách 5)</div>'
)

S["крепкий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">креп-</span>'
    '<span class="hd-gloss">CHẮC, VỮNG — cùng thân với <b>кре́пость</b> (pháo đài)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-ий</span>'
    '<span class="hd-gloss">đuôi tính từ chỉ phẩm chất</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cứ hình dung bức tường pháo đài: cái gì mang thân này thì không vỡ, '
    'không lung lay — <i>кре́пкая верёвка</i> (dây chắc), <i>кре́пкий сон</i> (giấc ngủ say), '
    '<i>кре́пкое здоро́вье</i> (sức khỏe dẻo dai). Dạng ngắn giống cái dồn trọng âm ra đuôi: '
    '<i>кре́пок · крепка́</i>.</div>'
    '<div class="hd-warn"><b>Trà và cà phê ĐẬM dùng từ này,</b> không dùng <b>си́льный</b>. '
    '<b>си́льный</b> là mạnh về LỰC (gió mạnh, người lực lưỡng).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кре́пость</b> pháo đài; độ bền · <b>кре́пко</b> chặt, chắc · '
    '<b>укрепи́ть</b> củng cố · <b>кре́пнуть</b> mạnh dần lên</div>'
)

S["меньше"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мень-</span>'
    '<span class="hd-gloss">ÍT, NHỎ — cùng gốc Ấn–Âu xa với <i>minus</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ше</span>'
    '<span class="hd-gloss">đuôi SO SÁNH HƠN, y như <b>бо́льше</b>, <b>лу́чше</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là vế đối của <b>бо́льше</b>, và một mình nó phục vụ hai từ: '
    '<b>ма́ло</b> ⇒ "ít hơn", <b>ма́ленький</b> ⇒ "nhỏ hơn". Thân <b>мал-</b> bị thay hẳn '
    'bằng <b>мень-</b> — chỗ này phải thuộc, không suy ra được.</div>'
    '<div class="hd-warn"><b>Thứ đem ra so đứng ở CÁCH 2:</b> <i>Я сплю ме́ньше тебя́</i>; '
    'giữ cách 1 thì thêm <b>чем</b> — <i>ме́ньше, чем ты</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ма́ленький</b> nhỏ · <b>ме́ньший</b> nhỏ hơn (tính từ, biến cách được) · '
    '<b>уме́ньшить</b> làm giảm · <b>меньшинство́</b> thiểu số</div>'
)

S["оригинальный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">оригина́л-</span>'
    '<span class="hd-gloss">BẢN GỐC — mượn quốc tế, cùng gốc với <i>original</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi biến danh từ thành tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ghép xong ra cái đuôi <b>-альный</b> — dấu hiệu của cả kho từ mượn '
    'quốc tế (<b>норма́льный</b>, <b>музыка́льный</b>), thấy nó là gần như đọc được ngay bằng '
    'tiếng Anh. Nhưng nghĩa dùng hằng ngày lệch khỏi '
    '"nguyên bản": nó thường là ĐỘC ĐÁO, khác người — <i>оригина́льная иде́я</i> là ý tưởng '
    'lạ và sáng tạo, chứ không phải ý tưởng gốc.</div>'
    '<div class="hd-warn"><b>Nghĩa "bản gốc" nằm ở danh từ,</b> không ở tính từ: '
    '<b>оригина́л</b> là bản gốc (đối lại <b>ко́пия</b> bản sao). Khen một người là '
    '<b>оригина́льный</b> tức khen họ độc đáo.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оригина́л</b> bản gốc · <b>оригина́льно</b> một cách độc đáo · '
    '<b>норма́льный</b> bình thường · <b>музыка́льный</b> thuộc về âm nhạc (cùng đuôi)</div>'
)

S["разный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раз-</span>'
    '<span class="hd-gloss">TẢN RA MỖI HƯỚNG — cùng mảnh với tiền tố trong <b>разби́ть</b> '
    '(đập vỡ tung)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mảnh <b>раз-</b> ở đâu cũng mang nghĩa "tách ra, mỗi mảnh một phía" '
    '⇒ mấy thứ này mỗi cái một kiểu, không cái nào giống cái nào. Vì thế nó hầu như luôn đi '
    'với danh từ số nhiều: <i>ра́зные лю́ди</i>, <i>ра́зные стра́ны</i>.</div>'
    '<div class="hd-warn"><b>Đừng thay bằng друго́й:</b> '
    '<i>ра́зные кни́ги</i> = mấy quyển sách KHÁC NHAU (so với nhau); '
    '<i>друга́я кни́га</i> = một quyển sách KHÁC (không phải quyển này).</div>'
    '<div class="hd-warn"><b>Cụm phải thuộc:</b> <b>по-ра́зному</b> (có gạch nối) = '
    '"mỗi người một kiểu, mỗi lúc một khác".</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ра́зница</b> sự chênh lệch · <b>разли́чный</b> khác biệt (trang trọng) · '
    '<b>разнообра́зный</b> đa dạng</div>'
)

S["редкий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ред-</span>'
    '<span class="hd-gloss">THƯA, cách quãng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-ий</span>'
    '<span class="hd-gloss">đuôi tính từ chỉ phẩm chất, y như <b>кре́пкий</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc là THƯA trong không gian — <i>ре́дкие во́лосы</i> (tóc thưa), '
    '<i>ре́дкий лес</i> (rừng thưa). Thưa trong thời gian thì thành "hiếm khi xảy ra". '
    'So sánh hơn đổi thân <b>д → ж</b>: <b>ре́же</b> — đúng phép biến âm của '
    '<b>ходи́ть → хожу́</b>.</div>'
    '<div class="hd-warn"><b>Dạng hay gặp nhất lại là trạng từ:</b> <b>ре́дко</b> "hiếm khi", '
    'đối lại <b>ча́сто</b> "thường xuyên" — <i>Я ре́дко смотрю́ телеви́зор</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ре́дко</b> hiếm khi · <b>ре́дкость</b> của hiếm, sự hiếm có · '
    '<b>ре́же</b> ít khi hơn</div>'
)

S["так"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — đây là một từ chỉ định cổ, đứng cùng bộ với '
    '<b>тако́й</b>, <b>там</b>, <b>тогда́</b>, <b>тот</b>: tất cả đều mở đầu bằng <b>т-</b> '
    'trỏ "cái đó, chỗ đó, lúc đó".</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nó là bản TRẠNG TỪ của <b>тако́й</b>. <b>тако́й</b> đi kèm danh từ '
    '(<i>тако́й дом</i> = một ngôi nhà như thế), còn <b>так</b> đi kèm động từ hoặc tính từ '
    '(<i>Он так говори́т</i> = anh ấy nói như thế; <i>Так хорошо́!</i> = hay đến thế!).</div>'
    '<div class="hd-warn"><b>Viết liền hay viết rời là hai nghĩa khác nhau:</b> '
    '<b>так же</b> (rời) = "y hệt như"; <b>та́кже</b> (liền) = "ngoài ra, cũng".</div>'
    '<div class="hd-warn"><b>Hai cụm phải thuộc:</b> <b>так как</b> = "bởi vì" (mở đầu mệnh đề '
    'lý do) · <b>и так да́лее</b> = "vân vân".</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тако́й</b> như thế (đi với danh từ) · <b>та́кже</b> ngoài ra, cũng · '
    '<b>так что</b> vì vậy nên · <b>тогда́</b> khi đó</div>'
)

S["теперь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — một hư từ cổ, các mảnh của nó đã dính liền từ lâu, '
    'nay không tách ra được nữa. Học nguyên khối.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ này luôn ngầm so với TRƯỚC KIA: "giờ thì khác rồi". '
    '<i>Ра́ньше бы́ло тру́дно, а тепе́рь легко́</i> — chính chữ <b>ра́ньше</b> ở vế đầu là dấu hiệu '
    'của nó. Còn <b>сейча́с</b> chỉ trỏ đúng thời điểm đang nói, không hàm ý so sánh gì cả.</div>'
    '<div class="hd-warn"><b>Chỗ hai từ KHÔNG thay được cho nhau:</b> <b>сейча́с</b> còn nghĩa '
    '"ngay lập tức, lát nữa thôi" (<i>Сейча́с иду́!</i> = tôi đến ngay đây); '
    '<b>тепе́рь</b> không bao giờ mang nghĩa đó.</div>'
)

S["толстый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">толст-</span>'
    '<span class="hd-gloss">DÀY, MẬP</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một thân dùng cho cả vật lẫn người: <i>то́лстая кни́га</i> (quyển sách '
    'dày), <i>то́лстый челове́к</i> (người béo). So sánh hơn là <b>то́лще</b> — cụm <b>ст</b> '
    'gặp đuôi so sánh thì biến thành <b>щ</b>, phép biến âm này gặp lại nhiều lần. Dạng ngắn '
    'giống cái dồn trọng âm ra đuôi: <i>толст · толста́</i>.</div>'
    '<div class="hd-warn"><b>Gọi thẳng một người là то́лстый thì nặng lời.</b> '
    'Lịch sự thì dùng <b>по́лный</b> (đầy đặn).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>толщина́</b> độ dày · <b>толсте́ть</b> béo lên · '
    '<b>толстя́к</b> gã béo</div>'
)

S["тонкий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">тон-</span>'
    '<span class="hd-gloss">MẢNH, MỎNG — cùng gốc Ấn–Âu xa với <i>thin</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-ий</span>'
    '<span class="hd-gloss">đuôi tính từ chỉ phẩm chất</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa vật lý "mỏng, mảnh" mọc thẳng ra nghĩa bóng "tinh, kín đáo": '
    '<i>то́нкая рабо́та</i> (việc làm tỉ mỉ), <i>то́нкий вкус</i> (khiếu thẩm mỹ tinh), '
    '<i>то́нкий ю́мор</i> (kiểu đùa sâu, phải nghĩ mới hiểu). So sánh hơn <b>то́ньше</b>; '
    'dạng ngắn giống đực mọc nguyên âm chạy: <i>то́нок · тонка́</i>.</div>'
    '<div class="hd-warn"><b>Người GẦY thì không dùng từ này:</b> <b>то́нкий</b> tả vật mỏng '
    'và dáng người thanh mảnh theo nghĩa đẹp, còn gầy gò vì thiếu ăn là <b>худо́й</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>то́нкость</b> nét tinh tế · <b>то́нко</b> (làm) một cách tinh tế · '
    '<b>утончённый</b> tinh xảo, cầu kỳ</div>'
)

S["удобный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố: đạt tới trạng thái vừa vặn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-доб-</span>'
    '<span class="hd-gloss">HỢP, VỪA KHỚP — cùng thân với <b>подо́бный</b> (tương tự)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ghép thẳng ba mảnh: cái gì "đạt tới chỗ vừa khớp" thì hợp với người '
    'dùng ⇒ vừa là ngồi thấy dễ chịu (<i>удо́бное кре́сло</i>), vừa là sắp xếp thấy tiện '
    '(<i>удо́бное вре́мя</i>). Một từ ôm cả hai nghĩa mà tiếng Việt tách làm hai.</div>'
    '<div class="hd-warn"><b>Hẹn giờ thì dùng dạng vị ngữ удо́бно + CÁCH 3:</b> '
    '<i>Вам удо́бно в пять?</i> = năm giờ anh có tiện không?</div>'
    '<div class="hd-warn"><b>Bản phủ định lệch nghĩa:</b> <b>неудо́бно</b> còn nghĩa '
    '"ngại, khó xử" — <i>Мне неудо́бно проси́ть</i> = tôi ngại mở lời nhờ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>удо́бство</b> tiện nghi · <b>неудо́бный</b> bất tiện · '
    '<b>подо́бный</b> tương tự · <b>удо́бно</b> tiện, thoải mái</div>'
)

# ---------------------------------------------------------------------------
# ĐỀ BÀI tiếng Việt của deck 1-go (README §2c). Chỉ sửa từ nào đang có NHIỀU HƠN
# MỘT đáp án đúng, hoặc là từ `oth` (badge chỉ hiện "oth" nên vô dụng).
# Đã đối chiếu với toàn bộ 1023 thẻ trong kho: 7 va chạm dính vào lô này đã hết.
# ---------------------------------------------------------------------------

# 'hơn, nữa' đụng тоже ('cũng, cũng vậy, nữa'); `oth` nên phải nói rõ từ loại,
# và "so sánh hơn" là thứ không field nào chứa.
V["больше"] = "trạng từ so sánh hơn: nhiều hơn, lớn hơn (thứ đem ra so đứng ở cách 2)"

# cặp đối của больше — tách bằng đúng hai nghĩa ít/nhỏ, không dùng lại chữ nào của nó.
V["меньше"] = "trạng từ so sánh hơn: ít hơn, nhỏ hơn (thứ đem ra so đứng ở cách 2)"

# 'xa' đụng далеко (trạng từ). Bỏ hẳn chữ 'xa' trơn, giữ nghĩa tả sự vật.
V["далёкий"] = "xa xôi, cách trở (miền đất, quá khứ ở tít đằng kia)"

# 'dài' đụng длинный. Bỏ chữ 'dài', nói thẳng đây là dài về THỜI GIAN.
V["долгий"] = "lâu, kéo dài nhiều thời gian (mùa đông, cuộc trò chuyện)"

# 'thú vị' + 'hay' đụng интересный, хороший, хорошо. Đổi hẳn sang chữ khác và
# nêu chỗ trạng từ này khác tính từ: nó nói về cả sự việc.
V["интересно"] = ("thấy cuốn hút, đáng chú ý — nói về cả sự việc, không đứng trước "
                  "danh từ; cũng nghĩa 'tự hỏi không biết…'")

# 'khỏe' đụng сильный và хорошо. Bỏ 'khỏe', giữ ba nét dùng thật.
V["крепкий"] = "chắc, bền, vững chãi (dây, giấc ngủ); đậm (trà, cà phê)"

# 'bây giờ' đụng сейчас. Bỏ 'bây giờ', giữ đúng nét riêng: đối lại với trước kia.
V["теперь"] = "trạng từ: giờ thì, từ nay trở đi (hàm ý trước kia khác)"

# `oth`: badge vô dụng ⇒ ghi từ loại. Điểm phân biệt là CÓ CHUYỂN ĐỘNG (khác дома).
V["домой"] = "trạng từ chỉ hướng: về nhà (đang đi về phía nhà mình)"

# `oth`: ghi từ loại + tách khỏi dạng thân mật здравствуй.
V["здравствуйте"] = "lời chào lịch sự: xin chào (với người lạ, người trên, hoặc nhiều người)"

# `oth`: ghi từ loại + tách khỏi такой (đi với danh từ).
V["так"] = ("trạng từ: như thế, theo cách đó (đi kèm động từ hoặc tính từ, "
            "không đứng trước danh từ)")
