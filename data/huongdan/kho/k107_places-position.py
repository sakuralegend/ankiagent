# -*- coding: utf-8 -*-
"""k107 — places-position: 19 từ mới (đợt A1-A2 TRKI), soạn từng thẻ độc lập.

Không khối hệ thống. Chỗ cần nhất quán:
(1) bốn động từ chuyển động: лете́ть (một chiều) / полете́ть (по- khởi sự) cùng khuôn
    идти́/пойти́; води́ть, вози́ть là NHIỀU CHIỀU của вести́, везти́ (e -> o);
(2) я вожу́ trùng giữa води́ть và вози́ть — nói ở cả hai thẻ;
(3) dãy здесь/сюда́/отсю́да · там/туда́/отту́да trải ở ĐÚNG thẻ отсю́да, отту́да dẫn chiếu;
(4) gốc езд/езж (đi xe) xuyên пое́здка, прие́зд, уезжа́ть, уе́хать.
"""

S = {}

# -------------------------------------------------------- бесплатный
S["бесплатный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бес-</span>'
    '<span class="hd-gloss">KHÔNG, thiếu (chính là <b>без</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-плат-</span>'
    '<span class="hd-gloss">TRẢ TIỀN — gốc của <b>плати́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen «không phải trả tiền». Trạng từ: <b>беспла́тно</b>. '
    'Dạng ngắn giống đực chen thêm <b>е</b>: <b>беспла́тен</b>.</div>'
    '<div class="hd-warn"><b>без-</b> viết thành <b>бес-</b> trước phụ âm vô thanh (п, к, т, с…): '
    '<b>беспла́тный</b>, <b>бесполе́зный</b> vô ích. Viết theo âm, không phải lỗi chính tả.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>плати́ть</b> trả tiền · <b>пла́та</b> tiền phí · '
    '<b>зарпла́та</b> tiền lương · <b>беспла́тно</b> miễn phí (trạng từ)</div>'
)

# -------------------------------------------------------- везде
S["везде"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вез-</span>'
    '<span class="hd-gloss">vốn là <b>весь</b> — TẤT CẢ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-де</span>'
    '<span class="hd-gloss">hậu tố «Ở CHỖ», còn thấy trong <b>где</b>, <b>нигде́</b></span></div>'
    '<div class="hd-warn">⚠️ Mức tin: cách chẻ này là từ nguyên, mắt thường không còn thấy — '
    'dùng để nhớ, không phải luật suy ra được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Tất cả các chỗ» → mọi nơi, chỗ nào cũng. Trả lời câu <b>где?</b>. '
    'Đồng nghĩa <b>всю́ду</b> (nghe sách vở hơn một chút); <b>везде́</b> là từ nói hằng ngày.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>где</b> ở đâu · <b>нигде́</b> không ở đâu · '
    '<b>весь</b> tất cả · <b>всю́ду</b> khắp nơi</div>'
)

# -------------------------------------------------------- вниз
S["вниз"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">vào, HƯỚNG TỚI</span></div>'
    '<div class="hd-row"><span class="hd-piece">низ</span>'
    '<span class="hd-gloss">PHẦN DƯỚI, đáy</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Hướng về phía dưới» — chỉ HƯỚNG chuyển động, trả lời <b>куда́?</b>. '
    'Ngược lại: <b>вверх</b> lên trên.</div>'
    '<div class="hd-warn"><b>Иди́ вниз</b> = đi xuống dưới (hướng) · <b>Он внизу́</b> = anh ấy '
    'ở dưới (vị trí). Cùng kiểu <b>сюда́</b> / <b>здесь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>низ</b> phần dưới · <b>ни́зкий</b> thấp · '
    '<b>внизу́</b> ở dưới · <b>сни́зу</b> từ dưới lên</div>'
)

# -------------------------------------------------------- водить
S["водить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вод-</span>'
    '<span class="hd-gloss">gốc DẪN (một chiều là <b>вести́</b>, e → o)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Động từ chuyển động NHIỀU CHIỀU, như <b>ходи́ть</b>: dẫn đi lại, hay '
    'dẫn, và biết lái — <b>Я вожу́ маши́ну</b> = tôi biết lái, có lái xe. «Tôi» đổi д → ж, các ngôi '
    'khác trọng âm lùi: <b>вожу́, во́дишь</b>.</div>'
    '<div class="hd-warn"><b>я вожу́</b> vừa là «tôi dẫn, lái» (<b>води́ть</b>) vừa là «tôi chở» '
    '(<b>вози́ть</b>). Ngôi khác mới tách: <b>во́дишь</b> / <b>во́зишь</b>.</div>'
    '<div class="hd-warn"><b>вода́</b> (nước) trùng mặt chữ <b>вод-</b> nhưng khác gốc hẳn — '
    'đừng nối hai từ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вести́</b> dẫn (một chiều) · <b>води́тель</b> tài xế · '
    '<b>экскурсово́д</b> hướng dẫn viên · <b>руководи́тель</b> người lãnh đạo</div>'
)

# -------------------------------------------------------- возить
S["возить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">воз-</span>'
    '<span class="hd-gloss">gốc CHỞ — chính là <b>вез-</b> của <b>везти́</b>, e → o</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">NHIỀU CHIỀU của <b>везти́</b>, như <b>е́здить</b> ↔ <b>е́хать</b>: chở đi '
    'chở về, chở thường xuyên. Đổi e → o khi sang nhiều chiều là khuôn chung: '
    '<b>нести́ → носи́ть</b>. «Tôi» đổi з → ж: <b>вожу́, во́зишь</b>.</div>'
    '<div class="hd-warn"><b>я вожу́</b> trùng với «tôi dẫn, lái» của <b>води́ть</b>. '
    'Ngôi khác mới tách: <b>во́зишь</b> / <b>во́дишь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>везти́</b> chở (một chiều) · <b>привезти́</b> chở tới · '
    '<b>отвезти́</b> chở đi, đưa tới · <b>парово́з</b> đầu máy hơi nước (hơi + chở)</div>'
)

# -------------------------------------------------------- восточный
S["восточный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">восто́к</span>'
    '<span class="hd-gloss">PHÍA ĐÔNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ (к + н → чн)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>к</b> đổi thành <b>ч</b> trước <b>-н-</b>, y như <b>молоко́ → моло́чный</b>. '
    'Cùng khuôn với <b>за́падный</b>, <b>се́верный</b>. Dạng ngắn gần như không dùng.</div>'
    '<div class="hd-warn">⚠️ Mức tin: từ nguyên — <b>восто́к</b> vốn là «chỗ mặt trời dâng lên» '
    '(<b>вос-</b> lên + <b>ток</b> dòng chảy). Dùng để nhớ, không phải luật.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>восто́к</b> phía đông · <b>Да́льний Восто́к</b> Viễn Đông · '
    '<b>Бли́жний Восто́к</b> Trung Đông</div>'
)

# -------------------------------------------------------- глубокий
S["глубокий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">глуб-</span>'
    '<span class="hd-gloss">SÂU</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ок-ий</span>'
    '<span class="hd-gloss">hậu tố tính từ, như <b>высо́кий</b>, <b>широ́кий</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Sâu nghĩa đen lẫn nghĩa bóng: <b>глубо́кая река́</b> sông sâu, '
    '<b>глубо́кая мысль</b> ý sâu sắc. Dạng ngắn giống cái trọng âm nhảy ra đuôi: '
    '<b>глубока́</b>. Trạng từ: <b>глубоко́</b>.</div>'
    '<div class="hd-warn">So sánh hơn rụng hẳn <b>-ок-</b>, phải thuộc: <b>глу́бже</b> sâu hơn — '
    'như <b>высо́кий → вы́ше</b>, <b>широ́кий → ши́ре</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>глубина́</b> độ sâu · <b>глубоко́</b> sâu (trạng từ) · '
    '<b>углуби́ть</b> làm sâu thêm</div>'
)

# -------------------------------------------------------- корабль
S["корабль"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: từ mượn rất cổ, gốc Hy Lạp.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Con tàu lớn nói chung; đi với «vũ trụ» thành <b>косми́ческий кора́бль</b> '
    'tàu vũ trụ. Trọng âm nhảy ra đuôi ngay từ cách 2: <b>кора́бль → корабля́, кораблю́</b>; '
    'số nhiều <b>корабли́</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: từ nguyên — cùng nguồn Hy Lạp <i>kárabos</i> với tiếng Anh '
    '<i>caravel</i> (thuyền buồm). Dùng để nhớ, không phải luật.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кора́блик</b> con tàu nhỏ · <b>корабе́льный</b> thuộc về tàu</div>'
)

# -------------------------------------------------------- лететь
S["лететь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">лет- / лёт-</span>'
    '<span class="hd-gloss">gốc BAY</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">MỘT CHIỀU, như <b>идти́</b>, <b>е́хать</b>: đang bay tới một nơi. Bay qua '
    'lại, biết bay là <b>лета́ть</b>. Cặp HT: <b>полете́ть</b>. «Tôi» đổi т → ч: '
    '<b>лечу́, лети́шь</b>.</div>'
    '<div class="hd-warn"><b>я лечу́</b> còn là «tôi chữa bệnh» (<b>лечи́ть</b>, <b>ле́чишь</b>) — '
    'chỉ ngôi «tôi» trùng, ngữ cảnh tách.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лета́ть</b> bay (nhiều chiều) · <b>полёт</b> chuyến bay · '
    '<b>лётчик</b> phi công · <b>самолёт</b> máy bay (tự + bay) · <b>вертолёт</b> trực thăng</div>'
)

# -------------------------------------------------------- нигде
S["нигде"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ни-</span>'
    '<span class="hd-gloss">KHÔNG… NÀO (phủ định trọn)</span></div>'
    '<div class="hd-row"><span class="hd-piece">где</span>'
    '<span class="hd-gloss">ở đâu</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Không ở đâu». Trả lời <b>где?</b> (vị trí); không đi tới đâu (hướng) là '
    '<b>никуда́</b>. Ngược lại: <b>везде́</b>.</div>'
    '<div class="hd-warn">Câu phải có thêm <b>не</b>: <b>Я нигде́ не был.</b> = Tôi chưa đi đâu cả. '
    'Phủ định kép là bắt buộc, không phải thừa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>где</b> ở đâu · <b>никуда́</b> không đi đâu · '
    '<b>никогда́</b> không bao giờ · <b>ничего́</b> không gì cả</div>'
)

# -------------------------------------------------------- отсюда
S["отсюда"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">TỪ, rời khỏi</span></div>'
    '<div class="hd-row"><span class="hd-piece">сюда́</span>'
    '<span class="hd-gloss">về đây</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Rời khỏi chỗ này» → từ đây. Ba từ ứng ba câu hỏi: '
    '<b>где?</b> <b>здесь</b> ở đây · <b>куда́?</b> <b>сюда́</b> về đây · '
    '<b>отку́да?</b> <b>отсю́да</b> từ đây. Bên «đó» y hệt: <b>там · туда́ · отту́да</b>. '
    'Trong lập luận còn nghĩa «do đó».</div>'
    '<div class="hd-warn"><b>Э́то далеко́ отсю́да?</b> = Chỗ đó có xa đây không? — câu hỏi đường '
    'hay dùng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сюда́</b> về đây · <b>здесь</b> ở đây · '
    '<b>отту́да</b> từ đó · <b>отку́да</b> từ đâu</div>'
)

# -------------------------------------------------------- оттуда
S["оттуда"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">TỪ, rời khỏi</span></div>'
    '<div class="hd-row"><span class="hd-piece">туда́</span>'
    '<span class="hd-gloss">tới đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Rời khỏi chỗ đó» → từ đó, từ đằng kia. Dãy ba từ: <b>там</b> ở đó · '
    '<b>туда́</b> tới đó · <b>отту́да</b> từ đó. Bảng đủ hai bên nằm ở thẻ <b>отсю́да</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>туда́</b> tới đó · <b>там</b> ở đó · '
    '<b>отсю́да</b> từ đây · <b>отку́да</b> từ đâu</div>'
)

# -------------------------------------------------------- поездка
S["поездка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố — ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-езд-</span>'
    '<span class="hd-gloss">gốc ĐI XE (<b>е́здить</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-а</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Một lần đi xe» → chuyến đi, thường bằng xe, tàu, máy bay. Số nhiều '
    'cách 2 chen nguyên âm: <b>пое́здок</b>.</div>'
    '<div class="hd-warn"><b>по́езд</b> (tàu hỏa) ≠ <b>пое́здка</b> (chuyến đi): cùng gốc <b>езд</b>, '
    'khác trọng âm, khác nghĩa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>е́здить</b> đi lại bằng xe · <b>е́хать</b> đi xe · '
    '<b>прие́зд</b> sự đến · <b>съе́здить</b> đi một chuyến</div>'
)

# -------------------------------------------------------- полететь
S["полететь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố KHỞI SỰ — bắt đầu, lên đường</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лете́ть</span>'
    '<span class="hd-gloss">bay (một chiều)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng khuôn <b>пое́хать</b>, <b>пойти́</b>: <b>лете́ть</b> là đang bay, '
    '<b>полете́ть</b> là cất cánh bay đi. Chia y <b>лете́ть</b>: <b>полечу́, полети́шь</b>.</div>'
    '<div class="hd-warn"><b>За́втра я полечу́ в Москву́.</b> = Mai tôi bay đi Moskva — chuyến bay '
    'dự định nói bằng tương lai của <b>полете́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лете́ть</b> đang bay · <b>лета́ть</b> bay (nhiều chiều) · '
    '<b>полёт</b> chuyến bay · <b>самолёт</b> máy bay</div>'
)

# -------------------------------------------------------- приезд
S["приезд"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">TỚI NƠI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-езд</span>'
    '<span class="hd-gloss">gốc ĐI XE</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>прие́хать</b>: sự đến bằng xe, tàu. Ngược lại là '
    '<b>отъе́зд</b> sự rời đi. Đi bộ đến thì là <b>прихо́д</b>.</div>'
    '<div class="hd-warn">Ở sân bay, bảng «Đến» ghi <b>Прилёт</b> (<b>при-</b> + <b>лёт</b> bay), '
    'không phải <b>прие́зд</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>прие́хать</b> đến bằng xe · <b>приезжа́ть</b> đến bằng xe (CHT) · '
    '<b>отъе́зд</b> sự rời đi · <b>пое́здка</b> chuyến đi</div>'
)

# -------------------------------------------------------- путешествовать
S["путешествовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пут-е-</span>'
    '<span class="hd-gloss">ĐƯỜNG — gốc của <b>путь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-шеств-</span>'
    '<span class="hd-gloss">ĐI, BƯỚC (gốc cổ)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-ть</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-warn">⚠️ Mức tin: chẻ theo từ nguyên — <b>-шеств-</b> là «đi» còn thấy trong '
    '<b>ше́ствие</b> đoàn diễu hành (từ sách vở). Dùng để nhớ, không phải luật.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đi trên đường xa» → du lịch, chu du. Lớp <b>-ова-</b>: khi chia đổi thành '
    '<b>-у-</b> — <b>путеше́ствую, путеше́ствуешь</b>. Đi khắp một nước: '
    '<b>по</b> + cách 3 (<b>по Росси́и</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>путь</b> con đường · <b>путеше́ствие</b> chuyến du lịch · '
    '<b>путеше́ственник</b> người du hành</div>'
)

# -------------------------------------------------------- соседний
S["соседний"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сосе́д</span>'
    '<span class="hd-gloss">HÀNG XÓM</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ий</span>'
    '<span class="hd-gloss">đuôi tính từ MỀM</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thuộc nhà hàng xóm» → bên cạnh, kế bên: <b>сосе́дняя ко́мната</b> phòng '
    'bên. Đuôi mềm nên chia <b>-яя, -ее, -ие</b>, giống <b>си́ний</b>, <b>после́дний</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: từ nguyên — <b>сосе́д</b> vốn là <b>со-</b> cùng + '
    '<b>сед-</b> ngồi (như <b>сиде́ть</b>) = «người ngồi cạnh». Dùng để nhớ, không phải luật.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сосе́д</b> hàng xóm · <b>сосе́дка</b> hàng xóm nữ · '
    '<b>сосе́дство</b> sự kề cận</div>'
)

# -------------------------------------------------------- уезжать
S["уезжать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">RỜI KHỎI, ra xa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-езжа-</span>'
    '<span class="hd-gloss">gốc ĐI XE (<b>езд</b> → <b>езж</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thể chưa HT của <b>уе́хать</b>: đang đi, sắp đi, hay đi khỏi. Chia đều: '
    '<b>уезжа́ю, уезжа́ешь</b>. Rời đi bằng chân là <b>уходи́ть</b>.</div>'
    '<div class="hd-warn"><b>За́втра я уезжа́ю.</b> = Mai tôi đi rồi — hiện tại dùng cho chuyến '
    'đi sắp tới, rất hay gặp.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уе́хать</b> (HT) · <b>е́хать</b> đi xe · '
    '<b>приезжа́ть</b> đến bằng xe · <b>отъе́зд</b> sự rời đi</div>'
)

# -------------------------------------------------------- уехать
S["уехать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">RỜI KHỎI, ra xa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́хать</span>'
    '<span class="hd-gloss">đi xe</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">HT của <b>уезжа́ть</b>: đã đi khỏi, giờ không còn ở đây. Ngược lại: '
    '<b>прие́хать</b>. Thân chia không theo nguyên thể mà lấy <b>ед-</b> '
    'của <b>е́ду</b>: <b>уе́ду, уе́дешь</b>.</div>'
    '<div class="hd-warn"><b>Он уе́хал.</b> = Anh ấy đi xa rồi (rời thành phố) · <b>Он ушёл.</b> = '
    'anh ấy đi ra rồi (rời phòng, đi bộ).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уезжа́ть</b> (CHT) · <b>прие́хать</b> đến bằng xe · '
    '<b>уйти́</b> rời đi bằng chân · <b>отъе́зд</b> sự rời đi</div>'
)

V = {
    # Luồng chính: RÚT 'khắp nơi' (всюду k43 giữ); всюду đã nhường 'mọi nơi'.
    "везде": "mọi nơi, ở mọi chỗ",
    # Bỏ ngoặc "(xe)"; NHIỀU CHIỀU theo khuôn ходить «đi lại» — thêm "dẫn đi lại".
    "водить": "lái xe, dẫn dắt, dẫn đi lại, đưa đi",
    # Trục lô: không dùng 'chở' trơn (везти giữ 'chở bằng xe'); nhiều chiều kiểu ездить.
    "возить": "chở qua lại, chở đi chở về, vận chuyển",
    # Luồng chính: cùng kiểu северный/южный/западный ở k106; 'phương Đông' = oriental.
    "восточный": "phía đông, miền đông, phương Đông",
    # Một chiều theo khuôn ехать «đi xe, đang đi tới bằng xe»; giữ 'bay' trơn (trục lô).
    "лететь": "bay, đang bay tới, đi máy bay",
    # Thêm "bắt đầu bay" cho khớp пойти/повезти (по- khởi sự).
    "полететь": "bay đi, bắt đầu bay, khởi hành bằng máy bay",
    # "ở đây ra" không phải tiếng Việt tự nhiên; thêm nghĩa "hence" (do đó).
    "отсюда": "từ đây, từ chỗ này, do đó",
    # Thêm "chu du" (to voyage / go on travels).
    "путешествовать": "du lịch, chu du",
    # Luồng chính: RÚT 'rời đi' (уйти/уходить k98 giữ); bỏ "về quê" (nới rộng).
    # Cặp thể: cùng một bộ nghĩa, badge thể tách hai vế.
    "уезжать": "đi khỏi bằng xe, đi xa",
    "уехать": "đi khỏi bằng xe, đi xa",
}
