# -*- coding: utf-8 -*-
"""k24 — life::home: đồ đạc trong nhà, phần lớn là danh từ MỘT âm tiết
(пол·стол·стул·дом·шкаф) nơi trọng âm cư xử mỗi từ một kiểu, cộng ba từ
dựng bằng cùng hậu tố công cụ -ло (мы́ло·зе́ркало·одея́ло)."""

# 🔴 KHÔNG dựng biến khối dùng chung rồi cộng vào mọi thẻ (README §3).

S = {}

S["пол"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пол-</span>'
    '<span class="hd-gloss">gốc trơn, không chẻ thêm được</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một vỏ chữ, hai nghĩa rời hẳn nhau: mặt sàn ta đi lên, '
    'và giới tính (nam/nữ). Chỉ ngữ cảnh tách được, không có mẹo nào khác.</div>'
    '<div class="hd-warn">📍 <b>на полу́</b> = trên sàn (đồ vật nằm ở đâu) — dạng '
    '"cách vị trí" riêng sau <b>на</b>/<b>в</b>, khác <b>о по́ле</b> = nói VỀ cái sàn. '
    'Ngoài chỗ đó trọng âm đứng yên ở gốc suốt số ít.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>напо́льный</b> đặt dưới sàn · <b>полово́й</b> thuộc giới tính · '
    '<b>полови́на</b> một nửa (họ với nghĩa "giới tính": hai nửa loài người)</div>'
)

S["стол"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">стол-</span>'
    '<span class="hd-gloss">bàn; nghĩa cổ: ngai, chỗ ngồi cao</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa cổ "ngai vua" còn sống nguyên trong <b>столи́ца</b> — '
    'thủ đô là thành phố đặt ngai. Từ chỗ ngồi cao mà ra mặt bàn.</div>'
    '<div class="hd-warn">📍 Trọng âm bỏ gốc ngay từ cách 2 rồi ở lì đuôi: '
    '<b>стола́</b>, <b>столо́м</b>, số nhiều <b>столы́</b>. Đừng kéo <b>стул</b> theo '
    'khuôn này — nó ngược hẳn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>столи́ца</b> thủ đô · <b>столо́вая</b> phòng ăn, căng-tin · '
    '<b>насто́льный</b> để bàn</div>'
)

S["стул"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">стул</span>'
    '<span class="hd-gloss">mượn thẳng tiếng Đức <i>Stuhl</i>, không chẻ được</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bắt qua tiếng Anh <i>stool</i> — cùng một gốc German. '
    'Nó chỉ khác <b>стол</b> đúng một nguyên âm, nhưng không phải biến thể của '
    '<b>стол</b>: hai từ vào tiếng Nga bằng hai đường riêng, nên chia cũng riêng.</div>'
    '<div class="hd-warn">📍 Số nhiều bẻ hẳn khuôn: <b>сту́лья</b>, <b>сту́льев</b> '
    '(kiểu <b>бра́тья</b>), và trọng âm ngồi yên ở gốc suốt — ngược hẳn <b>столы́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сту́льчик</b> ghế nhỏ, ghế ăn trẻ em</div>'
)

S["дом"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дом-</span>'
    '<span class="hd-gloss">nhà, nhà cửa, gia đình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc Ấn–Âu rất cổ, cùng nguồn với <i>domus</i> tiếng Latin, '
    'nên tiếng Anh <i>domestic</i> "thuộc gia đình" là chỗ bắc cầu chắc nhất.</div>'
    '<div class="hd-warn">📍 Số nhiều lấy đuôi <b>-а́</b> có trọng âm: <b>дома́</b>, '
    '<b>домо́в</b> — không có "до́мы". Chú ý <b>дома́</b> (những ngôi nhà) chỉ khác '
    '<b>до́ма</b> (đang ở nhà) ở chỗ đánh dấu. Còn <b>на дому́</b> = làm việc tại nhà, '
    'khác <b>в до́ме</b> = ở bên trong ngôi nhà.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>до́ма</b> ở nhà · <b>домо́й</b> về nhà · '
    '<b>дома́шний</b> thuộc về nhà · <b>до́мик</b> ngôi nhà nhỏ</div>'
)

S["телефон"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">теле-</span>'
    '<span class="hd-gloss">XA (gốc Hy Lạp)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-фон</span>'
    '<span class="hd-gloss">ÂM THANH, tiếng nói</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ghép thẳng: "tiếng nói từ xa". Hai mảnh này đều làm việc '
    'tiếp ở chỗ khác — <b>теле-</b> quay lại trong <b>телеви́зор</b> (nhìn xa), '
    '<b>-фон</b> quay lại trong <b>микрофо́н</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>телефо́нный</b> thuộc điện thoại · <b>микрофо́н</b> micrô · '
    '<b>магнитофо́н</b> máy ghi âm</div>'
)

S["зеркало"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">зер-</span>'
    '<span class="hd-gloss">NHÌN (gốc cổ, còn sống trong <b>зре́ние</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-(к)ало</span>'
    '<span class="hd-gloss">hậu tố VẬT DỤNG: cái để làm việc đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen "cái để nhìn". Hậu tố <b>-ло</b> dựng tên đồ vật '
    'từ động từ, và nó mở khoá luôn hai từ nữa ngay trong lô này: <b>мы́ло</b> cái để '
    'rửa, <b>одея́ло</b> cái để trùm.</div>'
    '<div class="hd-warn">📍 Sang số nhiều trọng âm nhảy ra đuôi: <b>зеркала́</b>. '
    'Riêng cách 2 số nhiều rụng hết đuôi nên nó lùi về gốc: <b>зерка́л</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>зре́ние</b> thị giác · <b>зри́тель</b> khán giả · '
    '<b>зерка́льный</b> như gương, bóng loáng</div>'
)

S["мыло"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мы-</span>'
    '<span class="hd-gloss">RỬA (từ <b>мыть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ло</span>'
    '<span class="hd-gloss">hậu tố VẬT DỤNG</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">"Cái để rửa" — đúng cùng khuôn <b>зе́ркало</b> và '
    '<b>одея́ло</b> trong lô này. Biết một hậu tố, đọc ra được cả ba từ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мыть</b> rửa · <b>мы́ться</b> tắm rửa · '
    '<b>умыва́ться</b> rửa mặt · <b>мы́льница</b> hộp đựng xà phòng</div>'
)

S["одеяло"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">BAO QUANH, trùm khắp</span></div>'
    '<div class="hd-row"><span class="hd-piece">-де-</span>'
    '<span class="hd-gloss">ĐẶT LÊN, khoác (như <b>оде́ть</b> mặc cho ai)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́ло</span>'
    '<span class="hd-gloss">hậu tố VẬT DỤNG</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ba mảnh cộng lại: "cái khoác trùm quanh người". '
    'Cùng ổ với <b>оде́жда</b> quần áo — chăn cũng là thứ ta mặc, chỉ khác là mặc khi ngủ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оде́жда</b> quần áo · <b>одева́ться</b> mặc quần áo · '
    '<b>наде́ть</b> mặc vào, đeo vào</div>'
)

S["окно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ок-</span>'
    '<span class="hd-gloss">MẮT (từ <b>о́ко</b> cổ, nay còn trong <b>очки́</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-но</span>'
    '<span class="hd-gloss">đuôi danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cửa sổ là "con mắt của ngôi nhà" — nghĩa đen còn đọc ra được. '
    'Đuôi <b>-о</b> cho biết luôn đây là giống trung.</div>'
    '<div class="hd-warn">📍 Số ít trọng âm ở đuôi (<b>окно́</b>, <b>окна́</b>), sang số '
    'nhiều nó lùi về gốc: <b>о́кна</b>. Cách 2 số nhiều rụng đuôi nên mọc thêm một '
    'nguyên âm chạy: <b>о́кон</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>очки́</b> kính mắt · <b>подоко́нник</b> bệ cửa sổ · '
    '<b>о́ко</b> mắt (từ cổ, văn chương)</div>'
)

S["ведро"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вед-</span>'
    '<span class="hd-gloss">gốc trơn, không chẻ được nữa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ро</span>'
    '<span class="hd-gloss">đuôi danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ nguyên nối nó với <b>вода́</b> — cái xô là đồ đựng nước. '
    'Neo nghĩa vào đó thì nhớ được, nhưng xem tiếp ô đỏ trước khi tin chắc.</div>'
    '<div class="hd-warn">⚠️ Mức tin: chỗ nối với <b>вода́</b> là từ nguyên xa, KHÔNG '
    'phải luật chẻ từ suy ra được. Dùng làm mẹo nhớ thì tốt, đừng dùng làm căn cứ.</div>'
    '<div class="hd-warn">📍 Số nhiều đổi cả nguyên âm lẫn chỗ trọng âm: <b>вёдра</b>, '
    'cách 2 <b>вёдер</b>. Chữ <b>ё</b> tự nó đã mang trọng âm nên không đánh dấu thêm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ведёрко</b> xô nhỏ, xô con</div>'
)

S["бюро"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бюро</span>'
    '<span class="hd-gloss">mượn thẳng tiếng Pháp <i>bureau</i>, không chẻ được</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhận qua tiếng Anh <i>bureau</i>. Nó giữ nguyên lối Pháp cả ở '
    'trọng âm cuối từ <b>бюро́</b> lẫn ở chỗ không chịu biến hình — xem ô đỏ.</div>'
    '<div class="hd-warn">📍 KHÔNG biến cách. Cả 6 cách, cả số nhiều đều viết y hệt: '
    '<b>бюро́</b>. Số nhiều chỉ nhận ra qua động từ và tính từ đứng cạnh.</div>'
    '<div class="hd-warn">📍 Cụm hay gặp: <b>спра́вочное бюро́</b> = quầy hỏi đáp, '
    'phòng chỉ dẫn — nghĩa "văn phòng dịch vụ" của từ này nằm ở đó.</div>'
)

S["компьютер"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">компьютер</span>'
    '<span class="hd-gloss">mượn thẳng tiếng Anh <i>computer</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghe gần y tiếng Anh nên nghĩa khỏi phải học. Việc duy nhất '
    'là mặt chữ: khúc <i>-pu-</i> viết bằng <b>-пью-</b> (ь rồi ю), và trọng âm rơi '
    'đúng vào chính khúc đó — <b>компью́тер</b>, không phải cuối từ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>компью́терный</b> thuộc máy tính · '
    '<b>компью́терщик</b> dân máy tính (khẩu ngữ)</div>'
)

S["телевизор"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">теле-</span>'
    '<span class="hd-gloss">XA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-виз-</span>'
    '<span class="hd-gloss">NHÌN (gốc Latin, như <i>vision</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ор</span>'
    '<span class="hd-gloss">hậu tố tên MÁY MÓC, khí cụ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">"Máy nhìn xa", đối xứng đúng với <b>телефо́н</b> "tiếng nói từ xa" '
    'cùng lô này. Đuôi <b>-ор</b> báo đây là cái máy, y như <b>мото́р</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>телеви́дение</b> ngành truyền hình · '
    '<b>телефо́н</b> điện thoại (chung mảnh <b>теле-</b>)</div>'
)

S["ковёр"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ковёр</span>'
    '<span class="hd-gloss">gốc trơn, từ nguyên còn tranh cãi — không chẻ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không chẻ được, cũng không bắc cầu sang tiếng Anh được: '
    'đây là từ phải thuộc trơn. Bù lại, cái đáng học nằm hết ở chỗ nó biến hình.</div>'
    '<div class="hd-warn">📍 Nguyên âm chạy: <b>ё</b> rụng hẳn khi có đuôi — '
    '<b>ковёр</b> nhưng <b>ковра́</b>, <b>ковро́м</b>, số nhiều <b>ковры́</b>. '
    'Trọng âm theo đuôi ra ngoài; ở dạng gốc thì <b>ё</b> tự nó đã là trọng âm, '
    'không đánh dấu thêm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ко́врик</b> thảm nhỏ, thảm chùi chân · '
    '<b>ковро́вый</b> bằng thảm</div>'
)

S["пакет"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пакет</span>'
    '<span class="hd-gloss">mượn qua tiếng Pháp/Đức, gốc như <i>pack</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bắc thẳng sang tiếng Anh <i>packet</i>. Nhưng nghĩa dùng '
    'hằng ngày ở Nga rộng hơn tiếng Anh: <b>паке́т</b> trước hết là cái TÚI đựng đồ '
    '(túi nilon siêu thị), rồi mới đến gói hàng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>упако́вка</b> bao bì · <b>упакова́ть</b> đóng gói · '
    '<b>паке́тик</b> túi con, gói nhỏ</div>'
)

S["шкаф"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">шкаф</span>'
    '<span class="hd-gloss">mượn tiếng Đức <i>Schaff</i>, gốc trơn trong tiếng Nga</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không có mảnh Nga nào để bám, nên bám bằng cụm hay gặp: '
    '<b>кни́жный шкаф</b> tủ sách, <b>шкаф для оде́жды</b> tủ quần áo.</div>'
    '<div class="hd-warn">📍 <b>в шкафу́</b> = ở trong tủ (đồ nằm đâu) — dạng "cách vị trí" '
    'riêng sau <b>в</b>, khác <b>о шка́фе</b> = nói VỀ cái tủ. Đó là ô duy nhất lệch: '
    'cách 2 vẫn là <b>шка́фа</b>, trọng âm đứng yên suốt số ít, chỉ số nhiều mới ra '
    'đuôi <b>шкафы́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>шка́фчик</b> tủ nhỏ, ngăn tủ có khoá</div>'
)

S["кровать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кровать</span>'
    '<span class="hd-gloss">mượn rất cổ từ tiếng Hy Lạp — không chẻ được</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đừng nối nó với <b>кровь</b> (máu) hay <b>кры́ша</b> (mái) — '
    'trông giống mà không cùng gốc. Từ này phải thuộc trơn.</div>'
    '<div class="hd-warn">📍 Đuôi <b>-ь</b> ở đây là giống CÁI, đi lớp biến cách thứ ba: '
    'một dạng <b>крова́ти</b> dùng chung cho cách 2, 3, 6 lẫn số nhiều. Trọng âm đứng '
    'yên ở mọi dạng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>крова́тка</b> giường cũi trẻ em</div>'
)


# --- Field Vietnamese (README §2c): đề bài deck 1-go, chỉ được có MỘT đáp án -----
# KHÔNG ghi từ loại / giống / thể / phản thân — bốn badge đã in sẵn ở mặt đề bài.
V = {}

# пол đụng chính nó (đồng tự), стол ↔ стул đụng nhau — ba dòng dưới phải tách bạch.
V["пол"] = "sàn nhà (mặt sàn ta đi lên) — cũng chính là từ chỉ giới tính nam/nữ"
V["стол"] = "cái bàn (mặt bàn có chân, để ăn hoặc làm việc)"
V["стул"] = "cái ghế tựa (một chiếc ghế rời, không phải ghế bành)"

V["дом"] = "ngôi nhà, toà nhà (bản thân công trình, không phải \"ở nhà\")"
V["шкаф"] = "cái tủ đứng (tủ quần áo, tủ sách)"
V["кровать"] = "cái giường (khung giường để nằm ngủ)"
V["ведро"] = "cái xô xách nước (thùng có quai)"
V["пакет"] = "cái túi đựng đồ (túi nilon, túi giấy), gói hàng — không phải túi xách"
V["компьютер"] = "máy vi tính (để bàn hoặc laptop, không phải máy tính bỏ túi)"
V["бюро"] = "văn phòng dịch vụ, quầy chỉ dẫn (từ mượn, không biến cách)"
