# -*- coding: utf-8 -*-
"""k198 — concepts::emotion: cảm xúc, tính cách, suy nghĩ.

Chỗ cần nhất quán trong lô:
(1) Bốn từ một họ пуга́ть / испуга́ть / пуга́ться / испуга́ться — CÙNG một khuôn chẻ:
    пуг- LÀM SỢ · ис- chỉ biến thành HT (không nghĩa riêng) · -ся = tự mình. Cách 2 (sợ cái gì)
    nói ở пуга́ться, испуга́ться nhắc lại một câu; ô đỏ боя́ться ↔ испуга́ться chỉ ở испуга́ться.
(2) обду́мать / обду́мывать: об- QUANH + дум- NGHĨ, khớp ду́мать [k54]; bẫy «đi thẳng cách 4,
    không có о» đặt ở обду́мать, обду́мывать dẫn chiếu.
(3) предпоче́сть / предпочита́ть: пред- TRƯỚC + по- + чт/чит- COI TRỌNG, ĐẾM — cùng gốc
    чита́ть, счита́ть, честь (đã tự kiểm: chia y hệt проче́сть). Bảng chia lệch ở thẻ HT,
    cấu trúc «cái chọn cách 4, cái gạt cách 3» ở thẻ CHT.
(4) надоеда́ть / надое́сть: на- + до- + есть ĂN (từ nguyên đã tự kiểm, chia y hệt есть).
    Cấu trúc đảo vai «Мне надое́ло» ở thẻ HT.
(5) волне́ние / взволно́ванный: «dậy sóng», khớp волна́ [k163] và волнова́ться [k98].
(6) чу́ткий: чут- ← чу́ять, cùng gốc чу́вство [k115]; сочу́вствие dùng lại cách chẻ чу́вство.
(7) оби́дный ← оби́да [k04]: об- + -ид- (ви́деть), không chẻ lại, chỉ dẫn chiếu.
Họ hàng không vắng ở thẻ nào (интуи́ция, наи́вный là từ mượn nhưng có phái sinh thông dụng).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "обдумать": "suy nghĩ kỹ, cân nhắc, nghĩ cho thấu",                 # bỏ «xong» trong «cân nhắc xong» — dấu thể trá hình, badge đã nói
    "волнение": "sự xúc động, sự hồi hộp, sự lo lắng, sự bồn chồn, sự náo động, biển động",  # THIẾU excitement · unrest/riots · swell/choppy water
    "чуткий": "nhạy cảm, tinh tế, tế nhị, biết quan tâm, thính, cảnh giác",  # THIẾU tactful · keen/acute (tai, mũi) · alert/watchful
    "обидный": "xúc phạm, làm tổn thương, chạm tự ái, gây tủi thân, đáng bực mình",  # THIẾU annoying/vexing/galling
    "благородный": "cao thượng, cao quý, hào hiệp, quý tộc",            # THIẾU noble (by birth)/aristocratic
    "взволнованный": "lo lắng, bồn chồn, xúc động, hồi hộp",            # THIẾU excited
    "пугать": "làm cho sợ, hù, dọa, làm giật mình",                    # THIẾU intimidate/cow
}

# --------------------------------------------------------------------- обдумать
S["обдумать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">QUANH, khắp mọi mặt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дум-</span>'
    '<span class="hd-gloss">NGHĨ — như <b>ду́мать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Nghĩ quanh mọi mặt» ⇒ suy nghĩ kỹ, cân nhắc thấu. Vế CHT thêm '
    '<b>-ыва-</b>: <b>обду́мывать</b>.</div>'
    '<div class="hd-warn">Khác <b>ду́мать о</b> + cách 6: <b>обду́мать</b> đi THẲNG cách 4, '
    'không giới từ — <b>обду́мать план</b> cân nhắc kỹ kế hoạch.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ду́мать</b> nghĩ · <b>приду́мать</b> nghĩ ra · '
    '<b>заду́маться</b> trầm ngâm · <b>обду́манный</b> có cân nhắc</div>'
)

# --------------------------------------------------------------------- обдумывать
S["обдумывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">QUANH, khắp mọi mặt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дум-</span>'
    '<span class="hd-gloss">NGHĨ — như <b>ду́мать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-ть</span>'
    '<span class="hd-gloss">kéo dài ⇒ thể CHT</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vế CHT của <b>обду́мать</b>: đang nghiền ngẫm, chưa chốt. Chia đều lớp 1: '
    '<b>обду́мываю, обду́мываешь</b>. Cũng đi thẳng cách 4 như <b>обду́мать</b>: '
    '<b>обду́мывать отве́т</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ду́мать</b> nghĩ · <b>обду́мать</b> (HT) · '
    '<b>заду́мываться</b> trầm ngâm · <b>обду́манный</b> có cân nhắc</div>'
)

# --------------------------------------------------------------------- предпочесть
S["предпочесть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пред-</span>'
    '<span class="hd-gloss">TRƯỚC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-по-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-че́сть</span>'
    '<span class="hd-gloss">gốc ĐẾM, COI TRỌNG — <b>чт</b>/<b>чит</b>/<b>чёт</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Coi trọng cái này TRƯỚC cái kia» ⇒ thích hơn, chọn hơn. Gốc chung với '
    '<b>чита́ть</b>, <b>счёт</b>, <b>честь</b> (từ nguyên, không phải luật).</div>'
    '<div class="hd-warn">Bảng chia không suy từ nguyên thể được — chia y hệt <b>проче́сть</b>: '
    '<b>предпочту́, предпочтёшь</b>; quá khứ <b>предпочёл, предпочла́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>предпочита́ть</b> (CHT) · <b>предпочте́ние</b> sự ưu tiên · '
    '<b>счита́ть</b> đếm, cho là · <b>честь</b> danh dự</div>'
)

# --------------------------------------------------------------------- предпочитать
S["предпочитать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пред-</span>'
    '<span class="hd-gloss">TRƯỚC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-по-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-чит-а-ть</span>'
    '<span class="hd-gloss">gốc ĐẾM, COI TRỌNG — như <b>чита́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vế CHT của <b>предпоче́сть</b> — gốc lộ rõ dạng <b>чит</b>, chia đều '
    'lớp 1: <b>предпочита́ю</b>. Dùng cho sở thích thường xuyên: tôi vốn thích … hơn.</div>'
    '<div class="hd-warn">Cái được chọn → cách 4, cái bị gạt → cách 3, không giới từ: '
    '<b>Я предпочита́ю чай ко́фе</b> = Tôi thích trà hơn cà phê.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>предпоче́сть</b> (HT) · <b>предпочте́ние</b> sự ưu tiên · '
    '<b>чита́ть</b> đọc · <b>счита́ть</b> đếm, cho là</div>'
)

# --------------------------------------------------------------------- интуиция
S["интуиция"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được trong tiếng Nga: mượn Latin <i>intuitio</i>, '
    'chính là Anh <i>intuition</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi <b>-ция</b> ứng đúng với Anh <i>-tion</i> (<b>ста́нция</b> '
    '<i>station</i>), luôn giống cái, và trọng âm luôn rơi vào âm tiết ngay TRƯỚC nó: '
    '<b>интуи́ция</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>интуити́вный</b> thuộc trực giác · <b>интуити́вно</b> theo trực giác</div>'
)

# --------------------------------------------------------------------- сочувствие
S["сочувствие"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">CÙNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-чу́вств-</span>'
    '<span class="hd-gloss">CẢM — <b>чу́вство</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ие</span>'
    '<span class="hd-gloss">→ danh từ, giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cảm CÙNG người khác» ⇒ đồng cảm — ghép y như Anh <i>sym-pathy</i> '
    '(<i>sym</i> cùng + <i>pathy</i> cảm). Chữ <b>в</b> đầu không đọc, như <b>чу́вство</b>.</div>'
    '<div class="hd-warn">Động từ <b>сочу́вствовать</b> + cách 3: <b>Я вам сочу́вствую</b> = '
    'Tôi rất thông cảm / chia buồn với anh.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>чу́вство</b> cảm giác · <b>чу́вствовать</b> cảm thấy · '
    '<b>сочу́вствовать</b> đồng cảm</div>'
)

# --------------------------------------------------------------------- вдохновение
S["вдохновение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дох-</span>'
    '<span class="hd-gloss">THỞ — như <b>вдох</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-нов-ение</span>'
    '<span class="hd-gloss">→ danh từ giống trung (từ <b>вдохнови́ть</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thổi hơi VÀO» ⇒ cảm hứng — trùng khít Anh <i>in-spire</i> '
    '(<i>in</i> vào + <i>spirare</i> thở). Ai truyền cảm hứng thì <b>вдохнови́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вдох</b> hơi hít vào · <b>вдохнови́ть</b> truyền cảm hứng · '
    '<b>вдохновля́ть</b> (CHT) · <b>дыша́ть</b> thở</div>'
)

# --------------------------------------------------------------------- волнение
S["волнение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">волн-</span>'
    '<span class="hd-gloss">SÓNG — <b>волна́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ, giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Sự dậy sóng» ở cả ba tầng: biển động (<b>волне́ние на мо́ре</b>), '
    'lòng xao động (hồi hộp, lo âu), xã hội dậy sóng — số nhiều <b>волне́ния</b> là náo động, '
    'bạo loạn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>волна́</b> con sóng · <b>волнова́ться</b> lo lắng · '
    '<b>взволно́ванный</b> xúc động</div>'
)

# --------------------------------------------------------------------- чуткий
S["чуткий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">чут-</span>'
    '<span class="hd-gloss">CẢM NHẬN, ĐÁNH HƠI — <b>чу́ять</b>, cùng gốc <b>чу́вство</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-ий</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cảm nhận nhanh» ⇒ thính (tai, mũi), rồi nhạy với người: tế nhị, '
    'biết quan tâm. Dạng ngắn chèn <b>о</b>, giống cái nhấn đuôi: <b>чу́ток, чутка́</b>.</div>'
    '<div class="hd-warn"><b>чу́ткий сон</b> = giấc ngủ tỉnh, động nhẹ là thức.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>чу́ять</b> đánh hơi · <b>чу́вство</b> cảm giác · '
    '<b>чу́ткость</b> sự tinh ý</div>'
)

# --------------------------------------------------------------------- упрямый
S["упрямый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố</span></div>'
    '<div class="hd-row"><span class="hd-piece">-прям-</span>'
    '<span class="hd-gloss">THẲNG — như <b>прямо́й</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đứng thẳng đơ, không chịu cúi» ⇒ cứng đầu, bướng; nói về sự cố gắng thì '
    'thành lì, bền bỉ: <b>упря́мо идти́ к це́ли</b> bền bỉ tiến tới đích.</div>'
    '<div class="hd-warn">⚠️ Mức tin: nối với <b>прямо́й</b> là từ nguyên, các nhà từ nguyên '
    'chưa thống nhất — dùng để nhớ, đừng suy ra luật.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>упря́мство</b> tính bướng · <b>упря́мо</b> bướng bỉnh, kiên trì · '
    '<b>упря́миться</b> giở bướng</div>'
)

# --------------------------------------------------------------------- наивный
S["наивный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">наи́в-</span>'
    '<span class="hd-gloss">mượn Pháp <i>naïf</i> — Anh <i>naive</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ tiếng Nga</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc mượn, chỉ gắn thêm đuôi Nga. <b>а</b> và <b>и</b> đọc tách hai âm, '
    'nhấn <b>и́</b>. Dạng ngắn chèn <b>е</b>: <b>наи́вен, наи́вна</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>наи́вность</b> sự ngây thơ · <b>наи́вно</b> một cách ngây thơ</div>'
)

# --------------------------------------------------------------------- обидный
S["обидный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">оби́д-</span>'
    '<span class="hd-gloss">NỖI TỦI — <b>оби́да</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">→ tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Gây ra <b>оби́да</b>» ⇒ xúc phạm, làm tủi: <b>оби́дные слова́</b>. '
    'Dạng ngắn trung tính là câu hằng ngày: <b>Мне оби́дно</b> tôi thấy tủi · <b>Оби́дно!</b> '
    'Cay thật!</div>'
    '<div class="hd-warn"><b>оби́дный</b> nói về CÁI gây tủi; NGƯỜI hay tự ái là '
    '<b>оби́дчивый</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оби́да</b> nỗi tủi · <b>оби́деть</b> làm ai tủi · '
    '<b>оби́деться</b> tự ái</div>'
)

# --------------------------------------------------------------------- благородный
S["благородный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">благо-</span>'
    '<span class="hd-gloss">TỐT LÀNH — <b>бла́го</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-род-</span>'
    '<span class="hd-gloss">DÒNG DÕI — <b>род</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">→ tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Dòng dõi tốt» ⇒ quý tộc, rồi nghĩa bóng: cao thượng — như Anh '
    '<i>noble</i> cũng mang cả hai. Dạng ngắn chèn <b>е</b>: <b>благоро́ден</b>.</div>'
    '<div class="hd-warn"><b>благоро́дные мета́ллы</b> = kim loại quý (vàng, bạc).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>благоро́дство</b> sự cao thượng · <b>род</b> dòng giống · '
    '<b>родно́й</b> ruột thịt · <b>благодари́ть</b> cảm ơn</div>'
)

# --------------------------------------------------------------------- взволнованный
S["взволнованный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вз-</span>'
    '<span class="hd-gloss">BỪNG LÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-волн-</span>'
    '<span class="hd-gloss">SÓNG — <b>волна́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-нн-ый</span>'
    '<span class="hd-gloss">phân từ bị động: «bị làm cho…»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Bị khuấy cho dậy sóng» ⇒ xúc động, bồn chồn — trạng thái SAU khi bị '
    '<b>взволнова́ть</b>. Nói về mình thường dùng dạng ngắn: <b>Я взволно́ван</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>волна́</b> con sóng · <b>волнова́ться</b> lo lắng · '
    '<b>волне́ние</b> sự xúc động · <b>взволнова́ть</b> làm xao động</div>'
)

# --------------------------------------------------------------------- пугать
S["пугать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пуг-</span>'
    '<span class="hd-gloss">LÀM SỢ — gốc trơn, nhớ thẳng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi động từ, chia đều lớp 1</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cả họ bốn từ đều từ gốc này: thêm <b>ис-</b> ⇒ HT <b>испуга́ть</b>; '
    'thêm <b>-ся</b> ⇒ tự mình sợ <b>пуга́ться</b>. Người bị dọa → cách 4: '
    '<b>Не пуга́й меня́!</b> Đừng dọa tôi!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>испу́г</b> cơn hoảng sợ · <b>пу́гало</b> bù nhìn · '
    '<b>пугли́вый</b> nhát, dễ giật mình · <b>напуга́ть</b> làm sợ (HT)</div>'
)

# --------------------------------------------------------------------- испугать
S["испугать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ис-</span>'
    '<span class="hd-gloss">chỉ biến thành HT — không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пуг-а-ть</span>'
    '<span class="hd-gloss">LÀM SỢ — <b>пуга́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một lần dọa, có kết quả: <b>Ты меня́ испуга́л!</b> Anh làm em hết hồn! '
    'Chia đều lớp 1 như <b>пуга́ть</b>, người bị dọa vẫn ở cách 4.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пуга́ть</b> (CHT) · <b>испуга́ться</b> hoảng sợ · '
    '<b>испу́г</b> cơn hoảng sợ</div>'
)

# --------------------------------------------------------------------- пугаться
S["пугаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пуг-а-ть</span>'
    '<span class="hd-gloss">LÀM SỢ — <b>пуга́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">tự mình — tự làm mình sợ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Tự thấy sợ» ⇒ sợ, giật mình. Vế CHT, hợp nói thói quen: '
    '<b>Она́ всегда́ пуга́ется гро́ма</b> cô ấy lần nào cũng giật mình vì sấm.</div>'
    '<div class="hd-warn">Sợ CÁI GÌ → cách 2, như <b>боя́ться</b>: <b>пуга́ться соба́к</b> '
    'hay giật mình vì chó.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пуга́ть</b> làm sợ · <b>испуга́ться</b> (HT) · '
    '<b>пугли́вый</b> nhát, dễ giật mình</div>'
)

# --------------------------------------------------------------------- испугаться
S["испугаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ис-</span>'
    '<span class="hd-gloss">chỉ biến thành HT — không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пуг-а-ть</span>'
    '<span class="hd-gloss">LÀM SỢ — <b>пуга́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">tự mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Khoảnh khắc hoảng lên: <b>Я испуга́лся</b> tôi giật thót. Sợ cái gì vẫn '
    'cách 2 như <b>пуга́ться</b>: <b>испуга́ться темноты́</b>.</div>'
    '<div class="hd-warn"><b>боя́ться</b> = sợ kéo dài (trạng thái) · <b>испуга́ться</b> = '
    'hoảng lên một lúc, vì bị bất ngờ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>испуга́ть</b> làm sợ · <b>пуга́ться</b> (CHT) · '
    '<b>испу́г</b> cơn hoảng sợ</div>'
)

# --------------------------------------------------------------------- надоедать
S["надоедать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">ĐẦY, tới mức đủ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-до-</span>'
    '<span class="hd-gloss">TỚI TẬN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-еда́-ть</span>'
    '<span class="hd-gloss">ĂN — <b>есть</b>, <b>еда́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Ăn tới tận ngán» ⇒ làm phát chán, quấy rầy. Vế CHT của '
    '<b>надое́сть</b>, chia đều lớp 1: <b>надоеда́ю, надоеда́ешь</b>. Người bị phiền '
    'ở cách 3, như <b>надое́сть</b>: <b>Не надоеда́й мне!</b> Đừng quấy tôi!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>есть</b> ăn · <b>еда́</b> đồ ăn · <b>надое́сть</b> (HT) · '
    '<b>надое́дливый</b> phiền phức</div>'
)

# --------------------------------------------------------------------- надоесть
S["надоесть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">ĐẦY, tới mức đủ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-до-</span>'
    '<span class="hd-gloss">TỚI TẬN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-есть</span>'
    '<span class="hd-gloss">ĂN — chính là <b>есть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Ăn tới tận ngán» ⇒ chán ngấy. Bảng chia không suy từ nguyên thể được — '
    'chia y hệt <b>есть</b>: <b>надое́ст, надоеди́м, надоедя́т</b>; quá khứ <b>надое́л</b>.</div>'
    '<div class="hd-warn">Đảo vai: cái gây chán làm CHỦ NGỮ, người chán ở cách 3 — '
    '<b>Мне надое́ло!</b> Tôi chán lắm rồi! · <b>Ты мне надое́л.</b> Tôi ngán anh rồi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>есть</b> ăn · <b>еда́</b> đồ ăn · <b>надоеда́ть</b> (CHT) · '
    '<b>надое́дливый</b> phiền phức</div>'
)

# --------------------------------------------------------------------- нервничать
S["нервничать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">нерв-</span>'
    '<span class="hd-gloss">DÂY THẦN KINH (Anh <i>nerve</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-нича-ть</span>'
    '<span class="hd-gloss">đuôi động từ chỉ một kiểu cư xử (như <b>безде́льничать</b> '
    'ăn không ngồi rồi)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cư xử như thần kinh đang căng» ⇒ bồn chồn, căng thẳng ngay lúc này (còn tính khí '
    'thì <b>не́рвный</b>). Chia đều lớp 1: <b>не́рвничаю, не́рвничаешь</b>.</div>'
    '<div class="hd-warn"><b>Не не́рвничай!</b> = Bình tĩnh nào, đừng cuống!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>нерв</b> dây thần kinh · <b>не́рвный</b> dễ kích động</div>'
)

B = {
    "docbangmat": 89,
    "loitubat": 2,   # пугаться: câu ví dụ hỏng («Она пугается те́мноты? Không — xem ô đỏ»), trọng âm sai те́мноты (đúng темноты́) -> thay bằng пуга́ется гро́ма
                     # надоедать: viết «Đảo vai như надое́сть» cho câu Не надоеда́й мне — câu đó KHÔNG đảo vai (chủ ngữ là người quấy) -> chỉ nói «người bị phiền ở cách 3»
    "nguonsai": 0,   # ba khớp họ máy báo đều tự kiểm: предпочесть <- чт/чит (chia y hệt прочесть) ĐÚNG; надоесть <- есть ĂN (chia y hệt есть) ĐÚNG; упрямый <- прямой KHÔNG chắc (xem baolen)
    "baolen": [
        "Chỗ KHÔNG chắc: упрямый ↔ прямой — giữ cách chẻ -прям- THẲNG nhưng gắn ô đỏ «⚠️ Mức tin… các nhà từ nguyên chưa thống nhất»; KHÔNG đưa прямой vào Họ hàng.",
        "Mức tin vừa (ghi «từ nguyên, không phải luật» ngay trên thẻ): предпочесть/предпочитать cùng gốc чита́ть, счёт, честь. Cấu tạo пред-+по-+чт/чит và bảng chia giống прочесть thì chắc.",
        "Bác ngầm dữ liệu từ điển: dạng ngắn giống cái взволно́ванна (từ điển in) — chỉ viết «Я взволно́ван», né cặp -нна/-на (phân từ thường viết взволно́вана); không khẳng định dạng nào.",
        "сочувствие ↔ Anh sym-pathy và вдохновение ↔ in-spire: viết là «ghép y như», KHÔNG khẳng định là dịch sao phỏng (calque).",
        "V cần duyệt (7 thẻ): обдумать (bỏ «xong» trong «cân nhắc xong» — dấu thể trá hình) · волнение (THÊM sự hồi hộp, sự náo động, biển động — excitement/unrest/swell) · чуткий (THÊM tế nhị, thính, cảnh giác — tactful/keen/alert) · обидный (THÊM gây tủi thân, đáng bực mình — annoying/vexing) · благородный (THÊM quý tộc — noble by birth) · взволнованный (THÊM hồi hộp — excited) · пугать (THÊM dọa — intimidate). 14 thẻ còn lại đề cũ đã đúng, không viết V.",
        "Trùng nghĩa trong lô đều được badge tách: пугать/испугать & пугаться/испугаться (thể), пугать/пугаться (phản thân), обдумать/обдумывать, предпочесть/предпочитать, надоедать/надоесть (thể). Không có ca phải báo.",
    ],
}
