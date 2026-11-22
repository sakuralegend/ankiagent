# -*- coding: utf-8 -*-
"""k178 — concepts::state: nhu cầu, khả năng, nhà nước, chính trị, hiểu biết.

Chỗ cần nhất quán trong lô:
(1) gốc треб- = CẦN — khớp thẻ тре́бовать [k124] («gốc CẦN»). потре́бность, тре́боваться,
    потре́боваться dùng đúng chữ đó. Cấu trúc «ai cần → cách 3» dạy ĐẦY ĐỦ ở тре́боваться,
    потре́боваться chỉ trỏ sang.
(2) gốc вер- = TIN — khớp ве́рить [k99], наве́рное [k101]. вероя́тно ↔ наве́рное tách ở ô đỏ
    của вероя́тно; вероя́тность chỉ trỏ cụm по всей вероя́тности.
(3) -глас- = dạng cổ của го́лос — согла́сие chẻ y khuôn thẻ согла́сный [k88].
(4) -ним-/-ня- NẮM LẤY — понима́ние khớp понима́ть [k54], поня́ть [k60].
(5) о́браз HÌNH ẢNH — воображе́ние khớp образова́ние [k09]; з → ж (вообрази́ть → воображе́ние).
(6) -един- MỘT — объедине́ние khớp еди́ный [k123].
(7) арестова́ть / аресто́вывать: luật «за + cách 4 = lý do» nói ở арестова́ть, cặp kia trỏ sang.
(8) оборо́на: KHÔNG nối với боро́ться (luồng chính đánh dấu là khớp chuỗi oan) — chỉ dạy trong
    họ оборо́н-.
Họ hàng cố ý vắng: không thẻ nào — конфли́кт là từ mượn nhưng có phái sinh Nga thật.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "потребность": "nhu cầu, đòi hỏi",                       # RÚT «sự cần thiết» — nằm gọn trong необходи́мость [k161]; need/want/requirement
    "вероятно": "có lẽ, có khả năng",                         # RÚT «chắc là» — наве́рное [k101] «có lẽ, chắc là» nằm gọn trong đề cũ
    "потребоваться": "cần đến, được cần đến, trở nên cần thiết",  # bỏ «sẽ» (dấu thời/thể, badge đã in thể)
    "оборона": "sự phòng thủ, quốc phòng, tuyến phòng thủ",   # defense / defensive position; bỏ «hàng phòng ngự» (gloss không xác nhận nghĩa thể thao)
    "объединение": "sự hợp nhất, sự sáp nhập, sự liên kết, liên hiệp",  # THIẾU «union» (tổ chức)
}

# --------------------------------------------------------------------- потребность
S["потребность"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố — ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-треб-н-</span>'
    '<span class="hd-gloss">CẦN — gốc của <b>тре́бовать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ость</span>'
    '<span class="hd-gloss">→ danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Điều mình CẦN» ⇒ nhu cầu. <b>тре́бовать</b> là đòi người khác; '
    '<b>потре́бность</b> là cái tự bên trong mình cần.</div>'
    '<div class="hd-warn">Cần CÁI GÌ → <b>в</b> + cách 6: <b>потре́бность в сне</b> nhu cầu ngủ, '
    '<b>потре́бность в по́мощи</b> nhu cầu được giúp.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тре́бовать</b> đòi hỏi · <b>тре́бование</b> yêu cầu · '
    '<b>тре́боваться</b> cần · <b>потре́боваться</b> cần đến</div>'
)

# --------------------------------------------------------------------- вероятность
S["вероятность"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вероя́тн-</span>'
    '<span class="hd-gloss">← <b>вероя́тный</b> có khả năng; lõi <b>вер-</b> TIN như <b>ве́рить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ость</span>'
    '<span class="hd-gloss">→ danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Điều đáng TIN là sẽ xảy ra ⇒ khả năng; đem ra đo bằng số ⇒ xác suất: '
    '<b>тео́рия вероя́тностей</b> lý thuyết xác suất.</div>'
    '<div class="hd-warn"><b>по всей вероя́тности</b> — rất có thể, nhiều khả năng là.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вероя́тно</b> có lẽ · <b>вероя́тный</b> có khả năng xảy ra · '
    '<b>ве́рить</b> tin · <b>наве́рное</b> có lẽ</div>'
)

# --------------------------------------------------------------------- вероятно
S["вероятно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вероя́тн-</span>'
    '<span class="hd-gloss">← <b>вероя́тный</b> có khả năng; lõi <b>вер-</b> TIN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">→ trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trạng từ <b>-о</b> của <b>вероя́тный</b>, cùng nhà với <b>вероя́тность</b>. '
    'Đứng giữa câu thì kẹp hai dấu phẩy: <b>Он, вероя́тно, опозда́ет.</b></div>'
    '<div class="hd-warn">Cùng gốc <b>вер-</b>, cùng nghĩa với <b>наве́рное</b>, nhưng '
    '<b>вероя́тно</b> trang trọng hơn — hay gặp trong tin tức, văn viết; nói chuyện hằng ngày '
    'thì <b>наве́рное</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вероя́тность</b> khả năng, xác suất · <b>вероя́тный</b> có khả năng · '
    '<b>наве́рное</b> có lẽ · <b>ве́рить</b> tin</div>'
)

# --------------------------------------------------------------------- требоваться
S["требоваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">треб-</span>'
    '<span class="hd-gloss">CẦN — gốc của <b>тре́бовать</b> đòi hỏi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-</span>'
    '<span class="hd-gloss">lớp <b>-овать</b>: chia thành <b>-у-</b> → <b>тре́буется</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">«được…» — bị đòi, được cần đến</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Được đòi hỏi» ⇒ cần thiết. Câu đảo ngược tiếng Việt: thứ được cần làm '
    'chủ ngữ, người cần đứng ở cách 3.</div>'
    '<div class="hd-warn"><b>Мне тре́буется по́мощь.</b> = Tôi cần giúp đỡ (nghĩa đen: «với tôi, '
    'sự giúp đỡ được cần»). = <b>Мне нужна́ по́мощь</b>, nhưng trang trọng hơn.</div>'
    '<div class="hd-warn">Biển tuyển người: <b>Тре́буется продаве́ц</b> = Cần tuyển người bán hàng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тре́бовать</b> đòi hỏi · <b>потре́боваться</b> cần đến · '
    '<b>потре́бность</b> nhu cầu · <b>тре́бование</b> yêu cầu</div>'
)

# --------------------------------------------------------------------- потребоваться
S["потребоваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố thể — chỉ đóng việc lại, không thêm nghĩa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-треб-ова-ть-ся</span>'
    '<span class="hd-gloss">y hệt <b>тре́боваться</b> — được cần đến</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thể hoàn thành của <b>тре́боваться</b>, nên hay gặp ở tương lai và quá '
    'khứ: <b>Мне потре́буется вре́мя.</b> Tôi sẽ cần thời gian · <b>Потре́бовалось три го́да.</b> '
    'Đã phải mất ba năm.</div>'
    '<div class="hd-why">Người cần đứng ở cách 3 — cấu trúc đầy đủ nằm ở thẻ <b>тре́боваться</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тре́боваться</b> cần · <b>потре́бовать</b> đòi · '
    '<b>потре́бность</b> nhu cầu</div>'
)

# --------------------------------------------------------------------- дума
S["дума"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дум-</span>'
    '<span class="hd-gloss">Ý NGHĨ, sự suy tính — gốc của <b>ду́мать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nơi người ta ngồi lại cùng suy tính việc chung ⇒ hội đồng. Nay gần như '
    'chỉ còn nghĩa cơ quan lập pháp; nghĩa «ý nghĩ» là văn thơ cổ.</div>'
    '<div class="hd-warn"><b>Госуда́рственная ду́ма</b> (gọi tắt <b>Госду́ма</b>) — Duma Quốc gia, '
    'hạ viện của Nga.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ду́мать</b> nghĩ · <b>поду́мать</b> nghĩ một lát · '
    '<b>приду́мать</b> nghĩ ra · <b>заду́маться</b> trầm ngâm</div>'
)

# --------------------------------------------------------------------- оборона
S["оборона"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ thành mảnh dùng được: lõi <b>-оборон-</b> là gốc cổ «che chắn», '
    'nay chỉ còn sống trong chính họ này.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhớ qua cả họ: <b>обороня́ть</b> phòng thủ → <b>оборо́на</b> sự phòng thủ → '
    '<b>оборо́нный</b> thuộc quốc phòng.</div>'
    '<div class="hd-warn"><b>министе́рство оборо́ны</b> — Bộ Quốc phòng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обороня́ть</b> phòng thủ · <b>обороня́ться</b> tự vệ · '
    '<b>оборо́нный</b> thuộc quốc phòng · <b>оборони́тельный</b> mang tính phòng thủ</div>'
)

# --------------------------------------------------------------------- объединение
S["объединение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">объ-</span>'
    '<span class="hd-gloss">об- QUANH, gom lại; <b>ъ</b> giữ <b>е</b> đọc tách «ye»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-един-</span>'
    '<span class="hd-gloss">MỘT — như <b>еди́ный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gom quanh lại thành MỘT ⇒ sự hợp nhất. Cái khối sinh ra sau khi hợp nhất '
    'cũng gọi là <b>объедине́ние</b> — liên hiệp, hiệp hội.</div>'
    '<div class="hd-warn"><b>Организа́ция Объединённых На́ций</b> — Liên Hợp Quốc, viết tắt ООН.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>объедини́ть</b> hợp nhất · <b>еди́ный</b> thống nhất · '
    '<b>еди́нство</b> sự thống nhất · <b>соедини́ть</b> nối lại · <b>оди́н</b> một</div>'
)

# --------------------------------------------------------------------- правовой
S["правовой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">прав-</span>'
    '<span class="hd-gloss">ĐÚNG → LUẬT — như <b>пра́во</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ов-о́й</span>'
    '<span class="hd-gloss">đuôi tính từ, trọng âm nằm ở đuôi</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tính từ của <b>пра́во</b> ở nghĩa «luật»: <b>правова́я систе́ма</b> hệ thống '
    'pháp luật. Đừng lẫn với <b>пра́вильный</b> (đúng) hay <b>пра́вый</b> (bên phải).</div>'
    '<div class="hd-warn"><b>правово́е госуда́рство</b> — nhà nước pháp quyền.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пра́во</b> quyền, luật · <b>пра́вило</b> quy tắc · '
    '<b>пра́вда</b> sự thật · <b>прави́тельство</b> chính phủ</div>'
)

# --------------------------------------------------------------------- партийный
S["партийный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">парти́-</span>'
    '<span class="hd-gloss">← <b>па́ртия</b> đảng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-йн-ый</span>'
    '<span class="hd-gloss">đuôi tính từ; trọng âm nhảy sang <b>-ти́-</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tính từ của <b>па́ртия</b>: <b>парти́йный биле́т</b> thẻ đảng. Dạng ngắn '
    'hiếm, chỉ ở nghĩa «trung thành với đảng»; giống đực mất <b>й</b>, chèn <b>е</b>: '
    '<b>парти́ен</b> (còn lại giữ nguyên: <b>парти́йна</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>па́ртия</b> đảng, lô hàng, ván đấu · <b>партиза́н</b> du kích · '
    '<b>беспарти́йный</b> không đảng phái</div>'
)

# --------------------------------------------------------------------- чиновник
S["чиновник"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">чин-</span>'
    '<span class="hd-gloss">CẤP BẬC, phẩm hàm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ов-</span>'
    '<span class="hd-gloss">đuôi tính từ «thuộc về»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ник</span>'
    '<span class="hd-gloss">NGƯỜI — như <b>рабо́тник</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người có CẤP BẬC trong bộ máy nhà nước ⇒ quan chức. Thời Sa hoàng, mọi '
    'công chức đều mang một <b>чин</b>.</div>'
    '<div class="hd-warn">Sắc thái hay hơi chê: kẻ giấy tờ, quan liêu. Trung tính hơn là '
    '<b>госслу́жащий</b> công chức nhà nước.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>чин</b> cấp bậc, phẩm hàm · <b>чино́вничество</b> giới quan chức</div>'
)

# --------------------------------------------------------------------- политик
S["политик"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">поли́т-</span>'
    '<span class="hd-gloss">gốc Hy Lạp — như <b>поли́тика</b> chính trị</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ик</span>'
    '<span class="hd-gloss">NGƯỜI làm ngành đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một cặp mở cả lớp từ: <b>-ик</b> = người, <b>-ика</b> = ngành. '
    '<b>поли́тик / поли́тика</b> y như <b>фи́зик / фи́зика</b>, <b>матема́тик / матема́тика</b>.</div>'
    '<div class="hd-warn">Chỉ khác nhau một chữ <b>-а</b>: <b>поли́тик</b> là NGƯỜI (giống đực), '
    '<b>поли́тика</b> là NGÀNH (giống cái).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поли́тика</b> chính trị, chính sách · <b>полити́ческий</b> thuộc chính trị</div>'
)

# --------------------------------------------------------------------- заговор
S["заговор"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за́-</span>'
    '<span class="hd-gloss">tiền tố — ở đây không mang nghĩa riêng dễ dịch</span></div>'
    '<div class="hd-row"><span class="hd-piece">-говор</span>'
    '<span class="hd-gloss">NÓI — như <b>говори́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng khuôn với <b>догово́р</b> (thoả thuận): <b>за́говор</b> là lời bàn '
    'bạc ngầm để chống ai ⇒ âm mưu. Chống AI → <b>про́тив</b> + cách 2.</div>'
    '<div class="hd-warn">Trọng âm ở tiền tố: <b>за́говор</b> — khác <b>заговори́ть</b> (bắt đầu '
    'nói). Cụm hay gặp: <b>тео́рия за́говора</b> thuyết âm mưu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>говори́ть</b> nói · <b>разгово́р</b> cuộc trò chuyện · '
    '<b>догово́р</b> hợp đồng · <b>загово́рщик</b> kẻ âm mưu</div>'
)

# --------------------------------------------------------------------- конфликт
S["конфликт"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn, không chẻ trong tiếng Nga — y hệt tiếng Anh <i>conflict</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Xung đột VỚI ai → <b>с</b> + cách 5: <b>конфли́кт с сосе́дями</b>. '
    'Giữa hai bên → <b>ме́жду</b> + cách 5.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>конфли́ктный</b> hay gây mâu thuẫn · <b>конфликтова́ть</b> xung đột, '
    'cãi nhau</div>'
)

# --------------------------------------------------------------------- арестовать
S["арестовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">аре́ст-</span>'
    '<span class="hd-gloss">← <b>аре́ст</b> sự bắt giữ (từ mượn)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-ть</span>'
    '<span class="hd-gloss">lớp <b>-овать</b>: chia thành <b>-у-</b> → <b>аресту́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ + <b>-овать</b> = làm việc đó, như <b>ата́ка → атакова́ть</b>. Bắt AI → '
    'cách 4: <b>арестова́ть престу́пника</b>.</div>'
    '<div class="hd-warn">Bắt VÌ tội gì → <b>за</b> + cách 4: <b>арестова́ть за кра́жу</b> bắt vì '
    'tội trộm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>аре́ст</b> sự bắt giữ · <b>аресто́вывать</b> bắt (chưa hoàn thành) · '
    '<b>аресто́ванный</b> bị bắt</div>'
)

# --------------------------------------------------------------------- арестовывать
S["арестовывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">арест-</span>'
    '<span class="hd-gloss">← <b>аре́ст</b> sự bắt giữ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ов-ыва-ть</span>'
    '<span class="hd-gloss"><b>-ыва-</b> đổi thể hoàn thành → chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chèn <b>-ыва-</b> vào <b>арестова́ть</b> là ra thể chưa hoàn thành, và '
    'trọng âm lùi lên <b>-сто́-</b>: <b>арестова́ть → аресто́вывать</b>. Chia đều: '
    '<b>аресто́вываю</b>. Luật <b>за</b> + cách 4 nằm ở thẻ <b>арестова́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>аре́ст</b> sự bắt giữ · <b>арестова́ть</b> bắt giữ (hoàn thành)</div>'
)

# --------------------------------------------------------------------- понимание
S["понимание"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố — không thêm nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ним-</span>'
    '<span class="hd-gloss">NẮM LẤY — lõi của <b>поня́ть</b>, <b>приня́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ание</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>понима́ть</b>: «nắm được» ý người ta ⇒ sự hiểu — y như tiếng '
    'Anh <i>grasp</i>. Hiểu cả hoàn cảnh của người ta ⇒ sự thông cảm.</div>'
    '<div class="hd-warn"><b>Спаси́бо за понима́ние</b> — Cảm ơn đã thông cảm (câu quen thuộc cuối các '
    'thông báo).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>понима́ть</b> hiểu · <b>поня́ть</b> hiểu ra · <b>поня́тный</b> dễ hiểu · '
    '<b>поня́тие</b> khái niệm · <b>принима́ть</b> nhận</div>'
)

# --------------------------------------------------------------------- воображение
S["воображение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">во-</span>'
    '<span class="hd-gloss">VÀO TRONG — như <b>в</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ображ-</span>'
    '<span class="hd-gloss">HÌNH ẢNH — <b>о́браз</b>, <b>з</b> đổi thành <b>ж</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đưa HÌNH ẢNH vào trong đầu ⇒ tưởng tượng — tiếng Anh cũng thế: '
    '<i>imagination</i> ← <i>image</i>. Động từ <b>вообрази́ть</b> có <b>з</b>, sang danh từ thì '
    '<b>з → ж</b>, như <b>вы́разить → выраже́ние</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вообрази́ть</b> tưởng tượng · <b>о́браз</b> hình ảnh · '
    '<b>изображе́ние</b> hình ảnh, sự miêu tả · <b>образова́ние</b> giáo dục</div>'
)

# --------------------------------------------------------------------- согласие
S["согласие"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">CÙNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-глас-</span>'
    '<span class="hd-gloss">TIẾNG NÓI — dạng cổ của <b>го́лос</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ие</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">CÙNG một tiếng nói ⇒ sự đồng ý; cùng tiếng nói lâu dài ⇒ hoà thuận: '
    '<b>жить в согла́сии</b> sống hoà thuận.</div>'
    '<div class="hd-warn">Đồng ý CHO việc gì → <b>дать согла́сие на</b> + cách 4: '
    '<b>дать согла́сие на брак</b> ưng thuận cuộc hôn nhân.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>согла́сный</b> đồng ý · <b>согласи́ться</b> đồng ý · '
    '<b>соглаше́ние</b> hiệp định · <b>го́лос</b> giọng, phiếu bầu</div>'
)

B = {
    "docbangmat": 72,
    "loitubat": 3,   # требоваться: «= мне ну́жно» sai (phải là мне нужна́ по́мощь) · арестовать: ví dụ
                     # организова́ть KHÔNG phải «danh từ + -овать» -> đổi ата́ка → атакова́ть · понимание:
                     # «câu cuối của mọi thông báo» nói quá -> hạ xuống «câu quen thuộc»
    "nguonsai": 2,   # оборона: bỏ «hàng phòng ngự» (gloss không xác nhận nghĩa thể thao) ·
                     # потребность: «sự cần thiết» là nghĩa nới rộng (gloss need/requirement)
    "baolen": [
        "Va chạm nghĩa ĐÃ GỠ (mô phỏng do_va_cham trên bộ sưu tập thật + V của lô: 0 va chạm dính từ k178): "
        "вероятно «có lẽ, có khả năng» (rút «chắc là» nên наве́рное hết nằm gọn trong nó) · "
        "потребность «nhu cầu, đòi hỏi» (rút «sự cần thiết», thêm/giữ «đòi hỏi» = requirement).",
        "V cần duyệt: потребоваться bỏ «sẽ» («sẽ cần» là dấu thời/thể, badge đã in thể) -> «cần đến, được cần đến, trở nên cần thiết»; "
        "оборона thêm «quốc phòng», bỏ «hàng phòng ngự»; объединение thêm «liên hiệp» (union = tổ chức).",
        "оборона: KHÔNG nối với боро́ться theo đúng bối cảnh luồng chính. Nhưng tôi KHÔNG chắc «khác gốc»: theo Vasmer "
        "оборони́ть ← боронити «che chở», có thể cùng gốc xa *bor- với бороть — thẻ chỉ nói «gốc cổ che chắn», không khẳng định chiều nào.",
        "воображение: chẻ во- = «VÀO TRONG (như в)» theo cách hiểu вообрази́ть là phỏng dịch tiếng Đức einbilden — khá chắc (~80%), "
        "không gắn ô Mức tin vì tôi đánh giá đủ chắc; cần duyệt nếu muốn chặt hơn.",
        "партийный: họ hàng có партиза́н «du kích» — cùng gốc Latin pars qua tiếng Ý partigiano (mượn, không phái sinh Nga).",
        "дума: thẻ думать [k54] ghi ду́ма «ý nghĩ»; thẻ này nói nghĩa đó nay là văn thơ cổ, nghĩa chính là Duma/hội đồng — không mâu thuẫn, chỉ lệch nhấn.",
        "Không ô Mức tin nào trong lô; không từ nào vắng Họ hàng.",
    ],
}
