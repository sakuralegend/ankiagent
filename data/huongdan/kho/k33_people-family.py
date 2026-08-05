# -*- coding: utf-8 -*-
"""k33 — people::family: người trong nhà và người quanh mình.

Trục của lô: tiếng Nga gọi người thân bằng DẠNG THÂN MẬT (-ушка, -очка) chứ không
bằng từ trang trọng, và tách hẳn hai bên nam/nữ ở chuyện cưới xin (жена́т ↔ за́мужем).
"""

# 🔴 KHÔNG dựng biến khối dùng chung (HE/LUAT/THE…) rồi cộng vào mọi thẻ.
# Đó là cách cũ, đã bỏ 28/07 — xem README §3.

S = {}

S["подруга"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">(đi) CÙNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-друг-</span>'
    '<span class="hd-gloss">BẠN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <b>друг</b> khoác thêm <b>по-</b> và đuôi giống cái: '
    '“người cùng làm bạn” ở phái nữ. Bạn nam là <b>друг</b>, bạn nữ là <b>подру́га</b> — '
    'một gốc, hai đuôi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дру́жба</b> tình bạn · <b>дружи́ть</b> chơi thân · '
    '<b>дру́жный</b> đoàn kết</div>'
)

S["девочка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дев-</span>'
    '<span class="hd-gloss">CON GÁI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-очк-</span>'
    '<span class="hd-gloss">hậu tố NHỎ, thân mật</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>дев-</b> cộng đuôi nhỏ <b>-очка</b> ⇒ con gái còn bé. '
    'Đổi hậu tố thành <b>-ушка</b> là lớn lên một bậc: <b>де́вушка</b> cô gái trẻ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>де́вушка</b> cô gái trẻ · <b>де́ва</b> thiếu nữ (văn chương)</div>'
    '<div class="hd-why">Bảng chia: cách 2 và cách 4 số nhiều chèn thêm một nguyên âm vào chỗ '
    'hai phụ âm dính nhau — <b>де́вочек</b>. Danh từ cái đuôi <b>-ка</b> nào cũng vậy.</div>'
)

S["бабушка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">баб-</span>'
    '<span class="hd-gloss">ĐÀN BÀ LỚN TUỔI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ушк-</span>'
    '<span class="hd-gloss">hậu tố thân mật</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng một hậu tố <b>-ушка</b> với <b>де́душка</b>: tiếng Nga gọi ông bà '
    'bằng dạng THÂN MẬT, chứ không bằng từ trang trọng. Nghe <b>-ушка</b> là nghe thấy tình cảm '
    'trong đó.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ба́ба</b> đàn bà, bà già (nói thô) · <b>ба́бушкин</b> của bà</div>'
    '<div class="hd-why">Bảng chia: chỉ một chỗ lệch — cách 2 và 4 số nhiều chèn thêm chữ '
    '<b>е</b>: <b>ба́бушек</b>, y như <b>де́вочек</b>.</div>'
)

S["девушка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дев-</span>'
    '<span class="hd-gloss">CON GÁI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ушк-</span>'
    '<span class="hd-gloss">hậu tố thân mật</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc <b>де́вочка</b>, chỉ đổi hậu tố: <b>-очка</b> còn bé, '
    '<b>-ушка</b> đã lớn. Đây cũng là tiếng gọi lịch sự một cô gái lạ ngoài đường.</div>'
    '<div class="hd-warn">Ba bậc tuổi, đừng lẫn: <b>де́вочка</b> trẻ con → <b>де́вушка</b> '
    'thiếu nữ đến thanh niên → <b>же́нщина</b> phụ nữ trưởng thành.</div>'
    '<div class="hd-warn"><b>моя́ де́вушка</b> = bạn gái đang yêu; còn <b>моя́ подру́га</b> '
    'thường chỉ là một người bạn nữ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>де́вочка</b> bé gái · <b>де́ва</b> thiếu nữ (văn chương)</div>'
    '<div class="hd-why">Bảng chia: cách 2 và 4 số nhiều chèn thêm chữ <b>е</b> — '
    '<b>де́вушек</b>.</div>'
)

S["дедушка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дед-</span>'
    '<span class="hd-gloss">ÔNG, CỤ GIÀ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ушк-</span>'
    '<span class="hd-gloss">hậu tố thân mật</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi trông như giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng hậu tố với <b>ба́бушка</b>. Nhưng đuôi <b>-а</b> ở đây KHÔNG '
    'làm nó thành giống cái: từ chỉ đàn ông thì vẫn là giống đực ⇒ <b>мой де́душка</b>, không '
    'phải <b>моя́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дед</b> ông, cụ già · <b>де́душкин</b> của ông</div>'
    '<div class="hd-why">Bảng chia: đuôi chia y hệt một danh từ cái đuôi <b>-ка</b> '
    '(<b>де́душке</b>, <b>де́душкой</b>), chỉ cách 2 và 4 số nhiều chèn thêm <b>е</b>: '
    '<b>де́душек</b>.</div>'
)

S["мама"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: <b>ма́ма</b> là tiếng bập bẹ đầu đời, gần như ngôn ngữ '
    'nào cũng có (mama, má). Đừng cố tìm gốc cho nó.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhớ theo chỗ dùng, không theo cấu tạo: <b>ма́ма</b> là tiếng gọi trong '
    'nhà, còn từ trung tính dùng khi nói với người ngoài hay khai giấy tờ là <b>мать</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ма́мин</b> của mẹ · <b>ма́мочка</b> mẹ yêu</div>'
)

S["жена"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">жен-</span>'
    '<span class="hd-gloss">VỢ, ĐÀN BÀ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́</span>'
    '<span class="hd-gloss">đuôi giống cái, mang trọng âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>жен-</b> mọc ra cả một họ: <b>же́нщина</b> phụ nữ, '
    '<b>жени́ться</b> lấy vợ, và <b>жена́тый</b> nghĩa đen là “có vợ” — nên từ đó chỉ nói về '
    'đàn ông.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>же́нщина</b> phụ nữ · <b>жена́тый</b> đã có vợ · <b>жени́ться</b> '
    'lấy vợ · <b>жени́х</b> chú rể</div>'
    '<div class="hd-why">Bảng chia: số ít trọng âm ở đuôi (<b>жена́</b>, <b>жены́</b>); sang số '
    'nhiều nó nhảy về gốc và chữ <b>е</b> hoá thành <b>ё</b> — <b>жёны</b>, <b>жён</b>.</div>'
)

S["папа"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: cũng là tiếng bập bẹ (pa-pa), cùng loại với '
    '<b>ма́ма</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi <b>-а</b> mà vẫn là giống đực vì nó chỉ đàn ông — <b>мой па́па</b>, '
    'cùng kiểu với <b>де́душка</b>. Đây là tiếng gọi trong nhà; từ trang trọng là '
    '<b>оте́ц</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>па́пин</b> của bố</div>'
)

S["сестра"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сестр-</span>'
    '<span class="hd-gloss">CHỊ / EM GÁI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́</span>'
    '<span class="hd-gloss">đuôi giống cái, mang trọng âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc Ấn–Âu với <i>sister</i> tiếng Anh. Tiếng Nga không phân chị với '
    'em: <b>сестра́</b> là cả hai, muốn rõ thì thêm <b>ста́ршая</b> lớn / <b>мла́дшая</b> '
    'nhỏ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сестри́чка</b> chị/em gái (thân mật) · <b>двою́родная сестра́</b> '
    'chị/em họ</div>'
    '<div class="hd-why">Bảng chia: số nhiều đổi hai chỗ — trọng âm chạy về gốc và <b>е</b> hoá '
    '<b>ё</b> (<b>сёстры</b>), rồi cách 2 và 4 chèn thêm một chữ <b>ё</b> vào giữa: '
    '<b>сестёр</b>.</div>'
)

S["ребята"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">реб-</span>'
    '<span class="hd-gloss">TRẺ CON</span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́т-</span>'
    '<span class="hd-gloss">hậu tố “con non”, số nhiều</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi số nhiều</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc <b>ребёнок</b>. Đuôi <b>-я́та</b> là dạng số nhiều của khuôn '
    '“con non” (<b>котёнок</b> → <b>котя́та</b> mèo con), nên từ này vừa là “bọn trẻ” vừa là '
    'tiếng gọi thân mật cả nhóm bạn.</div>'
    '<div class="hd-warn">Từ này CHỈ CÓ SỐ NHIỀU — không có dạng số ít. Muốn nói một đứa thì '
    'phải mượn từ khác: <b>ребёнок</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ребёнок</b> đứa trẻ · <b>ребя́ческий</b> trẻ con, ngây ngô</div>'
)

S["враг"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: <b>враг</b> là một gốc trơn, không có tiền tố hay hậu '
    'tố nào bám vào.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhớ theo cặp đối: <b>друг</b> bạn ↔ <b>враг</b> thù — hai từ cùng ngắn, '
    'cùng vần <b>-аг/-уг</b>, nghĩa thì ngược hẳn. Gốc này cho cả nhóm từ nói về sự thù địch, '
    'nhận ra một từ là nhận ra cả nhóm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вражда́</b> mối thù · <b>вражде́бный</b> thù địch · '
    '<b>враже́ский</b> của quân địch</div>'
    '<div class="hd-why">Bảng chia: trọng âm chỉ đứng yên ở dạng gốc <b>враг</b>; mọi dạng còn '
    'lại đều đẩy nó ra đuôi — <b>врага́</b>, <b>врагу́</b>, <b>враги́</b>.</div>'
)

S["друг"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: <b>друг</b> là gốc trơn. Nhớ kèm cặp đối của nó, '
    '<b>враг</b> kẻ thù — hai từ vần với nhau mà nghĩa ngược hẳn.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>друг-</b> mọc ra <b>подру́га</b> bạn nữ, <b>дру́жба</b> tình bạn, '
    '<b>дружи́ть</b> chơi thân.</div>'
    '<div class="hd-warn"><b>друг дру́га</b> = NHAU, không phải “bạn của bạn”. Nửa đầu đứng yên, '
    'nửa sau đổi cách: <b>друг с дру́гом</b> với nhau, <b>друг к дру́гу</b> về phía nhau.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>подру́га</b> bạn nữ · <b>дру́жба</b> tình bạn · <b>дружи́ть</b> '
    'chơi thân · <b>дру́жный</b> đoàn kết</div>'
    '<div class="hd-why">Bảng chia: số nhiều đổi hẳn thân từ, <b>г</b> thành <b>зь</b> rồi thêm '
    '<b>-я</b> — <b>друзья́</b>, cách 2 <b>друзе́й</b>. Chỗ này phải thuộc, không suy ra '
    'được.</div>'
)

S["народ"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">DỒN LÊN, tích lại</span></div>'
    '<div class="hd-row"><span class="hd-piece">-род-</span>'
    '<span class="hd-gloss">SINH RA, DÒNG GIỐNG</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen “cái sinh sôi tụ lại” ⇒ nhân dân, dân tộc. Gốc <b>род</b> '
    'này còn nằm trong <b>ро́дина</b> quê hương và <b>родно́й</b> ruột thịt.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>род</b> dòng giống · <b>ро́дина</b> quê hương · <b>наро́дный</b> '
    'thuộc về nhân dân</div>'
    '<div class="hd-why">Bảng chia: cách 2 có hai dạng — <b>наро́да</b> là dạng bình thường, còn '
    '<b>наро́ду</b> là dạng “chia phần”, dùng khi ước lượng số lượng: <b>мно́го наро́ду</b> '
    'đông người.</div>'
)

S["свидание"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">CÙNG, lại với nhau</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вид-</span>'
    '<span class="hd-gloss">NHÌN, THẤY</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ание</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen “cùng nhìn thấy nhau” ⇒ cuộc hẹn gặp. Cùng gốc với '
    '<b>ви́деть</b> nhìn thấy; đuôi <b>-ание</b> nói ngay đây là danh từ giống trung.</div>'
    '<div class="hd-warn"><b>до свида́ния</b> tạm biệt — nghĩa đen “cho tới lần gặp lại”. '
    '<b>до</b> luôn kéo cách 2, nên đuôi phải đổi thành <b>-ия</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ви́деть</b> nhìn thấy · <b>свиде́тель</b> nhân chứng (người đã '
    'thấy) · <b>уви́деться</b> gặp lại nhau</div>'
)

S["муж"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: <b>муж</b> là gốc trơn, nghĩa cổ của nó là “người đàn '
    'ông”.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>муж-</b> cho <b>мужчи́на</b> đàn ông, <b>му́жество</b> lòng dũng '
    'cảm (“chất đàn ông”), và <b>за́мужем</b> đã có chồng — nghĩa đen “ở sau lưng chồng”.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мужчи́на</b> đàn ông · <b>за́мужем</b> đã có chồng · '
    '<b>му́жество</b> lòng dũng cảm</div>'
    '<div class="hd-why">Bảng chia: số nhiều đi lối riêng, thêm <b>-ья</b> — <b>мужья́</b>, '
    'cách 2 <b>муже́й</b>. Cùng kiểu bất thường với <b>друг</b> → <b>друзья́</b>.</div>'
)

S["гений"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được theo gốc Nga: <b>ге́ний</b> mượn thẳng tiếng Latin '
    '<i>genius</i>, y như <i>genius</i> tiếng Anh.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái đáng nhớ là đuôi: danh từ đực tận cùng <b>-ий</b> không đổi sang '
    '<b>-е</b> ở cách 6 mà giữ nguyên <b>-и</b> — <b>о ге́нии</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гениа́льный</b> thiên tài, xuất chúng · <b>гениа́льность</b> sự '
    'xuất chúng</div>'
)

S["родной"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">род-</span>'
    '<span class="hd-gloss">SINH RA, DÒNG GIỐNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-</span>'
    '<span class="hd-gloss">biến danh từ → tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́й</span>'
    '<span class="hd-gloss">đuôi tính từ, mang trọng âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">“Thuộc về dòng máu của mình” ⇒ ruột thịt. Đi với ngôn ngữ thì thành '
    '“mẹ đẻ”, đi với nơi chốn thì thành “quê gốc” — vẫn là một nghĩa đó.</div>'
    '<div class="hd-warn">Số nhiều <b>родны́е</b> đứng một mình là DANH TỪ: người thân, họ hàng. '
    'Tính từ hoá danh từ, không thêm chữ nào.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>род</b> dòng giống · <b>ро́дина</b> quê hương · <b>роди́тели</b> '
    'cha mẹ · <b>роди́ться</b> được sinh ra</div>'
)

S["женатый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">жен-</span>'
    '<span class="hd-gloss">VỢ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ат-</span>'
    '<span class="hd-gloss">hậu tố “có mang cái đó”</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen là “có vợ”, nên nó chỉ nói về đàn ông. Dùng thật thì hay gặp '
    'dạng ngắn hơn là dạng đầy đủ: <b>он жена́т</b>.</div>'
    '<div class="hd-warn">Chuyện cưới xin tách hẳn hai bên: đàn ông <b>он жена́т</b>, đàn bà '
    '<b>она́ за́мужем</b> — hai từ khác gốc hẳn nhau, không phải hai giống của cùng một từ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>жена́</b> vợ · <b>жени́ться</b> lấy vợ · <b>жени́х</b> chú rể</div>'
)

S["человек"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được cho người học: từ nguyên của <b>челове́к</b> tới nay vẫn '
    'còn tranh cãi, tách ra là bịa.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thứ phải thuộc không phải gốc mà là bộ đôi: một người là '
    '<b>челове́к</b>, còn số nhiều đổi sang từ khác hẳn — <b>лю́ди</b>.</div>'
    '<div class="hd-warn">Nhưng sau số đếm thì quay lại <b>челове́к</b>, không dùng '
    '<b>лю́ди</b>: <b>пять челове́к</b> năm người, <b>ско́лько челове́к</b> bao nhiêu người.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>челове́ческий</b> thuộc về con người · <b>челове́чество</b> '
    'nhân loại</div>'
    '<div class="hd-why">Bảng chia: cả cột số nhiều đổi sang thân từ khác — <b>лю́ди</b>, '
    '<b>люде́й</b>, <b>лю́дям</b>. Dạng <b>челове́ки</b> nằm cạnh đó là lối cổ, đừng dùng.</div>'
)

S["ребёнок"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">реб-</span>'
    '<span class="hd-gloss">TRẺ CON</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ёнок</span>'
    '<span class="hd-gloss">hậu tố “CON NON”</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi <b>-ёнок</b> là khuôn chung cho con non (<b>котёнок</b> mèo con), '
    'và số nhiều của khuôn đó là <b>-я́та</b> ⇒ <b>ребя́та</b>. Nhưng nói “bọn trẻ” bình thường '
    'thì tiếng Nga dùng <b>де́ти</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ребя́та</b> bọn trẻ, các cậu · <b>ребя́ческий</b> trẻ con, '
    'ngây ngô</div>'
    '<div class="hd-why">Bảng chia: chữ <b>о</b> cuối rơi mất ngay khi đổi cách '
    '(<b>ребёнка</b>, <b>ребёнку</b>), còn số nhiều thì thay bằng từ khác hẳn — <b>де́ти</b>, '
    'hoặc <b>ребя́та</b> khi gọi thân mật.</div>'
)

S["замужем"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">Ở PHÍA SAU</span></div>'
    '<div class="hd-row"><span class="hd-piece">-муж-</span>'
    '<span class="hd-gloss">CHỒNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ем</span>'
    '<span class="hd-gloss">đuôi cách 5 đã hoá đá</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen “ở sau lưng chồng” ⇒ đang có chồng. Cả cụm dính lại thành một '
    'trạng từ nên không biến đổi gì nữa, và trọng âm bị <b>за-</b> hút về đầu.</div>'
    '<div class="hd-warn"><b>за́мужем</b> là TRẠNG THÁI đang có chồng; còn HÀNH ĐỘNG đi lấy '
    'chồng là <b>вы́йти за́муж</b> — bỏ <b>-ем</b>, chuyển sang cách 4.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>муж</b> chồng · <b>заму́жняя</b> đã có chồng (tính từ)</div>'
)

# ---------------------------------------------------------------------------
# FIELD `Vietnamese` — đề bài của deck 1-go, user GÕ từ Nga từ dòng này.
# Chỉ ghi những từ cần sửa; không ghi từ loại / giống / thể (đã có badge).
V = {
    'друг': 'người bạn nam',
    'подруга': 'người bạn nữ',
    'девочка': 'bé gái, cô bé',
    'девушка': 'cô gái trẻ, thiếu nữ',
    'мама': 'mẹ, má',
    'папа': 'bố, ba',
    'сестра': 'chị gái, em gái',
    'ребята': 'các cậu, bọn trẻ, đám bạn',
    'враг': 'kẻ thù, kẻ địch',
    'народ': 'nhân dân, dân chúng',
    'свидание': 'buổi hẹn hò, cuộc hẹn gặp',
    'родной': 'ruột thịt, cùng huyết thống',
    'женатый': 'đã có vợ',
    'замужем': 'đã có chồng',
    'ребёнок': 'đứa trẻ, đứa con nhỏ',
}
