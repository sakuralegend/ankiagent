# -*- coding: utf-8 -*-
"""k166 — language::communication: lời nói, kênh truyền tin, và vài từ «thời điểm / lượt / tổng».

Chỗ cần nhất quán trong lô:
(1) gốc яв- = HIỆN RA, LỘ RÕ — заяви́ть · заявля́ть, khớp явля́ться, появи́ться, объяви́ть,
    заявле́ние (đã có thẻ). Biến âm в→вл (заявлю́) nói ở заяви́ть, thẻ IMPF không lặp.
(2) gốc вин- = LỖI — извини́ться · извиня́ться, khớp вина́, винова́тый, извини́ть.
    Cách đòi (пе́ред + C5, за + C4) nói ở thẻ PERF; thẻ IMPF nói chuyện «Я извиня́юсь».
(3) gốc прав- = THẲNG, ĐÚNG — непра́вда, khớp пра́вда, пра́вильный, пра́вый «đúng».
(4) -либо / -нибудь / -то — chỉ nói ở когда́-либо, bằng một câu về chính từ đó.
(5) đuôi -шн-ий biến trạng từ thời gian thành tính từ — ны́нешний, khớp сего́дняшний.
Họ hàng cố ý vắng: код (mượn đứng một mình; phái sinh коди́ровать… quá xa người mới, không chắc
trọng âm), интервью́ (mượn tiếng Anh nguyên khối, không phái sinh thông dụng).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "итог": "tổng kết, kết cục, tổng số",        # bỏ «kết quả» — nằm gọn trong результа́т; gloss: outcome/summary/total
    "сумма": "tổng, tổng số, số tiền",            # «;» → «,»
    "канал": "kênh, kênh đào, ống dẫn",           # «;» → «,»; duct từ gloss; bỏ «con kênh» trùng ý «kênh đào»
    "заявить": "tuyên bố, khẳng định, đòi quyền",  # bỏ nhãn thể; KHÔNG thêm «thông báo» — sẽ nuốt gọn объяви́ть
    "заявлять": "tuyên bố, khẳng định, trình báo, đòi quyền",   # bỏ nhãn thể; report to police từ gloss
    "извиниться": "xin lỗi",                      # bỏ nhãn thể — badge PERF/IMPF đã tách
    "извиняться": "xin lỗi",
    "нынешний": "hiện nay, hiện tại, ngày nay",   # bỏ «bây giờ» (trạng từ = тепе́рь); present-day
    "когда-либо": "bao giờ, từng",                # «;» → «,»
    "очередной": "tiếp theo, kế tiếp, thêm một, định kỳ",   # bỏ «lại một... nữa»; next in turn / yet another / scheduled
    "трубка": "ống nghe điện thoại, ống nhỏ, tẩu thuốc",    # tube / tobacco pipe từ gloss
}

# ----------------------------------------------------------------- неправда
S["неправда"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не-</span>'
    '<span class="hd-gloss">KHÔNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-правд-а</span>'
    '<span class="hd-gloss">sự thật (<b>пра́вда</b>), gốc прав- «thẳng, đúng»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Không phải sự thật». Câu hay gặp nhất là cãi lại người khác: '
    '<b>Э́то непра́вда!</b> «Không đúng!». Nhẹ hơn <b>ложь</b> lời nói dối — nói непра́вда '
    'là bảo điều đó sai, chưa hẳn buộc tội người ta cố ý lừa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пра́вда</b> sự thật · <b>пра́вильный</b> đúng · '
    '<b>пра́вый</b> đúng, bên phải · <b>пра́вило</b> quy tắc</div>'
)

# ----------------------------------------------------------------- трубка
S["трубка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">труб-</span>'
    '<span class="hd-gloss">ỐNG (<b>труба́</b> ống, ống khói, kèn)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-а</span>'
    '<span class="hd-gloss">đuôi «nhỏ» ⇒ cái ống nhỏ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ống nhỏ cầm tay ⇒ ống nghe điện thoại, tẩu thuốc. Trọng âm lùi về đầu: '
    '<b>труба́</b> → <b>тру́бка</b>. Cách 2 số nhiều chêm о: <b>тру́бок</b>.</div>'
    '<div class="hd-warn">Nghe điện thoại nói bằng chính từ này: <b>взять тру́бку</b> nhấc máy · '
    '<b>положи́ть тру́бку</b> gác máy.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>труба́</b> ống, kèn · <b>тру́бочка</b> ống hút</div>'
)

# ----------------------------------------------------------------- реклама
S["реклама"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn tiếng Pháp <i>réclame</i>, gốc Latin '
    '<i>reclamare</i> «kêu to lên» — họ với tiếng Anh <i>clamour</i>, <i>exclaim</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Quảng cáo = rao to cho mọi người nghe. Là danh từ giống cái, chỉ cả ngành '
    'lẫn một mẩu quảng cáo: <b>рекла́ма по телеви́зору</b> quảng cáo trên TV.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рекла́мный</b> thuộc quảng cáo · '
    '<b>реклами́ровать</b> quảng cáo (động từ)</div>'
)

# ----------------------------------------------------------------- код
S["код"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn qua tiếng Pháp từ Latin <i>codex</i> — cùng gốc '
    'tiếng Anh <i>code</i>, nghĩa cũng khớp.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giống đực, biến cách đều: <b>ко́да</b>, <b>ко́ды</b>. '
    'Dùng như tiếng Anh: <b>код го́рода</b> mã vùng điện thoại, '
    '<b>исхо́дный код</b> mã nguồn.</div>'
)

# ----------------------------------------------------------------- крик
S["крик"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">крик</span>'
    '<span class="hd-gloss">TIẾNG HÉT — gốc trơn, không có đuôi</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc của cả cặp động từ: <b>кри́кнуть</b> hét lên một tiếng (-ну- = một lần), '
    '<b>крича́ть</b> la hét — ở đây к đổi thành ч trước -а-ть, phép đổi gặp khắp nơi '
    '(<b>рука́</b> → <b>ру́чка</b>).</div>'
    '<div class="hd-warn">Cụm cố định: <b>после́дний крик мо́ды</b> «tiếng hét cuối cùng của thời '
    'trang» = mốt mới nhất.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>крича́ть</b> la hét · <b>кри́кнуть</b> hét lên</div>'
)

# ----------------------------------------------------------------- канал
S["канал"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn Latin <i>canalis</i> «ống, rãnh». Tiếng Anh tách nó '
    'thành hai chữ <i>canal</i> và <i>channel</i> — tiếng Nga giữ một chữ cho cả hai.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc là đường dẫn nước ⇒ kênh đào (<b>Пана́мский кана́л</b>) ⇒ '
    'đường dẫn tín hiệu ⇒ kênh truyền hình: <b>смотре́ть по пе́рвому кана́лу</b> xem trên '
    'kênh một (по + cách 3).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>канализа́ция</b> hệ thống cống thoát nước</div>'
)

# ----------------------------------------------------------------- заявить
S["заявить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng dễ suy</span></div>'
    '<div class="hd-row"><span class="hd-piece">-яв-</span>'
    '<span class="hd-gloss">HIỆN RA, LỘ RÕ (như <b>появи́ться</b> xuất hiện)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-ть</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm cho ý mình lộ rõ trước mọi người ⇒ tuyên bố, khẳng định công khai: '
    '<b>заяви́ть о своём реше́нии</b> tuyên bố quyết định (о + cách 6), hoặc '
    '<b>заяви́ть, что…</b>. Cùng gốc với <b>объяви́ть</b> thông báo.</div>'
    '<div class="hd-why">Ngôi «tôi» chêm л: <b>заявлю́</b>, rồi trọng âm lùi: <b>зая́вишь</b>, '
    '<b>зая́вит</b> — như <b>люби́ть</b> → <b>люблю́</b>, <b>лю́бишь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>заявле́ние</b> lời tuyên bố, lá đơn · <b>объяви́ть</b> thông báo · '
    '<b>появи́ться</b> xuất hiện · <b>я́вный</b> rõ ràng</div>'
)

# ----------------------------------------------------------------- заявлять
S["заявлять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-яв-</span>'
    '<span class="hd-gloss">«làm cho lộ rõ» — như <b>заяви́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-л-я-ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành, mang sẵn л của <b>заявлю́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp thể của <b>заяви́ть</b>, chia đều theo -аю/-яю: <b>заявля́ю</b>, '
    '<b>заявля́ешь</b>. Cùng khuôn với <b>объявля́ть</b> và <b>появля́ться</b> — biết một cặp '
    'là đoán được hai cặp kia.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>заявле́ние</b> lời tuyên bố, lá đơn · <b>объявля́ть</b> thông báo · '
    '<b>явля́ться</b> là, trình diện</div>'
)

# ----------------------------------------------------------------- интервью
S["интервью"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn nguyên tiếng Anh <i>interview</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không biến cách — mọi cách đều viết <b>интервью́</b>; đuôi lạ nên xếp giống '
    'trung. Nhấn âm cuối.</div>'
    '<div class="hd-warn">Hai chiều khác động từ: <b>дать интервью́</b> trả lời phỏng vấn (người '
    'được hỏi) · <b>взять интервью́ у</b> + cách 2 phỏng vấn ai (nhà báo).</div>'
)

# ----------------------------------------------------------------- извиниться
S["извиниться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">из-</span>'
    '<span class="hd-gloss">RA KHỎI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вин-</span>'
    '<span class="hd-gloss">LỖI (<b>вина́</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-ть-ся</span>'
    '<span class="hd-gloss">đuôi động từ + «tự mình»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>извини́ть</b> = gỡ lỗi ra khỏi người khác ⇒ tha lỗi; thêm -ся ⇒ tự '
    'mình đi xin được gỡ lỗi ⇒ xin lỗi. Câu «Xin lỗi!» nói thẳng thì dùng mệnh lệnh của từ kia: '
    '<b>Извини́те!</b></div>'
    '<div class="hd-warn">Đòi hai cách: <b>извини́ться пе́ред</b> + cách 5 (với ai) · '
    '<b>за</b> + cách 4 (vì gì): <b>извини́ться пе́ред дру́гом за опозда́ние</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вина́</b> lỗi · <b>винова́тый</b> có lỗi · <b>извини́ть</b> tha lỗi · '
    '<b>извине́ние</b> lời xin lỗi</div>'
)

# ----------------------------------------------------------------- извиняться
S["извиняться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">из-вин-</span>'
    '<span class="hd-gloss">«gỡ lỗi ra» — như <b>извини́ться</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я-ть-ся</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành + «tự mình»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp thể của <b>извини́ться</b>, cùng cách đòi (пе́ред + cách 5, за + cách 4). '
    'Chia đều: <b>извиня́юсь</b>, <b>извиня́ешься</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: sắc thái dùng, không phải luật. <b>Я извиня́юсь</b> nghe '
    'khắp nơi, nhưng nhiều người coi là kém lịch sự hơn <b>Извини́те</b> — muốn chắc thì nói '
    'Извини́те.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>извиня́ть</b> tha lỗi · <b>вина́</b> lỗi · <b>извине́ние</b> lời xin lỗi</div>'
)

# ----------------------------------------------------------------- нынешний
S["нынешний"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ныне-</span>'
    '<span class="hd-gloss">BÂY GIỜ (<b>ны́не</b>, văn viết)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-шн-ий</span>'
    '<span class="hd-gloss">đuôi biến trạng từ thời gian thành tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng khuôn <b>сего́дня</b> → <b>сего́дняшний</b>: «thuộc về bây giờ» ⇒ '
    'hiện nay: <b>ны́нешнее вре́мя</b> thời nay. Đuôi -ний là tính từ MỀM: '
    '<b>ны́нешняя</b>, <b>ны́нешнего</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ны́не</b> nay (văn viết) · <b>ны́нче</b> dạo này (khẩu ngữ) · '
    '<b>сего́дняшний</b> của hôm nay</div>'
)

# ----------------------------------------------------------------- внезапный
S["внезапный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ chắc được: thân <b>внеза́п-</b> là gốc cổ, nghĩa từng mảnh đã mờ. '
    'Chỉ cần nhận đuôi -н-ый của tính từ.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trạng từ <b>внеза́пно</b> đột nhiên — nghĩa như <b>вдруг</b>, nhưng trang '
    'trọng hơn. Dạng ngắn giống đực chêm е: <b>внеза́пен</b> (các dạng khác đều: '
    '<b>внеза́пна</b>, <b>внеза́пны</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>внеза́пно</b> đột nhiên · <b>внеза́пность</b> sự bất ngờ</div>'
)

# ----------------------------------------------------------------- когда-либо
S["когда-либо"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">когда́</span>'
    '<span class="hd-gloss">KHI NÀO</span></div>'
    '<div class="hd-row"><span class="hd-piece">-либо</span>'
    '<span class="hd-gloss">«bất kỳ» (từ <b>ли́бо</b> hoặc là)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Khi nào cũng được» ⇒ <i>ever</i>, trong câu hỏi và so sánh: '
    '<b>лу́чше, чем когда́-либо</b> tốt hơn bao giờ hết. Nghĩa gần <b>когда́-нибудь</b> nhưng '
    'văn viết hơn; còn <b>когда́-то</b> là một lúc ĐÃ có thật (hồi xưa).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>когда́</b> khi nào · <b>ли́бо</b> hoặc là · <b>кто́-либо</b> bất kỳ ai · '
    '<b>что́-либо</b> bất cứ điều gì</div>'
)

# ----------------------------------------------------------------- сумма
S["сумма"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn Latin <i>summa</i> — cùng gốc tiếng Anh <i>sum</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tổng của phép cộng, và hay gặp nhất là tổng tiền: '
    '<b>на су́мму сто рубле́й</b> trị giá một trăm rúp. Đuôi -а nên giống cái.</div>'
    '<div class="hd-warn">Cụm cố định: <b>кру́гленькая су́мма</b> «khoản tròn trĩnh» = một món '
    'tiền kha khá.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сумми́ровать</b> cộng gộp, tổng hợp</div>'
)

# ----------------------------------------------------------------- толпа
S["толпа"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: gốc Slav trơn.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đám đông người: <b>толпа́ люде́й</b>, <b>в толпе́</b> giữa đám đông. '
    'Số ít nhấn đuôi, sang số nhiều trọng âm nhảy lên đầu: <b>то́лпы</b>, <b>то́лпам</b> '
    '(cách 2 <b>толп</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>толпи́ться</b> chen chúc, tụ tập đông</div>'
)

# ----------------------------------------------------------------- итог
S["итог"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">и-</span>'
    '<span class="hd-gloss">VÀ (<b>и</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тог</span>'
    '<span class="hd-gloss">«của cái đó» (<b>того́</b>)</span></div>'
    '<div class="hd-warn">⚠️ Mức tin: đây là từ nguyên, không phải luật suy ra được — rút từ dòng '
    'sổ sách <b>итого́</b> «cộng lại là», ghép từ <b>и того́</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dòng «cộng lại» cuối sổ ⇒ con số tổng, bản tổng kết, kết cục cuối cùng.</div>'
    '<div class="hd-warn">Hai cụm phải thuộc: <b>в ито́ге</b> rốt cuộc · '
    '<b>подвести́ ито́ги</b> tổng kết, nhìn lại.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>итого́</b> tổng cộng · <b>ито́говый</b> tổng kết, cuối cùng</div>'
)

# ----------------------------------------------------------------- очередной
S["очередной"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">очеред-</span>'
    '<span class="hd-gloss">HÀNG, LƯỢT (<b>о́чередь</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ой</span>'
    '<span class="hd-gloss">đuôi tính từ nhấn đuôi</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đến lượt» ⇒ cái tiếp theo trong chuỗi (<b>очередно́й но́мер</b> số tiếp '
    'theo), hay cái đến theo lịch (định kỳ). Trọng âm nhảy từ đầu xuống đuôi: '
    '<b>о́чередь</b> → <b>очередно́й</b>.</div>'
    '<div class="hd-warn">Hay mang giọng chán: <b>в очередно́й раз</b> lại thêm một lần nữa · '
    '<b>очередна́я оши́бка</b> lại một lỗi nữa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>о́чередь</b> hàng, lượt · <b>по о́череди</b> lần lượt</div>'
)

B = {
    "docbangmat": 79,
    "loitubat": 0,
    "nguonsai": 0,
    "baolen": [
        "итог: V = «tổng kết, kết cục, tổng số» — đã BỎ «kết quả» để gỡ va chạm với результа́т (k65 đã nạp); mất nghĩa đầu của gloss (result), «kết cục» thay cho outcome. Cần duyệt.",
        "Va chạm nghĩa: mô phỏng do_va_cham trên toàn bộ thẻ với V mới (chỉ đọc) — 0 va chạm dính lô k166.",
        "заяви́ть/заявля́ть: CỐ Ý không đưa «thông báo» vào V — thêm vào thì đề объяви́ть/объявля́ть {thông báo, tuyên bố} nằm gọn trong đề заявить (cùng badge). «đòi quyền» lấy từ gloss claim/lay claim to — cần duyệt.",
        "непра́вда ↔ пра́во/пра́вый: luồng chính khai BÁO OAN, tôi cho là cùng gốc THẬT (прав- «thẳng, đúng», правда ← правый theo từ nguyên phổ biến) — đã để пра́вый, пра́вило trong Họ hàng; luồng chính không đồng ý thì bỏ hai từ đó.",
        "Chỗ KHÔNG chắc (đã hạ mức tin): итог ← итого́ ← и того́ (ô ⚠️ Mức tin); «Я извиня́юсь kém lịch sự hơn Извини́те» là sắc thái dùng (ô ⚠️ Mức tin). внеза́пный: không chẻ, không nêu từ nguyên vì không chắc.",
        "V cần duyệt (nới theo gloss): ны́нешний bỏ «bây giờ» (đó là trạng từ) → «hiện nay, hiện tại, ngày nay» · очередно́й «tiếp theo, kế tiếp, thêm một, định kỳ» · тру́бка +«ống nhỏ, tẩu thuốc» · кана́л +«ống dẫn», bỏ «con kênh» · су́мма, когда́-либо chỉ đổi «;» → «,».",
        "Dữ liệu GrammarJSON của извини́ться ghi gerundPast «извиня́сь» — đó là phó động từ của thể IMPF; không dùng, báo để biết.",
        "Họ hàng vắng có chủ ý: код, интервью́ (mượn đứng một mình).",
    ],
}
