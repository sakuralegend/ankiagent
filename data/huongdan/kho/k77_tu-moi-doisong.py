# -*- coding: utf-8 -*-
"""k77 — từ mới đời sống: user vừa thêm, các từ KHÔNG cùng một họ.

Không ép một trục chung — mỗi thẻ soạn độc lập. Ba chỗ phải nhất quán với thẻ đã
có trong kho: cặp `вставлять`↔`вставить` (và phải tách khỏi `вставать/встать`
«đứng dậy»), bộ đuôi quốc tịch `-ец/-ка` đã dạy ở `немец/немка`, và gốc `-говор-`
nối `разговорить` với `говорить/поговорить/разговаривать`.
"""

S = {}

# ----------------------------------------------------------------- вилка
S["вилка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вил-</span>'
    '<span class="hd-gloss">gốc <b>ви́лы</b> — cái chĩa, cái nạng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">hậu tố NHỎ, kéo theo giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái chĩa <b>ви́лы</b> thu nhỏ lại rồi đặt lên bàn ăn thì '
    'thành cái nĩa. Phích cắm điện cũng gọi là <b>ви́лка</b>, vì hai chấu của nó '
    'chìa ra y như hai răng nĩa.</div>'
    '<div class="hd-warn">Cách 2 số nhiều chèn thêm <b>-о-</b> cho khỏi dính ba phụ '
    'âm: <b>ви́лка → ви́лок</b>. Cùng luật nguyên âm chạy với <b>ло́жка → ло́жек</b>.</div>'
)

# ------------------------------------------------------------- вставлять
S["вставлять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO, vào bên trong</span></div>'
    '<div class="hd-row"><span class="hd-piece">-став-</span>'
    '<span class="hd-gloss">gốc ĐẶT (như <b>поста́вить</b> đặt, để)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ля́ть</span>'
    '<span class="hd-gloss">hậu tố kéo dài → thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đặt (<b>-став-</b>) một vật VÀO (<b>в-</b>) bên trong cái gì '
    'đó = cắm, chèn, nhét vào. Hậu tố <b>-ля-</b> kéo việc ấy dài ra thành quá trình '
    'đang diễn ra.</div>'
    '<div class="hd-warn">Cặp thể: <b>вставля́ть</b> là đang/thường cắm, còn '
    '<b>вста́вить</b> là cắm xong một lần — <b>Вставь ключ в замо́к</b> = Cắm chìa '
    'vào ổ khoá đi.</div>'
    '<div class="hd-warn">Đừng lẫn với <b>встава́ть / встать</b> «đứng dậy»: bộ này '
    'luôn cần TÂN NGỮ (cắm CÁI GÌ vào), còn <b>встать</b> là tự mình đứng lên, không '
    'có tân ngữ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вста́вить</b> cắm vào (một lần) · <b>поста́вить</b> đặt, để</div>'
)

# ------------------------------------------------------------ иностранец
S["иностранец"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ино-</span>'
    '<span class="hd-gloss">KHÁC, thuộc về cái khác</span></div>'
    '<div class="hd-row"><span class="hd-piece">-стран-</span>'
    '<span class="hd-gloss">gốc <b>страна́</b> — đất nước</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ец</span>'
    '<span class="hd-gloss">hậu tố NGƯỜI, giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người của một đất nước KHÁC. Vẫn đúng bộ đuôi quốc tịch đã '
    'học: <b>не́мец</b> người Đức, <b>не́мка</b> phụ nữ Đức — chỉ thay phần gốc phía '
    'trước là ra từ mới.</div>'
    '<div class="hd-warn">Chữ <b>е</b> trong <b>-ец</b> rơi mất ngay khi thêm đuôi: '
    '<b>иностра́нец → иностра́нца, иностра́нцы</b>. Y hệt <b>не́мец → не́мца</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>иностра́нка</b> phụ nữ nước ngoài · <b>иностра́нный</b> '
    'thuộc nước ngoài · <b>страна́</b> đất nước</div>'
)

# ------------------------------------------------------------ иностранка
S["иностранка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ино-</span>'
    '<span class="hd-gloss">KHÁC, thuộc về cái khác</span></div>'
    '<div class="hd-row"><span class="hd-piece">-стран-</span>'
    '<span class="hd-gloss">gốc <b>страна́</b> — đất nước</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">hậu tố NGƯỜI, giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng một thân với <b>иностра́нец</b>, chỉ đổi đuôi <b>-ец</b> '
    '(nam) sang <b>-ка</b> (nữ) — đúng cặp <b>не́мец / не́мка</b> đã học.</div>'
    '<div class="hd-warn">Ngược chiều với <b>иностра́нец</b>: ở đây nguyên âm CHÈN '
    'THÊM chứ không rơi — cách 2 số nhiều là <b>иностра́нок</b>, cùng luật nguyên '
    'âm chạy với <b>ло́жка → ло́жек</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>иностра́нец</b> người nước ngoài (nam) · '
    '<b>иностра́нный</b> thuộc nước ngoài · <b>страна́</b> đất nước</div>'
)

# --------------------------------------------------------------- круглый
S["круглый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">круг-</span>'
    '<span class="hd-gloss">gốc <b>круг</b> — vòng tròn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лый</span>'
    '<span class="hd-gloss">hậu tố + đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái gì mang hình <b>круг</b> thì là <b>кру́глый</b>. Hậu tố '
    '<b>-л-</b> biến danh từ thành tính từ chỉ hình dạng, rồi <b>-ый</b> là đuôi tính '
    'từ giống đực quen thuộc.</div>'
    '<div class="hd-warn">Dạng ngắn chỉ mình giống cái đẩy trọng âm ra đuôi: '
    '<b>кругл · кругла́ · кру́гло · кру́глы</b>.</div>'
    '<div class="hd-warn">Cụm phải thuộc: <b>кру́глый год</b> = quanh năm suốt tháng · '
    '<b>кру́глые су́тки</b> = suốt ngày đêm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>круг</b> vòng tròn, hình tròn</div>'
)

# ------------------------------------------------------------- объявлять
S["объявлять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">объ-</span>'
    '<span class="hd-gloss">об- «ra khắp xung quanh» + dấu cứng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-яв-</span>'
    '<span class="hd-gloss">gốc LỘ RA, hiện ra</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ля́ть</span>'
    '<span class="hd-gloss">hậu tố → thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm cho một điều LỘ RA (<b>-яв-</b>) khắp xung quanh '
    '(<b>об-</b>) = công bố. Phải có dấu cứng vì tiền tố kết thúc bằng phụ âm mà gốc '
    'lại mở đầu bằng <b>я</b>.</div>'
    '<div class="hd-warn">Sắc thái: đây là thông báo CHÍNH THỨC — nhà nước, toà án, '
    'bác sĩ, loa sân bay. Chuyện của riêng mình thì dùng <b>сказа́ть</b>.</div>'
    '<div class="hd-warn">Cặp thể: <b>объявля́ть</b> là việc thường làm, '
    '<b>объяви́ть</b> là công bố xong một lần.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>объяви́ть</b> công bố (một lần) · <b>объявле́ние</b> bản '
    'thông báo, mẩu rao vặt</div>'
)

# ------------------------------------------------------------ по-другому
S["по-другому"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố tạo trạng từ chỉ CÁCH THỨC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-друго́му</span>'
    '<span class="hd-gloss">cách 3 của <b>друго́й</b> — khác</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng khuôn <b>по-ру́сски</b> đã học: <b>по-</b> cộng một đuôi '
    'biến cách đóng băng thì ra trạng từ chỉ cách thức. Nghĩa đen «theo cái khác» → '
    'làm khác đi, theo cách khác.</div>'
    '<div class="hd-warn">Luôn viết có GẠCH NỐI, và cả khuôn <b>по-</b>…<b>-ому</b> '
    'đều thế: <b>по-но́вому</b> theo lối mới, <b>по-мо́ему</b> theo ý tôi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>друго́й</b> khác · <b>по-ру́сски</b> bằng tiếng Nga (cùng '
    'khuôn <b>по-</b>)</div>'
)

# -------------------------------------------------------------- подумать
S["подумать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">«một lượt, một chút» → thể hoàn thành</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ду́мать</span>'
    '<span class="hd-gloss">gốc <b>ду́мать</b> — nghĩ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>по-</b> ở đây không đổi nghĩa gốc, nó chỉ đóng gói việc '
    'nghĩ thành MỘT lượt có điểm dừng: nghĩ một lát rồi thôi, hoặc cân nhắc xong một '
    'lần.</div>'
    '<div class="hd-warn">Cách nó đòi: nghĩ VỀ ai/cái gì thì <b>об</b> + cách 6 — '
    '<b>Я поду́маю об э́том</b>. Nghĩ nát óc về một việc khó thì <b>над</b> + cách 5.</div>'
    '<div class="hd-warn">Câu cửa miệng: <b>Я поду́маю</b> = «Để tôi nghĩ đã» — lời từ '
    'chối lịch sự, không phải lời hứa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ду́мать</b> nghĩ (thể chưa hoàn thành)</div>'
)

# --------------------------------------------------------------- полезно
S["полезно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">поле́з-</span>'
    '<span class="hd-gloss">gốc <b>по́льза</b> — lợi ích</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-</span>'
    '<span class="hd-gloss">hậu tố tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>по́льза</b> là lợi ích. Thêm <b>-н-</b> ra tính từ '
    '<b>поле́зный</b> «có ích» (chữ <b>ь</b> nhả thành <b>е</b>), đổi đuôi sang '
    '<b>-о</b> thì thành lời nhận xét: «(việc đó) có ích».</div>'
    '<div class="hd-warn">Là VỊ NGỮ VÔ NHÂN XƯNG, câu không có chủ ngữ: <b>Ходи́ть '
    'пешко́м поле́зно</b> = Đi bộ thì tốt. Người hưởng lợi đứng ở CÁCH 3, y như '
    '<b>ну́жно</b>: <b>Э́то поле́зно де́тям</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поле́зный</b> có ích · <b>испо́льзовать</b> sử dụng</div>'
)

# --------------------------------------------------------------- рабочий
S["рабочий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рабо́ч-</span>'
    '<span class="hd-gloss">gốc <b>рабо́та</b> việc làm (т → ч)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span>'
    '<span class="hd-gloss">đuôi TÍNH TỪ, không phải đuôi danh từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vốn là tính từ «thuộc về việc làm» — <b>рабо́чий день</b> ngày '
    'làm việc. Đứng trơ một mình, không kèm danh từ nào, thì nó tự thành danh từ '
    '«người làm» = công nhân.</div>'
    '<div class="hd-warn">Là danh từ nhưng CHIA THEO MẪU TÍNH TỪ: <b>рабо́чего, '
    'рабо́чему, рабо́чим, рабо́чие</b>. Cùng kiểu với <b>ру́сский</b> khi nó nghĩa «một '
    'người Nga».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рабо́та</b> công việc · <b>рабо́тать</b> làm việc</div>'
)

# ----------------------------------------------------------- разговорить
S["разговорить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раз-</span>'
    '<span class="hd-gloss">BUNG RA, mở tung ra</span></div>'
    '<div class="hd-row"><span class="hd-piece">-говор-</span>'
    '<span class="hd-gloss">gốc NÓI (như <b>говори́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi động từ, thể hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>раз-</b> là bung ra. Bung cái sự nói của NGƯỜI KHÁC ra: gỡ '
    'cho một người đang lầm lì chịu mở miệng. Bạn là chủ ngữ, người chịu nói là tân '
    'ngữ.</div>'
    '<div class="hd-warn">Từ hiếm. Cái bạn gặp hằng ngày là <b>разгова́ривать</b> «trò '
    'chuyện» — tự mình nói chuyện với ai đó, khác hẳn nghĩa «gỡ cho người ta nói» ở '
    'đây.</div>'
    '<div class="hd-warn">Kéo dài thể thì <b>о</b> trong gốc đổi thành <b>а</b>: '
    '<b>разговори́ть → разгова́ривать</b>. Hậu tố <b>-ива-</b> luôn kéo trọng âm về '
    'ngay trước nó.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>говори́ть</b> nói · <b>поговори́ть</b> nói chuyện một lát · '
    '<b>разгова́ривать</b> trò chuyện</div>'
)

# ------------------------------------------------------------- серьёзный
S["серьёзный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">серьёз-</span>'
    '<span class="hd-gloss">mượn tiếng Pháp <i>sérieux</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ный</span>'
    '<span class="hd-gloss">đuôi Nga hoá từ mượn thành tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không có gốc Nga nào để chẻ sâu hơn: phần <b>серьёз-</b> là '
    'chữ mượn, nhận mặt thẳng qua tiếng Anh <i>serious</i>. Đuôi <b>-ный</b> là khuôn '
    'quen để biến từ mượn thành tính từ Nga.</div>'
    '<div class="hd-warn">Hai chỗ dễ viết sai: phải có <b>ь</b> sau <b>р</b>, và phải '
    'là <b>ё</b> chứ không phải <b>е</b>. Vì <b>ё</b> tự mang trọng âm nên từ này '
    'không bao giờ có dấu sắc.</div>'
    '<div class="hd-warn">Dạng ngắn giống đực chèn thêm <b>-е-</b>: <b>серьёзен</b>, '
    'còn lại đều đặn <b>серьёзна · серьёзно · серьёзны</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>серьёзно</b> một cách nghiêm túc — trạng từ, viết y hệt dạng ngắn giống trung</div>'
)

# -------------------------------------------------------------- спагетти
S["спагетти"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn nguyên xi tiếng Ý <i>spaghetti</i>, vốn '
    'là số nhiều của <i>spaghetto</i> «sợi dây con». Tiếng Nga bê cả vỏ, không thêm '
    'đuôi Nga nào.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhận mặt thẳng qua tiếng Anh <i>spaghetti</i>; chữ Nga chỉ là '
    'phiên tự. Đúng lớp từ mượn kết thúc bằng nguyên âm mà tiếng Nga không chịu '
    'bẻ.</div>'
    '<div class="hd-warn">KHÔNG BIẾN CÁCH: cả mười hai ô trong bảng đều là '
    '<b>спаге́тти</b>, đứng ở cách nào cũng vậy — cùng lớp với <b>метро́</b> và '
    '<b>кино́</b> đã học.</div>'
)

# --------------------------------------------------------------- спорить
S["спорить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">спор-</span>'
    '<span class="hd-gloss">gốc <b>спор</b> — cuộc tranh luận</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>спор</b> là cuộc tranh cãi, <b>спо́рить</b> là làm cái việc '
    'đó. Từ «cãi nhau bằng lời» trượt thẳng sang «cá cược», vì đánh cược cũng là hai '
    'bên khăng khăng mình đúng.</div>'
    '<div class="hd-warn">KHÔNG cùng gốc với <b>спорт</b> hay <b>тра́нспорт</b> — hai '
    'từ kia là chữ mượn (Anh <i>sport</i>, Latin <i>portare</i> mang vác). Giống mặt '
    'chữ chỉ là trùng hợp.</div>'
    '<div class="hd-warn">Cách nó đòi: cãi VỚI ai thì <b>с</b> + cách 5, cãi VỀ chuyện '
    'gì thì <b>о</b> + cách 6. Rủ cá cược thì nói trống: <b>Спо́рим?</b> = Cá '
    'không?</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>спор</b> cuộc tranh cãi · <b>поспо́рить</b> cãi một trận, '
    'đánh cược (thể hoàn thành)</div>'
)

# ------------------------------------------------------------- уважаемый
S["уважаемый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-важ-</span>'
    '<span class="hd-gloss">cùng phần gốc với <b>ва́жно</b> — quan trọng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ем-</span>'
    '<span class="hd-gloss">hậu tố «ĐANG ĐƯỢC …»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>уважа́ть</b> vốn là cân xem ai đó nặng ký đến đâu → coi '
    'trọng, kính trọng. Đuôi <b>-емый</b> lật sang chiều bị động, nên cả từ nghĩa đen '
    'là «người đang được kính trọng».</div>'
    '<div class="hd-warn">Chỗ bạn gặp nó nhiều nhất là đầu thư và email trang trọng: '
    '<b>Уважа́емый Ива́н Ива́нович!</b> / <b>Уважа́емая А́нна!</b> = «Kính gửi…».</div>'
    '<div class="hd-warn">Hậu tố <b>-емый</b> mở khoá cả một lớp: <b>люби́мый</b> = '
    'người ĐƯỢC yêu. Thấy đuôi này là hiểu ngay chiều bị động.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ва́жно</b> quan trọng · <b>уважа́ть</b> kính trọng</div>'
)

# ----------------------------------------------------------- удивительно
S["удивительно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-див-</span>'
    '<span class="hd-gloss">gốc ДИВО — điều lạ lùng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́тельн-</span>'
    '<span class="hd-gloss">hậu tố «GÂY RA điều đó»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>удиви́ть</b> là làm ai đó thấy lạ. Hậu tố <b>-тельный</b> '
    'đã học biến nó thành tính từ «gây kinh ngạc», rồi <b>-о</b> hạ xuống thành lời '
    'nhận xét trống không.</div>'
    '<div class="hd-warn">Hai chỗ dùng khác hẳn nhau: đứng một mình là câu nhận xét — '
    '<b>Удиви́тельно, что он пришёл</b> = Lạ thật, anh ta lại đến. Đứng trước tính từ '
    'thì thành «đến mức kinh ngạc»: <b>удиви́тельно краси́вый</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>удиви́тельный</b> đáng kinh ngạc · <b>удиви́ться</b> '
    'ngạc nhiên</div>'
)

# ------------------------------------------------------ фотографироваться
S["фотографироваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">фото-</span>'
    '<span class="hd-gloss">ÁNH SÁNG (tiếng Hy Lạp)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-граф-</span>'
    '<span class="hd-gloss">VIẾT, VẼ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́рова-</span>'
    '<span class="hd-gloss">khuôn Nga hoá động từ quốc tế</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ться</span>'
    '<span class="hd-gloss">phản thân: quay về CHÍNH MÌNH</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ghép lại là «vẽ bằng ánh sáng». Thêm <b>-ся</b> thì hành động '
    'quay ngược về người nói: không phải mình chụp người khác, mà mình đi chụp ảnh '
    'chính mình.</div>'
    '<div class="hd-warn">Lớp <b>-ирова́ть</b> đổi đuôi sang <b>-у-</b> ở thì hiện tại: '
    '<b>фотографи́руюсь, фотографи́руешься</b> — luật chung của cả lớp <b>-овать</b>.</div>'
    '<div class="hd-warn">Bỏ <b>-ся</b> là đổi hẳn người trong ảnh: '
    '<b>фотографи́ровать</b> chụp NGƯỜI KHÁC, còn <b>фотографи́роваться</b> là mình '
    'được chụp.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>фо́то</b> tấm ảnh · <b>фото́граф</b> thợ chụp ảnh</div>'
)

# ------------------------------------------------------------ что-нибудь
S["что-нибудь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">что</span>'
    '<span class="hd-gloss">cái gì</span></div>'
    '<div class="hd-row"><span class="hd-piece">-нибудь</span>'
    '<span class="hd-gloss">tiểu từ «bất kỳ, chưa xác định»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>-нибудь</b> nghĩa là «cái nào cũng được» — chính người nói '
    'cũng KHÔNG biết đó là cái gì. Ghép vào <b>что</b> thì ra «bất cứ thứ gì, cái gì '
    'đó cũng được».</div>'
    '<div class="hd-warn">Cặp dễ lẫn: dùng <b>что́-нибудь</b> khi cái đó chưa có thật '
    '— câu hỏi, câu sai khiến, chuyện tương lai: <b>Скажи́ что́-нибудь!</b> Còn '
    '<b>что́-то</b> là có thật, chỉ chưa gọi tên ra.</div>'
    '<div class="hd-warn">Chỉ phần <b>что</b> biến cách, đuôi <b>-нибудь</b> đứng yên: '
    '<b>чего́-нибудь, чему́-нибудь, о чём-нибудь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>что</b> cái gì · <b>кто</b> ai · <b>что́бы</b> để mà</div>'
)

# ============================================================ field Vietnamese
# Chỉ sửa dòng thật sự hỏng: có ngoặc chú thích (README §2c cấm), thiếu nghĩa mà
# gloss tiếng Anh xác nhận, hoặc trùng nguyên cụm với thẻ khác mà badge không tách.
V = {
    # gloss tiếng Anh có "an electrical plug" — nghĩa thông dụng đang thiếu hẳn
    "вилка": "cái nĩa, phích cắm điện",
    # bỏ "quan trọng": trùng nguyên cụm với большой (cùng badge adj, không tách được)
    "серьёзный": "nghiêm túc, nghiêm trọng",
    # bỏ ngoặc chú thích "(dạng sợi)"
    "спагетти": "mì Ý",
    # bỏ ngoặc "(cho chính mình)" — badge phản thân đã in sẵn trên mặt đề bài
    "фотографироваться": "chụp ảnh, đi chụp ảnh",
    # bỏ dấu gạch chéo, viết thành danh sách nghĩa; KHÔNG lấy "dissuade" của từ điển
    # — đó là nghĩa của отговорить, không phải разговорить
    "разговорить": "khiến ai đó chịu nói, gợi cho ai mở lòng",
    # bỏ ngoặc "(nữ)": иностранка vốn RỖNG GenderBadge nên cái ngoặc là thứ duy
    # nhất tách nó khỏi иностранец. Luồng chính đã điền FEM ♀ (12/08), badge in
    # sẵn trên mặt đề bài giờ tách được, nên ngoặc thành thừa + phạm cấm ③.
    "иностранка": "người nước ngoài",
}
