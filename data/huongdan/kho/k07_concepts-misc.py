# -*- coding: utf-8 -*-
"""k07 — concepts::misc: 15 từ rời, KHÔNG cùng một họ (14 danh từ + 1 dạng
trạng từ `кита́йски`). Vì lô không có trục chung nên mỗi thẻ đứng một mình —
không khối hệ thống dùng chung (README §3), tối đa 2 ô đỏ, nhắm dưới một màn
hình iPhone (README §2b).

Hai chỗ lặp lại tự nhiên trong lô, cố ý giải thích NHẤT QUÁN chứ không dựng
khối chung: ① nguyên âm chạy `о` ở `па́лка / ма́рка / прыжо́к`; ② dạng cách 6
riêng sau в/на ở `круг` (в кругу́) và `край` (в краю́).

Câu chú ý bảng chia (chuẩn v3, mục C) đặt ở CUỐI thẻ, ngay trên chỗ máy nối
bảng vào. 7/15 từ có khối BAT THUONG: па́лка · ма́рка · герб · круг · де́ньги ·
край · прыжо́к.
"""

# 🔴 KHÔNG dựng biến khối dùng chung (HE/LUAT/THE…) rồi cộng vào mọi thẻ — README §3.

S = {}
V = {}

S["палка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пал-</span>'
    '<span class="hd-gloss">KHÚC GỖ DÀI cầm được</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-а</span>'
    '<span class="hd-gloss">hậu tố + đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>пал-</b> chỉ một khúc gỗ dài cầm trong tay: to thì để '
    'chống đi, nhỏ thì thêm hậu tố nhỏ thành <b>па́лочка</b> — que, đũa, dùi trống.</div>'
    '<div class="hd-warn"><b>перегну́ть па́лку</b> = bẻ cong cây gậy quá tay → làm quá lố, '
    'đi quá đà. Nghe rất nhiều trong lời trách.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>па́лочка</b> que nhỏ, đũa, dùi trống · '
    '<b>кита́йские па́лочки</b> đôi đũa ăn cơm</div>'
    '<div class="hd-why"><b>Bảng chia:</b> đều tăm tắp, lệch đúng một ô — cách 2 số nhiều '
    '<b>па́лок</b>. Bỏ <i>-а</i> đi thì <i>л</i> dính sát <i>к</i> không đọc nổi, nên '
    'tiếng Nga chèn <b>о</b> vào giữa.</div>'
)

S["марка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — mượn nguyên khối từ tiếng Đức <i>Marke</i> '
    '(cái dấu, cái ký hiệu), cùng gốc với tiếng Anh <i>mark</i>. Tiếng Nga chỉ thêm '
    'đuôi <i>-а</i> cho nó thành danh từ giống cái.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giữ đúng một nghĩa gốc là <b>CÁI DẤU</b>, rồi tách hai nhánh: '
    'dấu dán lên phong bì = con tem; dấu của nhà sản xuất = nhãn hiệu, hãng.</div>'
    '<div class="hd-warn"><b>держа́ть ма́рку</b> = giữ vững nhãn hiệu → giữ thể diện, giữ '
    'phong độ, không để mất mặt.</div>'
    '<div class="hd-why"><b>Bảng chia:</b> y hệt <b>па́лка</b> — chỉ cách 2 số nhiều lệch, '
    'chèn <b>о</b> vào giữa <i>р</i> và <i>к</i> thành <b>ма́рок</b>.</div>'
)

S["музыка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">муз-</span>'
    '<span class="hd-gloss">Му́за — nữ thần nghệ thuật Hy Lạp</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ык-а</span>'
    '<span class="hd-gloss">hậu tố Hy Lạp + đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một từ Hy Lạp <i>mousikē</i> = "nghề của các nàng Muse" đẻ ra cả '
    '<i>music</i> lẫn <b>му́зыка</b>. Trọng âm Nga rơi vào âm ĐẦU và đứng yên suốt bảng '
    'chia.</div>'
    '<div class="hd-warn"><b>Nhưng thêm hậu tố là trọng âm nhảy:</b> му́зыка → '
    '<b>музыка́льный</b> (thuộc âm nhạc, có khiếu nhạc) → <b>музыка́нт</b> (nhạc công). '
    'Đọc му́зыкальный là sai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>музыка́нт</b> nhạc công · <b>музыка́льный</b> thuộc âm nhạc · '
    '<b>му́за</b> nàng thơ, nguồn cảm hứng</div>'
)

S["форма"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — mượn từ Latin <i>forma</i> vừa có nghĩa '
    '"hình dáng" vừa có nghĩa "cái khuôn". Cùng gốc với tiếng Anh <i>form</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bám vào nghĩa <b>CÁI KHUÔN</b> là suy ra cả ba nghĩa Nga: hình '
    'đúc theo khuôn = hình dạng · tờ giấy in sẵn theo khuôn = biểu mẫu · bộ quần áo may '
    'theo khuôn quy định = đồng phục.</div>'
    '<div class="hd-warn"><b>быть в фо́рме</b> đọc theo ngữ cảnh: nói về người mặc gì thì là '
    '"đang mặc đồng phục", còn nói về sức khoẻ / thi đấu thì là <b>đang sung sức, đúng '
    'phong độ</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>формирова́ть</b> tạo dựng, hình thành · <b>рефо́рма</b> cải '
    'cách · <b>информа́ция</b> thông tin · <b>унифо́рма</b> đồng phục</div>'
)

S["сцена"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — mượn qua Latin <i>scaena</i> từ tiếng Hy Lạp '
    '<i>skēnē</i>, vốn nghĩa là <b>cái lều dựng phía sau chỗ diễn</b> để diễn viên thay đồ. '
    'Cùng gốc với tiếng Anh <i>scene</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ cái lều đó ra chỗ diễn (<b>сце́на</b> = sân khấu), rồi ra thứ '
    'diễn trên đó (<b>сце́на</b> = cảnh, màn trong phim/kịch). Một từ, hai nghĩa nối liền '
    'nhau.</div>'
    '<div class="hd-warn"><b>устро́ить сце́ну</b> = làm ầm ĩ, làm toáng lên với ai — đúng '
    'nghĩa "diễn một màn". Giống hệt <i>make a scene</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сцена́рий</b> kịch bản (trọng âm nhảy ra <i>-на́-</i>) · '
    '<b>сценари́ст</b> người viết kịch bản</div>'
)

S["группа"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — mượn từ tiếng Đức <i>Gruppe</i>, gốc xa hơn là '
    'tiếng Ý <i>gruppo</i> = <b>cái nút thắt, cụm túm lại</b>. Cùng gốc tiếng Anh '
    '<i>group</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cứ giữ hình ảnh "túm thành một cụm" là ra hết các nghĩa Nga: nhóm '
    'người, lớp học, và cả <b>ban nhạc</b> — tiếng Nga gọi ban nhạc là <b>гру́ппа</b>, '
    'không mượn chữ <i>band</i>.</div>'
    '<div class="hd-warn"><b>Bẫy chính tả:</b> viết HAI chữ <i>п</i> nhưng chỉ đọc một. '
    'Từ mượn giữ nguyên phụ âm đôi của bản gốc — <b>гру́ппа</b>, không phải <i>гру́па</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>группово́й</b> thuộc về nhóm, tập thể · <b>подгру́ппа</b> nhóm '
    'nhỏ, phân nhóm</div>'
)

S["карта"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — mượn qua Ba Lan/Đức từ Latin <i>charta</i> = '
    '<b>tờ giấy cói</b>. Cùng gốc với tiếng Anh <i>chart</i>, <i>card</i>, '
    '<i>carton</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc là TỜ GIẤY, rồi tách hai nhánh: tờ giấy vẽ mặt đất = bản '
    'đồ · tờ giấy in hình = quân bài, và ngày nay là thẻ ngân hàng.</div>'
    '<div class="hd-warn"><b>игра́ть в ка́рты</b> = chơi bài. Trò chơi thì '
    '<b>игра́ть в</b> + cách 4; còn nhạc cụ thì <b>игра́ть на</b> + cách 6.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ка́рточка</b> tấm thẻ nhỏ, phiếu · <b>карто́н</b> bìa cứng. '
    '⚠️ <b>карто́шка</b> (khoai tây) KHÔNG cùng gốc — nó mượn từ Đức <i>Kartoffel</i>.</div>'
)

S["герб"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — mượn qua tiếng Ba Lan <i>herb</i>, gốc là tiếng '
    'Đức cổ <i>erbe</i> = <b>di sản thừa kế</b> (nay là <i>Erbe</i>).</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Quốc huy đúng là "cái được thừa kế": dấu hiệu của một dòng họ hay '
    'một nhà nước, truyền đời này sang đời khác. Nó đứng chung bộ ba biểu tượng nhà nước '
    'với quốc kỳ và quốc ca.</div>'
    '<div class="hd-warn">⚠️ Mức tin: đoạn <i>herb ← erbe</i> là từ nguyên, không phải luật '
    'suy ra được — dùng để dễ nhớ thôi, đừng coi là quy tắc.</div>'
    '<div class="hd-why"><b>Bảng chia:</b> từ một âm tiết nên ở dạng gốc trọng âm không có '
    'chỗ nào khác để đứng; hễ thêm đuôi là nó nhảy hẳn ra đuôi và ở đó suốt cả bảng — '
    '<b>герба́</b>, <b>гербу́</b>, số nhiều <b>гербы́</b>.</div>'
)

S["круг"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">круг</span>'
    '<span class="hd-gloss">VÒNG, HÌNH TRÒN — gốc Slav trơn, không hậu tố</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>круг-</b> đẻ ra cả một họ chỉ nói chuyện "vòng": tròn, xung '
    'quanh, và vòng nhỏ. Trước hậu tố <i>-ок</i>, chữ <i>г</i> đổi thành <i>ж</i> — '
    '<b>кружо́к</b> (đúng phép biến âm г→ж).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кру́глый</b> tròn · <b>вокру́г</b> quanh, xung quanh · '
    '<b>круго́м</b> khắp xung quanh · <b>кружо́к</b> vòng nhỏ; câu lạc bộ</div>'
    '<div class="hd-why"><b>Bảng chia:</b> số ít trọng âm đứng yên ở <b>кру́г-</b>, sang số '
    'nhiều nó nhảy hết ra đuôi (<b>круги́</b>, <b>круго́в</b>). Riêng cách 6 có hai dạng: '
    '<i>о кру́ге</i> = nói VỀ vòng tròn, còn <i>в кругу́</i> = ở TRONG vòng — dạng '
    '<i>-у́</i> chỉ dùng sau в/на.</div>'
)

S["газ"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — một nhà hoá học thế kỷ 17 nặn ra từ này từ chữ Hy '
    'Lạp <i>chaos</i> (hỗn mang), để gọi thứ vật chất không có hình. Cùng gốc tiếng Anh '
    '<i>gas</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ba nghĩa nhưng cùng một hình ảnh "thứ khí chạy trong ống": chất khí '
    '→ khí đốt trong bếp → bàn đạp xăng (<i>нажа́ть на газ</i> = đạp ga).</div>'
    '<div class="hd-warn"><b>Đừng gộp với газе́та</b> (tờ báo) — nó mượn từ tiếng Ý '
    '<i>gazzetta</i>, tên một đồng xu ở Venice, chẳng liên quan gì tới chất khí.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>га́зовый</b> chạy bằng ga, thuộc chất khí · <b>газиро́вка</b> '
    'nước có ga · <b>газопрово́д</b> đường ống dẫn khí</div>'
)

S["алмаз"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — mượn qua các tiếng Turkic từ tiếng Ả Rập '
    '<i>al-mās</i>, gốc xa hơn là Hy Lạp <i>adamas</i> = <b>thứ không gì phá nổi</b>. '
    'Cùng nguồn với tiếng Anh <i>diamond</i> và <i>adamant</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhớ đúng nghĩa gốc "không gì phá nổi" là nhớ luôn công dụng: đá '
    'cứng nhất, nên người ta lấy nó làm mũi khoan và dao cắt kính.</div>'
    '<div class="hd-warn"><b>Tiếng Việt gọi chung là "kim cương", tiếng Nga tách đôi:</b> '
    '<b>алма́з</b> là viên THÔ, chưa mài (và kim cương dùng vào kỹ thuật); còn viên đã mài '
    'giác gắn lên nhẫn là <b>бриллиа́нт</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>алма́зный</b> bằng kim cương — <i>Алма́зный фонд</i> là kho báu '
    'quốc gia Nga trong điện Kremlin</div>'
)

S["деньги"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">деньг-</span>'
    '<span class="hd-gloss">де́ньга — tên một ĐỒNG XU Nga thời xưa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и</span>'
    '<span class="hd-gloss">đuôi số nhiều</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiền = <b>nhiều đồng xu</b>, nên từ này chỉ tồn tại ở số nhiều: '
    'không có dạng số ít, cũng không dùng nó để nói "một đồng tiền".</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>де́нежный</b> thuộc về tiền, bằng tiền · <b>де́нежки</b> tiền '
    'nong (thân mật, hơi đùa)</div>'
    '<div class="hd-why"><b>Bảng chia:</b> chỉ có nửa số nhiều, và nửa đó gãy làm đôi. Hai '
    'ô đầu giữ trọng âm ở đầu, chữ <i>ь</i> bật thành <i>е</i>: <b>де́ньги</b>, '
    '<b>де́нег</b>. Ba ô sau trọng âm nhảy ra đuôi: <b>деньга́м</b>, <b>деньга́ми</b>, '
    '<b>деньга́х</b>.</div>'
)

S["китайски"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кита́й-</span>'
    '<span class="hd-gloss">TRUNG QUỐC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ск-</span>'
    '<span class="hd-gloss">hậu tố "thuộc về, theo lối"</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и</span>'
    '<span class="hd-gloss">đuôi trạng từ của khuôn по-…-ски</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dạng này <b>không đứng một mình</b> — nó chỉ sống bên trong '
    '<b>по-кита́йски</b> = theo lối Trung Quốc, bằng tiếng Trung: '
    '<i>говори́ть по-кита́йски</i>.</div>'
    '<div class="hd-warn"><b>Cặp tính từ ↔ trạng từ, đúng khuôn ру́сский / по-ру́сски:</b> '
    'có chữ "tiếng" thì dùng tính từ — <i>кита́йский язы́к</i>; nói/viết/đọc bằng thứ tiếng '
    'đó thì dùng trạng từ — <i>по-кита́йски</i>, không kèm danh từ nào.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>Кита́й</b> Trung Quốc · <b>кита́ец</b> người TQ (nam) · '
    '<b>китая́нка</b> người TQ (nữ) · <b>кита́йский</b> thuộc Trung Quốc</div>'
)

S["край"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">край</span>'
    '<span class="hd-gloss">MÉP, RÌA NGOÀI CÙNG — gốc Slav trơn</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mọi nghĩa đều là "phần ngoài cùng": mép cốc, bờ vực, rồi rộng ra '
    'thành <b>vùng đất ở rìa</b> — và Nga lấy luôn chữ này đặt tên đơn vị hành chính lớn '
    '(<i>Краснода́рский край</i>).</div>'
    '<div class="hd-warn"><b>слу́шать кра́ем у́ха</b> = nghe bằng mép tai → nghe loáng '
    'thoáng, nghe qua loa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кра́йний</b> ngoài cùng, cuối cùng · <b>кра́йне</b> cực kỳ · '
    '<b>окра́ина</b> vùng ven, ngoại vi</div>'
    '<div class="hd-why"><b>Bảng chia:</b> số nhiều dồn trọng âm ra đuôi — <b>края́</b>, '
    '<b>краёв</b>. Và giống <b>круг</b>, cách 6 số ít có dạng riêng sau в/на: '
    '<i>в краю́</i> (ở nơi ấy) bên cạnh <i>о кра́е</i>.</div>'
)

S["прыжок"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">прыж-</span>'
    '<span class="hd-gloss">NHẢY — chính là gốc của <b>пры́гать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́к</span>'
    '<span class="hd-gloss">hậu tố: MỘT lần hành động</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Động từ <b>пры́гать</b> (nhảy) cộng hậu tố <i>-ок</i> ra danh từ '
    'chỉ MỘT cú nhảy. Trước hậu tố <i>-ок</i>, chữ <i>г</i> đổi thành <i>ж</i> — đúng phép '
    'biến âm г→ж cũng thấy ở <b>кружо́к</b> (từ <b>круг</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пры́гать</b> nhảy (đang, nhiều lần) · <b>пры́гнуть</b> nhảy một '
    'cái · <b>прыгу́н</b> vận động viên nhảy</div>'
    '<div class="hd-why"><b>Bảng chia:</b> chữ <b>о</b> trong <i>-о́к</i> là nguyên âm CHẠY '
    '— nó chỉ có ở dạng gốc <b>прыжо́к</b>, hễ thêm đuôi là rơi mất và trọng âm dời ra đuôi: '
    '<b>прыжка́</b>, <b>прыжку́</b>, <b>прыжко́м</b>, số nhiều <b>прыжки́</b>.</div>'
)


# ------------------------------------------------------------------ FIELD Vietnamese
# README §2c — dòng này là ĐỀ BÀI của deck 1-go, user gõ từ Nga từ nó.
# KHÔNG ghi từ loại/giống/thể (đã có badge), TRỪ từ có PoS = oth.
V["палка"]    = "cây gậy, thanh gỗ dài (gậy chống, gậy đánh)"
V["марка"]    = "con tem thư; nhãn hiệu, hãng (của xe, của hàng hoá)"
V["форма"]    = "hình dạng, khuôn; biểu mẫu; bộ đồng phục"
V["группа"]   = "nhóm (tập hợp người/vật cùng loại); ban nhạc"
V["круг"]     = "hình tròn, vòng tròn; một vòng (chạy/bơi một vòng)"
V["алмаз"]    = "kim cương thô, chưa mài giác"
V["деньги"]   = "tiền, tiền bạc (từ chỉ dùng ở số nhiều)"
V["край"]     = "mép, rìa, bờ ngoài cùng; vùng đất, miền"
V["прыжок"]   = "cú nhảy (một lần nhảy)"
# PoS = oth ⇒ badge vô dụng, phải ghi rõ từ loại. Và phải tách khỏi hai thẻ khác
# trong bộ sưu tập: по-кита́йски ("bằng tiếng Trung") và кита́йский (tính từ).
V["китайски"] = '(trạng từ) "bằng tiếng Trung" — gõ phần SAU dấu gạch nối, KHÔNG có по-'
