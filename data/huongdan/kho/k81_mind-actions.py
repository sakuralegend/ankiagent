# -*- coding: utf-8 -*-
"""k81 — mind-actions: từ mới user vừa thêm, trục trí óc + cảm xúc + hành động.

Các từ KHÔNG cùng một họ, nên mỗi thẻ soạn độc lập, không ép trục chung và
không dựng khối hệ thống. Rủi ro riêng của lô này: phần lớn từ ở đây là THỂ KIA
của một thẻ đã có trong kho (забыва́ть↔забы́ть, полюби́ть↔люби́ть, суме́ть↔уме́ть…),
nên chỗ nào cũng phải nói cái mà thẻ kia KHÔNG nói: tiền tố thêm vào đổi gì.
"""

S = {}

# ------------------------------------------------------------- забывать
S["забывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">tiền tố: bỏ lại PHÍA SAU, ra khỏi tầm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бы-</span>'
    '<span class="hd-gloss">gốc <b>быть</b> — LÀ, tồn tại</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва́ть</span>'
    '<span class="hd-gloss">hậu tố KÉO DÀI → thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái gì đó thôi TỒN TẠI trong đầu, bị bỏ lại phía sau — '
    'đó là quên. Hậu tố <b>-ва-</b> kéo việc quên ra thành đang quên / hay quên, '
    'nên đây là thể chưa hoàn thành.</div>'
    '<div class="hd-warn">Thể hoàn thành <b>забы́ть</b> chia bám theo <b>быть</b>: '
    '<b>я забу́ду, ты забу́дешь</b> — không phải «забы́ю».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>быть</b> là, tồn tại · <b>забы́ть</b> quên mất (xong) · '
    '<b>забы́вчивый</b> hay quên · <b>незабыва́емый</b> không thể nào quên</div>'
)

# ------------------------------------------------------------- извинять
S["извинять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">из-</span>'
    '<span class="hd-gloss">tiền tố: RA KHỎI, lấy ra ngoài</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вин-</span>'
    '<span class="hd-gloss">gốc <b>винова́тый</b> — LỖI, tội</span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Lấy cái LỖI RA KHỎI người ta = tha lỗi cho họ. Vậy chủ ngữ là '
    'người THA, còn kẻ có lỗi đứng ở cách 4: <b>Извини́те меня́</b> = xin hãy gỡ lỗi '
    'cho tôi.</div>'
    '<div class="hd-warn">Muốn nói «tôi xin lỗi» thì dùng dạng mệnh lệnh <b>извини́</b> '
    '/ <b>извини́те</b>. Bản thân <b>извиня́ть</b> là tha lỗi CHO NGƯỜI KHÁC, đừng dịch '
    'thẳng thành «xin lỗi».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>винова́тый</b> có lỗi · <b>извини́ть</b> tha lỗi (xong) · '
    '<b>извине́ние</b> lời xin lỗi · <b>извини́ться</b> tự xin lỗi</div>'
)

# -------------------------------------------------------------- интерес
S["интерес"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được thành mảnh Nga: đây là từ mượn nguyên khối, '
    'vào tiếng Nga từ Tây Âu, gốc Latin <i>inter-esse</i> = '
    '«có phần ở trong đó».</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng là chữ <i>interest</i> của tiếng Anh viết bằng chữ Nga, '
    'nghĩa cũng trùng: sự chú ý hướng về một cái gì. Kết thúc bằng phụ âm cứng nên là '
    'danh từ giống đực, biến cách đều.</div>'
    '<div class="hd-warn">Quan tâm TỚI cái gì thì dùng <b>к</b> + cách 3: '
    '<b>интере́с к му́зыке</b> = sự quan tâm tới âm nhạc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>интере́сный</b> thú vị · <b>интересова́ться</b> quan tâm '
    'tới · <b>поинтересова́ться</b> hỏi han · <b>интере́сно</b> hay đấy, thú vị</div>'
)

# ------------------------------------------------------------- полюбить
S["полюбить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố KHỞI ĐIỂM: bước vào một trạng thái mới</span></div>'
    '<div class="hd-row"><span class="hd-piece">-люб-</span>'
    '<span class="hd-gloss">gốc <b>люби́ть</b> — YÊU, thích</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi động từ lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ở đây <b>по-</b> KHÔNG phải «làm một tí» mà đánh dấu điểm '
    'chuyển: từ chỗ chưa yêu sang chỗ đã yêu. <b>Я полюби́л её</b> = tôi đã đem lòng '
    'yêu cô ấy, chứ không phải «yêu một lúc».</div>'
    '<div class="hd-warn">Riêng ngôi TÔI chèn thêm <b>-л-</b> sau <b>б</b>, và trọng '
    'âm nhảy: <b>я полюблю́</b> nhưng <b>ты полю́бишь, они́ полю́бят</b>. Cùng luật với '
    '<b>люби́ть → я люблю́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>люби́ть</b> yêu, thích · <b>любо́вь</b> tình yêu · '
    '<b>люби́мый</b> yêu quý, ưa nhất</div>'
)

# --------------------------------------------------------------- узнать
S["узнать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố: ĐẠT TỚI, tới nơi rồi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-зна-</span>'
    '<span class="hd-gloss">gốc <b>знать</b> — BIẾT</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ chỗ chưa biết mà ĐẠT TỚI chỗ biết → biết được, tìm ra. '
    'Nghĩa «nhận ra» cũng đi ra từ đó: gặp lại người quen, phải một giây mới «biết ra» '
    'đó là ai.</div>'
    '<div class="hd-warn">Dễ lẫn với thể chưa hoàn thành <b>узнава́ть</b>: hai dạng ngôi '
    'TÔI chỉ khác trọng âm — <b>узнаю́</b> (đang dò hỏi) so với <b>узна́ю</b> (sẽ biết '
    'ra).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>знать</b> biết · <b>зна́ние</b> kiến thức · '
    '<b>знако́мый</b> quen, người quen · <b>призна́ться</b> thú nhận</div>'
)

# ---------------------------------------------------------------- уметь
S["уметь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ум-</span>'
    '<span class="hd-gloss">gốc <b>ум</b> — TRÍ ÓC, đầu óc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ть</span>'
    '<span class="hd-gloss">đuôi động từ chỉ TRẠNG THÁI, như <b>боле́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Có cái ĐẦU cho một việc = biết cách làm việc đó. Chia đều '
    'đặn: <b>я уме́ю, ты уме́ешь</b>.</div>'
    '<div class="hd-warn">Khác <b>мочь</b>: <b>уме́ть</b> là có KỸ NĂNG, đã học nên biết '
    'cách; <b>мочь</b> là lúc này có điều kiện. <b>Я уме́ю пла́вать</b> = tôi biết bơi, '
    'còn <b>Я могу́ пла́вать</b> = giờ tôi bơi được.</div>'
    '<div class="hd-warn">Sau <b>уме́ть</b> luôn là ĐỘNG TỪ NGUYÊN THỂ, không bao giờ là '
    'danh từ: nói được <b>уме́ю чита́ть</b>, còn «biết tiếng Nga» phải nói '
    '<b>зна́ю ру́сский</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ум</b> trí óc · <b>у́мный</b> thông minh · '
    '<b>суме́ть</b> xoay sở được · <b>уме́лый</b> khéo tay</div>'
)

# ------------------------------------------------------------- уставать
S["уставать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố: cạn đi, hết đà</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ста-</span>'
    '<span class="hd-gloss">gốc <b>стать</b> — đứng, trụ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва́ть</span>'
    '<span class="hd-gloss">hậu tố KÉO DÀI → thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trụ không còn nổi nữa thì là mệt. Mệt VÌ cái gì thì dùng '
    '<b>от</b> + cách 2: <b>уста́л от рабо́ты</b> = mệt vì công việc.</div>'
    '<div class="hd-warn">Hậu tố <b>-ва-</b> RỤNG ở thì hiện tại: <b>я устаю́, ты '
    'устаёшь</b> — không phải «устава́ю». Cùng bảng với <b>дава́ть → даю́</b> và '
    '<b>встава́ть → встаю́</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: mối nối <b>-ста-</b> với <b>стать</b> là từ '
    'nguyên, không phải luật suy ra được — dùng để nhớ thì tốt, đừng dùng để đoán từ '
    'mới.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уста́ть</b> mệt rồi (xong) · <b>уста́лый</b> mệt mỏi · '
    '<b>уста́лость</b> sự mệt mỏi</div>'
)

# ----------------------------------------------------- поинтересоваться
S["поинтересоваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố: một lần, một lúc → thể hoàn thành</span></div>'
    '<div class="hd-row"><span class="hd-piece">-интерес-</span>'
    '<span class="hd-gloss">gốc <b>интере́с</b> — sự quan tâm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова́-</span>'
    '<span class="hd-gloss">hậu tố biến danh từ thành động từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">phản thân: mối quan tâm dấy lên trong CHÍNH MÌNH</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tự mình dấy lên mối quan tâm, một lần — nên trong đời thường '
    'nó thành «hỏi han một câu». Nhóm <b>-овать</b> đổi <b>-ова-</b> thành <b>-у-</b> '
    'khi chia: <b>я поинтересу́юсь</b>.</div>'
    '<div class="hd-warn">Hỏi han VỀ cái gì thì để cách 5, không cần giới từ: '
    '<b>Он поинтересова́лся мои́м здоро́вьем</b> = anh ấy hỏi han sức khoẻ tôi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>интере́с</b> sự quan tâm · <b>интересова́ться</b> quan tâm '
    'tới · <b>интере́сный</b> thú vị</div>'
)

# -------------------------------------------------------------- научить
S["научить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">tiền tố: chất cho ĐẦY, tới nơi tới chốn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-уч-</span>'
    '<span class="hd-gloss">gốc <b>учи́ть</b> — dạy, học</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi động từ lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>учи́ть</b> là đang dạy; thêm <b>на-</b> là dạy tới lúc người '
    'ta LÀM ĐƯỢC. Có kết quả rồi mới dùng được từ này.</div>'
    '<div class="hd-warn">Kết cấu: dạy AI thì cách 4, dạy LÀM GÌ thì để nguyên thể — '
    '<b>Он научи́л меня́ гото́вить</b> = anh ấy dạy tôi nấu ăn. Thêm <b>-ся</b> thành '
    '<b>научи́ться</b> = tự học được.</div>'
    '<div class="hd-warn">Trọng âm nhảy về trước ở mọi ngôi trừ TÔI: <b>я научу́</b> '
    'nhưng <b>ты нау́чишь, они́ нау́чат</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>учи́ть</b> dạy, học · <b>учи́ться</b> học · '
    '<b>учи́тель</b> thầy giáo · <b>нау́ка</b> khoa học</div>'
)

# --------------------------------------------------------------- суметь
S["суметь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">tiền tố: làm trọn một lần → thể hoàn thành</span></div>'
    '<div class="hd-row"><span class="hd-piece">-уме́-</span>'
    '<span class="hd-gloss">gốc <b>ум</b> — TRÍ ÓC, biết cách</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>уме́ть</b> là biết cách; thêm <b>с-</b> thành lần này đem '
    'cái biết ấy ra dùng và làm xong. <b>Она́ суме́ла его́ убеди́ть</b> = cô ấy thuyết '
    'phục nổi anh ta.</div>'
    '<div class="hd-warn">Ba từ sát nhau, phân theo đúng câu này: <b>уме́ть</b> biết '
    'cách (kỹ năng) — <b>суме́ть</b> lần này làm nổi — <b>смочь</b> đủ điều kiện nên '
    'làm được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уме́ть</b> biết làm · <b>ум</b> trí óc · '
    '<b>у́мный</b> thông minh · <b>уме́лый</b> khéo tay</div>'
)

# ------------------------------------------------------------ выполнять
S["выполнять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span>'
    '<span class="hd-gloss">tiền tố: RA, cho tới hết</span></div>'
    '<div class="hd-row"><span class="hd-piece">-полн-</span>'
    '<span class="hd-gloss">gốc <b>по́лный</b> — ĐẦY, trọn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm cho ĐẦY tới hết = thi hành trọn một nhiệm vụ. Vì thế nó đi '
    'với việc được giao — <b>план, рабо́ту, обеща́ние</b> — chứ không thay được '
    '<b>де́лать</b> ở việc lặt vặt hằng ngày.</div>'
    '<div class="hd-warn">Sang thể hoàn thành, tiền tố <b>вы-</b> hút trọng âm về mình: '
    '<b>выполня́ть → вы́полнить</b>. Đây là luật chung của <b>вы-</b>, y hệt '
    '<b>выходи́ть → вы́йти</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>по́лный</b> đầy, hoàn toàn · <b>вы́полнить</b> thi hành '
    'xong · <b>заполня́ть</b> điền vào · <b>испо́лнить</b> thực hiện, biểu diễn</div>'
)

# ------------------------------------------------------------- закурить
S["закурить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">tiền tố BẮT ĐẦU: động tác đầu tiên của việc ấy</span></div>'
    '<div class="hd-row"><span class="hd-piece">-кур-</span>'
    '<span class="hd-gloss">gốc <b>кури́ть</b> — hút thuốc, bốc khói</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi động từ lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là <b>за-</b> nghĩa BẮT ĐẦU, không phải <b>за-</b> «vào». '
    'Nên <b>закури́ть</b> là châm điếu thuốc rồi rít hơi đầu, chứ không phải hút thuốc '
    'nói chung. Cùng lối với <b>запе́ть</b> cất tiếng hát, <b>заговори́ть</b> cất tiếng '
    'nói.</div>'
    '<div class="hd-warn">Trọng âm nhảy về trước ở mọi ngôi trừ TÔI: <b>я закурю́</b> '
    'nhưng <b>ты заку́ришь, они́ заку́рят</b> — y hệt <b>кури́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кури́ть</b> hút thuốc · <b>кури́льщик</b> người hút thuốc · '
    '<b>некуря́щий</b> người không hút thuốc</div>'
)

# -------------------------------------------------------------- записать
S["записать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">tiền tố: đưa VÀO, cất vào chỗ nào đó</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пис-</span>'
    '<span class="hd-gloss">gốc <b>писа́ть</b> — VIẾT</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Viết rồi cất VÀO một chỗ — vào sổ, vào băng, vào máy. Đó là lý '
    'do cùng một từ vừa là ghi chép vừa là thu âm: cái gì cũng «đưa vào» được.</div>'
    '<div class="hd-warn">Thân hiện tại đổi <b>с → ш</b> và trọng âm lùi: '
    '<b>я запишу́, ты запи́шешь, они́ запи́шут</b>. Y hệt <b>писа́ть → пишу́, пи́шешь</b>.'
    '</div>'
    '<div class="hd-warn">Thêm <b>-ся</b> là ghi tên CHÍNH MÌNH vào: '
    '<b>записа́ться к врачу́</b> = đặt lịch khám.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>писа́ть</b> viết · <b>за́пись</b> bản ghi · '
    '<b>запи́ска</b> mẩu giấy nhắn · <b>по́дпись</b> chữ ký</div>'
)

# ------------------------------------------------------------- повторить
S["повторить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố: một lần trọn vẹn → thể hoàn thành</span></div>'
    '<div class="hd-row"><span class="hd-piece">-втор-</span>'
    '<span class="hd-gloss">gốc <b>второ́й</b> — THỨ HAI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi động từ lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm cho có LẦN THỨ HAI = nhắc lại, ôn lại. Hiếm khi một số thứ '
    'tự đẻ ra động từ như thế, nên nhớ <b>второ́й</b> là nhớ luôn từ này. Trọng âm đứng '
    'yên ở đuôi: <b>я повторю́, ты повтори́шь</b>.</div>'
    '<div class="hd-warn">Câu cửa miệng phải thuộc: <b>Повтори́те, пожа́луйста</b> = '
    'xin nhắc lại giúp tôi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>второ́й</b> thứ hai · <b>повторя́ть</b> lặp lại (nhiều lần) · '
    '<b>повторе́ние</b> sự lặp lại, việc ôn tập</div>'
)

# -------------------------------------------------------------- подарить
S["подарить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố: một lần trọn vẹn → thể hoàn thành</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дар-</span>'
    '<span class="hd-gloss">gốc <b>дар</b> — MÓN QUÀ, cùng nhà với <b>дать</b> cho</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi động từ lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cho mà không đòi lại thì là quà: gốc <b>-дар-</b> nối thẳng '
    '<b>дать</b> (cho) với <b>дар</b> (quà). Thêm <b>по-</b> là đã tặng xong một lần.</div>'
    '<div class="hd-warn">Người nhận đứng ở cách 3, món quà ở cách 4: '
    '<b>Я подари́л ей цветы́</b> = tôi đã tặng cô ấy hoa.</div>'
    '<div class="hd-warn">Trọng âm nhảy về trước ở mọi ngôi trừ TÔI: <b>я подарю́</b> '
    'nhưng <b>ты пода́ришь, они́ пода́рят</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дар</b> món quà · <b>дари́ть</b> tặng · '
    '<b>пода́рок</b> món quà · <b>благодари́ть</b> cảm ơn</div>'
)

# ----------------------------------------------------------- подготовить
S["подготовить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span>'
    '<span class="hd-gloss">tiền tố: lót nền, làm sẵn TỪ TRƯỚC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-готов-</span>'
    '<span class="hd-gloss">gốc <b>гото́вый</b> — SẴN SÀNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi động từ lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm cho SẴN SÀNG từ trước. Khác <b>гото́вить</b> trơn ở đúng '
    'chỗ dễ nhầm: <b>гото́вить</b> còn nghĩa nấu ăn, còn <b>подгото́вить</b> thì luôn là '
    'chuẩn bị / luyện cho sẵn sàng, không bao giờ là nấu.</div>'
    '<div class="hd-warn">Riêng ngôi TÔI chèn thêm <b>-л-</b> sau <b>в</b>: '
    '<b>я подгото́влю</b> nhưng <b>ты подгото́вишь</b>. Cùng luật môi + л với '
    '<b>люби́ть → люблю́</b>.</div>'
    '<div class="hd-warn">Thêm <b>-ся</b> là tự chuẩn bị, đi với <b>к</b> + cách 3: '
    '<b>подгото́виться к экза́мену</b> = ôn cho kỳ thi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гото́вый</b> sẵn sàng · <b>гото́вить</b> chuẩn bị, nấu · '
    '<b>подгото́вка</b> sự chuẩn bị</div>'
)

# --------------------------------------------------------------- позвать
S["позвать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố: một tiếng gọi trọn vẹn → thể hoàn thành</span></div>'
    '<div class="hd-row"><span class="hd-piece">-зв-</span>'
    '<span class="hd-gloss">gốc <b>звать</b> — GỌI, cất tiếng gọi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ điển nói rõ đây là gọi BẰNG TIẾNG — cất tiếng gọi ai đó '
    'lại. Người bị gọi đứng ở cách 4: <b>Позови́ Ната́шу</b> = gọi Natasha hộ với.</div>'
    '<div class="hd-warn">Thân hiện tại nở thêm <b>-о-</b>, không suy được từ nguyên '
    'thể: <b>я позову́, ты позовёшь</b>. Cùng bảng với <b>звать → зову́, зовёшь</b>.</div>'
    '<div class="hd-warn">Quá khứ giống cái nhảy trọng âm ra cuối: <b>он позва́л</b> '
    'nhưng <b>она́ позвала́</b>. Đúng nhóm với <b>брать → брала́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>звать</b> gọi · <b>зов</b> tiếng gọi · '
    '<b>назва́ние</b> tên gọi · <b>называ́ться</b> được gọi là</div>'
)

# ------------------------------------------------------------- поспорить
S["поспорить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố: một trận, một lần → thể hoàn thành</span></div>'
    '<div class="hd-row"><span class="hd-piece">-спор-</span>'
    '<span class="hd-gloss">gốc <b>спор</b> — cuộc tranh cãi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi động từ lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ <b>спор</b> gói lại thành một trận cãi đã xong. Nghĩa '
    '«cá cược» đi ra từ đó: hai bên cãi ai đúng, rồi đặt cược lên chính phần cãi ấy.</div>'
    '<div class="hd-warn">Cãi VỚI ai thì <b>с</b> + cách 5, VỀ chuyện gì thì <b>о</b> + '
    'cách 6: <b>Я поспо́рил с бра́том о поли́тике</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>спор</b> cuộc tranh cãi · <b>спо́рить</b> tranh cãi · '
    '<b>спо́рный</b> gây tranh cãi</div>'
)

# ------------------------------------------------------------ поцеловать
S["поцеловать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố: một cái, một lần → thể hoàn thành</span></div>'
    '<div class="hd-row"><span class="hd-piece">-цел-</span>'
    '<span class="hd-gloss">gốc <b>це́лый</b> — NGUYÊN VẸN, lành lặn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова́ть</span>'
    '<span class="hd-gloss">hậu tố tạo động từ, nhóm chia <b>-у́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc là lời chúc cho được LÀNH LẶN — lời chúc sức khoẻ ấy '
    'về sau hoá thành cái hôn. Chia theo nhóm <b>-овать</b>: <b>я поцелу́ю, ты '
    'поцелу́ешь</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: mối nối với <b>це́лый</b> là từ nguyên, không phải '
    'luật suy ra được. Còn <b>цель</b> «mục tiêu» thì KHÔNG cùng gốc — nó mượn từ tiếng '
    'Đức, chỉ tình cờ trông giống.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>целова́ть</b> hôn · <b>поцелу́й</b> nụ hôn · '
    '<b>це́лый</b> nguyên vẹn, cả</div>'
)


# ==================================================================== V
# Field `Vietnamese` = ĐỀ BÀI của deck 1-go (README §2c). Chỉ khai từ phải sửa.
V = {
    # SAI NGHĨA: извиня́ть là THA LỖI CHO NGƯỜI KHÁC. "xin lỗi" là извини́ться
    # (hoặc mệnh lệnh извини́те) -> để nguyên là dạy user gõ nhầm sang từ phản thân.
    "извинять": "tha thứ, bỏ qua, thứ lỗi",
    # bỏ "tìm hiểu": đó là nghĩa QUÁ TRÌNH, hợp với узнава́ть; узна́ть là biết RA.
    "узнать": "biết được, nhận ra",
    # bỏ "có khả năng làm gì" — cụm đó kéo về phía мочь/смочь. уме́ть là KỸ NĂNG.
    "уметь": "biết làm gì, biết cách làm gì",
    # VA CHẠM A: суме́ть <-> смочь "có thể, làm được" (cùng v + PERF). Rút gọn vế
    # của mình: bỏ hai nghĩa rộng, giữ sắc thái "xoay sở nổi nhờ biết cách".
    "суметь": "xoay sở được, làm nổi",
    # VA CHẠM A (2 chỗ): выполня́ть <-> де́лать "làm, thực hiện" (cùng v + IMPF).
    # Bỏ cả "làm" lẫn "thực hiện", giữ đúng nghĩa lõi "carry out" của gloss Anh.
    "выполнять": "hoàn thành, thi hành",
    # VA CHẠM A: позва́ть <-> пригласи́ть "mời" (cùng v + PERF). Từ điển ghi rõ nghĩa
    # lõi là gọi BẰNG TIẾNG -> bỏ "mời", để пригласи́ть giữ trọn nghĩa đó.
    "позвать": "gọi",
    # VA CHẠM A: поинтересова́ться <-> спроси́ть "hỏi, hỏi thăm" (cùng v + PERF).
    # Bỏ "hỏi thăm" cho спроси́ть giữ; "hỏi han" là đúng gloss Anh "to inquire".
    "поинтересоваться": "quan tâm, hỏi han",
    # bỏ mệnh đề giải thích "hướng dẫn cho ai biết làm gì" (§2c cấm ③)
    "научить": "dạy, dạy cho biết làm",
    # bỏ "hút thuốc" trơn — đó là кури́ть; за- ở đây là BẮT ĐẦU.
    "закурить": "bắt đầu hút thuốc, châm thuốc",
    # bỏ "làm quà" — không phải nghĩa của động từ này.
    "подарить": "tặng, biếu",
    # bỏ mệnh đề giải thích "luyện cho ai làm được việc gì" (§2c cấm ③)
    "подготовить": "chuẩn bị trước, huấn luyện",
}
