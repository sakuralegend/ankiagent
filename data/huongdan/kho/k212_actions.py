# -*- coding: utf-8 -*-
"""k212 — actions: 10 cặp thể + уберечь; trục là GỐC + TIỀN TỐ, và cách thể CHT giãn gốc.

Chỗ cần nhất quán trong lô:
(1) оправдать/оправдывать: прав- THẲNG, ĐÚNG (k93); о- LÀM CHO thành (k131, k175) — об- của облегчить cùng vai.
(2) разглядеть/разглядывать: гляд- NHÌN (k157); раз- TÁCH RA từng phần. Hai vế lệch nghĩa (kết quả / quá trình).
(3) призвать/призывать: зв-/зов-/зыв- GỌI (k112, k122).
(4) завязать/завязывать: -вяз- BUỘC, THẮT (k05, k160); за- ghim cho CHẮC (k85 запоминать).
(5) разорвать/сорвать + CHT: рв-/рыв- XÉ, GIẬT (k161, k195); о đệm trước рв.
(6) приступать/приступить: -ступ- BƯỚC CHÂN (k97).
(7) облегчать/облегчить: лёгк-/легч- NHẸ (k40). (8) стучать: khuôn крик → кричать (k124).
(9) уберечь: берег- GIỮ GÌN, г + ть → чь (k149).
Họ hàng cố ý vắng: không có.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "оправдать": "biện hộ, bào chữa, biện minh, tha bổng, xứng đáng với",      # + acquit
    "оправдывать": "biện hộ, bào chữa, biện minh, tha bổng, xứng đáng với",    # + acquit, live up to
    "призвать": "kêu gọi, hô hào, triệu tập, gọi nhập ngũ",                    # + conscript
    "призывать": "kêu gọi, hô hào, thúc giục, gọi nhập ngũ",                   # + conscript
    "завязать": "buộc, thắt, cột, thiết lập, từ bỏ",                           # + establish, give up
    "завязывать": "buộc, thắt, cột, thiết lập, từ bỏ",                         # + enter into, give up
    "разрывать": "xé, xé nát, cắt đứt, đào bới",                               # + dig up (đồng tự, HT разрыть)
    "сорвать": "xé ra, bóc ra, giật ra, hái, phá hỏng, trút giận",             # + pick, disrupt, vent
    "срывать": "xé bỏ, bóc ra, giật xuống, hái, phá hỏng, trút giận",          # như trên
    "приступать": "bắt tay vào, bắt đầu làm, khởi sự, tiến hành",              # gỡ ⊇ начина́ть[k85]
    "приступить": "bắt tay vào, bắt đầu làm, khởi sự, tiến hành",              # gỡ ⊇ нача́ть[k87]
    "качать": "đung đưa, lắc, ru, bơm, tải xuống",                             # + pump, download; «lắc lư» là nội động
    "покачать": "lắc, lắc đầu, ru một lúc, đung đưa một lúc",                  # + swing for a while
    "облегчать": "làm cho dễ hơn, tạo điều kiện, đơn giản hoá, làm nhẹ bớt, làm dịu",  # + lighten, soothe
}

# ------------------------------------------------------------ оправдать
S["оправдать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span><span class="hd-gloss">LÀM CHO thành… — như <b>освободи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-правд-</span><span class="hd-gloss">ĐÚNG — từ <b>пра́вда</b>, gốc <i>прав-</i> (<b>пра́вый</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span><span class="hd-gloss">đuôi động từ, chia đều: <b>оправда́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm cho việc ấy thành ĐÚNG ⇒ biện minh, bào chữa; toà thấy bị cáo «đúng» ⇒ tha bổng. Cặp CHT: <b>опра́вдывать</b>.</div>'
    '<div class="hd-warn"><b>оправда́ть ожида́ния</b> đáp ứng kỳ vọng · <b>оправда́ть дове́рие</b> xứng đáng với lòng tin.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>опра́вдывать</b> (CHT) · <b>оправда́ние</b> lời bào chữa · <b>пра́вда</b> sự thật · <b>пра́вый</b> đúng</div>'
)

# ------------------------------------------------------------ оправдывать
S["оправдывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span><span class="hd-gloss">LÀM CHO thành…</span></div>'
    '<div class="hd-row"><span class="hd-piece">-правд-</span><span class="hd-gloss">ĐÚNG — từ <b>пра́вда</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-ть</span><span class="hd-gloss">đuôi thể chưa hoàn thành, chia đều: <b>опра́вдываю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>оправда́ть</b>. Thêm <i>-ыва-</i> thì trọng âm lùi về âm ngay trước nó — y như <b>рассказа́ть → расска́зывать</b>.</div>'
    '<div class="hd-warn"><b>Цель опра́вдывает сре́дства.</b> Mục đích biện minh cho phương tiện.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оправда́ть</b> (HT) · <b>опра́вдываться</b> thanh minh cho mình · <b>оправда́ние</b> lời bào chữa · <b>пра́вда</b> sự thật</div>'
)

# ------------------------------------------------------------ разглядеть
S["разглядеть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раз-</span><span class="hd-gloss">TÁCH RA từng phần</span></div>'
    '<div class="hd-row"><span class="hd-piece">-гляд-</span><span class="hd-gloss">NHÌN — <b>гляде́ть</b>, <b>взгляд</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ть</span><span class="hd-gloss">đuôi động từ, chia đuôi <i>-и-</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhìn tới khi các nét TÁCH RA khỏi nhau ⇒ nhìn rõ, nhận ra được. д → ж chỉ ở ngôi «tôi», y như <b>гляжу́</b>: <b>разгляжу́</b>, còn lại <b>разгляди́шь</b>, <b>разглядя́т</b>.</div>'
    '<div class="hd-warn">Vế HT này nói KẾT QUẢ — có nhìn ra được không: <b>не могу́ разгляде́ть</b> tôi không nhìn rõ. Còn <b>разгля́дывать</b> là quá trình ngắm nghía.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>разгля́дывать</b> ngắm nghía · <b>гляде́ть</b> nhìn · <b>взгляд</b> cái nhìn · <b>вы́глядеть</b> trông có vẻ</div>'
)

# ------------------------------------------------------------ разглядывать
S["разглядывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раз-</span><span class="hd-gloss">TÁCH RA từng phần</span></div>'
    '<div class="hd-row"><span class="hd-piece">-гляд-</span><span class="hd-gloss">NHÌN — <b>гляде́ть</b>, <b>взгляд</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-ть</span><span class="hd-gloss">đuôi thể chưa hoàn thành, chia đều: <b>разгля́дываю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đưa mắt qua TỪNG PHẦN một ⇒ ngắm nghía, xem thật kỹ. Đi thẳng với cách 4, không cần <i>на</i>: <b>разгля́дывать карти́ну</b> ngắm kỹ bức tranh.</div>'
    '<div class="hd-warn">Đừng đọc là «đang cố <b>разгляде́ть</b>»: từ này là ngắm kỹ thứ đã thấy; <b>разгляде́ть</b> là nhìn ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>разгляде́ть</b> (HT) nhìn rõ · <b>огля́дываться</b> ngoái nhìn · <b>взгляд</b> cái nhìn · <b>гляде́ть</b> nhìn</div>'
)

# ------------------------------------------------------------ призвать
S["призвать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span><span class="hd-gloss">TỚI, về phía mình — như <b>пригласи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-зв-</span><span class="hd-gloss">GỌI — chính là <b>звать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span><span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gọi người ta TỚI một việc ⇒ kêu gọi: <b>призва́ть к</b> + cách 3, hoặc + nguyên thể. Gọi tới quân ngũ: <b>призва́ть в а́рмию</b>. Cặp CHT: <b>призыва́ть</b>.</div>'
    '<div class="hd-warn">Tương lai lấy thân <i>зов-</i> y như <b>зову́</b>: <b>призову́</b>, <b>призовёшь</b>; quá khứ giống cái nhảy trọng âm: <b>призвала́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>призыва́ть</b> (CHT) · <b>призы́в</b> lời kêu gọi · <b>призва́ние</b> thiên hướng · <b>звать</b> gọi · <b>вы́звать</b> gọi đến</div>'
)

# ------------------------------------------------------------ призывать
S["призывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span><span class="hd-gloss">TỚI, về phía mình</span></div>'
    '<div class="hd-row"><span class="hd-piece">-зыв-</span><span class="hd-gloss">GỌI — gốc <i>зв-/зов-</i> của <b>звать</b>, đổi mặt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span><span class="hd-gloss">đuôi thể chưa hoàn thành, chia đều: <b>призыва́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>призва́ть</b>; mặt gốc <i>-зыв-</i> y hệt <b>называ́ть</b>, <b>вызыва́ть</b>. Gọi ai (cách 4) làm gì (nguyên thể): <b>Призыва́ю вас помо́чь.</b> Tôi kêu gọi các bạn giúp đỡ.</div>'
    '<div class="hd-warn">Kêu gọi ĐIỀU GÌ: <b>к</b> + cách 3 — <b>призыва́ть к ми́ру</b> kêu gọi hoà bình.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>призва́ть</b> (HT) · <b>призы́в</b> lời kêu gọi · <b>призывни́к</b> người đến tuổi nhập ngũ · <b>вызыва́ть</b> gọi đến</div>'
)

# ------------------------------------------------------------ завязать
S["завязать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span><span class="hd-gloss">ghim lại cho CHẮC — như <b>запо́мнить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-вяз-</span><span class="hd-gloss">BUỘC, THẮT — <b>связа́ть</b>, <b>связь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span><span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Buộc lại cho chắc: <b>завяза́ть шнурки́</b>. «Thắt» mối quan hệ ⇒ <b>завяза́ть разгово́р</b> bắt chuyện. Tương lai y <b>связа́ть</b>: з → ж ở MỌI ngôi, trọng âm lùi từ ngôi hai — <b>завяжу́</b>, <b>завя́жешь</b>.</div>'
    '<div class="hd-warn"><b>завяза́ть с</b> + cách 5 (khẩu ngữ) = bỏ hẳn: <b>завяза́ть с куре́нием</b> cai thuốc lá.</div>'
    '<div class="hd-warn">Ở các nghĩa này từ luôn là HT. Có từ khác trùng mặt chữ: <b>завяза́ть</b> (<b>завяза́ю</b>) — CHT, «sa lầy».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>завя́зывать</b> (CHT) · <b>развяза́ть</b> cởi nút · <b>вяза́ть</b> buộc, đan · <b>связь</b> mối liên hệ</div>'
)

# ------------------------------------------------------------ завязывать
S["завязывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span><span class="hd-gloss">ghim lại cho CHẮC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вяз-</span><span class="hd-gloss">BUỘC, THẮT — như <b>свя́зывать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-ть</span><span class="hd-gloss">đuôi thể chưa hoàn thành, chia đều: <b>завя́зываю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>завяза́ть</b>; trọng âm lùi về gốc, ngay trước <i>-ыва-</i>, y như <b>свя́зывать</b>. Dùng cho thói quen, kỹ năng: <b>уме́ть завя́зывать га́лстук</b> biết thắt cà vạt.</div>'
    '<div class="hd-warn"><b>Завя́зывай!</b> (khẩu ngữ) = Thôi ngay đi!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>завяза́ть</b> (HT) · <b>свя́зывать</b> buộc, nối · <b>развя́зывать</b> cởi nút · <b>связь</b> mối liên hệ</div>'
)

# ------------------------------------------------------------ разорвать
S["разорвать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">разо-</span><span class="hd-gloss">= <i>раз-</i> TÁCH RA từng mảnh; thêm <i>о</i> đệm trước <i>рв</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-рв-</span><span class="hd-gloss">XÉ, GIẬT — chính là <b>рвать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span><span class="hd-gloss">đuôi động từ; <i>а</i> rơi khi chia</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Xé cho TÁCH thành mảnh ⇒ xé nát, mạnh hơn <b>порва́ть</b> (làm rách). «Xé» quan hệ ⇒ cắt đứt: <b>разорва́ть отноше́ния</b>. Cặp CHT: <b>разрыва́ть</b>.</div>'
    '<div class="hd-warn">Chia như <b>рвать</b>: <b>разорву́</b>, <b>разорвёшь</b>; quá khứ giống cái nhấn đuôi: <b>разорвала́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>разрыва́ть</b> (CHT) · <b>разры́в</b> chỗ đứt, sự đoạn tuyệt · <b>рвать</b> xé · <b>взорва́ть</b> làm nổ</div>'
)

# ------------------------------------------------------------ разрывать
S["разрывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раз-</span><span class="hd-gloss">TÁCH RA từng mảnh</span></div>'
    '<div class="hd-row"><span class="hd-piece">-рыв-</span><span class="hd-gloss">XÉ, GIẬT — thân dài của <b>рвать</b>, như <b>взрыв</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span><span class="hd-gloss">đuôi thể chưa hoàn thành, chia đều: <b>разрыва́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>разорва́ть</b>. Gốc giãn <i>рв → рыв</i> khi sang CHT, y như <b>взорва́ть → взрыва́ть</b>; hết cụm <i>рв</i> nên khỏi cần <i>о</i> đệm.</div>'
    '<div class="hd-warn">Trùng mặt chữ với từ của gốc <b>рыть</b> ĐÀO: <b>разрыва́ть зе́млю</b> đào bới đất — cặp HT của nó là <b>разры́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>разорва́ть</b> (HT) · <b>разры́в</b> chỗ đứt, sự đoạn tuyệt · <b>взрыв</b> vụ nổ · <b>переры́в</b> giờ nghỉ</div>'
)

# ------------------------------------------------------------ сорвать
S["сорвать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span><span class="hd-gloss">= <i>с-</i> KHỎI bề mặt, từ trên xuống; thêm <i>о</i> đệm trước <i>рв</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-рв-</span><span class="hd-gloss">XÉ, GIẬT — chính là <b>рвать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span><span class="hd-gloss">đuôi động từ; <i>а</i> rơi khi chia: <b>сорву́</b>, <b>сорвёшь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giật KHỎI chỗ đang bám ⇒ giật ra, hái: <b>сорва́ть я́блоко</b>. Giật đổ việc đang chạy ⇒ phá hỏng: <b>сорва́ть уро́к</b>. Quá khứ giống cái nhấn đuôi: <b>сорвала́</b>. Cặp CHT: <b>срыва́ть</b>.</div>'
    '<div class="hd-warn">Trút giận lên AI: <b>на</b> + cách 6 — <b>сорва́ть злость на бра́те</b> trút giận lên em trai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>срыва́ть</b> (CHT) · <b>срыв</b> sự đổ vỡ · <b>рвать</b> xé · <b>разорва́ть</b> xé nát</div>'
)

# ------------------------------------------------------------ срывать
S["срывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span><span class="hd-gloss">KHỎI bề mặt, từ trên xuống — như <b>снять</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-рыв-</span><span class="hd-gloss">XÉ, GIẬT — thân dài của <b>рвать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span><span class="hd-gloss">đuôi thể chưa hoàn thành, chia đều: <b>срыва́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>сорва́ть</b>: gió giật lá khỏi cây — <b>ве́тер срыва́ет ли́стья</b>; làm hỏng kế hoạch — <b>срыва́ть сро́ки</b> làm trễ hạn.</div>'
    '<div class="hd-warn"><b>Не срыва́й на мне зло!</b> Đừng trút giận lên tôi! — <b>на</b> + cách 6.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сорва́ть</b> (HT) · <b>срыв</b> sự đổ vỡ · <b>взрыв</b> vụ nổ · <b>рвать</b> xé</div>'
)

# ------------------------------------------------------------ приступать
S["приступать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span><span class="hd-gloss">TỚI, áp sát vào — như <b>приходи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ступ-</span><span class="hd-gloss">BƯỚC CHÂN — như <b>поступа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span><span class="hd-gloss">đuôi thể chưa hoàn thành, chia đều: <b>приступа́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bước TỚI sát công việc ⇒ bắt tay vào làm. Trang trọng hơn <b>начина́ть</b>, hay gặp ở chỗ làm. Cặp HT: <b>приступи́ть</b>.</div>'
    '<div class="hd-warn">Luôn đi với <b>к</b> + cách 3: <b>приступа́ть к рабо́те</b> — còn <b>начина́ть</b> đi thẳng cách 4: <b>начина́ть рабо́ту</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>приступи́ть</b> (HT) · <b>при́ступ</b> cơn (bệnh, giận) · <b>поступа́ть</b> hành động · <b>вступа́ть</b> gia nhập</div>'
)

# ------------------------------------------------------------ приступить
S["приступить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span><span class="hd-gloss">TỚI, áp sát vào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ступ-</span><span class="hd-gloss">BƯỚC CHÂN — như <b>вступи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span><span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp HT của <b>приступа́ть</b>: bước tới một lần ⇒ bắt tay vào — <b>Присту́пим?</b> Ta bắt đầu nhé? Đòi <b>к</b> + cách 3.</div>'
    '<div class="hd-warn">Ngôi «tôi» chèn л và nhấn đuôi: <b>приступлю́</b>; các ngôi khác trọng âm lùi vào thân: <b>присту́пишь</b>, <b>присту́пят</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>приступа́ть</b> (CHT) · <b>при́ступ</b> cơn (bệnh, giận) · <b>вступи́ть</b> gia nhập · <b>поступи́ть</b> nhập học; hành động</div>'
)

# ------------------------------------------------------------ качать
S["качать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кач-</span><span class="hd-gloss">ĐU ĐƯA, đưa qua đưa lại</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span><span class="hd-gloss">đuôi động từ, chia đều: <b>кача́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đưa qua đưa lại ⇒ lắc, ru: <b>кача́ть ребёнка</b>. Cần bơm cũng đưa lên đưa xuống ⇒ bơm: <b>кача́ть во́ду</b>; «bơm» dữ liệu về máy ⇒ tải xuống. Không dính gì tới <b>ка́чество</b> (từ <b>как</b>).</div>'
    '<div class="hd-warn">Cặp HT tuỳ nghĩa: lắc → <b>покача́ть</b>; tải về → <b>скача́ть</b>.</div>'
    '<div class="hd-warn"><b>кача́ть голово́й</b> lắc đầu — cái bị lắc ở cách 5.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кача́ться</b> đung đưa · <b>каче́ли</b> cái xích đu · <b>скача́ть</b> tải về</div>'
)

# ------------------------------------------------------------ покачать
S["покачать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span><span class="hd-gloss">MỘT LÚC, một ít — như <b>поговори́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-кач-</span><span class="hd-gloss">ĐU ĐƯA, đưa qua đưa lại</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span><span class="hd-gloss">đuôi động từ, chia đều: <b>покача́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đưa qua đưa lại MỘT LÚC rồi thôi: ru bé một lúc, lắc đầu vài cái. Cặp HT của <b>кача́ть</b> ở nghĩa lắc, ru.</div>'
    '<div class="hd-warn">Gặp nhiều nhất: <b>покача́ть голово́й</b> (cách 5) lắc đầu — tỏ ý không đồng tình, ái ngại.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кача́ть</b> (CHT) · <b>кача́ться</b> đung đưa · <b>каче́ли</b> cái xích đu</div>'
)

# ------------------------------------------------------------ облегчать
S["облегчать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span><span class="hd-gloss">LÀM CHO thành… — cùng vai <i>о-</i> của <b>освободи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-легч-</span><span class="hd-gloss">NHẸ — <b>лёгкий</b>, к → ч như <b>ле́гче</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span><span class="hd-gloss">đuôi thể chưa hoàn thành, chia đều: <b>облегча́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm cho NHẸ — <b>лёгкий</b> vừa là nhẹ vừa là dễ, nên động từ cũng hai hướng: làm cho dễ hơn (<b>облегча́ть рабо́ту</b>) và làm dịu (<b>облегча́ть боль</b>).</div>'
    '<div class="hd-warn">Chỉ lệch một âm tiết là đổi thể: <b>облегча́ют</b> họ đang làm nhẹ (CHT) · <b>облегча́т</b> họ sẽ làm nhẹ (<b>облегчи́ть</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>облегчи́ть</b> (HT) · <b>облегче́ние</b> sự nhẹ nhõm · <b>лёгкий</b> nhẹ, dễ · <b>ле́гче</b> nhẹ hơn, dễ hơn</div>'
)

# ------------------------------------------------------------ облегчить
S["облегчить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span><span class="hd-gloss">LÀM CHO thành…</span></div>'
    '<div class="hd-row"><span class="hd-piece">-легч-</span><span class="hd-gloss">NHẸ — <b>лёгкий</b>, к → ч như <b>ле́гче</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span><span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp HT của <b>облегча́ть</b>: làm cho nhẹ hơn, dễ hơn, xong một lần. Chữ <i>ё</i> của <b>лёгкий</b> mất trọng âm nên về <i>е</i>.</div>'
    '<div class="hd-warn">Nhấn ở đuôi suốt bảng: <b>облегчи́ть</b>, <b>облегчу́</b>, <b>облегчи́шь</b> — người Nga cũng hay nhấn nhầm vào <i>е</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>облегча́ть</b> (CHT) · <b>облегче́ние</b> sự nhẹ nhõm · <b>лёгкий</b> nhẹ, dễ · <b>легко́</b> dễ dàng</div>'
)

# ------------------------------------------------------------ постучать
S["постучать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span><span class="hd-gloss">MỘT LÚC, vài cái</span></div>'
    '<div class="hd-row"><span class="hd-piece">-стуч-</span><span class="hd-gloss">= <b>стук</b> TIẾNG GÕ, biến âm к → ч</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span><span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gõ vài cái rồi thôi: <b>Постучи́ ещё раз.</b> Gõ lần nữa đi. Đuôi <i>-ать</i> nhưng chia lớp HAI: <b>постучу́</b>, <b>постучи́шь</b>, <b>постуча́т</b>. Cặp CHT: <b>стуча́ть</b>.</div>'
    '<div class="hd-warn">Gõ cửa: <b>в</b> + cách 4 — <b>постуча́ть в дверь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>стуча́ть</b> (CHT) · <b>стук</b> tiếng gõ · <b>сту́кнуть</b> gõ một cái</div>'
)

# ------------------------------------------------------------ стучать
S["стучать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">стуч-</span><span class="hd-gloss">= <b>стук</b> TIẾNG GÕ, biến âm к → ч</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span><span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Phát ra tiếng gõ» ⇒ gõ, đập. Y khuôn <b>крик → крича́ть</b>, cũng chia lớp HAI: <b>стучу́</b>, <b>стучи́шь</b>, <b>стуча́т</b>. Răng va lập cập cũng dùng từ này: <b>зу́бы стуча́т</b>.</div>'
    '<div class="hd-warn">Gõ cửa, cửa sổ → <b>в</b> + cách 4: <b>стуча́ть в окно́</b>. Gõ lên mặt vật → <b>по</b> + cách 3: <b>стуча́ть по столу́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>постуча́ть</b> (HT) · <b>стук</b> tiếng gõ · <b>сту́кнуть</b> gõ một cái</div>'
)

# ------------------------------------------------------------ уберечь
S["уберечь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span><span class="hd-gloss">tới đích, làm được TRỌN — như <b>успе́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-бере́чь</span><span class="hd-gloss">GIỮ GÌN — chính là <b>бере́чь</b>; г + ть → чь</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giữ được TRỌN, không để hại tới ⇒ che chở, bảo vệ. Chia y <b>бере́чь</b>: <b>уберегу́</b>, <b>убережёшь</b>, <b>уберегу́т</b>; quá khứ <b>уберёг</b>, <b>уберегла́</b>.</div>'
    '<div class="hd-warn">Giữ ai KHỎI cái gì: cách 4 + <b>от</b> + cách 2 — <b>убере́чь сы́на от опа́сности</b> giữ con khỏi nguy hiểm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бере́чь</b> (CHT) · <b>сбере́чь</b> giữ được, để dành · <b>бе́режный</b> nâng niu</div>'
)

B = {
    "docbangmat": 139,
    "loitubat": 3,
    "nguonsai": 4,
    "baolen": [
        "Va chạm приступа́ть/приступи́ть ⊇ начина́ть[k85]/нача́ть[k87] «bắt đầu»: gỡ phía mình bằng V «bắt tay vào, bắt đầu làm, khởi sự, tiến hành» (nghĩa chính giữ nguyên dưới dạng «bắt đầu làm»). Đã chạy thử do_va_cham (chỉ đọc Anki) với V mới: 0 va chạm dính từ của lô.",
        "Badge SAI trên thẻ завяза́ть: in BI-ASP, vì OpenRussian gộp завяза́ть (завяжу́, HT, buộc) với từ đồng tự завяза́ть (завяза́ю, CHT của завя́знуть, sa lầy). Thẻ này dạy từ «buộc», đúng ra phải PERF. Lô không sửa được badge, đã ghi ô đỏ; cần luồng chính/user quyết định sửa GrammarJSON/AspectBadge (завя́знуть cũng không phải cặp của nghĩa «buộc»).",
        "GrammarJSON призва́ть ghi quá khứ «призва́ла» — chuẩn là призвала́ (như звала́, назвала́). Ô Hướng dẫn viết призвала́; bảng chia trên thẻ vẫn sai, cần sửa dữ liệu thẻ.",
        "V cần duyệt (14 thẻ): оправда́ть/опра́вдывать «biện hộ, bào chữa, biện minh, tha bổng, xứng đáng với»; призва́ть/призыва́ть + «gọi nhập ngũ»; завяза́ть/завя́зывать + «thiết lập, từ bỏ» (không thêm «bắt đầu» trần vì sẽ đẻ va chạm mới với начина́ть); разрыва́ть + «đào bới» (đồng tự, HT разры́ть); сорва́ть/срыва́ть + «hái, phá hỏng, trút giận»; приступа́ть/приступи́ть như trên; кача́ть «đung đưa, lắc, ru, bơm, tải xuống»; покача́ть + «đung đưa một lúc»; облегча́ть + «làm nhẹ bớt, làm dịu». 7 thẻ còn lại giữ đề cũ.",
        "Nguồn sai đã bác (4): badge/cặp BI-ASP + завя́знуть của завяза́ть; призва́ла; кача́ть «lắc lư», «đẩy đưa» (không khớp to rock/swing ngoại động); gloss «get stuck / sink in / bogged down» của завяза́ть là của từ đồng tự nên không đưa vào V.",
        "Chỗ KHÔNG chắc: (1) sắc thái «кача́ть bơm ← cần bơm đưa lên đưa xuống» là lối giải thích hình ảnh. (2) за- của завяза́ть giải là «ghim cho chắc» theo khuôn запо́мнить k85/k88, nghĩa tiền tố hơi mờ. (3) у- của убере́чь giải theo khuôn успе́ть k116 «tới đích, trọn».",
        "Bỏ nghĩa lóng «tố giác» (snitch) của стуча́ть và nghĩa cổ «tới gần / gặng hỏi» của приступа́ть/приступи́ть khỏi V theo luật chỉ nghĩa thông dụng.",
    ],
}
