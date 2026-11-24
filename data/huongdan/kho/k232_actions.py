# -*- coding: utf-8 -*-
"""k232 — actions: 5 cặp thể + động từ mượn đuôi -ова́ть; trục là GỐC + ĐUÔI CHIA.

Chỗ cần nhất quán với lô đã nạp:
(1) отстать/отставать: от- RỜI RA + -ста- ĐỨNG — khớp встать, расстаться k189, отсталый k149.
(2) -ва́-ть: rụng ở отстава́ть (như встава́ть), KHÔNG rụng ở продлева́ть, остыва́ть — nói ở thẻ đó.
(3) продлить/продлевать: про- kéo tiếp + -дл- DÀI — khớp продолжить k88, длина k133.
(4) завернуть/заворачивать: вер(т)-/ворот- QUAY — khớp вернуть k94, поворот k173.
(5) формировать: -ирова́ть nhấn đuôi — khớp сформировать k219; регули́ровать, компенси́ровать nhấn и.
(6) наградить/награждать: khớp награда k121. (7) разрезать: ре́з- CẮT — khớp отрезать k206.
Họ hàng cố ý vắng: không có (mọi từ đều có họ thật).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "ползти": "bò, trườn, lan truyền",                       # «lan ra» mơ hồ: to spread (of rumours), circulate
    "отставать": "tụt lại sau, bị bỏ lại, chậm hơn, để yên, thôi quấy rầy, bong ra",   # + leave alone; come off
    "отстать": "tụt lại sau, bị bỏ lại, chậm hơn, để yên, thôi quấy rầy, bong ra",
    "продлевать": "gia hạn, kéo dài",                         # «nối dài» là vật thể (удлинить)
    "продлить": "gia hạn, kéo dài",
    "завернуть": "gói, bọc, rẽ, ghé vào, vặn chặt, xắn lên",  # + turn; drop in; screw tight; roll up
    "заворачивать": "gói, bọc, rẽ, ghé vào, vặn chặt, xắn lên",   # thiếu hẳn wrap
    "арендовать": "thuê, mướn",                               # «thuê dài hạn» lặp + không có trong gloss
    "характеризовать": "mô tả, nhận xét, nêu đặc điểm, nói lên đặc điểm",   # bỏ «đánh giá», chữ «của» treo
    "урегулировать": "giải quyết, dàn xếp, hòa giải, điều chỉnh",  # «làm ổn» gượng; + adjust / regulate
    "формировать": "tạo thành, hình thành, lập, gây dựng",    # y hệt сформировать (cặp thể)
    "остывать": "nguội đi, lạnh đi, bình tĩnh lại, mất hứng thú",
    "остыть": "nguội đi, lạnh đi, bình tĩnh lại, mất hứng thú",
    "наградить": "khen thưởng, tặng thưởng, trao thưởng, trao huân chương",
    "награждать": "khen thưởng, tặng thưởng, trao thưởng, trao huân chương",
    "разрезать": "cắt ra, cắt thành miếng, xẻ",               # «chia bằng dao» là lời giải thích
}

# --------------------------------------------------------------------- ползти
S["ползти"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">полз-</span>'
    '<span class="hd-gloss">BÒ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ти́</span>'
    '<span class="hd-gloss">đuôi nguyên thể nhấn cuối — như <b>идти́</b>, <b>нести́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Động từ chuyển động MỘT HƯỚNG: đang bò về một phía; bò qua bò lại, bò nói '
    'chung là <b>по́лзать</b>. Hiện tại nhấn đuôi: <b>ползу́, ползёшь</b>. Nghĩa bóng: tin đồn «bò» '
    'đi ⇒ lan truyền — <b>ползу́т слу́хи</b>.</div>'
    '<div class="hd-warn">Quá khứ giống đực không có <i>-л</i>: <b>полз</b>, rồi <b>ползла́, '
    'ползло́, ползли́</b> — như <b>нёс, несла́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>по́лзать</b> bò (nhiều chiều) · <b>поползти́</b> bắt đầu bò (HT) · '
    '<b>ползунки́</b> quần cho bé tập bò</div>'
)

# ------------------------------------------------------------------ отставать
S["отставать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">RỜI RA, tách khỏi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ста-</span>'
    '<span class="hd-gloss">ĐỨNG — như <b>встать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва́-ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đứng rời khỏi đoàn đang đi ⇒ tụt lại; rời khỏi người ta ⇒ để yên, thôi quấy '
    'rầy; rời khỏi tường ⇒ bong ra. Hiện tại RỤNG <i>-ва-</i> như <b>встава́ть → встаю́</b>: '
    '<b>отстаю́, отстаёшь</b>. Cặp HT: <b>отста́ть</b>.</div>'
    '<div class="hd-warn">Tụt sau AI: <i>от</i> + cách 2 — <b>отстава́ть от гру́ппы</b>. Đồng hồ '
    'chạy chậm: <b>Часы́ отстаю́т</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отста́ть</b> (HT) · <b>отстава́ние</b> sự tụt hậu · <b>отста́лый</b> lạc '
    'hậu · <b>встава́ть</b> đứng dậy</div>'
)

# -------------------------------------------------------------------- отстать
S["отстать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">RỜI RA, tách khỏi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ста́-ть</span>'
    '<span class="hd-gloss">ĐỨNG — như <b>стать</b>, <b>встать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp HT của <b>отстава́ть</b>: người khác đi tiếp, mình đứng lại ⇒ đã tụt '
    'lại. Tương lai mọc <i>н</i>, y như <b>стать → ста́ну</b>: <b>отста́ну, отста́нешь</b>.</div>'
    '<div class="hd-warn"><b>Отста́нь от меня́!</b> — Để tôi yên! (nghĩa đen: «rời khỏi tôi đi»). '
    'Câu gắt, nói với người lạ là thô.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отстава́ть</b> (CHT) · <b>отста́лый</b> lạc hậu (= đã tụt lại) · '
    '<b>оста́ться</b> ở lại · <b>расста́ться</b> chia tay</div>'
)

# ----------------------------------------------------------------- продлевать
S["продлевать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">kéo tiếp về phía trước — như <b>продолжа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-дл-</span>'
    '<span class="hd-gloss">DÀI — như <b>длина́</b>, <b>дли́нный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ева́-ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Kéo cho DÀI thêm về phía trước ⇒ gia hạn. Thứ được gia hạn đứng cách 4: '
    '<b>продлева́ть ви́зу</b>. Cặp HT: <b>продли́ть</b>.</div>'
    '<div class="hd-warn"><i>-ва-</i> ở đây KHÔNG rụng: <b>продлева́ю, продлева́ешь</b>. Chỉ rụng ở '
    'họ <b>дава́ть</b>, <i>-става́ть</i>, <i>-знава́ть</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>продли́ть</b> (HT) · <b>продле́ние</b> sự gia hạn · <b>дли́ться</b> kéo '
    'dài · <b>дли́нный</b> dài · <b>до́лгий</b> lâu</div>'
)

# ------------------------------------------------------------------- продлить
S["продлить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">kéo tiếp về phía trước — như <b>продо́лжить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-дл-</span>'
    '<span class="hd-gloss">DÀI — như <b>длина́</b>, <b>дли́нный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́-ть</span>'
    '<span class="hd-gloss">đuôi động từ → HT</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm cho DÀI thêm, lắp y như Anh pro-long. Trọng âm nằm ở đuôi suốt: '
    '<b>продлю́, продли́шь</b>. Gia hạn thêm bao lâu: <i>на</i> + cách 4 — <b>продли́ть ви́зу на '
    'ме́сяц</b>. Cặp CHT: <b>продлева́ть</b>.</div>'
    '<div class="hd-warn"><b>продли́ть</b> = kéo dài THỜI HẠN (visa, hợp đồng, kỳ nghỉ) · '
    '<b>продо́лжить</b> = làm tiếp việc đang dở.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>продлева́ть</b> (CHT) · <b>продле́ние</b> sự gia hạn · <b>дли́ться</b> '
    'kéo dài · <b>длина́</b> chiều dài · <b>до́лгий</b> lâu</div>'
)

# ------------------------------------------------------------------ завернуть
S["завернуть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">RA SAU, che khuất — như giới từ <i>за</i> «đằng sau»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вер-</span>'
    '<span class="hd-gloss">QUAY, XOAY — gốc đầy đủ <i>верт-</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ну́-ть</span>'
    '<span class="hd-gloss">một cái, dứt điểm → HT</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Quay giấy cho khuất món đồ ⇒ gói; quay người khuất sau góc phố ⇒ rẽ, tiện '
    'đường thì ghé vào; xoay vòi cho kín ⇒ vặn chặt. Chia như <b>верну́ть</b>: <b>заверну́, '
    'завернёшь</b>.</div>'
    '<div class="hd-warn">Gói VÀO cái gì: <i>в</i> + cách 4 — <b>заверну́ть пода́рок в бума́гу</b>. '
    'Ở quầy hàng: <b>Заверни́те, пожа́луйста!</b> — Gói lại giúp tôi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>завора́чивать</b> (CHT) · <b>верну́ть</b> trả lại · <b>поверну́ть</b> rẽ, '
    'quay · <b>поворо́т</b> chỗ rẽ</div>'
)

# --------------------------------------------------------------- заворачивать
S["заворачивать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">RA SAU, che khuất</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вора́ч-</span>'
    '<span class="hd-gloss">QUAY — gốc <i>ворот-</i>: <i>о → а</i>, <i>т → ч</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành, chia đều: <b>завора́чиваю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>заверну́ть</b>, đủ cả gói lẫn rẽ. Gốc đổi mặt <i>вер ↔ '
    'ворач</i> đúng như <b>поверну́ть ↔ повора́чивать</b>: thuộc một cặp là có cả hai.</div>'
    '<div class="hd-warn"><b>завора́чивать за у́гол</b> — rẽ qua góc phố: sau <i>за</i> là cách 4 '
    'vì đang đi tới đó.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>заверну́ть</b> (HT) · <b>повора́чивать</b> rẽ (CHT) · <b>поворо́т</b> chỗ '
    'rẽ · <b>разворо́т</b> sự quay đầu xe</div>'
)

# ----------------------------------------------------------------- арендовать
S["арендовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">аренд-</span>'
    '<span class="hd-gloss">từ mượn <b>аре́нда</b> sự thuê (gốc Latin)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова́ть</span>'
    '<span class="hd-gloss">đuôi biến danh từ thành động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm việc <b>аре́нда</b> ⇒ thuê. Khi chia <i>-ова-</i> thành <i>-у́-</i>: '
    '<b>аренду́ю, аренду́ешь</b>. Thuê CỦA AI: <i>у</i> + cách 2. Một dạng dùng cho cả hai thể.</div>'
    '<div class="hd-warn"><b>арендова́ть</b> nghe giấy tờ, hợp đồng (văn phòng, xe, đất); thuê căn hộ '
    'để ở, đời thường nói <b>снима́ть кварти́ру</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>аре́нда</b> sự thuê · <b>аренда́тор</b> người thuê · <b>аре́ндный</b> '
    'thuộc về thuê mướn</div>'
)

# ------------------------------------------------------------ характеризовать
S["характеризовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">характер-</span>'
    '<span class="hd-gloss">TÍNH CÁCH, bản chất — <b>хара́ктер</b> (từ mượn, gốc Hy Lạp)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-изова́ть</span>'
    '<span class="hd-gloss">= Anh -ize, đuôi động từ mượn</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng tiếng Anh characterize: nói ra bản chất ⇒ mô tả, nhận xét; hoặc chính '
    'việc ấy để lộ bản chất ⇒ nói lên đặc điểm. Trọng âm dồn về đuôi, khi chia: '
    '<b>характеризу́ю, характеризу́ет</b>. HT hay dùng: <b>охарактеризова́ть</b>.</div>'
    '<div class="hd-warn">Nhận xét ai LÀ thế nào: <i>как</i> + cách 4 — <b>Его́ характеризу́ют как '
    'че́стного челове́ка.</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>хара́ктер</b> tính cách · <b>характе́рный</b> đặc trưng · '
    '<b>характери́стика</b> đặc điểm, bản nhận xét</div>'
)

# ------------------------------------------------------------------ упаковать
S["упаковать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố thể hoàn thành, không mang nghĩa riêng rõ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пак-</span>'
    '<span class="hd-gloss">GÓI — từ mượn, gốc như Anh pack; có trong <b>паке́т</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова́ть</span>'
    '<span class="hd-gloss">đuôi động từ, chia <b>-у́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghe pack là ra nghĩa: đóng gói, xếp vali. Chia: <b>упаку́ю, упаку́ешь</b>. '
    'Cặp CHT: <b>упако́вывать</b>. Đổi <i>у-</i> sang <i>рас-</i> là mở gói: '
    '<b>распакова́ть</b>.</div>'
    '<div class="hd-warn"><b>упакова́ть</b> = đóng vào hộp, vali, bao bì · <b>заверну́ть</b> = quấn '
    'giấy, vải quanh món đồ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>упако́вка</b> bao bì · <b>пакова́ть</b> đóng gói (CHT, khẩu ngữ) · '
    '<b>паке́т</b> cái túi, gói</div>'
)

# --------------------------------------------------------------- регулировать
S["регулировать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">регул-</span>'
    '<span class="hd-gloss">Latin regula cây thước, quy tắc — như <b>регуля́рный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ровать</span>'
    '<span class="hd-gloss">đuôi động từ mượn, chia <b>-и́рую</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đưa về «đúng thước», như Anh regulate: điều chỉnh âm lượng, điều tiết giao '
    'thông — <b>регули́ровать движе́ние</b>. Thứ được chỉnh đứng cách 4. HT khi chỉnh máy móc: '
    '<b>отрегули́ровать</b>.</div>'
    '<div class="hd-warn">Nhấn <i>и́</i> và đứng yên: <b>регули́рую, регули́руешь</b> — khác '
    '<b>формирова́ть → формиру́ю</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>урегули́ровать</b> dàn xếp (HT) · <b>регули́рование</b> sự điều tiết · '
    '<b>регуля́тор</b> bộ điều chỉnh · <b>регуля́рный</b> đều đặn</div>'
)

# -------------------------------------------------------------- урегулировать
S["урегулировать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">ở đây: làm cho XONG, ĐƯỢC việc → HT</span></div>'
    '<div class="hd-row"><span class="hd-piece">-регул-</span>'
    '<span class="hd-gloss">Latin regula cây thước, quy tắc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ровать</span>'
    '<span class="hd-gloss">đuôi động từ mượn, chia <b>-и́рую</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đưa chuyện rối về «đúng quy tắc» cho xong ⇒ giải quyết, dàn xếp. Trọng âm '
    'đứng yên: <b>урегули́рую, урегули́руешь</b>.</div>'
    '<div class="hd-warn">Hay đi với tranh chấp, quan hệ: <b>урегули́ровать конфли́кт</b>. Chỉnh máy, '
    'chỉnh âm lượng thì thường dùng <b>отрегули́ровать</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>регули́ровать</b> điều chỉnh (CHT) · <b>урегули́рование</b> sự dàn xếp · '
    '<b>регуля́рный</b> đều đặn</div>'
)

# ---------------------------------------------------------------- формировать
S["формировать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">форм-</span>'
    '<span class="hd-gloss">HÌNH, KHUÔN — chính là <b>фо́рма</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ирова́ть</span>'
    '<span class="hd-gloss">đuôi động từ mượn</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúc cho thành hình, như Anh form: <b>формирова́ть хара́ктер</b> gây dựng '
    'tính cách, <b>формирова́ть прави́тельство</b> lập chính phủ. Cặp HT: <b>сформирова́ть</b>; tự '
    'nó thành hình thì thêm <i>-ся</i>: <b>формирова́ться</b>.</div>'
    '<div class="hd-warn">Nguyên thể nhấn đuôi, khi chia nhấn <i>-у́-</i>: <b>формиру́ю, '
    'формиру́ешь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сформирова́ть</b> (HT) · <b>формирова́ние</b> sự hình thành · '
    '<b>фо́рма</b> hình dạng · <b>рефо́рма</b> cải cách</div>'
)

# ------------------------------------------------------------- компенсировать
S["компенсировать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">компенс-</span>'
    '<span class="hd-gloss">BÙ — Latin compensare, như <b>компенса́ция</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ровать</span>'
    '<span class="hd-gloss">= Anh -ate, đuôi động từ mượn</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">compensate → <b>компенси́ровать</b>. Trọng âm đứng yên ở <i>и́</i>: '
    '<b>компенси́рую, компенси́руешь</b>. Một dạng dùng cho cả hai thể.</div>'
    '<div class="hd-warn">Bù CÁI GÌ là cách 4, không giới từ (Anh: compensate FOR); bù CHO AI là '
    'cách 3: <b>компенси́ровать рабо́чим уще́рб</b>. Chữ <i>за</i> đi với danh từ: <b>компенса́ция '
    'за уще́рб</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>компенса́ция</b> sự đền bù, tiền bồi thường</div>'
)

# ------------------------------------------------------------------- остывать
S["остывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">ở đây: chuyển hẳn sang trạng thái đó</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сты-</span>'
    '<span class="hd-gloss">LẠNH ĐI — động từ <b>стыть</b> nguội dần</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва́-ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đồ nóng nguội dần: <b>Суп остыва́ет!</b> Người «nóng» nguội dần ⇒ bình tĩnh '
    'lại, mất hứng thú. Cặp HT: <b>осты́ть</b>.</div>'
    '<div class="hd-warn"><i>-ва-</i> KHÔNG rụng: <b>остыва́ю, остыва́ешь</b> — khác <b>отстава́ть → '
    'отстаю́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>осты́ть</b> (HT) · <b>стыть</b> nguội dần · họ xa (<i>сты-/студ-</i> '
    'LẠNH): <b>просту́да</b> cảm lạnh, <b>простуди́ться</b> bị cảm</div>'
)

# --------------------------------------------------------------------- остыть
S["остыть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">ở đây: chuyển hẳn sang trạng thái đó → HT</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сты́-ть</span>'
    '<span class="hd-gloss">LẠNH ĐI — động từ <b>стыть</b> nguội dần</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đã nguội hẳn: <b>Чай осты́л.</b> Với người: đã nguôi giận. Cặp CHT: '
    '<b>остыва́ть</b>. Hết hứng VỚI cái gì: <i>к</i> + cách 3 — <b>осты́ть к му́зыке</b>.</div>'
    '<div class="hd-warn">Tương lai mọc <i>н</i>, như <b>стать → ста́ну</b>: <b>осты́ну, осты́нешь</b>; '
    'mệnh lệnh <b>Осты́нь!</b> = Bình tĩnh lại đi!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>остыва́ть</b> (CHT) · <b>стыть</b> nguội dần · họ xa (<i>сты-/студ-</i> '
    'LẠNH): <b>просту́да</b> cảm lạnh, <b>простуди́ться</b> bị cảm</div>'
)

# --------------------------------------------------------------------- шагать
S["шагать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">шаг-</span>'
    '<span class="hd-gloss">BƯỚC CHÂN — chính là <b>шаг</b>, gốc trơn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi động từ, chia đều: <b>шага́ю, шага́ешь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bước hết bước này tới bước khác ⇒ sải bước, đi bộ. Bước trên cái gì: '
    '<i>по</i> + cách 3 — <b>шага́ть по у́лице</b>.</div>'
    '<div class="hd-warn">Bước đúng MỘT bước thì dùng thể HT đuôi <i>-ну-</i>: <b>шагну́ть</b> — '
    '<b>шагну́ть вперёд</b> bước lên một bước.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>шаг</b> bước chân · <b>шагну́ть</b> bước một bước (HT) · '
    '<b>перешагну́ть</b> bước qua · <b>шажо́к</b> bước nhỏ</div>'
)

# ------------------------------------------------------------------ наградить
S["наградить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">lên, trao vào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-град-</span>'
    '<span class="hd-gloss">gốc của <b>награ́да</b> phần thưởng, nay không đứng riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́-ть</span>'
    '<span class="hd-gloss">đuôi động từ → HT</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trao <b>награ́да</b> cho ai ⇒ khen thưởng. Chỉ ngôi «tôi» đổi <i>д → ж</i>: '
    '<b>награжу́</b>, rồi <b>награди́шь, наградя́т</b>. Cặp CHT: <b>награжда́ть</b>.</div>'
    '<div class="hd-warn">NGƯỜI ở cách 4, PHẦN THƯỞNG ở cách 5: <b>награди́ть геро́я о́рденом</b> — '
    'ngược với «tặng cái gì cho ai».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>награжда́ть</b> (CHT) · <b>награ́да</b> phần thưởng · '
    '<b>награжде́ние</b> lễ trao thưởng</div>'
)

# ----------------------------------------------------------------- награждать
S["награждать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">lên, trao vào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-гражд-</span>'
    '<span class="hd-gloss">gốc của <b>награ́да</b> phần thưởng, <i>д → жд</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́-ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành, chia đều: <b>награжда́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>награди́ть</b>. Chữ <i>жд</i> chỉ là <i>д</i> biến âm, như '
    '<b>победи́ть → побежда́ть</b> — không dính gì tới <b>ждать</b> «chờ».</div>'
    '<div class="hd-warn">Thưởng BẰNG gì: cách 5; thưởng VÌ gì: <i>за</i> + cách 4 — <b>награжда́ть '
    'меда́лью за сме́лость</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>награди́ть</b> (HT) · <b>награ́да</b> phần thưởng · <b>награжде́ние</b> '
    'lễ trao thưởng</div>'
)

# ------------------------------------------------------------------ разрезать
S["разрезать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раз-</span>'
    '<span class="hd-gloss">TÁCH RA từng phần</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ре́з-а-ть</span>'
    '<span class="hd-gloss">CẮT — chính là <b>ре́зать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cắt cho cả khối TÁCH thành nhiều phần: <b>разре́зать торт</b>; khác '
    '<b>отре́зать</b> — cắt rời MỘT miếng ra. Như <b>ре́зать</b>, <i>з → ж</i> ở mọi ngôi: '
    '<b>разре́жу, разре́жешь</b>. Cắt thành mấy phần: <i>на</i> + cách 4.</div>'
    '<div class="hd-warn">Cùng mặt chữ, chỉ khác chỗ nhấn: <b>разре́зать</b> (HT, cắt xong) · '
    '<b>разреза́ть</b> (CHT, chia đều <b>разреза́ю</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ре́зать</b> cắt · <b>отре́зать</b> cắt rời · <b>наре́зать</b> thái ra · '
    '<b>разре́з</b> đường cắt, mặt cắt · <b>ре́зкий</b> gắt, đột ngột</div>'
)

B = {
    "docbangmat": 130,
    "loitubat": 3,   # отстать: viết «Отстань! CHỈ dùng với người thân» (nói quá) -> «nói với người lạ là thô»
                     # урегулировать: viết «KHÔNG dùng» cho máy móc như luật cấm -> «thường dùng отрегули́ровать»
                     # компенсировать: viết «за CHỈ theo danh từ» -> «за đi với danh từ»
    "nguonsai": 2,   # ползти: «trọng âm dịch trong quá khứ» — thật ra nhấn đuôi suốt, điểm lạ là полз không -л
                     # разрезать: «không suy được» — chia y ре́зать, з -> ж
    "baolen": [
        "V cần duyệt (16 thẻ): ползти (lan ra -> lan truyền, bỏ bò lổm ngổm) · отставать, отстать (THÊM để yên, thôi quấy rầy, bong ra) · продлевать, продлить (BỎ nối dài) · завернуть, заворачивать (cùng dãy; THÊM rẽ / gói, ghé vào, vặn chặt, xắn lên) · арендовать (BỎ thuê dài hạn) · характеризовать (BỎ đánh giá) · урегулировать (làm ổn -> điều chỉnh) · формировать (y hệt сформировать) · остывать, остыть (cùng dãy, THÊM mất hứng thú) · наградить, награждать (cùng dãy) · разрезать (BỎ chia bằng dao). Giữ nguyên: упаковать, регулировать, компенсировать, шагать.",
        "«ghé vào» lấy từ gloss завернуть (drop in), gloss заворачивать không ghi riêng; «mất hứng thú» lấy từ gloss остывать, gloss остыть không ghi — nhập chung vì cùng cặp thể.",
        "Trùng hết nghĩa chỉ giữa 5 cặp thể trong lô và формировать ↔ сформировать [k219]: badge thể tách. Chưa chạy lại vacham với V mới (không đọc Anki); nên chạy riêng арендовать «thuê, mướn» ↔ нанимать/нанять.",
        "Cần nhìn badge: арендовать, компенсировать trên thẻ ghi «một dạng dùng cho cả hai thể» (theo từ điển Nga: сов. и несов.) — nếu AspectBadge in chỉ IMPF thì hai bên đá nhau. характеризовать cũng hai thể theo từ điển; thẻ chỉ nói HT hay dùng là охарактеризовать.",
        "урегулировать KHÔNG san V với регулировать: nghĩa chính khác (dàn xếp ↔ điều chỉnh), HT chỉnh máy là отрегулировать.",
        "Không chắc: остыть ↔ простуда ghi «họ xa» (сты-/студ- theo từ nguyên); cố ý không nối стыд «xấu hổ» dù từ nguyên có gắn. за- «ra sau, che khuất» ở завернуть là cách hiểu để nhớ, từ điển không tách nghĩa tiền tố.",
        "Máy sót họ: остыть ↔ простудиться [k150]; упаковать ↔ пакет [k24].",
    ],
}
