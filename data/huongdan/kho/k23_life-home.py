# -*- coding: utf-8 -*-
"""k23 — life::home: đồ đạc và bộ phận trong nhà.

Trục của lô: phần lớn là từ MƯỢN đã Nga hoá (ва́за, ла́мпа, кварти́ра, эта́ж,
зал, утю́г, ко́мната) đứng cạnh vài từ gốc Nga có bảng chia gồ ghề
(ло́жка/ба́лка/по́лка/поду́шка chèn nguyên âm ở số nhiều cách 2;
стена́/утю́г/эта́ж/нож/потоло́к kéo trọng âm xuống đuôi).
Luật chèn nguyên âm giải thích ĐỦ đúng một lần ở ло́жка, các thẻ sau dẫn chiếu.
"""

S = {}
V = {}

# ---------------------------------------------------------------- ваза
S["ваза"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn nguyên khối từ tiếng Pháp '
    '<i>vase</i> (gốc La-tinh <i>vas</i> = đồ đựng). Chỉ đuôi -а là của tiếng '
    'Nga, và chính nó kéo từ này vào lớp danh từ giống cái.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng chữ "vase" của tiếng Anh, chỉ khoác thêm đuôi -а. '
    'Biến cách đều đặn, không có chỗ nào phải nhớ riêng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ва́зочка</b> lọ nhỏ, chén nhỏ (đựng mứt, kem)</div>'
)

# ---------------------------------------------------------------- ложка
S["ложка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">лож-</span>'
    '<span class="hd-gloss">gốc cổ, nay không tách ra nghĩa riêng được</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái (ở đây KHÔNG có nghĩa "nhỏ")</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Số nhiều cách 2 mất sạch đuôi, hai phụ âm ж-к dồn vào '
    'nhau nên tiếng Nga chèn một nguyên âm vào giữa: <b>ло́жек</b>. Luật này lặp '
    'ở mọi danh từ đuôi -ка trong lô — chèn е sau ж·ч·ш·щ và phụ âm mềm, chèn о '
    'sau phụ âm cứng.</div>'
    '<div class="hd-warn">📌 Đơn vị đo trong mọi công thức nấu ăn: '
    '<b>ча́йная ло́жка</b> thìa cà phê · <b>столо́вая ло́жка</b> thìa canh.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ло́жечка</b> thìa nhỏ</div>'
)

# ---------------------------------------------------------------- балка
S["балка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn từ tiếng Đức / Hà Lan '
    '(<i>Balken</i>, <i>balk</i> = thanh gỗ ngang). Đuôi -ка ở đây chỉ là vỏ '
    'Nga hoá, không mang nghĩa "nhỏ".</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhớ bằng hình: thanh xà ngang đỡ trần và sàn. Số nhiều '
    'cách 2 chèn о — <b>ба́лок</b>, cùng luật với <b>ло́жка</b> → <b>ло́жек</b>.</div>'
    '<div class="hd-warn">⚠️ Đồng tự: <b>ба́лка</b> còn nghĩa "khe cạn, hẻm núi" '
    'ở vùng thảo nguyên miền Nam — hai từ khác gốc trùng mặt chữ, phải đoán '
    'bằng ngữ cảnh.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>балко́н</b> ban công — cùng nguồn Giéc-manh, vào '
    'tiếng Nga qua tiếng Ý (từ nguyên, không phải luật suy ra được)</div>'
)

# ---------------------------------------------------------------- полка
S["полка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пол-</span>'
    '<span class="hd-gloss">tấm ván (cùng gốc với <b>пол</b> = sàn nhà)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">"Tấm ván gắn lên tường" chính là cái kệ. Số nhiều cách '
    '2 chèn о: <b>по́лок</b> (như <b>ло́жка</b> → <b>ло́жек</b>).</div>'
    '<div class="hd-warn">⚠️ Cùng mặt chữ nhưng là hai từ khác hẳn, tách bằng '
    'trọng âm: <b>по́лка</b> cái kệ — còn <b>полка́</b> là cách 2 của '
    '<b>полк</b> "trung đoàn".</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>по́лочка</b> kệ nhỏ · <b>пол</b> sàn nhà — cùng gốc "tấm ván"</div>'
)

# ---------------------------------------------------------------- подушка
S["подушка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span>'
    '<span class="hd-gloss">dưới</span></div>'
    '<div class="hd-row"><span class="hd-piece">-душ-</span>'
    '<span class="hd-gloss">gốc "thổi phồng" (cùng họ với <b>дуть</b> thổi)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: cái được thổi phồng lên để kê xuống dưới. '
    'Số nhiều cách 2 chèn е sau ш — <b>поду́шек</b>, cùng luật với '
    '<b>ло́жка</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: rất nhiều người tách поду́шка = под + '
    'у́хо ("kê dưới tai"). Nghe hợp lý nhưng đó là từ nguyên dân gian; các từ '
    'điển từ nguyên nối nó với дуть "thổi phồng". Cả hai đều là từ nguyên, '
    'không phải luật suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поду́шечка</b> gối nhỏ; viên kẹo dẹt</div>'
)

# ---------------------------------------------------------------- дома
S["дома"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дом-</span>'
    '<span class="hd-gloss">NHÀ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi của một cách cũ, đã đông cứng thành trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bộ ba phải thuộc, khác nhau ở HƯỚNG: <b>до́ма</b> đang '
    'ở nhà (đứng yên) — <b>домо́й</b> về nhà (đi tới) — <b>из до́ма</b> ra khỏi '
    'nhà (đi khỏi).</div>'
    '<div class="hd-warn">⚠️ Ba mặt chữ trông như một: <b>до́ма</b> trạng từ "ở '
    'nhà" · <b>до́ма</b> cách 2 của <b>дом</b> (о́коло до́ма = cạnh ngôi nhà) · '
    '<b>дома́</b> số nhiều "những ngôi nhà".</div>'
    '<div class="hd-warn">⚠️ <b>до́ма</b> không đi kèm giới từ nào: nói '
    '<b>я до́ма</b> = tôi ở nhà. Muốn nói "ở trong ngôi nhà" mới dùng '
    '<b>в до́ме</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дом</b> ngôi nhà · <b>дома́шний</b> thuộc về nhà · '
    '<b>домо́й</b> về nhà</div>'
)

# ---------------------------------------------------------------- стена
S["стена"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn стен-, không chẻ nhỏ thêm được; -а là đuôi '
    'giống cái.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trọng âm ĐỘNG: dạng nguyên nặng ở đuôi <b>стена́</b>, '
    'nhưng cách 4 số ít lùi về gốc — <b>сте́ну</b>, và số nhiều cách 1 cũng vậy '
    '— <b>сте́ны</b>. Các cách sau của số nhiều lại xuống đuôi: '
    '<b>стена́ми</b> (cách 5), о <b>стена́х</b> (cách 6).</div>'
    '<div class="hd-warn">📌 Thành ngữ hay gặp: <b>как об сте́ну горо́х</b> — '
    'nói mãi mà không vào, đúng kiểu "nước đổ đầu vịt".</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сте́нка</b> vách, thành (nồi, tủ) · <b>стенно́й</b> '
    'gắn tường — <b>стенны́е часы́</b> đồng hồ treo tường</div>'
)

# ---------------------------------------------------------------- корзина
S["корзина"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">корз-</span>'
    '<span class="hd-gloss">gốc đã mờ nghĩa, không tách thêm được</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ина</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái, cùng khuôn với <b>карти́на</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng khuôn -ина và cùng chỗ trọng âm với '
    '<b>карти́на</b> ngay trong lô này — nhớ một lần được cả hai. Biến cách '
    'đều đặn, không có gì bất thường.</div>'
    '<div class="hd-warn">⚠️ Chỉ khác nhau đúng hai chữ cái: <b>корзи́на</b> '
    'cái giỏ — <b>карти́на</b> bức tranh. Đọc kỹ trước khi gõ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>корзи́нка</b> giỏ nhỏ · <b>му́сорная корзи́на</b> '
    'sọt rác</div>'
)

# ---------------------------------------------------------------- картина
S["картина"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">карт-</span>'
    '<span class="hd-gloss">từ <b>ка́рта</b> — tấm bìa, tờ giấy dày</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ина</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái, cùng khuôn với <b>корзи́на</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">"Tấm giấy có hình vẽ trên đó" → bức tranh. Gốc '
    '<i>charta</i> La-tinh cũng đẻ ra card, chart, carton của tiếng Anh.</div>'
    '<div class="hd-warn">⚠️ <b>карти́на</b> là tranh VẼ (sơn dầu, treo tường), '
    'hoặc bộ phim. Ảnh CHỤP là <b>фотогра́фия</b> / <b>сни́мок</b> — chớ dùng '
    'карти́на cho ảnh chụp.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ка́рта</b> bản đồ; quân bài · <b>карти́нка</b> hình '
    'nhỏ, tranh minh hoạ · <b>ка́рточка</b> tấm thẻ</div>'
)

# ---------------------------------------------------------------- лампа
S["лампа"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn qua tiếng Đức / Pháp '
    '(<i>Lampe</i>, <i>lampe</i>), gốc Hy Lạp <i>lampas</i> = ngọn đuốc. Đuôi '
    '-а là phần Nga hoá, kéo từ này vào giống cái.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng chữ "lamp" của tiếng Anh. Biến cách đều đặn, '
    'trọng âm đứng yên ở âm đầu qua mọi cách.</div>'
    '<div class="hd-warn">📌 <b>ла́мпа</b> là CẢ CÂY đèn (đèn bàn, đèn trần); '
    'cái bóng vặn vào là <b>ла́мпочка</b>. "Bật đèn lên" trong nhà thì nói '
    '<b>включи́ть свет</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ла́мпочка</b> bóng đèn · <b>насто́льная ла́мпа</b> '
    'đèn bàn</div>'
)

# ---------------------------------------------------------------- квартира
S["квартира"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được trong tiếng Nga: mượn từ tiếng Đức '
    '<i>Quartier</i> "chỗ trú quân", gốc La-tinh <i>quartus</i> = thứ tư.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bắc cầu sang tiếng Anh: "quarters" (chỗ ở, doanh trại) '
    'và "quarter" (một phần tư) — cùng một gốc <i>quartus</i>.</div>'
    '<div class="hd-warn">⚠️ Ba cỡ, đừng lẫn: <b>дом</b> cả toà nhà — '
    '<b>кварти́ра</b> một căn hộ trong toà đó — <b>ко́мната</b> một phòng bên '
    'trong căn hộ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кварти́рный</b> thuộc căn hộ · <b>квартпла́та</b> '
    'tiền nhà hằng tháng · <b>кварта́л</b> khu phố (cùng gốc "phần tư")</div>'
)

# ---------------------------------------------------------------- комната
S["комната"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn qua tiếng Ba Lan từ La-tinh trung '
    'cổ <i>caminata</i> = "phòng có lò sưởi" (<i>caminus</i> = lò sưởi).</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính <i>caminus</i> đó đẻ ra chữ "chimney" (ống khói) '
    'của tiếng Anh: căn phòng đáng gọi là phòng là căn có lò sưởi.</div>'
    '<div class="hd-warn">⚠️ Mức tin: đây là từ nguyên, không phải luật suy ra '
    'được từ mặt chữ tiếng Nga — mặt chữ ко́мната nay không còn mảnh nào tự nói '
    'lên nghĩa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ко́мнатный</b> trong nhà — <b>ко́мнатные '
    'расте́ния</b> cây cảnh trong nhà, <b>ко́мнатная температу́ра</b> nhiệt độ '
    'phòng</div>'
)

# ---------------------------------------------------------------- утюг
S["утюг"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn từ các thứ tiếng Turk '
    '(<i>ütü</i> = là, ủi). Vào tiếng Nga là một khối trơn.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trọng âm dính chặt vào ĐUÔI: hễ có đuôi là nó nhảy '
    'theo — <b>утюга́</b> (cách 2), <b>утюго́м</b> (cách 5), số nhiều '
    '<b>утюги́</b>. Không bao giờ lùi về đầu từ.</div>'
    '<div class="hd-warn">📌 "Là quần áo" hằng ngày nói <b>гла́дить</b> / '
    '<b>погла́дить</b>. <b>утю́жить</b> nghe mạnh hơn, gần "cán cho phẳng lì".</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>утю́жить</b> là phẳng, cán phẳng</div>'
)

# ---------------------------------------------------------------- этаж
S["этаж"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn thẳng từ tiếng Pháp '
    '<i>étage</i> (tầng, bậc).</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trọng âm luôn ở đuôi: <b>этажа́</b> (cách 2), số nhiều '
    '<b>этажи́</b>. Cách đếm tầng giống tiếng Việt — tầng 1 là tầng sát mặt '
    'đất, khác kiểu "ground floor" của tiếng Anh.</div>'
    '<div class="hd-warn">📌 "Ở tầng mấy" đi với на + cách 6, không dùng в: '
    '<b>на пе́рвом этаже́</b> = ở tầng một.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>этаже́рка</b> kệ nhiều tầng (cũng từ tiếng Pháp) · '
    '<b>двухэта́жный</b> hai tầng · <b>многоэта́жка</b> nhà cao tầng</div>'
)

# ---------------------------------------------------------------- нож
S["нож"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn нож-, không chẻ nhỏ thêm được. Danh từ giống '
    'đực, dạng nguyên không có đuôi.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dạng nguyên chỉ một âm nên nhìn tưởng trọng âm đứng '
    'yên; thật ra hễ thêm đuôi là nó xuống đuôi: <b>ножа́</b> (cách 2), '
    '<b>ножо́м</b> (cách 5), số nhiều <b>ножи́</b>, <b>ноже́й</b>.</div>'
    '<div class="hd-warn">⚠️ Đừng lẫn với <b>но́жка</b> = cái chân nhỏ (chân '
    'bàn, chân ghế) — nó ra từ <b>нога́</b> "chân", không liên quan tới dao.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>но́жницы</b> cái kéo (chỉ dùng số nhiều) · '
    '<b>но́жик</b> dao nhỏ · <b>ножо́вка</b> cưa tay</div>'
)

# ---------------------------------------------------------------- потолок
S["потолок"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố cổ, nay không tách ra nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тол-</span>'
    '<span class="hd-gloss">gốc "nền, đáy" (từ nguyên; nay không dùng riêng)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ок</span>'
    '<span class="hd-gloss">đuôi danh từ giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thêm đuôi là hai chuyện xảy ra cùng lúc: nguyên âm о '
    'của đuôi -ок RỚT MẤT, và trọng âm xuống đuôi — <b>потолка́</b> (cách 2), '
    '<b>потолко́м</b> (cách 5), на <b>потолке́</b> (cách 6).</div>'
    '<div class="hd-warn">📌 <b>взять с потолка́</b> = bịa ra, phán đại một con '
    'số (nghĩa đen: nhặt từ trần nhà xuống).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>потоло́чный</b> thuộc trần — <b>потоло́чный '
    'вентиля́тор</b> quạt trần</div>'
)

# ---------------------------------------------------------------- зал
S["зал"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn từ tiếng Đức <i>Saal</i> = gian '
    'phòng rộng. Tiếng Nga xưa còn dùng dạng giống cái за́ла, nay chuẩn là зал '
    'giống đực.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng nguồn Giéc-manh với <i>salle</i> tiếng Pháp và '
    '"salon" (từ nguyên). Biến cách đều, trọng âm đứng yên.</div>'
    '<div class="hd-warn">📌 Trong nhà ở, khẩu ngữ Nga gọi phòng khách là '
    '<b>зал</b>; cách nói chuẩn hơn là <b>гости́ная</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>спортза́л</b> phòng tập · <b>зри́тельный зал</b> '
    'khán phòng</div>'
)

# ================================================================= FIELD Vietnamese
# Đề bài của deck 1-go: user nhìn dòng này rồi GÕ từ Nga, nên nó phải chỉ còn
# đúng một đáp án. KHÔNG ghi từ loại / giống — mặt đề bài đã in badge sẵn.
V['подушка'] = 'cái gối, đệm lót'
V['дома'] = 'ở nhà'
V['корзина'] = 'cái giỏ, cái sọt, thùng rác'
V['картина'] = 'bức tranh, cảnh tượng'
V['лампа'] = 'cây đèn, bóng đèn'
V['квартира'] = 'căn hộ'
V['комната'] = 'căn phòng, buồng'
V['утюг'] = 'cái bàn là, bàn ủi'
V['зал'] = 'phòng lớn, sảnh, hội trường, phòng tập'
V["полка"] = "cái kệ, giá gắn tường"
