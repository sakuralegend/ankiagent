# -*- coding: utf-8 -*-
"""k97 — actions: 22 từ mới (đợt A1-A2 TRKI), mười cặp thể + hai danh từ soạn như một họ.

Không khối hệ thống. Chỗ cần nhất quán:
(1) mười cặp thể chung lô — mỗi vế nói phần của nó, không chép nhau; по- của vế HT
    chỉ đánh dấu XONG (như помеша́ть k96), trừ khi nói rõ;
(2) họ побе́да / победи́ть / побежда́ть: gốc -бед-, д→жд ở vế CHT (như роди́ться → рожда́ться);
    nối với беда́ chỉ ở mức từ nguyên, hạ mức tin ở thẻ побе́да;
(3) họ сове́т / сове́товать / посове́товать: gốc -вет- «LỜI NÓI» khớp отве́т (k05), приве́т (k57);
(4) про- + -дав- khớp продаве́ц (k36); благо- + -дар- khớp дари́ть (k76);
    сесть / сади́ться khớp сиде́ть (k85): ngồi XUỐNG vs ĐANG ngồi; -яв- khớp объявле́ние (k52).
Bẫy họ hàng đã gạt: яви́ться (k98 tự lo, không nêu); сад (vườn) cùng gốc xa với сади́ться — không nêu.
"""

S = {}

# -------------------------------------------------------- благодарить
S["благодарить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">благо-</span>'
    '<span class="hd-gloss">ĐIỀU TỐT LÀNH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дар-</span>'
    '<span class="hd-gloss">MÓN QUÀ, trao tặng — gốc của <b>дари́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Trao lại điều tốt lành» ⇒ cảm ơn. Trọng âm đứng yên ở đuôi: '
    '<b>благодарю́, благодари́шь</b>. Cặp thể: <b>поблагодари́ть</b>.</div>'
    '<div class="hd-warn">Người được cảm ơn ở cách 4, lý do là <b>за</b> + cách 4: '
    '<b>благодари́ть дру́га за по́мощь</b>. <b>Благодарю́ вас!</b> = Xin cảm ơn anh/chị!</div>'
    '<div class="hd-warn"><b>благодаря́</b> + cách 3 = NHỜ CÓ: <b>благодаря́ вам</b> nhờ có anh.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поблагодари́ть</b> cảm ơn (HT) · <b>благода́рность</b> lòng biết ơn · '
    '<b>благода́рный</b> biết ơn · <b>пода́рок</b> món quà</div>'
)

# -------------------------------------------------------- поблагодарить
S["поблагодарить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">đánh dấu XONG, không thêm nghĩa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-благодари́ть</span>'
    '<span class="hd-gloss">chính là <b>благодари́ть</b> — «trao lại điều tốt lành»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một lời cảm ơn trọn vẹn, cụ thể: <b>Я хочу́ поблагодари́ть вас за '
    'по́мощь.</b> Tôi muốn cảm ơn anh vì đã giúp. Chia như vế CHT: <b>поблагодарю́, '
    'поблагодари́шь</b> — nghĩa tương lai. Người được cảm ơn vẫn ở cách 4.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>благодари́ть</b> cảm ơn (CHT) · <b>благода́рность</b> lòng biết ơn · '
    '<b>благодаря́</b> nhờ có</div>'
)

# -------------------------------------------------------- победа
S["победа"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố mang sẵn từ <b>победи́ть</b>, nghĩa riêng đã mờ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бед-</span>'
    '<span class="hd-gloss">gốc cổ ÉP, KHUẤT PHỤC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ rút thẳng từ động từ <b>победи́ть</b> (bỏ <b>-ить</b>, '
    'thêm <b>-а</b>): việc khuất phục được đối thủ ⇒ chiến thắng. '
    '<b>День Побе́ды</b> = Ngày Chiến thắng, 9 tháng 5.</div>'
    '<div class="hd-warn">⚠️ Mức tin: <b>-бед-</b> cùng gốc với <b>беда́</b> tai hoạ là '
    'chuyện TỪ NGUYÊN (từ cổ «ép buộc»), không phải luật suy ra được — chỉ dùng để nhớ.</div>'
    '<div class="hd-warn">Giành chiến thắng = <b>одержа́ть побе́ду</b>; thắng AI thì '
    '<b>над</b> + cách 5.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>победи́ть</b> chiến thắng (HT) · <b>побежда́ть</b> chiến thắng (CHT) · '
    '<b>победи́тель</b> người chiến thắng</div>'
)

# -------------------------------------------------------- победить
S["победить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">nghĩa riêng đã mờ, nhớ cả khối <b>побед-</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-бед-</span>'
    '<span class="hd-gloss">gốc cổ ÉP, KHUẤT PHỤC — như <b>побе́да</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Động từ mẹ của <b>побе́да</b>. Đánh bại AI ở cách 4 '
    '(<b>победи́ть врага́</b>); thắng TRONG cuộc gì là <b>в</b> + cách 6 '
    '(<b>победи́ть в ма́тче</b>). <b>Мы победи́м!</b> = Chúng ta sẽ thắng! '
    'Cặp thể: <b>побежда́ть</b>.</div>'
    '<div class="hd-warn">KHÔNG có dạng «tôi»: không nói «победю́» hay «побежу́». '
    'Muốn nói «tôi sẽ thắng» ⇒ <b>Я одержу́ побе́ду</b> hoặc <b>Я смогу́ победи́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>побе́да</b> chiến thắng · <b>побежда́ть</b> chiến thắng (CHT) · '
    '<b>победи́тель</b> người chiến thắng</div>'
)

# -------------------------------------------------------- побеждать
S["побеждать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">nghĩa riêng đã mờ, như ở <b>победи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-бежд-</span>'
    '<span class="hd-gloss">chính là <b>-бед-</b>, biến âm <b>д → жд</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi lớp 1, chia đều: <b>побежда́ю, побежда́ешь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vế CHT của <b>победи́ть</b>; <b>д</b> hoá <b>жд</b> theo cùng khuôn '
    '<b>роди́ться → рожда́ться</b>. Dùng cho thắng nhiều lần, hay thắng: <b>На́ша кома́нда '
    'всегда́ побежда́ет.</b> Đội ta luôn thắng. Vế này có đủ ngôi «tôi»: <b>побежда́ю</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>победи́ть</b> chiến thắng (HT) · <b>побе́да</b> chiến thắng · '
    '<b>победи́тель</b> người chiến thắng</div>'
)

# -------------------------------------------------------- совет
S["совет"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">CÙNG nhau</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вет</span>'
    '<span class="hd-gloss">gốc cổ LỜI NÓI — như trong <b>отве́т</b>, <b>приве́т</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Lời bàn cùng nhau» ⇒ lời khuyên; và cả nơi người ta ngồi lại bàn '
    '⇒ HỘI ĐỒNG. Chữ «Xô viết» trong Liên Xô (<b>Сове́тский Сою́з</b>) chính là phiên âm từ này.</div>'
    '<div class="hd-warn">Cho lời khuyên = <b>дать сове́т</b>, không dùng «сказа́ть»: '
    '<b>Дай мне сове́т.</b> Cho tôi lời khuyên đi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сове́товать</b> khuyên · <b>сове́тский</b> thuộc Xô viết · '
    '<b>отве́т</b> câu trả lời · <b>приве́т</b> lời chào</div>'
)

# -------------------------------------------------------- советовать
S["советовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сове́т-</span>'
    '<span class="hd-gloss">LỜI KHUYÊN — chính là <b>сове́т</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-ть</span>'
    '<span class="hd-gloss">đuôi biến danh từ thành động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đưa ra <b>сове́т</b>» ⇒ khuyên. Như mọi động từ <b>-овать</b>, '
    'ở hiện tại <b>-ова-</b> đổi thành <b>-у-</b>: <b>сове́тую, сове́туешь</b>. '
    'Cặp thể: <b>посове́товать</b>.</div>'
    '<div class="hd-warn">Khuyên AI ⇒ cách 3, không phải cách 4 như tiếng Anh <i>advise him</i>: '
    '<b>Я сове́тую тебе́ отдохну́ть.</b> Tôi khuyên bạn nghỉ ngơi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сове́т</b> lời khuyên · <b>посове́товать</b> khuyên (HT) · '
    '<b>сове́товаться</b> hỏi ý kiến</div>'
)

# -------------------------------------------------------- посоветовать
S["посоветовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">đánh dấu XONG, không thêm nghĩa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сове́товать</span>'
    '<span class="hd-gloss">chính là <b>сове́товать</b> — khuyên</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một lời khuyên cụ thể, một lần: <b>посове́тую, посове́туешь</b> '
    '(nghĩa tương lai). Người được khuyên vẫn ở cách 3: <b>Посове́туй мне хоро́шую кни́гу.</b> '
    'Gợi ý cho tôi một cuốn sách hay.</div>'
    '<div class="hd-warn"><b>Что вы посове́туете?</b> = Anh/chị gợi ý món nào? — câu hỏi '
    'quen ở nhà hàng, cửa hàng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сове́товать</b> khuyên (CHT) · <b>сове́т</b> lời khuyên · '
    '<b>сове́товаться</b> hỏi ý kiến</div>'
)

# -------------------------------------------------------- поступать
S["поступать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố, ở đây nghĩa riêng đã mờ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ступ-</span>'
    '<span class="hd-gloss">BƯỚC CHÂN — gốc của <b>ступе́нька</b> bậc thang</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi lớp 1, chia đều: <b>поступа́ю, поступа́ешь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hai hình ảnh của «bước»: <b>bước một bước</b> ⇒ hành động, cư xử; '
    '<b>bước vào</b> ⇒ vào trường. Vế CHT nói việc đang diễn ra: <b>Он поступа́ет в '
    'университе́т</b> = cậu ấy đang thi vào đại học, chưa biết đậu chưa.</div>'
    '<div class="hd-warn">Vào trường: <b>в</b> + cách 4. Cư xử với AI: <b>с</b> + cách 5. '
    '<b>Так не поступа́ют!</b> = Không ai cư xử như thế!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поступи́ть</b> vào học, hành động (HT) · <b>посту́пок</b> việc làm, '
    'hành vi · <b>ступе́нька</b> bậc thang</div>'
)

# -------------------------------------------------------- поступить
S["поступить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố, ở đây nghĩa riêng đã mờ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ступ-</span>'
    '<span class="hd-gloss">BƯỚC CHÂN — như <b>поступа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đã bước vào ⇒ ĐẬU vào: <b>Я поступи́л в университе́т.</b> Tôi đã '
    'vào được đại học. Nghĩa cư xử: <b>Ты пра́вильно поступи́л.</b> Cậu làm thế là đúng.</div>'
    '<div class="hd-warn">Ngôi «tôi» chèn <b>л</b> sau <b>п</b> và giữ trọng âm ở đuôi: '
    '<b>поступлю́</b>; từ ngôi hai trọng âm lùi về gốc: <b>посту́пишь, посту́пят</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поступа́ть</b> thi vào, cư xử (CHT) · <b>посту́пок</b> việc làm, '
    'hành vi · <b>поступле́ние</b> sự nhập học</div>'
)

# -------------------------------------------------------- тратить
S["тратить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">тра́т-</span>'
    '<span class="hd-gloss">gốc trơn TIÊU HAO — không chẻ nhỏ hơn được</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi lớp chia 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ngôi «tôi» <b>т → ч</b>: <b>тра́чу</b>, còn lại giữ <b>т</b>: '
    '<b>тра́тишь</b>; trọng âm đứng yên ở gốc. Tiêu tiền lẫn tiêu thời gian đều dùng nó: '
    '<b>тра́тить вре́мя</b>. Cặp thể: <b>потра́тить</b>.</div>'
    '<div class="hd-warn">Tiêu CÁI GÌ ở cách 4, tiêu VÀO việc gì là <b>на</b> + cách 4: '
    '<b>тра́тить де́ньги на кни́ги</b> tiêu tiền vào sách.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>потра́тить</b> tiêu (HT) · <b>тра́та</b> khoản tiêu, sự phí · '
    '<b>истра́тить</b> tiêu sạch</div>'
)

# -------------------------------------------------------- потратить
S["потратить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">đánh dấu XONG, không thêm nghĩa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тра́тить</span>'
    '<span class="hd-gloss">chính là <b>тра́тить</b> — tiêu hao</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiêu xong một khoản cụ thể: <b>Я потра́тил всю зарпла́ту.</b> '
    'Tôi đã tiêu hết lương. Chia như vế CHT: <b>потра́чу, потра́тишь</b> — nghĩa tương lai. '
    'Tiêu vào việc gì vẫn là <b>на</b> + cách 4.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тра́тить</b> tiêu (CHT) · <b>тра́та</b> khoản tiêu, sự phí</div>'
)

# -------------------------------------------------------- шутить
S["шутить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">шут-</span>'
    '<span class="hd-gloss">THẰNG HỀ, anh pha trò (<b>шут</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm trò như anh hề ⇒ nói đùa. Ngôi «tôi» <b>т → ч</b> và trọng âm ở '
    'đuôi: <b>шучу́</b>; từ ngôi hai lùi về gốc: <b>шу́тишь, шу́тят</b>. Trêu AI: '
    '<b>над</b> + cách 5. Cặp thể: <b>пошути́ть</b>.</div>'
    '<div class="hd-warn"><b>Ты шу́тишь?</b> = Đùa à? (thật không đấy?) — câu bật ra hằng '
    'ngày.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>шу́тка</b> câu đùa · <b>пошути́ть</b> đùa (HT) · <b>шут</b> thằng hề · '
    '<b>шутли́вый</b> hay bỡn cợt</div>'
)

# -------------------------------------------------------- пошутить
S["пошутить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">XONG, một lần — một câu đùa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-шути́ть</span>'
    '<span class="hd-gloss">chính là <b>шути́ть</b> — nói đùa</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chia y như vế CHT, chỉ đổi sang nghĩa tương lai: <b>пошучу́, '
    'пошу́тишь</b>.</div>'
    '<div class="hd-warn"><b>Я пошути́л!</b> = Tôi đùa thôi mà! — câu chữa cháy khi người '
    'nghe tưởng thật.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>шути́ть</b> đùa (CHT) · <b>шу́тка</b> câu đùa · <b>шут</b> thằng hề</div>'
)

# -------------------------------------------------------- появиться
S["появиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">đánh dấu XONG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-яв-</span>'
    '<span class="hd-gloss">HIỆN RÕ — gốc của <b>я́вный</b> rõ ràng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть-ся</span>'
    '<span class="hd-gloss">đuôi lớp 2 + <b>-ся</b> «tự mình»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Tự hiện rõ ra» ⇒ xuất hiện. Ngôi «tôi» chèn <b>л</b> sau <b>в</b>: '
    '<b>появлю́сь</b>; từ ngôi hai trọng âm lùi về gốc: <b>поя́вишься</b>. '
    'Cặp thể: <b>появля́ться</b>.</div>'
    '<div class="hd-warn"><b>у</b> + cách 2 + <b>появи́ться</b> = mới CÓ thêm: '
    '<b>У меня́ появи́лась иде́я.</b> Tôi vừa nảy ra một ý.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>появля́ться</b> xuất hiện (CHT) · <b>появле́ние</b> sự xuất hiện · '
    '<b>явле́ние</b> hiện tượng · <b>объявле́ние</b> thông báo</div>'
)

# -------------------------------------------------------- появляться
S["появляться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố mang sẵn từ vế HT</span></div>'
    '<div class="hd-row"><span class="hd-piece">-явл-</span>'
    '<span class="hd-gloss"><b>-яв-</b> HIỆN RÕ, mang sẵn <b>л</b> chèn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́ть-ся</span>'
    '<span class="hd-gloss">đuôi lớp 1 + <b>-ся</b>, chia đều: <b>появля́юсь, '
    'появля́ешься</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vế CHT của <b>появи́ться</b>: chữ <b>л</b> mà vế HT chỉ chèn ở ngôi '
    '«tôi» thì ở đây nằm cố định trong thân, như <b>объявле́ние</b>. Dùng cho chuyện lặp lại '
    'hay đang dần lộ ra: <b>Он ре́дко появля́ется до́ма.</b> Anh ấy hiếm khi ló mặt ở nhà.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>появи́ться</b> xuất hiện (HT) · <b>появле́ние</b> sự xuất hiện · '
    '<b>явле́ние</b> hiện tượng</div>'
)

# -------------------------------------------------------- продавать
S["продавать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">chuyển hẳn sang tay người khác</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дава́ть</span>'
    '<span class="hd-gloss">TRAO, đưa cho — chính là <b>дава́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trao hẳn hàng qua tay người khác ⇒ bán (khớp <b>продаве́ц</b> người bán). '
    'Cặp thể: <b>прода́ть</b>.</div>'
    '<div class="hd-warn">Chia y như <b>дава́ть</b>: <b>-ва-</b> RỤNG ở hiện tại — '
    '<b>продаю́, продаёшь, продаю́т</b>, không phải «продаваю». Mệnh lệnh lại giữ: '
    '<b>продава́й</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>прода́ть</b> bán (HT) · <b>продаве́ц</b> người bán · <b>прода́жа</b> '
    'việc bán · <b>дава́ть</b> cho, đưa</div>'
)

# -------------------------------------------------------- продать
S["продать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">chuyển hẳn sang tay người khác</span></div>'
    '<div class="hd-row"><span class="hd-piece">-да́ть</span>'
    '<span class="hd-gloss">CHO, đưa — chính là <b>дать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vế HT của <b>продава́ть</b>: đã trao hẳn ⇒ bán xong. '
    '<b>дать</b> là một trong vài động từ chia lạ nhất tiếng Nga, và <b>прода́ть</b> chia '
    'y hệt nó — thuộc một lần dùng được cho cả hai.</div>'
    '<div class="hd-warn">Tương lai: <b>прода́м, прода́шь, прода́ст, продади́м, продади́те, '
    'продаду́т</b>. Quá khứ trọng âm nhảy: <b>про́дал</b> nhưng <b>продала́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>продава́ть</b> bán (CHT) · <b>прода́жа</b> việc bán · '
    '<b>продаве́ц</b> người bán · <b>дать</b> cho, đưa</div>'
)

# -------------------------------------------------------- расти
S["расти"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рас-/рос-</span>'
    '<span class="hd-gloss">gốc LỚN LÊN, MỌC — hai mặt chữ của cùng một gốc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ти́</span>'
    '<span class="hd-gloss">đuôi nguyên thể <b>-ти</b>, như <b>идти́</b>, <b>нести́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hiện tại giữ <b>т</b>: <b>расту́, растёшь</b>. Quá khứ đổi '
    '<b>а → о</b>, rụng <b>т</b>, giống đực không có <b>-л</b>: <b>рос, росла́, росли́</b>. '
    'Mặt chữ <b>рос-</b> ấy là chìa khoá nhận họ hàng. Cặp thể: <b>вы́расти</b>.</div>'
    '<div class="hd-warn">Không có tân ngữ — cây TỰ mọc, giá TỰ tăng: <b>Це́ны расту́т.</b> '
    'Trồng, nuôi lớn CÁI GÌ là từ khác: <b>выра́щивать</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вы́расти</b> lớn lên (HT) · <b>рост</b> chiều cao, sự tăng · '
    '<b>расте́ние</b> cây cối · <b>взро́слый</b> người lớn</div>'
)

# -------------------------------------------------------- вырасти
S["вырасти"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы́-</span>'
    '<span class="hd-gloss">RA, tới hết mức</span></div>'
    '<div class="hd-row"><span class="hd-piece">-расти</span>'
    '<span class="hd-gloss">chính là <b>расти́</b> — lớn lên</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Lớn ra hết cỡ» ⇒ lớn lên xong, trưởng thành. Động từ HT có '
    '<b>вы-</b> thì trọng âm LUÔN nằm ở <b>вы́</b>, mọi dạng: <b>вы́расту, вы́растешь</b>; '
    'quá khứ theo <b>расти́</b>: <b>вы́рос, вы́росла</b>.</div>'
    '<div class="hd-warn"><b>Где ты вы́рос?</b> = Bạn lớn lên ở đâu? — câu hỏi làm quen '
    'rất hay gặp.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>расти́</b> lớn lên (CHT) · <b>выра́щивать</b> trồng, nuôi lớn · '
    '<b>взро́слый</b> người lớn · <b>рост</b> chiều cao</div>'
)

# -------------------------------------------------------- сесть
S["сесть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сес-</span>'
    '<span class="hd-gloss">gốc NGỒI <b>сед-</b> (biến thể của <b>сид-</b> trong <b>сиде́ть</b>), '
    '<b>д</b> hoá <b>с</b> trước <b>-ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Động tác NGỒI XUỐNG, xong một lần (vế CHT: <b>сади́ться</b>). '
    'Thân tương lai phải thuộc riêng: <b>ся́ду, ся́дешь</b>; quá khứ: <b>сел, се́ла</b>. '
    'Máy bay <b>сел</b> = đã hạ cánh.</div>'
    '<div class="hd-warn">Ngồi VÀO đâu ⇒ cách 4: <b>сесть на стул</b>, <b>сесть в авто́бус</b> '
    '(lên xe buýt). Còn ĐANG ngồi ở đâu ⇒ <b>сиде́ть на сту́ле</b>, cách 6.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сади́ться</b> ngồi xuống (CHT) · <b>сиде́ть</b> đang ngồi · '
    '<b>сосе́д</b> hàng xóm</div>'
)

# -------------------------------------------------------- садиться
S["садиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сад-</span>'
    '<span class="hd-gloss">gốc NGỒI — thêm một biến thể của <b>сид-</b>/<b>сед-</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть-ся</span>'
    '<span class="hd-gloss">đuôi lớp 2 + <b>-ся</b> «tự đặt mình»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Tự đặt mình ngồi» ⇒ ngồi xuống; vế CHT của <b>сесть</b>. Ngôi «tôi» '
    '<b>д → ж</b>: <b>сажу́сь</b>, còn lại giữ <b>д</b>: <b>сади́шься</b>. Ngồi vào đâu vẫn là '
    'cách 4. Mặt trời «ngồi xuống» ⇒ lặn: <b>Со́лнце сади́тся.</b></div>'
    '<div class="hd-warn"><b>Сади́тесь, пожа́луйста!</b> = Mời anh/chị ngồi! — lời mời lịch '
    'sự dùng vế CHT này.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сесть</b> ngồi xuống (HT) · <b>сиде́ть</b> đang ngồi · '
    '<b>сажа́ть</b> đặt ngồi, trồng cây</div>'
)


# ------------------------------------------------------------------ VIỆT
V = {
    # Tiếng Anh xếp "council / board" ngay sau advice — đề bài thiếu hẳn nghĩa này.
    "совет": "lời khuyên, sự góp ý, hội đồng",
    # Bỏ ngoặc "(trường)" — cấm ghi chú trong ngoặc; "đậu vào" là của vế HT,
    # vế CHT là đang thi vào.
    "поступать": "hành động, nhập học, thi vào",
    # Bỏ ngoặc "(tiền bạc, thời gian)".
    "тратить": "tiêu, tiêu tốn, lãng phí",
    # Rút 'có mặt' — nghĩa đó thuộc быть (k03). Thêm 'hiện ra, ló ra' từ gloss
    # "come into view / become visible".
    "появляться": "xuất hiện, hiện ra, ló ra",
    # Bỏ ngoặc "(mặt trời)".
    "садиться": "ngồi xuống, lên xe, lặn",
    # Thiếu nghĩa "to land / touch down" mà tiếng Anh có.
    "сесть": "ngồi xuống, lên xe, hạ cánh",
}
