# -*- coding: utf-8 -*-
"""k130 — language-grammar: 18 từ trộn (vị trí trên/dưới/giữa, đi xe & chở, đại từ -то/-нибудь).

Không khối hệ thống. Chỗ cần nhất quán trong lô:
(1) Tính từ đuôi MỀM -ний (ни́жний, ве́рхний, да́льний): mỗi thẻ một câu, không bảng.
(2) Gốc quay -ворот-/-врат- (наоборо́т ↔ обрати́ться k126); серед-/сред- (середи́на) cùng hiện tượng.
(3) вез-/воз- = chở bằng xe: phép so chở/mang/dẫn trải ĐÚNG MỘT lần ở привезти́, thẻ khác dẫn chiếu.
(4) -то ↔ -нибудь: quy tắc nằm ở thẻ кто́-то (k110); куда = hướng, где = vị trí.
Họ hàng: 18/18 thẻ có (чемода́н chỉ có чемода́нчик; бензи́н, пассажи́р có tính từ phái sinh).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa, ngăn bằng dấu phẩy.
V = {
    "куда-то": "đi đâu đó, tới chỗ nào đó",
    "куда-нибудь": "đi bất cứ đâu, tới bất kỳ chỗ nào",     # bỏ «đi đâu đó» — trùng куда́-то
    "где-нибудь": "ở bất cứ đâu, ở bất kỳ chỗ nào",          # bỏ «ở đâu đó» — trùng где́-то (cũ)
    "дальний": "ở xa, phía xa, đường dài",                   # bỏ «xa» — trùng далёкий (cũ)
    "наоборот": "hoàn toàn ngược lại, theo chiều ngược lại, lộn ngược",  # trùng обратно + напротив
    "привезти": "chở đến, chở tới",                          # bỏ «mang về» — trùng вернуть (cũ)
    "привозить": "chở đến, chở tới, giao đến",               # bỏ «mang đến» — trùng приносить (cũ)
    "отвезти": "đưa đi, chở đi khỏi",                        # tránh «chở đi» — trùng повезти (cũ)
    "некуда": "không có chỗ nào để đi, không còn chỗ để đặt",
}

# ---------------------------------------------------------------- середина
S["середина"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">серед-</span>'
    '<span class="hd-gloss">GIỮA — dạng Nga của <b>сред-</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ина</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái — như <b>ширина́</b> bề rộng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Khoảng giữa». Tiếng Nga hay có cặp chèn thêm nguyên âm ↔ dạng gọn: '
    '<i>серед-</i> ↔ <i>сред-</i>, y như <b>го́род</b> ↔ <i>-град</i>. Vì thế <b>сре́дний</b>, '
    '<b>среда́</b> (thứ tư — ngày giữa tuần) cùng gốc với từ này.</div>'
    '<div class="hd-warn"><b>в середи́не</b> + cách 2 = ở giữa một khoảng: <b>в середи́не '
    'ию́ля</b> giữa tháng bảy. Giữa HAI thứ thì là <b>ме́жду</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сре́дний</b> ở giữa, trung bình · <b>среда́</b> thứ tư · '
    '<b>среди́</b> giữa (những) · <b>посреди́</b> ở chính giữa</div>'
)

# ------------------------------------------------------------------ нижний
S["нижний"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ниж-</span>'
    '<span class="hd-gloss">← <b>низ</b> phần dưới (<i>з → ж</i>, như <b>ни́же</b> thấp hơn)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ний</span>'
    '<span class="hd-gloss">đuôi tính từ MỀM, chỉ vị trí</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thuộc phần dưới» ⇒ ở dưới, tầng dưới. Đuôi mềm nên đổi là '
    '<b>ни́жняя</b>, <b>ни́жнее</b> (không phải -ая/-ое), và thực tế KHÔNG dùng dạng ngắn — '
    'dạng ngắn trong bảng chỉ là lý thuyết. Cặp đối: <b>ве́рхний</b>.</div>'
    '<div class="hd-warn"><b>ни́жний эта́ж</b> tầng dưới · <b>ни́жнее бельё</b> đồ lót · '
    '<b>Ни́жний Но́вгород</b> tên một thành phố lớn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>низ</b> phần dưới · <b>внизу́</b> ở dưới · <b>вниз</b> xuống dưới · '
    '<b>ни́зкий</b> thấp</div>'
)

# ----------------------------------------------------------------- верхний
S["верхний"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">верх-</span>'
    '<span class="hd-gloss"><b>верх</b> ĐỈNH, phần trên</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ний</span>'
    '<span class="hd-gloss">đuôi tính từ MỀM, chỉ vị trí</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp đối của <b>ни́жний</b>, cùng đuôi mềm: <b>ве́рхняя</b>, '
    '<b>ве́рхнее</b>, không dùng dạng ngắn. <b>ве́рхний эта́ж</b> tầng trên, <b>ве́рхняя '
    'по́лка</b> giường tầng trên (trên tàu).</div>'
    '<div class="hd-warn"><b>ве́рхняя оде́жда</b> = áo khoác ngoài (áo choàng, áo phao), '
    'không phải «áo phía trên».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>верх</b> phần trên · <b>наверху́</b> ở trên · <b>вверх</b> lên '
    'trên · <b>све́рху</b> từ trên xuống</div>'
)

# ----------------------------------------------------------------- дальний
S["дальний"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">даль-</span>'
    '<span class="hd-gloss">← <b>даль</b> khoảng xa, cõi xa (gốc <i>дал-</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ний</span>'
    '<span class="hd-gloss">đuôi tính từ MỀM, chỉ vị trí</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc <i>дал-</i> với <b>далёкий</b>, nhưng <b>да́льний</b> hay là '
    '«cái ở phía xa / đường dài»: <b>да́льний у́гол</b> góc phía xa, <b>да́льний ро́дственник</b> '
    'bà con xa. Dạng ngắn gần như không gặp; làm vị ngữ thì nói <b>далеко́</b>.</div>'
    '<div class="hd-warn"><b>Да́льний Восто́к</b> = Viễn Đông (miền đông nước Nga, giáp '
    'Thái Bình Dương).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>далёкий</b> xa xôi · <b>далеко́</b> xa · <b>да́льше</b> xa hơn, '
    'tiếp theo · <b>даль</b> khoảng xa</div>'
)

# ------------------------------------------------------------------ отъезд
S["отъезд"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">RỜI KHỎI</span></div>'
    '<div class="hd-row"><span class="hd-piece">ъ</span>'
    '<span class="hd-gloss">dấu cứng — chỉ để tách, không mang nghĩa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-езд</span>'
    '<span class="hd-gloss">ĐI BẰNG XE — gốc của <b>е́хать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cuộc rời đi bằng xe» ⇒ sự khởi hành. Dấu <b>ъ</b> giữ <i>т</i> cứng, '
    'đọc tách <i>от|е́зд</i>. Đối nghĩa: <b>прие́зд</b> sự đến. Hay gặp: <b>пе́ред '
    'отъе́здом</b> trước lúc lên đường.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>е́хать</b> đi xe · <b>прие́зд</b> sự đến · <b>уе́хать</b> rời đi · '
    '<b>перее́хать</b> chuyển nhà · <b>по́езд</b> tàu hoả</div>'
)

# ----------------------------------------------------------------- чемодан
S["чемодан"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn từ phương Đông, không chẻ theo gốc Nga được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Học nguyên khối, kèm một thành ngữ hay gặp: <b>сиде́ть на '
    'чемода́нах</b> = «ngồi trên vali» ⇒ đồ đạc đã xếp xong, sắp sửa lên đường.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>чемода́нчик</b> vali nhỏ, cặp táp (đuôi <i>-чик</i> làm nhỏ đi)</div>'
)

# ----------------------------------------------------------------- маршрут
S["маршрут"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">марш-</span>'
    '<span class="hd-gloss"><b>марш</b> hành quân, đi đều</span></div>'
    '<div class="hd-row"><span class="hd-piece">-рут</span>'
    '<span class="hd-gloss">= tiếng Anh <i>route</i>, TUYẾN</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mượn tiếng Đức <i>Marschroute</i> «tuyến hành quân», nay là lộ '
    'trình nói chung và tuyến xe cố định: <b>маршру́т авто́буса</b> tuyến xe buýt.</div>'
    '<div class="hd-warn"><b>маршру́тка</b> = xe buýt nhỏ chạy tuyến cố định — rất hay gặp '
    'ở Nga (rút gọn từ <b>маршру́тное такси́</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>маршру́тка</b> xe buýt nhỏ · <b>марш</b> hành khúc, cuộc hành quân</div>'
)

# ----------------------------------------------------------------- отвезти
S["отвезти"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">RỜI XA khỏi chỗ mình</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вез-ти́</span>'
    '<span class="hd-gloss">CHỞ bằng xe — chính là <b>везти́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Chở rời đi» ⇒ chở ai/cái gì tới chỗ khác: <b>Я отвезу́ тебя́ в '
    'аэропо́рт</b> = tôi chở cậu ra sân bay. Thể HT, cặp: <b>отвози́ть</b>. Quá khứ như '
    '<b>везти́</b>: <b>отвёз</b> (không có -л), rồi trọng âm dồn về cuối: <b>отвезла́</b>, '
    '<b>отвезли́</b>. Phép so chở/mang/dẫn ở thẻ <b>привезти́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>везти́</b> chở · <b>вози́ть</b> chở qua lại · <b>привезти́</b> chở '
    'đến · <b>отвози́ть</b> chở đi (CHT)</div>'
)

# ------------------------------------------------------------------ бензин
S["бензин"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn châu Âu, không chẻ được — gần tiếng Anh <i>benzine</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người Anh nói <i>petrol</i>, người Mỹ <i>gas</i>, người Nga gọi theo '
    'chất <i>benzine</i>. Danh từ giống đực, chỉ chất ⇒ dùng số ít.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бензи́новый</b> chạy xăng · <b>бензоколо́нка</b> cây xăng</div>'
)

# ---------------------------------------------------------------- пассажир
S["пассажир"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пассаж-</span>'
    '<span class="hd-gloss">= <i>passage</i>, sự đi qua</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́р</span>'
    '<span class="hd-gloss">đuôi mượn chỉ NGƯỜI — như <b>банки́р</b>, <b>команди́р</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mượn tiếng Pháp <i>passager</i> — anh em với tiếng Anh '
    '<i>passenger</i>. Trọng âm nằm ở đuôi <b>-и́р</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пассажи́рский</b> chở khách: <b>пассажи́рский по́езд</b> tàu khách</div>'
)

# ---------------------------------------------------------------- привезти
S["привезти"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">TỚI NƠI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вез-ти́</span>'
    '<span class="hd-gloss">CHỞ bằng xe — chính là <b>везти́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Chở tới nơi», hay dùng cho đồ mang về sau chuyến đi: <b>Что ты '
    'привёз из Москвы́?</b> = cậu mang gì từ Moskva về? Thể HT, cặp: <b>привози́ть</b>. '
    'Quá khứ <b>привёз</b>, <b>привезла́</b> — như <b>отвезти́</b>.</div>'
    '<div class="hd-warn">Ba gốc «mang» phải tách: <i>вез-</i> chở bằng xe → <b>привезти́</b> · '
    '<i>нес-</i> cầm tay, đi bộ → <b>принести́</b> · <i>вед-</i> dẫn người → <b>привести́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>везти́</b> chở · <b>вози́ть</b> chở qua lại · <b>привози́ть</b> chở '
    'đến (CHT) · <b>отвезти́</b> chở đi</div>'
)

# --------------------------------------------------------------- привозить
S["привозить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">TỚI NƠI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-воз-и́ть</span>'
    '<span class="hd-gloss">CHỞ nhiều lượt — chính là <b>вози́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thể CHT của <b>привезти́</b>: chở tới đều đặn, nhiều lần — '
    '<b>Нам приво́зят хлеб ка́ждое у́тро</b> = sáng nào cũng có người chở bánh mì tới. Chia '
    'như <b>вози́ть</b>: ngôi «tôi» <i>з → ж</i> và trọng âm lùi: <b>привожу́</b>, '
    '<b>приво́зишь</b>. Phép so chở/mang/dẫn ở thẻ <b>привезти́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вози́ть</b> chở qua lại · <b>привезти́</b> chở đến (HT) · '
    '<b>отвози́ть</b> chở đi</div>'
)

# ------------------------------------------------------------------ некуда
S["некуда"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не́-</span>'
    '<span class="hd-gloss">KHÔNG CÓ — luôn mang trọng âm</span></div>'
    '<div class="hd-row"><span class="hd-piece">куда</span>'
    '<span class="hd-gloss">ĐI ĐÂU (hướng tới)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Không có chỗ nào để tới». Khuôn: người ở cách 3 + <b>не́куда</b> + '
    'nguyên mẫu: <b>Мне не́куда идти́</b> = tôi không có chỗ nào để đi. Cùng khuôn '
    '<b>не́когда</b>, <b>не́чего</b>.</div>'
    '<div class="hd-warn"><b>Я никуда́ не иду́</b> = tôi KHÔNG đi đâu cả · <b>Мне не́куда '
    'идти́</b> = tôi KHÔNG CÓ chỗ để đi. <i>ни-</i> cần thêm <b>не</b> + động từ chia; '
    '<i>не́-</i> đi với nguyên mẫu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>куда́</b> đi đâu · <b>никуда́</b> không đi đâu cả · <b>не́когда</b> '
    'không có thời gian · <b>не́чего</b> không có gì để</div>'
)

# ----------------------------------------------------------------- куда-то
S["куда-то"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">куда́</span>'
    '<span class="hd-gloss">ĐI ĐÂU (hướng tới)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-то</span>'
    '<span class="hd-gloss">«… nào đó» — có thật, chỉ là không biết</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng khuôn <b>кто́-то</b>, nhưng là HƯỚNG đi: <b>Он куда́-то ушёл</b> '
    '= anh ấy đi đâu đó rồi (chắc chắn đã đi, chỉ không biết đi đâu). Ở yên một chỗ thì là '
    '<b>где́-то</b>. Phép so <i>-то</i> ↔ <i>-нибудь</i> nằm ở thẻ <b>кто́-то</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>куда́</b> đi đâu · <b>где́-то</b> ở đâu đó · <b>куда́-нибу́дь</b> đi '
    'bất cứ đâu · <b>никуда́</b> không đi đâu cả</div>'
)

# ---------------------------------------------------------------- наоборот
S["наоборот"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">sang, lên (giới từ <b>на</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">оборо́т</span>'
    '<span class="hd-gloss"><i>об-</i> + <i>-ворот-</i> QUAY (<i>в</i> rụng) → vòng quay, mặt '
    'sau</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Quay sang mặt kia» ⇒ ngược lại. Cùng gốc quay (dạng gọn '
    '<i>-врат-</i>) với <b>обрати́ться</b> quay về phía ai → hỏi, nhờ. Đứng một mình làm câu '
    'đáp: — <b>Ты уста́л?</b> — <b>Наоборо́т!</b> = Mệt à? — Ngược lại hẳn!</div>'
    '<div class="hd-warn">Quay về chỗ cũ là <b>обра́тно</b>, không phải <b>наоборо́т</b>: '
    '<b>Пое́хали обра́тно</b> = quay về thôi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обра́тно</b> trở lại · <b>обрати́ться</b> quay sang hỏi · '
    '<b>оборо́т</b> vòng quay, mặt sau · <b>поворо́т</b> chỗ rẽ</div>'
)

# --------------------------------------------------------------- во-вторых
S["во-вторых"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">во</span>'
    '<span class="hd-gloss">= giới từ <b>в</b>, dạng đông cứng</span></div>'
    '<div class="hd-row"><span class="hd-piece">вторы́х</span>'
    '<span class="hd-gloss"><b>второ́й</b> thứ hai, cách 6 số nhiều</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng khuôn <b>во-пе́рвых</b>: «trong những điều thứ hai» ⇒ thứ hai là. '
    'Luôn tách bằng dấu phẩy: <b>Во-пе́рвых, уже́ по́здно, во-вторы́х, я уста́л.</b> Từ số ba '
    'chỉ còn <b>в-</b>: <b>в-тре́тьих</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>второ́й</b> thứ hai · <b>вто́рник</b> thứ ba (ngày thứ hai trong '
    'tuần) · <b>во-пе́рвых</b> thứ nhất là</div>'
)

# ------------------------------------------------------------- куда-нибудь
S["куда-нибудь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">куда́</span>'
    '<span class="hd-gloss">ĐI ĐÂU (hướng tới)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-нибудь</span>'
    '<span class="hd-gloss">«… nào cũng được» — chưa xác định</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hướng đi chưa chọn, chỗ nào cũng được: <b>Пойдём куда́-нибу́дь?</b> = '
    'đi đâu chơi không? Trong câu hỏi: <b>Ты куда́-нибу́дь е́здил?</b> = cậu có đi đâu không? '
    'Đã đi thật mà không rõ chỗ ⇒ <b>куда́-то</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>куда́-то</b> đi đâu đó · <b>где́-нибудь</b> ở bất cứ đâu · '
    '<b>кто́-нибудь</b> bất kỳ ai · <b>никуда́</b> không đi đâu cả</div>'
)

# -------------------------------------------------------------- где-нибудь
S["где-нибудь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">где</span>'
    '<span class="hd-gloss">Ở ĐÂU (vị trí)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-нибудь</span>'
    '<span class="hd-gloss">«… nào cũng được» — chưa xác định</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỗ chưa định, chỗ nào cũng được: <b>Дава́й встре́тимся где́-нибудь в '
    'це́нтре</b> = gặp nhau chỗ nào đó ở trung tâm. Câu hỏi: <b>Ты где́-нибудь рабо́таешь?</b> '
    '= cậu có đi làm ở đâu không? Biết chắc là có, chỉ không rõ chỗ ⇒ <b>где́-то</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>где</b> ở đâu · <b>где́-то</b> ở đâu đó · <b>куда́-нибу́дь</b> đi '
    'bất cứ đâu · <b>нигде́</b> không ở đâu cả</div>'
)
