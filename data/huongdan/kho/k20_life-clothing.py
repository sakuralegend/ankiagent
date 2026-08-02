# -*- coding: utf-8 -*-
"""k20 — life::clothing: đồ mặc trên người + phụ kiện + vải.

Trục thật của lô (rút ra sau khi đọc `tiep`, không đoán theo tên topic):
17 danh từ cụ thể, chia làm ba nhóm rất khác nhau về cách học —
  (a) TỪ MƯỢN đứng một mình (шу́ба, ю́бка, ша́пка, ке́пка, га́лстук, костю́м,
      карма́н, пальто́, шарф, сапо́г, ке́ды): CẤM chẻ giả, nói thẳng là mượn;
  (b) từ Nga chẻ được thật (оде́жда, пла́тье, кольцо́, ткань, руба́шка, су́мка):
      đây mới là chỗ đáng bỏ công chẻ;
  (c) hai chỗ BẤT THƯỜNG đắt nhất lô: пальто́ KHÔNG biến cách, và ке́ды hầu như
      chỉ dùng số nhiều.
Xuyên suốt lô là luật đệm nguyên âm ở cách 2 số nhiều của nhóm -ка
(ю́бок · су́мок · ша́пок · ке́пок · руба́шек) — mỗi thẻ nói bằng chính từ của nó,
KHÔNG dựng khối dùng chung.
"""

S = {}
V = {}

# ---------------------------------------------------------------- áo khoác
S["шуба"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">шуб-</span>'
    '<span class="hd-gloss">thân mượn, mang trọn nghĩa "áo lông"</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thân <b>шуб-</b> là từ mượn nên không chẻ nhỏ thêm được, '
    'nhưng tiếng Nga đã đẻ từ mới trên nó. Nghĩa hẹp: áo khoác bằng <i>da lông thú</i>, '
    'cấp ấm cao nhất — <b>пальто́</b> chỉ là áo dạ dài.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>шу́бка</b> áo lông ngắn, áo lông trẻ em · '
    '<b>полушу́бок</b> áo lông nửa thân (dài đến hông)</div>'
)
V["шуба"] = "áo lông thú (áo khoác bằng da lông, mặc mùa đông)"

S["пальто"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn thẳng tiếng Pháp <i>paletot</i>, '
    'không mảnh nào mang nghĩa riêng trong tiếng Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Áo khoác dài bằng dạ hoặc vải — không phải lông thú '
    '(lông thú là <b>шу́ба</b>).</div>'
    '<div class="hd-warn">⚠️ KHÔNG BIẾN CÁCH: <b>в пальто́</b>, <b>без пальто́</b>, '
    '<b>два пальто́</b> — mọi cách và cả số nhiều đều đúng một mặt chữ. '
    'Đây là cả một lớp từ mượn tận cùng -о/-е/-и: <b>метро́</b>, <b>кино́</b>, '
    '<b>ко́фе</b>, <b>такси́</b>. Giống trung.</div>'
)
V["пальто"] = "áo măng tô, áo khoác dài bằng dạ"

# ---------------------------------------------------------------- quần áo nói chung
S["одежда"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">bao quanh</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дежд-</span>'
    '<span class="hd-gloss">gốc "đặt, khoác lên"</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: "cái khoác bao quanh người". Cùng gốc với '
    '<b>наде́ть</b>, <b>оде́ть</b> và <b>одея́ло</b> (chăn — cái phủ lên).</div>'
    '<div class="hd-warn">⚠️ Hai động từ này rất hay lẫn: <b>наде́ть</b> đi với '
    'ĐỒ VẬT (<i>наде́ть шу́бу</i> — mặc áo lông vào), còn <b>оде́ть</b> đi với '
    'NGƯỜI (<i>оде́ть ребёнка</i> — mặc quần áo cho đứa bé). Cả hai đều cách 4.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оде́ться</b> mặc đồ vào · <b>разде́ться</b> cởi đồ ra · '
    '<b>одея́ло</b> chăn</div>'
)
V["одежда"] = "quần áo, trang phục (nói chung, không đếm từng cái)"

# ---------------------------------------------------------------- nhóm -ка
S["юбка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">юб-</span>'
    '<span class="hd-gloss">thân mượn, không có nghĩa riêng trong tiếng Nga</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỉ che từ eo xuống và mặc rời — còn <b>пла́тье</b> là mảnh '
    'liền cả thân. Cách 2 số nhiều phải đệm thêm <b>о</b>: bỏ đuôi -а thì còn hai phụ '
    'âm б-к đứng sát nhau, nên thành <b>ю́бок</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ю́бочка</b> váy nhỏ, váy trẻ em</div>'
)
V["юбка"] = "chân váy (chỉ phần dưới, mặc rời)"

S["сумка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сум-</span>'
    '<span class="hd-gloss">gốc "cái bị, cái đãy"</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">hậu tố nhỏ hơn + giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vốn là dạng nhỏ của <b>сума́</b> "cái bị" (nay hiếm gặp). '
    'Đây là túi RỜI mang theo tay hay vai — túi may liền trên quần áo là <b>карма́н</b>. '
    'Cách 2 số nhiều đệm <b>о</b>: <b>су́мок</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сума́</b> bị, đãy (từ cổ) · <b>су́мочка</b> túi xách nhỏ</div>'
)
V["сумка"] = "túi xách, cặp (vật đựng rời, mang theo người)"

S["шапка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">шап-</span>'
    '<span class="hd-gloss">gốc mượn, từ Latin <i>cappa</i> "mũ trùm"</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng nguồn với <i>cap</i> tiếng Anh. Là mũ mềm trùm kín đầu, '
    'đội lúc rét, KHÔNG có lưỡi trai (loại có lưỡi trai là <b>ке́пка</b>). '
    'Nghĩa bóng hay gặp: dòng tiêu đề trên đầu trang báo — "cái mũ" của trang giấy. '
    'Cách 2 số nhiều đệm <b>о</b>: <b>ша́пок</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ша́почка</b> mũ nhỏ, mũ vải mỏng</div>'
)
V["шапка"] = "mũ len, mũ ấm trùm đầu (không có lưỡi trai)"

S["кепка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кеп-</span>'
    '<span class="hd-gloss">từ <b>ке́пи</b>, mũ lính kiểu Pháp</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">đuôi Nga hoá, giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiếng Nga mượn <b>ке́пи</b> rồi gắn đuôi -ка quen thuộc, '
    'thành mũ vải CÓ lưỡi trai. Đối lập thẳng với <b>ша́пка</b> (mũ ấm trùm kín, '
    'không lưỡi trai). Cách 2 số nhiều đệm <b>о</b>: <b>ке́пок</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ке́пи</b> mũ lính lưỡi trai (từ mượn, không biến cách)</div>'
)
V["кепка"] = "mũ lưỡi trai, nón kết"

S["рубашка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">руб-</span>'
    '<span class="hd-gloss">gốc cổ «рубъ» — tấm vải thô, mép vải</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ашк-а</span>'
    '<span class="hd-gloss">hậu tố + đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc là "đồ may bằng tấm vải thô"; dạng dân dã '
    '<b>руба́ха</b> nay vẫn dùng cho áo cánh kiểu nông thôn. Cách 2 số nhiều vẫn là '
    'luật đệm nguyên âm, nhưng sau <b>ш</b> thì viết <b>е</b> chứ không viết о: '
    '<b>руба́шек</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>руба́ха</b> áo cánh dân dã</div>'
)
V["рубашка"] = "áo sơ mi (có cổ, cài khuy)"

# ---------------------------------------------------------------- đi chân
S["сапог"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không mảnh nào mang nghĩa riêng: mượn rất sớm, nhiều '
    'khả năng từ ngôn ngữ Turk.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ủng, giày ống cao cổ. Đi theo đôi nên hay gặp ở số nhiều '
    '<b>сапоги́</b>. Ngoài dạng nguyên, trọng âm chuyển hết ra đuôi (<b>сапога́</b>, '
    '<b>сапоги́</b>) — rồi cách 2 số nhiều lại trở về đúng mặt chữ nguyên: '
    '<b>па́ра сапо́г</b> "một đôi ủng".</div>'
    '<div class="hd-warn">⚠️ Thành ngữ hay gặp: <b>два сапога́ па́ра</b> — "cùng một '
    'giuộc", nói hai người giống nhau, thường ý chê.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сапо́жник</b> thợ đóng, sửa giày · <b>сапожо́к</b> ủng nhỏ</div>'
)
V["сапог"] = "ủng, giày ống cao cổ (một chiếc)"

S["кеды"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: từ tên nhãn giày Mỹ <i>Keds</i>, được Nga hoá '
    'thành danh từ thường — cùng kiểu với <b>ксе́рокс</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giày vải đế bằng, đi theo đôi nên hầu như luôn đứng ở số nhiều: '
    '<b>но́вые ке́ды</b>. Số ít <b>кед</b> chỉ dùng khi nói về MỘT chiếc. '
    'Cách 2 số nhiều có hai dạng đều đúng: <b>ке́дов</b> và <b>кед</b> '
    '(<b>па́ра кед</b>). Phân biệt với <b>кроссо́вки</b>: đó mới là giày thể thao có '
    'đế đệm, còn <b>ке́ды</b> chỉ là giày vải đế phẳng.</div>'
)
V["кеды"] = "giày vải đế bằng, giày ba ta (từ chỉ dùng ở số nhiều)"

# ---------------------------------------------------------------- bộ đồ, phụ kiện
S["платье"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">плат-</span>'
    '<span class="hd-gloss">tấm vải</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ье</span>'
    '<span class="hd-gloss">hậu tố gom thành khối → giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc "tấm vải" ấy còn cho ra <b>плато́к</b>. Vì -ье là đuôi '
    'gom khối nên nghĩa cổ của <b>пла́тье</b> là "quần áo nói chung"; ngày nay thu hẹp '
    'lại thành váy liền cả thân của nữ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>плато́к</b> khăn vuông (trùm đầu, khăn tay)</div>'
)
V["платье"] = "váy liền thân, đầm (áo và váy liền một mảnh)"

S["костюм"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được trong tiếng Nga: mượn thẳng tiếng Pháp '
    '<i>costume</i>; gốc xa hơn là Latin <i>consuetudo</i> "thói quen, lệ" — cùng nguồn '
    'với <i>custom</i> và <i>costume</i> tiếng Anh.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa lõi không phải "vest" mà là BỘ ĐỒ ĐỒNG BỘ, nhiều món cùng '
    'một dạng: <b>спорти́вный костю́м</b> bộ đồ thể thao, <b>купа́льный костю́м</b> '
    'đồ bơi, <b>маскара́дный костю́м</b> đồ hoá trang.</div>'
)
V["костюм"] = "bộ đồ đồng bộ (bộ vest nam, bộ đồ thể thao)"

S["галстук"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">Hals-</span>'
    '<span class="hd-gloss">tiếng Đức: cổ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-tuch</span>'
    '<span class="hd-gloss">tiếng Đức: khăn</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mượn nguyên cụm Đức <i>Halstuch</i> "khăn cổ". Chẻ được là chẻ '
    'trong tiếng Đức thôi — sang tiếng Nga hai mảnh đó KHÔNG còn nghĩa riêng, cả từ chia '
    'như một danh từ giống đực bình thường. Nơ con bướm gọi là '
    '<b>га́лстук-ба́бочка</b>, đúng nghĩa đen "cà vạt con bướm".</div>'
)

S["шарф"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: từ mượn châu Âu, vào Nga qua tiếng Đức.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhìn thẳng ra <i>scarf</i> tiếng Anh, gần như cùng mặt chữ. '
    'Là dải DÀI quấn quanh cổ; khăn vuông trùm đầu thì gọi là <b>плато́к</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ша́рфик</b> khăn quàng nhỏ</div>'
)
V["шарф"] = "khăn quàng cổ (dải dài quấn quanh cổ)"

S["карман"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn: mượn từ ngôn ngữ Turk, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Túi MAY LIỀN trên quần áo — khác <b>су́мка</b> là túi rời mang '
    'theo. Tiếng Nga dựng hẳn một nhánh từ trên nó, đều xoay quanh nghĩa "cỡ bỏ túi" và '
    '"tiền trong túi".</div>'
    '<div class="hd-warn">⚠️ Cụm phải thuộc: <b>не по карма́ну</b> — "quá đắt so với túi '
    'tiền", không kham nổi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>карма́нный</b> cỡ bỏ túi · <b>карма́нник</b> kẻ móc túi</div>'
)
V["карман"] = "túi áo, túi quần (may liền trên quần áo)"

S["кольцо"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">коль-</span>'
    '<span class="hd-gloss">từ cổ «ко́ло» — vòng tròn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-цо</span>'
    '<span class="hd-gloss">hậu tố nhỏ hơn → giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc đúng là "vòng nhỏ". Số nhiều dồn trọng âm về đầu '
    '(<b>ко́льца</b>), riêng cách 2 số nhiều thành <b>коле́ц</b> — dấu mềm ь rơi mất, '
    'chèn <b>е</b> vào thay chỗ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>колесо́</b> bánh xe · <b>о́коло</b> quanh, gần · '
    '<b>кольцева́я</b> (tuyến, đường) vành đai</div>'
)
V["кольцо"] = "nhẫn; cái vòng, khoen (hình tròn khép kín)"

S["ткань"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">тк-</span>'
    '<span class="hd-gloss">gốc động từ <b>ткать</b> — dệt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-нь</span>'
    '<span class="hd-gloss">hậu tố dựng danh từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: "cái được dệt ra". Danh từ tận cùng -ь không đoán '
    'được giống, phải nhớ kèm: <b>ткань</b> là giống CÁI. Nghĩa thứ hai hay gặp trong '
    'sách vở: mô sinh học (mô cơ, mô thần kinh).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ткать</b> dệt · <b>ткач</b> thợ dệt · <b>тка́цкий</b> thuộc '
    'nghề dệt</div>'
)
V["ткань"] = "vải, tấm vải dệt"
