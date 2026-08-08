# -*- coding: utf-8 -*-
"""k68 — tu-moi: 12 từ user vừa thêm, KHÔNG cùng họ nhau.

Không có trục chung và cố ý không có khối hệ thống dùng chung: mỗi thẻ chỉ nói
đúng phần của chính từ đó. Hai từ живо́тное / насеко́мое tình cờ cùng là tính từ
được danh từ hoá — mỗi thẻ tự nói lấy một câu, không dựng bảng chung.
"""

# 🔴 KHÔNG dựng biến khối dùng chung (HE/LUAT/THE…) rồi cộng vào mọi thẻ.

S = {}
V = {}

# ------------------------------------------------------------------- две́рь
S["дверь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">двер-</span>'
    '<span class="hd-gloss">gốc CỬA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ь</span>'
    '<span class="hd-gloss">dấu mềm khép từ; ở từ này là danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc двер- cùng ổ Ấn–Âu với <i>door</i> tiếng Anh và '
    '<i>Tür</i> tiếng Đức, nên mặt chữ tự gợi nghĩa. ⚠️ Nhưng đừng suy ra luật '
    'giống từ đuôi <b>-ь</b>: <b>день</b>, <b>слова́рь</b> đuôi y hệt mà là giống '
    'đực — giống của mỗi từ đuôi -ь phải nhớ riêng.</div>'
    '<div class="hd-warn">⚠️ Số nhiều đổi trọng âm giữa chừng: cách 1 và cách 4 '
    'giữ nhấn đầu (<b>две́ри</b>), các cách còn lại nhấn đuôi — <b>двере́й</b>, '
    '<b>дверя́м</b>, <b>дверя́ми</b>, <b>дверя́х</b>. Riêng cách 5 có hai dạng '
    'đều dùng được: <b>дверя́ми</b> và <b>дверьми́</b>.</div>'
    '<div class="hd-warn">⚠️ Sau <b>в</b>/<b>на</b> chỉ VỊ TRÍ, từ này có dạng '
    'riêng nhấn đuôi: <b>в двери́</b> ở ngay khung cửa. Còn nói VỀ cái cửa thì '
    '<b>о две́ри</b>. Hai dạng đều đúng, không phải lỗi bảng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дверно́й</b> thuộc về cửa · <b>две́рца</b> cửa nhỏ '
    '(cửa tủ, cửa xe)</div>'
)

# ------------------------------------------------------------------ дива́н
S["диван"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: từ mượn nguyên khối, vào tiếng Nga từ '
    'Ba Tư <i>dīvān</i> qua tiếng Thổ. Cùng một nguồn với <i>divan</i> tiếng '
    'Anh và <i>divano</i> tiếng Ý.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ nguyên đi theo đường: sổ sách → phòng hội đồng → '
    'dãy ghế dài kê dọc tường phòng đó → cái ghế dài. Chia hoàn toàn theo mẫu '
    'chuẩn giống đực, trọng âm đứng yên ở <b>-а́н</b> suốt bảng.</div>'
    '<div class="hd-warn">⚠️ <b>дива́н</b> là ghế DÀI nhiều chỗ; ghế một chỗ có '
    'tay vịn là <b>кре́сло</b>, ghế thường không tay vịn là <b>стул</b>.</div>'
    '<div class="hd-warn">⚠️ Ngồi/nằm thì dùng <b>на</b> + cách 6: '
    '<b>на дива́не</b>. Nằm hẳn xuống thì <b>на дива́н</b> (cách 4).</div>'
)

# --------------------------------------------------------------------- еда́
S["еда"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ед-</span>'
    '<span class="hd-gloss">gốc ĂN (của <b>есть</b> ăn)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi ⇒ danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc ăn + đuôi danh từ = "cái để ăn". Cùng gốc ед- còn '
    'có <b>обе́д</b> (об- quanh + ед- ăn ⇒ bữa ăn chính giữa ngày). Trọng âm ở '
    'đuôi suốt bảng: <b>еды́</b>, <b>еде́</b>, <b>еду́</b>.</div>'
    '<div class="hd-warn">⚠️ Là danh từ KHỐI, chỉ có số ít — y như "thức ăn" '
    'tiếng Việt, không đếm được và không có dạng số nhiều.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>есть</b> ăn · <b>съесть</b> ăn hết · <b>обе́д</b> '
    'bữa trưa · <b>обе́дать</b> ăn trưa · <b>съедо́бный</b> ăn được</div>'
)

# -------------------------------------------------------------- живо́тное
S["животное"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">жив-</span>'
    '<span class="hd-gloss">gốc SỐNG (<b>жить</b>, <b>жизнь</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-от-</span>'
    '<span class="hd-gloss">cho <b>живо́т</b>, xưa nghĩa "sự sống", nay "bụng"</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ое</span>'
    '<span class="hd-gloss">đuôi TÍNH TỪ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: "cái có sự sống". Vốn là tính từ '
    '<b>живо́тный</b> đứng trước một danh từ; danh từ đó rụng đi, tính từ ở lại '
    'gánh luôn vai danh từ.</div>'
    '<div class="hd-warn">⚠️ Vì vốn là tính từ nên nó CHIA NHƯ TÍNH TỪ, không '
    'theo mẫu danh từ giống trung: <b>живо́тного</b>, <b>живо́тному</b>, '
    '<b>живо́тным</b>, о <b>живо́тном</b> — đọc cả bảng bằng mắt tính từ là '
    'đúng hết.</div>'
    '<div class="hd-warn">⚠️ Là vật sống, nên cách 4 số nhiều mượn hình cách 2: '
    '<b>ви́жу живо́тных</b>, không phải <i>живо́тные</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>жить</b> sống · <b>жизнь</b> cuộc sống · '
    '<b>живо́й</b> sống, sinh động · <b>живо́т</b> bụng</div>'
)

# --------------------------------------------------------------- игру́шка
S["игрушка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">игр-</span>'
    '<span class="hd-gloss">gốc CHƠI (<b>игра́</b>, <b>игра́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ушк-</span>'
    '<span class="hd-gloss">hậu tố làm ra vật nhỏ, thân mật (<b>избу́шка</b> '
    'căn nhà nhỏ)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi ⇒ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ <b>игра́</b> "trò chơi" thêm hậu tố đồ vật ⇒ '
    '<b>игру́шка</b> là CÁI ĐỒ để chơi, không phải bản thân trò chơi. Thêm hậu '
    'tố thì trọng âm rời khỏi đuôi, chuyển sang chính hậu tố: игра́ → '
    'игру́шка.</div>'
    '<div class="hd-warn">⚠️ Cách 2 số nhiều phải chèn một nguyên âm cho đỡ '
    'chồng phụ âm: <b>игру́шек</b>. Chèn <b>е</b> vì đứng sau ш; còn sau phụ âm '
    'cứng thì chèn о, như <b>перча́тка</b> → <b>перча́ток</b>.</div>'
    '<div class="hd-warn">⚠️ Cụm phải thuộc: <b>мя́гкая игру́шка</b> "đồ chơi '
    'mềm" = thú nhồi bông.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>игра́</b> trò chơi · <b>игра́ть</b> chơi · '
    '<b>игро́к</b> người chơi, đấu thủ</div>'
)

# -------------------------------------------------------------- интерне́т
S["интернет"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Trong tiếng Nga không chẻ được: mượn nguyên khối từ '
    'tiếng Anh <i>internet</i> (bên đó mới là <i>inter-</i> giữa + <i>net</i> '
    'mạng lưới).</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỉ cần nhớ chỗ nhấn: <b>интерне́т</b> nhấn âm tiết '
    'cuối, và đứng yên ở đó suốt bảng chia. Từ mượn đuôi <b>-ет</b> hầu như đều '
    'thế: <b>биле́т</b> vé, <b>паке́т</b> gói, <b>кабине́т</b> phòng làm '
    'việc.</div>'
    '<div class="hd-warn">⚠️ "Ở trên mạng" dùng <b>в</b> + cách 6: '
    '<b>в интерне́те</b> — không dùng на như tiếng Việt "trên mạng".</div>'
    '<div class="hd-warn">⚠️ Nay viết thường (<b>интерне́т</b>); lối viết hoa '
    'Интернет là kiểu cũ, gặp trong sách báo trước đây.</div>'
)

# -------------------------------------------------------------- крокоди́л
S["крокодил"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: từ quốc tế, vào tiếng Nga qua tiếng '
    'Hy Lạp <i>krokódeilos</i> — cùng nguồn với <i>crocodile</i> tiếng Anh.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mặt chữ gần y hệt tiếng Anh, việc duy nhất phải học là '
    'chỗ nhấn: <b>крокоди́л</b> nhấn âm cuối, và mọi dạng đều giữ nguyên chỗ '
    'nhấn đó.</div>'
    '<div class="hd-warn">⚠️ Là con vật SỐNG, nên cách 4 mượn hình cách 2: '
    '<b>ви́жу крокоди́ла</b> (không phải <i>крокоди́л</i>), số nhiều '
    '<b>крокоди́лов</b>.</div>'
    '<div class="hd-warn">⚠️ Thành ngữ dùng chung với tiếng Việt: '
    '<b>крокоди́ловы слёзы</b> — nước mắt cá sấu.</div>'
)

# ----------------------------------------------------------------- ку́хня
S["кухня"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кух-</span>'
    '<span class="hd-gloss">gốc mượn, từ <i>coquere</i> "nấu" của La Tinh qua '
    'tiếng Đức <i>Küche</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ня</span>'
    '<span class="hd-gloss">trùng khuôn các danh từ chỉ NƠI CHỐN: '
    '<b>спа́льня</b> phòng ngủ, <b>пека́рня</b> lò bánh</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng một ổ với <i>kitchen</i>, <i>cuisine</i>, '
    '<i>cook</i> — nhớ một cái là nhớ cả chùm. Và cũng như <i>cuisine</i>, từ '
    'này mang luôn nghĩa "nền ẩm thực": <b>ру́сская ку́хня</b> món ăn Nga.</div>'
    '<div class="hd-warn">⚠️ Cả bảng chia đúng mẫu, chỉ lệch ĐÚNG MỘT Ô: cách 2 '
    'số nhiều chèn thêm о — <b>ку́хонь</b>. Chính chữ о đó cũng nằm trong tính '
    'từ <b>ку́хонный</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ку́хонный</b> thuộc về bếp — dùng cho dao bếp, bàn '
    'bếp, đồ bếp</div>'
)

# ----------------------------------------------------------------- лежа́ть
S["лежать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">леж-</span>'
    '<span class="hd-gloss">gốc NẰM (biến thể của лег-/лож-)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể, thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi -ать mà lại chia theo LỚP 2 (đuôi -и-): '
    '<b>лежу́</b>, <b>лежи́шь</b>… đúng như <b>слы́шать</b>, <b>держа́ть</b>. '
    'Ngôi "họ" viết <b>лежа́т</b> chứ không phải -ят, vì sau ж người Nga viết а '
    'chứ không viết я.</div>'
    '<div class="hd-warn">⚠️ Là TRẠNG THÁI đang nằm, không phải hành động nằm '
    'xuống: nằm xuống là <b>лечь</b> / <b>ложи́ться</b>. Đồ vật cũng "nằm": '
    '<b>Кни́га лежи́т на столе́</b> = quyển sách để trên bàn.</div>'
    '<div class="hd-warn">⚠️ Trả lời Где? nên đi cách 6: '
    '<b>лежа́ть на дива́не</b>. Còn <b>лечь</b> trả lời Куда? nên đi cách 4: '
    '<b>лечь на дива́н</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лечь</b> nằm xuống · <b>ложи́ться</b> nằm xuống '
    '(chưa hoàn thành) · <b>положи́ть</b> đặt nằm xuống · <b>полежа́ть</b> nằm '
    'một lát</div>'
)

# ------------------------------------------------------------- насеко́мое
S["насекомое"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">tiền tố LÊN, VÀO</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сек-</span>'
    '<span class="hd-gloss">gốc CHÉM, KHÍA (<b>сечь</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ом-ое</span>'
    '<span class="hd-gloss">đuôi tính từ giống trung, nghĩa bị động</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dịch từng mảnh từ <i>insectum</i> La Tinh (in- vào + '
    'sect- cắt): con vật có thân trông như bị KHÍA thành từng đốt. '
    '<i>Insect</i> tiếng Anh cũng chính hình ảnh đó, chỉ khác tiếng.</div>'
    '<div class="hd-warn">⚠️ Vốn là tính từ nên chia theo đuôi TÍNH TỪ: '
    '<b>насеко́мого</b>, <b>насеко́мому</b>, <b>насеко́мым</b>, о '
    '<b>насеко́мом</b> — kể cả cách 4 số nhiều lấy hình cách 2 '
    '(<b>насеко́мых</b>) vì côn trùng là vật sống.</div>'
    '<div class="hd-warn">⚠️ Đây là tên gọi CHUNG của cả lớp côn trùng; trong '
    'lời nói thường ngày người Nga hay gọi thẳng từng con: <b>жук</b>, '
    '<b>му́ха</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сечь</b> chém, chặt · <b>насе́чка</b> đường khía, '
    'vết khắc</div>'
)

# ------------------------------------------------------------- перча́тка
S["перчатка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">перч-</span>'
    '<span class="hd-gloss">từ <b>перст</b> "ngón tay" (từ cổ)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-атк-а</span>'
    '<span class="hd-gloss">đuôi làm ra vật, giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ nguyên: dạng cổ là перстчатка "cái (bọc) ngón tay", '
    'cụm стч nói nhanh mòn thành ч. Nhớ được <b>перст</b> là nhớ luôn '
    '<b>напёрсток</b> — cái đê khâu đội lên ngón tay.</div>'
    '<div class="hd-warn">⚠️ Cách 2 số nhiều chèn о: <b>перча́ток</b>. Chỗ hay '
    'gặp nhất là đếm đôi — <b>па́ра перча́ток</b> một đôi găng.</div>'
    '<div class="hd-warn">⚠️ <b>перча́тка</b> là găng CHIA NGÓN. Loại bao liền '
    'chỉ hở ngón cái là <b>ва́режка</b> / <b>рукави́ца</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>перст</b> ngón tay (cổ) · <b>напёрсток</b> cái đê '
    'khâu · <b>пе́рстень</b> chiếc nhẫn (có mặt)</div>'
)

# -------------------------------------------------------------- пече́нье
S["печенье"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">печ-</span>'
    '<span class="hd-gloss">gốc NƯỚNG / LÒ (<b>печь</b> vừa là "nướng" vừa là '
    '"cái lò")</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ень-е</span>'
    '<span class="hd-gloss">đuôi ⇒ danh từ giống trung, chỉ cái được làm ra</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen "đồ được nướng" ⇒ bánh quy. Đuôi -ье cho biết '
    'đây là danh từ giống trung; trọng âm rơi vào âm tiết giữa và đứng yên ở đó '
    'suốt bảng chia.</div>'
    '<div class="hd-warn">⚠️ Đừng lẫn với <b>пе́чень</b> (lá gan, giống cái, '
    'nhấn đầu). Cùng mặt chữ печ- mà khác hẳn nghĩa lẫn chỗ nhấn.</div>'
    '<div class="hd-warn">⚠️ Là danh từ KHỐI như "bánh quy" tiếng Việt: thường '
    'không đếm cái. Bảng vẫn in số nhiều <b>пече́нья</b>, cách 2 là '
    '<b>пече́ний</b> (đuôi -ье → -ий), nhưng thực tế hiếm dùng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>печь</b> nướng; cái lò · <b>пе́чка</b> bếp lò · '
    '<b>вы́печка</b> đồ nướng, bánh trái · <b>печёный</b> đã nướng</div>'
)

# ================================================== field Vietnamese (đề bài)
# Chỉ sửa ba dòng: một dòng SAI nghĩa, một dòng có ngoặc chú (cấm theo §2c),
# một dòng gán cho từ này cái nghĩa của từ khác.
# Chín từ còn lại đã đúng khuôn "thuần danh sách nghĩa" ⇒ để nguyên.

# cũ: "ghế sofa, ghế bành" — "ghế bành" là кре́сло (ghế một chỗ có tay vịn),
# không phải дива́н.
V["диван"] = "ghế sofa, đi văng, ghế dài"

# cũ: "bếp (phòng bếp hoặc phong cách ẩm thực)" — có ngoặc chú giải, §2c cấm.
V["кухня"] = "nhà bếp, phòng bếp, ẩm thực, cách nấu ăn"

# cũ: "nằm, đặt nằm, để ở vị trí nằm" — "đặt nằm" là ngoại động từ (класть /
# положи́ть). лежа́ть là NỘI động từ chỉ trạng thái.
# Cũng KHÔNG lấy "nằm ở / toạ lạc": nghĩa "be situated" đó đã là của находи́ться
# ("nằm ở, tọa lạc, được đặt ở") — quét lại toàn bộ sưu tập thấy trùng ngay.
V["лежать"] = "nằm"
