# -*- coding: utf-8 -*-
"""k09 — language::education: vật mang chữ (giấy, sách, báo, bảng) + đơn vị của
ngôn ngữ (chữ cái, từ vựng, nguyên thể) + hai gốc đẻ ra truyện: каз- (nói) và
образ- / -ня- (tạo hình, chiếm lấy).

Không có khối dùng chung: mỗi thẻ chỉ nói về chính từ của nó (README §3).
"""

S = {}
V = {}

S["буква"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">букв-</span>'
    '<span class="hd-gloss">CHỮ CÁI — gốc trơn, không chẻ nhỏ hơn được</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Neo bằng hai từ con: <b>буква́рь</b> là quyển sách dạy chữ đầu đời, '
    'còn <b>буква́льно</b> là “theo đúng từng chữ một” tức là theo nghĩa đen.</div>'
    '<div class="hd-why">Cách 2 số nhiều là <b>букв</b>, đuôi rỗng và <b>không</b> chèn thêm '
    'nguyên âm — vì <b>к</b> ở đây thuộc chính gốc từ, không phải hậu tố <b>-ка</b> như trong '
    '<b>ско́бка</b> (cách 2 số nhiều <b>ско́бок</b>).</div>'
    '<div class="hd-warn">Cặp phải thuộc khi tập viết: <b>прописна́я бу́ква</b> chữ hoa · '
    '<b>стро́чная бу́ква</b> chữ thường.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>буква́рь</b> sách vỡ lòng · <b>буква́льный</b> theo nghĩa đen · '
    '<b>буква́льно</b> đúng từng chữ</div>'
)

S["бумага"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бумаг-</span>'
    '<span class="hd-gloss">GIẤY — gốc trơn, không chẻ nhỏ hơn được</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là chỗ thấy rõ phép biến âm <b>г → ж</b> khi thêm hậu tố: '
    '<b>бума́га</b> giấy → <b>бума́жный</b> bằng giấy → <b>бума́жник</b> “cái đựng giấy tờ” '
    'tức là cái ví. Ba từ một dây, học một lần được cả ba.</div>'
    '<div class="hd-warn">Số nhiều <b>бума́ги</b> đổi hẳn nghĩa: không phải “nhiều tờ giấy” '
    'mà là <b>giấy tờ, hồ sơ</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бума́жный</b> bằng giấy · <b>бума́жка</b> mảnh giấy · '
    '<b>бума́жник</b> ví tiền</div>'
)

S["книга"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">книг-</span>'
    '<span class="hd-gloss">SÁCH — gốc trơn, không chẻ nhỏ hơn được</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cũng chạy phép biến âm <b>г → ж</b> như <b>бума́га</b>: '
    '<b>кни́га</b> → <b>кни́жка</b> quyển sổ nhỏ → <b>кни́жный</b> thuộc về sách. Cụm dùng '
    'hằng ngày: <b>кни́жный магази́н</b> hiệu sách.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кни́жка</b> quyển sổ, sách nhỏ · <b>кни́жный</b> thuộc về sách</div>'
)

S["скобка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">скоб-</span>'
    '<span class="hd-gloss">CÁI ĐAI, CÁI MÓC — từ <b>скоба́</b> thanh kim loại uốn cong</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-</span>'
    '<span class="hd-gloss">hậu tố thu nhỏ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái móc kim loại uốn cong ấy thu nhỏ lại thì đúng bằng hình dấu ngoặc '
    '— tên gọi đi thẳng từ hình dáng.</div>'
    '<div class="hd-why">Chú ý bảng chia: cách 2 số nhiều chèn thêm <b>о</b> → <b>ско́бок</b>, '
    'vì bỏ hết đuôi thì cụm <b>-бк</b> đứng cuối không đọc nổi. Mọi ô còn lại giữ trọng âm '
    'đứng yên ở <b>ско́-</b>.</div>'
    '<div class="hd-warn">Cụm hay gặp: <b>в ско́бках</b> trong ngoặc · '
    '<b>откры́ть ско́бку</b> mở ngoặc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>скоба́</b> cái đai, ghim kẹp</div>'
)

S["сказка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">tiền tố thể: làm cho việc nói thành trọn vẹn, gần như không thêm nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-каз-</span>'
    '<span class="hd-gloss">NÓI, CHỈ RA — cùng gốc với <b>сказа́ть</b> nói</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-а</span>'
    '<span class="hd-gloss">hậu tố biến việc làm thành VẬT: cái đã được kể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>сказа́ть</b> kể ra → <b>ска́зка</b> là cái được kể, và vì được kể '
    'nên có thể bịa: đó là truyện cổ tích. Cùng gốc <b>каз-</b> với <b>расска́з</b> trong lô '
    'này — <b>ска́зка</b> là chuyện tưởng tượng, <b>расска́з</b> là truyện kể đời thường.</div>'
    '<div class="hd-why">Chú ý bảng chia: cách 2 số nhiều chèn <b>о</b> → <b>ска́зок</b>; '
    'trọng âm không rời <b>ска́-</b> ở bất cứ ô nào.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сказа́ть</b> nói · <b>сказа́ние</b> truyền thuyết · '
    '<b>расска́з</b> truyện ngắn · <b>сказу́емое</b> vị ngữ</div>'
)

S["лексика"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">лекс-</span>'
    '<span class="hd-gloss">TỪ, LỜI — gốc Hy Lạp <i>lexis</i>, cùng nguồn với <i>lexicon</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ик-а</span>'
    '<span class="hd-gloss">hậu tố gọi tên CẢ MỘT MẢNG, không phải một cá thể: <b>грамма́тика</b>, <b>фи́зика</b>, <b>му́зыка</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ghép hai mảnh ra nghĩa đen: “kho từ” — toàn bộ vốn từ của một ngôn '
    'ngữ hay một người. Đuôi <b>-ика</b> báo ngay đây là danh từ giống cái và là tên gọi của '
    'cả một mảng, không phải một cá thể.</div>'
    '<div class="hd-warn">Bảng chia bên dưới vẫn in ra số nhiều, nhưng đây là danh từ tập hợp '
    'nên thực tế <b>chỉ dùng số ít</b>. Muốn nói “nhiều từ” thì dùng <b>слова́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лексико́н</b> vốn từ, tự vị · <b>лекси́ческий</b> thuộc từ vựng</div>'
)

S["доска"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">доск-</span>'
    '<span class="hd-gloss">TẤM VÁN — gốc trơn, không chẻ nhỏ hơn được</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc là tấm ván; cái bảng trong lớp chỉ là tấm ván sơn đen — '
    '<b>кла́ссная доска́</b>. Nhớ nghĩa “ván” trước thì nghĩa “bảng” tự suy ra.</div>'
    '<div class="hd-warn">Trọng âm CHẠY, phải để mắt: số ít nhấn đuôi (<b>доска́</b>, '
    '<b>доски́</b>, <b>доске́</b>) nhưng cách 4 lùi về gốc <b>до́ску</b>, và cả số nhiều cũng về '
    'gốc: <b>до́ски</b>, cách 2 <b>до́сок</b> (có chèn <b>о</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>доще́чка</b> tấm biển nhỏ · <b>доща́тый</b> đóng bằng ván '
    '(biến âm <b>ск → щ</b>)</div>'
)

S["открытка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">tiền tố MỞ RA, bỏ ra</span></div>'
    '<div class="hd-row"><span class="hd-piece">-кры-т-</span>'
    '<span class="hd-gloss">CHE, ĐẬY + đuôi bị động → “đã được mở”</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-а</span>'
    '<span class="hd-gloss">hậu tố NÉN cả cụm từ thành một chữ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc là cụm <b>откры́тое письмо́</b> “thư để ngỏ” — thư không phong bì, '
    'ai cũng đọc được. Cụm hai chữ bị nén lại bằng <b>-ка</b> thành <b>откры́тка</b>.</div>'
    '<div class="hd-why">Chú ý bảng chia: cách 2 số nhiều chèn <b>о</b> → <b>откры́ток</b>; '
    'trọng âm đứng yên ở <b>-кры́-</b> khắp bảng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>откры́ть</b> mở · <b>откры́тый</b> mở, để ngỏ · '
    '<b>закры́ть</b> đóng · <b>кры́ша</b> mái nhà (cái che)</div>'
)

S["ручка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рук- → руч-</span>'
    '<span class="hd-gloss">TAY — từ <b>рука́</b>, biến âm <b>к → ч</b> trước hậu tố</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-а</span>'
    '<span class="hd-gloss">hậu tố thu nhỏ: “cái tay nhỏ”, “thứ vừa tay”</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một mảnh nghĩa đẻ ra cả bốn nghĩa: thứ cầm vừa tay để viết là cây '
    '<b>bút</b>; chỗ đặt tay lên là <b>tay nắm</b> cửa hay <b>núm vặn</b>; còn tay của em bé '
    'thì đúng nghĩa đen là “bàn tay nhỏ”.</div>'
    '<div class="hd-warn">Cách 2 số nhiều là <b>ру́чек</b> — chèn <b>е</b> chứ không phải '
    '<b>о</b> như <b>ско́бок</b> hay <b>ска́зок</b>, vì đứng ngay trước là chữ rít <b>ч</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рука́</b> tay · <b>ручно́й</b> làm bằng tay · '
    '<b>рука́в</b> tay áo · <b>ру́копись</b> bản thảo viết tay</div>'
)

S["газета"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">газет-</span>'
    '<span class="hd-gloss">từ mượn châu Âu, cùng nguồn với <i>gazette</i> tiếng Anh</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi có sẵn của từ gốc, khớp luôn với danh từ giống cái tiếng Nga</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mượn nguyên khối nên không chẻ sâu hơn được: chỉ cần nhớ trọng âm rơi '
    'vào giữa — <b>газе́та</b> — và giữ nguyên ở mọi ô của bảng chia.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>газе́тный</b> thuộc về báo · <b>газе́тчик</b> người bán báo, '
    'nhà báo</div>'
)

S["инфинитив"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ин-</span>'
    '<span class="hd-gloss">tiền tố Latin phủ định: KHÔNG (như <i>in</i>-visible)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-финит-</span>'
    '<span class="hd-gloss">GIỚI HẠN, KẾT THÚC — cùng gốc <i>final</i>, <i>finish</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ив</span>'
    '<span class="hd-gloss">đuôi danh từ mượn Latin, hút trọng âm về chính nó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen là “dạng KHÔNG bị giới hạn”: không chia ngôi, không chia số, '
    'không chia thì. Trong tiếng Nga đó là dạng đuôi <b>-ть</b> ghi trong từ điển.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">Cùng đuôi <b>-и́в</b>, nhóm mượn Latin này đều nhấn vào chính nó: <b>моти́в</b> '
    'động cơ · <b>акти́в</b> tài sản · <b>объекти́в</b> ống kính · <b>детекти́в</b> thám tử</div>'
)

S["образование"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">образ-</span>'
    '<span class="hd-gloss">HÌNH ẢNH, HÌNH DẠNG — từ <b>о́браз</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-</span>'
    '<span class="hd-gloss">hậu tố động từ: LÀM CHO thành, tạo ra</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ние</span>'
    '<span class="hd-gloss">biến động từ thành danh từ, và luôn là giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen là “sự tạo hình”. Với vật chất thì đó là <b>sự hình thành</b>; '
    'với con người thì tạo hình chính là dạy dỗ — nên cùng một từ cũng có nghĩa '
    '<b>giáo dục, học vấn</b>.</div>'
    '<div class="hd-warn">Cụm phải thuộc: <b>вы́сшее образова́ние</b> học vấn bậc đại học · '
    '<b>получи́ть образова́ние</b> được ăn học.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>о́браз</b> hình ảnh · <b>образова́ть</b> tạo thành · '
    '<b>образо́ванный</b> có học · <b>образе́ц</b> mẫu, khuôn</div>'
)

S["занятие"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">tiền tố CHIẾM LẤY, phủ kín</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ня-</span>'
    '<span class="hd-gloss">LẤY, CẦM — cùng gốc với <b>заня́ть</b> chiếm chỗ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тие</span>'
    '<span class="hd-gloss">biến động từ thành danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen là “cái chiếm lấy thời gian của bạn” — từ đó ra cả ba nghĩa: '
    'buổi học, hoạt động đang làm, và nghề nghiệp. Cùng gốc với <b>за́нят</b> “tôi đang bận”.</div>'
    '<div class="hd-warn">Động từ cùng gốc <b>занима́ться</b> (học, luyện tập) đòi <b>cách 5</b>: '
    '<b>занима́ться спо́ртом</b> chơi thể thao · <b>занима́ться ру́сским языко́м</b> học tiếng Nga.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>заня́ть</b> chiếm · <b>за́нят</b> bận · <b>занима́ться</b> học, luyện '
    '· <b>за́нятость</b> việc làm</div>'
)

S["колледж"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mượn nguyên khối từ <i>college</i> nên <b>không chẻ ra mảnh nào</b> trong '
    'tiếng Nga. Nghe gần như tiếng Anh, chỉ có hai chỗ dễ sai: giữ đủ <b>hai chữ л</b> và đặt trọng '
    'âm ở âm đầu — <b>ко́лледж</b>.</div>'
    '<div class="hd-warn">Ở Nga <b>ко́лледж</b> là trường nghề / trung cấp học sau phổ thông, '
    '<b>không</b> phải bậc đại học. Đại học là <b>университе́т</b> hoặc <b>институ́т</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>колле́га</b> đồng nghiệp — cùng gốc Latin <i>collegium</i> “hội đoàn”</div>'
)

S["рассказ"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рас-</span>'
    '<span class="hd-gloss">tiền tố TẢN RA, ra khắp lượt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-каз</span>'
    '<span class="hd-gloss">NÓI, CHỈ RA — cùng gốc với <b>сказа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">(đuôi rỗng)</span>'
    '<span class="hd-gloss">danh từ dựng thẳng từ động từ, không thêm hậu tố; kết thúc bằng phụ âm cứng nên là giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>рассказа́ть</b> kể ra cho khắp lượt → <b>расска́з</b> là cái được kể: '
    'một câu chuyện, và trong văn học là truyện ngắn.</div>'
    '<div class="hd-why">Cùng gốc <b>каз-</b> với <b>ска́зка</b> trong lô này, nhưng chia việc rõ: '
    '<b>ска́зка</b> là chuyện cổ tích bịa ra, <b>расска́з</b> là chuyện kể lại.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рассказа́ть</b> kể · <b>расска́зчик</b> người kể · '
    '<b>сказа́ть</b> nói · <b>указа́тель</b> biển chỉ đường, mục lục</div>'
)

# ---- §2c: đề bài deck 1-go — chỉ sửa từ thật sự thiếu nghĩa -----------------
# `образование` gloss tiếng Anh là "education / formation" nhưng dòng cũ chỉ có
# phần "education"; thiếu hẳn nghĩa "sự hình thành" mà chính gloss xác nhận.
V["образование"] = "giáo dục, học vấn, sự hình thành"
