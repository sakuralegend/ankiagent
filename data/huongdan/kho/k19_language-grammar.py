# -*- coding: utf-8 -*-
"""k19 — language-grammar: bộ hư từ đời thường — cặp tồn tại есть/нет, bộ ba
khả năng мочь/можно/нельзя (hai từ sau là vị ngữ VÔ NHÂN XƯNG, người đi cách 3),
và các trạng từ đông cứng từ dạng biến cách (рядом, прямо, конечно, немного)."""

S = {}
V = {}

# ------------------------------------------------------- cặp tồn tại: есть / нет

S["есть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — nhưng phải tách HAI từ trùng hệt mặt chữ: '
    '<b>есть</b>¹ là nguyên thể «ăn», <b>есть</b>² là mảnh còn sót của <b>быть</b> '
    '«là», nay mang nghĩa «có, tồn tại».</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>есть</b>² vốn là ngôi «nó» của <b>быть</b>, nhưng tiếng Nga '
    'đã bỏ hết các ngôi khác nên nó dùng chung cho mọi ngôi và KHÔNG chia: '
    '<b>у меня́ есть</b>, <b>у них есть</b> đều một mặt chữ.</div>'
    '<div class="hd-warn">⚠️ Cặp phải thuộc: có thì <b>у меня́ есть</b> + cách 1, không có '
    'thì đổi hẳn sang <b>нет</b> + cách 2 — <b>у меня́ нет вре́мени</b>.</div>'
    '<div class="hd-warn">⚠️ Bảng chia bên dưới là của <b>есть</b>¹ «ăn», và thân từ đổi '
    'hẳn giữa chừng: <b>ем · ешь · ест</b> nhưng số nhiều <b>еди́м · еди́те · едя́т</b> mọc '
    'thêm chữ д. Quá khứ cũng ngắn bất ngờ: <b>ел · е́ла</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>еда́</b> thức ăn · <b>съесть</b> ăn hết (một lần rồi xong) · '
    '<b>обе́д</b> bữa trưa (об- quanh + gốc ед «ăn»)</div>'
)

S["нет"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не-</span>'
    '<span class="hd-gloss">KHÔNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-т</span>'
    '<span class="hd-gloss">mảnh mòn của <b>есть</b> «có»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen là «không-có» — chính vì thế một chữ <b>нет</b> vừa làm '
    'câu trả lời «không», vừa làm vị ngữ «không tồn tại». Nó đúng là <b>есть</b> bị phủ '
    'định, nên hai từ luôn đi thành cặp trong đầu.</div>'
    '<div class="hd-warn">⚠️ Sau <b>нет</b> danh từ BẮT BUỘC sang cách 2: '
    '<b>нет вре́мени</b>, <b>нет де́нег</b>. Người Việt hay để nguyên cách 1 ở đây.</div>'
    '<div class="hd-warn">⚠️ Khác <b>не</b>: <b>не</b> phải dính vào từ đứng ngay sau nó '
    '(<b>не зна́ю</b>), còn <b>нет</b> đứng được một mình cả câu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>не</b> không (phủ định từ đứng sau) · <b>не́ту</b> dạng khẩu '
    'ngữ của «không có»</div>'
)

# --------------------------------------------- bộ ba khả năng: мочь / можно / нельзя

S["мочь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мог-/мож-</span>'
    '<span class="hd-gloss">gốc «có sức, có khả năng»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-чь</span>'
    '<span class="hd-gloss">đuôi nguyên thể của nhóm gốc tận cùng г/к</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi <b>-чь</b> thay cho <b>-ть</b> mở khoá cả một nhóm nhỏ mà '
    'gốc kết thúc bằng г/к: <b>мочь · печь · бере́чь · лечь</b>. Cùng gốc với '
    '<b>по́мощь</b> «sự giúp đỡ» — giúp tức là cho thêm sức.</div>'
    '<div class="hd-warn">⚠️ Chú ý bảng chia: г đổi thành ж ở BỐN ngôi giữa '
    '(<b>мо́жешь · мо́жет · мо́жем · мо́жете</b>), còn hai đầu giữ г — <b>могу́ · мо́гут</b>. '
    'Chỉ mỗi ngôi «tôi» kéo trọng âm ra đuôi.</div>'
    '<div class="hd-warn">⚠️ Bảng in <b>моги́</b> và <b>бу́ду мочь</b>, nhưng người Nga không '
    'nói vậy: từ này gần như không có mệnh lệnh, và «tôi sẽ có thể» dùng thể hoàn thành '
    '<b>смогу́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>смочь</b> có thể (một lần rồi xong) · <b>возмо́жность</b> khả '
    'năng · <b>по́мощь</b> sự giúp đỡ</div>'
)

S["можно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мож-</span>'
    '<span class="hd-gloss">gốc «có thể» (đúng gốc của <b>мочь</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-но</span>'
    '<span class="hd-gloss">đuôi dựng vị ngữ nói trống</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Khác <b>мочь</b> ở chỗ câu KHÔNG có chủ ngữ: <b>мочь</b> cần một '
    'người ở cách 1 (<b>я могу́</b>), còn <b>мо́жно</b> nói trống, ai được phép thì đặt ở '
    'CÁCH 3 — <b>мне мо́жно</b> «tôi được phép». Hỏi xin phép chỉ cần một chữ: '
    '<b>Мо́жно?</b></div>'
    '<div class="hd-warn">⚠️ Phủ định của nó KHÔNG bao giờ là «не мо́жно» — tiếng Nga thay '
    'hẳn bằng một từ khác: <b>нельзя́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мочь</b> có thể · <b>возмо́жно</b> có lẽ · '
    '<b>невозмо́жно</b> không tài nào được</div>'
)

S["нельзя"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не-</span>'
    '<span class="hd-gloss">KHÔNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-льзя</span>'
    '<span class="hd-gloss">mảnh cổ nghĩa «được», nay không sống một mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dùng y hệt <b>мо́жно</b> nhưng ngược dấu: câu nói trống, người bị '
    'cấm đặt ở cách 3 — <b>мне нельзя́</b> «tôi không được phép».</div>'
    '<div class="hd-warn">⚠️ THỂ của động từ theo sau đổi hẳn nghĩa: chưa hoàn thành là '
    'CẤM (<b>здесь нельзя́ кури́ть</b> «cấm hút thuốc»), hoàn thành là KHÔNG NỔI '
    '(<b>дверь нельзя́ откры́ть</b> «cửa mở không ra»).</div>'
    '<div class="hd-warn">⚠️ Mức tin: việc <b>-льзя</b> từng là một từ riêng nghĩa «được» '
    'là từ nguyên, không phải luật suy ra được — nhớ để chẻ cho dễ, đừng dùng nó suy ra '
    'từ nào khác.</div>'
)

# --------------------------------------------- trạng từ đông cứng từ dạng biến cách

S["рядом"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ряд-</span>'
    '<span class="hd-gloss">gốc «hàng, dãy»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ом</span>'
    '<span class="hd-gloss">đuôi CÁCH 5, đã đông cứng thành trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen «ở cùng một hàng» ⇒ «ngay cạnh». Đây đúng là kiểu trạng '
    'từ dựng bằng cách 5 của danh từ, giống <b>у́тром</b> «buổi sáng» — nhận ra đuôi là '
    'đoán được nghĩa.</div>'
    '<div class="hd-warn">⚠️ Cạnh CÁI GÌ thì bắt buộc có giới từ <b>с</b> + cách 5: '
    '<b>ря́дом с до́мом</b> «cạnh nhà». Đứng một mình <b>ря́дом</b> chỉ nghĩa «ở gần đây».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ряд</b> hàng, dãy · <b>поря́док</b> trật tự · '
    '<b>наряду́</b> ngang hàng với</div>'
)

S["прямо"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">прям-</span>'
    '<span class="hd-gloss">gốc «thẳng»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi biến tính từ thành trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ tính từ <b>прямо́й</b> «thẳng» ra trạng từ bằng <b>-о</b>, và '
    'trọng âm chạy ngược về gốc: прямо́й → <b>пря́мо</b>. Nghĩa đen là «đi thẳng», nghĩa '
    'bóng là «trúng phóc, đúng ngay».</div>'
    '<div class="hd-warn">⚠️ Nghĩa bóng gặp nhiều hơn nghĩa đen: <b>пря́мо сейча́с</b> «ngay '
    'bây giờ», <b>пря́мо здесь</b> «đúng ngay đây».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>прямо́й</b> thẳng · <b>напряму́ю</b> thẳng thừng · '
    '<b>прямоуго́льник</b> hình chữ nhật</div>'
)

S["конечно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кон-</span>'
    '<span class="hd-gloss">gốc «cùng, kết thúc» — của <b>коне́ц</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-</span>'
    '<span class="hd-gloss">hậu tố dựng tính từ <b>коне́чный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen «một cách chung cuộc» ⇒ «khỏi bàn nữa, tất nhiên rồi». '
    'Muốn nhấn thêm thì thêm tiểu từ <b>же</b>: <b>коне́чно же</b> «thì tất nhiên rồi».</div>'
    '<div class="hd-warn">⚠️ Viết чн nhưng ĐỌC là [шн] — nghe thành «конешно». Cùng luật '
    'với <b>ску́чно</b> và <b>что</b>; không biết thì nghe băng sẽ không nhận ra từ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>коне́ц</b> kết thúc · <b>коне́чный</b> cuối cùng · '
    '<b>наконе́ц</b> cuối cùng thì</div>'
)

S["немного"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не-</span>'
    '<span class="hd-gloss">KHÔNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">мно́г-</span>'
    '<span class="hd-gloss">gốc «nhiều»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chẻ ra là «không nhiều», nhưng dùng theo hướng TÍCH CỰC — «có một '
    'chút, đủ dùng». Chê ít quá thì phải đổi sang <b>ма́ло</b>.</div>'
    '<div class="hd-warn">⚠️ Từ chỉ lượng thì danh từ theo sau sang CÁCH 2: '
    '<b>немно́го вре́мени</b>, <b>немно́го люде́й</b> — cùng luật với <b>мно́го</b>, '
    '<b>ма́ло</b>, <b>ско́лько</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мно́го</b> nhiều · <b>мно́гие</b> nhiều người/nhiều cái · '
    '<b>немно́жко</b> một tí ti</div>'
)

# ---------------------------------------------------- tiểu từ & liên từ gốc trơn

S["но"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — liên từ gốc trơn, một khối hai chữ cái.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiếng Việt dịch cả <b>но</b> lẫn <b>а</b> thành «nhưng», thật ra '
    'chúng khác nhau: <b>но</b> BẺ NGƯỢC ý vừa nói (mệt <b>но</b> vẫn đi), còn <b>а</b> chỉ '
    'đặt hai vế cạnh nhau để so (tôi đi, <b>а</b> anh ở lại). Cứ hỏi «hai vế có chọi nhau '
    'không?».</div>'
    '<div class="hd-warn">⚠️ Cụm phải thuộc: <b>не то́лько… но и</b> «không những… mà còn». '
    'Vế sau bắt buộc có <b>и</b>, bỏ đi là câu hỏng.</div>'
)

S["хотя"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">хот-</span>'
    '<span class="hd-gloss">gốc «muốn» (của <b>хоте́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-я</span>'
    '<span class="hd-gloss">đuôi phó động từ «đang…», đã đông cứng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vốn là dạng «đang muốn» của <b>хоте́ть</b>, nghĩa đen «dù có muốn '
    'thế nào đi nữa» ⇒ thành liên từ «mặc dù». Nhớ được mối nối này thì không lẫn nó với '
    'các liên từ khác.</div>'
    '<div class="hd-warn">⚠️ <b>хотя́ бы</b> lại là chuyện khác hẳn: «ít ra, chí ít» — '
    '<b>позвони́ хотя́ бы</b> «ít ra thì gọi một cú».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>хоте́ть</b> muốn · <b>хоть</b> dù (dạng ngắn, thân mật hơn)</div>'
)

S["всё"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вс-</span>'
    '<span class="hd-gloss">gốc «toàn bộ» (của <b>весь</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ё</span>'
    '<span class="hd-gloss">đuôi giống TRUNG số ít</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Là dạng giống trung của <b>весь</b>: «toàn bộ cái ấy» ⇒ «mọi thứ». '
    'Vì là số ít nên động từ theo sau cũng số ít — <b>всё гото́во</b>.</div>'
    '<div class="hd-warn">⚠️ <b>всё</b> (có hai chấm, giống trung) «mọi thứ» ≠ <b>все</b> '
    '(không chấm, số nhiều) «mọi người». Người Nga hay bỏ hai chấm khi viết, phải đoán '
    'theo động từ: <b>всё бы́ло</b> / <b>все бы́ли</b>.</div>'
    '<div class="hd-warn">⚠️ Còn một nghĩa nữa, làm trạng từ «vẫn cứ, suốt»: '
    '<b>всё ещё</b> «vẫn còn cho tới giờ».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>весь</b> toàn bộ · <b>всегда́</b> luôn luôn · '
    '<b>всё равно́</b> dù sao cũng thế</div>'
)

S["ещё"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — tiểu từ gốc trơn, một khối.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một chữ ôm hai hướng dùng. THÊM VÀO: <b>ещё раз</b> «một lần nữa», '
    '<b>ещё оди́н</b> «thêm một cái». CHƯA DỨT: <b>он ещё спит</b> «nó vẫn đang ngủ». Cụm '
    '<b>всё ещё</b> gộp cả hai — «vẫn còn cho tới tận giờ».</div>'
    '<div class="hd-warn">⚠️ Cặp lẫn nhiều nhất: <b>ещё не</b> «vẫn CHƯA» (chuyện còn có '
    'thể tới) khác <b>уже́ не</b> «KHÔNG CÒN nữa» (chuyện đã hết).</div>'
)

S["ой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — thán từ, chỉ là tiếng bật ra khỏi miệng.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bật ra khi ĐAU hoặc GIẬT MÌNH (<b>ой, бо́льно!</b> «ối, đau!»), và '
    'cả khi chợt nhớ ra điều gì (<b>ой, я забы́л</b> «ôi, tôi quên mất»). Là lời buột ra '
    'cho chính mình, nên không dùng trong câu trang trọng.</div>'
    '<div class="hd-warn">⚠️ Đừng lẫn với <b>эй</b> «này!» — <b>эй</b> là tiếng GỌI người '
    'khác, còn <b>ой</b> không nhắm vào ai.</div>'
)


# ---------------------------------------------------------------------------
# V — sửa field Vietnamese (README §2c). Ở lô này gần như từ nào cũng mang
# PoS = oth (badge vô dụng) và các cụm khiếm khuyết Việt hoá đâm nhau rất mạnh:
# "phải / cần / được / có thể" ứng với мочь · можно · нельзя cùng lúc.
# ---------------------------------------------------------------------------

V['но'] = 'nhưng'
V['нет'] = 'không, không có, không tồn tại'
V['есть'] = 'ăn, có, tồn tại'
V['мочь'] = 'có thể, đủ sức'
V['можно'] = 'được, được phép, có thể'
V['нельзя'] = 'không được, cấm, không thể'
V['прямо'] = 'thẳng, ngay, đúng phóc'
V['рядом'] = 'ngay cạnh, sát bên, kề bên'
V['немного'] = 'một chút, một ít, hơi'
V['хотя'] = 'mặc dù, dù rằng, ít ra'
V['всё'] = 'mọi thứ, tất cả'
V['ещё'] = 'nữa, thêm nữa, vẫn còn'
V['ой'] = 'ối, ôi, ái'
