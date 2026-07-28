# -*- coding: utf-8 -*-
"""k49 — places::city: hỏi đường và đi lại — bốn động từ chuyển động có tiền tố
(до- tới được đích vs при- tới và có mặt, giao với идти́ chân vs е́хать xe),
bộ ba câu hỏi куда́/где/отку́да, và tiền tố пере- nối перехо́д ↔ переса́дка."""

# ------------------------------------------------------------------ khối chung
# LẶP Ở MỌI THẺ TRONG HỌ LÀ CỐ Ý (README §3). Tối đa 2 khối một thẻ (README §2).

HE_DVIZH = (
    '<div class="hd-sec">■ Hệ thống — ĐỘNG TỪ CHUYỂN ĐỘNG: mỗi kiểu đi có HAI động từ</div>'
    '<div class="hd-why">Tiếng Nga tách chữ "đi" theo <b>hai</b> trục cùng lúc, và phải chọn xong cả hai trước khi mở miệng: ① đi <b>bằng gì</b> — chân hay phương tiện; ② đi <b>một chiều</b> hay <b>đi đi lại lại</b>.</div>'
    '<div class="hd-row"><span class="hd-piece">MỘT CHIỀU<br>đang trên đường, có đích</span>'
    '<span class="hd-gloss">chân: <b>идти́</b> · xe: <b>е́хать</b><br><i>Я иду́ в шко́лу</i> = tôi đang trên đường tới trường (ngay lúc này)</span></div>'
    '<div class="hd-row"><span class="hd-piece">NHIỀU CHIỀU<br>thói quen, đi rồi về</span>'
    '<span class="hd-gloss">chân: <b>ходи́ть</b> · xe: <b>е́здить</b><br><i>Я хожу́ в шко́лу</i> = tôi (vẫn thường) đi học</span></div>'
    '<div class="hd-warn"><b>Chân hay phương tiện — chỗ người mới hay lẫn nhất:</b><br>Đi bằng chân dùng <b>идти́ / ходи́ть</b>; ngồi lên bất cứ thứ gì chở mình đi (kể cả ngựa) thì dùng <b>е́хать / е́здить</b>.<br>Nhưng chính <b>phương tiện</b> lại tự "đi bộ": <i>авто́бус идёт</i>, <i>по́езд идёт</i> — xe cộ tự chạy nên nó dùng <b>идти́</b>. Cùng lối nghĩ đó: <i>идёт дождь</i> = trời đang mưa, <i>вре́мя идёт</i> = thời gian trôi.</div>'
    '<div class="hd-warn"><b>Chia — hai động từ này bất quy tắc, buộc phải thuộc:</b><br>'
    '<b>идти́</b>: <b>иду́</b> · <b>идёшь</b> · <b>идёт</b> · <b>идём</b> · <b>идёте</b> · <b>иду́т</b> — quá khứ đổi hẳn thân từ: <b>шёл</b>, <b>шла</b>, <b>шло</b>, <b>шли</b>.<br>'
    '<b>е́хать</b>: <b>е́ду</b> · <b>е́дешь</b> · <b>е́дет</b> · <b>е́дем</b> · <b>е́дете</b> · <b>е́дут</b> — quá khứ đều đặn <b>е́хал</b>. Nhìn kỹ: nguyên thể mang <b>х</b>, hiện tại đổi thành <b>д</b>.<br>'
    '🔴 <b>е́хать không có mệnh lệnh của riêng nó</b>: bảo ai "đi đi" thì phải mượn thân từ khác — <b>поезжа́й!</b> / <b>поезжа́йте!</b> (dạng <i>е́хай</i> là sai, đừng suy ra).</div>'
)

HE_PREF = (
    '<div class="hd-sec">■ Hệ thống — TIỀN TỐ dán vào động từ chuyển động làm HAI việc một lúc</div>'
    '<div class="hd-why">Gắn tiền tố vào <b>идти́</b> / <b>е́хать</b> thì <b>đồng thời</b>: ① thêm nghĩa HƯỚNG, ② biến động từ sang <b>thể HOÀN THÀNH</b>. Nên <b>прийти́</b> vừa là "đến", vừa mang sẵn nghĩa "đến xong rồi". Thuộc bộ tiền tố này là đọc được hàng trăm động từ mà không phải học thêm từ nào.</div>'
    '<div class="hd-row"><span class="hd-piece">при- ↔ у-</span><span class="hd-gloss">TỚI VÀ CÓ MẶT ↔ BỎ ĐI KHỎI: <b>прийти́</b> / <b>прие́хать</b> đến nơi · <b>уйти́</b> / <b>уе́хать</b> đi mất</span></div>'
    '<div class="hd-row"><span class="hd-piece">до-</span><span class="hd-gloss">ĐẾN TẬN, đi hết quãng đường tới được đích: <b>дойти́</b> / <b>дое́хать</b>. Luôn kéo theo giới từ <b>до</b> + cách 2.</span></div>'
    '<div class="hd-row"><span class="hd-piece">в- ↔ вы-</span><span class="hd-gloss">VÀO ↔ RA: <b>войти́</b> / <b>вы́йти</b>. Chú ý <b>вы-</b> hút hết trọng âm về mình ở thể hoàn thành: <b>вы́йду</b>, <b>вы́шел</b>.</span></div>'
    '<div class="hd-row"><span class="hd-piece">под- ↔ от-</span><span class="hd-gloss">LẠI GẦN ↔ RỜI RA MỘT CHÚT: <b>подойти́</b> к + cách 3 · <b>отойти́</b> от + cách 2</span></div>'
    '<div class="hd-row"><span class="hd-piece">пере- · за- · об- · по-</span><span class="hd-gloss">QUA BÊN KIA <b>перейти́</b> · GHÉ QUA <b>зайти́</b> · VÒNG QUANH <b>обойти́</b> · BẮT ĐẦU ĐI <b>пойти́</b>, <b>пое́хать</b></span></div>'
    '<div class="hd-warn"><b>Thể CHƯA hoàn thành lấy ở đâu — luật rất gọn:</b><br>Dán chính tiền tố đó lên thân <b>NHIỀU CHIỀU</b>: <b>-ходи́ть</b> cho chân, <b>-езжа́ть</b> cho xe.<br>прийти́ ← <b>приходи́ть</b> · дойти́ ← <b>доходи́ть</b> · прие́хать ← <b>приезжа́ть</b> · дое́хать ← <b>доезжа́ть</b><br>🔴 Và khi đã có tiền tố thì <b>nghĩa "nhiều chiều" biến mất</b>: <b>приходи́ть</b> không còn là "đến đi đến lại", nó chỉ là thể chưa hoàn thành của "đến".</div>'
    '<div class="hd-warn"><b>Tiền tố nào thì giới từ ấy — nhớ theo cặp là không sai cách:</b><br>'
    '<b>в-</b> … <b>в</b> + cách 4 · <b>вы-</b> … <b>из</b> + cách 2 · <b>до-</b> … <b>до</b> + cách 2 · <b>под-</b> … <b>к</b> + cách 3 · <b>от-</b> … <b>от</b> + cách 2 · <b>при-</b> … <b>в</b>/<b>на</b> + cách 4.<br>Tiền tố và giới từ thường là <b>cùng một chữ</b> — đó không phải trùng hợp, đó là cách tiếng Nga dựng câu.</div>'
)

HE_HUONG = (
    '<div class="hd-sec">■ Hệ thống — КУДА́ / ГДЕ / ОТКУ́ДА: ba câu hỏi, ba bộ trả lời riêng</div>'
    '<div class="hd-why">Tiếng Việt dùng chung một chữ "đâu" cho cả ba. Tiếng Nga tách hẳn, và <b>chọn nhầm bộ là câu sai ngữ pháp</b> chứ không chỉ nghe lạ.</div>'
    '<div class="hd-row"><span class="hd-piece">куда́?<br>đi đâu (có chuyển động)</span><span class="hd-gloss"><b>сюда́</b> lại đây · <b>туда́</b> đến đó · <b>домо́й</b> về nhà · <b>нале́во</b> sang trái · <b>напра́во</b> sang phải · <b>наза́д</b> lùi lại · <b>вперёд</b> tiến lên</span></div>'
    '<div class="hd-row"><span class="hd-piece">где?<br>ở đâu (đứng yên)</span><span class="hd-gloss"><b>здесь</b> ở đây · <b>там</b> ở đó · <b>до́ма</b> ở nhà · <b>сле́ва</b> phía trái · <b>спра́ва</b> phía phải · <b>сза́ди</b> phía sau · <b>впереди́</b> phía trước</span></div>'
    '<div class="hd-row"><span class="hd-piece">отку́да?<br>từ đâu</span><span class="hd-gloss"><b>отсю́да</b> từ đây · <b>отту́да</b> từ đó · <b>из до́ма</b> từ nhà · <b>с рабо́ты</b> từ chỗ làm</span></div>'
    '<div class="hd-warn"><b>Cặp tiền tố на- / с- mở khoá cả bảng trên:</b><br>'
    '<b>на-</b> + hướng = <b>ĐI VỀ PHÍA</b> đó, trả lời куда́: <b>нале́во</b>, <b>напра́во</b>, <b>наза́д</b>, <b>наве́рх</b>.<br>'
    '<b>с-</b> + hướng = <b>Ở PHÍA</b> đó, trả lời где: <b>сле́ва</b>, <b>спра́ва</b>, <b>сза́ди</b>, <b>све́рху</b>.<br>'
    '<i>Поверни́те напра́во</i> = rẽ phải (куда́) · <i>Апте́ка спра́ва</i> = hiệu thuốc ở bên phải (где).</div>'
    '<div class="hd-warn">Cùng đúng luật ấy khi trả lời bằng danh từ, chỉ khác là nó hiện ra thành CÁCH:<br><b>в шко́ле</b> (cách 6 — ở trong trường, где) ↔ <b>в шко́лу</b> (cách 4 — vào trường, куда́) ↔ <b>из шко́лы</b> (cách 2 — từ trường ra, отку́да).<br>⇒ Câu hỏi quyết định CÁCH, giới từ chỉ đi theo. Nhớ được điều này là gỡ được một trong những lỗi dai nhất của người mới.</div>'
)

HE_NE = (
    '<div class="hd-sec">■ Hệ thống — не viết LIỀN hay viết RỜI</div>'
    '<div class="hd-why">Với trạng từ đuôi <b>-о</b> và với tính từ, chữ <b>не</b> có thể dính vào thành một từ. Luật gọn lại còn hai vế:<br>• Viết <b>LIỀN</b> khi cả cụm mang một nghĩa mới và thay được bằng từ đồng nghĩa không có не: <b>недалеко́</b> = <b>бли́зко</b> (gần) · <b>нехорошо́</b> = <b>пло́хо</b> (dở) · <b>недорого́й</b> = <b>дешёвый</b> (rẻ).<br>• Viết <b>RỜI</b> khi thật sự phủ định, nhất là khi có vế đối lập với <b>а</b>: <i>Э́то не далеко́, а о́чень далеко́</i> = chỗ đó không phải xa, mà là rất xa.</div>'
    '<div class="hd-warn">Ba dấu hiệu buộc viết RỜI, nhớ thành bộ: ① có <b>а</b> đối lập phía sau · ② có <b>во́все не</b>, <b>отню́дь не</b> · ③ có <b>ничу́ть</b>, <b>ниско́лько</b>. Ngoài ba chỗ đó, trạng từ <b>-о</b> gần như luôn viết liền.</div>'
    '<div class="hd-warn">⚠️ Mức tin: đây là quy tắc chính tả có ngoại lệ và có vùng xám (chính người Nga cũng tra sách khi viết trang trọng). Với mức của bạn hiện nay, cứ dùng vế đầu — thay được bằng từ đồng nghĩa thì viết liền — là đủ đúng gần như mọi lúc.</div>'
)

HE_PERE = (
    '<div class="hd-sec">■ Hệ thống — tiền tố ПЕРЕ-: qua · chuyển · làm lại</div>'
    '<div class="hd-why">Nghĩa lõi của <b>пере-</b> là <b>vượt từ bên này sang bên kia</b> — cùng một ý niệm với giới từ <b>че́рез</b> (qua, xuyên). Ba nhánh nghĩa đều mọc thẳng ra từ đó:</div>'
    '<div class="hd-row"><span class="hd-piece">① QUA, SANG</span><span class="hd-gloss"><b>перейти́</b> đi qua · <b>перее́хать</b> đi qua bằng xe; chuyển nhà · <b>перевести́</b> dẫn qua → <b>DỊCH</b> (chuyển ý từ tiếng này sang tiếng kia) · <b>перехо́д</b> lối qua</span></div>'
    '<div class="hd-row"><span class="hd-piece">② CHUYỂN CHỖ</span><span class="hd-gloss"><b>пересе́сть</b> đổi chỗ ngồi, đổi tàu · <b>переса́дка</b> sự chuyển tàu; sự cấy ghép · <b>переда́ть</b> chuyển giao, trao lại</span></div>'
    '<div class="hd-row"><span class="hd-piece">③ LÀM LẠI / QUÁ MỨC</span><span class="hd-gloss"><b>переде́лать</b> làm lại · <b>переписа́ть</b> chép lại · <b>перечита́ть</b> đọc lại — và nhánh "quá tay": <b>перее́сть</b> ăn quá no · <b>переплати́ть</b> trả dư tiền</span></div>'
    '<div class="hd-warn">⚠️ Mức tin: chuyện <b>пере-</b> và <b>че́рез</b> chung một gốc Slav là <b>từ nguyên</b>, không phải luật suy ra được — cứ dùng nó làm cái móc treo nghĩa. Còn ba nhánh nghĩa ở trên thì là mô tả cách dùng thật, dùng ngay được.</div>'
)

HE_HOIDUONG = (
    '<div class="hd-sec">■ Hệ thống — HỎI ĐƯỜNG: nguyên bộ câu, học liền một mạch</div>'
    '<div class="hd-why">Cả lô từ này phục vụ đúng một tình huống. Học rời từng chữ thì lúc cần vẫn đứng hình; học nguyên bộ dưới đây thì dùng được ngay.</div>'
    '<div class="hd-row"><span class="hd-piece">MỞ LỜI</span><span class="hd-gloss"><i>Извини́те, пожа́луйста…</i> = xin lỗi cho hỏi… — với người lạ thì luôn mở đầu bằng câu này</span></div>'
    '<div class="hd-row"><span class="hd-piece">HỎI</span><span class="hd-gloss"><i>Как дойти́ до…?</i> (đi bộ) · <i>Как дое́хать до…?</i> (bằng xe) · <i>Где нахо́дится…?</i> (nằm ở đâu) · <i>Э́то далеко́?</i> (có xa không)</span></div>'
    '<div class="hd-row"><span class="hd-piece">NGHE ĐÁP</span><span class="hd-gloss"><i>Иди́те пря́мо</i> đi thẳng · <i>пото́м нале́во</i> rồi rẽ trái · <i>на углу́</i> ở góc phố · <i>че́рез доро́гу</i> bên kia đường · <i>ря́дом с ба́нком</i> cạnh ngân hàng · <i>напро́тив шко́лы</i> đối diện trường</span></div>'
    '<div class="hd-row"><span class="hd-piece">CHỐT</span><span class="hd-gloss"><i>Нет, недалеко́, мину́т де́сять пешко́м</i> = không xa, đi bộ chừng mười phút · <i>Спаси́бо большо́е!</i></span></div>'
    '<div class="hd-warn"><b>Ba chữ nhỏ mà nghe là biết trình độ:</b> <b>пря́мо</b> = đi thẳng (đừng nhầm với <b>про́сто</b> = chỉ là, đơn giản) · <b>поворо́т</b> = chỗ rẽ, nên <i>второ́й поворо́т напра́во</i> = chỗ rẽ thứ hai bên phải · và người Nga rất hay đáp bằng <b>пройти́</b> (đi bộ xuyên qua tới nơi): <i>Как пройти́ к метро́?</i> — trong thực tế đồng nghĩa với <b>дойти́ до</b>.</div>'
)

S = {}

S["дойти"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-</span><span class="hd-gloss">ĐẾN TẬN, cho tới — cùng một chữ với giới từ <b>до</b> (đến, trước khi)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-й-</span><span class="hd-gloss">thân của <b>идти́</b> sau khi bị tiền tố nuốt mất chữ <b>и</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ти́</span><span class="hd-gloss">đuôi nguyên thể (dạng cổ, nhấn ở đuôi)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>до-</b> nghĩa là "cho tới tận", nên <b>дойти́</b> = <b>đi bộ tới được đích</b>. Trọng tâm của nó là <b>quãng đường đã vượt hết</b>, chứ không phải việc có mặt ở đó — đúng như tiếng Anh <i>reach</i>.</div>'
    '<div class="hd-warn"><b>Chính tả: и biến thành й.</b> Khi tiền tố kết thúc bằng nguyên âm gắn vào <b>идти́</b>, chữ <b>и</b> co lại thành <b>й</b>: до + идти́ → <b>дойти́</b> · при + идти́ → <b>прийти́</b> · по + идти́ → <b>пойти́</b> · за + идти́ → <b>зайти́</b>. Một luật, dùng cho cả họ.</div>'
    '<div class="hd-warn"><b>Chia:</b> <b>дойду́</b> · <b>дойдёшь</b> · <b>дойдёт</b> · <b>дойдём</b> · <b>дойдёте</b> · <b>дойду́т</b> — thân <b>-йд-</b> hiện ra ở mọi ngôi.<br>Quá khứ mượn thân khác hẳn: <b>дошёл</b> · <b>дошла́</b> · <b>дошло́</b> · <b>дошли́</b>. Đây là thể HOÀN THÀNH, nên bộ đuôi "hiện tại" ở trên thật ra mang nghĩa <b>TƯƠNG LAI</b>: <i>Я дойду́ за де́сять мину́т</i> = tôi sẽ tới nơi sau mười phút.</div>'
    '<div class="hd-warn"><b>Cách nó đòi — không có lựa chọn nào khác:</b> <b>дойти́ до</b> + cách 2. Cái đích luôn đi sau <b>до</b>.<br><i>Как дойти́ до метро́?</i> = đi bộ tới ga tàu điện ngầm thế nào? — đây là <b>câu hỏi đường tiêu chuẩn</b> khi bạn định đi bộ. Câu trả lời quen thuộc: <i>Иди́те пря́мо, пото́м напра́во</i>.</div>'
    '<div class="hd-warn"><b>Nghĩa bóng — dùng rất nhiều, và vẫn là "đi tới đích":</b><br><i>Письмо́ дошло́</i> = thư đã tới nơi · <i>До меня́ дошло́</i> = tôi hiểu ra rồi (nghĩa đen: "nó đã đến được chỗ tôi") · <i>Дошло́ до того́, что…</i> = sự việc đi tới mức là…<br>Nghĩa <i>amount to</i> trong từ điển Anh chính là nhánh này.</div>'
    '<div class="hd-sec">Họ hàng — gốc ид/й/ход</div>'
    '<div class="hd-fam"><b>идти́</b> đi (bộ) · <b>доходи́ть</b> bản chưa hoàn thành của chính nó · <b>дохо́д</b> thu nhập — cái "đi tới" tay bạn · <b>вход</b> lối vào · <b>вы́ход</b> lối ra · <b>перехо́д</b> lối qua đường · <b>похо́д</b> chuyến đi bộ, hành quân</div>'
    + HE_DVIZH + HE_PREF
)

S["доехать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-</span><span class="hd-gloss">ĐẾN TẬN, tới được đích (y hệt tiền tố ở <b>дойти́</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́хать</span><span class="hd-gloss">đi bằng phương tiện — thân giữ nguyên, không co lại như <b>идти́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>дое́хать</b> là <b>bản có bánh xe của дойти́</b>. Hai từ khác nhau đúng một điểm: bạn dùng chân hay dùng phương tiện. Ghép cặp mà học thì được hai từ với công sức của một.</div>'
    '<div class="hd-warn"><b>Chia:</b> <b>дое́ду</b> · <b>дое́дешь</b> · <b>дое́дет</b> · <b>дое́дем</b> · <b>дое́дете</b> · <b>дое́дут</b> — trọng âm đứng yên ở <b>е́</b> suốt, không nhảy đi đâu. Quá khứ đều đặn: <b>дое́хал</b>, <b>дое́хала</b>, <b>дое́хали</b>. Thể hoàn thành ⇒ những đuôi trên là <b>TƯƠNG LAI</b>.</div>'
    '<div class="hd-warn"><b>Cách nó đòi — hai chỗ, đừng lẫn:</b><br>• Đích đến: <b>дое́хать до</b> + <b>cách 2</b> — <i>дое́хать до вокза́ла</i>.<br>• Phương tiện: <b>на</b> + <b>cách 6</b> — <i>на авто́бусе</i>, <i>на метро́</i>, <i>на такси́</i>, <i>на маши́не</i>.<br>🔴 Phương tiện dùng <b>на</b>, KHÔNG dùng <b>в</b>. Nói <i>в авто́бусе</i> thì nghĩa thành "ở bên trong xe buýt" (đang ngồi trong đó), không phải "đi bằng xe buýt".</div>'
    '<div class="hd-warn"><b>Ba câu bạn sẽ dùng ngay khi ra đường:</b><br><i>Как дое́хать до це́нтра?</i> = đi tới trung tâm thế nào? · <i>Как мне лу́чше дое́хать?</i> = tôi nên đi đường nào thì hơn? · <i>Мы дое́хали</i> = chúng tôi tới nơi rồi.<br>Câu trả lời hay gặp: <i>На метро́, две остано́вки</i>.</div>'
    '<div class="hd-warn"><b>Đối chiếu до- và при- ngay tại đây:</b> <b>дое́хать до до́ма</b> nhấn việc <b>đi hết đường về được tới nhà</b>; <b>прие́хать домо́й</b> nhấn việc <b>đã có mặt ở nhà</b>. Cùng một chuyến đi, khác nhau ở chỗ bạn muốn người nghe chú ý điều gì.</div>'
    '<div class="hd-sec">Họ hàng — gốc ех/езд</div>'
    '<div class="hd-fam"><b>е́хать</b> đi (bằng xe) · <b>е́здить</b> đi lại thường xuyên · <b>доезжа́ть</b> bản chưa hoàn thành · <b>прие́хать</b> đến · <b>уе́хать</b> đi khỏi · <b>перее́хать</b> chuyển nhà · <b>по́езд</b> tàu hoả · <b>пое́здка</b> chuyến đi · <b>езда́</b> sự đi xe · <b>вы́езд</b> lối ra (cho xe)</div>'
    + HE_DVIZH + HE_PREF
)

S["прийти"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span><span class="hd-gloss">TỚI SÁT BÊN VÀ Ở LẠI — cùng chữ với giới từ <b>при</b> (ở cạnh, kèm theo)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-й-</span><span class="hd-gloss">thân của <b>идти́</b>, chữ <b>и</b> đã co lại</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ти́</span><span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nếu <b>до-</b> là "đi hết quãng đường", thì <b>при-</b> là "<b>tới nơi và có mặt tại đó</b>". Chính vì thế <b>прийти́</b> mới là từ thường dùng nhất để nói ai đó <b>đã đến</b>.</div>'
    '<div class="hd-warn"><b>So cặp cho rõ — cùng một chuyến, khác trọng tâm:</b><br><i>Я дошёл до до́ма</i> = tôi lê được về tới nhà (nhấn quãng đường)<br><i>Я пришёл домо́й</i> = tôi đã về đến nhà (nhấn: giờ tôi ở nhà)<br>Và để ý giới từ đi kèm khác nhau: <b>до</b> + cách 2 với <b>до-</b>, còn <b>при-</b> thì <b>в</b>/<b>на</b> + cách 4, hoặc <b>к</b> + cách 3 khi đến chỗ một người.</div>'
    '<div class="hd-warn">🔴 <b>Bẫy chính tả nổi tiếng:</b> nguyên thể viết <b>прийти́</b> (có <b>й</b>), nhưng vừa chia là <b>й</b> biến mất: <b>приду́</b> · <b>придёшь</b> · <b>придёт</b> · <b>придём</b> · <b>придёте</b> · <b>приду́т</b>. Viết <i>придти</i> là dạng cũ, nay bị coi là sai; viết <i>прийду</i> cũng sai. Nhớ: <b>й chỉ sống ở nguyên thể</b>.<br>Quá khứ: <b>пришёл</b> · <b>пришла́</b> · <b>пришло́</b> · <b>пришли́</b>.</div>'
    '<div class="hd-warn"><b>Cụm dùng thật, gặp gần như mỗi ngày:</b><br><i>прийти́ домо́й</i> về đến nhà · <i>прийти́ в го́сти</i> đến chơi nhà ai · <i>прийти́ во́время</i> đến đúng giờ · <i>прийти́ на по́мощь</i> đến ứng cứu · <i>прийти́ в себя́</i> tỉnh lại, hoàn hồn (nghĩa đen: "đi trở vào chính mình").</div>'
    '<div class="hd-sec">Họ hàng — gốc ид/й/ход</div>'
    '<div class="hd-fam"><b>приходи́ть</b> bản chưa hoàn thành · <b>прихо́д</b> sự đến · <b>идти́</b> đi bộ · <b>уйти́</b> bỏ đi · <b>войти́</b> đi vào · <b>вы́йти</b> đi ra · <b>подойти́</b> lại gần; cũng có nghĩa "vừa vặn, hợp" · <b>прохо́жий</b> người qua đường · <b>вход</b> lối vào</div>'
    + HE_DVIZH + HE_PREF
)

S["приехать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span><span class="hd-gloss">TỚI NƠI VÀ CÓ MẶT ở đó</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́хать</span><span class="hd-gloss">đi bằng phương tiện</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ô vuông thứ tư của bảng bốn từ: <b>дойти́</b> (chân, tới được) — <b>дое́хать</b> (xe, tới được) — <b>прийти́</b> (chân, đến nơi) — <b>прие́хать</b> (xe, đến nơi). Chọn tiền tố theo <b>ý bạn muốn nhấn</b>, chọn thân từ theo <b>chân hay bánh xe</b>.</div>'
    '<div class="hd-warn"><b>Chia:</b> <b>прие́ду</b> · <b>прие́дешь</b> · <b>прие́дет</b> · <b>прие́дем</b> · <b>прие́дете</b> · <b>прие́дут</b>; quá khứ <b>прие́хал</b>, <b>прие́хала</b>, <b>прие́хали</b>.<br>🔴 Đây là thể hoàn thành nên <i>Я прие́ду за́втра</i> có nghĩa <b>tôi SẼ đến</b> — không phải "tôi đến". Muốn nói hiện tại hay thói quen thì phải mượn bản chưa hoàn thành <b>приезжа́ть</b>: <i>Он ча́сто приезжа́ет</i> = anh ấy hay ghé sang.</div>'
    '<div class="hd-warn"><b>Cách nó đòi — nơi đến và nơi xuất phát đi thành cặp:</b><br>• Đến: <b>в</b>/<b>на</b> + cách 4 — <i>прие́хать в Москву́</i>, <i>прие́хать на рабо́ту</i>.<br>• Từ đâu tới: <b>из</b>/<b>с</b> + cách 2 — <i>прие́хать из Вьетна́ма</i>.<br>Luật ghép cặp: chỗ nào dùng <b>в</b> thì rời ra bằng <b>из</b>; chỗ nào dùng <b>на</b> thì rời ra bằng <b>с</b>. Đừng trộn chéo.</div>'
    '<div class="hd-warn"><b>Câu làm quen bạn sẽ nghe rất sớm:</b><br><i>Отку́да вы прие́хали?</i> = anh từ đâu tới? — <i>Я прие́хал из Вьетна́ма</i>.<br>Chú ý <b>прие́хал</b> ở đây là quá khứ nhưng dịch sang tiếng Việt lại thành trạng thái hiện tại ("tôi từ Việt Nam sang"): hành động xong rồi, kết quả còn nguyên.</div>'
    '<div class="hd-sec">Họ hàng — gốc ех/езд</div>'
    '<div class="hd-fam"><b>приезжа́ть</b> bản chưa hoàn thành · <b>прие́зд</b> sự đến (danh từ) · <b>уе́хать</b> đi khỏi · <b>отъе́зд</b> sự khởi hành · <b>е́хать</b> đi xe · <b>е́здить</b> đi lại · <b>пое́здка</b> chuyến đi · <b>по́езд</b> tàu hoả</div>'
    + HE_DVIZH + HE_PREF
)

S["ехать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">е́х- / е́д-</span><span class="hd-gloss">gốc ĐI BẰNG PHƯƠNG TIỆN — một gốc, hai mặt: <b>х</b> ở nguyên thể, <b>д</b> ở hiện tại</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span><span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ gốc trơn, không chẻ thêm được. Cái đáng học ở đây là <b>cặp х/д</b>: thấy <b>д</b> là biết đang ở dạng chia hoặc ở từ phái sinh — <b>е́ду</b>, <b>е́здить</b>, <b>по́езд</b>, <b>пое́здка</b>, <b>езда́</b> đều mang <b>д</b>; còn <b>х</b> chỉ ở lại trong <b>е́хать</b> và họ nguyên thể có tiền tố (<b>прие́хать</b>, <b>уе́хать</b>).</div>'
    '<div class="hd-warn"><b>Cách nó đòi — ba ô phải điền:</b><br>• Đi bằng gì: <b>на</b> + cách 6 — <i>на авто́бусе</i>, <i>на по́езде</i>, <i>на маши́не</i>, <i>на метро́</i>, <i>на такси́</i>.<br>• Đi tới đâu: <b>в</b>/<b>на</b> + cách 4 — <i>е́хать в го́род</i>.<br>• Đi dọc theo: <b>по</b> + cách 3 — <i>е́хать по у́лице</i>.<br>Còn đi bằng chân thì không giới từ nào cả, chỉ một chữ <b>пешко́м</b> (xem thẻ riêng).</div>'
    '<div class="hd-warn"><b>Thể:</b> <b>е́хать</b> (chưa hoàn thành) → <b>пое́хать</b> (hoàn thành). Tiền tố <b>по-</b> ở đây thêm sắc thái <b>bắt đầu đi, lên đường</b>: <i>Мы пое́дем в Москву́</i> = chúng tôi sẽ lên đường đi Moskva.<br><i>Пое́хали!</i> = "Đi thôi!" — câu cửa miệng; hình thức là quá khứ số nhiều nhưng dùng như lời rủ.</div>'
    '<div class="hd-warn"><b>Sắc thái hay bị bỏ qua:</b> <b>е́хать</b> nói về <b>một chuyến đang diễn ra, có hướng</b>. Hỏi <i>Куда́ ты е́дешь?</i> là hỏi chuyến đi lúc này. Muốn nói thói quen thì phải đổi sang <b>е́здить</b>: <i>Я е́зжу на рабо́ту на метро́</i> = tôi đi làm bằng tàu điện ngầm (hằng ngày). Để ý biến âm <b>зд→зж</b> ở ngôi <b>я</b>: <b>е́зжу</b> nhưng <b>е́здишь</b>.</div>'
    '<div class="hd-sec">Họ hàng — gốc ех/езд</div>'
    '<div class="hd-fam"><b>е́здить</b> đi lại (nhiều chiều) · <b>пое́хать</b> lên đường · <b>прие́хать</b> đến · <b>уе́хать</b> đi khỏi · <b>перее́хать</b> chuyển nhà · <b>вы́ехать</b> ra khỏi · <b>по́езд</b> tàu hoả · <b>пое́здка</b> chuyến đi · <b>езда́</b> sự đi xe · <b>вы́езд</b> lối ra · <b>прие́зд</b> sự đến</div>'
    + HE_DVIZH
)

S["находиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span><span class="hd-gloss">LÊN TRÊN, vấp phải, chạm vào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ход-</span><span class="hd-gloss">gốc ĐI (dạng "nhiều chiều" của <b>идти́</b>, thấy trong <b>ходи́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-ть</span><span class="hd-gloss">hậu tố lớp 2 + đuôi nguyên thể</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span><span class="hd-gloss">hậu tố phản thân — ở đây mang nghĩa BỊ ĐỘNG: "được… "</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đọc từng mảnh sẽ ra nghĩa gần như không cần học: <b>находи́ть</b> = "đi mà vấp phải" → <b>tìm ra</b>. Thêm <b>-ся</b> thành "được tìm thấy" → <b>nằm ở đâu</b>. Tiếng Anh có đúng cùng một lối nghĩ: <i>to be found</i> → <i>to be located</i>.</div>'
    '<div class="hd-warn"><b>Chia (lớp 2) — biến âm д→ж CHỈ ở ngôi я:</b><br><b>нахожу́сь</b> · <b>нахо́дишься</b> · <b>нахо́дится</b> · <b>нахо́димся</b> · <b>нахо́дитесь</b> · <b>нахо́дятся</b>.<br>Trọng âm cũng theo kiểu quen thuộc: nhấn đuôi ở ngôi <b>я</b>, rồi lùi về gốc từ ngôi <b>ты</b> trở đi. Hậu tố <b>-ся</b> rút thành <b>-сь</b> khi đứng sau nguyên âm (<b>нахожу́сь</b>) và giữ nguyên sau phụ âm (<b>нахо́дится</b>).</div>'
    '<div class="hd-warn"><b>Dùng cho VẬT và ĐỊA ĐIỂM, không dùng cho người trong lời nói thường:</b><br><i>Где нахо́дится вокза́л?</i> = nhà ga ở đâu ạ? — câu hỏi đường lịch sự, dùng được với người lạ.<br>Nói ngắn <i>Где вокза́л?</i> cũng hoàn toàn đúng và tự nhiên hơn trong khẩu ngữ.<br>Nhưng về mình thì nói <i>Я в Москве́</i>, chứ <i>Я нахожу́сь в Москве́</i> nghe như đang viết báo cáo.</div>'
    '<div class="hd-warn">🔴 <b>Đừng lẫn hai từ chỉ khác nhau đúng hai chữ:</b><br><b>находи́ть</b> (không có <b>-ся</b>) = <b>tìm thấy</b>, có tân ngữ cách 4 — <i>Я нашёл ключи́</i> = tôi tìm thấy chìa khoá.<br><b>находи́ться</b> (có <b>-ся</b>) = <b>nằm ở</b>, không bao giờ có tân ngữ — <i>Апте́ка нахо́дится спра́ва</i>.<br>Cặp thể của nhánh "tìm" là <b>находи́ть</b> → <b>найти́</b> (нашёл, нашла́).</div>'
    '<div class="hd-sec">Họ hàng — gốc ход</div>'
    '<div class="hd-fam"><b>ходи́ть</b> đi lại · <b>найти́</b> tìm ra · <b>нахо́дка</b> vật nhặt được, "món hời" · <b>вход</b> lối vào · <b>вы́ход</b> lối ra · <b>перехо́д</b> lối qua đường · <b>прохо́д</b> lối đi · <b>похо́д</b> chuyến đi bộ · <b>дохо́д</b> thu nhập</div>'
    + HE_HUONG + HE_HOIDUONG
)

S["налево"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span><span class="hd-gloss">VỀ PHÍA — cùng chữ với giới từ <b>на</b> đi với cách 4 (hướng tới)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ле́во</span><span class="hd-gloss">dạng ngắn giống trung cổ của tính từ <b>ле́вый</b> = bên trái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là <b>на + cách 4</b> đã đông cứng lại thành một chữ: "về phía trái". Vì mang <b>на-</b> nên nó trả lời <b>куда́?</b> — có chuyển động. Bạn đọc được luôn cả họ theo cùng khuôn: <b>напра́во</b>, <b>наза́д</b>, <b>наве́рх</b>.</div>'
    '<div class="hd-warn"><b>Đối lập phải nhớ thành cặp:</b> <b>нале́во</b> (rẽ sang trái — куда́) ↔ <b>сле́ва</b> (ở bên trái — где).<br><i>Поверни́те нале́во</i> = rẽ trái · <i>Апте́ка сле́ва</i> = hiệu thuốc ở bên trái.<br>Muốn nói "bên trái CỦA cái gì" thì thêm <b>от</b> + cách 2: <i>нале́во от вхо́да</i> = phía trái lối vào.</div>'
    '<div class="hd-warn"><b>Sắc thái khẩu ngữ — biết để khỏi hiểu nhầm:</b> <b>нале́во</b> còn là tiếng lóng rất phổ biến cho việc "làm chui, ngoài luồng": <i>рабо́тать нале́во</i> = làm thêm không khai báo; <i>ходи́ть нале́во</i> = ngoại tình.<br>⚠️ Mức tin: đây là nghĩa <b>khẩu ngữ</b>, không dùng trong văn viết trang trọng — nhưng gặp trong phim và hội thoại thì rất thường.</div>'
    '<div class="hd-sec">Họ hàng — gốc лев</div>'
    '<div class="hd-fam"><b>ле́вый</b> bên trái; cánh tả; (khẩu ngữ) hàng lậu · <b>сле́ва</b> ở phía trái · <b>левша́</b> người thuận tay trái · <b>нале́во</b> ↔ <b>напра́во</b> cặp đối</div>'
    + HE_HUONG + HE_HOIDUONG
)

S["направо"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span><span class="hd-gloss">VỀ PHÍA (на + cách 4, chỉ hướng)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пра́во</span><span class="hd-gloss">dạng ngắn giống trung cổ của <b>пра́вый</b> = bên phải</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng khuôn với <b>нале́во</b>, chỉ đổi gốc. Nhưng gốc <b>прав-</b> đáng dừng lại lâu hơn: nó là <b>một trong những gốc sinh sôi nhất tiếng Nga</b> vì gộp ba nghĩa vào một ý niệm "thẳng, ngay, không lệch": <b>bên PHẢI</b> · <b>ĐÚNG</b> · <b>QUYỀN</b>. Nhớ một gốc, mở được cả chục từ trừu tượng khó.</div>'
    '<div class="hd-warn">⚠️ Mức tin: tiếng Anh <i>right</i> cũng gộp đúng ba nghĩa đó (bên phải / đúng / quyền lợi). Đây là <b>trùng hợp về lối nghĩ của con người</b>, hai từ không cùng gốc — nhưng dùng làm chỗ bám thì rất tiện, và nó giúp bạn không ngạc nhiên khi thấy <b>пра́во</b> nghĩa là "quyền".</div>'
    '<div class="hd-warn"><b>Cặp đối:</b> <b>напра́во</b> (rẽ sang phải — куда́) ↔ <b>спра́ва</b> (ở bên phải — где).<br><i>Поверни́те напра́во на светофо́ре</i> = tới đèn giao thông thì rẽ phải · <i>напра́во от вхо́да</i> = bên phải lối vào.<br>Thành ngữ: <i>напра́во и нале́во</i> = tứ tung, bừa bãi (<i>раздава́ть обеща́ния напра́во и нале́во</i> = hứa hẹn lung tung).</div>'
    '<div class="hd-sec">Họ hàng — gốc прав (rất lớn)</div>'
    '<div class="hd-fam"><b>пра́вый</b> bên phải; cánh hữu · <b>спра́ва</b> ở phía phải · <b>пра́во</b> quyền; luật học · <b>пра́вда</b> sự thật · <b>пра́вильно</b> đúng rồi · <b>пра́вило</b> quy tắc · <b>прави́тельство</b> chính phủ · <b>справедли́вый</b> công bằng · <b>испра́вить</b> sửa cho đúng</div>'
    + HE_HUONG + HE_HOIDUONG
)

S["напротив"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span><span class="hd-gloss">Ở PHÍA, về phía</span></div>'
    '<div class="hd-row"><span class="hd-piece">-про́тив</span><span class="hd-gloss">chính là giới từ <b>про́тив</b> = chống lại, đối mặt với</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>про́тив</b> gốc nghĩa là "quay mặt vào nhau, ngược chiều nhau". Thêm <b>на-</b> thành "<b>ở phía đối mặt</b>" — tức là <b>đối diện</b>. Lối nghĩ y hệt tiếng Anh <i>opposite</i>, vốn cũng dựng từ <i>ob-</i> = ngược lại.</div>'
    '<div class="hd-warn"><b>Hai vai trò khác hẳn nhau, nhìn câu là biết vai nào:</b><br>① <b>Giới từ + cách 2</b> = đối diện: <i>напро́тив до́ма</i> = đối diện ngôi nhà · <i>Он сиди́т напро́тив меня́</i> = anh ta ngồi đối diện tôi.<br>② <b>Trạng từ nối câu</b> = ngược lại, trái lại: <i>Я не уста́л, напро́тив, я по́лон сил</i> = tôi không mệt, ngược lại, tôi đầy sức.<br>Vai ② luôn đứng tách bằng dấu phẩy — đó là dấu hiệu nhận ra.</div>'
    '<div class="hd-warn">🔴 <b>Đừng lẫn với про́тив trần:</b> <b>про́тив</b> = <b>chống lại, phản đối</b> (<i>Я про́тив</i> = tôi phản đối; <i>лека́рство про́тив гри́ппа</i> = thuốc trị cúm). <b>напро́тив</b> KHÔNG bao giờ mang nghĩa phản đối — thêm <b>на-</b> là nghĩa đã chuyển hẳn sang không gian.</div>'
    '<div class="hd-warn"><b>Phân biệt với từ gần nghĩa:</b> <b>пе́ред</b> + cách 5 = ngay trước mặt, sát phía trước (<i>пе́ред до́мом</i> = trước nhà). <b>напро́тив</b> = đối diện <b>qua</b> một khoảng trống hay qua đường. Còn <b>наоборо́т</b> cũng dịch là "ngược lại", nhưng nó thiên về "làm ngược thứ tự"; ở vai trò nối câu thì hai từ thay nhau được.</div>'
    '<div class="hd-sec">Họ hàng — gốc против</div>'
    '<div class="hd-fam"><b>про́тив</b> chống lại · <b>проти́вник</b> đối thủ · <b>противополо́жный</b> đối lập, trái ngược · <b>противоре́чие</b> mâu thuẫn · <b>наоборо́т</b> ngược lại</div>'
    + HE_HUONG + HE_HOIDUONG
)

S["туда"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">т-</span><span class="hd-gloss">gốc chỉ định XA — cùng ổ với <b>тот</b> (cái kia), <b>там</b> (ở đó)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-уда́</span><span class="hd-gloss">đuôi cổ chỉ HƯỚNG ĐI TỚI — thấy lại y hệt ở <b>куда́</b>, <b>сюда́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không phải học thuộc rời rạc: cả nhóm này là <b>một bảng ba cột nhân ba hàng</b> rất đều. Cột là ba câu hỏi (ở đâu / đi đâu / từ đâu), hàng là ba gốc chỉ định:</div>'
    '<div class="hd-row"><span class="hd-piece">т- (đó, xa)</span><span class="hd-gloss"><b>там</b> ở đó · <b>туда́</b> đến đó · <b>отту́да</b> từ đó về</span></div>'
    '<div class="hd-row"><span class="hd-piece">зд-/с- (đây)</span><span class="hd-gloss"><b>здесь</b> ở đây · <b>сюда́</b> lại đây · <b>отсю́да</b> từ đây đi</span></div>'
    '<div class="hd-row"><span class="hd-piece">к- (hỏi)</span><span class="hd-gloss"><b>где</b> ở đâu · <b>куда́</b> đi đâu · <b>отку́да</b> từ đâu</span></div>'
    '<div class="hd-warn">🔴 <b>Lỗi kinh điển của người mới:</b> nói <i>Я иду́ там</i> là <b>sai</b> — có chuyển động thì bắt buộc <b>туда́</b>: <i>Я иду́ туда́</i>. Ngược lại <i>Он туда́</i> khi định nói "anh ấy ở đó" cũng sai, phải là <i>Он там</i>. Chọn cột theo <b>động từ</b>: động từ có hướng (идти́, е́хать, положи́ть) kéo theo <b>туда́</b>; động từ đứng yên (быть, жить, находи́ться) kéo theo <b>там</b>.</div>'
    '<div class="hd-warn"><b>Cụm dùng thật, rất hay gặp khi đi lại:</b><br><i>биле́т туда́ и обра́тно</i> = vé khứ hồi · <i>туда́-сюда́</i> = qua lại, lăng xăng · <i>Вы попа́ли не туда́</i> = anh gọi nhầm số rồi (nghĩa đen: "anh rơi vào không phải chỗ đó") · <i>Ни туда́ ни сюда́</i> = kẹt cứng, không nhúc nhích được.</div>'
    '<div class="hd-sec">Họ hàng — đuôi hướng và đuôi thời gian</div>'
    '<div class="hd-fam"><b>там</b> ở đó · <b>отту́да</b> từ đó · <b>сюда́</b> lại đây · <b>куда́</b> đi đâu · <b>тот</b> cái kia · và cùng lối dựng ấy ở THỜI GIAN với đuôi <b>-гда́</b>: <b>тогда́</b> khi đó · <b>когда́</b> khi nào · <b>всегда́</b> luôn luôn · <b>иногда́</b> đôi khi</div>'
    + HE_HUONG + HE_HOIDUONG
)

S["далеко"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дал-</span><span class="hd-gloss">gốc XA — chính là danh từ <b>даль</b> (miền xa, chốn xa xăm)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ек-</span><span class="hd-gloss">hậu tố tính từ (thấy trong <b>далёкий</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́</span><span class="hd-gloss">đuôi biến tính từ thành TRẠNG TỪ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dây chuyền rất sạch: <b>даль</b> (danh từ) → <b>далёкий</b> (tính từ) → <b>далеко́</b> (trạng từ). Để ý trọng âm <b>chạy về cuối</b> khi thành trạng từ — đây là kiểu rất hay gặp ở cặp tính từ/trạng từ ngắn: <b>далёкий → далеко́</b>, giống <b>хоро́ший → хорошо́</b>, <b>лёгкий → легко́</b>.</div>'
    '<div class="hd-warn"><b>Nó vừa là trạng từ vừa là cả một câu:</b> tiếng Nga không cần động từ "thì, là" ở hiện tại, nên <i>Э́то далеко́</i> = "cái đó thì xa" là câu hoàn chỉnh. Hỏi đường: <i>Далеко́?</i> — <i>Нет, недалеко́</i>.<br>Muốn nói xa KHỎI cái gì thì <b>далеко́ от</b> + cách 2: <i>Я живу́ далеко́ от це́нтра</i>.</div>'
    '<div class="hd-warn"><b>Ba từ cùng gốc mà khác vai, đừng trộn:</b><br>• <b>далёкий</b> = xa (khoảng cách, thời gian, quan hệ) — <i>далёкое про́шлое</i> quá khứ xa xôi.<br>• <b>да́льний</b> = thuộc tuyến xa, đường dài — <i>по́езд да́льнего сле́дования</i> tàu đường dài, <i>Да́льний Восто́к</i> Viễn Đông.<br>• <b>да́льше</b> = so sánh hơn "xa hơn", <b>và</b> = "tiếp theo, đi tiếp" — <i>Что да́льше?</i> = rồi sao nữa? · <i>Иди́те да́льше</i> = đi tiếp nữa đi.</div>'
    '<div class="hd-warn"><b>Cụm phủ định mạnh — hay gặp trong văn viết:</b> <i>далеко́ не</i> = "còn lâu mới, hoàn toàn không". <i>Э́то далеко́ не всё</i> = đó còn lâu mới là tất cả · <i>Он далеко́ не глуп</i> = anh ta chẳng ngu chút nào.<br>Chú ý ở đây <b>не</b> viết RỜI — xem khối bên dưới.</div>'
    '<div class="hd-sec">Họ hàng — gốc дал</div>'
    '<div class="hd-fam"><b>даль</b> miền xa · <b>далёкий</b> xa · <b>да́льний</b> đường dài · <b>да́льше</b> xa hơn; tiếp theo · <b>вдали́</b> ở đằng xa · <b>вдаль</b> ra xa · <b>удали́ть</b> xoá đi, gỡ bỏ · <b>недалеко́</b> không xa</div>'
    + HE_NE + HE_HOIDUONG
)

S["недалеко"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не-</span><span class="hd-gloss">phủ định, ở đây <b>dính liền</b> nên tạo ra nghĩa mới chứ không chỉ phủ định</span></div>'
    '<div class="hd-row"><span class="hd-piece">-далеко́</span><span class="hd-gloss">xa (xem thẻ <b>далеко́</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Viết liền nên nó không còn là "không xa" theo kiểu phủ định lạnh lùng, mà thành <b>một từ dương tính nghĩa GẦN</b> — thay được bằng <b>бли́зко</b>. Đây chính là mẹo thử của luật chính tả ở khối bên dưới: thay được bằng từ đồng nghĩa không có <b>не</b> thì viết liền.</div>'
    '<div class="hd-warn"><b>Sắc thái so với бли́зко:</b> <b>недалеко́</b> = "không xa lắm, đi tới được" — người Nga hay dùng nó để trấn an khi chỉ đường. <b>бли́зко</b> = "gần" thuần tuý, sát hơn. <b>ря́дом</b> = "ngay cạnh, sát bên" — gần nhất trong ba từ.<br><i>Э́то далеко́?</i> — <i>Нет, недалеко́, мину́т де́сять пешко́м</i>.</div>'
    '<div class="hd-warn"><b>Cách nó đòi:</b> <b>недалеко́ от</b> + cách 2 — <i>Магази́н недалеко́ от до́ма</i> = cửa hàng gần nhà. Cụm rất hay dùng: <i>недалеко́ отсю́да</i> = gần đây thôi.</div>'
    '<div class="hd-warn">⚠️ Mức tin — trọng âm: từ điển ghi nhận <b>cả hai</b> cách nhấn, <b>недалеко́</b> và <b>неда́леко</b>, đều đúng. Bạn cứ dùng <b>недалеко́</b> cho khớp với <b>далеко́</b>, và đừng ngạc nhiên khi nghe người Nga nhấn kiểu kia.</div>'
    '<div class="hd-warn">🔴 <b>Bẫy nghĩa bóng:</b> tính từ <b>недалёкий</b> nói về người thì KHÔNG có nghĩa "ở gần" mà là <b>đầu óc hạn hẹp, chậm hiểu</b>. Đừng dùng để khen ai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>далеко́</b> xa · <b>бли́зко</b> gần · <b>бли́зкий</b> gần gũi, thân thiết · <b>ря́дом</b> ngay cạnh · <b>побли́зости</b> quanh đây · <b>недалёкий</b> không xa; (về người) nông cạn</div>'
    + HE_NE + HE_HOIDUONG
)

S["пешком"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пеш-</span><span class="hd-gloss">gốc ĐI BỘ, BẰNG CHÂN — sống trong tính từ <b>пе́ший</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ко́м</span><span class="hd-gloss">đuôi <b>cách 5</b> (công cụ) đã hoá thạch: "bằng…"</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cách 5 trả lời câu hỏi "bằng gì", nên <b>пешко́м</b> đúng nghĩa đen là "<b>bằng chân</b>". Nó là một dạng cách 5 đã đông cứng lại thành trạng từ — cùng kiểu với <b>ве́чером</b> (vào buổi tối), <b>у́тром</b>, <b>зимо́й</b>. Đã đông cứng thì <b>không biến đổi gì nữa</b>: cứ ghép thẳng vào động từ.</div>'
    '<div class="hd-warn">⚠️ Mức tin: đuôi <b>-ом</b> ở đây đúng là đuôi cách 5, nhưng danh từ gốc mà nó chia từ đó đã biến mất khỏi tiếng Nga hiện đại — chuyện này là <b>từ nguyên</b>, không phải luật bạn suy ra được. Phần dùng được ngay chỉ là: <b>пешко́м</b> bất biến, và nó luôn trả lời câu hỏi <b>как?</b> (bằng cách nào).</div>'
    '<div class="hd-warn">🔴 <b>Đối lập cần nhớ nhất trong cả mảng đi lại:</b><br>Đi bằng phương tiện → <b>на</b> + cách 6: <i>на авто́бусе</i>, <i>на метро́</i>, <i>на маши́не</i>.<br>Đi bằng chân → chỉ một chữ <b>пешко́м</b>, không giới từ, không cách nào cả.<br>Đừng dịch máy móc thành <i>на нога́х</i> — cụm đó có nghĩa khác hẳn: "đang đứng suốt / đang ốm mà vẫn gắng gượng".</div>'
    '<div class="hd-warn"><b>Câu dùng thật:</b> <i>Я хожу́ на рабо́ту пешко́м</i> = tôi đi bộ đi làm · <i>Туда́ мо́жно дойти́ пешко́м за де́сять мину́т</i> = tới đó đi bộ mất mười phút · <i>Пойдём пешко́м?</i> = đi bộ nhé?</div>'
    '<div class="hd-warn"><b>Cả một lớp trạng từ dựng bằng cách 5 hoá thạch — nhận ra khuôn là đoán được nghĩa:</b><br>Thời gian: <b>у́тром</b> buổi sáng · <b>днём</b> ban ngày · <b>ве́чером</b> buổi tối · <b>но́чью</b> ban đêm · <b>зимо́й</b> mùa đông · <b>весно́й</b> mùa xuân · <b>ле́том</b> mùa hè · <b>о́сенью</b> mùa thu.<br>Cách thức: <b>пешко́м</b> đi bộ · <b>бего́м</b> chạy ù · <b>шёпотом</b> thì thầm.<br>Điểm chung: chúng vốn là danh từ ở cách 5 ("bằng buổi sáng", "bằng chân"), nay đã cứng lại thành trạng từ và <b>không biến đổi nữa</b>.</div>'
    '<div class="hd-warn"><b>Đừng lẫn ba cách nói về việc đi bằng chân:</b><br>• <b>идти́ пешко́м</b> = di chuyển bằng chân, nhấn <b>phương tiện</b> (đối lập với đi xe).<br>• <b>гуля́ть</b> = đi dạo, đi chơi — nhấn <b>mục đích thư giãn</b>, không có đích đến.<br>• <b>прогу́лка</b> = cuộc dạo chơi (danh từ).<br><i>Я иду́ пешко́м на рабо́ту</i> ≠ <i>Я гуля́ю в па́рке</i>.</div>'
    '<div class="hd-sec">Họ hàng — gốc пеш/пех</div>'
    '<div class="hd-fam"><b>пе́ший</b> đi bộ (tính từ) · <b>пешехо́д</b> người đi bộ (<b>пеш</b> + <b>ход</b>) · <b>пешехо́дный перехо́д</b> vạch qua đường · <b>пехо́та</b> bộ binh · <b>пе́шка</b> con tốt trong cờ vua — quân "đi bộ"</div>'
    '<div class="hd-warn">⚠️ Mức tin — một cây cầu sang tiếng Anh: gốc <b>пеш-</b> được các từ điển từ nguyên nối về gốc Ấn–Âu nghĩa "chân", cùng ổ với Latin <i>pes / pedis</i> → tiếng Anh <i>pedestrian</i> (người đi bộ), <i>pedal</i>. Đối chiếu <b>пешехо́д</b> với <i>pedestrian</i> thì thấy hai ngôn ngữ ghép cùng một ý. Đây là <b>từ nguyên</b>, không phải luật suy ra được — dùng làm móc treo trí nhớ thì tốt, đừng suy tiếp sang từ khác.</div>'
)

S["нужно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">нужн-</span><span class="hd-gloss">gốc CẦN, THIẾU — từ danh từ <b>нужда́</b> (nhu cầu, sự túng thiếu)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span><span class="hd-gloss">đuôi <b>dạng ngắn giống trung</b> của tính từ <b>ну́жный</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vì <b>-о</b> là đuôi <b>giống trung</b> nên nó không gắn với ai cả — và chính điều đó cho phép dựng câu <b>vô nhân xưng</b>: nghĩa đen là "(việc đó) là cần", từ đó ra "cần phải, phải". Cùng cỗ máy này còn có <b>мо́жно</b> (được phép), <b>нельзя́</b> (không được), <b>ва́жно</b> (quan trọng), <b>тру́дно</b> (khó).</div>'
    '<div class="hd-warn">🔴 <b>Khuôn câu số một — thuộc nguyên khuôn này là dùng được ngay:</b><br><b>КОМУ (cách 3) + ну́жно + ĐỘNG TỪ NGUYÊN THỂ</b><br><i>Мне ну́жно идти́</i> = tôi phải đi · <i>Вам ну́жно отдохну́ть</i> = anh cần nghỉ ngơi · <i>Что мне ну́жно де́лать?</i> = tôi cần làm gì?<br>Người trong câu này KHÔNG phải chủ ngữ — nó đứng cách 3. Câu tiếng Nga kiểu này không có chủ ngữ nào cả.</div>'
    '<div class="hd-warn">🔴 <b>Khuôn thứ hai — chỗ sai nhiều nhất:</b> khi thứ cần là một <b>ĐỒ VẬT</b> chứ không phải hành động, thì đồ vật đó đứng <b>cách 1</b> và <b>ну́жно phải hợp giống với nó</b>:<br><i>Мне <b>ну́жен</b> слова́рь</i> (giống đực) · <i>Мне <b>нужна́</b> по́мощь</i> (giống cái) · <i>Мне <b>ну́жно</b> вре́мя</i> (giống trung) · <i>Мне <b>нужны́</b> де́ньги</i> (số nhiều).<br>Nghĩa đen: "<b>từ điển</b> là cần đối với tôi" — cái đồ vật mới là chủ ngữ. Nắm được điều này thì bốn dạng trên không còn phải học vẹt.</div>'
    '<div class="hd-warn"><b>Quá khứ và tương lai chỉ thêm một chữ:</b> <b>бы́ло</b> / <b>бу́дет</b>.<br><i>Мне ну́жно бы́ло идти́</i> = tôi đã phải đi · <i>Мне ну́жно бу́дет идти́</i> = tôi sẽ phải đi.<br>Nhưng nếu là đồ vật thì <b>бы́ло</b> cũng hợp giống theo: <i>Мне нужна́ была́ по́мощь</i>.</div>'
    '<div class="hd-warn"><b>ну́жно hay на́до?</b> Gần như thay nhau được. Khác biệt thật:<br>• <b>на́до</b> khẩu ngữ hơn, và <b>không bao giờ hợp giống</b> — chỉ đi với động từ nguyên thể.<br>• Phủ định: <b>не ну́жно</b> / <b>не на́до</b> = không cần, đừng. <i>Не на́до!</i> = Thôi, đừng!<br>• Còn <b>до́лжен</b> thì khác hẳn về ngữ pháp: người đứng <b>cách 1</b> và từ này hợp giống với người — <i>Я до́лжен идти́</i> (nam) / <i>Я должна́ идти́</i> (nữ), nghĩa nghiêng về <b>nghĩa vụ</b>.</div>'
    '<div class="hd-warn">🔴 <b>Kiểu câu rất Nga, học sớm thì nói nghe tự nhiên hẳn:</b> sau <b>ну́жно</b> có thể <b>bỏ hẳn động từ chuyển động</b>, chỉ để lại nơi cần đến:<br><i>Мне ну́жно домо́й</i> = tôi phải về nhà · <i>Мне ну́жно в апте́ку</i> = tôi cần ra hiệu thuốc · <i>Вам ну́жно на сле́дующей</i> = anh phải xuống ở trạm sau.<br>Động từ <b>идти́</b>/<b>е́хать</b> bị lược đi vì hướng đã nói hết ý — người Nga nói kiểu này suốt ngày.</div>'
    '<div class="hd-warn"><b>Trọng âm bốn dạng ngắn — theo đúng kiểu chung của dạng ngắn tính từ:</b> <b>ну́жен</b> · <b>нужна́</b> · <b>ну́жно</b> · <b>нужны́</b>. Giống cái nhảy trọng âm ra đuôi, ba dạng kia nhấn gốc (số nhiều thì có thể nhấn cả hai chỗ).<br>⚠️ Mức tin: dạng số nhiều được từ điển ghi cả <b>нужны́</b> lẫn <b>ну́жны</b>; còn <b>нужна́</b> nhấn đuôi thì chắc chắn, đừng đọc thành <i>ну́жна</i>.</div>'
    '<div class="hd-sec">Họ hàng — gốc нужд/нужн</div>'
    '<div class="hd-fam"><b>ну́жный</b> cần thiết · <b>нужда́</b> nhu cầu; sự túng thiếu · <b>нужда́ться</b> cần đến, thiếu thốn · <b>необходи́мо</b> nhất thiết phải (mạnh hơn <b>ну́жно</b>) · <b>на́до</b> phải, cần</div>'
)

S["адрес"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được theo tiếng Nga — đây là <b>từ mượn</b>, vào Nga qua tiếng Pháp <i>adresse</i>, gốc Latin <b>ad-</b> (tới) + <b>directus</b> (chỉ thẳng). Nghĩa lõi: "chỉ dẫn để hướng cái gì tới đúng chỗ". Đừng bịa cấu trúc Nga cho nó.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa thì bạn nhận ra ngay vì nó là <i>address</i>. Cái thật sự phải học ở từ này <b>không phải nghĩa mà là SỐ NHIỀU</b> — và đó lại là một luật lớn mở khoá cả chục danh từ hay dùng.</div>'
    '<div class="hd-warn">🔴 <b>Nhóm danh từ giống đực có số nhiều đuôi -á (thay vì -ы/-и), trọng âm nhảy về cuối:</b><br><b>а́дрес → адреса́</b> · <b>дом → дома́</b> · <b>го́род → города́</b> · <b>ве́чер → вечера́</b> · <b>по́езд → поезда́</b> · <b>глаз → глаза́</b> · <b>учи́тель → учителя́</b> · <b>до́ктор → доктора́</b> · <b>па́спорт → паспорта́</b> · <b>но́мер → номера́</b><br>Nhóm này phải thuộc, nhưng nó không lớn và toàn từ bạn dùng hằng ngày, nên học một lượt là xong.</div>'
    '<div class="hd-warn">⚠️ Mức tin: có <b>dấu hiệu</b> chứ không có luật chắc — phần lớn từ trong nhóm là danh từ hai âm tiết, trọng âm số ít rơi vào âm đầu, và thường chỉ vật dụng hay chức danh quen thuộc. Dấu hiệu này giúp <b>nghi ngờ đúng chỗ</b>, không dùng để khẳng định; gặp từ mới thì vẫn phải tra.</div>'
    '<div class="hd-warn"><b>Dùng thật:</b> <i>Како́й у вас а́дрес?</i> = địa chỉ của anh là gì? · <i>дома́шний а́дрес</i> địa chỉ nhà · <i>электро́нный а́дрес</i> địa chỉ email · <i>Напиши́те а́дрес</i> = viết địa chỉ ra giúp tôi.<br>Nghĩa bóng hay gặp trên báo: <b>в а́дрес</b> + cách 2 = nhắm vào ai — <i>кри́тика в а́дрес мини́стра</i> = lời phê bình nhắm vào ông bộ trưởng.</div>'
    '<div class="hd-warn">🔴 <b>Cặp bẫy đẹp nhất của từ này — hai dạng viết giống hệt nhau, chỉ khác trọng âm:</b><br><b>а́дреса</b> (nhấn đầu) = <b>cách 2 số ít</b> — <i>но́мер а́дреса</i>.<br><b>адреса́</b> (nhấn cuối) = <b>cách 1 số nhiều</b> — <i>их адреса́</i>.<br>Đây chính là lý do người học tiếng Nga phải để tâm tới trọng âm: nó không phải trang trí, nó là <b>ngữ pháp</b>. Số ít nhấn gốc suốt (<b>а́дрес, а́дреса, а́дресу, а́дресом</b>), số nhiều nhấn đuôi suốt (<b>адреса́, адресо́в, адреса́м, адреса́ми</b>).</div>'
    '<div class="hd-warn"><b>Địa chỉ Nga viết ngược với thói quen Việt: TO trước, NHỎ sau.</b><br><i>Москва́, у́лица Ле́нина, дом 5, кварти́ра 12</i> — thành phố → phố → số nhà → số căn hộ.<br>Viết tắt bạn sẽ thấy trên phong bì và trong đơn từ: <b>ул.</b> = <b>у́лица</b> phố · <b>пр.</b> = <b>проспе́кт</b> đại lộ · <b>д.</b> = <b>дом</b> · <b>кв.</b> = <b>кварти́ра</b> · <b>и́ндекс</b> = mã bưu chính.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>адреса́т</b> người nhận · <b>адресова́ть</b> gửi tới, nhắm tới · <b>а́дресный</b> thuộc địa chỉ, có địa chỉ cụ thể · và cùng gốc Latin <i>directus</i>: <b>дире́ктор</b> giám đốc (người "chỉ hướng"), <b>директи́ва</b> chỉ thị</div>'
)

S["схема"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được theo tiếng Nga — từ mượn Hy Lạp <i>skhēma</i> = hình dạng, dáng vẻ, bố cục. Chú ý: chữ <b>с</b> đầu từ ở đây <b>không phải</b> tiền tố Nga <b>с-</b>, nó nằm trong từ gốc. Đừng chẻ nhầm thành <b>с</b> + <i>хема</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng một từ Hy Lạp đã cho tiếng Anh <i>scheme</i>, <i>schema</i>, <i>schematic</i>. Nhưng <b>nghĩa hai bên lệch nhau</b>, và đây mới là chỗ đáng nhớ: tiếng Anh <i>scheme</i> nghiêng về "kế hoạch, mưu đồ"; tiếng Nga <b>схе́ма</b> nghĩa thường gặp nhất là <b>SƠ ĐỒ, BẢN VẼ</b>.</div>'
    '<div class="hd-warn"><b>Dùng thật trong việc đi lại — nghĩa bạn sẽ gặp trước tiên:</b><br><i>схе́ма метро́</i> = bản đồ tuyến tàu điện ngầm (tấm sơ đồ dán trong toa) · <i>схе́ма прое́зда</i> = sơ đồ đường đi tới địa chỉ · <i>схе́ма ли́ний</i> = sơ đồ các tuyến · <i>по схе́ме</i> = theo sơ đồ, theo đúng bài bản.</div>'
    '<div class="hd-warn"><b>Chọn đúng từ trong bốn từ dễ lẫn:</b><br>• <b>схе́ма</b> = sơ đồ, bản vẽ giản lược (metro, mạch điện).<br>• <b>ка́рта</b> = bản đồ địa lý — và cũng là <b>thẻ</b> (ngân hàng, chơi bài).<br>• <b>план</b> = mặt bằng, bản đồ thành phố; và "kế hoạch".<br>• <b>чертёж</b> = bản vẽ kỹ thuật đúng tỉ lệ.</div>'
    '<div class="hd-warn"><b>Giống và biến cách:</b> đuôi <b>-а</b> ⇒ <b>giống cái</b>, biến cách hoàn toàn đều và <b>trọng âm đứng yên ở gốc</b> suốt mọi cách: <b>схе́ма</b> · <b>схе́мы</b> · <b>схе́ме</b> · <b>схе́му</b> · <b>схе́мой</b> · о <b>схе́ме</b>. Với từ mượn thì đây là tin tốt: không có gì bất thường phải nhớ.</div>'
    '<div class="hd-warn">Nghĩa "mưu đồ" kiểu tiếng Anh <b>cũng có</b> trong tiếng Nga hiện đại, nhưng là nghĩa phái sinh và luôn đi kèm từ chỉ rõ: <i>моше́нническая схе́ма</i> = chiêu lừa đảo, <i>се́рая схе́ма</i> = cách làm ăn lách luật. Một mình chữ <b>схе́ма</b> thì trung tính.</div>'
    '<div class="hd-warn"><b>Một cặp hậu tố mở khoá cả lớp từ — gặp ngay ở chính từ này:</b><br>• <b>-и́ческий</b> = <b>thuộc về, có tính chất khách quan</b>, không khen chê: <b>схемати́ческий</b> (dạng sơ đồ) · <b>истори́ческий</b> (thuộc lịch sử) · <b>экономи́ческий</b> (thuộc kinh tế) · <b>класси́ческий</b> (cổ điển).<br>• <b>-и́чный</b> = <b>mang tính chất ấy ở mức đánh giá</b>, thường có sắc thái: <b>схемати́чный</b> (sơ sài quá, thiếu chi tiết — chê) · <b>истори́чный</b> (đúng với lịch sử) · <b>экономи́чный</b> (tiết kiệm) · <b>логи́чный</b> (hợp lý).<br>Nhớ một cặp là đọc được hàng trăm tính từ quốc tế: dạng dài <b>-ический</b> tả loại, dạng ngắn <b>-ичный</b> tả mức độ.</div>'
    '<div class="hd-warn"><b>Chỗ bạn sẽ gặp từ này sớm nhất:</b> trong toa tàu điện ngầm luôn treo tấm <b>схе́ма</b> các tuyến, và khi hỏi đường ai đó sẽ nói <i>Посмотри́те на схе́му</i> = anh nhìn sơ đồ đi. Bản đồ giấy cầm tay thì lại là <b>ка́рта</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>схемати́ческий</b> mang tính sơ đồ · <b>схемати́чный</b> giản lược, sơ sài (chê) · <b>схемати́чно</b> một cách sơ lược · cùng gốc Hy Lạp trong tiếng Anh: <i>scheme</i>, <i>schema</i>, <i>schematic</i></div>'
)

S["переход"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пере-</span><span class="hd-gloss">QUA, SANG BÊN KIA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ход</span><span class="hd-gloss">gốc ĐI — dạng danh từ trần của <b>ходи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">(không đuôi)</span><span class="hd-gloss">danh từ giống đực kết thúc bằng phụ âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: "<b>cái sự đi qua</b>" — rồi thành "<b>chỗ để đi qua</b>". Đây là một cỗ máy tạo danh từ cực rẻ: lấy động từ có tiền tố, <b>cắt trụi đuôi</b> là ra danh từ.<br><b>входи́ть → вход</b> lối vào · <b>выходи́ть → вы́ход</b> lối ra · <b>переходи́ть → перехо́д</b> lối qua · <b>приходи́ть → прихо́д</b> sự đến · <b>проходи́ть → прохо́д</b> lối đi.</div>'
    '<div class="hd-warn"><b>Ba nghĩa hay gặp, tất cả đều là "chỗ/việc đi qua":</b><br>① <b>Lối qua đường</b> — <i>пешехо́дный перехо́д</i> vạch kẻ qua đường, <i>подзе́мный перехо́д</i> hầm bộ hành. Biển báo ngoài phố ghi đúng chữ <i>ПЕРЕХОД</i>.<br>② <b>Đường nối giữa hai tuyến metro</b> — <i>перехо́д на Кольцеву́ю ли́нию</i> = lối chuyển sang tuyến Vành đai. Nghe thông báo trong tàu là gặp.<br>③ <b>Sự chuyển đổi</b> (trừu tượng) — <i>перехо́д к ры́ночной эконо́мике</i>, <i>перехо́дный пери́од</i> giai đoạn chuyển tiếp.</div>'
    '<div class="hd-warn"><b>Động từ đi kèm và cách nó đòi:</b> <b>переходи́ть</b> / <b>перейти́</b> + <b>cách 4 thẳng, không giới từ</b> — <i>перейти́ у́лицу</i> = qua đường. Cũng nói được <i>перейти́ че́рез у́лицу</i>, nghĩa như nhau, nhấn "băng ngang" hơn.<br>Còn <b>перейти́ на</b> + cách 4 = chuyển sang (tuyến khác, việc khác, chủ đề khác).</div>'
    '<div class="hd-warn"><b>Giống, số:</b> giống đực, số nhiều <b>перехо́ды</b>, trọng âm đứng yên ở <b>-хо́-</b> qua mọi cách. Danh từ nhóm <b>-ход</b> nhìn chung rất ngoan, không có nguyên âm chạy.</div>'
    '<div class="hd-sec">Họ hàng — gốc ход</div>'
    '<div class="hd-fam"><b>ход</b> bước đi; nước cờ · <b>ходи́ть</b> đi lại · <b>вход</b> lối vào · <b>вы́ход</b> lối ra · <b>выходно́й</b> ngày nghỉ · <b>прохо́д</b> lối đi · <b>похо́д</b> chuyến đi bộ · <b>дохо́д</b> thu nhập · <b>пешехо́д</b> người đi bộ · <b>парохо́д</b> tàu thuỷ (đi bằng "hơi" <b>пар</b>)</div>'
    + HE_PERE
)

S["пересадка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пере-</span><span class="hd-gloss">CHUYỂN SANG chỗ khác</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сад-</span><span class="hd-gloss">gốc ĐẶT NGỒI, ĐẶT XUỐNG — thấy trong <b>сади́ться</b>, <b>посади́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-а</span><span class="hd-gloss">hậu tố tạo danh từ chỉ HÀNH ĐỘNG, giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: "<b>sự đặt ngồi sang chỗ khác</b>". Từ đúng một hình ảnh đó mọc ra ba nghĩa mà từ điển liệt kê tưởng như rời rạc:<br>• <b>đổi tàu / đổi xe / quá cảnh</b> — đứng dậy khỏi ghế này, ngồi sang ghế kia;<br>• <b>cấy ghép</b> (y học) — <i>переса́дка се́рдца</i>, "đặt quả tim sang chỗ khác". Tiếng Anh <i>transplant</i> = <i>trans</i> (qua) + <i>plant</i> (trồng) là <b>đúng cùng một hình ảnh</b>;<br>• <b>sang chậu, trồng lại cây</b> — <i>переса́дка расте́ний</i>.</div>'
    '<div class="hd-warn"><b>Dùng khi đi lại — nhớ nguyên cụm:</b><br><i>сде́лать переса́дку</i> = đổi tuyến, chuyển tàu (dùng động từ <b>сде́лать</b>, không phải "làm" nào khác) · <i>по́езд без переса́док</i> = tàu chạy thẳng · <i>биле́т с переса́дкой</i> = vé có quá cảnh · <i>Здесь переса́дка на кра́сную ли́нию</i>.</div>'
    '<div class="hd-warn"><b>Động từ tương ứng:</b> <b>переса́живаться</b> / <b>пересе́сть</b> = đổi chỗ ngồi, đổi tàu — chia <b>переся́ду</b>, <b>переся́дешь</b>, <b>переся́дут</b>; quá khứ <b>пересе́л</b>.<br><i>Вам ну́жно пересе́сть на друго́й авто́бус</i> = anh phải đổi sang xe buýt khác.</div>'
    '<div class="hd-warn">🔴 <b>Một gốc, ba mặt — biến âm cổ đã tách nó ra, nhưng nghĩa vẫn dính nhau:</b><br><b>сид-</b> trạng thái: <b>сиде́ть</b> đang ngồi · <b>сес-</b> một lần: <b>сесть</b> ngồi xuống, lên xe · <b>сад-</b> quá trình / phái sinh: <b>сади́ться</b> đang ngồi xuống, <b>сад</b> khu vườn (nơi cây được ĐẶT xuống!), <b>поса́дка</b> việc lên tàu; việc hạ cánh.<br><i>Сади́тесь, пожа́луйста</i> = mời ngồi — câu lịch sự chuẩn.</div>'
    '<div class="hd-sec">Họ hàng — gốc сад/сид/сес</div>'
    '<div class="hd-fam"><b>сади́ться</b> ngồi xuống; lên xe · <b>сесть</b> ngồi xuống (một lần) · <b>сиде́ть</b> đang ngồi · <b>посади́ть</b> đặt ngồi; trồng cây · <b>сад</b> vườn · <b>поса́дка</b> sự lên tàu; sự hạ cánh · <b>пересе́сть</b> đổi chỗ · <b>заса́да</b> ổ phục kích</div>'
    + HE_PERE
)

S["остановка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span><span class="hd-gloss">tiền tố mang sắc thái HOÀN TẤT, làm cho thành ra</span></div>'
    '<div class="hd-row"><span class="hd-piece">-стан-</span><span class="hd-gloss">gốc ĐỨNG, DỪNG — cùng ổ với <b>стать</b>, <b>стоя́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ов-</span><span class="hd-gloss">mảnh nối, không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-а</span><span class="hd-gloss">hậu tố danh từ hành động — và từ đó ra NƠI xảy ra hành động</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen "<b>sự dừng lại</b>", rồi trượt sang "<b>chỗ dừng</b>" — đúng cỗ máy <b>-ка</b> ta vừa thấy ở <b>переса́дка</b> và <b>поса́дка</b>: hậu tố này đặt tên cho hành động, và tiếng Nga rất hay dùng chính cái tên đó để gọi luôn địa điểm.</div>'
    '<div class="hd-warn">🔴 <b>Ba từ tiếng Việt đều dịch là "ga/trạm" — chọn sai là lộ ngay:</b><br>• <b>остано́вка</b> = trạm xe buýt, trạm xe điện (ngoài phố, chỉ là cái biển và mái che).<br>• <b>ста́нция</b> = ga tàu điện ngầm, ga xép — <i>ста́нция метро́</i>.<br>• <b>вокза́л</b> = nhà ga lớn của tàu hoả (toà nhà) — <i>Ки́евский вокза́л</i>.</div>'
    '<div class="hd-warn"><b>Dùng thật khi đi xe:</b><br><i>Вам две остано́вки</i> = anh đi hai trạm nữa · <i>Сле́дующая остано́вка…</i> = trạm kế tiếp là… (câu loa trên xe) · <i>Вы выхо́дите на сле́дующей?</i> = anh có xuống trạm sau không? · <i>без остано́вки</i> = không ngừng nghỉ.</div>'
    '<div class="hd-warn"><b>Động từ tương ứng — chú ý chữ -ся đổi hẳn nghĩa:</b><br><b>останови́ть</b> = làm cho cái gì dừng lại (có tân ngữ cách 4): <i>Останови́те маши́ну</i>.<br><b>останови́ться</b> = tự dừng lại; <b>và</b> = trọ lại, ở tạm: <i>Я останови́лся в гости́нице</i> = tôi trọ ở khách sạn.<br>Chia: <b>остановлю́сь</b> · <b>остано́вишься</b> · <b>остано́вятся</b> — biến âm <b>в→вл</b> chỉ ở ngôi <b>я</b>, đúng luật lớp 2.<br><i>Останови́тесь здесь, пожа́луйста</i> = cho tôi dừng ở đây (nói với tài xế).</div>'
    '<div class="hd-warn">⚠️ Mức tin — một cây cầu đáng nhớ: <b>ста́нция</b> là từ mượn từ Latin <i>statio</i> (chỗ đứng), mà <i>statio</i> lại cùng gốc Ấn–Âu với chính <b>стоя́ть</b> của tiếng Nga; tiếng Anh <i>stand</i>, <i>station</i>, <i>stable</i> cũng cùng ổ đó. Đây là <b>từ nguyên</b>, không phải luật suy ra được — nhưng nó giải thích vì sao hai từ Nga trông xa lạ mà nghĩa lại chồng lên nhau.</div>'
    '<div class="hd-warn">🔴 <b>Nguyên âm chạy — luật của mọi danh từ đuôi -ка:</b> ở <b>cách 2 số nhiều</b>, giữa hai phụ âm cuối mọc thêm một nguyên âm để đọc được:<br><b>остано́вка → остано́вок</b> · <b>переса́дка → переса́док</b> · <b>де́вушка → де́вушек</b> · <b>ло́жка → ло́жек</b> · <b>ма́рка → ма́рок</b><br>Chọn <b>о</b> hay <b>е</b> thì theo phụ âm đứng trước: sau phụ âm cứng ra <b>о</b>, sau phụ âm mềm hoặc <b>ш ж ч щ</b> ra <b>е</b>. Vì vậy mới có <i>по́езд без переса́док</i> chứ không phải <i>без пересадк</i>.</div>'
    '<div class="hd-sec">Họ hàng — gốc ста/стан</div>'
    '<div class="hd-fam"><b>останови́ть</b> làm dừng · <b>останови́ться</b> dừng lại; trọ lại · <b>стоя́ть</b> đứng · <b>стоя́нка</b> bãi đỗ xe · <b>ста́нция</b> ga · <b>стать</b> trở thành; đứng lại · <b>встать</b> đứng dậy · <b>оста́ться</b> ở lại · <b>постоя́нный</b> thường xuyên, cố định</div>'
)
