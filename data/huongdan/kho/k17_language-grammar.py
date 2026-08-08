# -*- coding: utf-8 -*-
"""k17 — language::grammar: bộ từ HỎI (к-/ч-) và bộ từ TRỎ (т-/э-) đi thành cặp,
hỏi thế nào thì đáp đúng thế ấy; kèm ba từ chỉ chỗ там · тут · здесь."""

# 🔴 KHÔNG dựng biến khối dùng chung rồi cộng vào mọi thẻ (README §3).
# Cặp hỏi↔đáp ч-/т- chỉ được trải ở đúng hai thẻ nó là trọng tâm (почему · потому);
# bộ где/куда/откуда chỉ trải ở thẻ там. Thẻ khác không nhắc lại.

S = {}

# ------------------------------------------------------------------ кто
S["кто"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">к-</span>'
    '<span class="hd-gloss">gốc HỎI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-то</span>'
    '<span class="hd-gloss">tiểu từ trỏ, nay dính liền, không tách ra được nữa</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gần như cả họ từ hỏi tiếng Nga mở đầu bằng к- hoặc ч-: '
    '<b>кто</b> ai · <b>что</b> cái gì · <b>как</b> thế nào · <b>како́й</b> loại nào — '
    'đúng kiểu <i>who / what / how</i> đều wh- trong tiếng Anh. Chia việc rất gọn: '
    '<b>кто</b> hỏi NGƯỜI, <b>что</b> hỏi VẬT.</div>'
    '<div class="hd-warn">⚠️ Sau <b>кто</b>, động từ luôn ở số ít giống đực — kể cả khi '
    'đang hỏi về phụ nữ hay về cả một đám đông: <b>Кто пришёл?</b> = Ai đã đến?</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>никто́</b> không ai · <b>кто-то</b> ai đó · '
    '<b>кто-нибудь</b> ai đó bất kỳ · <b>кото́рый</b> người/cái mà</div>'
)

# ------------------------------------------------------------------ что
S["что"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ч-</span>'
    '<span class="hd-gloss">gốc HỎI, chính là к- của <b>кто</b> đã mềm đi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-то</span>'
    '<span class="hd-gloss">tiểu từ trỏ, đã dính liền</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>кто</b> và <b>что</b> là một cặp sinh đôi: cùng khuôn, chỉ khác '
    'chữ đầu. <b>кто</b> hỏi người, <b>что</b> hỏi vật — <b>Кто э́то?</b> (Ai đấy?) so với '
    '<b>Что э́то?</b> (Cái gì đấy?). Làm chủ ngữ thì <b>что</b> kéo động từ về số ít giống '
    'trung: <b>Что случи́лось?</b> = Có chuyện gì vậy?</div>'
    '<div class="hd-warn">⚠️ <b>что</b> còn một vai thứ hai, không hỏi han gì cả: nó là liên '
    'từ "rằng" nối hai vế câu — <b>Он сказа́л, что придёт</b> = Anh ấy nói rằng sẽ đến. '
    'Vế nối kiểu này bắt buộc có dấu phẩy đứng trước.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>почему́</b> tại sao · <b>потому́</b> vì thế · '
    '<b>ничего́</b> không gì cả · <b>что́бы</b> để mà</div>'
)

# ------------------------------------------------------------------ какой
S["какой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">как-</span>'
    '<span class="hd-gloss">chính là <b>как</b> = như thế nào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́й</span>'
    '<span class="hd-gloss">đuôi tính từ ⇒ phải hợp giống, số, cách</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>како́й</b> là <b>как</b> mặc áo tính từ, nên nó đứng trước danh từ '
    'và đổi đuôi theo danh từ đó: <b>како́й дом</b> · <b>кака́я кни́га</b> · '
    '<b>како́е сло́во</b>. Nó hỏi LOẠI, hỏi TÍNH CHẤT ("nhà thế nào?"), khác <b>что</b> '
    'hỏi thẳng bản thân đồ vật.</div>'
    '<div class="hd-warn">⚠️ Cũng chính nó làm câu cảm thán, lúc đó không có ý hỏi: '
    '<b>Како́й краси́вый го́род!</b> = Thành phố đẹp quá!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>как</b> như thế nào · <b>тако́й</b> như thế, thế đấy · '
    '<b>ника́к</b> không tài nào</div>'
)

# ------------------------------------------------------------------ почему
S["почему"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">theo, do</span></div>'
    '<div class="hd-row"><span class="hd-piece">чему́</span>'
    '<span class="hd-gloss">cách 3 của <b>что</b> (cái gì)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen "do CÁI GÌ" — nên <b>почему́</b> hỏi NGUYÊN NHÂN: chuyện đã '
    'xảy ra rồi, nay tìm lời giải thích. Đừng lẫn với <b>заче́м</b> (за + чем = "để làm cái '
    'gì") hỏi MỤC ĐÍCH: <b>Почему́ ты пришёл?</b> = vì lí do gì · <b>Заче́м ты пришёл?</b> '
    '= đến để làm gì.</div>'
    '<div class="hd-warn">⚠️ Học trọn cặp hỏi–đáp thì khỏi phải nhớ rời: '
    '<b>Почему́?</b> → <b>Потому́ что…</b> (bởi vì…) · <b>Заче́м?</b> → <b>Что́бы…</b> (để mà…)'
    '</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>потому́</b> vì thế · <b>поэ́тому</b> vì vậy · '
    '<b>отчего́</b> do đâu · <b>что</b> cái gì</div>'
)

# ------------------------------------------------------------------ потому
S["потому"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">theo, do</span></div>'
    '<div class="hd-row"><span class="hd-piece">тому́</span>'
    '<span class="hd-gloss">cách 3 của <b>то</b> (cái đó)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>потому́</b> chính là <b>почему́</b> thay đầu HỎI ч- bằng đầu TRỎ '
    'т-: hỏi "do cái gì" thì đáp "do cái đó". Cả tiếng Nga chạy theo cặp này — '
    '<b>что</b>↔<b>то</b>, <b>како́й</b>↔<b>тако́й</b>, <b>как</b>↔<b>так</b>.</div>'
    '<div class="hd-warn">⚠️ Đứng một mình, <b>потому́</b> nghĩa là "vì thế", trỏ ngược về lí '
    'do vừa nói. Phải có <b>что</b> đi kèm mới thành "bởi vì": '
    '<b>Он не пришёл, потому́ что заболе́л</b> = Anh ấy không đến, bởi vì ốm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>почему́</b> tại sao · <b>поэ́тому</b> vì vậy · '
    '<b>тот</b> cái kia · <b>тогда́</b> lúc đó</div>'
)

# ------------------------------------------------------------------ как
S["как"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: <b>как</b> là từ gốc trơn, chẻ ra thì không mảnh nào '
    'còn mang nghĩa riêng. Ngược lại, chính nó là mảnh gốc mà <b>како́й</b> mượn.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hai việc, một từ. Hỏi CÁCH THỨC: <b>Как ты рабо́таешь?</b> = Anh làm '
    'việc thế nào? Và SO SÁNH "như, giống như": <b>Он рабо́тает как маши́на</b> = Anh ấy làm '
    'việc như cái máy. Từ đáp lại của nó là <b>так</b> (như vậy đấy).</div>'
    '<div class="hd-warn">⚠️ Ba cụm gặp hằng ngày: <b>как то́лько</b> = ngay khi · '
    '<b>так как</b> = bởi vì · <b>как мо́жно</b> + so sánh hơn = "…nhất có thể".</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>так</b> như vậy · <b>тако́й</b> như thế · <b>како́й</b> loại nào · '
    '<b>ника́к</b> không tài nào</div>'
)

# ------------------------------------------------------------------ это
S["это"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">э-</span>'
    '<span class="hd-gloss">trỏ "đây, cái này"</span></div>'
    '<div class="hd-row"><span class="hd-piece">-то</span>'
    '<span class="hd-gloss">đuôi giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vốn là dạng giống trung của <b>э́тот</b>, nhưng đã tách ra sống riêng '
    'thành từ mở đầu câu giới thiệu — và ở vai đó nó KHÔNG đổi hình dù nói về cái gì: '
    '<b>Э́то дом</b> · <b>Э́то кни́га</b> · <b>Э́то моя́ сестра́</b>, đều là "Đây là…". Nó đứng '
    'thay chỗ động từ "là" mà tiếng Nga không dùng ở thì hiện tại.</div>'
    '<div class="hd-warn">⚠️ Đừng lẫn với <b>э́тот</b>: <b>Э́то кни́га</b> = "Đây LÀ quyển '
    'sách" (giới thiệu) · <b>э́та кни́га</b> = "quyển sách NÀY" (chỉ định, phải hợp giống).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>э́тот</b> …này · <b>поэ́тому</b> vì vậy (по + э́тому = "theo cái '
    'này") · <b>при э́том</b> đồng thời với đó</div>'
)

# ------------------------------------------------------------------ этот
S["этот"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">э-</span>'
    '<span class="hd-gloss">trỏ "ở đây", chỗ người nói</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тот</span>'
    '<span class="hd-gloss">chính là <b>тот</b> = cái kia, cái đằng ấy</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ghép lại đúng nghĩa "cái kia nhưng ở ĐÂY này", nên <b>э́тот</b> (gần) '
    'đối lại <b>тот</b> (xa). Là từ chỉ định đứng trước danh từ nên phải hợp giống và số: '
    '<b>э́тот дом</b> · <b>э́та кни́га</b> · <b>э́то письмо́</b> · <b>э́ти лю́ди</b>.</div>'
    '<div class="hd-warn">⚠️ Dạng giống trung <b>э́то</b> trùng mặt chữ với từ <b>э́то</b> '
    '"đây là". <b>Э́то письмо́</b> vì thế đọc được hai kiểu — "Đây là bức thư" hoặc "bức thư '
    'này" — phải nhìn cả câu mới biết.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тот</b> cái kia · <b>э́то</b> đây là · <b>поэ́тому</b> vì vậy</div>'
)

# ------------------------------------------------------------------ там
S["там"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được thành mảnh có nghĩa riêng. Chỉ nhận ra được đầu т- '
    'của cả họ từ TRỎ: <b>то</b>, <b>тот</b>, <b>тогда́</b>, <b>там</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiếng Việt gộp hết vào chữ "đâu/đó", tiếng Nga tách làm ba và bắt '
    'chọn đúng: ở đâu <b>где</b> → ở đó <b>там</b> · đi đâu <b>куда́</b> → tới đó '
    '<b>туда́</b> · từ đâu <b>отку́да</b> → từ đó <b>отту́да</b>.</div>'
    '<div class="hd-warn">⚠️ Chọn nhầm là sai ngữ pháp chứ không chỉ kém hay: '
    '<b>Я живу́ там</b> (tôi sống Ở đó) nhưng <b>Я иду́ туда́</b> (tôi đi TỚI đó) — động từ '
    'chuyển động luôn kéo <b>туда́</b>, không bao giờ <b>там</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>туда́</b> tới đó · <b>отту́да</b> từ đó · <b>тот</b> cái kia · '
    '<b>тогда́</b> lúc đó</div>'
)

# ------------------------------------------------------------------ тут
# Họ hàng bỏ hẳn: hư từ gốc trơn, tiếng Nga không sinh ra từ phái sinh nào chắc chắn
# cùng gốc với nó (сюда́/отсю́да là gốc сь- của здесь, không phải gốc тут).
S["тут"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: hư từ gốc trơn, một mảnh duy nhất.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>тут</b> và <b>здесь</b> cùng nghĩa "ở đây", khác nhau ở giọng: '
    '<b>тут</b> là lời nói chuyện hằng ngày, <b>здесь</b> trung tính và hay gặp trong văn '
    'viết. Còn "lại ĐÂY" thì cả hai đều chịu, phải đổi sang <b>сюда́</b>: '
    '<b>Иди́ сюда́!</b> = Lại đây!</div>'
    '<div class="hd-warn">⚠️ <b>тут</b> có thêm một nghĩa THỜI GIAN mà <b>здесь</b> không có: '
    '"ngay lúc đó" — <b>Тут он по́нял</b> = Ngay lúc đó anh ta hiểu ra. Cụm <b>тут же</b> = '
    'ngay tức khắc.</div>'
)

# ------------------------------------------------------------------ здесь
S["здесь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сь-</span>'
    '<span class="hd-gloss">trỏ "này" — nay viết thành з vì đứng trước д</span></div>'
    '<div class="hd-row"><span class="hd-piece">-де-</span>'
    '<span class="hd-gloss">mảnh chỉ NƠI CHỐN, cũng nằm trong <b>где</b> = ở đâu</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сь</span>'
    '<span class="hd-gloss">lặp lại phần trỏ "này" một lần nữa</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ghép lại là "chốn này" — nên <b>здесь</b> trả lời cho <b>где?</b> '
    'chứ không trả lời <b>куда́?</b>. Đây là từ trung tính, dùng được cả lúc nói lẫn lúc '
    'viết; <b>тут</b> cùng nghĩa nhưng thân mật hơn.</div>'
    '<div class="hd-warn">⚠️ Mức tin: chỗ chẻ trên là TỪ NGUYÊN (nguồn gốc lịch sử), không '
    'phải luật suy ra được. Dùng để nhớ mặt chữ thôi, đừng đem chẻ các từ khác theo.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>зде́шний</b> ở đây, người bản xứ chỗ này · <b>сюда́</b> tới đây · '
    '<b>отсю́да</b> từ đây</div>'
)

# ------------------------------------------------------------------ вот
# Họ hàng bỏ hẳn: tiểu từ chỉ trỏ, không có từ phái sinh cùng gốc chắc chắn.
S["вот"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: tiểu từ chỉ trỏ, một mảnh duy nhất.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>вот</b> đi kèm động tác — chỉ tay vào, hoặc chìa ra: '
    '<b>Вот кни́га</b> = "Sách đây này". Khác hẳn <b>э́то</b> chỉ định danh: '
    '<b>Э́то кни́га</b> = "Đây là quyển sách". Vật ở xa thì đổi sang <b>вон</b>: '
    '<b>Вон он идёт</b> = Anh ta đang đi đằng kia kìa.</div>'
    '<div class="hd-warn">⚠️ Ba cụm dùng suốt ngày: <b>вот так</b> = đúng kiểu đó · '
    '<b>вот и всё</b> = xong, thế là hết · <b>вот-вот</b> = sắp sửa, chỉ chực.</div>'
)

# ------------------------------------------------------------------ вон
# Họ hàng bỏ hẳn: tiểu từ chỉ trỏ, không có từ phái sinh cùng gốc chắc chắn.
S["вон"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: tiểu từ chỉ trỏ, một mảnh duy nhất.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>вон</b> là <b>вот</b> phiên bản Ở XA: cái gì trong tầm tay thì '
    '<b>вот</b>, cái gì phải chỉ tay ra tít đằng kia thì <b>вон</b>. '
    '<b>Вон там мой дом</b> = Nhà tôi ở tít đằng kia.</div>'
    '<div class="hd-warn">⚠️ Cùng mặt chữ nhưng là một từ khác hẳn, gốc khác hẳn (họ với '
    '<b>вне</b> = bên ngoài): <b>вон</b> = "ra ngoài, cút" — <b>Вон отсю́да!</b> = Cút khỏi '
    'đây! · <b>вы́гнать вон</b> = tống cổ ra.</div>'
)

# ------------------------------------------------------------------ ничего
S["ничего"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ни-</span>'
    '<span class="hd-gloss">phủ định: không một… nào</span></div>'
    '<div class="hd-row"><span class="hd-piece">чего́</span>'
    '<span class="hd-gloss">cách 2 của <b>что</b> (cái gì)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bản thân từ đã ở sẵn cách 2, nên nó vào thẳng chỗ tân ngữ sau động từ '
    'phủ định: <b>Я ничего́ не зна́ю</b> = Tôi chẳng biết gì cả. Và tiếng Nga BẮT BUỘC phủ '
    'định hai lần — đã có <b>ни-</b> thì vẫn phải có <b>не</b> trước động từ, bỏ đi là sai.'
    '</div>'
    '<div class="hd-warn">⚠️ Trong lời nói hằng ngày nó lại là câu trả lời tích cực: '
    '<b>Как дела́? — Ничего́.</b> = "Sao rồi? — Cũng ổn." Và <b>Ничего́!</b> = "Không sao '
    'đâu!" khi ai đó xin lỗi mình.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ничто́</b> không cái gì (làm chủ ngữ) · <b>никто́</b> không ai · '
    '<b>никогда́</b> không bao giờ · <b>нигде́</b> không ở đâu</div>'
)


# ======================================================================
# V — sửa field `Vietnamese` (README §2c). Đây là ĐỀ BÀI của deck 1-go.
#
# Cả lô này là chỗ đề bài dễ có nhiều đáp án đúng nhất: nghi vấn ↔ chỉ định
# đâm nhau (что/какой/как, это/этот, там/тут/здесь, вот/вон).
#
# 🔴 10/14 từ có PoS = oth -> badge chỉ in "oth", vô dụng, nên PHẢI ghi từ loại.
#    кто · что · какой · этот là `pron`, badge lo rồi -> không ghi.
V = {}

V['кто'] = 'ai'
V['что'] = 'gì, cái gì, rằng'
V['какой'] = 'nào, loại nào, thế nào'
V['почему'] = 'tại sao, vì sao'
V['потому'] = 'vì thế, chính vì vậy'
V['как'] = 'như thế nào, bằng cách nào, như, giống như'
V['это'] = 'đây là, đó là, cái này'
V['этот'] = 'này, cái này'
V['там'] = 'ở đó, đằng đó'
V['тут'] = 'ngay đây, ngay lúc ấy'
V['здесь'] = 'ở đây, tại đây, chỗ này'
V['вот'] = 'đây này, đây rồi, đó'
V['вон'] = 'kia kìa, đằng kia, ra ngoài'
V['ничего'] = 'không gì cả, chẳng có gì, không sao'
