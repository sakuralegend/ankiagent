# -*- coding: utf-8 -*-
"""k175 — actions: 10 cặp thể động từ, mỗi cặp một gốc.

Chỗ cần nhất quán trong lô:
(1) Cặp thể = cùng một gốc, hai đuôi: HT (hoàn thành) / CHT (chưa hoàn thành). Thẻ CHT nói
    đuôi -ива-/-а-; thẻ HT nói cách chia tương lai khi nó lệch quy tắc.
(2) Biến âm kiểu sách nhà thờ: д → жд (подтверди́ть → подтвержда́ть), т → щ (посвяти́ть →
    посвяща́ть, пропусти́ть → пропущу́) — cùng một câu ở mỗi thẻ, không bảng.
(3) Gốc mất phụ âm ở nguyên thể/quá khứ: пад- (пропа́сть, пропа́л — д lộ ở пропаду́),
    влек- (привле́чь, к → ч), рет- (приобрести́, т → с), вед- (завести́, д lộ ở заведу́).
(4) за- + вести́ → HT, за- + води́ть → CHT: khớp thẻ вести́ / води́ть / заво́д.
(5) Báo oan (khớp chuỗi): тро́гать↔стро́гий, пропа́сть↔опа́сный, привле́чь↔лечь,
    подтвержда́ть↔ждать — không ghép.
(6) пропа́сть động từ ≠ про́пасть danh từ «vực thẳm» — ô đỏ ở thẻ пропа́сть.
Họ hàng cố ý vắng: không thẻ nào — mọi gốc đều có họ thật.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "трогать": "chạm, sờ, động vào, đụng, làm phiền, làm cảm động",      # thiếu disturb/bother, move (emotionally)
    "пропадать": "mất, biến mất, mất tăm, mất tích, uổng phí",           # thiếu be wasted / go to waste
    "пропасть": "mất, biến mất, mất tích, tiêu tan, uổng phí",           # thiếu be wasted / be in vain
    "пропускать": "bỏ lỡ, bỏ qua, bỏ sót, cho qua, cho vào, vắng mặt",   # «nghỉ học» là một cách dùng; thiếu let in / omit
    "пропустить": "bỏ lỡ, bỏ qua, bỏ sót, cho qua, cho vào, vắng mặt",   # thiếu let in / omit; cùng bộ với cặp
    "назначать": "bổ nhiệm, chỉ định, hẹn, xếp lịch, kê đơn",            # thiếu prescribe
    "назначить": "bổ nhiệm, chỉ định, hẹn, ấn định, kê đơn",             # thiếu prescribe
    "завести": "khởi động, nổ máy, lên dây cót, nuôi, sắm, lập, bắt chuyện, dẫn đi",   # thiếu get/acquire, establish, strike up, lead
    "заводить": "khởi động, nổ máy, lên dây cót, nuôi, sắm, lập, bắt chuyện, dẫn đi",  # như trên; bỏ «mở cho chạy» (trùng)
}

# --------------------------------------------------------------------- обеспечивать
S["обеспечивать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">LÀM CHO thành… — như <b>освободи́ть</b> làm cho tự do</span></div>'
    '<div class="hd-row"><span class="hd-piece">-беспеч-</span>'
    '<span class="hd-gloss">VÔ LO — <b>без</b> không + <b>печ-</b> lo (<b>пе́чься</b> lo cho)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm cho ai KHÔNG CÒN PHẢI LO (<b>беспе́чный</b> vô tư lự) ⇒ lo đủ cho, '
    'bảo đảm. Chia đều: <b>обеспе́чиваю</b>. Cặp HT: <b>обеспе́чить</b>.</div>'
    '<div class="hd-warn">Hai kiểu câu: <b>обеспе́чивать</b> ai (C4) + cái gì (C5) = cấp cho ai cái gì · '
    '<b>обеспе́чивать безопа́сность</b> = bảo đảm an toàn (C4).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обеспе́чение</b> sự bảo đảm, sự cung cấp · <b>обеспе́ченный</b> khá giả · '
    '<b>беспе́чный</b> vô tư lự</div>'
)

# --------------------------------------------------------------------- обеспечить
S["обеспечить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">LÀM CHO thành…</span></div>'
    '<div class="hd-row"><span class="hd-piece">-беспеч-</span>'
    '<span class="hd-gloss">VÔ LO — như <b>беспе́чный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm xong việc «khiến ai hết lo» ⇒ đã cấp đủ, đã bảo đảm. Tương lai chia đều: '
    '<b>обеспе́чу, обеспе́чишь</b>. Cặp CHT: <b>обеспе́чивать</b>.</div>'
    '<div class="hd-warn">Thứ được cấp đi ở C5: <b>обеспе́чить шко́лу компью́терами</b> — trang bị '
    'máy tính cho trường.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обеспе́чение</b> sự bảo đảm · <b>обеспе́ченный</b> khá giả · '
    '<b>беспе́чный</b> vô tư lự</div>'
)

# --------------------------------------------------------------------- трогать
S["трогать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">трог-</span>'
    '<span class="hd-gloss">CHẠM (gốc trơn)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chạm tay vào — và chạm vào LÒNG: <b>Э́то меня́ тро́гает</b> = điều đó làm '
    'tôi cảm động. Đòi C4. Chia đều: <b>тро́гаю</b>. Cặp HT chính: <b>тро́нуть</b> '
    '(<b>-ну-</b> một cái, г rơi trước н).</div>'
    '<div class="hd-warn"><b>Не тро́гай!</b> — Đừng đụng vào! · <b>Не тро́гай меня́</b> — để tôi yên.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тро́нуть</b> chạm, làm cảm động (HT) · <b>потро́гать</b> sờ thử · '
    '<b>тро́гательный</b> cảm động · <b>тро́нуться</b> khởi hành</div>'
)

# --------------------------------------------------------------------- потрогать
S["потрогать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">MỘT LÚC, một chút</span></div>'
    '<div class="hd-row"><span class="hd-piece">-трог-ать</span>'
    '<span class="hd-gloss">CHẠM — như <b>тро́гать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chạm MỘT LÚC để cảm nhận ⇒ sờ thử: <b>потро́гать ткань</b> sờ thử vải. '
    'Cùng khuôn <b>по-</b> «một lát» như <b>поговори́ть</b> nói chuyện một lát. '
    'Tương lai: <b>потро́гаю</b>.</div>'
    '<div class="hd-warn">Chạm MỘT CÁI, hay chạm tới lòng người, là <b>тро́нуть</b> — không phải '
    '<b>потро́гать</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тро́гать</b> chạm, sờ (CHT) · <b>тро́нуть</b> chạm, làm cảm động · '
    '<b>тро́гательный</b> cảm động</div>'
)

# --------------------------------------------------------------------- пропадать
S["пропадать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">QUA, trôi mất đi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пад-</span>'
    '<span class="hd-gloss">RƠI — gốc của <b>па́дать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Rơi lọt mất đi ⇒ biến mất, thất lạc, hoặc bị phí: <b>Еда́ пропада́ет</b> '
    'đồ ăn bị bỏ phí. Chia đều: <b>пропада́ю</b>. Cặp HT: <b>пропа́сть</b>.</div>'
    '<div class="hd-warn"><b>Где ты пропада́л?</b> — Cậu biến đi đâu (suốt thời gian qua) thế?</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пропа́сть</b> biến mất (HT) · <b>па́дать</b> rơi · <b>упа́сть</b> ngã · '
    '<b>пропа́жа</b> đồ bị mất</div>'
)

# --------------------------------------------------------------------- пропасть
S["пропасть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">QUA, trôi mất đi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пас-ть</span>'
    '<span class="hd-gloss">RƠI — gốc <b>пад-</b>, д rơi mất trước -ть</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chia như <b>упа́сть</b>: д hiện lại ở tương lai <b>пропаду́, пропадёшь</b>, '
    'mất ở quá khứ <b>пропа́л, пропа́ла</b>. Cặp CHT: <b>пропада́ть</b>.</div>'
    '<div class="hd-warn"><b>пропа́сть без ве́сти</b> — mất tích (không tin tức gì).</div>'
    '<div class="hd-warn">Cùng mặt chữ, nhấn khác: <b>про́пасть</b> (danh từ giống cái) = vực thẳm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пропада́ть</b> biến mất (CHT) · <b>па́дать</b> rơi · <b>упа́сть</b> ngã · '
    '<b>пропа́жа</b> đồ bị mất</div>'
)

# --------------------------------------------------------------------- подтвердить
S["подтвердить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span>'
    '<span class="hd-gloss">ĐỠ thêm từ dưới — như <b>поддержа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-тверд-</span>'
    '<span class="hd-gloss">CỨNG, VỮNG — gốc của <b>твёрдый</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đỡ cho điều đã nói thêm VỮNG ⇒ xác nhận. Ngôi «tôi» д → ж: '
    '<b>подтвержу́</b>, còn lại giữ д: <b>подтверди́шь</b>. Cặp CHT: <b>подтвержда́ть</b>.</div>'
    '<div class="hd-warn"><b>Подтверди́ть</b> — nút «Xác nhận» trên app, web: '
    '<b>подтверди́ть зака́з</b> xác nhận đơn hàng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>твёрдый</b> cứng, vững · <b>подтвержде́ние</b> sự xác nhận · '
    '<b>утверди́ть</b> phê duyệt</div>'
)

# --------------------------------------------------------------------- подтверждать
S["подтверждать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span>'
    '<span class="hd-gloss">ĐỠ thêm từ dưới</span></div>'
    '<div class="hd-row"><span class="hd-piece">-твержд-</span>'
    '<span class="hd-gloss">CỨNG, VỮNG — <b>твёрд-</b>, д thành жд</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">HT <b>-ди́ть</b> → CHT <b>-жда́ть</b> là một khuôn lặp lại: '
    '<b>победи́ть → побежда́ть</b>. Chia đều: <b>подтвержда́ю</b>. Cặp HT: <b>подтверди́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>твёрдый</b> cứng, vững · <b>подтвержде́ние</b> sự xác nhận · '
    '<b>утверди́ть</b> phê duyệt</div>'
)

# --------------------------------------------------------------------- привлекать
S["привлекать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">TỚI GẦN, về phía mình</span></div>'
    '<div class="hd-row"><span class="hd-piece">-влек-</span>'
    '<span class="hd-gloss">KÉO, LÔI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Kéo về phía mình ⇒ thu hút, lôi cuốn; kéo người vào việc ⇒ huy động. '
    'Chia đều: <b>привлека́ю</b>. Cặp HT: <b>привле́чь</b>.</div>'
    '<div class="hd-warn"><b>привлека́ть внима́ние</b> — thu hút sự chú ý.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>привлека́тельный</b> hấp dẫn · <b>увле́чься</b> say mê · '
    '<b>увлече́ние</b> sở thích · <b>развлече́ние</b> trò giải trí · <b>отвле́чь</b> làm xao nhãng</div>'
)

# --------------------------------------------------------------------- привлечь
S["привлечь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">TỚI GẦN, về phía mình</span></div>'
    '<div class="hd-row"><span class="hd-piece">-влечь</span>'
    '<span class="hd-gloss">KÉO — gốc <b>влек-</b>, к + ть → чь</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi <b>-чь</b> giấu chữ к: nó hiện lại khi chia — <b>привлеку́, '
    'привлечёшь, привлеку́т</b>; quá khứ <b>привлёк, привлекла́</b>. Cùng khuôn với <b>печь → пеку́</b>. '
    'Cặp CHT: <b>привлека́ть</b>.</div>'
    '<div class="hd-warn"><b>привле́чь к отве́тственности</b> — truy cứu trách nhiệm (đưa ra pháp luật).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>привлека́тельный</b> hấp dẫn · <b>увле́чься</b> say mê · '
    '<b>увлече́ние</b> sở thích · <b>отвле́чь</b> làm xao nhãng</div>'
)

# --------------------------------------------------------------------- пропускать
S["пропускать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">QUA, xuyên qua</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пуск-</span>'
    '<span class="hd-gloss">THẢ, BUÔNG — như <b>о́тпуск</b>, <b>отпуска́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thả cho đi QUA: cho người qua cửa — hoặc để buổi học, chuyến xe trôi '
    'qua mất ⇒ bỏ lỡ: <b>пропуска́ть уро́ки</b> bỏ học. Chia đều: <b>пропуска́ю</b>. '
    'Cặp HT: <b>пропусти́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пропусти́ть</b> bỏ lỡ (HT) · <b>про́пуск</b> thẻ ra vào · '
    '<b>о́тпуск</b> kỳ nghỉ phép · <b>отпуска́ть</b> thả ra · <b>пусть</b> cứ để</div>'
)

# --------------------------------------------------------------------- пропустить
S["пропустить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">QUA, xuyên qua</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пуст-и́ть</span>'
    '<span class="hd-gloss">THẢ, BUÔNG — như <b>отпусти́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ngôi «tôi» ст → щ và trọng âm ở cuối: <b>пропущу́</b>; các ngôi khác '
    'nhấn lùi vào thân: <b>пропу́стишь, пропу́стят</b>. Cặp CHT: <b>пропуска́ть</b>.</div>'
    '<div class="hd-warn"><b>Пропусти́те, пожа́луйста!</b> — Cho tôi đi qua với! (nơi đông người).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пропуска́ть</b> bỏ lỡ (CHT) · <b>про́пуск</b> thẻ ra vào · '
    '<b>отпусти́ть</b> thả ra · <b>пусто́й</b> rỗng · <b>пусть</b> cứ để</div>'
)

# --------------------------------------------------------------------- приобрести
S["приобрести"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">THÊM VÀO cho mình</span></div>'
    '<div class="hd-row"><span class="hd-piece">-об-</span>'
    '<span class="hd-gloss">tiền tố cũ — chữ б thuộc về đây</span></div>'
    '<div class="hd-row"><span class="hd-piece">-рес-ти́</span>'
    '<span class="hd-gloss">GẶP, TÌM THẤY — gốc <b>рет-</b>, т + т → ст</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tìm thấy thêm về cho mình ⇒ có được, mua được. т hiện lại ở tương lai '
    '<b>приобрету́, приобретёшь</b>; quá khứ rơi mất: <b>приобрёл, приобрела́</b>. '
    'Cặp CHT: <b>приобрета́ть</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: <b>-рет-</b> nối với <b>встре́тить</b> là từ nguyên (mặt chữ đã '
    'mờ), không phải luật suy ra được.</div>'
    '<div class="hd-warn">«Mua» kiểu trang trọng của quảng cáo, thông báo: <b>приобрести́ биле́т</b>. '
    'Nói thường thì <b>купи́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>приобрета́ть</b> có được (CHT) · <b>приобрете́ние</b> thứ mua được · '
    '<b>обрести́</b> tìm được</div>'
)

# --------------------------------------------------------------------- приобретать
S["приобретать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-об-</span>'
    '<span class="hd-gloss">THÊM VÀO cho mình (hai tiền tố)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-рет-</span>'
    '<span class="hd-gloss">GẶP, TÌM THẤY</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dần dần có thêm cho mình: <b>приобрета́ть о́пыт</b> tích luỹ kinh nghiệm. '
    'Chia đều: <b>приобрета́ю</b>. Cặp HT: <b>приобрести́</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: <b>-рет-</b> là gốc của <b>встре́тить</b> gặp — từ nguyên, '
    'không phải luật suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>приобрести́</b> có được (HT) · <b>приобрете́ние</b> thứ mua được · '
    '<b>обрести́</b> tìm được</div>'
)

# --------------------------------------------------------------------- назначать
S["назначать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">LÊN, đặt vào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-знач-</span>'
    '<span class="hd-gloss">DẤU — <b>знак</b>, к → ч</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đánh dấu lên một người, một ngày ⇒ chỉ định người (bổ nhiệm), ấn định '
    'ngày (hẹn), chỉ định thuốc (kê đơn). Chia đều: <b>назнача́ю</b>. Cặp HT: <b>назна́чить</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>знак</b> dấu hiệu · <b>зна́чить</b> có nghĩa là · '
    '<b>значе́ние</b> ý nghĩa · <b>назначе́ние</b> sự bổ nhiệm, công dụng</div>'
)

# --------------------------------------------------------------------- назначить
S["назначить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">LÊN, đặt vào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-знач-</span>'
    '<span class="hd-gloss">DẤU — như <b>знак</b>, <b>зна́чить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đã đánh dấu chọn xong: <b>назна́чить встре́чу</b> hẹn một cuộc gặp. '
    'Tương lai chia đều: <b>назна́чу, назна́чишь</b>. Cặp CHT: <b>назнача́ть</b>.</div>'
    '<div class="hd-warn">Bổ nhiệm LÀM GÌ → C5: <b>Его́ назна́чили дире́ктором</b> — anh ấy được '
    'bổ nhiệm làm giám đốc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>знак</b> dấu hiệu · <b>зна́чить</b> có nghĩa là · '
    '<b>значе́ние</b> ý nghĩa · <b>назначе́ние</b> sự bổ nhiệm</div>'
)

# --------------------------------------------------------------------- посвятить
S["посвятить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố — không mang nghĩa riêng ở đây</span></div>'
    '<div class="hd-row"><span class="hd-piece">-свят-</span>'
    '<span class="hd-gloss">THÁNH — gốc của <b>свято́й</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dâng trọn cho điều thiêng liêng ⇒ dành hết cho, đề tặng; cho người vào '
    'chốn thiêng ⇒ cho biết bí mật. Ngôi «tôi» т → щ: <b>посвящу́</b>. Cặp CHT: <b>посвяща́ть</b>.</div>'
    '<div class="hd-warn">Dành CÁI GÌ (C4) CHO AI/VIỆC GÌ (C3): <b>посвяти́ть жизнь нау́ке</b> — '
    'dành cả đời cho khoa học.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>свято́й</b> thánh · <b>свяще́нник</b> linh mục · '
    '<b>посвяще́ние</b> lời đề tặng</div>'
)

# --------------------------------------------------------------------- посвящать
S["посвящать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố — không mang nghĩa riêng ở đây</span></div>'
    '<div class="hd-row"><span class="hd-piece">-свящ-</span>'
    '<span class="hd-gloss">THÁNH — <b>свят-</b>, т thành щ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">HT <b>-ти́ть</b> → CHT <b>-ща́ть</b> là một khuôn lặp lại: <b>защити́ть → защища́ть</b>; '
    'cùng chữ щ như <b>свяще́нник</b>. Chia đều: <b>посвяща́ю</b>. Cặp HT: <b>посвяти́ть</b>.</div>'
    '<div class="hd-warn"><b>посвяща́ть</b> ai (C4) <b>в та́йну</b> — cho ai biết bí mật.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>свято́й</b> thánh · <b>свяще́нник</b> linh mục · '
    '<b>посвяще́ние</b> lời đề tặng</div>'
)

# --------------------------------------------------------------------- завести
S["завести"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">BẮT ĐẦU; hoặc vào sâu, ra xa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вес-ти́</span>'
    '<span class="hd-gloss">DẪN — <b>вести́</b>, gốc <b>вед-</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dẫn cho bắt đầu chạy ⇒ nổ máy, lên dây cót; dẫn về nhà mình ⇒ có thêm. '
    'д hiện lại ở tương lai <b>заведу́, заведёшь</b>; quá khứ <b>завёл, завела́</b>. '
    'Tiền tố + <b>вести́</b> = HT; cặp CHT là tiền tố + <b>води́ть</b>: <b>заводи́ть</b>.</div>'
    '<div class="hd-warn"><b>завести́ маши́ну</b> nổ máy xe · <b>буди́льник</b> đặt báo thức · '
    '<b>соба́ку</b> nuôi chó · <b>разгово́р</b> bắt chuyện.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вести́</b> dẫn · <b>води́ть</b> dẫn, lái · <b>заво́д</b> nhà máy · '
    '<b>заведе́ние</b> cơ sở, quán</div>'
)

# --------------------------------------------------------------------- заводить
S["заводить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">BẮT ĐẦU; hoặc vào sâu, ra xa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вод-и́ть</span>'
    '<span class="hd-gloss">DẪN — như <b>води́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiền tố + <b>води́ть</b> = CHT (cặp HT: <b>завести́</b>). Ngôi «tôi» д → ж: '
    '<b>завожу́</b>; các ngôi khác nhấn lùi vào thân: <b>заво́дишь</b>. <b>заво́д</b> nhà máy là nơi '
    'việc được «dựng lên cho chạy».</div>'
    '<div class="hd-warn"><b>заводи́ть</b> cũng là «làm cho phấn khích, kích động»: '
    '<b>Не заводи́ его́!</b> — Đừng chọc cho nó nổi nóng!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>води́ть</b> dẫn, lái · <b>вести́</b> dẫn · <b>заво́д</b> nhà máy · '
    '<b>заведе́ние</b> cơ sở, quán</div>'
)

B = {
    "docbangmat": 106,
    "loitubat": 1,
    "nguonsai": 0,
    "baolen": [
        "Tự sửa 1 lỗi: thẻ посвяти́ть ghi по- là «tiền tố hoàn thành» — sai, vì посвяща́ть (CHT) vẫn giữ по-; đã hạ thành «tiền tố, không mang nghĩa riêng ở đây».",
        "THÊM 1 mục MIEN_TRU (data/huongdan/mientru.py): пропа́сть — đồng tự thật, ĐỘNG TỪ biến mất ↔ danh từ про́пасть vực thẳm (nouns.csv chỉ có danh từ). Cùng lớp với помо́чь đã miễn trừ. Luồng chính duyệt.",
        "Không chắc (từ nguyên, ghi Mức tin trên thẻ): приобрести́/приобрета́ть = при- + об- + gốc -рет- của встре́тить (theo Vasmer).",
        "Không chắc (từ nguyên, KHÔNG gắn Mức tin vì mặt chữ còn thấy): обеспе́чить ← беспе́чный (без + печ- «lo», пе́чься); пусто́й cùng gốc пусти́ть (theo bối cảnh luồng chính + Vasmer).",
        "V cần duyệt: тро́гать (+làm phiền, làm cảm động) · пропада́ть/пропа́сть (+uổng phí) · пропуска́ть/пропусти́ть (bỏ «nghỉ học» — một cách dùng; +bỏ sót, cho vào, vắng mặt; hai thẻ cùng bộ, badge thể tách) · назнача́ть/назна́чить (+kê đơn) · завести́/заводи́ть (+nuôi, sắm, lập, bắt chuyện, dẫn đi; bỏ «làm cho chạy»/«mở cho chạy» trùng ý).",
        "Cố ý KHÔNG sửa: приобрета́ть giữ «nhiễm phải» (gloss chỉ ghi «acquire or gain» — luồng chính xem có muốn bỏ); заводи́ть nghĩa «kích động» (excite, get worked up) chỉ dạy ở ô đỏ, không đưa vào V vì là khẩu ngữ.",
        "Va chạm nghĩa: lệnh tiep báo (khong co); trong lô các cặp thể chung nghĩa, badge thể tách.",
    ],
}
