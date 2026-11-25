# -*- coding: utf-8 -*-
"""k259 — qualities::colors: TRỞ NÊN màu gì / TRỞ NÊN thế nào (-еть, -ну-ть, -ся); trục là động từ TỰ đổi trạng thái.

Chỗ cần nhất quán với lô đã nạp:
(1) -е́ть TRỞ NÊN như thế, по- chỉ báo hoàn thành: khớp краснеть/покраснеть k242, бледнеть k249.
(2) -ну- rụng ở quá khứ: khớp замёрзнуть k241, погаснуть k253. (3) мок- ƯỚT: khớp мокрый k128.
(4) вы́- TỚI HẾT + сух-/суш- KHÔ: khớp сушить/высушить k253. (5) ис- + порт- LÀM HỎNG: khớp портить k184; -ся: сломаться k253.
(6) вес- SỨC NẶNG: khớp весы k246, взвесить k256. (7) бес- + luật viết: khớp бесполезный k167; цвет- MÀU: khớp разноцветный k231.
(8) -ов-/-ев- «có màu của»: khớp розовый k44.
Họ hàng cố ý vắng: không có (từ nào cũng có họ thật).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "промокать": "bị ướt, ướt sũng, ngấm nước",                 # dãy chung của cặp
    "промокнуть": "bị ướt, ướt sũng, ngấm nước",                # «ướt như chuột» là thành ngữ, không phải nghĩa
    "высохнуть": "khô đi, ráo nước, khô héo",
    "сохнуть": "khô đi, ráo nước, khô héo",                     # «hanh khô» là thời tiết, sai
    "испортиться": "bị hỏng, hư, ôi thiu, xấu đi",              # + break down, get worse
    "портиться": "bị hỏng, hư, ôi thiu, xấu đi",
    "оливковый": "thuộc ô liu, màu ô liu, xanh ô liu",
    "бесцветный": "không màu, nhạt nhòa, nhạt nhẽo",            # «trong suốt» là прозра́чный; «vô vị» là безвку́сный
    "белеть": "trắng ra, trở nên trắng, tái đi, hiện lên màu trắng",
    "побелеть": "trắng ra, trở nên trắng, tái đi",
    "чернеть": "đen đi, trở nên đen, hiện lên màu đen",         # bỏ «sẫm lại»: đó là темне́ть
    "почернеть": "đen đi, trở nên đen",
    "желтеть": "vàng đi, ngả vàng, trở nên vàng, hiện lên màu vàng",
}

# ------------------------------------------------------------------ промокать
S["промокать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">XUYÊN QUA, thấm suốt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мок-</span>'
    '<span class="hd-gloss">ƯỚT — <b>мо́крый</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nước thấm suốt qua ⇒ người thì ướt sũng, đồ vật thì để nước ngấm vào: '
    '<b>Боти́нки промока́ют.</b> Đôi giày bị ngấm nước. Cặp HT: <b>промо́кнуть</b>.</div>'
    '<div class="hd-warn">Kèm cách 4 thì thành việc khác: THẤM nước ở cái gì cho khô — '
    '<b>промока́ть гу́бы салфе́ткой</b> thấm môi bằng khăn giấy.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>промо́кнуть</b> (HT) · <b>мо́крый</b> ướt · '
    '<b>мо́кнуть</b> bị ngấm nước · <b>непромока́емый</b> chống thấm nước</div>'
)

# ----------------------------------------------------------------- промокнуть
S["промокнуть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">XUYÊN QUA, thấm suốt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мок-</span>'
    '<span class="hd-gloss">ƯỚT — <b>мо́крый</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ну-ть</span>'
    '<span class="hd-gloss">tự CHUYỂN SANG trạng thái ấy</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đã ướt suốt qua lớp áo ⇒ ướt sũng: <b>промо́кнуть до ни́тки</b> ướt «tới tận sợi chỉ». '
    'Quá khứ rụng <i>-ну-</i>, giống đực rụng luôn <i>-л</i>: <b>промо́к, промо́кла, промо́кли</b>; '
    'tương lai vẫn giữ: <b>промо́кну</b>. Cặp CHT: <b>промока́ть</b>.</div>'
    '<div class="hd-warn">Trọng âm đổi là đổi từ: <b>промокну́ть</b> = THẤM cho khô (bằng khăn, giấy), '
    'có tân ngữ, quá khứ giữ nguyên <i>-ну-</i>: <b>промокну́л лоб платко́м</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>промока́ть</b> (CHT) · <b>мо́крый</b> ướt · '
    '<b>мо́кнуть</b> bị ngấm nước · <b>намо́кнуть</b> bị ướt</div>'
)

# --------------------------------------------------------------------- весить
S["весить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вес-</span>'
    '<span class="hd-gloss">SỨC NẶNG — <b>вес</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-ть</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Có <b>вес</b> bao nhiêu đó ⇒ nặng: <b>Ско́лько ве́сит чемода́н?</b> Cái vali nặng bao nhiêu? '
    'Số cân đứng ngay sau động từ ở cách 4, không giới từ: <b>ве́сить то́нну</b>. '
    'Ngôi «tôi» <i>с → ш</i>: <b>ве́шу, ве́сишь</b>. Chỉ tả trạng thái nên không có cặp HT.</div>'
    '<div class="hd-warn"><b>ве́сить</b> = tự nó NẶNG; đem CÂN nó là <b>взве́сить</b>. '
    '<b>пове́сить</b> lại là TREO lên — không phải cặp HT của <b>ве́сить</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вес</b> cân nặng · <b>весы́</b> cái cân · <b>взве́сить</b> cân, cân nhắc · '
    '<b>невесо́мый</b> nhẹ như không</div>'
)

# ------------------------------------------------------------------ высохнуть
S["высохнуть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы́-</span>'
    '<span class="hd-gloss">TỚI HẾT, trọn — thể hoàn thành, luôn giành trọng âm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сох-</span>'
    '<span class="hd-gloss">KHÔ — <b>сухо́й</b>, <i>у/о</i> thay nhau</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ну-ть</span>'
    '<span class="hd-gloss">tự CHUYỂN SANG trạng thái ấy</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tự khô HẲN: <b>Бельё вы́сохло.</b> Đồ giặt khô rồi. Quá khứ rụng <i>-ну-</i>, '
    'giống đực rụng luôn <i>-л</i>: <b>вы́сох, вы́сохла, вы́сохли</b> — đừng nói «высохнул». '
    'Cặp CHT: <b>со́хнуть</b>.</div>'
    '<div class="hd-warn">Tự khô là <b>вы́сохнуть</b>, không tân ngữ; có người LÀM khô là <b>вы́сушить</b>: '
    '<b>Во́лосы вы́сохли</b> tóc khô rồi ↔ <b>Я вы́сушил во́лосы</b> tôi sấy khô tóc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>со́хнуть</b> (CHT) · <b>высыха́ть</b> (CHT, khô cạn dần) · <b>сухо́й</b> khô · '
    '<b>вы́сушить</b> làm khô · <b>за́суха</b> hạn hán</div>'
)

# -------------------------------------------------------------------- сохнуть
S["сохнуть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сох-</span>'
    '<span class="hd-gloss">KHÔ — <b>сухо́й</b>, <i>у/о</i> thay nhau</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ну-ть</span>'
    '<span class="hd-gloss">tự CHUYỂN SANG trạng thái ấy</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tự khô dần; cây cối thì khô héo: <b>Бельё со́хнет.</b> Đồ giặt đang khô. '
    'Có <i>-ну-</i> mà vẫn là CHT, như <b>мёрзнуть</b>. Quá khứ thường rụng <i>-ну-</i>: <b>сох, со́хла, со́хли</b>; '
    '<b>со́хнул</b> có nhưng hiếm. Cặp HT: <b>вы́сохнуть</b>.</div>'
    '<div class="hd-warn">Tự khô là <b>со́хнуть</b>; đem phơi, sấy cái gì là <b>суши́ть</b> + cách 4.</div>'
    '<div class="hd-warn">Khẩu ngữ: <b>со́хнуть по</b> + cách 3 = tương tư ai, héo hon vì ai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вы́сохнуть</b> (HT) · <b>сухо́й</b> khô · <b>засо́хнуть</b> khô quắt · '
    '<b>пересо́хнуть</b> khô khốc (<b>в го́рле пересо́хло</b> khô cả cổ)</div>'
)

# ---------------------------------------------------------------- испортиться
S["испортиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ис- (из-)</span>'
    '<span class="hd-gloss">tiền tố thể, ở đây không thêm nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-портить</span>'
    '<span class="hd-gloss">LÀM HỎNG — chính là <b>по́ртить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">việc xảy ra với chính nó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tự hỏng mất rồi: <b>Молоко́ испо́ртилось.</b> Sữa hỏng rồi. Cái gì tệ đi cũng dùng được: '
    '<b>пого́да испо́ртилась</b> trời trở xấu. Ngôi «tôi» <i>т → ч</i>: <b>испо́рчусь, испо́ртишься</b>. '
    'Cặp CHT: <b>по́ртиться</b>.</div>'
    '<div class="hd-warn">Thức ăn, thời tiết, tâm trạng hỏng → <b>испо́ртиться</b>; '
    'máy móc hỏng thì hay nói <b>слома́ться</b> hơn. Có người LÀM hỏng → <b>испо́ртить</b>, bỏ <i>-ся</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>по́ртиться</b> (CHT) · <b>испо́ртить</b> làm hỏng · '
    '<b>испо́рченный</b> hư hỏng, ôi thiu · <b>по́рча</b> sự hư hỏng</div>'
)

# ------------------------------------------------------------------ портиться
S["портиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">портить</span>'
    '<span class="hd-gloss">LÀM HỎNG — chính là <b>по́ртить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">việc xảy ra với chính nó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đang tự hỏng dần, dễ hỏng: <b>Молоко́ в жару́ бы́стро по́ртится.</b> Trời nóng sữa mau hỏng. '
    'Cái gì tệ dần đi cũng dùng được: <b>зре́ние по́ртится</b> mắt kém đi. '
    'Ngôi «tôi» <i>т → ч</i>: <b>по́рчусь, по́ртишься</b>. Cặp HT: <b>испо́ртиться</b>.</div>'
    '<div class="hd-warn">Trên bao bì, trong siêu thị: <b>скоропо́ртящиеся проду́кты</b> = thực phẩm mau hỏng '
    '(<i>скоро</i> mau + <i>портящиеся</i> đang hỏng).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>испо́ртиться</b> (HT) · <b>по́ртить</b> làm hỏng · <b>по́рча</b> sự hư hỏng</div>'
)

# ------------------------------------------------------------------ сиреневый
S["сиреневый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сирен-</span>'
    '<span class="hd-gloss">HOA TỬ ĐINH HƯƠNG — <b>сире́нь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ев-ый</span>'
    '<span class="hd-gloss">«có màu của» — là <i>-ов-</i> sau phụ âm mềm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Màu của hoa <b>сире́нь</b> ⇒ tím nhạt. Cùng cách làm với <b>ро́за → ро́зовый</b>, '
    'chỉ khác <b>сире́нь</b> kết thúc mềm (<i>ь</i>) nên <i>-ов-</i> thành <i>-ев-</i>. '
    'Trọng âm đứng yên chỗ của <b>сире́нь</b>.</div>'
    '<div class="hd-warn"><b>сире́невый</b> là tím NHẠT; tím đậm như hoa violet là <b>фиоле́товый</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сире́нь</b> hoa lilac, tử đinh hương · '
    '<b>ро́зовый</b> hồng (cùng cách đặt tên màu theo hoa)</div>'
)

# --------------------------------------------------------------------- сирень
S["сирень"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn, không chẻ được — gốc Latin <i>syringa</i>, vẫn là tên khoa học của cây này '
    '(Anh cũng có <i>syringa</i>; <i>lilac</i> là gốc khác).</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giống CÁI đuôi <i>-ь</i>: <b>бе́лая сире́нь</b>, cách 5 <b>сире́нью</b> — '
    '<b>па́хнет сире́нью</b> thơm mùi tử đinh hương. Hoa hay cây đều nói số ít: <b>Цветёт сире́нь</b> '
    'lilac đang nở, <b>ве́тка сире́ни</b> một cành lilac.</div>'
    '<div class="hd-warn"><b>сире́на</b> là CÒI BÁO ĐỘNG — chỉ giống mặt chữ, không cùng từ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сире́невый</b> màu tím nhạt (màu hoa này)</div>'
)

# ------------------------------------------------------------------ оливковый
S["оливковый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">оливк-</span>'
    '<span class="hd-gloss">QUẢ Ô LIU — <b>оли́вка</b>, cùng gốc Latin với Anh <i>olive</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ов-ый</span>'
    '<span class="hd-gloss">«có màu của, làm từ»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Màu quả ô liu ⇒ xanh ô liu: <b>оли́вковая ку́ртка</b>. Cùng cách làm với '
    '<b>ро́за → ро́зовый</b>. Cùng từ này còn là «làm từ ô liu»: <b>оли́вковое ма́сло</b> dầu ô liu — '
    'cụm gặp nhiều nhất.</div>'
    '<div class="hd-warn">Ở cửa hàng Nga: <b>оли́вки</b> thường là quả XANH, quả ĐEN gọi là <b>масли́ны</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оли́вка</b> quả ô liu · <b>оли́ва</b> cây ô liu</div>'
)

# ----------------------------------------------------------------- бесцветный
S["бесцветный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бес-</span>'
    '<span class="hd-gloss">KHÔNG CÓ (= <b>без</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-цве́т-</span>'
    '<span class="hd-gloss">MÀU — <b>цвет</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không có màu: <b>бесцве́тный лак</b> sơn bóng không màu; nghĩa bóng ⇒ nhạt nhẽo, không có nét gì: '
    '<b>бесцве́тный го́лос</b> giọng đều đều vô hồn. Viết <i>с</i> vì đứng trước <i>ц</i> vô thanh '
    '(luật ở thẻ <b>бесполе́зный</b>). Dạng ngắn giống đực chen <i>е</i>: <b>бесцве́тен</b>.</div>'
    '<div class="hd-warn"><b>бесцве́тный</b> là không có màu; nhìn XUYÊN qua được là <b>прозра́чный</b> — '
    'kính màu vẫn <b>прозра́чный</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>цвет</b> màu · <b>цветно́й</b> có màu · <b>разноцве́тный</b> nhiều màu · '
    '<b>обесцве́тить</b> tẩy màu</div>'
)

# --------------------------------------------------------------------- белеть
S["белеть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бел-</span>'
    '<span class="hd-gloss">TRẮNG — <b>бе́лый</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ть</span>'
    '<span class="hd-gloss">TRỞ NÊN như thế</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Trở nên trắng» ⇒ trắng ra, cùng khuôn <b>кра́сный → красне́ть</b>. Riêng CHT còn nghĩa '
    '«hiện lên màu trắng» giữa khung cảnh — câu thơ Lermontov nổi tiếng: <b>Беле́ет па́рус одино́кий</b> '
    'cánh buồm đơn độc hiện lên trắng. Chia đều, giữ <b>е</b>: <b>беле́ю, беле́ешь</b>. Cặp HT: <b>побеле́ть</b>.</div>'
    '<div class="hd-warn">Một chữ <i>е/и</i> đổi nghĩa: <b>беле́ть</b> TỰ trắng ra, không tân ngữ; '
    '<b>бели́ть</b> LÀM cho trắng — <b>бели́ть сте́ны</b> quét vôi tường.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>побеле́ть</b> (HT) · <b>бе́лый</b> trắng · <b>белизна́</b> màu trắng, vẻ trắng · '
    '<b>бельё</b> đồ giặt, đồ lót</div>'
)

# ------------------------------------------------------------------- побелеть
S["побелеть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">chỉ báo hoàn thành, không thêm nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бел-</span>'
    '<span class="hd-gloss">TRẮNG — <b>бе́лый</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ть</span>'
    '<span class="hd-gloss">TRỞ NÊN như thế</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đã trở nên trắng»: <b>Всё побеле́ло от сне́га.</b> Tuyết phủ trắng cả. '
    'Mặt người ⇒ trắng bệch, tái đi. Chia như cặp CHT <b>беле́ть</b>: <b>побеле́ю, побеле́ешь</b>.</div>'
    '<div class="hd-warn">Tái đi VÌ gì → <b>от</b> + cách 2: <b>побеле́ть от стра́ха</b> trắng bệch vì sợ.</div>'
    '<div class="hd-warn"><b>побеле́л</b> tự trắng ra ↔ <b>побели́л</b> đã quét vôi (từ <b>побели́ть</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>беле́ть</b> (CHT) · <b>бе́лый</b> trắng · <b>бели́ть</b> quét vôi, tẩy trắng</div>'
)

# ------------------------------------------------------------------ почернеть
S["почернеть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">chỉ báo hoàn thành, không thêm nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-черн-</span>'
    '<span class="hd-gloss">ĐEN — <b>чёрный</b>, mất trọng âm nên <i>ё → е</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ть</span>'
    '<span class="hd-gloss">TRỞ NÊN như thế</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đã trở nên đen»: <b>Серебро́ почерне́ло.</b> Bạc bị đen rồi. Cùng khuôn '
    '<b>красне́ть → покрасне́ть</b>. Chia như cặp CHT <b>черне́ть</b>: <b>почерне́ю, почерне́ешь</b>.</div>'
    '<div class="hd-warn">Đen đi VÌ gì → <b>от</b> + cách 2: <b>почерне́ть от ды́ма</b> ám khói đen, '
    '<b>почерне́ть от го́ря</b> sạm người vì đau khổ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>черне́ть</b> (CHT) · <b>чёрный</b> đen · <b>черни́ла</b> mực viết</div>'
)

# -------------------------------------------------------------------- чернеть
S["чернеть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">черн-</span>'
    '<span class="hd-gloss">ĐEN — <b>чёрный</b>, mất trọng âm nên <i>ё → е</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ть</span>'
    '<span class="hd-gloss">TRỞ NÊN như thế</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Trở nên đen» ⇒ đen đi, cùng khuôn <b>кра́сный → красне́ть</b>. Riêng CHT còn nghĩa '
    '«hiện lên màu đen» giữa khung cảnh: <b>Вдали́ черне́ет лес.</b> Đằng xa khu rừng hiện lên đen sẫm. '
    'Chia đều, giữ <b>е</b>: <b>черне́ю, черне́ешь</b>. Cặp HT: <b>почерне́ть</b>.</div>'
    '<div class="hd-warn">Một chữ <i>е/и</i> đổi nghĩa: <b>черне́ть</b> TỰ đen đi; '
    '<b>черни́ть</b> LÀM đen, và nghĩa bóng là BÔI NHỌ ai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>почерне́ть</b> (HT) · <b>чёрный</b> đen · <b>чернота́</b> màu đen, bóng tối · '
    '<b>черни́ка</b> quả việt quất</div>'
)

# -------------------------------------------------------------------- желтеть
S["желтеть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">желт-</span>'
    '<span class="hd-gloss">VÀNG — <b>жёлтый</b>, mất trọng âm nên <i>ё → е</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ть</span>'
    '<span class="hd-gloss">TRỞ NÊN như thế</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Trở nên vàng» ⇒ ngả vàng, cùng khuôn <b>кра́сный → красне́ть</b>: <b>Ли́стья желте́ют.</b> '
    'Lá đang ngả vàng. Riêng CHT còn nghĩa «hiện lên màu vàng»: <b>Вдали́ желте́ет по́ле.</b> Đằng xa cánh đồng hiện lên vàng. '
    'Chia đều, giữ <b>е</b>: <b>желте́ю, желте́ешь</b>. Cặp HT: <b>пожелте́ть</b>.</div>'
    '<div class="hd-warn">Tự ngả vàng, không có tân ngữ. Sơn cái gì thành vàng là <b>кра́сить в жёлтый цвет</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пожелте́ть</b> (HT) · <b>жёлтый</b> vàng · <b>желто́к</b> lòng đỏ trứng · '
    '<b>желтизна́</b> sắc vàng</div>'
)

# ------------------------------------------------------------------ пожелтеть
S["пожелтеть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">chỉ báo hoàn thành, không thêm nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-желт-</span>'
    '<span class="hd-gloss">VÀNG — <b>жёлтый</b>, mất trọng âm nên <i>ё → е</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ть</span>'
    '<span class="hd-gloss">TRỞ NÊN như thế</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đã trở nên vàng»: <b>Бума́га пожелте́ла.</b> Giấy ngả vàng rồi. Cùng khuôn '
    '<b>красне́ть → покрасне́ть</b>. Chia như cặp CHT <b>желте́ть</b>: <b>пожелте́ю, пожелте́ешь</b>.</div>'
    '<div class="hd-warn">Ngả vàng VÌ gì → <b>от</b> + cách 2: <b>пожелте́ть от вре́мени</b> '
    'ố vàng theo thời gian; hay gặp dạng tính từ <b>пожелте́вшие страни́цы</b> những trang giấy ố vàng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>желте́ть</b> (CHT) · <b>жёлтый</b> vàng · <b>желто́к</b> lòng đỏ trứng</div>'
)

# loitubat 2: «nghĩa ngược chiều» ở промокать (chỉ là việc khác, có tân ngữ); «câu thơ ai cũng thuộc» ở белеть nói quá.
# nguonsai 4: сирень cách 4 số nhiều; вешённый; «to show black/yellow» ở thể HT; dạng ngắn + trạng từ оливковый.
B = {
    "docbangmat": 127,
    "loitubat": 2,
    "nguonsai": 4,
    "baolen": [
        "CỬA SOÁT CÒN 1 DÒNG: thẻ почернеть viết черне́ть, nouns.csv có danh từ đồng tự че́рнеть (một loài vịt) — đồng tự THẬT, cần luồng chính thêm «черне́ть» vào mientru.py (tôi không sửa vì chỉ được tạo file lô; không bỏ tên cặp CHT để né cửa).",
        "сирень — bảng SAI: cách 4 số nhiều ghi «сире́ней», vô tri nên phải là «сире́ни» (khối DUNG QUY TAC cũng vì thế báo nhầm).",
        "весить — bảng: phân từ bị động «вешённый» không tồn tại (nội động); mệnh lệnh «весь, ве́сьте» hầu như không dùng.",
        "оливковый — bảng: dạng ngắn оли́вков/-а/-о/-ы và trạng từ оли́вково do máy sinh, tính từ quan hệ không có; nên bỏ trống. Gloss EN THIẾU nghĩa hay gặp nhất «olive (adj)» (оли́вковое ма́сло) — V giữ nguyên theo gloss, cần duyệt có thêm «bằng ô liu» không.",
        "почернеть, пожелтеть — gloss EN «to show black / to show yellow» chỉ đúng với CHT (черне́ть, желте́ть), nên V hai thẻ HT không có «hiện lên màu…»; nên cắt gloss.",
        "белеть/побелеть, чернеть/почернеть, желтеть/пожелтеть — V: hai vế chung dãy, vế CHT thêm một nghĩa «hiện lên màu…» (vế HT nằm gọn trong vế CHT, badge thể tách). «bạc đi» (to go grey, tóc) không đưa vào vì thường nói седе́ть.",
        "промокать — V theo dãy chung của cặp, CHƯA gồm nghĩa ngoại động «thấm (bằng khăn, giấy)» dù gloss có (to soak up / to blot, cặp промокну́ть); nghĩa đó nằm ở ô đỏ. Cần duyệt.",
        "промокнуть — V bỏ «ướt như chuột», «ướt hết»; ví dụ 2 dịch «ướt như chuột» nên sửa thành «ướt sũng».",
        "сохнуть/высохнуть — V không có «tương tư» (со́хнуть по ком) và «gầy rộc» (gloss phụ, khẩu ngữ).",
        "бесцветный — V bỏ «trong suốt» (прозрачный), «vô vị» (безвкусный).",
        "Ví dụ gượng, nên thay: побелеть «Да побелей ты уже, хватит солярия!», чернеть «Не черней на солнце» và почернеть «Почерней хоть немного» (rám nắng là загоре́ть), испортиться «Только не испортись до вечера, борщ мой!», белеть «Я каждую зиму белею, как лист бумаги», промокать «Не промокай под дождём».",
    ],
}
