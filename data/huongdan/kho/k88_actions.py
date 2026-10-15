# -*- coding: utf-8 -*-
"""k88 — actions: 18 từ mới user vừa thêm (đợt A1 TRKI), soạn từng thẻ độc lập.

Không khối hệ thống. Chỗ cần nhất quán:
(1) ba cặp thể chung lô (посла́ть/посыла́ть, продо́лжить(ся)/продолжа́ть(ся),
    сфотографи́ровать/фотографи́ровать) — mỗi vế nói phần của nó, không chép nhau;
(2) bốn vế про-долж- : người làm thì không -ся, việc tự diễn thì -ся — trải ở
    продолжа́ться, hai thẻ kia dẫn chiếu;
(3) năm thẻ HT của thẻ cũ (постро́ить, почу́вствовать, продо́лжить, реши́ть, запо́мнить)
    khớp khuôn chẻ đã có ở k85: стро- XÂY, чу́вств-, -долж- DÀI, реш- GỠ, за- + -помн-.
"""

S = {}

# -------------------------------------------------------- внимательный
S["внимательный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO trong</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ним-</span>'
    '<span class="hd-gloss">gốc LẤY, NHẬN — như trong <b>понима́ть</b>, <b>принима́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́тельный</span>'
    '<span class="hd-gloss">đuôi tính từ "có tính hay…"</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thu nhận mọi thứ VÀO đầu ⇒ chăm chú, để ý. Là tính từ của '
    '<b>внима́ние</b> (sự chú ý). Dạng ngắn giống đực chèn <b>е</b>: <b>внима́телен</b>; '
    'các dạng kia giữ nguyên: <b>внима́тельна, внима́тельны</b>.</div>'
    '<div class="hd-warn">Trạng từ <b>внима́тельно</b> = chăm chú, kỹ: '
    '<b>Слу́шайте внима́тельно!</b> Hãy nghe kỹ!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>внима́ние</b> sự chú ý · <b>внима́тельно</b> chăm chú · '
    '<b>невнима́тельный</b> lơ đễnh</div>'
)

# -------------------------------------------------------- запомнить
S["запомнить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">ghim lại cho chắc — như <b>записа́ть</b> ghi lại</span></div>'
    '<div class="hd-row"><span class="hd-piece">-по́мн-</span>'
    '<span class="hd-gloss">NHỚ — chính là <b>по́мнить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ghim một lần vào trí nhớ cho xong — từ đó trở đi là <b>по́мнить</b>. '
    'Cặp thể: <b>запомина́ть</b> (thẻ đó phân biệt ba từ một gốc). Chia đều: '
    '<b>запо́мню, запо́мнишь</b>.</div>'
    '<div class="hd-warn">Mệnh lệnh <b>Запо́мни!</b> / <b>Запо́мните!</b> = Nhớ lấy! Nhớ kỹ nhé!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>по́мнить</b> còn nhớ · <b>запомина́ть</b> ghi nhớ (CHT) · '
    '<b>вспо́мнить</b> nhớ lại · <b>па́мять</b> trí nhớ</div>'
)

# -------------------------------------------------------- послать
S["послать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố, ở đây KHÔNG mang nghĩa riêng tách ra được</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сла-</span>'
    '<span class="hd-gloss">gốc GỬI — trong bảng chia hiện ra dạng <b>шл-</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thân tương lai không suy được từ nguyên thể, phải thuộc: '
    '<b>пошлю́, пошлёшь … пошлю́т</b> (<b>сл</b> thành <b>шл</b>, <b>а</b> rơi). '
    'Quá khứ thì đều: <b>посла́л</b>. Cặp thể: <b>посыла́ть</b>.</div>'
    '<div class="hd-warn"><b>Посла́ть</b> một NGƯỜI trống không, không nói gửi đi làm gì '
    '(<i>Он меня́ посла́л</i>) = bảo cút đi, chửi — nghĩa tục, tránh dùng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>посыла́ть</b> gửi (CHT) · <b>посо́л</b> đại sứ (người được gửi đi; '
    '<b>посла́</b>) · <b>посо́льство</b> đại sứ quán · <b>посы́лка</b> bưu kiện</div>'
)

# -------------------------------------------------------- посылать
S["посылать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">giữ lại từ <b>посла́ть</b>, không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сыл-</span>'
    '<span class="hd-gloss">gốc GỬI — cùng gốc <b>сл-</b>, chèn thêm <b>ы</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gửi nhiều lần, hay đang gửi. Bảng chia đều tăm tắp: <b>посыла́ю, '
    'посыла́ешь</b> — dễ hơn hẳn cặp thể <b>посла́ть</b> (<b>пошлю́</b>). Người nhận ở cách 3: '
    '<i>посыла́ть ма́ме письмо́</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>посла́ть</b> gửi (HT) · <b>посы́лка</b> bưu kiện · '
    '<b>посо́л</b> đại sứ</div>'
)

# -------------------------------------------------------- построить
S["построить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">chỉ đánh dấu XONG, không thêm nghĩa</span></div>'
    '<div class="hd-row"><span class="hd-piece">стро-</span>'
    '<span class="hd-gloss">gốc XÂY, DỰNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp thể hoàn thành của <b>стро́ить</b>: xây cho tới khi xong. '
    'Chia đều: <b>постро́ю, постро́ишь</b>.</div>'
    '<div class="hd-warn">"Ngôi nhà được xây năm…" người Nga nói bằng ngôi 3 số nhiều, không '
    'chủ ngữ: <b>Дом постро́или в 1900 году́.</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>стро́ить</b> xây (CHT) · <b>строи́тель</b> thợ xây · '
    '<b>строи́тельный</b> thuộc xây dựng · <b>стро́йка</b> công trường</div>'
)

# -------------------------------------------------------- почувствовать
S["почувствовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">chỉ đánh dấu XONG / chợt bắt đầu</span></div>'
    '<div class="hd-row"><span class="hd-piece">чу́вств-</span>'
    '<span class="hd-gloss">chính là <b>чу́вство</b> — cảm giác</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-ть</span>'
    '<span class="hd-gloss">đuôi biến danh từ thành động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp thể của <b>чу́вствовать</b>: khoảnh khắc CHỢT cảm thấy — '
    '<i>Я почу́вствовал боль.</i> <b>-ова-</b> chia thành <b>-у-</b>: <b>почу́вствую</b>. '
    'Chữ <b>в</b> đầu không đọc, như ở thẻ <b>чу́вствовать</b>.</div>'
    '<div class="hd-warn">Thấy trong người ra sao thì có <b>себя́</b>: '
    '<b>Я почу́вствовал себя́ лу́чше.</b> Tôi thấy khoẻ hơn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>чу́вствовать</b> cảm thấy (CHT) · <b>чу́вство</b> cảm giác, tình cảm · '
    '<b>чувстви́тельный</b> nhạy cảm</div>'
)

# -------------------------------------------------------- продолжаться
S["продолжаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">продолжа́-ть</span>'
    '<span class="hd-gloss">tiếp tục — <b>про-</b> kéo tới + <b>-долж-</b> DÀI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">việc TỰ nó, không có người tác động</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chủ ngữ là SỰ VIỆC, không phải người: <b>Фильм продолжа́ется '
    'два часа́.</b> Phim kéo dài hai tiếng. Cặp thể: <b>продо́лжиться</b>.</div>'
    '<div class="hd-warn">Người tiếp tục làm → <b>продолжа́ть</b> / <b>продо́лжить</b>. '
    'Việc tự tiếp diễn → thêm <b>-ся</b>: <i>Я продолжа́ю рабо́ту</i> nhưng '
    '<i>Рабо́та продолжа́ется</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>продолжа́ть</b> tiếp tục · <b>продолже́ние</b> phần tiếp theo '
    '(<b>Продолже́ние сле́дует</b> còn tiếp) · <b>до́лгий</b> lâu, dài</div>'
)

# -------------------------------------------------------- продолжить
S["продолжить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">kéo tiếp về phía trước</span></div>'
    '<div class="hd-row"><span class="hd-piece">-до́лж-</span>'
    '<span class="hd-gloss">gốc DÀI — của <b>до́лгий</b>, <b>г</b> hoá <b>ж</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi thể hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp thể của <b>продолжа́ть</b> — trọng âm lùi lên <b>-до́л-</b> và '
    'đứng yên ở đó: <b>продо́лжу, продо́лжишь</b>.</div>'
    '<div class="hd-warn">Thường đi với DANH TỪ: <b>продо́лжить разгово́р</b> (tiếp tục câu '
    'chuyện). Tiếp tục LÀM gì (+ nguyên thể) thì quen dùng <b>продолжа́ть</b>: '
    '<i>продолжа́ть чита́ть</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>продолжа́ть</b> tiếp tục (CHT) · <b>продо́лжиться</b> tự tiếp diễn · '
    '<b>продолже́ние</b> phần tiếp theo</div>'
)

# -------------------------------------------------------- продолжиться
S["продолжиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">продо́лжи-ть</span>'
    '<span class="hd-gloss">tiếp tục (HT) — <b>про-</b> + <b>-долж-</b> DÀI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">việc TỰ nó tiếp diễn</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hay gặp nhất ở thì tương lai, nói việc SẼ tiếp diễn sau một quãng '
    'ngắt: <b>Уро́к продо́лжится по́сле переры́ва.</b> Buổi học sẽ tiếp tục sau giờ nghỉ. '
    'Ai làm / việc tự diễn: xem thẻ <b>продолжа́ться</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>продолжа́ться</b> kéo dài (CHT) · <b>продо́лжить</b> tiếp tục · '
    '<b>продолже́ние</b> phần tiếp theo</div>'
)

# -------------------------------------------------------- рад
S["рад"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn <b>рад-</b> VUI, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỉ có DẠNG NGẮN, không có dạng dài ⇒ luôn đứng sau chủ ngữ: '
    '<b>Я рад</b> (nam) · <b>Я ра́да</b> (nữ) · <b>Мы ра́ды</b>.</div>'
    '<div class="hd-warn">Vui VÌ ai/cái gì → cách 3: <b>Я рад тебе́.</b> Vui được làm gì → '
    'nguyên thể: <b>Рад вас ви́деть!</b> Rất vui được gặp anh/chị!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ра́дость</b> niềm vui · <b>ра́доваться</b> vui mừng · '
    '<b>ра́достный</b> hân hoan</div>'
)

# -------------------------------------------------------- решить
S["решить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">реш-</span>'
    '<span class="hd-gloss">gốc GỠ, CỞI nút (xem mức tin ở thẻ <b>реша́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp thể của <b>реша́ть</b>: gỡ xong nút thắt. + danh từ = giải xong '
    '(<i>реши́ть зада́чу</i>); + nguyên thể = quyết làm gì (<i>Я реши́л оста́ться</i>). '
    'Trọng âm ở đuôi: <b>решу́, реши́шь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>реша́ть</b> giải, quyết định (CHT) · <b>реше́ние</b> lời giải, '
    'quyết định · <b>разреша́ть</b> cho phép</div>'
)

# -------------------------------------------------------- смелый
S["смелый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сме-</span>'
    '<span class="hd-gloss">gốc DÁM — của <b>сметь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-л-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người DÁM làm ⇒ dũng cảm. Dạng ngắn: chỉ giống cái nhảy trọng âm '
    'xuống đuôi — <b>смела́</b>; còn lại giữ ở gốc: <b>смел, сме́ло, сме́лы</b>. '
    'Trạng từ <b>сме́ло</b> = mạnh dạn: <i>Говори́ сме́ло!</i></div>'
    '<div class="hd-warn">⚠️ Mức tin: nối với <b>сметь</b> là từ nguyên, không phải luật suy ra '
    'được. Còn <b>смея́ться</b> (cười) chỉ trùng mặt chữ, KHÔNG cùng họ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сметь</b> dám · <b>сме́ло</b> mạnh dạn · '
    '<b>сме́лость</b> lòng dũng cảm</div>'
)

# -------------------------------------------------------- согласный
S["согласный"] = (
    '<div class="hd-why">Hay dùng nhất là DẠNG NGẮN: <b>Я согла́сен</b> · nữ <b>Я согла́сна</b> · '
    '<b>Мы согла́сны</b> — tôi đồng ý.</div>'
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">CÙNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-глас-</span>'
    '<span class="hd-gloss">TIẾNG NÓI — dạng cổ của <b>го́лос</b> (giọng)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ный</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">CÙNG một tiếng nói ⇒ đồng ý. Dạng ngắn giống đực chèn <b>е</b> '
    '(<b>согла́сен</b>), các dạng kia thì không.</div>'
    '<div class="hd-warn">Đồng ý VỚI ai → <b>с</b> + cách 5: <b>Я согла́сен с тобо́й.</b> '
    'Đồng ý NHẬN cái gì → <b>на</b> + cách 4: <i>Я согла́сна на всё.</i></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>соглаша́ться</b> đồng ý · <b>согла́сие</b> sự đồng ý · '
    '<b>го́лос</b> giọng, phiếu bầu</div>'
)

# -------------------------------------------------------- спокойный
S["спокойный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">tiền tố, nghĩa đã mờ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-поко́й-</span>'
    '<span class="hd-gloss">chính là <b>поко́й</b> — sự yên, sự nghỉ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ный</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Có <b>поко́й</b> ⇒ bình tĩnh, yên ả. Dạng ngắn giống đực đổi <b>й</b> '
    'thành <b>е</b>: <b>споко́ен</b>; các dạng kia giữ <b>й</b>: <b>споко́йна, споко́йны</b>.</div>'
    '<div class="hd-warn">Câu chúc phải thuộc, ở cách 2: <b>Споко́йной но́чи!</b> Chúc ngủ ngon!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>споко́йно</b> bình tĩnh · <b>беспоко́иться</b> lo lắng (không yên) · '
    '<b>успоко́иться</b> bình tĩnh lại</div>'
)

# -------------------------------------------------------- сфотографировать
S["сфотографировать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">chỉ đánh dấu XONG, không thêm nghĩa</span></div>'
    '<div class="hd-row"><span class="hd-piece">фотограф-</span>'
    '<span class="hd-gloss">mượn, = <i>photograph</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ровать</span>'
    '<span class="hd-gloss">đuôi biến từ mượn thành động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chụp xong một tấm. Thứ được chụp ở cách 4: '
    '<b>Сфотографи́руй меня́!</b> Chụp ảnh tôi đi! Chia: <b>сфотографи́рую</b>.</div>'
    '<div class="hd-warn">Chụp NGƯỜI KHÁC/vật → không <b>-ся</b>. Mình đứng cho người ta chụp → '
    '<b>фотографи́роваться</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>фотографи́ровать</b> chụp (CHT) · <b>фотогра́фия</b> bức ảnh · '
    '<b>фото́граф</b> thợ ảnh</div>'
)

# -------------------------------------------------------- фотографировать
S["фотографировать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">фотограф-</span>'
    '<span class="hd-gloss">mượn, = <i>photograph</i> (ánh sáng + viết)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ровать</span>'
    '<span class="hd-gloss">đuôi biến từ mượn thành động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi <b>-и́ровать</b> khi chia đổi <b>-ова-</b> thành <b>-у-</b>: '
    '<b>фотографи́рую, фотографи́руешь</b>. Trọng âm đứng yên trên <b>-и́-</b>. '
    'Cặp thể: <b>сфотографи́ровать</b>.</div>'
    '<div class="hd-warn">Biển hay gặp: <b>Фотографи́ровать нельзя́!</b> Cấm chụp ảnh!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>фотогра́фия</b> bức ảnh · <b>фото́граф</b> thợ ảnh · '
    '<b>фотографи́роваться</b> chụp ảnh mình</div>'
)

# -------------------------------------------------------- характер
S["характер"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn (gốc Hy Lạp), không chẻ được — chính là <i>character</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trọng âm ở âm tiết hai: <b>хара́ктер</b>. Ai có tính gì → <b>у</b> + '
    'cách 2: <b>У неё лёгкий хара́ктер.</b> Cô ấy dễ tính.</div>'
    '<div class="hd-warn">"Nhân vật" trong phim, truyện KHÔNG phải <b>хара́ктер</b> mà là '
    '<b>персона́ж</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>характе́рный</b> đặc trưng (trọng âm dịch sang <b>-те́-</b>)</div>'
)

# -------------------------------------------------------- юмор
S["юмор"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>humor</i>, chỉ cần nhớ trọng âm ở đầu: <b>ю́мор</b>.</div>'
    '<div class="hd-warn">Cụm phải thuộc: <b>чу́вство ю́мора</b> = khiếu hài hước '
    '(<b>ю́мор</b> ở cách 2). <i>У него́ хоро́шее чу́вство ю́мора.</i></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>юмори́ст</b> người viết/diễn hài · <b>юмористи́ческий</b> hài hước</div>'
)


V = {
    # Thiếu hẳn nghĩa chính "attentive" (chăm chú) — tiếng Anh xếp nó đầu tiên.
    "внимательный": "chăm chú, chu đáo, cẩn thận, ân cần",
    # Rút gọn: "nhớ" trùng помнить (k48), "học thuộc" trùng выучить (k59, cùng HT).
    "запомнить": "ghi nhớ",
    # "làm" là nghĩa nới rộng, tiếng Anh không có; "dựng lên" = erect.
    "построить": "xây dựng, dựng lên",
}
