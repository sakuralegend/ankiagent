# -*- coding: utf-8 -*-
"""k94 — actions: 20 từ mới (đợt A1-A2 TRKI), chín cặp thể chung lô + держать(ся).

Không khối hệ thống. Chỗ cần nhất quán:
(1) hai động từ chuyển động MỘT CHIỀU (бежа́ть, везти́) nói cùng một khuôn với
    идти́/е́хать đã có trên thẻ; по- của побежа́ть/повезти́ là KHỞI SỰ, y như пое́хать (k80);
(2) по- của побыва́ть KHÔNG phải khởi sự — nói rõ ở thẻ đó;
(3) ba động từ HT có вы́- (вы́брать, вы́ключить, вы́ступить): trọng âm luôn nằm ở вы́ —
    mỗi thẻ nói một câu về chính từ đó, không lập bảng;
(4) верну́ть ↔ возвраща́ть: cặp thể KHÁC MẶT CHỮ, cùng một gốc sâu «quay» (верт/врат).
"""

S = {}

# -------------------------------------------------------- бежать
S["бежать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">беж- / бег-</span>'
    '<span class="hd-gloss">gốc CHẠY — <b>г</b> và <b>ж</b> là cùng một gốc (biến âm г → ж)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Là động từ chuyển động MỘT CHIỀU, y như <b>идти́</b>: đang chạy '
    'về một hướng ngay lúc này. Chạy lòng vòng, chạy hằng ngày là <b>бе́гать</b>. '
    'Cặp HT: <b>побежа́ть</b>.</div>'
    '<div class="hd-warn">Bảng chia trộn hai gốc — phải thuộc: <b>бегу́, бежи́шь, бежи́т, '
    'бежи́м, бежи́те, бегу́т</b>. Chỉ «tôi» và «họ» mang <b>г</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бе́гать</b> chạy (nhiều chiều) · <b>бег</b> môn chạy · '
    '<b>бегу́н</b> vận động viên chạy · <b>убежа́ть</b> chạy mất · <b>побе́г</b> cuộc trốn chạy</div>'
)

# -------------------------------------------------------- побежать
S["побежать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố KHỞI SỰ — bắt đầu, lên đường</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бежа́ть</span>'
    '<span class="hd-gloss">chạy (một chiều)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng khuôn với <b>пое́хать</b>, <b>пойти́</b>: <b>бежа́ть</b> là đang '
    'chạy, <b>побежа́ть</b> là vụt chạy đi, cất bước chạy. Bảng chia chép y <b>бежа́ть</b>, '
    'kể cả chỗ trộn gốc: <b>побегу́, побежи́шь, побегу́т</b>.</div>'
    '<div class="hd-warn"><b>Он побежа́л домо́й.</b> = Nó chạy vụt về nhà — nói lúc xuất phát, '
    'chưa chắc đã tới nơi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бежа́ть</b> đang chạy · <b>бе́гать</b> chạy (nhiều chiều) · '
    '<b>прибежа́ть</b> chạy tới nơi · <b>убежа́ть</b> chạy mất</div>'
)

# -------------------------------------------------------- бывать
S["бывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бы-</span>'
    '<span class="hd-gloss">gốc LÀ, Ở — chính là <b>быть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва-ть</span>'
    '<span class="hd-gloss">hậu tố LẶP LẠI: hay, thường, đôi khi</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>быть</b> là «ở, có» một lần; thêm <b>-ва-</b> thành «hay ở, '
    'thường có». Khác <b>быть</b>, nó chia đều: <b>быва́ю, быва́ешь</b>. '
    'Bản HT: <b>побыва́ть</b>.</div>'
    '<div class="hd-warn">Nơi chốn ở cách 6 vì gốc là «ở», không phải «đi»: '
    '<b>Я ча́сто быва́ю в Москве́.</b> — tôi hay có mặt ở Moskva.</div>'
    '<div class="hd-warn"><b>Быва́ет!</b> = Chuyện thường mà! · <b>Так не быва́ет.</b> '
    '= Làm gì có chuyện đó.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>быть</b> là, ở · <b>побыва́ть</b> từng đến · '
    '<b>забыва́ть</b> quên · <b>бы́вший</b> cựu, trước đây · <b>собы́тие</b> sự kiện</div>'
)

# -------------------------------------------------------- побывать
S["побывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">«một chuyến, một lúc» — ở đây KHÔNG phải «bắt đầu»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-быва́ть</span>'
    '<span class="hd-gloss">hay có mặt (gốc <b>быть</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Có mặt ở đó trọn một chuyến» ⇒ đã từng đến, đã ghé. Hay dùng '
    'nhất ở quá khứ để kể trải nghiệm: <b>Я побыва́л в Пари́же.</b> — tôi từng đến Paris. '
    'Chia đều: <b>побыва́ю, побыва́ешь</b>.</div>'
    '<div class="hd-warn">Nơi chốn ở CÁCH 6 (<b>в Пари́же</b>), không phải cách 4 như sau '
    'động từ đi lại — vì gốc là «ở», không phải «đi tới».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>быва́ть</b> hay có mặt · <b>быть</b> là, ở · '
    '<b>побы́ть</b> ở lại một lúc · <b>забы́ть</b> quên</div>'
)

# -------------------------------------------------------- везти
S["везти"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вез-</span>'
    '<span class="hd-gloss">gốc CHỞ (bằng xe) — đổi thành <b>воз-</b> trong <b>вози́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ти́</span>'
    '<span class="hd-gloss">đuôi nguyên thể có trọng âm, như <b>идти́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Động từ MỘT CHIỀU, y như <b>е́хать</b>: đang chở ai/cái gì tới một '
    'nơi. Chở đi chở lại nhiều lần là <b>вози́ть</b>. Hiện tại chia đều '
    '(<b>везу́, везёшь</b>), nhưng quá khứ giống đực mất <b>-л</b>: <b>вёз</b>, rồi '
    '<b>везла́, везли́</b>.</div>'
    '<div class="hd-warn">Nghĩa thứ hai, rất hay gặp: <b>Мне везёт.</b> = Tôi gặp may. '
    'Người gặp may ở CÁCH 3, động từ không đổi theo người.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вози́ть</b> chở (nhiều chiều) · <b>повезти́</b> chở đi; gặp may · '
    '<b>привезти́</b> chở tới, mang về · <b>везе́ние</b> vận may · '
    '<b>парово́з</b> đầu máy hơi nước</div>'
)

# -------------------------------------------------------- повезти
S["повезти"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố KHỞI SỰ — như <b>пое́хать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-везти́</span>'
    '<span class="hd-gloss">chở (một chiều); gặp may</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mang cả hai nghĩa của <b>везти́</b> sang thể HT: «chở đi, lên đường '
    'chở» và «đã gặp may». Quá khứ cũng mất <b>-л</b> như gốc: <b>повёз, повезла́</b>.</div>'
    '<div class="hd-warn"><b>Мне повезло́!</b> = Tôi may quá! · <b>Не повезло́.</b> = Xui rồi. '
    'Luôn ở dạng trung tính <b>-ло</b>, người gặp may ở cách 3.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>везти́</b> đang chở; gặp may · <b>вози́ть</b> chở (nhiều chiều) · '
    '<b>везе́ние</b> vận may · <b>привезти́</b> chở tới</div>'
)

# -------------------------------------------------------- вернуть
S["вернуть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вер-</span>'
    '<span class="hd-gloss">gốc QUAY, XOAY (gốc đầy đủ <b>верт-</b>, như <b>верте́ть</b> xoay)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ну-ть</span>'
    '<span class="hd-gloss">hậu tố «một lần, dứt điểm»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Quay ngược một cái» ⇒ trả lại, đưa về chỗ cũ, lấy lại. Chia: '
    '<b>верну́, вернёшь</b>. Trả CÁI GÌ ở cách 4, trả CHO AI ở cách 3: '
    '<b>верну́ть кни́гу дру́гу</b>.</div>'
    '<div class="hd-warn">Cặp CHT lệch mặt chữ, phải thuộc riêng: <b>верну́ть</b> ↔ '
    '<b>возвраща́ть</b>. Thêm <b>-ся</b> là chính mình quay về: <b>верну́ться</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>верну́ться</b> quay về · <b>возвраща́ть</b> trả lại (CHT) · '
    '<b>верте́ть</b> xoay · <b>поворо́т</b> khúc rẽ</div>'
)

# -------------------------------------------------------- вернуться
S["вернуться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">верну́ть</span>'
    '<span class="hd-gloss">đưa về chỗ cũ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">chính mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đưa CHÍNH MÌNH về chỗ cũ ⇒ trở về, quay lại. Về ĐÂU: '
    '<b>в/на</b> + cách 4; từ ĐÂU: <b>из/с</b> + cách 2. Cặp CHT: <b>возвраща́ться</b>.</div>'
    '<div class="hd-warn"><b>Я ско́ро верну́сь.</b> = Tôi sẽ quay lại ngay.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>верну́ть</b> trả lại · <b>возвраща́ться</b> trở về (CHT) · '
    '<b>возвраще́ние</b> sự trở về</div>'
)

# -------------------------------------------------------- возвращать
S["возвращать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">воз-</span>'
    '<span class="hd-gloss">ở đây: NGƯỢC lại, về</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вращ-</span>'
    '<span class="hd-gloss">QUAY (gốc <i>врат</i>, <b>т → щ</b>) — như <b>враща́ть</b> xoay tròn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>возвраща́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Quay ngược về» ⇒ trả lại, mang về. Vật ở cách 4, người nhận ở '
    'cách 3. Gốc <i>врат</i> là dạng sách vở của <i>ворот</i> (quay), nên cùng gốc sâu với '
    '<b>верну́ть</b> và <b>поворо́т</b>.</div>'
    '<div class="hd-warn">Cặp HT dùng hằng ngày là <b>верну́ть</b>, không phải '
    '<b>возврати́ть</b> (có, nhưng trang trọng).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>возвраща́ться</b> trở về · <b>возвра́т</b> sự hoàn trả · '
    '<b>враща́ть</b> xoay tròn · <b>верну́ть</b> trả lại (HT)</div>'
)

# -------------------------------------------------------- возвращаться
S["возвращаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">возвраща́ть</span>'
    '<span class="hd-gloss">quay ngược về, mang về</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">chính mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mang CHÍNH MÌNH về ⇒ trở về, quay lại. Thể CHT: đang trên đường '
    'về, hoặc về thường xuyên. Cặp HT: <b>верну́ться</b>.</div>'
    '<div class="hd-warn">Về nhà là <b>домо́й</b> (hướng tới), không phải <b>до́ма</b> (ở nhà): '
    '<b>Я возвраща́юсь домо́й.</b> — tôi đang về nhà.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>возвраща́ть</b> trả lại · <b>возвраще́ние</b> sự trở về · '
    '<b>верну́ться</b> quay về (HT)</div>'
)

# -------------------------------------------------------- включать
S["включать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO trong</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ключ-</span>'
    '<span class="hd-gloss">chính là <b>ключ</b> — chìa khoá</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>включа́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tra VÀO như tra chìa vào ổ ⇒ bật máy lên; đưa VÀO một tập hợp ⇒ '
    'bao gồm. Đảo <b>в-</b> thành <b>вы-</b> (ra) là được nghĩa ngược: <b>выключа́ть</b> tắt. '
    'Cặp HT: <b>включи́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ключ</b> chìa khoá · <b>выключа́ть</b> tắt · '
    '<b>выключа́тель</b> công tắc · <b>включа́я</b> kể cả, bao gồm cả</div>'
)

# -------------------------------------------------------- включить
S["включить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO trong</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ключ-</span>'
    '<span class="hd-gloss">chìa khoá (<b>ключ</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-ть</span>'
    '<span class="hd-gloss">đuôi HT lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tra vào ⇒ bật lên một lần cho xong (<b>включи́ свет</b> — bật đèn đi); '
    'hoặc đưa vào danh sách: <b>включи́ть в</b> + cách 4. Cặp CHT: <b>включа́ть</b>.</div>'
    '<div class="hd-warn">Trọng âm nằm ở ĐUÔI suốt cả bảng: <b>включу́, включи́шь, '
    'включи́т</b>. Nói <i>вклю́чит</i> là lỗi người Nga hay bắt bẻ nhất.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ключ</b> chìa khoá · <b>вы́ключить</b> tắt · '
    '<b>выключа́тель</b> công tắc</div>'
)

# -------------------------------------------------------- выключать
S["выключать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span>'
    '<span class="hd-gloss">RA ngoài</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ключ-</span>'
    '<span class="hd-gloss">chìa khoá (<b>ключ</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>выключа́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Rút chìa RA ⇒ tắt, ngắt. Đối xứng hoàn toàn với <b>включа́ть</b> '
    '(bật): chỉ đổi <b>в-</b> ↔ <b>вы-</b>. Thể CHT mang trọng âm ở đuôi <b>-а́ть</b>; '
    'cặp HT <b>вы́ключить</b> thì dồn hết về <b>вы́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>включа́ть</b> bật · <b>выключа́тель</b> công tắc · '
    '<b>ключ</b> chìa khoá</div>'
)

# -------------------------------------------------------- выключить
S["выключить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы́-</span>'
    '<span class="hd-gloss">RA ngoài — mang trọng âm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ключ-и-ть</span>'
    '<span class="hd-gloss">chìa khoá + đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Rút chìa ra một lần cho xong ⇒ tắt hẳn: <b>Вы́ключи телеви́зор!</b> '
    '— Tắt ti vi đi! Cặp CHT: <b>выключа́ть</b>.</div>'
    '<div class="hd-warn">Động từ HT có <b>вы́-</b> thì trọng âm đứng ở <b>вы́</b> trong MỌI '
    'dạng: <b>вы́ключу, вы́ключишь, вы́ключил</b> — khác hẳn <b>включу́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>включи́ть</b> bật · <b>выключа́тель</b> công tắc · '
    '<b>ключ</b> chìa khoá</div>'
)

# -------------------------------------------------------- выбирать
S["выбирать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span>'
    '<span class="hd-gloss">RA ngoài</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бир-</span>'
    '<span class="hd-gloss">gốc LẤY — cùng gốc <b>брать</b> (<b>бр/бир/бер</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>выбира́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">LẤY RA một cái từ cả đống ⇒ chọn; chọn người ⇒ bầu. Mẫu '
    '<b>-бира́ть</b> (CHT) ↔ <b>-бра́ть</b> (HT) lặp lại ở <b>собира́ть / собра́ть</b>. '
    'Cặp HT: <b>вы́брать</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>брать</b> lấy · <b>вы́бор</b> sự lựa chọn · '
    '<b>вы́боры</b> cuộc bầu cử · <b>собира́ть</b> gom, thu thập</div>'
)

# -------------------------------------------------------- выбрать
S["выбрать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы́-</span>'
    '<span class="hd-gloss">RA ngoài — mang trọng âm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-брать</span>'
    '<span class="hd-gloss">LẤY — chính là <b>брать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Lấy ra một cái cho xong ⇒ chọn được, bầu được. Thân tương lai lấy '
    'y từ <b>беру́</b> của <b>брать</b>: <b>вы́беру, вы́берешь, вы́берут</b> — trọng âm '
    'luôn ở <b>вы́</b>. Cặp CHT: <b>выбира́ть</b>.</div>'
    '<div class="hd-warn">Bầu ai LÀM gì: chức vụ ở CÁCH 5 — '
    '<b>Его́ вы́брали президе́нтом.</b> Người ta bầu ông ấy làm tổng thống.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>брать</b> lấy · <b>вы́бор</b> sự lựa chọn · '
    '<b>вы́боры</b> cuộc bầu cử · <b>собра́ть</b> gom lại</div>'
)

# -------------------------------------------------------- выступать
S["выступать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span>'
    '<span class="hd-gloss">RA ngoài, ra trước</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ступ-</span>'
    '<span class="hd-gloss">gốc BƯỚC — như <b>ступе́нька</b> bậc thang</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>выступа́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">BƯỚC RA trước mọi người ⇒ lên sân khấu biểu diễn, lên bục phát biểu, '
    'đứng ra bày tỏ lập trường. Cặp HT: <b>вы́ступить</b>.</div>'
    '<div class="hd-warn">Ủng hộ / phản đối: <b>выступа́ть за</b> + cách 4 · '
    '<b>выступа́ть про́тив</b> + cách 2.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>выступле́ние</b> bài phát biểu, tiết mục · '
    '<b>поступа́ть</b> vào (trường); hành xử · <b>ступе́нька</b> bậc thang</div>'
)

# -------------------------------------------------------- выступить
S["выступить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы́-</span>'
    '<span class="hd-gloss">RA ngoài — mang trọng âm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ступ-и-ть</span>'
    '<span class="hd-gloss">BƯỚC + đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bước ra một lần, trọn một tiết mục hay một bài nói: '
    '<b>вы́ступить на конфере́нции</b> — phát biểu ở hội nghị. Cặp CHT: <b>выступа́ть</b>.</div>'
    '<div class="hd-warn">Ngôi «tôi» chèn <b>л</b> sau <b>п</b>: <b>вы́ступлю</b>, nhưng '
    '<b>вы́ступишь, вы́ступят</b>. Trọng âm luôn ở <b>вы́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>выступле́ние</b> bài phát biểu, tiết mục · '
    '<b>поступи́ть</b> vào (trường) · <b>ступе́нька</b> bậc thang</div>'
)

# -------------------------------------------------------- держать
S["держать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">держ-</span>'
    '<span class="hd-gloss">gốc GIỮ, CẦM</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể — nhưng chia theo lớp THỨ HAI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cầm trong tay, giữ ở một chỗ, giữ đúng (<b>держа́ть сло́во</b> giữ lời).</div>'
    '<div class="hd-warn">Đuôi <b>-ать</b> mà KHÔNG chia <i>-аю</i>: <b>держу́, де́ржишь, '
    'де́ржит, де́ржат</b> — trọng âm lùi về gốc từ ngôi thứ hai.</div>'
    '<div class="hd-warn"><b>Держи́!</b> = Cầm lấy! (khi đưa đồ cho ai).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>держа́ться</b> bám vào · <b>поддержа́ть</b> ủng hộ, đỡ · '
    '<b>подде́ржка</b> sự ủng hộ · <b>содержа́ние</b> nội dung (cái được giữ bên trong)</div>'
)

# -------------------------------------------------------- держаться
S["держаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">держа́ть</span>'
    '<span class="hd-gloss">giữ, cầm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">chính mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giữ CHÍNH MÌNH: bám vào cho khỏi ngã, giữ mình đứng vững, giữ một '
    'phong thái (cư xử). Chia như <b>держа́ть</b>: <b>держу́сь, де́ржишься</b>.</div>'
    '<div class="hd-warn">Bám vào CÁI GÌ: <b>за</b> + cách 4 — '
    '<b>Держи́тесь за по́ручни.</b> Hãy bám vào tay vịn.</div>'
    '<div class="hd-warn"><b>Держи́сь!</b> = Cố lên! Trụ vững nhé! — lời động viên rất hay gặp.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>держа́ть</b> cầm, giữ · <b>поддержа́ть</b> ủng hộ · '
    '<b>подде́ржка</b> sự ủng hộ</div>'
)

V = {
    # Thêm nghĩa MỘT CHIỀU theo khuôn идти́ «đi bộ, đang đi tới»; "trốn chạy" -> "chạy trốn".
    "бежать": "chạy, đang chạy tới, chạy trốn",
    # Bỏ "ghé qua" (trùng приходить, k80). Thêm "có mặt" (to be at a place), "thường đến" (to frequent).
    "бывать": "hay có mặt, thường đến, hay xảy ra",
    # Bỏ ngoặc "(một nơi nào đó)"; thêm "ở lại một thời gian" (to spend some time).
    "побывать": "từng đến, ghé thăm, ở lại một thời gian",
    # Một chiều theo khuôn е́хать «đi xe, đang đi tới bằng xe»; bỏ "chở" trơn (sẽ là của возить);
    # bỏ "vận may" (danh từ, không phải nghĩa của động từ).
    "везти": "chở bằng xe, đang chở tới, gặp may",
    # Thiếu hẳn nghĩa chở (to take / transport); "may mắn" là tính/danh từ -> bỏ.
    "повезти": "chở đi, bắt đầu chở, gặp may",
    # Cặp thể: cho đủ cùng một bộ nghĩa, chỉ badge thể tách hai vế.
    "вернуть": "trả lại, hoàn trả, mang về, lấy lại",
    "возвращать": "trả lại, hoàn trả, mang về, lấy lại",
    # Bỏ ngoặc "(thiết bị)".
    "включать": "bật, bao gồm, đưa vào",
    # Bỏ "mở" (trùng открыть, k87) và ngoặc.
    "включить": "bật, đưa vào, thêm vào",
    # Thiếu nghĩa "to elect / vote for".
    "выбирать": "chọn, lựa chọn, bầu",
    "выбрать": "chọn, lựa chọn, bầu",
    # Bỏ ngoặc "(điện, thiết bị)"; cho khớp cặp выключать.
    "выключить": "tắt, ngắt",
    # "cố gắng" là nghĩa nới rộng từ câu Держи́сь!; thiếu "to behave".
    "держаться": "bám vào, giữ lấy, cư xử, trụ vững",
}
