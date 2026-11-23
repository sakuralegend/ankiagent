# -*- coding: utf-8 -*-
"""k211 — language::documents: giấy tờ, xuất bản; trục là GỐC + TIỀN TỐ.

Chỗ cần nhất quán trong lô:
(1) посередине: серед- GIỮA — khớp середина k130, среди k111.
(2) вправо/влево: в- VÀO PHÍA + прав- / лев- — khớp направо/налево k49, правый k93.
(3) окружать/окружить: круг → круж- VÒNG — khớp круг k07, вокруг k114.
(4) проезд: про- QUA + -езд ĐI BẰNG XE — khớp проезжать/проехать k141.
(5) издавать/издать: из- RA + -да- ĐƯA, CHO — khớp издательство k196; chia như дать/давать
    (передать k65, сдавать/сдать k98).
(6) предавать/предать: пре- QUA (dạng sách cổ của пере-) — khớp предатель k168.
(7) предъявить/предъявлять: -яв- LỘ RA, HIỆN RÕ — khớp заявление k120, появиться k97.
(8) изобретение: -об- + -рет- TÌM THẤY — khớp приобрести k175 (kèm cùng mức tin).
Họ hàng cố ý vắng: không có (вуз, блокнот, портфель, квитанция là từ viết tắt / từ mượn nhưng
vẫn có từ cùng gốc thật trong tiếng Nga).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "посередине": "ở giữa, ở chính giữa, nửa đường",                         # «giữa» trơn là giới từ, lẫn ме́жду
    "проезд": "chuyến đi, việc đi lại, lượt đi, việc xe đi qua, lối xe đi",  # + driving through, thoroughfare
    "издавать": "xuất bản, phát hành, ban hành, phát ra, toả ra",            # + enact, emit / give off
    "издать": "xuất bản, phát hành, ban hành, phát ra, toả ra",              # «in ra» gloss không có; + emit / give off
    "предавать": "phản bội, bán đứng, giao nộp",                             # «bán rẻ» = bán giá thấp; hand over
    "предать": "phản bội, bán đứng, giao nộp",
    "вуз": "cơ sở giáo dục đại học",                                         # gỡ ⊇ ко́лледж[k09], университе́т[k39]
    "портфель": "cặp, cặp táp, cặp sách, danh mục đầu tư",                   # + portfolio
}

# ----------------------------------------------------------------- посередине
S["посередине"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">TẠI, theo</span></div>'
    '<div class="hd-row"><span class="hd-piece">-серед-</span>'
    '<span class="hd-gloss">GIỮA — như <b>середи́на</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́н-е</span>'
    '<span class="hd-gloss">đuôi cách của <b>середи́на</b>, nay đông cứng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giới từ dính hẳn vào <b>середи́на</b> (phần giữa) ⇒ «ở chỗ giữa»; '
    'trên đường đi thì là nửa đường. Đã thành trạng từ nên không biến đổi nữa.</div>'
    '<div class="hd-warn">Thêm cách 2 thì nó làm giới từ: <b>посереди́не ко́мнаты</b> ở '
    'giữa phòng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>середи́на</b> phần giữa · <b>посреди́</b> ở giữa · '
    '<b>среди́</b> giữa (những) · <b>сре́дний</b> ở giữa, trung bình</div>'
)

# --------------------------------------------------------------------- вправо
S["вправо"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO PHÍA (có hướng)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-прав-</span>'
    '<span class="hd-gloss">gốc của <b>пра́вый</b> — ở đây là BÊN PHẢI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Vào phía phải» ⇒ sang phải: <b>Поверни́те впра́во!</b> Rẽ phải! '
    'Tiền tố nói rõ câu hỏi: <i>в-</i>, <i>на-</i> = ĐI VỀ phía (<b>куда́?</b>) · <i>с-</i> '
    '= Ở phía (<b>где?</b> — <b>спра́ва</b>).</div>'
    '<div class="hd-warn">Gần như thay được cho <b>напра́во</b>. Nói lệch, xê dịch sang '
    'phải thì hay gặp <b>впра́во</b>: <b>шаг впра́во</b> một bước sang phải.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пра́вый</b> bên phải, đúng · <b>напра́во</b> sang phải · '
    '<b>спра́ва</b> ở bên phải · <b>пра́вда</b> sự thật</div>'
)

# ---------------------------------------------------------------------- влево
S["влево"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO PHÍA (có hướng)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лев-</span>'
    '<span class="hd-gloss">BÊN TRÁI — gốc của <b>ле́вый</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Vào phía trái» ⇒ sang trái: <b>шаг вле́во</b> một bước sang trái. '
    'Soi gương với <b>впра́во</b>. Ở bên trái (đứng yên) thì là <b>сле́ва</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ле́вый</b> bên trái · <b>нале́во</b> sang trái · <b>сле́ва</b> '
    'ở bên trái · <b>левша́</b> người thuận tay trái</div>'
)

# ------------------------------------------------------------------- окружать
S["окружать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">QUANH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-круж-</span>'
    '<span class="hd-gloss">VÒNG — <b>круг</b>, г → ж</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>окружа́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm thành một VÒNG quanh cái gì ⇒ bao quanh: <b>Дере́вню окружа́ет '
    'лес.</b> Rừng bao quanh làng. Phép <i>г → ж</i> y như <b>кружо́к</b>. Cặp HT: '
    '<b>окружи́ть</b>.</div>'
    '<div class="hd-warn">Phân từ của nó dùng hằng ngày: <b>окружа́ющий</b> xung quanh → '
    '<b>окружа́ющая среда́</b> môi trường.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>окружи́ть</b> (HT) · <b>окруже́ние</b> những người, thứ quanh '
    'mình · <b>круг</b> vòng tròn · <b>вокру́г</b> xung quanh</div>'
)

# ------------------------------------------------------------------- окружить
S["окружить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">QUANH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-круж-</span>'
    '<span class="hd-gloss">VÒNG — <b>круг</b>, г → ж</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp HT của <b>окружа́ть</b> — nghĩa xem ở thẻ đó. Trọng âm nằm ở '
    'đuôi suốt bảng: <b>окружу́, окружи́шь, окружа́т</b>.</div>'
    '<div class="hd-warn">Bao quanh AI (cách 4) BẰNG GÌ (cách 5): <b>окружи́ть дете́й '
    'забо́той</b> chăm chút bọn trẻ, nghĩa đen «vây trẻ bằng sự chăm lo».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>окружа́ть</b> (CHT) · <b>окруже́ние</b> môi trường quanh mình · '
    '<b>о́круг</b> khu, quận (vùng khoanh lại) · <b>кру́глый</b> tròn</div>'
)

# --------------------------------------------------------------------- проезд
S["проезд"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">QUA, xuyên qua</span></div>'
    '<div class="hd-row"><span class="hd-piece">-езд</span>'
    '<span class="hd-gloss">ĐI BẰNG XE — như <b>по́езд</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>прое́хать</b> / <b>проезжа́ть</b>: việc đi xe QUA, '
    'rồi cả CHỖ cho xe qua. Trong thành phố là chuyến đi, lượt đi xe. Đi BỘ qua thì là '
    '<b>прохо́д</b>.</div>'
    '<div class="hd-warn">Hai chỗ gặp hằng ngày: <b>опла́та прое́зда</b> trả tiền vé xe · '
    'biển <b>Прое́зд запрещён</b> cấm xe qua.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>прое́хать</b> đi xe qua · <b>проездно́й</b> vé tháng · '
    '<b>по́езд</b> tàu hoả · <b>подъе́зд</b> cổng, lối vào · <b>е́здить</b> đi xe (nhiều '
    'lần)</div>'
)

# ------------------------------------------------------------ железнодорожный
S["железнодорожный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">желе́зн-</span>'
    '<span class="hd-gloss">SẮT — <b>желе́зный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-о-</span>'
    '<span class="hd-gloss">nguyên âm nối hai gốc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-доро́ж-</span>'
    '<span class="hd-gloss">CON ĐƯỜNG — <b>доро́га</b>, г → ж</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ный</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gộp cụm <b>желе́зная доро́га</b> thành một tính từ — ghép đúng như '
    'tiếng Việt «đường sắt»: <b>железнодоро́жный вокза́л</b> ga đường sắt. Từ dài nhưng '
    'trọng âm chính chỉ một, ở <i>-ро́ж-</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>желе́зо</b> sắt · <b>желе́зный</b> bằng sắt · <b>доро́га</b> '
    'con đường · <b>доро́жный</b> thuộc đường sá · <b>железнодоро́жник</b> nhân viên đường '
    'sắt</div>'
)

# -------------------------------------------------------------------- вопреки
S["вопреки"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">во-</span>'
    '<span class="hd-gloss">giới từ <i>в</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-прек-</span>'
    '<span class="hd-gloss">NGANG, NGƯỢC LẠI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́</span>'
    '<span class="hd-gloss">đuôi cũ, nay không mang nghĩa riêng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đi ngang, ngược lại điều gì ⇒ trái với, bất chấp: <b>вопреки́ '
    'всему́</b> bất chấp tất cả · <b>вопреки́ прогно́зу</b> trái với dự báo.</div>'
    '<div class="hd-warn">Đòi cách 3 — cùng nhóm với <b>благодаря́</b> nhờ có, '
    '<b>согла́сно</b> theo.</div>'
    '<div class="hd-warn">⚠️ Mức tin: <i>прек-</i> là dạng sách của <i>перёк-</i> trong '
    '<b>поперёк</b> — từ nguyên, không phải luật suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поперёк</b> theo chiều ngang · <b>попере́чный</b> nằm '
    'ngang</div>'
)

# --------------------------------------------------------------------- ничуть
S["ничуть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ни-</span>'
    '<span class="hd-gloss">KHÔNG một … nào — như <b>никто́</b>, <b>ничего́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-чуть</span>'
    '<span class="hd-gloss"><b>чуть</b> một tí</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Không lấy MỘT TÍ» ⇒ không hề. Đáp gọn một mình được: <b>Ты '
    'уста́л? — Ничу́ть!</b> Mệt không? — Không hề!</div>'
    '<div class="hd-warn">Trong câu đầy đủ, động từ vẫn phải có <b>не</b>: <b>Я ничу́ть не '
    'жале́ю.</b> Tôi chẳng hề tiếc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>чуть</b> một tí, suýt · <b>чуть-чу́ть</b> một chút · '
    '<b>чу́точку</b> một tẹo</div>'
)

# ------------------------------------------------------------------ заголовок
S["заголовок"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">ở đây không mang nghĩa riêng dễ nhớ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-голо́в-</span>'
    '<span class="hd-gloss">ĐẦU — <b>голова́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ок</span>'
    '<span class="hd-gloss">→ danh từ giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái đứng ở ĐẦU bài ⇒ tiêu đề — tiếng Anh cùng hình ảnh: <i>head → '
    'heading, headline</i>. Nguyên âm chạy: <i>о</i> của <i>-ок</i> rơi ngay khi thêm đuôi: '
    '<b>заголо́вок → заголо́вка, заголо́вки</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>голова́</b> cái đầu · <b>подзаголо́вок</b> tiêu đề phụ · '
    '<b>загла́вие</b> tên sách, tên bài · <b>гла́вный</b> chính, chủ yếu</div>'
)

# ---------------------------------------------------------------------- обзор
S["обзор"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">QUANH, khắp lượt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-зор</span>'
    '<span class="hd-gloss">NHÌN — mặt khác của <i>зр-</i> trong <b>зре́ние</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">NHÌN KHẮP một lượt ⇒ bài tổng quan; chỗ nhìn được khắp xung quanh '
    '⇒ tầm nhìn. Tiếng Anh ghép gần y vậy: <i>over-view</i>.</div>'
    '<div class="hd-warn">Tổng quan VỀ cái gì ở cách 2: <b>обзо́р новосте́й</b> điểm tin · '
    '<b>обзо́р фи́льма</b> bài đánh giá phim.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>зре́ние</b> thị lực · <b>зри́тель</b> khán giả · '
    '<b>кругозо́р</b> tầm hiểu biết · <b>обозрева́тель</b> nhà bình luận</div>'
)

# -------------------------------------------------------------------- блокнот
S["блокнот"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ theo kiểu Nga được: từ mượn nguyên khối.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mượn tiếng Pháp <i>bloc-notes</i>: <i>bloc</i> khối, xấp + '
    '<i>notes</i> ghi chép ⇒ XẤP giấy để GHI. Cùng họ với Anh <i>block</i> và '
    '<i>note</i>.</div>'
    '<div class="hd-warn">Anh <i>notebook</i> ứng với hai từ Nga: <b>блокно́т</b> sổ giấy · '
    '<b>ноутбу́к</b> máy tính xách tay.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>блок</b> khối · <b>блокно́тик</b> sổ tay nhỏ · <b>но́та</b> nốt '
    'nhạc (cùng Latin <i>nota</i> dấu ghi)</div>'
)

# ------------------------------------------------------------------- издавать
S["издавать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">из-</span>'
    '<span class="hd-gloss">RA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дава́ть</span>'
    '<span class="hd-gloss">ĐƯA, CHO — chính là <b>дава́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đưa RA ngoài: đưa sách ra ⇒ xuất bản; đưa luật ra ⇒ ban hành; để '
    'tiếng, mùi thoát ra ⇒ phát ra, toả ra. Chia y hệt <b>дава́ть</b>: hiện tại rơi mất '
    '<i>-ва-</i> — <b>издаю́, издаёшь</b>. Cặp HT: <b>изда́ть</b>.</div>'
    '<div class="hd-warn">Âm thanh, mùi đứng ở cách 4: <b>издава́ть зву́ки</b> phát ra '
    'tiếng · <b>издава́ть за́пах</b> toả mùi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>изда́ть</b> (HT) · <b>изда́ние</b> ấn phẩm, lần xuất bản · '
    '<b>изда́тель</b> người xuất bản · <b>изда́тельство</b> nhà xuất bản</div>'
)

# --------------------------------------------------------------------- издать
S["издать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">из-</span>'
    '<span class="hd-gloss">RA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-да́-ть</span>'
    '<span class="hd-gloss">ĐƯA, CHO — chính là <b>дать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp HT của <b>издава́ть</b> — nghĩa xem ở thẻ đó. Chia theo bảng '
    'riêng của <b>дать</b>, không suy được từ nguyên thể: <b>изда́м, изда́шь, изда́ст, '
    'издади́м, издади́те, издаду́т</b>. Quá khứ giống cái đẩy trọng âm ra đuôi: '
    '<b>издала́</b>.</div>'
    '<div class="hd-warn">Phân từ bị động kéo trọng âm về tiền tố: <b>и́зданный</b> — trên '
    'sách hay gặp <b>и́здано в Москве́</b> xuất bản tại Moskva.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>издава́ть</b> (CHT) · <b>изда́ние</b> ấn phẩm · '
    '<b>изда́тель</b> người xuất bản · <b>дать</b> cho · <b>сдать</b> nộp, thi đậu</div>'
)

# ------------------------------------------------------------------ предавать
S["предавать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пре-</span>'
    '<span class="hd-gloss">QUA — dạng sách cổ của <i>пере-</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-дава́ть</span>'
    '<span class="hd-gloss">CHO, TRAO — chính là <b>дава́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trao người mình QUA tay địch ⇒ phản bội. Chia y hệt '
    '<b>дава́ть</b>, hiện tại rơi mất <i>-ва-</i>: <b>предаю́, предаёшь</b>. Cặp HT: '
    '<b>преда́ть</b>.</div>'
    '<div class="hd-warn">Cùng hai mảnh mà hai số phận: <b>передава́ть</b> (пере- Nga) '
    'chuyển, truyền · <b>предава́ть</b> (пре- sách cổ) phản bội.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>преда́ть</b> (HT) · <b>преда́тель</b> kẻ phản bội · '
    '<b>преда́тельство</b> sự phản bội · <b>дава́ть</b> cho</div>'
)

# -------------------------------------------------------------------- предать
S["предать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пре-</span>'
    '<span class="hd-gloss">QUA — dạng sách cổ của <i>пере-</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-да́-ть</span>'
    '<span class="hd-gloss">CHO, TRAO — chính là <b>дать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp HT của <b>предава́ть</b> — nghĩa xem ở thẻ đó. Chia theo bảng '
    'riêng của <b>дать</b>: <b>преда́м, преда́шь, преда́ст, предади́м, предади́те, '
    'предаду́т</b>. Quá khứ giống cái đẩy trọng âm ra đuôi: <b>предала́</b>.</div>'
    '<div class="hd-warn">Nghĩa «giao nộp»: người, vật ở cách 4, nơi nhận ở cách 3 — '
    '<b>преда́ть суду́</b> đưa ra toà.</div>'
    '<div class="hd-warn">Phân từ <b>пре́данный</b> khi làm tính từ lại là «trung thành, '
    'tận tuỵ» — người đã trao trọn mình.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>предава́ть</b> (CHT) · <b>преда́тель</b> kẻ phản bội · '
    '<b>переда́ть</b> trao lại, chuyển hộ · <b>дать</b> cho</div>'
)

# ----------------------------------------------------------------- предъявить
S["предъявить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пред-</span>'
    '<span class="hd-gloss">TRƯỚC, ra trước mặt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ъ-</span>'
    '<span class="hd-gloss">dấu ngăn: tiền tố kết phụ âm gặp <i>я</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-яв-</span>'
    '<span class="hd-gloss">LỘ RA, HIỆN RÕ — như <b>я́вный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cho HIỆN RA trước mặt người kiểm tra ⇒ xuất trình. Chỉ ngôi «tôi» '
    'chèn <i>л</i> và nhấn đuôi: <b>предъявлю́</b>; từ ngôi hai trọng âm lùi về gốc: '
    '<b>предъя́вишь</b>. Cặp CHT: <b>предъявля́ть</b>.</div>'
    '<div class="hd-warn">Thứ đưa ra ở cách 4: <b>предъяви́ть па́спорт</b> xuất trình hộ '
    'chiếu · <b>предъяви́ть обвине́ние</b> + cách 3: buộc tội ai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>предъявля́ть</b> (CHT) · <b>объяви́ть</b> tuyên bố · '
    '<b>заяви́ть</b> tuyên bố, khai báo · <b>появи́ться</b> xuất hiện · <b>я́вный</b> rõ '
    'ràng</div>'
)

# ---------------------------------------------------------------- предъявлять
S["предъявлять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пред-ъ-</span>'
    '<span class="hd-gloss">TRƯỚC, ra trước mặt (<i>ъ</i> ngăn trước <i>я</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-яв-</span>'
    '<span class="hd-gloss">LỘ RA, HIỆN RÕ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-л-я́-ть</span>'
    '<span class="hd-gloss">đuôi CHT, <i>л</i> chen sau <i>в</i> như <b>явля́ться</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>предъяви́ть</b> — nghĩa xem ở thẻ đó. Ở thể này '
    '<i>л</i> có mặt suốt bảng và chia đều: <b>предъявля́ю, предъявля́ешь</b>.</div>'
    '<div class="hd-warn">Đưa ra đòi hỏi cũng dùng nó: <b>предъявля́ть тре́бования</b> nêu '
    'yêu cầu · <b>предъявля́ть прете́нзии</b> khiếu nại.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>предъяви́ть</b> (HT) · <b>объявля́ть</b> tuyên bố (CHT) · '
    '<b>явле́ние</b> hiện tượng · <b>заявле́ние</b> đơn từ</div>'
)

# ------------------------------------------------------------------ квитанция
S["квитанция"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">квит-</span>'
    '<span class="hd-gloss">HẾT NỢ, xong nợ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́нция</span>'
    '<span class="hd-gloss">đuôi danh từ mượn, giống cái — như <b>диста́нция</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giấy chứng nhận đã trả XONG NỢ ⇒ biên lai. Cùng gốc Latin với Anh '
    '<i>quit</i>, <i>quits</i> (hết nợ nhau): <b>Мы кви́ты.</b> Ta huề nhé.</div>'
    '<div class="hd-warn"><b>квита́нция</b> là giấy nộp tiền (điện nước, bưu điện, tiền '
    'phạt) · <b>чек</b> là phiếu máy tính tiền ở cửa hàng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кви́ты</b> huề, hết nợ nhau · <b>квито́к</b> mẩu biên nhận '
    '(khẩu ngữ)</div>'
)

# ---------------------------------------------------------------- изобретение
S["изобретение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">из-</span>'
    '<span class="hd-gloss">RA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-об-</span>'
    '<span class="hd-gloss">tiền tố cũ — chữ <i>б</i> thuộc về đây</span></div>'
    '<div class="hd-row"><span class="hd-piece">-рет-</span>'
    '<span class="hd-gloss">GẶP, TÌM THẤY — như <b>приобрета́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ние</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">TÌM RA thứ chưa ai có ⇒ phát minh. Tiếng Anh cùng hình ảnh: '
    '<i>invent</i> từ Latin <i>invenire</i> «tìm thấy». Tìm thấy thứ ĐÃ có sẵn thì là '
    '<b>откры́тие</b> phát hiện.</div>'
    '<div class="hd-warn">⚠️ Mức tin: mảnh <i>-рет-</i> «tìm thấy» là từ nguyên (mặt chữ đã '
    'mờ), không phải luật suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>изобрести́</b> phát minh (HT) · <b>изобрета́ть</b> (CHT) · '
    '<b>изобрета́тель</b> nhà phát minh · <b>приобрести́</b> có được, mua</div>'
)

# ------------------------------------------------------------------------ вуз
S["вуз"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в</span>'
    '<span class="hd-gloss"><b>вы́сшее</b> BẬC CAO</span></div>'
    '<div class="hd-row"><span class="hd-piece">у</span>'
    '<span class="hd-gloss"><b>уче́бное</b> HỌC TẬP</span></div>'
    '<div class="hd-row"><span class="hd-piece">з</span>'
    '<span class="hd-gloss"><b>заведе́ние</b> CƠ SỞ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chữ viết tắt đã thành danh từ thường: viết chữ nhỏ, biến cách như '
    'mọi từ giống đực — <b>поступи́ть в вуз</b> vào đại học, <b>учи́ться в ву́зе</b> học '
    'đại học.</div>'
    '<div class="hd-warn">Tên gọi CHUNG cho mọi trường bậc đại học: <b>университе́т</b>, '
    '<b>институ́т</b>, <b>акаде́мия</b>. Còn <b>ко́лледж</b> ở Nga dạy nghề bậc trung cấp, '
    'không tính là <b>вуз</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вы́сший</b> cao nhất, bậc cao · <b>уче́бный</b> thuộc việc học '
    '· <b>заведе́ние</b> cơ sở · <b>ву́зовский</b> thuộc trường đại học</div>'
)

# ------------------------------------------------------------------- портфель
S["портфель"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ theo kiểu Nga được: từ mượn nguyên khối.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mượn tiếng Pháp <i>portefeuille</i>: <i>porte</i> mang + '
    '<i>feuille</i> tờ giấy ⇒ đồ MANG GIẤY TỜ. Anh <i>portfolio</i> đúng hai mảnh ấy qua '
    'tiếng Ý — nên có cả nghĩa «danh mục»: <b>портфе́ль а́кций</b> danh mục cổ phiếu.</div>'
    '<div class="hd-warn">Kết bằng <i>ь</i> mà giống ĐỰC: <b>но́вый портфе́ль</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>портати́вный</b> xách tay (cùng <i>porter</i> mang) · '
    '<b>портмоне́</b> ví tiền (Pháp <i>porte-monnaie</i>)</div>'
)

B = {
    "docbangmat": 116,
    "loitubat": 3,
    "nguonsai": 4,
    "baolen": [
        "Va chạm вуз ⊇ ко́лледж[k09] / университе́т[k39]: gỡ phía lô này — вуз «cơ sở giáo dục đại học». Đã chạy thử do_va_cham (chỉ đọc Anki) với V của mọi file lô k207–k216 đang có: 0 va chạm dính 22 từ này.",
        "V cần duyệt (8 thẻ): посереди́не (bỏ «giữa» trơn); прое́зд + «việc xe đi qua, lối xe đi»; издава́ть/изда́ть «xuất bản, phát hành, ban hành, phát ra, toả ra» (bỏ «in», «in ra»); предава́ть/преда́ть «phản bội, bán đứng, giao nộp» (bỏ «bán rẻ», «trao phó», «trao cho»); вуз; портфе́ль + «danh mục đầu tư». 14 thẻ còn lại giữ đề cũ.",
        "Gần đồng nghĩa, máy không bắt nhưng đề rất sát: впра́во «sang phải, về phía phải» ↔ напра́во[k49] «sang phải, về bên phải»; вле́во ↔ нале́во[k49] y vậy. Cùng badge adv, chỉ khác phía/bên — hai cặp này đồng nghĩa thật, không có nghĩa riêng nào để thêm; user quyết.",
        "Sát tương tự: ничу́ть ↔ ниско́лько chung «không hề, chẳng chút nào» (ниско́лько badge pron nên đã tách). Giữ nguyên.",
        "Nguồn sai đã bác (4): изда́ть «in ra» (gloss không có print); предава́ть và преда́ть «bán rẻ» (nghĩa là bán giá thấp, betray = bán đứng); вуз «trường cao đẳng» (college của Anh, ко́лледж Nga không thuộc вуз).",
        "Chỗ KHÔNG chắc: (1) вопреки́ ↔ поперёк và (2) изобрете́ние -рет- là từ nguyên, đã ghi ô ⚠️ Mức tin. (3) преда́ть/предава́ть: gloss «consign / commit» chỉ sống trong cụm (преда́ть земле́, огню́), không đưa vào V, dạy преда́ть суду́ ở ô đỏ. (4) и́здано: OpenRussian chỉ ghi и́зданный, dạng ngắn suy theo.",
    ],
}
