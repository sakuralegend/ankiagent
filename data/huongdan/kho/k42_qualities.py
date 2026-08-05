# -*- coding: utf-8 -*-
"""k42 — qualities: 9 TÍNH TỪ phẩm chất + 9 TRẠNG TỪ đuôi -о.

Trục thật của lô (chốt sau khi đọc `tiep`, không đoán theo nhãn topic):

· Nửa TÍNH TỪ: cả 9 từ đều có khối BAT THUONG, và bất thường ấy chỉ nằm ở
  DẠNG NGẮN — giống cái đẩy trọng âm ra đuôi (стара́ · сильна́ · добра́ ·
  хитра́ · быстра́ · чиста́). Nói trọn khuôn đó ở đúng MỘT thẻ (старый), các
  thẻ sau chỉ nhắc phần riêng của mình (chèn е/ё, biến âm ст→щ).

· Nửa TRẠNG TỪ: chỗ đáng học nhất KHÔNG phải "bỏ -ый thêm -о" mà là TRỌNG ÂM
  có đứng yên hay không. Ba từ nhảy (дешёвый→дёшево lùi về đầu · лёгкий→легко́
  và высо́кий→высоко́ đẩy ra cuối), ba từ đứng yên (ни́зко · гро́мко · я́рко).
  Vì ё luôn được nhấn nên chữ ё phải chạy theo trọng âm — đó là lời giải
  thích chung cho cả дёшево lẫn легко́.

KHÔNG dựng khối dùng chung (README §3): mỗi câu trên đây được viết bằng lời
nói về CHÍNH từ đang đứng, không bê nguyên bảng sang thẻ khác.
"""

S = {}

# ------------------------------------------------------------ TÍNH TỪ

S["прекрасный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пре-</span>'
    '<span class="hd-gloss">VƯỢT MỨC, quá mức thường</span></div>'
    '<div class="hd-row"><span class="hd-piece">-крас-</span>'
    '<span class="hd-gloss">ĐẸP</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ghép thẳng ba mảnh: "đẹp vượt mức" ⇒ tuyệt vời. Gốc '
    '<b>крас-</b> vốn nghĩa là ĐẸP chứ không phải "đỏ" — vì thế '
    '<i>Красная площадь</i> ban đầu là "quảng trường ĐẸP", còn nghĩa "đỏ" của '
    '<b>кра́сный</b> chỉ đến sau.</div>'
    '<div class="hd-warn">Dạng ngắn giống đực chèn thêm <b>е</b> cho đọc được: '
    '<b>прекра́сен</b>. Ba dạng còn lại chỉ cắt đuôi, trọng âm nằm yên ở '
    '<b>-кра́с-</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>краси́вый</b> đẹp · <b>кра́ска</b> sơn, màu vẽ · '
    '<b>кра́сный</b> đỏ · <b>прекра́сно</b> tuyệt, quá tốt.</div>'
)

S["аналогичный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ана-</span>'
    '<span class="hd-gloss">THEO, tương ứng (Hy Lạp <i>aná</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лог-</span>'
    '<span class="hd-gloss">LỜI, lẽ, tỉ lệ (<i>lógos</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́чн-ый</span>'
    '<span class="hd-gloss">đuôi tính từ mượn, ứng với <i>-ic</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng chữ <i>analogous</i>: Hy Lạp <i>analogía</i> là '
    '"cùng một tỉ lệ" — hai thứ đặt cạnh nhau mà theo cùng tỉ lệ thì giống nhau. '
    'Đuôi <b>-и́чный</b> thường kéo trọng âm về chính chữ <b>и́</b> '
    '(<b>симпати́чный</b>, <b>энерги́чный</b>), tuy vẫn có từ lệch ra ngoài '
    'khuôn như <b>ти́пичный</b>.</div>'
    '<div class="hd-warn">Dạng ngắn giống đực chèn thêm <b>е</b>: '
    '<b>аналоги́чен</b>; ba dạng kia chỉ cắt đuôi. Trọng âm ở nguyên chỗ cũ '
    'trong cả bảng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ана́лог</b> vật tương đương · <b>анало́гия</b> sự '
    'tương tự · <b>ло́гика</b> logic · <b>логи́ческий</b> thuộc logic.</div>'
)

S["национальный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">национ-</span>'
    '<span class="hd-gloss">DÂN TỘC — thân Latin đầy đủ <i>nation-</i>, còn '
    '<b>на́ция</b> là dạng rút</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́льн-ый</span>'
    '<span class="hd-gloss">đuôi tính từ quốc tế, ứng với <i>-al</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>на́ция</b> ← Latin <i>natio</i> "nòi giống, sự sinh '
    'ra" (cùng nhà với <i>native</i>). Đuôi <b>-а́льный</b> kéo trọng âm về '
    'chính nó, nên danh từ nhấn đầu <b>на́ция</b> mà tính từ nhấn giữa '
    '<b>национа́льный</b>.</div>'
    '<div class="hd-warn">Nghĩa lõi là DÂN TỘC, không phải nhà nước: '
    '<i>национальная кухня</i> = món ăn dân tộc. "Thuộc nhà nước" là '
    '<b>госуда́рственный</b>, và "quốc tịch" là <b>гражда́нство</b> — ba thứ '
    'khác nhau, tiếng Việt hay gộp làm một.</div>'
    '<div class="hd-warn">Dạng ngắn giống đực thay <b>ь</b> bằng <b>е</b>: '
    '<b>национа́лен</b>; ba dạng còn lại cắt đuôi là xong, trọng âm không nhúc '
    'nhích.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>на́ция</b> dân tộc · <b>национа́льность</b> dân tộc, '
    'tộc người · <b>интернациона́льный</b> quốc tế.</div>'
)

S["сильный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сил-</span>'
    '<span class="hd-gloss">SỨC MẠNH (từ <b>си́ла</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ьн-ый</span>'
    '<span class="hd-gloss">hậu tố "có, đầy"</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Suy thẳng từ hai mảnh: "có sức" ⇒ mạnh. Cùng gốc '
    '<b>сил-</b> còn cho <b>уси́лие</b> (dồn sức = sự cố gắng) và '
    '<b>наси́лие</b> (dùng sức lên người khác = bạo lực).</div>'
    '<div class="hd-warn">Tiếng Nga dùng "MẠNH" ở đúng chỗ tiếng Việt nói "to": '
    '<i>сильный дождь</i> = mưa to, <i>сильный ветер</i> = gió lớn.</div>'
    '<div class="hd-warn">Dạng ngắn lệch cả chữ lẫn trọng âm: giống đực '
    '<b>силён</b> (<b>ь</b> thành <b>ё</b> và trọng âm chạy ra cuối), giống cái '
    '<b>сильна́</b>; hai dạng còn lại giữ trọng âm ở gốc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>си́ла</b> sức mạnh · <b>уси́лие</b> sự cố gắng · '
    '<b>наси́лие</b> bạo lực · <b>си́льно</b> mạnh, dữ (trạng từ).</div>'
)

S["старый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">стар-</span>'
    '<span class="hd-gloss">GIÀ, CŨ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc Slav trơn, không chẻ nhỏ hơn được, và một gốc gánh '
    'cả hai nghĩa tiếng Việt tách đôi: <i>старый дом</i> = nhà CŨ, '
    '<i>старый человек</i> = người GIÀ.</div>'
    '<div class="hd-warn">Dạng ngắn giống cái đẩy trọng âm ra đuôi: '
    '<b>стара́</b>. Đây là kiểu nhảy hay gặp nhất ở tính từ ngắn — riêng lô này '
    'đã có thêm <b>сильна́</b>, <b>добра́</b>, <b>хитра́</b>, <b>быстра́</b>, '
    '<b>чиста́</b>. Giống trung và số nhiều thì được nhấn cả hai kiểu '
    '(<b>ста́ро</b> hoặc <b>старо́</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ста́рость</b> tuổi già · <b>стари́к</b> ông lão · '
    '<b>старе́ть</b> già đi · <b>старомо́дный</b> lỗi mốt.</div>'
)

S["добрый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">добр-</span>'
    '<span class="hd-gloss">TỐT LÀNH, thiện</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>добр-</b> nói về TẤM LÒNG, không nói về chất '
    'lượng: <b>до́брый</b> là tốt bụng, nhân hậu; còn "tốt" theo nghĩa hay, '
    'giỏi, được việc thì là <b>хоро́ший</b>. Danh từ cùng gốc <b>добро́</b> = '
    'điều thiện.</div>'
    '<div class="hd-warn">Bốn cụm phải thuộc, dùng hằng ngày: '
    '<b>до́брое у́тро</b> · <b>до́брый день</b> · <b>до́брый ве́чер</b> · '
    '<b>Всего́ до́брого!</b> (chúc mọi điều tốt lành — câu chia tay).</div>'
    '<div class="hd-warn">Dạng ngắn giống trung là <b>до́бро</b> nhấn ĐẦU; '
    'nhấn cuối <b>добро́</b> lại là DANH TỪ "điều thiện". Giống cái đẩy trọng '
    'âm ra đuôi như thường: <b>добра́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>добро́</b> điều thiện · <b>доброта́</b> lòng tốt · '
    '<b>доброжела́тельный</b> có thiện ý.</div>'
)

S["хитрый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">хитр-</span>'
    '<span class="hd-gloss">MƯU MẸO, khôn vặt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc trơn, cùng nhà với <b>хи́трость</b> (mưu mẹo) và '
    '<b>хитри́ть</b> (giở trò). Sắc thái là khôn có kèm lươn lẹo — nhẹ thì láu '
    'cá, nặng thì xảo quyệt; còn khôn ngoan sáng suốt thuần khen là '
    '<b>у́мный</b>.</div>'
    '<div class="hd-warn">Dạng ngắn giống đực chèn thêm <b>ё</b> vào giữa: '
    '<b>хитёр</b> — và trọng âm rơi ngay vào chữ đó, vì <b>ё</b> trong tiếng '
    'Nga hầu như luôn được nhấn. Giống cái vẫn <b>хитра́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>хи́трость</b> mưu mẹo, mánh khoé · <b>хитри́ть</b> '
    'giở trò khôn vặt.</div>'
)

S["быстрый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">быстр-</span>'
    '<span class="hd-gloss">NHANH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc Slav trơn, không chẻ nhỏ hơn được. Trạng từ tương '
    'ứng là <b>бы́стро</b> (nhanh) — ở riêng từ này trọng âm đứng yên khi đổi '
    'đuôi, nên đọc y như nhau, chỉ khác chữ cuối.</div>'
    '<div class="hd-warn">Dạng ngắn giống đực dồn ba phụ âm liền: <b>быстр</b>. '
    'Giống cái đẩy trọng âm ra đuôi <b>быстра́</b>, còn <b>бы́стро</b> và '
    '<b>бы́стры</b> giữ ở gốc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бы́стро</b> nhanh (trạng từ) · <b>быстрота́</b> tốc '
    'độ, sự nhanh nhẹn.</div>'
)

S["чистый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">чист-</span>'
    '<span class="hd-gloss">SẠCH, thuần, không lẫn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một gốc đi hai chặng: "sạch" (<i>чистая вода</i> nước '
    'sạch) rồi "không pha lẫn gì" (<i>чистая правда</i> = sự thật thuần, đúng '
    'y). Động từ cùng gốc là <b>чи́стить</b> — lau, cọ, gọt vỏ.</div>'
    '<div class="hd-warn">So sánh hơn KHÔNG dùng đuôi <b>-ее</b> mà biến âm '
    '<b>ст → щ</b>: sạch hơn là <b>чи́ще</b>. Dạng ngắn thì theo khuôn quen — '
    'giống cái đẩy trọng âm ra đuôi, <b>чиста́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>чистота́</b> sự sạch sẽ · <b>чи́стить</b> lau chùi, '
    'gọt · <b>чи́сто</b> sạch (trạng từ).</div>'
)

# ------------------------------------------------------------ TRẠNG TỪ

S["дёшево"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дёшев-</span>'
    '<span class="hd-gloss">RẺ (gốc của <b>дешёвый</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tính từ <b>дешёвый</b> đổi đuôi thành <b>-о</b>, nhưng '
    'trọng âm lùi hẳn về âm đầu. Vì chữ <b>ё</b> trong tiếng Nga hầu như luôn '
    'được nhấn, nên nó phải CHẠY THEO trọng âm: <b>дешёвый</b> → '
    '<b>дёшево</b>.</div>'
    '<div class="hd-warn">Cặp câu hỏi giá cả, luôn đi với <b>сто́ить</b>: '
    '<i>Сколько это стоит?</i> — <i>Дёшево</i> (rẻ) hoặc <i>Дорого</i> '
    '(đắt).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дешёвый</b> rẻ (tính từ) · <b>дешеви́зна</b> sự rẻ, '
    'giá thấp · <b>подешеве́ть</b> rẻ đi, xuống giá.</div>'
)

S["много"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мног-</span>'
    '<span class="hd-gloss">NHIỀU</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>мног-</b> cùng nhánh Ấn–Âu với <i>many</i> '
    'tiếng Anh, nên chỉ cần nhớ một lần. Nó dựng ra cả <b>мно́жество</b> (số '
    'lượng lớn) lẫn <b>умножа́ть</b> (nhân, trong toán).</div>'
    '<div class="hd-warn">Danh từ đứng sau <b>мно́го</b> luôn ở CÁCH 2: đếm '
    'được thì số nhiều (<i>много книг</i> nhiều sách), không đếm được thì số ít '
    '(<i>много воды</i> nhiều nước). Cùng luật ấy cho <b>ма́ло</b>, '
    '<b>ско́лько</b>, <b>не́сколько</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мно́гие</b> nhiều (người, vật) · <b>мно́жество</b> '
    'số lượng lớn · <b>умножа́ть</b> nhân lên.</div>'
)

S["дорого"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дорог-</span>'
    '<span class="hd-gloss">ĐẮT; QUÝ, thân thương</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tính từ <b>дорого́й</b> nhấn ở đuôi, còn trạng từ lùi '
    'trọng âm về âm đầu — <b>до́рого</b>. Cùng kiểu lùi ấy với <b>дёшево</b>, '
    'nên hai từ trái nghĩa lại đọc theo cùng một nhịp.</div>'
    '<div class="hd-warn">Gốc này có hai nhánh nghĩa rời hẳn nhau: giá cả và '
    'tình cảm. Tính từ giữ cả hai (<i>Дорогой друг!</i> = Bạn thân mến!), còn '
    'trạng từ <b>до́рого</b> chỉ nói về GIÁ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дорого́й</b> đắt; thân mến · <b>дорожа́ть</b> lên '
    'giá · <b>дорогови́зна</b> sự đắt đỏ.</div>'
)

S["легко"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">лег-</span>'
    '<span class="hd-gloss">NHẸ (gốc của <b>лёгкий</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-о́</span>'
    '<span class="hd-gloss">hậu tố + đuôi trạng từ, mang trọng âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhẹ về sức ⇒ dễ về việc: cái gì tốn ít sức thì '
    '<b>легко́</b>. Trọng âm đẩy hẳn ra đuôi nên chữ <b>ё</b> của '
    '<b>лёгкий</b> MẤT LUÔN hai chấm, thành <b>е</b> thường — <b>ё</b> chỉ tồn '
    'tại ở chỗ được nhấn.</div>'
    '<div class="hd-warn">Nghĩa lõi là ÍT TỐN CÔNG. Đừng kéo nó sang "một chút" '
    '(đó là <b>немно́го</b>) hay "nhẹ nhàng, khẽ, yên tĩnh" (đó là '
    '<b>ти́хо</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лёгкий</b> nhẹ; dễ · <b>облегчи́ть</b> làm nhẹ bớt · '
    '<b>лёгкие</b> phổi (nghĩa đen: "cái nhẹ").</div>'
)

S["низко"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">низ-</span>'
    '<span class="hd-gloss">PHẦN DƯỚI, đáy (danh từ <b>низ</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-о</span>'
    '<span class="hd-gloss">hậu tố + đuôi trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Suy thẳng từ mảnh đầu: ở phần dưới ⇒ thấp. Cùng gốc '
    '<b>низ-</b> còn cho <b>внизу́</b> (ở phía dưới) và <b>снижа́ть</b> (hạ '
    'xuống, giảm).</div>'
    '<div class="hd-warn">Đổi tính từ sang trạng từ mà trọng âm đứng yên: '
    '<b>ни́зкий</b> → <b>ни́зко</b>. Từ trái nghĩa lại làm ngược — '
    '<b>высо́кий</b> → <b>высоко́</b>, trọng âm chạy hẳn ra đuôi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ни́зкий</b> thấp (tính từ) · <b>внизу́</b> ở phía '
    'dưới · <b>снижа́ть</b> hạ xuống, giảm.</div>'
)

S["громко"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">гром-</span>'
    '<span class="hd-gloss">SẤM (danh từ <b>гром</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-о</span>'
    '<span class="hd-gloss">hậu tố + đuôi trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Sấm là tiếng to nhất trời đất: kêu như sấm ⇒ '
    '<b>гро́мкий</b>, làm việc gì như sấm ⇒ <b>гро́мко</b>. Trọng âm đứng yên ở '
    '<b>гро́-</b> trong cả họ, không phải nhớ thêm gì.</div>'
    '<div class="hd-warn">So sánh hơn biến âm <b>к → ч</b>: <b>гро́мче</b>. Đây '
    'là câu hay dùng nhất của từ này — <i>Говорите громче!</i> = Nói to lên!'
    '</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гром</b> sấm · <b>гро́мкий</b> to, vang (tính từ).'
    '</div>'
)

S["высоко"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">высок-</span>'
    '<span class="hd-gloss">CAO</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́</span>'
    '<span class="hd-gloss">đuôi trạng từ, mang trọng âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tính từ <b>высо́кий</b> nhấn ở giữa, còn trạng từ đẩy '
    'trọng âm hẳn ra đuôi — <b>высоко́</b>, đúng kiểu <b>легко́</b> ở trên. '
    'Danh từ cùng gốc là <b>высота́</b> (chiều cao).</div>'
    '<div class="hd-warn">Cụm phải thuộc, dùng cả nghĩa bóng: '
    '<b>высоко́ цени́ть</b> = đánh giá cao, coi trọng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>высо́кий</b> cao (tính từ) · <b>высота́</b> chiều '
    'cao, độ cao · <b>вы́сший</b> cao nhất, tối cao.</div>'
)

S["ярко"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ярк-</span>'
    '<span class="hd-gloss">CHÓI, gay gắt (gốc của <b>я́ркий</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ này nói về CƯỜNG ĐỘ của màu và ánh sáng: '
    '<i>яркое солнце</i> nắng chói, <i>яркий цвет</i> màu rực. Nghĩa bóng đi '
    'thẳng ra từ đó — nổi bật, gây ấn tượng mạnh: <i>яркий пример</i> = ví dụ '
    'điển hình.</div>'
    '<div class="hd-warn">Ba chữ "sáng" đừng lẫn: <b>я́рко</b> = chói, rực '
    '(cường độ mạnh) · <b>светло́</b> = đủ sáng để nhìn · <b>я́сно</b> = rõ '
    'ràng, dễ hiểu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>я́ркий</b> chói, rực rỡ · <b>я́ркость</b> độ sáng, '
    'sự rực rỡ.</div>'
)

S["горько"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">горьк-</span>'
    '<span class="hd-gloss">ĐẮNG (gốc của <b>го́рький</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>гор-</b> này cùng nhà với <b>горе́ть</b> (cháy) '
    'và <b>го́ре</b> (nỗi đau buồn): cái vị làm rát lưỡi như bị đốt, và nỗi '
    'buồn cũng "đắng". Nên <b>го́рько</b> dùng được cho cả vị lẫn lòng người — '
    '<i>горько плакать</i> = khóc cay đắng.</div>'
    '<div class="hd-warn">Đám cưới Nga: khách hô <b>Го́рько!</b> nghĩa là "đắng '
    'quá!", và cô dâu chú rể phải hôn nhau cho "ngọt lại". Người Nga nào cũng '
    'biết cách dùng này.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>го́рький</b> đắng · <b>го́ре</b> nỗi đau buồn · '
    '<b>горе́ть</b> cháy.</div>'
)


# ---- ĐỀ BÀI tiếng Việt (README §2c): chỉ sửa từ nào đang có nhiều hơn 1 đáp án.
# Không ghi từ loại / giống / thể — mặt đề bài đã in sẵn badge (cả 18 từ đều
# adj hoặc adv, badge tự tách mọi cặp tính từ ↔ trạng từ trong lô).
V = {
    'прекрасный': 'tuyệt vời, tuyệt đẹp, xuất sắc',
    'национальный': 'thuộc dân tộc, mang bản sắc dân tộc',
    'сильный': 'mạnh, khoẻ, dữ dội, to',
    'добрый': 'tốt bụng, nhân hậu, tử tế',
    'много': 'nhiều, rất nhiều',
    'легко': 'dễ dàng, không tốn công',
    'низко': 'thấp, ở dưới thấp',
    'высоко': 'cao, ở trên cao',
    'громко': 'to tiếng, lớn tiếng',
    'ярко': 'rực rỡ, chói, sáng',
}
