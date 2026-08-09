# -*- coding: utf-8 -*-
"""k70 — tu-moi: 14 từ user vừa thêm, KHÔNG cùng họ nhau.

Không có trục chung, và cố ý không có khối hệ thống dùng chung: mỗi thẻ chỉ nói
đúng phần của chính từ đó. Hai chỗ giao nhau nằm trọn trong lô nên được xử lý
cả hai phía: спать ↔ спа́льня (cùng gốc сп-) và конце́рт ↔ спекта́кль (nghĩa sát
nhau — mỗi thẻ tự phân biệt lấy một câu, không dựng bảng chung).
"""

# 🔴 KHÔNG dựng biến khối dùng chung (HE/LUAT/THE…) rồi cộng vào mọi thẻ.

S = {}
V = {}

# ------------------------------------------------------------------- ви́рус
S["вирус"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn nguyên khối từ Latin '
    '<i>virus</i> (chất độc, nọc), vào tiếng Nga qua đường sách vở nên giữ '
    'nguyên hình, chỉ thêm đuôi cách vào sau.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen Latin là <i>chất độc</i>. Tiếng Nga dùng '
    'chung một từ cho vi-rút sinh học và vi-rút máy tính, y như tiếng Việt. '
    'Chia theo mẫu chuẩn giống đực, trọng âm đứng yên ở <b>ви́</b>- suốt bảng '
    'nên không có gì phải nhớ thêm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ви́русный</b> thuộc về vi-rút · '
    '<b>антиви́рус</b> phần mềm diệt vi-rút</div>'
)

# -------------------------------------------------------------- занима́ться
S["заниматься"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">tiền tố: chiếm lấy, bắt vào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-нима-</span>'
    '<span class="hd-gloss">gốc LẤY, CHIẾM (như <b>заня́ть</b> chiếm chỗ)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">phản thân: làm cho CHÍNH MÌNH</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ghép lại đúng nghĩa đen: <i>tự chiếm lấy mình bằng '
    'việc gì</i> → dành thời gian cho việc đó. Chưa hoàn thành; bạn cùng cặp '
    'hoàn thành là <b>заня́ться</b> (bắt tay vào).</div>'
    '<div class="hd-warn">⚠️ Việc làm phải ở <b>cách 5</b>, không có giới từ: '
    '<b>занима́ться спо́ртом</b> tập thể thao · <b>занима́ться му́зыкой</b> học '
    'nhạc. Nhớ sai cách là câu hỏng.</div>'
    '<div class="hd-warn">⚠️ Đừng lẫn với <b>рабо́тать</b>: занима́ться là bỏ '
    'thời gian ra làm/học một việc, còn рабо́тать là đi làm kiếm sống hoặc máy '
    'móc đang chạy.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>заня́тие</b> buổi học, hoạt động · '
    '<b>за́нятый</b> bận · <b>заня́ть</b> chiếm, mượn</div>'
)

# -------------------------------------------------------------- инструме́нт
S["инструмент"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ theo lối Nga được: mượn nguyên khối từ '
    'Latin <i>instrumentum</i> (đồ nghề), dựng từ <i>in-struere</i> xếp vào, '
    'dựng lên. Chỉ còn nhận ra được cái đuôi <b>-ме́нт</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng ổ với <i>instrument</i> tiếng Anh nên nghĩa tự '
    'đoán ra: đồ nghề của thợ, dụng cụ đo, và nhạc cụ. Đuôi mượn <b>-ме́нт</b> '
    'kéo theo hai điều đều đúng cho cả loạt: từ mang giống ĐỰC, và trọng âm '
    'rơi đúng vào <b>-ме́нт</b>, đứng yên suốt bảng.</div>'
    '<div class="hd-warn">⚠️ Nhạc cụ nói đủ là <b>музыка́льный инструме́нт</b> '
    '— <b>фле́йта</b> là một инструме́нт; đứng trơ một mình thì '
    '<b>инструме́нт</b> thường được hiểu là đồ nghề của thợ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">Cùng đuôi mượn -ме́нт: <b>докуме́нт</b> tài liệu · '
    '<b>моме́нт</b> khoảnh khắc</div>'
)

# ----------------------------------------------------------------- конце́рт
S["концерт"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được trong tiếng Nga: mượn nguyên khối từ '
    'tiếng Ý <i>concerto</i>, gốc Latin <i>con-</i> (cùng) + <i>certare</i> '
    '(đua, tranh tài).</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc là <i>cùng đua tài với nhau</i> — người độc '
    'tấu đua với dàn nhạc. Vì thế tiếng Nga giữ cả hai nghĩa trong một từ: '
    'buổi diễn nhạc, và bản nhạc viết cho nhạc cụ độc tấu với dàn nhạc.</div>'
    '<div class="hd-warn">⚠️ Buổi diễn thì đi với <b>на</b>, không dùng '
    '<b>в</b>: đi tới thì <b>на конце́рт</b> (cách 4), đang ở đó thì '
    '<b>на конце́рте</b> (cách 6).</div>'
    '<div class="hd-warn">⚠️ <b>конце́рт</b> là buổi diễn ÂM NHẠC; buổi diễn có '
    'diễn viên đóng vai (kịch, ba-lê) là <b>спекта́кль</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>конце́ртный</b> thuộc buổi hoà nhạc '
    '(конце́ртный зал phòng hoà nhạc)</div>'
)

# ------------------------------------------------------------------ кре́сло
S["кресло"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">крес-</span>'
    '<span class="hd-gloss">gốc cổ, nay không còn nghĩa riêng đứng một mình</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ло</span>'
    '<span class="hd-gloss">hậu tố tạo danh từ chỉ ĐỒ VẬT, luôn giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái đuôi <b>-ло</b> mới là chỗ đáng nhớ: nó nặn ra tên '
    'đồ vật và kéo theo giống trung, gặp lại ở <b>мы́ло</b> (xà phòng), '
    '<b>весло́</b> (mái chèo). Gốc <i>крес-</i> thì tra từ nguyên còn cãi nhau, '
    'đừng cố tìm nghĩa cho nó.</div>'
    '<div class="hd-warn">⚠️ Nguyên âm chạy ở số nhiều cách 2: chèn thêm '
    '<b>-е-</b> → <b>пять кре́сел</b> năm cái ghế bành (không phải кре́слов).</div>'
    '<div class="hd-warn">⚠️ Ba cái ghế đừng lẫn: <b>кре́сло</b> một chỗ ngồi CÓ '
    'TAY VỊN · <b>стул</b> ghế tựa không tay vịn · <b>дива́н</b> ghế dài nhiều '
    'chỗ.</div>'
)

# ------------------------------------------------------------------ ме́бель
S["мебель"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn tiếng Pháp <i>meuble</i>, gốc '
    'Latin <i>mobilis</i> — thứ DI CHUYỂN ĐƯỢC.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng ổ với <i>mobile</i> tiếng Anh: đồ đạc là phần '
    'khiêng đi được của căn nhà, khác với tường và sàn gắn liền đất. ⚠️ Đuôi '
    '<b>-ь</b> KHÔNG cho biết giống: từ này giống CÁI (<b>ме́бель</b> но́вая), '
    'trong khi <b>спекта́кль</b> đuôi y hệt lại là giống đực — mỗi từ đuôi -ь '
    'phải nhớ giống riêng.</div>'
    '<div class="hd-warn">⚠️ Đây là từ gộp cả đống, KHÔNG có số nhiều và không '
    'đếm được: muốn nói "hai món đồ" phải mượn từ đếm — '
    '<b>два предме́та ме́бели</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ме́бельный</b> thuộc về đồ nội thất '
    '(ме́бельный магази́н cửa hàng nội thất)</div>'
)

# -------------------------------------------------------------------- пляж
S["пляж"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn tiếng Pháp <i>plage</i>, gốc '
    'Latin <i>plagia</i> (dải bờ thoai thoải). Cùng ổ với <i>playa</i> tiếng '
    'Tây Ban Nha.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chia theo mẫu chuẩn giống đực, nhưng để ý cách 5: sau '
    'chữ <b>ж</b> mà trọng âm không rơi vào đuôi thì viết <b>-ем</b> chứ không '
    '-ом → <b>пля́жем</b>. Luật chính tả này lặp lại sau ж, ш, ч, щ, ц.</div>'
    '<div class="hd-warn">⚠️ Bãi biển đi với <b>на</b>: ra bãi là '
    '<b>на пляж</b> (cách 4), đang ở ngoài bãi là <b>на пля́же</b> (cách 6). '
    'Còn <b>мо́ре</b> là chính cái biển, <b>пляж</b> chỉ là dải cát ven bờ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пля́жный</b> thuộc bãi biển '
    '(пля́жный волейбо́л bóng chuyền bãi biển)</div>'
)

# ----------------------------------------------------------------- спа́льня
S["спальня"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">спа-</span>'
    '<span class="hd-gloss">gốc NGỦ, lấy thẳng từ <b>спать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-льн-</span>'
    '<span class="hd-gloss">hậu tố "dùng để…", có sẵn ở tính từ спа́льный</span></div>'
    '<div class="hd-row"><span class="hd-piece">-я</span>'
    '<span class="hd-gloss">đuôi ⇒ danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đọc thẳng ra nghĩa: <i>(phòng) dùng để ngủ</i>. Trọng '
    'âm bám gốc <b>спа́</b>- suốt bảng, không chạy đi đâu.</div>'
    '<div class="hd-warn">⚠️ Số nhiều cách 2 gãy khuôn: dấu mềm rụng và chèn '
    '<b>-е-</b> vào giữa → <b>мно́го спа́лен</b> nhiều phòng ngủ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>спать</b> ngủ · <b>спа́льный</b> để ngủ '
    '(спа́льный мешо́к túi ngủ)</div>'
)

# ------------------------------------------------------------------- спать
S["спать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сп-</span>'
    '<span class="hd-gloss">gốc NGỦ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">đuôi nguyên thể, ở đây KHÔNG báo lớp chia</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nguyên thể đuôi -ать mà lại chia theo lớp 2 '
    '(спишь, спит, спят) — chỗ này phải nhớ riêng. Ngôi "tôi" chèn thêm '
    '<b>-л-</b>: <b>сплю</b>. Đó là luật chung cho gốc kết thúc bằng п, б, в, '
    'м, ф, gặp lại ở люби́ть → люблю́.</div>'
    '<div class="hd-warn">⚠️ Quá khứ dịch trọng âm ở đúng dạng giống cái: '
    'спал · <b>спала́</b> · спа́ло · спа́ли.</div>'
    '<div class="hd-warn">⚠️ "Đi ngủ" không phải спать: động tác lên giường là '
    '<b>ложи́ться спать</b>. Riêng <b>спать</b> chỉ tả trạng thái đang ngủ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>спа́льня</b> phòng ngủ · <b>поспа́ть</b> ngủ một lát '
    '· <b>вы́спаться</b> ngủ đẫy giấc</div>'
)

# --------------------------------------------------------------- спекта́кль
S["спектакль"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn tiếng Pháp <i>spectacle</i>, gốc '
    'Latin <i>spectare</i> — NGẮM, XEM. Đứng một mình trong tiếng Nga, không '
    'đẻ ra họ từ nào nên thẻ này không có mục Họ hàng.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng ổ với <i>spectacle</i>, <i>spectator</i> tiếng '
    'Anh: спекта́кль là thứ dựng ra để NGƯỜI TA NGẮM, tức buổi diễn trên sân '
    'khấu có diễn viên đóng vai. ⚠️ Đuôi <b>-ь</b> ở từ này là giống ĐỰC '
    '(интере́сный спекта́кль), đừng suy giống từ cái đuôi.</div>'
    '<div class="hd-warn">⚠️ Đi xem kịch là <b>на спекта́кль</b> (cách 4), đang '
    'xem là <b>на спекта́кле</b> (cách 6). Buổi diễn thuần âm nhạc thì là '
    '<b>конце́рт</b>, không gọi là спекта́кль.</div>'
)

# ----------------------------------------------------------------- таре́лка
S["тарелка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">тарел-</span>'
    '<span class="hd-gloss">gốc mượn, có sẵn ở dạng cũ таре́ль</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">hậu tố vốn chỉ vật nhỏ, nay đã thành dạng thường</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">⚠️ Mức tin: đây là từ nguyên, không phải luật suy ra '
    'được — các từ điển cho rằng từ này vào tiếng Nga qua tiếng Đức '
    '<i>Teller</i> (cái đĩa), và một trong hai chữ <i>l</i> của nguồn đã đổi thành <i>р</i>, cho dạng Nga cũ таре́ль. Nhớ '
    'được thì rẻ, không nhớ cũng không mất gì.</div>'
    '<div class="hd-warn">⚠️ Nguyên âm chạy ở số nhiều cách 2: chèn '
    '<b>-о-</b> → <b>пять таре́лок</b> năm cái đĩa.</div>'
    '<div class="hd-warn">⚠️ Thành ngữ phải thuộc: <b>не в свое́й таре́лке</b> '
    '— thấy lạc lõng, không thoải mái, như bị đặt nhầm chỗ.</div>'
)

# ------------------------------------------------------------------ фле́йта
S["флейта"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">флейт-</span>'
    '<span class="hd-gloss">gốc mượn nguyên khối</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi ⇒ danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vào tiếng Nga từ các thứ tiếng châu Âu (Đức <i>Flöte</i>, Hà Lan <i>fluit</i>), cùng ổ với '
    '<i>flute</i> tiếng Anh; nhiều từ điển nối cả ổ này về Latin <i>flare</i> THỔI — nhạc cụ dùng hơi '
    'để thổi. Chia theo mẫu chuẩn giống cái, trọng âm đứng yên.</div>'
    '<div class="hd-warn">⚠️ Chơi nhạc cụ luôn là <b>игра́ть на</b> + cách 6: '
    '<b>игра́ть на фле́йте</b>, đúng khuôn với игра́ть на гита́ре.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>флейти́ст</b> người thổi sáo — cùng khuôn -и́ст '
    'với <b>гитари́ст</b> người chơi ghi-ta</div>'
)

# ---------------------------------------------------------------- футбо́лка
S["футболка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">футбол-</span>'
    '<span class="hd-gloss">gốc BÓNG ĐÁ (<b>футбо́л</b>, mượn từ football)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-</span>'
    '<span class="hd-gloss">hậu tố rút cả cụm áo bóng đá thành MỘT từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi ⇒ danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen là <i>áo kiểu bóng đá</i> — cái áo cầu thủ '
    'mặc ra sân, sau lan ra thành áo phông bất kỳ. Trọng âm nằm ở gốc '
    '<b>-бо́л</b> và không nhúc nhích.</div>'
    '<div class="hd-warn">⚠️ Nguyên âm chạy ở số nhiều cách 2: chèn '
    '<b>-о-</b> → <b>пять футбо́лок</b> năm cái áo phông.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>футбо́л</b> bóng đá · <b>футболи́ст</b> cầu thủ '
    'bóng đá</div>'
)

# ----------------------------------------------------------------- экза́мен
S["экзамен"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn nguyên khối từ Latin '
    '<i>examen</i> — cái kim của bàn cân, rồi thành sự cân nhắc, sát hạch.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng ổ với <i>exam</i>, <i>examine</i> tiếng Anh, và '
    'hình ảnh gốc vẫn dùng được: kỳ thi là lúc kiến thức bị đem lên bàn cân. '
    'Chia theo mẫu chuẩn giống đực, trọng âm đứng yên ở <b>-за́-</b>.</div>'
    '<div class="hd-warn">⚠️ Chỗ đắt nhất của từ này: đổi thể là đổi hẳn nghĩa. '
    '<b>сдава́ть экза́мен</b> = ĐI THI, chưa biết đỗ hay trượt · '
    '<b>сдать экза́мен</b> = THI ĐỖ. Trượt thì nói '
    '<b>провали́ть экза́мен</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>экзамена́тор</b> giám khảo · '
    '<b>экзаменова́ть</b> sát hạch, hỏi thi</div>'
)

# =====================================================================
# FIELD TIẾNG VIỆT (đề bài deck 1-go) — README §2c.
# Chỉ khai từ nào THẬT SỰ cần sửa; 11 từ còn lại của lô giữ nguyên.

# cũ: "học tập, tập luyện, làm việc, bận rộn với cái gì đó"
#   · "làm việc" trùng nguyên cụm với рабо́тать "làm việc, đi làm, chạy,
#     hoạt động", mà cả hai đều là v·IMPF nên badge không tách được ⇒ bỏ.
#   · "bận rộn với cái gì đó" là LỜI GIẢI THÍCH cách dùng, §2c cấm ⇒ bỏ.
#   · Thay bằng "chuyên tâm" — đúng phần nghĩa "to be engaged in" của gloss.
V["заниматься"] = "học tập, tập luyện, chuyên tâm"

# cũ: "buổi hòa nhạc" — thiếu hẳn nghĩa thứ hai mà gloss tiếng Anh có
# ("concerto"): bản nhạc cho nhạc cụ độc tấu với dàn nhạc.
# KHÔNG thêm "buổi biểu diễn" chung chung: cụm đó để dành cho спекта́кль.
V["концерт"] = "buổi hòa nhạc, bản concerto"

# cũ: "kỳ thi, bài kiểm tra" — "bài kiểm tra" trùng nguyên cụm với зачёт và
# тест (cả ba đều n·MASC, badge không tách được). экза́мен là SỰ KIỆN sát
# hạch, không phải tờ đề, nên trả cụm "bài kiểm tra" về cho hai từ kia.
V["экзамен"] = "kỳ thi, kỳ sát hạch"
