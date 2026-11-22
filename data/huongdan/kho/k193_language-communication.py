# -*- coding: utf-8 -*-
"""k193 — language::communication (lô trộn): nói, nghe, gọi điện, nhận xét.

Chỗ cần nhất quán trong lô:
(1) вы́слушать / выслу́шивать: -слуш- ← слух TAI, khớp слу́шать [k02]; phân biệt прослу́шать [k02].
(2) дозвони́ться / дозва́ниваться: -звон- TIẾNG CHUÔNG, khớp звони́ть [k54]; о→а ở thể CHT.
    Bẫy chung: дозвони́ться ДО + cách 2 ≠ звони́ть + cách 3.
(3) посы́лка: «по- giữ lại từ посла́ть + -сыл- gốc GỬI», khớp посыла́ть [k88].
(4) замеча́ние: за- tiền tố thể + -мет-/-меч- DẤU, khớp заме́тить/замеча́ть [k95].
(5) акаде́мик ↔ акаде́мия [k39]: trọng âm giữ -де́-.
(6) предыду́щий: пред- + -ыд- (= ид- ĐI) + -ущ-, soi gương сле́дующий [k75].
Họ hàng cố ý vắng: комплиме́нт, па́уза (từ mượn đứng một mình, không có từ phái sinh thông dụng).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "балл": "điểm, điểm số, cấp",                           # «thang điểm» = scale, sai; gloss degree/force -> «cấp» (gió, động đất)
    "комплимент": "lời khen",                               # «lời tán tỉnh» gloss không xác nhận (chỉ «compliment»)
    "выслушать": "nghe hết, lắng nghe đến cùng, nghe tim phổi",      # thêm auscultate
    "выслушивать": "nghe hết, lắng nghe đến cùng, nghe tim phổi",    # bỏ «nghe tâm sự» (gloss không có); badge thể tách với выслушать
}

# --------------------------------------------------------------------- академик
S["академик"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">акаде́м-</span>'
    '<span class="hd-gloss">← <b>акаде́мия</b> viện hàn lâm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ик</span>'
    '<span class="hd-gloss">hậu tố chỉ NGƯỜI, như <b>хи́мик</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người của Viện hàn lâm. Trọng âm đứng yên ở <b>-де́-</b> y như '
    '<b>акаде́мия</b>.</div>'
    '<div class="hd-warn">Đây là DANH HIỆU — thành viên chính thức của một Viện Hàn lâm, '
    'không phải «người làm học thuật» nói chung. Nhà khoa học nói chung là <b>учёный</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>акаде́мия</b> viện hàn lâm · <b>академи́ческий</b> học thuật, '
    'hàn lâm (trọng âm nhảy)</div>'
)

# --------------------------------------------------------------------- балл
S["балл"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn (Pháp <i>balle</i> / Đức <i>Ball</i> «quả bóng»), không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Xưa người ta bỏ phiếu bằng viên bi — đếm bi là đếm điểm (cùng gốc tiếng '
    'Anh <i>ballot</i>). Nay là một nấc trên thang đo: điểm thi ở trường (<b>пять ба́ллов</b> = '
    'điểm tối đa), cấp gió, cấp động đất (<b>землетрясе́ние в семь ба́ллов</b>).</div>'
    '<div class="hd-warn">HAI chữ <b>л</b>: <b>балл</b> điểm — một <b>л</b>: <b>бал</b> dạ hội. '
    'Hai từ mượn khác nhau, đọc như nhau.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>баллоти́роваться</b> ra ứng cử (← bỏ phiếu bằng bi) · '
    '<b>пятиба́лльный</b> theo thang 5 điểm</div>'
)

# --------------------------------------------------------------------- посылка
S["посылка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">giữ lại từ <b>посла́ть</b>, không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сыл-</span>'
    '<span class="hd-gloss">gốc GỬI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Lấy <b>посыла́ть</b> bỏ đuôi động từ, gắn <b>-ка</b> ⇒ thứ được gửi đi = '
    'bưu kiện, và cả việc gửi. Số nhiều cách 2 chen <b>о</b> vào giữa <b>л</b>–<b>к</b>: '
    '<b>нет посы́лок</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>посыла́ть</b> gửi (CHT) · <b>посла́ть</b> gửi (HT) · '
    '<b>посо́л</b> đại sứ</div>'
)

# --------------------------------------------------------------------- замечание
S["замечание"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">tiền tố thể, KHÔNG mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-меч-</span>'
    '<span class="hd-gloss">gốc DẤU, đánh dấu — <b>т</b> hoá <b>ч</b> như <b>замеча́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ание</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Điều mình «đánh dấu» được rồi nói ra ⇒ lời nhận xét. Nói ra cái LỖI mình '
    'để ý thấy ⇒ lời nhắc nhở, phê bình.</div>'
    '<div class="hd-warn"><b>сде́лать замеча́ние</b> + cách 3 = nhắc nhở, khiển trách ai: '
    '<b>Учи́тель сде́лал ему́ замеча́ние</b>. Nghĩa hay gặp nhất ở trường, chỗ làm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>заме́тить</b> / <b>замеча́ть</b> để ý thấy · <b>заме́тка</b> ghi chú · '
    '<b>замеча́тельный</b> tuyệt vời</div>'
)

# --------------------------------------------------------------------- почерк
S["почерк"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa rõ — đừng suy</span></div>'
    '<div class="hd-row"><span class="hd-piece">-черк</span>'
    '<span class="hd-gloss">NÉT GẠCH — như <b>подчеркну́ть</b> gạch chân</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cách mỗi người đưa nét bút ⇒ nét chữ, chữ viết tay. Nói bóng cũng được: '
    '<b>по́черк а́втора</b> = dấu ấn, lối riêng của tác giả. Trọng âm ở đầu: <b>по́-</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>подчеркну́ть</b> gạch chân; nhấn mạnh · <b>зачеркну́ть</b> gạch bỏ · '
    '<b>вы́черкнуть</b> gạch tên khỏi danh sách</div>'
)

# --------------------------------------------------------------------- комплимент
S["комплимент"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn Pháp <i>compliment</i>, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= tiếng Anh <i>compliment</i>, đọc y nguyên, trọng âm ở <b>-ме́-</b>. '
    'Giống đực, biến cách đều.</div>'
    '<div class="hd-warn">Khen ai là <b>сде́лать комплиме́нт</b> + cách 3: <b>сде́лать ей '
    'комплиме́нт</b> — cụm chuẩn, hay gặp hơn hẳn <b>сказа́ть</b>.</div>'
)

# --------------------------------------------------------------------- жест
S["жест"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn (Latin <i>gestus</i>, qua Pháp <i>geste</i>), không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= tiếng Anh <i>gesture</i> bỏ đuôi. Nghĩa bóng như tiếng Việt «cử chỉ»: '
    '<b>краси́вый жест</b> = một cử chỉ đẹp.</div>'
    '<div class="hd-warn">KHÔNG cùng gốc <b>жесто́кий</b> tàn nhẫn hay <b>жёсткий</b> cứng — '
    'chỉ trùng mặt chữ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>жестикули́ровать</b> khoa tay múa chân · <b>жестикуля́ция</b> '
    'điệu bộ tay chân</div>'
)

# --------------------------------------------------------------------- выслушать
S["выслушать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span>'
    '<span class="hd-gloss">RA — làm cho tới hết</span></div>'
    '<div class="hd-row"><span class="hd-piece">-слуш-</span>'
    '<span class="hd-gloss">← <b>слух</b> TAI, sự nghe</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">chia đều</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghe cho «ra» hết: để người ta nói xong rồi mới đáp. Tân ngữ là NGƯỜI '
    'hoặc lời họ, cách 4: <b>вы́слушать дру́га</b>. Bác sĩ cũng <b>вы́слушать</b> bệnh nhân bằng ống nghe. '
    'Thể HT có <b>вы-</b> thì <b>вы́-</b> luôn mang trọng âm: <b>вы́слушаю</b>.</div>'
    '<div class="hd-warn"><b>прослу́шать</b> nghe trọn một BÀI (giảng, nhạc) — <b>вы́слушать</b> '
    'nghe hết lời một NGƯỜI.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>выслу́шивать</b> (CHT) · <b>слу́шать</b> nghe · '
    '<b>прослу́шать</b> nghe trọn · <b>слух</b> thính giác</div>'
)

# --------------------------------------------------------------------- выслушивать
S["выслушивать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span>'
    '<span class="hd-gloss">RA — làm cho tới hết</span></div>'
    '<div class="hd-row"><span class="hd-piece">-слуш-</span>'
    '<span class="hd-gloss">← <b>слух</b> TAI, sự nghe</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ть</span>'
    '<span class="hd-gloss">đuôi CHƯA hoàn thành: kéo dài, lặp lại</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>вы́слушать</b>: chèn <b>-ива-</b> và trọng âm rời '
    '<b>вы-</b> sang gốc — <b>выслу́шивать</b>, <b>выслу́шиваю</b>. Dùng cho việc đang diễn ra '
    'hay lặp lại: <b>Он всегда́ выслу́шивает меня́</b> = anh ấy lúc nào cũng chịu nghe tôi nói hết.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вы́слушать</b> (HT) · <b>слу́шать</b> nghe · <b>слух</b> thính giác</div>'
)

# --------------------------------------------------------------------- ирония
S["ирония"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn Hy Lạp <i>eirōneia</i>, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= tiếng Anh <i>irony</i>. Đuôi <b>-ия</b> → giống cái, chia y như '
    '<b>акаде́мия</b>.</div>'
    '<div class="hd-warn"><b>иро́ния судьбы́</b> = trớ trêu của số phận — tên bộ phim «<b>Иро́ния '
    'судьбы́</b>» (1975), người Nga xem lại mỗi đêm giao thừa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ирони́чный</b> mỉa mai · <b>иронизи́ровать</b> châm biếm</div>'
)

# --------------------------------------------------------------------- рекомендация
S["рекомендация"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рекоменд-</span>'
    '<span class="hd-gloss">= <i>recommend</i> khuyên, giới thiệu</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ция</span>'
    '<span class="hd-gloss">= <i>-ation</i> tiếng Anh → danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đổi <i>-ation</i> thành <b>-ация</b> là ra cả lớp từ quốc tế: '
    '<b>информа́ция</b>, <b>организа́ция</b>. Trọng âm luôn ở <b>-а́-</b>.</div>'
    '<div class="hd-warn"><b>по рекоменда́ции</b> + cách 2 = theo lời khuyên / lời giới thiệu của ai: '
    '<b>по рекоменда́ции врача́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рекомендова́ть</b> khuyên, giới thiệu (<b>рекоменду́ю</b>) · '
    '<b>рекоменда́тельный</b> giới thiệu (<b>рекоменда́тельное письмо́</b> thư giới thiệu)</div>'
)

# --------------------------------------------------------------------- дозваниваться
S["дозваниваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-</span>'
    '<span class="hd-gloss">TỚI NƠI, tới đích</span></div>'
    '<div class="hd-row"><span class="hd-piece">-зван-</span>'
    '<span class="hd-gloss">= <b>звон-</b> TIẾNG CHUÔNG, <b>о</b> đổi <b>а</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ть-ся</span>'
    '<span class="hd-gloss">đuôi CHƯA hoàn thành + phản thân</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cố cho tiếng chuông reo TỚI được đầu bên kia: nhấn vào quá trình gọi mãi. '
    '<b>Я дозва́ниваюсь уже́ час</b> = tôi gọi cả tiếng mà chưa được. Thể CHT đổi <b>о → а</b> '
    'y như <b>спроси́ть → спра́шивать</b>. Người cần gọi: <b>до</b> + cách 2 (xem <b>дозвони́ться</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дозвони́ться</b> (HT) · <b>звони́ть</b> gọi điện · '
    '<b>звоно́к</b> cuộc gọi; chuông</div>'
)

# --------------------------------------------------------------------- дозвониться
S["дозвониться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-</span>'
    '<span class="hd-gloss">TỚI NƠI, tới đích</span></div>'
    '<div class="hd-row"><span class="hd-piece">-звон-</span>'
    '<span class="hd-gloss">TIẾNG CHUÔNG — chính là <b>звони́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-ть-ся</span>'
    '<span class="hd-gloss">lớp chia thứ hai + phản thân</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiếng chuông đã TỚI được nơi ⇒ gọi được, liên lạc được. Hay dùng ở phủ định: '
    '<b>Не могу́ дозвони́ться</b> = gọi mãi không được. Trọng âm bám đuôi như <b>звони́ть</b>: '
    '<b>дозвони́шься</b>.</div>'
    '<div class="hd-warn">Gọi được cho AI: <b>до</b> + cách 2 — <b>дозвони́ться до врача́</b>, '
    'khác hẳn <b>звони́ть врачу́</b> (cách 3).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дозва́ниваться</b> (CHT) · <b>звони́ть</b> gọi điện · '
    '<b>звоно́к</b> cuộc gọi; chuông</div>'
)

# --------------------------------------------------------------------- пауза
S["пауза"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn Latin <i>pausa</i>, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= tiếng Anh <i>pause</i>; đuôi <b>-а</b> → giống cái. Trọng âm ở đầu: '
    '<b>па́-</b>. Ngưng một chút là <b>сде́лать па́узу</b>; trong âm nhạc là dấu lặng.</div>'
)

# --------------------------------------------------------------------- годовщина
S["годовщина"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">год-</span>'
    '<span class="hd-gloss">NĂM</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ов-</span>'
    '<span class="hd-gloss">nối, như <b>годово́й</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-щи́на</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ngày tròn NĂM kể từ một sự kiện. Đếm bằng số thứ tự: '
    '<b>деся́тая годовщи́на сва́дьбы</b> = kỷ niệm 10 năm ngày cưới.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>год</b> năm · <b>годово́й</b> (thuộc) cả năm · '
    '<b>ежего́дный</b> hằng năm</div>'
)

# --------------------------------------------------------------------- предыдущий
S["предыдущий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пред-</span>'
    '<span class="hd-gloss">TRƯỚC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыд-</span>'
    '<span class="hd-gloss">= <b>ид-</b> ĐI (<b>идти́</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ущ-ий</span>'
    '<span class="hd-gloss">đuôi phân từ «đang …» + đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cái đang đi phía trước» ⇒ liền trước, trước đó — soi gương '
    '<b>сле́дующий</b> «cái đang theo sau». <b>и</b> thành <b>ы</b> sau tiền tố tận cùng phụ âm '
    'cứng, như <b>с</b> + <b>игра́ть</b> → <b>сыгра́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>идти́</b> đi · <b>прийти́</b> đến</div>'
)

B = {
    "docbangmat": 61,
    "loitubat": 2,   # комплимент: «Không dùng сказа́ть» nói quá (сказа́ть комплиме́нт vẫn có người nói) -> «cụm chuẩn, hay gặp hơn hẳn»
                     # академик: «Viện Hàn lâm Khoa học» hẹp quá (còn viện hàn lâm nghệ thuật…) -> «một Viện Hàn lâm»
    "nguonsai": 3,   # балл «thang điểm» (= scale, không phải point) · комплимент «lời tán tỉnh» · выслушивать «nghe tâm sự» — gloss Anh không xác nhận
    "baolen": [
        "V cần duyệt (4): балл «điểm, điểm số, cấp» (bỏ «thang điểm», thêm «cấp» theo gloss degree/force) · "
        "комплимент «lời khen» · выслушать + выслушивать cùng «nghe hết, lắng nghe đến cùng, nghe tim phổi» "
        "(thêm auscultate; badge thể tách hai thẻ). Đã chạy do_va_cham trên toàn bộ thẻ với V thay vào: không đẻ va chạm mới.",
        "Chỗ KHÔNG chắc: балл ← quả bóng/viên bi bỏ phiếu (cùng gốc ballot, баллоти́роваться) — từ nguyên theo Vasmer, ghi thẳng không gắn Mức tin; "
        "по- trong по́черк ghi «không mang nghĩa rõ — đừng suy»; KHÔNG nối -черк- với черта́ [k157] vì không chắc cùng gốc.",
        "Họ hàng cố ý vắng: комплиме́нт, па́уза (từ mượn đứng một mình).",
        "жест: V hiện «cử chỉ, động tác, hành động biểu thị» — «hành động biểu thị» hơi tối nghĩa nhưng không sai, để nguyên; user muốn gọn thì sửa tay.",
    ],
}
