# -*- coding: utf-8 -*-
"""k173 — language::documents (lô trộn): giấy tờ, đi lại, khoảng cách, đại từ bất định.

Chỗ cần nhất quán trong lô:
(1) отпра́виться / отправля́ться: khuôn thẻ отпра́вить / отправля́ть [k164] — от- RỜI ĐI,
    -прав- HƯỚNG; thêm -ся = tự mình đi.
(2) согла́сно / соглаше́ние: со- CÙNG + -глас-/-глаш- TIẾNG NÓI (dạng cổ của го́лос), khớp
    согласи́ться / соглаша́ться [k124] «biến âm с → ш».
(3) поворо́т: họ QUAY, XOAY của верну́ть [k94] (верт-/ворот-). KHÔNG ghép với воро́та (họ đóng/mở).
(4) расстоя́ние: стоя- ĐỨNG như стоя́нка [k50]. полёт: лет- BAY như полете́ть [k107].
(5) по́дпись: под- DƯỚI + -пис- VIẾT như подписа́ть [k135]. страхо́вка: gốc страх [k153].
(6) кое-кто́ / ка́к-нибудь: khuôn thẻ кое-что́ [k154] và кто́-нибудь [k112].
(7) смех: gốc CƯỜI của смея́ться [k99] (chuyển vào lô chỉ để cân cỡ).
Họ hàng cố ý vắng: không có (mọi từ trong lô đều có họ thật).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "поворот": "chỗ rẽ, khúc quanh, bước ngoặt",       # gloss: turning point / turn (of events)
    "как-нибудь": "bằng cách nào đó, dịp nào đó",      # bỏ dấu chấm phẩy
    "акт": "biên bản, văn bản, hành vi",               # bỏ dấu chấm phẩy
}

# --------------------------------------------------------------------- расстояние
S["расстояние"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рас-</span>'
    '<span class="hd-gloss">TÁCH RA, mỗi bên một ngả</span></div>'
    '<div class="hd-row"><span class="hd-piece">-стоя́-</span>'
    '<span class="hd-gloss">ĐỨNG (<b>стоя́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ние</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hai thứ ĐỨNG TÁCH xa nhau ⇒ khoảng cách. Tiếng Anh dựng y hệt: '
    '<i>dis-tance</i> = Latin <i>dis-</i> «tách ra» + <i>stare</i> «đứng».</div>'
    '<div class="hd-warn"><b>на расстоя́нии</b> + cách 2: <b>на расстоя́нии двух ме́тров</b> '
    'cách xa hai mét.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>стоя́ть</b> đứng · <b>стоя́нка</b> bãi đỗ · <b>расста́ться</b> chia '
    'tay (đứng tách ra) — cùng nhánh gốc сто-/ста- «đứng»</div>'
)

# --------------------------------------------------------------------- поворот
S["поворот"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố thể của <b>поверну́ть</b>, không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ворот-</span>'
    '<span class="hd-gloss">QUAY, XOAY — biến thể của <b>верт-</b> (<b>верте́ть</b>, '
    '<b>верну́ть</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỗ đường QUAY hướng ⇒ chỗ rẽ, khúc quanh; chỗ sự việc quay hướng ⇒ '
    'bước ngoặt. Động từ «rẽ»: <b>поверну́ть</b> (HT) ↔ <b>повора́чивать</b> (CHT) — '
    'е/о chạy qua lại trong cùng gốc.</div>'
    '<div class="hd-warn"><b>указа́тель поворо́та</b> = đèn xi nhan (cái báo rẽ).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поверну́ть</b> rẽ, quay · <b>верну́ть</b> trả lại · '
    '<b>верте́ть</b> xoay · <b>разворо́т</b> sự quay đầu xe</div>'
)

# --------------------------------------------------------------------- сверху
S["сверху"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">TỪ (chỗ nào) xuống — như giới từ <b>с</b> + cách 2</span></div>'
    '<div class="hd-row"><span class="hd-piece">-верх-</span>'
    '<span class="hd-gloss"><b>верх</b> ĐỈNH, phần trên</span></div>'
    '<div class="hd-row"><span class="hd-piece">-у</span>'
    '<span class="hd-gloss">đuôi cách 2 cũ, đóng băng thành trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Từ phía đỉnh» ⇒ từ trên xuống, và cả «ở mặt trên»: <b>Све́рху лежи́т '
    'кни́га</b>. Cặp đối: <b>сни́зу</b> từ dưới lên — cùng khuôn <b>с-</b> + <b>-у</b>.</div>'
    '<div class="hd-warn"><b>све́рху до́низу</b> = từ trên xuống dưới, từ đầu đến cuối.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>верх</b> phần trên · <b>ве́рхний</b> ở trên · <b>наверху́</b> ở '
    'trên · <b>вверх</b> lên trên</div>'
)

# --------------------------------------------------------------------- отправиться
S["отправиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">RỜI ĐI, tách khỏi mình</span></div>'
    '<div class="hd-row"><span class="hd-piece">-прав-</span>'
    '<span class="hd-gloss">HƯỚNG, điều khiển — gốc của <b>пра́вить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-ть-ся</span>'
    '<span class="hd-gloss">đuôi lớp chia 2 + TỰ mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>отпра́вить</b> là hướng một vật rời đi (gửi); thêm <b>-ся</b> là hướng '
    'CHÍNH MÌNH rời đi ⇒ lên đường. Đi đâu: <b>в</b>/<b>на</b> + cách 4. Ngôi «tôi» chêm '
    '<b>л</b> như <b>отпра́вить</b>: <b>я отпра́влюсь</b>, rồi <b>ты отпра́вишься</b>.</div>'
    '<div class="hd-warn"><b>отпра́виться в путь</b> = lên đường.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отпра́вить</b> gửi đi · <b>отправля́ться</b> lên đường (CHT) · '
    '<b>отправле́ние</b> sự khởi hành · <b>напра́виться</b> đi về phía</div>'
)

# --------------------------------------------------------------------- отправляться
S["отправляться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-прав-</span>'
    '<span class="hd-gloss">RỜI ĐI + HƯỚNG — như <b>отпра́виться</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-л-я́ть-ся</span>'
    '<span class="hd-gloss"><b>л</b> mượn từ <b>отпра́влюсь</b> + đuôi CHT + TỰ mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>отпра́виться</b>, chia đều: <b>отправля́юсь, '
    'отправля́ешься</b>. Dùng cho thói quen và LỊCH CHẠY tàu xe — hiện tại nói được cả giờ sắp '
    'tới: <b>Авто́бус отправля́ется в семь</b>.</div>'
    '<div class="hd-warn">Đã đi một lần, xong ⇒ <b>отпра́вился</b> (HT); lặp lại, đang đi, '
    'theo lịch ⇒ <b>отправля́лся</b> (CHT).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отправля́ть</b> gửi đi (CHT) · <b>отпра́виться</b> lên đường (HT) · '
    '<b>отправле́ние</b> sự khởi hành</div>'
)

# --------------------------------------------------------------------- ракета
S["ракета"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn (qua tiếng Đức <i>Rakete</i>, gốc Ý <i>rocchetta</i>), không chẻ '
    'được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc tiếng Anh <i>rocket</i> — nghĩa trùng khít. Khác ở trọng âm: '
    'tiếng Nga nhấn giữa, <b>раке́та</b>. Đuôi <b>-а</b> ⇒ giống cái.</div>'
    '<div class="hd-warn"><b>раке́тка</b> là cái VỢT (tennis, cầu lông) — khác gốc (Pháp '
    '<i>raquette</i>), chỉ trùng mặt chữ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>раке́тный</b> (thuộc) tên lửa</div>'
)

# --------------------------------------------------------------------- полёт
S["полёт"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố như trong <b>полете́ть</b>, không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лёт</span>'
    '<span class="hd-gloss">BAY (<b>лете́ть</b>) — е thành <b>ё</b> khi mang trọng âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>полете́ть</b>: sự bay, một chuyến bay. Cùng mảnh '
    '<b>-лёт</b> với <b>самолёт</b> (tự bay) và <b>вертолёт</b> (xoay + bay).</div>'
    '<div class="hd-warn"><b>Прия́тного полёта!</b> = Chúc chuyến bay vui vẻ! (lời chúc đòi '
    'cách 2).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лете́ть</b> đang bay · <b>полете́ть</b> bay đi · <b>самолёт</b> máy '
    'bay · <b>вертолёт</b> trực thăng · <b>лётчик</b> phi công</div>'
)

# --------------------------------------------------------------------- из-под
S["из-под"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">из</span>'
    '<span class="hd-gloss">TỪ TRONG ra</span></div>'
    '<div class="hd-row"><span class="hd-piece">под</span>'
    '<span class="hd-gloss">DƯỚI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng khuôn <b>из-за</b>: «từ bên dưới ra», kéo cách 2 — '
    '<b>Кот вы́лез из-под крова́ти</b> con mèo chui ra từ gầm giường. <b>под</b> nói chỗ ở dưới, '
    '<b>из-под</b> nói hướng rời khỏi chỗ đó.</div>'
    '<div class="hd-warn"><b>ба́нка из-под варе́нья</b> = cái lọ VỐN ĐỰNG mứt (giờ đã rỗng), '
    'không phải «lọ dưới mứt».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>из</b> từ trong ra · <b>под</b> dưới · <b>из-за</b> từ phía sau ra '
    '(cùng khuôn)</div>'
)

# --------------------------------------------------------------------- согласно
S["согласно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">CÙNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-глас-</span>'
    '<span class="hd-gloss">TIẾNG NÓI — dạng cổ của <b>го́лос</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-о</span>'
    '<span class="hd-gloss">tính từ <b>согла́сный</b> → trạng từ <b>-о</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cùng một tiếng nói VỚI cái gì» ⇒ khớp với, theo đúng. Giọng giấy tờ, '
    'văn bản: <b>согла́сно зако́ну</b> theo luật, <b>согла́сно пла́ну</b> theo kế hoạch.</div>'
    '<div class="hd-warn"><b>согла́сно</b> + CÁCH 3: <b>согла́сно пра́вилам</b>. Viết cách 2 '
    '(<i>согласно закона</i>) là lỗi — người Nga cũng hay mắc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>согла́сный</b> đồng ý · <b>согласи́ться</b> đồng ý (HT) · '
    '<b>соглаше́ние</b> thoả thuận · <b>го́лос</b> giọng</div>'
)

# --------------------------------------------------------------------- кое-кто
S["кое-кто"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кое-</span>'
    '<span class="hd-gloss">người nói BIẾT là ai, chỉ chưa nói ra</span></div>'
    '<div class="hd-row"><span class="hd-piece">кто</span>'
    '<span class="hd-gloss">AI (từ hỏi)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>Кое-кто́ опя́ть опозда́л</b> = Có người lại đến muộn (tôi biết là ai, '
    'không nêu tên). Còn <b>кто́-то</b> là chính người nói cũng không biết ai. Chỉ phần '
    '<b>кто</b> biến cách: <b>кое-кого́</b>, <b>кое-кому́</b>.</div>'
    '<div class="hd-warn">Có giới từ thì nó chen vào GIỮA, gạch nối biến mất: кое '
    '<b>у кого́</b>, кое <b>с кем</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кто</b> ai · <b>кто́-то</b> ai đó · <b>кое-что́</b> một thứ · '
    '<b>кое-где́</b> đây đó · <b>кое-ка́к</b> qua loa</div>'
)

# --------------------------------------------------------------------- как-нибудь
S["как-нибудь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">как</span>'
    '<span class="hd-gloss">thế nào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-нибудь</span>'
    '<span class="hd-gloss">«… nào cũng được» — chưa xác định</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cách nào cũng được» ⇒ bằng cách nào đó: <b>Ка́к-нибудь спра́вимся</b> '
    'rồi cũng xoay xở được. Dời sang thời gian ⇒ dịp nào đó SẮP TỚI: <b>Заходи́ ка́к-нибудь!</b> '
    'hôm nào ghé chơi nhé!</div>'
    '<div class="hd-warn">Hôm nào đó SẼ… ⇒ <b>ка́к-нибудь</b>; hôm nọ ĐÃ… ⇒ <b>ка́к-то</b> '
    '(<b>ка́к-то раз</b> có một lần).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>как</b> thế nào · <b>ка́к-то</b> bằng cách nào đó · '
    '<b>кто́-нибудь</b> bất kỳ ai · <b>когда́-нибудь</b> một ngày nào đó</div>'
)

# --------------------------------------------------------------------- сквозь
S["сквозь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: giới từ nguyên khối, gốc Slav cổ.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đòi cách 4 như <b>че́рез</b>, nhưng hình ảnh khác: <b>сквозь</b> là đi '
    'XUYÊN BÊN TRONG một lớp cản — <b>сквозь толпу́</b> chen qua đám đông, <b>сквозь тума́н</b> '
    'qua làn sương. <b>че́рез</b> là vượt ngang, vượt trên: <b>че́рез доро́гу</b>; và chỉ '
    '<b>че́рез</b> mới có nghĩa thời gian.</div>'
    '<div class="hd-warn"><b>сквозь зу́бы</b> = (nói) rít qua kẽ răng — miễn cưỡng, '
    'không muốn nói.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>наскво́зь</b> xuyên suốt, thấu (ướt sũng) · <b>сквозня́к</b> gió lùa · '
    '<b>сквозно́й</b> xuyên qua</div>'
)

# --------------------------------------------------------------------- страховка
S["страховка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">страх-</span>'
    '<span class="hd-gloss">SỢ (<b>страх</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ов-</span>'
    '<span class="hd-gloss">mảnh của <b>страхова́ть</b> bảo hiểm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">→ danh từ giống cái, giọng đời thường</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thứ mua để khỏi phải SỢ rủi ro. Đời thường nói <b>страхо́вка</b>; giấy '
    'tờ, tên ngành nói <b>страхова́ние</b>. Cách 2 số nhiều chèn <b>о</b> vào cụm -вк: '
    '<b>страхо́вок</b>.</div>'
    '<div class="hd-warn"><b>медици́нская страхо́вка</b> = bảo hiểm y tế.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>страх</b> nỗi sợ · <b>страхова́ть</b> bảo hiểm · '
    '<b>страхова́ние</b> ngành bảo hiểm · <b>стра́шный</b> đáng sợ</div>'
)

# --------------------------------------------------------------------- пресса
S["пресса"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn (Pháp <i>presse</i>), không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng như tiếng Anh <i>the press</i>: máy ÉP chữ in ra báo ⇒ báo chí nói '
    'chung. Danh từ tập hợp, chỉ dùng số ít: <b>в пре́ссе</b> trên báo chí. Đuôi <b>-а</b> ⇒ '
    'giống cái.</div>'
    '<div class="hd-warn">Bỏ <b>-а</b> là thành từ khác: <b>пресс</b> (giống đực) = máy ép — và '
    'cơ bụng: <b>кача́ть пресс</b> tập cơ bụng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пресс-конфере́нция</b> họp báo · <b>пресс</b> máy ép · '
    '<b>прессова́ть</b> ép, nén</div>'
)

# --------------------------------------------------------------------- соглашение
S["соглашение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">CÙNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-глаш-</span>'
    '<span class="hd-gloss">= <b>-глас-</b> TIẾNG NÓI, biến âm с → ш</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>соглаша́ться</b>: các bên CÙNG một tiếng nói ⇒ thoả thuận, '
    'hiệp định (thường thành văn bản). Còn <b>согла́сие</b> chỉ là sự đồng ý — thái độ, '
    'không phải bản ký kết.</div>'
    '<div class="hd-warn"><b>прийти́ к соглаше́нию</b> = đạt được thoả thuận · '
    '<b>заключи́ть соглаше́ние</b> = ký kết thoả thuận.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>соглаша́ться</b> đồng ý (CHT) · <b>согласи́ться</b> đồng ý (HT) · '
    '<b>согла́сие</b> sự đồng ý · <b>согла́сно</b> theo</div>'
)

# --------------------------------------------------------------------- акт
S["акт"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn Latin <i>actus</i> «việc đã làm», không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc tiếng Anh <i>act</i>: một hành vi (<b>акт наси́лия</b> hành vi bạo '
    'lực) — và văn bản ghi lại việc đã làm ⇒ biên bản. Nghĩa «biên bản» là chỗ phải '
    'nhớ riêng.</div>'
    '<div class="hd-warn"><b>соста́вить акт</b> = lập biên bản (sau va chạm, hư hỏng, bàn giao).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>актёр</b> diễn viên · <b>акти́вный</b> tích cực · <b>а́кция</b> '
    'cổ phiếu, chiến dịch</div>'
)

# --------------------------------------------------------------------- подпись
S["подпись"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span>'
    '<span class="hd-gloss">DƯỚI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пис-</span>'
    '<span class="hd-gloss">gốc VIẾT — <b>писа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ь</span>'
    '<span class="hd-gloss">đuôi danh từ, ở đây là giống CÁI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thứ VIẾT ở DƯỚI văn bản ⇒ chữ ký — danh từ của <b>подписа́ть</b>. '
    'Trọng âm về đầu: <b>по́дпись</b>.</div>'
    '<div class="hd-warn">Mọi danh từ đuôi <b>-пись</b> đều giống CÁI: <b>моя́ по́дпись</b>. '
    '«Ký vào» = <b>поста́вить по́дпись</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>подписа́ть</b> ký · <b>подпи́сывать</b> ký (CHT) · <b>за́пись</b> bản '
    'ghi · <b>на́дпись</b> dòng chữ ghi trên vật · <b>писа́ть</b> viết</div>'
)

# --------------------------------------------------------------------- смех
S["смех"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được — nhưng là gốc CƯỜI của cả họ '
    '<b>смея́ться</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>смея́ться</b>; chỉ dùng số ít. Có dạng cũ <b>сме́ху</b> '
    'sống trong cụm: <b>умира́ть со сме́ху</b> cười muốn chết.</div>'
    '<div class="hd-warn"><b>смех сквозь слёзы</b> = cười trong nước mắt.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>смея́ться</b> cười · <b>засмея́ться</b> bật cười · '
    '<b>смешно́й</b> buồn cười · <b>насме́шка</b> lời chế giễu</div>'
)

B = {
    "docbangmat": 81,
    "loitubat": 2,
    "nguonsai": 0,
    "baolen": [
        "VA CHẠM KHÔNG GỠ ĐƯỢC: сквозь «xuyên qua» vẫn nằm gọn trong че́рез «qua, xuyên qua, băng qua, sau» [k66 đã nạp] (cùng prep). Gloss сквозь chỉ có «through» nên không có nghĩa nào để thêm mà gloss xác nhận. Lối duy nhất thấy được: thêm «lọt qua» (có trong từ điển Nga–Việt: ánh sáng lọt qua khe — свет сквозь щель) — nhưng đó là từ đồng nghĩa tiếng Việt, gloss Anh không tách. Tôi để nguyên, chờ luồng chính/user chọn.",
        "V cần duyệt: поворот thêm «bước ngoặt» (gloss: turning point / turn (of events)); как-нибудь và акт chỉ đổi dấu chấm phẩy thành dấu phẩy, giữ nguyên nghĩa. Mô phỏng do_va_cham chỉ đọc trên toàn bộ thẻ với V mới: va chạm dính lô k173 chỉ còn сквозь↔через.",
        "Không chắc lắm: ракета ghi «qua tiếng Đức Rakete, gốc Ý rocchetta» (Vasmer ghi Đức hoặc Hà Lan); поворот chẻ -ворот- = biến thể của верт- (theo chỉ dẫn luồng chính, khớp thẻ верну́ть) — từ nguyên phổ biến, không phải luật suy ra.",
        "loitubat=2 là: (1) thẻ акт từng ghi «nghĩa biên bản tiếng Anh không có» — sai, act tiếng Anh cũng có nghĩa văn bản pháp lý, đã bỏ; (2) thẻ полёт từng gán по- nghĩa «cất cánh bay đi» — không có căn cứ, đã sửa thành «không mang nghĩa riêng». Lỗi máy bắt (thiếu dấu наси́лия, chữ k Latin trong кое) không tính.",
    ],
}
