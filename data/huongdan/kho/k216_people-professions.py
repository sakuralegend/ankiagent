# -*- coding: utf-8 -*-
"""k216 — people::professions (lô trộn): ly hôn, tín ngưỡng, nghề, nghèo khó, xã hội.

Chỗ cần nhất quán trong lô:
(1) вес-/вед- ↔ вод- «DẪN» như вести́, завести́, провести́, води́ть, вводи́ть đã có: hai đôi
    развести́сь/разводи́ться và подвести́/подводи́ть; под- SÁT LẠI GẦN như подойти́, подвози́ть;
    câu я подвожу́ khớp thẻ подвози́ть.
(2) Đuôi -ин «MỘT người» rụng ở số nhiều: мусульма́нин, россия́нин (như христиани́н, англича́нин).
(3) крит- PHÁN XÉT (krinein); бед- TAI HOẠ, CẢNH KHỐN; с- + -пас- CHE CHỞ; кон- CÙNG + -кур- CHẠY.
(4) Đuôi -т → -ция: конкуре́нт/конкуре́нция, интеллиге́нт/интеллиге́нция dẫn chiếu nhau.
Họ hàng cố ý vắng: зять (gốc trơn, không phái sinh thông dụng).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "развестись": "ly hôn, ly dị, sinh sôi nảy nở",   # «sinh sôi nhiều» ngượng; khớp разводиться (badge thể tách)
    "подвести": "dẫn đến, dắt tới, đưa lại gần, làm thất vọng, phụ lòng",   # THIẾU let down / disappoint / fail
    "подводить": "dẫn đến, dắt tới, đưa lại gần, làm thất vọng, phụ lòng",  # như trên
    "спасатель": "nhân viên cứu hộ, người cứu hộ",    # «lính cứu hỏa» = пожарный, gloss không có firefighter
}

# --------------------------------------------------------------------- подбородок
S["подбородок"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span><span class="hd-gloss">DƯỚI — như '
    '<b>подва́л</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-бород-</span><span class="hd-gloss">RÂU — '
    '<b>борода́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ок</span><span class="hd-gloss">hậu tố danh '
    'từ giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Chỗ nằm dưới râu» ⇒ cái cằm. <b>о</b> trong <b>-ок</b> chạy mất khi '
    'thêm đuôi, như <b>подро́сток</b>: <b>подборо́дка</b>, <b>на подборо́дке</b>, '
    '<b>подборо́дки</b>. Trọng âm đứng yên ở <b>-ро́-</b>.</div>'
    '<div class="hd-warn"><b>двойно́й подборо́док</b> «cằm đôi» ⇒ nọng cằm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>борода́</b> râu · <b>борода́тый</b> có râu</div>'
)

# --------------------------------------------------------------------- развестись
S["развестись"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раз-</span><span class="hd-gloss">TÁCH RA, ra '
    'nhiều ngả — như <b>рас-</b> trong <b>расста́ться</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-вес- (вед-)</span><span class="hd-gloss">DẪN '
    '— như <b>вести́</b>; gốc thật là <i>вед-</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ти́-сь</span><span class="hd-gloss">đuôi '
    'nguyên thể + <b>-сь</b> (= <b>-ся</b>, sau nguyên âm)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mỗi người tự dẫn mình đi một ngả ⇒ ly hôn; toả ra nhiều ngả ⇒ (con '
    'vật) sinh sôi nảy nở. <i>д</i> hiện lại ở tương lai: <b>разведу́сь</b>, '
    '<b>разведётся</b>; quá khứ rơi <i>д</i>, nhấn đuôi: <b>развёлся</b>, <b>развела́сь</b>, '
    '<b>развели́сь</b>. Cặp CHT: <b>разводи́ться</b>.</div>'
    '<div class="hd-warn">Ly hôn VỚI ai: <b>с</b> + cách 5, nam nữ như nhau — <b>развести́сь '
    'с му́жем</b> / <b>с жено́й</b>. Lúc cưới thì nam nữ nói khác nhau: <b>жени́ться на</b> + '
    'cách 6, <b>вы́йти за́муж за</b> + cách 4.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>разво́д</b> cuộc ly hôn · <b>разводи́ть</b> tách ra; gây giống · '
    '<b>вести́</b> dẫn · <b>провести́</b> tiến hành</div>'
)

# --------------------------------------------------------------------- разводиться
S["разводиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раз-</span><span class="hd-gloss">TÁCH RA, ra '
    'nhiều ngả</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вод-и́ть-</span><span class="hd-gloss">DẪN — '
    'chính là <b>води́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span><span class="hd-gloss">tự mình, lẫn '
    'nhau</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thể CHƯA HOÀN THÀNH của <b>развести́сь</b> (tiền tố + '
    '<b>води́ть</b>): đang làm thủ tục ly hôn, hoặc ly hôn nhiều lần; con vật thì sinh sôi '
    'nảy nở. Chia như <b>води́ть</b>: ngôi «tôi» <i>д → ж</i>, các ngôi khác trọng âm lùi: '
    '<b>развожу́сь</b>, <b>разво́дишься</b>, <b>разво́дятся</b>.</div>'
    '<div class="hd-warn">Ly hôn VỚI ai: <b>с</b> + cách 5 — <b>Она́ разво́дится с '
    'му́жем</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>развести́сь</b> (HT) · <b>разво́д</b> cuộc ly hôn · '
    '<b>разводи́ть</b> tách ra; gây giống · <b>води́ть</b> dẫn đi lại</div>'
)

# --------------------------------------------------------------------- подвести
S["подвести"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span><span class="hd-gloss">SÁT LẠI GẦN '
    '— như <b>подойти́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-вес- (вед-)</span><span class="hd-gloss">DẪN '
    '— như <b>вести́</b>; gốc thật là <i>вед-</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ти́</span><span class="hd-gloss">đuôi nguyên '
    'thể có trọng âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dẫn tới sát bên CÁI GÌ: <b>к</b> + cách 3 — <b>подвести́ к '
    'окну́</b>. <i>д</i> hiện lại ở tương lai: <b>подведу́</b>, <b>подведёшь</b>; quá khứ rơi '
    '<i>д</i>: <b>подвёл</b>, <b>подвела́</b>. Cặp CHT: <b>подводи́ть</b>.</div>'
    '<div class="hd-warn">Rất hay gặp với NGƯỜI (cách 4): làm người đang trông cậy mình phải '
    'thất vọng — <b>Не подведи́ меня́!</b> Đừng làm tôi thất vọng nhé!</div>'
    '<div class="hd-warn"><b>подвести́ ито́ги</b> — tổng kết, nhìn lại.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>подводи́ть</b> (CHT) · <b>вести́</b> dẫn · <b>завести́</b> nổ '
    'máy; lập · <b>провести́</b> tiến hành</div>'
)

# --------------------------------------------------------------------- подводить
S["подводить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span><span class="hd-gloss">SÁT LẠI '
    'GẦN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вод-и́ть</span><span class="hd-gloss">DẪN — '
    'chính là <b>води́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thể CHƯA HOÀN THÀNH của <b>подвести́</b>: đang dẫn, hay dẫn lại gần '
    '(<b>к</b> + cách 3); với người (cách 4) là làm thất vọng: <b>Он никогда́ не подво́дит '
    'друзе́й</b> — anh ấy không bao giờ phụ lòng bạn bè. Ngôi «tôi» <i>д → ж</i>, các ngôi '
    'khác trọng âm lùi: <b>подво́дишь</b>, <b>подво́дят</b>.</div>'
    '<div class="hd-warn"><b>я подвожу́</b> trùng với «tôi cho đi nhờ xe» của '
    '<b>подвози́ть</b>. Ngôi khác mới tách: <b>подво́дишь</b> / <b>подво́зишь</b>.</div>'
    '<div class="hd-warn"><b>подво́дный</b> «dưới nước» KHÁC gốc: ở đó là <b>вода́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>подвести́</b> (HT) · <b>води́ть</b> dẫn đi lại · <b>вводи́ть</b> '
    'đưa vào, nhập</div>'
)

# --------------------------------------------------------------------- католик
S["католик"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn Hy Lạp <i>katholikos</i> «phổ quát, chung cho tất cả», không '
    'chẻ ra mảnh Nga được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người thuộc Giáo hội «phổ quát» ⇒ tín đồ Công giáo. Tiếng Anh '
    '<i>Catholic</i> cùng gốc, nhưng tiếng Nga nhấn <b>-то́-</b>; tận cùng <b>-ик</b> như các '
    'từ chỉ người <b>фи́зик</b>, <b>кри́тик</b>. Phụ nữ: <b>католи́чка</b>.</div>'
    '<div class="hd-warn"><b>като́лик</b> là NGƯỜI; «thuộc Công giáo» phải là tính từ '
    '<b>католи́ческий</b>: <b>католи́ческая це́рковь</b>. Tiếng Anh dùng một chữ '
    '<i>Catholic</i> cho cả hai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>католи́ческий</b> thuộc Công giáo · <b>католи́чка</b> nữ tín đồ '
    '(<i>к → ч</i>) · <b>католи́чество</b> đạo Công giáo</div>'
)

# --------------------------------------------------------------------- мусульманин
S["мусульманин"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мусульма́н-</span><span class="hd-gloss">HỒI '
    'GIÁO — mượn qua Ba Tư, cùng gốc Ả Rập với <i>Muslim</i>, <i>Islam</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ин</span><span class="hd-gloss">MỘT người — '
    'rụng ở số nhiều</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng khuôn <b>христиани́н</b>, <b>граждани́н</b>: số nhiều rụng '
    '<b>-ин</b> — <b>мусульма́не</b>, cách 2 trụi đuôi: <b>мно́го мусульма́н</b>. Riêng ở đây '
    'trọng âm đứng yên. Phụ nữ: thay <b>-ин</b> bằng <b>-ка</b> — <b>мусульма́нка</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мусульма́нка</b> nữ tín đồ · <b>мусульма́нский</b> thuộc Hồi giáo '
    '· <b>мусульма́нство</b> đạo Hồi</div>'
)

# --------------------------------------------------------------------- россиянин
S["россиянин"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">росси-</span><span class="hd-gloss">nước NGA '
    '— <b>Росси́я</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́н-</span><span class="hd-gloss">người '
    'thuộc xứ — như <b>-ан-</b> trong <b>англича́нин</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ин</span><span class="hd-gloss">MỘT người — '
    'rụng ở số nhiều</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Người của nước Nga» ⇒ công dân Nga, bất kể dân tộc. Số nhiều rụng '
    '<b>-ин</b>: <b>россия́не</b>, cách 2 trụi đuôi: <b>россия́н</b>. Phụ nữ: '
    '<b>россия́нка</b>.</div>'
    '<div class="hd-warn"><b>россия́нин</b> đi với <b>росси́йский</b> (quốc gia, quốc tịch); '
    '<b>ру́сский</b> là dân tộc, tiếng nói. Người dân tộc khác mang quốc tịch Nga vẫn là '
    '<b>россия́нин</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>Росси́я</b> nước Nga · <b>росси́йский</b> thuộc quốc gia Nga · '
    '<b>россия́нка</b> nữ công dân Nga</div>'
)

# --------------------------------------------------------------------- забастовка
S["забастовка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span><span class="hd-gloss">BẮT '
    'ĐẦU</span></div>'
    '<div class="hd-row"><span class="hd-piece">-баст-</span><span class="hd-gloss">«THÔI, ĐỦ '
    'RỒI!» — <b>ба́ста</b>, mượn Ý <i>basta</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ов-к-а</span><span class="hd-gloss">→ danh '
    'từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Công nhân hô «thôi, không làm nữa!» ⇒ cuộc đình công. Cách 2 số '
    'nhiều chèn <i>о</i>: <b>забасто́вок</b>. Tuyên bố đình công: <b>объяви́ть '
    'забасто́вку</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: lối nối với <b>ба́ста</b> là từ nguyên, không phải luật '
    'suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бастова́ть</b> đình công · <b>забасто́вщик</b> người đình '
    'công</div>'
)

# --------------------------------------------------------------------- нищий
S["нищий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">нищ-</span><span class="hd-gloss">CÙNG KHỔ, '
    'không còn gì — gốc trơn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span><span class="hd-gloss">đuôi tính từ '
    '(sau <i>щ</i> viết <i>и</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nặng hơn <b>бе́дный</b> một bậc: <b>бе́дный</b> là nghèo, '
    '<b>ни́щий</b> là nghèo tới mức phải ngửa tay xin. Dạng ngắn giống đực trụi đuôi, giống '
    'cái đẩy trọng âm ra cuối: <b>нищ</b>, <b>нища́</b>, <b>ни́щи</b>.</div>'
    '<div class="hd-warn">Còn đứng một mình làm danh từ «kẻ ăn xin», vẫn chia như tính từ: '
    '<b>дать де́нег ни́щему</b> cho người ăn xin tiền.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>нищета́</b> cảnh bần cùng · <b>ни́щенский</b> bèo bọt (lương, mức '
    'sống) · <b>обнища́ть</b> khánh kiệt</div>'
)

# --------------------------------------------------------------------- критик
S["критик"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">крит-</span><span class="hd-gloss">PHÁN XÉT — '
    'Hy Lạp <i>krinein</i>, như <i>critic</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ик</span><span class="hd-gloss">NGƯỜI (khác '
    '<b>-ика</b> = hoạt động, ngành)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người phán xét hay dở ⇒ nhà phê bình; cũng là người hay chê. '
    '<b>кри́тик</b> ↔ <b>кри́тика</b> cùng khuôn <b>фи́зик</b> ↔ <b>фи́зика</b>, trọng âm '
    'đứng yên ở đầu. <b>литерату́рный кри́тик</b> nhà phê bình văn học.</div>'
    '<div class="hd-warn"><b>кри́тика</b> vừa là «sự phê bình», vừa là cách 2, cách 4 của '
    '<b>кри́тик</b>: <b>слу́шать кри́тика</b> = nghe NHÀ phê bình; nghe LỜI phê bình là '
    '<b>слу́шать кри́тику</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кри́тика</b> sự phê bình · <b>критикова́ть</b> phê bình · '
    '<b>крити́ческий</b> phê phán; nguy kịch · <b>крите́рий</b> tiêu chí</div>'
)

# --------------------------------------------------------------------- критический
S["критический"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">крит-</span><span class="hd-gloss">PHÁN XÉT — '
    'Hy Lạp <i>krinein</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ческ-ий</span><span class="hd-gloss">= '
    '<i>-ical</i> tiếng Anh: <i>critical</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hai nghĩa từ hai danh từ cùng gốc: «phán xét» như <b>кри́тика</b> ⇒ '
    'có tính phê phán (<b>крити́ческое мышле́ние</b> tư duy phản biện); «khúc ngoặt» như '
    '<b>кри́зис</b> ⇒ nguy kịch, then chốt (<b>крити́ческое состоя́ние</b> tình trạng nguy '
    'kịch). Trọng âm dời: <b>кри́тика</b> → <b>крити́ческий</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кри́тик</b> nhà phê bình · <b>кри́тика</b> sự phê bình · '
    '<b>критикова́ть</b> phê bình · <b>кри́зис</b> khủng hoảng</div>'
)

# --------------------------------------------------------------------- организатор
S["организатор"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">организ-</span><span class="hd-gloss">= '
    '<i>organize</i> — như <b>организова́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́тор</span><span class="hd-gloss">NGƯỜI làm '
    '(= Latin <i>-ator</i>), giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người đứng ra tổ chức. Đổi đuôi là ra việc: <b>организа́тор</b> '
    'người ↔ <b>организа́ция</b> việc tổ chức, cơ quan — trọng âm cùng một chỗ. Tổ chức CÁI '
    'GÌ: cách 2 — <b>организа́тор конце́рта</b>.</div>'
    '<div class="hd-warn">Số nhiều <b>организа́торы</b>, trọng âm đứng yên — khác <b>до́ктор '
    '→ доктора́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>организа́ция</b> tổ chức · <b>организова́ть</b> tổ chức (động từ) '
    '· <b>органи́зм</b> cơ thể</div>'
)

# --------------------------------------------------------------------- терапевт
S["терапевт"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn Hy Lạp <i>therapeutēs</i> «người chăm sóc, chữa trị», không '
    'chẻ ra mảnh Nga được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc <i>therapist</i>, <i>therapy</i>: người chữa trị ⇒ ở Nga là '
    'bác sĩ nội khoa. Trọng âm luôn ở <b>-пе́вт</b>: <b>терапе́вт</b>, '
    '<b>терапе́вта</b>.</div>'
    '<div class="hd-warn">Bẫy <i>therapist</i>: <b>терапе́вт</b> là bác sĩ khám đầu tiên ở '
    'phòng khám (<b>участко́вый терапе́вт</b>). Nhà trị liệu tâm lý là '
    '<b>психотерапе́вт</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>терапи́я</b> liệu pháp; nội khoa · <b>психотерапе́вт</b> nhà trị '
    'liệu tâm lý</div>'
)

# --------------------------------------------------------------------- инвалид
S["инвалид"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ин-</span><span class="hd-gloss">KHÔNG (Latin '
    '<i>in-</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вали́д</span><span class="hd-gloss">KHOẺ '
    '(Latin <i>validus</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mượn Latin, chẻ theo Latin: «không còn khoẻ» ⇒ người khuyết tật — '
    'chính là <i>invalid</i> tiếng Anh. Trọng âm luôn ở <b>-ли́-</b>. <b>инвали́д войны́</b> '
    'thương binh; <b>инвали́дная коля́ска</b> xe lăn.</div>'
    '<div class="hd-warn"><b>инвали́д</b> là từ trong luật, giấy tờ; nói tế nhị về người thì '
    'dùng <b>челове́к с инвали́дностью</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>инвали́дность</b> tình trạng khuyết tật · <b>инвали́дный</b> dành '
    'cho người khuyết tật</div>'
)

# --------------------------------------------------------------------- спасатель
S["спасатель"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span><span class="hd-gloss">tiền tố, ở '
    'đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пас-а-</span><span class="hd-gloss">CHE CHỞ, '
    'trông giữ — thân của <b>спаса́ть</b> cứu</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тель</span><span class="hd-gloss">NGƯỜI làm '
    '— như <b>води́тель</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Người cứu» làm nghề ⇒ nhân viên cứu hộ (bãi biển, núi, vùng thiên '
    'tai). Đuôi <b>-тель</b> luôn giống đực dù tận cùng <b>-ь</b>; trọng âm giữ như động từ: '
    '<b>спаса́ть → спаса́тель</b>.</div>'
    '<div class="hd-warn">Dập lửa là <b>пожа́рный</b>; tìm và đưa người ra khỏi chỗ nguy là '
    '<b>спаса́тель</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>спаса́ть</b> / <b>спасти́</b> cứu · <b>спасе́ние</b> sự cứu thoát '
    '· <b>спаса́тельный жиле́т</b> áo phao · <b>спаси́бо</b> cảm ơn</div>'
)

# --------------------------------------------------------------------- бедность
S["бедность"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бедн-</span><span class="hd-gloss">NGHÈO — '
    '<b>бе́дный</b>, gốc <i>бед-</i> TAI HOẠ, CẢNH KHỐN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ость</span><span class="hd-gloss">→ danh từ '
    'trừu tượng, luôn giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bỏ <b>-ый</b> của <b>бе́дный</b>, thêm <b>-ость</b> ⇒ «cái nghèo». '
    'Trọng âm giữ ở gốc như tính từ. <b>жить в бе́дности</b> sống trong cảnh nghèo.</div>'
    '<div class="hd-warn"><b>за черто́й бе́дности</b> — dưới mức nghèo («bên kia vạch '
    'nghèo»).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бе́дный</b> nghèo, tội nghiệp · <b>беда́</b> tai hoạ · '
    '<b>бедня́к</b> người nghèo · <b>бе́дствие</b> thảm hoạ</div>'
)

# --------------------------------------------------------------------- бедствие
S["бедствие"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бед-</span><span class="hd-gloss">TAI HOẠ, '
    'CẢNH KHỐN — <b>беда́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ств-ие</span><span class="hd-gloss">→ danh '
    'từ trừu tượng giống trung, như <b>де́йствие</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>беда́</b> cỡ lớn ⇒ thảm hoạ: <b>беда́</b> có thể chỉ là chuyện '
    'rủi của một người, <b>бе́дствие</b> thường giáng xuống cả vùng, cả nước. Cách 2 số nhiều '
    'đuôi <b>-ий</b>: <b>бе́дствий</b>.</div>'
    '<div class="hd-warn"><b>стихи́йное бе́дствие</b> thiên tai · <b>терпе́ть бе́дствие</b> '
    '(tàu, máy bay) đang lâm nạn · <b>сигна́л бе́дствия</b> tín hiệu cấp cứu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>беда́</b> tai hoạ · <b>бе́дный</b> nghèo, tội nghiệp · '
    '<b>бе́дность</b> sự nghèo khó</div>'
)

# --------------------------------------------------------------------- интеллигенция
S["интеллигенция"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">интеллиген(т)-</span><span '
    'class="hd-gloss">NGƯỜI TRÍ THỨC — <b>интеллиге́нт</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ция</span><span class="hd-gloss">đuôi danh '
    'từ giống cái; <i>т</i> nhường chỗ cho <i>ц</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cả lớp <b>интеллиге́нт</b> gộp lại ⇒ giới trí thức; tiếng Anh '
    '<i>intelligentsia</i> chính là mượn lại từ tiếng Nga. Danh từ tập hợp, thường ở số ít: '
    '<b>ру́сская интеллиге́нция</b>.</div>'
    '<div class="hd-warn">KHÔNG phải <i>intelligence</i>: trí thông minh là <b>ум</b>, '
    '<b>интелле́кт</b>; tình báo là <b>разве́дка</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>интеллиге́нт</b> người trí thức · <b>интеллиге́нтный</b> có học, '
    'có văn hoá · <b>интелле́кт</b> trí tuệ</div>'
)

# --------------------------------------------------------------------- конкуренция
S["конкуренция"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кон-</span><span class="hd-gloss">CÙNG (Latin '
    '<i>con-</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-кур-</span><span class="hd-gloss">CHẠY — như '
    '<b>ко́нкурс</b>, <b>курье́р</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́нция</span><span class="hd-gloss">= '
    '<i>-ence</i>, danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mượn Latin, chẻ theo Latin: «cùng chạy đua» ⇒ sự cạnh tranh. Người '
    'là <b>конкуре́нт</b>, việc là <b>конкуре́нция</b> — <i>т → ц</i> như <b>интеллиге́нт → '
    'интеллиге́нция</b>. <b>жёсткая конкуре́нция</b> cạnh tranh gay gắt.</div>'
    '<div class="hd-warn"><b>вне конкуре́нции</b> — không ai sánh kịp · <b>соста́вить '
    'конкуре́нцию</b> + cách 3: cạnh tranh được với ai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>конкуре́нт</b> đối thủ cạnh tranh · <b>конкури́ровать</b> cạnh '
    'tranh · <b>ко́нкурс</b> cuộc thi</div>'
)

# --------------------------------------------------------------------- зять
S["зять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người đàn ông vào nhà mình nhờ cưới: cưới con gái mình ⇒ con rể; '
    'cưới chị, em gái mình ⇒ anh rể, em rể. Số nhiều thêm <b>-ья</b>, trọng âm ra cuối như '
    '<b>мужья́</b>, <b>сыновья́</b>; nhưng cách 2 là <b>-ёв</b>: <b>зятья́</b>, '
    '<b>зятьёв</b>, <b>зятья́м</b>.</div>'
    '<div class="hd-warn">Anh <i>brother-in-law</i> gộp nhiều người, Nga tách: chồng của chị, '
    'em gái mình là <b>зять</b>; anh em trai của vợ là <b>шу́рин</b>, của chồng là '
    '<b>де́верь</b>.</div>'
)

B = {
    "docbangmat": 108,
    "loitubat": 4,
    "nguonsai": 3,
    "baolen": [
        "V cần duyệt (4): подвести + подводить (THÊM «làm thất vọng, phụ lòng» — gloss let down / disappoint / fail, nghĩa hay gặp nhất với người mà đề cũ thiếu hẳn; «tổng kết» chỉ sống trong подвести́ ито́ги nên để ở ô đỏ, không vào đề) · развестись («sinh sôi nhiều» ⇒ «sinh sôi nảy nở», giờ trùng y разводиться, badge thể tách) · спасатель (bỏ «lính cứu hỏa cứu hộ» = пожарный; gloss không có firefighter).",
        "Ví dụ: 3 câu của mỗi thẻ подвести / подводить (_opus_k216.json) đều chỉ minh hoạ «dẫn tới, đưa lại gần», chưa câu nào có «làm thất vọng» — nếu duyệt V thì nên đổi một câu.",
        "бедствие: giữ nguyên «thiên tai» trong đề dù đúng ra thiên tai là стихи́йное бе́дствие (gloss chỉ disaster / calamity) — không sửa vì chưa sai hẳn; luồng chính cân.",
        "Nguồn đã bác (3): vi của спасатель («lính cứu hỏa»); vi của подвести và подводить thiếu nghĩa let down.",
        "Lỗi tự bắt (4): католик chẻ ép -ик theo kiểu Nga ⇒ nói thẳng từ mượn không chẻ; организатор «trọng âm luôn ở -а-» nói quá (а́втор không thế) ⇒ bỏ; бедствие «беда là của một người» nói quá ⇒ hạ xuống; россиянин ví dụ người Tatar kết luận cứng ⇒ viết lại.",
        "Không chắc: забастовка ← баста đã ghi ⚠️ Mức tin. Va chạm sau khi áp V chưa chạy lại trên Anki (agent không chạm Anki) — cửa tiep báo không có với đề cũ.",
        "Họ hàng cố ý vắng: зять. Câu «kẻ ăn xin» ở нищий chỉ nằm trong ô đỏ, không vào V.",
    ],
}
