# -*- coding: utf-8 -*-
"""k35 — people::professions: tên nghề, trục là ĐUÔI CHỈ NGƯỜI.

Nga tự đẻ tên nghề bằng hậu tố (-тель, -ник, -ик, -иц/-ниц/-щиц cho nữ);
từ mượn thì bê nguyên khối (-ор, -ер, -мен) và không có dạng giống cái.
Mỗi thẻ chỉ nói đuôi của CHÍNH NÓ — không dựng bảng đuôi chung.
"""

S = {}
V = {}

# ---------------------------------------------------------------- коллега
S["коллега"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кол-</span>'
    '<span class="hd-gloss">CÙNG (tiền tố Latin <i>col-</i> = <i>con-</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лег-</span>'
    '<span class="hd-gloss">CỬ, GIAO VIỆC (Latin <i>legare</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi danh từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Latin <i>collega</i> = "người cùng được cử vào một chức" '
    '→ người làm chung việc với mình. Đúng chữ <i>colleague</i> tiếng Anh, '
    'chỉ đổi vỏ.</div>'
    '<div class="hd-warn">Đuôi <b>-а</b> nên chia y hệt danh từ giống cái, '
    'nhưng từ này dùng cho CẢ NAM LẪN NỮ — thứ đi kèm mới cho biết giới: '
    '<b>мой колле́га</b> (anh đồng nghiệp) · <b>моя́ колле́га</b> (chị đồng nghiệp).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>колле́гия</b> hội đồng, ban · '
    '<b>коллекти́в</b> tập thể</div>'
)

# ---------------------------------------------------------------- актриса
S["актриса"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">акт-</span>'
    '<span class="hd-gloss">DIỄN, MÀN KỊCH (Latin <i>actus</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ис-</span>'
    '<span class="hd-gloss">đuôi chỉ NGƯỜI NỮ, mượn theo tiếng Pháp</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chuỗi ba bậc: <b>акт</b> hồi kịch → <b>актёр</b> người diễn '
    '(nam) → <b>актри́са</b> người diễn (nữ). Tiếng Anh cũng đi đúng ba bậc đó: '
    '<i>act – actor – actress</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>актёр</b> diễn viên nam · <b>акт</b> hồi kịch, hành vi · '
    '<b>акти́вный</b> năng động, tích cực</div>'
)

# ---------------------------------------------------------------- певица
S["певица"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пе-/пев-</span>'
    '<span class="hd-gloss">HÁT (gốc của <i>петь</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-иц-</span>'
    '<span class="hd-gloss">đuôi chỉ NGƯỜI NỮ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>петь</b> hát → <b>певе́ц</b> ca sĩ nam → '
    '<b>певи́ца</b> ca sĩ nữ. Cặp đuôi <b>-ец</b> (nam) / <b>-ица</b> (nữ) lặp ở '
    'nhiều danh từ chỉ sinh vật: <b>лев</b> sư tử → <b>льви́ца</b> sư tử cái.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>петь</b> hát · <b>пе́сня</b> bài hát · '
    '<b>певе́ц</b> ca sĩ nam</div>'
)

# ---------------------------------------------------------------- учительница
S["учительница"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">уч-</span>'
    '<span class="hd-gloss">HỌC, DẠY</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-тель</span>'
    '<span class="hd-gloss">NGƯỜI làm việc ấy → <b>учи́тель</b> thầy giáo</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ниц-а</span>'
    '<span class="hd-gloss">đổi sang NGƯỜI NỮ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Xếp chồng đúng ba tầng: <b>учи́ть</b> dạy → <b>учи́тель</b> '
    'thầy giáo → <b>учи́тельница</b> cô giáo. Từ dài ra hai lần mà trọng âm vẫn bám '
    'chặt ở <b>-чи-</b>, không hề dịch.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>учи́ть</b> dạy · <b>учи́ться</b> học · '
    '<b>учени́к</b> học trò · <b>учи́тель</b> thầy giáo</div>'
)

# ---------------------------------------------------------------- продавщица
S["продавщица"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">ĐƯA HẲN RA KHỎI TAY</span></div>'
    '<div class="hd-row"><span class="hd-piece">-да-в-</span>'
    '<span class="hd-gloss">CHO, ĐƯA (gốc của <i>дать</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-щиц-а</span>'
    '<span class="hd-gloss">NGƯỜI NỮ LÀM NGHỀ ẤY</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">"Đưa hẳn ra khỏi tay" chính là BÁN: <b>дать</b> đưa + '
    '<b>про-</b> → <b>продава́ть</b> bán. Đuôi <b>-щик</b> (nam) / <b>-щиц-а</b> (nữ) '
    'là đuôi chuyên dùng để gọi tên NGHỀ: <b>убо́рщица</b> nữ lao công.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>продава́ть</b> bán · <b>прода́жа</b> việc bán · '
    '<b>продаве́ц</b> người bán hàng (nam) · <b>дать</b> đưa, cho</div>'
)

# ---------------------------------------------------------------- педагогический
S["педагогический"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пед-</span>'
    '<span class="hd-gloss">TRẺ EM (Hy Lạp <i>paid-</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-агог-</span>'
    '<span class="hd-gloss">DẪN DẮT (Hy Lạp <i>agogos</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ическ-ий</span>'
    '<span class="hd-gloss">đuôi tính từ "thuộc về"</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người Hy Lạp gọi kẻ DẪN TRẺ tới trường là <i>paidagogos</i>; '
    'nghĩa "nghề dạy học" mọc ra từ đó. Tiếng Anh giữ nguyên khối: <i>pedagogy</i>. '
    'Nói về NGÀNH SƯ PHẠM, không phải "sự học hành" nói chung.</div>'
    '<div class="hd-warn">⚠️ Bảng chia phía dưới có HAI ô máy dựng SAI, đừng chép: '
    'ô 1 cột "он" in педагоги́ческый và ô 5 cột "оно" in педагоги́ческым — chữ '
    '<b>ы</b> đó không có thật, đúng phải là <b>педагоги́ческий</b> và '
    '<b>педагоги́ческим</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>педаго́г</b> nhà sư phạm, người dạy học · '
    '<b>педаго́гика</b> khoa sư phạm</div>'
)
V["педагогический"] = "thuộc về sư phạm, thuộc về nghề dạy học"

# ---------------------------------------------------------------- медицинский
S["медицинский"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">медицин-</span>'
    '<span class="hd-gloss">Y HỌC (<b>медици́на</b>, Latin <i>medicina</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ск-</span>'
    '<span class="hd-gloss">THUỘC VỀ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là cái máy đẻ tính từ chạy êm nhất của tiếng Nga: '
    'lấy danh từ, dán <b>-ск-ий</b>, được "thuộc về danh từ đó" — <b>медици́на</b> '
    'y học → <b>медици́нский</b> thuộc y tế. Trọng âm ở lại chỗ cũ (<b>-ци́-</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>медици́на</b> y học · <b>ме́дик</b> người làm ngành y · '
    '<b>медсестра́</b> y tá</div>'
)

# ---------------------------------------------------------------- строительный
S["строительный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">стро-</span>'
    '<span class="hd-gloss">XÂY, DỰNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-тель</span>'
    '<span class="hd-gloss">NGƯỜI làm việc ấy → <b>строи́тель</b> thợ xây</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ba bậc: <b>стро́ить</b> xây → <b>строи́тель</b> thợ xây → '
    '<b>строи́тельный</b> thuộc về xây dựng. Trọng âm nhảy đúng MỘT lần, ngay lúc '
    'thêm <b>-тель</b> (<b>стро́ить</b> ở <b>о</b> → <b>строи́тель</b> ở <b>и</b>), '
    'rồi đứng yên.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>стро́ить</b> xây · <b>строи́тель</b> thợ xây · '
    '<b>строи́тельство</b> việc xây dựng · <b>стро́йка</b> công trường</div>'
)

# ---------------------------------------------------------------- химик
S["химик"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">хим-</span>'
    '<span class="hd-gloss">HÓA (gốc của <b>хи́мия</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ик</span>'
    '<span class="hd-gloss">NGƯỜI làm ngành ấy</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp NGÀNH / NGƯỜI: bỏ <b>-ия</b> thay bằng <b>-ик</b> là '
    'từ môn học ra người làm môn đó — <b>хи́мия</b> môn hóa → <b>хи́мик</b> nhà hóa '
    'học. Đổi đuôi kiểu này trọng âm ĐỨNG YÊN ở <b>хи́-</b>; nhưng thêm đuôi tính từ '
    'thì nó dịch ra sau: <b>хими́ческий</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>хи́мия</b> môn hóa học · '
    '<b>хими́ческий</b> thuộc về hóa học</div>'
)

# ---------------------------------------------------------------- художник
S["художник"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">худож-</span>'
    '<span class="hd-gloss">KHÉO TAY, TÀI NGHỆ (chữ Slav cổ, nay không đứng riêng)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ник</span>'
    '<span class="hd-gloss">NGƯỜI gắn với việc ấy</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen là "người khéo tay" — tiếng Nga chốt nó vào nghề '
    'tạo hình, nên <b>худо́жник</b> mặc định là họa sĩ (vẽ), chứ không phải nghệ sĩ '
    'nói chung.</div>'
    '<div class="hd-warn">⚠️ Mức tin: mảnh <b>худож-</b> là từ nguyên, không phải luật '
    'suy ra được. Nhưng đủ để chốt một điều dùng được: nó KHÔNG cùng gốc với '
    '<b>худо́й</b> (gầy; tồi) dù hai từ nhìn giống hệt nhau ở bốn chữ đầu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>худо́жественный</b> thuộc nghệ thuật · '
    '<b>худо́жество</b> mỹ thuật</div>'
)

# ---------------------------------------------------------------- бизнесмен
S["бизнесмен"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бизнес-</span>'
    '<span class="hd-gloss">KINH DOANH (Anh <i>business</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ме́н</span>'
    '<span class="hd-gloss">NGƯỜI (Anh <i>man</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bê nguyên khối <i>businessman</i>, hai mảnh vẫn nhìn ra được. '
    'Chỗ dễ sai là trọng âm: đứng riêng thì <b>би́знес</b> nhấn đầu, nhưng ghép vào '
    'thì nhấn dồn hết ra mảnh cuối — <b>бизнесме́н</b>. Nhiều từ mượn khác cùng đuôi '
    'cũng nhận trọng âm như vậy: <b>спортсме́н</b> vận động viên.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>би́знес</b> việc kinh doanh · '
    '<b>спортсме́н</b> vận động viên</div>'
)

# ---------------------------------------------------------------- менеджер
S["менеджер"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn nguyên khối tiếng Anh <i>manager</i>, '
    'vào tiếng Nga muộn (thời mở cửa kinh tế) nên chưa mọc mảnh Nga nào.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giữ nguyên chỗ nhấn của tiếng Anh — âm tiết ĐẦU: '
    '<b>ме́неджер</b>, và nó đứng yên suốt cả bảng chia. Còn một nét lạ của từ mượn '
    'mới: chữ <b>е</b> ở đây không làm mềm phụ âm đứng trước, khác hẳn từ Nga gốc.</div>'
    '<div class="hd-warn">Từ mượn chỉ nghề thường KHÔNG có dạng giống cái riêng: '
    'phụ nữ vẫn gọi là <b>ме́неджер</b> — khác hẳn nghề gốc Nga vốn có đuôi nữ '
    '(<b>певи́ца</b>, <b>учи́тельница</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ме́неджмент</b> việc quản trị, ngành quản lý</div>'
)

# ---------------------------------------------------------------- инженер
S["инженер"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">инжен-</span>'
    '<span class="hd-gloss">TÀI TRÍ, SÁNG CHẾ (Latin <i>ingenium</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́р</span>'
    '<span class="hd-gloss">NGƯỜI làm nghề ấy (đuôi mượn tiếng Pháp)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vào tiếng Nga qua tiếng Pháp <i>ingenieur</i>, cùng ổ với '
    '<i>engine</i> và <i>ingenious</i> tiếng Anh: "người nghĩ ra máy móc". Đuôi '
    '<b>-е́р</b> ở lớp từ mượn Pháp thường kéo trọng âm về cuối — <b>инжене́р</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>инжене́рный</b> thuộc về kỹ sư, thuộc kỹ thuật</div>'
)

# ---------------------------------------------------------------- профессор
S["профессор"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">RA TRƯỚC, CÔNG KHAI (Latin <i>pro-</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-фесс-</span>'
    '<span class="hd-gloss">TUYÊN XƯNG, NÓI RA (Latin <i>professus</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ор</span>'
    '<span class="hd-gloss">NGƯỜI làm việc ấy</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen Latin: "người công khai nói ra cái mình biết" — '
    'tức người đứng ra giảng. Cùng gốc với <b>профе́ссия</b> nghề nghiệp: cái nghề '
    'cũng là cái mình "tuyên xưng" mình làm.</div>'
    '<div class="hd-warn">Số nhiều KHÔNG lấy <b>-ы</b> như phần lớn danh từ giống '
    'đực: đuôi là <b>-а́</b> VÀ trọng âm nhảy hẳn ra cuối — số ít <b>профе́ссор</b> '
    'nhưng số nhiều <b>профессора́</b>, cách 2 <b>профессоро́в</b>. Cùng nhóm với '
    '<b>до́ктор</b> → <b>доктора́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>профе́ссия</b> nghề nghiệp · '
    '<b>профессиона́л</b> người chuyên nghiệp</div>'
)

# ---------------------------------------------------------------- диктор
S["диктор"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дикт-</span>'
    '<span class="hd-gloss">ĐỌC RA, ĐỌC CHO CHÉP (Latin <i>dictare</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ор</span>'
    '<span class="hd-gloss">NGƯỜI làm việc ấy</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng ổ với <i>dictate</i>, <i>dictionary</i> tiếng Anh. '
    'Ghép hai mảnh ra đúng nghề: người ĐỌC văn bản viết sẵn trên đài, trên TV.</div>'
    '<div class="hd-warn">Không phải "người dẫn chương trình" — người dẫn, người điều '
    'khiển buổi phát là <b>веду́щий</b>. <b>Ди́ктор</b> chỉ đọc bản tin đã soạn, '
    'không dẫn dắt, không phỏng vấn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>диктова́ть</b> đọc cho người khác chép · '
    '<b>дикта́нт</b> bài chính tả</div>'
)
V["диктор"] = "phát thanh viên, người đọc bản tin trên đài/TV"
