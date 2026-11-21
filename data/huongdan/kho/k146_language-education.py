# -*- coding: utf-8 -*-
"""k146 — language::education: từ của trường đại học (khoa, điểm, giấy tờ), chỉ suy luận.

Chỗ cần nhất quán trong lô:
(1) đuôi -и́ческий = "thuộc về môn -ия/-ика", trọng âm dời về -и́-: биологи́ческий,
    математи́ческий, политехни́ческий (k147 soạn геологи́ческий cùng khuôn).
(2) đuôi -ёрка/-ойка gọi tên CON SỐ = điểm ở trường: дво́йка, четвёрка — khớp пятёрка (k142).
(3) đuôi -тор = NGƯỜI ĐIỀU KHIỂN (ре́ктор ↔ дире́ктор k69); đuôi động từ mượn -и́ровать
    (конспекти́ровать ↔ деклари́ровать, контроли́ровать).
(4) gốc фо́рм- = KHUÔN/BIỂU MẪU (k07): офо́рмить/оформля́ть = đưa vào đúng mẫu.
Họ hàng cố ý vắng: ка́федра, семина́р (từ mượn đứng một mình).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "русско-английский": "Nga-Anh",                        # bỏ ngoặc
    "оформить": "làm giấy tờ, làm thủ tục",                # bỏ «xong/hoàn tất» — nhãn thể trá hình
    "декларация": "bản khai, bản tuyên ngôn",              # RÚT «tờ khai» — trùng анке́та (k100); gloss declaration/proclamation
    "двойка": "điểm 2, điểm kém, điểm trượt",              # bỏ ngoặc; khớp пятёрка «điểm 5»
    "четвёрка": "điểm 4, điểm khá",                        # bỏ ngoặc
    "кафедра": "bộ môn, bục giảng",                        # bỏ ngoặc; gloss lectern/rostrum
    "политехнический": "bách khoa",                        # bỏ ngoặc
    "гуманитарный": "nhân văn, nhân đạo",                  # gloss humanities / humanitarian
    "ректор": "hiệu trưởng đại học",                       # gỡ ngoặc; «hiệu trưởng» trơn trùng дире́ктор (k69)
    "конспектировать": "ghi tóm tắt",                      # RÚT «ghi chép» — trùng запи́сывать (k11)
}

# ----------------------------------------------------------------- русско-английский
S["русско-английский"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ру́сск-о-</span>'
    '<span class="hd-gloss">gốc <b>ру́сский</b> + nguyên âm nối <i>-о-</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-англи́йский</span>'
    '<span class="hd-gloss">tính từ <b>англи́йский</b>, giữ nguyên</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hai tính từ ghép bằng gạch nối: vế đầu rút về gốc + <i>-о-</i> và đứng yên, '
    'chỉ vế sau biến đổi — <b>в русско-англи́йском словаре́</b>. Thứ tự là chiều dịch: tra Nga ra Anh.</div>'
    '<div class="hd-warn">Chiều ngược lại KHÔNG phải «английско-русский» mà là <b>англо-ру́сский</b> — '
    'vế Anh dùng gốc ngắn <i>англо-</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ру́сский</b> thuộc về Nga · <b>англи́йский</b> thuộc về Anh · '
    '<b>по-ру́сски</b> bằng tiếng Nga</div>'
)

# ----------------------------------------------------------------- оформить
S["оформить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">LÀM CHO CÓ — dựng động từ từ danh từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-фо́рм-</span>'
    '<span class="hd-gloss">KHUÔN, BIỂU MẪU — <b>фо́рма</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đưa vào đúng khuôn» ⇒ làm giấy tờ cho đúng mẫu: <b>офо́рмить ви́зу</b> làm visa, '
    '<b>офо́рмить докуме́нты</b> làm hồ sơ. Cũng là «tạo hình cho» ⇒ trình bày, trang trí.</div>'
    '<div class="hd-warn">Ngôi «tôi» chèn <i>л</i> sau <i>м</i>: <b>офо́рмлю</b>, còn lại <b>офо́рмишь</b>, '
    '<b>офо́рмит</b>. Chữ <i>л</i> ấy nằm sẵn trong vế chưa hoàn thành <b>оформля́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оформля́ть</b> làm thủ tục (chưa HT) · <b>оформле́ние</b> thủ tục; cách trình bày · '
    '<b>фо́рма</b> khuôn, biểu mẫu</div>'
)

# ----------------------------------------------------------------- оформлять
S["оформлять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-фо́рм-</span>'
    '<span class="hd-gloss">đưa vào KHUÔN — như <b>офо́рмить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-л-</span>'
    '<span class="hd-gloss">âm chèn sau <i>м</i>, không mang nghĩa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́ть</span>'
    '<span class="hd-gloss">đuôi kéo về CHƯA hoàn thành, lớp 1</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vế chưa hoàn thành của <b>офо́рмить</b>: thủ tục đang làm, hay làm nhiều lần — '
    '<b>Я сейча́с оформля́ю ви́зу</b> tôi đang làm visa. Chia đều như <b>чита́ть</b>: '
    '<b>оформля́ю</b>, <b>оформля́ешь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>офо́рмить</b> làm xong thủ tục (HT) · <b>оформле́ние</b> thủ tục; cách trình bày · '
    '<b>фо́рма</b> khuôn, biểu mẫu</div>'
)

# ----------------------------------------------------------------- декларация
S["декларация"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">де-клар-</span>'
    '<span class="hd-gloss">Latin <i>declarare</i> — làm cho RÕ (<i>clarus</i>, như <i>clear</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ция</span>'
    '<span class="hd-gloss">= tiếng Anh <i>-ation</i>, danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>declaration</i>: «nói rõ ra» ⇒ bản KHAI rõ mình có gì (thuế, hành lý), '
    'hoặc bản TUYÊN BỐ trịnh trọng. Đuôi <b>-а́ция</b> luôn nhấn ở <b>-а́-</b>.</div>'
    '<div class="hd-warn">Cụm phải thuộc: <b>тамо́женная деклара́ция</b> tờ khai hải quan · '
    '<b>запо́лнить деклара́цию</b> điền tờ khai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>деклари́ровать</b> khai báo (hải quan, thu nhập)</div>'
)

# ----------------------------------------------------------------- двойка
S["двойка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дв-</span>'
    '<span class="hd-gloss">HAI — <b>два</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́йк-а</span>'
    '<span class="hd-gloss">đuôi gọi tên CON SỐ như một vật, như <b>тро́йка</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trường Nga chấm thang 5, nên <b>дво́йка</b> là điểm TRƯỢT: '
    '<b>получи́ть дво́йку</b> bị điểm 2. Cũng dùng cho số xe buýt, quân bài «hai».</div>'
    '<div class="hd-warn">Số nhiều cách 2 đổi <i>й</i> thành <i>е</i>: <b>дво́ек</b> (như <b>копе́йка → копе́ек</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>два</b> hai · <b>дво́е</b> hai người · <b>тро́йка</b> điểm 3 · '
    '<b>пятёрка</b> điểm 5</div>'
)

# ----------------------------------------------------------------- четвёрка
S["четвёрка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">четвёр-</span>'
    '<span class="hd-gloss">BỐN — gốc của <b>четвёртый</b>, <b>че́тверо</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-а</span>'
    '<span class="hd-gloss">đuôi gọi tên CON SỐ như một vật, như <b>пятёрка</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thang 5 điểm: <b>четвёрка</b> là điểm KHÁ, ngay dưới <b>пятёрка</b>. '
    'Gốc có <i>в</i> như <b>четвёртый</b>, không lấy thẳng từ <b>четы́ре</b>; chữ <i>ё</i> luôn mang trọng âm.</div>'
    '<div class="hd-warn">Số nhiều cách 2 chen <i>о</i>: <b>четвёрок</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>четы́ре</b> bốn · <b>четвёртый</b> thứ tư · <b>че́тверо</b> bốn người · '
    '<b>дво́йка</b> điểm 2</div>'
)

# ----------------------------------------------------------------- кафедра
S["кафедра"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga — mượn Hy Lạp <i>kathédra</i> «chiếc ghế ngồi», '
    'cùng gốc với tiếng Anh <i>cathedral</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ghế của thầy giảng ⇒ BỤC GIẢNG ⇒ cái «ghế» giáo sư trong trường ⇒ BỘ MÔN '
    '(tiếng Anh cũng gọi là <i>chair</i>). Một <b>факульте́т</b> chia thành nhiều bộ môn. Trọng âm ở đầu.</div>'
    '<div class="hd-warn">Làm việc ở bộ môn dùng <b>на</b>, như <b>факульте́т</b>: '
    '<b>рабо́тать на ка́федре</b>.</div>'
)

# ----------------------------------------------------------------- произношение
S["произношение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">произ-</span>'
    '<span class="hd-gloss">RA phía trước</span></div>'
    '<div class="hd-row"><span class="hd-piece">-нош-</span>'
    '<span class="hd-gloss">MANG — <i>с → ш</i>, như <b>ношу́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ние</span>'
    '<span class="hd-gloss">đuôi → danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Mang tiếng ra ngoài» ⇒ cách phát âm. Chữ <i>ш</i> là phép đổi <i>с → ш</i> '
    'y như ngôi «tôi» của <b>произноси́ть</b>: <b>произношу́</b>.</div>'
    '<div class="hd-warn"><b>У него́ хоро́шее произноше́ние</b> = anh ấy phát âm tốt.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>произноси́ть</b> phát âm · <b>произнести́</b> phát âm (HT) · '
    '<b>носи́ть</b> mang</div>'
)

# ----------------------------------------------------------------- биологический
S["биологический"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">био-ло́г-</span>'
    '<span class="hd-gloss">học thuyết về SỰ SỐNG — <b>биоло́гия</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ческ-ий</span>'
    '<span class="hd-gloss">«thuộc về» môn đó, = tiếng Anh <i>-ical</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Môn <b>-ия</b> đổi sang <b>-и́ческий</b> là thành tính từ, và trọng âm dời lên '
    '<b>-и́-</b>: <b>биоло́гия → биологи́ческий</b>, <i>biology → biological</i>. '
    'Cùng khuôn: <b>математи́ческий</b>, <b>геологи́ческий</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>биоло́гия</b> sinh học · <b>био́лог</b> nhà sinh học</div>'
)

# ----------------------------------------------------------------- политехнический
S["политехнический"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">поли-</span>'
    '<span class="hd-gloss">NHIỀU (Hy Lạp <i>polys</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-техн-</span>'
    '<span class="hd-gloss">TAY NGHỀ, kỹ thuật — <b>те́хника</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ческ-ий</span>'
    '<span class="hd-gloss">«thuộc về», như <b>биологи́ческий</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Nhiều ngành kỹ thuật» ⇒ bách khoa: <b>политехни́ческий университе́т</b> '
    'trường đại học bách khoa. Tiếng Anh: <i>polytechnic</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>те́хника</b> kỹ thuật, máy móc · <b>техни́ческий</b> thuộc kỹ thuật</div>'
)

# ----------------------------------------------------------------- математический
S["математический"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">математ-</span>'
    '<span class="hd-gloss">môn TOÁN — <b>матема́тика</b> bỏ <i>-ика</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ческ-ий</span>'
    '<span class="hd-gloss">«thuộc về», = tiếng Anh <i>-ical</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Môn <b>-ика</b> cũng dựng tính từ bằng <b>-и́ческий</b>, trọng âm dời từ <b>-ма́-</b> '
    'sang <b>-ти́-</b>: <b>матема́тика → математи́ческий</b>, <i>mathematical</i>. '
    '<b>математи́ческий факульте́т</b> khoa toán.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>матема́тика</b> môn toán · <b>матема́тик</b> nhà toán học</div>'
)

# ----------------------------------------------------------------- университетский
S["университетский"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">университе́т-</span>'
    '<span class="hd-gloss">TRƯỜNG ĐẠI HỌC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ск-ий</span>'
    '<span class="hd-gloss">«thuộc về» — dựng tính từ từ danh từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ + <b>-ский</b>, trọng âm đứng yên ở <b>-те́-</b>: '
    '<b>университе́тский городо́к</b> khu đại học, <b>университе́тское образова́ние</b> học vấn đại học.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>университе́т</b> trường đại học</div>'
)

# ----------------------------------------------------------------- гуманитарный
S["гуманитарный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">гуман-</span>'
    '<span class="hd-gloss">CON NGƯỜI, tính người (Latin <i>humanus</i>, như <i>human</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ита́р-н-ый</span>'
    '<span class="hd-gloss">= tiếng Anh <i>-itarian</i>, đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Về con người» ra hai nghĩa: ngành học về con người — '
    '<b>гуманита́рные нау́ки</b> khoa học nhân văn (đối lập ngành tự nhiên); '
    'và giúp con người — <b>гуманита́рная по́мощь</b> viện trợ nhân đạo.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гума́нный</b> nhân đạo, nhân hậu · <b>гумани́зм</b> chủ nghĩa nhân văn</div>'
)

# ----------------------------------------------------------------- контрольный
S["контрольный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">контро́ль-</span>'
    '<span class="hd-gloss">SỰ KIỂM TRA (Pháp <i>contrôle</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Dùng để kiểm tra»: <b>контро́льный пункт</b> trạm kiểm soát, '
    '<b>контро́льная гру́ппа</b> nhóm đối chứng. Dấu mềm của <b>контро́ль</b> giữ nguyên trước <i>н</i>.</div>'
    '<div class="hd-warn">Ở trường, <b>контро́льная</b> đứng một mình đã là danh từ «bài kiểm tra»: '
    '<b>писа́ть контро́льную</b> làm bài kiểm tra.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>контро́ль</b> sự kiểm soát · <b>контроли́ровать</b> kiểm soát · '
    '<b>контролёр</b> người soát vé</div>'
)

# ----------------------------------------------------------------- семинар
S["семинар"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga — mượn Latin <i>seminarium</i> «vườn ươm» '
    '(<i>semen</i> hạt giống), cùng gốc tiếng Anh <i>seminar</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỗ «ươm» ý tưởng: ở đại học Nga, <b>семина́р</b> là buổi học nhóm nhỏ, sinh viên '
    'trình bày và thảo luận — đi cặp với <b>ле́кция</b>, nơi thầy giảng. Trọng âm ở cuối.</div>'
    '<div class="hd-warn">Dùng <b>на</b>, như <b>ле́кция</b>: <b>на семина́ре</b> ở buổi seminar.</div>'
)

# ----------------------------------------------------------------- ректор
S["ректор"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рек-</span>'
    '<span class="hd-gloss">ĐIỀU KHIỂN (Latin <i>regere</i>, như <i>regime</i>, <i>regulate</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тор</span>'
    '<span class="hd-gloss">NGƯỜI LÀM việc đó, như <b>дире́ктор</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Người điều khiển» trường ĐẠI HỌC. Trường phổ thông thì người đứng đầu là '
    '<b>дире́ктор</b>; khoa có <b>дека́н</b>.</div>'
    '<div class="hd-warn">Số nhiều có HAI dạng song song: <b>ре́кторы</b> (chuẩn) và <b>ректора́</b> '
    '(khẩu ngữ, nhấn cuối như <b>директора́</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>проре́ктор</b> phó hiệu trưởng · <b>дире́ктор</b> giám đốc</div>'
)

# ----------------------------------------------------------------- курсы
S["курсы"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">курс-</span>'
    '<span class="hd-gloss">KHOÁ, đường đi — <b>курс</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ы</span>'
    '<span class="hd-gloss">đuôi số nhiều</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Số nhiều <b>ку́рсы</b> mang nghĩa riêng: lớp học NGẮN HẠN ngoài trường chính — '
    '<b>ку́рсы англи́йского языка́</b> lớp tiếng Anh. Đi học là <b>ходи́ть на ку́рсы</b>.</div>'
    '<div class="hd-warn">Đừng lẫn: <b>на ку́рсах</b> = ở lớp học ngắn hạn · '
    '<b>на пе́рвом ку́рсе</b> (số ít) = sinh viên năm thứ nhất.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>курс</b> khoá học, năm học · <b>курсова́я</b> tiểu luận môn học</div>'
)

# ----------------------------------------------------------------- конспектировать
S["конспектировать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">конспе́кт-</span>'
    '<span class="hd-gloss">BẢN TÓM TẮT bài (Latin <i>conspectus</i> «cái nhìn bao quát»)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ровать</span>'
    '<span class="hd-gloss">đuôi dựng động từ từ từ mượn</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm ra <b>конспе́кт</b> ⇒ ghi tóm ý chính của bài giảng, của sách. '
    'Đuôi <b>-и́ровать</b> chia bỏ <i>-ова-</i> thành <i>-у-</i>: <b>конспекти́рую</b>, '
    '<b>конспекти́руешь</b> — như <b>контроли́ровать</b>.</div>'
    '<div class="hd-warn">Khác <b>запи́сывать</b>: ghi lại nguyên văn. <b>конспекти́ровать</b> là CHẮT ý, '
    'viết ngắn lại.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>конспе́кт</b> bản tóm tắt, vở ghi bài · '
    '<b>законспекти́ровать</b> ghi tóm tắt xong (HT)</div>'
)

B = {
    "docbangmat": 67,
    "loitubat": 3,   # произноше́ние: lỡ viết «dựng từ ngôi tôi» (sai cơ chế — chỉ là cùng phép с→ш) · о- của офо́рмить ghi «bao quanh» (sai, đây là о- dựng động từ từ danh từ) · ка́федра: lỡ để danh từ cách 1 sau «nhiều»
    "nguonsai": 1,   # гуманита́рный: máy báo dạng ngắn «bất thường» nhưng гуманита́рен chèn е là ĐÚNG quy tắc -рный ⇒ không viết câu chú ý
    "baolen": [
        "ректор V='hiệu trưởng đại học': gỡ ngoặc «(trường đại học)» thành một cụm, không thêm chữ mới; «hiệu trưởng» trơn trùng дире́ктор (k69), cả hai đều danh từ giống đực nên badge không tách. Cần duyệt.",
        "декларация V='bản khai, bản tuyên ngôn': rút «tờ khai» (trùng анке́та k100); «bản tuyên ngôn» lấy từ gloss proclamation/declaration — cần duyệt.",
        "конспектировать V='ghi tóm tắt': rút «ghi chép» (trùng запи́сывать k11). Còn đúng một nghĩa, nhưng đủ tách.",
        "оформить/оформлять V cùng 'làm giấy tờ, làm thủ tục' (оформлять giữ nguyên field cũ, оформить bỏ «xong/hoàn tất» vì là nhãn thể trá hình) — badge THỂ tách hai thẻ.",
        "гуманитарный V='nhân văn, nhân đạo' viết lại từ gloss humanities/humanitarian; chưa soi được field của thẻ khác (nếu có гума́нный) có «nhân đạo» không — cache _vacham_vi.txt chỉ ghi cụm đã trùng.",
        "двойка: ví dụ nguyên âm chạy đổi từ ча́йка→ча́ек sang копе́йка→копе́ек vì từ điển đọc «чаек» thành чаёк (đồng tự) — KHÔNG nới MIEN_TRU.",
        "Không chắc tuyệt đối: ре́кторы (chuẩn) / ректора́ (khẩu ngữ) — từ điển in cả hai song song, nhãn «chuẩn/khẩu ngữ» là theo từ điển chính tả Nga, không phải máy xác nhận.",
        "Bỏ «Поли́тех» (tên gọi tắt) khỏi thẻ политехнический vì không chắc chỗ trọng âm.",
    ],
}
