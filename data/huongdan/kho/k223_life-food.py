# -*- coding: utf-8 -*-
"""k223 — life::food: đồ ăn, uống, ngủ, họ hàng; trục là GỐC đã có thẻ.

Chỗ cần nhất quán trong lô:
(1) потомок đối xứng предок k183, пото́м k46 · двоюродный: два k28, родно́й k33.
(2) напиваться/напиться: пи- UỐNG — khớp пить k22, вы́пить k59, пья́ный k163, напи́ток k168.
(3) будильник: буди- + -льник — khớp холодильник k174, будить k201.
(4) выспаться/высыпаться: сп-/сн-/сып- NGỦ, đồng tự gốc сы́пать — khớp k129, k192.
(5) горчица: горьк- → горч- — khớp горький k108 · наушники: х → ш — khớp ухо k32.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "двоюродный": "họ, con chú con bác, con cô con cậu",            # bỏ «bà con họ» (rộng hơn first cousin)
    "сытый": "no, no nê",                                           # «đủ ăn» gloss không có
    "напиваться": "uống say, uống thoả thích, uống cho đã khát",    # «nát rượu» = nghiện; + drink one's fill
    "напиться": "uống say, uống thoả thích, uống cho đã khát",      # «say rượu» là trạng thái = пьяный
    "наушники": "tai nghe, chụp tai giữ ấm, chụp tai chống ồn",     # «bịt tai» là hành động / nút tai
    "выспаться": "ngủ đủ giấc, ngủ đẫy giấc",
    "высыпаться": "ngủ đủ giấc, ngủ đẫy giấc",
}

# ---------------------------------------------------------------- двоюродный
S["двоюродный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">двою-</span>'
    '<span class="hd-gloss">HAI — dạng biến cách cổ của <b>два</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-род-</span>'
    '<span class="hd-gloss">DÒNG HỌ — <b>род</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thuộc HAI nhánh của một họ» ⇒ chung ông bà, khác bố mẹ. Đối lập là '
    '<b>родно́й</b> ruột thịt: <b>родно́й брат</b> anh em ruột ↔ <b>двою́родный брат</b> '
    'anh em họ.</div>'
    '<div class="hd-warn">Gần như luôn đi kèm từ chỉ người thân: <b>двою́родный брат</b>, '
    '<b>двою́родная сестра́</b> — bên nội hay ngoại, vai trên hay dưới đều gọi thế. '
    '<b>двою́родный дед</b> = anh em trai của ông bà.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>трою́родный</b> họ xa thêm một đời (chung cụ) · <b>два</b> hai · '
    '<b>род</b> dòng họ · <b>родно́й</b> ruột thịt · <b>ро́дственник</b> người họ hàng</div>'
)

# ------------------------------------------------------------------- потомок
S["потомок"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пото́м-</span>'
    '<span class="hd-gloss">SAU ĐÓ — <b>пото́м</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ок</span>'
    '<span class="hd-gloss">đuôi danh từ, như ở <b>пре́док</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người đến SAU mình ⇒ con cháu, hậu duệ. Đối xứng với <b>пре́док</b> '
    '(người có TRƯỚC) ⇒ tổ tiên.</div>'
    '<div class="hd-warn">Chú ý bảng chia: <i>о</i> của <i>-ок</i> rụng ở mọi dạng có đuôi — '
    '<b>пото́мок</b> → <b>пото́мка</b>, <b>пото́мки</b>. Trọng âm đứng yên.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пото́м</b> sau đó · <b>пото́мство</b> con cháu (nói gộp) · '
    'đối nghĩa: <b>пре́док</b> tổ tiên</div>'
)

# --------------------------------------------------------------------- тыква
S["тыква"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: gốc trơn.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ giống cái đều đặn, trọng âm đứng yên ở <i>ты́-</i>. Cả quả lẫn '
    'phần ruột đem nấu đều gọi bằng từ này: <b>суп из ты́квы</b> súp bí đỏ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ты́квенный</b> thuộc về bí đỏ (<b>ты́квенная ка́ша</b> cháo bí đỏ, '
    '<b>ты́квенные се́мечки</b> hạt bí)</div>'
)

# ------------------------------------------------------------------- горчица
S["горчица"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">горч-</span>'
    '<span class="hd-gloss">ĐẮNG — gốc của <b>го́рький</b>, <i>к → ч</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ц-а</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thứ có vị đắng» ⇒ mù tạt. Phép đổi <i>к → ч</i> trước hậu tố gặp lại ở '
    '<b>чесно́к</b> → <b>чесно́чный</b>. Ăn kèm thì dùng <b>с</b> + cách 5: '
    '<b>соси́ски с горчи́цей</b> xúc xích với mù tạt.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>го́рький</b> đắng · <b>горчи́ть</b> có vị đắng · '
    '<b>горчи́чный</b> thuộc về mù tạt</div>'
)

# --------------------------------------------------------------------- сытый
S["сытый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сыт-</span>'
    '<span class="hd-gloss">NO — gốc trơn, không chẻ tiếp</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trái với <b>голо́дный</b> đói. Chú ý dạng ngắn: chỉ giống cái nhảy trọng '
    'âm ra đuôi — <b>сыт</b>, <b>сыта́</b>, <b>сы́то</b>, <b>сы́ты</b>.</div>'
    '<div class="hd-warn">«Tôi no rồi» nói bằng dạng ngắn: <b>Спаси́бо, я сыт</b> (nam) · '
    '<b>я сыта́</b> (nữ).</div>'
    '<div class="hd-warn">NGƯỜI no là <b>сы́тый</b>; MÓN ĂN chắc bụng là <b>сы́тный</b>: '
    '<b>сы́тный обе́д</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сы́тный</b> chắc bụng · <b>насы́тить</b> làm cho no · '
    '<b>сыт по го́рло</b> no căng, (bóng) chán ngấy</div>'
)

# -------------------------------------------------------------------- персик
S["персик"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: từ mượn. <i>-ик</i> ở đây KHÔNG phải hậu tố «nhỏ» của '
    'tiếng Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ngược về Latinh là <i>persicum</i> «(quả) Ba Tư» — cùng gốc với tên nước '
    '<b>Пе́рсия</b> Ba Tư và với chính <i>peach</i> tiếng Anh (đi qua tiếng Pháp nên mòn mặt chữ).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пе́рсиковый</b> thuộc về đào, màu hồng đào</div>'
)

# -------------------------------------------------------------------- чеснок
S["чеснок"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Với người học hiện nay thì không chẻ, coi như một khối.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chú ý bảng chia: trọng âm nhảy hẳn ra đuôi — <b>чесно́к</b> → '
    '<b>чеснока́</b>, <b>чесноко́м</b>; mà <i>о</i> KHÔNG rụng (khác <b>пото́мок</b> → '
    '<b>пото́мка</b>). Chỉ dùng số ít; đếm bằng <b>зу́бчик чеснока́</b> tép tỏi («răng nhỏ»), '
    '<b>голо́вка чеснока́</b> củ tỏi («đầu nhỏ»).</div>'
    '<div class="hd-warn">⚠️ Mức tin: từ nguyên thường nối với <b>чеса́ть</b> chải, gãi (củ tách '
    'ra từng tép) — là lịch sử của từ, không phải luật suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>чесно́чный</b> thuộc về tỏi, <i>к → ч</i> '
    '(<b>чесно́чный со́ус</b> xốt tỏi)</div>'
)

# ------------------------------------------------------------------ макароны
S["макароны"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn gốc tiếng Ý, cùng từ <i>macaroni</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tên gọi chung cho mì kiểu Ý, không riêng loại hình ống: '
    '<b>макаро́ны с сы́ром</b> mì ống phô mai.</div>'
    '<div class="hd-warn">Dùng ở số nhiều. Cách 2 trơ thân, không có <i>-ов</i>: '
    '<b>таре́лка макаро́н</b>, <b>килогра́мм макаро́н</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>макаро́нный</b> thuộc về mì ống · <b>макаро́нина</b> một cọng mì '
    '(khẩu ngữ)</div>'
)

# --------------------------------------------------------------------- вафля
S["вафля"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn gốc German, cùng gốc <i>waffle</i> và '
    '<i>wafer</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một từ Nga ôm cả hai từ Anh: bánh xốp giòn (<i>wafer</i>) lẫn bánh nướng '
    'khuôn (<i>waffle</i>). Điểm chung là mặt bánh kẻ ô.</div>'
    '<div class="hd-warn">Chú ý bảng chia: chỉ cách 2 số nhiều gãy khuôn, chèn <i>е</i>: '
    '<b>па́чка ва́фель</b> gói bánh xốp.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ва́фельный</b> thuộc về bánh xốp (<b>ва́фельное полоте́нце</b> khăn '
    'dệt ô tổ ong) · <b>ва́фельница</b> khuôn nướng bánh waffle</div>'
)

# ---------------------------------------------------------------- напиваться
S["напиваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-…-ся</span>'
    '<span class="hd-gloss">đi thành cặp: làm cho THOẢ, cho ĐÃ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пи-</span>'
    '<span class="hd-gloss">UỐNG — <b>пить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва́-ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp chưa hoàn thành của <b>напи́ться</b>: thói quen hoặc lặp lại. Có '
    '<i>-ва-</i> nên chia đều, hết bất thường của <b>пить</b>: <b>напива́юсь</b>, '
    '<b>напива́ешься</b>.</div>'
    '<div class="hd-warn">Nói trống thì hiểu là chuyện rượu: <b>Он ча́сто напива́ется</b> = '
    'anh ta hay uống say.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>напи́ться</b> (HT) · <b>пить</b> uống · <b>напи́ток</b> đồ uống · '
    '<b>пья́ный</b> say rượu</div>'
)

# ------------------------------------------------------------------ напиться
S["напиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-…-ся</span>'
    '<span class="hd-gloss">đi thành cặp: làm cho THOẢ, cho ĐÃ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пи-</span>'
    '<span class="hd-gloss">UỐNG — <b>пить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Uống cho đã» ⇒ hết khát, hoặc say. Cùng khuôn <i>на-…-ся</i>: '
    '<b>нае́сться</b> ăn no nê. Uống đã khát thì kèm cách 2: <b>напи́ться воды́</b>; nói trống '
    'thường là say: <b>Он опя́ть напи́лся</b>.</div>'
    '<div class="hd-warn">Chú ý bảng chia: như <b>пить</b>, thân thành <i>пь-</i> — '
    '<b>напью́сь</b>, <b>напьёшься</b>, sai khiến <b>напе́йся</b>. Quá khứ giống cái nhấn đuôi: '
    '<b>напи́лся</b> nhưng <b>напила́сь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>напива́ться</b> (CHT) · <b>вы́пить</b> uống cạn · <b>напи́ток</b> '
    'đồ uống · <b>пья́ный</b> say rượu</div>'
)

# ------------------------------------------------------------------ скамейка
S["скамейка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">скаме́й-</span>'
    '<span class="hd-gloss">BĂNG GHẾ — <b>скамья́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-а</span>'
    '<span class="hd-gloss">hậu tố «nhỏ» + đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vốn là «băng ghế nhỏ», nay là từ thường ngày cho ghế dài nhiều người '
    'ngồi, nhất là ở công viên: <b>сиде́ть на скаме́йке</b>. Cùng khuôn: <b>семья́</b> → '
    '<b>семе́йка</b>.</div>'
    '<div class="hd-warn">Chú ý bảng chia: chỉ cách 2 số nhiều gãy khuôn, <i>й → е</i>: '
    '<b>скаме́йка</b> → <b>мно́го скаме́ек</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>скамья́</b> băng ghế · <b>скаме́ечка</b> ghế băng nhỏ</div>'
)

# ------------------------------------------------------------------ наушники
S["наушники"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">TRÊN — giới từ <b>на</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-у́ш-</span>'
    '<span class="hd-gloss">TAI — <b>у́хо</b>, <b>у́ши</b> (<i>х → ш</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ник-и</span>'
    '<span class="hd-gloss">đồ vật + đuôi số nhiều</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đồ ở trên tai» ⇒ tai nghe, và cả cái chụp tai. Thường dùng số nhiều vì '
    'có hai bên; số ít <b>нау́шник</b> chỉ là MỘT bên: <b>пра́вый нау́шник</b> bên phải.</div>'
    '<div class="hd-warn">Đang đeo tai nghe = <b>в</b> + cách 6, như mặc quần áo: '
    '<b>Он в нау́шниках</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>у́хо</b> tai · <b>ушно́й</b> thuộc về tai</div>'
)

# ----------------------------------------------------------------- будильник
S["будильник"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">буди-</span>'
    '<span class="hd-gloss">ĐÁNH THỨC — <b>буди́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-льник</span>'
    '<span class="hd-gloss">«đồ dùng để làm việc đó»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái để đánh thức. Cùng đuôi với <b>холоди́льник</b> tủ lạnh '
    '(<b>холоди́ть</b> làm lạnh).</div>'
    '<div class="hd-warn">Đặt báo thức: <b>поста́вить буди́льник на семь часо́в</b>. '
    'Chuông reo: <b>буди́льник звони́т</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>буди́ть</b> đánh thức · <b>разбуди́ть</b> đánh thức (HT)</div>'
)

# ------------------------------------------------------------------- диабет
S["диабет"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được trong tiếng Nga: mượn gốc Hy Lạp, cùng từ '
    '<i>diabetes</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Khác tiếng Anh ở chỗ không có <i>-es</i>, nên là giống đực đều đặn: '
    '<b>У него́ диабе́т</b>. Tên đầy đủ <b>са́харный диабе́т</b> có sẵn chữ «đường», như '
    '«tiểu đường».</div>'
    '<div class="hd-warn">Cụm: <b>диабе́т второ́го ти́па</b> tiểu đường típ 2.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>диабе́тик</b> người bị tiểu đường · <b>диабети́ческий</b> thuộc về '
    'tiểu đường</div>'
)

# ----------------------------------------------------------------- выспаться
S["выспаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы́-…-ся</span>'
    '<span class="hd-gloss">đi thành cặp: làm cho ĐỦ, cho trọn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сп-ать</span>'
    '<span class="hd-gloss">NGỦ — <b>спать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ngủ cho tới khi đủ: <b>Я вы́спался</b> tôi ngủ đã rồi. Phủ định là '
    'thiếu ngủ: <b>Я не вы́спался</b>.</div>'
    '<div class="hd-warn">Chú ý bảng chia: như <b>спать</b>, chỉ ngôi «tôi» chèn <i>л</i> — '
    '<b>вы́сплюсь</b>, <b>вы́спишься</b>. Trọng âm khỏi lo: <i>вы́-</i> của thể hoàn thành giữ '
    'suốt, kể cả <b>вы́спалась</b> (so <b>спала́</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>высыпа́ться</b> (CHT) · <b>спать</b> ngủ · <b>сон</b> giấc ngủ · '
    '<b>засну́ть</b> ngủ thiếp đi</div>'
)

# ---------------------------------------------------------------- высыпаться
S["высыпаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-…-ся</span>'
    '<span class="hd-gloss">đi thành cặp: làm cho ĐỦ, cho trọn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сып-</span>'
    '<span class="hd-gloss">NGỦ — mặt khác của <i>сп-</i> / <i>сн-</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành, chia đều</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp chưa hoàn thành của <b>вы́спаться</b>: <b>Я не высыпа́юсь</b> = '
    'dạo này tôi toàn thiếu ngủ. Gốc đổi mặt đúng như <b>просну́ться</b> → '
    '<b>просыпа́ться</b>; ở thể này <i>вы-</i> không hút trọng âm.</div>'
    '<div class="hd-warn">Nghĩa «đổ ra, vãi ra» trong từ điển là của từ khác cùng mặt chữ (gốc '
    '<b>сы́пать</b> rắc; cặp HT <b>вы́сыпаться</b>) — thẻ này không học nghĩa đó.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вы́спаться</b> (HT) · <b>спать</b> ngủ · <b>просыпа́ться</b> '
    'tỉnh dậy · <b>засыпа́ть</b> ngủ thiếp đi</div>'
)

B = {
    "docbangmat": 85,
    "loitubat": 1,      # выспаться chẻ -ся «cho chính mình» (bịa) -> вы-…-ся đi cặp (sửa cả высыпаться)
    "nguonsai": 5,      # nghĩa Việt: «bà con họ» · «đủ ăn» · «nát rượu» · «say rượu» · «bịt tai»
    "baolen": [
        "V cần duyệt (7): двоюродный bỏ «bà con họ» (rộng hơn first cousin), thêm «con cô con cậu» · сытый bỏ «đủ ăn» · напиваться/напиться thống nhất «uống say, uống thoả thích, uống cho đã khát» (bỏ «nát rượu», «say rượu») · наушники «bịt tai» -> «chụp tai giữ ấm, chụp tai chống ồn» (earmuffs, ear defenders) · выспаться/высыпаться thống nhất «ngủ đủ giấc, ngủ đẫy giấc».",
        "вафля: «bánh quế» đã soi, GIỮ (một dạng wafer; gloss wafer xác nhận được). Không chắc user muốn giữ, muốn gọn thì bỏ còn «bánh xốp, bánh waffle».",
        "высыпаться: gloss thẻ có cả «spill out» — đồng tự khác gốc (сы́пать), V cố ý không đưa vào theo lựa chọn của luồng chính; thẻ có một câu chặn. Nên gỡ ba gloss spill/trickle/pour out khỏi field tiếng Anh cho khớp.",
        "Từ nguyên theo trí nhớ, không tra được trong repo: двою- là dạng biến cách cổ của два · скамейка < скамья · чеснок ~ чесать (thẻ đã ghi Mức tin) · вафля mượn German · персик ~ Latinh persicum.",
        "Va chạm: lệnh tiep báo (khong co) với đề CŨ; V mới chưa chạy vacham thật (không đụng Anki).",
    ],
}
