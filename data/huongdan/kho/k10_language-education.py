# -*- coding: utf-8 -*-
"""k10 — language::education: lớp học và chữ nghĩa.

Trục của lô: **cái được NÓI ra và cái được VIẾT ra**. Ba gốc chạy xuyên lô —
`пис-` (viết: письмо́, пи́сьменно), `прос-` (hỏi: вопро́с, вопроси́тельный),
`слов-/рок-` (lời: сло́во, уро́к) — nên mỗi thẻ chỉ cần nói phần của chính nó.
"""

# 🔴 KHÔNG dựng biến khối dùng chung (HE/LUAT/THE…) rồi cộng vào mọi thẻ.
# Đó là cách cũ, đã bỏ 28/07 — xem README §3.

S = {}
V = {}

S["итальянский"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">италья́н-</span>'
    '<span class="hd-gloss">Ý — thân của <b>Ита́лия</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ский</span>'
    '<span class="hd-gloss">đuôi tính từ quốc tịch</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng khuôn với <b>ру́сский</b>, <b>англи́йский</b>: tên nước + đuôi '
    '<i>-ский</i>. Riêng <b>Ита́лия</b> chèn thêm <i>-ьян-</i> vào giữa, như '
    '<b>Аме́рика</b> → <b>америка́нский</b>. Trọng âm nhảy sang đúng chỗ chèn: '
    '<b>Ита́лия</b> nhấn ở <i>та</i>, còn <b>италья́нский</b> nhấn ở <i>ян</i>.</div>'
    '<div class="hd-warn">Nói MỘT THỨ TIẾNG thì dùng trạng từ: <b>говори́ть по-италья́нски</b>. '
    'Tính từ chỉ đứng trước danh từ: <b>италья́нский язы́к</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>Ита́лия</b> nước Ý · <b>италья́нец</b> người Ý · '
    '<b>италья́нка</b> phụ nữ Ý · <b>по-италья́нски</b> bằng tiếng Ý</div>'
)

S["вопросительный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вопро́с-</span>'
    '<span class="hd-gloss">câu hỏi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́тельн-</span>'
    '<span class="hd-gloss">hậu tố «dùng để…, có tính chất…»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hậu tố <i>-тельный</i> biến danh từ thành tính từ chỉ CÔNG DỤNG: '
    '<b>вопро́с</b> câu hỏi → <b>вопроси́тельный</b> «dùng để hỏi». Lắp đuôi thì trọng âm '
    'rời gốc, nhảy sang <i>-и́-</i>.</div>'
    '<div class="hd-warn"><b>вопроси́тельный знак</b> = dấu chấm hỏi «?» · '
    '<b>вопроси́тельное предложе́ние</b> = câu nghi vấn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вопро́с</b> câu hỏi · <b>спроси́ть</b> hỏi · '
    '<b>проси́ть</b> xin · <b>про́сьба</b> lời thỉnh cầu</div>'
)

S["учебник"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">уч-</span>'
    '<span class="hd-gloss">học, dạy</span></div>'
    '<div class="hd-row"><span class="hd-piece">-еб-</span>'
    '<span class="hd-gloss">phần thân lấy từ <b>учёба</b> việc học</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ник</span>'
    '<span class="hd-gloss">vật/người mang chức năng đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hậu tố <i>-ник</i> cho ra «cái dùng để…»: <b>ча́йник</b> là cái dùng cho trà, '
    '<b>уче́бник</b> là quyển dùng cho việc học.</div>'
    '<div class="hd-warn"><b>учёба</b> → <b>уче́бник</b>: chữ <i>ё</i> chỉ tồn tại khi nó MANG '
    'trọng âm; trọng âm dời đi thì <i>ё</i> viết thành <i>е</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>учи́ть</b> dạy, học thuộc · <b>учи́ться</b> đi học · '
    '<b>учи́тель</b> giáo viên · <b>учени́к</b> học sinh · <b>учёба</b> việc học</div>'
)

S["урок"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố</span></div>'
    '<div class="hd-row"><span class="hd-piece">-рок-</span>'
    '<span class="hd-gloss">gốc cổ «điều nói ra, điều định ra»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bài học là phần thầy ĐỊNH RA cho trò, nên <b>уро́к</b> vừa là tiết học '
    'trên lớp vừa là bài phải làm ở nhà. Cùng khuôn ghép: <i>с-</i> + <i>рок</i> = <b>срок</b> kỳ hạn.</div>'
    '<div class="hd-warn"><b>де́лать уро́ки</b> = làm bài tập về nhà — cụm này luôn ở SỐ NHIỀU.</div>'
    '<div class="hd-warn">⚠️ Mức tin: gốc cổ <i>рек-/рок-</i> «nói» là từ nguyên, không phải '
    'luật suy ra được — dùng để nhớ, đừng dùng để đoán từ mới.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>срок</b> kỳ hạn · <b>проро́к</b> nhà tiên tri — cùng gốc cổ '
    '<i>рек-/рок-</i> «nói»</div>'
)

S["язык"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — <b>язы́к</b> là một khối gốc trơn có từ tiếng Slav cổ, '
    'mọi mảnh tách ra đều là bịa.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một từ, hai tầng nghĩa nối liền nhau: CÁI LƯỠI (bộ phận) → cái mà lưỡi '
    'tạo ra, tức TIẾNG NÓI, NGÔN NGỮ. Tiếng Anh đi đúng con đường ấy: <i>tongue</i> vừa là lưỡi '
    'vừa là <i>mother tongue</i>.</div>'
    '<div class="hd-warn"><b>тяну́ть за язы́к</b> «kéo lưỡi ai» = ép người ta phải nói ra điều '
    'họ không định nói.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>языкозна́ние</b> ngôn ngữ học · <b>двуязы́чный</b> song ngữ · '
    '<b>язычо́к</b> lưỡi nhỏ, lưỡi gà</div>'
    '<div class="hd-sec">Bảng chia</div>'
    '<div class="hd-why">Trọng âm chỉ ở lại <i>-зы́-</i> khi từ đứng trần; hễ có đuôi là nó nhảy '
    'xuống đuôi — <b>языка́</b>, <b>языку́</b>, <b>языки́</b>.</div>'
)

S["журнал"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được trong tiếng Nga: <b>журна́л</b> mượn thẳng tiếng Pháp '
    '<i>journal</i>, mà <i>jour</i> tiếng Pháp là «ngày».</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc «của từng ngày» dựng ra cả ba nghĩa: sổ ghi theo ngày → sổ '
    'ghi chép nói chung → ấn phẩm ra đều kỳ, tức tạp chí. Tiếng Anh giữ nguyên mặt chữ: '
    '<i>journal</i>.</div>'
    '<div class="hd-warn"><b>журна́л</b> là sổ ghi THEO TRÌNH TỰ cho nhiều người xem '
    '(<b>кла́ссный журна́л</b> sổ đầu bài của lớp); nhật ký riêng tư là <b>дневни́к</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>журнали́ст</b> nhà báo · <b>журнали́стика</b> nghề báo, ngành báo chí</div>'
)

S["мел"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Một âm tiết, không chẻ được — <b>мел</b> là tên chất liệu, không phải '
    'từ ghép.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đi từ CHẤT sang VẬT: <b>мел</b> là loại đá vôi trắng mềm, nên vừa là '
    'thỏi phấn viết bảng vừa là vôi quét tường. Chỉ ba chữ cái — đừng lẫn với <b>ме́лкий</b> '
    '(nhỏ, nông).</div>'
    '<div class="hd-warn">Viết BẰNG phấn dùng cách 5, không cần giới từ: '
    '<b>писа́ть ме́лом</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мелово́й</b> bằng phấn, thuộc đá phấn</div>'
)

S["глагол"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được trong tiếng Nga hiện đại: <b>глаго́л</b> vốn là một từ '
    'Slav cổ nguyên khối, nghĩa «lời nói».</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ nghĩa cổ «lời nói», nhà ngữ pháp lấy nó đặt tên cho loại từ chở '
    'HÀNH ĐỘNG của câu — tức động từ. Nghĩa «lời nói» nay chỉ còn trong thơ cũ, học nghĩa '
    'ngữ pháp là đủ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>глаго́льный</b> thuộc động từ · <b>глаго́лица</b> bảng chữ Slav '
    'đầu tiên, có trước <b>кири́ллица</b></div>'
)

S["роман"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: <b>рома́н</b> mượn tiếng Pháp <i>roman</i>, vốn nghĩa '
    '«viết bằng tiếng bình dân» chứ không bằng tiếng Latin.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Truyện dài viết cho dân thường đọc → tiểu thuyết; mà tiểu thuyết thời '
    'ấy toàn kể chuyện yêu đương, nên <b>рома́н</b> ôm luôn nghĩa thứ hai: chuyện tình cảm. '
    'Tiếng Anh giữ nhánh sau: <i>romance</i>.</div>'
    '<div class="hd-warn"><b>у них рома́н</b> = họ đang có chuyện tình cảm với nhau.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>романи́ст</b> nhà tiểu thuyết · <b>рома́нс</b> bản tình ca · '
    '<b>рома́нтика</b> chất lãng mạn</div>'
)

S["слово"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">слов-</span>'
    '<span class="hd-gloss">lời, cái nói ra</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <i>слов-</i> là «cái nói ra»: từ đó ra cả TỪ lẫn LỜI NÓI, và ra '
    'nghĩa thứ ba là LỜI HỨA (<b>дать сло́во</b> hứa). Đổi nguyên âm thành <i>слав-</i> được '
    '<b>сла́ва</b> vinh quang — tiếng tăm cũng chỉ là lời người ta nói về mình.</div>'
    '<div class="hd-warn"><b>к сло́ву</b> nhân tiện · <b>по слова́м</b> + cách 2: theo lời của ai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>слова́рь</b> từ điển · <b>посло́вица</b> tục ngữ · '
    '<b>сло́вно</b> như thể · <b>сла́ва</b> vinh quang</div>'
    '<div class="hd-sec">Bảng chia</div>'
    '<div class="hd-why">Số ít giữ trọng âm ở gốc (<b>сло́ва</b>, <b>сло́ву</b>); sang số nhiều '
    'nó nhảy hết xuống đuôi — <b>слова́</b>, <b>слова́м</b>.</div>'
)

S["письмо"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пис-</span>'
    '<span class="hd-gloss">viết</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ьм-</span>'
    '<span class="hd-gloss">hậu tố tạo danh từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen là «cái được viết ra», nên một từ ôm cả ba: bức thư, việc '
    'viết, và hệ chữ viết (<b>кита́йское письмо́</b> chữ Hán).</div>'
    '<div class="hd-warn"><b>пи́сьма</b> (số nhiều: những bức thư) và <b>письма́</b> (cách 2 số '
    'ít: của bức thư) chỉ khác nhau ở CHỖ NHẤN.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>писа́ть</b> viết · <b>писа́тель</b> nhà văn · '
    '<b>пи́сьменный</b> thuộc chữ viết · <b>по́дпись</b> chữ ký</div>'
    '<div class="hd-sec">Bảng chia</div>'
    '<div class="hd-why">Ngược hẳn <b>сло́во</b>: số ít nhấn ở đuôi (<b>письма́</b>), số nhiều '
    'nhấn về gốc (<b>пи́сьма</b>); riêng cách 2 số nhiều chen thêm <i>-е-</i> cho đọc được: '
    '<b>пи́сем</b>.</div>'
)

S["письменно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пи́сьм-</span>'
    '<span class="hd-gloss">viết (từ <b>письмо́</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-енн-</span>'
    '<span class="hd-gloss">hậu tố tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Lấy tính từ <b>пи́сьменный</b>, bỏ đuôi tính từ, thay bằng <i>-о</i> là '
    'ra trạng từ. Trọng âm đã rời đuôi về gốc ngay ở bước <b>письмо́</b> → <b>пи́сьменный</b> '
    'và nằm yên đó.</div>'
    '<div class="hd-warn"><b>пи́сьменно</b> = «bằng văn bản», đối lập với <b>у́стно</b> «bằng '
    'lời nói» — KHÔNG có nghĩa «viết tay». Ví dụ: <b>отве́тить пи́сьменно</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>письмо́</b> bức thư · <b>пи́сьменный</b> thuộc chữ viết · '
    '<b>пи́сьменность</b> hệ chữ viết · <b>писа́ть</b> viết</div>'
)

S["суффикс"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">суф-</span>'
    '<span class="hd-gloss">Latin <i>sub-</i> «dưới, sau»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-фикс</span>'
    '<span class="hd-gloss">Latin <i>fixus</i> «gắn chặt»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen «gắn vào phía sau» — đúng việc mà <i>-ник</i>, <i>-тель</i>, '
    '<i>-ение</i> đang làm. Tiếng Anh <i>suffix</i> cùng gốc nên nhớ một lần dùng được cả hai. '
    'Sách ngữ pháp Nga còn gọi tiền tố bằng từ thuần Nga là <b>приста́вка</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пре́фикс</b> tiền tố, gắn phía TRƯỚC · <b>фикси́ровать</b> '
    'cố định, ghi nhận</div>'
)

S["вопрос"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">во-</span>'
    '<span class="hd-gloss">tiền tố <i>въ-</i> «vào»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-прос-</span>'
    '<span class="hd-gloss">gốc «hỏi, xin»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <i>прос-</i> cho <b>проси́ть</b> «xin»; ghép tiền tố «vào» thành '
    '«cái hỏi vào» → câu hỏi, rồi rộng ra thành vấn đề, chuyện phải giải. Ở thể chưa hoàn '
    'thành gốc biến âm <i>с → ш</i>: <b>спра́шивать</b>.</div>'
    '<div class="hd-warn">«Đặt câu hỏi» là <b>зада́ть вопро́с</b> (nghĩa đen «giao câu hỏi»), '
    'không dùng động từ «làm» hay «hỏi».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>проси́ть</b> xin · <b>спроси́ть</b> hỏi · <b>про́сьба</b> lời thỉnh '
    'cầu · <b>вопроси́тельный</b> nghi vấn</div>'
)

S["класс"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: <b>класс</b> là từ mượn quốc tế, gốc Latin '
    '<i>classis</i> «hạng, nhóm».</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một gốc, ba nghĩa xếp thành chuỗi: HẠNG/NHÓM → nhóm học sinh cùng năm '
    '(lớp 5) → căn phòng nơi nhóm ấy ngồi.</div>'
    '<div class="hd-warn"><b>класс</b> là lớp và phòng học; còn một TIẾT học là <b>уро́к</b>: '
    '«hôm nay có năm tiết» là <b>пять уро́ков</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кла́ссный</b> thuộc lớp · <b>класси́ческий</b> cổ điển · '
    '<b>классифика́ция</b> sự phân loại</div>'
)

# --- Field Vietnamese (đề bài deck 1-go) — chỉ từ nào thật sự cần sửa (README §2c)
# `письменно` đang ghi "viết tay": sai nghĩa. Trạng từ này đối lập với `у́стно`
# (bằng lời nói), không nói gì về việc viết bằng tay hay đánh máy.
V["письменно"] = "bằng văn bản, bằng chữ viết"
