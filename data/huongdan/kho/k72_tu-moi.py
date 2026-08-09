# -*- coding: utf-8 -*-
"""k72 — tu-moi: 13 từ user vừa thêm, KHÔNG cùng một họ.

Không có trục chung, và cố ý không có khối hệ thống dùng chung: mỗi thẻ chỉ nói
đúng phần của chính từ đó. Ba chỗ giao nhau nằm trọn trong lô nên được xử lý cả
hai phía: баскетбо́л ↔ те́ннис (cùng nhóm tên môn thể thao mượn — mỗi thẻ tự nói
lấy một câu, không dựng bảng chung), вы́ставка ↔ выходны́е (cùng tiền tố вы-),
видеоигра́ ↔ игра́ (từ ghép trong suốt).
"""

# 🔴 KHÔNG dựng biến khối dùng chung (HE/LUAT/THE…) rồi cộng vào mọi thẻ.

S = {}
V = {}

# ------------------------------------------------------------- баскетбо́л
S["баскетбол"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">баскет-</span>'
    '<span class="hd-gloss">basket — cái rổ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бо́л</span>'
    '<span class="hd-gloss">ball — quả bóng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mượn nguyên khối từ tiếng Anh <i>basketball</i>: '
    'bóng ném vào rổ. Cùng khuôn với <b>футбо́л</b> (foot+ball), nên gặp đuôi '
    '<i>-бо́л</i> là biết đang gọi tên một môn bóng. Trọng âm đứng yên ở cuối, '
    'và vì là tên một môn nên từ này không có số nhiều.</div>'
    '<div class="hd-warn">⚠️ Đuôi <i>-бо́л</i> chỉ là <i>ball</i> mượn vào, KHÔNG '
    'dính gì tới mặt chữ <i>бол-</i> trong <b>боле́ть</b>, <b>больни́ца</b>, '
    '<b>большо́й</b> — trùng chữ thôi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>футбо́л</b> bóng đá · <b>спорт</b> thể thao · '
    '<b>спорти́вный</b> thuộc về thể thao · <b>мяч</b> quả bóng</div>'
)

# ------------------------------------------------------------- видеоигра́
S["видеоигра"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ви́део-</span>'
    '<span class="hd-gloss">hình ảnh (Latin <i>video</i> = tôi nhìn thấy)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-игра́</span>'
    '<span class="hd-gloss">trò chơi, y nguyên từ <b>игра́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ ghép trong suốt: dán <i>ви́део</i> vào trước <b>игра́</b>, '
    'nên nó giữ nguyên cả giống cái lẫn cách chia của <b>игра́</b>. Trọng âm cũng '
    'chạy y hệt: số ít dồn ra đuôi, số nhiều kéo ngược lên gốc — '
    '<b>игра́ → и́гры</b>, <b>видеоигра́ → видеои́гры</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>игра́</b> trò chơi · <b>игру́шка</b> đồ chơi · '
    '<b>игра́ть</b> chơi · <b>ви́деть</b> nhìn thấy (họ xa, cùng gốc Ấn–Âu)</div>'
)

# ------------------------------------------------------------------ война́
S["война"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вой-</span>'
    '<span class="hd-gloss">gốc ĐÁNH NHAU, binh đao</span></div>'
    '<div class="hd-row"><span class="hd-piece">-на́</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <i>вой-</i> cho cả chùm chuyện binh đao: <b>во́ин</b> '
    'chiến binh, <b>вое́нный</b> thuộc về quân sự. Nhớ kèm cặp đối lập kinh điển '
    'với <b>мир</b>: «Война́ и мир». Số ít dồn trọng âm ra đuôi <b>война́</b>, số '
    'nhiều kéo ngược về gốc <b>во́йны</b>.</div>'
    '<div class="hd-warn">⚠️ Đừng nhìn nhầm sang <b>войти́</b> đi vào — từ đó là '
    '<i>в- + идти́</i>, khác gốc hoàn toàn, chỉ trùng ba chữ đầu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>во́ин</b> chiến binh · <b>вое́нный</b> thuộc về quân sự · '
    '<b>мир</b> hoà bình, thế giới</div>'
)

# --------------------------------------------------------------- вы́ставка
S["выставка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span>'
    '<span class="hd-gloss">tiền tố: RA NGOÀI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-став-</span>'
    '<span class="hd-gloss">gốc ĐẶT, DỰNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: đặt RA ngoài cho người ta xem → cuộc trưng bày. '
    'Cùng tiền tố <i>вы-</i> với <b>вы́ход</b> (lối RA), và ở cả hai từ trọng âm rơi '
    'đúng lên tiền tố rồi đứng yên suốt bảng: <b>вы́</b>-.</div>'
    '<div class="hd-warn">⚠️ Cách 2 số nhiều chèn thêm một chữ <i>о</i> cho dễ đọc: '
    '<b>вы́ставок</b> (nguyên âm chạy, tránh đuôi <i>-вк</i>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поста́вить</b> đặt, để · <b>вста́вить</b> chèn vào · '
    '<b>вы́ход</b> lối ra</div>'
)

# -------------------------------------------------------------- выходны́е
S["выходные"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span>'
    '<span class="hd-gloss">RA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ход-</span>'
    '<span class="hd-gloss">gốc ĐI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-</span>'
    '<span class="hd-gloss">biến thành tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ы́е</span>'
    '<span class="hd-gloss">đuôi TÍNH TỪ số nhiều</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: những ngày ĐI RA khỏi công việc. Đây vốn là tính '
    'từ <b>выходно́й</b> đem dùng thẳng làm danh từ, nên nó chỉ có số nhiều và chia '
    'theo đuôi tính từ (<b>выходны́х</b>, <b>выходны́м</b>), không phải đuôi danh từ.</div>'
    '<div class="hd-warn">⚠️ Vào cuối tuần nói là <b>на выходны́х</b> (cách 6) — thuộc '
    'cả cụm, đừng ghép từng chữ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>выходно́й</b> ngày nghỉ · <b>вы́ход</b> lối ra · '
    '<b>вход</b> lối vào · <b>ходи́ть</b> đi · <b>перехо́д</b> lối qua đường</div>'
)

# ----------------------------------------------------------- конфере́нция
S["конференция"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кон-</span>'
    '<span class="hd-gloss">Latin <i>com-</i>: CÙNG NHAU</span></div>'
    '<div class="hd-row"><span class="hd-piece">-фер-</span>'
    '<span class="hd-gloss">Latin <i>ferre</i>: MANG, ĐEM</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́нция</span>'
    '<span class="hd-gloss">đuôi danh từ mượn</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen Latin: mang ý kiến lại cùng nhau — đúng là '
    '<i>conference</i> của tiếng Anh, bắc cầu thẳng được.</div>'
    '<div class="hd-warn">⚠️ Cả lớp từ đuôi <i>-ция</i> đều GIỐNG CÁI, và trọng âm '
    'luôn rơi vào âm tiết ngay TRƯỚC <i>-ция</i>: <b>ле́кция</b>, <b>ста́нция</b>, '
    '<b>констру́кция</b>, <b>конфере́нция</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ле́кция</b> bài giảng · <b>ста́нция</b> ga tàu, trạm · '
    '<b>констру́кция</b> kết cấu</div>'
)

# ----------------------------------------------------------------- ку́рица
S["курица"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кур-</span>'
    '<span class="hd-gloss">gốc GÀ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-иц(а)</span>'
    '<span class="hd-gloss">hậu tố chỉ GIỐNG CÁI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hậu tố <i>-иц(а)</i> đánh dấu giống cái, nên nghĩa đen là '
    'con gà mái; tiếng Nga dùng luôn từ này cho cả món thịt gà.</div>'
    '<div class="hd-warn">⚠️ Số nhiều rụng luôn <i>-иц-</i>, quay về gốc ngắn: '
    '<b>ку́ры</b>, cách 2 <b>кур</b>. Phải thuộc, không suy ra được.</div>'
    '<div class="hd-warn">⚠️ <b>кури́ть</b> hút thuốc giống mặt chữ đến mức nguy hiểm '
    'nhưng KHÁC GỐC hoàn toàn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кури́ный</b> thuộc về gà · cùng hậu tố: <b>певи́ца</b> '
    'nữ ca sĩ · <b>продавщи́ца</b> nữ bán hàng</div>'
)

# ------------------------------------------------------------------ ле́том
S["летом"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ле́т-</span>'
    '<span class="hd-gloss">mùa hè (từ <b>ле́то</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ом</span>'
    '<span class="hd-gloss">đuôi CÁCH 5 giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không phải từ riêng: đây là <b>ле́то</b> ở cách 5, mà cách 5 '
    'trần đã tự mang sẵn nghĩa «vào…». Trọng âm giữ nguyên chỗ cũ của <b>ле́то</b>, '
    'khác <b>зима́ → зимо́й</b> phải kéo ra đuôi.</div>'
    '<div class="hd-warn">⚠️ KHÔNG thêm giới từ: nói <b>ле́том</b>, không nói в ле́то. '
    'Đuôi cách 5 đã làm xong việc của giới từ rồi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ле́то</b> mùa hè · <b>ле́тний</b> thuộc về mùa hè · '
    '<b>зимо́й</b> vào mùa đông · <b>у́тром</b> vào buổi sáng · <b>ве́чером</b> vào buổi tối</div>'
)

# ----------------------------------------------------------------- носи́ть
S["носить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">нос-/нош-</span>'
    '<span class="hd-gloss">gốc MANG, VÁC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỉ một gốc mang: mang trên tay thì thành vác, mang trên '
    'người thì thành mặc và đeo. Đây là động từ chuyển động ĐA HƯỚNG — mang đi mang '
    'lại, mang thường xuyên; bạn cùng cặp một hướng là <b>нести́</b> đang mang đi một '
    'lượt.</div>'
    '<div class="hd-warn">⚠️ Ngôi tôi vừa biến âm <i>с → ш</i> vừa kéo trọng âm ra đuôi: '
    '<b>я ношу́</b>, nhưng <b>ты но́сишь</b>, <b>они́ но́сят</b>.</div>'
    '<div class="hd-warn">⚠️ Với quần áo, <b>носи́ть</b> là thường mặc, thói quen — '
    'không phải động tác mặc vào lúc này.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>нести́</b> mang đi một lượt · <b>но́ша</b> gánh, vật mang</div>'
)

# -------------------------------------------------------------- програ́мма
S["программа"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">Hy Lạp <i>pro-</i>: TRƯỚC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-грамм-</span>'
    '<span class="hd-gloss">Hy Lạp <i>gramma</i>: chữ viết</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: cái được VIẾT RA TRƯỚC — chương trình, lịch trình, '
    'rồi mở rộng sang phần mềm máy tính. Cùng chữ Hy Lạp <i>gramma</i> với '
    '<b>грамма́тика</b>, nên hai từ này nhớ kèm nhau được.</div>'
    '<div class="hd-warn">⚠️ Giữ đúng HAI chữ <i>м</i>: <b>програ́мма</b>. Người làm '
    'nghề là <b>программи́ст</b> — trọng âm nhảy hẳn xuống <i>-и́ст</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>программи́ст</b> lập trình viên · <b>грамма́тика</b> ngữ pháp · '
    '<b>килогра́мм</b> ki-lô-gam (cùng chữ, khác nhánh nghĩa)</div>'
)

# ------------------------------------------------------------------- ра́но
S["рано"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ра́н-</span>'
    '<span class="hd-gloss">gốc SỚM (như <b>ра́нний</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi biến tính từ thành trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dựng theo khuôn trạng từ quen thuộc: gốc <i>ра́н-</i> + đuôi '
    '<i>-о</i>. Đứng một mình không cần chủ ngữ thì nó thành cả một câu: «Ещё ра́но» = '
    'còn sớm mà.</div>'
    '<div class="hd-warn">⚠️ Đừng chép đuôi từ nọ sang từ kia: tính từ cùng gốc là '
    '<b>ра́нний</b> với HAI chữ <i>н</i>, còn trạng từ <b>ра́но</b> chỉ một.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ра́нний</b> sớm, ban đầu · <b>ра́ньше</b> trước đây, sớm hơn · '
    '<b>зара́нее</b> từ trước, sẵn từ sớm</div>'
)

# ----------------------------------------------------------------- ро́дина
S["родина"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">род-</span>'
    '<span class="hd-gloss">gốc SINH RA, DÒNG GIỐNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ин(а)</span>'
    '<span class="hd-gloss">hậu tố tạo danh từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: nơi mình được SINH RA. Gốc <i>род-</i> ở đây cũng '
    'chính là gốc của <b>роди́ться</b> và <b>наро́д</b> (<i>на- + род</i> = cả một dòng '
    'giống chung), nên nhớ một từ là mở được cả chùm. Trọng âm đứng yên ở <b>ро́</b>- '
    'suốt bảng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>род</b> dòng họ · <b>роди́тель</b> bố hoặc mẹ · '
    '<b>роди́ться</b> chào đời · <b>родно́й</b> ruột thịt · <b>наро́д</b> nhân dân</div>'
)

# ------------------------------------------------------------------ те́ннис
S["теннис"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn nguyên khối từ tiếng Anh <i>tennis</i>, '
    'giữ nguyên cả hai chữ <i>н</i>, chỉ thêm đuôi cách vào sau.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tên một môn nên không có số nhiều, và trọng âm đứng yên ở '
    '<b>те́</b>- suốt bảng. Cùng nhóm từ mượn với <b>футбо́л</b> và <b>баскетбо́л</b>, '
    'khác ở chỗ hai từ kia còn chẻ ra được <i>-бо́л</i> (ball), <b>те́ннис</b> thì không.</div>'
    '<div class="hd-warn">⚠️ Bóng bàn là <b>насто́льный те́ннис</b> — nghĩa đen quần vợt '
    'trên bàn, từ <b>стол</b> cái bàn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>футбо́л</b> bóng đá · <b>баскетбо́л</b> bóng rổ · '
    '<b>спорт</b> thể thao · <b>игра́ть</b> chơi · <b>мяч</b> quả bóng</div>'
)

# =====================================================================
# FIELD TIẾNG VIỆT (đề bài deck 1-go) — README §2c.
# Chỉ khai từ nào THẬT SỰ cần sửa; 9 từ còn lại của lô giữ nguyên.

# cũ: "con gà (động vật hoặc món ăn)" — ngoặc là ghi chú, §2c cấm tuyệt đối.
# Gloss Anh có đúng hai mục "hen" + "chicken" ⇒ trải thẳng thành danh sách:
# gà mái (nghĩa gốc, vì -иц(а) là hậu tố giống cái), con gà nói chung, và thịt
# gà — chính là phần "món ăn" mà cái ngoặc cũ đang định nói.
V["курица"] = "con gà mái, con gà, thịt gà"

# cũ: "mặc (quần áo), đeo (phụ kiện), mang/vác (đồ vật)" — BA ngoặc trong một
# dòng, nặng nhất lô. Bỏ hết thì còn đúng một danh sách trần khớp gloss Anh
# ("to wear" / "to carry by hand or on the body"). Đã quét cả 1119 thẻ: không
# thẻ nào khác mang một trong bốn nghĩa này.
V["носить"] = "mặc, đeo, mang, vác"

# cũ: "sớm" — THIẾU hẳn nửa nghĩa mà gloss Anh có: "it is early / it is too
# early" là vị ngữ vô nhân xưng («Ещё ра́но» = còn sớm), không phải trạng từ.
# Bổ sung cũng là cách rẻ nhất để tách khỏi ра́нний "sớm, ban đầu".
V["рано"] = "sớm, còn sớm"

# cũ: "môn quần vợt" — LỆCH KHUÔN của cả họ tên môn thể thao: футбо́л ghi trần
# "bóng đá", баскетбо́л ghi trần "bóng rổ", riêng те́ннис thừa chữ "môn". Đưa về
# khuôn trần cho ba thẻ nói cùng một giọng; thêm "tennis" vì tiếng Việt dùng cả
# hai tên.
V["теннис"] = "quần vợt, tennis"
