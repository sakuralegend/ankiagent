# -*- coding: utf-8 -*-
"""k163 — people::professions: người theo nghề/việc, và vài danh từ đời sống (thương tích, rượu, sóng).

Chỗ cần nhất quán trong lô:
(1) -тель = người làm việc đó — води́тель (khớp руководи́тель k119), председа́тель.
(2) gốc сед-/сид- = NGỒI — председа́тель; khớp сосе́д (k71), сиде́ть (k85).
(3) gốc влад-/влас- = NẮM GIỮ — владе́лец; khớp власть (k115, có о́бласть).
(4) об-(в)яз- = BUỘC QUANH — обя́занность; khớp обя́занный (k156), обяза́тельно (k93).
(5) ра́на → ра́нить → ра́неный: hai thẻ cùng lô, ô đỏ phân biệt ра́на/тра́вма đặt ở ра́на.
(6) từ mượn Latin/Hy Lạp (майо́р, инспе́ктор, проду́кция, тра́вма, нарко́тик, регио́н): chẻ theo
    mảnh gốc trùng tiếng Anh, KHÔNG bịa mảnh tiếng Nga.
Họ hàng cố ý vắng: майо́р (mượn đứng một mình — мажо́р cùng gốc Latin nhưng nghĩa xa, chỉ gây rối).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "обязанность": "nghĩa vụ, bổn phận",      # bỏ «trách nhiệm» — chứa trọn отве́тственность (k159); gloss duty/obligation là nghĩa chính
    "регион": "vùng, miền, khu vực",          # thêm «miền» (region) — trước đó «vùng, khu vực» nằm gọn trong райо́н (đã nạp)
}

# ----------------------------------------------------------------- вор
S["вор"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: gốc trơn — chính nó là gốc cho cả họ «trộm».</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Số ít trọng âm nằm yên ở gốc (<b>во́ра</b>, <b>во́ру</b>); số nhiều từ cách 2 '
    'nhảy ra đuôi: <b>во́ры</b> → <b>воро́в</b>, <b>вора́м</b>. Động từ «ăn trộm» hay gặp nhất lại '
    'KHÁC gốc: <b>укра́сть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ворова́ть</b> ăn trộm · <b>воровство́</b> sự trộm cắp · '
    '<b>вори́шка</b> kẻ trộm vặt</div>'
)

# ----------------------------------------------------------------- майор
S["майор"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn qua tiếng Đức, gốc Latin <i>major</i> «lớn hơn» — cùng '
    'gốc tiếng Anh <i>major</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Người lớn hơn» ⇒ cấp trên một bậc: <b>лейтена́нт</b> → <b>капита́н</b> → '
    '<b>майо́р</b>. Trọng âm đứng yên ở <b>-о́р</b> mọi dạng.</div>'
    '<div class="hd-warn">Đừng nhầm với tiếng Anh <i>mayor</i> «thị trưởng» — thị trưởng là '
    '<b>мэр</b>.</div>'
)

# ----------------------------------------------------------------- инспектор
S["инспектор"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ин-</span>'
    '<span class="hd-gloss">VÀO TRONG (Latin <i>in-</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-спект-</span>'
    '<span class="hd-gloss">NHÌN (Latin <i>spect-</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ор</span>'
    '<span class="hd-gloss">người làm việc đó (<i>-or</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mảnh Latin, không phải mảnh Nga — ghép lại đúng tiếng Anh <i>inspector</i>: '
    '«người nhìn vào tận trong» ⇒ thanh tra. Cùng đuôi <b>-ор</b> với <b>дире́ктор</b>, '
    '<b>а́втор</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>инспе́кция</b> cuộc thanh tra, cơ quan thanh tra · '
    '<b>проспе́кт</b> đại lộ («tầm nhìn ra xa», cùng <i>spect-</i>)</div>'
)

# ----------------------------------------------------------------- владелец
S["владелец"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">владе́л-</span>'
    '<span class="hd-gloss">đã NẮM GIỮ, làm chủ (<b>владе́ть</b> → он <b>владе́л</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ец</span>'
    '<span class="hd-gloss">người (đuôi giống đực)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Người làm chủ» ⇒ chủ sở hữu. Nguyên âm <b>е</b> trong <b>-ец</b> rụng khi '
    'thêm đuôi, <b>ь</b> giữ cho л mềm: <b>владе́льца</b>, <b>владе́льцу</b>, '
    '<b>владе́льцем</b>.</div>'
    '<div class="hd-warn"><b>владе́ть</b> + cách 5: <b>владе́ть магази́ном</b> làm chủ cửa hàng — '
    'và <b>владе́ть языко́м</b> = thông thạo một ngôn ngữ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>владе́ть</b> làm chủ, sở hữu · <b>власть</b> quyền lực · '
    '<b>о́бласть</b> tỉnh, vùng</div>'
)

# ----------------------------------------------------------------- председатель
S["председатель"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пред-</span>'
    '<span class="hd-gloss">PHÍA TRƯỚC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сед-</span>'
    '<span class="hd-gloss">NGỒI (như <b>сосе́д</b>, <b>сиде́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-тель</span>'
    '<span class="hd-gloss">người làm việc đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Người ngồi ở ghế đầu» ⇒ chủ tịch, người chủ toạ. Tiếng Anh <i>preside</i>, '
    '<i>president</i> ghép đúng hai mảnh ấy từ Latin: <i>prae</i> «trước» + <i>sedere</i> «ngồi». '
    'Đi với cách 2: <b>председа́тель комите́та</b> chủ tịch uỷ ban.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>заседа́ние</b> cuộc họp («ngồi lại») · <b>сосе́д</b> hàng xóm · '
    '<b>сиде́ть</b> ngồi</div>'
)

# ----------------------------------------------------------------- водитель
S["водитель"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вод-</span>'
    '<span class="hd-gloss">DẪN, LÁI (<b>води́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-тель</span>'
    '<span class="hd-gloss">người làm việc đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Người lái» ⇒ tài xế. Cùng khuôn với <b>руководи́тель</b> «người dắt tay». '
    'Lái xe là <b>води́ть маши́ну</b>; bằng lái là <b>води́тельские права́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>води́ть</b> dẫn, lái · <b>руководи́тель</b> người lãnh đạo · '
    '<b>вести́</b> dẫn (một chiều)</div>'
)

# ----------------------------------------------------------------- прибыль
S["прибыль"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">THÊM VÀO, tới</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бы-</span>'
    '<span class="hd-gloss">CÓ, LÀ (<b>быть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ль</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cái có thêm vào» ⇒ lợi nhuận. Giống cái — đuôi <b>-ь</b> không tự báo giống: '
    '<b>больша́я при́быль</b>. Trái nghĩa cùng khuôn: <b>у́быль</b> (у- bớt đi) sự hao hụt.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>при́быльный</b> có lãi · <b>прибы́ть</b> đến nơi · <b>у́быль</b> sự hao hụt · '
    '<b>быть</b> là, có</div>'
)

# ----------------------------------------------------------------- обязанность
S["обязанность"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-(в)яз-</span>'
    '<span class="hd-gloss"><b>об-</b> quanh + <b>вяз-</b> BUỘC (<b>вяза́ть</b>), <b>в</b> rụng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ан-н-</span>'
    '<span class="hd-gloss">«bị …» (<b>обя́занный</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ость</span>'
    '<span class="hd-gloss">→ danh từ trừu tượng, giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Điều mình bị buộc vào» ⇒ nghĩa vụ, bổn phận — y như tiếng Anh <i>obligation</i> '
    '(Latin <i>ob-</i> + <i>ligare</i> «buộc»). Nói về công việc thường dùng số nhiều: '
    '<b>служе́бные обя́занности</b> nhiệm vụ công việc.</div>'
    '<div class="hd-warn"><b>обя́занность</b> = việc BUỘC PHẢI LÀM; <b>отве́тственность</b> = trách '
    'nhiệm phải GÁNH khi có chuyện (от-ве́т- «trả lời cho»).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обя́занный</b> có nghĩa vụ · <b>обяза́тельно</b> nhất định · '
    '<b>связь</b> mối liên hệ · <b>вяза́ть</b> buộc, đan</div>'
)

# ----------------------------------------------------------------- продукция
S["продукция"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-ду́к-</span>'
    '<span class="hd-gloss">«dẫn ra» — như <b>проду́кт</b> (Latin <i>pro-duct-</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ция</span>'
    '<span class="hd-gloss">= <i>-tion</i>, luôn giống cái (như <b>организа́ция</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mảnh Latin ghép đúng tiếng Anh <i>production</i>: toàn bộ hàng một nhà máy, '
    'một ngành làm ra. Danh từ gom cả khối nên gần như chỉ dùng số ít.</div>'
    '<div class="hd-warn"><b>проду́кция</b> = hàng sản xuất ra; <b>проду́кты</b> (số nhiều của '
    '<b>проду́кт</b>) = thực phẩm đi chợ mua.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>проду́кт</b> sản phẩm · <b>продукти́вный</b> năng suất</div>'
)

# ----------------------------------------------------------------- ванна
S["ванна"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn tiếng Đức <i>Wanne</i> «bồn, chậu».</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hai <b>н</b> của gốc giữ ở mọi dạng, kể cả cách 2 số nhiều cụt đuôi: '
    '<b>ванн</b>. Tắm bồn là <b>приня́ть ва́нну</b>.</div>'
    '<div class="hd-warn"><b>ва́нна</b> = cái bồn tắm; <b>ва́нная</b> = phòng tắm (tính từ dùng như '
    'danh từ, biến cách kiểu tính từ: <b>в ва́нной</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ва́нная</b> phòng tắm</div>'
)

# ----------------------------------------------------------------- мусор
S["мусор"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: gốc trơn.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ không đếm được, chỉ dùng số ít: <b>мно́го му́сора</b>. Số nhiều '
    '<b>мусора́</b> chỉ gặp trong tiếng lóng, nghĩa là «cớm» — đừng dùng.</div>'
    '<div class="hd-warn"><b>вы́нести му́сор</b> = đem rác đi đổ — câu việc nhà nghe hằng ngày.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>му́сорный</b> thuộc về rác (<b>му́сорное ведро́</b> thùng rác) · '
    '<b>мусоропрово́д</b> ống đổ rác</div>'
)

# ----------------------------------------------------------------- травма
S["травма"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn Hy Lạp <i>trauma</i> «vết thương» — đúng tiếng Anh '
    '<i>trauma</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dùng cho cả chấn thương cơ thể lẫn sang chấn tâm lý: <b>получи́ть тра́вму</b> '
    'bị chấn thương. Không họ với <b>трава́</b> cỏ — chỉ trùng mặt chữ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>травми́ровать</b> gây chấn thương · <b>травмато́лог</b> bác sĩ chấn thương · '
    '<b>травмпу́нкт</b> phòng cấp cứu chấn thương</div>'
)

# ----------------------------------------------------------------- рана
S["рана"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: gốc trơn — chính nó là gốc cho <b>ра́нить</b>, '
    '<b>ра́неный</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỗ da thịt bị rách, đâm: <b>ко́лотая ра́на</b> vết đâm. Nghĩa bóng: '
    '<b>зали́зывать ра́ны</b> «liếm vết thương» = gượng dậy sau thất bại.</div>'
    '<div class="hd-warn"><b>ра́на</b> = vết thương hở (dao, đạn); <b>тра́вма</b> = chấn thương nói chung '
    '(gãy, bong gân, va đập).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ра́нить</b> làm bị thương · <b>ра́неный</b> bị thương · '
    '<b>ране́ние</b> sự bị thương</div>'
)

# ----------------------------------------------------------------- раненый
S["раненый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ра́н-</span>'
    '<span class="hd-gloss">VẾT THƯƠNG (<b>ра́на</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ен-</span>'
    '<span class="hd-gloss">«bị …» (phân từ bị động của <b>ра́нить</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Bị làm cho có vết thương» ⇒ bị thương. Trọng âm đứng yên ở <b>ра́-</b>. '
    'Làm vị ngữ thì dùng dạng ngắn: <b>Он ра́нен</b> anh ấy bị thương.</div>'
    '<div class="hd-warn">Chính tả: đứng một mình viết MỘT <b>н</b> — <b>ра́неный солда́т</b>; có từ '
    'phụ đi kèm thì HAI <b>н</b> — <b>ра́ненный в но́гу</b> bị thương ở chân.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ра́на</b> vết thương · <b>ра́нить</b> làm bị thương · '
    '<b>ране́ние</b> sự bị thương</div>'
)

# ----------------------------------------------------------------- пьяный
S["пьяный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пь-</span>'
    '<span class="hd-gloss">UỐNG — gốc <b>пи-</b> của <b>пить</b>, mất и như <b>пью</b>, <b>пьёт</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ян-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đã uống (quá)» ⇒ say. Nói ai đang say thì dùng dạng ngắn, giống cái trọng âm '
    'nhảy ra đuôi: <b>он пьян</b> · <b>она́ пьяна́</b> · <b>они́ пья́ны</b> (cũng nói <b>пьяны́</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пить</b> uống · <b>пья́ница</b> kẻ nghiện rượu · <b>пья́нство</b> thói rượu '
    'chè · <b>напи́ться</b> uống say</div>'
)

# ----------------------------------------------------------------- наркотик
S["наркотик"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn Hy Lạp <i>narkē</i> «tê dại» — cùng gốc tiếng Anh '
    '<i>narcotic</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thứ làm tê dại» ⇒ ma tuý. Nói chung thường dùng số nhiều: '
    '<b>употребля́ть нарко́тики</b> dùng ma tuý.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>нарко́з</b> gây mê · <b>наркома́н</b> người nghiện ma tuý · '
    '<b>нарко́лог</b> bác sĩ cai nghiện</div>'
)

# ----------------------------------------------------------------- сериал
S["сериал"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сери-</span>'
    '<span class="hd-gloss">LOẠT, TẬP (<b>се́рия</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́л</span>'
    '<span class="hd-gloss">đuôi mượn, như tiếng Anh <i>serial</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một chuỗi nhiều tập ⇒ phim bộ; mỗi tập là một <b>се́рия</b>. Trọng âm dời từ '
    '<b>се́-</b> sang <b>-а́л</b>. Xem phim bộ: <b>смотре́ть сериа́л</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>се́рия</b> tập phim, loạt · <b>сери́йный</b> hàng loạt</div>'
)

# ----------------------------------------------------------------- волна
S["волна"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: gốc trơn <b>волн-</b> — chính nó sinh ra <b>волнова́ться</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Lòng «dậy sóng» ⇒ <b>волнова́ться</b> lo lắng. Số ít trọng âm ở đuôi '
    '(<b>волну́</b>), số nhiều lùi lên gốc: <b>во́лны</b>, <b>во́лнами</b>; cách 2 nhiều cụt đuôi: '
    '<b>волн</b>. Nghĩa bóng như tiếng Việt: <b>волна́ жары́</b> đợt nắng nóng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>волнова́ться</b> lo lắng · <b>волне́ние</b> sự xúc động · '
    '<b>взволно́ванный</b> xúc động</div>'
)

# ----------------------------------------------------------------- тень
S["тень"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: gốc trơn.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giống cái — đuôi <b>-ь</b> không tự báo giống. Vừa là cái bóng đổ, vừa là chỗ '
    'râm mát. Số nhiều từ cách 2 trọng âm ra đuôi: <b>тене́й</b>, <b>теня́м</b>.</div>'
    '<div class="hd-warn"><b>в тени́</b> «trong bóng râm» — sau в trọng âm nhảy ra đuôi; '
    '<b>о те́ни</b> «về cái bóng» thì không.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тени́стый</b> rợp bóng · <b>отте́нок</b> sắc thái, sắc độ</div>'
)

# ----------------------------------------------------------------- регион
S["регион"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn Latin <i>regio</i> — đúng tiếng Anh <i>region</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vùng lớn của một nước hay thế giới. Khác <b>райо́н</b>: quận, khu — đơn vị nhỏ '
    'trong thành phố, trong tỉnh.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>региона́льный</b> thuộc vùng, khu vực</div>'
)

B = {
    "docbangmat": 74,
    "loitubat": 1,      # тень: «sau в/на trọng âm nhảy ra đuôi» → chỉ «sau в» (на тени́ không phải cách nói thường) — đọc lại tự bắt
    "nguonsai": 1,      # тень: cột prep của bảng ghi тени́ — đó là dạng vị trí sau в; cách 6 thường là о те́ни, thẻ viết theo cách đúng
    "baolen": [
        "Máy bắt (không phải tôi tự bắt) 2 lỗi trọng âm trong mục Họ hàng, đã sửa: мусоропро́вод → мусоропрово́д, оттено́к → отте́нок. Họ hàng là phần không máy nào đối chiếu được ngoài trọng âm — luồng chính nên lướt thêm một lần.",
        "V cần duyệt: обязанность «nghĩa vụ, bổn phận» (bỏ «trách nhiệm» theo chia của luồng chính) · регион «vùng, miền, khu vực» (thêm «miền», giữ «vùng» và «khu vực» — hết nằm gọn trong райо́н).",
        "Không chắc vừa phải: прибыль = при- + бы- (быть) «cái có thêm vào» — theo Vasmer (прибы́ть nghĩa cổ «tăng thêm»), không phải luật suy ra được; viết như cách nhớ, không hạ mức tin. ва́нна mượn Đức Wanne, майо́р mượn qua Đức gốc Latin major — từ nguyên phổ biến.",
        "инспектор: Họ hàng có проспе́кт «đại lộ» (Latin prospectus, cùng spect- «nhìn») — từ nguyên đúng nhưng nghĩa xa; bỏ được nếu thấy gượng.",
        "майор cố ý không có Họ hàng (mượn đứng một mình). Ô đỏ duy nhất của thẻ là bẫy tiếng Anh mayor ↔ мэр.",
        "раненый: ô đỏ chính tả một н / hai н (ра́неный солда́т ↔ ра́ненный в но́гу) — luật sách giáo khoa Nga (Rosenthal), tin cao. Thẻ chỉ dạy nghĩa TÍNH TỪ, không nhắc nghĩa danh từ «người bị thương».",
    ],
}
