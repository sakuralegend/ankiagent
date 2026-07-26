# -*- coding: utf-8 -*-
"""LÔ 10 — field `HuongDan`: 15 từ về HỌC TẬP và KHÁI NIỆM.

Hai hậu tố trục:
  * `-ение / -ание` — biến động từ thành DANH TỪ TRỪU TƯỢNG, luôn GIỐNG TRUNG
  * `-ик` (người làm nghề) vs `-ика` (ngành học) — cặp đối lập gọn, nhận là dùng được

Và hai họ gốc lớn nhất trong lô: `чёт/счит` (đếm) và `род` (sinh ra) — riêng `род`
mở khoá cả chục từ nền tảng, kể cả thuật ngữ ngữ pháp "giống".

Chạy: python data/huongdan/lo10_hoctap_2026-07-27.py [--apply]
"""
import json
import sys
import urllib.request

ANKI = "http://127.0.0.1:8765"

ENIE = (
    '<div class="hd-sec">-ение / -ание: động từ đóng gói thành danh từ</div>'
    '<div class="hd-why">Gặp đuôi này là biết ngay ba điều, không cần tra: đây là <b>DANH TỪ</b>, '
    'nó <b>sinh ra từ một động từ</b>, và nó <b>GIỐNG TRUNG</b>.</div>'
    '<div class="hd-fam"><b>упражне́ние</b> bài tập · <b>спряже́ние</b> sự chia động từ · '
    '<b>объявле́ние</b> thông báo · <b>предложе́ние</b> câu; lời đề nghị · '
    '<b>зада́ние</b> nhiệm vụ · <b>явле́ние</b> hiện tượng</div>'
    '<div class="hd-why">Giống trung ⇒ tính từ đi kèm phải là dạng <b>-ое</b>: '
    '<b>дома́шнее зада́ние</b> (bài tập về nhà), <b>но́вое явле́ние</b> (hiện tượng mới).</div>'
)

IKA = (
    '<div class="hd-sec">-ик = NGƯỜI · -ика = NGÀNH</div>'
    '<div class="hd-why">Một cặp đối lập cực gọn: cùng một gốc, đổi đuôi là đổi từ người sang môn học.</div>'
    '<div class="hd-fam"><b>фи́зик</b> nhà vật lý → <b>фи́зика</b> môn vật lý · '
    '<b>матема́тик</b> → <b>матема́тика</b> · <b>хи́мик</b> → <b>хи́мия</b> · '
    '<b>исто́рик</b> → <b>исто́рия</b></div>'
    '<div class="hd-warn"><b>Tin tốt: trọng âm ĐỨNG YÊN</b> giữa hai dạng — фи́зик/фи́зика, '
    'матема́тик/матема́тика, исто́рик/исто́рия đều nhấn đúng một chỗ. Học chỗ nhấn một lần là '
    'dùng được cho cả cặp.</div>'
)

S = {}

# ---------- Họ gốc чёт/счит: đếm ----------

S["счёт"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span><span class="hd-gloss">GỘP LẠI, cộng vào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-чёт</span><span class="hd-gloss">ĐẾM — gốc <b>чёт/чит/счит</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>cái đã cộng gộp lại</b>. Từ một hình ảnh đó toả ra đủ nghĩa mà bạn sẽ gặp: <b>hoá đơn</b> (cộng tiền món ăn), <b>tài khoản</b> ngân hàng, <b>tỉ số</b> trận đấu.</div>'
    '<div class="hd-warn"><b>Câu phải thuộc khi đi ăn:</b> <b>Счёт, пожа́луйста!</b> = Tính tiền giúp tôi! Đây là một trong những câu bạn dùng sớm nhất.</div>'
    '<div class="hd-warn"><b>ё luôn mang trọng âm</b> ⇒ <b>счёт</b>. Nhưng số nhiều lại đổi mặt: <b>счета́</b> (hoá đơn) — chữ ё thành е khi mất trọng âm. Đây là luật chung: <b>ё chỉ tồn tại ở chỗ có nhấn</b>.</div>'
    '<div class="hd-sec">Họ hàng — gốc чёт/чит/счит (đếm)</div>'
    '<div class="hd-fam"><b>счита́ть</b> đếm; cho rằng · <b>зачёт</b> kỳ kiểm tra đạt/không đạt · <b>отчёт</b> bản báo cáo · <b>учёт</b> sự thống kê · <b>счётчик</b> đồng hồ đo</div>'
)

S["зачёт"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span><span class="hd-gloss">TÍNH VÀO, ghi nhận cho</span></div>'
    '<div class="hd-row"><span class="hd-piece">-чёт</span><span class="hd-gloss">ĐẾM — cùng gốc <b>счёт</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>được tính vào</b> (tính vào kết quả học tập). Chẻ ra rồi thì thấy nó là anh em ruột của <b>счёт</b> — chỉ khác tiền tố.</div>'
    '<div class="hd-warn"><b>Điều bạn cần biết về hệ thống Nga:</b> đại học Nga có HAI loại thi. <b>Зачёт</b> chỉ chấm <b>đạt / không đạt</b> (зачёт / незачёт), không cho điểm. Còn <b>экза́мен</b> mới chấm điểm theo thang 5. Đừng dịch cả hai thành "thi".</div>'
    '<div class="hd-warn"><b>ё luôn nhấn</b> ⇒ <b>зачёт</b>, nhấn cuối.</div>'
    '<div class="hd-sec">Họ hàng — gốc чёт (đếm)</div>'
    '<div class="hd-fam"><b>счёт</b> hoá đơn, tỉ số · <b>зачёт</b> kiểm tra đạt/trượt · <b>считать</b> đếm · <b>отчёт</b> báo cáo</div>'
)

# ---------- Họ gốc род: sinh ra ----------

S["род"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ <b>gốc trơn</b> một âm tiết — nhưng là một trong những <b>gốc sinh lợi nhất</b> tiếng Nga. Nghĩa lõi: <b>SINH RA, dòng dõi</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là từ đáng bỏ công nhất trong cả lô, vì nó mở khoá cả chục từ nền tảng mà bạn sẽ gặp liên tục. Học một gốc, nhận ra được cả họ.</div>'
    '<div class="hd-fam"><b>роди́ть</b> sinh · <b>роди́тели</b> bố mẹ · <b>ро́дина</b> quê hương, tổ quốc · <b>родно́й</b> ruột thịt, thân thương · <b>наро́д</b> nhân dân (<b>на</b>+<b>род</b> = những người cùng sinh ra) · <b>приро́да</b> thiên nhiên (<b>при</b>+<b>род</b> = cái vốn sinh ra như thế) · <b>ро́дственник</b> họ hàng</div>'
    '<div class="hd-warn"><b>Nghĩa NGỮ PHÁP bạn dùng mỗi ngày:</b> <b>род</b> = <b>GIỐNG</b> của danh từ. <b>мужско́й род</b> giống đực · <b>же́нский род</b> giống cái · <b>сре́дний род</b> giống trung. Chính là hệ thống bạn học ở lô danh từ đời sống.</div>'
    '<div class="hd-why">Ẩn dụ nằm dưới: giống ngữ pháp được người xưa hình dung như <b>dòng dõi</b> của từ — từ nào "sinh ra" trong dòng nào thì mang đuôi dòng ấy.</div>'
)

# ---------- Hậu tố -ение ----------

S["упражнение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span><span class="hd-gloss">tiền tố</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пражн-</span><span class="hd-gloss">gốc, nghĩa "làm cho bận, luyện"</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span><span class="hd-gloss">biến ĐỘNG TỪ → DANH TỪ, giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ động từ <b>упражня́ть</b> (luyện tập) đóng gói lại: <b>упражне́ние</b> = <b>bài tập</b>. Đây là từ bạn thấy ở đầu mỗi mục sách giáo khoa.</div>'
    '<div class="hd-warn">⚠️ Mức tin: gốc <b>-пражн-</b> tôi <b>không dám khẳng định</b> nối với từ nào bạn đã biết — các nhà từ nguyên còn tranh luận. Cái chắc chắn và dùng được là <b>khuôn -ение</b> ở dưới, chứ không phải gốc.</div>'
    '<div class="hd-warn"><b>Cụm trong sách:</b> <b>Упражне́ние 5</b> — đọc là "упражне́ние пять". Và <b>де́лать упражне́ния</b> = làm bài tập.</div>'
    + ENIE
)

S["спряжение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span><span class="hd-gloss">CÙNG, gộp lại</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пряж-</span><span class="hd-gloss">BUỘC, THẮNG ngựa vào xe (<b>г</b> mềm thành <b>ж</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span><span class="hd-gloss">biến động từ → danh từ, giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Là <b>спряга́ться</b> (mà bạn đã có thẻ) đóng gói thành danh từ. Hình ảnh gốc: <b>thắng mấy con ngựa vào chung một cỗ xe</b> — chia động từ cũng là buộc một gốc vào cả bộ đuôi sáu ngôi.</div>'
    '<div class="hd-why">Tiếng Anh trùng khít: <i>conjugation</i> ← <i>con-</i> (cùng) + <i>iugum</i> (cái ách buộc bò). Hai ngôn ngữ chọn đúng một ẩn dụ.</div>'
    '<div class="hd-warn"><b>Thuật ngữ bạn dùng ngay:</b> tiếng Nga có <b>hai lớp chia</b> — <b>пе́рвое спряже́ние</b> (lớp 1, nguyên âm <b>Е</b>) và <b>второ́е спряже́ние</b> (lớp 2, nguyên âm <b>И</b>). Chính là thứ bạn học ở lô động từ.</div>'
    '<div class="hd-why">Biến âm <b>г → ж</b> lại xuất hiện: <b>спряга́ть</b> → <b>спряже́ние</b>. Đúng luật đã gặp ở <b>снег → сне́жный</b>.</div>'
    + ENIE
)

S["начало"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span><span class="hd-gloss">tiền tố</span></div>'
    '<div class="hd-row"><span class="hd-piece">-чал-</span><span class="hd-gloss">BẮT ĐẦU (<b>нача́ть</b> = bắt đầu)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span><span class="hd-gloss">đuôi danh từ GIỐNG TRUNG</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Là động từ <b>нача́ть</b> đóng gói thành danh từ — nhưng bằng đuôi <b>-о</b> trần chứ không phải <b>-ение</b>. Cả hai kiểu đều cho ra <b>giống trung</b>.</div>'
    '<div class="hd-warn"><b>Từ cùng gốc gây bất ngờ:</b> <b>нача́льник</b> = <b>sếp, thủ trưởng</b> — nghĩa đen là "người khởi đầu, người đứng đầu". Thấy <b>нач-</b> là nhận ra ngay.</div>'
    '<div class="hd-warn"><b>Cặp đối:</b> <b>нача́ло</b> khởi đầu ↔ <b>коне́ц</b> kết thúc. Cụm hay dùng: <b>в нача́ле</b> = lúc đầu · <b>с самого нача́ла</b> = ngay từ đầu.</div>'
    '<div class="hd-sec">Họ hàng — gốc чал/чин (bắt đầu)</div>'
    '<div class="hd-fam"><b>нача́ть</b> bắt đầu (HT) · <b>начина́ть</b> bắt đầu (chưa HT) · <b>нача́ло</b> sự khởi đầu · <b>нача́льник</b> thủ trưởng · <b>снача́ла</b> lúc đầu; lại từ đầu</div>'
)

# ---------- Hậu tố -ик / -ика ----------

S["физика"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">физ-</span><span class="hd-gloss">Hy Lạp <i>physis</i> — TỰ NHIÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ика</span><span class="hd-gloss">hậu tố NGÀNH HỌC</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc: <b>môn học về tự nhiên</b>. Cùng gốc với tiếng Anh <i>physics</i>, <i>physical</i>, và cả <i>physician</i> (bác sĩ — người hiểu cơ thể tự nhiên).</div>'
    '<div class="hd-warn"><b>Trọng âm ở ĐẦU:</b> <b>фи́зика</b> — khác đa số từ mượn khác vốn nhấn cuối. May là dạng người (<b>фи́зик</b>) cũng nhấn đúng chỗ đó, không phải nhớ hai kiểu.</div>'
    + IKA
)

S["физик"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">физ-</span><span class="hd-gloss">Hy Lạp <i>physis</i> — TỰ NHIÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ик</span><span class="hd-gloss">hậu tố NGƯỜI LÀM NGHỀ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỉ khác <b>фи́зика</b> đúng một chữ <b>а</b> — mà đổi hẳn từ MÔN HỌC sang NGƯỜI HỌC nó. Đây là cặp gọn nhất để nhớ luật <b>-ик / -ика</b>.</div>'
    '<div class="hd-warn"><b>Bẫy giống:</b> <b>фи́зик</b> kết thúc bằng phụ âm ⇒ <b>giống đực</b>, và <b>luôn giống đực kể cả khi là phụ nữ</b> — y như <b>врач</b>. Nói <b>«Она́ хоро́ший фи́зик»</b> với tính từ giống đực.</div>'
    '<div class="hd-why">Hậu tố <b>-ик</b> còn dùng cho vật nhỏ (<b>до́мик</b> ngôi nhà nhỏ) — cùng một chữ, hai việc. Phân biệt bằng ngữ cảnh.</div>'
    + IKA
)

S["грамматика"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">граммат-</span><span class="hd-gloss">Hy Lạp <i>gramma</i> — CHỮ VIẾT, nét vạch</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ика</span><span class="hd-gloss">hậu tố NGÀNH HỌC</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc: <b>môn học về chữ viết</b>. Gốc <i>gramma</i> nằm trong hàng loạt từ bạn đã biết: <i>grammar</i>, <i>telegram</i>, <i>program</i>, <i>diagram</i> — và cả tiếng Nga: <b>програ́мма</b>, <b>телегра́мма</b>.</div>'
    '<div class="hd-warn"><b>Hai chữ М:</b> <b>грамма́тика</b> — giữ nguyên hai <b>м</b> của tiếng Hy Lạp. Cùng kiểu với <b>програ́мма</b>. Đây là chỗ dễ gõ thiếu.</div>'
    '<div class="hd-warn"><b>Từ cùng gốc rất hay dùng:</b> <b>гра́мотный</b> = biết chữ; giỏi, thạo việc. <i>гра́мотный специали́ст</i> = chuyên gia có nghề.</div>'
    + IKA
)

# ---------- Còn lại ----------

S["спорт"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn từ tiếng Anh <b>sport</b>, vốn từ tiếng Pháp cổ <i>desport</i> = <b>"mang tâm trí ĐI KHỎI"</b> công việc ← <i>des-</i> (đi khỏi) + <i>porter</i> (mang). Thể thao vốn nghĩa là <b>sự giải khuây</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-warn"><b>Danh từ này KHÔNG có số nhiều</b> trong tiếng Nga — <b>спорт</b> là khái niệm chung. Muốn nói "các môn thể thao" thì dùng <b>ви́ды спо́рта</b> (các loại của thể thao).</div>'
    '<div class="hd-warn"><b>Cụm dùng thật:</b> <b>занима́ться спо́ртом</b> = chơi thể thao, tập luyện. Chú ý <b>спо́ртом</b> ở <b>cách 5</b> — động từ <b>занима́ться</b> luôn đòi cách đó.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>спорт</b> thể thao · <b>спорти́вный</b> thuộc thể thao · <b>спортсме́н</b> vận động viên · <b>спортза́л</b> phòng tập</div>'
)

S["спортивный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">спорт-</span><span class="hd-gloss">спорт — thể thao</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ивн-</span><span class="hd-gloss">hậu tố tính từ quốc tế (đúng <i>-ive</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span><span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hậu tố <b>-ивный</b> là anh em với <b>-альный</b> mà bạn đã học — cũng là cửa vào kho từ quốc tế: <i>active</i> → <b>акти́вный</b> · <i>massive</i> → <b>масси́вный</b> · <i>effective</i> → <b>эффекти́вный</b>.</div>'
    '<div class="hd-warn"><b>Hai nghĩa:</b> <b>спорти́вный костю́м</b> = bộ đồ thể thao (thuộc thể thao) · <b>спорти́вный па́рень</b> = chàng trai thể thao, khoẻ khoắn (có dáng vận động viên).</div>'
    '<div class="hd-warn"><b>Trọng âm rơi vào -ти́в-</b>, đúng luật chung của từ mượn: nhấn về cuối hơn tiếng Anh.</div>'
)

S["точка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">точ-</span><span class="hd-gloss">CHẤM, chọc — cùng gốc <b>ткнуть</b> (chọc, dí)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-а</span><span class="hd-gloss">hậu tố vật nhỏ + đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>vết chọc nhỏ</b> — đúng cách một cái chấm ra đời. Từ đó ra mọi nghĩa: dấu chấm câu, điểm trên bản đồ, điểm trong hình học.</div>'
    '<div class="hd-why">Cùng gốc là <b>то́чный</b> (chính xác) — chính xác tức là <b>trúng đúng cái chấm</b>. Và <b>то́чно</b> = "đúng vậy, chính xác", một từ đệm bạn sẽ nghe suốt trong hội thoại.</div>'
    '<div class="hd-warn"><b>Cụm rất hay dùng:</b> <b>то́чка зре́ния</b> = <b>quan điểm</b> — nghĩa đen "điểm của cái nhìn", đúng như tiếng Anh <i>point of view</i>.</div>'
    '<div class="hd-sec">Họ hàng — gốc точ/тк</div>'
    '<div class="hd-fam"><b>то́чный</b> chính xác · <b>то́чно</b> chính xác, đúng thế · <b>то́чка</b> dấu chấm; điểm · <b>уто́чнить</b> làm rõ thêm</div>'
)

S["цвет"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ <b>gốc trơn</b>. Nghĩa: <b>MÀU SẮC</b> — nhưng gốc của nó nối màu với <b>hoa</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một gốc <b>цвет-</b> cho hai thứ: <b>màu</b> và <b>bông hoa</b> (<b>цвето́к</b>), vì hoa chính là chỗ màu sắc hiện ra rực rỡ nhất trong tự nhiên. Động từ <b>цвести́</b> = nở hoa.</div>'
    '<div class="hd-warn"><b>BẪY SỐ NHIỀU — hai dạng, hai nghĩa khác hẳn:</b><br>'
    '<b>цвета́</b> = các MÀU SẮC<br>'
    '<b>цветы́</b> = các BÔNG HOA<br>'
    'Cùng một gốc mà tách đôi ở số nhiều. Nhớ sai là mua nhầm quà.</div>'
    '<div class="hd-warn"><b>Câu hỏi phải thuộc:</b> <b>Како́го цве́та?</b> = Màu gì? Chú ý dùng <b>cách 2</b> (цве́та), không phải cách 1.</div>'
    '<div class="hd-sec">Họ hàng — gốc цвет</div>'
    '<div class="hd-fam"><b>цвет</b> màu sắc · <b>цвето́к</b> bông hoa · <b>цветы́</b> hoa (số nhiều) · <b>цвести́</b> nở hoa · <b>цветно́й</b> có màu</div>'
)

S["чудо"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ <b>gốc trơn</b>, đuôi <b>-о</b> nên <b>giống trung</b>. Nghĩa: <b>phép màu, điều kỳ diệu</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-warn"><b>SỐ NHIỀU BẤT THƯỜNG — phải thuộc riêng:</b> <b>чу́до</b> → <b>чудеса́</b>, mọc thêm cả cụm <b>-ес-</b>. Chỉ một nhóm nhỏ danh từ giống trung làm vậy, và đáng thuộc cả cụm: <b>чу́до → чудеса́</b> · <b>не́бо</b> bầu trời <b>→ небеса́</b>. Đây là dấu vết của một lớp biến cách cổ đã biến mất.</div>'
    '<div class="hd-why">Từ này rất sống trong tiếng Nga đời thường: <b>чуде́сный</b> = tuyệt vời (lời khen thường ngày, không hề trang trọng) · <b>чуда́к</b> = người lập dị, hâm hâm (nói vui, không ác ý).</div>'
    '<div class="hd-warn"><b>Nhắc lại luật ЧУ:</b> viết <b>чу́до</b> với <b>У</b>, không đời nào là <i>*чюдо</i>.</div>'
    '<div class="hd-sec">Họ hàng — gốc чуд</div>'
    '<div class="hd-fam"><b>чу́до</b> phép màu · <b>чудеса́</b> những điều kỳ diệu · <b>чуде́сный</b> tuyệt vời · <b>чуда́к</b> người lập dị</div>'
)

S["тип"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn qua Hy Lạp <b>typos</b> = <b>DẤU IN, vết đóng</b> — cái khuôn dập ra hàng loạt bản giống nhau. Từ đó ra nghĩa "kiểu, loại".</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc với hàng loạt từ bạn đã biết: <i>type</i>, <i>typical</i>, <i>typography</i>. Tiếng Nga giữ nguyên: <b>типи́чный</b> (điển hình), <b>типогра́фия</b> (nhà in).</div>'
    '<div class="hd-warn"><b>Nghĩa lóng phải biết để khỏi hiểu nhầm:</b> trong khẩu ngữ, <b>тип</b> còn nghĩa là <b>"gã, tay ấy"</b> — và mang sắc thái <b>hơi coi thường</b>. <i>Стра́нный тип</i> = một gã kỳ quặc. Đừng dùng từ này để chỉ người bạn tôn trọng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тип</b> kiểu, loại · <b>типи́чный</b> điển hình · <b>типогра́фия</b> nhà in · <b>прототи́п</b> nguyên mẫu</div>'
)


# ---------------------------------------------------------------------------
def ac(action, **params):
    req = urllib.request.Request(
        ANKI, json.dumps({"action": action, "version": 6, "params": params}).encode())
    out = json.load(urllib.request.urlopen(req, timeout=180))
    if out.get("error"):
        raise RuntimeError(f"{action}: {out['error']}")
    return out["result"]


def main():
    apply = "--apply" in sys.argv
    ok, miss = [], []
    for word, html in S.items():
        ids = ac("findNotes", query=f'note:RU_Word WordClean:{word}')
        if len(ids) != 1:
            miss.append((word, len(ids)))
            continue
        if apply:
            ac("updateNoteFields", note={"id": ids[0], "fields": {"HuongDan": html}})
        ok.append(word)
    print(f"khop: {len(ok)}/{len(S)}")
    for w, n in miss:
        print(f"  !! {w}: tim thay {n} note")
    if apply:
        print("da ghi. sync:", ac("sync"))
    else:
        print("(chua ghi gi — them --apply de ghi that)")


if __name__ == "__main__":
    main()
