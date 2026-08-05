# -*- coding: utf-8 -*-
"""k26 — nature::plants: cây cỏ và cảnh vật ngoài trời.

Trục của lô: phần lớn là danh từ gốc Slav cổ, nên chỗ đáng học không phải cấu
trúc từ mà là (a) TRỌNG ÂM NHẢY khi sang số nhiều — 11/18 từ dính — và (b) mấy
cặp nghĩa rất dễ lẫn nhau trong tiếng Việt (cỏ ↔ tán lá, hồ ↔ ao ↔ đầm lầy,
vườn ↔ trảng trống). Vài từ có cầu nối Ấn–Âu thật (луна́–lunar, зерно́–grain,
де́рево–tree, не́бо–nebula) thì bắc cầu, còn lại nói thẳng là gốc trơn.
"""

S = {}
V = {}

S["трава"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">трав-</span>'
    '<span class="hd-gloss">CỎ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cỏ mọc sát đất. Từ này ôm cả nghĩa "cây cỏ, thảo dược": '
    '<b>травяно́й</b> чай là trà thảo mộc, và số nhiều <b>тра́вы</b> thường hiểu là '
    '"các loại cây thuốc".</div>'
    '<div class="hd-why">Chú ý bảng chia: số ít trọng âm nằm ở đuôi '
    '(<b>трава́</b>, <b>травы́</b>), sang số nhiều nó lùi hẳn về gốc — '
    '<b>тра́вы</b>, <b>тра́вами</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тра́вка</b> cỏ non · <b>травяно́й</b> bằng cỏ, thảo mộc · '
    '<b>отра́ва</b> thuốc độc (cùng gốc cổ, nghĩa xưa là "thứ cho ăn")</div>'
)

S["листва"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">лист-</span>'
    '<span class="hd-gloss">CHIẾC LÁ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва</span>'
    '<span class="hd-gloss">hậu tố GỘP CẢ ĐÁM</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một chiếc lá rời là <b>лист</b>; thêm <b>-ва</b> thành tên gọi '
    'cho toàn bộ lá trên cây gộp lại. Vì là danh từ tập hợp nên <b>листва́</b> '
    '<b>không đếm được và không có số nhiều</b> — bảng chia chỉ có cột số ít.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лист</b> chiếc lá; tờ giấy · <b>листо́к</b> tờ rơi, lá nhỏ · '
    '<b>листопа́д</b> mùa lá rụng · <b>листа́ть</b> lật giở từng trang</div>'
)

S["ёлка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ёл-</span>'
    '<span class="hd-gloss">từ ель — cây vân sam</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">hậu tố nhỏ, thân mật</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>ель</b> + <b>-ка</b> = "cây vân sam nhỏ". Người Nga gọi cây '
    'dựng đêm 31/12 là <b>ёлка</b> — cây Noel của họ vốn là vân sam, không phải thông. '
    'Chữ <b>ё</b> luôn tự mang trọng âm nên từ này không cần đánh dấu.</div>'
    '<div class="hd-why">Chú ý bảng chia: cách 2 số nhiều chèn thêm một chữ '
    '<b>о</b> cho đọc được — <b>ёлок</b>, chứ không phải "ёлк".</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ель</b> cây vân sam (giống cái, đuôi -ь) · '
    '<b>ело́вый</b> bằng gỗ vân sam · <b>ёлочка</b> cây thông nhỏ</div>'
)

S["речка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">реч-</span>'
    '<span class="hd-gloss">từ река́ — sông (к đổi thành ч)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">hậu tố nhỏ, thân mật</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>река́</b> + <b>-ка</b>, và <b>к</b> phải đổi thành <b>ч</b> '
    'đúng luật biến âm г/к/х → ж/ч/ш; trọng âm lùi lên gốc: <b>ре́чка</b>. Nghĩa không '
    'chỉ là sông bé, mà còn là cách gọi trìu mến một con sông quen.</div>'
    '<div class="hd-why">Chú ý bảng chia: cách 2 số nhiều chèn thêm <b>е</b> — '
    '<b>ре́чек</b>.</div>'
    '<div class="hd-warn">⚠️ Đừng lẫn <b>ре́чка</b> (sông) với <b>речь</b> (lời nói, bài '
    'phát biểu): nhìn giống nhau nhưng là hai gốc khác hẳn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>река́</b> sông · <b>речно́й</b> thuộc về sông</div>'
)

S["луна"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">лун-</span>'
    '<span class="hd-gloss">VẬT SÁNG TRÊN TRỜI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc Ấn–Âu với <i>luna</i> tiếng Latin, nên tiếng Anh có '
    '<i>lunar</i>, <i>lunatic</i>; nghĩa gốc là "cái phát sáng". Tiếng Nga dùng '
    '<b>луна́</b> cho mặt trăng như một thiên thể.</div>'
    '<div class="hd-why">Chú ý bảng chia: số ít trọng âm ở đuôi (<b>луна́</b>, '
    '<b>луны́</b>), số nhiều lùi về gốc — <b>лу́ны</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лу́нный</b> thuộc mặt trăng · <b>лунохо́д</b> xe thám hiểm '
    'mặt trăng · <b>луна́тик</b> người mộng du</div>'
)

S["поляна"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пол-</span>'
    '<span class="hd-gloss">ĐỒNG TRỐNG (cùng gốc по́ле)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ян-а</span>'
    '<span class="hd-gloss">đuôi tạo danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>по́ле</b> là khoảng đất trống trải; <b>поля́на</b> là mảnh '
    'trống ấy lọt vào giữa rừng — chỗ cây thưa hẳn ra, cỏ mọc, người hay dừng nghỉ. '
    'Không phải đất trồng trọt, cũng không phải vườn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>по́ле</b> cánh đồng · <b>полево́й</b> thuộc đồng ruộng · '
    '<b>поля́нка</b> trảng nhỏ</div>'
)

S["липа"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">лип-</span>'
    '<span class="hd-gloss">DÍNH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Theo từ nguyên, cùng gốc với <b>ли́пкий</b> "dính" — nhựa và '
    'lớp vỏ trong của cây này dính tay. Hoa của nó dùng pha trà: <b>ли́повый</b> чай.</div>'
    '<div class="hd-warn">⚠️ Tiếng Anh gọi cây này là <i>lime tree</i> nhưng nó '
    '<b>không dính dáng gì tới quả chanh</b>: đây là cây đoan (Tilia, cũng gọi '
    '<i>linden</i>), cây bóng mát trồng đầy đường phố Nga.</div>'
    '<div class="hd-warn">⚠️ Khẩu ngữ <b>ли́па</b> còn nghĩa "đồ dởm, giấy tờ giả": '
    '<b>ли́повый па́спорт</b> = hộ chiếu giả.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ли́пкий</b> dính · <b>ли́пнуть</b> dính vào · '
    '<b>ли́повый</b> bằng gỗ đoan; (lóng) giả mạo</div>'
)

S["дуб"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дуб</span>'
    '<span class="hd-gloss">GỐC TRƠN — không chẻ nhỏ được, không có phụ tố</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một trong những tên cây cổ nhất, phải thuộc thẳng. Cây sồi là '
    'biểu tượng của sự vững chãi và nặng nề, nên nghĩa bóng của <b>дубо́вый</b> là '
    '"thô, cứng đờ, chẳng mềm mại".</div>'
    '<div class="hd-why">Chú ý bảng chia: số ít trọng âm đứng yên ở gốc (<b>ду́ба</b>, '
    '<b>ду́бом</b>), sang số nhiều nhảy hẳn xuống đuôi — <b>дубы́</b>, '
    '<b>дубо́в</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дубо́вый</b> bằng gỗ sồi; thô kệch · <b>дуби́на</b> gậy gộc; '
    '(mắng) đồ đần · <b>дубра́ва</b> rừng sồi</div>'
)

S["остров"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">VÒNG QUANH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-стров-</span>'
    '<span class="hd-gloss">DÒNG CHẢY (cùng gốc струя́)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen theo từ nguyên: "chỗ bị dòng nước chảy vòng quanh" — '
    'đúng định nghĩa hòn đảo. Nhận ra được <b>о-</b> "vòng quanh" thì cũng đọc ra '
    '<b>полуо́стров</b> = nửa đảo = bán đảo.</div>'
    '<div class="hd-why">Chú ý bảng chia: số nhiều không lấy đuôi -ы mà lấy '
    '<b>-а́</b> có trọng âm — <b>острова́</b>, <b>острово́в</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>островно́й</b> thuộc về đảo · <b>полуо́стров</b> bán đảo '
    '(полу- một nửa)</div>'
)

S["юг"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">юг</span>'
    '<span class="hd-gloss">GỐC TRƠN — không chẻ nhỏ được</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ gốc trơn, phải thuộc. Cái đáng học kèm là giới từ: "ở miền '
    'Nam" là <b>на ю́ге</b> (cách 6), còn "đi về phía nam" là <b>на юг</b> (cách 4) — '
    'cùng một giới từ на, đổi cách là đổi nghĩa đứng-yên/di-chuyển.</div>'
    '<div class="hd-why">Chú ý bảng chia: số ít trọng âm đứng yên ở gốc (<b>ю́га</b>, '
    '<b>ю́ге</b>); số nhiều <b>юга́</b> mới nhảy xuống đuôi, nhưng dạng này chỉ gặp '
    'trong khẩu ngữ <b>на юга́</b> = đi nghỉ ở các tỉnh miền Nam.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ю́жный</b> thuộc phía nam · <b>южа́нин</b> người miền Nam · '
    '<b>юго-восто́к</b> đông nam</div>'
)

S["сад"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сад-</span>'
    '<span class="hd-gloss">ĐẶT XUỐNG, TRỒNG (cùng gốc сажа́ть, сиде́ть)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vườn là chỗ cây được "đặt ngồi xuống" đất — cùng một gốc với '
    '<b>сажа́ть</b> "trồng" và <b>сиде́ть</b> "ngồi". Nhớ tách với <b>огоро́д</b>: '
    '<b>сад</b> là vườn CÂY, <b>огоро́д</b> là vườn RAU.</div>'
    '<div class="hd-why">Chú ý bảng chia: cách 6 có hai dạng và chúng khác việc — nói '
    'VỀ khu vườn thì <b>о са́де</b>, nhưng ở TRONG vườn thì <b>в саду́</b>, trọng âm '
    'rơi xuống đuôi. Đây là "cách vị trí" riêng của một nhóm danh từ giống đực.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сажа́ть</b> trồng cây · <b>са́дик</b> vườn nhỏ; nhà trẻ · '
    '<b>де́тский сад</b> trường mẫu giáo · <b>садо́вник</b> người làm vườn</div>'
)

S["солнце"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">солн-</span>'
    '<span class="hd-gloss">MẶT TRỜI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-це</span>'
    '<span class="hd-gloss">hậu tố nhỏ đã hoá thạch → giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc Ấn–Âu với <i>sol</i> tiếng Latin, nên tiếng Anh có '
    '<i>solar</i>. Đuôi <b>-це</b> vốn là hậu tố "nhỏ" nay dính chặt vào từ, và nó cho '
    'biết ngay đây là danh từ giống trung.</div>'
    '<div class="hd-warn">⚠️ Chữ <b>л</b> KHÔNG đọc: <b>со́лнце</b> nghe thành '
    '"со́нце", <b>со́лнечный</b> nghe thành "со́нечный". Viết vẫn phải có л.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>со́лнечный</b> nắng, thuộc mặt trời · <b>подсо́лнух</b> hoa '
    'hướng dương (под- dưới + солн- mặt trời)</div>'
)

S["небо"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">неб-</span>'
    '<span class="hd-gloss">TRỜI, MÂY MÙ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc Ấn–Âu với <i>nebula</i> tiếng Latin ("sương mù, đám '
    'mây") — nghĩa cổ là vùng mây phủ trên đầu, rồi mới thành "bầu trời".</div>'
    '<div class="hd-why">Chú ý bảng chia: số nhiều mọc thêm khúc <b>-ес-</b> và trọng âm '
    'nhảy xuống đuôi — <b>небеса́</b> "các tầng trời", cách 2 là <b>небе́с</b>. Dạng cổ '
    'còn sót lại, giống <b>чу́до</b> → <b>чудеса́</b>.</div>'
    '<div class="hd-warn">⚠️ Đừng lẫn với <b>нёбо</b> (vòm miệng): từ đó viết bằng '
    '<b>ё</b> và trọng âm nằm ở đó.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>небе́сный</b> thuộc bầu trời · <b>небоскрёб</b> nhà chọc '
    'trời (небо + скрести́ cào, cạo)</div>'
)

S["дерево"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дерев-</span>'
    '<span class="hd-gloss">CÂY, GỖ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc Ấn–Âu với <i>tree</i> tiếng Anh. Một từ ôm hai nghĩa: '
    'cái cây đang sống, và gỗ làm vật liệu — <b>из де́рева</b> = làm bằng gỗ.</div>'
    '<div class="hd-why">Chú ý bảng chia: số nhiều đổi hẳn đuôi thành <b>-ья</b> và '
    'trọng âm nhảy vào giữa — <b>дере́вья</b>, <b>дере́вьев</b> (cùng kiểu với '
    '<b>брат</b> → <b>бра́тья</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>деревя́нный</b> bằng gỗ · <b>древе́сный</b> thuộc về gỗ, '
    'thân mộc</div>'
)

S["зерно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">зерн-</span>'
    '<span class="hd-gloss">HẠT</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc Ấn–Âu với <i>granum</i> tiếng Latin, nên tiếng Anh có '
    '<i>grain</i> và <i>corn</i>. Số ít vừa là một hạt riêng lẻ, vừa là thóc lúa nói '
    'chung (cả vụ mùa); số nhiều <b>зёрна</b> mới là "từng hạt một".</div>'
    '<div class="hd-why">Chú ý bảng chia: sang số nhiều chữ <b>е</b> trong gốc biến '
    'thành <b>ё</b> và kéo trọng âm về theo — <b>зёрна</b>; riêng cách 2 số nhiều còn '
    'chèn thêm một chữ <b>е</b>: <b>зёрен</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>зёрнышко</b> hạt bé xíu · <b>зерново́й</b> thuộc ngũ cốc</div>'
)

S["озеро"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">озер-</span>'
    '<span class="hd-gloss">HỒ (gốc Slav cổ, không chẻ nhỏ thêm được)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không có cầu nối nào sang tiếng Anh, phải thuộc thẳng. Đổi lại, '
    'nhớ theo bộ ba nước đọng: <b>о́зеро</b> hồ · <b>пруд</b> ao (nhỏ, thường do người '
    'đào) · <b>боло́то</b> đầm lầy.</div>'
    '<div class="hd-why">Chú ý bảng chia: số ít trọng âm ở đầu (<b>о́зеро</b>), sang số '
    'nhiều chữ <b>е</b> thành <b>ё</b> và hút trọng âm về mình — <b>озёра</b>, '
    '<b>озёр</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>озёрный</b> thuộc về hồ</div>'
)

S["болото"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">болот-</span>'
    '<span class="hd-gloss">ĐẦM LẦY (gốc Slav cổ, không chẻ nhỏ được)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đất sũng nước, bước xuống là lún. Bảng chia hoàn toàn theo quy '
    'tắc và trọng âm đứng yên ở <b>-ло́-</b> suốt cả bảng, nên phần duy nhất phải nhớ là '
    'mặt chữ.</div>'
    '<div class="hd-why">Nghĩa bóng dùng rất nhiều: <b>боло́то</b> là chỗ trì trệ, ao tù '
    '— nơi nào chẳng có gì nhúc nhích thì người Nga gọi đúng bằng từ này.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>боло́тный</b> thuộc đầm lầy · <b>боло́тистый</b> lầy lội, '
    'sình lầy</div>'
)

S["степь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">степь</span>'
    '<span class="hd-gloss">GỐC TRƠN — không chẻ nhỏ được</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính từ Nga này đi thẳng vào tiếng Anh thành <i>steppe</i>: '
    'vùng đồng cỏ khô mênh mông, gần như không có cây, trải dài phía nam nước Nga.</div>'
    '<div class="hd-why">Chú ý bảng chia: số ít trọng âm ở gốc (<b>сте́пи</b>, '
    '<b>сте́пью</b>); số nhiều thì cách 1 và cách 4 vẫn <b>сте́пи</b>, các cách còn lại '
    'mới nhảy xuống đuôi — <b>степе́й</b>, <b>степя́м</b>. Ngoài <b>о сте́пи</b> "về thảo nguyên" '
    'còn dạng chỉ vị trí <b>в степи́</b> "ở giữa thảo nguyên", trọng âm xuống đuôi.</div>'
    '<div class="hd-warn">⚠️ Là danh từ giống CÁI dù đuôi chỉ có <b>-ь</b>, nên tính từ '
    'phải theo giống cái: <b>широ́кая степь</b>, không phải "широкий".</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>степно́й</b> thuộc thảo nguyên</div>'
)


# ── Field Vietnamese: đề bài của deck 1-go, phải chỉ có MỘT đáp án đúng ──────
# Lô này lắm cặp lẫn nhau: cỏ ↔ tán lá, hồ ↔ ao ↔ đầm lầy, vườn ↔ trảng trống,
# cây nói chung ↔ cây vân sam. Ba dòng vi của nguồn còn SAI hẳn tên loài/nghĩa
# (липа, озеро, степь) — sửa luôn ở đây.
V["трава"]   = "cỏ, thảm cỏ mọc dưới đất"
V['листва'] = 'tán lá, lá cây'
V['ёлка'] = 'cây vân sam nhỏ, cây thông Noel'
V['речка'] = 'con sông nhỏ, con suối'
V['луна'] = 'mặt trăng'
V["поляна"]  = "trảng trống, khoảng đất trống giữa rừng"
V['липа'] = 'cây đoan, cây bồ đề'
V["сад"]     = "vườn cây, khu vườn"
V["небо"]    = "bầu trời"
V['дерево'] = 'cây, gỗ'
V["зерно"]   = "hạt ngũ cốc, hạt thóc"
V['озеро'] = 'hồ, hồ nước'
V["болото"]  = "đầm lầy"
V['степь'] = 'thảo nguyên'
