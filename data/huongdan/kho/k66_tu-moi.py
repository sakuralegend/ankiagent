# -*- coding: utf-8 -*-
"""k66 — tu-moi: bốn từ KHÔNG cùng họ, nhưng ba trong bốn đều là "sau/lát nữa"
(по́зже · попо́зже · че́рез, cộng thêm пото́м đã có sẵn trong kho).
Trục thật của lô: mỗi thẻ phải tự nói ra CÁI GÌ TÁCH NÓ khỏi ba từ kia —
по́зже so với một mốc · попо́зже dịu đi một chút · че́рез kéo theo danh từ cách 4.
"""

# 🔴 KHÔNG dựng biến khối dùng chung (HE/LUAT/THE…) rồi cộng vào mọi thẻ.

S = {}
V = {}

# ------------------------------------------------------------------ по́зже
S["позже"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по́зд-</span>'
    '<span class="hd-gloss">gốc MUỘN, TRỄ (<b>по́здний</b> muộn)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е</span>'
    '<span class="hd-gloss">đuôi SO SÁNH HƠN, làm д đổi thành ж</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cắt đuôi tính từ của <b>по́здний</b> còn gốc позд-, '
    'gắn đuôi so sánh -е rồi đổi д → ж ⇒ <b>по́зже</b> "muộn hơn". '
    'Cùng phép đổi д → ж: <b>молодо́й → моло́же</b> trẻ hơn.</div>'
    '<div class="hd-warn">⚠️ Thứ đem ra so đứng ở CÁCH 2: <b>по́зже меня́</b> '
    'muộn hơn tôi — y như <b>бо́льше</b>. Muốn giữ cách 1 thì thêm чем: '
    '<b>по́зже, чем я</b>.</div>'
    '<div class="hd-warn">⚠️ <b>по́зже</b> luôn ngầm so với MỘT MỐC; '
    '<b>пото́м</b> chỉ là việc kế tiếp trong chuỗi, không so với gì.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>по́здний</b> muộn · <b>по́здно</b> muộn (trạng từ) · '
    '<b>опозда́ть</b> đến muộn · <b>опозда́ние</b> sự đến muộn</div>'
)

# ---------------------------------------------------------------- попо́зже
S["попозже"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố LÀM DỊU: "hơn một chút"</span></div>'
    '<div class="hd-row"><span class="hd-piece">по́зже</span>'
    '<span class="hd-gloss">muộn hơn</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đặt по- trước một từ so sánh hơn là hạ giọng nó xuống: '
    '<b>по́зже</b> muộn hơn → <b>попо́зже</b> muộn hơn MỘT CHÚT. '
    'Đây là по- làm dịu, không phải по- của thể hoàn thành ở động từ.</div>'
    '<div class="hd-warn">⚠️ Chỗ dùng thật là lời ĐỀ NGHỊ dời lại: '
    '<b>Позвони́ попо́зже</b> gọi lại lát nữa. Không đem gì ra so, nên không '
    'kéo theo cách 2 như <b>по́зже</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">Cùng khuôn по- + so sánh hơn: <b>побо́льше</b> nhiều hơn '
    'chút · <b>поме́ньше</b> ít hơn chút · <b>пора́ньше</b> sớm hơn chút · '
    '<b>подо́льше</b> lâu hơn chút</div>'
)

# ----------------------------------------------------------------- учёба
S["учёба"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">уч-</span>'
    '<span class="hd-gloss">gốc HỌC / DẠY (<b>учи́ть</b>, <b>учи́ться</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ёб-а</span>'
    '<span class="hd-gloss">hậu tố -б- chỉ VIỆC LÀM; -а ⇒ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc уч- + hậu tố -б- của việc làm ⇒ "việc học". Cùng khuôn: '
    '<b>ходьба́</b> việc đi bộ, <b>борьба́</b> cuộc đấu tranh, <b>дру́жба</b> tình bạn. '
    'Chữ ё tự nó đã mang trọng âm, nên trọng âm đứng yên suốt bảng chia.</div>'
    '<div class="hd-warn">⚠️ <b>учёба</b> là việc học của NGƯỜI ĐANG ĐI HỌC (quá trình '
    'ngồi học) — không phải <b>образова́ние</b> = nền giáo dục, trình độ học vấn.</div>'
    '<div class="hd-warn">⚠️ Bảng chia in <b>учёбою</b> ở cách 5: đó là dạng CŨ/thơ ca, '
    'nay viết <b>учёбой</b>. Các ô số nhiều cũng gần như không dùng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>учи́ться</b> đi học · <b>учи́тель</b> thầy giáo · '
    '<b>учени́к</b> học sinh · <b>учёный</b> nhà khoa học · <b>нау́ка</b> khoa học</div>'
)

# ----------------------------------------------------------------- че́рез
S["через"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: giới từ nguyên khối, gốc Slav cổ — '
    'dạng cổ <b>чрез</b> nay chỉ còn trong thơ và trong vài từ ghép.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỉ một hình ảnh: VƯỢT QUA MỘT KHOẢNG. Khoảng không gian — '
    '<b>че́рез доро́гу</b> băng qua đường. Khoảng thời gian — <b>че́рез час</b> '
    'một tiếng NỮA, đếm từ bây giờ.</div>'
    '<div class="hd-warn">⚠️ <b>че́рез</b> bắt buộc có danh từ theo sau, và danh từ đó '
    'ở CÁCH 4: <b>неде́ля</b> → <b>че́рез неде́лю</b> một tuần nữa.</div>'
    '<div class="hd-warn">⚠️ <b>че́рез</b> đo một khoảng tính từ bây giờ; còn '
    '<b>по́зже</b> và <b>пото́м</b> đứng một mình, không danh từ, không đo khoảng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>чересчу́р</b> quá mức (← че́рез + чур "vạch ranh") · '
    '<b>чрезме́рный</b> quá đáng · <b>чрезвыча́йный</b> khác thường, khẩn cấp</div>'
)

# ================================================== field Vietnamese (đề bài)
# Ba từ dưới đây đều rơi vào ô "sau / lát nữa", lại có PoS = oth nên badge không
# tách được gì. Mỗi dòng phải tự loại ba từ kia ra — kể cả пото́м nằm ngoài lô.
# 🔴 Không viết chữ Nga vào đây: đề bài mà có chữ Nga là lộ đáp án.
V["позже"] = ("trạng từ so sánh hơn: muộn hơn, trễ hơn (có một mốc đem ra so, "
              "mốc đó ở cách 2 — không phải «sau đó», "
              "không phải «muộn hơn một chút»)")
V["попозже"] = ("trạng từ: muộn hơn MỘT CHÚT, để lát nữa hẵng (dạng đã làm dịu bằng "
                "tiền tố — không phải «muộn hơn» trơn, không phải "
                "«sau đó»)")
V["через"] = ("giới từ đi với cách 4, luôn đứng TRƯỚC một danh từ: băng qua, xuyên qua; "
              "hoặc «sau … nữa» tính từ bây giờ (một tiếng nữa) — "
              "không phải trạng từ đứng một mình")
V["учёба"] = ("việc học, chuyện đi học (quá trình học của học sinh, sinh viên — "
              "không phải nền giáo dục, không phải trình độ học vấn)")
