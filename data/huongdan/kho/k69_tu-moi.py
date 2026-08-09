# -*- coding: utf-8 -*-
"""k69 — tu-moi: 14 từ user vừa thêm 09/08, KHÔNG cùng họ nhau.

Nửa đầu của 28 từ mới: người (nghề nghiệp + gia đình) và khái niệm trừu tượng.
Không có trục chung ⇒ cố ý KHÔNG có khối hệ thống dùng chung: mỗi thẻ chỉ nói
đúng phần của chính từ đó. Hai chỗ chạm nhau (дире́ктор và о́тпуск cùng lấy số
nhiều -а́ nhấn cuối) được nối bằng đúng một dòng dẫn chiếu, không dựng bảng chung.
"""

# 🔴 KHÔNG dựng biến khối dùng chung (HE/LUAT/THE…) rồi cộng vào mọi thẻ.

S = {}
V = {}

# ------------------------------------------------------------------- актёр
S["актёр"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">акт-</span>'
    '<span class="hd-gloss">gốc Latin <i>actus</i> — HÀNH ĐỘNG, MÀN DIỄN; cùng ổ '
    'với <i>act</i>, <i>action</i> tiếng Anh</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ёр</span>'
    '<span class="hd-gloss">hậu tố NGƯỜI LÀM NGHỀ ĐÓ, mượn từ <i>-eur</i> tiếng Pháp</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ghép thẳng: người thực hiện hành động trên sân khấu. Cùng '
    'khuôn <b>-ёр</b> user đã có <b>шофёр</b> tài xế, và <b>режиссёр</b> đạo diễn — '
    'cả ba đều là nghề mượn qua tiếng Pháp.</div>'
    '<div class="hd-warn">⚠️ Từ này không có dấu trọng âm vì <b>ё</b> tự nó luôn là '
    'âm được nhấn: trong một từ đơn, <b>ё</b> luôn kéo trọng âm về mình. Thấy '
    '<b>ё</b> là biết đọc nhấn ở đâu, khỏi cần dấu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>актри́са</b> nữ diễn viên · <b>акт</b> hồi kịch, hành vi</div>'
)

# -------------------------------------------------------------- ветерина́р
S["ветеринар"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được thành mảnh tiếng Nga: mượn nguyên khối từ '
    'Latin <i>veterinarius</i> "thuộc về gia súc thồ" (← <i>veterina</i> con vật kéo '
    'cày). Cùng nguồn với <i>veterinarian</i> tiếng Anh, nên nhớ qua tiếng Anh là nhanh nhất.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghề chữa bệnh cho THÚ, đặt cạnh <b>врач</b> chữa bệnh cho '
    'người. Đuôi <b>-а́р</b> ở đây là phần đuôi của từ Latin chứ không phải hậu tố '
    'Nga, nên đừng đi tìm nghĩa riêng cho nó.</div>'
    '<div class="hd-warn">⚠️ Đừng nối với <b>ве́тер</b> gió, <b>приве́т</b> chào, '
    '<b>отве́т</b> câu trả lời — cả ba chỉ trùng mặt chữ <b>вет</b> với từ này chứ '
    'không cùng gốc, nên không giúp đoán nghĩa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ветерина́рный</b> thuộc thú y · <b>ветерина́рия</b> ngành thú y</div>'
)

# -------------------------------------------------------------------- внук
S["внук"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn: <b>внук</b> là một khối Slav cổ, không tách được '
    'thành mảnh nào mang nghĩa riêng. Chỉ có một chỗ ghép được, là tiền tố ở dưới.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhớ theo bậc đời đã học: <b>де́душка</b> ông → <b>оте́ц</b> '
    'cha → <b>сын</b> con trai → <b>внук</b> cháu. Thêm tiền tố <b>пра-</b> là lùi '
    'thêm một đời nữa, đúng như <i>great-</i> tiếng Anh: <b>пра́внук</b> chắt.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вну́чка</b> cháu gái · <b>пра́внук</b> chắt</div>'
)

# --------------------------------------------------------------- дире́ктор
S["директор"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дирек-</span>'
    '<span class="hd-gloss">gốc Latin <i>dirigere</i> — CHỈ HƯỚNG, ĐIỀU KHIỂN; cùng '
    'ổ với <i>direct</i>, <i>direction</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-тор</span>'
    '<span class="hd-gloss">hậu tố NGƯỜI LÀM VIỆC ĐÓ, đúng bằng <i>-tor/-or</i> tiếng Anh</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">"Người chỉ hướng" ⇒ ai đứng đầu một chỗ đều gọi bằng từ '
    'này: giám đốc công ty, hiệu trưởng trường học.</div>'
    '<div class="hd-warn">⚠️ Số nhiều KHÔNG lấy <b>-ы</b> mà lấy <b>-а́</b> nhấn '
    'cuối, rồi trọng âm ở lại cuối suốt bảng: <b>директора́</b>, <b>директоро́в</b>, '
    '<b>директора́м</b>. Cùng lớp này có <b>профе́ссор</b> → <b>профессора́</b>, và '
    '<b>о́тпуск</b> trong lô này.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дире́кция</b> ban giám đốc, ban lãnh đạo</div>'
)

# --------------------------------------------------------------- культу́ра
S["культура"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">культ-</span>'
    '<span class="hd-gloss">gốc Latin <i>colere</i> — VUN TRỒNG, CHĂM SÓC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-у́ра</span>'
    '<span class="hd-gloss">đuôi danh từ trừu tượng mượn theo, đúng bằng <i>-ure</i> tiếng Anh</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc là "sự vun trồng đất" — vì thế tiếng Nga đến nay vẫn '
    'gọi cây trồng là <b>культу́ры</b>. Vun trồng con người thay vì vun trồng đất '
    'thì ra nghĩa dùng hằng ngày: văn hóa. Đuôi <b>-а</b> cho biết đây là danh từ '
    'giống cái, chia trọn theo mẫu chuẩn, trọng âm đứng yên suốt bảng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>культу́рный</b> có văn hóa, lịch sự · <b>физкульту́ра</b> thể dục '
    '(rút gọn từ <b>физи́ческая культу́ра</b>)</div>'
)

# ---------------------------------------------------------------- ма́льчик
S["мальчик"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ма́ль-</span>'
    '<span class="hd-gloss">gốc NHỎ — cùng gốc với <b>ма́ленький</b> nhỏ và <b>ма́ло</b> ít</span></div>'
    '<div class="hd-row"><span class="hd-piece">-чик</span>'
    '<span class="hd-gloss">hậu tố nhỏ, trìu mến ⇒ danh từ giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen là "người nhỏ" ⇒ cậu bé. Cặp đối của nó trong bộ là '
    '<b>де́вочка</b> bé gái — hai từ này luôn đi thành đôi. Trọng âm bám chặt gốc '
    '<b>ма́</b> suốt bảng, kể cả số nhiều <b>ма́льчики</b>.</div>'
    '<div class="hd-warn">⚠️ <b>ма́льчик</b> là bé trai bất kỳ, xét theo tuổi. Còn <b>сын</b> '
    'là con trai CỦA AI đó, xét theo quan hệ và không phụ thuộc tuổi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ма́ленький</b> nhỏ, bé · <b>малы́ш</b> bé, em bé · <b>ма́ло</b> ít</div>'
)

# ----------------------------------------------------------------- о́тпуск
S["отпуск"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о́т-</span>'
    '<span class="hd-gloss">tiền tố RỜI RA, TÁCH KHỎI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пуск</span>'
    '<span class="hd-gloss">gốc THẢ, BUÔNG (của <b>пусти́ть</b> thả ra)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen "sự thả cho rời đi" — được thả khỏi chỗ làm ⇒ nghỉ '
    'phép. Danh từ dựng bằng cách cắt trụi đuôi động từ, không thêm gì, nên trọng '
    'âm lùi hẳn về tiền tố: <b>о́тпуск</b>.</div>'
    '<div class="hd-warn">⚠️ Số nhiều lấy <b>-а́</b> nhấn cuối chứ không lấy <b>-и</b>: '
    '<b>отпуска́</b>, <b>отпуско́в</b> — cùng lớp với <b>дире́ктор</b> → <b>директора́</b> '
    'trong lô này.</div>'
    '<div class="hd-warn">⚠️ Ba từ dễ lẫn: <b>о́тпуск</b> là nghỉ phép của người ĐI LÀM, '
    '<b>выходно́й</b> là ngày nghỉ trong tuần, còn <b>отдыха́ть</b> là hành động nghỉ ngơi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пусти́ть</b> thả, cho vào · <b>отпусти́ть</b> thả ra, buông · '
    '<b>вы́пуск</b> đợt ra lò, khóa tốt nghiệp</div>'
)

# ----------------------------------------------------------------- оши́бка
S["ошибка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">tiền tố, ở đây mang sắc thái CHỆCH, TRƯỢT KHỎI ĐÍCH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ши́б-</span>'
    '<span class="hd-gloss">gốc VA, ĐÁNH (còn thấy ở <b>ушиби́ть</b> đánh bầm)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">hậu tố ⇒ danh từ giống cái, chỉ MỘT lần/MỘT cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen là "một cú đánh trượt" ⇒ chỗ sai, lỗi. Động từ cùng '
    'gốc là <b>ошиба́ться</b> nhầm, mắc lỗi. Cách 2 số nhiều chèn thêm một nguyên âm cho '
    'dễ đọc — <b>о</b> ở <b>оши́бок</b>, <b>е</b> ở <b>де́вочка</b> → <b>де́вочек</b>: '
    'chọn chữ nào là do phụ âm đứng trước quyết định.</div>'
    '<div class="hd-warn">⚠️ Phân vai với <b>вина́</b>: <b>оши́бка</b> là CHỖ SAI trong bài '
    'làm hay việc làm, đếm được từng cái; <b>вина́</b> là trách nhiệm, là việc ai '
    'là người có lỗi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ошиба́ться</b> nhầm, mắc lỗi · <b>оши́бочный</b> sai, nhầm lẫn</div>'
)

# --------------------------------------------------------------- писа́тель
S["писатель"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пис-</span>'
    '<span class="hd-gloss">gốc VIẾT (của <b>писа́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-</span>'
    '<span class="hd-gloss">nguyên âm thân của <b>писа́ть</b>, giữ nguyên khi ghép</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тель</span>'
    '<span class="hd-gloss">hậu tố NGƯỜI LÀM VIỆC ĐÓ, đúng bằng <i>-er</i> tiếng Anh</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cộng thẳng ba mảnh ra "người viết" ⇒ nhà văn. Hậu tố '
    '<b>-тель</b> mở khóa cả một lớp nghề đã học: <b>учи́тель</b> thầy giáo, '
    '<b>роди́тель</b> bố hoặc mẹ — gặp đuôi này là đoán được "người làm việc gì đó".</div>'
    '<div class="hd-warn">⚠️ Danh từ <b>-тель</b> luôn là giống ĐỰC, dù đuôi <b>-ь</b> '
    'trông y hệt giống cái. Đừng suy ra luật "đuôi mềm là giống cái": <b>день</b> và '
    '<b>слова́рь</b> cũng đuôi <b>-ь</b> mà đều giống đực.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>писа́ть</b> viết · <b>написа́ть</b> viết xong · <b>письмо́</b> bức thư · '
    '<b>пи́сьменно</b> bằng chữ viết · <b>запи́сывать</b> ghi chép</div>'
)

# --------------------------------------------------------------- поли́тика
S["политика"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">полит-</span>'
    '<span class="hd-gloss">gốc Hy Lạp <i>polis</i> thành bang ⇒ việc chung của nhà nước</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ика</span>'
    '<span class="hd-gloss">hậu tố NGÀNH, LĨNH VỰC — như <b>фи́зика</b> vật lý</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">"Việc của thành bang" ⇒ chính trị. Cùng một từ dùng luôn cho '
    'đường lối cụ thể của một bên nào đó ⇒ chính sách. Cặp <b>-ик</b> người / '
    '<b>-ика</b> ngành đã học lộ ra rõ ở đây: <b>поли́тик</b> là NGƯỜI làm chính trị, '
    '<b>поли́тика</b> là chính bản thân LĨNH VỰC đó.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поли́тик</b> nhà chính trị · <b>полити́ческий</b> thuộc về chính trị</div>'
)

# ------------------------------------------------------------------ посо́л
S["посол"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố, ở đây đánh dấu một lần gửi trọn vẹn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-со́л- / -сл-</span>'
    '<span class="hd-gloss">gốc GỬI ĐI (của <b>посла́ть</b> gửi)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen là "người được gửi đi" ⇒ sứ giả, đại sứ. Nơi làm '
    'việc của người ấy dựng từ đúng gốc ấy: <b>посо́льство</b> đại sứ quán.</div>'
    '<div class="hd-warn">⚠️ Chữ <b>о</b> trong <b>посо́л</b> là nguyên âm CHẠY: vừa thêm '
    'đuôi là nó biến mất, để lộ gốc thật <b>сл</b> — <b>посла́</b>, <b>послу́</b>, '
    '<b>посло́м</b>, <b>посло́в</b>. Chính dạng <b>посла́</b> cho thấy họ hàng với '
    '<b>посла́ть</b>, còn dạng <b>посо́л</b> thì giấu mất.</div>'
    '<div class="hd-warn">⚠️ Từ điển gộp thêm nghĩa "sự ướp muối" vào mục này. Đó là '
    'một từ ĐỒNG TỰ khác hẳn, dựng từ <b>соль</b> muối; nghĩa đại sứ không dính gì '
    'tới muối, và hai từ chia khác nhau.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>посо́льство</b> đại sứ quán · <b>посла́ть</b> gửi đi</div>'
)

# --------------------------------------------------------------- пробле́ма
S["проблема"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">tiền tố Hy Lạp — RA PHÍA TRƯỚC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бле́м-</span>'
    '<span class="hd-gloss">gốc Hy Lạp <i>ballein</i> — NÉM</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi ⇒ danh từ giống cái, chia trọn theo mẫu chuẩn</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen "cái được ném ra trước mặt" ⇒ chuyện bày ra chắn '
    'đường, phải giải quyết. Cùng ổ với <i>problem</i> tiếng Anh nên chỉ cần nhớ '
    'trọng âm rơi vào <b>-бле́-</b>.</div>'
    '<div class="hd-warn">⚠️ <b>про-</b> ở đây nằm sẵn trong từ mượn, KHÔNG phải tiền tố '
    'Nga <b>про-</b> (xuyên qua, làm suốt). Tách nó ra rồi đi tra phần còn lại là '
    'không ra gì.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пробле́мный</b> rắc rối, có vấn đề</div>'
)

# ----------------------------------------------------------------- сто́ить
S["стоить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сто́-</span>'
    '<span class="hd-gloss">gốc ĐỨNG — xem ô mức tin bên dưới</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2 ⇒ <b>сто́ю</b>, <b>сто́ишь</b>, <b>сто́ит</b>, <b>сто́ят</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giá của một món là con số mà nó "đứng ở đó". Tiếng Anh đi đúng '
    'đường ấy: <i>cost</i> ← Latin <i>constare</i> "đứng cùng". Từ nghĩa giá tiền mọc '
    'ra nghĩa thứ hai dùng rất nhiều: <b>сто́ит</b> + động từ nguyên thể = "đáng làm, '
    'nên làm".</div>'
    '<div class="hd-warn">⚠️ Mức tin: việc nối <b>сто́ить</b> với <b>стоя́ть</b> đứng là '
    'từ nguyên, không phải luật suy ra được. Dùng nó để nhớ nghĩa thì tốt, đừng dùng '
    'để đoán cách chia.</div>'
    '<div class="hd-warn">⚠️ Hai từ này có dạng TRÙNG HẲN mặt chữ, chỉ khác chỗ nhấn: '
    '<b>сто́ю</b> tôi có giá ↔ <b>стою́</b> tôi đang đứng; <b>сто́ит</b> nó có giá ↔ '
    '<b>стои́т</b> nó đang đứng. Bỏ dấu trọng âm ra là hai dạng trùng khít, '
    'phải dựa vào cả câu mới biết là từ nào.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сто́имость</b> giá trị, chi phí</div>'
)

# ----------------------------------------------------------------- тури́ст
S["турист"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">тур-</span>'
    '<span class="hd-gloss">gốc CHUYẾN ĐI MỘT VÒNG, mượn từ Pháp <i>tour</i>; cùng ổ '
    'với <i>tour</i>, <i>turn</i> tiếng Anh</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ст</span>'
    '<span class="hd-gloss">hậu tố NGƯỜI THEO NGHỀ/CHỦ TRƯƠNG ĐÓ, luôn mang trọng âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">"Người đi một vòng" ⇒ khách du lịch. Cùng khuôn <b>-и́ст</b> '
    'user đã có <b>журнали́ст</b> nhà báo — đuôi này bám vào đâu là ra người làm việc đó.</div>'
    '<div class="hd-warn">⚠️ Cặp hậu tố đi liền nhau, học một lần dùng cả đời: '
    '<b>-и́ст</b> là NGƯỜI, <b>-и́зм</b> là ngành hay chủ nghĩa. <b>тури́ст</b> khách '
    'du lịch ↔ <b>тури́зм</b> ngành du lịch, y như <b>оптими́ст</b> ↔ <b>оптими́зм</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тури́зм</b> du lịch, ngành du lịch · <b>туристи́ческий</b> thuộc về du lịch</div>'
)

# ==================================================================== FIELD VIỆT
# Chỉ hai từ cần sửa; 12 từ còn lại dòng cũ đã là thuần danh sách nghĩa, khớp
# gloss tiếng Anh và khớp khuôn của họ hàng cùng tag ⇒ để nguyên (QD-27).
# внук: dòng cũ dùng dấu gạch chéo "cháu nội/ngoại"; khuôn nhà của cùng tag
#   people::family là dấu phẩy (де́душка "ông, ông nội, ông ngoại") ⇒ tách ra.
# ошибка: gloss Anh là "mistake"; thêm "sự nhầm lẫn" cho đủ nhánh nghĩa đó —
#   liệt kê đủ thì tự tách khỏi вина́ (trách nhiệm, ai có lỗi).
V["внук"] = "cháu trai, cháu nội, cháu ngoại"
V["ошибка"] = "lỗi, sai lầm, sự nhầm lẫn"
