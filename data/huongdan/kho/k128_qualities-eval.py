# -*- coding: utf-8 -*-
"""k128 — qualities::eval: 20 từ đánh giá / trạng thái, trục là GỐC Nga dưới lớp từ mượn.

Không khối hệ thống. Chỗ phải khớp với thẻ đã xong / lô song song:
(1) цен- «GIÁ», о- «phủ lên, áp vào» — y như оце́нка (k121);
(2) вис-/вес-/веш- «TREO» — y như висе́ть (k102), ве́шать/пове́сить (k131);
(3) раз-/раж- «ĐÁNH, GIÁNG» (рази́ть) — khớp вы́разить (k135);
(4) зна- «BIẾT» — y như узна́ть (k81); -вык- «QUEN» — y như обы́чный (k108);
(5) từ mượn quốc tế (кри́зис, си́мвол, фронт, прогре́сс, катастро́фа, револю́ция)
    không bịa cấu trúc Nga — chỉ nói mảnh gốc Hy Lạp/Latin khi tiếng Anh cùng mảnh.
"""

V = {
    "обладать": "sở hữu, được phú cho",
    "символ": "biểu tượng, ký tự",
    "оценить": "đánh giá, định giá",
    "поражение": "sự thất bại, tổn thương",
    "узнавать": "nhận ra, biết tin, tìm hiểu",
    "привыкать": "quen với",
    "привыкнуть": "quen với",
}

S = {}

S["мокрый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мок-</span>'
    '<span class="hd-gloss">gốc ƯỚT, NGẤM NƯỚC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-р-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thấy <i>мок-</i> là thấy nước: <b>мо́кнуть</b> bị ngấm nước. Trái nghĩa: '
    '<b>сухо́й</b> khô. Dạng ngắn giống cái nhảy trọng âm ra đuôi: <b>мокра́</b>, còn lại giữ '
    'ở gốc — <b>мо́кро, мо́кры</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мо́кнуть</b> bị ướt, ngấm nước · <b>промо́кнуть</b> ướt sũng · '
    '<b>намочи́ть</b> làm ướt (<i>к → ч</i>)</div>'
)

# `велик` (ве́лик = xe đạp, từ lóng) ĐÃ XOÁ 21/11: user chọn bỏ — trùng trọn với велосипе́д,
# còn sách TRKI nhiều khả năng ý là dạng ngắn вели́к. Nằm ở `bo` của k128 trong hangdoi.json.

S["обладать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">bao quanh, trùm lên</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лад-</span>'
    '<span class="hd-gloss">= <i>влад-</i> QUYỀN LÀM CHỦ (<b>власть</b>), rơi mất <i>в</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành, chia đều: <b>облада́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm chủ trùm lên cái gì ⇒ sở hữu. Hay dùng cho PHẨM CHẤT, năng lực, '
    'quyền: <b>облада́ть тала́нтом</b> có tài. Đồ vật thường ngày thì nói <b>име́ть</b> / '
    '<b>у меня́ есть</b>.</div>'
    '<div class="hd-warn">Đòi <b>cách 5</b>, không phải cách 4 như <b>име́ть</b>: '
    '<b>Он облада́ет си́лой</b> = anh ấy có sức mạnh.</div>'
    '<div class="hd-warn">⚠️ Mức tin: <i>-лад-</i> = <i>влад-</i> (rơi <i>в</i> sau <i>об-</i>, '
    'như <b>обы́чный</b>) là từ nguyên, không phải luật suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>владе́ть</b> làm chủ (cũng + cách 5) · <b>власть</b> quyền lực · '
    '<b>владе́лец</b> chủ sở hữu · <b>облада́тель</b> người sở hữu</div>'
)

S["принадлежать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">áp sát vào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-над-</span>'
    '<span class="hd-gloss">BÊN TRÊN — như giới từ <b>над</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-леж-а́ть</span>'
    '<span class="hd-gloss">NẰM — chính là <b>лежа́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Nằm sát vào» ai ⇒ thuộc về người đó. Chia lớp 2 y như <b>лежа́ть</b>: '
    '<b>принадлежу́, принадлежи́шь, принадлежа́т</b>. Chủ sở hữu đứng ở <b>cách 3</b>: '
    '<b>Дом принадлежи́т мне</b> = căn nhà thuộc về tôi.</div>'
    '<div class="hd-warn">Thuộc một NHÓM thì thêm <b>к</b>: <b>принадлежа́ть к поколе́нию</b> '
    '= thuộc một thế hệ.</div>'
    '<div class="hd-warn">⚠️ Mức tin: đường nghĩa «nằm sát ⇒ thuộc về» là từ nguyên, không '
    'phải luật suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лежа́ть</b> nằm · <b>принадле́жность</b> sự thuộc về; đồ dùng đi kèm</div>'
)

S["катастрофа"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ката-</span>'
    '<span class="hd-gloss">XUỐNG (Hy Lạp)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-стро́ф-а</span>'
    '<span class="hd-gloss">LẬT, QUAY (Hy Lạp <i>strophē</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Lật nhào xuống» ⇒ thảm hoạ — chính là <i>catastrophe</i>. Nhấn ở '
    '<b>-стро́-</b>; đuôi <i>-а</i> nên giống cái.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>катастрофи́ческий</b> thảm khốc · <b>авиакатастро́фа</b> tai nạn '
    'máy bay</div>'
)

S["лишний"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">лиш-</span>'
    '<span class="hd-gloss">gốc DƯ RA, VƯỢT MỨC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ий</span>'
    '<span class="hd-gloss">đuôi tính từ MỀM, như <b>дома́шний</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dư ra so với cần ⇒ thừa, không cần. Đuôi mềm nên giống cái, giống trung '
    'là <b>ли́шняя</b>, <b>ли́шнее</b> — không phải <i>-ая/-ое</i>.</div>'
    '<div class="hd-warn"><b>ли́шний биле́т</b> vé dư · <b>ничего́ ли́шнего</b> không có gì '
    'thừa · <b>не ли́шний</b> = cũng nên có.</div>'
    '<div class="hd-warn">⚠️ Mức tin: nối với <b>лишь</b> «chỉ» và <b>лиши́ть</b> «tước đi» là '
    'từ nguyên, không phải luật suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лишь</b> chỉ, mới · <b>лиши́ть</b> tước đi</div>'
)

S["символ"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn Hy Lạp <i>symbolon</i> = <i>symbol</i>. Không chẻ được trong tiếng '
    'Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỗ lệch đáng nhớ: <i>b</i> Hy Lạp vào tiếng Nga thành <i>в</i> — như '
    '<b>алфави́т</b> (alphabet). Nhấn ở đầu: <b>си́мвол</b>.</div>'
    '<div class="hd-warn">Cũng là KÝ TỰ trên máy: <b>не бо́льше ста си́мволов</b> = không quá '
    '100 ký tự.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>символи́ческий</b> tượng trưng</div>'
)

S["прогресс"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">TỚI TRƯỚC (Latin <i>pro-</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-гре́сс</span>'
    '<span class="hd-gloss">BƯỚC (Latin <i>gressus</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Bước tới trước» ⇒ tiến bộ = <i>progress</i>, giữ cả hai chữ <i>с</i>. '
    'Đổi <i>про-</i> thành <i>ре-</i> «lùi lại» là ra trái nghĩa <b>регре́сс</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>прогресси́вный</b> tiến bộ, cấp tiến · <b>регре́сс</b> sự thoái bộ</div>'
)

S["оценивать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">phủ lên, áp vào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-це́н-</span>'
    '<span class="hd-gloss">GIÁ — <b>цена́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ть</span>'
    '<span class="hd-gloss">biến <b>оцени́ть</b> thành thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Áp giá lên» ⇒ đánh giá, như <b>оце́нка</b>. Chèn <i>-ива-</i> thì trọng '
    'âm lùi về gốc và ở yên đó: <b>оце́ниваю, оце́ниваешь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оцени́ть</b> đánh giá (HT) · <b>оце́нка</b> sự đánh giá, điểm số · '
    '<b>цена́</b> giá · <b>це́нный</b> quý giá</div>'
)

S["оценить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-це́н-</span>'
    '<span class="hd-gloss">áp GIÁ lên — như <b>оце́нка</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đánh giá xong, ra con số. Khi chia, trọng âm chỉ ở đuôi tại ngôi «tôi»: '
    '<b>оценю́</b>, rồi lùi về gốc — <b>оце́нишь, оце́нят</b>.</div>'
    '<div class="hd-warn">Nghĩa thứ hai: TRÂN TRỌNG — <b>Я оцени́л ва́шу по́мощь</b> = tôi rất '
    'quý sự giúp đỡ của anh. Định giá ở mức nào: <b>в</b> + cách 4.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оце́нивать</b> đánh giá (CHT) · <b>цени́ть</b> quý trọng · '
    '<b>цена́</b> giá</div>'
)

S["зависеть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">tiền tố — ghép lại là «treo VÀO»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ви́с-еть</span>'
    '<span class="hd-gloss">TREO — chính là <b>висе́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Treo vào cái gì thì phụ thuộc cái đó — y như tiếng Anh <i>depend</i> '
    '(Latin «treo», như <i>pendant</i>). Ngôi «tôi» đổi <i>с → ш</i> như <b>вишу́</b>: '
    '<b>зави́шу</b>, còn lại giữ <i>с</i> — <b>зави́сишь</b>.</div>'
    '<div class="hd-warn">Luôn đi với <b>от</b> + cách 2: <b>Э́то зави́сит от пого́ды</b> = '
    'còn tuỳ thời tiết.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>висе́ть</b> treo · <b>ве́шать</b> treo lên · '
    '<b>зави́симость</b> sự phụ thuộc · <b>незави́симый</b> độc lập · '
    '<b>зави́снуть</b> (máy) bị treo</div>'
)

S["поражение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố — <b>порази́ть</b> đánh trúng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-раж-</span>'
    '<span class="hd-gloss">ĐÁNH, GIÁNG (<i>раз-</i>, <i>з → ж</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bị đánh trúng ⇒ THẤT BẠI; trên cơ thể, chỗ bị đánh trúng ⇒ TỔN THƯƠNG. '
    'Trái nghĩa: <b>побе́да</b> chiến thắng.</div>'
    '<div class="hd-warn"><b>потерпе́ть пораже́ние</b> = chịu thất bại, thua trận.</div>'
    '<div class="hd-warn">⚠️ Mức tin: nối <i>-раж-</i> với <b>вы́разить</b> là từ nguyên, '
    'không phải luật suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>порази́ть</b> đánh trúng; làm sửng sốt · <b>порази́тельный</b> đáng '
    'kinh ngạc · <b>вы́разить</b> biểu đạt</div>'
)

S["кризис"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn Hy Lạp <i>krisis</i> = <i>crisis</i>. Không chẻ được trong tiếng '
    'Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc Hy Lạp là «phán xét, quyết định»: khủng hoảng là khúc ngoặt buộc '
    'phải quyết. Nhấn ở đầu: <b>кри́зис</b>; tận cùng phụ âm nên giống đực.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кри́зисный</b> khủng hoảng (tính từ) · <b>кри́тика</b> phê bình — '
    'cùng gốc «phán xét»</div>'
)

S["фронт"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn Pháp <i>front</i> (Latin <i>frons</i> «trán, mặt trước»). Không '
    'chẻ được trong tiếng Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Mặt trước» của đạo quân ⇒ mặt trận. Số nhiều nhảy trọng âm ra đuôi: '
    '<b>фронты́, фронто́в, фронта́м</b>.</div>'
    '<div class="hd-warn">Ra mặt trận / ở mặt trận dùng <b>на</b>: <b>на фронт</b>, '
    '<b>на фро́нте</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>фронтово́й</b> thuộc mặt trận · <b>фронта́льный</b> trực diện</div>'
)

S["революция"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ре-</span>'
    '<span class="hd-gloss">LẠI, NGƯỢC (Latin)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-волю́-</span>'
    '<span class="hd-gloss">LĂN, XOAY (Latin <i>volvere</i>, như <i>revolve</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ция</span>'
    '<span class="hd-gloss">= <i>-tion</i>, danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Xoay ngược lại» ⇒ lật đổ trật tự cũ = <i>revolution</i>. Đổi <i>ре-</i> '
    'thành <i>э-</i> «ra ngoài» là <b>эволю́ция</b> tiến hoá.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>революцио́нный</b> cách mạng (tính từ) · <b>революционе́р</b> nhà '
    'cách mạng · <b>эволю́ция</b> sự tiến hoá</div>'
)

S["психологический"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">психо-ло́г-</span>'
    '<span class="hd-gloss">như <b>психоло́гия</b> — môn học về tâm trí</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ческий</span>'
    '<span class="hd-gloss">= <i>-ical</i>, đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bỏ <i>-ия</i> của <b>психоло́гия</b>, thêm <i>-ический</i> — trọng âm '
    'nhảy sang <b>-ги́-</b>, ngay trước đuôi, như <b>биологи́ческий</b>.</div>'
    '<div class="hd-warn">Đừng lẫn với <b>психи́ческий</b> = thuộc TÂM THẦN: <b>психи́ческое '
    'здоро́вье</b> sức khoẻ tâm thần.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>психоло́гия</b> tâm lý học · <b>психо́лог</b> nhà tâm lý học</div>'
)

S["узнавать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-зна-</span>'
    '<span class="hd-gloss">ĐẠT TỚI chỗ BIẾT — như <b>узна́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва-ть</span>'
    '<span class="hd-gloss">biến thành thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thân hiện tại RƠI <i>-ва-</i>, y như <b>дава́ть → даю́</b>: '
    '<b>узнаю́, узнаёшь, узнаю́т</b>. Quá khứ lại giữ: <b>узнава́л</b>.</div>'
    '<div class="hd-warn"><b>узнаю́</b> (nhấn cuối) = tôi đang nhận ra, đang dò hỏi; '
    '<b>узна́ю</b> (nhấn giữa) là của <b>узна́ть</b> = tôi sẽ biết.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>узна́ть</b> biết được (HT) · <b>знать</b> biết · <b>зна́ние</b> kiến '
    'thức · <b>знако́мый</b> người quen</div>'
)

S["наблюдать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">hướng VÀO đối tượng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-блюд-</span>'
    '<span class="hd-gloss">gốc cổ TRÔNG GIỮ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">thể chưa hoàn thành, chia đều: <b>наблюда́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chăm chú trông vào ⇒ quan sát. Trùng khéo với tiếng Anh <i>observe</i>: '
    'cùng gốc ra <b>соблюда́ть</b> = <i>observe</i> luật lệ, tuân thủ.</div>'
    '<div class="hd-warn">Theo dõi, trông chừng AI: <b>за</b> + cách 5 — <b>наблюда́ть за '
    'детьми́</b>. Ngắm một hiện tượng: cách 4 trơn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>наблюде́ние</b> sự quan sát · <b>наблюда́тель</b> người quan sát · '
    '<b>соблюда́ть</b> tuân thủ</div>'
)

S["привыкать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">TỚI, gắn vào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вык-</span>'
    '<span class="hd-gloss">gốc QUEN — cũng là <i>-ыч-</i> trong <b>обы́чный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">thể chưa hoàn thành, chia đều: <b>привыка́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đang trên đường đi TỚI chỗ quen ⇒ đang quen dần. Xong rồi thì là '
    '<b>привы́кнуть</b>.</div>'
    '<div class="hd-warn">Quen VỚI cái gì: <b>к</b> + cách 3 — <b>привыка́ть к кли́мату</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>привы́кнуть</b> quen (HT) · <b>привы́чка</b> thói quen · '
    '<b>обы́чный</b> thường lệ · <b>отвыка́ть</b> bỏ quen</div>'
)

S["привыкнуть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-вык-</span>'
    '<span class="hd-gloss">TỚI chỗ QUEN — như <b>привыка́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ну-ть</span>'
    '<span class="hd-gloss">đuôi thể hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Quá khứ rơi cả <i>-ну-</i> lẫn <i>-л</i> ở giống đực: <b>привы́к</b>, '
    'rồi <b>привы́кла, привы́кли</b> — như <b>мо́кнуть → мок</b>.</div>'
    '<div class="hd-warn"><b>Я привы́к</b> (quá khứ) = tôi QUEN RỒI, nghĩa hiện tại như '
    '<i>I\'m used to it</i>. Quen với gì: <b>к</b> + cách 3.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>привыка́ть</b> quen dần (CHT) · <b>привы́чка</b> thói quen · '
    '<b>отвы́кнуть</b> mất thói quen</div>'
)
