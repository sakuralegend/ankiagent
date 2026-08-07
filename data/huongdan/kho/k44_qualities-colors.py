# -*- coding: utf-8 -*-
"""k44 — qualities::colors: 11 tên màu. Trục của lô: mỗi tên màu đến từ MỘT
nguồn khác nhau (gốc Nga trơn, tên hoa/quả/vỏ cây, hay từ mượn châu Âu), và
tính từ màu là chỗ trọng âm dạng ngắn chạy nhiều nhất."""

S = {}
V = {}

# --------------------------------------------------------------------- синий
S["синий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">син-</span>'
    '<span class="hd-gloss">XANH LAM (xanh đậm)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span>'
    '<span class="hd-gloss">đuôi tính từ MỀM</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cả lô màu chỉ mình từ này biến đổi mềm: '
    '<b>си́ний</b>, <b>си́няя</b>, <b>си́нее</b>, <b>си́ние</b> — '
    'các màu khác đều đuôi cứng -ый/-ой.</div>'
    '<div class="hd-why">Dạng ngắn: chỉ giống cái kéo trọng âm ra đuôi '
    '(<b>синя́</b>); ba dạng kia giữ nguyên chỗ cũ (<b>синь</b>, '
    '<b>си́не</b>, <b>си́ни</b>).</div>'
    '<div class="hd-warn">Tiếng Nga cắt "xanh dương" thành HAI từ riêng chứ '
    'không phải hai sắc độ của một từ: <b>си́ний</b> là xanh đậm (mực, biển '
    'sâu), còn xanh nhạt, xanh da trời phải dùng <b>голубо́й</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>синева́</b> khoảng xanh thẳm · '
    '<b>сине́ть</b> ngả xanh · <b>синя́к</b> vết bầm tím</div>'
)
V["синий"] = "xanh lam, xanh dương đậm"

# ------------------------------------------------------------------- голубой
S["голубой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">голуб-</span>'
    '<span class="hd-gloss">từ го́лубь — chim bồ câu</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ой</span>'
    '<span class="hd-gloss">đuôi tính từ luôn mang trọng âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Màu xám xanh ở cổ con bồ câu, nên từ này là xanh '
    'nhạt, xanh da trời. Đuôi -ой có trọng âm nên cả bảng chia trọng âm nằm '
    'ở đuôi: <b>голубо́го</b>, <b>голубы́е</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: liên hệ với <b>го́лубь</b> là TỪ '
    'NGUYÊN (chuyện nguồn gốc), không phải luật suy ra được — dùng để nhớ, '
    'đừng dùng để đoán nghĩa từ mới.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>го́лубь</b> chim bồ câu · '
    '<b>голуби́ка</b> quả việt quất xanh · <b>голубе́ть</b> ngả xanh nhạt</div>'
)
V["голубой"] = "xanh da trời, xanh lơ, xanh nhạt"

# ---------------------------------------------------------------- оранжевый
S["оранжевый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">оранж-</span>'
    '<span class="hd-gloss">mượn tiếng Pháp orange — quả cam</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ев-ый</span>'
    '<span class="hd-gloss">đuôi tính từ; sau ж viết -ев-, không -ов-</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng một gốc với orange của tiếng Anh: tên màu đi ra '
    'từ tên quả. Đây là từ mượn nguyên khối, phần оранж- không có nghĩa riêng '
    'trong tiếng Nga.</div>'
    '<div class="hd-warn">Nhưng quả cam thì KHÔNG gọi theo gốc này: quả cam là '
    '<b>апельси́н</b>, mượn theo một đường khác. Gốc оранж- ở lại tiếng Nga '
    'chỉ để làm tên màu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оранжере́я</b> nhà kính trồng cây (vốn là "nhà '
    'trồng cam")</div>'
)

# --------------------------------------------------------------- коричневый
S["коричневый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">корич-</span>'
    '<span class="hd-gloss">từ кори́ца — quế</span></div>'
    '<div class="hd-row"><span class="hd-piece">-нев-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nâu = màu của vỏ quế. Chính <b>кори́ца</b> lại là '
    '"mẩu vỏ nhỏ" của <b>кора́</b> (vỏ cây), nên nâu ở đây đúng là màu vỏ '
    'cây.</div>'
    '<div class="hd-warn">Nâu của MẮT và TÓC không dùng từ này: mắt nâu là '
    '<b>ка́рие глаза́</b>, tóc nâu hạt dẻ là <b>кашта́новые во́лосы</b>. '
    '<b>кори́чневый</b> để dành cho đồ vật.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кора́</b> vỏ cây · <b>кори́ца</b> quế</div>'
)

# ------------------------------------------------------------------- розовый
S["розовый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">роз-</span>'
    '<span class="hd-gloss">từ ро́за — hoa hồng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ов-ый</span>'
    '<span class="hd-gloss">"có màu của, làm bằng"</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hồng là màu của <b>ро́за</b>. Hậu tố -ов- gắn thẳng '
    'vào tên một vật để ra tính từ "thuộc về vật ấy" — ở đây là "màu hoa '
    'hồng".</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ро́за</b> hoa hồng · <b>розе́тка</b> ổ cắm điện '
    '(vốn nghĩa "bông hồng nhỏ")</div>'
)

# --------------------------------------------------------------- фиолетовый
S["фиолетовый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">фиолет-</span>'
    '<span class="hd-gloss">mượn của châu Âu, gốc Latin viola — hoa '
    'tím</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ов-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bắc cầu thẳng sang violet của tiếng Anh — cùng một '
    'gốc Latin. Tên màu này đi vào tiếng Nga nguyên khối, không chẻ ra được '
    'mảnh nào mang nghĩa tiếng Nga.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>фиа́лка</b> hoa violet, hoa tím (cùng gốc Latin, '
    'mượn theo đường khác)</div>'
)

# --------------------------------------------------------------------- белый
S["белый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бел-</span>'
    '<span class="hd-gloss">TRẮNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc Nga trơn, không chẻ thêm được. Bù lại бел- đẻ '
    'rất khoẻ: nó nằm trong tên đồ vải, trong tên độ trắng, và trong cả tên '
    'nước <b>Белару́сь</b> ("Rus trắng").</div>'
    '<div class="hd-why">Dạng ngắn: giống cái <b>бела́</b> đẩy trọng âm ra '
    'đuôi, giống trung và số nhiều dùng được cả hai chỗ '
    '(<b>бе́ло</b>/<b>бело́</b>), riêng giống đực <b>бел</b> đứng yên.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бельё</b> đồ vải, đồ lót · <b>белизна́</b> độ '
    'trắng · <b>беле́ть</b> hiện lên trắng</div>'
)

# -------------------------------------------------------------------- чёрный
S["чёрный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">чёрн-</span>'
    '<span class="hd-gloss">ĐEN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hễ trọng âm rời khỏi ё thì ё phải viết thành е — '
    'thấy ngay ở <b>черна́</b> và <b>черни́ла</b>. Nhớ một luật này là đọc '
    'được cả họ từ.</div>'
    '<div class="hd-why">Dạng ngắn giống đực chèn thêm một nguyên âm chạy: '
    '<b>чёрен</b>; ba dạng còn lại kéo trọng âm ra đuôi (<b>черна́</b>, '
    '<b>черно́</b>, <b>черны́</b>).</div>'
    '<div class="hd-warn">Hai cụm gặp hằng ngày: <b>чёрный хлеб</b> bánh mì '
    'đen (làm từ lúa mạch đen) · <b>Чёрное мо́ре</b> Biển Đen.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>черни́ла</b> mực viết (thứ "làm cho đen") · '
    '<b>черни́ка</b> quả việt quất đen</div>'
)

# ------------------------------------------------------------------- красный
S["красный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">крас-</span>'
    '<span class="hd-gloss">gốc nghĩa ĐẸP, sau mới thành ĐỎ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc крас- vốn nói về cái ĐẸP (<b>краси́вый</b>, '
    '<b>красота́</b>); nghĩa "đỏ" là lớp nghĩa sinh sau. Tên '
    '<b>Кра́сная пло́щадь</b> vẫn thường được giải nghĩa theo lớp cũ ấy: '
    '"Quảng trường Đẹp".</div>'
    '<div class="hd-why">Dạng ngắn: giống đực chèn nguyên âm chạy '
    '<b>кра́сен</b>, giống cái đẩy trọng âm ra đuôi <b>красна́</b>, còn '
    'trung và số nhiều dùng được cả hai chỗ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>краси́вый</b> đẹp · <b>кра́ска</b> sơn, thuốc '
    'màu · <b>краси́ть</b> sơn, nhuộm</div>'
)

# ------------------------------------------------------------------- зелёный
S["зелёный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">зел-</span>'
    '<span class="hd-gloss">XANH LỤC, gốc nói về cây cỏ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ён-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Xanh lá là màu của <b>зе́лень</b> — rau xanh, rau '
    'thơm. Chữ ё luôn mang trọng âm, nên khi trọng âm chạy đi chỗ khác thì ё '
    'phải viết thành е: <b>зелёный</b> → <b>зелена́</b>.</div>'
    '<div class="hd-why">Dạng ngắn chạy về hai đầu: <b>зе́лен</b>, '
    '<b>зе́лено</b> lùi trọng âm về đầu, còn <b>зелена́</b> đẩy ra '
    'đuôi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>зе́лень</b> rau xanh, rau thơm · '
    '<b>зелене́ть</b> xanh lên, đâm chồi</div>'
)

# -------------------------------------------------------------------- жёлтый
S["жёлтый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">жёлт-</span>'
    '<span class="hd-gloss">VÀNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dạng ngắn: <b>жёлт</b> đứng yên, giống cái '
    '<b>желта́</b> chắc chắn dồn trọng âm ra đuôi, trung và số nhiều dùng '
    'được cả hai chỗ (<b>жёлто</b>/<b>желто́</b>) — và hễ trọng âm đi khỏi ё '
    'thì ё viết thành е.</div>'
    '<div class="hd-warn">⚠️ Mức tin: đây là từ nguyên. <b>жёлтый</b> được '
    'coi là cùng gốc Ấn–Âu xa với yellow của tiếng Anh và với <b>зо́лото</b> '
    '(vàng kim loại) — dùng để nhớ, không phải luật suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>желто́к</b> lòng đỏ trứng (tiếng Nga gọi là "cái '
    'vàng") · <b>желте́ть</b> ngả vàng</div>'
)
