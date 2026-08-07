# -*- coding: utf-8 -*-
"""k12 — language::grammar: bộ khung câu tiếng Nga.

Hư từ nối câu (и · а · да · не), hai giới từ trục в/на, cặp hỏi где/куда,
cặp hướng вперёд/наза́д, đại từ она́/они́, và một thuật ngữ ngữ pháp mượn
(императи́в). Trục xuyên suốt: VỊ TRÍ đứng yên khác HƯỚNG có chuyển động.
"""

S = {}
V = {}

S["а"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">а</span>'
    '<span class="hd-gloss">CÒN, MÀ — một chữ cái, không chẻ nhỏ hơn được</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiếng Nga chia việc cho ba liên từ: <b>и</b> cộng dồn hai thứ '
    'cùng chiều, <b>а</b> đặt hai vế song song để SO SÁNH, <b>но</b> mới là chống lại. '
    '<i>Я студе́нт, а он врач</i> — tôi là sinh viên, còn anh ấy là bác sĩ; hai vế khác '
    'nhau chứ không ai phản đối ai.</div>'
    '<div class="hd-warn"><b>а</b> mở đầu câu hỏi ngắn để hất sang người khác: '
    '<i>А ты?</i> = "Còn bạn thì sao?".</div>'
)

S["да"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">да</span>'
    '<span class="hd-gloss">VÂNG — hư từ hai chữ cái, không chẻ được</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một chữ dùng cho mọi mức lịch sự: tiếng Việt phải chọn giữa '
    '"vâng / ừ / dạ" tuỳ người nghe, tiếng Nga chỉ có <b>да</b>. Muốn lịch sự thì thêm '
    'lời chứ không đổi từ: <i>да, коне́чно</i> = vâng, tất nhiên.</div>'
    '<div class="hd-warn">Từ điển còn ghi <b>да</b> nghĩa "và / nhưng" — đó là tiếng Nga '
    'cổ và khẩu ngữ dân dã, chỉ còn sống trong ít cụm cố định (<i>жил да был</i> = ngày '
    'xửa ngày xưa). Mặc định hằng ngày vẫn là <b>и</b> và <b>но</b>.</div>'
)

S["куда"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ку-</span>'
    '<span class="hd-gloss">thân từ để hỏi, cùng ổ với <b>кто</b>, <b>како́й</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-да</span>'
    '<span class="hd-gloss">mảnh chỉ HƯỚNG — lặp lại ở <b>сюда́</b>, <b>туда́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp nền của cả lô: <b>где</b> hỏi chỗ ĐỨNG YÊN, <b>куда́</b> hỏi '
    'chỗ ĐI TỚI. <i>Где ты?</i> = bạn đang ở đâu; <i>Куда́ ты идёшь?</i> = bạn đi đâu. '
    'Sai cặp này là câu hỏi hỏng nghĩa chứ không phải lỗi nhỏ.</div>'
    '<div class="hd-warn">Phủ định phải đi ĐÔI: <b>никуда́</b> luôn kéo theo <b>не</b> — '
    '<i>Я никуда́ не иду́</i> = tôi chẳng đi đâu cả.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сюда́</b> tới đây · <b>туда́</b> tới đó · <b>отку́да</b> từ đâu '
    'tới · <b>никуда́</b> chẳng đi đâu</div>'
)

S["пока"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пока́</span>'
    '<span class="hd-gloss">hư từ liền khối — <b>по-</b> ở đây không còn nghĩa riêng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một chữ ba việc, đều xoay quanh ý "chừng nào còn": '
    '<i>Пока́!</i> = tạm biệt · <i>Пока́ я чита́л…</i> = trong khi tôi đọc · '
    '<i>Пока́ всё хорошо́</i> = tạm thời mọi thứ đều ổn.</div>'
    '<div class="hd-warn"><b>пока́ не</b> = "cho đến khi". Tiếng Nga giữ chữ <b>не</b> mà '
    'tiếng Việt KHÔNG dịch: <i>Жди, пока́ я не приду́</i> = đợi cho đến khi tôi đến '
    '(không phải "cho đến khi tôi không đến").</div>'
    '<div class="hd-warn"><b>Пока́!</b> chỉ chào bạn bè ngang hàng. Với người lớn tuổi '
    'hoặc người lạ phải dùng <b>до свида́ния</b>.</div>'
)

S["на"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на</span>'
    '<span class="hd-gloss">MẶT TRÊN — giới từ một âm, không chẻ được</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hình ảnh gốc là BỀ MẶT, đối lập với <b>в</b> (bên trong). Cùng một '
    'giới từ nhưng hai cách, và chính cái cách nói lên đứng yên hay chuyển động: '
    '<i>на столе́</i> (cách 6) = đang ở trên bàn · <i>на стол</i> (cách 4) = đặt lên bàn.</div>'
    '<div class="hd-warn">Một nhóm danh từ bắt buộc dùng <b>на</b> dù tiếng Việt nói "ở '
    'trong": <i>на рабо́те</i> ở chỗ làm · <i>на у́лице</i> ngoài phố · <i>на уро́ке</i> '
    'trong giờ học · <i>на вокза́ле</i> ở ga. Không suy ra được, phải thuộc.</div>'
    '<div class="hd-warn"><b>на са́мом де́ле</b> = thật ra, thực chất — cụm dùng hằng ngày, '
    'nghĩa đen là "trên chính sự việc".</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">Dính vào danh từ chỉ phía là thành trạng từ chỉ hướng: '
    '<b>наза́д</b> lùi lại · <b>наве́рх</b> lên trên · <b>нале́во</b> sang trái</div>'
)

S["она"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">он-</span>'
    '<span class="hd-gloss">thân của đại từ ngôi ba</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi giống CÁI, đúng đuôi <b>-а</b> của danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng một thân <b>он-</b>, chỉ thay đuôi là ra cả bộ: <b>он</b> / '
    '<b>она́</b> / <b>оно́</b> / <b>они́</b>. Và <b>она́</b> thay cho MỌI danh từ giống cái, '
    'kể cả đồ vật — <i>кни́га… она́ на столе́</i> = quyển sách… nó ở trên bàn.</div>'
    '<div class="hd-warn">Sau giới từ mọc thêm chữ <b>н</b>: <i>у неё</i>, <i>с ней</i>, '
    '<i>о ней</i>. Nhưng khi <b>её</b> là sở hữu "của cô ấy" thì KHÔNG có <b>н</b>: '
    '<i>её кни́га</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>он</b> anh ấy · <b>оно́</b> nó (giống trung) · <b>они́</b> họ · '
    '<b>её</b> của cô ấy</div>'
)

S["пожалуйста"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-жа́л-</span>'
    '<span class="hd-gloss">gốc <b>жал-</b> THƯƠNG XÓT, BAN ƠN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-уйста</span>'
    '<span class="hd-gloss">đuôi cổ đã đông cứng, nay không đứng riêng được</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc <b>жал-</b> với <b>сожале́ние</b> (sự tiếc nuối) và '
    '<b>жа́лость</b> (lòng thương). Nghĩa đen là "xin ngài ban ơn cho" — nói "làm ơn" bằng '
    'cách xin lòng thương.</div>'
    '<div class="hd-warn">⚠️ Mức tin: chỗ chẻ <b>-уйста</b> là từ nguyên còn tranh cãi, '
    'không phải luật suy ra được. Phần chắc chắn là gốc <b>жал-</b>.</div>'
    '<div class="hd-warn">Một chữ đi cả hai chiều: xin việc gì thì <b>пожа́луйста</b> = '
    '"làm ơn"; ai cảm ơn mình thì đáp lại cũng bằng <b>пожа́луйста</b> = "không có chi".</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>жа́лость</b> lòng thương · <b>сожале́ние</b> sự tiếc nuối · '
    '<b>жа́ловаться</b> than phiền · <b>пожа́луй</b> có lẽ</div>'
)

S["в"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в</span>'
    '<span class="hd-gloss">BÊN TRONG — một chữ cái, không chẻ được</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hình ảnh gốc là LÒNG TRONG, đối lập với <b>на</b> (mặt trên). '
    'Vẫn một giới từ, vẫn hai cách như <b>на</b>: <i>в шко́ле</i> (cách 6) = đang ở trong '
    'trường · <i>в шко́лу</i> (cách 4) = đi vào trường.</div>'
    '<div class="hd-warn">Trước cụm phụ âm khó đọc, <b>в</b> phình ra thành <b>во</b>: '
    '<i>во Фра́нции</i>, <i>во вто́рник</i>, <i>во сне</i>. Chỉ là chuyện dễ đọc, nghĩa '
    'không đổi.</div>'
    '<div class="hd-warn">Chỉ thời gian thì cách nhảy theo độ dài: thứ trong tuần đi cách 4 '
    '(<i>в понеде́льник</i>), còn tháng đi cách 6 (<i>в январе́</i>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">Làm tiền tố nghĩa "vào trong": <b>входи́ть</b> đi vào · '
    '<b>вход</b> lối vào · <b>вложи́ть</b> đặt vào trong</div>'
)

S["императив"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">императ-</span>'
    '<span class="hd-gloss">Latin <i>imperare</i> RA LỆNH, CẦM QUYỀN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́в</span>'
    '<span class="hd-gloss">đuôi mượn <i>-ivus</i>, dấu hiệu từ quốc tế</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng ổ với tiếng Anh <i>imperative</i> và <i>emperor</i>: gốc '
    '"ra lệnh" cho ra <b>импера́тор</b> (người ra lệnh) và <b>императи́в</b> (lời ra lệnh). '
    'Đuôi <b>-и́в</b> là dấu hiệu từ mượn quốc tế: hễ thấy nó thì đó là danh từ giống '
    'đực, biến cách bình thường.</div>'
    '<div class="hd-warn">Đây là thuật ngữ ngữ pháp: dạng sai khiến của động từ '
    '(<i>чита́й!</i> đọc đi). Sách giáo khoa Nga thường gọi bằng tên thuần Nga '
    '<b>повели́тельное наклоне́ние</b> — gặp hai chữ đó là cùng một thứ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">Cùng gốc: <b>импера́тор</b> hoàng đế · <b>импе́рия</b> đế quốc. '
    'Chỉ cùng đuôi <b>-и́в</b>: <b>акти́в</b>, <b>моти́в</b>, <b>объекти́в</b></div>'
)

S["назад"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">giới từ <b>на</b> dính liền, chỉ hướng nhắm tới</span></div>'
    '<div class="hd-row"><span class="hd-piece">-за́д</span>'
    '<span class="hd-gloss">danh từ <b>зад</b> PHÍA SAU, PHẦN ĐUÔI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen ghép thẳng từ hai mảnh: "về phía sau". Từ đó ra ba việc '
    'quen thuộc: <i>шаг наза́д</i> = một bước lùi · <i>верни́сь наза́д</i> = quay lại đi · '
    '<i>два го́да наза́д</i> = cách đây hai năm.</div>'
    '<div class="hd-warn"><b>наза́д</b> luôn có CHUYỂN ĐỘNG. Muốn nói đứng yên "ở phía sau" '
    'thì phải đổi từ, dùng <b>сза́ди</b> — đúng cặp <b>куда́</b> / <b>где</b> của lô này.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>зад</b> phần đuôi, mặt sau · <b>за́дний</b> ở đằng sau · '
    '<b>сза́ди</b> từ phía sau, ở phía sau</div>'
)

S["вперёд"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">giới từ <b>в</b> dính liền, chỉ hướng nhắm tới</span></div>'
    '<div class="hd-row"><span class="hd-piece">-перёд</span>'
    '<span class="hd-gloss">PHÍA TRƯỚC — cùng gốc với giới từ <b>пе́ред</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Sinh đôi đối xứng với <b>наза́д</b>: cả hai đều là giới từ dán vào '
    'một danh từ chỉ phía rồi đông cứng thành trạng từ chỉ hướng. Chữ <b>ё</b> luôn mang '
    'trọng âm, nên <b>вперёд</b> không bao giờ cần dấu sắc.</div>'
    '<div class="hd-warn">Vẫn luật đứng yên / chuyển động: <b>вперёд</b> là đi tới trước, '
    'còn "ở phía trước" đứng yên là <b>впереди́</b>. Cặp này khớp đúng với '
    '<b>наза́д</b> / <b>сза́ди</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пе́ред</b> trước · <b>пере́дний</b> ở phía trước · '
    '<b>впереди́</b> đằng trước</div>'
)

S["где"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">г-</span>'
    '<span class="hd-gloss">thân từ để hỏi, cùng ổ với <b>к-</b> của <b>кто</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-де</span>'
    '<span class="hd-gloss">mảnh chỉ NƠI CHỐN — lặp ở <b>везде́</b>, <b>нигде́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đối trọng của <b>куда́</b>: <b>где</b> hỏi chỗ ĐỨNG YÊN nên câu '
    'trả lời để cách 6, <b>куда́</b> hỏi chỗ ĐI TỚI nên câu trả lời để cách 4. Còn '
    '<b>отку́да</b> = từ đâu ra.</div>'
    '<div class="hd-warn"><b>где</b> không chỉ để hỏi — nó còn nối hai vế câu thành "nơi mà": '
    '<i>дом, где я живу́</i> = ngôi nhà nơi tôi sống. Không có dấu hỏi nào ở đây cả.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>везде́</b> khắp nơi · <b>нигде́</b> chẳng đâu · '
    '<b>где́-то</b> ở đâu đó</div>'
)

S["тоже"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">то</span>'
    '<span class="hd-gloss">CÁI ĐÓ — đại từ chỉ định</span></div>'
    '<div class="hd-row"><span class="hd-piece">-же</span>'
    '<span class="hd-gloss">tiểu từ nhấn CHÍNH, ĐÚNG CÁI ĐÓ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen suy thẳng từ hai mảnh: "cũng chính cái đó". '
    '<i>Я то́же студе́нт</i> = tôi cũng là sinh viên — người thì khác, việc thì y hệt.</div>'
    '<div class="hd-warn">Viết LIỀN <b>то́же</b> = "cũng". Viết RỜI <b>то же</b> = "cái đó" '
    '(<i>то же са́мое</i> = chính cái đó). Một dấu cách đổi hẳn nghĩa.</div>'
    '<div class="hd-warn">Đừng lẫn với <b>ещё</b>. <b>то́же</b> thêm NGƯỜI hay VIỆC cùng '
    'loại; <b>ещё</b> thêm SỐ LƯỢNG: <i>Я то́же хочу́</i> = tôi cũng muốn, còn '
    '<i>Дай ещё</i> = cho thêm nữa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>та́кже</b> ngoài ra, hơn nữa · <b>тот</b> cái kia · '
    '<b>то</b> cái đó</div>'
)

S["не"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не</span>'
    '<span class="hd-gloss">KHÔNG — tiểu từ hai chữ cái, không chẻ được</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>не</b> phủ định đúng cái từ đứng NGAY SAU nó, nên đổi chỗ là đổi '
    'nghĩa: <i>Я не чита́л</i> = tôi không đọc, còn <i>Не я чита́л</i> = không phải tôi đọc '
    '(người khác đọc). Nó không mang trọng âm, đọc dính vào từ sau.</div>'
    '<div class="hd-warn"><b>не</b> khác <b>нет</b>. <b>не</b> luôn bám vào một từ khác '
    '(<i>не зна́ю</i>); <b>нет</b> đứng một mình để trả lời, hoặc nghĩa "không có" và kéo '
    'theo cách 2: <i>у меня́ нет вре́мени</i>.</div>'
    '<div class="hd-warn">Tiếng Nga bắt buộc PHỦ ĐỊNH KÉP: đã có <b>ничего́</b>, '
    '<b>никто́</b>, <b>никогда́</b> thì vẫn phải giữ <b>не</b> — <i>Я ничего́ не зна́ю</i> = '
    'tôi chẳng biết gì cả.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>нет</b> không, không có · <b>нельзя́</b> không được phép · '
    '<b>неве́рно</b> không đúng</div>'
)

S["все"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вс-</span>'
    '<span class="hd-gloss">gốc TOÀN BỘ, dạng đầy đủ là <b>весь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е</span>'
    '<span class="hd-gloss">đuôi SỐ NHIỀU</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một gốc, bốn dạng theo giống và số: <b>весь</b> (đực) / '
    '<b>вся</b> (cái) / <b>всё</b> (trung) / <b>все</b> (số nhiều). Đứng một mình không kèm '
    'danh từ thì <b>все</b> mặc định được hiểu là người, nên tự nó đã có nghĩa "mọi người".</div>'
    '<div class="hd-warn">🔴 Một dấu hai chấm đổi hẳn nghĩa: <b>все</b> (chữ <b>е</b>) = mọi '
    'NGƯỜI, <i>все зна́ют</i> = ai cũng biết. <b>всё</b> (chữ <b>ё</b>) = mọi THỨ, '
    '<i>всё гото́во</i> = mọi thứ đã xong.</div>'
    '<div class="hd-warn"><b>весь</b> là dạng SỐ ÍT nên chỉ bám vào danh từ số ít '
    '(<i>весь день</i> = cả ngày), còn <b>все</b> là số nhiều của chính nó và '
    'đứng một mình đã đủ nghĩa: <i>все пришли́</i> = mọi người đã đến.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>весь</b> cả, toàn bộ · <b>всё</b> mọi thứ · <b>всегда́</b> luôn '
    'luôn · <b>вся́кий</b> mọi loại</div>'
)

S["и"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">и</span>'
    '<span class="hd-gloss">VÀ — một chữ cái, không chẻ nhỏ hơn được</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Liên từ CỘNG DỒN: hai thứ cùng chiều, không đối nhau. So với hai '
    'liên từ kia của lô: <b>и</b> cộng thêm, <b>а</b> đặt song song để so sánh, <b>но</b> '
    'chống lại. <i>брат и сестра́</i> = anh trai và chị gái.</div>'
    '<div class="hd-warn">Nhân đôi thành <b>и… и…</b> là "cả… lẫn…": '
    '<i>и брат, и сестра́</i> = cả anh trai lẫn chị gái.</div>'
    '<div class="hd-warn">Đứng ngay trước một từ, <b>и</b> thôi làm liên từ mà thành tiểu từ '
    'nhấn "ngay cả": <i>И он пришёл</i> = ngay cả anh ấy cũng đến.</div>'
)

S["они"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">он-</span>'
    '<span class="hd-gloss">thân của đại từ ngôi ba</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и</span>'
    '<span class="hd-gloss">đuôi SỐ NHIỀU, cùng bộ <b>-ы/-и</b> của danh từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vẫn thân <b>он-</b> như <b>она́</b>, chỉ đổi đuôi sang số nhiều. '
    'Số nhiều thì không phân biệt giống nữa, nên <b>они́</b> dùng chung cho người lẫn vật: '
    '<i>кни́ги… они́ здесь</i> = mấy quyển sách… chúng ở đây.</div>'
    '<div class="hd-warn">Luật mọc chữ <b>н</b> sau giới từ giống hệt <b>она́</b>: '
    '<i>у них</i>, <i>с ни́ми</i>, <i>о них</i> — nhưng sở hữu "của họ" thì trần, '
    '<i>их дом</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>он</b> anh ấy · <b>она́</b> cô ấy · <b>оно́</b> nó · '
    '<b>их</b> của họ</div>'
)

# --- Field Vietnamese (đề bài deck 1-go). Chỉ những từ THẬT SỰ cần sửa. ---
V["а"] = "còn, mà"                              # bỏ "nhưng": trùng но(nhưng) + да
V["да"] = "vâng, đúng vậy, ừ"                   # bỏ "nhưng": khẩu ngữ hiếm, không thông dụng
V["на"] = "trên, ở trên, lên"                   # bỏ "vào"(trùng в, по) và "tới"(trùng к)
V["в"] = "trong, ở trong, vào"                  # bỏ "ở" trần: quá gần у(ở chỗ), на(ở)
V["пока"] = "tạm biệt, trong khi, tạm thời, cho đến khi"   # thêm "for now / so far"
V["она"] = "cô ấy, bà ấy, nó"                   # thêm "nó" cho khớp он; она thay mọi dt giống cái
V["они"] = "họ, chúng nó"                       # bỏ "chúng" trần: nuốt vào мы(chúng tôi/ta)
V["императив"] = "thức mệnh lệnh, dạng mệnh lệnh"          # императив là DẠNG, không phải câu
V["назад"] = "về phía sau, lùi lại, quay lại, cách đây"    # trả lại nghĩa không gian gốc
V["вперёд"] = "về phía trước, tiến lên"         # bỏ mục lặp "tiến về phía trước"
V["тоже"] = "cũng, cũng vậy"                    # bỏ "nữa": đó là nghĩa của ещё
V["не"] = "không, chẳng"                        # tách khỏi нет(không, không có, không tồn tại)
V["все"] = "mọi người, ai nấy"                  # bỏ "mọi thứ"(=всё); "tất cả" thuộc всё/весь
V["и"] = "và, ngay cả"                          # bỏ "cũng"(trùng тоже) và "chính là"(không có)
