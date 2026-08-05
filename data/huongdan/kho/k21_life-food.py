# -*- coding: utf-8 -*-
"""k21 — life::food: đồ ăn thức uống + tính từ tả vị và tả nguyên liệu.

Trục thật rút ra từ `tiep` (không đoán theo tên topic): 15 danh từ đồ ăn/thức
uống — phần lớn là DANH TỪ KHỐI (không đếm được, nhiều từ chỉ có số ít), kéo
theo luật cách 2 phần lượng ча́ю · хле́ба · со́ку — cộng 6 tính từ chia làm hai
nhóm: tả VỊ (сла́дкий · ки́слый · вку́сный, dạng ngắn đều bất thường) và tả
NGUYÊN LIỆU (мясно́й · кури́ный · ва́ренный, tính từ quan hệ).
"""

S = {}

# ---------------------------------------------------------------- danh từ

S["вода"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вод-</span>'
    '<span class="hd-gloss">NƯỚC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>вод-</b> chính là gốc Ấn–Âu đã cho water và '
    'wet trong tiếng Anh — không phải mẹo bắc cầu, mà cùng một gốc thật.</div>'
    '<div class="hd-warn">Trọng âm nhảy ngay trong số ít: bình thường ở đuôi '
    '(<b>вода́</b>, <b>воды́</b>, <b>воде́</b>), nhưng cách 4 số ít <b>во́ду</b> '
    'và cả số nhiều <b>во́ды</b> thì nhảy về đầu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>во́дка</b> vốn nghĩa là "nước nhỏ" (hậu tố -ка) · '
    '<b>водопрово́д</b> đường ống nước · <b>наводне́ние</b> lũ lụt</div>'
)

S["рюмка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рюм-</span>'
    '<span class="hd-gloss">thân mượn, không mang nghĩa riêng trong tiếng Nga'
    '</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">hậu tố đồ vật nhỏ, giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hậu tố -ка cho biết đây là vật nhỏ: <b>рю́мка</b> là ly '
    'nhỏ có chân, đủ một ngụm rượu mạnh — khác hẳn <b>стака́н</b> (cốc to).</div>'
    '<div class="hd-warn">Cách 2 số nhiều chen thêm một о cho dễ đọc: '
    '<b>рю́мка</b> → <b>рю́мок</b>. Đây là nguyên âm chạy: danh từ đuôi -ка có '
    'cụm phụ âm đứng trước đuôi đều phải chen о hoặc е vào đó.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рю́мочка</b> ly bé xíu · <b>рю́мочная</b> quán rượu '
    'bình dân (chỗ bán rượu theo рю́мка)</div>'
)

S["свёкла"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">свёкл-</span>'
    '<span class="hd-gloss">thân mượn thẳng từ tiếng Hy Lạp cổ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỉ cái đuôi -а là của tiếng Nga; thân từ không chẻ nhỏ '
    'hơn được. Trọng âm đứng yên ở ё suốt cả bảng chia.</div>'
    '<div class="hd-warn">Chuẩn là <b>свёкла</b> (trọng âm đầu từ). Rất nhiều '
    'người Nga nói свекла́ — đó là sai chuẩn. Thấy chữ ё là biết trọng âm ở đâu, '
    'vì ё luôn mang trọng âm.</div>'
    '<div class="hd-warn">Hệ quả: khi trọng âm rời đi thì ё buộc phải viết thành '
    'е — <b>свёкла</b> nhưng <b>свеко́льный</b>. Luật này lặp ở <b>мёд</b> trong '
    'cùng lô.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>свеко́льный</b> thuộc củ dền · <b>свеко́льник</b> '
    'món súp củ dền ăn lạnh</div>'
)

S["сметана"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">gom lại, vét lại</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мет-</span>'
    '<span class="hd-gloss">QUÉT, HỚT</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ана</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen là "cái được hớt lên": lớp béo nổi trên mặt '
    'sữa bị vét lấy. Cùng gốc мет- với <b>мести́</b> (quét nhà).</div>'
    '<div class="hd-warn">⚠️ Mức tin: chỗ chẻ này là từ nguyên, không phải luật '
    'suy ra được. Người Nga ngày nay không còn cảm thấy мет- trong từ này nữa.'
    '</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>смета́нный</b> làm bằng kem chua · <b>мести́</b> '
    'quét · <b>подмета́ть</b> quét dọn</div>'
)

S["икра"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không chẻ được: <b>икра́</b> là gốc Slav cổ đứng một '
    'mình. Đây là danh từ khối, nên bảng chia bên dưới chỉ có số ít — tiếng Nga '
    'không đếm nó thành từng cái.</div>'
    '<div class="hd-warn"><b>икра́</b> không chỉ là trứng cá: nó là tên chung cho '
    'mọi món NGHIỀN NHUYỄN — <b>кабачко́вая икра́</b> (bí ngồi nghiền), '
    '<b>баклажа́нная икра́</b> (cà tím nghiền) là món ăn hằng ngày.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>икри́нка</b> một hạt trứng cá — hậu tố -инка nghĩa '
    'là "một hạt tách ra từ khối", như <b>снежи́нка</b> một bông tuyết</div>'
)

S["колбаса"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không chẻ được: thân колбас- vào tiếng Nga đã nguyên '
    'khối và nguồn gốc còn đang tranh cãi. Chỉ đuôi -а́ là của tiếng Nga, báo '
    'giống cái.</div>'
    '<div class="hd-warn">Trọng âm dịch khi sang số nhiều: số ít dồn ra đuôi '
    '(<b>колбаса́</b>, <b>колбасу́</b>), số nhiều lùi vào giữa — '
    '<b>колба́сы</b>, <b>колба́с</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>колба́ска</b> xúc xích nhỏ (thường để nướng) · '
    '<b>колба́сный</b> thuộc về xúc xích — cả hai đều giữ trọng âm ở giữa như số '
    'nhiều</div>'
)

S["мята"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мят-</span>'
    '<span class="hd-gloss">thân mượn từ tiếng Latinh</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng một nguồn Latinh đã cho mint và menthol trong '
    'tiếng Anh: nhìn <b>мя́та</b> nghĩ ngay tới mint, không cần mẹo gì thêm.</div>'
    '<div class="hd-warn"><b>мя́та</b> (bạc hà) KHÔNG cùng gốc với <b>мять</b> / '
    '<b>мя́тый</b> (vò nhàu), cũng không liên quan <b>мя́со</b> (thịt) — chỉ '
    'trùng mặt chữ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мя́тный</b> vị bạc hà (<b>мя́тный чай</b> trà bạc hà)'
    '</div>'
)

S["груша"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">груш-</span>'
    '<span class="hd-gloss">gốc Slav cổ, không chẻ nhỏ hơn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ dễ chia: trọng âm đứng yên ở гру́- trong mọi cách và '
    'cả số nhiều, không có gì phải nhớ thêm.</div>'
    '<div class="hd-warn"><b>гру́ша</b> còn là bao cát hình quả lê ở phòng tập '
    '(<b>боксёрская гру́ша</b>) — nghĩa "vật hình quả lê" đi khá xa khỏi quả '
    'trái cây.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гру́шевый</b> vị lê, bằng lê (<b>гру́шевый сок</b>) — '
    'trọng âm ở гру́-, không phải грушёвый</div>'
)

S["хлеб"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không chẻ được. Nhiều nhà từ nguyên cho rằng <b>хлеб</b> '
    'là từ mượn rất cổ từ tiếng German, cùng nguồn với loaf — hãy coi đó là mẹo '
    'nhớ, không phải luật.</div>'
    '<div class="hd-warn">Hai số nhiều, hai nghĩa khác nhau: <b>хле́бы</b> là '
    'những ổ bánh đếm được, còn <b>хлеба́</b> là lúa mì ngoài đồng. Bảng chia bên '
    'dưới chỉ in dạng thứ nhất.</div>'
    '<div class="hd-warn">Muốn nói "một ít bánh mì" thì dùng cách 2 phần lượng: '
    '<b>купи́ть хле́ба</b>. Nói <b>купи́ть хлеб</b> (cách 4) là mua trọn cả ổ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>хле́бный</b> thuộc bánh mì · <b>хле́бница</b> giỏ '
    'đựng bánh — hậu tố -ница luôn là đồ đựng, như <b>са́харница</b> lọ đường'
    '</div>'
)

S["обед"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">quanh, khắp</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ед-</span>'
    '<span class="hd-gloss">ĂN (gốc của есть, еда́)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc -ед- là "ăn", và nó cùng gốc Ấn–Âu với eat trong '
    'tiếng Anh. Nhận ra -ед- ở đâu là biết chỗ đó nói chuyện ăn uống.</div>'
    '<div class="hd-warn">Dịch là "bữa trưa" nhưng với người Nga <b>обе́д</b> là '
    'bữa CHÍNH trong ngày (súp rồi mới tới món chính), ăn khoảng 13–15 giờ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обе́дать</b> ăn trưa · <b>еда́</b> thức ăn · '
    '<b>есть</b> ăn · <b>объеда́ться</b> ăn quá no</div>'
)

S["мёд"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không chẻ được, nhưng đây là một trong những từ cổ nhất '
    'châu Âu: cùng gốc Ấn–Âu với mead (rượu mật ong) tiếng Anh và madhu tiếng '
    'Phạn.</div>'
    '<div class="hd-warn">Chữ ё chỉ tồn tại khi mang trọng âm. Sang số nhiều '
    'trọng âm chạy ra đuôi nên ё phải viết thành е: <b>мёд</b> → <b>меды́</b>, '
    '<b>медо́в</b>. Giống <b>свёкла</b> → <b>свеко́льный</b> trong cùng lô.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>медо́вый</b> bằng mật ong (<b>медо́вый ме́сяц</b> '
    'tuần trăng mật) · <b>медве́дь</b> gấu — vốn là "kẻ ăn mật", мёд ghép với '
    'gốc -ед- (ăn) y như trong <b>обе́д</b></div>'
)

S["пюре"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không chẻ được: mượn nguyên xi từ tiếng Pháp purée '
    '("đã nghiền"). Đuôi -е khiến nó là giống trung, như mọi từ mượn kết thúc '
    'bằng nguyên âm.</div>'
    '<div class="hd-warn">KHÔNG biến cách — mọi cách đều viết y hệt '
    '<b>пюре́</b> (с <b>пюре́</b>, в <b>пюре́</b>), và trọng âm luôn nằm ở cuối. '
    'Bảng chia bên dưới trông "lỗi" chính là vì thế.</div>'
    '<div class="hd-warn">Đứng một mình, <b>пюре́</b> thường được hiểu là '
    '<b>карто́фельное пюре́</b> (khoai tây nghiền), nhưng còn có '
    '<b>я́блочное пюре́</b> (táo nghiền).</div>'
    # Không có mục Họ hàng: đây là từ mượn đứng một mình, tiếng Nga không đẻ ra
    # từ phái sinh nào từ nó. Bỏ hẳn là lựa chọn có ý thức (README §2).
)

S["чай"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không chẻ được. Mượn từ tiếng Trung theo đường bộ Trung '
    'Á; tiếng Anh mượn cùng chữ Hán ấy nhưng qua phương ngữ ven biển nên thành '
    'tea — một cây, hai con đường.</div>'
    '<div class="hd-why">Số nhiều dồn trọng âm ra đuôi: <b>чаи́</b>, '
    '<b>чаёв</b> — dạng này nghĩa là "các loại trà".</div>'
    '<div class="hd-warn">Cách 2 có HAI dạng: <b>ча́я</b> bình thường, và '
    '<b>ча́ю</b> là dạng PHẦN LƯỢNG, dùng khi nói "một ít" — <b>вы́пить ча́ю</b> '
    '(uống chút trà). Cùng luật với <b>хле́ба</b>, <b>со́ку</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ча́йник</b> ấm đun nước (tiếng lóng: kẻ gà mờ) · '
    '<b>ча́йный</b> thuộc trà (<b>ча́йная ло́жка</b> thìa nhỏ)</div>'
)

S["завтрак"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">vào lúc, nhằm vào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-втр-</span>'
    '<span class="hd-gloss">BUỔI SÁNG (biến thể của утр-, như у́тро)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ак</span>'
    '<span class="hd-gloss">đuôi danh từ giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vốn là cụm за у́тра — "vào lúc sáng"; у trong утр- biến '
    'thành в. Cũng chính cụm ấy cho ra <b>за́втра</b>: buổi sáng kế tiếp, tức '
    'ngày mai.</div>'
    '<div class="hd-warn">Chúng chỉ khác nhau đúng chữ к cuối: <b>за́втрак</b> '
    'bữa sáng · <b>за́втра</b> ngày mai. Đây là chỗ gõ nhầm nhiều nhất.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>за́втракать</b> ăn sáng · <b>поза́втракать</b> ăn '
    'sáng xong · <b>у́тро</b> buổi sáng · <b>за́втра</b> ngày mai</div>'
)

S["сок"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không chẻ được. Gốc Slav cổ, nghĩa rộng là "chất lỏng '
    'chảy ra từ cây" — nên nó vừa là nước ép trái cây vừa là nhựa cây '
    '(<b>берёзовый сок</b>).</div>'
    '<div class="hd-warn">Cách 2 có hai dạng: <b>стака́н со́ка</b> (một cốc nước '
    'ép) nhưng khi nói "một ít" thì dùng dạng phần lượng <b>со́ку</b> — cùng luật '
    'với <b>ча́ю</b>, <b>хле́ба</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>со́чный</b> mọng nước · <b>сочи́ться</b> rỉ ra, ứa ra '
    '· <b>соковыжима́лка</b> máy ép (сок + <b>выжима́ть</b> vắt)</div>'
)

# ---------------------------------------------------------------- tính từ

S["сладкий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">слад-</span>'
    '<span class="hd-gloss">NGỌT</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-</span>'
    '<span class="hd-gloss">hậu tố tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc слад- là bản Slav Nhà thờ của со́лод- (mạch nha) — '
    'đúng cặp như го́род/град. Trạng từ tương ứng là <b>сла́дко</b>.</div>'
    '<div class="hd-warn">So sánh hơn KHÔNG dùng đuôi -ее như tính từ thường: '
    'ngọt hơn là <b>сла́ще</b> — hậu tố -к- rụng mất, còn д biến thành щ.</div>'
    '<div class="hd-warn">Dạng ngắn không suy thẳng ra được: giống đực chen thêm '
    'о (<b>сла́док</b>), giống cái đẩy trọng âm ra đuôi (<b>сладка́</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сла́дость</b> vị ngọt · <b>сла́дости</b> đồ ngọt '
    '(luôn số nhiều) · <b>сла́дкое</b> món tráng miệng · <b>наслажде́ние</b> '
    'khoái cảm</div>'
)

S["мясной"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мяс-</span>'
    '<span class="hd-gloss">THỊT (từ мя́со)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-</span>'
    '<span class="hd-gloss">hậu tố "thuộc về"</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́й</span>'
    '<span class="hd-gloss">đuôi tính từ, mang trọng âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>мя́со</b> thêm -н- thành <b>мясно́й</b>, và trọng âm '
    'nhảy hẳn ra đuôi — nghe đuôi -о́й là biết trọng âm nằm ở đó.</div>'
    '<div class="hd-warn">Đây là tính từ QUAN HỆ: nó chỉ nói "làm từ thịt", chứ '
    'không tả mức độ. Vì thế bảng chia bên dưới bỏ trống cả dạng ngắn lẫn so '
    'sánh hơn — không thể "thịt hơn" được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мя́со</b> thịt · <b>мясни́к</b> người bán thịt · '
    '<b>мясору́бка</b> máy xay thịt (мя́со + <b>руби́ть</b> chặt)</div>'
)

S["кислый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кис-</span>'
    '<span class="hd-gloss">CHUA, LÊN MEN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-л-ый</span>'
    '<span class="hd-gloss">hậu tố dựng tính từ từ động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ <b>ки́снуть</b> (chua đi, thiu) mà ra: cái đã lên men '
    'thì chua. Cùng gốc với <b>квас</b> — nước uống làm bằng bánh mì lên men.</div>'
    '<div class="hd-warn">Dạng ngắn không suy thẳng ra được: giống đực chen thêm '
    'е (<b>ки́сел</b>), giống cái đẩy trọng âm ra đuôi (<b>кисла́</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кислота́</b> axit, vị chua · <b>ки́снуть</b> chua đi · '
    '<b>квас</b> nước kvas · <b>кислоро́д</b> ô-xy (ки́слый + gốc род "sinh ra")'
    '</div>'
)

S["куриный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кур-</span>'
    '<span class="hd-gloss">GÀ (từ ку́рица)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ин-ый</span>'
    '<span class="hd-gloss">hậu tố "của con vật này"</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hậu tố -ин- mở khoá cả một lớp: <b>пчела́</b> → '
    '<b>пчели́ный</b> (của ong), <b>ло́шадь</b> → <b>лошади́ный</b> (của ngựa). '
    'Trọng âm luôn nhảy vào chính hậu tố.</div>'
    '<div class="hd-warn"><b>кури́ный</b> (thuộc về gà) không hề cùng gốc với '
    '<b>кури́ть</b> (hút thuốc) — hai từ trông giống nhau đến mức dễ đọc nhầm.'
    '</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ку́рица</b> con gà mái · <b>ку́ры</b> đàn gà (số '
    'nhiều bất thường của <b>ку́рица</b>)</div>'
)

S["варенный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вар-</span>'
    '<span class="hd-gloss">ĐUN SÔI, NẤU</span></div>'
    '<div class="hd-row"><span class="hd-piece">-енн-ый</span>'
    '<span class="hd-gloss">hậu tố phân từ bị động: "được đun"</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc вар- là "đun sôi"; -енн- biến động từ thành phân từ '
    'bị động, tức là "cái đang được người ta đun".</div>'
    '<div class="hd-warn">Một chữ н hay hai là hai từ khác nhau: '
    '<b>ва́ренный</b> (hai н) là phân từ, luôn kéo theo bổ ngữ — '
    '<b>ва́ренный</b> в <b>молоке́</b>; còn <b>варёный</b> (một н) là tính từ '
    'thường — <b>варёное яйцо́</b>.</div>'
    '<div class="hd-warn">Dạng ngắn của phân từ luôn RỤNG bớt một н, nên bảng '
    'dạng ngắn bên dưới chỉ còn một н.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вари́ть</b> nấu, luộc · <b>варе́нье</b> mứt quả · '
    '<b>по́вар</b> đầu bếp · <b>самова́р</b> ấm samovar ("tự đun")</div>'
)

S["вкусный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">vào (trong miệng)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-кус-</span>'
    '<span class="hd-gloss">CẮN, NẾM</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">hậu tố tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: "thuộc về cái đưa vào miệng mà cắn". Nhận ra '
    'gốc кус- là đọc được cả <b>кусо́к</b> lẫn <b>заку́ска</b>.</div>'
    '<div class="hd-warn">Khen món ăn, người Nga nói dạng trung tính dùng như '
    'trạng từ: <b>Вку́сно!</b> — chứ không nói <b>вку́сный</b> trống không.</div>'
    '<div class="hd-warn">Dạng ngắn: giống đực chen thêm е (<b>вку́сен</b>), '
    'giống cái đẩy trọng âm ra đuôi (<b>вкусна́</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вкус</b> vị; gu thẩm mỹ · <b>вку́сно</b> ngon (trạng '
    'từ) · <b>заку́ска</b> món khai vị · <b>кусо́к</b> miếng</div>'
)


# ---------------------------------------------------------------------------
# V — sửa field `Vietnamese` (README §2c). Đây là ĐỀ BÀI của deck `1-go`:
# user nhìn dòng này rồi GÕ từ Nga, nên nó phải chỉ có một đáp án đúng.
# KHÔNG ghi từ loại / giống / thể — mặt đề bài đã in sẵn bốn badge.
# ---------------------------------------------------------------------------
V = {}

# "hạt bạc hà" là sai: мя́та là cả cây / lá, không phải hạt.
V["мята"] = "cây bạc hà, lá bạc hà"

# "khoai tây nghiền" quá hẹp — пюре́ là món nghiền nói chung.
V['пюре'] = 'món nghiền nhuyễn, khoai tây nghiền'

# "xúc xích" trống không đụng соси́ска (xúc xích nhỏ luộc).
V['колбаса'] = 'xúc xích, giò'

# "kem chua" đụng сли́вки (kem tươi) trong đầu người Việt.
V['сметана'] = 'kem chua, váng sữa chua'

# "đã luộc" một mình dẫn thẳng tới варёный (một н). Phải chỉ ra đây là dạng
# kéo theo bổ ngữ — thứ không badge nào chứa.
V['варенный'] = 'luộc, nấu chín'

# "đậm đà" không đúng nghĩa вку́сный; thêm nét "hợp vị" cho khỏi đụng хоро́ший.
V["вкусный"] = "ngon, ngon miệng"

# "ly nhỏ (để uống rượu mạnh)" còn đụng сто́пка/бока́л; nêu chi tiết có chân.
V["рюмка"] = "ly nhỏ có chân, uống rượu mạnh"
