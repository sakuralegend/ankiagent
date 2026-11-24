# -*- coding: utf-8 -*-
"""k245 — language::communication: hồi ký, bài phê bình, ký/đăng ký, nghe trộm, bình luận, bóng gió, nín thinh, nói hỗn, phàn nàn, từ biệt.

Chỗ cần nhất quán trong lô:
(1) подписа́ться / подпи́сываться: под- DƯỚI + -пис- VIẾT — khớp подписа́ть [k135], по́дпись [k173]; tách khỏi расписа́ться [k236].
(2) подслу́шать / подслу́шивать: под- LÉN + -слуш- ← слух — khớp вы́слушать [k193].
(3) комменти́ровать / про-, груби́ть / на-: tiền tố thể KHÔNG mang nghĩa riêng.
(4) намека́ть / намекну́ть: на- VÀO + -мек- NGHĨ (từ nguyên, ghi mức tin).
(5) промолча́ть ← молча́ть [k96], замолча́ть [k142]; груби́ть ← гру́бый [k129]; пожа́ловаться ← жа́ловаться [k200];
    прости́ться ← прости́ть [k129], проща́ться [k126]; гра́мотный ↔ грамма́тика [k51].
Họ hàng không vắng ở thẻ nào.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "мемуары": "hồi ký",                                                  # «hồi ức» là воспомина́ние; gloss chỉ memoirs
    "подписаться": "ký tên, đăng ký theo dõi, đặt mua dài hạn",           # «đăng ký», «theo dõi» trơ quá rộng; cặp thể cùng dãy
    "подписываться": "ký tên, đăng ký theo dõi, đặt mua dài hạn",         # giữ nguyên, khai để cặp thể cùng dãy
    "грамотный": "biết đọc biết viết, có trình độ, giỏi chuyên môn, bài bản, không sai lỗi",  # THIẾU correct / error-free
    "подслушать": "nghe trộm, nghe lén, tình cờ nghe được",               # overhear; cặp thể cùng dãy
    "подслушивать": "nghe trộm, nghe lén, tình cờ nghe được",
    "комментировать": "bình luận, nhận xét",                              # «bình phẩm» nới quá gloss comment
    "прокомментировать": "bình luận, nhận xét",                           # cặp thể cùng dãy
    "грубить": "nói thô lỗ, nói nặng lời, cư xử bất nhã",                 # «thô lỗ» trơ là tính từ гру́бый; «xúc phạm» là оскорби́ть
    "нагрубить": "nói thô lỗ, nói nặng lời, cư xử bất nhã",               # giữ nguyên, khai để cặp thể cùng dãy
    "проститься": "từ biệt, chia tay",                                    # rút «nói lời tạm biệt» (попроща́ться)
}

# --------------------------------------------------------------------- мемуары
S["мемуары"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn nguyên khối tiếng Pháp <i>mémoires</i>, không chẻ được theo tiếng Nga; chỉ thêm đuôi '
    'số nhiều <b>-ы</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Pháp <i>mémoire</i> = TRÍ NHỚ, cùng gốc tiếng Anh <i>memory, memoir</i> ⇒ những điều nhớ lại, '
    'viết thành sách = hồi ký. Hồi ký VỀ gì: <b>о</b> + cách 6, <b>мемуа́ры о войне́</b>.</div>'
    '<div class="hd-warn">Luôn dùng SỐ NHIỀU, kể cả chỉ một cuốn: <b>писа́ть мемуа́ры</b>. Cách 2 là '
    '<b>мемуа́ров</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мемуари́ст</b> người viết hồi ký · <b>мемуа́рный</b> (thuộc) hồi ký · '
    '<b>мемориа́л</b> đài tưởng niệm (cùng gốc Latin «trí nhớ»)</div>'
)

# --------------------------------------------------------------------- рецензия
S["рецензия"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn từ gốc Latin (<i>re-</i> LẠI + <i>cens-</i> ĐÁNH GIÁ); trong tiếng Nga coi là một khối, '
    'đuôi <b>-ия</b> giống cái.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Xét lại mà đánh giá» ⇒ bài phê bình một cuốn sách, bộ phim, vở diễn. Mảnh <i>cens-</i> là của '
    'tiếng Anh <i>censor</i>, <i>census</i>.</div>'
    '<div class="hd-warn">Bài viết VỀ cái gì: <b>на</b> + cách 4 — <b>реце́нзия на фильм</b>. Khác '
    '<b>обзо́р</b> (điểm khắp một lượt) vốn đi với cách 2: <b>обзо́р фи́льма</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рецензе́нт</b> người viết phê bình · <b>рецензи́ровать</b> viết bài nhận xét · '
    '<b>цензу́ра</b> sự kiểm duyệt</div>'
)

# --------------------------------------------------------------------- подписаться
S["подписаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span>'
    '<span class="hd-gloss">DƯỚI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пис-</span>'
    '<span class="hd-gloss">gốc VIẾT — <b>писа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть-ся</span>'
    '<span class="hd-gloss">đuôi động từ, quay về CHÍNH MÌNH</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">VIẾT tên MÌNH ở DƯỚI ⇒ ký tên; ký vào danh sách nhận báo ⇒ đặt mua dài hạn, theo dõi kênh. '
    'Đúng cả hai nghĩa của <i>sub-scribe</i>. Chia như <b>писа́ть</b>: с → ш, trọng âm lùi từ ngôi hai — '
    '<b>подпишу́сь, подпи́шешься</b>.</div>'
    '<div class="hd-warn">Theo dõi CÁI GÌ: <b>на</b> + cách 4 — <b>подписа́ться на кана́л</b>. '
    'Ký DƯỚI văn bản: <b>под</b> + cách 5 — <b>под письмо́м</b>.</div>'
    '<div class="hd-warn">Ký NHẬN hàng, nhận tiền là <b>расписа́ться</b>, không dùng từ này.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>подпи́сываться</b> (CHT) · <b>подписа́ть</b> ký (văn bản) · <b>подпи́ска</b> sự đặt mua '
    'dài hạn · <b>подпи́счик</b> người theo dõi</div>'
)

# --------------------------------------------------------------------- подписываться
S["подписываться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-пис-</span>'
    '<span class="hd-gloss">VIẾT ở DƯỚI = ký (xem <b>подписа́ться</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-ть-ся</span>'
    '<span class="hd-gloss">hậu tố biến hoàn thành → CHƯA hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ký, đăng ký theo dõi như một thói quen. Chia đều, giữ <b>с</b> ở mọi ngôi: '
    '<b>подпи́сываюсь, подпи́сываешься</b>. Trọng âm nhảy về ngay trước <i>-ыва-</i>, y như '
    '<b>подписа́ть → подпи́сывать</b>.</div>'
    '<div class="hd-warn">Câu mời quen trên mạng: <b>Подпи́сывайтесь на наш кана́л!</b> = Hãy đăng ký kênh của chúng tôi! '
    '(<b>на</b> + cách 4).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>подписа́ться</b> (HT) · <b>подпи́ска</b> sự đặt mua dài hạn · '
    '<b>по́дпись</b> chữ ký · <b>писа́ть</b> viết</div>'
)

# --------------------------------------------------------------------- грамотный
S["грамотный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">гра́мот-</span>'
    '<span class="hd-gloss">CHỮ NGHĨA — <b>гра́мота</b>, từ Hy Lạp gramma «chữ viết»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">→ tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Có chữ nghĩa» ⇒ biết đọc biết viết ⇒ có trình độ, giỏi nghề; nói về bài viết, lời nói thì là '
    'chuẩn, không sai lỗi: <b>гра́мотная речь</b>. Trạng từ: <b>гра́мотно писа́ть</b> viết đúng chính tả.</div>'
    '<div class="hd-warn">Cùng gốc với <b>грамма́тика</b> nhưng chỉ MỘT <b>м</b>.</div>'
    '<div class="hd-warn">Dạng ngắn giống đực chèn <b>е</b>: <b>гра́мотен</b> (còn lại đều: <b>гра́мотна, '
    'гра́мотны</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гра́мота</b> chữ nghĩa, giấy khen · <b>гра́мотность</b> sự biết chữ, sự viết đúng · '
    '<b>негра́мотный</b> mù chữ · <b>грамма́тика</b> ngữ pháp</div>'
)

# --------------------------------------------------------------------- подслушать
S["подслушать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span>'
    '<span class="hd-gloss">DƯỚI → LÉN, không để ai thấy</span></div>'
    '<div class="hd-row"><span class="hd-piece">-слуш-</span>'
    '<span class="hd-gloss">← <b>слух</b> TAI, sự nghe</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">chia đều</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">NGHE LÉN ⇒ nghe trộm. Cùng chữ <b>под-</b> «lén» với <b>подсмотре́ть</b> nhìn trộm. '
    'Nghe trộm cái gì → cách 4: <b>подслу́шать разгово́р</b>. Trọng âm đứng yên: <b>подслу́шаю</b>.</div>'
    '<div class="hd-warn">Thêm <b>случа́йно</b> thì hết ý xấu: <b>случа́йно подслу́шать</b> = tình cờ nghe được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>подслу́шивать</b> (CHT) · <b>слу́шать</b> nghe · <b>вы́слушать</b> nghe hết lời · '
    '<b>слух</b> thính giác</div>'
)

# --------------------------------------------------------------------- подслушивать
S["подслушивать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-слуш-</span>'
    '<span class="hd-gloss">NGHE LÉN (xem <b>подслу́шать</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ть</span>'
    '<span class="hd-gloss">hậu tố biến hoàn thành → CHƯA hoàn thành; sau <b>ш</b> viết <i>и</i>, không viết '
    '<i>ы</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đang nghe trộm, hay nghe trộm: <b>подслу́шивать под две́рью</b> nghe lén ngoài cửa. '
    'Chia đều: <b>подслу́шиваю, подслу́шиваешь</b>; trọng âm không đổi so với vế HT.</div>'
    '<div class="hd-warn">Bảo đừng nghe trộm thì dùng vế CHT này: <b>Не подслу́шивай!</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>подслу́шать</b> (HT) · <b>слу́шать</b> nghe · '
    '<b>выслу́шивать</b> nghe hết lời (CHT) · <b>слух</b> thính giác</div>'
)

# --------------------------------------------------------------------- комментировать
S["комментировать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">коммент-</span>'
    '<span class="hd-gloss">mượn, cùng gốc tiếng Anh <i>comment</i> — hai chữ <b>м</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ровать</span>'
    '<span class="hd-gloss">đuôi động từ mượn</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thấy <i>comment</i> là ra nghĩa: bình luận. Khi chia, <i>-ова-</i> thành <i>-у-</i>, trọng âm '
    'đứng yên ở <i>и</i>: <b>комменти́рую, комменти́руешь</b>.</div>'
    '<div class="hd-warn">Anh nói <i>comment ON</i>, Nga thì cách 4 trần, KHÔNG giới từ: '
    '<b>комменти́ровать но́вость</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>прокомменти́ровать</b> (HT) · <b>коммента́рий</b> lời bình luận · '
    '<b>коммента́тор</b> bình luận viên</div>'
)

# --------------------------------------------------------------------- прокомментировать
S["прокомментировать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">tiền tố thể — KHÔNG mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-комменти́ровать</span>'
    '<span class="hd-gloss">bình luận — <i>comment</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vế hoàn thành: đưa ra MỘT lời bình luận cụ thể. Chia y vế kia: '
    '<b>прокомменти́рую, прокомменти́руешь</b>. Tân ngữ cách 4: <b>прокомменти́ровать реше́ние</b>.</div>'
    '<div class="hd-warn">Câu từ chối quen trên báo: <b>Без коммента́риев</b> = Miễn bình luận.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>комменти́ровать</b> (CHT) · <b>коммента́рий</b> lời bình luận · '
    '<b>коммента́тор</b> bình luận viên</div>'
)

# --------------------------------------------------------------------- намекать
S["намекать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">VÀO, trỏ vào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мек-</span>'
    '<span class="hd-gloss">gốc cổ NGHĨ, HIỂU RA — như <b>смека́лка</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">chia đều: <b>намека́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trỏ ý VÀO cho người ta tự HIỂU RA ⇒ nói ẩn ý, ám chỉ. Tiền tố <b>на-</b> kéo luôn giới từ '
    '<b>на</b> + cách 4; ám chỉ VỚI ai → cách 3: <b>намека́ть дру́гу на де́ньги</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: <b>-мек-</b> là từ nguyên, tiếng Nga nay không còn cảm thấy mảnh này.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>намекну́ть</b> (HT) · <b>намёк</b> lời ám chỉ · <b>смека́лка</b> sự nhanh trí</div>'
)

# --------------------------------------------------------------------- намекнуть
S["намекнуть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-мек-</span>'
    '<span class="hd-gloss">trỏ ý VÀO cho người ta HIỂU RA (xem <b>намека́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ну́-ть</span>'
    '<span class="hd-gloss">làm MỘT cái — thể hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Buông MỘT câu bóng gió rồi thôi. Trọng âm nằm ở đuôi suốt bảng chia: '
    '<b>намекну́, намекнёшь, намекну́т</b>; quá khứ giữ <i>-ну-</i>: <b>намекну́л</b>.</div>'
    '<div class="hd-warn">Vẫn <b>на</b> + cách 4, hoặc cả một mệnh đề: <b>Он намекну́л, что пора́ идти́.</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>намека́ть</b> (CHT) · <b>намёк</b> lời ám chỉ · <b>смека́лка</b> sự nhanh trí</div>'
)

# --------------------------------------------------------------------- промолчать
S["промолчать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">QUA, trọn một quãng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-молч-а́ть</span>'
    '<span class="hd-gloss">IM, KHÔNG NÓI — <b>молча́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Im cho QUA» ⇒ lẽ ra đáp lại mà không nói gì: <b>Он промолча́л.</b> Cũng là im TRỌN một quãng: '
    '<b>промолча́ть весь ве́чер</b>. Chia lớp 2 như <b>молча́ть</b>: <b>промолчу́, промолчи́шь</b>.</div>'
    '<div class="hd-warn">Khác <b>замолча́ть</b>: đang nói thì im bặt. <b>промолча́ть</b> là từ đầu đã không '
    'mở miệng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>молча́ть</b> im lặng · <b>молча́ние</b> sự im lặng · <b>молчали́вый</b> ít nói · '
    '<b>мо́лча</b> lặng lẽ, không nói gì</div>'
)

# --------------------------------------------------------------------- грубить
S["грубить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">груб-</span>'
    '<span class="hd-gloss">THÔ, chưa mài giũa — <b>гру́бый</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2: cư xử kiểu đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cư xử THÔ ⇒ nói thô lỗ, hỗn. Riêng ngôi «tôi» chèn <b>л</b> sau <b>б</b> (như <b>люблю́</b>): '
    '<b>грублю́</b>, rồi <b>груби́шь, грубя́т</b>. Cặp HT: <b>нагруби́ть</b>.</div>'
    '<div class="hd-warn">Hỗn VỚI ai → cách 3, không giới từ: <b>груби́ть роди́телям</b>. Đừng nhầm với '
    '<b>оскорби́ть</b> xúc phạm, vốn đòi cách 4.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гру́бый</b> thô lỗ · <b>гру́бо</b> thô bạo · <b>гру́бость</b> sự thô lỗ · '
    '<b>грубия́н</b> kẻ thô lỗ</div>'
)

# --------------------------------------------------------------------- нагрубить
S["нагрубить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">tiền tố thể — KHÔNG mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-груб-и́ть</span>'
    '<span class="hd-gloss">THÔ, chưa mài giũa → cư xử thô (xem <b>груби́ть</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đã hỗn một lần, chuyện đã rồi: <b>Он нагруби́л учи́телю.</b> Người bị hỗn đứng cách 3 như vế '
    'kia. Chỉ ngôi «tôi» chèn <b>л</b>: <b>нагрублю́, нагруби́шь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>груби́ть</b> (CHT) · <b>гру́бый</b> thô lỗ · <b>гру́бость</b> sự thô lỗ · '
    '<b>грубия́н</b> kẻ thô lỗ</div>'
)

# --------------------------------------------------------------------- пожаловаться
S["пожаловаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố thể — KHÔNG mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-жа́л-</span>'
    '<span class="hd-gloss">THƯƠNG XÓT, tiếc — như <b>жаль</b>, <b>сожале́ние</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-ть-ся</span>'
    '<span class="hd-gloss">đuôi <b>-овать</b> (chia <b>-ую</b>) + phản thân</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Kể khổ cho người ta thương mình», một lần ⇒ phàn nàn, đi mách. Chia như <b>жа́ловаться</b>: '
    '<b>пожа́луюсь, пожа́луешься</b>.</div>'
    '<div class="hd-warn">Than CÁI GÌ: <b>на</b> + cách 4, với AI: cách 3 — '
    '<b>пожа́ловаться нача́льнику на шум</b>.</div>'
    '<div class="hd-warn">Bỏ <b>-ся</b> là nghĩa khác hẳn: <b>Добро́ пожа́ловать!</b> = Chào mừng!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>жа́ловаться</b> (CHT) · <b>жа́лоба</b> lời phàn nàn, đơn khiếu nại · <b>жале́ть</b> thương, '
    'tiếc · <b>пожа́луйста</b> làm ơn</div>'
)

# --------------------------------------------------------------------- проститься
S["проститься"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">прост-</span>'
    '<span class="hd-gloss">THOÁNG, TỰ DO — gốc của <b>просто́й</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2 — <b>прости́ть</b> tha thứ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">cho NHAU</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Lúc chia tay tha cho nhau ⇒ từ biệt. Ngôi «tôi» đổi <b>ст → щ</b>: <b>прощу́сь</b>, rồi '
    '<b>прости́шься</b>. Đi với <b>с</b> + cách 5: <b>прости́ться с друзья́ми</b>.</div>'
    '<div class="hd-warn"><b>попроща́ться</b> là chào tạm biệt hằng ngày; <b>прости́ться</b> trang trọng hơn, hay dùng cho '
    'cuộc chia tay lâu dài. Cũng là từ bỏ: <b>прости́ться с мечто́й</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>проща́ться</b> (CHT) · <b>прости́ть</b> tha thứ · <b>проща́ние</b> sự từ biệt · '
    '<b>просто́й</b> đơn giản</div>'
)

B = {
    "docbangmat": 91,
    "loitubat": 0,
    "nguonsai": 2,   # грубить: gloss «to insult» là оскорбить (груби́ть đòi cách 3) -> không cho vào V
                     # мемуары: nouns.csv ghi pl_only=0, có dạng số ít -> dạy luôn dùng số nhiều
    "baolen": [
        "V cần duyệt (9 thẻ đổi thật): мемуары (BỎ hồi ức — thẻ воспоминание = «ký ức, hồi ức») · подписаться (đăng ký / theo dõi trơ -> đăng ký theo dõi; đặt mua -> đặt mua dài hạn, khớp cặp CHT) · грамотный (THÊM không sai lỗi = correct, error-free) · подслушать, подслушивать (cùng dãy; tình cờ nghe được = overhear; BỎ lén nghe được) · комментировать (BỎ bình phẩm) · прокомментировать (BỎ lên tiếng về) · грубить (thô lỗ trơ là tính từ; BỎ xúc phạm; khớp cặp HT) · проститься (RÚT nói lời tạm biệt theo lời giao). подписываться, нагрубить khai trong V nhưng không đổi.",
        "CÂU GƯỢNG мемуары câu 1: «пишет мемуар» (từ chỉ dùng số nhiều). Đề nghị: Дед пишет мемуары о своей молодости. / Grandpa is writing his <b>memoirs</b> about his youth. / Ông mình đang viết <b>hồi ký</b> về thời trẻ.",
        "CÂU GƯỢNG мемуары câu 2: «половину мемуара». Đề nghị: Я прочитала половину мемуаров за один вечер. / I read half of the <b>memoirs</b> in one evening. / Mình đọc hết nửa cuốn <b>hồi ký</b> trong một buổi tối.",
        "подслушать câu 2: dịch «tình cờ nghe lén được» tự mâu thuẫn, EN là overheard. Đề nghị giữ câu Nga/Anh, dịch: Mình <b>tình cờ nghe được</b> họ nói chuyện trong bếp.",
        "грубить câu 3: dịch dùng «thô lỗ» trơ, V nay là «nói thô lỗ». Đề nghị giữ câu Nga/Anh, dịch: Đừng <b>nói thô lỗ</b> với em gái nữa, nó mới sáu tuổi.",
        "намекать câu 1: «намекаем ему про уборку» là khẩu ngữ, chuẩn (và thẻ dạy) là на + cách 4. Đề nghị: Мы третий день намекаем ему на уборку. / giữ nguyên Anh, Việt.",
        "подписаться câu 1–2 dịch «theo dõi», «đã đăng ký» (rút gọn của «đăng ký theo dõi» trong V) và подписываться câu 3 dịch «đăng ký»: để được, không bắt buộc sửa.",
        "Trùng hết nghĩa trong lô chỉ có 5 cặp thể (подпис-, подслуш-, коммент-, намек-, груб-) — badge thể tách. проститься ↔ прощаться[k126] cùng nghĩa (thứ tự khác: thẻ kia «chia tay, từ biệt»), badge thể tách.",
        "Không chắc, KHÔNG khẳng định: gốc -мек- (từ nguyên, ghi ô Mức tin); sắc thái проститься trang trọng hơn попрощаться là xu hướng, không phải luật.",
        "Thẻ cũ đã xem (подписать, подпись, расписаться, выслушать, молчать, замолчать, молчаливый, грубый, жаловаться, жаль, жалеть, прощаться, попрощаться, простить, обзор, грамматика): không gặp lỗi trọng âm hay chi tiết sai.",
    ],
}
