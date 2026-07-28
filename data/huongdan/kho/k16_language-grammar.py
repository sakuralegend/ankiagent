# -*- coding: utf-8 -*-
"""k16 — language::grammar: đại từ nhân xưng & sở hữu.

Trục của lô: bảng biến cách của bảy đại từ nhân xưng (chỗ BUỘC PHẢI THUỘC, nhưng
gọn hơn vẻ ngoài rất nhiều), và ranh giới giữa bốn đại từ sở hữu PHẢI CHIA
(мой·твой·наш·ваш) với ba cái ĐỨNG YÊN (его́·её·их).

Hai khối dùng chung, KHÔNG thẻ nào mang cả hai trừ его́/её/их — đúng ba từ đó
thật sự làm cả hai việc (tân ngữ ngôi ba + sở hữu bất biến), nên chúng cần cả hai bảng.
"""

# ---------------------------------------------------------------- khối dùng chung 1
NX = (
    '<div class="hd-sec">■ Hệ thống 1 — BẢNG BIẾN CÁCH ĐẠI TỪ NHÂN XƯNG</div>'
    '<div class="hd-why">Sáu cách nhân bảy đại từ nghe như 42 ô phải học thuộc. Thật ra chỉ có ba điều phải nhớ, phần còn lại suy ra được:<br>'
    '<b>(1)</b> cách 2 và cách 4 <u>luôn viết giống hệt nhau</u> ở mọi đại từ nhân xưng — mất luôn một cột;<br>'
    '<b>(2)</b> <b>я</b> và <b>ты</b> đi cùng khuôn, <b>мы</b> và <b>вы</b> đi cùng khuôn (chỉ đổi một phụ âm đầu);<br>'
    '<b>(3)</b> ngôi thứ ba mọc thêm <b>н-</b> sau giới từ — ô đỏ ngay dưới bảng.</div>'
    '<div class="hd-row"><span class="hd-piece"><b>я</b> tôi</span><span class="hd-gloss">2·4 <b>меня́</b> — 3 <b>мне</b> — 5 <b>мной</b> — 6 о <b>мне</b></span></div>'
    '<div class="hd-row"><span class="hd-piece"><b>ты</b> cậu</span><span class="hd-gloss">2·4 <b>тебя́</b> — 3 <b>тебе́</b> — 5 <b>тобо́й</b> — 6 о <b>тебе́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece"><b>он</b> · <b>оно́</b></span><span class="hd-gloss">2·4 <b>его́</b> — 3 <b>ему́</b> — 5 <b>им</b> — 6 о <b>нём</b></span></div>'
    '<div class="hd-row"><span class="hd-piece"><b>она́</b></span><span class="hd-gloss">2·4 <b>её</b> — 3 <b>ей</b> — 5 <b>ей</b> — 6 о <b>ней</b></span></div>'
    '<div class="hd-row"><span class="hd-piece"><b>мы</b></span><span class="hd-gloss">2·4 <b>нас</b> — 3 <b>нам</b> — 5 <b>на́ми</b> — 6 о <b>нас</b></span></div>'
    '<div class="hd-row"><span class="hd-piece"><b>вы</b></span><span class="hd-gloss">2·4 <b>вас</b> — 3 <b>вам</b> — 5 <b>ва́ми</b> — 6 о <b>вас</b></span></div>'
    '<div class="hd-row"><span class="hd-piece"><b>они́</b></span><span class="hd-gloss">2·4 <b>их</b> — 3 <b>им</b> — 5 <b>и́ми</b> — 6 о <b>них</b></span></div>'
    '<div class="hd-warn"><b>🔴 LUẬT н- — bẫy số một của người mới học:</b><br>'
    'Ba đại từ ngôi thứ ba (<b>он</b>, <b>она́</b>, <b>они́</b>) <u>mọc thêm chữ н-</u> khi đứng ngay sau giới từ:<br>'
    '&nbsp;&nbsp;<b>его́</b> → <b>у него́</b>, <b>от него́</b> · <b>ему́</b> → <b>к нему́</b> · <b>им</b> → <b>с ним</b><br>'
    '&nbsp;&nbsp;<b>её</b> → <b>у неё</b> · <b>ей</b> → <b>к ней</b> · <b>их</b> → <b>у них</b> · <b>и́ми</b> → <b>с ни́ми</b><br>'
    'Cách 6 thì <u>luôn</u> có н-, vì cách 6 không bao giờ đứng một mình mà không có giới từ: <b>о нём</b>, <b>о ней</b>, <b>о них</b>.<br>'
    '⚠️ Nhưng <b>его́ · её · их</b> khi làm <u>sở hữu</u> thì KHÔNG BAO GIỜ thêm н-, kể cả sau giới từ:<br>'
    '&nbsp;&nbsp;<b>у него́</b> дом = anh ấy có nhà &nbsp;|&nbsp; <b>у его́ бра́та</b> = ở chỗ anh trai <i>của anh ấy</i>.<br>'
    'Lý do rất sạch, không phải học vẹt: ở câu sau, giới từ <b>у</b> chi phối <b>бра́та</b> chứ không chi phối <b>его́</b> — <b>его́</b> chỉ dính vào danh từ.<br>'
    'Ngôi một và ngôi hai không dính luật này: <b>у меня́</b>, <b>у тебя́</b>, <b>у нас</b>, <b>у вас</b>.</div>'
)

# ---------------------------------------------------------------- khối dùng chung 2
SH = (
    '<div class="hd-sec">■ Hệ thống 2 — SỞ HỮU: BỐN CÁI PHẢI CHIA, BA CÁI ĐỨNG YÊN</div>'
    '<div class="hd-why">Đây đúng là chỗ nên tách bạch “luật suy ra được” với “chỗ buộc phải thuộc”. Nhóm trên thì suy; nhóm dưới thì khỏi làm gì cả — và chính vì khỏi làm gì mà nó hay bị lẫn với đại từ nhân xưng.</div>'
    '<div class="hd-row"><span class="hd-piece">PHẢI CHIA<br>(nam — nữ — trung — số nhiều)</span><span class="hd-gloss">'
    '<b>мой</b> · <b>моя́</b> · <b>моё</b> · <b>мои́</b> — của tôi<br>'
    '<b>твой</b> · <b>твоя́</b> · <b>твоё</b> · <b>твои́</b> — của cậu<br>'
    '<b>наш</b> · <b>на́ша</b> · <b>на́ше</b> · <b>на́ши</b> — của chúng tôi<br>'
    '<b>ваш</b> · <b>ва́ша</b> · <b>ва́ше</b> · <b>ва́ши</b> — của các bạn / của ngài</span></div>'
    '<div class="hd-row"><span class="hd-piece">ĐỨNG YÊN<br>(bất biến)</span><span class="hd-gloss">'
    '<b>его́</b> của anh ấy · <b>её</b> của cô ấy · <b>их</b> của họ<br>'
    'Đúng một hình cho mọi giống, mọi số, mọi cách: <b>его́ дом</b> · <b>его́ кни́га</b> · <b>его́ де́ти</b> · <b>с его́ бра́том</b>.</span></div>'
    '<div class="hd-warn"><b>Luật vàng — ngược hẳn tiếng Anh:</b> đại từ sở hữu tiếng Nga hợp với <u>VẬT ĐƯỢC SỞ HỮU</u>, không hợp với người chủ. <b>моя́ кни́га</b> = sách của tôi; cái đuôi nữ tính đó là vì <b>кни́га</b> giống cái, chứ không phải vì tôi là ai. Tiếng Anh làm ngược: <i>his book / her book</i> đổi theo người chủ.<br>'
    '⇒ Hệ quả bất ngờ: nhóm bất biến <b>его́ · её · их</b> lại là nhóm <i>giống tiếng Anh nhất</i> và dễ nhất — chỉ cần biết chủ là ai, khỏi ngó danh từ.</div>'
    '<div class="hd-warn"><b>Hai kiểu đuôi, đừng trộn:</b><br>'
    '• <b>мой</b> / <b>твой</b> / <b>свой</b> — nhấn ở ĐUÔI, đuôi dài: <b>моего́</b>, <b>моему́</b>, <b>мои́м</b>, о <b>моём</b>.<br>'
    '• <b>наш</b> / <b>ваш</b> — cùng đúng bộ đuôi ấy, nhưng nhấn ở GỐC: <b>на́шего</b>, <b>на́шему</b>, <b>на́шим</b>, о <b>на́шем</b>.<br>'
    '⇒ Khác biệt thật giữa hai kiểu <u>chỉ là chỗ nhấn</u>, không phải bộ đuôi. Thuộc một cặp là có luôn cặp kia, vì trong mỗi cặp chỉ đổi phụ âm đầu.</div>'
)

S = {}

S["я"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được. <b>я</b> là một từ gốc trần, ngắn nhất mà tiếng Nga có: đúng một chữ cái. Dạng cổ của nó trong tiếng Slav nhà thờ là <b>азъ</b> — cũng chính là TÊN của chữ cái đầu bảng chữ Slav cổ (bảng chữ đó đặt tên các chữ bằng những từ có nghĩa). Tiếng Nga hiện đại mài nó xuống còn một âm.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính dạng cổ <b>азъ</b> mới còn lộ dây họ hàng với <i>ego</i> (Latin), <i>ich</i> (Đức), <i>I</i> (Anh). Nhưng điều đáng nhớ hơn nhiều: <b>я</b> chỉ tồn tại ở cách 1. Vừa rời vị trí chủ ngữ là nó đổi sang thân <b>мен-</b>: <b>меня́</b>, <b>мне</b>, <b>мной</b>. Hai thân khác hẳn nhau cho cùng một từ — không suy ra được, nhưng chỉ có hai, thuộc là xong.</div>'
    '<div class="hd-warn">⚠️ Mức tin: dây <b>азъ</b> ↔ <i>ego</i> ↔ <i>I</i> là từ nguyên (rất được đồng thuận), KHÔNG phải luật suy ra được. Dùng nó để nhớ thì tốt; đừng dùng để đoán hình của từ.</div>'
    '<div class="hd-warn"><b>Khác tiếng Anh:</b> <b>я</b> viết THƯỜNG khi ở giữa câu (<i>I</i> tiếng Anh luôn viết hoa). Có câu người Nga mắng trẻ con: <b>Я — после́дняя бу́ква в алфави́те</b> — “tôi” là chữ cái cuối bảng chữ cái, ý là đừng lúc nào cũng tôi với tôi.</div>'
    '<div class="hd-warn"><b>🔴 Ba câu bạn dùng mỗi ngày, và cả ba đều KHÔNG dùng tới hình cách 1:</b><br>'
    '&nbsp;&nbsp;<b>У меня́ есть…</b> = tôi có… (nghĩa đen “ở chỗ tôi có”). Tiếng Nga hầu như không dùng động từ “có”; thay vào đó là <b>у</b> + cách 2. Vậy “tôi có” bắt đầu bằng <b>меня́</b>.<br>'
    '&nbsp;&nbsp;<b>Меня́ зову́т…</b> = tôi tên là… (nghĩa đen “người ta gọi tôi là”) — <b>меня́</b> ở cách 4.<br>'
    '&nbsp;&nbsp;<b>Мне на́до…</b> / <b>Мне нра́вится…</b> = tôi cần… / tôi thích… — cách 3, vì người trải nghiệm trong tiếng Nga rất hay nằm ở cách 3 chứ không làm chủ ngữ.<br>'
    '⇒ Học <b>я</b> mà chỉ thuộc mỗi chữ <b>я</b> thì chưa nói được câu nào. Ba hình <b>меня́ · мне · мной</b> mới là phần dùng thật.</div>'
    '<div class="hd-warn"><b>Quá khứ lộ giới tính người nói:</b> động từ quá khứ tiếng Nga chia theo GIỐNG chứ không theo ngôi. Bạn là nam thì nói <b>я знал</b>, <b>я был</b>, <b>я сде́лал</b>; người nữ nói <b>я зна́ла</b>, <b>я была́</b>, <b>я сде́лала</b>. Cùng một chữ <b>я</b>, hai đuôi khác nhau — đây là chỗ người mới hay quên và tự khai sai giới tính của mình.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>меня́</b> tôi (cách 2·4) · <b>мне</b> cho tôi (cách 3) · <b>мной</b> bởi tôi (cách 5) · <b>мой</b> của tôi · <b>мы</b> chúng tôi · <b>сам</b> tự mình (hay đi kèm: <b>я сам</b> = chính tôi)</div>'
    + NX
)

S["ты"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — từ gốc trần hai chữ cái. Nhưng gốc <b>т-</b> của nó tái xuất ở khắp nơi: <b>тебя́</b>, <b>тебе́</b>, <b>тобо́й</b>, và cả đại từ sở hữu <b>твой</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là chỗ hiếm hoi mà từ nguyên giúp nhớ thật: <b>ты</b> ↔ tiếng Anh cổ <i>thou</i>, Latin <i>tu</i>, Pháp <i>tu</i>. Tiếng Anh từng có <u>đúng cặp</u> <i>thou</i> (thân mật, một người) / <i>you</i> (lịch sự hoặc số nhiều) — y hệt cặp <b>ты</b> / <b>вы</b> của tiếng Nga. Tiếng Anh về sau bỏ <i>thou</i>, giữ mỗi <i>you</i>; tiếng Nga giữ nguyên cả hai. Vậy bạn không phải học một khái niệm mới, chỉ là học lại một khái niệm tiếng Anh đã đánh mất.</div>'
    '<div class="hd-warn">⚠️ Mức tin: <b>ты</b> ↔ <i>thou</i> ↔ <i>tu</i> là từ nguyên, tuy đây là một trong những dây chắc nhất của ngữ hệ Ấn–Âu. Còn chuyện tiếng Anh từng có cặp <i>thou/you</i> song song với <b>ты</b>/<b>вы</b> thì là sự thật lịch sử, kiểm được — dùng thoải mái.</div>'
    '<div class="hd-warn"><b>Dùng sai từ này là mất lịch sự, không phải lỗi ngữ pháp:</b> chỉ dùng với bạn bè, người thân, trẻ con, và người bằng tuổi đã đồng ý xưng hô thân mật. Với người lạ, người lớn tuổi, thầy cô, khách hàng, cấp trên — luôn <b>вы</b>. Có hẳn động từ cho việc chuyển: <b>перейти́ на ты</b> = chuyển sang xưng hô thân mật (thường do người lớn tuổi hơn đề nghị).<br>'
    'Cặp chào tương ứng: <b>приве́т</b> đi với <b>ты</b> · <b>здра́вствуйте</b> đi với <b>вы</b>.</div>'
    '<div class="hd-warn"><b>Mẹo nhận dạng cực rẻ:</b> đuôi động từ <b>-шь</b> <u>chỉ tồn tại cho ngôi <b>ты</b></u>, không ngôi nào khác có. Thấy <b>-шь</b> là biết ngay đang nói với một người thân mật: <b>ты де́лаешь</b>, <b>ты говори́шь</b>, <b>ты хо́чешь</b>. Mệnh lệnh cũng chia đôi theo cặp này: <b>иди́</b> (với ты) ↔ <b>иди́те</b> (với вы).</div>'
    '<div class="hd-warn"><b>Câu dùng thật:</b> <b>Как тебя́ зову́т?</b> = cậu tên gì? · <b>У тебя́ есть…?</b> = cậu có… không? · <b>Я тебе́ скажу́</b> = tớ sẽ nói cho cậu. Cả ba đều không dùng hình <b>ты</b> — hệt như thẻ <b>я</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тебя́</b> cậu (cách 2·4) · <b>тебе́</b> cho cậu (cách 3) · <b>тобо́й</b> bởi cậu (cách 5) · <b>твой</b> của cậu · <b>вы</b> các bạn / ngài (dạng lịch sự của chính từ này)</div>'
    + NX
)

S["мы"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được. Điều đáng chú ý là <b>мы</b> chỉ sống ở cách 1; mọi cách còn lại chuyển sang thân <b>н-</b>: <b>нас</b>, <b>нам</b>, <b>на́ми</b>. Cùng kiểu “hai thân cho một từ” như <b>я → меня́</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bắc cầu tiếng Anh ở đây rất đáng dùng, nhưng bắc vào <u>các cách</u> chứ không phải vào <b>мы</b>: <b>нас</b> ↔ <i>us</i>, Latin <i>nos</i> — cùng một gốc Ấn–Âu <i>*nos</i> chỉ “chúng tôi” ngoài vị trí chủ ngữ. Thấy <b>н-</b> là nghĩ tới <i>us</i>, thế là có luôn <b>нас · нам · на́ми</b> và cả <b>наш</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: <b>нас</b> ↔ <i>us</i>/<i>nos</i> là dây họ hàng vững. Còn <b>мы</b> ↔ <i>we</i> thì các nguồn không thống nhất — đây là từ nguyên, không phải luật suy ra được, đừng dựa vào nó để đoán dạng.</div>'
    '<div class="hd-warn"><b>🔴 Cấu trúc rất Nga, dịch từng chữ sẽ hiểu sai:</b> <b>мы с тобо́й</b> nghĩa đen là “chúng tôi với cậu”, nhưng nghĩa thật là <u>“tớ với cậu”</u> — tổng cộng hai người, không phải ba. Tương tự <b>мы с бра́том</b> = tôi với anh trai (hai người), <b>мы с ва́ми</b> = tôi với các bạn.<br>'
    'Người mới hay dịch thành “chúng tôi và…”, thành ra đếm dư người. Cứ nhớ: <b>мы с X</b> = tôi + X.</div>'
    '<div class="hd-warn"><b>Đuôi động từ ngôi này là -м</b>, cả hai lớp chia đều thế: <b>мы де́лаем</b>, <b>мы говори́м</b>. Rủ rê thì dùng <b>дава́й</b> / <b>дава́йте</b> + động từ: <b>дава́йте пойдём</b> = ta đi nào.<br>'
    '<b>У нас</b> ngoài nghĩa “chúng tôi có” còn hay mang nghĩa “ở nước tôi, ở chỗ chúng tôi”: <b>у нас во Вьетна́ме</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>нас</b> chúng tôi (cách 2·4) · <b>нам</b> cho chúng tôi (cách 3) · <b>на́ми</b> bởi chúng tôi (cách 5) · <b>наш</b> của chúng tôi · <b>я</b> tôi (số ít tương ứng)</div>'
    + NX
)

S["вы"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được. Như <b>мы</b>, nó chỉ sống ở cách 1 rồi chuyển sang thân <b>в-</b>: <b>вас</b>, <b>вам</b>, <b>ва́ми</b>. Đối chiếu thẳng hàng với <b>мы → нас · нам · на́ми</b> — chỉ đổi <b>н</b> thành <b>в</b>, không phải học thêm gì.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một hình, hai công việc:<br>'
    '<b>(1)</b> số nhiều thật của <b>ты</b> — nói với nhiều người, kể cả bạn thân;<br>'
    '<b>(2)</b> ngôi lịch sự với <u>một</u> người — người lạ, người lớn tuổi, thầy cô, khách.<br>'
    'Tiếng Anh từng có đúng hệ này (<i>thou</i> / <i>you</i>) rồi bỏ mất một nửa; <b>вас</b> ↔ Latin <i>vos</i> vẫn còn nhìn thấy dây họ hàng.</div>'
    '<div class="hd-warn"><b>🔴 Luật viết hoa — có thật, và có ý nghĩa:</b><br>'
    '• Viết hoa <b>Вы</b>, <b>Вас</b>, <b>Вам</b> khi trang trọng và hướng tới <u>một người cụ thể</u>: thư từ, đơn từ, email công việc, quảng cáo hướng tới cá nhân.<br>'
    '• Viết thường <b>вы</b> khi đang nói với <u>nhiều người</u>, và trong hội thoại đời thường.<br>'
    'Viết hoa nhầm chỗ không sai ngữ pháp, nhưng nó nói với người đọc rằng bạn đang cố trang trọng — nên đừng rắc bừa.</div>'
    '<div class="hd-warn"><b>Bẫy chia động từ:</b> dù <b>Вы</b> chỉ MỘT người, mọi thứ đi kèm vẫn chia <u>số nhiều</u>: <b>Вы зна́ете</b> (không phải зна́ешь), quá khứ <b>Вы бы́ли</b> (không phải был). Đây là chỗ người mới hay sửa “cho hợp lý” rồi thành sai.</div>'
    '<div class="hd-warn"><b>Câu dùng thật:</b> <b>Как вас зову́т?</b> = ngài tên gì? (bản lịch sự của <b>Как тебя́ зову́т?</b>) · <b>У вас есть…?</b> = ngài có… không? (câu hỏi trong cửa hàng) · <b>Извини́те</b> đi với <b>вы</b>, <b>извини́</b> đi với <b>ты</b>.<br>'
    'Chưa chắc dùng cái nào thì chọn <b>вы</b>: lịch sự quá tay chỉ hơi xa cách, còn thân mật quá tay là khiếm nhã.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вас</b> các bạn (cách 2·4) · <b>вам</b> cho các bạn (cách 3) · <b>ва́ми</b> bởi các bạn (cách 5) · <b>ваш</b> của các bạn · <b>ты</b> cậu (bản thân mật) · <b>мы</b> chúng tôi (cùng khuôn biến cách)</div>'
    + NX
)

S["он"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — một âm tiết trần. Nhưng bốn hình cách 1 của cả bộ ngôi ba thì rất đều: <b>он</b> (nam) · <b>она́</b> (nữ) · <b>оно́</b> (trung) · <b>они́</b> (số nhiều). Chỉ mình <b>он</b> không mang trọng âm đánh dấu vì nó có đúng một nguyên âm; ba hình kia đều nhấn ở đuôi.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ cách 2 trở đi, <b>он</b> và <b>оно́</b> dùng chung một bộ hình hoàn toàn: <b>его́ · ему́ · им · нём</b>. Giống trung không có bộ riêng — bớt được đúng một cột trong bảng.</div>'
    '<div class="hd-warn"><b>🔴 Chỗ khác tiếng Anh nhiều nhất: tiếng Nga KHÔNG có “it”.</b><br>'
    'Chọn <b>он</b> / <b>она́</b> / <b>оно́</b> theo <u>giống ngữ pháp của danh từ</u>, không theo “người hay vật”:<br>'
    '&nbsp;&nbsp;<b>стол</b> (cái bàn) là <b>он</b> · <b>кни́га</b> (quyển sách) là <b>она́</b> · <b>окно́</b> (cửa sổ) là <b>оно́</b>.<br>'
    '“Quyển sách đâu rồi? — Nó ở trên bàn” trong tiếng Nga là <b>Она́ на столе́</b>, dịch sát thì thành “cô ấy ở trên bàn”. Nghe lạ tai lúc đầu, nhưng đây là luật máy móc: nhìn chữ cái cuối của danh từ là biết chọn hình nào.</div>'
    '<div class="hd-warn"><b>Đừng lược bỏ đại từ.</b> Tiếng Nga ở thì quá khứ chia theo giống chứ không theo ngôi (<b>он знал</b> / <b>она́ зна́ла</b> đều là “biết”), nên bỏ đại từ đi là mất luôn thông tin ai làm. Khác với tiếng Ý hay Tây Ban Nha, tiếng Nga giữ đại từ gần như luôn luôn.</div>'
    '<div class="hd-warn"><b>Nhớ kèm luật н-:</b> hình trần <b>его́</b>, <b>ему́</b>, <b>им</b> chỉ đứng sau động từ; hễ có giới từ phía trước là thành <b>него́</b>, <b>нему́</b>, <b>ним</b>. So sánh: <b>Я ви́жу его́</b> (tôi thấy anh ta) ↔ <b>Я иду́ к нему́</b> (tôi đi tới chỗ anh ta).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>она́</b> cô ấy · <b>оно́</b> nó (giống trung) · <b>они́</b> họ · <b>его́</b> anh ấy (cách 2·4); của anh ấy · <b>ему́</b> cho anh ấy · <b>нём</b> về anh ấy (luôn sau giới từ)</div>'
    + NX
)

S["его"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được. Đây là một hình cổ, và đuôi <b>-его́</b> của nó chính là đuôi cách 2 giống đực mà bạn sẽ gặp lại ở mọi tính từ mềm (<b>си́него</b>, <b>после́днего</b>) và ở <b>моего́</b>, <b>на́шего</b>.</div>'
    '<div class="hd-sec">Cách nhớ — MỘT HÌNH, HAI CÔNG VIỆC</div>'
    '<div class="hd-why">Đây là điểm cốt tử của thẻ này. <b>его́</b> làm hai việc chẳng liên quan gì nhau, và tiếng Nga viết y hệt nhau:<br>'
    '<b>(1) Đại từ nhân xưng</b> — cách 2 hoặc cách 4 của <b>он</b>/<b>оно́</b>, nghĩa là “anh ấy / nó” ở vị trí tân ngữ: <b>Я ви́жу его́</b> = tôi thấy anh ta.<br>'
    '<b>(2) Đại từ sở hữu bất biến</b> — nghĩa là “của anh ấy”, gắn vào danh từ đứng sau: <b>его́ дом</b> = nhà của anh ấy.</div>'
    '<div class="hd-warn"><b>🔴 Cách phân biệt, dùng được ngay không cần suy nghĩ:</b><br>'
    '• Ngay sau nó là một danh từ mà nó bổ nghĩa? → nghĩa <u>sở hữu</u>.<br>'
    '• Nó đứng làm tân ngữ của động từ, hoặc bị giới từ chi phối? → nghĩa <u>nhân xưng</u>.<br>'
    '<b>Phép thử н-</b> còn chắc hơn: sau giới từ, nghĩa nhân xưng BẮT BUỘC đổi thành <b>него́</b>; nghĩa sở hữu thì đứng yên.<br>'
    '&nbsp;&nbsp;<b>у него́ дом</b> = anh ấy có một cái nhà (nhân xưng, có н-)<br>'
    '&nbsp;&nbsp;<b>у его́ бра́та</b> = ở chỗ anh trai của anh ấy (sở hữu, không н-)<br>'
    'Hai câu chỉ khác nhau một chữ н, mà nghĩa lệch hẳn — nên đây là chỗ đáng dừng lại lâu nhất trong cả lô.</div>'
    '<div class="hd-warn"><b>Luật chính tả–phát âm mở khoá cả một lớp từ:</b> chữ <b>г</b> trong đuôi <b>-его́</b> / <b>-ого́</b> đọc thành âm “в”. Không phải ngoại lệ riêng của từ này: <b>моего́</b>, <b>но́вого</b>, <b>сего́дня</b> đều thế. Viết một đằng đọc một nẻo, nhưng nhất quán tuyệt đối ở mọi đuôi cách 2 giống đực/trung.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>он</b> anh ấy (cách 1) · <b>ему́</b> cho anh ấy (cách 3) · <b>им</b> bởi anh ấy (cách 5) · <b>него́</b> dạng sau giới từ · <b>её</b> của cô ấy · <b>их</b> của họ (hai bạn đồng hành bất biến) · <b>сего́дня</b> hôm nay (đúng là “của ngày này”, cùng đuôi cách 2)</div>'
    + NX + SH
)

S["её"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được. Lưu ý chính tả: viết đúng là <b>её</b> với chữ <b>ё</b>, và <b>ё</b> trong tiếng Nga <u>luôn</u> mang trọng âm — nên từ này không cần dấu nhấn thêm. Sách báo Nga hay in thành “ее” cho tiện chữ, nhưng đó là lược bỏ dấu chấm chứ không phải chính tả chuẩn.</div>'
    '<div class="hd-sec">Cách nhớ — MỘT HÌNH, HAI CÔNG VIỆC</div>'
    '<div class="hd-why">Giống hệt <b>его́</b>, chỉ đổi giống:<br>'
    '<b>(1) Nhân xưng</b> — cách 2·4 của <b>она́</b>, “cô ấy” ở vị trí tân ngữ: <b>Я ви́жу её</b> = tôi thấy cô ấy.<br>'
    '<b>(2) Sở hữu bất biến</b> — “của cô ấy”: <b>её дом</b>, <b>её кни́га</b>, <b>её де́ти</b> — một hình cho cả ba, không đổi theo danh từ.</div>'
    '<div class="hd-warn"><b>🔴 Đừng lẫn hai hình её và ей — cùng một đại từ, khác vai:</b><br>'
    '&nbsp;&nbsp;<b>её</b> = cách 2·4 → “cô ấy” làm tân ngữ trực tiếp, hoặc “của cô ấy”.<br>'
    '&nbsp;&nbsp;<b>ей</b> = cách 3 (cho cô ấy) và cả cách 5 (bởi cô ấy) — một hình gánh hai cách, thêm một chỗ tiết kiệm.<br>'
    '&nbsp;&nbsp;<b>Я дал ей кни́гу</b> = tôi đưa cho cô ấy quyển sách &nbsp;↔&nbsp; <b>Я ви́жу её</b> = tôi thấy cô ấy.</div>'
    '<div class="hd-warn"><b>Luật н- áp dụng đủ:</b> sau giới từ, nghĩa nhân xưng thành <b>неё</b> / <b>ней</b> — <b>у неё</b> (cô ấy có), <b>без неё</b> (không có cô ấy), <b>к ней</b> (tới chỗ cô ấy), <b>о ней</b> (về cô ấy). Nghĩa sở hữu vẫn trơ: <b>у её сестры́</b> = ở chỗ chị gái của cô ấy.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>она́</b> cô ấy (cách 1) · <b>ей</b> cho / bởi cô ấy · <b>неё</b>, <b>ней</b> dạng sau giới từ · <b>его́</b> của anh ấy · <b>их</b> của họ</div>'
    + NX + SH
)

S["их"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — hai chữ cái, một nguyên âm. Nó là hình cách 2·4 của <b>они́</b>, và cũng là đại từ sở hữu “của họ”. Đúng bộ ba <b>его́ · её · их</b> đều làm hai việc như nhau.</div>'
    '<div class="hd-sec">Cách nhớ — MỘT HÌNH, HAI CÔNG VIỆC</div>'
    '<div class="hd-why"><b>(1) Nhân xưng</b>: <b>Я ви́жу их</b> = tôi thấy họ · <b>У них есть маши́на</b> = họ có xe (sau giới từ nên mọc н-).<br>'
    '<b>(2) Sở hữu bất biến</b>: <b>их дом</b>, <b>их кни́га</b>, <b>их де́ти</b> — không hề đổi hình.<br>'
    'Vì nó bất biến, người mới thường thấy nhóm này <i>dễ</i> — và đúng là dễ, miễn đừng lẫn nó với các hình khác của <b>они́</b>.</div>'
    '<div class="hd-warn"><b>🔴 Ba hình của они́ rất hay bị trộn, tách ra một lần cho xong:</b><br>'
    '&nbsp;&nbsp;<b>их</b> = cách 2·4 → họ (tân ngữ) hoặc của họ.<br>'
    '&nbsp;&nbsp;<b>им</b> = cách 3 → cho họ. <b>Я дал им кни́гу</b>.<br>'
    '&nbsp;&nbsp;<b>и́ми</b> = cách 5 → bởi họ. Sau giới từ: <b>с ни́ми</b> = cùng với họ.<br>'
    'Ba hình này chỉ khác nhau ở đuôi, mà nghĩa thì khác hẳn vai trò trong câu.</div>'
    '<div class="hd-warn"><b>Sắc thái dùng thật — một lỗi rất phổ biến của chính người Nga:</b> nhiều người nói <b>и́хний</b> thay cho <b>их</b> (bắt chước kiểu chia của <b>наш</b>/<b>ваш</b>). Đây là dạng KHÔNG chuẩn, sách vở và văn viết đều không nhận. Bạn sẽ nghe thấy nó trong khẩu ngữ — cứ hiểu, nhưng đừng dùng.<br>'
    'Nó lộ ra vì sao <b>их</b> bất biến lại khó chịu với người bản ngữ: cả hệ sở hữu quanh nó đều chia, riêng nó thì không.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>они́</b> họ (cách 1) · <b>им</b> cho họ (cách 3) · <b>и́ми</b> bởi họ (cách 5) · <b>них</b>, <b>ним</b>, <b>ни́ми</b> dạng sau giới từ · <b>его́</b> của anh ấy · <b>её</b> của cô ấy</div>'
    + NX + SH
)

S["мой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">м-</span><span class="hd-gloss">thân ngôi thứ nhất số ít — chính là thân của <b>меня́</b>, <b>мне</b>, <b>мной</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ой / -я́ / -ё / -и́</span><span class="hd-gloss">đuôi sở hữu, đổi theo giống và số của <u>vật được sở hữu</u></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là một trong vài chỗ mà từ nguyên thật sự giúp nhớ: <b>мой</b> ↔ <i>my / mine</i>, Latin <i>meus</i>, Pháp <i>mon</i> — cùng gốc Ấn–Âu chỉ sở hữu ngôi một. Cả tiếng Anh lẫn tiếng Nga đều dựng đại từ sở hữu từ đúng cái thân <b>м-</b> đó. Nhớ được dây này là bắt luôn <b>меня́</b> và <b>мне</b>.<br>'
    'Bốn hình: <b>мой</b> (nam) · <b>моя́</b> (nữ) · <b>моё</b> (trung) · <b>мои́</b> (số nhiều) — và trọng âm rơi vào ĐUÔI ở cả bốn.</div>'
    '<div class="hd-warn">⚠️ Mức tin: quan hệ <b>мой</b> ↔ <i>my/mine</i> ↔ <i>meus</i> là từ nguyên, không phải luật. Nhưng nó thuộc nhóm đại từ — lớp từ ít bị thay thế nhất trong mọi ngôn ngữ — nên độ đồng thuận rất cao.</div>'
    '<div class="hd-warn"><b>Đứng một mình cũng được, và không cần động từ “là”:</b> <b>Э́та кни́га — моя́</b> = quyển sách này là của tôi. Khi chưa nói rõ vật gì thì dùng hình giống trung: <b>Э́то моё</b> = cái này của tôi.<br>'
    'Trật tự chuẩn là sở hữu đứng TRƯỚC danh từ (<b>мой дом</b>); đứng sau chỉ gặp ở lối nói cổ và câu cảm thán.</div>'
    '<div class="hd-warn"><b>🔴 CHỖ BUỘC PHẢI BIẾT: khi nào phải thay bằng <u>свой</u></b><br>'
    'Nếu người sở hữu <u>chính là chủ ngữ của câu</u>, tiếng Nga thích dùng <b>свой</b> (“của chính mình”) hơn:<br>'
    '&nbsp;&nbsp;<b>Я люблю́ свою́ рабо́ту</b> = tôi yêu công việc của mình.<br>'
    'Với ngôi một và ngôi hai thì <b>мой</b> vẫn chấp nhận được. Nhưng với ngôi thứ ba thì <b>свой</b> là bắt buộc, vì nó gánh một khác biệt nghĩa không có cách nào diễn khác:<br>'
    '&nbsp;&nbsp;<b>Он лю́бит свою́ жену́</b> = anh ấy yêu vợ mình (vợ của chính anh ấy)<br>'
    '&nbsp;&nbsp;<b>Он лю́бит его́ жену́</b> = anh ấy yêu vợ của người đàn ông khác<br>'
    'Một chữ đổi, cả câu chuyện đổi. <b>свой</b> chia y hệt <b>мой</b>: <b>свой · своя́ · своё · свои́</b>.</div>'
    '<div class="hd-warn"><b>Từ đồng tự — đừng hoảng khi gặp:</b> <b>мой</b> còn là dạng mệnh lệnh của động từ <b>мыть</b> (rửa). <b>Мой посу́ду!</b> = rửa bát đi! Nhận ra bằng ngữ cảnh: sở hữu thì đứng trước danh từ và không sai khiến ai cả.<br>'
    'Câu cảm thán quen thuộc: <b>Бо́же мой!</b> = trời ơi! — ở đây sở hữu đứng SAU danh từ, một trật tự cổ còn sót lại.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>моя́</b>, <b>моё</b>, <b>мои́</b> các hình giống–số · <b>моего́</b> của cái của tôi (cách 2) · <b>моему́</b> (cách 3) · <b>свой</b> của chính mình · <b>я</b>, <b>меня́</b>, <b>мне</b> cùng thân <b>м-</b> · <b>по-мо́ему</b> theo ý tôi</div>'
    + SH
)

S["твой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">тв-</span><span class="hd-gloss">thân ngôi thứ hai thân mật — từ <b>ты</b>, <b>тебя́</b>, <b>тобо́й</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ой / -я́ / -ё / -и́</span><span class="hd-gloss">đúng bộ đuôi của <b>мой</b>, không sai một chữ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Học <b>твой</b> gần như không tốn công thêm: lấy <b>мой</b> rồi đổi <b>м-</b> thành <b>тв-</b>, mọi thứ còn lại y nguyên — <b>твой · твоя́ · твоё · твои́</b>, trọng âm vẫn ở đuôi. Bắc cầu tiếng Anh cũng song song: <b>мой</b> ↔ <i>my</i> thì <b>твой</b> ↔ <i>thy / thine</i> (dạng cổ của <i>your</i>), Latin <i>tuus</i>.</div>'
    '<div class="hd-warn"><b>🔴 Nó đi liền với cách xưng hô, không tách rời được:</b> chỉ dùng <b>твой</b> với người mà bạn gọi là <b>ты</b>. Nói chuyện lịch sự (<b>вы</b>) mà buột ra <b>твой</b> thì nghe suồng sã ngay lập tức — phải là <b>ваш</b>.<br>'
    'Vậy nên hai từ này nên học thành cặp có điều kiện: <b>ты → твой</b> · <b>вы → ваш</b>.</div>'
    '<div class="hd-warn"><b>Cũng nhường chỗ cho <u>свой</u>:</b> khi chủ ngữ chính là người sở hữu, câu tự nhiên là <b>Ты лю́бишь свою́ рабо́ту</b> chứ không phải <i>твою́ рабо́ту</i>. Với ngôi hai thì dùng <b>твой</b> không sai, nhưng tai người Nga nghe <b>свой</b> mượt hơn.</div>'
    '<div class="hd-warn"><b>Câu dùng thật:</b> <b>Как твои́ дела́?</b> = dạo này cậu sao rồi? · <b>За твоё здоро́вье!</b> = chúc sức khoẻ cậu! (câu nâng ly) · <b>Э́то твоя́ кни́га?</b> = sách của cậu à? — trả lời gọn: <b>Да, моя́</b> hoặc <b>Э́то твоё</b>, khỏi cần động từ “là”.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>твоя́</b>, <b>твоё</b>, <b>твои́</b> các hình giống–số · <b>твоего́</b> (cách 2) · <b>твоему́</b> (cách 3) · <b>ты</b>, <b>тебя́</b>, <b>тебе́</b> cùng thân · <b>ваш</b> bản lịch sự · <b>по-тво́ему</b> theo ý cậu</div>'
    + SH
)

S["наш"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span><span class="hd-gloss">thân ngôi thứ nhất số nhiều — chính là <b>нас</b>, <b>нам</b>, <b>на́ми</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ш</span><span class="hd-gloss">phụ âm dựng đại từ sở hữu; chỉ có <b>наш</b> và <b>ваш</b> mang nó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thấy <b>н-</b> là nghĩ “chúng tôi”: <b>нас</b> ↔ <i>us</i> / Latin <i>nos</i>, và <b>наш</b> ↔ Latin <i>noster</i>, tiếng Anh <i>our</i>. Cả một cụm đi cùng nhau, học một lần.<br>'
    'Bốn hình: <b>наш</b> · <b>на́ша</b> · <b>на́ше</b> · <b>на́ши</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: <i>noster</i> / <i>our</i> là quan hệ từ nguyên chứ không phải luật suy ra được. Dùng để nhớ thì tốt, đừng dùng để đoán dạng.</div>'
    '<div class="hd-warn"><b>🔴 Khác <u>мой</u> ở đúng một điểm, và đó là điểm hay sai: TRỌNG ÂM.</b><br>'
    '&nbsp;&nbsp;<b>мой</b> nhấn ĐUÔI suốt: <b>моя́</b>, <b>моё</b>, <b>мои́</b>, <b>моего́</b>, <b>моему́</b>.<br>'
    '&nbsp;&nbsp;<b>наш</b> nhấn GỐC suốt: <b>на́ша</b>, <b>на́ше</b>, <b>на́ши</b>, <b>на́шего</b>, <b>на́шему</b>.<br>'
    'Bộ đuôi thì y hệt nhau — khác biệt nằm gọn ở chỗ nhấn, nên đây là thứ phải nghe và nhớ chứ không suy ra được. Nói <i>наша́</i> hay <i>мо́я</i> là hai lỗi ngược nhau, cùng một nguyên nhân: gộp hai kiểu làm một.</div>'
    '<div class="hd-warn"><b>Câu dùng thật:</b> <b>наш го́род</b> thành phố chúng tôi · <b>на́ша страна́</b> đất nước chúng tôi · <b>на́ше вре́мя</b> thời của chúng ta · <b>на́ши де́ти</b> con cái chúng tôi.<br>'
    '<b>Sắc thái:</b> <b>наш челове́к</b> nghĩa đen là “người của chúng tôi”, dùng thật thì là “người phe mình, người đáng tin” — một cách khen rất Nga.<br>'
    'Hình số nhiều <b>на́ши</b> còn dùng trơ trọi như một danh từ, nghĩa “phe mình, người nhà mình”: <b>На́ши вы́играли</b> = đội mình thắng rồi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>на́ша</b>, <b>на́ше</b>, <b>на́ши</b> các hình giống–số · <b>на́шего</b> (cách 2) · <b>на́шему</b> (cách 3) · <b>мы</b>, <b>нас</b>, <b>нам</b> cùng thân · <b>ваш</b> cùng kiểu đuôi · <b>по-на́шему</b> theo ý chúng tôi</div>'
    + SH
)

S["ваш"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ва-</span><span class="hd-gloss">thân ngôi thứ hai số nhiều / lịch sự — từ <b>вас</b>, <b>вам</b>, <b>ва́ми</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ш</span><span class="hd-gloss">cùng phụ âm sở hữu với <b>наш</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Toàn bộ thẻ này là một phép đổi chữ: lấy <b>наш</b>, đổi <b>н</b> thành <b>в</b>. <b>ваш</b> · <b>ва́ша</b> · <b>ва́ше</b> · <b>ва́ши</b>, bộ đuôi y nguyên, trọng âm vẫn đứng yên ở gốc. Quan hệ <b>наш</b>–<b>ваш</b> lặp đúng quan hệ <b>мы</b>–<b>вы</b> và <b>нас</b>–<b>вас</b>: một cặp đối xứng chạy suốt hệ đại từ.</div>'
    '<div class="hd-warn"><b>🔴 Hai nghĩa, đúng như <u>вы</u>:</b><br>'
    '• “của các bạn” — nói với nhiều người, kể cả bạn thân. Nhóm bạn thân vẫn dùng <b>ваш</b>, vì đây là số nhiều thật chứ không riêng chuyện lịch sự.<br>'
    '• “của ngài / của quý vị” — nói lịch sự với một người.<br>'
    'Đừng rút gọn thành “<b>ваш</b> = trang trọng”; hiểu thế sẽ lúng túng khi cần nói với hai người bạn.</div>'
    '<div class="hd-warn"><b>Viết hoa trong thư từ:</b> khi trang trọng và hướng tới một người, viết <b>Ваш</b>, <b>Ва́ша</b> — đi kèm <b>Вы</b> viết hoa. Câu kết thư chuẩn: <b>С уваже́нием, ваш …</b> = trân trọng, …<br>'
    'Nói với nhiều người thì viết thường.</div>'
    '<div class="hd-warn"><b>Câu bạn sẽ nghe ở sân bay và quầy lễ tân:</b> <b>Ваш па́спорт, пожа́луйста</b> = xin hộ chiếu của ngài · <b>Ва́ше и́мя?</b> = ngài tên gì? · <b>Ва́ша фами́лия?</b> = họ của ngài? · <b>Ва́ши докуме́нты</b> = giấy tờ của ngài.<br>'
    'Bản lịch sự của câu hỏi thăm quen thuộc: <b>Как ва́ши дела́?</b> (so với <b>Как твои́ дела́?</b> khi nói với bạn thân).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ва́ша</b>, <b>ва́ше</b>, <b>ва́ши</b> các hình giống–số · <b>ва́шего</b> (cách 2) · <b>ва́шему</b> (cách 3) · <b>вы</b>, <b>вас</b>, <b>вам</b> cùng thân · <b>наш</b> cùng kiểu đuôi · <b>твой</b> bản thân mật</div>'
    + SH
)

S["сам"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — gốc trần <b>сам-</b>. Nó không phải đại từ nhân xưng mà là đại từ NHẤN MẠNH: đi kèm một đại từ hoặc danh từ để nói “chính người đó, tự người đó làm”.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bắc cầu tiếng Anh khá vững: gốc Ấn–Âu chỉ “một, cùng một” cho ra <i>same</i> và <i>self</i> trong tiếng Anh, cho ra <b>сам</b> trong tiếng Nga. Nghĩa lõi là “đúng cái đó, không phải cái khác”.<br>'
    'Bốn hình theo giống–số: <b>сам</b> (nam) · <b>сама́</b> (nữ) · <b>само́</b> (trung) · <b>са́ми</b> (số nhiều).</div>'
    '<div class="hd-warn">⚠️ Mức tin: liên hệ <b>сам</b> ↔ <i>same</i> / <i>self</i> là từ nguyên, và ở đây kém chắc hơn mấy dây đại từ khác trong lô. Dùng để hình dung nghĩa lõi “cùng một, chính nó”, đừng coi là bằng chứng.</div>'
    '<div class="hd-warn"><b>🔴 Trọng âm NHẢY, và nhảy không đều — đây là chỗ dễ sai nhất:</b><br>'
    '&nbsp;&nbsp;<b>сам</b> → <b>сама́</b> (nhấn đuôi) → <b>само́</b> (nhấn đuôi) → nhưng <b>са́ми</b> lại LÙI VỀ GỐC.<br>'
    'Ba hình đầu nhấn đuôi, riêng số nhiều nhấn gốc. Các cách khác cũng nhấn đuôi: <b>самого́</b>, <b>самому́</b>, <b>сами́м</b>.<br>'
    'Ví dụ: <b>Я сам сде́лал</b> = chính tôi làm · <b>Она́ сама́ пришла́</b> = cô ấy tự đến · <b>Они́ са́ми зна́ют</b> = chính họ biết.</div>'
    '<div class="hd-warn"><b>🔴 BA THỨ TRÔNG GIỐNG NHAU, phải tách bạch một lần:</b><br>'
    '<b>1. сам</b> = tự mình, chính mình — <u>nhấn mạnh</u>, luôn đi kèm chủ thể: <b>Он сам пришёл</b>.<br>'
    '<b>2. са́мый</b> = “nhất” — công cụ dựng so sánh cực cấp, một từ hoàn toàn khác, chỉ trùng phần đầu: <b>са́мый большо́й</b> = to nhất, <b>са́мый ва́жный</b> = quan trọng nhất.<br>'
    '<b>3. hậu tố -ся</b> = hành động quay về chính chủ thể. Đây mới là “phản thân” thật, còn <b>сам</b> chỉ nhấn mạnh, KHÔNG thay được <b>-ся</b>:<br>'
    '&nbsp;&nbsp;<b>Он мо́ется</b> = anh ấy tắm (tự rửa mình) · <b>Он сам мо́ет маши́ну</b> = chính anh ấy rửa xe (không nhờ ai).<br>'
    '<b>4. себя́</b> = “mình” ở vị trí TÂN NGỮ — <b>Он ви́дит себя́</b> = anh ấy nhìn thấy chính mình. Khác vai với <b>сам</b>: <b>сам</b> đi cùng chủ ngữ, <b>себя́</b> làm tân ngữ.</div>'
    '<div class="hd-warn"><b>Hai cụm nghe rất nhiều:</b> <b>сам по себе́</b> = tự nó, riêng nó, độc lập · <b>сам собо́й</b> = tự động, tự khắc (<b>Всё реши́лось само́ собо́й</b> = mọi chuyện tự nó ổn thoả).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сама́</b>, <b>само́</b>, <b>са́ми</b> các hình giống–số · <b>са́мый</b> nhất (cực cấp) · <b>себя́</b> chính mình (tân ngữ) · <b>сам собо́й</b> tự khắc · <b>самолёт</b> máy bay (nghĩa đen: cái tự bay) · <b>самова́р</b> ấm samovar (cái tự đun)</div>'
    + NX
)

S["чей"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ч-</span><span class="hd-gloss">gốc nghi vấn, cùng họ với <b>кто</b> ai, <b>что</b> cái gì</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ей / -ья / -ьё / -ьи</span><span class="hd-gloss">đuôi sở hữu, đổi theo danh từ đứng sau</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>ч-</b> ở đây là hậu duệ của gốc nghi vấn Ấn–Âu cho ra cả bộ <i>wh-</i> tiếng Anh: <b>кто</b> ↔ <i>who</i>, <b>что</b> ↔ <i>what</i>, <b>чей</b> ↔ <i>whose</i>. Ba câu hỏi, một gốc.<br>'
    'Chữ <b>ь</b> trong <b>чья</b>, <b>чьё</b>, <b>чьи</b> là dấu mềm PHÂN CÁCH: nó tách phụ âm khỏi nguyên âm phía sau, nên đọc thành hai mảnh chứ không dính liền.</div>'
    '<div class="hd-warn"><b>🔴 Đây KHÔNG phải “của ai” bất biến — nó chia theo danh từ đứng sau:</b><br>'
    '&nbsp;&nbsp;<b>Чей э́то дом?</b> — nhà của ai? (<b>дом</b> giống đực)<br>'
    '&nbsp;&nbsp;<b>Чья э́то кни́га?</b> — sách của ai? (<b>кни́га</b> giống cái)<br>'
    '&nbsp;&nbsp;<b>Чьё э́то ме́сто?</b> — chỗ của ai? (<b>ме́сто</b> giống trung)<br>'
    '&nbsp;&nbsp;<b>Чьи э́то де́ти?</b> — con của ai? (số nhiều)<br>'
    'Người mới hay đóng cứng ở một hình <b>чей</b> rồi dùng cho mọi câu. Cứ nhớ nó theo cùng luật với <b>мой</b>/<b>твой</b>: hợp với VẬT, không hợp với người chủ — mà ở đây người chủ còn chưa biết là ai, nên lại càng không thể hợp theo chủ.</div>'
    '<div class="hd-warn"><b>Đừng lẫn với <u>кого́</u>:</b><br>'
    '&nbsp;&nbsp;<b>кого́</b> = “ai” ở vị trí tân ngữ hoặc cách 2 — <b>Кого́ ты ви́дишь?</b> = cậu thấy ai?<br>'
    '&nbsp;&nbsp;<b>чей</b> = “của ai”, luôn bám vào một danh từ — <b>Чей ты друг?</b> = cậu là bạn của ai?<br>'
    'Câu trả lời cho <b>чей</b> chính là hệ sở hữu ở khối dưới: <b>мой</b>, <b>твой</b>, <b>наш</b>, <b>ваш</b>, hoặc <b>его́</b> · <b>её</b> · <b>их</b>.</div>'
    '<div class="hd-warn"><b>Không chỉ dùng để hỏi:</b> nó nối được hai mệnh đề — <b>Я зна́ю, чья э́то маши́на</b> = tôi biết đây là xe của ai. Các cách khác: <b>чьего́</b>, <b>чьему́</b>, <b>чьим</b>.<br>'
    'Đừng lấy nó thay <b>кото́рый</b> (đại từ quan hệ “mà, cái mà”) — <b>кото́рый</b> nối một mệnh đề bất kỳ, còn <b>чей</b> chỉ nối khi quan hệ là SỞ HỮU, và trong văn nói người Nga thường tránh <b>чей</b> ở vai này.<br>'
    'Dạng bất định dựng thẳng từ nó: <b>чей-то</b> = của ai đó (có chủ, không rõ ai) · <b>чей-нибу́дь</b> = của bất kỳ ai.</div>'
    '<div class="hd-warn">⚠️ Mức tin: bộ <b>кто</b> · <b>что</b> · <b>чей</b> ↔ <i>who</i> · <i>what</i> · <i>whose</i> là từ nguyên, nhưng có luật biến âm đều đặn chống lưng (âm gốc Ấn–Âu cho ra <b>к/ч</b> ở tiếng Slav và <i>wh-</i> ở tiếng Anh), nên đây là dây đáng tin để nhớ cả cụm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>чья</b>, <b>чьё</b>, <b>чьи</b> các hình giống–số · <b>кто</b> ai · <b>что</b> cái gì · <b>кого́</b> ai (cách 2·4) · <b>како́й</b> loại nào · <b>чей-то</b> của ai đó · <b>ниче́й</b> của không ai — hình giống cái <b>ничья́</b> dùng trơ như danh từ nghĩa là “trận hoà”</div>'
    + SH
)
