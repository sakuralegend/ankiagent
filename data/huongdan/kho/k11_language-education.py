# -*- coding: utf-8 -*-
"""k11 — language::education: đồ dùng và việc làm trong lớp học.

Trục: hai gốc động từ -пис- (viết) và -чит- (đọc), mỗi gốc một cặp thể; phần
còn lại là đồ dùng (тетра́дь · слова́рь · каранда́ш) và sản phẩm chữ nghĩa
(текст · стих · дикта́нт · ле́кция · тест) — phần lớn là từ mượn nên chỗ đáng
dạy nằm ở TỪ NGUYÊN chứ không ở cấu tạo Nga.
"""

S = {}
V = {}

# ------------------------------------------------------------------ chữ nghĩa

S["диктант"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дикт-</span>'
    '<span class="hd-gloss">đọc to cho người khác chép (Latin <i>dictare</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ант</span>'
    '<span class="hd-gloss">đuôi của từ mượn; ở đây chỉ BÀI TẬP</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thầy đọc — trò chép, đúng nghĩa gốc <i>dictare</i>. Tiếng Anh cùng '
    'gốc: <i>dictation</i>, <i>dictionary</i>, <i>dictator</i>.</div>'
    '<div class="hd-warn">Đuôi <b>-ант</b> thường chỉ NGƯỜI (<b>музыка́нт</b> nhạc công), '
    'riêng <b>дикта́нт</b> là ngoại lệ: nó là bài tập, không phải người.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>диктова́ть</b> đọc cho chép · <b>дикта́тор</b> kẻ độc tài · '
    '<b>ди́ктор</b> phát thanh viên</div>'
)

S["тест"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">тест</span>'
    '<span class="hd-gloss">mượn nguyên khối từ tiếng Anh <i>test</i> — không chẻ được'
    '</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa cũng rộng đúng như tiếng Anh: bài kiểm tra ở lớp, và phép thử '
    'ngoài đời — <i>тест на бере́менность</i> que thử thai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тести́ровать</b> kiểm thử, chạy thử</div>'
)

S["текст"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">текст</span>'
    '<span class="hd-gloss">Latin <i>textus</i> = "cái được DỆT" (<i>texere</i> dệt)'
    '</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người La Mã coi một bài viết là tấm vải dệt bằng chữ. Cùng gốc trong '
    'tiếng Anh: <i>text</i>, <i>textile</i> vải, <i>texture</i> kết cấu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>конте́кст</b> ngữ cảnh — "dệt CÙNG" · <b>подте́кст</b> hàm ý — '
    '"dệt BÊN DƯỚI"</div>'
)

S["стих"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">стих</span>'
    '<span class="hd-gloss">Hy Lạp <i>stíchos</i> = HÀNG, DÒNG — không chẻ được</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc là một HÀNG, nên <b>стих</b> là một dòng thơ chứ không phải '
    'cả bài.</div>'
    '<div class="hd-warn">Cả bài thơ là <b>стихотворе́ние</b>. Riêng số nhiều <b>стихи́</b> mới '
    'mang nghĩa "thơ" nói chung.</div>'
    '<div class="hd-why">Bảng chia: trọng âm chỉ đứng yên ở dạng gốc <b>стих</b>, còn mọi cách '
    'khác nó nhảy hẳn ra đuôi (<b>стиха́</b>, <b>стихи́</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>стихотворе́ние</b> bài thơ · <b>стихотво́рный</b> thuộc về thơ '
    '(<b>стих</b> + <b>твор-</b> tạo ra)</div>'
)

# ------------------------------------------------------------------ đồ dùng

S["карандаш"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кара-</span>'
    '<span class="hd-gloss">ĐEN (tiếng Turk)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-даш ← таш</span>'
    '<span class="hd-gloss">ĐÁ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">"Đá đen" — đúng là thỏi than chì đen kẹp giữa hai mảnh gỗ.</div>'
    '<div class="hd-why">Bảng chia: trọng âm ở <b>каранда́ш</b> nằm cuối từ, rồi rời hẳn sang '
    'đuôi ở mọi cách khác (<b>карандаша́</b>, <b>карандаши́</b>).</div>'
    '<div class="hd-warn">⚠️ Mức tin: hai mảnh trên là TỪ NGUYÊN tiếng Turk, để nhớ mặt chữ. '
    'Tiếng Nga ngày nay coi đây là một khối liền, không chẻ ra được.</div>'
)

S["тетрадь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">тетра-</span>'
    '<span class="hd-gloss">BỐN (Hy Lạp)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дь</span>'
    '<span class="hd-gloss">phần đuôi Nga hoá, kết bằng dấu mềm <b>ь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hy Lạp <i>tetrádion</i> = tờ giấy gấp làm TƯ rồi khâu lại thành tập. '
    'Cùng tiền tố với <i>tetrahedron</i> khối bốn mặt trong tiếng Anh.</div>'
    '<div class="hd-warn"><b>тетра́дь</b> kết bằng <b>ь</b> nhưng là giống CÁI, còn '
    '<b>слова́рь</b> cùng đuôi ấy lại giống ĐỰC. Đuôi <b>ь</b> không cho biết giống — phải nhớ '
    'từng từ một.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тетра́дка</b> quyển vở (cách nói thân mật)</div>'
)

S["словарь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">слов-</span>'
    '<span class="hd-gloss">TỪ, LỜI — gốc của <b>сло́во</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-арь</span>'
    '<span class="hd-gloss">đuôi chỉ NƠI CHỨA hoặc NGƯỜI COI GIỮ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">"Chỗ chứa các từ". Cùng đuôi: <b>буква́рь</b> sách vỡ lòng (từ '
    '<b>бу́ква</b> chữ cái), <b>врата́рь</b> thủ môn (người giữ cổng).</div>'
    '<div class="hd-why">Bảng chia: trọng âm rời <b>слова́рь</b> để sang hẳn đuôi ở mọi cách '
    'còn lại (<b>словаря́</b>, <b>словари́</b>).</div>'
    '<div class="hd-warn">Kết bằng <b>ь</b> nhưng giống ĐỰC — ngược với <b>тетра́дь</b> cùng '
    'đuôi mà giống cái.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сло́во</b> từ, lời · <b>посло́вица</b> tục ngữ</div>'
)

# ------------------------------------------------------------------ gốc -пис- (viết)

S["писать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пис-</span>'
    '<span class="hd-gloss">VẠCH DẤU, khắc dấu lên mặt phẳng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>пис-</b> vốn là "vạch dấu", nên <b>писа́ть</b> vừa là viết chữ '
    'vừa là VẼ tranh sơn dầu. Cùng nguồn Ấn–Âu với <i>picture</i>, <i>paint</i>.</div>'
    '<div class="hd-why">Bảng chia: ở thì hiện tại <b>с</b> đổi thành <b>ш</b> ở mọi ngôi '
    '(<b>пишу́</b>, <b>пи́шешь</b>…), và trọng âm chỉ đứng ở đuôi tại ngôi "tôi", các ngôi còn '
    'lại lùi về gốc <b>пи́ш-</b>.</div>'
    '<div class="hd-warn">Trọng âm ở đây ĐỔI HẲN NGHĨA: <b>писа́ть</b> là viết, còn '
    '<b>пи́сать</b> (nhấn đầu) là đi tiểu. Nhấn sai chỗ là nói ra một từ khác.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>письмо́</b> lá thư · <b>писа́тель</b> nhà văn · '
    '<b>пи́сьменный</b> thuộc về chữ viết</div>'
)

S["написать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">tiền tố THỂ — không thêm nghĩa, chỉ khoá hành động lại thành '
    '"viết xong"</span></div>'
    '<div class="hd-row"><span class="hd-piece">-писать</span>'
    '<span class="hd-gloss">viết (xem thẻ <b>писа́ть</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng kiểu ghép: <b>рисова́ть</b> vẽ → <b>нарисова́ть</b> vẽ xong. '
    'Tiền tố <b>на-</b> đóng hành động lại, cho ra một sản phẩm đã hoàn tất.</div>'
    '<div class="hd-why">Bảng chia: y hệt <b>писа́ть</b> — <b>с</b> đổi thành <b>ш</b> '
    '(<b>напишу́</b>, <b>напи́шешь</b>…), trọng âm chỉ ở đuôi tại ngôi "tôi". Nhưng vì đây là '
    'thể hoàn thành nên bảng "hiện tại" ấy thật ra mang nghĩa TƯƠNG LAI.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>на́дпись</b> dòng chữ ghi phía trên · <b>по́дпись</b> chữ ký · '
    '<b>нарисова́ть</b> vẽ xong (cùng tiền tố <b>на-</b>)</div>'
)

S["записывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">ghi XUỐNG để giữ lại, chốt thành bản lưu</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пис-</span>'
    '<span class="hd-gloss">viết (xem thẻ <b>писа́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-</span>'
    '<span class="hd-gloss">đuôi kéo bản hoàn thành <b>записа́ть</b> trở lại thành CHƯA hoàn '
    'thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>писа́ть</b> là viết ra chữ; thêm <b>за-</b> thành "viết xuống để '
    'lưu" — số điện thoại, bài giảng, cả giọng hát (ghi âm).</div>'
    '<div class="hd-warn">Đừng lẫn với <b>писа́ть</b>: cái quan trọng ở <b>запи́сывать</b> là '
    'BẢN LƯU còn lại, không phải động tác cầm bút.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>за́пись</b> bản ghi · <b>запи́ска</b> mẩu giấy nhắn · '
    '<b>записа́ть</b> ghi lại (thể hoàn thành)</div>'
)

# ------------------------------------------------------------------ gốc -чит- (đọc) + học

S["читать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">чит-</span>'
    '<span class="hd-gloss">ĐỌC; gốc cổ nghĩa là "lần từng cái một, đếm"</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">đuôi nguyên thể, chia đều đặn không có gì bất thường</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đọc là lần lượt nhận từng dấu hiệu — nên cùng gốc với '
    '<b>счита́ть</b> đếm. Người Nga "đếm chữ" thì thành "đọc".</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>чте́ние</b> việc đọc · <b>чита́тель</b> độc giả · '
    '<b>счита́ть</b> đếm, cho rằng</div>'
)

S["прочитать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">XUYÊN SUỐT, từ đầu tới cuối</span></div>'
    '<div class="hd-row"><span class="hd-piece">-читать</span>'
    '<span class="hd-gloss">đọc (xem thẻ <b>чита́ть</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>про-</b> đặt cái ĐÍCH vào hành động: <b>чита́ть</b> là đang đọc, '
    '<b>прочита́ть</b> là đọc hết từ đầu tới cuối.</div>'
    '<div class="hd-warn">Cụm phải thuộc: <b>прочита́ть ле́кцию</b> hay <b>прочита́ть '
    'докла́д</b> nghĩa là GIẢNG BÀI, TRÌNH BÀY trước đám đông — không phải đọc thầm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">Cùng tiền tố <b>про-</b> "làm cho hết": <b>прослу́шать</b> nghe hết · '
    '<b>просмотре́ть</b> xem hết</div>'
)

S["учить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">уч-</span>'
    '<span class="hd-gloss">LÀM CHO QUEN TAY — gốc chung của cả dạy lẫn học</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi nguyên thể lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một gốc <b>уч-</b> ôm cả hai đầu của việc học. Thứ tách hai nghĩa ra '
    'không phải bản thân từ, mà là CÁCH của tân ngữ đi sau.</div>'
    '<div class="hd-warn"><b>учи́ть</b> + đồ vật ở cách 4 = HỌC THUỘC cái đó. '
    '<b>учи́ть</b> + người ở cách 4 + môn ở cách 3 = DẠY người ấy môn ấy.</div>'
    '<div class="hd-why">Bảng chia: trọng âm chỉ rơi vào đuôi ở ngôi "tôi" (<b>учу́</b>), mọi '
    'ngôi còn lại lùi về gốc (<b>у́чишь</b>, <b>у́чит</b>, <b>у́чат</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>учи́тель</b> giáo viên · <b>учени́к</b> học sinh · '
    '<b>учёба</b> việc học · <b>нау́ка</b> khoa học</div>'
)

# ------------------------------------------------------------------ giờ học

S["химия"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">хим-</span>'
    '<span class="hd-gloss">gốc mượn, đi vòng từ tiếng Ả Rập <i>al-kīmiyā</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ия</span>'
    '<span class="hd-gloss">đuôi tên NGÀNH, luôn là danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhìn đuôi <b>-ия</b> là biết ngay hai điều: đây là tên một ngành, và '
    'nó giống cái — giống hệt <b>исто́рия</b>, <b>геогра́фия</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>хи́мик</b> nhà hoá học · <b>хими́ческий</b> thuộc về hoá học — '
    'chú ý trọng âm chạy sang giữa từ ở tính từ</div>'
)

S["лекция"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">лекц-</span>'
    '<span class="hd-gloss">Latin <i>lectio</i> = VIỆC ĐỌC (<i>legere</i> đọc, lượm)'
    '</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ия</span>'
    '<span class="hd-gloss">đuôi tên sự việc, danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bài giảng thời xưa đúng nghĩa là thầy ĐỌC sách cho trò chép. Cùng gốc '
    'Latin với <i>lecture</i>, <i>collect</i>, <i>select</i>.</div>'
    '<div class="hd-warn">Người Nga "đọc" một bài giảng chứ không "nói": <b>чита́ть '
    'ле́кцию</b> mới là cách diễn đạt chuẩn cho việc đứng lớp.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ле́ктор</b> giảng viên · <b>колле́кция</b> bộ sưu tập (cùng gốc '
    'Latin <i>lect-</i> lượm, chọn)</div>'
)

# ---------------------------------------------------------------------------
# VIỆC THỨ HAI — field `Vietnamese` (README §2c): thuần danh sách nghĩa.
V["стих"] = "câu thơ, dòng thơ, câu kinh thánh"
V["лекция"] = "bài giảng, buổi giảng"
V["писать"] = "viết, nhắn tin"
V["читать"] = "đọc"
V["записывать"] = "ghi chép, ghi lại, ghi âm"
