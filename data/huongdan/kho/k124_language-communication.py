# -*- coding: utf-8 -*-
"""k124 — language::communication: lô hỗn hợp — sáu cặp thể động từ «nói năng» + hai từ mượn
-ия + vài trạng từ thời gian, soạn từng thẻ độc lập.

Chỗ cần nhất quán trong lô:
(1) biến âm д → жд ở thể CHT (убеди́ть/убежда́ть, обсуди́ть/обсужда́ть) — cùng khuôn với
    победи́ть/побежда́ть đã soạn; д → ж ở dạng «tôi» (обсужу́).
(2) gốc -лаг-/-лож- «đặt» (предлага́ть/предложи́ть) — cùng cách chẻ với предложе́ние (k112).
(3) gốc -глас- «tiếng nói» (согласи́ться/соглаша́ться) — cùng cách chẻ với согла́сный (k88).
(4) когда́-то: phép so -то ↔ -нибудь một câu về CHÍNH từ đó; khuôn đầy đủ ở thẻ кто́-то.
Họ hàng: không thẻ nào cố ý vắng.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "теория": "lý thuyết, thuyết",                # bỏ «giả thuyết» — đó là гипо́теза, gloss chỉ có «theory»
    "знак": "dấu hiệu, biển báo, ký hiệu",        # «ký tự» trùng буква, gloss là sign/symbol/mark
    "потребовать": "đòi, đòi hỏi, yêu cầu",       # «yêu cầu» lấy lại 19/11: user duyệt bỏ nó khỏi попроси́ть (k87)
    "требовать": "đòi, đòi hỏi, yêu cầu",         # «yêu cầu» lấy lại 19/11: user duyệt bỏ nó khỏi проси́ть (k85)
    "предлагать": "đề nghị, đề xuất",             # RÚT «mời» — trùng звать, приглаша́ть
    "предложить": "đề nghị, đề xuất",
    "убедить": "thuyết phục",                     # bỏ «được» — nhãn thể trá hình, badge đã có
    "убеждать": "thuyết phục",
    "обсудить": "thảo luận, bàn bạc",             # bỏ «bàn xong» — nhãn thể trá hình
    "обсуждать": "thảo luận, bàn bạc",
    "крикнуть": "hét lên, gọi to",
    "кричать": "hét, la hét, gào",
    "согласиться": "đồng ý",
    "соглашаться": "đồng ý",
    "бывший": "cựu, trước đây, nguyên",           # RÚT «cũ» — trùng ста́рый (k42, xong)
}

# ------------------------------------------------------------------ теория
S["теория"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">тео́р-</span>'
    '<span class="hd-gloss">= <i>theor-</i> tiếng Anh (Hy Lạp «ngắm, xem xét»)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ия</span>'
    '<span class="hd-gloss">= đuôi <i>-y</i> tiếng Anh, danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ mượn: <i>theory</i> đổi <i>-y</i> → <b>-ия</b>, như <b>исто́рия</b> '
    '<i>history</i>. Trọng âm KHÔNG theo tiếng Anh: <i>THEory</i> nhưng <b>тео́рия</b>. '
    '«Trên lý thuyết» = <b>в тео́рии</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>теорети́ческий</b> thuộc lý thuyết · <b>теоре́тик</b> nhà lý thuyết</div>'
)

# ------------------------------------------------------------- лаборатория
S["лаборатория"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">лабор-</span>'
    '<span class="hd-gloss">= <i>labor</i> LAO ĐỘNG (Latin)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-атор-ия</span>'
    '<span class="hd-gloss">= <i>-atory</i>: NƠI làm việc đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chép thẳng <i>laboratory</i>, đổi <i>-y</i> → <b>-ия</b> như <b>тео́рия</b>. '
    'Đọc đủ sáu âm tiết, nhấn vào «то»: <b>лаборато́рия</b>.</div>'
    '<div class="hd-warn"><b>лаборато́рная рабо́та</b> = bài thực hành thí nghiệm ở trường.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лабора́нт</b> nhân viên phòng thí nghiệm · '
    '<b>лаборато́рный</b> thuộc phòng thí nghiệm</div>'
)

# ---------------------------------------------------------------- название
S["название"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">tiền tố, không tách ra nghĩa riêng (như ở <b>назва́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-зв-</span>'
    '<span class="hd-gloss">gốc GỌI — chính là <b>звать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ание</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>назва́ть</b> đặt tên: «cái mà vật được gọi ra» ⇒ '
    'tên gọi.</div>'
    '<div class="hd-warn"><b>назва́ние</b> là tên của VẬT (sách, phim, phố, công ty); tên NGƯỜI '
    'là <b>и́мя</b>: <b>Как называ́ется фильм?</b> · <b>Как тебя́ зову́т?</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>назва́ть</b> đặt tên · <b>называ́ть</b> gọi là · '
    '<b>называ́ться</b> được gọi là · <b>звать</b> gọi</div>'
)

# -------------------------------------------------------------------- знак
S["знак"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">зна-</span>'
    '<span class="hd-gloss">BIẾT — gốc của <b>знать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-к</span>'
    '<span class="hd-gloss">→ danh từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cái giúp nhận BIẾT» ⇒ dấu hiệu, ký hiệu, biển báo '
    '(<b>доро́жный знак</b> biển báo giao thông). Thêm đuôi thì к → ч: <b>зна́чить</b> '
    'có nghĩa là.</div>'
    '<div class="hd-warn">Tên hai chữ cái: <b>мя́гкий знак</b> = <b>ь</b> · <b>твёрдый знак</b> '
    '= <b>ъ</b>. Dấu câu = <b>знак препина́ния</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>знать</b> biết · <b>зна́чить</b> có nghĩa là · <b>значе́ние</b> ý nghĩa · '
    '<b>знако́мый</b> quen · <b>зна́ние</b> kiến thức</div>'
)

# --------------------------------------------------------------- требовать
S["требовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">треб-</span>'
    '<span class="hd-gloss">gốc CẦN (như trong <b>потре́бность</b> nhu cầu)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-ть</span>'
    '<span class="hd-gloss">lớp chia <b>-овать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bắt điều mình CẦN phải xảy ra ⇒ đòi, đòi hỏi. Lớp <b>-овать</b> bỏ '
    '<b>-ова-</b> lấy <b>-у-</b>: <b>я тре́бую, ты тре́буешь</b>. Cặp thể: <b>потре́бовать</b>. '
    'Đòi CÁI GÌ thường ở cách 2: <b>тре́бовать внима́ния</b>; đòi TỪ AI: <b>от</b> + cách 2.</div>'
    '<div class="hd-warn"><b>проси́ть</b> = xin, nhờ (người kia được quyền từ chối) · '
    '<b>тре́бовать</b> = đòi (coi như mình có quyền).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тре́бование</b> yêu cầu, đòi hỏi · <b>потре́бность</b> nhu cầu · '
    '<b>употребля́ть</b> sử dụng</div>'
)

# ------------------------------------------------------------- потребовать
S["потребовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố tạo thể, không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тре́бовать</span>'
    '<span class="hd-gloss">ĐÒI — chính là <b>тре́бовать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thể HOÀN THÀNH của <b>тре́бовать</b>: đưa ra một lời đòi cụ thể. Chia '
    'y hệt: <b>потре́бую, потре́буешь</b>; cũng đòi cách 2: <b>потре́бовать объясне́ний</b>.</div>'
    '<div class="hd-warn"><b>Э́то потре́бует вре́мени</b> = việc này sẽ cần thời gian — chủ ngữ '
    'là VIỆC, nghĩa là «cần».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тре́бовать</b> đòi (CHT) · <b>тре́бование</b> yêu cầu · '
    '<b>потре́бность</b> nhu cầu</div>'
)

# -------------------------------------------------------------- предлагать
S["предлагать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пред-</span>'
    '<span class="hd-gloss">TRƯỚC, ra phía trước</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лаг-</span>'
    '<span class="hd-gloss">ĐẶT — mặt kia của <b>-лож-</b> trong <b>положи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đặt ra trước mặt» ⇒ đề nghị — ghép y hệt <i>pro-pose</i>, như '
    '<b>предложе́ние</b>. Thể CHT mang <b>-лаг-</b>, thể HT <b>предложи́ть</b> mang <b>-лож-</b>. '
    'Chia đều: <b>предлага́ю, предлага́ешь</b>.</div>'
    '<div class="hd-warn">Đề nghị AI (cách 3) CÁI GÌ (cách 4), hoặc + nguyên thể: <b>Я предлага́ю '
    'тебе́ чай</b> · <b>Предлага́ю пойти́ в кино́</b> = mình đi xem phim đi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>предложи́ть</b> đề nghị (HT) · <b>предложе́ние</b> lời đề nghị, câu · '
    '<b>предло́г</b> giới từ («đặt trước») · <b>положи́ть</b> đặt</div>'
)

# -------------------------------------------------------------- предложить
S["предложить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пред-</span>'
    '<span class="hd-gloss">TRƯỚC, ra phía trước</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лож-</span>'
    '<span class="hd-gloss">ĐẶT — gốc của <b>положи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-ть</span>'
    '<span class="hd-gloss">đuôi lớp chia 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thể HOÀN THÀNH của <b>предлага́ть</b>: đưa ra một đề nghị cụ thể. '
    'Trọng âm dịch y như <b>положи́ть</b>: <b>я предложу́</b> nhưng <b>ты предло́жишь</b>, '
    '<b>они́ предло́жат</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>предлага́ть</b> đề nghị (CHT) · <b>предложе́ние</b> lời đề nghị, câu · '
    '<b>положи́ть</b> đặt</div>'
)

# ----------------------------------------------------------------- убедить
S["убедить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố, nghĩa riêng đã mờ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бед-</span>'
    '<span class="hd-gloss">gốc cổ ÉP, KHUẤT PHỤC — như <b>побе́да</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-ть</span>'
    '<span class="hd-gloss">đuôi lớp chia 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Khuất phục được LÝ LẼ của người kia ⇒ thuyết phục được. Thuyết phục AI '
    '(cách 4) VỀ điều gì: <b>в</b> + cách 6 — <b>убеди́ть его́ в э́том</b>. '
    'Cặp thể: <b>убежда́ть</b>.</div>'
    '<div class="hd-warn">⚠️ Giống <b>победи́ть</b>: dạng «tôi» bị tránh — từ điển có in '
    '<b>убежу́</b> nhưng gần như không ai nói; dùng <b>Я смогу́ убеди́ть</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: <b>-бед-</b> chung gốc với <b>побе́да</b> là chuyện TỪ '
    'NGUYÊN, không phải luật suy ra được — chỉ dùng để nhớ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>убежда́ть</b> thuyết phục (CHT) · <b>убежде́ние</b> niềm tin, sự '
    'thuyết phục · <b>убеди́ться</b> tin chắc · <b>побе́да</b> chiến thắng</div>'
)

# ---------------------------------------------------------------- убеждать
S["убеждать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố, nghĩa riêng đã mờ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бежд-</span>'
    '<span class="hd-gloss">= <b>-бед-</b> biến âm д → жд</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thể CHT của <b>убеди́ть</b>: đang cố thuyết phục, chưa chắc đã được. '
    'д → жд y như <b>побежда́ть</b>, <b>обсужда́ть</b>. Chia đều: <b>убежда́ю, убежда́ешь</b>; '
    'cùng cách đòi <b>в</b> + cách 6.</div>'
    '<div class="hd-warn">Hai thể tách rất rõ: <b>Он до́лго убежда́л меня́, но не убеди́л</b> — '
    'anh ấy thuyết phục tôi mãi mà không được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>убеди́ть</b> thuyết phục (HT) · <b>убежде́ние</b> niềm tin · '
    '<b>убеди́тельный</b> có sức thuyết phục</div>'
)

# ---------------------------------------------------------------- обсудить
S["обсудить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">QUANH, khắp mọi phía</span></div>'
    '<div class="hd-row"><span class="hd-piece">-суд-</span>'
    '<span class="hd-gloss">XÉT — gốc của <b>суд</b> toà án, <b>суди́ть</b> xét xử</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-ть</span>'
    '<span class="hd-gloss">đuôi lớp chia 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Xét quanh mọi phía» một việc ⇒ thảo luận; thể HT: bàn cho ra kết quả. '
    'Dạng «tôi» д → ж, trọng âm lùi ở ngôi khác: <b>я обсужу́</b>, <b>ты обсу́дишь</b>.</div>'
    '<div class="hd-warn">Bàn CÁI GÌ: cách 4 thẳng, KHÔNG có <b>о</b> — <b>обсуди́ть план</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обсужда́ть</b> thảo luận (CHT) · <b>обсужде́ние</b> cuộc thảo luận · '
    '<b>суд</b> toà án · <b>суди́ть</b> xét xử</div>'
)

# --------------------------------------------------------------- обсуждать
S["обсуждать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">QUANH, khắp mọi phía</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сужд-</span>'
    '<span class="hd-gloss">= <b>-суд-</b> XÉT, biến âm д → жд</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thể CHT của <b>обсуди́ть</b>: đang bàn, hay bàn. д → жд giống '
    '<b>убежда́ть</b>, <b>побежда́ть</b>. Chia đều: <b>обсужда́ю, обсужда́ешь</b>.</div>'
    '<div class="hd-warn">Cách 4 thẳng, KHÔNG có <b>о</b>: <b>Мы обсужда́ем фильм</b>. Muốn dùng '
    '<b>о</b> thì đổi động từ: <b>говори́ть о фи́льме</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обсуди́ть</b> thảo luận (HT) · <b>обсужде́ние</b> cuộc thảo luận · '
    '<b>суд</b> toà án</div>'
)

# ---------------------------------------------------------------- крикнуть
S["крикнуть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">крик-</span>'
    '<span class="hd-gloss">TIẾNG HÉT — danh từ <b>крик</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ну-ть</span>'
    '<span class="hd-gloss">MỘT LẦN, bật ra một cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hậu tố <b>-ну-</b> biến việc kéo dài thành MỘT cái chớp nhoáng: '
    '<b>крича́ть</b> la hét → <b>кри́кнуть</b> hét lên một tiếng; cùng khuôn <b>стуча́ть</b> → '
    '<b>сту́кнуть</b> gõ một cái. Chia: <b>кри́кну, кри́кнешь</b>.</div>'
    '<div class="hd-warn"><b>кри́кнуть кому́</b> (cách 3) = gọi to cho ai · '
    '<b>кри́кнуть на кого́</b> (<b>на</b> + cách 4) = quát ai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>крик</b> tiếng hét · <b>крича́ть</b> la hét · '
    '<b>закрича́ть</b> bắt đầu hét lên</div>'
)

# ----------------------------------------------------------------- кричать
S["кричать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">крич-</span>'
    '<span class="hd-gloss">= <b>крик</b> TIẾNG HÉT, biến âm к → ч</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Phát ra tiếng hét» ⇒ la hét. Đuôi <b>-ать</b> nhưng chia lớp HAI như '
    '<b>слы́шать</b>: <b>кричу́, кричи́шь, крича́т</b>. Bản một lần: <b>кри́кнуть</b>.</div>'
    '<div class="hd-warn">Quát mắng AI: <b>на</b> + cách 4 — <b>Не кричи́ на меня́!</b> = Đừng '
    'quát tôi!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>крик</b> tiếng hét · <b>кри́кнуть</b> hét lên một tiếng · '
    '<b>закрича́ть</b> bắt đầu hét lên</div>'
)

# ------------------------------------------------------------- согласиться
S["согласиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">CÙNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-глас-</span>'
    '<span class="hd-gloss">TIẾNG NÓI — dạng cổ của <b>го́лос</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-ть-ся</span>'
    '<span class="hd-gloss">đuôi lớp chia 2 + phản thân</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">CÙNG một tiếng nói ⇒ đồng ý — động từ của <b>согла́сный</b>. Thể HT: '
    'gật đầu một lần là xong. Dạng «tôi» с → ш: <b>я соглашу́сь</b>, còn lại giữ с: '
    '<b>ты согласи́шься</b>.</div>'
    '<div class="hd-warn">Đồng ý VỚI ai: <b>с</b> + cách 5 · đồng ý NHẬN điều gì: <b>на</b> + '
    'cách 4 — <b>Он согласи́лся на рабо́ту</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>соглаша́ться</b> đồng ý (CHT) · <b>согла́сный</b> đồng ý (tính từ) · '
    '<b>согла́сие</b> sự đồng ý · <b>го́лос</b> giọng</div>'
)

# ------------------------------------------------------------- соглашаться
S["соглашаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">CÙNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-глаш-</span>'
    '<span class="hd-gloss">= <b>-глас-</b> TIẾNG NÓI, biến âm с → ш</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть-ся</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành + phản thân</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thể CHT của <b>согласи́ться</b>; с → ш y như dạng <b>соглашу́сь</b>. '
    'Chia đều: <b>соглаша́юсь, соглаша́ешься</b>. Cùng cách đòi: <b>с</b> + cách 5, '
    '<b>на</b> + cách 4.</div>'
    '<div class="hd-warn">Nói «tôi đồng ý» hằng ngày, người Nga dùng tính từ ngắn '
    '<b>Я согла́сен / согла́сна</b> nhiều hơn động từ này.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>согласи́ться</b> đồng ý (HT) · <b>согла́сный</b> đồng ý (tính từ) · '
    '<b>согла́сие</b> sự đồng ý</div>'
)

# ---------------------------------------------------------------- навсегда
S["навсегда"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">giới từ <b>на</b> «cho (bao lâu)», như <b>на неде́лю</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-все-гда</span>'
    '<span class="hd-gloss">= <b>всегда́</b> luôn luôn</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cho TẤT CẢ mọi lúc» ⇒ mãi mãi, vĩnh viễn: <b>всегда́</b> thêm <b>на-</b> '
    'đằng trước.</div>'
    '<div class="hd-warn"><b>всегда́</b> = luôn luôn, lần nào cũng vậy · <b>навсегда́</b> = từ '
    'nay về sau, không đổi nữa: <b>Он уе́хал навсегда́</b> — anh ấy đi hẳn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>всегда́</b> luôn luôn · <b>когда́</b> khi nào · <b>весь</b> toàn bộ</div>'
)

# ----------------------------------------------------------------- впервые
S["впервые"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">giới từ <b>в</b> dính liền: «vào»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-перв-ые</span>'
    '<span class="hd-gloss">THỨ NHẤT — chính là <b>пе́рвый</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Vào lần thứ nhất» ⇒ lần đầu tiên. Cùng nghĩa với cụm <b>в пе́рвый '
    'раз</b>: <b>Я впервы́е в Москве́</b> — tôi đến Moskva lần đầu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пе́рвый</b> thứ nhất · <b>сперва́</b> trước hết, ban đầu</div>'
)

# ------------------------------------------------------------------ бывший
S["бывший"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бы-</span>'
    '<span class="hd-gloss">LÀ, Ở — gốc của <b>быть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-вш-</span>'
    '<span class="hd-gloss">«ĐÃ (làm)» — hậu tố phân từ quá khứ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đã từng LÀ» ⇒ cựu, trước đây: <b>бы́вший президе́нт</b> cựu tổng thống, '
    '<b>бы́вший муж</b> chồng cũ. <b>-вш-</b> gắn được vào thân quá khứ của mọi động từ: '
    '<b>чита́вший</b> người đã đọc.</div>'
    '<div class="hd-warn">Đứng một mình như danh từ: <b>мой бы́вший / моя́ бы́вшая</b> = người yêu '
    'cũ. Rao vặt <b>б/у</b> = <b>бы́вший в употребле́нии</b>, đồ đã qua sử dụng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>быть</b> là, ở · <b>быва́ть</b> hay có, hay ở · '
    '<b>собы́тие</b> sự kiện</div>'
)

# ---------------------------------------------------------------- когда-то
S["когда-то"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">когда́</span>'
    '<span class="hd-gloss">KHI NÀO (từ hỏi)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-то</span>'
    '<span class="hd-gloss">«… nào đó» — có thật, chỉ không nói rõ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng khuôn với <b>кто́-то</b>: «vào lúc nào đó» — gần như luôn nói về '
    'QUÁ KHỨ: <b>Когда́-то здесь был лес</b> — ngày xưa ở đây từng là rừng.</div>'
    '<div class="hd-warn">Hỏi «đã BAO GIỜ … chưa?» thì dùng <b>-нибудь</b>: <b>Ты когда́-нибудь был '
    'в Москве́?</b> — <b>Да, я когда́-то жил там.</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>когда́</b> khi nào · <b>когда́-нибудь</b> bao giờ (bất kỳ) · '
    '<b>кто́-то</b> ai đó</div>'
)

# ------------------------------------------------------------- по-прежнему
S["по-прежнему"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-… -ему</span>'
    '<span class="hd-gloss">«theo KIỂU …»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пре́жн-</span>'
    '<span class="hd-gloss">TRƯỚC KIA — từ <b>пре́жний</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Khuôn <b>по-</b> + tính từ + <b>-ому/-ему</b>, luôn có gạch nối: '
    '<b>по-но́вому</b> theo cách mới, <b>по-сво́ему</b> theo cách riêng. Theo kiểu trước kia ⇒ '
    'vẫn như cũ: <b>Он по-пре́жнему живёт в Москве́</b> — anh ấy vẫn sống ở Moskva.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пре́жний</b> trước kia, cũ · <b>пре́жде</b> trước đây</div>'
)
