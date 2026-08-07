# -*- coding: utf-8 -*-
"""k43 — qualities: 18 TRẠNG TỪ phẩm chất, gần hết là <tính từ bỏ đuôi + -о>.

Trục của lô: mỗi thẻ chỉ nói về CHÍNH TỪ ĐÓ — gốc nó là gì, gốc đó còn mở ra
từ nào. Luật "tính từ → trạng từ bằng -о" đã dạy ở lô 12, ở đây chỉ nhắc bằng
một dòng chẻ từ, KHÔNG dựng lại bảng.
"""

S = {}
V = {}

# ------------------------------------------------------------------ số lượng
S["мало"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мал-</span>'
    '<span class="hd-gloss">NHỎ, ÍT</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc với <b>ма́ленький</b> "nhỏ": ít chính là '
    '"nhỏ về số lượng".</div>'
    '<div class="hd-warn"><b>ма́ло</b> kéo danh từ đứng sau về cách 2: '
    '<b>ма́ло вре́мени</b> ít thời gian.</div>'
    '<div class="hd-warn"><b>ма́ло</b> = quá ít, thiếu (chê). '
    '<b>немно́го</b> = một chút, vừa đủ (trung tính).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ма́ленький</b> nhỏ · <b>ма́лый</b> bé · '
    '<b>малы́ш</b> đứa bé · <b>нема́ло</b> không ít</div>'
)
V["мало"] = "ít, quá ít, không đủ"

S["очень"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: <b>о́чень</b> là một khối trơn, trong '
    'tiếng Nga hiện đại không còn gốc sống nào để tách ra.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhớ bằng VỊ TRÍ thay vì bằng gốc: <b>о́чень</b> luôn '
    'đứng ngay trước cái nó tăng cường — <b>о́чень хорошо́</b>, '
    '<b>о́чень люблю́</b>.</div>'
    '<div class="hd-warn">Trước DANH TỪ thì phải mượn <b>мно́го</b>: '
    '<b>о́чень мно́го рабо́ты</b> rất nhiều việc.</div>'
)
V["очень"] = "rất, lắm, vô cùng"

# ------------------------------------------------------------ nặng / khó / tệ
S["тяжело"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">тяж-</span>'
    '<span class="hd-gloss">NẶNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ел- + -о</span>'
    '<span class="hd-gloss">đuôi tính từ → trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen là "nặng" (<b>тяжёлый</b>), nghĩa bóng là '
    '"nặng nhọc, vất vả" — dùng cho cả cơ bắp lẫn tâm trạng.</div>'
    '<div class="hd-warn"><b>тяжело́</b> nói về SỨC NẶNG (nặng tay, nặng lòng); '
    '<b>тру́дно</b> nói về ĐỘ KHÓ (khó giải, khó nhớ).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тяжёлый</b> nặng · <b>тя́жесть</b> sức nặng, gánh '
    'nặng · <b>тяжеле́е</b> nặng hơn</div>'
)
V["тяжело"] = "nặng, nặng nề, nặng nhọc, vất vả"

S["трудно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">труд-</span>'
    '<span class="hd-gloss">LAO ĐỘNG, CÔNG SỨC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н- + -о</span>'
    '<span class="hd-gloss">đuôi tính từ → trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>труд</b> là "lao động": việc nào đòi bỏ công '
    'sức thì việc đó khó.</div>'
    '<div class="hd-warn">Mẫu câu hay gặp: người ở cách 3 + <b>тру́дно</b> + '
    'động từ nguyên thể — <b>мне тру́дно поня́ть</b> tôi khó hiểu được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>труд</b> lao động · <b>тру́дный</b> khó · '
    '<b>тру́дность</b> khó khăn · <b>труди́ться</b> làm lụng</div>'
)
V["трудно"] = "khó, khó khăn"

S["плохо"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">плох-</span>'
    '<span class="hd-gloss">XẤU, TỆ (gốc trơn)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ nhỏ thêm được. Trạng từ giữ trọng '
    'âm ở gốc <b>пло́хо</b>, còn tính từ đẩy nó ra đuôi: <b>плохо́й</b>.</div>'
    '<div class="hd-warn">So sánh hơn ĐỔI HẲN GỐC: <b>пло́хо → ху́же</b> tệ hơn '
    '(y như <i>bad → worse</i>). Không có dạng nào kiểu «плохее».</div>'
    '<div class="hd-warn"><b>мне пло́хо</b> = "tôi thấy khó ở, mệt", không phải '
    '"tôi tệ".</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>плохо́й</b> xấu, tồi · <b>непло́хо</b> không tệ</div>'
)
V["плохо"] = "xấu, tồi, kém, dở"

S["неплохо"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не-</span>'
    '<span class="hd-gloss">KHÔNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">плох- + -о</span>'
    '<span class="hd-gloss">tệ → trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Khen theo lối nói vòng: "không tệ". Trong tiếng Nga đây '
    'là lời KHEN thật, mạnh hơn "tạm được" chứ không phải chê nhẹ.</div>'
    '<div class="hd-warn">Đáp <b>— Как дела́? — Непло́хо.</b> là tích cực hơn '
    '<b>норма́льно</b> một bậc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пло́хо</b> tệ · <b>неплохо́й</b> khá tốt · '
    '<b>плохо́й</b> xấu</div>'
)
V["неплохо"] = "không tệ, khá tốt"

S["хорошо"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">хорош-</span>'
    '<span class="hd-gloss">TỐT (gốc trơn)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc trơn. Trọng âm trượt ra sau khi thành trạng từ: '
    '<b>хоро́ший</b> (giữa) → <b>хорошо́</b> (cuối).</div>'
    '<div class="hd-warn">So sánh hơn ĐỔI HẲN GỐC: <b>хорошо́ → лу́чше</b> tốt '
    'hơn (y như <i>good → better</i>).</div>'
    '<div class="hd-warn"><b>Хорошо́!</b> đứng một mình = "Được rồi, đồng ý".</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>хоро́ший</b> tốt, hay · <b>хороше́ть</b> đẹp ra · '
    '<b>хоро́шенький</b> xinh xắn</div>'
)
V["хорошо"] = "tốt, hay, giỏi, khỏe"

S["нормально"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">норм-</span>'
    '<span class="hd-gloss">CHUẨN, ĐỊNH MỨC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-альн- + -о</span>'
    '<span class="hd-gloss">đuôi tính từ → trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng <b>но́рма</b> "chuẩn" thì là bình thường. Đuôi '
    '<b>-альный</b> là biển báo từ quốc tế — đoán nghĩa qua <i>normal</i> '
    'được.</div>'
    '<div class="hd-warn">Đáp <b>— Как дела́? — Норма́льно.</b> là câu trả lời '
    'TÍCH CỰC ("ổn cả"), không phải chê nhạt nhẽo.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>но́рма</b> định mức · <b>норма́льный</b> bình thường '
    '· <b>ненорма́льный</b> bất thường</div>'
)
V["нормально"] = "bình thường, ổn"

# ------------------------------------------------------------- rõ / khó hiểu
S["ясно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ясн-</span>'
    '<span class="hd-gloss">RÕ, SÁNG TỎ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>ясн-</b> mở khoá một động từ rất hay gặp: '
    '<b>объясни́ть</b> = <b>об-</b> (bao quanh) + <b>ясн-</b> = "làm cho rõ" = '
    'giải thích.</div>'
    '<div class="hd-warn"><b>я́сно</b> nói bản thân sự việc RÕ; <b>поня́тно</b> '
    'nói người nghe HIỂU được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>я́сный</b> rõ ràng · <b>объясни́ть</b> giải thích · '
    '<b>объясне́ние</b> lời giải thích · <b>вы́яснить</b> làm sáng tỏ</div>'
)
V["ясно"] = "rõ, rõ ràng, rành rọt"

S["понятно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố thể hoàn thành, không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ня-</span>'
    '<span class="hd-gloss">NẮM, LẤY</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тн- + -о</span>'
    '<span class="hd-gloss">đuôi tính từ → trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>-ня-/-ним-</b> nghĩa là "lấy, nắm". '
    '<b>поня́ть</b> "hiểu" chính là "nắm được" ý — nên <b>поня́тно</b> là "nắm '
    'được, dễ hiểu".</div>'
    '<div class="hd-warn"><b>Поня́тно.</b> đứng một mình = "Tôi hiểu rồi" — là '
    'câu đáp, không phải lời khen.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поня́ть</b> hiểu · <b>поня́тие</b> khái niệm · '
    '<b>приня́ть</b> nhận · <b>заня́ть</b> chiếm, mượn</div>'
)
V["понятно"] = "dễ hiểu, rành mạch, hiểu rồi"

S["непонятно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не-</span>'
    '<span class="hd-gloss">KHÔNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">понятн- + -о</span>'
    '<span class="hd-gloss">dễ hiểu → trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỉ là <b>поня́тно</b> gắn thêm <b>не-</b>, và trọng âm '
    'không nhúc nhích: vẫn ở <b>-я-</b>.</div>'
    '<div class="hd-warn">Viết LIỀN vì <b>не-</b> tạo ra một từ mới có nghĩa '
    'riêng. Chỉ tách rời khi trong câu có <b>а</b> đối lập.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>непоня́тный</b> khó hiểu · <b>поня́тно</b> dễ hiểu · '
    '<b>поня́ть</b> hiểu · <b>непонима́ние</b> sự không hiểu nhau</div>'
)
V["непонятно"] = "khó hiểu, không hiểu được"

S["важно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">важ-</span>'
    '<span class="hd-gloss">SỨC NẶNG, TRỌNG LƯỢNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н- + -о</span>'
    '<span class="hd-gloss">đuôi tính từ → trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>важ-</b> vốn là "sức nặng" — cái gì nặng cân thì '
    'quan trọng. Cùng gốc: <b>уважа́ть</b> "tôn trọng" = coi người ta là có sức '
    'nặng.</div>'
    '<div class="hd-warn">Đừng lẫn với <b>ну́жно</b>: <b>ва́жно</b> nói về GIÁ '
    'TRỊ (đáng coi trọng), <b>ну́жно</b> nói về SỰ CẦN (phải làm).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ва́жный</b> quan trọng · <b>ва́жность</b> tầm quan '
    'trọng · <b>уважа́ть</b> tôn trọng · <b>уваже́ние</b> sự tôn trọng</div>'
)
V["важно"] = "quan trọng, hệ trọng"

# ------------------------------------------------------------- sáng / tối
S["светло"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">свет-</span>'
    '<span class="hd-gloss">ÁNH SÁNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-л- + -о</span>'
    '<span class="hd-gloss">đuôi tính từ → trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ danh từ <b>свет</b> ra tính từ <b>све́тлый</b> rồi ra '
    'trạng từ <b>светло́</b> — trọng âm trượt ra cuối. Hay dùng kiểu không có '
    'chủ ngữ: <b>на у́лице светло́</b> ngoài trời đang sáng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>свет</b> ánh sáng · <b>све́тлый</b> sáng, tươi sáng · '
    '<b>светофо́р</b> đèn giao thông · <b>освеще́ние</b> sự chiếu sáng</div>'
)
V["светло"] = "sáng sủa, trời sáng"

S["темно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">тем- (~ тьм-)</span>'
    '<span class="hd-gloss">BÓNG TỐI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н- + -о</span>'
    '<span class="hd-gloss">đuôi tính từ → trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một gốc ba mặt chữ: <b>тьма</b> → <b>темно́</b> → '
    '<b>тёмный</b>. Trọng âm rơi vào gốc thì <b>е</b> hoá thành <b>ё</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тьма</b> bóng tối · <b>тёмный</b> tối, sẫm màu · '
    '<b>темнота́</b> bóng tối · <b>потемне́ть</b> tối sầm lại</div>'
)
V["темно"] = "tối, tối tăm, trời tối"

# ------------------------------------------------------------- nhanh / chậm / khẽ
S["быстро"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">быстр-</span>'
    '<span class="hd-gloss">NHANH (gốc trơn)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ nhỏ được. Trọng âm nằm ở '
    '<b>бы-</b> với tính từ và trạng từ; danh từ <b>быстрота́</b> và dạng so sánh <b>быстре́е</b> mới kéo nó ra sau.</div>'
    '<div class="hd-warn"><b>бы́стро</b> nhanh về TỐC ĐỘ (chạy nhanh); '
    '<b>ско́ро</b> nhanh về THỜI ĐIỂM (sắp tới nơi).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бы́стрый</b> nhanh · <b>быстрота́</b> tốc độ · '
    '<b>быстре́е</b> nhanh hơn</div>'
)
V["быстро"] = "nhanh, nhanh chóng, mau"

S["медленно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">медл-</span>'
    '<span class="hd-gloss">CHẦN CHỪ, KÉO DÀI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-енн- + -о</span>'
    '<span class="hd-gloss">đuôi tính từ → trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đi ra từ động từ <b>ме́длить</b> "chần chừ": làm mà cứ '
    'chần chừ thì là làm chậm. Trọng âm đứng yên ở gốc <b>ме́дл-</b> suốt cả họ.</div>'
    '<div class="hd-warn">HAI chữ <b>н</b>: <b>ме́дленно</b> — vì tính từ gốc đã '
    'mang sẵn đuôi <b>-енн-</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ме́длить</b> chần chừ · <b>ме́дленный</b> chậm · '
    '<b>заме́длить</b> làm chậm lại</div>'
)
V["медленно"] = "chậm, chậm rãi, từ từ"

S["тихо"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">тих-</span>'
    '<span class="hd-gloss">YÊN, KHẼ (gốc trơn)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>тих-</b> đổi <b>х → ш</b> khi thêm hậu tố: '
    '<b>ти́хий</b> → <b>тишина́</b> "sự yên lặng". Đó là phép biến âm '
    '<b>г/к/х → ж/ч/ш</b> gặp khắp tiếng Nga.</div>'
    '<div class="hd-warn"><b>говори́ть ти́хо</b> là nói KHẼ, nhỏ tiếng (trái với '
    '<b>гро́мко</b>) — không phải nói chậm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ти́хий</b> yên tĩnh, khẽ · <b>тишина́</b> sự yên lặng '
    '· <b>тихо́нько</b> khe khẽ · <b>зати́хнуть</b> lặng đi</div>'
)
V["тихо"] = "khẽ, nhỏ tiếng, yên tĩnh, lặng lẽ"

# ------------------------------------------------------------------- nơi chốn
S["всюду"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вс-</span>'
    '<span class="hd-gloss">TOÀN BỘ (từ <b>весь</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-юду</span>'
    '<span class="hd-gloss">đuôi chỉ NƠI CHỐN</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vẫn cái <b>вс-</b> "toàn bộ" của <b>весь</b>, chỉ đổi '
    'đuôi để đổi chiều: <b>всегда́</b> mọi LÚC — <b>всю́ду</b> mọi NƠI — '
    '<b>все</b> mọi NGƯỜI.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>весь</b> toàn bộ · <b>всегда́</b> luôn luôn · '
    '<b>повсю́ду</b> khắp mọi nơi · <b>все</b> tất cả</div>'
)
V["всюду"] = "khắp nơi, mọi nơi"
