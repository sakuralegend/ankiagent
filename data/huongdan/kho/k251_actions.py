# -*- coding: utf-8 -*-
"""k251 — actions: cặp tiền tố chuyển động (под-/вы-/про-), họ лить, тереть, класть/-лож-."""

S = {}

S["ремонтировать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ремонт-</span><span class="hd-gloss">SỬA — <b>ремо́нт</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́рова-ть</span><span class="hd-gloss">đuôi động từ mượn; khi chia <i>-ова-</i> → <i>-у-</i>: <b>ремонти́рую</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm việc <b>ремо́нт</b> ⇒ sửa máy móc, sửa sang nhà cửa. Sửa cái gì để cách 4: <b>ремонти́ровать кварти́ру</b>. Cặp HT: <b>отремонти́ровать</b>.</div>'
    '<div class="hd-warn"><b>чини́ть</b> chỉ làm cho món đồ hết hỏng; <b>ремонти́ровать</b> bao cả sửa lớn và tân trang nhà cửa, đường sá.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отремонти́ровать</b> (HT) · <b>ремо́нт</b> việc sửa chữa · <b>ремо́нтник</b> thợ sửa</div>'
)

S["перекладывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пере-</span><span class="hd-gloss">SANG chỗ khác</span></div>'
    '<div class="hd-row"><span class="hd-piece">-клад-</span><span class="hd-gloss">ĐẶT — gốc của <b>класть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-ть</span><span class="hd-gloss">thể chưa hoàn thành, chia đều: <b>перекла́дываю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đặt sang» chỗ khác ⇒ chuyển, dời đồ. Cặp HT <b>переложи́ть</b> dùng gốc <b>-лож-</b>, y như cặp <b>класть</b> / <b>положи́ть</b>.</div>'
    '<div class="hd-warn">Đặt gánh nặng SANG người khác ⇒ đùn đẩy: <b>на</b> + cách 4 — <b>перекла́дывать отве́тственность на други́х</b> đùn trách nhiệm cho người khác.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>переложи́ть</b> (HT) · <b>класть</b> đặt · <b>скла́дывать</b> xếp, gấp · <b>откла́дывать</b> hoãn, để dành</div>'
)

S["переложить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пере-</span><span class="hd-gloss">SANG chỗ khác</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лож-</span><span class="hd-gloss">gốc NẰM — làm cho NẰM ⇒ đặt, như <b>положи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span><span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đặt sang» ⇒ chuyển, dời. Từ đâu: <b>из</b> + cách 2; sang đâu: <b>в / на</b> + cách 4 — <b>переложи́ть ве́щи из су́мки в чемода́н</b>. Cặp CHT khác gốc: <b>перекла́дывать</b>.</div>'
    '<div class="hd-warn">Trọng âm lùi sau «tôi», như <b>положи́ть</b>: <b>переложу́</b>, nhưng <b>перело́жишь, перело́жат</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>перекла́дывать</b> (CHT) · <b>положи́ть</b> đặt · <b>отложи́ть</b> hoãn · <b>сложи́ть</b> xếp, cộng</div>'
)

S["подбегать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span><span class="hd-gloss">SÁT LẠI GẦN — như <b>подойти́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-бег-а́ть</span><span class="hd-gloss">CHẠY — khuôn của <b>бе́гать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chạy tới sát bên. Tiền tố + <b>-бега́ть</b> = CHT, tiền tố + <b>-бежа́ть</b> = HT (<b>подбежа́ть</b>). Chia đều, trọng âm nhảy sang đuôi: <b>бе́гать</b> nhưng <b>подбега́ю</b>.</div>'
    '<div class="hd-warn">Chạy lại gần CÁI GÌ, AI: <b>к</b> + cách 3 — <b>подбега́ть к окну́</b>, <b>подбега́ть к ма́ме</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>подбежа́ть</b> (HT) · <b>бе́гать</b> chạy (nhiều chiều) · <b>убега́ть</b> bỏ chạy · <b>подходи́ть</b> lại gần</div>'
)

S["подбежать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span><span class="hd-gloss">SÁT LẠI GẦN — như <b>подойти́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-беж-а́ть</span><span class="hd-gloss">CHẠY — chính là <b>бежа́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chạy tới sát bên, xong một lượt. Chia y hệt <b>бежа́ть</b>, chỉ «tôi» và «họ» mang <b>г</b>: <b>подбегу́, подбежи́шь, подбегу́т</b>; sai khiến <b>подбеги́</b>. Cặp CHT: <b>подбега́ть</b>.</div>'
    '<div class="hd-warn"><b>подбежа́ть к</b> + cách 3 = chạy lại GẦN, tới sát bên; <b>прибежа́ть</b> = chạy và đã TỚI NƠI.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>подбега́ть</b> (CHT) · <b>бежа́ть</b> chạy · <b>прибежа́ть</b> chạy đến · <b>подойти́</b> lại gần</div>'
)

S["выбегать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span><span class="hd-gloss">RA NGOÀI — ở thể CHT mất trọng âm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бег-а́ть</span><span class="hd-gloss">CHẠY — khuôn của <b>бе́гать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chạy từ trong ra ngoài. Ra khỏi đâu: <b>из</b> + cách 2; ra tới đâu: <b>в / на</b> + cách 4 — <b>выбега́ть из до́ма на у́лицу</b>. Cặp HT <b>вы́бежать</b> kéo trọng âm lên đầu.</div>'
    '<div class="hd-warn"><b>выбега́ть</b> = chạy RA NGOÀI, nhấn điểm rời · <b>убега́ть</b> = chạy ĐI MẤT, không còn ở đây.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вы́бежать</b> (HT) · <b>бе́гать</b> chạy (nhiều chiều) · <b>убега́ть</b> bỏ chạy · <b>выходи́ть</b> đi ra</div>'
)

S["выбежать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы́-</span><span class="hd-gloss">RA NGOÀI — ở thể HT luôn mang trọng âm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бежать</span><span class="hd-gloss">CHẠY — chính là <b>бежа́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chạy ra ngoài, xong một lượt. Chia như <b>бежа́ть</b> (chỉ «tôi» và «họ» mang <b>г</b>), nhưng trọng âm đứng ở <b>вы́-</b> suốt bảng: <b>вы́бегу, вы́бежишь, вы́бегут</b>; sai khiến <b>вы́беги</b>.</div>'
    '<div class="hd-warn"><b>вы́бежать из до́ма</b> = chạy RA NGOÀI, nhấn điểm rời · <b>убежа́ть из до́ма</b> = chạy ĐI MẤT, bỏ nhà đi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>выбега́ть</b> (CHT) · <b>бежа́ть</b> chạy · <b>убежа́ть</b> chạy đi mất · <b>вы́йти</b> đi ra</div>'
)

S["испачкать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ис-</span><span class="hd-gloss">(<b>из-</b>) tiền tố thể, ở đây không thêm nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пачк-</span><span class="hd-gloss">BẨN — như <b>па́чкать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span><span class="hd-gloss">đuôi động từ, chia đều: <b>испа́чкаю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>па́чкать</b> làm trọn ⇒ làm bẩn. Bẩn bằng chất gì: cách 5 — <b>испа́чкать ру́ки кра́ской</b> làm tay dính sơn.</div>'
    '<div class="hd-warn"><b>из-</b> đứng trước phụ âm vô thanh (<b>п</b>) thì viết <b>ис-</b>, như <b>испо́ртить</b>.</div>'
    '<div class="hd-warn">Tự mình dây bẩn thì thêm <b>-ся</b>: <b>Ты весь испа́чкался!</b> Con lấm lem hết rồi!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>па́чкать</b> (CHT) · <b>испа́чкаться</b> bị lấm bẩn · <b>запа́чкать</b> làm dây bẩn</div>'
)

S["пачкать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пачк-</span><span class="hd-gloss">BẨN — gốc trơn, không chẻ thêm được</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span><span class="hd-gloss">đuôi động từ, chia đều: <b>па́чкаю, па́чкаешь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Để sơn, mực, bùn dây ra ⇒ làm bẩn. Cái bị bẩn để cách 4, chất gây bẩn để cách 5: <b>па́чкать сте́ны кра́ской</b>. Làm bẩn danh tiếng ⇒ bôi nhọ: <b>па́чкать репута́цию</b>. Cặp HT: <b>испа́чкать</b>.</div>'
    '<div class="hd-warn">Không dính <b>па́чка</b> gói — chữ đó mượn từ tiếng Đức, chỉ giống mặt chữ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>испа́чкать</b> (HT) · <b>па́чкаться</b> bị lấm bẩn · <b>запа́чкать</b> làm dây bẩn</div>'
)

S["пролетать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span><span class="hd-gloss">XUYÊN QUA, NGANG QUA — như <b>пройти́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-лет-а́ть</span><span class="hd-gloss">BAY — khuôn của <b>лета́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bay ngang qua; thời gian «bay qua» ⇒ trôi vèo: <b>Вре́мя бы́стро пролета́ет.</b> Chia đều: <b>пролета́ю</b>. Cặp HT: <b>пролете́ть</b>.</div>'
    '<div class="hd-warn">Bay qua PHÍA TRÊN: <b>над</b> + cách 5 (<b>над го́родом</b>) · bay NGANG bên: <b>ми́мо</b> + cách 2 (<b>ми́мо окна́</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пролете́ть</b> (HT) · <b>лета́ть</b> bay (nhiều chiều) · <b>полёт</b> chuyến bay · <b>проходи́ть</b> đi qua</div>'
)

S["пролететь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span><span class="hd-gloss">XUYÊN QUA, NGANG QUA — như <b>пройти́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-лете́ть</span><span class="hd-gloss">bay — <b>лете́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bay qua xong một lượt. Quãng đường để cách 4 trần: <b>пролете́ть ты́сячу киломе́тров</b>. Thời gian vèo qua: <b>Ле́то пролете́ло!</b> Hè trôi vèo mất rồi! Cặp CHT: <b>пролета́ть</b>.</div>'
    '<div class="hd-warn">Chia như <b>лете́ть</b>, т → ч chỉ ở «tôi»: <b>пролечу́</b>, nhưng <b>пролети́шь, пролетя́т</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пролета́ть</b> (CHT) · <b>лете́ть</b> bay (một chiều) · <b>вы́лететь</b> bay ra · <b>улете́ть</b> bay đi</div>'
)

S["помахать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span><span class="hd-gloss">MỘT LÚC, vài cái</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мах-</span><span class="hd-gloss">VUNG, vẫy — như <b>маха́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́-ть</span><span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>маха́ть</b> vài cái rồi thôi ⇒ vẫy chào. Vẫy AI: cách 3, vẫy BẰNG gì: cách 5 — <b>помаха́ть ма́ме руко́й</b>. Dỗ trẻ con: <b>Помаши́ ба́бушке!</b> Vẫy bà đi con!</div>'
    '<div class="hd-warn">х → ш ở MỌI ngôi tương lai, trọng âm lùi sau «tôi»: <b>помашу́, пома́шешь, пома́шут</b>.</div>'
    '<div class="hd-warn"><b>помаха́ть</b> vẫy vài cái · <b>махну́ть</b> vẫy đúng MỘT cái.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>маха́ть</b> vẫy (CHT) · <b>махну́ть</b> vẫy một cái · <b>взмах</b> cú vung · <b>разма́х</b> tầm vung, quy mô</div>'
)

S["упростить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span><span class="hd-gloss">làm cho TRỞ NÊN…</span></div>'
    '<div class="hd-row"><span class="hd-piece">-прост-</span><span class="hd-gloss">ĐƠN GIẢN — <b>просто́й</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span><span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm cho ĐƠN GIẢN ⇒ đơn giản hóa. Cùng khuôn <b>у-</b> + gốc tính từ + <b>-ить</b> với trái nghĩa <b>усложни́ть</b> làm phức tạp. Cặp CHT: <b>упроща́ть</b>.</div>'
    '<div class="hd-warn">ст → щ chỉ ở «tôi»: <b>упрощу́</b>, nhưng <b>упрости́шь, упростя́т</b>. Chữ <b>щ</b> ấy nằm cố định trong <b>упроща́ть</b> và so sánh <b>про́ще</b> đơn giản hơn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>упроща́ть</b> (CHT) · <b>упроще́ние</b> sự đơn giản hóa · <b>просто́й</b> đơn giản · <b>про́сто</b> đơn giản, chỉ là</div>'
)

S["упрощать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span><span class="hd-gloss">làm cho TRỞ NÊN…</span></div>'
    '<div class="hd-row"><span class="hd-piece">-прощ-</span><span class="hd-gloss">= <b>прост-</b> ĐƠN GIẢN, sau khi ст → щ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́-ть</span><span class="hd-gloss">đuôi CHT, chia đều: <b>упроща́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>упрости́ть</b>: làm cho ĐƠN GIẢN. Nhận cặp bằng phép ст → щ, y như <b>прости́ть</b> ↔ <b>проща́ть</b> tha thứ.</div>'
    '<div class="hd-warn">Còn để chê «đơn giản hóa quá mức»: <b>Не упроща́й!</b> Đừng đơn giản hóa vấn đề!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>упрости́ть</b> (HT) · <b>упроще́ние</b> sự đơn giản hóa · <b>про́ще</b> đơn giản hơn · <b>усложня́ть</b> làm phức tạp</div>'
)

S["потереть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span><span class="hd-gloss">MỘT LÚC, vài cái</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тер-</span><span class="hd-gloss">CHÀ, XÁT — gốc <i>тер-/тир-</i> của <b>тере́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́-ть</span><span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>тере́ть</b> một lúc ⇒ chà, xoa, dụi vài cái: <b>потере́ть ру́ки</b> xoa tay. Nạo đồ ăn cũng dùng: <b>потере́ть сыр на тёрке</b> nạo phô mai. Cặp CHT: <b>тере́ть</b>.</div>'
    '<div class="hd-warn">Tương lai rụng <b>е</b> của gốc: <b>потру́, потрёшь, потру́т</b>; quá khứ giống đực không có <b>-л</b>: <b>потёр, потёрла</b>; sai khiến <b>потри́</b>.</div>'
    '<div class="hd-warn">Đừng lẫn <b>потеря́ть</b> làm mất — khác gốc, chia <b>потеря́ю</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тере́ть</b> (CHT) · <b>вы́тереть</b> lau · <b>стере́ть</b> xoá · <b>тёрка</b> cái nạo</div>'
)

S["тереть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">тер-</span><span class="hd-gloss">CHÀ, XÁT — gốc trơn, còn có dạng <i>тир-</i> (<b>вытира́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́-ть</span><span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Xát đi xát lại trên một mặt: chà vết bẩn, dụi mắt (<b>тере́ть глаза́</b>), nạo rau củ (<b>тере́ть морко́вь на тёрке</b>). Thêm <b>вы́-</b> cho nước, bụi RA hết mới thành lau: <b>вы́тереть</b>. Cặp HT: <b>потере́ть</b>.</div>'
    '<div class="hd-warn">Hiện tại rụng <b>е</b> của gốc: <b>тру, трёшь, трут</b>; quá khứ giống đực không có <b>-л</b>: <b>тёр, тёрла</b>; sai khiến <b>три</b> (trùng mặt chữ số ba).</div>'
    '<div class="hd-warn">Giày cọ đau chân cũng là từ này: <b>Ту́фли трут.</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>потере́ть</b> (HT) · <b>вытира́ть</b> lau · <b>стира́ть</b> giặt, xoá · <b>тёрка</b> cái nạo</div>'
)

S["клеить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кле-</span><span class="hd-gloss">KEO — <b>клей</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-ть</span><span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dùng keo ⇒ dán. Chia như <b>стро́ить</b>: <b>кле́ю, кле́ишь, кле́ят</b>, trọng âm đứng yên. Dán lên đâu: <b>на</b> + cách 4 — <b>кле́ить обо́и на сте́ну</b>. Cặp HT: <b>скле́ить</b> dán liền lại.</div>'
    '<div class="hd-warn">Sai khiến <b>клей!</b> viết y hệt danh từ <b>клей</b> keo. Dán VÀO một vật khác là <b>прикле́ить к</b> + cách 3.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>клей</b> keo · <b>скле́ить</b> dán liền lại · <b>прикле́ить</b> dán vào · <b>накле́йка</b> nhãn dán</div>'
)

S["лить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ли-</span><span class="hd-gloss">ĐỔ, RÓT — gốc trơn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span><span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cho chất lỏng chảy thành dòng: rót trà, đổ nước; nước, mưa tự trút xuống cũng là <b>лить</b>. Rót đầy xong là <b>нали́ть</b>, đổ ra hết là <b>вы́лить</b>.</div>'
    '<div class="hd-warn">и của gốc biến thành <b>ь</b>, y như <b>пить → пью</b>: <b>лью, льёшь, льют</b>; sai khiến <b>лей</b>. Quá khứ giống cái nhảy ra đuôi: <b>лил</b> nhưng <b>лила́</b>.</div>'
    '<div class="hd-warn"><b>Дождь льёт как из ведра́</b> = mưa như trút nước («như đổ từ xô»).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>нали́ть</b> rót đầy · <b>вы́лить</b> đổ ra · <b>поли́ть</b> tưới · <b>ли́вень</b> mưa rào</div>'
)

S["выливать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span><span class="hd-gloss">RA — ở thể CHT mất trọng âm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ли-</span><span class="hd-gloss">ĐỔ, RÓT — <b>лить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва́-ть</span><span class="hd-gloss">đuôi CHT, chia đều: <b>вылива́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đổ ra» cho hết, thường là đổ bỏ. Đổ từ đâu: <b>из</b> + cách 2; đổ vào đâu: <b>в</b> + cách 4 — <b>вылива́ть во́ду из ва́зы в ра́ковину</b>. Cặp HT: <b>вы́лить</b>.</div>'
    '<div class="hd-warn"><b>налива́ть</b> rót VÀO cho đầy ↔ <b>вылива́ть</b> đổ RA cho hết.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вы́лить</b> (HT) · <b>лить</b> đổ, rót · <b>налива́ть</b> rót · <b>полива́ть</b> tưới</div>'
)

S["вылить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы́-</span><span class="hd-gloss">RA — ở thể HT luôn mang trọng âm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ли-ть</span><span class="hd-gloss">ĐỔ, RÓT — <b>лить</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đổ RA hết, đổ bỏ. Chia như <b>лить</b> nhưng trọng âm đứng ở <b>вы́-</b> suốt bảng nên <b>ё</b> thành <b>е</b>: <b>вы́лью, вы́льешь, вы́льют</b>; quá khứ <b>вы́лила</b>; sai khiến <b>вы́лей</b>. Cặp CHT: <b>вылива́ть</b>.</div>'
    '<div class="hd-warn"><b>вы́литый</b> = giống như đúc: <b>Он вы́литый оте́ц.</b> Nó giống bố như đúc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вылива́ть</b> (CHT) · <b>лить</b> đổ, rót · <b>нали́ть</b> rót đầy · <b>проли́ть</b> làm đổ</div>'
)

S["возвратить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">воз-</span><span class="hd-gloss">ở đây: NGƯỢC lại, về</span></div>'
    '<div class="hd-row"><span class="hd-piece">-врат-</span><span class="hd-gloss">QUAY — như <b>враща́ть</b> xoay tròn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span><span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Quay ngược về» ⇒ trả lại, lấy lại. Vật ở cách 4, người nhận ở cách 3. т → щ ở «tôi»: <b>возвращу́</b>, nhưng <b>возврати́шь</b>; chữ <b>щ</b> ấy nằm cố định trong CHT <b>возвраща́ть</b>.</div>'
    '<div class="hd-warn">Trang trọng, hay gặp trong giấy tờ: <b>возврати́ть де́ньги</b> hoàn tiền. Nói hằng ngày dùng <b>верну́ть</b>: <b>Верни́ мне кни́гу!</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>возвраща́ть</b> (CHT) · <b>возвра́т</b> sự hoàn trả · <b>возврати́ться</b> trở về · <b>верну́ть</b> trả lại</div>'
)

S["бегун"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бег-</span><span class="hd-gloss">CHẠY — <b>бег</b> môn chạy</span></div>'
    '<div class="hd-row"><span class="hd-piece">-у́н</span><span class="hd-gloss">NGƯỜI hay làm việc đó — như <b>болту́н</b> kẻ ba hoa</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người chạy ⇒ vận động viên chạy, người chạy bộ. Nữ: <b>бегу́нья</b>. Chuyên cự ly nào: <b>на</b> + cách 4 — <b>бегу́н на дли́нные диста́нции</b>.</div>'
    '<div class="hd-warn">Trọng âm rơi ra đuôi ở mọi cách khác: <b>бегуна́, бегуно́м, бегуны́, бегуно́в</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бег</b> môn chạy · <b>бе́гать</b> chạy (nhiều chiều) · <b>бежа́ть</b> chạy (một chiều) · <b>пробе́жка</b> buổi chạy bộ</div>'
)

V = {
    "ремонтировать": "sửa, sửa chữa, tân trang",
    "перекладывать": "chuyển, dời, đặt sang chỗ khác, đùn đẩy",
    "переложить": "chuyển, dời, đặt sang chỗ khác, đùn đẩy",
    "испачкать": "làm bẩn, làm lem, bôi nhọ",
    "пачкать": "làm bẩn, làm lem, bôi nhọ",
    "пролетать": "bay qua, bay ngang, trôi vèo",
    "пролететь": "bay qua, bay ngang, trôi vèo",
    "помахать": "vẫy, vẫy tay, vung",
    "упростить": "đơn giản hóa, làm đơn giản",
    "упрощать": "đơn giản hóa, làm đơn giản",
    "потереть": "chà, xoa, dụi, nạo",
    "тереть": "chà, xoa, dụi, nạo",
    "лить": "rót, đổ, chảy, trút",
    "выливать": "đổ ra, đổ đi, trút hết",
    "вылить": "đổ ra, đổ đi, trút hết",
    "возвратить": "trả lại, hoàn lại, gửi trả, lấy lại",
    "бегун": "người chạy bộ, vận động viên chạy",
}


B = {
    "docbangmat": 170, "loitubat": 1, "nguonsai": 2,
    "baolen": [
        "выбегать / выбежать: KHÔNG có trong V. Nghĩa riêng gloss Anh xác nhận ngoài «chạy ra»: không có (cả hai chỉ «to run out»). Câu ví dụ cả 6 câu đã bôi «chạy ra» (выбежать 1 bôi «sẽ chạy ra»), không sửa.",
        "возвратить: dãy V «trả lại, hoàn lại, gửi trả, lấy lại» cố ý LỆCH dãy cặp возвращать «trả lại, hoàn trả, mang về, lấy lại», vì chép nguyên thì trùng HẾT với вернуть (cùng PERF). Chung «trả lại, lấy lại», riêng «hoàn lại, gửi trả» (gloss refund / send back).",
        "помахать: không chép dãy của махать (nghĩa «đập cánh, khoát» gloss помахать không có); chung «vẫy, vung», riêng «vẫy tay».",
        "ремонтировать: bỏ «đại tu», dùng chung dãy отремонтировать.",
        "Gloss Anh thiếu: потереть chỉ có «to rub», thiếu «to grate» (потереть сыр rất thường) — V dùng chung dãy với тереть nên có «nạo».",
        "Gloss Anh sai/lạ: испачкать «desecrate with awful words» — bác; nghĩa bóng đúng là «to tarnish, smear (a reputation)» như пачкать.",
        "Cặp thể nguồn gượng: лить ↔ налить (OpenRussian partners) — налить là cặp của наливать; лить không có cặp HT thuần. Thẻ chỉ nói «rót đầy xong là налить, đổ ra hết là вылить», không gọi là cặp.",
        "Bảng chia/trọng âm 22 từ đã tải lại OpenRussian đối chiếu: không thấy sai.",
        "Không chắc: gốc пачк- của пачкать (nguồn gốc xa chưa rõ) — thẻ ghi «gốc trơn»; chỉ khẳng định không dính пачка, khớp thẻ пачка. упростить ↔ простить: chỉ nhắc phép ст → щ giống nhau ở thẻ упрощать, không đưa vào Họ hàng (thẻ простой có ghi chung gốc xa).",
        "Thẻ cùng họ đã đọc (ремонт, класть, бежать, лететь, махать, простой, вытереть, лить, возвращать, пачка): không thấy sai.",
    ],
}
