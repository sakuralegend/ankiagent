# -*- coding: utf-8 -*-
"""k262 — actions: chín cặp thể + bốn động từ lẻ; trục là TIỀN TỐ + gốc đã học.

Chỗ cần nhất quán với lô đã nạp:
(1) повыситься/-шаться: по- không nghĩa riêng + вы́с-/выш- CAO, khớp повысить k215.
(2) об- / раз- + лить: и → ь, quá khứ -лила́, khớp лить k251, налить k213; chêm о như разбить k80.
(3) в- VÀO; -бег-а́ть / -беж-а́ть / -лет-а́ть / -лете́ть viết như k251, k227.
(4) про- XUYÊN QUA, NGANG QUA (k239, k251); плы- BƠI, TRÔI, thân плыв- (k96).
(5) рас- TÁCH RA các phía + сы́п- RẮC, VÃI (k253). (6) маз- BÔI, PHẾT (k22).
(7) при-со-еди́н- (k171, k201). (8) из- tới CẠN, quá mức (избить k228).
(9) рас- TÁCH RA từng phần, nghe RÕ như разглядеть k212.
Họ hàng cố ý vắng: không có.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "повыситься": "tăng, tăng lên, lên cao, được lên chức",     # dãy chung của cặp
    "повышаться": "tăng, tăng lên, lên cao, được lên chức",
    "обливать": "dội, xối, tạt, làm ướt sũng, làm đổ lên",      # «tưới lên» là поли́ть; + splash / spill on
    "облить": "dội, xối, tạt, làm ướt sũng, làm đổ lên",
    "разливать": "rót ra, múc chia, đóng chai, làm đổ",         # dãy chung; + spill
    "разлить": "rót ra, múc chia, đóng chai, làm đổ",
    "баловать": "chiều, cưng, nuông chiều, chiều hư",           # + to spoil
    "избаловать": "chiều hư, chiều hỏng",                       # «làm cho hư» dễ hiểu thành hỏng đồ
    "проплывать": "bơi qua, bơi hết, đi thuyền qua, trôi qua",  # + to sail
    "проплыть": "bơi qua, bơi hết, đi thuyền qua, trôi qua",
    "мазать": "bôi, phết, trét, thoa, làm bẩn",                 # + to soil / make dirty (намазать không có)
    "намазать": "bôi, phết, trét, thoa",                        # cùng thứ tự với мазать
    "рассыпать": "làm đổ, làm vương vãi, rắc, rải",             # «làm rơi tung» gượng; khớp рассы́паться «vương vãi»
    "присоединить": "nối, gắn vào, kết nối, gộp vào, sáp nhập",  # dãy chung; + annex / attach
    "присоединять": "nối, gắn vào, kết nối, gộp vào, sáp nhập",
}

# ---------------------------------------------------------------- повыситься
S["повыситься"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вы́с-</span>'
    '<span class="hd-gloss">CAO — gốc của <b>высо́кий</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить-ся</span>'
    '<span class="hd-gloss">đuôi lớp 2 + <i>-ся</i>: tự nó lên</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tự nó lên CAO ⇒ giá, lương, nhiệt độ tăng. Có người làm cho tăng thì bỏ <i>-ся</i>: '
    '<b>повы́сить</b>. Chỉ ngôi «tôi» đổi <i>с → ш</i>: <b>повы́шусь, повы́сишься</b> — ngôi này gần như chỉ '
    'gặp khi nói lên chức: <b>повы́ситься в до́лжности</b>. Cặp CHT: <b>повыша́ться</b>.</div>'
    '<div class="hd-warn">Tăng THÊM bao nhiêu → <b>на</b> + cách 4; tăng TỚI mức → <b>до</b> + cách 2: '
    '<b>Це́ны повы́сились на пять проце́нтов.</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>повыша́ться</b> (CHT) · <b>повы́сить</b> nâng, tăng · '
    '<b>повыше́ние</b> sự tăng, sự thăng chức · <b>высота́</b> chiều cao</div>'
)

# ---------------------------------------------------------------- повышаться
S["повышаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-выш-</span>'
    '<span class="hd-gloss">CAO — <i>выс-</i> với с → ш, như <b>вы́ше</b> cao hơn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть-ся</span>'
    '<span class="hd-gloss">đuôi CHT + <i>-ся</i>: tự nó lên</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>повы́ситься</b>: đang lên, hay lên nhiều lần — '
    '<b>Температу́ра повыша́ется.</b> Nhiệt độ đang lên. Thể này <i>ш</i> ở mọi ngôi, chia đều: '
    '<b>повыша́юсь, повыша́ется</b>.</div>'
    '<div class="hd-warn"><b>повы́шенная температу́ра</b> = hơi sốt («nhiệt độ bị nâng cao») — '
    'câu phải biết khi đi khám bệnh.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>повы́ситься</b> (HT) · <b>повыша́ть</b> nâng, tăng · '
    '<b>повыше́ние</b> sự tăng · <b>вы́сший</b> cao nhất</div>'
)

# ------------------------------------------------------------------ обливать
S["обливать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">phủ KHẮP quanh người, quanh vật</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ли-</span>'
    '<span class="hd-gloss">ĐỔ, RÓT — <b>лить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва́-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>облива́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đổ cho nước phủ khắp ⇒ dội, xối, làm ướt sũng. Cách 4 là CÁI BỊ ƯỚT, chất lỏng để '
    'cách 5, y như <b>полива́ть</b> (tưới): <b>облива́ть бра́та водо́й</b>. Cặp HT: <b>обли́ть</b>.</div>'
    '<div class="hd-warn"><b>облива́ть гря́зью</b> + cách 4 = bôi nhọ ai («dội bùn lên»).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обли́ть</b> (HT) · <b>облива́ться</b> tự dội nước lên mình · '
    '<b>лить</b> đổ, rót · <b>разлива́ть</b> rót ra</div>'
)

# -------------------------------------------------------------------- облить
S["облить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">phủ KHẮP quanh người, quanh vật</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ли́-ть</span>'
    '<span class="hd-gloss">ĐỔ, RÓT — <b>лить</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp HT của <b>облива́ть</b>. Cố ý dội hay lỡ tay làm đổ lên người đều là nó: '
    '<b>Она́ облила́ меня́ со́ком.</b> Cô ấy làm đổ nước quả lên người tôi (tôi cách 4, nước quả cách 5).</div>'
    '<div class="hd-warn">Chia như <b>лить</b> (<i>и → ь</i>) nhưng chêm <b>о</b> sau <i>об</i>: '
    '<b>оболью́, обольёшь, оболью́т</b>; sai khiến <b>обле́й</b>.</div>'
    '<div class="hd-warn">Quá khứ giống cái nhảy ra đuôi: <b>облила́</b>. Các dạng kia có hai cách đọc đều '
    'đúng: <b>обли́л</b> hay <b>о́блил</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>облива́ть</b> (CHT) · <b>лить</b> đổ, rót · <b>поли́ть</b> tưới · '
    '<b>разли́ть</b> làm đổ, rót ra</div>'
)

# ----------------------------------------------------------------- разливать
S["разливать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раз-</span>'
    '<span class="hd-gloss">TÁCH RA nhiều phía</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ли-</span>'
    '<span class="hd-gloss">ĐỔ, RÓT — <b>лить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва́-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>разлива́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đổ chất lỏng RA NHIỀU PHÍA: cố ý thì là rót, múc chia ra nhiều cốc, nhiều bát, nhiều '
    'chai; lỡ tay thì là làm đổ. Chia ra các cốc → <b>по</b> + cách 3: <b>разлива́ть чай по ча́шкам</b>. '
    'Rót đầy một cốc thì <b>налива́ть</b>. Cặp HT: <b>разли́ть</b>.</div>'
    '<div class="hd-warn"><b>пи́во на разли́в</b> = bia tươi rót từ vòi, không phải bia chai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>разли́ть</b> (HT) · <b>разлива́ться</b> tràn ra · '
    '<b>разли́в</b> nước sông tràn bờ · <b>облива́ть</b> dội</div>'
)

# -------------------------------------------------------------------- разлить
S["разлить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раз-</span>'
    '<span class="hd-gloss">TÁCH RA nhiều phía</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ли́-ть</span>'
    '<span class="hd-gloss">ĐỔ, RÓT — <b>лить</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp HT của <b>разлива́ть</b>: làm đổ (<b>Я разли́л молоко́</b>) hoặc rót chia ra '
    '(<b>разли́ть суп по таре́лкам</b>). Chỉ dùng cho chất LỎNG; đường, muối, hạt bị đổ là <b>рассы́пать</b>.</div>'
    '<div class="hd-warn">Chia như <b>лить</b> (<i>и → ь</i>) nhưng chêm <b>о</b> sau <i>раз</i>: '
    '<b>разолью́, разольёшь, разолью́т</b>; sai khiến <b>разле́й</b>. Quá khứ giống cái <b>разлила́</b>.</div>'
    '<div class="hd-warn"><b>Их водо́й не разольёшь</b> = họ thân nhau như hình với bóng '
    '(dội nước cũng không tách ra được).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>разлива́ть</b> (CHT) · <b>разли́ться</b> tràn ra · '
    '<b>проли́ть</b> làm đổ · <b>обли́ть</b> dội, làm đổ lên</div>'
)

# ---------------------------------------------------------- совершенствовать
S["совершенствовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">соверше́н-</span>'
    '<span class="hd-gloss">HOÀN HẢO — <b>соверше́нный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ств-</span>'
    '<span class="hd-gloss">→ danh từ: <b>соверше́нство</b> sự hoàn hảo</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-ть</span>'
    '<span class="hd-gloss">đuôi động từ; khi chia <i>-ова- → -у-</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đưa dần tới sự hoàn hảo ⇒ trau dồi, cải tiến: <b>соверше́нствовать произноше́ние</b> '
    'trau dồi phát âm. Trọng âm đứng yên ở <i>-ше́н-</i> cả bảng: <b>соверше́нствую</b>. '
    'Cặp HT: <b>усоверше́нствовать</b>.</div>'
    '<div class="hd-warn"><b>владе́ть ру́сским в соверше́нстве</b> = thông thạo hoàn hảo tiếng Nga.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>соверше́нный</b> hoàn hảo · <b>соверше́нно</b> hoàn toàn · '
    '<b>соверше́нствоваться</b> tự hoàn thiện mình</div>'
)

# ------------------------------------------------------------------ баловать
S["баловать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бал-</span>'
    '<span class="hd-gloss">CHIỀU — không nối được sang từ quen nào; không dính <b>бал</b> dạ hội</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова́-ть</span>'
    '<span class="hd-gloss">đuôi động từ; khi chia <i>-ова- → -у-</i>: <b>балу́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chiều AI cách 4, bằng CÁI GÌ cách 5: <b>балова́ть дете́й пода́рками</b>. Nghĩa rộng từ '
    'cưng chiều một chút tới chiều quá hoá hư; hư hẳn rồi thì là HT <b>избалова́ть</b>.</div>'
    '<div class="hd-warn">Trọng âm chuẩn ở đuôi: <b>балова́ть, балу́ешь</b>. Nhiều người Nga đọc nhấn âm đầu '
    '— bị coi là sai.</div>'
    '<div class="hd-warn"><b>балова́ть себя́</b> + cách 5 = tự thưởng cho mình món gì.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>избалова́ть</b> chiều hư (HT) · <b>балова́ться</b> nghịch ngợm · '
    '<b>ба́ловень</b> con cưng, kẻ được nuông chiều</div>'
)

# ---------------------------------------------------------------- избаловать
S["избаловать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">из-</span>'
    '<span class="hd-gloss">tới CẠN, quá mức — như <b>изби́ть</b> đánh nhừ tử</span></div>'
    '<div class="hd-row"><span class="hd-piece">-балова́ть</span>'
    '<span class="hd-gloss">chiều, cưng — chính là <b>балова́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chiều QUÁ MỨC ⇒ chiều hư. Đây là kết quả xấu đã thấy rõ, còn <b>балова́ть</b> có thể '
    'chỉ là cưng. Chia y như nó, <i>-ова- → -у-</i>: <b>избалу́ю, избалу́ешь</b>.</div>'
    '<div class="hd-warn"><b>избало́ванный ребёнок</b> = đứa trẻ được chiều sinh hư — dạng rất hay gặp của '
    'từ này; trọng âm lùi về <i>-ло́-</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>балова́ть</b> chiều (CHT) · <b>балова́ться</b> nghịch ngợm · '
    '<b>ба́ловень</b> con cưng</div>'
)

# ---------------------------------------------------------------- баловаться
S["баловаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">балова́ть</span>'
    '<span class="hd-gloss">chiều, cưng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">làm nghĩa rẽ hẳn sang NGHỊCH, không phải «được chiều»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trẻ con quậy phá cho vui: <b>Не балу́йся!</b> Đừng nghịch! Nghĩa này phải thuộc, '
    'không suy thẳng từ <i>-ся</i> được. Chia <i>-ова- → -у-</i>: <b>балу́юсь, балу́ешься</b>.</div>'
    '<div class="hd-warn">Nghịch VỚI thứ gì → <b>с</b> + cách 5: <b>балова́ться с огнём</b>. Cách 5 trần là '
    'thỉnh thoảng làm cho vui: <b>балова́ться фотогра́фией</b> chụp ảnh chơi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>балова́ть</b> chiều, cưng · <b>избалова́ть</b> chiều hư · '
    '<b>баловство́</b> trò nghịch</div>'
)

# ---------------------------------------------------------------- проплывать
S["проплывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">XUYÊN QUA, NGANG QUA — như <b>пройти́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-плы-</span>'
    '<span class="hd-gloss">BƠI, TRÔI trên nước — <b>плыть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва́-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>проплыва́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bơi hay trôi ngang qua; cả thuyền, cả mây cũng <b>проплыва́ть</b>: '
    '<b>Облака́ проплыва́ют над го́родом.</b> Mây trôi qua trên thành phố. Cặp HT: <b>проплы́ть</b>.</div>'
    '<div class="hd-warn">NGANG bên cái gì: <b>ми́мо</b> + cách 2 — <b>проплыва́ть ми́мо о́строва</b>. '
    'Quãng đường để cách 4 trần — <b>проплыва́ть киломе́тр</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>проплы́ть</b> (HT) · <b>плыть</b> bơi (một chiều) · '
    '<b>пла́вать</b> bơi lội · <b>плове́ц</b> người bơi</div>'
)

# ------------------------------------------------------------------ проплыть
S["проплыть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">XUYÊN QUA, NGANG QUA — như <b>пройти́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-плы́ть</span>'
    '<span class="hd-gloss">BƠI, TRÔI trên nước — <b>плыть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp HT của <b>проплыва́ть</b>: bơi hết một quãng, hay trôi qua xong. Quãng đường để '
    'cách 4 trần: <b>проплы́ть сто ме́тров</b>; chui dưới gầm cầu: <b>проплы́ть под мосто́м</b>.</div>'
    '<div class="hd-warn">Thân chèn <b>в</b> y như <b>плыть</b>: <b>проплыву́, проплывёшь</b>; sai khiến '
    '<b>проплыви́</b>. Quá khứ giống cái trọng âm ra đuôi: <b>проплыла́</b>.</div>'
    '<div class="hd-warn"><b>проплы́ть</b> = bơi qua NGANG, hết quãng · <b>переплы́ть</b> = bơi SANG bờ bên kia.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>проплыва́ть</b> (CHT) · <b>плыть</b> bơi (một chiều) · '
    '<b>поплы́ть</b> bắt đầu bơi · <b>пла́вание</b> môn bơi</div>'
)

# ------------------------------------------------------------------- вбегать
S["вбегать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бег-а́ть</span>'
    '<span class="hd-gloss">CHẠY — khuôn của <b>бе́гать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chạy từ ngoài vào trong. Vào đâu: <b>в</b> + cách 4 — tiền tố <i>в-</i> đi với chính '
    'giới từ <b>в</b>: <b>вбега́ть в ко́мнату</b>. Trọng âm nhảy sang đuôi: <b>бе́гать</b> nhưng <b>вбега́ю</b>. '
    'Cặp HT: <b>вбежа́ть</b>.</div>'
    '<div class="hd-warn"><b>вбега́ть в дом</b> chạy VÀO nhà (cách 4) ↔ <b>выбега́ть из до́ма</b> chạy RA '
    'khỏi nhà (cách 2).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вбежа́ть</b> (HT) · <b>бе́гать</b> chạy (nhiều chiều) · '
    '<b>убега́ть</b> bỏ chạy · <b>бег</b> môn chạy</div>'
)

# ------------------------------------------------------------------- вбежать
S["вбежать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO</span></div>'
    '<div class="hd-row"><span class="hd-piece">-беж-а́ть</span>'
    '<span class="hd-gloss">CHẠY — chính là <b>бежа́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chạy vào, xong một lượt: <b>Де́ти вбежа́ли в класс.</b> Bọn trẻ chạy ùa vào lớp. '
    'Vào đâu: <b>в</b> + cách 4. Cặp CHT: <b>вбега́ть</b>.</div>'
    '<div class="hd-warn">Chia y hệt <b>бежа́ть</b>, chỉ «tôi» và «họ» mang <b>г</b>: '
    '<b>вбегу́, вбежи́шь, вбегу́т</b>; sai khiến <b>вбеги́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вбега́ть</b> (CHT) · <b>бежа́ть</b> chạy · '
    '<b>вы́бежать</b> chạy ra · <b>пробежа́ть</b> chạy qua</div>'
)

# -------------------------------------------------------------------- мазать
S["мазать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ма́з-</span>'
    '<span class="hd-gloss">gốc BÔI, PHẾT — như <b>ма́сло</b> (маз + сло) «thứ để phết»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trải thứ mềm, dẻo lên mặt: bơ lên bánh, kem lên da. Làm bẩn cũng là nó: '
    '<b>Не мажь стол!</b> Đừng làm bẩn bàn! Cặp HT của nghĩa bôi, phết: <b>нама́зать</b>.</div>'
    '<div class="hd-warn"><i>з → ж</i> ở MỌI ngôi, không chỉ «tôi»: <b>ма́жу, ма́жешь, ма́жут</b>; '
    'sai khiến <b>мажь</b>. Quá khứ giữ <i>з</i>: <b>ма́зал</b>.</div>'
    '<div class="hd-warn">Hai cách nói: <b>ма́зать хлеб ма́слом</b> (bánh cách 4, bơ cách 5) = '
    '<b>ма́зать ма́сло на хлеб</b> (bơ cách 4, <b>на</b> + cách 4).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>нама́зать</b> phết, bôi (HT) · <b>мазь</b> thuốc mỡ · '
    '<b>сма́зать</b> bôi một lớp, tra dầu · <b>ма́сло</b> bơ, dầu</div>'
)

# ------------------------------------------------------------------ намазать
S["намазать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">LÊN mặt trên, như giới từ <b>на</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ма́зать</span>'
    '<span class="hd-gloss">BÔI, PHẾT — chính là <b>ма́зать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Phết xong một lớp LÊN mặt: <b>нама́зать крем на лицо́</b> thoa kem lên mặt. '
    'Cũng như <b>ма́зать</b>, đổi vai được: <b>нама́зать хлеб ма́слом</b> — bánh cách 4, bơ cách 5.</div>'
    '<div class="hd-warn"><i>з → ж</i> ở mọi ngôi: <b>нама́жу, нама́жешь, нама́жут</b>; '
    'sai khiến <b>нама́жь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ма́зать</b> bôi, phết (CHT) · <b>нама́заться</b> tự bôi kem · '
    '<b>мазь</b> thuốc mỡ · <b>ма́сло</b> bơ, dầu</div>'
)

# ----------------------------------------------------------------- рассыпать
S["рассыпать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рас-</span>'
    '<span class="hd-gloss">TÁCH RA các phía</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сы́п-</span>'
    '<span class="hd-gloss">RẮC, VÃI thứ dạng hạt — <b>сы́пать</b>, <b>сыпь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm thứ khô, rời VÃI RA các phía: lỡ tay làm đổ đường, hay cố ý rắc, rải. '
    '<b>Я рассы́пал соль.</b> Chất lỏng thì <b>разли́ть</b>; tự nó đổ ra thì thêm <i>-ся</i>: <b>рассы́паться</b>.</div>'
    '<div class="hd-warn">Trọng âm tách hai thể: <b>рассы́пать</b> HT (thẻ này) — <b>рассыпа́ть</b> CHT, '
    'chia đều <b>рассыпа́ю</b>.</div>'
    '<div class="hd-warn">Tương lai <i>п → пл</i> ở mọi ngôi: <b>рассы́плю, рассы́плешь, рассы́плют</b>; '
    'sai khiến <b>рассы́пь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сы́пать</b> rắc, đổ · <b>рассы́паться</b> đổ tung, vương vãi · '
    '<b>насы́пать</b> đổ vào · <b>сыпь</b> nốt ban</div>'
)

# ------------------------------------------------------------------- влетать
S["влетать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лет-а́ть</span>'
    '<span class="hd-gloss">BAY — khuôn của <b>лета́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bay vào trong; người «bay vào» là lao vào, xông vào: <b>влета́ть в ко́мнату без сту́ка</b> '
    'xông vào phòng không gõ cửa. Vào đâu: <b>в</b> + cách 4. Chia đều: <b>влета́ю</b>. '
    'Cặp HT: <b>влете́ть</b>.</div>'
    '<div class="hd-warn"><b>влета́ть в окно́</b> bay VÀO qua cửa sổ ↔ <b>вылета́ть из окна́</b> bay RA '
    'khỏi cửa sổ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>влете́ть</b> (HT) · <b>лета́ть</b> bay (nhiều chiều) · '
    '<b>прилета́ть</b> bay đến · <b>полёт</b> chuyến bay</div>'
)

# ------------------------------------------------------------------- влететь
S["влететь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лете́ть</span>'
    '<span class="hd-gloss">BAY — <b>лете́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp HT của <b>влета́ть</b>: đã bay vào, lao vào. <b>В ку́хню влете́ла му́ха.</b> Một con '
    'ruồi bay vào bếp. Chia như <b>лете́ть</b>, т → ч chỉ ở «tôi»: <b>влечу́</b>, nhưng '
    '<b>влети́шь, влетя́т</b>.</div>'
    '<div class="hd-warn"><b>Мне влете́ло</b> = tôi bị mắng một trận: người bị mắng cách 3, không chủ ngữ — '
    '<b>Мне влете́ло от ма́мы.</b></div>'
    '<div class="hd-warn"><b>влете́ть в копе́ечку</b> = tốn một khoản ra trò.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>влета́ть</b> (CHT) · <b>лете́ть</b> bay (một chiều) · '
    '<b>вы́лететь</b> bay ra · <b>улете́ть</b> bay đi</div>'
)

# ---------------------------------------------------------------- расслышать
S["расслышать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рас-</span>'
    '<span class="hd-gloss">TÁCH RA từng phần, tới khi RÕ — như <b>разгляде́ть</b> nhìn rõ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-слы́ш-</span>'
    '<span class="hd-gloss">NGHE — <b>слы́шать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">nhưng chia LỚP 2: <b>расслы́шу, расслы́шишь, расслы́шат</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghe tới khi các tiếng TÁCH RA khỏi nhau ⇒ nghe rõ. Chỉ nói kết quả nên không có cặp '
    'CHT thường dùng. <b>слы́шать</b> là âm lọt vào tai, <b>расслы́шать</b> là rõ từng chữ.</div>'
    '<div class="hd-warn">Rất hay đi với «không»: <b>Прости́те, я не расслы́шал.</b> '
    'Xin lỗi, tôi nghe không rõ (nữ nói <b>расслы́шала</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>слы́шать</b> nghe thấy · <b>услы́шать</b> nghe thấy (HT) · '
    '<b>слы́шно</b> nghe được · <b>слух</b> thính giác, tin đồn</div>'
)

# --------------------------------------------------------------- присоединить
S["присоединить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">SÁT VÀO, THÊM VÀO</span></div>'
    '<div class="hd-row"><span class="hd-piece">-со-</span>'
    '<span class="hd-gloss">CÙNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-еди́н-</span>'
    '<span class="hd-gloss">MỘT — dạng cổ của <b>оди́н</b>, như <b>еди́ный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đưa một thứ THÊM VÀO cho CÙNG thành MỘT ⇒ nối, gắn vào, sáp nhập. Vào đâu: <b>к</b> + '
    'cách 3: <b>присоедини́ть при́нтер к компью́теру</b>. Tự mình gia nhập thì thêm <i>-ся</i>. '
    'Tương lai: <b>присоединю́, присоедини́шь</b>.</div>'
    '<div class="hd-warn"><b>соедини́ть</b> A <b>с</b> B: hai bên ngang nhau · <b>присоедини́ть</b> A <b>к</b> B: '
    'gắn cái thêm vào cái đã có sẵn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>присоединя́ть</b> (CHT) · <b>присоедини́ться</b> gia nhập · '
    '<b>соедини́ть</b> nối lại · <b>объедини́ть</b> hợp nhất</div>'
)

# --------------------------------------------------------------- присоединять
S["присоединять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-со-</span>'
    '<span class="hd-gloss">SÁT VÀO + CÙNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-еди́н-</span>'
    '<span class="hd-gloss">MỘT — như <b>еди́ный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành (-и́ть → -я́ть)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chưa HT của <b>присоедини́ть</b>, vẫn <b>к</b> + cách 3: <b>присоединя́ть но́вые зе́мли '
    'к госуда́рству</b> sáp nhập đất mới vào quốc gia. Chia đều <b>присоединя́ю, присоединя́ют</b>.</div>'
    '<div class="hd-warn">Ngôi «họ» của hai thể chỉ khác một chữ: HT <b>присоединя́т</b> — '
    'CHT <b>присоединя́ют</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>присоедини́ть</b> (HT) · <b>присоединя́ться</b> tham gia · '
    '<b>соединя́ть</b> nối · <b>присоедине́ние</b> sự sáp nhập</div>'
)

# docbangmat 183 · loitubat 3: ví dụ «присоединять провод к розетке» gượng (phải là подключать) → «новые земли к государству»;
# баловаться: câu suy nghĩa «nghịch» từ «được chiều» không có căn cứ → nói thẳng phải thuộc; расслышать «hầu như luôn» phủ định → «rất hay».
# nguonsai 1: мазать ghi bạn thể зама́зать (= tô kín, bít lại, nghĩa khác) — thẻ chỉ dùng нама́зать.
B = {
    "docbangmat": 183,
    "loitubat": 3,
    "nguonsai": 1,
    "baolen": [
        "мазать — bảng ghi bạn thể «нама́зать, зама́зать»; замазать là «tô kín, bít lại», không phải cặp của nghĩa bôi/phết. Đề nghị bỏ khỏi partners.",
        "облить — tính động từ bị động «облитый» trong bảng thiếu dấu trọng âm (chuẩn: обли́тый, cũng о́блитый). проплывать — «проплываемый» cũng thiếu dấu (проплыва́емый). Nhiều trạng động từ -вши/-вшись trong lô (обливши, разливши, избаловавши, влетевши, намазавши…) cũng thiếu dấu.",
        "присоединить — trạng động từ «присоединя́» và расслышать — «расслы́ша» là dạng cổ của thể HT, trùng/na ná CHT; bảng nên chỉ giữ присоедини́в, расслы́шав.",
        "баловать/избаловать — KHÔNG chung dãy V vì gloss khác thật: HT chỉ «to spoil» (chiều hư); CHT thêm cưng, nuông chiều. Bạn thể HT còn lại побалова́ть (chiều một chút) chưa có trên máy.",
        "мазать/намазать — V cùng dãy, riêng мазать thêm «làm bẩn» (gloss to soil / make dirty; намазать không có).",
        "повыситься/повышаться — gloss EN không có «lên chức», V giữ «được lên chức» vì nghĩa có thật (повыситься в должности) và một câu ví dụ trên thẻ đang dùng; cần duyệt.",
        "обливать/облить — V bỏ «tưới lên» (đó là поливать/полить), thêm «tạt», «làm đổ lên» (gloss splash / spill on). Câu ví dụ облить có «làm đổ».",
        "разливать/разлить — V chung dãy «rót ra, múc chia, đóng chai, làm đổ»; bỏ «chia ra rót» (không tự nhiên).",
        "рассыпать — «làm rơi tung» → «làm vương vãi» (gloss strew / scatter, khớp рассыпаться).",
        "присоединить/присоединять — V chung dãy, thêm «sáp nhập» cho HT (gloss HT thiếu annex nhưng CHT có, nghĩa thật của cả cặp).",
        "расслышать, баловаться, совершенствовать, вбегать/вбежать, влетать/влететь — giữ nguyên dòng tiếng Việt, không khai V. Nghĩa «thỉnh thoảng làm cho vui» của баловаться (dabble) chỉ nói trong ô đỏ, không đưa vào đề.",
        "Va chạm nghĩa: máy in (khong co), nhưng máy so dòng ĐANG có trên thẻ — V mới chưa được so, nên chạy lại vacham sau khi nạp.",
    ],
}
