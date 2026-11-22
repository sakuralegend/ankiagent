# -*- coding: utf-8 -*-
"""k184 — actions: 10 cặp thể (+1 lẻ), trục là TIỀN TỐ + gốc đã học.

Chỗ cần nhất quán trong lô:
(1) вед-/вод- «DẪN»: ввести/вводить · произвести/производить · вывести/выводить. MỘT câu luật
    giống hệt nhau ở cả 6 thẻ: tiền tố + вести́ → HT, tiền tố + води́ть → CHT (như привести́/
    приводи́ть k125). про-/-из- khớp произво́дство (k119); вы́- khớp вы́вод (k167).
(2) мен- «ĐỔI» (như меня́ть k95): отменить/отменять, меняться/поменяться.
    отмени́ть ↔ отме́тить (k160) = trùng mặt chữ, dùng làm ô đỏ.
(3) вер(т)-/ворот- «QUAY» (như верну́ть k94, поворо́т k173): повернуться/поворачиваться.
(4) чин- «xếp vào nếp» — khớp причи́на (k99). тян- — -ну- ở đây KHÔNG phải hậu tố «một lần» (k171).
(5) сущ- «đang có» như существова́ть (k122) — осуществить/осуществлять.
Họ hàng: không thẻ nào vắng.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "меняться": "thay đổi, đổi cho nhau, trao đổi, thay phiên nhau",   # gỡ ⊆ изменя́ться: bỏ «biến đổi», thêm swap/exchange/take turns
    "поменяться": "thay đổi, đổi cho nhau, trao đổi, đổi chỗ",           # cùng bộ với меня́ться (+exchange)
    "починить": "sửa, sửa chữa, vá",                                   # bỏ «sửa xong» — nhãn thể trá hình; +mend/patch
    "тянуть": "kéo, lôi, giật, kéo dài, trì hoãn",                     # thiếu drag out / delay
    "вывести": "dẫn ra, dắt ra, đưa ra, rút ra",                       # thiếu deduce/withdraw (→ вы́вод kết luận)
    "выводить": "dẫn ra, dắt ra, đưa ra, rút ra",                      # khớp bản id 4294 «dẫn ra, đưa ra, rút ra»
    "повернуться": "quay người, xoay người, quay lại",                 # bỏ «trở» — mơ hồ
    "поворачиваться": "quay, xoay, quay người",                        # bỏ «trở» — mơ hồ
}

# --------------------------------------------------------------------- ввести
S["ввести"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO TRONG — nên có HAI chữ <b>в</b> liền nhau</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вес- (вед-)</span>'
    '<span class="hd-gloss">DẪN — chính là <b>вести́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dẫn VÀO ⇒ đưa vào, đưa vào dùng (luật, biện pháp), nhập: '
    '<b>ввести́ паро́ль</b> nhập mật khẩu. Cả họ: tiền tố + <b>вести́</b> → HOÀN THÀNH, tiền tố + <b>води́ть</b> → CHƯA HOÀN THÀNH (như <b>привести́ / приводи́ть</b>). Chia như <b>вести́</b>: '
    '<b>введу́, введёшь</b>; quá khứ rơi <i>д</i>: <b>ввёл, ввела́</b>.</div>'
    '<div class="hd-warn"><b>ввести́ в заблужде́ние</b> = đánh lừa, làm ai hiểu lầm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вводи́ть</b> (CHT) · <b>введе́ние</b> phần mở đầu; sự đưa vào · '
    '<b>вести́</b> dẫn</div>'
)

# --------------------------------------------------------------------- вводить
S["вводить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO TRONG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вод-и́ть</span>'
    '<span class="hd-gloss">DẪN — chính là <b>води́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đang đưa vào, hay đưa vào: <b>вводи́ть да́нные</b> nhập dữ liệu. Cả họ: tiền tố + <b>вести́</b> → HOÀN THÀNH, tiền tố + <b>води́ть</b> → CHƯA HOÀN THÀNH (như <b>привести́ / приводи́ть</b>). Chia như <b>води́ть</b>: ngôi «tôi» <i>д → ж</i>, trọng âm lùi: '
    '<b>ввожу́, вво́дишь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ввести́</b> (HT) · <b>ввод</b> sự nhập (dữ liệu) · '
    '<b>води́ть</b> dẫn đi lại</div>'
)

# --------------------------------------------------------------------- произвести
S["произвести"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">ra phía trước</span></div>'
    '<div class="hd-row"><span class="hd-piece">-из-</span>'
    '<span class="hd-gloss">ra khỏi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вес- (вед-)</span>'
    '<span class="hd-gloss">DẪN — chính là <b>вести́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Dẫn ra» ⇒ làm ra sản phẩm, làm ra một việc (tiến hành), gây ra — '
    'khớp từng mảnh Latin <i>pro-ducere</i> → Anh <i>produce</i>. Cả họ: tiền tố + <b>вести́</b> → HOÀN THÀNH, tiền tố + <b>води́ть</b> → CHƯA HOÀN THÀNH (như <b>привести́ / приводи́ть</b>). '
    'Quá khứ rơi <i>д</i>: <b>произвёл, произвела́</b>.</div>'
    '<div class="hd-warn"><b>произвести́ впечатле́ние на</b> + cách 4 = gây ấn tượng với ai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>производи́ть</b> (CHT) · <b>произво́дство</b> sự sản xuất · '
    '<b>производи́тель</b> nhà sản xuất</div>'
)

# --------------------------------------------------------------------- производить
S["производить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">ra phía trước</span></div>'
    '<div class="hd-row"><span class="hd-piece">-из-</span>'
    '<span class="hd-gloss">ra khỏi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вод-и́ть</span>'
    '<span class="hd-gloss">DẪN — chính là <b>води́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Dẫn ra» thường xuyên ⇒ sản xuất: <b>Заво́д произво́дит маши́ны</b> '
    'nhà máy sản xuất ô tô. Cả họ: tiền tố + <b>вести́</b> → HOÀN THÀNH, tiền tố + <b>води́ть</b> → CHƯA HOÀN THÀNH (như <b>привести́ / приводи́ть</b>). Ngôi «tôi» <i>д → ж</i>, trọng âm lùi: '
    '<b>произвожу́, произво́дишь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>произвести́</b> (HT) · <b>произво́дство</b> sự sản xuất · '
    '<b>заво́д</b> nhà máy (cùng <b>-вод-</b>)</div>'
)

# --------------------------------------------------------------------- вывести
S["вывести"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы́-</span>'
    '<span class="hd-gloss">RA NGOÀI — ở thể HT luôn giữ trọng âm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вес- (вед-)</span>'
    '<span class="hd-gloss">DẪN — chính là <b>вести́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dẫn RA: <b>вы́вести соба́ку</b> dắt chó ra ngoài. Dẫn ra từ cái đã '
    'biết ⇒ rút ra (công thức, kết luận) — chính là <b>вы́вод</b>. Cả họ: tiền tố + <b>вести́</b> → HOÀN THÀNH, tiền tố + <b>води́ть</b> → CHƯA HOÀN THÀNH (như <b>привести́ / приводи́ть</b>). '
    'Trọng âm đứng yên ở <b>вы́</b>: <b>вы́веду, вы́вел, вы́вела</b>.</div>'
    '<div class="hd-warn"><b>вы́вести из себя́</b> «dẫn ai ra khỏi chính mình» = chọc ai nổi '
    'điên.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>выводи́ть</b> (CHT) · <b>вы́вод</b> kết luận · <b>вести́</b> dẫn</div>'
)

# --------------------------------------------------------------------- выводить
S["выводить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span>'
    '<span class="hd-gloss">RA NGOÀI — ở đây mất trọng âm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вод-и́ть</span>'
    '<span class="hd-gloss">DẪN — chính là <b>води́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đang dẫn ra, hay dẫn ra, rút ra; cả «làm cho vết bẩn ra»: '
    '<b>выводи́ть пя́тна</b> tẩy vết bẩn. Cả họ: tiền tố + <b>вести́</b> → HOÀN THÀNH, tiền tố + <b>води́ть</b> → CHƯA HOÀN THÀNH (như <b>привести́ / приводи́ть</b>). Trọng âm rời <b>вы-</b>: '
    '<b>вывожу́, выво́дишь</b> — ngược với <b>вы́вести</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вы́вести</b> (HT) · <b>вы́вод</b> kết luận · '
    '<b>води́ть</b> dẫn đi lại</div>'
)

# --------------------------------------------------------------------- починить
S["починить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố thể, KHÔNG mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-чини́ть</span>'
    '<span class="hd-gloss">sửa — chính là <b>чини́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>чини́ть</b> làm trọn ⇒ sửa xong một món: '
    '<b>почини́ть велосипе́д</b> sửa xe đạp. Trọng âm lùi từ ngôi 2: '
    '<b>починю́, почи́нишь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>чини́ть</b> (CHT) · <b>чин</b> cấp bậc · '
    '<b>причи́на</b> nguyên nhân</div>'
)

# --------------------------------------------------------------------- чинить
S["чинить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">чин-</span>'
    '<span class="hd-gloss">XẾP VÀO NẾP — như <b>чин</b> thứ bậc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đưa đồ hỏng về lại nếp ⇒ sửa, vá. Trọng âm lùi từ ngôi 2: '
    '<b>чиню́, чи́нишь</b>. Cặp HT: <b>почини́ть</b>.</div>'
    '<div class="hd-warn">Chỉ sửa ĐỒ VẬT. Sửa lỗi, sửa bài ⇒ <b>испра́вить</b>: '
    '<b>испра́вить оши́бку</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>почини́ть</b> (HT) · <b>чин</b> cấp bậc · '
    '<b>чино́вник</b> quan chức · <b>причи́на</b> nguyên nhân</div>'
)

# --------------------------------------------------------------------- испортить
S["испортить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ис- (из-)</span>'
    '<span class="hd-gloss">tiền tố thể, ở đây không thêm nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-по́ртить</span>'
    '<span class="hd-gloss">làm hỏng — chính là <b>по́ртить</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>по́ртить</b> làm trọn ⇒ làm hỏng hẳn: <b>испо́ртить пра́здник</b> '
    'phá hỏng ngày lễ. Ngôi «tôi» <i>т → ч</i>: <b>испо́рчу, испо́ртишь</b>.</div>'
    '<div class="hd-warn"><b>из-</b> đứng trước phụ âm vô thanh (<b>п</b>) thì viết <b>ис-</b>: '
    'gõ <b>испо́ртить</b>, không phải «изпортить».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>по́ртить</b> (CHT) · <b>испо́рченный</b> hư hỏng, ôi thiu</div>'
)

# --------------------------------------------------------------------- портить
S["портить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по́рт-</span>'
    '<span class="hd-gloss">LÀM HỎNG — gốc trơn, không nối sang từ quen nào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm cho tệ đi: <b>Не по́рти мне настрое́ние!</b> Đừng làm hỏng tâm trạng '
    'tôi! Ngôi «tôi» <i>т → ч</i>: <b>по́рчу, по́ртишь</b>. Cặp HT: <b>испо́ртить</b>.</div>'
    '<div class="hd-why"><b>порт</b> (cảng), <b>спорт</b>, <b>па́спорт</b> chỉ trùng mặt chữ — '
    'đừng nối nghĩa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>испо́ртить</b> (HT) · <b>по́ртиться</b> bị hỏng, ôi thiu · '
    '<b>по́рча</b> sự hư hỏng</div>'
)

# --------------------------------------------------------------------- потянуть
S["потянуть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố thể, KHÔNG mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тяну́ть</span>'
    '<span class="hd-gloss">kéo — chính là <b>тяну́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>тяну́ть</b> làm trọn một lần: <b>потяну́ть за ру́чку</b> kéo tay '
    'nắm. Trọng âm lùi từ ngôi 2: <b>потяну́, потя́нешь</b>.</div>'
    '<div class="hd-warn"><b>потяну́ть мы́шцу</b> = bị căng cơ (kéo giãn cơ).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тяну́ть</b> (CHT) · <b>вы́тянуть</b> kéo ra; bốc (phiếu) · '
    '<b>тя́га</b> lực kéo</div>'
)

# --------------------------------------------------------------------- тянуть
S["тянуть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">тян-</span>'
    '<span class="hd-gloss">KÉO, CĂNG — gốc trơn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-у́ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Kéo liên tục ⇒ kéo, lôi; kéo DÀI thời gian ⇒ dây dưa: <b>Не тяни́!</b> '
    'Đừng dây dưa! Kéo vào chỗ nào: <b>за</b> + cách 4 — <b>тяну́ть за верёвку</b>. '
    'Trọng âm lùi từ ngôi 2: <b>тяну́, тя́нешь</b>.</div>'
    '<div class="hd-warn"><b>-ну́ть</b> ở đây KHÔNG phải hậu tố «một lần» như <b>кивну́ть</b>: '
    '<b>тяну́ть</b> là CHƯA HOÀN THÀNH, cặp HT là <b>потяну́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>потяну́ть</b> (HT) · <b>тяну́ться</b> vươn tới; kéo dài · '
    '<b>вы́тянуть</b> kéo ra · <b>тя́га</b> lực kéo</div>'
)

# --------------------------------------------------------------------- осуществить
S["осуществить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">LÀM CHO THÀNH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сущ-еств-</span>'
    '<span class="hd-gloss">CÓ THẬT, đang có — như <b>существова́ть</b> tồn tại</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm cho thành cái CÓ THẬT ⇒ thực hiện, biến thành hiện thực: '
    '<b>осуществи́ть мечту́</b> thực hiện ước mơ. Giọng trang trọng, sách báo.</div>'
    '<div class="hd-warn">Ngôi «tôi» <i>в → вл</i>: <b>осуществлю́, осуществи́шь</b> — và cặp '
    'CHT giữ luôn <b>вл</b>: <b>осуществля́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>осуществля́ть</b> (CHT) · <b>осуществле́ние</b> sự thực hiện · '
    '<b>существова́ть</b> tồn tại · <b>существо́</b> sinh vật</div>'
)

# --------------------------------------------------------------------- осуществлять
S["осуществлять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">LÀM CHO THÀNH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сущ-еств-</span>'
    '<span class="hd-gloss">CÓ THẬT — như <b>существова́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-л-я́ть</span>'
    '<span class="hd-gloss"><i>в</i> thêm <i>л</i> + đuôi chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đang thực hiện, thực thi đều đặn: <b>осуществля́ть контро́ль</b> thực '
    'hiện việc kiểm soát. Chia đều: <b>осуществля́ю, осуществля́ешь</b>. Cặp HT: '
    '<b>осуществи́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>осуществи́ть</b> (HT) · <b>осуществле́ние</b> sự thực hiện · '
    '<b>существова́ть</b> tồn tại</div>'
)

# --------------------------------------------------------------------- отменить
S["отменить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">RỜI KHỎI, bỏ đi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мен-</span>'
    '<span class="hd-gloss">ĐỔI — như <b>меня́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đổi ý mà gạt bỏ đi ⇒ huỷ, bãi bỏ: <b>отмени́ть рейс</b> huỷ chuyến bay, '
    '<b>отмени́ть зако́н</b> bãi bỏ luật. Trọng âm lùi từ ngôi 2: <b>отменю́, отме́нишь</b>.</div>'
    '<div class="hd-warn"><b>отмени́ть</b> huỷ (gốc <b>мен-</b> đổi) ≠ <b>отме́тить</b> đánh dấu '
    '(gốc <b>мет-</b>) — chỉ khác <b>н</b>/<b>т</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отменя́ть</b> (CHT) · <b>отме́на</b> sự huỷ bỏ · '
    '<b>меня́ть</b> đổi · <b>заменя́ть</b> thay thế</div>'
)

# --------------------------------------------------------------------- отменять
S["отменять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">RỜI KHỎI, bỏ đi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мен-я́ть</span>'
    '<span class="hd-gloss">ĐỔI — như <b>меня́ть</b>, đuôi chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đang huỷ, hay huỷ: <b>Зимо́й ча́сто отменя́ют ре́йсы</b> mùa đông '
    'hay huỷ chuyến bay. Chia đều: <b>отменя́ю, отменя́ешь</b>. Cặp HT: <b>отмени́ть</b> '
    '(<i>-я́ть ↔ -и́ть</i>, như <b>заменя́ть / замени́ть</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отмени́ть</b> (HT) · <b>отме́на</b> sự huỷ bỏ · '
    '<b>изменя́ть</b> thay đổi</div>'
)

# --------------------------------------------------------------------- повернуться
S["повернуться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố thể, KHÔNG mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вер-ну-</span>'
    '<span class="hd-gloss">QUAY một cái — như <b>верну́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ться</span>'
    '<span class="hd-gloss">chính mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Quay CHÍNH MÌNH một cái ⇒ quay người. Quay về phía ai: <b>к</b> + cách 3 '
    '— <b>Он поверну́лся ко мне</b>. Chia: <b>поверну́сь, повернёшься</b>.</div>'
    '<div class="hd-warn"><b>поверну́ться</b> = xoay mình (tại chỗ) · <b>верну́ться</b> = trở về '
    '(chỗ cũ). Tiếng Việt đều là «quay lại».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>повора́чиваться</b> (CHT) · <b>поворо́т</b> chỗ rẽ · '
    '<b>верну́ться</b> trở về · <b>верте́ть</b> xoay</div>'
)

# --------------------------------------------------------------------- поворачиваться
S["поворачиваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố thể, KHÔNG mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вора́ч-</span>'
    '<span class="hd-gloss">QUAY — <b>-ворот-</b> như <b>поворо́т</b>, <i>т → ч</i> trước '
    '<i>-ива-</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ть-ся</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành + chính mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đang quay mình, hay xoay người. Chia đều: <b>повора́чиваюсь</b>. '
    'Cặp HT lệch mặt chữ: <b>поверну́ться</b> — <i>е/о</i> chạy qua lại trong cùng gốc quay.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поверну́ться</b> (HT) · <b>поворо́т</b> chỗ rẽ · '
    '<b>разворо́т</b> sự quay đầu xe</div>'
)

# --------------------------------------------------------------------- поделиться
S["поделиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố thể, KHÔNG mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дели́ться</span>'
    '<span class="hd-gloss">chia sẻ — chính là <b>дели́ться</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>дели́ться</b> làm trọn một lần. Cái được chia ở cách 5, người nhận '
    '<b>с</b> + cách 5: <b>подели́ться но́востью с дру́гом</b> kể tin cho bạn. '
    'Trọng âm lùi từ ngôi 2: <b>поделю́сь, поде́лишься</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дели́ться</b> (CHT) · <b>дели́ть</b> chia · <b>разде́л</b> phần, mục</div>'
)

# --------------------------------------------------------------------- меняться
S["меняться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мен-</span>'
    '<span class="hd-gloss">ĐỔI — chính là <b>меня́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́ть-ся</span>'
    '<span class="hd-gloss">đuôi + chính mình / lẫn nhau</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>-ся</b> mở hai nghĩa: tự đổi ⇒ thay đổi (<b>Пого́да меня́ется</b>); '
    'hai bên đổi CHO NHAU ⇒ trao đổi, thay phiên. <b>изменя́ться</b> chỉ có nghĩa thứ nhất. '
    'Chia đều: <b>меня́юсь, меня́ешься</b>.</div>'
    '<div class="hd-warn">Đổi với AI: <b>с</b> + cách 5; đổi CÁI GÌ: cách 5 — '
    '<b>меня́ться с дру́гом кни́гами</b> = đổi sách với bạn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поменя́ться</b> (HT) · <b>меня́ть</b> đổi · '
    '<b>обме́н</b> sự trao đổi · <b>изменя́ться</b> thay đổi</div>'
)

# --------------------------------------------------------------------- поменяться
S["поменяться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố thể, KHÔNG mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-меня́ться</span>'
    '<span class="hd-gloss">chính là <b>меня́ться</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>меня́ться</b> làm trọn một lần — hay gặp nhất là đổi cho nhau: '
    '<b>поменя́ться роля́ми</b> đổi vai cho nhau; cũng dùng cho «đã thay đổi»: '
    '<b>Всё поменя́лось</b>. Chia đều: <b>поменя́юсь, поменя́ешься</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>меня́ться</b> (CHT) · <b>поменя́ть</b> đổi · '
    '<b>обме́н</b> sự trao đổi</div>'
)

B = {
    "docbangmat": 111,
    "loitubat": 1,
    "nguonsai": 0,
    "baolen": [
        "Tự sửa 1 lỗi: thẻ выводи́ть viết «вы- ở thể CHT mất trọng âm» — quá rộng (вы́глядеть CHT vẫn nhấn вы́, đúng lỗi k171 từng bắt); đã hạ thành «ở đây mất trọng âm».",
        "Va chạm меня́ться ⊆ изменя́ться[k133]: gỡ phía mình — bỏ «biến đổi», giữ «thay đổi», thêm nghĩa có trong gloss (swap / exchange with each other / take turns) → «thay đổi, đổi cho nhau, trao đổi, thay phiên nhau». Nếu giữ «biến đổi» thì изменя́ться {thay đổi, biến đổi} lại nằm gọn trong меня́ться nên máy vẫn kêu. Chưa chạy được `vacham` (cần Anki) — luồng chính soát lại.",
        "выводи́ть: luồng chính nói id 4294 đã có «dẫn ra, đưa ra, rút ra», nhưng `tiep` in «dẫn ra, dắt ra, đưa ra» — V ghi «dẫn ra, dắt ra, đưa ra, rút ra» cho cả вы́вести/выводи́ть; luồng chính kiểm `nap` ghi đúng note nào.",
        "V cần duyệt: поменя́ться (+trao đổi), почини́ть (bỏ «sửa xong» — nhãn thể trá hình, +vá), тяну́ть (+kéo dài, trì hoãn — drag out/delay), вы́вести/выводи́ть (+rút ra — deduce/withdraw), поверну́ться/повора́чиваться (bỏ «trở» — mơ hồ; +quay người). Các từ khác giữ nguyên đề cũ.",
        "Luật -вести́ → HT / -води́ть → CHT: MỘT câu giống hệt nhau ở cả 6 thẻ ввести/вводить/произвести/производить/вывести/выводить, dẫn chiếu привести́/приводи́ть (k125). Lô k175 (завести/заводить) nên dùng đúng câu này.",
        "Không chắc (đã nói mềm hoặc không nói): по́ртить ghi «gốc trơn, không nối sang từ quen» — từ nguyên có thể dính порт «vải» cổ, không đưa lên thẻ; чини́ть ← чин «trật tự, thứ bậc» là nối hình thái theo thẻ причи́на (k99), không ghi Mức tin; о- trong осуществи́ть ghi «làm cho thành».",
        "Báo oan của máy đã bỏ: по́ртить/испо́ртить ↔ порт/спорт/па́спорт (đưa vào thẻ по́ртить như một câu «chỉ trùng mặt chữ»), отмени́ть ↔ отме́тить (thành ô đỏ), произвести́ ↔ изве́стный/произойти́ (không nhắc).",
    ],
}
