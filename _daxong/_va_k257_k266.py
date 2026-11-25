# -*- coding: utf-8 -*-
"""Vá sau đợt k257–k266 (25/11/2026). L2: chạy một lần.

Câu ví dụ gượng / thiếu nghĩa / dịch lệch đề mới (luồng chính đọc hết 600 câu + agent ghi); bảng chia
sai từ OpenRussian (цениться dán PERF, сирень cách 4 số nhiều, беспокойный «беспокойы»…); gloss Anh lạc
(ромашка dính nghĩa tục, отличительный sai chính tả); Сберба́нк viết hoa."""
import copy
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
ROOT = ROOT if os.path.exists(os.path.join(ROOT, "bot.py")) else os.path.dirname(ROOT)
sys.path.insert(0, ROOT)
from anki_tools import grammar                                            # noqa: E402
from anki_tools.anki_client import (doc_notes_cua_model, gan_tieng_vi_du, sync_now,   # noqa: E402
                                    sync_truoc_khi_ghi_lo, update_note_fields)
from anki_tools.backup import run_backup                                  # noqa: E402
from anki_tools.config import MODEL_NAME                                  # noqa: E402
from anki_tools.html_builder import dung_cloze, thay_vi_du                # noqa: E402

# mỗi dòng: từ ¦ câu số ¦ ru ¦ en ¦ vi   (_ = giữ nguyên; [..] = chỗ bôi)
CAU_TXT = """
седина¦3¦Она закрашивает [седину] раз в месяц.¦She dyes her [grey hair] once a month.¦Mỗi tháng cô ấy nhuộm che [tóc bạc] một lần.
косметический¦2¦Ей сделали [косметическую] операцию на носу.¦She had [cosmetic] surgery on her nose.¦Cô ấy được phẫu thuật [thẩm mỹ] mũi.
зевать¦3¦_¦Don't [space out], it's your turn to speak now.¦Đừng [lơ đễnh], tới lượt cậu nói rồi.
зевнуть¦1¦Я сейчас [зевну], извини, не выспался.¦I'm about to [yawn], sorry, I didn't get enough sleep.¦Tôi sắp [ngáp] đây, xin lỗi, tôi thiếu ngủ.
ровесник¦2¦_¦_¦Nó thua ván cờ chỉ trong một phút trước một [bạn đồng trang lứa].
националистический¦1¦_¦_¦Anh ta đọc một tờ tạp chí [mang tính dân tộc chủ nghĩa] nào đó, ghê thật.
националистический¦3¦_¦_¦Tôi chán mấy câu đùa [mang tính dân tộc chủ nghĩa] của anh ta rồi.
национализм¦2¦Историк пишет о корнях [национализма] в Европе.¦The historian writes about the roots of [nationalism] in Europe.¦Nhà sử học viết về gốc rễ của [chủ nghĩa dân tộc] ở châu Âu.
националист¦2¦_¦_¦Đừng gọi tôi là [người theo chủ nghĩa dân tộc], tôi chỉ yêu tiếng mẹ đẻ thôi.
журналистика¦2¦_¦_¦Cô ấy học [ngành báo chí], đã năm thứ hai rồi.
журналистика¦3¦Она ушла из [журналистики] в рекламу.¦She left [journalism] for advertising.¦Cô ấy bỏ [nghề báo] sang làm quảng cáo.
прожиточный¦1¦_¦_¦Mức thu nhập tối thiểu [đủ sống] lại được nâng lên vài đồng lẻ.
прожиточный¦2¦Его зарплата ниже [прожиточного] минимума.¦His salary is below the [subsistence] minimum.¦Lương anh ấy thấp hơn mức tối thiểu [cần cho sinh hoạt].
прожиточный¦3¦_¦_¦Trên tin tức lại tranh luận về mức tối thiểu [đủ sống].
индустриальный¦2¦После войны страна стала [индустриальной].¦After the war the country became [industrial].¦Sau chiến tranh, nước này trở thành nước [công nghiệp].
ухудшение¦2¦_¦_¦Hiện chưa có [sự xấu đi] nào, bà đang ngủ yên.
удачливый¦2¦Ей везёт во всём, она очень [удачливая].¦Everything goes her way, she's very [lucky].¦Cái gì cô ấy cũng trúng, đúng là người [hay gặp may].
безобразный¦1¦_¦_¦Cái mặt tiền mới đó [xấu xí] thật, thảm quá.
безобразный¦2¦_¦_¦Ngoài hành lang treo cái gương [xấu xí], bỏ nó đi.
безобразный¦3¦Вчера он устроил [безобразную] сцену в ресторане.¦Yesterday he made an [outrageous] scene in the restaurant.¦Hôm qua anh ta gây ra một màn [quá quắt] trong nhà hàng.
гуманный¦3¦_¦_¦Ở trại cứu hộ của bọn tớ quy định rất [nhân đạo].
бездарный¦2¦_¦_¦Đó là màn trình diễn [kém cỏi] nhất cả buổi hòa nhạc.
плодотворный¦2¦_¦_¦Buổi gặp với bạn thiết kế đã [có kết quả tốt].
цениться¦1¦_¦I think a skill like that [is valued] more and more.¦Tớ nghĩ kỹ năng như thế ngày càng [được coi trọng].
цениться¦2¦_¦_¦Trước đây loại tiền xu này rất [được đánh giá cao] trong giới sưu tầm.
равноправие¦2¦Женщины долго добивались [равноправия].¦Women fought for [equal rights] for a long time.¦Phụ nữ đã đấu tranh rất lâu để có [quyền bình đẳng].
равноправие¦3¦_¦_¦Trong gia đình họ mọi thứ dựa trên sự [bình quyền].
ввоз¦1¦_¦_¦[Việc đưa vào] thực phẩm qua biên giới giờ bị hạn chế.
ввоз¦3¦Компания занимается [ввозом] машин из Японии.¦The company deals in the [import] of cars from Japan.¦Công ty này chuyên [nhập khẩu] xe từ Nhật.
вывоз¦1¦_¦_¦Ở chỗ mình [việc chở đi] rác thải là vào thứ Ba, đừng quên nhé.
вывоз¦2¦_¦_¦Cậu có biết ai lo [việc chở đi] đồ gỗ cũ không?
вывоз¦3¦Правительство ограничило [вывоз] зерна.¦The government restricted grain [exports].¦Chính phủ hạn chế [xuất khẩu] ngũ cốc.
суверенный¦1¦Каждая республика хотела стать [суверенной].¦Every republic wanted to become [sovereign].¦Nước cộng hòa nào cũng muốn trở nên [có chủ quyền].
демократичный¦2¦_¦Our office has a [democratic] atmosphere, everyone's on first-name terms.¦Ở công ty bọn tớ không khí rất [dân chủ], ai cũng gọi nhau thân mật.
демократичный¦3¦Цены тут [демократичные], даже студентам по карману.¦The prices here are [affordable], even for students.¦Giá ở đây [phải chăng], sinh viên cũng mua nổi.
бюрократ¦2¦_¦_¦Tôi đợi [kẻ quan liêu] đó ba tiếng ngoài hành lang.
суверенитет¦3¦Речь идёт о потере [суверенитета].¦It's about the loss of [sovereignty].¦Đây là chuyện mất [chủ quyền].
реформировать¦3¦Давно пора [реформировать] суды.¦It's high time to [reform] the courts.¦Đã đến lúc phải [cải cách] tòa án rồi.
оккупировать¦1¦Во время войны немцы [оккупировали] город.¦During the war the Germans [occupied] the city.¦Trong chiến tranh quân Đức đã [chiếm đóng] thành phố.
оккупировать¦2¦_¦_¦Con mèo lại [chiếm giữ] ghế bành của tôi suốt cả ngày.
оккупировать¦3¦_¦_¦Đừng [chiếm giữ] nhà tắm nữa, tớ cũng muộn rồi!
волевой¦2¦У неё [волевой] подбородок и прямой взгляд.¦She has a [strong-willed] chin and a direct gaze.¦Cô ấy có cái cằm [cương nghị] và ánh nhìn thẳng.
волевой¦3¦_¦_¦Mình mà có được phẩm chất [có ý chí] như bạn thì tốt, thật đấy!
промокать¦1¦_¦_¦Đi đôi bốt này lần nào tôi cũng [bị ướt].
промокать¦2¦_¦_¦Mấy buổi tập đó bọn mình [ướt sũng] suốt.
промокать¦3¦Эти ботинки быстро [промокают].¦These boots [let water in] quickly.¦Đôi bốt này [ngấm nước] nhanh lắm.
промокнуть¦2¦_¦_¦Trên đường về bọn mình [ướt sũng] từ đầu đến chân.
сохнуть¦1¦Цветы [сохнут], полей их скорее.¦The flowers are [withering], water them quickly.¦Hoa đang [khô héo], tưới nhanh đi.
сохнуть¦2¦_¦_¦Đôi sneaker để cạnh lò sưởi hai ngày mới [khô đi].
испортиться¦3¦Погода может [испортиться] к вечеру.¦The weather may [get worse] by evening.¦Đến tối thời tiết có thể [xấu đi].
портиться¦3¦_¦_¦Thịt không thể [ôi thiu] chỉ sau một ngày.
оливковый¦3¦На салат лучше взять [оливковое] масло.¦For the salad it's better to take [olive] oil.¦Trộn salad thì nên lấy dầu [ô liu].
белеть¦1¦Вдалеке [белеют] снежные вершины.¦Snowy peaks [show white] in the distance.¦Đằng xa, những đỉnh núi tuyết [hiện lên màu trắng].
белеть¦2¦_¦_¦Tuyết [hiện lên màu trắng] trên mái nhà suốt tháng Giêng.
белеть¦3¦Волосы у него начали [белеть] рано.¦His hair started to [turn white] early.¦Tóc anh ấy bắt đầu [trắng ra] từ sớm.
побелеть¦1¦К утру от снега [побелеют] все крыши.¦By morning all the roofs will [turn white] with snow.¦Đến sáng mọi mái nhà sẽ [trắng ra] vì tuyết.
побелеть¦2¦_¦_¦Anh ấy [tái đi] khi thấy hóa đơn ở quán.
побелеть¦3¦Пальцы могут [побелеть] от холода.¦Fingers can [turn white] from the cold.¦Ngón tay có thể [trở nên trắng] vì lạnh.
почернеть¦1¦Убери бананы в холод, а то они [почернеют].¦Put the bananas somewhere cool or they'll [turn black].¦Cất chuối vào chỗ mát đi, không chúng [đen đi] đấy.
почернеть¦2¦_¦_¦Cái dây bạc [đen đi] chỉ sau vài tháng.
почернеть¦3¦От влаги дерево может [почернеть].¦Wood can [turn black] from damp.¦Gỗ có thể [trở nên đen] vì ẩm.
чернеть¦1¦Вдали [чернеет] лес.¦A forest [shows black] in the distance.¦Đằng xa một khu rừng [hiện lên màu đen].
чернеть¦2¦_¦_¦Bức tường cạnh bếp lò cứ [đen đi] vì khói.
чернеть¦3¦Серебро со временем начинает [чернеть].¦Silver starts to [turn black] over time.¦Theo thời gian, bạc bắt đầu [trở nên đen].
желтеть¦1¦_¦_¦Lá đã [vàng đi] rồi, sắp lạnh hẳn thôi.
пожелтеть¦1¦К сентябрю берёзы [пожелтеют].¦By September the birches will [turn yellow].¦Đến tháng Chín, bạch dương sẽ [ngả vàng].
пожелтеть¦2¦_¦_¦Nhìn này, cái lá cây đa cảnh đã [vàng đi] hẳn rồi.
нечаянно¦3¦Я [нечаянно] нажал не ту кнопку.¦I [accidentally] pressed the wrong button.¦Tôi [vô ý] bấm nhầm nút.
предчувствовать¦3¦_¦_¦Mèo biết [cảm thấy trước] thời tiết xấu.
обобщать¦1¦_¦_¦Cô ấy lúc nào cũng [khái quát hóa] mọi thứ, nghe mà tức.
обобщать¦2¦_¦_¦Ở lớp học, mỗi lần chúng tôi đều [tổng kết] phần đã học.
обобщать¦3¦_¦_¦Đừng [khái quát hóa], không phải con trai nào cũng vậy.
обобщить¦2¦_¦_¦Chúng tôi đã [tổng hợp] các phản hồi rồi gửi cho giám đốc.
обобщить¦3¦_¦_¦Để tôi thử [tổng kết] mọi thứ trong hai câu.
противопоставить¦1¦_¦_¦Tôi sẽ [đem] những sự thật đơn giản [ra chống lại] lời anh ta.
противопоставить¦2¦Автор [противопоставил] город деревне.¦The author [contrasted] the city with the village.¦Tác giả đã [đặt] thành phố [đối lập] với làng quê.
противопоставить¦3¦_¦_¦Thật lòng thì chẳng có gì để [đem ra chống lại] lập luận của họ.
противопоставлять¦1¦_¦_¦Anh ta cứ [đặt] công việc của mình [đối lập] với của tôi.
противопоставлять¦2¦_¦_¦Mẹ luôn [so sánh đối lập] tôi với anh trai.
противопоставлять¦3¦_¦_¦Đừng [đặt] mình [đối lập] với cả nhóm, hãy làm cùng nhau.
беспокойный¦2¦_¦_¦Bọn tôi có một đêm [không yên] vì mấy người láng giềng.
беспокойный¦3¦_¦My last few days have been very [hectic].¦Mấy ngày vừa rồi của tôi cứ [không yên].
азартный¦2¦Мы вчера устроили [азартную] партию в нарды.¦Yesterday we had a [heated] game of backgammon.¦Hôm qua bọn tôi chơi một ván backgammon rất [hăng máu].
жизнерадостный¦3¦_¦_¦Trong ảnh cưới ai cũng [vui vẻ] thế!
доброжелательный¦2¦_¦_¦Tôi nhận được một lá thư [có thiện ý] sau buổi phỏng vấn.
соскучиться¦1¦_¦_¦Cứ cho họ đi, một tuần nữa là họ [nhớ] nhà thôi.
соскучиться¦3¦_¦_¦Có ba ngày nên nó còn chưa kịp [nhớ] nữa.
сбербанк¦1¦Мне надо зайти в [Сбербанк] за картой.¦_¦_
сбербанк¦3¦Переведи деньги через [Сбербанк], так быстрее.¦_¦_
безлюдный¦1¦_¦_¦Buổi tối công viên [vắng người] hẳn, hơi rợn.
туризм¦1¦_¦_¦Tôi thích [đi bộ đường dài] hơn là ra bãi biển.
затормозить¦1¦_¦_¦Nếu anh ta không [phanh] thì sẽ có tai nạn.
затормозить¦3¦_¦_¦[Phanh] đi, có con chó trên đường kìa!
вполголоса¦1¦_¦_¦Anh ấy nói gì đó [khe khẽ], tôi không nghe được.
вполголоса¦2¦_¦_¦[Hạ giọng] thôi, em bé vừa ngủ.
вполголоса¦3¦_¦_¦Họ bàn chuyện gì đó [bằng giọng nhỏ] ở góc phòng.
телеграф¦1¦_¦_¦Ngày trước bà tôi ra [trạm điện báo] để gửi lời chúc.
телеграф¦2¦_¦_¦Ở [trạm điện báo] luôn có hàng dài dằng dặc.
телеграф¦3¦_¦_¦Trong thành phố gần như không còn [trạm điện báo] cũ nào.
переписываться¦1¦_¦_¦Họ vẫn [nhắn qua nhắn lại] mỗi ngày.
разговориться¦1¦_¦_¦Mình ngồi cạnh nhau đi, biết đâu sẽ [trò chuyện rôm rả].
систематически¦1¦_¦_¦Anh ta [đều đặn] đi làm muộn.
будни¦3¦_¦_¦Tôi mệt vì [cuộc sống thường nhật] xám xịt, muốn đi nghỉ.
периодический¦1¦_¦_¦Trong xe có tiếng gõ [theo chu kỳ], phải kiểm tra thôi.
обливать¦1¦Он каждое утро [обливает] ноги холодной водой.¦Every morning he [pours] cold water over his feet.¦Sáng nào anh ấy cũng [dội] nước lạnh lên chân.
разлить¦3¦_¦_¦Giúp mình [múc chia] súp ra từng bát với.
избаловать¦3¦_¦_¦Mình sợ [chiều hư] nó vì mấy món quà này.
вбегать¦3¦_¦_¦Đừng [chạy ùa vào] phòng mà không gõ cửa nữa.
влететь¦3¦Мальчик [влетел] в класс после звонка.¦The boy [rushed into] the classroom after the bell.¦Thằng bé [lao vào] lớp sau tiếng chuông.
присоединить¦1¦Завтра [присоединю] ваш отзыв к отчёту.¦Tomorrow I'll [add] your review to the report.¦Mai tôi sẽ [gộp] nhận xét của anh [vào] báo cáo.
присоединить¦2¦К городу [присоединили] соседние деревни.¦The neighbouring villages [were incorporated] into the city.¦Người ta đã [sáp nhập] các làng lân cận vào thành phố.
паркет¦3¦На таком [паркете] всегда остаются царапины.¦Scratches always stay on [parquet] like this.¦Trên loại [sàn gỗ] này lúc nào cũng còn vết xước.
гаснуть¦1¦Свет в зале медленно [гаснет].¦The lights in the hall are slowly [going out].¦Đèn trong khán phòng từ từ [tắt].
гаснуть¦2¦_¦_¦Đèn đường lần lượt [tắt] cái này đến cái khác.
обострение¦1¦_¦_¦Bà lại bị một [đợt bùng phát] viêm dạ dày.
парализовать¦1¦Снегопад может [парализовать] движение в городе.¦The snowfall may [paralyse] traffic in the city.¦Tuyết rơi có thể [làm tê liệt] giao thông trong thành phố.
хромать¦3¦У него [хромает] грамматика.¦His grammar [is weak].¦Ngữ pháp của nó còn [yếu kém].
ослабеть¦1¦_¦_¦Đến sáng giá lạnh sẽ [giảm bớt], dự báo trời ấm lên.
ослабеть¦3¦После болезни можно сильно [ослабеть].¦You can [lose] a lot of [strength] after an illness.¦Sau cơn bệnh người ta có thể [mất sức] nhiều.
слабеть¦1¦_¦_¦Đến chiều mà không có cà phê là tôi [mất sức] hẳn.
слабеть¦3¦К вечеру мороз начал [слабеть].¦By evening the frost began to [ease].¦Đến tối giá lạnh bắt đầu [giảm bớt].
слепнуть¦2¦_¦_¦Ngày trước người ta [bị mù] vì công việc như thế.
слепнуть¦3¦Старый пёс начал [слепнуть].¦The old dog started to [go blind].¦Con chó già bắt đầu [bị mù].
обостриться¦3¦_¦_¦Tôi sợ tình hình có thể [trở nên căng thẳng] ngay trong tối nay.
обостряться¦1¦Зимой у деда [обостряется] бронхит.¦In winter grandpa's bronchitis [flares up].¦Mùa đông bệnh viêm phế quản của ông lại [trở nặng].
обостряться¦3¦Ситуация на границе продолжает [обостряться].¦The situation on the border continues to [escalate].¦Tình hình biên giới tiếp tục [trở nên căng thẳng].
переполнить¦3¦Боюсь [переполнить] канистру, бензин прольётся.¦I'm afraid to [overfill] the can, the petrol will spill.¦Tôi sợ [rót quá đầy] can, xăng đổ ra mất.
переполнять¦1¦Мусор опять [переполняет] баки во дворе.¦Rubbish is [overfilling] the bins in the yard again.¦Rác lại [làm tràn] mấy cái thùng trong sân.
переполнять¦2¦_¦_¦Niềm vui [làm tràn ngập] lòng cô ấy, cô không thể im lặng.
споткнуться¦1¦_¦_¦Bật đèn lên, không thì bọn mình sẽ [vấp phải] mấy cái thùng.
споткнуться¦2¦_¦_¦Bọn mình [vấp] dây điện và làm rơi cái đèn.
спотыкаться¦2¦_¦_¦Suốt đường về bọn mình cứ [vấp] trong bóng tối.
спотыкаться¦3¦Не волнуйся и не [спотыкайся] на каждом слове.¦Don't be nervous and don't [stumble] over every word.¦Đừng hồi hộp và đừng [nói vấp] từng chữ.
разгораться¦1¦Дрова сухие, огонь быстро [разгорается].¦The wood is dry, the fire is quickly [blazing up].¦Củi khô nên lửa [cháy bùng] rất nhanh.
разгораться¦2¦_¦_¦Tối nào ở bàn ăn cũng [nổ ra] tranh luận.
разгораться¦3¦_¦_¦Nào, lửa ơi, [cháy bùng] đi, bọn tớ lạnh rồi.
разгореться¦1¦Боюсь, из-за этого [разгорится] скандал.¦I'm afraid a scandal will [break out] over this.¦Tôi sợ vì chuyện này sẽ [nổ ra] một vụ bê bối.
разрушаться¦1¦_¦_¦Căn nhà đang dần [đổ nát], không ai sửa cả.
разрушаться¦2¦_¦_¦Cây cầu [đổ nát] suốt nhiều năm cho đến khi bị đóng.
разрушаться¦3¦Зубы начинают [разрушаться] от сладкого.¦Teeth start to [decay] from sweets.¦Răng bắt đầu [bị phá hủy] vì đồ ngọt.
разрушиться¦1¦_¦_¦Nếu mưa không tạnh thì cái hàng rào sẽ [đổ sập] hẳn.
разрушиться¦2¦_¦_¦Sau vụ nổ, hai căn nhà [sụp đổ] hoàn toàn.
разрушиться¦3¦Без ремонта башня может [разрушиться].¦Without repairs the tower may [collapse].¦Không sửa thì tòa tháp có thể [sụp đổ].
насмотреться¦3¦_¦_¦[Ngắm] biển cho [no mắt] đi, nửa năm sau còn nhớ đấy.
употребляться¦1¦Это слово сейчас редко [употребляется].¦This word is rarely [used] now.¦Từ này bây giờ ít [được dùng].
ароматный¦3¦Зимой хорошо пить чай с [ароматным] мёдом.¦In winter it's nice to drink tea with [fragrant] honey.¦Mùa đông uống trà với mật ong [thơm] thì thích.
высотный¦2¦_¦_¦Anh ấy đã qua khóa huấn luyện [trên cao] và giờ làm trên cần cẩu.
высотный¦3¦_¦_¦Tôi chơi leo núi [ở độ cao lớn], hè này đi Elbrus.
гранит¦2¦Памятник сделан из красного [гранита].¦The monument is made of red [granite].¦Tượng đài này làm bằng [đá granit] đỏ.
граничить¦1¦_¦_¦Hai lô đất của chúng tôi [giáp ranh] ngay sau hàng rào cũ.
граничить¦2¦_¦_¦Khu vườn của anh ấy [tiếp giáp] rừng, rất yên tĩnh.
граничить¦3¦Его смелость порой может [граничить] с глупостью.¦His courage can sometimes [verge] on stupidity.¦Sự gan dạ của anh ta đôi khi [gần như là] ngu ngốc.
сушка¦3¦К чаю остались только [сушки].¦Only [dry bagel rings] were left for tea.¦Chỉ còn [bánh vòng khô] để ăn với trà.
малина¦3¦Пирог с [малиной] уже остыл.¦The [raspberry] pie has already cooled down.¦Bánh [mâm xôi] nguội rồi.
крупа¦1¦_¦_¦Trong tủ hết [hạt ngũ cốc] rồi, mua trên đường về nhé.
крупа¦2¦_¦_¦Tôi cần một cốc [hạt ngũ cốc] để nấu súp.
крупа¦3¦_¦_¦Trong mấy loại [hạt ngũ cốc] này đôi khi có rác.
квас¦2¦Бабушка угостила нас домашним [квасом].¦Grandma treated us to homemade [kvass].¦Bà mời bọn mình [kvas] tự làm.
керамика¦3¦Она увлекается [керамикой] с детства.¦She's been into [ceramics] since childhood.¦Cô ấy mê [nghề gốm] từ nhỏ.
гравюра¦1¦_¦_¦Bức [tranh khắc] cũ này tôi được thừa từ ông nội.
гравюра¦2¦Он полгода работал над этой [гравюрой].¦He worked on this [engraving] for half a year.¦Anh ấy làm bức [tranh khắc] này suốt nửa năm.
гравюра¦3¦_¦_¦Trên những bức [tranh khắc] này là Petersburg xưa.
антракт¦3¦_¦_¦Tôi chúa ghét những [giờ nghỉ giữa các màn] dài ở nhà hát.
репродукция¦1¦_¦_¦Ở hành lang nhà tôi treo một [bản sao] tranh Levitan.
репродукция¦3¦_¦_¦Trong tiệm đầy [bản in lại] rẻ tiền.
дублёнка¦1¦_¦_¦Cái [áo khoác da cừu] của tôi mùi như tủ cũ.
дублёнка¦2¦_¦_¦Cuối cùng tôi cũng đem [áo khoác da cừu] đi giặt khô.
дублёнка¦3¦_¦_¦Cửa hàng này không có cái [áo khoác da cừu] nào cả.
проспать¦3¦Он [проспал] всю дорогу до дома.¦He [slept through] the whole way home.¦Anh ấy [ngủ suốt] cả đường về nhà.
гвоздика¦3¦Добавь в глинтвейн немного [гвоздики].¦Add a few [cloves] to the mulled wine.¦Cho thêm ít [đinh hương] vào rượu nóng nhé.
ромашка¦2¦_¦_¦Tôi cho thêm chút mật ong vào trà [cúc La Mã].
хвойный¦2¦_¦_¦Bọn mình mua xà phòng mùi [lá kim], thơm như trong rừng.
"""
CAU = {}
for d in CAU_TXT.strip().splitlines():
    w, i, *ba = d.split("¦")
    assert len(ba) == 3 and (w, int(i)) not in CAU, d
    CAU[w, int(i)] = tuple(None if x == "_" else x.replace("[", "<hl>").replace("]", "</hl>") for x in ba)

MEANING = {   # danh sách nghĩa Anh MỚI, ngăn ";"
    "постареть": "to grow old; to age",
    "почернеть": "to turn black; to blacken",
    "пожелтеть": "to turn yellow",
    "доброжелательный": "kind; benevolent; friendly; well-disposed",
    "отличительный": "distinguishing; distinctive",
    "обострение": "worsening; aggravation; flare-up; escalation; intensification",
    "обостриться": "to worsen; to flare up; to escalate; to intensify; to become strained; to become more acute (of senses)",
    "обостряться": "to worsen; to flare up; to escalate; to intensify; to become strained; to become more acute (of senses)",
    "демографический": "demographic",
    "грузчик": "loader; mover; stevedore",
    "обозреватель": "commentator; columnist; editor (of a news section)",
    "заварить": "to brew (tea/coffee); to steep; to pour boiling water on",
    "ромашка": "camomile; chamomile; oxeye daisy; marguerite",
    "оливковый": "olive (adj); olive-coloured; olive-green",
    "безлюдный": "deserted; empty of people; uninhabited",
    "кратковременный": "short-lived; brief; momentary",
    "волевой": "strong-willed; volitional",
    "всесторонний": "comprehensive; thorough; all-round",
    "инициативный": "full of initiative; proactive",
    "требовательный": "demanding; exacting; strict; insistent; peremptory",
    "влетать": "to fly in; to rush in; to dash in; to burst in",
    "влететь": "to fly in; to rush in; to dash in; to burst in",
    "вбегать": "to come running in; to run in; to rush in",
    "вбежать": "to come running in; to run in; to rush in",
    "баловать": "to spoil; to pamper; to coddle; to indulge; to treat",
    "прожиточный": "living; subsistence",
    "закономерный": "conforming to a law; natural; logical; inevitable",
    "разочаровываться": "to be disappointed (in); to become disillusioned (with); to lose faith (in)",
    "присоединить": "to join; to attach; to connect; to add; to annex; to incorporate",
    "переполнить": "to overfill; to overwhelm (with a feeling)",
    "переполнять": "to overfill; to overwhelm (with a feeling)",
    "наесться": "to eat one's fill; to be full (from food)",
    "разгореться": "to blaze up; to flare up; to flame up; to catch fire properly; to break out; to erupt; to light up; to glow; to flush",
    "повыситься": "to increase; to rise; to be promoted",
    "повышаться": "to rise; to increase; to be promoted",
    "слабеть": "to weaken; to grow weak; to lose strength; to diminish",
    "беседка": "gazebo; arbour; summerhouse; pavilion",
    "сбербанк": "Sberbank; Savings Bank",
}


def _phan(g, k, cu, moi):
    ds = g["parts"][k]
    assert any(x["f"] == cu for x in ds), (k, cu, ds)
    if moi is None:
        g["parts"][k] = [x for x in ds if x["f"] != cu]
        if not g["parts"][k]:
            del g["parts"][k]
    else:
        for x in ds:
            x["f"] = moi if x["f"] == cu else x["f"]


def g_tsen(g):
    assert g["aspect"] == "perfective" and not any(g["present"])
    g["aspect"], g["present"] = "imperfective", list(g["presfut"])
    g["future"] = [b + " цени́ться" for b in ("бу́ду", "бу́дешь", "бу́дет", "бу́дем", "бу́дете", "бу́дут")]
    _phan(g, "gerundPast", "ценившись", "цени́вшись")


def g_siren(g):
    assert g["decl"]["pl"]["acc"] == "сире́ней"
    g["decl"]["pl"]["acc"] = "сире́ни"


def g_besp(g):
    assert g["shorts"][3] == "беспоко́йы"
    g["shorts"][3] = "беспоко́йны"


def g_ich(g):      # tính từ -ический: không có dạng ngắn, trạng từ là -ически
    assert g["shorts"][3].endswith("чески"), g["shorts"]
    g["shorts"], g["adverb"] = [""] * 4, g["shorts"][3]


def g_olivk(g):
    assert g["shorts"][0] == "оли́вков"
    g["shorts"], g["adverb"] = [""] * 4, ""


def g_mazat(g):
    g["partners"].remove("зама́зать")


GR = {"цениться": g_tsen, "сирень": g_siren, "беспокойный": g_besp, "оптимистический": g_ich,
      "сатирический": g_ich, "косметический": g_ich, "оливковый": g_olivk, "мазать": g_mazat,
      "весить": lambda g: _phan(g, "passivePast", "вешённый", None),
      "облить": lambda g: _phan(g, "passivePast", "облитый", "обли́тый"),
      "проплывать": lambda g: _phan(g, "passivePresent", "проплываемый", "проплыва́емый"),
      "присоединить": lambda g: _phan(g, "gerundPast", "присоединя́", None),
      "расслышать": lambda g: _phan(g, "gerundPast", "расслы́ша", None),
      "парализовать": lambda g: _phan(g, "passivePresent", "парализуемый", "парализу́емый"),
      "бредить": lambda g: _phan(g, "gerundPresent", "бредя", "бре́дя"),
      "подрабатывать": lambda g: _phan(g, "passivePresent", "подрабатываемый", "подраба́тываемый"),
      "предчувствовать": lambda g: (_phan(g, "passivePresent", "предчувствуемый", "предчу́вствуемый"),
                                    _phan(g, "passivePast", "предчувствованный", "предчу́вствованный"))}
O = {"сбербанк": {"Word": "Сберба́нк"}, "цениться": {"AspectBadge": '<div class="badge aspect-ipf">IMPF</div>'}}

kho = {n["noteId"]: {k: v["value"] for k, v in n["fields"].items()} for n in doc_notes_cua_model(MODEL_NAME)}
id_ = {}
for i, f in kho.items():
    id_.setdefault(f["WordClean"].strip(), []).append(i)


def mot(w):
    assert len(id_[w]) == 1, (w, id_[w])
    return id_[w][0]


ghi, gram = {}, {}
for w, o in O.items():
    ghi.setdefault(mot(w), {}).update(o)
for w, moi in MEANING.items():
    assert re.fullmatch(r'<ol class="meaning-list">(<li>[^<]*</li>)+</ol>', kho[mot(w)]["Meaning"]), w
    ghi.setdefault(mot(w), {})["Meaning"] = '<ol class="meaning-list">' + "".join(
        f"<li>{x.strip()}</li>" for x in moi.split(";")) + "</ol>"
for w, fn in GR.items():
    g = copy.deepcopy(json.loads(kho[mot(w)]["GrammarJSON"]))
    fn(g)
    gram[mot(w)] = g
_hl = re.compile(r'<span class="hl">(.*?)</span>')
_DAU = {"ru": r'<div class="ex-ru">(.*?)(?:<span class="nghe"|</div>)', "en": r'<div class="ex-en">(.*?)</div>',
        "vi": r'<span class="vi-text">(.*?)</span></div>'}
for (w, i), moi in CAU.items():
    nid = mot(w)
    h = ghi.get(nid, {}).get("ExamplesHTML", kho[nid]["ExamplesHTML"])
    khoi = re.findall(r"<details\b.*?</details>", h, re.S)
    assert len(khoi) == 3, w
    cu = {k: _hl.sub(r"<hl>\1</hl>", re.search(p, khoi[i - 1], re.S).group(1)) for k, p in _DAU.items()}
    ex = {k: m or cu[k] for k, m in zip(("ru", "en", "vi"), moi)}
    assert all("<hl>" in x for x in ex.values()), (w, i, ex)
    if moi[2]:
        v = ghi.get(nid, {}).get("Vietnamese", kho[nid]["Vietnamese"]).lower()
        b = " ".join(re.findall(r"<hl>(.*?)</hl>", moi[2])).lower()
        if b not in v:
            print("  ? ngoài đề:", w, i, "|", b, "|", v)
    ghi.setdefault(nid, {})["ExamplesHTML"] = thay_vi_du(h, i - 1, ex)
cz = {}
for nid in set(gram) | {n for n, o in ghi.items() if "ExamplesHTML" in o}:
    f = kho[nid]
    g = gram.get(nid) or json.loads(f["GrammarJSON"])
    cz[nid] = dung_cloze(ghi.get(nid, {}).get("ExamplesHTML", f["ExamplesHTML"]), g, f["WordClean"])
    if not cz[nid]:
        print("  ! cloze trống:", f["WordClean"], "| trước đây", bool(f["ClozeHTML"]))
print("KHAN: mọi bản cũ khớp —", len(set(ghi) | set(gram)), "thẻ,", len(CAU), "câu")
if "--apply" not in sys.argv:
    raise SystemExit
run_backup()
if not sync_truoc_khi_ghi_lo("vá k257-k266"):
    raise SystemExit("sync hỏng")
for nid, g in gram.items():
    grammar.remember(kho[nid]["WordClean"].strip(), g, note_id=nid)
for nid, o in ghi.items():
    f = kho[nid]
    if "ExamplesHTML" in o:
        h = gan_tieng_vi_du(o["ExamplesHTML"])
        assert h.count("<audio") == 3 == h.count('class="nghe"'), nid
        o["ExamplesHTML"] = h
        o["ClozeHTML"] = dung_cloze(h, gram.get(nid) or json.loads(f["GrammarJSON"]), f["WordClean"])
    assert update_note_fields(nid, o), nid
    print("ok", f["WordClean"], list(o))
print("sync:", sync_now())
