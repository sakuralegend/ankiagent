# -*- coding: utf-8 -*-
"""k54 — actions: LÔ SỬA. 19 thẻ động từ đã có nội dung tốt; việc của lô này là
(1) BỎ HẲN hai khối hệ thống dùng chung lặp ở gần như mọi thẻ ("Cặp thể — khái
niệm đắt nhất…" và "Hai lớp chia động từ", cộng "Luật biến âm ngôi tôi" và "Bộ
ba bữa ăn"), (2) hạ mỗi thẻ xuống tối đa 2 ô đỏ, (3) bảo đảm thẻ nào cũng có mục
"Họ hàng" thật. Mỗi thẻ đứng một mình — xem README §2b và §3."""

# 🔴 KHÔNG dựng biến khối dùng chung rồi cộng vào mọi thẻ — xem README §3.

S = {}
V = {}

S["видеть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вид-</span>'
    '<span class="hd-gloss">THẤY — chính là <b>вид</b> (quang cảnh, dáng vẻ)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-еть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>вид-</b> cùng nguồn Ấn–Âu với Latin <i>videre</i> (nhìn), '
    'từ đó ra tiếng Anh <i>video</i>, <i>evident</i>. Thấy <b>вид</b> là thấy chuyện NHÌN.</div>'
    '<div class="hd-warn"><b>Chia phải thuộc:</b> đuôi <b>-еть</b> thường báo lớp 1, '
    'nhưng <b>ви́деть</b> chia theo <b>LỚP 2</b> — cùng nhóm ngoại lệ với '
    '<b>смотре́ть</b>, <b>терпе́ть</b>, <b>зави́сеть</b>. Ngôi "tôi" biến âm '
    '<b>д→ж</b>: <b>ви́жу</b>, rồi <b>ви́дишь, ви́дит… ви́дят</b> trở lại bình thường.</div>'
    '<div class="hd-warn"><b>Cặp dễ lẫn:</b> <b>ви́деть</b> = thấy (mắt bắt được, không chủ ý) '
    '↔ <b>смотре́ть</b> = nhìn, xem (có chủ ý). Đúng như <i>see</i> ↔ <i>watch</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вид</b> quang cảnh; thể (ngữ pháp) · <b>уви́деть</b> nhìn thấy (HT) · '
    '<b>свида́ние</b> cuộc hẹn · <b>ви́дно</b> có thể thấy, rõ ràng · '
    '<b>до свида́ния</b> tạm biệt (nghĩa đen: cho tới lần gặp lại)</div>'
)

S["гулять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">гул-</span>'
    '<span class="hd-gloss">gốc trơn, nghĩa DẠO CHƠI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ять</span>'
    '<span class="hd-gloss">đuôi nguyên thể, lớp 1: <b>гуля́ю, гуля́ешь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không phải "đi bộ" theo nghĩa di chuyển, mà là <b>đi dạo cho thư thái</b> '
    '— ra ngoài chơi, không nhằm tới đâu cả. Đây là một hoạt động có vị trí hẳn hoi trong '
    'đời sống Nga: <b>гуля́ть в па́рке</b>.</div>'
    '<div class="hd-warn"><b>Tiếng Nga bắt bạn chọn, không có từ "đi" chung chung:</b> '
    '<b>идти́</b> đang đi bộ tới đâu đó · <b>ходи́ть</b> đi bộ thường xuyên · '
    '<b>е́хать</b> đi bằng xe · <b>гуля́ть</b> đi dạo chơi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>погуля́ть</b> dạo một lát (HT) · <b>прогу́лка</b> cuộc dạo chơi · '
    '<b>прогу́ливать</b> trốn học, trốn làm</div>'
)

S["думать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дум-</span>'
    '<span class="hd-gloss">NGHĨ — <b>ду́ма</b> = ý nghĩ (và là tên Quốc hội Nga)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">đuôi nguyên thể, lớp 1</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là <b>động từ mẫu</b> của lớp 1 — chia đều tăm tắp, không biến âm, '
    'không rụng chữ: <b>ду́маю, ду́маешь, ду́мает, ду́маем, ду́маете, ду́мают</b>. '
    'Thuộc bộ đuôi ở đây rồi áp cho hàng trăm động từ <b>-ать</b> khác.</div>'
    '<div class="hd-warn"><b>Cách nó đòi — phải thuộc:</b> <b>ду́мать о</b> + cách 6 = nghĩ VỀ. '
    '<i>Я ду́маю о тебе́</i> = Tôi nghĩ về bạn. Học động từ Nga là học luôn cái cách nó kéo theo.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ду́ма</b> ý nghĩ · <b>поду́мать</b> nghĩ (HT) · '
    '<b>приду́мать</b> nghĩ ra, bịa ra · <b>заду́мчивый</b> trầm ngâm · '
    '<b>вы́думка</b> điều bịa ra</div>'
)

S["жить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">жи-</span>'
    '<span class="hd-gloss">SỐNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một trong những động từ cốt lõi nhất, và là ví dụ sạch của luật '
    '<b>ЖИ viết И</b>.</div>'
    '<div class="hd-warn"><b>Chia BẤT THƯỜNG — phải thuộc lòng:</b> gốc mọc thêm <b>-в-</b> khi chia: '
    '<b>живу́, живёшь, живёт, живём, живёте, живу́т</b>. Nguyên thể không hề báo trước điều đó, '
    'nên đây là từ không suy được, chỉ nhớ được.</div>'
    '<div class="hd-warn"><b>Cách nó đòi:</b> <b>жить в</b> + cách 6 = sống ở đâu. '
    '<i>Я живу́ в Москве́</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>жизнь</b> cuộc sống · <b>живо́й</b> sống, sinh động · '
    '<b>жи́тель</b> cư dân · <b>живо́тное</b> con vật · '
    '<b>живо́т</b> cái bụng (xưa nghĩa là "sự sống")</div>'
)

S["завтракать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">завтрак-</span>'
    '<span class="hd-gloss"><b>за́втрак</b> — BỮA SÁNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">đuôi nguyên thể, lớp 1</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiếng Nga không ghép "ăn + sáng" như tiếng Việt: nó lấy thẳng '
    '<b>tên bữa ăn</b> rồi dán <b>-ать</b> vào là thành động từ. Cùng khuôn: '
    '<b>обе́д → обе́дать</b>, <b>у́жин → у́жинать</b>.</div>'
    '<div class="hd-why">Bản thân <b>за́втрак</b> cũng chẻ được: <b>за</b> (cho, vào lúc) + '
    '<b>у́тро</b> (buổi sáng) — "phần dành cho buổi sáng"; cùng nguồn với <b>за́втра</b> '
    '(ngày mai), vốn nghĩa "vào sáng hôm sau".</div>'
    '<div class="hd-warn">⚠️ Mức tin: mối liên hệ <b>за́втрак ↔ за́втра</b> là <b>từ nguyên</b>, '
    'không phải luật bạn suy ra được — nhưng nó có thật và giúp nhớ hai từ cùng lúc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>за́втрак</b> bữa sáng · <b>поза́втракать</b> ăn sáng xong (HT) · '
    '<b>за́втра</b> ngày mai</div>'
)

S["звонить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">звон-</span>'
    '<span class="hd-gloss">TIẾNG CHUÔNG — <b>звон</b> = tiếng ngân</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi nguyên thể, lớp 2: <b>звоню́, звони́шь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc là <b>rung chuông</b>; tới thời có điện thoại thì thành '
    '<b>gọi điện</b> — vì máy cũng đổ chuông. Hình ảnh vẫn còn nguyên trong từ.</div>'
    '<div class="hd-warn"><b>TRỌNG ÂM — bẫy nổi tiếng nhất tiếng Nga hiện đại:</b> chuẩn mực là '
    '<b>звони́т</b>, <b>звоня́т</b> (nhấn đuôi). Rất nhiều người Nga nói <i>зво́нит</i> và bị coi '
    'là nói sai. Bạn cứ nhấn đuôi là an toàn.</div>'
    '<div class="hd-warn"><b>Cách nó đòi:</b> <b>звони́ть кому́</b> + cách 3 = gọi CHO ai. '
    '<i>Я звоню́ ма́ме</i> — không phải cách 4 như tiếng Việt "gọi ai".</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>позвони́ть</b> gọi điện (HT) · <b>звон</b> tiếng chuông · '
    '<b>звоно́к</b> cú điện thoại; chuông cửa · <b>звене́ть</b> ngân vang</div>'
)

S["играть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">игр-</span>'
    '<span class="hd-gloss"><b>игра́</b> — TRÒ CHƠI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">đuôi nguyên thể, lớp 1: <b>игра́ю, игра́ешь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-warn"><b>Điểm đáng giá nhất của từ này là giới từ đi kèm — chọn sai là sai hẳn:</b> '
    '<b>игра́ть в</b> + cách 4 cho TRÒ CHƠI, MÔN THỂ THAO (<b>игра́ть в футбо́л</b>) · '
    '<b>игра́ть на</b> + cách 6 cho NHẠC CỤ (<b>игра́ть на гита́ре</b>).</div>'
    '<div class="hd-why">Mẹo phân biệt: thể thao thì bạn ở <b>trong</b> cuộc chơi (<b>в</b>), '
    'còn nhạc cụ thì bạn gảy <b>trên</b> mặt đàn (<b>на</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>игра́</b> trò chơi, ván đấu · <b>сыгра́ть</b> chơi một ván (HT) · '
    '<b>игру́шка</b> đồ chơi · <b>игро́к</b> người chơi</div>'
)

S["обедать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">обед-</span>'
    '<span class="hd-gloss"><b>обе́д</b> — BỮA TRƯA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">đuôi nguyên thể, lớp 1</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Lại đúng khuôn "tên bữa ăn + <b>-ать</b>" như <b>за́втракать</b> và '
    '<b>у́жинать</b>: một tên bữa là một động từ, khỏi ghép hai chữ.</div>'
    '<div class="hd-warn"><b>Sắc thái dùng thật:</b> <b>обе́д</b> ở Nga là bữa <b>chính</b> trong ngày, '
    'thường có xúp — không nhẹ như bữa trưa ta quen. Vì thế <b>обе́денный переры́в</b> '
    '(giờ nghỉ trưa) là một phần cố định của ngày làm việc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обе́д</b> bữa trưa · <b>пообе́дать</b> ăn trưa xong (HT) · '
    '<b>обе́денный</b> thuộc về bữa trưa</div>'
)

S["повторять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố</span></div>'
    '<div class="hd-row"><span class="hd-piece">-втор-</span>'
    '<span class="hd-gloss">THỨ HAI — chính là <b>второ́й</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ять</span>'
    '<span class="hd-gloss">đuôi nguyên thể, lớp 1</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen đẹp và trong: <b>làm lần thứ HAI</b> = lặp lại, ôn lại. '
    'Thấy <b>втор</b> là thấy số 2. Từ này bạn dùng suốt đời học — '
    '<b>повторя́ть слова́</b> = ôn từ vựng, đúng việc bạn làm với Anki mỗi ngày.</div>'
    '<div class="hd-warn"><b>Cặp thể đổi cả lớp chia:</b> <b>повторя́ть</b> (chưa HT, ôn đi ôn lại) / '
    '<b>повтори́ть</b> (HT, nhắc lại một lần). Đuôi đổi <b>-ять → -ить</b> nên dạng HT '
    'chuyển sang <b>lớp 2</b>: <b>повторю́, повтори́шь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>второ́й</b> thứ hai · <b>вто́рник</b> thứ Ba (ngày thứ HAI của tuần Nga, '
    'vì tuần bắt đầu từ thứ Hai) · <b>повторе́ние</b> sự ôn tập</div>'
)

S["понимать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ним-</span>'
    '<span class="hd-gloss">LẤY, NẮM — cùng gốc với <b>-я-/-ём-</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">đuôi nguyên thể, lớp 1</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>NẮM ĐƯỢC</b> — hiểu tức là túm được ý. Chính gốc bạn đã gặp ở '
    '<b>подъём</b> và <b>объём</b>, nay hiện ra dưới mặt nạ <b>-ним-</b>.</div>'
    '<div class="hd-why">Tiếng Anh dùng đúng ẩn dụ đó: <i>to grasp an idea</i>; và '
    '<i>comprehend</i> ← Latin <i>com-</i> + <i>prehendere</i> = <b>túm lấy</b>.</div>'
    '<div class="hd-warn"><b>Cặp thể ĐỔI MẶT rất mạnh:</b> <b>понима́ть</b> (chưa HT) / '
    '<b>поня́ть</b> (HT). Hai từ trông khác hẳn nhau mà vẫn là một cặp — kiểu cặp buộc phải '
    'nhớ nguyên đôi, không suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поня́ть</b> hiểu ra (HT) · <b>поня́тно</b> đã rõ · '
    '<b>приня́ть</b> nhận · <b>заня́ть</b> chiếm, mượn · <b>подня́ть</b> nâng lên · '
    '<b>сня́ть</b> cởi ra, thuê</div>'
)

S["проверять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">XUYÊN QUA, làm suốt lượt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вер-</span>'
    '<span class="hd-gloss">TIN — chính là <b>ве́ра</b> (niềm tin), <b>ве́рить</b> (tin)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ять</span>'
    '<span class="hd-gloss">đuôi nguyên thể, lớp 1</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>rà suốt lượt xem có tin được không</b> = kiểm tra. '
    'Tiếng Anh <i>verify</i> đi cùng đường: ← Latin <i>verus</i> = thật.</div>'
    '<div class="hd-why">Tiền tố <b>про-</b> đáng thuộc, thường mang ý "xuyên suốt, từ đầu đến cuối": '
    '<b>прочита́ть</b> đọc hết · <b>пройти́</b> đi qua · <b>проду́мать</b> nghĩ cho thấu.</div>'
    '<div class="hd-warn"><b>Cặp thể:</b> <b>проверя́ть</b> (chưa HT) / <b>прове́рить</b> (HT) — '
    'lại đúng khuôn <b>-ять/-ить</b> như <b>повторя́ть/повтори́ть</b>. Nhận ra khuôn này thì '
    'đoán được dạng còn lại của rất nhiều động từ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>прове́рить</b> kiểm tra (HT) · <b>прове́рка</b> cuộc kiểm tra · '
    '<b>ве́рить</b> tin · <b>ве́ра</b> niềm tin · <b>ве́рный</b> đúng, trung thành · '
    '<b>уве́рен</b> chắc chắn</div>'
)

S["рисовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рис-</span>'
    '<span class="hd-gloss">VẼ — mượn qua tiếng Ba Lan từ tiếng Đức <i>reißen</i> (vạch nét)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ов-ать</span>'
    '<span class="hd-gloss">hậu tố + đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhớ theo khuôn chia thì chắc hơn nhớ theo gốc: <b>-ова-</b> rụng, thay bằng '
    '<b>-у-</b> — <b>рису́ю, рису́ешь</b>. Đúng lớp <b>-овать</b> bạn thấy ở '
    '<b>целова́ть → целу́ю</b> và <b>танцева́ть → танцу́ю</b>.</div>'
    '<div class="hd-warn"><b>Bẫy nghĩa:</b> <b>рис</b> đứng một mình nghĩa là <b>GẠO</b>, '
    'chẳng liên quan gì tới vẽ. Hai từ trùng mặt chữ, khác gốc hoàn toàn — đừng nối chúng lại.</div>'
    '<div class="hd-warn"><b>Cặp thể:</b> <b>рисова́ть</b> / <b>нарисова́ть</b>. Tiền tố hoàn thành '
    'ở đây là <b>на-</b> chứ không phải <b>по-</b> — không có luật chọn tiền tố, phải nhớ từng từ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>нарисова́ть</b> vẽ xong (HT) · <b>рису́нок</b> bức vẽ · '
    '<b>рисова́ние</b> việc vẽ</div>'
)

S["сказать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">tiền tố hoàn thành (làm trọn một lần)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-каз-</span>'
    '<span class="hd-gloss">CHỈ RA, phô ra, nói ra</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>каз-</b> nghĩa "làm cho thấy" — nói ra là phô ý mình ra. '
    'Nó sinh cả một họ lớn mà bạn sẽ gặp liên tục.</div>'
    '<div class="hd-warn"><b>CẶP THỂ BẤT THƯỜNG, phải nhớ nguyên đôi:</b> '
    '<b>говори́ть</b> (chưa HT) / <b>сказа́ть</b> (HT) — hai từ <b>khác gốc hoàn toàn</b> '
    'mà vẫn là một cặp. Cách dùng gọn: kể lể, trò chuyện, nói một thứ tiếng → <b>говори́ть</b>; '
    'nói bật ra một câu cụ thể → <b>сказа́ть</b>.</div>'
    '<div class="hd-warn"><b>Chia bất quy tắc:</b> <b>скажу́, ска́жешь, ска́жет… ска́жут</b> — '
    'chữ <b>з</b> đổi thành <b>ж</b> ở MỌI ngôi, khác luật thường vốn chỉ đổi ở ngôi "tôi".</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>показа́ть</b> cho xem · <b>рассказа́ть</b> kể lại · '
    '<b>ска́зка</b> truyện cổ tích (cái được kể) · <b>прика́з</b> mệnh lệnh · '
    '<b>отказа́ться</b> từ chối</div>'
)

S["спросить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">tiền tố hoàn thành</span></div>'
    '<div class="hd-row"><span class="hd-piece">-прос-</span>'
    '<span class="hd-gloss">HỎI, XIN — cùng gốc <b>проси́ть</b> (xin)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi nguyên thể, lớp 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một gốc <b>прос-</b> sinh ra hai việc rất gần nhau: <b>проси́ть</b> = xin '
    '(mong được cho), <b>спроси́ть</b> = hỏi (mong được trả lời). Tiếng Việt tách hẳn hai từ, '
    'tiếng Nga thấy chúng cùng một gốc.</div>'
    '<div class="hd-warn"><b>Ngôi "tôi" biến âm:</b> <b>спрошу́</b> (с→ш), nhưng '
    '<b>спро́сишь, спро́сит… спро́сят</b> giữ nguyên. Đúng luật chung của lớp 2 — chỉ ngôi '
    '<b>я</b> đổi phụ âm cuối gốc.</div>'
    '<div class="hd-warn"><b>Cặp thể phải nhớ đôi:</b> <b>спра́шивать</b> (chưa HT) / '
    '<b>спроси́ть</b> (HT). Dạng chưa hoàn thành mọc thêm <b>-ива-</b> và đổi cả nguyên âm gốc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>проси́ть</b> xin, nhờ · <b>спра́шивать</b> hỏi (chưa HT) · '
    '<b>вопро́с</b> câu hỏi · <b>про́сьба</b> lời thỉnh cầu</div>'
)

S["спрягаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">CÙNG, gộp lại</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пряг-</span>'
    '<span class="hd-gloss">BUỘC, THẮNG (ngựa vào xe)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-аться</span>'
    '<span class="hd-gloss">đuôi nguyên thể + <b>-ся</b> phản thân</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hình ảnh gốc rất cụ thể: <b>thắng mấy con ngựa vào chung một cỗ xe</b>. '
    'Chia động từ cũng là buộc một gốc vào cả bộ đuôi cho sáu ngôi. Tiếng Anh trùng khít: '
    '<i>conjugate</i> ← Latin <i>con-</i> (cùng) + <i>iugum</i> (cái ách buộc bò).</div>'
    '<div class="hd-warn"><b>Đây là thuật ngữ trong sách giáo khoa của bạn:</b> '
    '<b>глаго́л спряга́ется</b> = động từ được chia. Đuôi <b>-ся</b> ở đây mang nghĩa '
    '<b>bị động</b> — "được chia", chứ không phải "tự chia mình".</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>спряже́ние</b> sự chia động từ; lớp chia · <b>спряга́ть</b> chia (động từ) · '
    '<b>запря́чь</b> thắng ngựa vào xe · <b>упря́жка</b> bộ yên cương</div>'
)

S["танцевать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">танц-</span>'
    '<span class="hd-gloss"><b>та́нец</b> — ĐIỆU NHẢY (mượn từ tiếng Đức <i>Tanz</i>); '
    'chữ <b>е</b> rụng khi thêm đuôi, như <b>ве́тер → ве́треный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ев-ать</span>'
    '<span class="hd-gloss">hậu tố + đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ quốc tế — bạn đã biết qua <i>dance</i>. Việc duy nhất phải học là '
    'bộ đuôi.</div>'
    '<div class="hd-warn"><b>Chia:</b> <b>танцу́ю, танцу́ешь</b> — <b>-ева-</b> rụng, thay bằng '
    '<b>-у-</b>, đúng khuôn <b>целова́ть → целу́ю</b>, <b>рисова́ть → рису́ю</b>.</div>'
    '<div class="hd-warn"><b>Vì sao là -ев- chứ không -ов-:</b> sau <b>ц</b> (và ж, ч, ш, щ), '
    '<b>о</b> không mang trọng âm phải viết thành <b>е</b>. Luật chính tả này chạy khắp '
    'tiếng Nga, không riêng từ này.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>та́нец</b> điệu nhảy · <b>потанцева́ть</b> nhảy một lát (HT) · '
    '<b>танцо́р</b> vũ công · <b>та́нцы</b> buổi khiêu vũ</div>'
)

S["ужинать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ужин-</span>'
    '<span class="hd-gloss"><b>у́жин</b> — BỮA TỐI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">đuôi nguyên thể, lớp 1</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hoàn tất bộ ba theo trục thời gian trong ngày: '
    '<b>за́втрак → обе́д → у́жин</b>, mỗi tên bữa dán <b>-ать</b> là thành động từ, '
    'cả ba chia y hệt nhau và cả ba lấy <b>по-</b> làm dạng hoàn thành.</div>'
    '<div class="hd-warn"><b>Trọng âm đứng yên ở chữ у đầu từ</b> qua mọi ngôi: '
    '<b>у́жинаю, у́жинаешь, у́жинают</b> — không dịch đi đâu cả.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>у́жин</b> bữa tối · <b>поу́жинать</b> ăn tối xong (HT)</div>'
)

S["учиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">уч-</span>'
    '<span class="hd-gloss">DẠY / HỌC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-</span>'
    '<span class="hd-gloss">nguyên âm nối, lớp 2</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ться</span>'
    '<span class="hd-gloss">đuôi PHẢN THÂN — hành động quay về chính mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là chỗ đuôi <b>-ся/-сь</b> lộ hết công dụng: <b>учи́ть</b> = dạy người khác; '
    'gắn <b>-ся</b> vào thành <b>учи́ться</b> = <b>dạy CHÍNH MÌNH</b> = đi học. Hai chữ mà lật ngược '
    'chiều của hành động.</div>'
    '<div class="hd-why"><b>-ся</b> vốn là dạng rút của <b>себя́</b> (bản thân). Nhớ điều này thì cả lớp '
    'động từ phản thân trở nên có lý: <b>мы́ться</b> tắm (rửa mình) · <b>одева́ться</b> mặc đồ.</div>'
    '<div class="hd-warn"><b>Chính tả:</b> sau nguyên âm viết <b>-сь</b>, sau phụ âm viết <b>-ся</b> — '
    '<b>учу́сь</b> nhưng <b>у́чится</b>. Và <b>у́чится</b> (ngôi 3) khác <b>учи́ться</b> '
    '(nguyên thể) đúng một dấu mềm, trọng âm cũng khác.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>учи́ть</b> dạy; học thuộc · <b>учи́тель</b> thầy giáo · '
    '<b>учени́к</b> học trò · <b>учёный</b> nhà khoa học · <b>нау́ка</b> khoa học</div>'
)

S["целовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">цел-</span>'
    '<span class="hd-gloss">NGUYÊN VẸN, lành lặn — chính là <b>це́лый</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ов-</span>'
    '<span class="hd-gloss">hậu tố tạo động từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc bất ngờ mà nhớ rất lâu: hôn vốn là <b>chúc cho lành lặn, nguyên vẹn</b> '
    '— cùng gốc với <b>це́лый</b> (nguyên vẹn) và <b>исцели́ть</b> (chữa lành). Tiếng Anh song song: '
    '<i>whole</i> và <i>heal</i> cũng cùng một gốc.</div>'
    '<div class="hd-warn"><b>Lớp -овать rất năng suất, và chia LẠ:</b> phần <b>-ова-</b> biến mất, '
    'thay bằng <b>-у-</b> — <b>целу́ю, целу́ешь</b>. Cùng khuôn: <b>рисова́ть → рису́ю</b> · '
    '<b>танцева́ть → танцу́ю</b>. Nhớ khuôn này là chia được cả trăm động từ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поцелова́ть</b> hôn một cái (HT) · <b>поцелу́й</b> nụ hôn · '
    '<b>це́лый</b> nguyên vẹn, cả · <b>исцели́ть</b> chữa lành</div>'
)

# ── Field Vietnamese (§2c) — ĐỀ BÀI của deck 1-go, user gõ từ Nga từ dòng này.
# Cả 19 từ đều là ĐỘNG TỪ nên thể (hoàn thành / chưa hoàn thành) phải hiện ra ở
# mọi dòng: thiếu nó thì "nói" ứng được với cả сказать lẫn говорить. Ngoài ra
# tách cặp động từ ↔ danh từ cùng gốc (ăn sáng ↔ bữa sáng, nhảy ↔ điệu nhảy).
V["видеть"]     = "nhìn thấy, trông thấy (chưa hoàn thành — mắt bắt được, không chủ ý)"
V["гулять"]     = "đi dạo chơi (chưa hoàn thành — dạo ngoài trời, không nhằm tới đâu)"
V["думать"]     = "nghĩ, suy nghĩ, cho rằng (chưa hoàn thành)"
V["жить"]       = "sống, sinh sống ở đâu (chưa hoàn thành)"
V["завтракать"] = "ăn sáng — ĐỘNG TỪ, chưa hoàn thành (không phải \"bữa sáng\")"
V["звонить"]    = "gọi điện thoại (chưa hoàn thành, không tiền tố)"
V["играть"]     = "chơi (chưa hoàn thành — thể thao, trò chơi, nhạc cụ)"
V["обедать"]    = "ăn trưa — ĐỘNG TỪ, chưa hoàn thành (không phải \"bữa trưa\")"
V["повторять"]  = "lặp lại, ôn tập (chưa hoàn thành — làm đi làm lại)"
V["понимать"]   = "hiểu (chưa hoàn thành — đang hiểu, thường hiểu)"
V["проверять"]  = "kiểm tra, rà soát (chưa hoàn thành)"
V["рисовать"]   = "vẽ, phác hoạ (chưa hoàn thành)"
V["сказать"]    = "nói ra, bảo một câu (HOÀN THÀNH — một lần, xong việc)"
V["спросить"]   = "hỏi một câu (HOÀN THÀNH — một lần, xong việc)"
V["спрягаться"] = "được chia (nói về động từ) — dạng phản thân -ся, chưa hoàn thành"
V["танцевать"]  = "nhảy múa, khiêu vũ — ĐỘNG TỪ, chưa hoàn thành (không phải \"điệu nhảy\")"
V["ужинать"]    = "ăn tối — ĐỘNG TỪ, chưa hoàn thành (không phải \"bữa tối\")"
V["учиться"]    = "học, đi học (chưa hoàn thành — phản thân, KHÔNG phải \"dạy\")"
V["целовать"]   = "hôn — ĐỘNG TỪ, chưa hoàn thành (không phải \"nụ hôn\")"
