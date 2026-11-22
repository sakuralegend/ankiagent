# -*- coding: utf-8 -*-
"""k187 — actions (lô trộn): 8 cặp thể + vài trạng từ/danh từ đo lường.

Chỗ cần nhất quán trong lô:
(1) рассчитать/рассчитывать: рас- + счита́ть, chẻ -с-/-чит- y hệt считать (k112). Bẫy: hai с,
    nhưng расчёт một с.
(2) выдать/выдавать: -да- CHO, -ва- hậu tố «đang/hay làm» (khớp дава́ть, отдава́ть k01/k97);
    HT вы́- luôn nhấn, CHT bỏ -ва- ở hiện tại: выдаю́.
(3) оплатить/оплачивать: плат- TRẢ TIỀN (khớp плати́ть k95). Trục: о- làm động từ nhận THẲNG
    cách 4 ⇒ оплати́ть счёт, khác заплати́ть ЗА счёт.
(4) преследовать: след- DẤU VẾT (k171). обмануть/обманывать: об- + -ман (k177).
(5) взорвать/взрывать: вз- + рв-/рыв- (k161 взрыв): thân ngắn рв (+о đệm) cho HT, thân dài рыв cho CHT.
(6) выбросить/выбрасывать: брос- NÉM (k122); о→а khi thêm -ыва-.
(7) посадить/сажать: сад- NGỒI (k97 садиться) — nghĩa «ĐẶT cho ngồi / đặt xuống».
(8) единица ↔ единый (k123); втроём ↔ трое (k116); целиком ↔ целый (k109);
    минимальный/максимум ↔ минимум (k169).
Họ hàng cố ý vắng: không có (mọi từ trong lô đều có họ thật).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "оплатить": "thanh toán, trả tiền cho, chi trả, trang trải",              # gỡ ⊇ заплати́ть[k95]: «to pay for / to cover (the cost of)»
    "оплачивать": "thanh toán, trả tiền cho, chi trả, trang trải, tài trợ",   # gỡ ⊇ плати́ть[k95]: + finance/fund
    "дрожать": "run, run rẩy, rung, lập cập",                                 # «rẩy» đứng một mình không phải nghĩa
}

# --------------------------------------------------------------------- единица
S["единица"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">еди́н-</span>'
    '<span class="hd-gloss">MỘT — dạng cổ của <b>оди́н</b>, như <b>еди́ный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ца</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cái MỘT» ⇒ số một, chữ số 1; cái một làm mốc để đếm ⇒ đơn vị: '
    '<b>едини́ца измере́ния</b> đơn vị đo.</div>'
    '<div class="hd-warn">Trường Nga chấm thang 5: <b>едини́ца</b> là điểm 1 — điểm kém nhất.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>еди́ный</b> thống nhất · <b>еди́нственный</b> duy nhất · '
    '<b>еди́нство</b> sự thống nhất · <b>оди́н</b> một</div>'
)

# --------------------------------------------------------------------- минимальный
S["минимальный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">миним-</span>'
    '<span class="hd-gloss">từ mượn Latin — chính là <b>ми́нимум</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́льный</span>'
    '<span class="hd-gloss">đuôi tính từ ≈ Anh <i>-al</i> (<i>minimal</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>ми́нимум</b> + <b>-а́льный</b>, trọng âm dời ra đuôi như '
    '<b>норма́льный</b>. Dạng ngắn giống đực chèn thêm <b>е</b> để tách cụm <b>-льн</b>: '
    '<b>минима́лен</b>. Trạng từ: <b>минима́льно</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ми́нимум</b> mức tối thiểu · <b>максима́льный</b> tối đa (cùng khuôn)</div>'
)

# --------------------------------------------------------------------- втроём
S["втроём"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">mảnh mở khuôn trạng từ «n người cùng nhau»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тро-</span>'
    '<span class="hd-gloss">BA — như <b>тро́е</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ём</span>'
    '<span class="hd-gloss">đuôi của khuôn, luôn nhấn</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhóm ba người làm chung một việc: <b>Мы пошли́ втроём</b> = ba chúng '
    'tôi cùng đi (tính cả người nói). Cùng khuôn: <b>вдвоём</b> hai người cùng nhau, '
    '<b>вчетверо́м</b> bốn người.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тро́е</b> ba người · <b>три</b> ba · <b>тро́йка</b> bộ ba · '
    '<b>вдвоём</b> hai người cùng nhau</div>'
)

# --------------------------------------------------------------------- целиком
S["целиком"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">цел-</span>'
    '<span class="hd-gloss">NGUYÊN, LÀNH — như <b>це́лый</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ико́м</span>'
    '<span class="hd-gloss">đuôi trạng từ, không mang nghĩa riêng — như <b>пешко́м</b> đi bộ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Nguyên cả khối, không tách ra» ⇒ toàn bộ, trọn vẹn: '
    '<b>прочита́ть кни́гу целико́м</b> đọc trọn cuốn sách.</div>'
    '<div class="hd-warn"><b>целико́м и по́лностью</b> = hoàn toàn, trăm phần trăm (cụm cố định).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>це́лый</b> nguyên, cả · <b>це́лое</b> tổng thể · '
    '<b>в це́лом</b> nhìn chung</div>'
)

# --------------------------------------------------------------------- максимум
S["максимум"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn Latin <i>maximum</i>, không chẻ được — chữ-đối-chữ tiếng Anh.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mức cao nhất. Đứng một mình như trạng từ «tối đa»: <b>ма́ксимум час</b> '
    'nhiều nhất một tiếng. Trái nghĩa: <b>ми́нимум</b>.</div>'
    '<div class="hd-warn"><b>как ма́ксимум</b> — nhiều nhất là, tối đa là.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>максима́льный</b> tối đa (trọng âm dời ra <b>-а́льный</b>)</div>'
)

# --------------------------------------------------------------------- рассчитать
S["рассчитать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рас-</span>'
    '<span class="hd-gloss">TÁCH RA từng phần, làm tới nơi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-с-чит-а́ть</span>'
    '<span class="hd-gloss">chính là <b>счита́ть</b>: с- GỘP + -чит- ĐẾM</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tính ra tới từng phần ⇒ tính toán, tính ra. Tính trả đủ lương rồi cho '
    'nghỉ ⇒ sa thải. Cặp CHT: <b>рассчи́тывать</b>.</div>'
    '<div class="hd-warn">Hai chữ <b>с</b> vì <b>рас-</b> + <b>счита́ть</b>. Nhưng danh từ '
    '<b>расчёт</b> chỉ MỘT <b>с</b>.</div>'
    '<div class="hd-warn"><b>рассчи́тан на</b> + cách 4 = được tính cho: <b>Зал рассчи́тан на '
    'сто челове́к.</b> Hội trường dành cho 100 người.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>счита́ть</b> đếm, cho rằng · <b>расчёт</b> sự tính toán · '
    '<b>счёт</b> hóa đơn · <b>чита́ть</b> đọc</div>'
)

# --------------------------------------------------------------------- рассчитывать
S["рассчитывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рас-</span>'
    '<span class="hd-gloss">TÁCH RA từng phần, làm tới nơi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-с-чит-</span>'
    '<span class="hd-gloss">như <b>счита́ть</b>: GỘP + ĐẾM</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-ть</span>'
    '<span class="hd-gloss">hậu tố «đang / hay làm» → CHT, chia đều: <b>рассчи́тываю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>рассчита́ть</b>. Tính trước vào phần người khác ⇒ '
    'trông cậy — nghĩa hay gặp nhất của thể CHT này.</div>'
    '<div class="hd-warn">Trông cậy vào AI/CÁI GÌ → <b>на</b> + cách 4: <b>Я рассчи́тываю на '
    'тебя́.</b> Tôi trông vào cậu đấy.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рассчита́ть</b> tính ra (HT) · <b>счита́ть</b> đếm · '
    '<b>расчёт</b> sự tính toán · <b>расчётливый</b> tính toán chi li</div>'
)

# --------------------------------------------------------------------- сойти
S["сойти"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">TỪ TRÊN XUỐNG, rời khỏi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о-</span>'
    '<span class="hd-gloss">nguyên âm đệm, không nghĩa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-йти́</span>'
    '<span class="hd-gloss">= <b>идти́</b> ĐI bộ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đi rời khỏi chỗ cao ⇒ xuống: <b>сойти́ с авто́буса</b> xuống xe buýt '
    '(<b>с</b> + cách 2). Bảng chia theo <b>идти́</b>: <b>сойду́</b>, và quá khứ mượn thân '
    '<b>шёл</b> như <b>пошёл</b>: <b>сошёл</b>, <b>сошла́</b>.</div>'
    '<div class="hd-warn"><b>сойти́ с ума́</b> = phát điên («rời khỏi trí óc»): '
    '<b>Ты с ума́ сошёл?</b> Mày điên à?</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сходи́ть</b> đi xuống (CHT) · <b>идти́</b> đi · '
    '<b>сумасше́дший</b> điên · <b>уйти́</b> rời đi</div>'
)

# --------------------------------------------------------------------- выдавать
S["выдавать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span>'
    '<span class="hd-gloss">RA NGOÀI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-да-</span>'
    '<span class="hd-gloss">CHO</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва-</span>'
    '<span class="hd-gloss">hậu tố «đang / hay làm» → CHT</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đưa RA cho ⇒ cấp, phát: <b>выдава́ть па́спорт</b> cấp hộ chiếu. Đưa ra '
    'cái lẽ ra phải giấu ⇒ để lộ. Như <b>дава́ть</b>, hiện tại BỎ <i>-ва-</i>: '
    '<b>выдаю́</b>, <b>выдаёшь</b>.</div>'
    '<div class="hd-warn"><b>выдава́ть себя́ за</b> + cách 4 = mạo nhận là: <b>Он выдаёт себя́ '
    'за врача́.</b> Hắn mạo nhận là bác sĩ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вы́дать</b> (HT) · <b>дава́ть</b> cho · <b>вы́дача</b> sự cấp phát · '
    '<b>отдава́ть</b> trả lại</div>'
)

# --------------------------------------------------------------------- выдать
S["выдать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы́-</span>'
    '<span class="hd-gloss">RA NGOÀI — ở thể HT luôn mang trọng âm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дать</span>'
    '<span class="hd-gloss">CHO — chính là <b>дать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đưa RA cho ⇒ cấp, phát: <b>вы́дать спра́вку</b> cấp giấy xác nhận; lỡ '
    'đưa ra ⇒ để lộ: <b>вы́дать секре́т</b>. Bảng chia bất quy tắc y hệt <b>дать</b> — nhớ '
    '<b>дать</b> là nhớ cả bảng: <b>вы́дам</b>, <b>вы́даст</b>, <b>вы́дадим</b>, '
    '<b>вы́дадут</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>выдава́ть</b> (CHT) · <b>дать</b> cho · <b>вы́дача</b> sự cấp phát · '
    '<b>отда́ть</b> trả lại</div>'
)

# --------------------------------------------------------------------- оплатить
S["оплатить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">PHỦ LÊN đối tượng — động từ nhận THẲNG cách 4</span></div>'
    '<div class="hd-row"><span class="hd-piece">-плат-и́ть</span>'
    '<span class="hd-gloss">gốc TRẢ TIỀN — chính là <b>плати́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trả tiền phủ trọn một khoản ⇒ thanh toán nó: <b>оплати́ть счёт</b> '
    'thanh toán hoá đơn. Chia như <b>плати́ть</b>: <b>т</b> hoá <b>ч</b> ở ngôi «tôi» — '
    '<b>оплачу́</b>, <b>опла́тишь</b>.</div>'
    '<div class="hd-warn">KHÔNG có <b>за</b>: <b>оплати́ть пое́здку</b> = <b>заплати́ть за '
    'пое́здку</b> (trả tiền chuyến đi). Nói «оплатить за» là lỗi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>опла́чивать</b> (CHT) · <b>опла́та</b> sự thanh toán · '
    '<b>плати́ть</b> trả tiền · <b>зарпла́та</b> tiền lương</div>'
)

# --------------------------------------------------------------------- оплачивать
S["оплачивать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">PHỦ LÊN đối tượng — nhận THẲNG cách 4</span></div>'
    '<div class="hd-row"><span class="hd-piece">-плач-</span>'
    '<span class="hd-gloss">= <b>плат-</b> TRẢ TIỀN, <b>т</b> hoá <b>ч</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ть</span>'
    '<span class="hd-gloss">hậu tố «đang / hay làm» → CHT, chia đều: <b>опла́чиваю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>оплати́ть</b>, cho khoản trả đều đặn: <b>опла́чивать '
    'кварти́ру</b> trả tiền nhà hằng tháng. Cũng KHÔNG có <b>за</b> — khác <b>плати́ть за</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оплати́ть</b> (HT) · <b>опла́та</b> sự thanh toán · '
    '<b>плати́ть</b> trả tiền · <b>беспла́тный</b> miễn phí</div>'
)

# --------------------------------------------------------------------- преследовать
S["преследовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пре-</span>'
    '<span class="hd-gloss">tiền tố cổ ≈ <b>пере-</b>, nghĩa riêng đã mờ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-след-</span>'
    '<span class="hd-gloss">DẤU VẾT — chính là <b>след</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-ть</span>'
    '<span class="hd-gloss">đuôi động từ như <b>сле́довать</b> đi theo, chia <b>-у-</b>: <b>пресле́дую</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Theo sát dấu vết ai ⇒ truy đuổi; bám không buông ⇒ ngược đãi, ám '
    'ảnh. Nhận thẳng cách 4: <b>пресле́довать престу́пника</b> truy đuổi tội phạm.</div>'
    '<div class="hd-warn"><b>пресле́довать по зако́ну</b> = truy tố.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>след</b> dấu vết · <b>следи́ть</b> theo dõi · <b>иссле́довать</b> '
    'nghiên cứu · <b>пресле́дование</b> sự truy đuổi</div>'
)

# --------------------------------------------------------------------- обмануть
S["обмануть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">VÒNG QUANH, qua mặt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ман-</span>'
    '<span class="hd-gloss">DỤ, VẪY GỌI — gốc của <b>мани́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-у́-ть</span>'
    '<span class="hd-gloss">hậu tố thể HT: làm xong một lần (<b>н</b> thuộc gốc)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dụ người ta đi vòng qua sự thật ⇒ lừa — động từ của <b>обма́н</b>. '
    'Trọng âm lùi từ ngôi hai: <b>обману́</b>, <b>обма́нешь</b>, <b>обма́нут</b>.</div>'
    '<div class="hd-warn"><b>Меня́ обману́ли!</b> = Tôi bị lừa rồi! — tiếng Nga nói «(họ) lừa '
    'tôi», không cần chủ ngữ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обма́н</b> sự lừa dối · <b>обма́нывать</b> (CHT) · '
    '<b>обма́нщик</b> kẻ lừa đảo · <b>мани́ть</b> vẫy gọi</div>'
)

# --------------------------------------------------------------------- обманывать
S["обманывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">VÒNG QUANH, qua mặt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ман-</span>'
    '<span class="hd-gloss">DỤ, VẪY GỌI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-ть</span>'
    '<span class="hd-gloss">hậu tố «đang / hay làm» → CHT, chia đều: <b>обма́нываю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>обману́ть</b>: hậu tố <b>-у-</b> rơi, thay bằng <b>-ыва-</b>, '
    'trọng âm về gốc <b>-ма́н-</b>. Dùng cho thói quen: <b>Он всегда́ обма́нывает.</b> '
    'Hắn lúc nào cũng lừa.</div>'
    '<div class="hd-warn">Cấm làm thì dùng CHT: <b>Не обма́нывай меня́!</b> = Đừng lừa tôi!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обма́н</b> sự lừa dối · <b>обману́ть</b> (HT) · '
    '<b>обма́нчивый</b> dễ đánh lừa</div>'
)

# --------------------------------------------------------------------- взорвать
S["взорвать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">взо-</span>'
    '<span class="hd-gloss">BẬT LÊN — <b>вз-</b> + <b>о</b> đệm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-рв-а́ть</span>'
    '<span class="hd-gloss">XÉ, GIẬT — chính là <b>рвать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Xé tung lên» ⇒ làm nổ (cũng là: làm ai nổi điên). Thân ngắn <b>рв</b> '
    'cho HT, thân dài <b>рыв</b> cho CHT <b>взрыва́ть</b> và danh từ <b>взрыв</b>. Chia như '
    '<b>рвать</b>: <b>взорву́</b>; quá khứ giống cái nhấn đuôi: <b>взорвала́</b>.</div>'
    '<div class="hd-warn">Tự nổ là <b>-ся</b>: <b>Бо́мба взорвала́сь.</b> Quả bom nổ. Không '
    '<b>-ся</b> là CÓ người cho nổ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>взрыв</b> vụ nổ · <b>взрыва́ть</b> (CHT) · <b>рвать</b> xé · '
    '<b>переры́в</b> giờ nghỉ</div>'
)

# --------------------------------------------------------------------- взрывать
S["взрывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вз-</span>'
    '<span class="hd-gloss">BẬT LÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-рыв-</span>'
    '<span class="hd-gloss">XÉ, GIẬT — mặt dài của <b>рв-</b>, như <b>взрыв</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>взрыва́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>взорва́ть</b>. Ở cặp này nhìn thân là biết thể: <b>рыв</b> '
    'dài (y hệt danh từ <b>взрыв</b>) ⇒ CHT; <b>рв</b> ngắn ⇒ HT.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>взрыв</b> vụ nổ · <b>взорва́ть</b> (HT) · <b>взрывча́тка</b> '
    'thuốc nổ · <b>переры́в</b> giờ nghỉ</div>'
)

# --------------------------------------------------------------------- выбрасывать
S["выбрасывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span>'
    '<span class="hd-gloss">RA NGOÀI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-брас-</span>'
    '<span class="hd-gloss">= <b>брос-</b> NÉM, <b>о</b> đổi <b>а</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-ть</span>'
    '<span class="hd-gloss">hậu tố «đang / hay làm» → CHT, chia đều: <b>выбра́сываю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ném RA ngoài ⇒ vứt đi: <b>выбра́сывать му́сор</b> đổ rác. Thêm '
    '<b>-ыва-</b> thì <b>о</b> trong gốc thành <b>а</b> — cùng khuôn <b>спроси́ть</b> → '
    '<b>спра́шивать</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вы́бросить</b> (HT) · <b>бро́сить</b> ném, bỏ · <b>броса́ть</b> ném · '
    '<b>вы́брос</b> sự thải ra</div>'
)

# --------------------------------------------------------------------- выбросить
S["выбросить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы́-</span>'
    '<span class="hd-gloss">RA NGOÀI — ở thể HT luôn mang trọng âm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-брос-ить</span>'
    '<span class="hd-gloss">NÉM — chính là <b>бро́сить</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ném ra ngoài ⇒ vứt bỏ; ném ra khỏi đầu ⇒ quên đi: <b>вы́бросить из '
    'головы́</b>. Ngôi «tôi» <b>с</b> hoá <b>ш</b> như <b>бро́сить</b>: <b>вы́брошу</b>, '
    'còn lại giữ <b>с</b>: <b>вы́бросишь</b>.</div>'
    '<div class="hd-warn">Đừng lẫn <b>вы́брать</b> = chọn ra — gốc khác (<b>брать</b> lấy).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>выбра́сывать</b> (CHT) · <b>бро́сить</b> ném, bỏ · '
    '<b>вы́брос</b> sự thải ra</div>'
)

# --------------------------------------------------------------------- посадить
S["посадить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố thể, KHÔNG mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сад-и́ть</span>'
    '<span class="hd-gloss">gốc NGỒI (biến thể <b>сид-</b>/<b>сед-</b>) — «ĐẶT cho ngồi»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">ĐẶT người vào chỗ ⇒ cho ngồi; đặt cây xuống đất ⇒ trồng (<b>сад</b> '
    'vườn); đặt máy bay xuống ⇒ hạ cánh. Ngôi «tôi» <b>д → ж</b>, trọng âm lùi: '
    '<b>посажу́</b>, <b>поса́дишь</b>.</div>'
    '<div class="hd-warn"><b>Его́ посади́ли.</b> = Hắn bị bỏ tù — nghĩa khẩu ngữ rất hay gặp.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сажа́ть</b> (CHT) · <b>сад</b> vườn · <b>сади́ться</b> ngồi xuống · '
    '<b>поса́дка</b> sự hạ cánh, sự lên tàu</div>'
)

# --------------------------------------------------------------------- сажать
S["сажать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">саж-</span>'
    '<span class="hd-gloss">= <b>сад-</b> NGỒI, <b>д</b> hoá <b>ж</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>сажа́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>посади́ть</b> — chữ <b>ж</b> chính là <b>д</b> đã biến âm, '
    'như <b>посажу́</b>. Cùng các nghĩa: cho ngồi, trồng cây, bỏ tù, hạ cánh.</div>'
    '<div class="hd-warn">Đặt NGƯỜI KHÁC ngồi = <b>сажа́ть</b>; TỰ ngồi xuống = <b>сади́ться</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>посади́ть</b> (HT) · <b>сад</b> vườn · <b>сади́ться</b> ngồi xuống · '
    '<b>са́женец</b> cây giống</div>'
)

# --------------------------------------------------------------------- дрожать
S["дрожать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дрож-</span>'
    '<span class="hd-gloss">RUN — gốc trơn, không chẻ thêm được</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể — nhưng chia lớp 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Run lên vì lạnh, vì sợ: <b>дрожа́ть от хо́лода</b> (<b>от</b> + cách 2 '
    'chỉ nguyên nhân). Đuôi <b>-жать</b> mà chia lớp 2, y như <b>лежа́ть</b>: <b>дрожу́</b>, '
    '<b>дрожи́шь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дрожь</b> cơn run · <b>задрожа́ть</b> run lên (HT) · '
    '<b>дрожа́ние</b> sự rung</div>'
)


# --------------------------------------------------------------------- báo cáo
B = {
    "docbangmat": 116,
    "loitubat": 3,
    "nguonsai": 1,
    "baolen": [
        "Va chạm оплати́ть ⊇ заплати́ть[k95] và опла́чивать ⊇ плати́ть[k95] (đề k95 «thanh toán, trả tiền» nằm gọn trong đề cũ của lô này): gỡ phía mình bằng V — thay «trả tiền» bằng «trả tiền cho» (gloss «to pay for»), thêm «trang trải» (to cover the cost of), опла́чивать thêm «tài trợ» (finance/fund). Không cắt «thanh toán». Máy sẽ xanh, nhưng về NGHĨA hai cặp vẫn chồng nhau thật (đều là «trả tiền»); chỗ khác thật là ngữ pháp (о- nhận thẳng cách 4, за- cần за + cách 4) — đã dạy ở ô đỏ thẻ оплати́ть. Chưa chạy `vacham` (cần Anki) — luồng chính soát lại.",
        "V cần duyệt: оплати́ть, опла́чивать (như trên), дрожа́ть «run, rung, rẩy, lập cập» → «run, run rẩy, rung, lập cập» («rẩy» đứng một mình không phải nghĩa). Các từ khác giữ nguyên đề cũ.",
        "Tự sửa 3 lỗi nội dung: (1) обману́ть chẻ «-ну- hậu tố» — sai, н thuộc gốc ман (обма́н, мани́ть), hậu tố chỉ là -у-; sửa ở cả hai thẻ обману́ть/обма́нывать. (2) рассчи́тывать viết «chỉ thể CHT mang nghĩa trông cậy» — khẳng định quá, hạ thành «nghĩa hay gặp nhất của thể CHT này». (3) пресле́довать: gán cho пре- nghĩa «bám riết» là tự bịa — đổi thành «nghĩa riêng đã mờ», nối -следовать với сле́довать đi theo.",
        "Nguồn sai (không chắc): CACH DUNG của рассчита́ть ghi «рассчитать на что: rely on st» — nghĩa «trông cậy» thuộc vế CHT рассчи́тывать на; vế HT рассчи́тан на thường là «được tính/thiết kế cho». Đã không chép, dạy рассчи́тан на ở thẻ рассчита́ть. Hai lỗi trọng âm взрывча́тка, са́женец là máy bắt, đã sửa theo từ điển (không tính vào loitubat).",
        "Chỗ KHÔNG chắc: целико́м so với пешко́м — cùng là trạng từ rút từ cách 5 của danh từ (це́лик, пешо́к) theo từ nguyên, tôi chỉ ghi «đuôi trạng từ, không mang nghĩa riêng — như пешко́м», không khẳng định từ nguyên. о- ở оплати́ть ghi «PHỦ LÊN đối tượng → nhận thẳng cách 4» là khái quát chức năng (обойти́, осмотре́ть), không phải luật tuyệt đối.",
    ],
}
