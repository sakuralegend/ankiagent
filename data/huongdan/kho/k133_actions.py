# -*- coding: utf-8 -*-
"""k133 — actions: 8 cặp thể + 6 từ lẻ, trục là GỐC dùng chung với thẻ cũ.

Không khối hệ thống. Khuôn gốc khớp các lô song song (luồng chính giao):
мен- «ĐỔI» (обме́н k131, меня́ть cũ) · гор- «CHÁY, ĐỐT» (го́ре k129) ·
дол-/длин- «DÀI» (надо́лго k126) · готов- «SẴN SÀNG» · вест- «TIN, BIẾT»
(KHÁC gốc вес- «treo» của пове́сить k131).
Mỗi vế của cặp chỉ nói phần của nó, không chép nhau.
"""

S = {}

S["навестить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">tới, đặt LÊN ai đó</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вест-</span>'
    '<span class="hd-gloss">TIN, BIẾT — như <b>весть</b> tin tức</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tìm tới ai để biết TIN người đó ⇒ đến thăm. Ngôi «tôi» đổi '
    '<i>ст → щ</i>: <b>навещу́</b>, nhưng <b>навести́шь</b> — chữ <i>щ</i> đó chính là thân của '
    'cặp thể <b>навеща́ть</b>.</div>'
    '<div class="hd-warn">Thăm NGƯỜI (bà, bạn ốm): <b>навести́ть</b> + cách 4. Thăm NƠI chốn '
    '(bảo tàng, thành phố): <b>посети́ть</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: nối với <b>весть</b> là từ nguyên. Đừng lẫn với '
    '<b>пове́сить</b> (treo) — mặt chữ gần giống, KHÁC gốc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>навеща́ть</b> đến thăm (CHT) · <b>весть</b> tin tức · '
    '<b>изве́стный</b> nổi tiếng, được biết đến · <b>извести́ть</b> báo tin</div>'
)

S["навещать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-вещ-</span>'
    '<span class="hd-gloss">tới hỏi TIN — như <b>навести́ть</b>, <i>ст</i> đã hoá <i>щ</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành, chia đều: <b>навеща́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thăm đều đặn, thăm nhiều lần: <i>навеща́ть ба́бушку ка́ждое воскресе́нье</i>. '
    'Mẹo nhận cặp: vế CHT mang sẵn chữ <i>щ</i> mà vế HT chỉ có ở ngôi «tôi» '
    '(<b>навещу́</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>навести́ть</b> đến thăm (HT) · <b>весть</b> tin tức · '
    '<b>изве́стный</b> nổi tiếng, được biết đến</div>'
)

S["гореть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">гор-</span>'
    '<span class="hd-gloss">CHÁY, ĐỐT</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ть</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2: <b>горю́, гори́шь, горя́т</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <i>гор-</i> nằm sẵn trong hai tính từ đã học: <b>горя́чий</b> nóng '
    '(như bị đốt) và <b>го́рький</b> đắng (vị cháy lưỡi). Cặp thể là <b>сгоре́ть</b>.</div>'
    '<div class="hd-warn"><b>Свет гори́т</b> = đèn đang sáng. Tiếng Nga coi đèn, nến, lửa '
    'đều là «cháy» — nên <b>горе́ть</b> cũng là sáng đèn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сгоре́ть</b> cháy rụi (HT) · <b>горя́чий</b> nóng · '
    '<b>го́рький</b> đắng · <b>го́ре</b> nỗi đau «thiêu đốt»</div>'
)

S["сгореть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">tiền tố thể hoàn thành — kết quả: cháy tới HẾT</span></div>'
    '<div class="hd-row"><span class="hd-piece">-гор-е́ть</span>'
    '<span class="hd-gloss">CHÁY — chính là <b>горе́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cháy xong, không còn gì ⇒ cháy rụi. Chia y như <b>горе́ть</b>: '
    '<b>сгорю́, сгори́шь</b>.</div>'
    '<div class="hd-warn"><b>Ла́мпочка сгоре́ла</b> = bóng đèn cháy (hỏng hẳn). '
    '<b>сгоре́ть на со́лнце</b> = bị cháy nắng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>горе́ть</b> cháy (CHT) · <b>горя́чий</b> nóng · '
    '<b>го́ре</b> nỗi đau «thiêu đốt»</div>'
)

S["ударить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">уда́р-</span>'
    '<span class="hd-gloss"><b>уда́р</b> cú ĐÁNH, đòn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2: <b>уда́рю, уда́ришь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giáng MỘT cú <b>уда́р</b> ⇒ đánh, đập. Ai bị đánh ở cách 4, chỗ bị đánh '
    'đi với <b>по</b> + cách 3: <i>уда́рить кого́-то по лицу́</i> = đánh vào mặt. '
    'Cặp thể là <b>ударя́ть</b>; còn <b>бить</b> là đánh liên tục.</div>'
    '<div class="hd-warn"><b>ударе́ние</b> = TRỌNG ÂM — âm tiết bị «đánh» mạnh vào. Chính cái '
    'dấu trên mọi từ bạn đang học.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уда́р</b> cú đánh, đòn · <b>ударя́ть</b> đánh (CHT) · '
    '<b>ударе́ние</b> trọng âm</div>'
)

S["поспешить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố thể hoàn thành — không thêm nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-спеш-и́ть</span>'
    '<span class="hd-gloss">VỘI — chính là <b>спеши́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vội lên một lần cho kịp việc trước mắt: <i>Поспеши́, а то опозда́ем!</i> '
    '= nhanh lên, không thì muộn. Chia như <b>спеши́ть</b>: <b>поспешу́, поспеши́шь</b>.</div>'
    '<div class="hd-warn"><b>поспеши́ть с вы́водами</b> = vội kết luận — vội tới mức hấp tấp.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>спеши́ть</b> vội (CHT) · <b>спе́шка</b> sự vội vàng · '
    '<b>не спеша́</b> thong thả</div>'
)

S["спешить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">спеш-</span>'
    '<span class="hd-gloss">VỘI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2: <b>спешу́, спеши́шь, спеша́т</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đang vội, lúc nào cũng vội: <i>Куда́ ты спеши́шь?</i> = bạn vội đi đâu thế? '
    'Cặp thể là <b>поспеши́ть</b>.</div>'
    '<div class="hd-warn"><b>Часы́ спеша́т</b> = đồng hồ chạy NHANH — đồng hồ cũng «vội».</div>'
    '<div class="hd-warn">⚠️ Mức tin: nối <i>спеш-</i> với <b>успе́ть</b> (kịp) và <b>успе́х</b> '
    '(thành công) là từ nguyên — gốc chung «tiến tới, kịp».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поспеши́ть</b> vội (HT) · <b>спе́шка</b> sự vội vàng · '
    '<b>не спеша́</b> thong thả · <b>успе́ть</b> kịp</div>'
)

S["добавить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-</span>'
    '<span class="hd-gloss">TỚI, cho đến đủ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бав-</span>'
    '<span class="hd-gloss">mảnh chung của <b>приба́вить</b> (tăng thêm), <b>уба́вить</b> (bớt đi) — một mình không có nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bù thêm cho đến đủ ⇒ thêm vào. Ngôi «tôi» chèn <i>л</i> sau <i>в</i>: '
    '<b>доба́влю</b>, nhưng <b>доба́вишь</b> — chữ <i>вл</i> đó là thân của <b>добавля́ть</b>.</div>'
    '<div class="hd-warn">Thêm «một ít» thì dùng cách 2: <b>Доба́вь со́ли</b> = cho thêm chút muối. '
    'Trong lời kể: <i>«…», — доба́вил он</i> = anh ấy nói thêm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>добавля́ть</b> thêm (CHT) · <b>доба́вка</b> phần thêm · '
    '<b>приба́вить</b> tăng thêm · <b>уба́вить</b> bớt đi</div>'
)

S["добавлять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-бавл-</span>'
    '<span class="hd-gloss">bù thêm cho đủ — như <b>доба́вить</b>, <i>в</i> đã thành <i>вл</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành, chia đều: <b>добавля́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thêm thường xuyên, thêm từ từ: <i>Ма́ма всегда́ добавля́ет чесно́к</i>. '
    'Mẹo nhận cặp: vế CHT mang sẵn <i>вл</i> mà vế HT chỉ có ở ngôi «tôi» '
    '(<b>доба́влю</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>доба́вить</b> thêm (HT) · <b>доба́вка</b> phần thêm · '
    '<b>приба́вить</b> tăng thêm · <b>уба́вить</b> bớt đi</div>'
)

S["заменить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">vào CHỖ của cái khác</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мен-</span>'
    '<span class="hd-gloss">ĐỔI — như <b>меня́ть</b>, <b>обме́н</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đổi một thứ vào chỗ thứ kia ⇒ thay thế. Trọng âm lùi từ ngôi «bạn»: '
    '<b>заменю́</b>, nhưng <b>заме́нишь, заме́нят</b>.</div>'
    '<div class="hd-warn">Thứ bị bỏ ở cách 4, thứ mới ở cách 5: <b>замени́ть са́хар мёдом</b> = '
    'thay đường BẰNG mật ong. Cũng hay nói <i>замени́ть … на</i> + cách 4.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>заменя́ть</b> thay thế (CHT) · <b>заме́на</b> sự thay thế, người thay · '
    '<b>меня́ть</b> đổi · <b>обме́н</b> trao đổi · <b>измени́ть</b> thay đổi</div>'
)

S["заменять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-мен-</span>'
    '<span class="hd-gloss">đổi vào CHỖ — như <b>замени́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành, chia đều: <b>заменя́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thay thường xuyên, hoặc đứng thay ai một thời gian: '
    '<i>Он заменя́л меня́ на рабо́те</i> = anh ấy làm thay tôi. Trọng âm đứng yên trên '
    '<i>-я́-</i> ở mọi ngôi — khác <b>замени́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>замени́ть</b> thay thế (HT) · <b>заме́на</b> sự thay thế · '
    '<b>меня́ть</b> đổi · <b>обме́н</b> trao đổi</div>'
)

S["добиваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-</span>'
    '<span class="hd-gloss">TỚI đích</span></div>'
    '<div class="hd-row"><span class="hd-piece">-би-</span>'
    '<span class="hd-gloss">ĐÁNH — chính là <b>бить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва́-ться</span>'
    '<span class="hd-gloss"><i>-ва-</i> thể chưa hoàn thành + <i>-ся</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đánh mở đường cho tới đích ⇒ cố cho bằng được. Thể CHT nên nhấn vào '
    'QUÁ TRÌNH nỗ lực, chưa nói là đã được. Chia đều: <b>добива́юсь, добива́ешься</b>.</div>'
    '<div class="hd-warn">Cái muốn đạt ở cách 2: <b>добива́ться успе́ха</b>. '
    '<b>добива́ться своего́</b> = làm cho bằng được ý mình.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>доби́ться</b> đạt được (HT) · <b>бить</b> đánh · '
    '<b>успе́х</b> thành công</div>'
)

S["добиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-</span>'
    '<span class="hd-gloss">TỚI đích</span></div>'
    '<div class="hd-row"><span class="hd-piece">-би́ть-ся</span>'
    '<span class="hd-gloss">ĐÁNH — chính là <b>бить</b>, thêm <i>-ся</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đánh mở đường tới đích và TỚI được ⇒ đạt được. Thân hiện tại chia y như '
    '<b>бить</b> (<b>бью, бьёшь</b>): <b>добью́сь, добьёшься</b> — chữ <i>и</i> rơi, '
    'thay bằng <i>ь</i>.</div>'
    '<div class="hd-warn">Cái đạt được ở cách 2: <b>доби́ться ски́дки</b> = xin được giảm giá. '
    '<b>доби́ться своего́</b> = đạt được ý mình.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>добива́ться</b> cố đạt (CHT) · <b>бить</b> đánh</div>'
)

S["готовиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">гото́в-</span>'
    '<span class="hd-gloss">SẴN SÀNG — như <b>гото́вый</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить-ся</span>'
    '<span class="hd-gloss">đuôi lớp 2 + <i>-ся</i>: làm cho CHÍNH MÌNH</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm cho chính mình sẵn sàng ⇒ chuẩn bị. Ngôi «tôi» chèn <i>л</i>: '
    '<b>гото́влюсь</b>, nhưng <b>гото́вишься</b>. Cặp thể là <b>подгото́виться</b>.</div>'
    '<div class="hd-warn">Chuẩn bị CHO cái gì: <b>к</b> + cách 3 — <b>гото́виться к экза́мену</b>. '
    'Không <i>-ся</i> thì khác: <b>гото́вить</b> обе́д = nấu bữa trưa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гото́вый</b> sẵn sàng · <b>гото́вить</b> nấu, chuẩn bị · '
    '<b>подгото́виться</b> chuẩn bị (HT) · <b>подгото́вка</b> sự chuẩn bị</div>'
)

S["подготовиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span>'
    '<span class="hd-gloss">tiền tố thể hoàn thành — không thêm nghĩa riêng đáng kể</span></div>'
    '<div class="hd-row"><span class="hd-piece">-гото́в-ить-ся</span>'
    '<span class="hd-gloss">làm mình SẴN SÀNG — chính là <b>гото́виться</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chuẩn bị xong, đã sẵn sàng: <i>Я хорошо́ подгото́вилась к собесе́дованию</i>. '
    'Chia như <b>гото́виться</b>: <b>подгото́влюсь, подгото́вишься</b>; vẫn đòi <b>к</b> + cách 3.</div>'
    '<div class="hd-warn">Đừng lẫn với <b>подгото́вить</b> (không <i>-ся</i>) = chuẩn bị CÁI GÌ, '
    'cho AI — <b>подгото́вить докла́д</b> soạn bài báo cáo.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гото́виться</b> chuẩn bị (CHT) · <b>подгото́вка</b> sự chuẩn bị · '
    '<b>гото́вый</b> sẵn sàng</div>'
)

S["измениться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">из-</span>'
    '<span class="hd-gloss">RA KHỎI trạng thái cũ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мен-</span>'
    '<span class="hd-gloss">ĐỔI — như <b>меня́ть</b>, <b>обме́н</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть-ся</span>'
    '<span class="hd-gloss">đuôi lớp 2 + <i>-ся</i>: tự nó đổi</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đổi ra khác cái cũ, và chính chủ ngữ đổi. Trọng âm lùi từ ngôi «bạn»: '
    '<b>изменю́сь</b>, nhưng <b>изме́нишься</b>.</div>'
    '<div class="hd-warn">Thẻ cũ <b>измени́ть</b> = ai đó đổi CÁI GÌ: <i>измени́ть план</i>. '
    'Có <i>-ся</i> = tự nó đổi: <i>План измени́лся</i>. <i>Ты не измени́лась!</i> = bạn chẳng khác xưa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>изменя́ться</b> thay đổi (CHT) · <b>измени́ть</b> thay đổi cái gì · '
    '<b>измене́ние</b> sự thay đổi · <b>меня́ть</b> đổi · <b>замени́ть</b> thay thế</div>'
)

S["изменяться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">из-мен-</span>'
    '<span class="hd-gloss">ĐỔI ra khác — như <b>измени́ться</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́ть-ся</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành + <i>-ся</i>, chia đều: <b>изменя́юсь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đang đổi, đổi liên tục: <i>Пого́да изменя́ется ка́ждый час</i>. '
    'Trọng âm đứng yên trên <i>-я́-</i> ở mọi ngôi — khác <b>измени́ться</b>.</div>'
    '<div class="hd-warn">Thẻ cũ <b>изменя́ть</b> (không <i>-ся</i>) = đổi CÁI GÌ. '
    'Có <i>-ся</i> thì không mang tân ngữ: chính chủ ngữ biến đổi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>измени́ться</b> thay đổi (HT) · <b>изменя́ть</b> thay đổi cái gì · '
    '<b>измене́ние</b> sự thay đổi · <b>меня́ть</b> đổi</div>'
)

S["длина"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дл-</span>'
    '<span class="hd-gloss">DÀI — như <b>дли́нный</b>, <b>до́лгий</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ина́</span>'
    '<span class="hd-gloss">đuôi danh từ chỉ KÍCH THƯỚC, giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc tính từ + <i>-ина́</i> ⇒ danh từ đo lường, cùng khuôn với '
    '<b>ширина́</b> chiều rộng (từ <b>широ́кий</b>), <b>глубина́</b> chiều sâu (từ <b>глубо́кий</b>). Trọng âm nằm ở đuôi; số nhiều (hiếm dùng) lùi về '
    'gốc: <b>дли́ны</b>.</div>'
    '<div class="hd-warn"><b>в длину́</b> = theo chiều dài: <i>два ме́тра в длину́</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дли́нный</b> dài · <b>до́лгий</b> lâu · <b>надо́лго</b> lâu dài · '
    '<b>дли́ться</b> kéo dài</div>'
)

S["тишина"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">тиш-</span>'
    '<span class="hd-gloss">YÊN — <b>ти́хий</b>, <i>х</i> đã hoá <i>ш</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ина́</span>'
    '<span class="hd-gloss">đuôi danh từ trừu tượng, giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>ти́хий</b> yên tĩnh + <i>-ина́</i> ⇒ sự yên tĩnh — cùng khuôn với '
    '<b>длина́</b>. Phép <i>х → ш</i> lặp lại ở so sánh hơn <b>ти́ше</b> (khẽ hơn, «khẽ thôi!»).</div>'
    '<div class="hd-warn"><b>Тишина́!</b> đứng một mình = «Trật tự! Im lặng!».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ти́хий</b> yên tĩnh · <b>ти́хо</b> khẽ, yên lặng · '
    '<b>ти́ше</b> khẽ hơn</div>'
)

S["практический"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">практ-</span>'
    '<span class="hd-gloss">mượn, cùng gốc tiếng Anh <i>practice</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ческий</span>'
    '<span class="hd-gloss">= <i>-ical</i> tiếng Anh, như <b>техни́ческий</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đổi <i>-ical</i> thành <i>-и́ческий</i> là ra: <i>practical</i> → '
    '<b>практи́ческий</b>. Nghĩa là THUỘC VỀ thực hành: <i>практи́ческое заня́тие</i> = buổi '
    'thực hành.</div>'
    '<div class="hd-warn">Người, đồ vật thiết thực, tiện dụng: <b>практи́чный</b> — khác đuôi, '
    'khác nghĩa.</div>'
    '<div class="hd-warn"><b>практи́чески</b> = hầu như, gần như — y như <i>practically</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пра́ктика</b> thực hành, thực tiễn · <b>практи́чный</b> thiết thực · '
    '<b>практи́чески</b> hầu như</div>'
)

S["сухой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сух-</span>'
    '<span class="hd-gloss">KHÔ — gốc trơn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́й</span>'
    '<span class="hd-gloss">đuôi tính từ mang trọng âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dạng ngắn trọng âm nhảy: <b>сух, суха́, су́хо, су́хи</b>. '
    'So sánh hơn đổi <i>х → ш</i>: <b>су́ше</b> — cùng phép đó cho ra <b>су́ша</b> '
    '(đất liền, chỗ KHÔ) và <b>суши́ть</b>. <b>су́хо</b> còn là trạng từ: khô khan, lạnh nhạt.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>суши́ть</b> phơi khô, sấy · <b>су́ша</b> đất liền</div>'
)

S["железный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">желе́з-</span>'
    '<span class="hd-gloss"><b>желе́зо</b> SẮT</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ный</span>'
    '<span class="hd-gloss">đuôi biến danh từ thành tính từ «bằng…, thuộc…»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>желе́зо</b> sắt + <i>-ный</i> ⇒ bằng sắt. Trọng âm đứng yên trên '
    '<i>-ле́-</i>. Dạng ngắn giống đực chèn <i>е</i>: <b>желе́зен</b> — chỉ gặp ở nghĩa bóng '
    '(cứng như sắt).</div>'
    '<div class="hd-warn"><b>желе́зная доро́га</b> = đường sắt, viết tắt <b>ж/д</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>желе́зо</b> sắt · <b>железнодоро́жный</b> thuộc đường sắt</div>'
)


# Field `Vietnamese` (README §2c): thuần danh sách nghĩa. Bỏ mọi nhãn thể trá hình
# «(xong)», «(một lần)», «(thường xuyên)», «(đang, thường)», «đang …» — badge Aspect đã in sẵn.
V = {
    "навестить": "đến thăm",                          # bỏ «(một lần)» — nhãn thể
    "навещать": "đến thăm",                           # bỏ «(thường xuyên)» — nhãn thể
    "гореть": "cháy, bốc cháy, sáng đèn, rực sáng",   # bỏ «đang» — nhãn thể; gloss: be on fire / be lit / glow
    "поспешить": "vội, vội vã, nhanh lên",            # bỏ «(một lần)» — nhãn thể
    "спешить": "vội, vội vã, gấp, chạy nhanh",        # thêm «chạy nhanh» — gloss «to gain (of a clock)»
    "добавить": "thêm, bổ sung, nói thêm",            # RÚT «thêm vào» — trùng включи́ть (cũ, cùng 4 badge)
    "добавлять": "thêm, bổ sung, nói thêm",           # giữ khớp vế HT; gloss: supplement / say in addition
    "заменить": "thay thế",                           # bỏ «(xong)»; KHÔNG thêm «thay» — trùng поменя́ть
    "добиться": "đạt được",                           # bỏ «(xong)» — nhãn thể
    "подготовиться": "chuẩn bị",                      # bỏ «xong» — nhãn thể trá hình
    "измениться": "thay đổi, đổi khác",               # bỏ «(xong)»; gloss: become different
    "изменяться": "thay đổi, biến đổi",               # bỏ «(đang, thường)»; gloss: be transformed / vary
    "тишина": "sự yên tĩnh, sự im lặng",              # gloss «silence» — thiếu nghĩa im lặng
}
