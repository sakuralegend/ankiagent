# -*- coding: utf-8 -*-
"""k256 — actions: bốn cặp thể + sáu động từ lẻ + danh từ, tính từ; trục là GỐC đã học + chỗ bảng chia lệch.

Chỗ cần nhất quán với lô đã nạp:
(1) соци- (socius) + -ло́гия MÔN HỌC VỀ: khớp социальный k121, психология k100. (2) о-про-верг- NÉM, quật: khớp опровергать k236.
(3) у- làm cho TRỞ NÊN + точн- CHÍNH XÁC: khớp уточнить. (4) -прек- NGANG, NGƯỢC LẠI: khớp вопреки k211.
(5) сла-/сыл-/шл- GỬI: khớp послать k88, прислать k142; пере- SANG: khớp перевезти k224.
(6) -долж- DÀI: khớp продолжительность. (7) -еть TRỞ NÊN như thế: khớp краснеть k242; у- HT: khớp устать k48.
(8) вз- LÊN: khớp взлететь k227; вес- SỨC NẶNG: khớp весы k246. (9) брод-/брес- LÊ BƯỚC: khớp бродить k215.
Họ hàng cố ý vắng: không có (từ nào cũng có họ thật).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "опровержение": "sự bác bỏ, lời bác bỏ, lời phản bác, lời phủ nhận, lời cải chính",  # + retraction / correction (published)
    "уточнение": "sự làm rõ, lời làm rõ, chi tiết bổ sung",
    "рекламировать": "quảng cáo",                               # «giới thiệu sản phẩm» ngoài gloss
    "упрекать": "trách móc, chê trách, oán trách",              # dãy chung của cặp
    "упрекнуть": "trách móc, chê trách, oán trách",
    "переслать": "chuyển tiếp, gửi, gửi sang",                  # «gửi lại» (send back) sai: đó là отосла́ть / верну́ть
    "пересылать": "chuyển tiếp, gửi, gửi sang",
    "продолжительный": "kéo dài, lâu dài",                      # bỏ «dài» trơ: trùng дли́нный k41
    "устаревать": "lỗi thời, trở nên lạc hậu, cũ đi",           # «dần» là badge thể
    "устареть": "lỗi thời, trở nên lạc hậu, cũ đi",
    "калькулятор": "máy tính bỏ túi, máy tính cầm tay",         # bỏ «máy tính» trơ: trùng компью́тер k24
    "взвесить": "cân, cân nhắc",
    "взвешивать": "cân, cân nhắc",
    "бездействовать": "không hành động, ngồi yên không làm gì, không hoạt động",  # + to not work; «thụ động» là tính từ
}

# ----------------------------------------------------------------- социология
S["социология"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">соци-о-</span>'
    '<span class="hd-gloss">XÃ HỘI — Latin <i>socius</i> bạn đồng hành, như <b>социа́льный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ло́гия</span>'
    '<span class="hd-gloss">MÔN HỌC VỀ… = Anh <i>-logy</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Môn học về xã hội» = <i>sociology</i>. Trọng âm ở <i>-ло́-</i> như '
    '<b>психоло́гия, биоло́гия</b>; bỏ <i>-ия</i> là ra người làm môn đó, trọng âm lùi một âm tiết: '
    '<b>социо́лог</b>. Tên môn học nên chỉ dùng số ít.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>социо́лог</b> nhà xã hội học · <b>социологи́ческий</b> thuộc xã hội học · '
    '<b>социа́льный</b> xã hội (tính từ)</div>'
)

# --------------------------------------------------------------- опровержение
S["опровержение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-про-</span>'
    '<span class="hd-gloss">hai tiền tố, không còn tách nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-верж-</span>'
    '<span class="hd-gloss">= <i>-верг-</i> NÉM, quật; <i>г</i> hoá <i>ж</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ние</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cú quật đổ» một lời nói ⇒ lời bác bỏ. Trên báo chí nó là lời CẢI CHÍNH: '
    '<b>напеча́тать опроверже́ние</b> đăng lời cải chính. Bác CÁI GÌ thì cách 2: '
    '<b>опроверже́ние слу́хов</b>.</div>'
    '<div class="hd-warn"><b>вы́ступить с опроверже́нием</b> = lên tiếng bác bỏ — cụm hay gặp trong tin tức.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>опроверга́ть</b> bác bỏ (CHT) · <b>опрове́ргнуть</b> (HT) · '
    '<b>отверга́ть</b> khước từ (cùng <i>-верг-</i>)</div>'
)

# ------------------------------------------------------------------ уточнение
S["уточнение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">làm cho TRỞ NÊN… — như <b>уточни́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-точн-</span>'
    '<span class="hd-gloss">CHÍNH XÁC — <b>то́чный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ние</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Việc làm cho chính xác hơn ⇒ sự làm rõ; và chính cái chi tiết được nói thêm '
    'cho rõ. Câu xin chen vào cuộc họp: <b>Мо́жно одно́ уточне́ние?</b> Cho tôi nói rõ thêm một điểm?</div>'
    '<div class="hd-warn"><b>внести́ уточне́ния в план</b> = chỉnh lại cho kế hoạch chính xác hơn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уточни́ть</b> làm rõ (HT) · <b>уточня́ть</b> (CHT) · '
    '<b>то́чность</b> độ chính xác · <b>то́чка</b> dấu chấm</div>'
)

# -------------------------------------------------------------- рекламировать
S["рекламировать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">реклам-</span>'
    '<span class="hd-gloss">QUẢNG CÁO — <b>рекла́ма</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́рова-ть</span>'
    '<span class="hd-gloss">đuôi động từ mượn; khi chia <i>-ова-</i> → <i>-у-</i>: '
    '<b>реклами́рую</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm <b>рекла́ма</b> cho cái gì (cách 4): <b>реклами́ровать но́вый телефо́н</b>. '
    'Trọng âm rời gốc sang <i>-и́р-</i> rồi đứng yên.</div>'
    '<div class="hd-warn">Một dạng dùng cho CẢ HAI thể, nhưng thực tế gần như luôn nghe như CHT. '
    'Quảng cáo rầm rộ xong rồi thì nói <b>разреклами́ровать</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рекла́ма</b> quảng cáo · <b>рекла́мный</b> thuộc quảng cáo · '
    '<b>рекламода́тель</b> bên thuê quảng cáo</div>'
)

# ------------------------------------------------------------------- упрекать
S["упрекать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố đã dính liền, không tách nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-прек-</span>'
    '<span class="hd-gloss">NGANG, NGƯỢC LẠI — như <b>вопреки́</b> bất chấp</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>упрека́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nói điều NGƯỢC tai người ta ⇒ trách móc. AI ở cách 4, về việc gì: '
    '<b>в</b> + cách 6 hoặc <b>за</b> + cách 4 — <b>упрека́ть му́жа в жа́дности</b> trách chồng keo kiệt.</div>'
    '<div class="hd-warn">⚠️ Mức tin: nối <i>-прек-</i> với <b>вопреки́</b> là từ nguyên, không phải luật '
    'suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>упрекну́ть</b> trách một câu (HT) · <b>упрёк</b> lời trách · '
    '<b>безупре́чный</b> không chê vào đâu được (<i>к</i> → <i>ч</i>)</div>'
)

# ------------------------------------------------------------------ упрекнуть
S["упрекнуть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-прек-</span>'
    '<span class="hd-gloss">TRÁCH — như <b>упрека́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ну́-ть</span>'
    '<span class="hd-gloss">MỘT LẦN, đuôi thể hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Buông MỘT câu trách — cùng khuôn <b>толка́ть → толкну́ть</b>. Trọng âm ở đuôi suốt '
    'bảng: <b>упрекну́, упрекнёшь</b>. Vẫn đòi <b>в</b> + cách 6 hoặc <b>за</b> + cách 4: '
    '<b>Она́ упрекну́ла меня́ в эгои́зме.</b> Cô ấy trách tôi ích kỷ.</div>'
    '<div class="hd-warn"><b>Тебя́ не́ в чем упрекну́ть.</b> Chẳng có gì để trách cậu — <b>не́ в чем</b> viết rời '
    'vì giới từ chen vào giữa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>упрека́ть</b> (CHT) · <b>упрёк</b> lời trách · '
    '<b>безупре́чный</b> không chê vào đâu được</div>'
)

# ------------------------------------------------------------------ переслать
S["переслать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пере-</span>'
    '<span class="hd-gloss">SANG, từ chỗ này qua chỗ kia</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сл-а́ть</span>'
    '<span class="hd-gloss">gốc GỬI — như <b>посла́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gửi SANG tay khác ⇒ chuyển tiếp (tin nhắn, thư, tiền). Tương lai đổi '
    '<i>сл</i> → <i>шл</i> y như <b>пошлю́</b>: <b>перешлю́, перешлёшь</b>; quá khứ đều: <b>пересла́л</b>. '
    'Người nhận ở cách 3: <b>пересла́ть дру́гу письмо́</b>.</div>'
    '<div class="hd-warn"><b>перешли́</b> có hai thân: <b>Перешли́ мне фо́то!</b> Chuyển tiếp ảnh cho tôi (mệnh '
    'lệnh) ↔ <b>Они́ перешли́ у́лицу.</b> Họ đã sang đường (<b>перейти́</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пересыла́ть</b> (CHT) · <b>посла́ть</b> gửi đi · <b>присла́ть</b> gửi tới · '
    '<b>посы́лка</b> bưu kiện</div>'
)

# ----------------------------------------------------------------- пересылать
S["пересылать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пере-</span>'
    '<span class="hd-gloss">SANG, từ chỗ này qua chỗ kia</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сыл-а́ть</span>'
    '<span class="hd-gloss">gốc GỬI, dạng <i>сыл</i> của <i>сл</i> — như <b>посыла́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đang chuyển tiếp, hay chuyển tiếp. Chia đều tăm tắp <b>пересыла́ю, пересыла́ешь</b> — '
    'dễ hơn hẳn cặp HT <b>пересла́ть</b> (<b>перешлю́</b>).</div>'
    '<div class="hd-warn">Bảo ĐỪNG làm thì dùng thể này: <b>Не пересыла́й э́то сообще́ние!</b> Đừng chuyển '
    'tiếp tin này! Bảo làm thì dùng HT: <b>Перешли́!</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пересла́ть</b> (HT) · <b>пересы́лка</b> việc gửi chuyển · '
    '<b>присыла́ть</b> gửi tới · <b>посы́лка</b> bưu kiện</div>'
)

# --------------------------------------------------------------- прошлогодний
S["прошлогодний"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">прошл-о-</span>'
    '<span class="hd-gloss">ĐÃ QUA, trước — <b>про́шлый</b>, <i>-о-</i> là nguyên âm nối</span></div>'
    '<div class="hd-row"><span class="hd-piece">-го́д-</span>'
    '<span class="hd-gloss">NĂM — <b>год</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ний</span>'
    '<span class="hd-gloss">đuôi tính từ MỀM, như <b>нового́дний</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>про́шлый год</b> (năm ngoái) dính lại thành một tính từ ⇒ của năm ngoái. Đuôi mềm: '
    '<b>прошлого́дняя, прошлого́днее</b>. Bảng có dạng ngắn nhưng không ai dùng — bỏ qua.</div>'
    '<div class="hd-warn"><b>ну́жен как прошлого́дний снег</b> «cần như tuyết năm ngoái» = chẳng cần tí nào.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>про́шлый</b> trước, vừa rồi · <b>год</b> năm · '
    '<b>нового́дний</b> thuộc năm mới · <b>ежего́дный</b> hằng năm</div>'
)

# ------------------------------------------------------------ продолжительный
S["продолжительный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">kéo tiếp về phía trước</span></div>'
    '<div class="hd-row"><span class="hd-piece">-долж-</span>'
    '<span class="hd-gloss">gốc DÀI — của <b>до́лгий</b>, <i>г</i> hoá <i>ж</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́тельн-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cứ kéo tiếp mãi» ⇒ kéo dài. Chỉ nói THỜI GIAN, giọng trang trọng hơn <b>до́лгий</b>: '
    '<b>продолжи́тельная боле́знь</b> bệnh kéo dài. Dài về kích thước là <b>дли́нный</b>. '
    'Dạng ngắn giống đực chen <i>е</i>: <b>продолжи́телен</b>.</div>'
    '<div class="hd-warn"><b>бу́рные, продолжи́тельные аплодисме́нты</b> — tràng vỗ tay vang dội kéo dài, câu '
    'quen trong biên bản hội nghị.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>продолжи́тельность</b> thời lượng · <b>продолжа́ть</b> tiếp tục · '
    '<b>продолже́ние</b> phần tiếp theo · <b>до́лго</b> lâu</div>'
)

# ----------------------------------------------------------------- устаревать
S["устаревать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">giữ lại từ <b>устаре́ть</b>, không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-стар-е-</span>'
    '<span class="hd-gloss">CŨ + TRỞ NÊN — <b>ста́рый</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва́-ть</span>'
    '<span class="hd-gloss">kéo dài ⇒ thể CHT</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đang cũ dần đi, hay bị lỗi thời. Giữ nguyên <i>-ва-</i> khi chia: '
    '<b>устарева́ю, устарева́ет</b>. Chủ ngữ là đồ vật, từ ngữ, ý tưởng: '
    '<b>Те́хника бы́стро устарева́ет.</b> Máy móc lỗi thời nhanh lắm.</div>'
    '<div class="hd-warn">Đừng đọc lướt thành <b>устава́ть</b> (mệt): kia là gốc khác, không có '
    '<i>-ре-</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>устаре́ть</b> (HT) · <b>ста́рый</b> cũ, già · <b>старе́ть</b> già đi · '
    '<b>старомо́дный</b> lỗi mốt</div>'
)

# ------------------------------------------------------------------- устареть
S["устареть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố làm nên thể hoàn thành — như <b>уста́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-стар-</span>'
    '<span class="hd-gloss">CŨ, GIÀ — <b>ста́рый</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ть</span>'
    '<span class="hd-gloss">TRỞ NÊN như thế — như <b>красне́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đã trở nên cũ ⇒ lỗi thời. Nói «cái này lỗi thời rồi» thì dùng QUÁ KHỨ: '
    '<b>Э́тот слова́рь устаре́л.</b> Chia đều, giữ <i>е</i>: <b>устаре́ет</b>.</div>'
    '<div class="hd-warn">Người già đi là <b>постаре́ть</b>; <b>устаре́ть</b> chủ yếu nói đồ vật, '
    'thông tin, lối nghĩ. Tính từ rất hay gặp: <b>устаре́вший</b> lỗi thời.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>устарева́ть</b> (CHT) · <b>ста́рый</b> cũ, già · <b>постаре́ть</b> già đi (HT) · '
    '<b>ста́рость</b> tuổi già</div>'
)

# ---------------------------------------------------------------- калькулятор
S["калькулятор"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">калькул-</span>'
    '<span class="hd-gloss">TÍNH TOÁN — Latin <i>calculare</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́тор</span>'
    '<span class="hd-gloss">= Anh <i>-ator</i>: máy làm việc đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= <i>calculator</i>. Chỉ là cái máy bấm số (hay ứng dụng tính toán trên điện thoại); '
    'máy vi tính là <b>компью́тер</b>. Trọng âm đứng yên ở <i>-я́-</i>: <b>калькуля́торы</b>.</div>'
    '<div class="hd-warn">Tính BẰNG máy dùng <b>на</b> + cách 6: <b>посчита́ть на калькуля́торе</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>калькуля́ция</b> bảng tính giá thành</div>'
)

# --------------------------------------------------------------------- брести
S["брести"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">брес-</span>'
    '<span class="hd-gloss">LÊ BƯỚC — gốc thật là <i>бред-</i>, <i>д</i> hoá <i>с</i> trước <i>-ти</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ти́</span>'
    '<span class="hd-gloss">đuôi nguyên thể nhấn cuối, như <b>вести́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Động từ chuyển động MỘT HƯỚNG: đi chậm, nặng nề về một phía; lang thang nhiều hướng là '
    '<b>броди́ть</b> — đúng khuôn <b>вести́ : води́ть</b>. Chia cũng y <b>вести́</b>: <b>бреду́, бредёшь</b>; '
    'quá khứ rơi <i>д</i>, trọng âm ở đuôi: <b>брёл, брела́, брели́</b>.</div>'
    '<div class="hd-warn"><b>приобрести́</b> (mua, có được) trông như có <i>брести</i> bên trong nhưng khác gốc: '
    'chữ <i>б</i> ở đó thuộc tiền tố <i>об-</i>, tương lai là <b>приобрету́</b> (<i>т</i>, không phải <i>д</i>). '
    '⚠️ Mức tin: từ nguyên.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>броди́ть</b> lang thang · <b>побрести́</b> lê bước đi (HT) · '
    '<b>бродя́га</b> kẻ lang thang · <b>брод</b> chỗ cạn lội qua được</div>'
)

# ------------------------------------------------------------------- взвесить
S["взвесить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вз-</span>'
    '<span class="hd-gloss">LÊN — như <b>взлете́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-вес-</span>'
    '<span class="hd-gloss">SỨC NẶNG — <b>вес</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-ть</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhấc LÊN cân xem nặng bao nhiêu; cân trong đầu ⇒ cân nhắc, y hệt Anh <i>weigh</i>: '
    '<b>взве́сить все за и про́тив</b> cân nhắc lợi hại. Ngôi «tôi» <i>с → ш</i>: '
    '<b>взве́шу, взве́сишь</b>.</div>'
    '<div class="hd-warn"><b>ве́сить</b> = NẶNG bao nhiêu (trạng thái); <b>взве́сить</b> = đem CÂN vật gì. '
    'Tự cân mình thì thêm <i>-ся</i>: <b>взве́ситься</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>взве́шивать</b> (CHT) · <b>вес</b> cân nặng · <b>весы́</b> cái cân · '
    '<b>взве́шенный</b> có cân nhắc kỹ</div>'
)

# ----------------------------------------------------------------- взвешивать
S["взвешивать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вз-</span>'
    '<span class="hd-gloss">LÊN — như <b>взлета́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-веш-</span>'
    '<span class="hd-gloss">= <i>-вес-</i> SỨC NẶNG, <i>с</i> hoá <i>ш</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ть</span>'
    '<span class="hd-gloss">kéo dài ⇒ thể CHT</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đang cân, hay cân; đang cân nhắc. Chữ <i>ш</i> cũng là chữ ở ngôi «tôi» '
    '<b>взве́шу</b> của cặp HT <b>взве́сить</b>. Chia đều: <b>взве́шиваю, взве́шиваешь</b>.</div>'
    '<div class="hd-warn"><b>взве́шивать ка́ждое сло́во</b> = cân nhắc từng lời.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>взве́сить</b> (HT) · <b>взве́шиваться</b> tự cân mình · '
    '<b>вес</b> cân nặng · <b>весы́</b> cái cân</div>'
)

# ------------------------------------------------------------- бездействовать
S["бездействовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">без-</span>'
    '<span class="hd-gloss">KHÔNG CÓ (giữ <i>з</i> trước <i>д</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-де́йств-</span>'
    '<span class="hd-gloss">HÀNH ĐỘNG — như <b>де́йствие</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-ть</span>'
    '<span class="hd-gloss">đuôi động từ; chia <i>-у-</i>: <b>безде́йствую</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không có hành động ⇒ ngồi yên không làm gì dù đáng ra phải làm: '
    '<b>Поли́ция безде́йствует.</b> Cảnh sát án binh bất động. Máy móc, nhà máy thì là không hoạt động: '
    '<b>Лифт безде́йствует.</b></div>'
    '<div class="hd-warn">Lười, ăn không ngồi rồi là <b>безде́льничать</b>; <b>безде́йствовать</b> là không ra tay '
    'trước một việc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>безде́йствие</b> sự không hành động · <b>де́йствовать</b> hành động · '
    '<b>де́йствие</b> hành động, tác dụng</div>'
)

# --------------------------------------------------------------- аплодировать
S["аплодировать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">аплод-</span>'
    '<span class="hd-gloss">VỖ TAY — tiếng Pháp <i>applaudir</i>, Anh <i>applaud</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́рова-ть</span>'
    '<span class="hd-gloss">đuôi động từ mượn; chia <i>-у-</i>: <b>аплоди́рую</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= <i>applaud</i>, vỗ tay để KHEN. Vỗ tay cho ai thì cách 3, không giới từ: '
    '<b>аплоди́ровать арти́сту</b>. Đứng dậy vỗ tay: <b>аплоди́ровать сто́я</b>.</div>'
    '<div class="hd-warn"><b>хло́пать</b> đời thường hơn và rộng hơn (vỗ vai, sập cửa); '
    '<b>аплоди́ровать</b> chỉ có vỗ tay tán thưởng. Bắt đầu vỗ tay (HT): <b>зааплоди́ровать</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>аплодисме́нты</b> tràng vỗ tay (chỉ số nhiều) · '
    '<b>зааплоди́ровать</b> vỗ tay vang lên (HT)</div>'
)

# docbangmat 123 · loitubat 5: «не в чем» thiếu trọng âm не́; «нужно как прошлогодний снег» → нужен (thành ngữ đúng dạng);
# Э́тот thiếu dấu; «брёл: trọng âm nhảy ra đuôi» → đứng ở đuôi (брёл một âm tiết); взвешивать «ш lấy từ взвешу» nói quá → «cũng là chữ ở».
# nguonsai 2: dạng ngắn прошлогодний; gloss «send back» của переслать.
B = {
    "docbangmat": 123,
    "loitubat": 5,
    "nguonsai": 2,
    "baolen": [
        "прошлогодний — bảng: DẠNG NGẮN (прошлого́ден · прошлого́дня · прошлого́дне · прошлого́дни) do máy sinh, tính từ quan hệ không có dạng ngắn; nên bỏ trống cả bốn ô.",
        "переслать — gloss EN «to forward/to send back»: «send back» sai (đó là отослать/вернуть); đúng là «to forward / to send (on)». V dùng chung dãy với пересылать: chuyển tiếp, gửi, gửi sang.",
        "взвесить — gloss EN «to suspend (in a liquid)» là thuật ngữ hiếm, không đưa vào V.",
        "рекламировать — badge BI-ASP ĐÚNG (Ожегов, Зализняк: св-нсв), thẻ đã nói thực tế dùng như CHT; V cắt «giới thiệu sản phẩm» còn «quảng cáo» (tách khỏi реклама bằng badge từ loại).",
        "опровержение — V thêm «lời cải chính» (gloss retraction / published correction).",
        "бездействовать — V bỏ «thụ động» (tính từ), thêm «không hoạt động» (gloss to not work). Thẻ dẫn бездельничать (ở lô khác trong đợt) là «lười, ăn không ngồi rồi».",
        "упрекать/упрекнуть — V bỏ «khiển trách», «quở trách» để cặp chung dãy: trách móc, chê trách, oán trách. Từ nguyên -прек- theo вопреки k211, đã gắn Mức tin.",
        "длительный chưa có trên máy — không va chạm với продолжительный; V продолжительный «kéo dài, lâu dài» nằm gần долгий «lâu, dài, kéo dài» nhưng không trùng hết.",
    ],
}
