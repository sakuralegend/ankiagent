# -*- coding: utf-8 -*-
"""k03 — actions: 6 động từ mà chỗ khó nằm ở THÂN CHIA, không ở nghĩa.

быть · забыть · взять đều có thân hiện tại/tương lai không suy được từ nguyên thể
(есть·буд- · забу́д- · возьм-), курить · ответить lệch một ô trong bảng (trọng âm
dịch · т→ч), стоять thì bẫy nằm ở cặp trọng âm стои́т / сто́ит.

🔴 KHÔNG dựng biến khối dùng chung (HE/LUAT/THE…) rồi cộng vào mọi thẻ — README §3.
Bảng chia do `congcu.py bang` tự nối lúc `nap`, ở đây chỉ viết CÂU CHÚ Ý phía trên nó.
"""

S = {}
V = {}

# ------------------------------------------------------------------ курить
S["курить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кур-</span>'
    '<span class="hd-gloss">khói, bốc khói</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi động từ, lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>кур-</b> là “làm ra khói” (<b>ку́рево</b> = thứ để hút) '
    '— hút thuốc chính là làm ra khói.</div>'
    '<div class="hd-warn">Biển báo gặp khắp nơi: <b>Не кури́ть!</b> = Cấm hút thuốc. '
    'Tiếng Nga ra lệnh cấm bằng chính nguyên thể.</div>'
    '<div class="hd-warn">⚠️ <b>ку́рица</b> (con gà) chỉ trông giống, khác gốc hẳn '
    '— đừng nối hai từ này.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>куре́ние</b> việc hút thuốc · <b>кури́льщик</b> người hút thuốc '
    '· <b>закури́ть</b> châm thuốc, bắt đầu hút</div>'
    '<div class="hd-why">Cả bảng chỉ có một ngôi giữ trọng âm ở đuôi: <b>курю́</b> (tôi). '
    'Từ ngôi <i>ты</i> trở đi nó lùi hết về gốc — <b>ку́ришь</b>, <b>ку́рит</b>…</div>'
)

# ---------------------------------------------------------------- ответить
S["ответить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">trả lại, đáp lại</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вет-</span>'
    '<span class="hd-gloss">lời, lời nói</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ghép lại đúng nghĩa đen “nói trả lại”. Gốc <b>-вет-</b> = lời '
    'mở luôn hai từ đã biết: <b>приве́т</b> (lời gửi tới), <b>сове́т</b> (cùng bàn lời).</div>'
    '<div class="hd-warn">Cách nó đòi: trả lời CÂU HỎI thì <b>на</b> + cách 4 '
    '(<b>отве́тить на вопро́с</b>), còn trả lời NGƯỜI thì người đứng ở cách 3.</div>'
    '<div class="hd-warn">Bạn cùng cặp là <b>отвеча́ть</b> (đang trả lời, hay trả lời). '
    'Nhưng <b>отвеча́ть за</b> + cách 4 lại là “chịu trách nhiệm về”.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отве́т</b> câu trả lời · <b>отве́тственность</b> trách nhiệm '
    '· <b>приве́т</b> chào · <b>сове́т</b> lời khuyên</div>'
    '<div class="hd-why">Bảng lệch đúng một ô: ngôi “tôi” đổi т→ч — <b>отве́чу</b>; '
    'năm ngôi còn lại giữ т (<b>отве́тишь</b>, <b>отве́тит</b>…). '
    'Phép đổi này lặp ở mọi động từ đuôi -тить.</div>'
)

# -------------------------------------------------------------------- быть
S["быть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бы-</span>'
    '<span class="hd-gloss">gốc “tồn tại”, còn thấy ở quá khứ был</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một động từ mà ba thời đi ba thân khác nhau hẳn — đó là lý do '
    'nó trông lộn xộn: <b>бы-</b> quá khứ · есть hiện tại · <b>буд-</b> tương lai.</div>'
    '<div class="hd-warn">Hiện tại BỎ TRỐNG hẳn: <b>Я студе́нт</b> = tôi là sinh viên, không '
    'có động từ nào. Chỉ khi nói “có, tồn tại” mới dùng есть: <b>У меня́ есть вре́мя</b>.</div>'
    '<div class="hd-warn">Là/làm ai thì người đó phải ở cách 5: <b>Он был врачо́м</b> '
    '= anh ấy từng là bác sĩ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бу́дущее</b> tương lai · быт đời sống thường ngày '
    '· <b>собы́тие</b> sự kiện (со- cùng + быть) · <b>забы́ть</b> quên</div>'
    '<div class="hd-why">Bảng dưới THIẾU tương lai, nhớ thêm: <b>бу́ду</b> · '
    '<b>бу́дешь</b> · <b>бу́дет</b> · <b>бу́дем</b> · <b>бу́дете</b> · <b>бу́дут</b>. '
    'Quá khứ thì trọng âm nhảy ra đuôi ở giống cái: был → <b>была́</b>.</div>'
)

# ------------------------------------------------------------------ забыть
S["забыть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">ra khỏi, quá khỏi tầm với</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бы-</span>'
    '<span class="hd-gloss">gốc của быть — tồn tại</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: để cái gì lại phía sau, ra khỏi tầm — ra khỏi đầu thì '
    'là quên. Gốc là быть nên thân tương lai cũng là буд-: <b>бу́ду</b> → <b>забу́ду</b>.</div>'
    '<div class="hd-warn">Cách nó đòi tuỳ loại: quên ĐỒ thì cách 4 (<b>забы́л зонт</b>), '
    'quên VIỆC thì <b>о</b> + cách 6 (<b>забы́л о встре́че</b>).</div>'
    '<div class="hd-warn">Câu dùng hằng ngày: <b>Не забу́дь!</b> = đừng quên nhé!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>забыва́ть</b> đang/hay quên · <b>забы́вчивый</b> hay quên (tính từ) '
    '· <b>незабу́дка</b> hoa lưu ly, nghĩa đen “chớ quên”</div>'
    '<div class="hd-why">Nguyên thể là забы́ть nhưng cả bảng tương lai đi thân '
    '<b>забу́д-</b> (<b>забу́ду</b>, <b>забу́дешь</b>…) — y hệt быть → бу́ду.</div>'
)

# ------------------------------------------------------------------- взять
S["взять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вз-</span>'
    '<span class="hd-gloss">hướng lên, nhấc lên</span></div>'
    '<div class="hd-row"><span class="hd-piece">-я-</span>'
    '<span class="hd-gloss">gốc cổ “cầm, nắm”</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">вз- (lên) + -я- (nắm) = nhấc lấy. Chính gốc -я- này là chỗ '
    'thân возьм- ở bảng dưới sinh ra.</div>'
    '<div class="hd-warn">Bạn cùng cặp là <b>брать</b> (đang lấy, hay lấy) — <b>взять</b> '
    'là lấy một phát rồi xong. Học kèm nhau, đừng học rời.</div>'
    '<div class="hd-warn"><b>взять с собо́й</b> = mang theo (đồ mang theo ở cách 4: '
    '<b>взял с собо́й кни́гу</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">theo từ nguyên, cùng gốc -я-/-ним-: <b>взя́тка</b> tiền hối lộ '
    '· <b>поня́ть</b> hiểu · <b>заня́ть</b> chiếm, vay · <b>подня́ть</b> nhấc lên</div>'
    '<div class="hd-why">Nguyên thể взять và thân tương lai возьм- trông như hai từ khác '
    'nhau, phải nhớ nguyên cặp: <b>возьму́</b>, <b>возьмёшь</b>. Quá khứ trọng âm nhảy ra '
    'đuôi ở giống cái: взял → <b>взяла́</b>.</div>'
)

# ------------------------------------------------------------------ стоять
S["стоять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сто-</span>'
    '<span class="hd-gloss">đứng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ять</span>'
    '<span class="hd-gloss">đuôi động từ, lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>сто-</b> là gốc Ấn–Âu, chính là <i>stand · stay</i> '
    'của tiếng Anh — từ này nhận ra chứ không phải học.</div>'
    '<div class="hd-warn">🔴 Đừng lẫn với <b>сто́ить</b> (giá bao nhiêu): khác nhau chỉ ở '
    'chỗ trọng âm — <b>он стои́т</b> anh ấy đang đứng, <b>он сто́ит</b> nó có giá.</div>'
    '<div class="hd-warn">Tiếng Việt nói “ở trên bàn”, tiếng Nga buộc chọn tư thế: '
    '<b>ва́за стои́т на столе́</b> (đứng) · <b>лежи́т</b> (nằm) · <b>виси́т</b> (treo).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>стоя́нка</b> bãi đỗ xe · <b>постоя́ть</b> đứng một lát '
    '· <b>настоя́щий</b> thật, hiện tại (cái đang đứng đây)</div>'
)

# ---------------------------------------------------------------------------
# FIELD Vietnamese — đề bài của deck 1-go, user GÕ từ Nga từ dòng này (§2c).
# KHÔNG ghi từ loại · giống · THỂ · phản thân: bốn badge đã in sẵn ở mặt đề bài.
# курить và забыть không đụng: trong kho 950 từ không có từ nào khác dịch ra
# “hút thuốc” / “quên”, nên đề bài cũ đã chỉ có một đáp án.
V["ответить"] = "trả lời, đáp lại (một lần rồi xong; trả lời câu hỏi = на + cách 4)"
V["быть"] = "là, có mặt, tồn tại (là/làm ai thì đi với cách 5)"
V["взять"] = "lấy, cầm lấy, mượn (lấy một phát rồi xong)"
V["стоять"] = "đứng, ở tại chỗ (người đứng, đồ vật đặt đứng ở đâu)"
