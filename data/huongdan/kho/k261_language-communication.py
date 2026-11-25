# -*- coding: utf-8 -*-
"""k261 — language::communication: họ «kể / nói / viết» với tiền tố + từ ghép hai gốc; trục là GỐC đã học.

Chỗ cần nhất quán với lô đã nạp:
(1) про- QUA + вод DẪN: khớp проводник k220. (2) без- KHÔNG CÓ: khớp безработный k233. (3) тур- CHUYẾN ĐI MỘT VÒNG
+ -и́зм NGÀNH: khớp турист k69, туристический k247. (4) пеш- ĐI CHÂN: khớp пешком k49. (5) -то «… nào đó»: khớp почему-то
k165. (6) -граф VIẾT, теле- XA: khớp география, телеграмма k89. (7) формул- CÔNG THỨC: khớp сформулировать k218.
(8) -с-каз- NÓI RA: khớp предсказать k221. (9) пере- QUA LẠI ở переписываться ↔ пере- LẠI ở пересказать: khớp переписка k218.
(10) раз- BUNG RA ở разговориться: khớp разговорить k77. (11) еже- MỖI: khớp ежедневный k147.
Họ hàng cố ý vắng: không có (từ nào cũng có họ thật).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "отчего-то": "chẳng rõ vì sao, chẳng hiểu sao",
    "пешеход": "người đi bộ, khách bộ hành",                    # «khách đi bộ» không phải tiếng Việt tự nhiên
    "затормозить": "phanh, giảm tốc, cản trở, kìm hãm",         # dãy chung với тормозить (đã nạp)
    "вполголоса": "bằng giọng nhỏ, hạ giọng, khe khẽ",          # «thì thào» sai: đó là шёпотом
    "телеграф": "điện báo, máy điện báo, trạm điện báo",        # «điện tín» là телегра́мма
    "формулировать": "diễn đạt, trình bày thành lời, phát biểu",  # dãy chung với сформулировать (đã nạp)
    "пересказать": "kể lại nội dung, thuật lại, diễn đạt lại",  # dãy chung của cặp; «tóm lại» ngoài gloss
    "пересказывать": "kể lại nội dung, thuật lại, diễn đạt lại",
    "разговориться": "bắt chuyện, trò chuyện rôm rả, trở nên nói nhiều",  # + become talkative; bỏ «mở lời»
    "систематически": "một cách có hệ thống, có phương pháp, đều đặn",  # + methodically; «thường xuyên» ngoài gloss
    "периодический": "định kỳ, theo chu kỳ, tuần hoàn",         # «thỉnh thoảng lặp lại» là lời giải thích
    "кратковременный": "trong thời gian ngắn, ngắn ngủi, thoáng qua",  # «tạm thời» là вре́менный; + momentary
}

# ----------------------------------------------------------------- газопровод
S["газопровод"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">газ-о-</span>'
    '<span class="hd-gloss">KHÍ ĐỐT — <b>газ</b>, cộng nguyên âm nối</span></div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">QUA, xuyên suốt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-во́д</span>'
    '<span class="hd-gloss">DẪN — <b>води́ть</b>, như <b>проводни́к</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cái dẫn khí đi suốt» ⇒ đường ống dẫn khí. Thay mảnh đầu là ra ống khác: '
    '<b>водопрово́д</b> ống nước, <b>нефтепрово́д</b> ống dẫn dầu.</div>'
    '<div class="hd-warn">Ống thì nhấn mảnh CUỐI: <b>газопрово́д, водопрово́д</b>. Đừng để '
    '<b>про́вод</b> (dây điện, nhấn đầu) kéo lệch — chính người Nga cũng hay nhấn sai chữ này.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>газ</b> khí đốt · <b>га́зовый</b> chạy bằng ga · '
    '<b>проводни́к</b> nhân viên toa tàu, chất dẫn điện · <b>про́вод</b> dây điện</div>'
)

# ---------------------------------------------------------------------- лицей
S["лицей"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn, không chẻ theo gốc Nga: Pháp <i>lycée</i> ← Latin <i>Lyceum</i> ← Hy Lạp '
    '<i>Lykeion</i>, khu vườn nơi Aristotle dạy học. Không dính gì tới <b>лицо́</b> khuôn mặt.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>lyceum</i>: ở Nga nay là trường trung học chuyên, học nặng một mảng '
    '(toán, lý…). Học Ở đó: <b>учи́ться в лице́е</b>. Đuôi <i>-й</i> nên là giống đực.</div>'
    '<div class="hd-warn"><b>лице́й</b> hay đi đôi với <b>гимна́зия</b> — cũng là trường chọn học sinh, nhưng '
    'truyền thống nghiêng về ngoại ngữ và khoa học xã hội.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лицеи́ст</b> học sinh trường này · <b>лице́йский</b> thuộc trường này</div>'
)

# ------------------------------------------------------------------ сбербанк
S["сбербанк"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сбер-</span>'
    '<span class="hd-gloss">TIẾT KIỆM — cắt ngắn từ <b>сберега́тельный</b>, gốc của <b>сбере́чь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ба́нк</span>'
    '<span class="hd-gloss">NGÂN HÀNG — <b>банк</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Ngân hàng để dành tiền». Là tên ngân hàng lớn nhất nước Nga nên thường viết hoa: '
    '<b>счёт в Сберба́нке</b> tài khoản ở Sberbank. Người Nga hay gọi tắt là <b>Сбер</b>.</div>'
    '<div class="hd-warn">Cắt ngắn chữ đầu rồi ghép là kiểu dựng từ rất Xô Viết: <b>сберка́сса</b> quỹ '
    'tiết kiệm, <b>сберкни́жка</b> sổ tiết kiệm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сбере́чь</b> tiết kiệm, bảo quản · <b>сбереже́ния</b> tiền để dành · '
    '<b>банк</b> ngân hàng · <b>банкома́т</b> máy ATM</div>'
)

# ------------------------------------------------------------------ безлюдный
S["безлюдный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">без-</span>'
    '<span class="hd-gloss">KHÔNG CÓ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лю́д-</span>'
    '<span class="hd-gloss">NGƯỜI — <b>лю́ди</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">→ tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không có người ⇒ vắng người, hoang vắng: <b>безлю́дная у́лица</b> phố vắng tanh. '
    'Bỏ <i>без-</i> là ra nghĩa ngược: <b>лю́дный</b> đông người.</div>'
    '<div class="hd-why"><b>Chú ý bảng chia:</b> dạng ngắn giống đực chèn <i>е</i> — <b>безлю́ден</b>; '
    'ba dạng kia đều đặn, trọng âm đứng yên.</div>'
    '<div class="hd-warn">«Đảo hoang» kiểu Robinson thì cụm quen là <b>необита́емый о́стров</b> (không ai ở).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лю́ди</b> người ta · <b>лю́дный</b> đông người · '
    '<b>многолю́дный</b> đông đúc · <b>безлю́дье</b> cảnh vắng người</div>'
)

# --------------------------------------------------------------------- туризм
S["туризм"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">тур-</span>'
    '<span class="hd-gloss">CHUYẾN ĐI MỘT VÒNG (Anh <i>tour</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́зм</span>'
    '<span class="hd-gloss">NGÀNH, chủ nghĩa — Anh <i>-ism</i>, luôn mang trọng âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>tourism</i>. <i>-и́ст</i> là NGƯỜI, <i>-и́зм</i> là NGÀNH: '
    '<b>тури́ст</b> khách du lịch ↔ <b>тури́зм</b> ngành du lịch. Giống đực, chỉ dùng số ít.</div>'
    '<div class="hd-warn">Tiếng Nga gọi cả chuyện đeo ba lô đi rừng núi là <b>тури́зм</b>: '
    '<b>пе́ший тури́зм</b> đi bộ đường dài, <b>го́рный тури́зм</b> đi núi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тур</b> chuyến du lịch · <b>тури́ст</b> khách du lịch · '
    '<b>туристи́ческий</b> (tính từ) du lịch</div>'
)

# ------------------------------------------------------------------- пешеход
S["пешеход"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пеш-</span>'
    '<span class="hd-gloss">ĐI CHÂN — <b>пе́ший</b>, <b>пешко́м</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е-</span>'
    '<span class="hd-gloss">nguyên âm nối (sau <i>ш</i> thì viết <i>е</i>, không viết <i>о</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-хо́д</span>'
    '<span class="hd-gloss">ĐI — <b>ходи́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Kẻ đi bằng chân» ⇒ người đi bộ. Cùng khuôn <b>теплохо́д</b> nhưng ở đây '
    '<i>-хо́д</i> là NGƯỜI, không phải tàu — nên cách 4 viết như cách 2: <b>пропусти́ть пешехо́да</b> '
    'nhường người đi bộ.</div>'
    '<div class="hd-warn"><b>пешехо́дный перехо́д</b> = vạch sang đường — chữ trên biển báo khắp nước Nga.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пешко́м</b> đi bộ (trạng từ) · <b>пешехо́дный</b> dành cho người đi bộ · '
    '<b>ходи́ть</b> đi · <b>перехо́д</b> lối qua đường</div>'
)

# --------------------------------------------------------------- затормозить
S["затормозить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">chỉ đánh dấu XONG, không thêm nghĩa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тормоз-</span>'
    '<span class="hd-gloss">CÁI PHANH — <b>то́рмоз</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́-ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đạp phanh một cái ⇒ phanh, giảm tốc: <b>Маши́на затормози́ла</b> Xe phanh lại. '
    '«Phanh» một công việc ⇒ cản trở, kìm hãm: <b>затормози́ть рабо́ту</b>. Cặp CHT: <b>тормози́ть</b>.</div>'
    '<div class="hd-why"><b>Chú ý bảng chia:</b> chỉ ngôi «tôi» biến âm <i>з → ж</i>, trọng âm ở đuôi suốt: '
    '<b>заторможу́, затормози́шь, затормозя́т</b>.</div>'
    '<div class="hd-warn"><b>ре́зко затормози́ть</b> = phanh gấp.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тормози́ть</b> (CHT) · <b>то́рмоз</b> cái phanh · '
    '<b>тормозно́й</b> thuộc về phanh · <b>торможе́ние</b> sự phanh</div>'
)

# ----------------------------------------------------------------- отчего-то
S["отчего-то"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">отчего́</span>'
    '<span class="hd-gloss">VÌ SAO — <i>от</i> từ + <i>чего</i>, cách 2 của <b>что</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-то</span>'
    '<span class="hd-gloss">«… nào đó» — có thật, chỉ là không biết</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Từ cái gì đó mà ra» ⇒ không hiểu sao: <b>Мне отчего́-то гру́стно</b> — không hiểu '
    'sao tôi thấy buồn. Cùng khuôn <b>кто́-то</b>; phép so <i>-то</i> ↔ <i>-нибудь</i> nằm ở thẻ đó.</div>'
    '<div class="hd-warn">Nghĩa y hệt <b>почему́-то</b>, chỉ ít dùng hơn và hay gặp trong truyện. Tự nói thì '
    'dùng <b>почему́-то</b>; gặp <b>отчего́-то</b> thì cần hiểu được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отчего́</b> vì sao · <b>оттого́</b> vì thế · '
    '<b>что́-то</b> cái gì đó · <b>заче́м-то</b> để làm gì đó</div>'
)

# ---------------------------------------------------------------- вполголоса
S["вполголоса"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">giới từ <b>в</b> dính liền, như <b>вслух</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">пол-</span>'
    '<span class="hd-gloss">NỬA — như <b>полго́да</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-го́лоса</span>'
    '<span class="hd-gloss">cách 2 của <b>го́лос</b> giọng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Ở mức nửa giọng» ⇒ bằng giọng nhỏ: <b>говори́ть вполго́лоса</b> nói khe khẽ. '
    'Cùng khuôn: <b>вполси́лы</b> nửa sức. Đã hoá trạng từ nên không biến đổi gì.</div>'
    '<div class="hd-warn">Nhỏ nhưng VẪN ra giọng. Thì thào không thành tiếng là <b>шёпотом</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>го́лос</b> giọng nói · <b>голосова́ть</b> bỏ phiếu («cất tiếng») · '
    '<b>полови́на</b> một nửa</div>'
)

# ------------------------------------------------------------------ телеграф
S["телеграф"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">теле-</span>'
    '<span class="hd-gloss">XA (Hy Lạp) — như <b>телефо́н</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-гра́ф</span>'
    '<span class="hd-gloss">VIẾT — như <b>геогра́фия</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Máy viết từ xa» = <i>telegraph</i>: hệ thống điện báo, cái máy, và cả nơi gửi điện. '
    'Trọng âm ở <i>-гра́ф</i>, khác <b>фото́граф, гео́граф</b>. Gửi BẰNG điện báo: <b>по телегра́фу</b>.</div>'
    '<div class="hd-warn"><b>телегра́ф</b> là máy, là trạm; tờ điện gửi đi là <b>телегра́мма</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>телегра́мма</b> bức điện · <b>телегра́фный</b> thuộc điện báo · '
    '<b>телеви́зор</b> tivi · <b>фото́граф</b> thợ ảnh</div>'
)

# ------------------------------------------------------------- формулировать
S["формулировать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">формул-</span>'
    '<span class="hd-gloss">CÔNG THỨC — <b>фо́рмула</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́рова-ть</span>'
    '<span class="hd-gloss">đuôi động từ gốc mượn</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đang đúc ý thành một «công thức» gọn ⇒ diễn đạt ra lời. Đúng Anh <i>formulate</i>. '
    'Đuôi <i>-овать → -ую</i>, trọng âm đứng yên: <b>формули́рую, формули́руешь</b>. '
    'Cặp HT: <b>сформули́ровать</b>.</div>'
    '<div class="hd-why">Cái được nói ra thì cách 4: <b>формули́ровать мы́сли</b> diễn đạt suy nghĩ.</div>'
    '<div class="hd-warn">Đừng lẫn <b>формирова́ть</b> tạo dựng (Anh <i>form</i>): không có <i>-ул-</i>, '
    'trọng âm ở <i>-ва́ть</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сформули́ровать</b> (HT) · <b>фо́рма</b> hình dạng, khuôn · '
    '<b>фо́рмула</b> công thức · <b>формулиро́вка</b> cách diễn đạt</div>'
)

# --------------------------------------------------------------- пересказать
S["пересказать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пере-</span>'
    '<span class="hd-gloss">LẠI, lần nữa — như <b>переписа́ть</b> chép lại</span></div>'
    '<div class="hd-row"><span class="hd-piece">-с-каз-</span>'
    '<span class="hd-gloss">NÓI RA — chính là <b>сказа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nói LẠI điều đã nghe, đã đọc bằng lời của mình. Cái gì: cách 4, cho ai: cách 3 — '
    '<b>пересказа́ть дру́гу фильм</b>. Cặp CHT: <b>переска́зывать</b>.</div>'
    '<div class="hd-why"><b>Chú ý bảng chia:</b> y hệt <b>сказа́ть</b> — <i>з → ж</i> ở mọi ngôi, trọng âm chỉ '
    'ở đuôi tại ngôi «tôi»: <b>перескажу́</b>, nhưng <b>переска́жешь, переска́жут</b>.</div>'
    '<div class="hd-warn"><b>рассказа́ть</b> = kể (chuyện gì cũng được); <b>пересказа́ть</b> = kể lại một nội '
    'dung CÓ SẴN: bài đọc, phim, lời người khác.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>переска́з</b> bài kể lại · <b>сказа́ть</b> nói · '
    '<b>расска́з</b> truyện ngắn · <b>ска́зка</b> truyện cổ tích</div>'
)

# ------------------------------------------------------------- пересказывать
S["пересказывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пере-</span>'
    '<span class="hd-gloss">LẠI, lần nữa — như <b>переписа́ть</b> chép lại</span></div>'
    '<div class="hd-row"><span class="hd-piece">-с-ка́з-</span>'
    '<span class="hd-gloss">NÓI RA — như <b>сказа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-ть</span>'
    '<span class="hd-gloss">hậu tố biến hoàn thành → CHƯA hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đang kể lại, hay kể lại. Thêm <i>-ыва-</i> thì trọng âm nhảy về ngay trước nó, y như '
    '<b>рассказа́ть → расска́зывать</b>; chia đều, giữ <i>з</i>: <b>переска́зываю, переска́зываешь</b> — '
    'dễ hơn hẳn cặp HT (<b>перескажу́</b>).</div>'
    '<div class="hd-warn">Cho ai: cách 3. <b>Не переска́зывай мне фильм!</b> Đừng kể nội dung phim cho tôi! — '
    'bảo ĐỪNG thì dùng thể này.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пересказа́ть</b> (HT) · <b>переска́з</b> bài kể lại · '
    '<b>расска́зывать</b> kể · <b>выска́зывать</b> bày tỏ</div>'
)

# ------------------------------------------------------------ переписываться
S["переписываться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пере-</span>'
    '<span class="hd-gloss">ở đây: QUA LẠI giữa hai bên — như <b>перепи́ска</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-пи́с-</span>'
    '<span class="hd-gloss">VIẾT — <b>писа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-ть-ся</span>'
    '<span class="hd-gloss">dấu thể CHƯA hoàn thành + <i>-ся</i> VỚI NHAU</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Viết qua viết lại với nhau ⇒ thư từ, nhắn tin. Với ai: <i>с</i> + cách 5 — '
    '<b>Я перепи́сываюсь с дру́гом</b>. Nghĩa này không có cặp HT, vì là việc kéo dài.</div>'
    '<div class="hd-warn">Bỏ <i>-ся</i> là đổi nghĩa: <b>перепи́сывать</b> = chép LẠI, viết lại.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>перепи́ска</b> thư từ qua lại · <b>писа́ть</b> viết · '
    '<b>письмо́</b> lá thư · <b>переписа́ть</b> chép lại</div>'
)

# ------------------------------------------------------------- разговориться
S["разговориться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раз-</span>'
    '<span class="hd-gloss">BUNG RA — như <b>разговори́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-говор-и́ть</span>'
    '<span class="hd-gloss">NÓI — <b>говори́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">TỰ MÌNH</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tự mình bung ra mà nói ⇒ bắt chuyện rồi càng lúc càng rôm rả. Khuôn '
    '<i>раз-…-ся</i> là «bắt đầu rồi càng lúc càng mạnh»: <b>распла́каться</b> oà khóc. Với ai: <i>с</i> + cách 5. '
    'Chia như <b>говори́ть</b>: <b>разговорю́сь, разговори́шься</b>.</div>'
    '<div class="hd-warn"><b>Мы разговори́лись в по́езде.</b> Chúng tôi bắt chuyện trên tàu. — Từ này là LÚC câu '
    'chuyện bén lên; còn «đang trò chuyện» là <b>разгова́ривать</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>говори́ть</b> nói · <b>разгово́р</b> cuộc nói chuyện · '
    '<b>разгово́рчивый</b> hay nói · <b>разговори́ть</b> gợi cho ai chịu nói</div>'
)

# ------------------------------------------------------------ систематически
S["систематически"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">систем-ат-</span>'
    '<span class="hd-gloss">HỆ THỐNG — <b>систе́ма</b>; <i>-ат-</i> là thân Hy Lạp, như '
    '<b>те́ма → темати́ческий</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́чески</span>'
    '<span class="hd-gloss">→ trạng từ — Anh <i>-ically</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>systematically</i>: làm có hệ thống, có phương pháp. Tính từ '
    '<i>-и́ческий</i> bỏ <i>й</i> là ra trạng từ, KHÔNG có đuôi <i>-о</i>: '
    '<b>системати́ческий → системати́чески</b>.</div>'
    '<div class="hd-warn">Gặp nhiều trong câu chê, nghĩa «hết lần này tới lần khác»: '
    '<b>Он системати́чески опа́здывает</b> — anh ta đi muộn đều đều.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>систе́ма</b> hệ thống · <b>системати́ческий</b> có hệ thống · '
    '<b>систематизи́ровать</b> hệ thống hoá</div>'
)

# --------------------------------------------------------------------- будни
S["будни"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бу́дн-</span>'
    '<span class="hd-gloss">NGÀY THƯỜNG, không phải ngày nghỉ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и</span>'
    '<span class="hd-gloss">đuôi số nhiều — từ này dùng ở số nhiều</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chuỗi ngày đi làm ⇒ ngày thường; rồi thành cả cuộc sống thường nhật đều đều: '
    '<b>трудовы́е бу́дни</b> những ngày làm việc. Ngược với <b>пра́здник</b> ngày lễ và <b>выходны́е</b> ngày nghỉ. '
    'Chia mềm: <b>бу́дней, бу́дням</b>.</div>'
    '<div class="hd-warn"><b>по бу́дням</b> = vào các ngày thường — chữ trên bảng giờ mở cửa.</div>'
    '<div class="hd-warn">⚠️ Mức tin: thường được nối với gốc <i>буд-</i> THỨC của <b>буди́ть</b> đánh thức («ngày '
    'phải dậy đi làm»); đó là từ nguyên, không phải luật suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бу́дничный</b> thường ngày, tẻ nhạt · <b>бу́дний день</b> ngày trong tuần</div>'
)

# ------------------------------------------------------------- периодический
S["периодический"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">период-</span>'
    '<span class="hd-gloss">THỜI KỲ, một vòng — <b>пери́од</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ческ-ий</span>'
    '<span class="hd-gloss">«thuộc về» — Anh <i>-ic</i>, luôn nhấn ở <i>и́</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>periodic</i>: cứ hết một vòng lại đến ⇒ định kỳ, tuần hoàn. Trọng âm bị kéo '
    'sang đuôi: <b>пери́од → периоди́ческий</b>.</div>'
    '<div class="hd-warn"><b>периоди́ческая систе́ма</b> = bảng tuần hoàn Mendeleev · '
    '<b>периоди́ческие изда́ния</b> = báo và tạp chí.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пери́од</b> thời kỳ · <b>периоди́чески</b> theo định kỳ · '
    '<b>перио́дика</b> báo chí định kỳ</div>'
)

# ----------------------------------------------------------- кратковременный
S["кратковременный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кратк-о-</span>'
    '<span class="hd-gloss">NGẮN — <b>кра́ткий</b>, cộng nguyên âm nối</span></div>'
    '<div class="hd-row"><span class="hd-piece">-времен-</span>'
    '<span class="hd-gloss">THỜI GIAN — thân của <b>вре́мя</b> (<b>вре́мени</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">→ tính từ (nên có hai chữ <i>н</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Có thời gian ngắn» ⇒ ngắn ngủi, thoáng qua. Thay mảnh đầu là ra nghĩa ngược: '
    '<b>долговре́менный</b> lâu dài.</div>'
    '<div class="hd-why"><b>Chú ý bảng chia:</b> dạng ngắn giống đực chèn <i>е</i> giữa hai chữ <i>н</i> — '
    '<b>кратковре́менен</b>; ba dạng kia đều đặn, trọng âm đứng yên.</div>'
    '<div class="hd-warn"><b>кратковре́менный дождь</b> = mưa thoáng qua — cụm quen của bản tin thời tiết.</div>'
    '<div class="hd-warn">Đừng lẫn <b>вре́менный</b> tạm thời: cái tạm thời vẫn có thể kéo dài nhiều năm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кра́ткий</b> ngắn gọn · <b>вре́мя</b> thời gian · '
    '<b>вре́менный</b> tạm thời · <b>совреме́нный</b> hiện đại</div>'
)

# -------------------------------------------------------------- ежемесячный
S["ежемесячный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">еже-</span>'
    '<span class="hd-gloss">MỖI — tiền tố cổ, nay chỉ còn trong từ chỉ thời gian</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ме́сяч-</span>'
    '<span class="hd-gloss">THÁNG — <b>ме́сяц</b>, <i>ц</i> hoá <i>ч</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">→ tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Mỗi tháng» ⇒ hằng tháng, cùng khuôn <b>ежедне́вный, ежего́дный</b>. <i>ц → ч</i> trước '
    '<i>н</i> y như <b>коне́ц → коне́чный</b>. Trạng từ: <b>ежеме́сячно</b>.</div>'
    '<div class="hd-warn"><b>ежеме́сячный платёж</b> = khoản trả hằng tháng (vay, trả góp).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ме́сяц</b> tháng · <b>ежеме́сячно</b> mỗi tháng · '
    '<b>ежедне́вный</b> hằng ngày · <b>ежего́дный</b> hằng năm</div>'
)

B = {
    "docbangmat": 104,
    "loitubat": 3,
    "nguonsai": 3,
    "baolen": [
        "отчего-то ↔ почему-то [k165 đã nạp] — cùng nghĩa thật, badge không tách; giữ nguyên, thẻ nói rõ отчего-то ít dùng hơn. Lệch nhẹ: отчего k196 ghi «mềm và văn nói hơn», thẻ này ghi «hay gặp trong truyện».",
        "nguonsai đếm 3 chỗ nghĩa Việt có sẵn bị bác: вполголоса «thì thào» (là шёпотом), телеграф «điện tín» (là телеграмма), кратковременный «tạm thời» (là временный). Không bác ô nào của bảng chia.",
        "затормозить — V dùng chung dãy với тормозить: phanh, giảm tốc, cản trở, kìm hãm; gloss EN chỉ có «brake or slow down», hai nghĩa sau lấy theo «slow down» + thẻ cặp (Ожегов có) — cần duyệt.",
        "пересказать/пересказывать — V chung «kể lại nội dung, thuật lại, diễn đạt lại»; bỏ «tóm lại»; tách рассказать bằng «kể lại nội dung» và «diễn đạt lại».",
        "безлюдный — gloss EN chỉ «uninhabited», hẹp: nghĩa thông dụng là «deserted, empty of people». V cũ (không có người, vắng người, hoang vắng) đúng, không sửa.",
        "разговориться — V bỏ «mở lời nói chuyện», thêm «trở nên nói nhiều» (become talkative). систематически — V bỏ «thường xuyên» (ngoài gloss), thêm «có phương pháp».",
        "будни — nối với будить là từ nguyên, đã gắn Mức tin. лицей — câu so với гимназия (nghiêng ngoại ngữ, xã hội) là xu hướng, không phải định nghĩa.",
        "переписываться — thẻ nói không có cặp HT ở nghĩa «thư từ qua lại»; переписаться (có trong từ điển) là chuyện khác / hiếm.",
    ],
}
