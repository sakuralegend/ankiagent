# -*- coding: utf-8 -*-
"""k76 — chúc mừng & lời chúc: từ mới user vừa thêm.

Không ép một trục chung; nhưng ba chỗ phải nói NHẤT QUÁN trong lô này:
gốc `здрав-`/`здоров-` (здоро́вье · поздра́вить · поздравля́ть), luật «lời chúc
bỏ lại cách 2» (жела́ть · уда́ча · прия́тный), và gốc «nhận» -я́т-/-приим-
(прия́тный · гостеприи́мный).
"""

S = {}

# --------------------------------------------------------------- праздник
S["праздник"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пра́здн-</span>'
    '<span class="hd-gloss">gốc <b>пра́здный</b> — rảnh việc, nhàn rỗi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ик</span>'
    '<span class="hd-gloss">hậu tố danh từ: cái mang tính chất ấy</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ngày lễ trước hết là NGÀY RẢNH VIỆC: <b>пра́здный</b> «nhàn rỗi» '
    'cộng đuôi <b>-ик</b> ra cái ngày người ta không phải làm. Chữ <b>д</b> nằm đó chỉ để '
    'lộ gốc ấy, khi đọc thì nuốt mất.</div>'
    '<div class="hd-warn">Câu chúc dùng được cho MỌI ngày lễ: <b>С пра́здником!</b> — '
    'giới từ <b>с</b> kéo theo cách 5, đúng khuôn <b>С днём рожде́ния!</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пра́здновать</b> ăn mừng, kỷ niệm · <b>пра́здничный</b> thuộc ngày '
    'lễ, tưng bừng · <b>пра́здный</b> nhàn rỗi, vô công</div>'
)

# --------------------------------------------------------------- рождение
S["рождение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рожд-</span>'
    '<span class="hd-gloss">gốc <b>род-</b> «sinh ra», bản sách vở nhà thờ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">hậu tố → danh từ giống trung, chỉ SỰ việc</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>род-</b> là «sinh»; đi qua tiếng Slavonic nhà thờ thì '
    '<b>д</b> hoá thành <b>жд</b>, y như <b>ходи́ть</b> → <b>хожде́ние</b>. Thêm '
    '<b>-ение</b> là ra danh từ giống trung: sự ra đời.</div>'
    '<div class="hd-warn">Sinh nhật là <b>день рожде́ния</b> «ngày của sự sinh» — chữ thứ hai '
    'đứng ở cách 2. Còn lời chúc là <b>С днём рожде́ния!</b> (<b>с</b> + cách 5).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>роди́ться</b> ra đời · <b>роди́тель</b> bố mẹ · <b>ро́дина</b> quê '
    'hương · <b>родно́й</b> ruột thịt · <b>наро́д</b> dân tộc</div>'
)

# ------------------------------------------------------------------ удача
S["удача"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố: đạt tới, xong xuôi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-да-</span>'
    '<span class="hd-gloss">gốc CHO, như <b>дать</b> · <b>дава́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ча</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">May mắn = cái được TRAO cho, gốc <b>да-</b> «cho» nằm ngay giữa từ. '
    'Việc gì tự nó xuôi theo ý mình thì <b>уда́ться</b> — thành, suôn sẻ.</div>'
    '<div class="hd-warn">Chúc may mắn nói trống không là <b>Уда́чи!</b> — cách 2, vì đó là '
    'phần đuôi còn lại của <b>Жела́ю тебе́ уда́чи</b>. Lời chúc tiếng Nga luôn bỏ lại cách 2 '
    'như vậy.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уда́ться</b> thành công, làm được · <b>уда́чный</b> suôn sẻ, đạt · '
    '<b>неуда́ча</b> thất bại · <b>дать</b> cho</div>'
)

# ------------------------------------------------------------------ успех
S["успех"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố: đạt tới, hoàn tất</span></div>'
    '<div class="hd-row"><span class="hd-piece">-спе́х</span>'
    '<span class="hd-gloss">gốc «kịp, tiến tới»: <b>успе́ть</b> · <b>спеши́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thành công là cái mình KỊP đạt tới: cùng gốc với <b>успе́ть</b> «kịp» '
    'và <b>спеши́ть</b> «vội vàng». Thêm hậu tố thì <b>х</b> hoá <b>ш</b>: '
    '<b>успе́х</b> → <b>успе́шный</b>.</div>'
    '<div class="hd-warn">Hỏi thăm công việc thì dùng SỐ NHIỀU: <b>Как успе́хи?</b> «Dạo này '
    'thế nào?»; lời chúc cũng số nhiều và ở cách 2: <b>Жела́ю успе́хов!</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>успе́шный</b> thành công · <b>успе́ть</b> kịp · '
    '<b>спеши́ть</b> vội vàng</div>'
)

# --------------------------------------------------------------- успешный
S["успешный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">успе́ш-</span>'
    '<span class="hd-gloss">từ <b>успе́х</b>, <b>х</b> hoá <b>ш</b> trước hậu tố</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-</span>'
    '<span class="hd-gloss">hậu tố biến danh từ thành tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ + <b>-н-</b> = tính từ, chỉ cần nhớ <b>х</b> hoá <b>ш</b> '
    'trước nó — cùng phép biến âm cho <b>смех</b> → <b>смешно́й</b> «buồn cười».</div>'
    '<div class="hd-warn">Dạng ngắn giống đực chèn thêm <b>е</b>: <b>успе́шен</b>, nhưng '
    '<b>успе́шна</b> · <b>успе́шно</b> · <b>успе́шны</b> thì không — hai phụ âm '
    '<b>шн</b> đứng sát nhau nên phải có nguyên âm chen vào. Trọng âm của từ này '
    'không nhúc nhích.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>успе́х</b> thành công · <b>успе́шно</b> một cách thành công · '
    '<b>успе́ть</b> kịp</div>'
)

# ---------------------------------------------------------------- радость
S["радость"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рад-</span>'
    '<span class="hd-gloss">gốc «vui mừng» (<b>рад</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ость</span>'
    '<span class="hd-gloss">hậu tố → danh từ trừu tượng giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi <b>-ость</b> biến một trạng thái thành cái SỰ: <b>рад</b> «thấy '
    'vui» → <b>ра́дость</b> «niềm vui». Danh từ <b>-ость</b> luôn giống cái và biến cách như '
    'từ tận cùng bằng <b>-ь</b>.</div>'
    '<div class="hd-warn">Gốc <b>рад</b> CHỈ có dạng ngắn: <b>рад</b> · <b>ра́да</b> · '
    '<b>ра́ды</b> — không có từ «ра́дый» nào cả. <b>Я рад вас ви́деть</b> = Rất vui được '
    'gặp bạn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рад</b> vui mừng · <b>ра́доваться</b> vui mừng, hân hoan · '
    '<b>ра́достный</b> vui sướng</div>'
)

# ----------------------------------------------------------------- желать
S["желать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">жел-</span>'
    '<span class="hd-gloss">gốc «mong, ước»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́-ть</span>'
    '<span class="hd-gloss">lớp chia 1: <b>жела́ю</b> · <b>жела́ешь</b> · <b>жела́ют</b></span>'
    '</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ nhỏ thêm được. Đây là động từ của LỜI CHÚC: nói '
    'ra điều mình mong cho người khác — nên nó gần «chúc» hơn là «muốn».</div>'
    '<div class="hd-warn">Học một lượt cả hai cách: <b>жела́ть</b> AI (cách 3) ĐIỀU GÌ '
    '(cách 2). <b>Жела́ю вам сча́стья</b> — thứ được chúc luôn nằm ở cách 2.</div>'
    '<div class="hd-warn">Chính vì luật ấy mà mọi lời chúc rút gọn đều đứng ở cách 2: '
    '<b>Уда́чи!</b> · <b>Прия́тного аппети́та!</b> · <b>Споко́йной но́чи!</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>жела́ние</b> mong muốn, điều ước · <b>пожела́ние</b> lời chúc · '
    '<b>пожела́ть</b> chúc một lần</div>'
)

# --------------------------------------------------------------- пожелать
S["пожелать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố thể: một lần, đã xong — không thêm nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">жела́-ть</span>'
    '<span class="hd-gloss">gốc «mong, ước» + đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vẫn là <b>жела́ть</b>, chỉ khác khung thời gian: <b>жела́ть</b> là điều '
    'mình vẫn hằng mong, còn <b>пожела́ть</b> là CẤT LỜI CHÚC một lần rồi xong.</div>'
    '<div class="hd-warn">Đổi thể không đổi cách: người nhận ở cách 3, điều chúc ở cách 2 — '
    '<b>Пожела́й мне уда́чи!</b> = Chúc tớ may mắn đi!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>жела́ть</b> mong, chúc · <b>жела́ние</b> mong muốn · '
    '<b>пожела́ние</b> lời chúc</div>'
)

# ------------------------------------------------------------- поздравить
S["поздравить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố thể: một lần, đã xong</span></div>'
    '<div class="hd-row"><span class="hd-piece">-здрав-</span>'
    '<span class="hd-gloss">gốc «khoẻ mạnh», bản Slavonic của <b>здоро́в-</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi nguyên thể lớp 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen là «chúc cho khoẻ» — cùng gốc với <b>здоро́вье</b> và với '
    'lời chào <b>здра́вствуйте</b>. Người Nga chúc mừng nhau bằng cách chúc sức khoẻ.</div>'
    '<div class="hd-warn">Hai cách phải thuộc cùng lúc: chúc mừng AI (cách 4) NHÂN DỊP gì '
    '(<b>с</b> + cách 5).</div>'
    '<div class="hd-warn">Ngôi «tôi» chèn <b>л</b> sau <b>в</b>: <b>я поздра́влю</b>, không '
    'phải «поздра́вю» — cùng luật với <b>люби́ть</b> → <b>люблю́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поздравля́ть</b> chúc mừng, thể chưa hoàn thành · '
    '<b>поздравле́ние</b> lời chúc mừng · <b>здра́вствуйте</b> xin chào</div>'
)

# ------------------------------------------------------------ поздравлять
S["поздравлять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">поздрав-</span>'
    '<span class="hd-gloss">«chúc cho khoẻ», gốc <b>здрав-</b> = <b>здоро́в-</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ля́-</span>'
    '<span class="hd-gloss">hậu tố kéo dài → thể chưa hoàn thành</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chêm <b>-я-</b> vào giữa là biến việc một lần thành việc LẶP LẠI hay '
    'ĐANG DIỄN RA. Chữ <b>л</b> hiện ra vì đứng ngay sau <b>в</b>, đúng chỗ mà ngôi «tôi» của '
    '<b>поздра́вить</b> cũng chèn <b>л</b>.</div>'
    '<div class="hd-warn">Đang chúc thì phải dùng thể CHƯA hoàn thành: '
    '<b>Поздравля́ю вас с пра́здником!</b> Nói <b>поздра́влю</b> là hoá thành lời hứa «tôi sẽ '
    'chúc», chưa chúc gì cả.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поздра́вить</b> chúc mừng một lần · <b>поздравле́ние</b> lời chúc '
    'mừng · <b>здоро́вье</b> sức khoẻ</div>'
)

# ----------------------------------------------------------------- дарить
S["дарить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дар-</span>'
    '<span class="hd-gloss">«món quà» (<b>дар</b>), từ gốc <b>да-</b> «cho»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể lớp 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>дар</b> là cái được CHO — cùng gốc <b>дать</b>. <b>Дари́ть</b> biến '
    'món quà ấy thành hành động: đem cho hẳn, không lấy lại.</div>'
    '<div class="hd-warn">Trọng âm nhảy về gốc ngay từ ngôi thứ hai: <b>дарю́</b> nhưng '
    '<b>да́ришь</b> · <b>да́рит</b> · <b>да́рят</b> — cùng khuôn <b>люблю́</b> / '
    '<b>лю́бишь</b>.</div>'
    '<div class="hd-warn">Người nhận ở cách 3, vật tặng ở cách 4: '
    '<b>Я дарю́ ма́ме цветы́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пода́рок</b> món quà · <b>подари́ть</b> tặng một lần · '
    '<b>благодари́ть</b> cảm ơn, nghĩa đen «trao điều tốt lành»</div>'
)

# ------------------------------------------------------------------- тост
S["тост"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn thẳng tiếng Anh <i>toast</i>, giữ nguyên khối và '
    'biến cách như mọi danh từ giống đực tận cùng bằng phụ âm.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một chữ ôm cả hai nghĩa vì tiếng Anh cũng thế: <i>toast</i> vốn là lát '
    'bánh mì nướng, và tục xưa thả một lát bánh nướng tẩm gia vị vào ly rượu trước khi nâng ly '
    'chúc. Tiếng Nga mượn về cả hai nghĩa.</div>'
    '<div class="hd-warn">⚠️ Mức tin: chuyện lát bánh trong ly rượu là TỪ NGUYÊN tiếng Anh, '
    'không phải luật tiếng Nga suy ra được — dùng để gắn hai nghĩa vào nhau, đừng coi là quy '
    'tắc.</div>'
    '<div class="hd-warn">Nâng ly chúc là <b>подня́ть тост</b>, và điều được chúc đi sau '
    '<b>за</b> + cách 4: <b>За здоро́вье!</b> · <b>За вас!</b></div>'
)

# ------------------------------------------------------------------- духи
S["духи"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дух-</span>'
    '<span class="hd-gloss">gốc «hơi, mùi, linh hồn»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́</span>'
    '<span class="hd-gloss">đuôi số nhiều — từ này KHÔNG có số ít</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nước hoa trong tiếng Nga là «những làn hơi»: cùng gốc với <b>дух</b> '
    '(hơi thở, tinh thần), <b>дыша́ть</b> (thở) và <b>во́здух</b> (không khí — cái hơi bốc '
    'lên).</div>'
    '<div class="hd-warn">Luôn ở SỐ NHIỀU, không có dạng số ít, kể cả khi chỉ một lọ: '
    '<b>Э́то францу́зские духи́</b>. Danh từ chỉ có số nhiều thì cũng không mang giống đực, '
    'cái hay trung nào cả.</div>'
    '<div class="hd-warn">Trọng âm là chỗ phân biệt duy nhất: <b>духи́</b> (cuối) = nước hoa, '
    'còn <b>ду́хи</b> (đầu) = các linh hồn, số nhiều của <b>дух</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дух</b> hơi thở, tinh thần · <b>дыша́ть</b> thở · '
    '<b>во́здух</b> không khí · <b>ду́шный</b> ngột ngạt</div>'
)

# ---------------------------------------------------------------- мечтать
S["мечтать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мечт-</span>'
    '<span class="hd-gloss">từ <b>мечта́</b> «ước mơ, mộng tưởng»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">lớp chia 1: <b>мечта́ю</b> · <b>мечта́ешь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Là động từ dựng thẳng từ danh từ <b>мечта́</b>: mang giấc mơ ấy trong '
    'đầu lúc ĐANG THỨC — ước ao, mơ tưởng tới một điều.</div>'
    '<div class="hd-warn">Điều mơ tới đứng sau <b>о</b> + cách 6: '
    '<b>Я мечта́ю о путеше́ствии</b>. Mơ được LÀM gì thì dùng nguyên thể: '
    '<b>мечта́ю уви́деть Москву́</b>.</div>'
    '<div class="hd-warn">Mơ lúc đang ngủ KHÔNG dùng từ này — chỗ đó là <b>ви́деть сон</b> '
    'hoặc <b>мне сни́лось</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мечта́</b> ước mơ · <b>мечта́тель</b> người mơ mộng · '
    '<b>помечта́ть</b> mơ mộng một lúc</div>'
)

# -------------------------------------------------------------- помечтать
S["помечтать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">«một lúc, một chốc» — không chỉ là dấu hiệu hoàn thành</span></div>'
    '<div class="hd-row"><span class="hd-piece">мечта́-ть</span>'
    '<span class="hd-gloss">gốc «mơ ước» + đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gắn <b>по-</b> vào một việc kéo dài thì được nghĩa LÀM MỘT LÁT RỒI '
    'THÔI: <b>посиде́ть</b> ngồi một lát, <b>погуля́ть</b> dạo một vòng, <b>помечта́ть</b> mơ '
    'mộng một chốc.</div>'
    '<div class="hd-warn">Đã «xong» nên không có thì hiện tại: chỉ nói <b>Дава́й помечта́ем!</b> '
    'hoặc <b>Я немно́го помечта́л</b>. Cách đi kèm vẫn là <b>о</b> + cách 6.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мечта́ть</b> mơ ước, thể chưa hoàn thành · <b>мечта́</b> ước mơ · '
    '<b>посиде́ть</b> ngồi một lát</div>'
)

# --------------------------------------------------------------- здоровье
S["здоровье"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">здоро́в-</span>'
    '<span class="hd-gloss">gốc «khoẻ mạnh» (<b>здоро́вый</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ье</span>'
    '<span class="hd-gloss">hậu tố danh từ trừu tượng, giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tính từ <b>здоро́вый</b> cộng <b>-ье</b> thành cái SỰ khoẻ. Gốc này có '
    'hai mặt: bản Nga <b>здоро́в-</b> và bản Slavonic <b>здрав-</b> (như <b>го́род</b> ↔ '
    '<b>град</b>) — mặt thứ hai đẻ ra <b>здра́вствуйте</b> và <b>поздра́вить</b>.</div>'
    '<div class="hd-warn">Hai câu chỉ khác một giới từ mà khác hẳn nghĩa: '
    '<b>За здоро́вье!</b> là chúc lúc nâng ly, còn <b>На здоро́вье!</b> KHÔNG phải chúc rượu — '
    'đó là câu đáp lại lời cảm ơn, kiểu «có gì đâu».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>здоро́вый</b> khoẻ mạnh · <b>здра́вствуйте</b> xin chào · '
    '<b>поздра́вить</b> chúc mừng</div>'
)

# --------------------------------------------------------- гостеприимный
S["гостеприимный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">гост-</span>'
    '<span class="hd-gloss"><b>гость</b> — khách</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е-</span>'
    '<span class="hd-gloss">nguyên âm nối hai gốc trong từ ghép</span></div>'
    '<div class="hd-row"><span class="hd-piece">-приим-</span>'
    '<span class="hd-gloss">«đón nhận», cùng gốc <b>принима́ть</b> · <b>приня́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ный</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đọc thẳng các mảnh là ra nghĩa: «đón-nhận-khách». Chữ <b>-е-</b> ở '
    'giữa chỉ là mối nối, không mang nghĩa gì.</div>'
    '<div class="hd-warn">Dùng cho cả người lẫn nơi chốn: <b>гостеприи́мный хозя́ин</b> chủ nhà '
    'hiếu khách, <b>гостеприи́мный дом</b> ngôi nhà mến khách.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гость</b> khách · <b>гости́ница</b> khách sạn · '
    '<b>гостеприи́мство</b> lòng hiếu khách · <b>принима́ть</b> đón tiếp, nhận</div>'
)

# --------------------------------------------------------------- приятный
S["приятный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">tiền tố: về phía mình</span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́т-</span>'
    '<span class="hd-gloss">gốc «lấy, nhận», như <b>приня́ть</b> · <b>взять</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ный</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái gì mình ĐÓN NHẬN được về phía mình thì dễ chịu, vừa lòng. Cũng gốc '
    'ấy cho <b>прия́тель</b> «bạn bè» và cho <b>гостеприи́мный</b> «hiếu khách».</div>'
    '<div class="hd-warn">Dạng ngắn giống trung <b>прия́тно</b> là câu làm quen phải thuộc: '
    '<b>О́чень прия́тно!</b> «Rất hân hạnh». Riêng giống đực chèn thêm <b>е</b>: '
    '<b>прия́тен</b>.</div>'
    '<div class="hd-warn">Chúc ăn ngon là <b>Прия́тного аппети́та!</b> — đứng ở cách 2 vì đó là '
    'lời chúc rút gọn của <b>жела́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>прия́тно</b> dễ chịu, thấy vui · <b>прия́тель</b> bạn bè · '
    '<b>приня́ть</b> nhận, tiếp nhận · <b>неприя́тный</b> khó chịu</div>'
)

# ----------------------------------------------------------------- весело
S["весело"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">весел-</span>'
    '<span class="hd-gloss">gốc «vui» của <b>весёлый</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bỏ đuôi tính từ, thêm <b>-о</b> là ra trạng từ. Chữ <b>ё</b> hoá '
    '<b>е</b> vì trọng âm bỏ nó mà đi: trong tiếng Nga <b>ё</b> LUÔN mang trọng âm, nên hễ '
    'trọng âm dời chỗ thì nó phải thành <b>е</b> — <b>весёлый</b> → <b>ве́село</b>.</div>'
    '<div class="hd-warn">Nó còn làm vị ngữ vô nhân xưng, người vui đứng ở cách 3: '
    '<b>Мне ве́село</b> = Tôi thấy vui. Câu không có chủ ngữ, cùng khuôn <b>Мне хорошо́</b>.'
    '</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>весёлый</b> vui vẻ · <b>весе́лье</b> niềm vui, cuộc vui · '
    '<b>весели́ться</b> vui chơi, đùa vui</div>'
)

# ============================================================ field Vietnamese
# Chỉ sửa dòng thật sự hỏng: va chạm nghĩa mà badge không tách nổi, ngoặc chú
# thích (README §2c cấm), hoặc dòng chưa dịch sang tiếng Việt.
V = {
    # va chạm THẬT với хотеть (cùng v + IMPF, badge không tách): bỏ "muốn",
    # giữ hai nghĩa riêng của желать là "mong muốn" và "chúc"
    "желать": "mong muốn, chúc",
    # dòng cũ là NGUYÊN VĂN TIẾNG ANH ("nice, pleasant, pleasing, agreeable"),
    # không dùng làm đề bài gõ tiếng Nga được
    "приятный": "dễ chịu, dễ mến, vừa ý",
    # bỏ ngoặc chú thích, tách thành hai nghĩa song song
    "тост": "bánh mì nướng, lời chúc rượu",
    # bỏ ngoặc "(quà)"
    "дарить": "tặng, biếu, ban tặng",
}
