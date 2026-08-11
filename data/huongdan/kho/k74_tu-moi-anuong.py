# -*- coding: utf-8 -*-
"""k74 — tu-moi-anuong: 19 từ ăn uống + khách khứa, KHÔNG cùng một họ.

Không có trục chung và cố ý không có khối hệ thống dùng chung. Mấy chỗ giao nhau
đều nằm trọn trong lô nên xử lý cả hai phía bằng một câu ngắn ở từng thẻ, không
dựng bảng chung: пиро́г ↔ торт (vỏ bột bọc nhân vs bánh kem), гость ↔ пригласи́ть
(cụm «в го́сти»), вме́сте ↔ ме́сто (в + мест-). Nhóm từ mượn được tra gốc TỪNG TỪ
chứ không gộp: во́дка là gốc Nga trong suốt (вода́ + -ка), кулинари́я / компо́т /
дие́та / торт / бутербро́д là mượn có gốc châu Âu tra được, còn кефи́р thì đường
vào tiếng Nga rõ nhưng gốc xa hơn các từ điển còn cãi — thẻ nói thẳng mức tin đó.
"""

# 🔴 KHÔNG dựng biến khối dùng chung (HE/LUAT/THE…) rồi cộng vào mọi thẻ.

S = {}
V = {}

# ------------------------------------------------------------------- блин
S["блин"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một khối, không chẻ ra được: <b>блин</b> là gốc trơn. '
    'Từ nguyên nối nó với <b>моло́ть</b> (xay) — xay ra bột rồi tráng thành bánh — '
    'nhưng đó là từ nguyên, không phải luật suy ra được. Cái phải nhớ là trọng âm '
    'chạy ra đuôi ở mọi cách khác: <b>блин → блина́, блины́</b>.</div>'
    '<div class="hd-warn">🔥 <b>Блин!</b> là thán từ nghe hằng ngày — bản nói giảm '
    'của <b>чёрт</b>, cỡ «Chết rồi!/Ôi trời!». Không hề thô, người lớn nói thoải mái.</div>'
    '<div class="hd-warn">💬 <b>Пе́рвый блин ко́мом</b> — «cái bánh đầu tiên bị vón cục»: '
    'lần đầu làm gì cũng hỏng, đừng nản.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бли́нчик</b> bánh kếp nhỏ, thường cuốn nhân</div>'
)

# -------------------------------------------------------------- бутербро́д
S["бутерброд"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бутер-</span>'
    '<span class="hd-gloss">Butter tiếng Đức — bơ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бро́д</span>'
    '<span class="hd-gloss">Brot tiếng Đức — bánh mì</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mượn nguyên khối tiếng Đức <i>Butterbrot</i> «bánh mì phết bơ», '
    'tức đúng <b>хлеб</b> với <b>ма́сло</b> — chỉ có điều cả hai mảnh đều là tiếng Đức, '
    'không phải gốc Nga. Món Nga này là lát bánh mì HỞ, đồ ăn đặt lên trên, không phải '
    'hai lát kẹp lại. Trọng âm ở âm cuối và đứng yên ở mọi cách.</div>'
    '<div class="hd-warn">⚠️ <b>-бро́д</b> ở đây là <i>Brot</i>, KHÔNG dính gì tới '
    '<b>брод</b> (chỗ cạn lội qua sông) hay <b>броди́ть</b> — chỉ trùng mặt chữ.</div>'
)

# ----------------------------------------------------------------- вме́сте
S["вместе"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">giới từ «ở trong»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мест-</span>'
    '<span class="hd-gloss">CHỖ, nơi — chính là <b>ме́сто</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е</span>'
    '<span class="hd-gloss">đuôi cách 6 đông cứng lại</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: «ở cùng một chỗ» → cùng nhau. Cụm giới từ + danh từ '
    'dính lại thành một trạng từ, nên nay viết liền và không biến đổi gì nữa.</div>'
    '<div class="hd-warn">⚠️ Khác <b>вме́сто</b> (thay cho) đúng một chữ cuối mà nghĩa '
    'ngược hẳn. Cách dùng cũng khác: <b>вме́сте с бра́том</b> cùng với anh (с + cách 5), '
    'còn <b>вме́сто бра́та</b> thay cho anh (kéo thẳng cách 2).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ме́сто</b> chỗ, nơi · <b>вме́сто</b> thay cho · '
    '<b>ме́стный</b> thuộc địa phương</div>'
)

# ------------------------------------------------------------------ во́дка
S["водка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вод-</span>'
    '<span class="hd-gloss">NƯỚC — gốc của <b>вода́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-</span>'
    '<span class="hd-gloss">hậu tố thu nhỏ / thân mật</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen «nước nhỏ, nước con» — đúng kiểu châu Âu gọi rượu mạnh '
    'là <i>aqua vitae</i> (nước sự sống). Đây là từ gốc Nga trong suốt, thấy ngay '
    '<b>вода́</b> bên trong; trọng âm nhảy về gốc <b>во́дка</b> chứ không ở đuôi như '
    '<b>вода́</b>.</div>'
    '<div class="hd-warn">⚠️ Số nhiều cách 2 CHÈN thêm о giữa д và к: <b>во́док</b>. Đó là '
    'nếp chung của danh từ cái đuôi <i>-ка</i> — gặp lại ở <b>ло́жка → ло́жек</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вода́</b> nước · <b>во́дный</b> thuộc về nước · '
    '<b>подво́дный</b> dưới nước</div>'
)

# ------------------------------------------------------------------ гость
S["гость"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được — nhưng nó là họ hàng Ấn–Âu thật sự của '
    '<i>guest</i> tiếng Anh (và <i>hostis</i> Latin): nghĩa cổ là «người lạ đến nhà». '
    'Trọng âm ở gốc trong số ít (<b>го́стя</b>) rồi dồn ra đuôi từ số nhiều cách 2 trở đi: '
    '<b>го́сти</b> nhưng <b>госте́й, гостя́м</b>.</div>'
    '<div class="hd-warn">⚠️ Đuôi <i>-ь</i> nhưng GIỐNG ĐỰC, ngược với phần lớn danh từ '
    '<i>-ь</i>: nói <b>но́вый гость</b>, không phải «но́вая».</div>'
    '<div class="hd-warn">💬 Hai cụm buộc thuộc, đều dùng dạng số nhiều: '
    '<b>идти́ в го́сти</b> đi làm khách (đang trên đường) · <b>быть в гостя́х</b> đang ở '
    'nhà người ta.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гости́ница</b> khách sạn · <b>гости́ная</b> phòng khách · '
    '<b>угости́ть</b> chiêu đãi ai món gì</div>'
)

# ------------------------------------------------------------------ дие́та
S["диета"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không có gốc Nga để chẻ: mượn từ Hy Lạp <i>diaita</i> «nếp sống, '
    'chế độ sinh hoạt», vào tiếng Nga qua các thứ tiếng châu Âu — cùng một từ với '
    '<i>diet</i> tiếng Anh. Chỉ phải đổi thói quen đọc: trọng âm rơi vào chữ е '
    '(<b>дие́та</b>), và hai nguyên âm и-е đọc rời nhau.</div>'
    '<div class="hd-warn">💬 Cụm phải thuộc: <b>сиде́ть на дие́те</b> — nghĩa đen «ngồi trên '
    'chế độ ăn» = đang ăn kiêng. Đi với <i>на</i> + cách 6.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>диети́ческий</b> thuộc chế độ ăn kiêng · '
    '<b>дието́лог</b> chuyên gia dinh dưỡng</div>'
)

# ------------------------------------------------------------------- ка́ша
S["каша"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc trơn của tiếng Slav, một khối. Nghĩa đen là ngũ cốc nấu nhừ — '
    'món sáng chuẩn của người Nga (<b>гре́чневая ка́ша</b> cháo kiều mạch, '
    '<b>ма́нная ка́ша</b> cháo bột báng). Chính cái «nhừ, quánh, trộn lẫn hết vào nhau» '
    'đẻ ra nghĩa bóng, và nghĩa bóng dùng nhiều ngang nghĩa đen.</div>'
    '<div class="hd-warn">🔥 <b>Ка́ша в голове́</b> — «trong đầu như nồi cháo»: rối tinh, '
    'không đâu vào đâu.</div>'
    '<div class="hd-warn">💬 <b>Завари́ть ка́шу</b> «nấu nồi cháo» = gây ra một mớ rắc rối, '
    'rồi ai đó phải dọn.</div>'
)

# ------------------------------------------------------------------ кефи́р
S["кефир"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Sữa lên men, chua nhẹ, loãng nên UỐNG chứ không xúc thìa. Không '
    'chẻ được: từ này vào tiếng Nga từ vùng Kavkaz, còn gốc xa hơn nữa thì các từ điển vẫn '
    'chưa thống nhất — đừng đi tìm gốc Nga cho nó. Điểm duy nhất phải luyện: trọng âm ở '
    'âm CUỐI và đứng yên ở mọi cách (<b>кефи́р, кефи́ра, кефи́ром</b>), khác thói quen đọc '
    '<i>KEfir</i> của tiếng Anh.</div>'
    '<div class="hd-warn">💬 Đồ uống thì đếm bằng vật chứa, và vật chứa kéo theo cách 2: '
    '<b>стака́н кефи́ра</b> một cốc kefir.</div>'
)

# ----------------------------------------------------------------- компо́т
S["компот"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mượn từ tiếng Pháp <i>compote</i>, gốc Latin <i>composita</i> '
    '«đặt chung với nhau» — cùng ổ với <i>compose / composite</i> tiếng Anh. Nhớ đúng cái '
    'hình ảnh đó: đủ thứ quả bỏ chung vào một nồi. Mặt chữ Nga không còn tách được nữa nên '
    'không chẻ; trọng âm ở âm cuối và đứng yên.</div>'
    '<div class="hd-warn">⚠️ Ở Nga <b>компо́т</b> là ĐỒ UỐNG: nước quả nấu loãng, uống bằng '
    'cốc, hay đứng cuối bữa ăn — không phải món mứt quả đặc như <i>compote</i> phương Tây.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>компози́тор</b> nhà soạn nhạc (họ xa: cùng gốc Latin '
    '«đặt cùng nhau»)</div>'
)

# ------------------------------------------------------------- кулинари́я
S["кулинария"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кулинар-</span>'
    '<span class="hd-gloss">Latin <i>culina</i> — cái BẾP</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́я</span>'
    '<span class="hd-gloss">đuôi tên một ngành, một lĩnh vực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vào tiếng Nga qua châu Âu, cùng gốc với <i>culinary</i> tiếng Anh. '
    'Đuôi <i>-ия</i> đánh dấu tên ngành, nên đây là «nghề bếp, nghệ thuật nấu nướng» chứ '
    'không phải việc nấu một bữa cụ thể.</div>'
    '<div class="hd-warn">⚠️ Trọng âm DỊCH khi đổi đuôi: danh từ <b>кулинари́я</b> nhưng '
    'tính từ <b>кулина́рный</b> kéo lên -на́р-. Đừng đọc theo quán tính.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кулина́рный</b> thuộc nấu nướng · <b>кулина́р</b> người sành '
    'bếp núc · <b>по́вар</b> đầu bếp (khác gốc, nhưng đây mới là từ thường dùng)</div>'
)

# ---------------------------------------------------------------- люби́мый
S["любимый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">люб-</span>'
    '<span class="hd-gloss">YÊU — gốc của <b>люби́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-им-</span>'
    '<span class="hd-gloss">đuôi «đang ĐƯỢC …», nghĩa bị động</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen «đang được yêu». Từ đó ra cả hai nghĩa: đồ vật thì thành '
    '«mà mình thích nhất», người thì thành «người mình yêu». Cùng khuôn <i>-им-</i> với '
    '<b>ви́димый</b> (nhìn thấy được).</div>'
    '<div class="hd-warn">⚠️ <b>Мой люби́мый фильм</b> đã hàm ý «thích NHẤT» rồi, không cần '
    'thêm <b>са́мый</b>.</div>'
    '<div class="hd-warn">💬 Dùng thẳng như danh từ thì là người yêu: <b>люби́мый</b> anh yêu, '
    '<b>люби́мая</b> em yêu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>люби́ть</b> yêu, thích · <b>любо́вь</b> tình yêu · '
    '<b>люби́мец</b> con cưng</div>'
)

# ------------------------------------------------------------------ пиро́г
S["пирог"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пир-</span>'
    '<span class="hd-gloss">BỮA TIỆC — <b>пир</b> là tiệc lớn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́г</span>'
    '<span class="hd-gloss">đuôi danh từ cũ, nay không mang nghĩa riêng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Món của bữa tiệc» — bánh nướng vỏ bột bọc nhân, ngọt hay mặn đều '
    'được. Chuỗi <b>пить → пир → пиро́г</b> là từ nguyên, không phải luật suy ra được. '
    'Trọng âm dồn ra đuôi ở mọi cách khác: <b>пироги́, пирого́м</b>.</div>'
    '<div class="hd-warn">⚠️ Hai đứa con chỉ khác chỗ đặt trọng âm: <b>пирожо́к</b> bánh nhỏ '
    'có nhân, cầm tay ăn — <b>пиро́жное</b> bánh ngọt kiểu Âu, không bọc nhân.</div>'
    '<div class="hd-warn">⚠️ <b>Пиро́г</b> không phải <b>торт</b>: торт là bánh kem nhiều '
    'tầng của tiệc sinh nhật.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пир</b> bữa tiệc lớn · <b>пить</b> uống (họ xa, cùng gốc)</div>'
)

# ---------------------------------------------------------------- пода́рок
S["подарок"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố làm trọn việc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-да́р-</span>'
    '<span class="hd-gloss">TRAO, TẶNG — <b>дар</b> món quà</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ок</span>'
    '<span class="hd-gloss">đuôi vật cụ thể, giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen «cái được trao cho», cùng gốc với <b>дать</b> (cho) và '
    '<b>дари́ть</b> (tặng).</div>'
    '<div class="hd-warn">⚠️ Nguyên âm CHẠY: chữ о của <i>-ок</i> biến mất ở mọi cách ngoài '
    'cách 1 — <b>пода́рок → пода́рка, пода́рку, пода́рком</b>. Đúng nếp của '
    '<b>поря́док → поря́дка</b>.</div>'
    '<div class="hd-warn">💬 <b>Подари́ть</b> đòi hai cách một lúc: người nhận cách 3, món '
    'quà cách 4 — <b>подари́ть дру́гу кни́гу</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дар</b> món quà, thiên phú · <b>дари́ть</b> tặng · '
    '<b>пода́рочный</b> để làm quà</div>'
)

# --------------------------------------------------------------- поле́зный
S["полезный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">поле́з-</span>'
    '<span class="hd-gloss">LỢI ÍCH — <b>по́льза</b>, ь nhả ra thành е</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-</span>'
    '<span class="hd-gloss">biến danh từ thành tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Có <b>по́льза</b>» = có ích. Chỗ duy nhất phải để ý là lúc ghép: '
    'ь nhả ra thành е và trọng âm nhảy sang -ле́з-.</div>'
    '<div class="hd-warn">⚠️ Dạng ngắn giống đực chèn thêm е: <b>поле́зен</b> '
    '(<b>поле́зна · поле́зно · поле́зны</b>) — <b>Спорт поле́зен для здоро́вья</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>по́льза</b> ích lợi · <b>испо́льзовать</b> sử dụng · '
    '<b>бесполе́зный</b> vô ích</div>'
)

# ------------------------------------------------------------- пригласи́ть
S["пригласить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">tới, đến gần chỗ mình</span></div>'
    '<div class="hd-row"><span class="hd-piece">-глас-</span>'
    '<span class="hd-gloss">TIẾNG NÓI — dạng cổ của <b>го́лос</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen «cất tiếng gọi ai đó đến chỗ mình» → mời. Cặp thể: '
    '<b>пригласи́ть</b> (hoàn thành) ↔ <b>приглаша́ть</b> (chưa hoàn thành).</div>'
    '<div class="hd-warn">⚠️ Chỉ ngôi «tôi» biến âm с → ш: <b>я приглашу́</b>, còn lại giữ с '
    '— <b>ты пригласи́шь, он пригласи́т</b>. Nếp chung của động từ đuôi <i>-си́ть</i>.</div>'
    '<div class="hd-warn">💬 Người được mời ở cách 4, rồi mới tới nơi đến: '
    '<b>пригласи́ть дру́га в го́сти</b> · <b>в рестора́н</b> · <b>на у́жин</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>приглаша́ть</b> mời (chưa hoàn thành) · <b>приглаше́ние</b> lời '
    'mời · <b>го́лос</b> giọng nói</div>'
)

# -------------------------------------------------------------- свобо́дный
S["свободный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">свобо́д-</span>'
    '<span class="hd-gloss">TỰ DO — <b>свобо́да</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-</span>'
    '<span class="hd-gloss">biến danh từ thành tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một hình ảnh «không bị buộc gì» đẻ ra cả ba nghĩa dùng thật: người '
    'thì RẢNH, chỗ ngồi thì TRỐNG, đất nước thì TỰ DO.</div>'
    '<div class="hd-warn">💬 Hai câu phải thuộc: <b>Э́то ме́сто свобо́дно?</b> «Chỗ này trống '
    'chứ?» · <b>Вы свобо́дны сего́дня?</b> «Hôm nay anh rảnh không?»</div>'
    '<div class="hd-warn">⚠️ Dạng ngắn chèn е ở giống đực: <b>свобо́ден · свобо́дна · '
    'свобо́дно · свобо́дны</b>. Dạng ngắn nói trạng thái lúc này, dạng dài tả tính chất.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>свобо́да</b> tự do · <b>свобо́дно</b> thoải mái; nói ngoại ngữ '
    '«trôi chảy»</div>'
)

# ------------------------------------------------------------------- торт
S["торт"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không chẻ được: mượn từ Ý <i>torta</i> / Đức <i>Torte</i>, gốc '
    'Latin <i>torta</i> «cái bánh xoắn» — cùng ổ với <i>torte</i> tiếng Anh. Trọng âm đứng '
    'YÊN ở chữ о trong mọi cách: <b>то́рта, то́рты</b> — ngược hẳn <b>пиро́г</b> vốn dồn '
    'trọng âm ra đuôi (<b>пироги́</b>).</div>'
    '<div class="hd-warn">⚠️ <b>Торт</b> là bánh kem nhiều tầng, cắt miếng ở tiệc sinh nhật; '
    '<b>пиро́г</b> là bánh nướng vỏ bột bọc nhân. Mua bánh sinh nhật thì hỏi торт.</div>'
)

# ----------------------------------------------------------------- удо́бно
S["удобно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố: làm cho đạt tới</span></div>'
    '<div class="hd-row"><span class="hd-piece">-до́б-</span>'
    '<span class="hd-gloss">VỪA, HỢP</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-о</span>'
    '<span class="hd-gloss">tính từ, rồi -о biến thành trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Là <b>удо́бный</b> thay đuôi <i>-о</i>: «vừa vặn với mình» → tiện, '
    'thoải mái. Gốc <i>-доб-</i> còn thấy ở <b>удо́бство</b> (tiện nghi).</div>'
    '<div class="hd-warn">⚠️ Câu KHÔNG có chủ ngữ, người thấy tiện đứng ở CÁCH 3: '
    '<b>Мне удо́бно</b> tôi thấy thoải mái · <b>Вам удо́бно в семь?</b> bảy giờ anh có '
    'tiện không?</div>'
    '<div class="hd-warn">💬 <b>Неудо́бно</b> ngoài nghĩa «bất tiện» còn nghĩa NGẠI: '
    '<b>Мне неудо́бно проси́ть</b> tôi ngại phải nhờ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>удо́бный</b> tiện, thoải mái · <b>удо́бство</b> tiện nghi · '
    '<b>подо́бный</b> tương tự</div>'
)

# ----------------------------------------------------------- удово́льствие
S["удовольствие"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">удо-</span>'
    '<span class="hd-gloss">tiền tố kép: đạt tới mức ĐỦ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-во́ль-</span>'
    '<span class="hd-gloss">Ý MUỐN — <b>во́ля</b> ý chí, ý muốn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ствие</span>'
    '<span class="hd-gloss">đuôi danh từ trừu tượng, giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen «được thoả ý muốn» → niềm vui, sự thích thú. Đuôi '
    '<i>-ие</i> cho biết đây là danh từ giống TRUNG, như <b>упражне́ние</b>.</div>'
    '<div class="hd-warn">💬 <b>С удово́льствием!</b> «Rất sẵn lòng!» — câu trả lời chuẩn khi '
    'nhận lời mời. Sau <i>с</i> là cách 5.</div>'
    '<div class="hd-warn">💬 <b>Получа́ть удово́льствие от</b> + cách 2 = thấy thích thú vì '
    'cái gì (<b>от му́зыки</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дово́льный</b> hài lòng · <b>во́ля</b> ý chí · '
    '<b>позво́лить</b> cho phép</div>'
)


# ===========================================================================
# FIELD TIENG VIET (README §2c) — chi sua nhung dong con ngoac / loi giai
# thich, dua ve THUAN danh sach nghia ngan bang dau phay.
# ===========================================================================

V["блин"] = "bánh kếp, bánh rán mỏng, chết tiệt"
V["каша"] = "cháo, mớ lộn xộn, sự rối rắm"
V["кефир"] = "kefir, sữa chua uống"
V["компот"] = "nước quả nấu, compote"
V["пирог"] = "bánh nướng có nhân, bánh pie"
