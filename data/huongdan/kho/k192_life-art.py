# -*- coding: utf-8 -*-
"""k192 — life::art (lô trộn): đồ bếp, món ăn, việc nhà, sân khấu — phần lớn là từ mượn.

Chỗ cần nhất quán trong lô:
(1) засну́ть / засыпа́ть: за- BẮT ĐẦU + gốc ngủ сн-/сып- — khớp thẻ просну́ться/просыпа́ться [k129],
    сон [k114]. Nghĩa «lấp đất» của засыпать là từ khác (gốc сы́пать), cùng cách nói như thẻ просыпа́ться.
(2) кры́шка ← кры́ша [k118] «кры́- CHE, PHỦ».
(3) сигнализа́ция ← сигна́л [k154]: từ mượn, chỉ tách đuôi quốc tế -изация.
(4) театра́льный ← теа́тр [k39]: теа́тр không chẻ, chỉ tách đuôi -а́льный.
(5) убо́рка ← убра́ть/убира́ть [k122]: у- + бр-/бер-/бир-/бор- LẤY.
(6) мука́ = BỘT (không phải му́ка «nỗi khổ») — ghi sự khác trọng âm.
Họ hàng cố ý vắng ở салфе́тка, лапша́, беко́н, кекс, про́бка, орке́стр: từ mượn đứng một mình,
không có phái sinh thông dụng nào đáng dạy.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "засыпать": "ngủ thiếp đi, chìm vào giấc ngủ",   # bỏ «lấp đất vào» (từ đồng tự khác, mục 2786) và «buồn ngủ rồi ngủ»
    "пробка": "tắc đường, ùn tắc giao thông, nút chai, nút bịt",  # thiếu hẳn cork/stopper/plug mà gloss có
}

# --------------------------------------------------------------------- салфетка
S["салфетка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn châu Âu (họ hàng với <i>serviette</i>), không chẻ theo tiếng Nga. '
    'Đuôi <b>-ка</b> cho biết giống cái.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><i>Serviette</i> = khăn ăn. Giấy ăn là <b>бума́жная салфе́тка</b> (khăn ăn bằng giấy). '
    'Nguyên âm chạy ở cách 2 số nhiều: <b>нет салфе́ток</b>.</div>'
)

# --------------------------------------------------------------------- мука
S["мука"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ chất liệu, thường chỉ dùng số ít: <b>мешо́к муки́</b> = một bao bột. '
    'Tính từ <b>мучно́й</b> lộ phép biến âm <b>к → ч</b>.</div>'
    '<div class="hd-warn">Trọng âm đổi nghĩa: <b>мука́</b> = bột · <b>му́ка</b> = nỗi đau khổ, dằn vặt.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мучно́й</b> làm từ bột · <b>мучно́е</b> đồ làm từ bột (bánh, mì)</div>'
)

# --------------------------------------------------------------------- лапша
S["лапша"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn (nhiều khả năng từ tiếng Turk), không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ tập hợp, chỉ số ít — một bát mì vẫn là <b>лапша́</b>. '
    'Trọng âm ở cuối và giữ nguyên: <b>лапшу́</b>, <b>с лапшо́й</b>.</div>'
    '<div class="hd-warn"><b>ве́шать лапшу́ на у́ши</b> = «treo mì lên tai» ⇒ lừa phỉnh, nói xạo. Câu rất hay nghe.</div>'
)

# --------------------------------------------------------------------- крем
S["крем"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn Pháp <i>crème</i> (= <i>cream</i>), không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chất sánh đặc: kem bôi da hoặc kem phết bánh. Cách 2 có thêm dạng <b>кре́му</b>, '
    'chỉ dùng khi nói «một ít kem» (kiểu <b>ча́ю</b>).</div>'
    '<div class="hd-warn">Kem ăn lạnh là <b>моро́женое</b>, không phải <b>крем</b>.</div>'
    '<div class="hd-warn"><b>тона́льный крем</b> = kem nền trang điểm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кре́мовый</b> bằng kem; màu kem</div>'
)

# --------------------------------------------------------------------- бекон
S["бекон"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn tiếng Anh <i>bacon</i>, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhận ra chứ không phải học. Chỉ cần nhớ trọng âm ở cuối: <b>беко́н</b>, '
    'và đây là danh từ chất liệu: <b>яи́чница с беко́ном</b> = trứng ốp la với thịt xông khói.</div>'
)

# --------------------------------------------------------------------- кекс
S["кекс"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn tiếng Anh, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>cakes</i> — tiếng Nga mượn dạng số nhiều của Anh rồi dùng như số ít, '
    'nên số nhiều Nga lại thêm đuôi nữa: <b>ке́ксы</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: chuyện mượn từ <i>cakes</i> là từ nguyên, không phải luật suy ra được.</div>'
    '<div class="hd-warn"><b>кекс</b> là bánh nướng dạng ổ/cốc, thường có nho khô; bánh kem sinh nhật là <b>торт</b>.</div>'
)

# --------------------------------------------------------------------- посуда
S["посуда"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng rõ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-суд-а</span>'
    '<span class="hd-gloss">VẬT ĐỰNG — như trong <b>сосу́д</b> cái bình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đồ để đựng» ⇒ bát đĩa nói chung. Danh từ tập hợp, chỉ số ít: '
    '<b>мыть посу́ду</b> = rửa bát (cả chồng bát vẫn là số ít).</div>'
    '<div class="hd-warn">⚠️ Mức tin: nối với <b>сосу́д</b> là từ nguyên, không phải luật suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сосу́д</b> bình, vật chứa · <b>посудомо́ечная маши́на</b> máy rửa bát</div>'
)

# --------------------------------------------------------------------- пробка
S["пробка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn (nhiều khả năng gốc Hà Lan/Đức), không chẻ theo tiếng Nga — không dính gì tới <b>про́бовать</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc là <b>nút chai</b>. Xe nối đuôi bịt kín con đường như nút bịt cổ chai ⇒ '
    'tắc đường. Nguyên âm chạy: <b>нет про́бок</b> = đường không tắc.</div>'
    '<div class="hd-warn"><b>стоя́ть в про́бке</b> = đang kẹt xe · <b>попа́сть в про́бку</b> = bị kẹt xe.</div>'
)

# --------------------------------------------------------------------- уборка
S["уборка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">RỜI KHỎI, ra xa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бор-</span>'
    '<span class="hd-gloss">LẤY — gốc <i>бр-/бер-</i> của <b>брать</b>, mặt <i>о</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">→ danh từ chỉ việc, giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>убра́ть</b>: «lấy đi cho khỏi chỗ» ⇒ dọn dẹp. Cũng hình ảnh đó '
    'ngoài đồng: <b>убо́рка урожа́я</b> = thu hoạch mùa màng (lấy lúa khỏi ruộng).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>убра́ть</b> dọn (HT) · <b>убира́ть</b> dọn (CHT) · <b>убо́рщица</b> cô lao công</div>'
)

# --------------------------------------------------------------------- крышка
S["крышка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кры́ш-</span>'
    '<span class="hd-gloss">từ <b>кры́ша</b> mái nhà — gốc <b>кры-</b> CHE, PHỦ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">thu nhỏ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Mái nhà nhỏ» úp trên nồi, trên hộp ⇒ nắp, vung. <b>Закры́ть кры́шкой</b> = đậy nắp lại — '
    'cùng gốc che. Nguyên âm chạy: <b>без кры́шек</b>.</div>'
    '<div class="hd-warn">Khẩu ngữ: <b>Тебе́ кры́шка!</b> = Mày tiêu rồi! (bị «đậy nắp»).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кры́ша</b> mái nhà · <b>закры́ть</b> đóng · <b>откры́ть</b> mở</div>'
)

# --------------------------------------------------------------------- игла
S["игла"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Số ít trọng âm ở cuối, sang số nhiều nhảy lên đầu: <b>игла́ → и́глы</b>. '
    'Trong đời thường người ta hay nói <b>иго́лка</b> hơn; <b>игла́</b> nghe trang trọng, kỹ thuật hơn '
    '(kim tiêm, gai nhím, lá kim).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>иго́лка</b> cây kim (khẩu ngữ)</div>'
)

# --------------------------------------------------------------------- сигнализация
S["сигнализация"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сигнал-</span>'
    '<span class="hd-gloss">từ mượn <b>сигна́л</b> tín hiệu</span></div>'
    '<div class="hd-row"><span class="hd-piece">-иза́ция</span>'
    '<span class="hd-gloss">= <i>-ization</i>, danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Hệ thống phát tín hiệu» ⇒ báo động. Đuôi <b>-иза́ция</b> đổi thẳng sang '
    '<i>-ization</i> tiếng Anh. Câu hay gặp: <b>Срабо́тала сигнализа́ция</b> = chuông báo động kêu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сигна́л</b> tín hiệu</div>'
)

# --------------------------------------------------------------------- диагноз
S["диагноз"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">диа-</span>'
    '<span class="hd-gloss">XUYÊN QUA (Hy Lạp)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-гноз</span>'
    '<span class="hd-gloss">BIẾT, nhận ra (Hy Lạp <i>gnōsis</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>diagnosis</i>: «nhìn xuyên qua triệu chứng mà biết bệnh». '
    'Khác tiếng Anh ở trọng âm: <b>диа́гноз</b>, nhấn vào <i>а</i>.</div>'
    '<div class="hd-warn"><b>поста́вить диа́гноз</b> = chẩn đoán (nghĩa đen «đặt chẩn đoán»).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>диагно́стика</b> ngành / việc chẩn đoán</div>'
)

# --------------------------------------------------------------------- наркоман
S["наркоман"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">нарко-</span>'
    '<span class="hd-gloss">MA TUÝ (Hy Lạp <i>narkē</i> tê dại)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ма́н</span>'
    '<span class="hd-gloss">NGƯỜI MÊ — như <i>maniac</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Người mê ma tuý» ⇒ con nghiện. Đổi <b>-ма́н</b> thành <b>-ма́ния</b> là ra '
    'chứng bệnh: <b>наркома́ния</b> = chứng nghiện ma tuý.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>нарко́тик</b> ma tuý · <b>наркома́ния</b> chứng nghiện · '
    '<b>нарко́з</b> gây mê</div>'
)

# --------------------------------------------------------------------- заснуть
S["заснуть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">BẮT ĐẦU, bước vào trạng thái</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сн-</span>'
    '<span class="hd-gloss">NGỦ — gốc của <b>сон</b>, <b>спать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-у́ть</span>'
    '<span class="hd-gloss"><b>-ну-</b> = một lần, xong ngay → thể hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Bước vào giấc ngủ» ⇒ ngủ thiếp đi — ngược hẳn với <b>просну́ться</b> «ra khỏi giấc ngủ». '
    'Chia như <b>просну́ться</b>: <b>засну́</b>, <b>заснёшь</b>. Cặp thể: <b>засыпа́ть</b>.</div>'
    '<div class="hd-warn"><b>Не могу́ засну́ть.</b> = Tôi không ngủ được (trằn trọc mãi không vào giấc).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>засыпа́ть</b> (CHT) · <b>спать</b> ngủ · <b>сон</b> giấc ngủ · '
    '<b>просну́ться</b> tỉnh dậy</div>'
)

# --------------------------------------------------------------------- засыпать
S["засыпать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">BẮT ĐẦU, bước vào trạng thái</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сып-</span>'
    '<span class="hd-gloss">NGỦ — mặt khác của <b>сп-</b>/<b>сн-</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành, chia đều: <b>засыпа́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp chưa hoàn thành của <b>засну́ть</b> — thói quen hoặc đang thiu thiu: '
    '<b>Я засыпа́ю в оди́ннадцать</b> = tôi thường ngủ lúc 11 giờ. Khuôn y hệt '
    '<b>просну́ться → просыпа́ться</b>.</div>'
    '<div class="hd-warn">Nghĩa «lấp đất, đổ đầy» trong từ điển là từ khác cùng mặt chữ (gốc <b>сы́пать</b> rắc, đổ) '
    '— thẻ này không học nghĩa đó.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>засну́ть</b> (HT) · <b>просыпа́ться</b> tỉnh dậy · <b>сон</b> giấc ngủ</div>'
)

# --------------------------------------------------------------------- фантастика
S["фантастика"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">фантаст-</span>'
    '<span class="hd-gloss">TƯỞNG TƯỢNG, kỳ ảo (như <i>fantastic</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ика</span>'
    '<span class="hd-gloss">→ danh từ chỉ cả một lĩnh vực, thể loại (như <b>му́зыка</b>, <b>фи́зика</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thể loại tưởng tượng» ⇒ truyện giả tưởng. Nói về đời thường thì '
    '<b>Э́то фанта́стика!</b> = khó tin thật!</div>'
    '<div class="hd-warn"><b>нау́чная фанта́стика</b> = khoa học viễn tưởng (sci-fi).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>фанта́зия</b> trí tưởng tượng · <b>фантасти́ческий</b> kỳ ảo, khó tin</div>'
)

# --------------------------------------------------------------------- драма
S["драма"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn Hy Lạp <i>drama</i> («hành động»), không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng chữ <i>drama</i>, và nghĩa trượt y như tiếng Anh: từ «vở kịch» sang '
    '«chuyện bi đát» ngoài đời.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>драмати́ческий</b> thuộc kịch; bi đát · <b>драмату́рг</b> nhà soạn kịch · '
    '<b>мелодра́ма</b> phim tình cảm sướt mướt</div>'
)

# --------------------------------------------------------------------- театральный
S["театральный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">театр-</span>'
    '<span class="hd-gloss">từ <b>теа́тр</b> nhà hát (mượn, không chẻ tiếp)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́льный</span>'
    '<span class="hd-gloss">→ tính từ «thuộc về…», kéo trọng âm về mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trọng âm dịch: <b>теа́тр → театра́льный</b>. <b>театра́льный институ́т</b> = '
    'trường sân khấu. Nghĩa bóng như <i>theatrical</i>: <b>театра́льный жест</b> = cử chỉ làm màu.</div>'
    '<div class="hd-why">Dạng ngắn giống đực chèn thêm <b>е</b>: <b>театра́лен</b>; hầu như chỉ gặp ở nghĩa bóng «làm màu».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>теа́тр</b> nhà hát · <b>кинотеа́тр</b> rạp chiếu phim</div>'
)

# --------------------------------------------------------------------- ритм
S["ритм"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn Hy Lạp <i>rhythmós</i> (= <i>rhythm</i>), không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhận ra chứ không phải học. Dùng cả ngoài âm nhạc: <b>ритм жи́зни</b> = nhịp sống.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ритми́чный</b> nhịp nhàng, đều đặn</div>'
)

# --------------------------------------------------------------------- оркестр
S["оркестр"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn (Hy Lạp <i>orkhēstra</i>, qua tiếng Pháp), không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>orchestra</i>, nhưng trọng âm ở giữa: <b>орке́стр</b>. '
    'Thêm tính từ phía trước là ra loại dàn nhạc: <b>симфони́ческий орке́стр</b> = dàn nhạc giao hưởng.</div>'
    '<div class="hd-warn"><b>духово́й орке́стр</b> = ban nhạc kèn đồng (đây là nghĩa «brass band» trong từ điển).</div>'
)

# --------------------------------------------------------------------- статуя
S["статуя"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn Latin <i>statua</i> (= <i>statue</i>), không chẻ theo tiếng Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhận ra từ <i>statue</i>. Trọng âm ở âm đầu: <b>ста́туя</b>; đuôi <b>-я</b> → giống cái.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>статуэ́тка</b> tượng nhỏ</div>'
)

B = {
    "docbangmat": 53,
    "loitubat": 3,   # посуда: câu «đừng nối với суд toà án» nói quá — theo Vasmer суд và сосуд có thể cùng *sǫdъ -> bỏ, chỉ giữ Mức tin
                     # мука: «chỉ dùng số ít» sai (có му́ки = các loại bột) -> «thường chỉ dùng số ít»
                     # оркестр: «đứng SAU một tính từ» sai vị trí (tính từ đứng trước) -> sửa câu
    "nguonsai": 1,   # засыпать: gloss Anh/Việt trộn nghĩa của đồng tự засы́пать «lấp đất» -> bác, V chỉ giữ nghĩa ngủ
    "baolen": [
        "MIEN_TRU THÊM 1 mục (đồng tự thật, đúng ngoại lệ được phép): «мука́» trong data/huongdan/mientru.py — "
        "chính từ đầu thẻ (mục id 58505, bột) bị cửa TRONG AM LECH kêu vì nouns.csv chỉ có му́ка «nỗi khổ». "
        "Không né được vì là từ đầu thẻ và ô đỏ cố ý dạy cặp мука́ ↔ му́ка. Luồng chính duyệt; phương án lùi: "
        "bỏ in đậm мука́/му́ка trong ô đỏ rồi gỡ mục.",
        "V cần duyệt (2): засыпать «ngủ thiếp đi, chìm vào giấc ngủ» (bỏ «lấp đất vào» của đồng tự và "
        "«buồn ngủ rồi ngủ»); пробка thêm «nút chai, nút bịt» (gloss cork/stopper/plug, đang thiếu hẳn).",
        "Trùng nghĩa CÓ CHỦ Ý, badge tách được: засыпать = заснуть = «ngủ thiếp đi, chìm vào giấc ngủ» "
        "(theo chốt của luồng chính) — chỉ AspectBadge (CHT/HT) tách. Nếu user thấy chưa đủ thì đây là chỗ cần nhìn.",
        "Chỗ KHÔNG chắc (đã gắn ⚠️ Mức tin hoặc nói rào): кекс ← tiếng Anh số nhiều «cakes»; посу́да ↔ сосу́д "
        "(-суд- vật đựng); лапша́ gốc Turk; про́бка gốc Hà Lan/Đức; салфе́тка họ hàng với serviette.",
        "Họ hàng cố ý vắng 6 thẻ (từ mượn đứng một mình): салфетка, лапша, бекон, кекс, пробка, оркестр.",
    ],
}
