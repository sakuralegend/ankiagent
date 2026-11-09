# -*- coding: utf-8 -*-
"""k110 — tu-moi: 5 từ mới user vừa thêm, KHÔNG cùng một trục — soạn từng thẻ độc lập.

Chỗ cần nhất quán trong lô:
(1) кто́-то / отку́да-то: cùng hạt -то «… nào đó (có thật, chỉ là không biết)»; phép
    so -то ↔ -нибудь trải ở кто́-то, thẻ отку́да-то chỉ dẫn chiếu một dòng;
(2) флеш-ка́рта: nghĩa thường gặp là BỘ NHỚ flash (USB, thẻ nhớ); thẻ học từ thì gọi ка́рточки.
Họ hàng cố ý vắng: алло́ (thán từ mượn, không có từ phái sinh Nga).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "алло": "alo",
    "знакомый": "quen thuộc, quen biết",
    "флеш-карта": "USB, thẻ nhớ",
}

# -------------------------------------------------------------------- алло
S["алло"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn từ châu Âu (Pháp <i>allô</i>, Anh <i>hallo</i>) — cùng nguồn với «a lô» của '
    'tiếng Việt. Không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là «alô» của mình, chỉ khác hai chỗ: viết HAI chữ <i>л</i>, và '
    'nhấn ở âm cuối như tiếng Pháp: <b>алло́</b>. Dùng khi nhấc máy, hoặc khi hỏi đầu dây bên '
    'kia còn nghe không: <b>Алло́, ты меня́ слы́шишь?</b></div>'
    '<div class="hd-warn">Chỉ dùng qua ĐIỆN THOẠI. Gặp mặt thì chào <b>приве́т</b> / '
    '<b>здра́вствуйте</b>.</div>'
)

# ---------------------------------------------------------------- знакомый
S["знакомый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">зна-</span>'
    '<span class="hd-gloss">BIẾT — gốc của <b>знать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ком-</span>'
    '<span class="hd-gloss">hậu tố cổ, ngày nay không còn nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đã được BIẾT» ⇒ quen: <b>знако́мое лицо́</b> gương mặt quen. Dạng ngắn '
    'dùng rất nhiều: <b>Мы знако́мы</b> — chúng ta quen nhau rồi.</div>'
    '<div class="hd-warn">Quen AI thì phải có <b>с</b> + cách 5: <b>Я знако́м с ним</b>.</div>'
    '<div class="hd-warn">Đứng một mình làm danh từ = NGƯỜI QUEN: <b>мой знако́мый</b>, '
    '<b>моя́ знако́мая</b> — vẫn biến cách như tính từ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>знать</b> biết · <b>узна́ть</b> biết được, nhận ra · '
    '<b>познако́миться</b> làm quen · <b>знако́мство</b> sự quen biết · '
    '<b>незнако́мый</b> lạ, chưa quen</div>'
)

# ------------------------------------------------------------------ кто-то
S["кто-то"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кто</span>'
    '<span class="hd-gloss">AI (từ hỏi)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-то</span>'
    '<span class="hd-gloss">«… nào đó» — có thật, chỉ là không biết hoặc không nói ra</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gắn <i>-то</i> vào từ hỏi là được «… nào đó»: <b>кто</b> ai → '
    '<b>кто́-то</b> ai đó. Chỉ phần <b>кто</b> biến cách, <i>-то</i> đứng yên: <b>кого́-то</b>, '
    '<b>кому́-то</b>. Động từ đi kèm mặc định ở giống đực số ít: <b>Кто́-то пришёл</b>.</div>'
    '<div class="hd-warn"><b>Кто́-то звони́л</b> = ĐÃ CÓ một người gọi, không biết là ai · '
    '<b>Кто́-нибудь звони́л?</b> = có AI (bất kỳ) gọi không? Hỏi han, nhờ vả thì dùng '
    '<i>-нибудь</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кто</b> ai · <b>никто́</b> không ai · <b>кто́-нибудь</b> bất kỳ ai · '
    '<b>что́-то</b> cái gì đó · <b>где́-то</b> ở đâu đó</div>'
)

# --------------------------------------------------------------- откуда-то
S["откуда-то"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">TỪ, rời khỏi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-куда</span>'
    '<span class="hd-gloss">đi ĐÂU (<b>куда́</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-то</span>'
    '<span class="hd-gloss">«… nào đó», như ở <b>кто́-то</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ba từ hỏi chỗ chốn: <b>где</b> ở đâu · <b>куда́</b> đi đâu · '
    '<b>отку́да</b> từ đâu. Gắn <i>-то</i> vào <b>отку́да</b> là «từ đâu đó»: '
    '<b>Отку́да-то слышна́ му́зыка</b> — từ đâu đó vọng lại tiếng nhạc.</div>'
    '<div class="hd-warn">Trọng âm dời: <b>куда́</b> nhấn cuối, nhưng <b>отку́да</b> nhấn ở '
    '<i>у</i> — <i>-то</i> không đổi gì thêm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отку́да</b> từ đâu · <b>отту́да</b> từ đó · <b>отсю́да</b> từ đây · '
    '<b>куда́-то</b> đi đâu đó · <b>где́-то</b> ở đâu đó</div>'
)

# -------------------------------------------------------------- флеш-карта
S["флеш-карта"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">флеш-</span>'
    '<span class="hd-gloss">mượn Anh <i>flash</i> (bộ nhớ flash), không biến cách</span></div>'
    '<div class="hd-row"><span class="hd-piece">ка́рта</span>'
    '<span class="hd-gloss">THẺ — từ đã học, cũng là «bản đồ»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dịch từng chữ «thẻ flash». Chỉ <b>ка́рта</b> biến cách: <b>на '
    'флеш-ка́рте</b> trên USB. Nói thường thì gọn thành <b>фле́шка</b>.</div>'
    '<div class="hd-warn">Nghĩa thường gặp là THIẾT BỊ nhớ (USB, thẻ nhớ máy ảnh). Thẻ học từ '
    'kiểu Anki thì người Nga hay gọi là <b>ка́рточки</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ка́рта</b> thẻ, bản đồ · <b>ка́рточка</b> tấm thẻ nhỏ · '
    '<b>фле́шка</b> USB (khẩu ngữ)</div>'
)
