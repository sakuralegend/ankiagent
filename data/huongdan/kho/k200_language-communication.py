# -*- coding: utf-8 -*-
"""k200 — language::communication (lô trộn): bày tỏ, phản bác, thú nhận, phàn nàn; thời điểm; phân số.

Chỗ cần nhất quán trong lô:
(1) -каз- «NÓI, chỉ ra — gốc của сказа́ть, показа́ть», chia з → ж (khớp отказа́ться [k117]):
    вы́сказать (вы- HT luôn nhấn) / выска́зывать (-ыва- CHT, trọng âm về -ка́з-).
(2) возрази́ть (thẻ chính, có Mức tin) / возража́ть / возраже́ние: воз- ĐÁP TRẢ + -раз-/-раж- «đánh»,
    khớp вы́разить / выража́ть [k135] (z→ж ở thể CHT, ở HT chỉ ngôi «tôi»).
(3) приблизи́тельный (thẻ chính) / приближа́ться / прибли́зиться: при- + -близ-/-ближ- GẦN,
    khớp бли́зкий / бли́же [k53] (ж của бли́же = ж của приближа́ться).
(4) признава́ться: -ва- rụng ở hiện tại, khớp признава́ть [k170].
(5) жа́ловаться: gốc жал- THƯƠNG XÓT, khớp сожале́ние [k57], жале́ть [k188].
(6) опозда́ние / продолже́ние / внача́ле / впосле́дствии: đọc thẳng từ опозда́ть [k87], продолжа́ть [k85],
    нача́ло [k57], после́дний [k109].
(7) вдво́е ← дво́е [k103] (đừng lẫn вдвоём [k126]) · три́жды ↔ два́жды [k116] · треть ← тре́тий [k30]
    · ниско́лько ↔ ско́лько [k31], не́сколько [k91].
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "сокращение": "sự cắt giảm, sự giảm bớt, sự rút ngắn, chữ viết tắt, sự tinh giản",  # thiếu hẳn abbreviation/short form/shortening
}

# --------------------------------------------------------------- рекомендовать
S["рекомендовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рекоменд-</span>'
    '<span class="hd-gloss">= recommend: khuyên, giới thiệu</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-ть</span>'
    '<span class="hd-gloss">đuôi gắn cho động từ mượn</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= recommend. <b>-ова-</b> thành <b>-у-</b> ở hiện tại: '
    '<b>рекоменду́ю</b>, <b>рекоменду́ешь</b>. Khuyên AI (cách 3) LÀM gì (nguyên thể): '
    '<b>Рекоменду́ю вам отдохну́ть</b>. Cũng là giới thiệu một người, một thứ cho ai.</div>'
    '<div class="hd-warn">Một dạng dùng được cho CẢ HAI thể; muốn nói rõ «đã khuyên xong» thì có '
    '<b>порекомендова́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рекоменда́ция</b> lời khuyên, thư giới thiệu · '
    '<b>рекоменда́тельный</b> để giới thiệu</div>'
)

# ------------------------------------------------------------------ высказать
S["высказать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы́-</span>'
    '<span class="hd-gloss">RA ngoài — thể HT nên luôn mang trọng âm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сказать</span>'
    '<span class="hd-gloss">= <b>сказа́ть</b>; gốc <b>-каз-</b> NÓI, chỉ ra — gốc của '
    '<b>сказа́ть</b>, <b>показа́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Nói RA điều đang giữ trong đầu» ⇒ bày tỏ (ý kiến, nhận xét). Chia y như '
    '<b>сказа́ть</b>: з → ж ở mọi ngôi, nhưng trọng âm dính chặt ở <b>вы́-</b>: '
    '<b>вы́скажу</b>, <b>вы́скажешь</b>, <b>вы́скажут</b>.</div>'
    '<div class="hd-warn"><b>вы́сказать мне́ние</b> = bày tỏ ý kiến. Thêm <b>-ся</b>: '
    '<b>вы́сказаться за / про́тив</b> = lên tiếng ủng hộ / phản đối.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>выска́зывать</b> (CHT) · <b>выска́зывание</b> câu nói, lời phát biểu · '
    '<b>сказа́ть</b> nói · <b>показа́ть</b> chỉ cho xem</div>'
)

# ---------------------------------------------------------------- высказывать
S["высказывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span>'
    '<span class="hd-gloss">RA ngoài</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сказ-</span>'
    '<span class="hd-gloss">gốc <b>-каз-</b> NÓI, chỉ ra — gốc của <b>сказа́ть</b>, '
    '<b>показа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-ть</span>'
    '<span class="hd-gloss">dấu thể CHƯA hoàn thành + đuôi</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chèn <b>-ыва-</b> vào <b>вы́сказать</b> là ra thể chưa hoàn thành: '
    '<b>вы-</b> mất trọng âm, trọng âm về <b>-ка́з-</b>, và chia đều, giữ з: '
    '<b>выска́зываю</b>, <b>выска́зываешь</b>. Cụm và cách dùng y hệt — xem thẻ '
    '<b>вы́сказать</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">Cùng khuôn <b>-ка́зывать</b>: <b>пока́зывать</b> chỉ cho xem · '
    '<b>расска́зывать</b> kể · <b>отка́зываться</b> từ chối</div>'
)

# ------------------------------------------------------------------ возразить
S["возразить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">воз-</span>'
    '<span class="hd-gloss">ĐÁP TRẢ, ngược lại</span></div>'
    '<div class="hd-row"><span class="hd-piece">-раз-</span>'
    '<span class="hd-gloss">gốc «đánh, giáng» — như <b>вы́разить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi lớp chia 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đánh TRẢ lại một lời» ⇒ phản bác, phản đối. Chỉ ngôi «tôi» đổi з → ж: '
    '<b>возражу́</b>, còn lại giữ з — <b>возрази́шь</b>, <b>возрази́т</b>. Cặp CHT '
    '<b>возража́ть</b> lấy luôn ж, y khuôn <b>вы́разить</b> → <b>выража́ть</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: «đánh» là từ nguyên của gốc <b>-раз-</b> (như ở '
    '<b>вы́разить</b>), không phải luật suy ra được.</div>'
    '<div class="hd-warn">Hay dùng để dẫn lời: «Нет», — <b>возрази́л</b> он. = «Không», anh ta '
    'cãi lại.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>возража́ть</b> (CHT) · <b>возраже́ние</b> lời phản bác · '
    '<b>выраже́ние</b> thành ngữ, nét mặt</div>'
)

# ------------------------------------------------------------------ возражать
S["возражать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">воз-</span>'
    '<span class="hd-gloss">ĐÁP TRẢ, ngược lại</span></div>'
    '<div class="hd-row"><span class="hd-piece">-раж-</span>'
    '<span class="hd-gloss">= <b>-раз-</b> «đánh», з hoá ж ở thể CHT (xem <b>возрази́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>возража́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>возрази́ть</b>. Phản bác AI ở cách 3 — '
    '<b>возража́ть ему́</b>; phản đối CÁI GÌ thì <b>про́тив</b> + cách 2 — '
    '<b>возража́ть про́тив пла́на</b>.</div>'
    '<div class="hd-warn">Câu xin phép lịch sự: <b>Вы не возража́ете, е́сли я откро́ю окно́?</b> = '
    'Anh có phiền không nếu tôi mở cửa sổ? Đáp <b>Не возража́ю</b> = cứ tự nhiên.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>возрази́ть</b> (HT) · <b>возраже́ние</b> lời phản bác · '
    '<b>выража́ть</b> bày tỏ (cùng <b>-раж-</b>)</div>'
)

# ---------------------------------------------------------------- возражение
S["возражение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">возраж-</span>'
    '<span class="hd-gloss">← <b>возрази́ть</b> phản bác, з hoá ж như ở <b>возража́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của cặp <b>возрази́ть</b> / <b>возража́ть</b>: lời phản bác, ý kiến '
    'phản đối. Mượn luôn ж của thể CHT, y như <b>выраже́ние</b> ← <b>выража́ть</b>.</div>'
    '<div class="hd-warn">Hỏi trong cuộc họp: <b>Возраже́ния есть?</b> = Có ai phản đối không? · '
    '<b>без возраже́ний</b> = không ai phản đối.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>возрази́ть</b> phản bác (HT) · <b>возража́ть</b> (CHT) · '
    '<b>выраже́ние</b> thành ngữ, nét mặt</div>'
)

# --------------------------------------------------------------- признаваться
S["признаваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">tiền tố, nghĩa ở đây mờ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-зна-</span>'
    '<span class="hd-gloss">BIẾT — gốc của <b>знать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва-ть-ся</span>'
    '<span class="hd-gloss">dấu thể chưa hoàn thành + đuôi + về chính mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>призна́ться</b>: thú nhận điều về chính mình. <b>-ва-</b> '
    'rụng ở hiện tại, trọng âm ra đuôi: <b>признаю́сь</b>, <b>признаёшься</b> — y khuôn '
    '<b>признава́ть</b>, <b>узнава́ть</b>. Điều thú nhận đi với <b>в</b> + cách 6: '
    '<b>признава́ться в оши́бке</b>.</div>'
    '<div class="hd-warn">Đầu câu <b>Признаю́сь, …</b> = Thú thật là… — chính là dạng hiện tại '
    'của từ này.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>призна́ться</b> (HT) · <b>признава́ть</b> thừa nhận · '
    '<b>призна́ние</b> lời thú nhận · <b>знать</b> biết</div>'
)

# ----------------------------------------------------------------- жаловаться
S["жаловаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">жа́л-</span>'
    '<span class="hd-gloss">THƯƠNG XÓT, tiếc — như <b>жаль</b>, <b>сожале́ние</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-ть-ся</span>'
    '<span class="hd-gloss">đuôi <b>-овать</b> (chia <b>-ую</b>) + phản thân</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Kể khổ cho người ta thương mình» ⇒ phàn nàn, kêu ca. <b>-ова-</b> thành '
    '<b>-у-</b> ở hiện tại, trọng âm đứng yên ở <b>жа́-</b>: <b>жа́луюсь</b>, <b>жа́луешься</b>. '
    'Cặp HT: <b>пожа́ловаться</b>.</div>'
    '<div class="hd-warn">Than CÁI GÌ: <b>на</b> + cách 4, với AI: cách 3 — '
    '<b>жа́ловаться врачу́ на головну́ю боль</b>. Bác sĩ mở đầu bằng: <b>На что жа́луетесь?</b> = '
    'Anh thấy khó chịu ở đâu?</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>жа́лоба</b> lời phàn nàn, đơn khiếu nại · <b>жаль</b> tiếc · '
    '<b>сожале́ние</b> sự tiếc nuối · <b>пожа́луйста</b> làm ơn</div>'
)

# ------------------------------------------------------------------ опоздание
S["опоздание"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">опозда-</span>'
    '<span class="hd-gloss">← <b>опозда́ть</b> đến muộn (gốc <b>позд-</b> MUỘN)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ние</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ đọc thẳng từ <b>опозда́ть</b>, trọng âm giữ ở <b>-да́-</b>. Trễ BAO '
    'LÂU vẫn dùng <b>на</b> + cách 4 như động từ: <b>опозда́ние на час</b> = trễ một tiếng.</div>'
    '<div class="hd-warn"><b>из-за опозда́ния</b> = vì đến muộn · <b>без опозда́ния</b> = đúng '
    'giờ, không trễ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>опозда́ть</b> đến muộn · <b>опа́здывать</b> (CHT) · <b>по́здно</b> muộn · '
    '<b>по́здний</b> muộn, khuya</div>'
)

# ---------------------------------------------------------------- продолжение
S["продолжение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">kéo tiếp về phía trước</span></div>'
    '<div class="hd-row"><span class="hd-piece">-долж-</span>'
    '<span class="hd-gloss">gốc DÀI — của <b>до́лгий</b>, г hoá ж</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>продолжа́ть</b> / <b>продо́лжить</b>: phần kéo DÀI thêm ⇒ sự '
    'tiếp tục, phần tiếp theo (tập sau của phim, của sách).</div>'
    '<div class="hd-warn"><b>Продолже́ние сле́дует</b> = Còn tiếp (cuối một tập phim, truyện dài kỳ).</div>'
    '<div class="hd-warn"><b>в продолже́ние</b> + cách 2 = trong suốt (văn viết): '
    '<b>в продолже́ние го́да</b> = suốt một năm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>продолжа́ть</b> tiếp tục · <b>продо́лжить</b> (HT) · <b>до́лгий</b> lâu, '
    'dài · <b>до́лго</b> lâu</div>'
)

# ------------------------------------------------------------------- вначале
S["вначале"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">giới từ <b>в</b> dính liền</span></div>'
    '<div class="hd-row"><span class="hd-piece">-нача́ле</span>'
    '<span class="hd-gloss">cách 6 của <b>нача́ло</b> phần đầu</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Ở trong phần đầu» ⇒ lúc đầu — thường báo trước rằng về sau đã khác: '
    '<b>Внача́ле бы́ло тру́дно, пото́м привы́к</b>. Lúc đầu thì khó, sau quen dần.</div>'
    '<div class="hd-warn">Có danh từ theo sau thì viết RỜI, + cách 2: <b>в нача́ле го́да</b> = vào '
    'đầu năm. Viết liền <b>внача́ле</b> chỉ khi nó đứng một mình.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>нача́ло</b> phần đầu · <b>нача́ть</b> bắt đầu · <b>снача́ла</b> trước '
    'tiên, lại từ đầu</div>'
)

# ------------------------------------------------------------------ накануне
S["накануне"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">giới từ <b>на</b> dính liền</span></div>'
    '<div class="hd-row"><span class="hd-piece">-кану́н-е</span>'
    '<span class="hd-gloss">cách 6 của <b>кану́н</b> ngày áp trước một dịp lễ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Vào hôm áp trước» ⇒ hôm trước đó. Đứng một mình: <b>Я звони́л ему́ '
    'накану́не</b>. Hôm trước tôi đã gọi cho anh ấy.</div>'
    '<div class="hd-warn">Làm giới từ thì kéo cách 2: <b>накану́не экза́мена</b> = hôm trước kỳ '
    'thi, ngay trước kỳ thi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кану́н</b> ngày áp lễ: <b>кану́н Но́вого го́да</b> đêm giao thừa</div>'
)

# -------------------------------------------------------------- впоследствии
S["впоследствии"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">giới từ <b>в</b> dính liền</span></div>'
    '<div class="hd-row"><span class="hd-piece">-после́дстви-и</span>'
    '<span class="hd-gloss">cách 6 của <b>после́дствие</b> hậu quả, «cái theo sau» — gốc '
    '<b>след-</b> như <b>после́дний</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Trong cái đến sau» ⇒ về sau, sau này: '
    '<b>Впосле́дствии он стал врачо́м</b>. Về sau anh ấy trở thành bác sĩ.</div>'
    '<div class="hd-warn">Từ của văn viết. Nói thường ngày thì dùng <b>пото́м</b> hoặc '
    '<b>по́зже</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>после́дствие</b> hậu quả · <b>после́дний</b> cuối cùng · '
    '<b>сле́дующий</b> tiếp theo · <b>по́сле</b> sau khi</div>'
)

# ------------------------------------------------------------ предварительный
S["предварительный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пред-</span>'
    '<span class="hd-gloss">TRƯỚC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вар-</span>'
    '<span class="hd-gloss">gốc cổ «đi trước, đón đầu»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-тельный</span>'
    '<span class="hd-gloss">hậu tố dựng tính từ từ động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thứ làm TRƯỚC việc chính ⇒ sơ bộ, tạm thời, đặt trước. Trạng từ '
    '<b>-о</b>: <b>предвари́тельно</b> = (làm) trước — <b>Позвони́те предвари́тельно</b>. Hãy gọi '
    'điện trước.</div>'
    '<div class="hd-warn">⚠️ Mức tin: <b>-вар-</b> là gốc cổ, đứng riêng không còn trong tiếng Nga '
    '— đừng nối với <b>вари́ть</b> nấu.</div>'
    '<div class="hd-warn"><b>предвари́тельная за́пись</b> = đăng ký, hẹn trước · <b>по '
    'предвари́тельным да́нным</b> = theo số liệu sơ bộ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">Cùng <b>пред-</b> TRƯỚC: <b>предупреди́ть</b> báo trước · '
    '<b>предсказа́ть</b> đoán trước</div>'
)

# --------------------------------------------------------------- сокращение
S["сокращение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-кращ-</span>'
    '<span class="hd-gloss">gốc NGẮN (<b>кра́ткий</b>), т hoá щ — từ <b>сократи́ть</b> làm ngắn lại</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Làm cho NGẮN lại» ⇒ cắt giảm, rút gọn. <b>крат-</b> chính là '
    '<b>корот-</b> của <b>коро́ткий</b> ở dạng Slavơ nhà thờ: оро ↔ ра, như <b>го́род</b> ↔ '
    '<b>-град</b>. т → щ trước <b>-ение</b>, như <b>посети́ть</b> → <b>посеще́ние</b>.</div>'
    '<div class="hd-warn">Cũng là CHỮ VIẾT TẮT, và cắt giảm biên chế: <b>попа́сть под '
    'сокраще́ние</b> = bị cho nghỉ việc vì cắt giảm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сократи́ть</b> / <b>сокраща́ть</b> cắt giảm · <b>кра́ткий</b> ngắn gọn · '
    '<b>коро́ткий</b> ngắn</div>'
)

# --------------------------------------------------------------------- вдвое
S["вдвое"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">«thành, vào»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дво́е</span>'
    '<span class="hd-gloss">thẻ <b>дво́е</b> — nhóm HAI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thành hai phần». Đi với so sánh hơn ⇒ GẤP ĐÔI: <b>вдво́е бо́льше</b> nhiều '
    'gấp đôi, <b>вдво́е доро́же</b> đắt gấp đôi. Đi với gập, cắt ⇒ LÀM ĐÔI: <b>сложи́ть вдво́е</b> '
    'gập đôi.</div>'
    '<div class="hd-warn"><b>вдво́е ме́ньше</b> = chỉ bằng MỘT NỬA — nghĩa «một nửa» ra từ đây. Đừng '
    'lẫn với <b>вдвоём</b> hai người cùng nhau.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дво́е</b> hai người · <b>втро́е</b> gấp ba · <b>вче́тверо</b> gấp bốn · '
    '<b>вдвоём</b> hai người cùng nhau</div>'
)

# ----------------------------------------------------------- приблизительный
S["приблизительный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">ĐẾN SÁT, tới gần</span></div>'
    '<div class="hd-row"><span class="hd-piece">-близ-</span>'
    '<span class="hd-gloss">GẦN — gốc của <b>бли́зкий</b>, <b>бли́зко</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-тельный</span>'
    '<span class="hd-gloss">hậu tố tính từ, từ <b>приблизи́ть</b> đưa lại gần</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đưa lại GẦN con số thật» ⇒ gần đúng, xấp xỉ. Lắp ráp y hệt tiếng Anh '
    'ap-proxim-ate: ap- = <b>при-</b> tới, proxim- = <b>близ-</b> gần. Trạng từ <b>-о</b> dùng '
    'nhiều hơn hẳn: <b>приблизи́тельно сто рубле́й</b> = khoảng một trăm rúp.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>приблизи́тельно</b> khoảng chừng · <b>прибли́зиться</b> đến gần · '
    '<b>бли́зкий</b> gần, thân · <b>бли́зко</b> ở gần</div>'
)

# --------------------------------------------------------------- приближаться
S["приближаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">ĐẾN SÁT, tới gần</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ближ-</span>'
    '<span class="hd-gloss">= <b>близ-</b> GẦN (<b>бли́зкий</b>), з hoá ж ở thể CHT</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть-ся</span>'
    '<span class="hd-gloss">đuôi CHT + phản thân, chia đều: <b>приближа́юсь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tự mình tiến lại GẦN ⇒ đến gần. ж này chính là ж trong <b>бли́же</b> gần '
    'hơn. Dùng cả cho thời gian: <b>Приближа́ется зима́</b>. Mùa đông đang tới gần.</div>'
    '<div class="hd-warn">Đến gần CÁI GÌ: <b>к</b> + cách 3 — <b>приближа́ться к до́му</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>прибли́зиться</b> (HT) · <b>бли́зкий</b> gần · <b>бли́же</b> gần hơn · '
    '<b>приблизи́тельный</b> gần đúng</div>'
)

# --------------------------------------------------------------- приблизиться
S["приблизиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">ĐẾN SÁT, tới gần</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бли́з-</span>'
    '<span class="hd-gloss">GẦN — gốc của <b>бли́зкий</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить-ся</span>'
    '<span class="hd-gloss">đuôi lớp chia 2 + phản thân</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp HT của <b>приближа́ться</b>: đã tới sát bên. Chỉ ngôi «tôi» đổi з → ж: '
    '<b>прибли́жусь</b>, còn lại giữ з — <b>прибли́зишься</b>; trọng âm đứng yên ở <b>-бли́-</b>. '
    'Cũng <b>к</b> + cách 3: <b>прибли́зиться к две́ри</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>приближа́ться</b> (CHT) · <b>бли́зкий</b> gần · <b>приблизи́тельный</b> '
    'gần đúng</div>'
)

# ------------------------------------------------------------------ нисколько
S["нисколько"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ни-</span>'
    '<span class="hd-gloss">phủ định NHẤN MẠNH — như <b>никто́</b>, <b>ничего́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ско́лько</span>'
    '<span class="hd-gloss">thẻ <b>ско́лько</b> — bao nhiêu</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Không bao nhiêu cả» ⇒ chẳng hề. Như mọi từ <b>ни-</b>, động từ vẫn phải có '
    '<b>не</b>: <b>Я ниско́лько не уста́л</b>. Tôi chẳng mệt chút nào. Đứng một mình làm câu đáp: '
    '<b>Ниско́лько!</b> = Không hề!</div>'
    '<div class="hd-warn">⚠️ Đừng lẫn với <b>не́сколько</b> «một vài»: <b>ни-</b> không nhấn → '
    '«không hề»; <b>не́-</b> mang trọng âm → «vài».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ско́лько</b> bao nhiêu · <b>не́сколько</b> một vài · <b>сто́лько</b> '
    'bấy nhiêu</div>'
)

# -------------------------------------------------------------------- трижды
S["трижды"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">три́-</span>'
    '<span class="hd-gloss"><b>три</b> ba</span></div>'
    '<div class="hd-row"><span class="hd-piece">-жды</span>'
    '<span class="hd-gloss">đuôi cổ «… lần», như <b>два́жды</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Anh em của <b>два́жды</b>, cùng đuôi với <b>одна́жды</b>. Bảng cửu chương: '
    '<b>Три́жды три — де́вять</b>. Đời thường hay nói <b>три ра́за</b>; <b>три́жды</b> nghe trang '
    'trọng hơn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>три</b> ba · <b>два́жды</b> hai lần · <b>одна́жды</b> một lần, một hôm</div>'
)

# ---------------------------------------------------------------------- треть
S["треть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">трет-</span>'
    '<span class="hd-gloss">từ <b>тре́тий</b> thứ BA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ь</span>'
    '<span class="hd-gloss">danh từ giống cái đuôi <b>-ь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Phần thứ ba» ⇒ một phần ba. Cùng khuôn: <b>че́тверть</b> một phần tư ← '
    '<b>четвёртый</b>. Hai phần ba = <b>две тре́ти</b>.</div>'
    '<div class="hd-warn">Số nhiều, trừ cách 1 và cách 4, trọng âm chạy ra đuôi: <b>трете́й</b>, '
    '<b>третя́м</b> — nhưng <b>две тре́ти</b> vẫn nhấn gốc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тре́тий</b> thứ ba · <b>три</b> ba · <b>че́тверть</b> một phần tư · '
    '<b>треуго́льник</b> tam giác</div>'
)

B = {
    "docbangmat": 134,
    "loitubat": 2,   # треть: «số nhiều từ cách 2 trở đi nhấn đuôi» sai ở cách 4 (тре́ти) -> «trừ cách 1 và cách 4»
                     # впоследствии: «nhìn từ một mốc trong quá khứ» nói quá (dùng được cả cho tương lai) -> bỏ
                     # (thêm 1 sửa nhỏ không tính: mảnh -вари- lệch với ô đỏ -вар- ở предварительный -> thống nhất -вар-)
    "nguonsai": 2,   # BAT THUONG «dạng ngắn có biến đổi» ở предварительный + приблизительный: thực ra đúng quy tắc
                     # chèn -е- (-телен), trọng âm đứng yên -> không viết câu chú ý (README: đúng quy tắc thì BỎ)
    "baolen": [
        "V cần duyệt (1): сокращение «sự cắt giảm, sự giảm bớt, sự rút ngắn, chữ viết tắt, sự tinh giản» — "
        "thêm «sự rút ngắn, chữ viết tắt» vì gloss có shortening/abbreviation/short form mà đề cũ thiếu hẳn. "
        "Đã chạy do_va_cham (chỉ đọc) trên 3695 thẻ với V thay vào: không đẻ va chạm mới, lô không dính va chạm nào.",
        "Chỗ KHÔNG chắc: рекомендовать ghi «một dạng dùng được cho CẢ HAI thể» (Ожегов: несов. и сов.) — "
        "nếu AspectBadge trên thẻ chỉ in một thể thì ô đỏ này lệch badge, luồng chính nên nhìn.",
        "Chỗ KHÔNG chắc: -вар- trong предварительный = gốc cổ Slavơ nhà thờ «đi trước» (đã gắn ⚠️ Mức tin, dặn đừng nối với "
        "вари́ть); «đánh» của -раз- trong возразить gắn Mức tin, thống nhất với вы́разить [k135]; воз- glossed «ĐÁP TRẢ, ngược lại».",
        "Khuôn -каз- chép đúng nguyên văn «NÓI, chỉ ra — gốc của сказа́ть, показа́ть», з → ж (вы́сказать/выска́зывать) — khớp k117, k195.",
        "Họ близ-: đã tự nối бли́зкий/бли́зко/бли́же [k53] (máy không thấy vì з↔ж); thẻ chính là приблизи́тельный.",
        "накануне: V hiện «hôm trước, ngày trước đó, trước ngày» — «trước ngày» hơi cụt nhưng khớp gloss on the eve of, để nguyên.",
    ],
}
