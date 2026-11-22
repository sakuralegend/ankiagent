# -*- coding: utf-8 -*-
"""k194 — people::professions (lô trộn): nghề nghiệp, con người, vài danh từ trừu tượng.

Chỗ cần nhất quán trong lô:
(1) Khuôn «-ник = người làm việc đó» chung cho сою́зник và защи́тник — chẻ cùng kiểu.
(2) Cặp моли́ться / помоли́ться soạn THÀNH ĐÔI; bảng chia (trọng âm dịch) nói ở thẻ CHT,
    thẻ HT chỉ dẫn chiếu.
(3) веду́щий = DANH TỪ «người dẫn chương trình» (luồng chính chốt); nghĩa tính từ
    «hàng đầu» chỉ nhắc trong Cách nhớ.
(4) Họ từ đã có thẻ, giữ cách chẻ: вне́шний (вне + -шн-), сою́з (со- + -юз), защити́ть
    (за- ra SAU + щит KHIÊN — theo k125), служи́ть (служ- ← слуга́), следи́ть (след- DẤU VẾT),
    предприя́тие (пред- + при-я/ним-).
Họ hàng cố ý vắng: аукцио́н (từ mượn Latin đứng một mình, không phái sinh thông dụng).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "гибель": "sự chết, sự tử vong, sự bỏ mạng, sự diệt vong, sự hủy diệt, sự sụp đổ",  # THIẾU destruction/ruin/collapse
    "нация": "dân tộc, quốc gia",                                     # bỏ «nhân dân» — đó là народ; "people" ở đây = một dân tộc
    "помолиться": "cầu nguyện, đọc lời cầu nguyện",                   # bỏ «một lúc» (sắc thái thể, badge đã nói)
    "ведущий": "người dẫn chương trình, MC, người dẫn bản tin, người phụ trách",  # «phát thanh viên dẫn» cụt; anchor, person in charge
    "деловой": "công việc, kinh doanh, công sở, chuyên nghiệp, thiết thực",       # THIẾU business (nghĩa chính); practical
    "предприниматель": "doanh nhân, chủ doanh nghiệp, nhà khởi nghiệp",       # va chạm бизнесмен [k35]: CẤM cắt nghĩa chính (user 22/11) — báo user
}

# --------------------------------------------------------------------- ножка
S["ножка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">нож-</span>'
    '<span class="hd-gloss">CHÂN — chính là <b>нога́</b>, <b>г → ж</b> trước hậu tố</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-а</span>'
    '<span class="hd-gloss">hậu tố NHỎ, giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cái chân nhỏ» ⇒ chân bàn, chân ghế, cuống hoa, thân nấm; '
    '<b>ку́риная но́жка</b> là đùi gà. Cách 2 số nhiều chèn <i>е</i>: <b>но́жек</b>.</div>'
    '<div class="hd-warn"><b>но́жка</b> (từ <b>нога́</b>) ≠ <b>но́жик</b> con dao nhỏ (từ '
    '<b>нож</b>) — cùng mặt chữ <i>нож-</i>, khác gốc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>нога́</b> chân · <b>подно́жка</b> bậc lên xe; cú ngáng chân · '
    '<b>босоно́жки</b> dép quai hậu</div>'
)

# --------------------------------------------------------------------- внешность
S["внешность"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вне</span>'
    '<span class="hd-gloss">Ở NGOÀI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-шн-</span>'
    '<span class="hd-gloss">→ tính từ <b>вне́шний</b> bên ngoài</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ость</span>'
    '<span class="hd-gloss">→ danh từ trừu tượng, giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cái thuộc về bên ngoài» của một người ⇒ ngoại hình, vẻ ngoài: '
    '<b>прия́тная вне́шность</b> ngoại hình dễ mến. Đuôi <b>-ость</b> nên luôn giống cái.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вне́шний</b> bên ngoài · <b>вне́шне</b> bề ngoài thì · '
    '<b>вне</b> ngoài · <b>извне́</b> từ bên ngoài</div>'
)

# --------------------------------------------------------------------- старуха
S["старуха"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">стар-</span>'
    '<span class="hd-gloss">GIÀ — từ <b>ста́рый</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-у́х-а</span>'
    '<span class="hd-gloss">hậu tố khẩu ngữ, ở đây chỉ người NỮ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vế nữ của <b>стари́к</b> ông già: cùng gốc, đổi hậu tố. Trọng âm '
    'đứng yên trên <b>-у́-</b> ở mọi dạng.</div>'
    '<div class="hd-warn">Nói thẳng mặt thì nghe sỗ. Lịch sự: <b>пожила́я же́нщина</b> người '
    'phụ nữ lớn tuổi, hoặc gọi thân <b>ба́бушка</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ста́рый</b> già, cũ · <b>стари́к</b> ông già · <b>ста́рость</b> '
    'tuổi già · <b>старе́ть</b> già đi</div>'
)

# --------------------------------------------------------------------- гибель
S["гибель"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">гиб-</span>'
    '<span class="hd-gloss">DIỆT VONG — gốc của <b>поги́бнуть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ель</span>'
    '<span class="hd-gloss">đuôi danh từ, ở đây GIỐNG CÁI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>поги́бнуть</b>: cái chết vì tai nạn, chiến tranh, '
    'thảm hoạ — không phải chết già. Dùng cả cho vật: <b>ги́бель корабля́</b> vụ đắm tàu, '
    '<b>ги́бель цивилиза́ции</b> sự diệt vong của một nền văn minh.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поги́бнуть</b> bỏ mạng (HT) · <b>погиба́ть</b> (CHT) · '
    '<b>ги́бнуть</b> tiêu vong · <b>поги́бший</b> người tử nạn</div>'
)

# --------------------------------------------------------------------- союзник
S["союзник"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">CÙNG, chung với nhau</span></div>'
    '<div class="hd-row"><span class="hd-piece">-юз-</span>'
    '<span class="hd-gloss">BUỘC, thắt lại — như trong <b>сою́з</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ник</span>'
    '<span class="hd-gloss">NGƯỜI gắn với việc đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Người cùng buộc vào một mối» ⇒ đồng minh, giữa nước với nước hay '
    'người với người. Cùng khuôn <b>-ник</b> với <b>защи́тник</b> trong lô này.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сою́з</b> liên minh · <b>сою́зница</b> nữ đồng minh · '
    '<b>сою́зный</b> thuộc liên minh, liên bang</div>'
)

# --------------------------------------------------------------------- защитник
S["защитник"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">ra SAU — như giới từ <b>за</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-щит-</span>'
    '<span class="hd-gloss"><b>щит</b> tấm KHIÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ник</span>'
    '<span class="hd-gloss">NGƯỜI làm việc đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người cho kẻ khác nấp SAU tấm khiên của mình ⇒ người bảo vệ. Một hình '
    'ảnh, ba chỗ dùng: hậu vệ trên sân bóng, luật sư bào chữa ở toà, người che chở.</div>'
    '<div class="hd-warn"><b>День защи́тника Оте́чества</b> (23/2) — Ngày Bảo vệ Tổ quốc, ở Nga '
    'thành ngày chúc mừng đàn ông.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>щит</b> tấm khiên · <b>защи́та</b> sự bảo vệ · <b>защити́ть</b> / '
    '<b>защища́ть</b> bảo vệ</div>'
)

# --------------------------------------------------------------------- нация
S["нация"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на́ц-</span>'
    '<span class="hd-gloss">Latin <i>natio</i> «nòi giống, sự sinh ra» — như <i>native</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ия</span>'
    '<span class="hd-gloss"><i>-ция</i> = tiếng Anh <i>-tion</i>, danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>nation</i>: cộng đồng cùng nòi giống ⇒ dân tộc; trong tên '
    'tổ chức thì là quốc gia — <b>Организа́ция Объединённых На́ций</b> Liên Hợp Quốc.</div>'
    '<div class="hd-warn"><b>на́ция</b> = dân tộc như một khối · <b>наро́д</b> = nhân dân, người '
    'dân, đám đông.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>национа́льный</b> thuộc dân tộc · <b>национа́льность</b> thành phần '
    'dân tộc · <b>интернациона́льный</b> quốc tế</div>'
)

# --------------------------------------------------------------------- молиться
S["молиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мол-</span>'
    '<span class="hd-gloss">KHẨN CẦU — gốc Slav trơn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-ть</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">phản thân</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>моли́ть</b> = van xin ai; thêm <b>-ся</b> ⇒ cầu nguyện. Ngôi «tôi» '
    'nhấn đuôi, các ngôi khác lùi về thân: <b>молю́сь</b>, nhưng <b>мо́лишься</b>, '
    '<b>мо́лятся</b>. Cặp thể: <b>моли́ться</b> / <b>помоли́ться</b>.</div>'
    '<div class="hd-warn">Cầu với AI → cách 3: <b>моли́ться Бо́гу</b> · cầu CHO ai → <b>за</b> + '
    'cách 4: <b>моли́ться за дете́й</b> · <b>на</b> + cách 4 = tôn sùng như thần.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>моли́тва</b> lời cầu nguyện · <b>мольба́</b> lời khẩn cầu · '
    '<b>умоля́ть</b> van nài</div>'
)

# --------------------------------------------------------------------- помолиться
S["помолиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố thể hoàn thành, không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">моли́ться</span>'
    '<span class="hd-gloss">cầu nguyện</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vế HT của <b>моли́ться</b>: cầu nguyện xong một lần. Chia và đòi cách '
    'y hệt — trọng âm cũng dịch: <b>помолю́сь</b>, <b>помо́лишься</b>. '
    '<b>Помоли́сь за меня́</b> — cầu nguyện cho tôi nhé.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>моли́ться</b> cầu nguyện (CHT) · <b>моли́тва</b> lời cầu nguyện</div>'
)

# --------------------------------------------------------------------- обслуживание
S["обслуживание"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">phủ lên trọn một đối tượng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-служ-</span>'
    '<span class="hd-gloss">PHỤC VỤ — từ <b>слуга́</b> đầy tớ, <b>г→ж</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ние</span>'
    '<span class="hd-gloss">đuôi CHT <b>обслу́живать</b> → danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>служи́ть</b> phục vụ AI → cách 3; thêm <b>об-</b> thì nhận thẳng '
    'cách 4: <b>обслу́живать клие́нтов</b>. Đuôi <i>-ива-</i> kéo trọng âm lên ngay trước nó: '
    '<b>обслу́живание</b>.</div>'
    '<div class="hd-warn"><b>техни́ческое обслу́живание</b> — bảo dưỡng xe, máy móc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обслужи́ть</b> phục vụ (HT) · <b>служи́ть</b> phục vụ · '
    '<b>услу́га</b> dịch vụ · <b>слу́жба</b> công việc, sự phục vụ</div>'
)

# --------------------------------------------------------------------- коммерческий
S["коммерческий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">комме́рч-</span>'
    '<span class="hd-gloss">THƯƠNG MẠI — <b>комме́рция</b>, <b>ц → ч</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-еск-ий</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>commercial</i>, giữ cả hai <i>м</i>. <i>ц</i> của danh từ '
    'hoá <i>ч</i> trước <b>-еский</b>, như <b>Гре́ция → гре́ческий</b>. Nghĩa lõi: làm ra để '
    'kiếm lời — <b>комме́рческий банк</b> ngân hàng thương mại.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>комме́рция</b> thương mại · <b>коммерса́нт</b> thương nhân</div>'
)

# --------------------------------------------------------------------- ведущий
S["ведущий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вед-</span>'
    '<span class="hd-gloss">DẪN — gốc của <b>вести́</b>: <b>веду́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ущ-ий</span>'
    '<span class="hd-gloss">«ĐANG làm» — như <b>бу́дущий</b>, <b>сле́дующий</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Người đang dẫn» ⇒ người dẫn chương trình. Gốc là tính từ (còn nghĩa '
    '«hàng đầu»: <b>веду́щий специали́ст</b> chuyên gia đầu ngành), nên danh từ này chia như '
    'tính từ: <b>с веду́щим</b>; nữ MC là <b>веду́щая</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вести́</b> dẫn · <b>води́ть</b> dẫn (nhiều chiều) · '
    '<b>руководи́тель</b> người lãnh đạo</div>'
)

# --------------------------------------------------------------------- деловой
S["деловой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дел-</span>'
    '<span class="hd-gloss">VIỆC — <b>де́ло</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ов-о́й</span>'
    '<span class="hd-gloss">đuôi tính từ, trọng âm nằm trên đuôi</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thuộc về công việc» ⇒ <b>делово́й обе́д</b> bữa trưa bàn công việc, '
    '<b>делово́й костю́м</b> com-lê công sở. Tả người: <b>делово́й челове́к</b> người thạo việc, '
    'thực tế.</div>'
    '<div class="hd-warn"><b>делово́й</b> = về công việc, giao dịch · <b>комме́рческий</b> = '
    'nhằm kiếm lời.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>де́ло</b> việc · <b>де́лать</b> làm · <b>делови́тый</b> tháo vát</div>'
)

# --------------------------------------------------------------------- аукцион
S["аукцион"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn (Latin <i>auctio</i>) — không chẻ được trong tiếng Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>auction</i>. Latin <i>auctio</i> ra từ <i>augere</i> «tăng '
    'thêm» (như <i>augment</i>) — giá cứ tăng tới người trả cao nhất. Tiếng Nga viết theo Latin: '
    '<b>аук-</b>, không phải <i>ак-</i>.</div>'
    '<div class="hd-warn"><b>на аукцио́не</b> — tại phiên đấu giá · <b>прода́ть с аукцио́на</b> — '
    'bán đấu giá.</div>'
)

# --------------------------------------------------------------------- наследство
S["наследство"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">LÊN, nối tiếp theo</span></div>'
    '<div class="hd-row"><span class="hd-piece">-след-</span>'
    '<span class="hd-gloss">DẤU VẾT — <b>след</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ств-о</span>'
    '<span class="hd-gloss">đuôi danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người đi tiếp trên dấu chân người trước là <b>насле́дник</b> người thừa '
    'kế; thứ họ nhận được là <b>насле́дство</b>.</div>'
    '<div class="hd-warn"><b>получи́ть в насле́дство</b> — được thừa hưởng · <b>оста́вить в '
    'насле́дство</b> — để lại.</div>'
    '<div class="hd-warn"><b>насле́дство</b> = của cải thừa kế · <b>насле́дие</b> = di sản tinh '
    'thần, văn hoá.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>след</b> dấu vết · <b>насле́дник</b> người thừa kế · '
    '<b>насле́довать</b> thừa kế</div>'
)

# --------------------------------------------------------------------- консультант
S["консультант"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">консульт-</span>'
    '<span class="hd-gloss">hỏi ý kiến — <i>consult</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́нт</span>'
    '<span class="hd-gloss">NGƯỜI làm việc đó — <i>-ant</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>consultant</i>: người làm công việc <b>консульта́ция</b>. Ở cửa '
    'hàng, <b>продаве́ц-консульта́нт</b> là nhân viên tư vấn bán hàng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>консульта́ция</b> buổi tư vấn · <b>консульти́ровать</b> tư vấn · '
    '<b>консульти́роваться</b> hỏi ý kiến</div>'
)

# --------------------------------------------------------------------- корреспондент
S["корреспондент"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">корреспонд-</span>'
    '<span class="hd-gloss">Latin <i>correspondere</i> «đáp lại nhau» ⇒ trao đổi thư</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́нт</span>'
    '<span class="hd-gloss">NGƯỜI làm việc đó — <i>-ent</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>correspondent</i>, cả hai <i>р</i>: người ở nơi khác gửi tin '
    'bài về toà soạn — <b>корреспонде́нт в Пари́же</b> phóng viên thường trú ở Paris.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>корреспонде́нция</b> thư từ; bài phóng sự</div>'
)

# --------------------------------------------------------------------- предприниматель
S["предприниматель"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пред-</span>'
    '<span class="hd-gloss">TRƯỚC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-при-ним-а-</span>'
    '<span class="hd-gloss">NHẬN LẤY — như <b>принима́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-тель</span>'
    '<span class="hd-gloss">NGƯỜI làm việc đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>предпринима́ть</b> = đứng ra nhận lấy một việc ⇒ khởi sự làm ăn; '
    'thêm <b>-тель</b> là người làm việc đó. Cùng lối ghép với Pháp <i>entre-prendre</i> → '
    '<i>entrepreneur</i>. Cùng nhà với <b>предприя́тие</b> doanh nghiệp.</div>'
    '<div class="hd-warn">Từ chuẩn của luật, giấy tờ: <b>индивидуа́льный предпринима́тель</b> — hộ '
    'kinh doanh cá thể. <b>бизнесме́н</b> là từ mượn, khẩu ngữ hơn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>предприя́тие</b> doanh nghiệp · <b>предприня́ть</b> tiến hành · '
    '<b>принима́ть</b> nhận</div>'
)

# --------------------------------------------------------------------- близнецы
S["близнецы"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">близ-</span>'
    '<span class="hd-gloss">GẦN — như <b>бли́зкий</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ец</span>'
    '<span class="hd-gloss">hậu tố chỉ người</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ы́</span>'
    '<span class="hd-gloss">số nhiều</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Những đứa ở sát bên nhau» ⇒ trẻ sinh đôi: <b>бра́тья-близнецы́</b> anh '
    'em sinh đôi. Viết hoa <b>Близнецы́</b> là chòm/cung Song Tử.</div>'
    '<div class="hd-warn">Một đứa là <b>близне́ц</b>; cả cặp <b>близнецы́</b> — <i>е</i> của '
    '<i>-ец</i> rơi, như <b>оте́ц → отцы́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бли́зкий</b> gần, thân · <b>бли́зко</b> ở gần</div>'
)

B = {
    "docbangmat": 68,
    "loitubat": 3,
    "nguonsai": 2,
    "baolen": [
        "Va chạm предприниматель↔бизнесмен (k35, mồ côi, không sửa): gỡ bằng V phía k194 — предприниматель bỏ chữ «doanh nhân», giữ «chủ doanh nghiệp, nhà khởi nghiệp, nhà kinh doanh». KHÔNG mất nghĩa (entrepreneur = người đứng ra làm chủ việc kinh doanh, vẫn đủ ở ba cụm còn lại); chỉ bỏ một từ đồng nghĩa trùng nguyên văn với đề бизнесмен. Mô phỏng do_va_cham với V áp vào (đọc Anki, không ghi): không còn va chạm nào dính từ k194. Nếu user thấy «doanh nhân» là nghĩa chính không được bỏ thì va chạm này không gỡ được từ phía lô.",
        "Nguồn sai bác (nguonsai=2): нация đề cũ có «nhân dân» — đó là nghĩa của народ, gloss «people» ở đây là «một dân tộc» ⇒ V còn «dân tộc, quốc gia». помолиться đề cũ «cầu nguyện một lúc» — помолиться là vế HT thường của молиться, không phải dạng «làm một lúc» ⇒ V «cầu nguyện, đọc lời cầu nguyện».",
        "Lỗi tự bắt (loitubat=3): старуха gloss -уха «người NỮ» nói quá (-уха còn tạo danh từ khẩu ngữ không chỉ người) ⇒ «hậu tố khẩu ngữ, ở đây chỉ người NỮ»; корреспондент câu «rộng hơn журналист» không chắc ⇒ thay bằng ví dụ thường trú; предприниматель «nói thường mới dùng бизнесмен» quá tay ⇒ «бизнесмен là từ mượn, khẩu ngữ hơn».",
        "Không chắc (mức tin vừa): близнецы chẻ близ- GẦN + -нец (từ nguyên theo Vasmer, tôi khá chắc nhưng không tra được trong repo); наследство «на- nối tiếp theo + след dấu vết» là đường nhớ từ mảnh chẻ, cấu tạo rõ nhưng không khẳng định là lịch sử nghĩa; деловой ô đỏ «деловой = về công việc · коммерческий = nhằm kiếm lời» là phân biệt sắc thái do tôi đúc kết. Không viết гибель↔гибкий cùng gốc (từ nguyên có tranh luận).",
        "Họ hàng cố ý vắng: аукцион (từ mượn Latin đứng một mình; аукционист hiếm, không đáng dạy).",
        "V cần duyệt (6 thẻ): гибель (THÊM sự hủy diệt, sự sụp đổ — destruction/ruin/collapse), нация + помолиться (xem dòng 2), ведущий («phát thanh viên dẫn» cụt ⇒ người dẫn bản tin; THÊM người phụ trách — person in charge), деловой (THÊM kinh doanh — nghĩa chính business; thiết thực — practical; bỏ «mang tính công việc» trùng), предприниматель (xem dòng 1). 13 thẻ còn lại đề cũ đã đúng, không viết V.",
    ],
}
