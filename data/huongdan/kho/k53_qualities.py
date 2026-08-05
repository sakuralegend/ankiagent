# -*- coding: utf-8 -*-
"""k53 — qualities: tính từ chỉ tính chất, trục chính là DANH TỪ + hậu tố thành
TÍNH TỪ (-н-, -лив-) và chỗ dạng ngắn lệch khỏi dạng dài.

Không có khối dùng chung: luật -н-/-лив- và luật biến âm được nói bằng MỘT câu
về chính từ đó trên mỗi thẻ (README §3).
"""

S = {}
V = {}

# ---------------------------------------------------------------- thời tiết
S["будничный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">будн-</span>'
    '<span class="hd-gloss">ngày thường trong tuần (бу́дни)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ичн-</span>'
    '<span class="hd-gloss">thuộc về, mang tính</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ngày của người Nga chia hai loại: <b>бу́дни</b> ngày đi làm và '
    '<b>пра́здник</b> ngày lễ. Cái gì mang tính <b>бу́дни</b> thì đều đều, không có gì '
    'đáng nhớ — từ đó ra nghĩa tẻ nhạt, xám xịt.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бу́дни</b> ngày thường (chỉ có số nhiều) · '
    '<b>бу́дний</b> thuộc ngày trong tuần (<b>бу́дний день</b>)</div>'
)
V['будничный'] = 'thường ngày, tẻ nhạt, đơn điệu'

S["ветреный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ветр-</span>'
    '<span class="hd-gloss">gió — gốc của <b>ве́тер</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ен-</span>'
    '<span class="hd-gloss">có, đầy cái đó</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chữ <b>е</b> trong <b>ве́тер</b> là nguyên âm chạy: thêm đuôi vào '
    'là nó rụng (<b>ве́тер</b> nhưng <b>ве́тра</b>, <b>ве́треный</b>). Nghĩa bóng đi thẳng từ '
    'nghĩa đen: trong đầu người ấy chỉ có gió thổi qua ⇒ nhẹ dạ, hay đổi ý.</div>'
    '<div class="hd-warn">✍️ Viết <b>ве́треный</b> MỘT chữ <b>н</b> — ngoại lệ nổi tiếng; '
    'hễ thêm tiền tố thì lại thành hai <b>н</b> (<b>безве́тренный</b> lặng gió).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ве́тер</b> gió · <b>ветеро́к</b> làn gió nhẹ · '
    '<b>ве́трено</b> trời có gió (trạng từ)</div>'
)
V['ветреный'] = 'có gió, lộng gió, nhẹ dạ, hay thay đổi'

S["дождливый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дожд-</span>'
    '<span class="hd-gloss">mưa — gốc của <b>дождь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-лив-</span>'
    '<span class="hd-gloss">hay có, đầy cái đó</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hậu tố <b>-лив-</b> gắn vào danh từ để nói "hay có cái đó", cùng '
    'khuôn với <b>счастли́вый</b> trong lô này. Nên <b>дождли́вый</b> tả cả một mùa hay đổ '
    'mưa, không phải một cơn mưa cụ thể.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дождь</b> mưa · <b>дождеви́к</b> áo mưa · '
    '<b>дождево́й</b> thuộc về mưa</div>'
)
V['дождливый'] = 'mưa nhiều, hay mưa'

S["морозный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мороз-</span>'
    '<span class="hd-gloss">cái rét đóng băng (<b>моро́з</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-</span>'
    '<span class="hd-gloss">thuộc về</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ + <b>-н-</b> là lối dựng tính từ hay gặp nhất, lô này còn '
    '<b>сне́жный</b> và <b>со́лнечный</b>. <b>моро́з</b> không phải cái lạnh chung chung mà '
    'là rét dưới 0 độ, đóng băng — nên <b>моро́зный</b> mạnh hơn <b>холо́дный</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>моро́з</b> rét đóng băng · <b>моро́женое</b> kem · '
    '<b>Дед Моро́з</b> Ông già Tuyết</div>'
    '<div class="hd-why">📋 Dạng ngắn giống đực chèn thêm <b>-е-</b> cho đọc được: '
    '<b>моро́зен</b>; ba dạng kia đều đặn, trọng âm đứng yên cả bảng.</div>'
)
V['морозный'] = 'giá buốt, có sương giá'

S["облачный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">облак-</span>'
    '<span class="hd-gloss">mây (<b>о́блако</b>) → <b>облач-</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-</span>'
    '<span class="hd-gloss">thuộc về, có</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chữ <b>к</b> của <b>о́блако</b> không đứng nổi trước <b>-н-</b> nên '
    'đổi thành <b>ч</b> — đúng luật г/к/х → ж/ч/ш. Nghĩa gốc là "trời có mây", nghĩa tin '
    'học "đám mây" đi theo tiếng Anh sau này.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>о́блако</b> đám mây · <b>безо́блачный</b> không một gợn mây, '
    'quang đãng</div>'
    '<div class="hd-why">📋 Dạng ngắn giống đực chèn <b>-е-</b>: <b>о́блачен</b>; trọng âm '
    'bám chặt <b>о́-</b> ở mọi dạng.</div>'
)
V['облачный'] = 'có mây, nhiều mây, đám mây'

S["пасмурный"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>па́смурный</b> KHÔNG chẻ được bằng từ tiếng Nga hôm nay — gốc '
    '<b>смур-</b> "xám xịt" nay không còn đứng một mình. Nhớ bằng cặp đối lập với '
    '<b>со́лнечный</b> trong lô này.</div>'
    '<div class="hd-warn">⚠️ Mức tin: chỗ "gốc <b>смур-</b>" là từ nguyên, không phải luật '
    'suy ra được — dùng để nhớ, đừng đem áp cho từ khác.</div>'
    '<div class="hd-why">Khác <b>о́блачный</b>: <b>о́блачный</b> chỉ nói trên trời CÓ mây, '
    'còn <b>па́смурный</b> là cả bầu trời xám kín không thấy nắng; nói về người thì là vẻ '
    'mặt ủ rũ.</div>'
    '<div class="hd-why">📋 Dạng ngắn giống đực chèn <b>-е-</b>: <b>па́смурен</b>; trọng âm '
    'không dịch đi đâu.</div>'
)
V['пасмурный'] = 'âm u, xám xịt, ủ rũ'

S["положительный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лож-</span>'
    '<span class="hd-gloss">ĐẶT, để (như <b>положи́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тельн-</span>'
    '<span class="hd-gloss">động từ → tính từ "có tính…"</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>-лож-</b> là "đặt xuống". Cái gì đã được đặt ra, khẳng định '
    'thì là <b>положи́тельный</b>: <b>положи́тельный отве́т</b> câu trả lời đồng ý, và trong '
    'toán là số dương.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>положи́ть</b> đặt xuống · <b>положе́ние</b> vị trí, tình thế · '
    '<b>отрица́тельный</b> tiêu cực, phủ định (cùng đuôi <b>-тельный</b>, nghĩa ngược)</div>'
    '<div class="hd-why">📋 Dạng ngắn giống đực rút <b>-льный</b> thành <b>-лен</b>: '
    '<b>положи́телен</b>; các dạng kia giữ nguyên thân.</div>'
)
V['положительный'] = 'tích cực, khẳng định, dương'

S["снежный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">снег-</span>'
    '<span class="hd-gloss">tuyết (<b>снег</b>) → <b>снеж-</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-</span>'
    '<span class="hd-gloss">thuộc về, phủ đầy</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng một luật với <b>о́блачный</b> trong lô: phụ âm cuối gốc mềm đi '
    'trước <b>-н-</b>, ở đây là <b>г → ж</b> (<b>снег</b> → <b>сне́жный</b>). Thấy <b>ж</b> '
    'là đoán được gốc có <b>г</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>снег</b> tuyết · <b>снежи́нка</b> bông tuyết · '
    '<b>снегови́к</b> người tuyết</div>'
    '<div class="hd-why">📋 Dạng ngắn giống đực chèn <b>-е-</b>: <b>сне́жен</b>; trọng âm '
    'giữ nguyên ở <b>сне́-</b>.</div>'
)

S["солнечный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">солн-</span>'
    '<span class="hd-gloss">mặt trời — gốc của <b>со́лнце</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ечн-</span>'
    '<span class="hd-gloss">thuộc về (chữ <b>ц</b> đổi thành <b>ч</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhìn <b>со́лнце</b> → <b>со́лнечный</b> là thấy <b>ц → ч</b>, cùng '
    'họ biến âm với <b>к → ч</b> của <b>о́блачный</b>. Từ này ôm cả nghĩa thường ngày '
    '(<b>со́лнечный день</b> ngày nắng) lẫn nghĩa thiên văn (<b>со́лнечная систе́ма</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>со́лнце</b> mặt trời · <b>подсо́лнух</b> hoa hướng dương '
    '(quay theo mặt trời)</div>'
    '<div class="hd-why">📋 Dạng ngắn giống đực chèn <b>-е-</b>: <b>со́лнечен</b>; trọng âm '
    'không rời <b>со́-</b>.</div>'
)

S["близкий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">близ-</span>'
    '<span class="hd-gloss">GẦN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-</span>'
    '<span class="hd-gloss">hậu tố tính từ, rụng khi so sánh hơn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span>'
    '<span class="hd-gloss">đuôi tính từ (sau <b>к</b> viết <b>и</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một gốc dùng cho cả khoảng cách lẫn tình cảm: <b>бли́зкий дом</b> '
    'nhà ở gần, <b>бли́зкий друг</b> bạn thân. Bỏ <b>-к-</b> đi và đổi <b>з → ж</b> thì ra '
    'so sánh hơn <b>бли́же</b> — dạng này phải thuộc, không suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бли́зко</b> ở gần (trạng từ) · <b>бли́же</b> gần hơn · '
    '<b>приблизи́тельно</b> khoảng chừng</div>'
    '<div class="hd-why">📋 Dạng ngắn lệch hai chỗ: giống đực chèn <b>-о-</b> '
    '(<b>бли́зок</b>), giống cái dồn trọng âm ra đuôi (<b>близка́</b>).</div>'
)

S["весёлый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">весёл-</span>'
    '<span class="hd-gloss">VUI, phấn khởi — gốc trơn, không chẻ nhỏ hơn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chữ <b>ё</b> LUÔN mang trọng âm. Nên hễ trọng âm rời khỏi gốc là '
    '<b>ё</b> tự động thành <b>е</b>: <b>весёлый</b> → <b>весела́</b>. Thấy <b>е</b> ở đó '
    'thì biết ngay trọng âm đã nhảy ra sau.</div>'
    '<div class="hd-warn">✍️ Gõ đủ hai chấm: <b>весёлый</b>, không phải "веселый" — thiếu '
    '<b>ё</b> là sai chính tả chứ không phải viết tắt.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ве́село</b> vui (<b>мне ве́село</b> tôi thấy vui) · '
    '<b>весе́лье</b> niềm vui · <b>весели́ться</b> vui chơi</div>'
    '<div class="hd-why">📋 Dạng ngắn: <b>ве́сел</b> · <b>весела́</b> · <b>ве́село</b> — chỉ '
    'giống cái nhấn ở đuôi, và đúng chỗ đó <b>ё</b> hoá <b>е</b>.</div>'
)
V['весёлый'] = 'vui vẻ, vui nhộn, tươi vui'

# Họ hàng: CỐ Ý BỎ. `ка́ждый` là đại từ cổ, các từ trông giống gốc đều là ghép
# hiện đại hiếm dùng — viết vào chỉ để lấp ô (README §2, CHUAN v3 mục D).
S["каждый"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>ка́ждый</b> là đại từ cổ, không chẻ được thành mảnh có nghĩa. '
    'Chỗ đáng nhớ là nó chia y hệt một tính từ: <b>ка́ждый день</b> mỗi ngày, '
    '<b>ка́ждую неде́лю</b> mỗi tuần (cách 4 chỉ thời gian lặp lại).</div>'
    '<div class="hd-warn">📌 Đi với danh từ SỐ ÍT — <b>ка́ждый день</b>, không phải "каждые '
    'дни".</div>'
    '<div class="hd-warn">⚠️ Ba từ hay lẫn: <b>ка́ждый</b> từng cái một · <b>все</b> cả nhóm '
    'gộp lại · <b>любо́й</b> cái nào cũng được.</div>'
)
V['каждый'] = 'mỗi, từng, mọi người'

S["слабый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">слаб-</span>'
    '<span class="hd-gloss">YẾU, ít sức — gốc trơn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một nghĩa "ít sức" trải ra thành cả nghĩa "ít đậm đặc": '
    '<b>сла́бый ве́тер</b> gió nhẹ, <b>сла́бый ко́фе</b> cà phê loãng. Cứ hình dung cái gì đó '
    'thiếu độ mạnh, không riêng con người.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сла́бость</b> sự yếu, điểm yếu (đuôi <b>-ость</b> dựng danh từ '
    'trừu tượng) · <b>слабе́ть</b> yếu dần đi</div>'
    '<div class="hd-why">📋 Dạng ngắn chỉ lệch ở giống cái: trọng âm dồn ra đuôi '
    '(<b>слаба́</b>), còn <b>слаб</b> · <b>сла́бо</b> · <b>сла́бы</b> vẫn nhấn gốc.</div>'
)
V['слабый'] = 'yếu, kém, loãng, nhạt'

S["счастливый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">có, được cùng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-част-</span>'
    '<span class="hd-gloss">PHẦN được chia (như <b>часть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лив-</span>'
    '<span class="hd-gloss">đầy, hay có</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Theo từ nguyên, nghĩa đen là "được chia phần tốt" — nên từ này ôm '
    'cả hạnh phúc lẫn may mắn. Đuôi <b>-лив-</b> giống hệt <b>дождли́вый</b> trong lô. Chữ '
    '<b>т</b> của <b>часть</b> vẫn viết dù không đọc: nhớ cụm <b>-стл-</b>.</div>'
    '<div class="hd-warn">🗣 Câu chúc phải thuộc: <b>Счастли́вого пути́!</b> — thượng lộ bình '
    'an, nói khi tiễn ai đi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сча́стье</b> hạnh phúc · <b>часть</b> phần</div>'
)
V['счастливый'] = 'hạnh phúc, may mắn'
