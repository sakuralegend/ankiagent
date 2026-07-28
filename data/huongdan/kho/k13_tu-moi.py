# -*- coding: utf-8 -*-
"""k13 — tu-moi: 4 từ user vừa thêm, KHÔNG cùng họ nhau.

Không có trục chung, không có khối hệ thống dùng chung (README §3):
mỗi thẻ tự đứng, chỉ nói kiến thức dính TRỰC TIẾP vào chính từ đó.
"""

S = {}
V = {}

# ─────────────────────────────────────────────────────────── здание
S["здание"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">зд-</span>'
    '<span class="hd-gloss">gốc cổ XÂY, NẶN (đắp từ đất sét)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ние</span>'
    '<span class="hd-gloss">đuôi biến việc làm thành DANH TỪ, luôn giống TRUNG</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái được dựng lên — cùng gốc với <b>созда́ть</b> (tạo ra). '
    'Nói về <b>khối công trình</b>; còn nhà theo nghĩa chỗ ở, tổ ấm là <b>дом</b>.</div>'
    '<div class="hd-warn">Danh từ đuôi <b>-ие</b> vào cách 6 thành <b>-ии</b>: '
    '<b>в зда́нии</b> (trong toà nhà), không phải -е.</div>'
    '<div class="hd-warn">Trông giống <b>здра́вствуйте</b>, <b>здоро́вье</b> nhưng KHÔNG '
    'họ hàng: hai từ kia từ gốc "khoẻ", <b>зда́ние</b> từ gốc "xây".</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>созда́ть</b> tạo ra · <b>созда́ние</b> sự tạo ra; sinh vật · '
    '<b>зо́дчий</b> kiến trúc sư (từ cổ)</div>'
)
V["здание"] = "tòa nhà, khối công trình xây dựng (không phải nhà ở, tổ ấm)"

# ─────────────────────────────────────────────────────────── лучше
S["лучше"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">луч-</span>'
    '<span class="hd-gloss">gốc cổ "tốt hơn", không đứng riêng (còn trong <b>лу́чший</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ше</span>'
    '<span class="hd-gloss">đuôi SO SÁNH HƠN: <b>да́льше</b>, <b>ра́ньше</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>хорошо́</b> / <b>хоро́ший</b> không tự làm ra dạng so sánh — '
    'tiếng Nga đổi hẳn sang gốc khác, y như tiếng Anh <i>good → better</i>.</div>'
    '<div class="hd-warn">Một mặt chữ gánh cả hai vai và không bao giờ đổi đuôi: '
    '"hay hơn" cho động từ (<b>говори́ть лу́чше</b>) và "tốt hơn" cho tính từ '
    '(<b>э́тот оте́ль лу́чше</b>).</div>'
    '<div class="hd-warn">So với ai: <b>лу́чше меня́</b> (cách 2) hoặc '
    '<b>лу́чше, чем я</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лу́чший</b> tốt nhất · <b>ху́же</b> tệ hơn (cũng đổi gốc, '
    'từ <b>пло́хо</b>) · <b>Лу́чше по́здно, чем никогда́</b> muộn còn hơn không</div>'
)
V["лучше"] = "tốt hơn, hay hơn (dạng SO SÁNH HƠN của “tốt”)"

# ─────────────────────────────────────────────────────────── отель
S["отель"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn nguyên khối tiếng Pháp <i>hôtel</i> '
    '(chữ h câm nên tiếng Nga không có х-).</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhận mặt ngay qua tiếng Anh <i>hotel</i>. Xa hơn: La Tinh '
    '<i>hospes</i> = chủ nhà đón khách, cùng ổ với <i>hospital</i>, <i>hostel</i>.</div>'
    '<div class="hd-warn">Đuôi <b>-ь</b> thường báo giống CÁI, nhưng <b>оте́ль</b> là giống '
    'ĐỰC — chia như <b>слова́рь</b>: <b>большо́й оте́ль</b>, <b>в оте́ле</b>.</div>'
    '<div class="hd-warn">Từ Nga thuần là <b>гости́ница</b> (từ <b>гость</b> = khách) và đó '
    'mới là từ trung tính hay gặp; <b>оте́ль</b> nghiêng về khách sạn kiểu Tây.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гости́ница</b> khách sạn (từ Nga) · <b>гость</b> khách · '
    '<b>но́мер</b> phòng khách sạn (cũng nghĩa "số")</div>'
)
V["отель"] = "khách sạn (dùng từ mượn quốc tế, không phải từ Nga thuần)"

# ─────────────────────────────────────────────────────────── столица
S["столица"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">стол-</span>'
    '<span class="hd-gloss">nghĩa CỔ là ngai vua (nay <b>стол</b> = cái bàn)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ца</span>'
    '<span class="hd-gloss">đuôi tạo danh từ giống CÁI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thành phố đặt ngai vua = thủ đô. Nghĩa "ngai" nay chỉ còn trong '
    '<b>престо́л</b> (ngai vàng). Anh <i>stool</i> (ghế đẩu) là họ hàng xa của <b>стол</b>.</div>'
    '<div class="hd-warn">"Thủ đô CỦA nước nào" đi cách 2: <b>столи́ца Росси́и</b>, '
    '<b>столи́ца Вьетна́ма</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>столи́чный</b> thuộc thủ đô · <b>престо́л</b> ngai vàng · '
    '<b>столо́вая</b> phòng ăn, căng-tin (cùng <b>стол</b> nhưng theo nghĩa "cái bàn")</div>'
)
