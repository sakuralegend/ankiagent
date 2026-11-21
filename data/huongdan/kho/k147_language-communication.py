# -*- coding: utf-8 -*-
"""k147 — language::communication: dạy/nuôi dạy, khen/chê, hỏi ý kiến, kết thúc + họ геология.

Chỗ cần nhất quán trong lô:
(1) воспитать/воспитывать: вос- LÊN + -пит- NUÔI — khớp воспитание (k135); -ыва- kéo trọng âm về пи́.
(2) обучать/обучить: о- không tách nghĩa + -уч- — khớp учить (k11), научить (k81), cặp а/и như изучать.
(3) геология = gốc; bỏ -ия ⇒ người (геолог); -ический = -ical ⇒ tính từ (khớp теоретический k141).
(4) советоваться/посоветоваться: -ся lật chiều сове́товать (k97): KHUYÊN → HỎI Ý KIẾN, с + cách 5.
(5) оканчиваться/окончиться: о→а khi thêm -ива- — khớp оканчивать (k100), окончить (k87).
(6) хвалить/ругать/критиковать: cùng khuôn «AI cách 4, VÌ GÌ за + cách 4».
Họ hàng cố ý vắng: сессия, диссертация (từ mượn đứng một mình).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "воспитать": "nuôi dạy, giáo dục",            # «nuôi dạy thành» cụt ý; gloss raise / bring up
    "воспитывать": "nuôi dạy, giáo dục",          # bỏ «(con)»; badge thể tách khỏi воспита́ть
    "обучить": "dạy, huấn luyện",                 # bỏ «(xong)»; badge thể tách khỏi обуча́ть
    "сессия": "kỳ thi, mùa thi, phiên họp",       # bỏ ngoặc; gloss exam period / session / sitting
    "устный": "bằng miệng, bằng lời, vấn đáp",    # ngoặc → nghĩa rời: у́стный экза́мен = thi vấn đáp
    "похвалить": "khen, khen ngợi",               # bỏ «(một lần)»
    "посоветоваться": "hỏi ý kiến, xin lời khuyên",  # «bàn với ai» = cách chi phối trá hình; gloss seek counseling
    "окончиться": "kết thúc, chấm dứt",           # bỏ «(xong)»
}

# ----------------------------------------------------------------- воспитать
S["воспитать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вос-</span>'
    '<span class="hd-gloss">LÊN (dạng của <b>воз-</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пит-</span>'
    '<span class="hd-gloss">NUÔI — gốc của <b>пита́ние</b> dinh dưỡng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Nuôi cho LỚN LÊN» ⇒ nuôi dạy thành người, cùng khuôn <b>воспита́ние</b>. '
    'Đây là bản HOÀN THÀNH — đã nuôi dạy xong: <i>Она́ воспита́ла трои́х дете́й.</i> '
    'Cặp CHT: <b>воспи́тывать</b>.</div>'
    '<div class="hd-warn"><b>воспи́танный</b> (phân từ của chính từ này) = LỄ PHÉP, có giáo dục '
    '— trọng âm lùi về <b>пи́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>воспита́ние</b> sự nuôi dạy · <b>воспи́тывать</b> nuôi dạy (CHT) · '
    '<b>воспита́тель</b> cô giáo mầm non · <b>пита́ние</b> dinh dưỡng</div>'
)

# ----------------------------------------------------------------- воспитывать
S["воспитывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">воспит-</span>'
    '<span class="hd-gloss">NUÔI cho LỚN LÊN — như <b>воспита́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-ть</span>'
    '<span class="hd-gloss">hậu tố → thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>-ыва-</b> biến <b>воспита́ть</b> thành bản CHT và kéo trọng âm lùi về '
    '<b>пи́</b>: <b>воспи́тываю</b>. Dùng cho việc nuôi dạy kéo dài nhiều năm: '
    '<i>Ба́бушка воспи́тывает вну́ка.</i></div>'
    '<div class="hd-warn">Dạy NẾT là <b>воспи́тывать</b>; dạy KIẾN THỨC, kỹ năng là '
    '<b>обуча́ть</b> — đúng như cặp <b>воспита́ние</b> / <b>обуче́ние</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>воспита́ть</b> nuôi dạy (HT) · <b>воспита́ние</b> sự nuôi dạy · '
    '<b>пита́ние</b> dinh dưỡng</div>'
)

# ----------------------------------------------------------------- обучать
S["обучать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không tách ra nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-уч-</span>'
    '<span class="hd-gloss">DẠY / HỌC — gốc của <b>учи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vẫn là <b>учи́ть</b> theo nghĩa DẠY, nhưng bài bản: đào tạo nghề, huấn '
    'luyện kỹ năng. Cặp HT <b>обучи́ть</b> chỉ khác nguyên âm đuôi, y như '
    '<b>изуча́ть</b> / <b>изучи́ть</b>.</div>'
    '<div class="hd-warn">Kết cấu như <b>учи́ть</b>: dạy AI ⇒ cách 4, dạy MÔN gì ⇒ cách 3 — '
    '<b>обуча́ть дете́й пла́ванию</b> dạy trẻ bơi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обучи́ть</b> dạy (HT) · <b>обуче́ние</b> việc đào tạo · '
    '<b>учи́ть</b> học, dạy · <b>уче́бник</b> sách giáo khoa</div>'
)

# ----------------------------------------------------------------- обучить
S["обучить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không tách ra nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-уч-</span>'
    '<span class="hd-gloss">DẠY — gốc của <b>учи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bản HOÀN THÀNH của <b>обуча́ть</b>: dạy tới lúc người ta làm được. Gần '
    '<b>научи́ть</b>, nhưng mang sắc chính quy — đào tạo nhân viên, huấn luyện lính. Kết cấu như '
    '<b>обуча́ть</b>: AI cách 4, MÔN cách 3.</div>'
    '<div class="hd-warn">Trọng âm nhảy về trước ở mọi ngôi trừ TÔI: <b>я обучу́</b> nhưng '
    '<b>ты обу́чишь, они́ обу́чат</b> — y như <b>научи́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обуча́ть</b> dạy (CHT) · <b>научи́ть</b> dạy cho biết làm · '
    '<b>учи́ть</b> học, dạy · <b>обуче́ние</b> việc đào tạo</div>'
)

# ----------------------------------------------------------------- геология
S["геология"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">гео-</span>'
    '<span class="hd-gloss">ĐẤT, Trái Đất (Hy Lạp <i>gē</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лог-</span>'
    '<span class="hd-gloss">LỜI, MÔN NGHIÊN CỨU (Hy Lạp <i>logos</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ия</span>'
    '<span class="hd-gloss">→ danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>geology</i>. Đuôi <b>-ло́гия</b> = <i>-logy</i>, luôn nhấn '
    '<b>ло́</b>: <b>биоло́гия</b>, <b>психоло́гия</b>. Từ đây ra hai từ theo khuôn cố định: bỏ '
    '<b>-ия</b> ⇒ NGƯỜI (<b>гео́лог</b>); thay bằng <b>-и́ческий</b> ⇒ TÍNH TỪ '
    '(<b>геологи́ческий</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гео́лог</b> nhà địa chất · <b>геологи́ческий</b> thuộc địa chất · '
    '<b>геогра́фия</b> địa lý · <b>биоло́гия</b> sinh học</div>'
)

# ----------------------------------------------------------------- геолог
S["геолог"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">гео-</span>'
    '<span class="hd-gloss">ĐẤT</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лог</span>'
    '<span class="hd-gloss">NGƯỜI theo môn ấy — <b>геоло́гия</b> bỏ <b>-ия</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bỏ đuôi môn học <b>-ия</b> là ra người làm môn đó: '
    '<b>геоло́гия → гео́лог</b>, y như <b>психоло́гия → психо́лог</b>. Để ý trọng âm lùi một '
    'bậc, về <b>гео́-</b>.</div>'
    '<div class="hd-warn">Tên nghề nên phụ nữ vẫn dùng dạng giống đực: '
    '<b>Она́ — гео́лог.</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>геоло́гия</b> địa chất học · <b>геологи́ческий</b> thuộc địa chất · '
    '<b>психо́лог</b> nhà tâm lý học</div>'
)

# ----------------------------------------------------------------- геологический
S["геологический"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">геолог-</span>'
    '<span class="hd-gloss">ĐỊA CHẤT — <b>геоло́гия</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ческий</span>'
    '<span class="hd-gloss">= tiếng Anh <i>-ical</i> → tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>geological</i>. Đuôi <b>-и́ческий</b> luôn mang trọng âm ở '
    '<b>и́</b>, nên trọng âm rời <b>ло́</b> của <b>геоло́гия</b> mà dịch về sau. Cùng khuôn: '
    '<b>биоло́гия → биологи́ческий</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>геоло́гия</b> địa chất học · <b>гео́лог</b> nhà địa chất · cùng đuôi: '
    '<b>биологи́ческий</b> sinh học, <b>истори́ческий</b> lịch sử</div>'
)

# ----------------------------------------------------------------- сессия
S["сессия"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ mượn (Latin <i>sessio</i> «sự ngồi»), không chẻ được — chính là '
    '<i>session</i>: buổi ngồi họp (<b>се́ссия парла́мента</b>). Với sinh viên Nga, nó là cả '
    'ĐỢT THI cuối học kỳ, nhiều môn liền nhau.</div>'
    '<div class="hd-warn"><b>сдать се́ссию</b> = thi qua hết đợt thi — câu sinh viên nói hằng '
    'ngày.</div>'
)

# ----------------------------------------------------------------- диссертация
S["диссертация"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ mượn (Latin <i>dissertatio</i>), không chẻ được — chính là '
    '<i>dissertation</i>. Đuôi <i>-ation</i> thành <b>-а́ция</b>, nhấn ở <b>а́</b>, như '
    '<b>консульта́ция</b>.</div>'
    '<div class="hd-warn">Bảo vệ luận án = <b>защити́ть диссерта́цию</b> — dùng đúng động từ '
    '«bảo vệ» như tiếng Việt.</div>'
)

# ----------------------------------------------------------------- пословица
S["пословица"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không tách ra nghĩa rõ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-слов-</span>'
    '<span class="hd-gloss">LỜI — chính là <b>сло́во</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-иц-а</span>'
    '<span class="hd-gloss">→ danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một «lời» đã thành khuôn, ai cũng nói theo ⇒ tục ngữ. Trọng âm giữ ở '
    '<b>сло́</b> như trong <b>сло́во</b>.</div>'
    '<div class="hd-warn"><b>Как говори́тся в посло́вице, …</b> = như tục ngữ có câu…</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сло́во</b> từ, lời · <b>слова́рь</b> từ điển · '
    '<b>сло́вно</b> như thể</div>'
)

# ----------------------------------------------------------------- устный
S["устный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">уст-</span>'
    '<span class="hd-gloss">MIỆNG — <b>уста́</b> (từ cổ, văn thơ)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">→ tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thuộc về miệng» ⇒ nói ra bằng miệng, không viết. Đối lại là '
    '<b>пи́сьменный</b> (từ <b>письмо́</b>) = bằng văn bản.</div>'
    '<div class="hd-warn"><b>у́стный экза́мен</b> thi vấn đáp · <b>пи́сьменный экза́мен</b> '
    'thi viết.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>у́стно</b> bằng miệng · <b>у́стье</b> cửa sông («miệng» sông) · '
    '<b>уста́</b> môi miệng (văn thơ)</div>'
)

# ----------------------------------------------------------------- критиковать
S["критиковать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">критик-</span>'
    '<span class="hd-gloss">PHÊ BÌNH — <b>кри́тика</b>, tiếng Anh <i>critic</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-ть</span>'
    '<span class="hd-gloss">đuôi biến danh từ thành động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>criticize</i>. Như mọi động từ <b>-ова́ть</b>, ở hiện tại '
    '<b>-ова-</b> đổi thành <b>-у-</b>: <b>критику́ю, критику́ешь</b>. Cặp HT: '
    '<b>покритикова́ть</b>.</div>'
    '<div class="hd-warn">Chê AI ⇒ cách 4, chê VÌ cái gì ⇒ <b>за</b> + cách 4: '
    '<b>критикова́ть его́ за оши́бки</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кри́тика</b> lời phê bình · <b>кри́тик</b> nhà phê bình · '
    '<b>крити́ческий</b> phê phán; nguy kịch</div>'
)

# ----------------------------------------------------------------- ругать
S["ругать"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc trơn <b>руг-</b>, không chẻ được. Mắng AI ⇒ cách 4, VÌ gì ⇒ '
    '<b>за</b> + cách 4 — cùng khuôn <b>критикова́ть</b>: <i>Ма́ма руга́ет сы́на за дво́йку.</i> '
    'Chia đều: <b>руга́ю</b>. Một bản HT hay gặp: <b>отруга́ть</b>.</div>'
    '<div class="hd-warn">Thêm <b>-ся</b> là nghĩa khác hẳn: <b>руга́ться</b> = CÃI NHAU '
    '(<b>с</b> + cách 5) hoặc chửi thề — không còn là mắng ai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>руга́ться</b> cãi nhau, chửi thề · <b>ру́гань</b> lời chửi bới</div>'
)

# ----------------------------------------------------------------- хвалить
S["хвалить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">хвал-</span>'
    '<span class="hd-gloss">KHEN — gốc của <b>похвала́</b> lời khen</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Khen AI ⇒ cách 4, VÌ gì ⇒ <b>за</b> + cách 4 — đúng khuôn ngược của '
    '<b>руга́ть</b>: <i>Учи́тель хва́лит её за рабо́ту.</i> Cặp HT: <b>похвали́ть</b>.</div>'
    '<div class="hd-warn">Trọng âm nhảy về trước ở mọi ngôi trừ TÔI: <b>я хвалю́</b> nhưng '
    '<b>ты хва́лишь, они́ хва́лят</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>похвали́ть</b> khen (HT) · <b>похвала́</b> lời khen · '
    '<b>хвала́</b> lời ca ngợi</div>'
)

# ----------------------------------------------------------------- похвалить
S["похвалить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">đánh dấu XONG, không thêm nghĩa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-хвали́ть</span>'
    '<span class="hd-gloss">chính là <b>хвали́ть</b> — khen</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một lời khen cụ thể, một lần: <i>Нача́льник похвали́л меня́.</i> '
    'Trọng âm nhảy y như <b>хвали́ть</b>: <b>похвалю́</b> nhưng <b>похва́лишь, похва́лят</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>хвали́ть</b> khen (CHT) · <b>похвала́</b> lời khen</div>'
)

# ----------------------------------------------------------------- советоваться
S["советоваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">совет-</span>'
    '<span class="hd-gloss">LỜI KHUYÊN — <b>сове́т</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-ть</span>'
    '<span class="hd-gloss">đuôi biến danh từ thành động từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">quay về phía mình: KHUYÊN → XIN lời khuyên</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>сове́товать</b> là đưa lời khuyên cho người khác; thêm <b>-ся</b> thì '
    'chiều ngược lại — mình đi hỏi ý kiến người ta. Chia như mọi <b>-овать</b>: '
    '<b>сове́туюсь</b>.</div>'
    '<div class="hd-warn">Hỏi ý kiến AI ⇒ <b>с</b> + cách 5, không phải cách 3 như '
    '<b>сове́товать</b>: <b>сове́товаться с врачо́м</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сове́т</b> lời khuyên · <b>сове́товать</b> khuyên · '
    '<b>посове́товаться</b> hỏi ý kiến (HT)</div>'
)

# ----------------------------------------------------------------- посоветоваться
S["посоветоваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">đánh dấu XONG, không thêm nghĩa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сове́товаться</span>'
    '<span class="hd-gloss">chính là <b>сове́товаться</b> — hỏi ý kiến</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hỏi ý kiến một lần cụ thể: <i>Мне ну́жно посове́товаться с ма́мой.</i> '
    'Mình cần hỏi ý mẹ.</div>'
    '<div class="hd-warn">Đừng lẫn <b>посове́товать</b>: có <b>-ся</b> = hỏi ý kiến (<b>с</b> + '
    'cách 5); không <b>-ся</b> = khuyên ai (cách 3) — <b>посове́товать дру́гу</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сове́товаться</b> hỏi ý kiến (CHT) · <b>посове́товать</b> khuyên · '
    '<b>сове́т</b> lời khuyên</div>'
)

# ----------------------------------------------------------------- ежедневный
S["ежедневный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">еже-</span>'
    '<span class="hd-gloss">MỖI — tiền tố cổ, nay chỉ còn trong từ chỉ thời gian</span></div>'
    '<div class="hd-row"><span class="hd-piece">-днев-</span>'
    '<span class="hd-gloss">NGÀY — <b>день</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">→ tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Mỗi ngày» ⇒ hằng ngày. <b>еже-</b> ghép được với mọi đơn vị thời gian: '
    '<b>ежего́дный</b> hằng năm, <b>ежеме́сячный</b> hằng tháng, <b>еженеде́льный</b> hằng tuần. '
    'Trạng từ: <b>ежедне́вно</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>день</b> ngày · <b>ежего́дный</b> hằng năm · '
    '<b>дневни́к</b> nhật ký</div>'
)

# ----------------------------------------------------------------- ежегодный
S["ежегодный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">еже-</span>'
    '<span class="hd-gloss">MỖI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-год-</span>'
    '<span class="hd-gloss">NĂM — <b>год</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">→ tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Mỗi năm» ⇒ hằng năm, thường niên — cùng khuôn <b>ежедне́вный</b>. '
    '<b>ежего́дный о́тпуск</b> = kỳ nghỉ phép năm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>год</b> năm · <b>ежедне́вный</b> hằng ngày · '
    '<b>ежего́дно</b> hằng năm</div>'
)

# ----------------------------------------------------------------- оканчиваться
S["оканчиваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không tách ra nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка́нч-</span>'
    '<span class="hd-gloss">gốc KẾT THÚC — <b>конч-</b> của <b>коне́ц</b>, о hoá а</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ть-ся</span>'
    '<span class="hd-gloss">thể chưa hoàn thành + TỰ nó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>ока́нчивать</b> là người làm xong (tốt nghiệp); thêm <b>-ся</b> thì '
    'sự việc TỰ đi tới <b>коне́ц</b>: <i>Уро́к ока́нчивается в три.</i> Sắc trang trọng hơn '
    '<b>конча́ться</b>. Cặp HT: <b>око́нчиться</b>.</div>'
    '<div class="hd-warn"><b>ока́нчиваться на</b> + cách 4 = CÓ ĐUÔI là… — '
    '<b>Сло́во ока́нчивается на «а»</b>. Cùng nghĩa với <b>оконча́ние</b> «đuôi từ» trong ngữ '
    'pháp.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ока́нчивать</b> tốt nghiệp · <b>око́нчиться</b> kết thúc (HT) · '
    '<b>оконча́ние</b> phần kết; đuôi từ · <b>коне́ц</b> phần cuối</div>'
)

# ----------------------------------------------------------------- окончиться
S["окончиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">око́нчи-ть</span>'
    '<span class="hd-gloss">chính là <b>око́нчить</b> — đi trọn tới <b>коне́ц</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">TỰ nó — không ai làm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Sự việc tự đi tới <b>коне́ц</b>, một lần là xong: '
    '<i>Конце́рт око́нчился.</i> Buổi hoà nhạc đã kết thúc. Trang trọng hơn <b>ко́нчиться</b>. '
    'Cặp CHT: <b>ока́нчиваться</b>.</div>'
    '<div class="hd-warn">Người LÀM xong thì không <b>-ся</b>: <b>Он око́нчил шко́лу</b> (tốt '
    'nghiệp). Việc TỰ hết mới có <b>-ся</b>: <b>Уро́к око́нчился</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>око́нчить</b> tốt nghiệp · <b>ока́нчиваться</b> kết thúc (CHT) · '
    '<b>ко́нчиться</b> hết · <b>коне́ц</b> phần cuối</div>'
)

B = {
    "docbangmat": 70,
    "loitubat": 3,   # геолог: định viết «trọng âm ло́ → е́» (sai, гео́лог nhấn о của гео-) → «lùi một bậc, về гео́-»
                     # оканчиваться: định viết «chính nghĩa này cho ra оконча́ние» (khẳng định từ nguyên quá mức) → «cùng nghĩa với»
                     # воспитать: định gọi -а́ть là «đuôi thể hoàn thành» (sai: thể do cặp -ыва- quyết định) → «đuôi nguyên thể»
    "nguonsai": 0,
    "baolen": [
        "VA CHAM KHONG GO BANG RUT GON: обучать 'dạy, huấn luyện' ↔ учить (k11) 'học, dạy' — chung «dạy», nhưng «dạy» là nghĩa lõi (gloss teach), không phải nới rộng; cả dòng vẫn khác nhau (§2c: «huấn luyện» vs «học»). GIỮ NGUYÊN, cần user duyệt",
        "VA CHAM KHONG GO BANG RUT GON: обучить 'dạy, huấn luyện' ↔ научить (k81) 'dạy, dạy cho biết làm' (chung «dạy») và ↔ подготовить (k81) 'chuẩn bị trước, huấn luyện' (chung «huấn luyện»). Rút cái nào cũng thành tập con của từ kia ⇒ tệ hơn; cả dòng ba từ đều khác nhau. Chỉ bỏ «(xong)»",
        "VA CHAM KHONG GO BANG RUT GON: оканчиваться 'kết thúc, chấm dứt' ↔ кончаться (k87) 'hết sạch, cạn kiệt, kết thúc' — «kết thúc» là nghĩa lõi (gloss to end); rút đi chỉ còn «chấm dứt» thì nghèo nghĩa. GIỮ NGUYÊN. Đề xuất (KHÔNG tự làm): thêm «kết thúc bằng» — gloss có end in / end with, là nghĩa riêng của оканчиваться на",
        "VA CHAM KHONG GO BANG RUT GON: окончиться 'kết thúc, chấm dứt' ↔ кончиться (k87) 'hết sạch, cạn kiệt, kết thúc' — như trên; chỉ bỏ «(xong)». «chấm dứt» là chữ tách được khỏi кончиться",
        "V CAN DUYET (thêm chữ từ gloss, chưa soát được toàn bộ sưu tập vì không đụng Anki — cần chạy `vacham`): сессия 'kỳ thi, mùa thi, phiên họp' (gloss exam period / session / sitting) · посоветоваться 'hỏi ý kiến, xin lời khuyên' (thay «bàn với ai» = cách chi phối trá hình; gloss seek counseling) · устный 'bằng miệng, bằng lời, vấn đáp' (đưa «vấn đáp» từ ngoặc ra thành nghĩa)",
        "GIU «giáo dục» ở воспитать/воспитывать dù trùng образование: khác từ loại (badge PoS tách). k135 bỏ «giáo dục» ở воспитание vì đó là danh từ trùng PoS với образование",
        "KHONG CHAC: ругать — bản HT ghi «một bản hay gặp: отруга́ть» (từ điển liệt kê 5 partner: обруга́ть, вы́ругать, заруга́ть, отруга́ть, ругну́ть), cố ý không khẳng định là cặp duy nhất",
        "KHONG CHAC: пословица — по- ghi «không tách ra nghĩa rõ»; еже- mô tả theo chức năng (MỖI), không khẳng định từ nguyên",
        "HO HANG CO Y VANG: сессия, диссертация (từ mượn đứng một mình, không có từ phái sinh Nga trong bộ sưu tập)",
    ],
}
