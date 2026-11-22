# -*- coding: utf-8 -*-
"""k164 — qualities (lô trộn): gửi đi, bắn, chạm, thành ra, lỗ, áp lực + tính từ/danh từ mượn.

Chỗ cần nhất quán trong lô:
(1) в→вл ở ngôi «tôi» lặp ở hai họ: отпра́вить → отпра́влю (→ отправля́ть), дави́ть → давлю́ (→ давле́ние).
(2) cặp thể отпра́вить / отправля́ть: от- + пра́вить «hướng, điều khiển» — KHÔNG lấy пра́во/пра́вый làm họ hàng.
(3) cặp thể вы́стрелить / стреля́ть: gốc стрел- = стрела́ «mũi tên».
(4) cặp thể каса́ться / косну́ться: кас-/кос- luân phiên, -ну- = một lần; cả hai đòi cách 2.
(5) получа́ться / получи́ться = получа́ть / получи́ть + -ся — giữ khối «по-луч-» như thẻ cũ.
Họ hàng cố ý vắng: ве́рсия (mượn, đứng một mình; университе́т là báo oan của máy).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "отправлять": "gửi đi, phái đi",                  # «gửi» nằm gọn trong посылать; đồng bộ cặp отправить
    "выстрелить": "bắn, nổ súng",                     # bỏ «một phát» (nhãn thể trá hình); to fire
    "касаться": "chạm, liên quan đến, đề cập",        # «;» -> «,»; to mention
    "коснуться": "chạm, liên quan đến, đề cập",       # đồng bộ cặp касаться, badge thể tách
    "получаться": "làm được, thành ra, ra kết quả",   # bỏ «nên hình»; KHÔNG «thành công»: đẩy удаваться (làm được, thành công) nằm gọn trong đề này
    "получиться": "làm được, thành ra, ra kết quả",   # đồng bộ cặp получаться; bỏ «thành công» vì удаться
    "дыра": "lỗ, lỗ thủng, chỗ hổng, nơi hẻo lánh",   # «;» -> «,»; backwater
    "давление": "áp suất, áp lực, huyết áp",          # «;» -> «,»; thiếu nghĩa vật lý «áp suất»
    "внешний": "bên ngoài, bề ngoài, đối ngoại",      # «ngoại» trơ trọi -> outward/external
    "реальный": "thực, thực tế, khả thi",             # «;» -> «,»; real/actual
    "обстоятельство": "hoàn cảnh, tình huống",        # «;» -> «,»
    "комплекс": "tổ hợp, khu phức hợp, mặc cảm",      # «;» -> «,»; thêm nghĩa tâm lý (комплекс неполноценности)
    "деталь": "chi tiết, bộ phận, linh kiện",         # «;» -> «,»; part/component
    "стиль": "phong cách, kiểu",                      # «;» -> «,»
    "версия": "phiên bản, dị bản",                    # «;» -> «,»
}

# --------------------------------------------------------------------- отправить
S["отправить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">RỜI ĐI, tách khỏi mình</span></div>'
    '<div class="hd-row"><span class="hd-piece">-прав-</span>'
    '<span class="hd-gloss">HƯỚNG, điều khiển — gốc của <b>пра́вить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Hướng cho rời khỏi mình» = gửi đi. Người nhận cách 3, vật gửi cách 4: '
    '<i>отпра́вить ма́ме письмо́</i>. Ngôi «tôi» chêm <b>л</b>: <b>отпра́влю</b>, rồi lại '
    '<b>отпра́вишь</b> — chính <b>вл</b> đó đi vào cặp thể <b>отправля́ть</b>.</div>'
    '<div class="hd-warn">Thêm <b>-ся</b> là TỰ mình đi: <b>отпра́виться</b> — lên đường, khởi '
    'hành.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отправля́ть</b> gửi đi (CHT) · <b>отправи́тель</b> người gửi · '
    '<b>напра́вить</b> hướng về · <b>испра́вить</b> sửa cho đúng</div>'
)

# --------------------------------------------------------------------- отправлять
S["отправлять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-прав-</span>'
    '<span class="hd-gloss">RỜI ĐI + HƯỚNG — như <b>отпра́вить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-л-я́ть</span>'
    '<span class="hd-gloss"><b>л</b> mượn từ <b>отпра́влю</b> + đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gửi nhiều lần, hay đang gửi; bảng chia đều: <b>отправля́ю, '
    'отправля́ешь</b>. So với <b>посыла́ть</b> thì nghe chính thức hơn — giọng bưu điện, nhà ga.</div>'
    '<div class="hd-warn"><b>По́езд отправля́ется в де́сять.</b> — Tàu khởi hành lúc mười giờ '
    '(<b>-ся</b> = tự đi).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отпра́вить</b> gửi đi (HT) · <b>отправле́ние</b> sự gửi, sự khởi hành · '
    '<b>отправи́тель</b> người gửi</div>'
)

# --------------------------------------------------------------------- выстрелить
S["выстрелить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы́-</span>'
    '<span class="hd-gloss">RA NGOÀI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-стрел-</span>'
    '<span class="hd-gloss">MŨI TÊN — <b>стрела́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Phóng mũi tên ra» = bắn MỘT phát; cặp thể của <b>стреля́ть</b> (bắn nói '
    'chung, bắn liên hồi). Như mọi động từ HT có <b>вы́-</b>, trọng âm dính chặt vào nó: '
    '<b>вы́стрелю, вы́стрелишь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вы́стрел</b> phát súng · <b>стреля́ть</b> bắn (CHT) · <b>стрела́</b> '
    'mũi tên · <b>стре́лка</b> kim đồng hồ, mũi tên chỉ đường</div>'
)

# --------------------------------------------------------------------- стрелять
S["стрелять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">стрел-</span>'
    '<span class="hd-gloss">MŨI TÊN — <b>стрела́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thời cung tên thì «bắn tên», nay dùng cho súng. Chia đều: <b>стреля́ю, '
    'стреля́ешь</b>. Một phát duy nhất là <b>вы́стрелить</b>; bắn chết là <b>застрели́ть</b>.</div>'
    '<div class="hd-warn">Bắn VÀO ai: <b>в</b> + cách 4 — <i>стреля́ть в цель</i>. Bắn BẰNG súng '
    'gì: <b>из</b> + cách 2 — <i>стреля́ть из ружья́</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вы́стрелить</b> bắn một phát (HT) · <b>вы́стрел</b> phát súng · '
    '<b>стрело́к</b> xạ thủ · <b>стре́лка</b> kim đồng hồ</div>'
)

# --------------------------------------------------------------------- касаться
S["касаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кас-</span>'
    '<span class="hd-gloss">CHẠM (trong cặp thể đổi thành <b>кос-</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть-ся</span>'
    '<span class="hd-gloss">đuôi CHT + <b>-ся</b> bắt buộc (không có «касать»)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chạm tay → «chạm» tới chuyện của ai = liên quan. Cái bị chạm đứng ở '
    '<b>cách 2</b>, không phải cách 4: <i>каса́ться руки́</i>. Cặp thể: <b>косну́ться</b>.</div>'
    '<div class="hd-warn"><b>Э́то тебя́ не каса́ется.</b> — Chuyện này không liên quan tới cậu. · '
    '<b>что каса́ется</b> + cách 2 — còn về…: <i>что каса́ется меня́</i> — còn về phần tôi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>косну́ться</b> chạm (HT) · <b>прикосну́ться</b> chạm nhẹ · '
    '<b>прикоснове́ние</b> sự chạm · <b>каса́тельная</b> tiếp tuyến</div>'
)

# --------------------------------------------------------------------- коснуться
S["коснуться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кос-</span>'
    '<span class="hd-gloss">CHẠM — cùng gốc <b>кас-</b>, nguyên âm đổi <b>а→о</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ну-</span>'
    '<span class="hd-gloss">MỘT lần, một cái</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть-ся</span>'
    '<span class="hd-gloss">đuôi nguyên thể + <b>-ся</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chạm một cái là xong = HT của <b>каса́ться</b>; vẫn đòi cách 2: '
    '<i>косну́ться вопро́са</i> — đề cập tới vấn đề. Chia: <b>косну́сь, коснёшься</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>каса́ться</b> chạm (CHT) · <b>прикосну́ться</b> chạm nhẹ · '
    '<b>неприкоснове́нный</b> bất khả xâm phạm</div>'
)

# --------------------------------------------------------------------- получаться
S["получаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">получа́ть</span>'
    '<span class="hd-gloss">NHẬN ĐƯỢC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">tự nó — việc tự «ra được»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Kết quả tự «về tay» = thành, ra được. Chủ ngữ là VIỆC, còn người làm đứng '
    'sau <b>у</b> + cách 2. Cặp thể: <b>получи́ться</b>.</div>'
    '<div class="hd-warn"><b>У меня́ не получа́ется.</b> — Mình làm mãi không được. Đừng nói '
    '«я не получа́юсь».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>получи́ться</b> thành (HT) · <b>получа́ть</b> nhận · '
    '<b>получа́тель</b> người nhận</div>'
)

# --------------------------------------------------------------------- получиться
S["получиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">получи́ть</span>'
    '<span class="hd-gloss">NHẬN ĐƯỢC (HT)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">tự nó — việc tự «ra được»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">HT của <b>получа́ться</b>: ra kết quả xong. Trọng âm theo đúng '
    '<b>получи́ть</b>: <b>получу́сь</b> nhưng <b>полу́чится</b>. Hay gặp nhất ở ngôi 3 và quá '
    'khứ: <b>получи́лось</b>.</div>'
    '<div class="hd-warn"><b>Получи́лось!</b> — Được rồi! · <b>Получи́лось так, что…</b> — Chuyện '
    'thành ra là…</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>получа́ться</b> thành (CHT) · <b>получи́ть</b> nhận (HT)</div>'
)

# --------------------------------------------------------------------- дыра
S["дыра"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Lỗ thủng nói chung, thường là lỗ to. Lỗ nhỏ hằng ngày (áo rách, tất '
    'thủng) người ta nói <b>ды́рка</b> — đuôi <b>-ка</b> thu nhỏ. Số nhiều trọng âm lùi về gốc: '
    '<b>ды́ры</b>.</div>'
    '<div class="hd-warn"><b>чёрная дыра́</b> — lỗ đen. Nói về một nơi: <i>Э́то не го́род, а '
    'дыра́!</i> — chỗ khỉ ho cò gáy.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ды́рка</b> cái lỗ · <b>ды́рочка</b> lỗ nhỏ xíu · <b>дыря́вый</b> '
    'thủng lỗ chỗ</div>'
)

# --------------------------------------------------------------------- давление
S["давление"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дав-л-</span>'
    '<span class="hd-gloss">ÉP, ĐÈ — <b>дави́ть</b>, ngôi «tôi» <b>давлю́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ние</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Sự đè ép: áp suất (vật lý), áp lực (lên người). <b>л</b> chêm vào y như '
    '<b>отпра́вить → отпра́влю</b>. Gây áp lực lên ai: <i>ока́зывать давле́ние на</i> + cách 4.</div>'
    '<div class="hd-warn">Đứng trơ trọi thường là <b>huyết áp</b>: <i>У меня́ давле́ние</i> — mình '
    'bị tăng huyết áp.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дави́ть</b> ép, đè · <b>подави́ть</b> đàn áp, dập tắt · <b>да́вка</b> '
    'cảnh chen lấn</div>'
)

# --------------------------------------------------------------------- внешний
S["внешний"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вне</span>'
    '<span class="hd-gloss">Ở NGOÀI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-шн-ий</span>'
    '<span class="hd-gloss">biến trạng từ thành tính từ, đuôi MỀM</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>-шний</b> là khuôn quen: <b>вчера́</b> → <b>вчера́шний</b>, <b>до́ма</b> '
    '→ <b>дома́шний</b>. Đuôi mềm nên <b>вне́шняя, вне́шнее</b>. Trái nghĩa: <b>вну́тренний</b>. '
    'Dạng ngắn rất hiếm dùng.</div>'
    '<div class="hd-warn"><b>вне́шняя поли́тика</b> — chính sách đối ngoại · <b>вне́шность</b> — '
    'ngoại hình.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вне</b> ngoài · <b>извне́</b> từ bên ngoài · <b>вне́шность</b> ngoại '
    'hình</div>'
)

# --------------------------------------------------------------------- конкретный
S["конкретный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">конкре́т-</span>'
    '<span class="hd-gloss">mượn Latin, như tiếng Anh <i>concrete</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><i>Concrete</i> theo nghĩa «cụ thể»: <i>конкре́тный приме́р</i> — ví dụ cụ '
    'thể. Trạng từ <b>конкре́тно</b> — cụ thể là.</div>'
    '<div class="hd-warn">Chỉ có nghĩa «cụ thể»: bê tông là <b>бето́н</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>конкре́тно</b> cụ thể là · <b>конкретизи́ровать</b> cụ thể hoá</div>'
)

# --------------------------------------------------------------------- реальный
S["реальный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">реа́л-</span>'
    '<span class="hd-gloss">mượn Latin, như tiếng Anh <i>real</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ьн-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Có thật, hoặc làm được thật: <i>реа́льный план</i> — kế hoạch khả thi. '
    'Dạng ngắn chêm <b>е</b>: <b>реа́лен</b>, còn lại đều <b>реа́льна, реа́льны</b>.</div>'
    '<div class="hd-warn"><b>реа́льно</b> trong khẩu ngữ = «thật luôn, thật sự»: <i>Э́то реа́льно '
    'тру́дно</i> — cái này khó thật sự.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>реа́льность</b> hiện thực · <b>реализова́ть</b> hiện thực hoá · '
    '<b>реали́зм</b> chủ nghĩa hiện thực</div>'
)

# --------------------------------------------------------------------- обстоятельство
S["обстоятельство"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">QUANH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-стоя́-</span>'
    '<span class="hd-gloss">ĐỨNG — <b>стоя́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-тельств-о</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Những gì «đứng quanh» sự việc = hoàn cảnh — khớp từng mảnh với tiếng Anh '
    '<i>circum-stance</i> (quanh + đứng). Trong ngữ pháp còn là «trạng ngữ».</div>'
    '<div class="hd-warn">Hay dùng số nhiều: <b>по семе́йным обстоя́тельствам</b> — vì lý do gia '
    'đình.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>стоя́ть</b> đứng · <b>состоя́ние</b> trạng thái · <b>обстано́вка</b> '
    'tình hình, cách bài trí · <b>обстоя́тельный</b> tỉ mỉ, chu đáo</div>'
)

# --------------------------------------------------------------------- комплекс
S["комплекс"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga — mượn Latin, như tiếng Anh <i>complex</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hai nghĩa như tiếng Anh: tổ hợp — <i>жило́й ко́мплекс</i> khu chung cư phức '
    'hợp; và mặc cảm — <i>ко́мплекс неполноце́нности</i> mặc cảm tự ti.</div>'
    '<div class="hd-warn">Trọng âm DỊCH khi thêm đuôi: <b>ко́мплекс</b> → <b>компле́ксный</b> '
    'tổng hợp, toàn diện.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>компле́ксный</b> tổng hợp, toàn diện</div>'
)

# --------------------------------------------------------------------- деталь
S["деталь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga — mượn tiếng Pháp <i>détail</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hai nghĩa: chi tiết (<i>во всех дета́лях</i> — đủ mọi chi tiết) và linh '
    'kiện máy (<i>дета́ли маши́ны</i>). Đuôi <b>-ь</b> mà giống CÁI: <b>дета́ли</b>, '
    '<b>дета́лью</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дета́льный</b> chi tiết, tỉ mỉ · <b>дета́льно</b> một cách chi tiết</div>'
)

# --------------------------------------------------------------------- стиль
S["стиль"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga — mượn, như tiếng Anh <i>style</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi <b>-ь</b> nhưng giống ĐỰC — khác <b>дета́ль</b>: <i>мой стиль</i>, '
    'số nhiều <b>сти́ли</b>. <i>в сти́ле</i> + cách 2 — theo phong cách…</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сти́льный</b> sành điệu, hợp mốt · <b>стили́ст</b> nhà tạo mẫu</div>'
)

# --------------------------------------------------------------------- версия
S["версия"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga — mượn Latin, như tiếng Anh <i>version</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi <b>-ия</b> như <b>ста́нция</b>: giống cái. Ngoài «phiên bản» '
    '(<i>но́вая ве́рсия</i>), còn là một cách giải thích sự việc: <i>по одно́й ве́рсии</i> — theo '
    'một giả thuyết.</div>'
)

B = {
    "docbangmat": 69,
    "loitubat": 1,
    "nguonsai": 0,
    "baolen": [
        "Va chạm отправля́ть ⊂ посыла́ть đã gỡ: cặp отпра́вить/отправля́ть cùng «gửi đi, phái đi» (bỏ «gửi» trơn). KHÔNG thêm «gửi» vào отправить: làm thế thì посла́ть «gửi, phái đi» [k88 đã nạp] nằm gọn trong отправить. Bỏ «chuyển tiếp» (to forward) vì đó là việc của переслать.",
        "V получа́ться/получи́ться = «làm được, thành ra, ra kết quả» — cố ý KHÔNG có «thành công»: có thì удава́ться/уда́ться «làm được, thành công» (đã có thẻ) nằm gọn trong đề này (máy giả lập bắt được, đã gỡ). Đổi lại получи́ться mất «thành công» trên đề bài — cần duyệt; phương án khác là получи́ться giữ «thành công» bỏ «làm được» (cặp lệch nhau, vẫn không va chạm).",
        "Đã giả lập do_va_cham (chỉ đọc Anki, áp V lô này): trùng đủ 4 badge dính k164 = 0. Bỏ lọc badge thì còn bốn cặp thể trong lô (badge thể tách): выстрелить⊃стрелять «bắn», касаться=коснуться, отправить=отправлять, получаться=получиться.",
        "V комплекс thêm «mặc cảm» (комплекс неполноценности) — gloss Anh chỉ ghi «complex», nghĩa tâm lý nằm trong chữ đó; nếu luồng chính coi là nới rộng thì bỏ.",
        "Không chắc: внешний — từ điển in dạng ngắn вне́шен/вне́шня…, thẻ chỉ nói «dạng ngắn rất hiếm dùng», không liệt kê. дыра́ khai «gốc trơn» (từ nguyên nối với драть còn tranh cãi nên không nêu). обстано́вка xếp họ với стоя́ть theo gốc ста- (từ nguyên).",
        "Họ hàng cố ý vắng: ве́рсия (mượn, đứng một mình). Bác báo oan máy отправить↔право/правый (dùng пра́вить/напра́вить/испра́вить thay), комплекс↔лексика, версия↔университет.",
        "Lỗi tự bắt (1): получиться ghi «gần như chỉ dùng ngôi 3 và quá khứ giống trung» — nói quá (получи́лся, получи́лась vẫn thường gặp), đã sửa thành «hay gặp nhất ở ngôi 3 và quá khứ».",
    ],
}
