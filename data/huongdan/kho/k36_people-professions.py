# -*- coding: utf-8 -*-
"""k36 — people::professions: tên NGHỀ dựng bằng bốn khuôn hậu tố khác nhau
(`-и́ст` mượn quốc tế · `-е́ц`, `-а́рь`, `-тель` thuần Nga), cộng vài từ mượn
nguyên khối của môi trường làm việc.
"""

# 🔴 KHÔNG dựng biến khối dùng chung (HE/LUAT/THE…) rồi cộng vào mọi thẻ.
# Đó là cách cũ, đã bỏ 28/07 — xem README §3.

S = {}
V = {}

# --------------------------------------------------------------- офис
S["офис"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn nguyên khối tiếng Anh '
    '<i>office</i>, trong tiếng Nga nó không có mảnh nào mang nghĩa riêng.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vỏ chữ giữ gần nguyên bản gốc, và trọng âm đứng yên ở '
    '<b>о́</b> qua mọi cách — đuôi chỉ mọc thêm phía sau.</div>'
    '<div class="hd-warn">⚠️ <b>о́фис</b> là CHỖ làm việc: căn phòng, toà nhà. '
    'Nghĩa “chức vụ, chức trách” mà <i>office</i> tiếng Anh cũng mang thì tiếng '
    'Nga dùng từ khác — đừng suy sang.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>о́фисный</b> thuộc về văn phòng</div>'
)

# --------------------------------------------------------------- студент
S["студент"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">студ-</span>'
    '<span class="hd-gloss">gốc Latin <i>studere</i>: dùi mài, chăm chú</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́нт</span>'
    '<span class="hd-gloss">đuôi chỉ NGƯỜI, mượn quốc tế</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng một chữ với <i>student</i>, <i>study</i>, chỉ đổi vỏ. '
    'Trọng âm nằm ở đuôi <b>-е́нт</b> và đứng yên đó qua mọi cách.</div>'
    '<div class="hd-warn">⚠️ <b>студе́нт</b> chỉ dùng cho người học ĐẠI HỌC. '
    'Học sinh trường phổ thông là <b>учени́к</b> — từ điển ghi rõ chỗ này.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>студе́нтка</b> nữ sinh viên · '
    '<b>студе́нческий</b> thuộc về sinh viên</div>'
)

# --------------------------------------------------------------- программист
S["программист"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">програ́мм-</span>'
    '<span class="hd-gloss">chương trình</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ст</span>'
    '<span class="hd-gloss">NGƯỜI làm nghề đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi <b>-и́ст</b> là khuôn nghề nghiệp mượn quốc tế, '
    'đúng <i>-ist</i> tiếng Anh, và nó luôn kéo trọng âm về mình: '
    '<b>программи́ст</b>, <b>экономи́ст</b>, <b>юри́ст</b> — ba từ cùng lô này.</div>'
    '<div class="hd-why">Nên trọng âm dịch chỗ khi ghép: '
    '<b>програ́мма</b> → <b>программи́ст</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>програ́мма</b> chương trình · '
    '<b>программи́ровать</b> lập trình</div>'
)

# --------------------------------------------------------------- экономист
S["экономист"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">эконо́м-</span>'
    '<span class="hd-gloss">kinh tế (Hy Lạp <i>oikos</i> nhà + <i>nomos</i> phép tắc)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ст</span>'
    '<span class="hd-gloss">NGƯỜI làm nghề đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc Hy Lạp nghĩa đen là “phép trông nom việc nhà cửa”, '
    'từ đó ra <b>эконо́мика</b>. Thêm <b>-и́ст</b> thì trọng âm rời gốc mà '
    'chạy xuống đuôi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>эконо́мика</b> nền kinh tế; kinh tế học · '
    '<b>экономи́ческий</b> thuộc về kinh tế · <b>эконо́мный</b> tiết kiệm</div>'
)

# --------------------------------------------------------------- юрист
S["юрист"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">юр-</span>'
    '<span class="hd-gloss">LUẬT (Latin <i>jus, juris</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ст</span>'
    '<span class="hd-gloss">NGƯỜI làm nghề đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thấy mảnh <b>юр-</b> là nghĩ tới luật: cùng gốc Latin '
    'với <i>jurist</i>, <i>jury</i>, <i>jurisdiction</i>.</div>'
    '<div class="hd-warn">⚠️ <b>юри́ст</b> là người có nghề luật nói chung — '
    'thẩm phán, công chứng viên, cố vấn pháp lý đều là <b>юри́ст</b>. Người ra '
    'toà bào chữa cho thân chủ gọi riêng là <b>адвока́т</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>юриди́ческий</b> thuộc về pháp lý, luật pháp</div>'
)

# --------------------------------------------------------------- фотограф
S["фотограф"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">фото-</span>'
    '<span class="hd-gloss">ÁNH SÁNG (Hy Lạp <i>phos, photos</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-граф</span>'
    '<span class="hd-gloss">người GHI LẠI, người vẽ (<i>graphein</i> viết)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen “người vẽ bằng ánh sáng”, y hệt '
    '<i>photograph</i>. Từ ngắn <b>фо́то</b> giữ trọng âm ở đầu, từ dài thì '
    'trọng âm dời sang mảnh sau: <b>фото́граф</b>.</div>'
    '<div class="hd-warn">⚠️ Bảng chia bên dưới có ba ô SAI do lỗi nguồn từ điển. '
    'Đúng phải là: cách 3 số ít <b>фото́графу</b>, cách 3 số nhiều '
    '<b>фото́графам</b>, cách 5 số nhiều <b>фото́графами</b>. Từ này chia hoàn '
    'toàn theo mẫu thường, không có gì đặc biệt.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>фо́то</b> bức ảnh · <b>фотогра́фия</b> tấm ảnh; nghề '
    'nhiếp ảnh · <b>фотографи́ровать</b> chụp ảnh</div>'
)

# --------------------------------------------------------------- продавец
S["продавец"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">chuyển hẳn sang tay người khác</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дав-</span>'
    '<span class="hd-gloss">TRAO, đưa cho (gốc <b>дава́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ц</span>'
    '<span class="hd-gloss">NGƯỜI làm việc đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen “người trao hàng đi”: <b>продава́ть</b> bán, '
    'cộng đuôi người <b>-е́ц</b> thuần Nga.</div>'
    '<div class="hd-warn">⚠️ Chữ <b>е</b> trong <b>-е́ц</b> RỤNG mất ngay khi '
    'thêm đuôi cách: <b>продаве́ц</b> nhưng <b>продавца́</b>, <b>продавцу́</b>, '
    '<b>продавцо́м</b>. Nhớ mỗi chỗ này là đọc trôi cả bảng chia.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>продава́ть</b> bán · <b>прода́жа</b> việc bán, đợt bán '
    '· <b>продавщи́ца</b> nữ bán hàng · <b>дать</b> cho, đưa</div>'
)

# --------------------------------------------------------------- певец
S["певец"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пев-</span>'
    '<span class="hd-gloss">thân của <b>петь</b> HÁT</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ц</span>'
    '<span class="hd-gloss">NGƯỜI làm việc đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúc cùng một khuôn với <b>продаве́ц</b> ở lô này: '
    'thân động từ + <b>-е́ц</b> = người làm việc ấy.</div>'
    '<div class="hd-warn">⚠️ Cũng rụng nguyên âm y như <b>продаве́ц</b>: '
    '<b>певе́ц</b> nhưng <b>певца́</b>, <b>певцу́</b>, <b>певцо́м</b> — chữ '
    '<b>е</b> của đuôi biến mất ở mọi cách còn lại.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>петь</b> hát · <b>пе́сня</b> bài hát · '
    '<b>певи́ца</b> nữ ca sĩ</div>'
)

# --------------------------------------------------------------- князь
S["князь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: một từ gốc, có mặt từ thời Slav cổ, '
    'không mảnh nào tách ra còn nghĩa riêng.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Được cho là mượn rất sớm từ tiếng German cổ '
    '<i>kuning</i> — cùng ngọn nguồn với <i>king</i> và <i>König</i>. Nghe '
    '<b>князь</b> thì nghĩ “người cầm đầu một vùng đất”, tước quý tộc thời xưa, '
    'không phải một nghề.</div>'
    '<div class="hd-warn">⚠️ Số nhiều nhảy hẳn khuôn: <b>князья́</b>, '
    '<b>князья́м</b>, <b>князья́ми</b> — đuôi <b>-ья́</b> mang trọng âm, trong '
    'khi số ít vẫn giữ trọng âm ở gốc (<b>кня́зя</b>, <b>кня́зю</b>). Bảng còn '
    'in thêm <b>кня́зи</b>: đó là lối cổ, đừng dùng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>княги́ня</b> vợ công tước, nữ công tước · '
    '<b>кня́жество</b> công quốc — chú ý <b>з</b> đổi thành <b>ж</b></div>'
)

# --------------------------------------------------------------- модель
S["модель"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn qua tiếng Pháp <i>modèle</i>, '
    'gốc Latin <i>modulus</i> “cái thước đo nhỏ”.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một chữ ôm ba việc — kiểu/dòng của một sản phẩm, mô '
    'hình thu nhỏ, và người mẫu. Nghĩa nào cũng quay về “cái mẫu để người khác '
    'theo”.</div>'
    '<div class="hd-warn">⚠️ Đuôi <b>-ь</b> KHÔNG cho biết giống. '
    '<b>моде́ль</b> là giống CÁI, còn <b>учи́тель</b>, <b>секрета́рь</b>, '
    '<b>князь</b> ngay trong lô này đều giống ĐỰC — giống của danh từ đuôi '
    '<b>-ь</b> phải nhớ theo từng từ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>модели́ровать</b> dựng mô hình, mô phỏng</div>'
)

# --------------------------------------------------------------- преподаватель
S["преподаватель"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пре-по-</span>'
    '<span class="hd-gloss">truyền qua, chuyển sang</span></div>'
    '<div class="hd-row"><span class="hd-piece">-да-</span>'
    '<span class="hd-gloss">CHO, trao (gốc <b>дать</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва-</span>'
    '<span class="hd-gloss">làm đi làm lại, đều đặn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тель</span>'
    '<span class="hd-gloss">NGƯỜI làm nghề đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen “người trao kiến thức sang cho người khác” → '
    '<b>преподава́ть</b> giảng dạy. Đuôi <b>-тель</b> là khuôn NGƯỜI thuần Nga, '
    'khác khuôn mượn <b>-и́ст</b> của <b>программи́ст</b> cùng lô.</div>'
    '<div class="hd-warn">⚠️ <b>преподава́тель</b> dạy ở ĐẠI HỌC, cao đẳng, hoặc '
    'dạy một môn cho người lớn. Dạy ở trường phổ thông thì gọi là '
    '<b>учи́тель</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>преподава́ть</b> giảng dạy · <b>дава́ть</b> cho, đưa</div>'
)

# --------------------------------------------------------------- учитель
S["учитель"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">учи́-</span>'
    '<span class="hd-gloss">DẠY; học thuộc (gốc <b>учи́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тель</span>'
    '<span class="hd-gloss">NGƯỜI làm nghề đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>учи́ть</b> ôm cả hai chiều “dạy” và “học thuộc”; '
    'thêm <b>-тель</b> là lấy ra người đứng ở chiều dạy.</div>'
    '<div class="hd-warn">⚠️ Số nhiều không lấy đuôi <b>-и</b> thường gặp mà là '
    '<b>учителя́</b>, và trọng âm nhảy hẳn xuống đuôi: <b>учителя́м</b>, '
    '<b>учителя́ми</b>. Số ít thì đứng yên ở <b>учи́-</b>.</div>'
    '<div class="hd-warn">⚠️ <b>учи́тель</b> dạy ở trường phổ thông; dạy bậc đại '
    'học thì gọi là <b>преподава́тель</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>учи́ть</b> dạy; học thuộc · <b>учи́ться</b> đi học · '
    '<b>учени́к</b> học sinh phổ thông · <b>учи́тельница</b> cô giáo</div>'
)

# --------------------------------------------------------------- секретарь
S["секретарь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">секрет-</span>'
    '<span class="hd-gloss">BÍ MẬT (Latin <i>secretus</i>: được tách riêng ra)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́рь</span>'
    '<span class="hd-gloss">NGƯỜI làm nghề đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen “người được tin cậy giữ chuyện kín” — đúng '
    'gốc của <i>secretary</i>. Đuôi <b>-а́рь</b> cũng là một khuôn chỉ người làm '
    'nghề, và nó kéo trọng âm về mình.</div>'
    '<div class="hd-warn">⚠️ Trọng âm dịch ngay trong SỐ ÍT chứ không đợi tới số '
    'nhiều: <b>секрета́рь</b> nhưng <b>секретаря́</b>, <b>секретарю́</b>, '
    '<b>секретарём</b> — mọi cách khác đều dồn xuống đuôi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>секре́т</b> bí mật · <b>секре́тный</b> mật, thuộc bí mật</div>'
)

# --------------------------------------------------------------- компания
S["компания"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ком-</span>'
    '<span class="hd-gloss">CÙNG nhau (Latin <i>com-</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пан-</span>'
    '<span class="hd-gloss">BÁNH MÌ (Latin <i>panis</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ия</span>'
    '<span class="hd-gloss">đuôi danh từ, giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen Latin là “những người bẻ chung một ổ bánh”, '
    'nên một chữ ôm cả hai nghĩa: hội bạn đi cùng nhau, và công ty — hội người '
    'cùng làm ăn.</div>'
    '<div class="hd-warn">⚠️ <b>компа́ния</b> (công ty, hội bạn) chỉ khác '
    '<b>кампа́ния</b> (chiến dịch, đợt vận động) đúng MỘT chữ. Mảnh <b>ком-</b> '
    '“cùng nhau” là chỗ bám để khỏi lẫn.</div>'
    '<div class="hd-why">Bảng dưới in hai dạng cách 5, <b>компа́нией</b> và '
    '<b>компа́ниею</b>: dạng sau là lối cổ trong văn thơ, chỉ dùng dạng đầu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>компаньо́н</b> người cùng hội, cộng sự</div>'
)

# --------------------------------------------------------------- профессия
S["профессия"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">ra phía trước, công khai</span></div>'
    '<div class="hd-row"><span class="hd-piece">-фесс-</span>'
    '<span class="hd-gloss">NÓI ra, tuyên bố (Latin <i>professus</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ия</span>'
    '<span class="hd-gloss">đuôi danh từ, giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen “điều mình khai ra trước mọi người” — cái '
    'nghề mình nhận là của mình, y như <i>profession</i>.</div>'
    '<div class="hd-warn">⚠️ Đừng lẫn <b>профе́ссия</b> nghề nghiệp với '
    '<b>профе́ссор</b> giáo sư: chung năm chữ đầu, chỉ khác cái đuôi.</div>'
    '<div class="hd-why">Bảng dưới in hai dạng cách 5, <b>профе́ссией</b> và '
    '<b>профе́ссиею</b>: dạng sau là lối cổ trong văn thơ, chỉ dùng dạng đầu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>профессиона́л</b> người làm nghề chuyên nghiệp · '
    '<b>профессиона́льный</b> thuộc về nghề, chuyên nghiệp</div>'
)


# ============================================================== FIELD TIẾNG VIỆT
# Đề bài của deck `1-go` — user GÕ từ Nga từ dòng này, nên mỗi đề chỉ được có
# ĐÚNG MỘT đáp án. Không ghi từ loại / giống / thể (mặt đề bài đã in badge).

# 'giáo viên' trước đây là đề bài của CẢ HAI từ dưới, cùng `n` + MASC ♂ nên
# badge không tách được -> tách bằng BẬC HỌC, mỗi bên giữ một từ riêng.
V["преподаватель"] = "giảng viên (dạy đại học, cao đẳng)"
# Bỏ "cô giáo": đó là đáp án của `учительница`, và mâu thuẫn với badge MASC ♂.
V["учитель"] = "thầy giáo (dạy trường phổ thông)"

# "(nam)" lặp đúng badge MASC ♂ mà user đang nhìn -> bỏ; `певица` có FEM ♀.
V["певец"] = "ca sĩ"

# Từ điển ghi rõ: студент là bậc ĐẠI HỌC, học sinh phổ thông là ученик.
V["студент"] = "sinh viên (bậc đại học)"

# "quý ông" là dịch nới rộng, sai hẳn: князь là TƯỚC quý tộc, không phải lối
# xưng hô lịch sự.
V["князь"] = "vương công, công tước (tước quý tộc Nga thời xưa)"

# Bỏ chữ "mẫu" đứng trơ (đụng `образец` mẫu, vật mẫu, hình mẫu).
V["модель"] = "người mẫu; kiểu, dòng (của xe, máy, sản phẩm)"

# Nghĩa "công ty" đứng trơ đụng `фирма` (công ty, hãng, thương hiệu) — cả hai
# đều `n` + FEM ♀ nên badge không tách. Đưa nghĩa RIÊNG của компания lên trước.
V["компания"] = "hội bạn đi cùng nhau (cũng dùng cho: công ty, doanh nghiệp)"
