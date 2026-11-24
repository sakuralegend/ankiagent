# -*- coding: utf-8 -*-
"""k171 — actions: 9 cặp/nhóm động từ hành động + danh từ дра́ка gom họ.

Chỗ cần nhất quán trong lô:
(1) hậu tố -ну- MỘT LẦN: кивну́ть và рискну́ть giải thích cùng một câu.
(2) gốc пуск-/пуст- THẢ, BUÔNG — отпуска́ть/отпусти́ть, khớp о́тпуск (k69), пусть (k80).
(3) gốc след- DẤU VẾT — следи́ть/последи́ть, khớp после́дний (k109), сле́дующий (k75).
    Máy ghép по́сле/посла́ть = báo oan, không dùng.
(4) gốc крад- — красть/укра́сть: д+т → ст. Máy ghép кра́сный/краси́вый/расти́ = báo oan;
    кра́сный còn được đưa vào ô đỏ như một bẫy mặt chữ. вор (k163) khác gốc.
(5) gốc прав- THẲNG, ĐÚNG — управля́ть, đúng khuôn управле́ние (k151).
(6) gốc дра-/дер- XÉ, GIẬT (драть) — дра́ться/подра́ться/дра́ка cùng một câu. Báo oan подро́сток/подру́га.
(7) gốc забот- — позабо́титься, khớp забо́титься (k129).
(8) gốc един- MỘT — присоедини́ться/присоединя́ться, khớp еди́ный (k123).
(9) со- + стоя- — состоя́ться, khớp состоя́ть (k123).
Họ hàng: không thẻ nào vắng.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "красть": "ăn cắp, trộm, đánh cắp",                                    # đề cũ nằm gọn trong воровать (k207)
    "рискнуть": "liều, mạo hiểm",                                          # bỏ «một lần» — nhãn thể trá hình
    "отпускать": "thả, buông, cho đi, cho nghỉ, để râu",                   # thiếu let go / time off / grow a beard
    "отпустить": "thả ra, buông, cho đi, cho nghỉ, để râu",                # cùng bộ với cặp thể; badge tách
    "последить": "trông, trông chừng, để mắt tới",                         # bỏ «giúp một lúc» — lời dùng
    "следить": "theo dõi, để ý, giám sát, trông chừng",                    # thiếu monitor / keep an eye on
    "управлять": "quản lý, điều hành, điều khiển, lái, cai trị",           # gỡ va chạm руководи́ть: control/drive/govern
    "присоединяться": "tham gia, gia nhập, nhập cùng, tán thành, được nối vào",  # side with / be attached
}

# --------------------------------------------------------------------- кивать
S["кивать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кив-</span>'
    '<span class="hd-gloss">GẬT (gốc trơn)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gật đầu — đang gật, hay gật nhiều lần. Gật VỚI AI → cách 3: '
    '<b>кива́ть ему́</b>; gật cái gì → cách 5: <b>кива́ть голово́й</b>. Chia đều: <b>кива́ю</b>. '
    'Cặp HT: <b>кивну́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кивну́ть</b> gật một cái (HT) · <b>киво́к</b> cái gật đầu</div>'
)

# --------------------------------------------------------------------- кивнуть
S["кивнуть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кив-</span>'
    '<span class="hd-gloss">GẬT</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ну́-ть</span>'
    '<span class="hd-gloss">hậu tố MỘT LẦN — một động tác chớp nhoáng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>-ну-</b> biến hành động thành MỘT cú: <b>кива́ть</b> gật → '
    '<b>кивну́ть</b> gật một cái. Cùng khuôn: <b>рискну́ть</b> trong lô này, <b>кри́кнуть</b> hét '
    'một tiếng, <b>пры́гнуть</b> nhảy một cái. Tương lai: <b>кивну́, кивнёшь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кива́ть</b> gật đầu (CHT) · <b>киво́к</b> cái gật đầu</div>'
)

# --------------------------------------------------------------------- вытаскивать
S["вытаскивать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span>'
    '<span class="hd-gloss">RA NGOÀI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-таск-</span>'
    '<span class="hd-gloss">KÉO LÊ — như <b>таска́ть</b>, <b>тащи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Kéo lê RA NGOÀI ⇒ lôi ra, kéo ra thứ nặng hoặc bị kẹt: '
    '<b>выта́скивать ве́щи из маши́ны</b> lôi đồ ra khỏi xe. Chia đều: <b>выта́скиваю</b>. '
    'Cặp HT: <b>вы́тащить</b> — ở đó <b>вы́</b> mới nhận trọng âm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вы́тащить</b> lôi ra (HT) · <b>тащи́ть</b> kéo lê · '
    '<b>таска́ть</b> kéo đi kéo lại</div>'
)

# --------------------------------------------------------------------- вытащить
S["вытащить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы́-</span>'
    '<span class="hd-gloss">RA NGOÀI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тащ-ить</span>'
    '<span class="hd-gloss">KÉO LÊ — như <b>тащи́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Kéo RA khỏi chỗ: <b>вы́тащить ры́бу из воды́</b> kéo cá lên khỏi nước. '
    'Cặp CHT: <b>выта́скивать</b>.</div>'
    '<div class="hd-warn">Luật suy ra được: động từ HT có <b>вы-</b> thì trọng âm LUÔN nằm ở '
    '<b>вы́</b>, mọi dạng: <b>вы́тащу, вы́тащишь, вы́тащил</b>. Sang CHT thì <b>вы-</b> thường mất nhấn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>выта́скивать</b> lôi ra (CHT) · <b>тащи́ть</b> kéo lê · '
    '<b>таска́ть</b> kéo đi kéo lại</div>'
)

# --------------------------------------------------------------------- рискнуть
S["рискнуть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">риск-</span>'
    '<span class="hd-gloss">RỦI RO — chính là <b>риск</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ну́-ть</span>'
    '<span class="hd-gloss">hậu tố MỘT LẦN, như <b>кивну́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Liều MỘT phen. Đi với nguyên thể = đánh liều làm gì: '
    '<b>Я рискну́ спроси́ть</b> tôi liều hỏi thử. Tương lai: <b>рискну́, рискнёшь</b>. '
    'Cặp CHT: <b>рискова́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>риск</b> rủi ro · <b>рискова́ть</b> mạo hiểm (CHT) · '
    '<b>риско́ванный</b> liều lĩnh</div>'
)

# --------------------------------------------------------------------- рисковать
S["рисковать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">риск-</span>'
    '<span class="hd-gloss">RỦI RO — từ mượn, như tiếng Anh <i>risk</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова́ть</span>'
    '<span class="hd-gloss">đuôi biến danh từ thành động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chấp nhận rủi ro ⇒ mạo hiểm, liều. <b>-ова-</b> thành <b>-у-</b> ở hiện tại: '
    '<b>риску́ю, риску́ешь</b>. Cặp HT: <b>рискну́ть</b>.</div>'
    '<div class="hd-warn">Liều MẤT cái gì → cách 5, không phải cách 4: <b>рискова́ть жи́знью</b> '
    'liều mạng. Tục ngữ: <b>Кто не риску́ет, тот не пьёт шампа́нского</b> — không liều thì '
    'chẳng có sâm-panh mà uống.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>риск</b> rủi ro · <b>рискну́ть</b> liều (HT) · '
    '<b>риско́ванный</b> liều lĩnh</div>'
)

# --------------------------------------------------------------------- отпускать
S["отпускать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">RỜI RA, TÁCH KHỎI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пуск-</span>'
    '<span class="hd-gloss">THẢ, BUÔNG (của <b>пусти́ть</b> thả ra)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thả cho RỜI ra ⇒ buông tay, thả đi, cho về: <b>отпуска́ть дете́й гуля́ть</b> '
    'cho trẻ đi chơi. Gốc <b>-пуск-</b> này chính là cái làm ra <b>о́тпуск</b> nghỉ phép — được thả '
    'khỏi chỗ làm. Chia đều: <b>отпуска́ю</b>. Cặp HT: <b>отпусти́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отпусти́ть</b> thả ra (HT) · <b>о́тпуск</b> nghỉ phép · '
    '<b>пуска́ть</b> thả, cho vào · <b>пропуска́ть</b> cho qua, bỏ lỡ</div>'
)

# --------------------------------------------------------------------- отпустить
S["отпустить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">RỜI RA, TÁCH KHỎI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пуст-и́ть</span>'
    '<span class="hd-gloss">THẢ, BUÔNG — như <b>пусти́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thả cho rời đi ⇒ thả ra, buông, cho về, cho nghỉ. Ngôi «tôi» đổi '
    '<b>ст → щ</b>: <b>отпущу́</b>; các ngôi khác lùi nhấn về gốc: <b>отпу́стишь, отпу́стят</b>. '
    'Cặp CHT: <b>отпуска́ть</b>.</div>'
    '<div class="hd-warn"><b>отпусти́ть бо́роду</b> = để râu (thả cho mọc) · '
    '<b>Боль отпусти́ла</b> = cơn đau dịu đi (nó «buông» mình ra).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отпуска́ть</b> thả (CHT) · <b>пусти́ть</b> thả, cho vào · '
    '<b>о́тпуск</b> nghỉ phép · <b>пусть</b> cứ để — vốn là mệnh lệnh cũ của <b>пусти́ть</b></div>'
)

# --------------------------------------------------------------------- следить
S["следить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">след-</span>'
    '<span class="hd-gloss">DẤU VẾT — chính là <b>след</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bám theo dấu vết ⇒ theo dõi, để mắt, trông nom. Ngôi «tôi» đổi '
    '<b>д → ж</b>: <b>слежу́</b>, các ngôi khác giữ <b>д</b>: <b>следи́шь</b>.</div>'
    '<div class="hd-warn">Theo dõi AI/CÁI GÌ → <b>за</b> + cách 5: <b>следи́ть за ребёнком</b> trông '
    'đứa bé · <b>следи́ть за собо́й</b> chăm chút bản thân.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>след</b> dấu vết · <b>сле́дующий</b> tiếp theo · '
    '<b>после́дний</b> cuối cùng · <b>иссле́довать</b> nghiên cứu · <b>сле́жка</b> sự bám đuôi</div>'
)

# --------------------------------------------------------------------- последить
S["последить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">MỘT LÚC — làm một chập rồi thôi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-след-и́ть</span>'
    '<span class="hd-gloss">THEO DẤU VẾT — như <b>следи́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Theo dõi một chập ⇒ trông giúp một lúc. Cùng khuôn <b>по-</b> «một lát»: '
    '<b>погуля́ть</b> đi dạo một lát, <b>поговори́ть</b> nói chuyện một lúc. Tương lai: '
    '<b>послежу́, последи́шь</b>.</div>'
    '<div class="hd-warn">Vẫn <b>за</b> + cách 5 như <b>следи́ть</b>: <b>Последи́ за мои́ми '
    'веща́ми!</b> Trông đồ giúp tôi nhé!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>следи́ть</b> theo dõi · <b>след</b> dấu vết · '
    '<b>после́дний</b> cuối cùng</div>'
)

# --------------------------------------------------------------------- красть
S["красть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">крад-</span>'
    '<span class="hd-gloss">ĂN TRỘM — gốc thật, <b>д</b> lộ ra ở hiện tại</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>д + т → ст</b>: <b>крад-ть → красть</b>, y như <b>класть → кладу́</b>. '
    'Hiện tại lộ <b>д</b>: <b>краду́, крадёшь</b>. Quá khứ <b>д</b> rụng trước <b>л</b>: '
    '<b>крал, кра́ла</b>. Cặp HT: <b>укра́сть</b>.</div>'
    '<div class="hd-warn">Bẫy mặt chữ: <b>кра́сный</b>, <b>краси́вый</b> KHÔNG cùng gốc — '
    'gốc của <b>красть</b> là <b>крад-</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>укра́сть</b> ăn cắp (HT) · <b>кра́жа</b> vụ trộm (<b>д → ж</b>) · '
    '<b>кра́сться</b> rón rén, lén đi</div>'
)

# --------------------------------------------------------------------- украсть
S["украсть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố hoàn thành, ở đây gần như không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-крад-ть</span>'
    '<span class="hd-gloss">ĂN TRỘM — như <b>красть</b> (д + т → ст)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chia y như <b>красть</b>: <b>украду́, украдёшь</b>; quá khứ <b>укра́л, '
    'укра́ла</b>. Kẻ trộm lại là <b>вор</b> — khác gốc. Cặp CHT: <b>красть</b>.</div>'
    '<div class="hd-warn">Trộm CỦA AI → <b>у</b> + cách 2. Câu hay gặp nhất: <b>У меня́ укра́ли '
    'телефо́н</b> = tôi bị trộm mất điện thoại (ngôi 3 số nhiều, không chủ ngữ = «bị»).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>красть</b> ăn cắp (CHT) · <b>кра́жа</b> vụ trộm · '
    '<b>кра́сться</b> rón rén, lén đi</div>'
)

# --------------------------------------------------------------------- управлять
S["управлять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố, nghĩa riêng đã mờ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-прав-</span>'
    '<span class="hd-gloss">THẲNG, ĐÚNG → <b>пра́вить</b> điều khiển cho đúng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-л-я́ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành, <b>л</b> chèn sau <b>в</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giữ cho mọi thứ chạy ĐÚNG hướng ⇒ quản lý, điều hành, lái, điều khiển. '
    'Chia đều: <b>управля́ю</b>. Chỉ có thể chưa hoàn thành.</div>'
    '<div class="hd-warn">Đòi cách 5, không phải cách 4: <b>управля́ть страно́й</b> cai trị đất '
    'nước · <b>управля́ть маши́ной</b> lái xe.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>управле́ние</b> sự quản lý · <b>пра́вить</b> cai trị, sửa bài · '
    '<b>прави́тельство</b> chính phủ · <b>пра́вило</b> quy tắc</div>'
)

# --------------------------------------------------------------------- драться
S["драться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дра- / дер-</span>'
    '<span class="hd-gloss">XÉ, GIẬT — gốc của <b>драть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть-ся</span>'
    '<span class="hd-gloss">đuôi + <b>-ся</b> «lẫn nhau»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Giằng xé lẫn nhau» ⇒ đánh nhau; với ai → <b>с</b> + cách 5. Hiện tại lộ thân '
    '<b>дер-</b>: <b>деру́сь, дерёшься</b> — cùng khuôn <b>брать → беру́</b>. Quá khứ giống cái '
    'nhấn đuôi: <b>драла́сь</b>. Cặp HT: <b>подра́ться</b>.</div>'
    '<div class="hd-warn">Chỉ đánh bằng tay chân. Cãi nhau bằng lời là <b>руга́ться</b> / '
    '<b>спо́рить</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дра́ка</b> vụ đánh nhau · <b>подра́ться</b> đánh nhau (HT) · '
    '<b>драть</b> xé, giật · <b>удра́ть</b> chuồn mất</div>'
)

# --------------------------------------------------------------------- подраться
S["подраться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố hoàn thành, không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дра-ть-ся</span>'
    '<span class="hd-gloss">XÉ, GIẬT lẫn nhau — như <b>дра́ться</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đánh nhau một trận trọn vẹn; với ai → <b>с</b> + cách 5. Chia y như '
    '<b>дра́ться</b>: <b>подеру́сь, подерёшься</b>; quá khứ giống cái <b>подрала́сь</b>. '
    'Cặp CHT: <b>дра́ться</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дра́ться</b> đánh nhau (CHT) · <b>дра́ка</b> vụ đánh nhau · '
    '<b>драть</b> xé, giật</div>'
)

# --------------------------------------------------------------------- драка
S["драка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дра-</span>'
    '<span class="hd-gloss">XÉ, GIẬT — như <b>дра́ться</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">đuôi danh từ, giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>дра́ться</b>: cuộc đánh nhau, vụ ẩu đả bằng tay chân.</div>'
    '<div class="hd-warn"><b>лезть в дра́ку</b> = lao vào đánh nhau, gây sự.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дра́ться</b> đánh nhau · <b>подра́ться</b> đánh nhau (HT) · '
    '<b>драть</b> xé, giật</div>'
)

# --------------------------------------------------------------------- позаботиться
S["позаботиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố hoàn thành</span></div>'
    '<div class="hd-row"><span class="hd-piece">-забо́т-</span>'
    '<span class="hd-gloss">SỰ CHĂM LO — chính là <b>забо́та</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить-ся</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2 + <b>-ся</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bản HT của <b>забо́титься</b>: lo liệu xong một việc. Ngôi «tôi» đổi '
    '<b>т → ч</b>: <b>позабо́чусь</b>, còn lại giữ <b>т</b>: <b>позабо́тишься</b>.</div>'
    '<div class="hd-warn">Lo CHO AI/CÁI GÌ → <b>о</b> + cách 6: <b>Я позабо́чусь о биле́тах</b> = '
    'tôi sẽ lo vụ vé.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>забо́титься</b> chăm lo (CHT) · <b>забо́та</b> sự chăm lo · '
    '<b>забо́тливый</b> chu đáo</div>'
)

# --------------------------------------------------------------------- присоединиться
S["присоединиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">SÁT VÀO, THÊM VÀO</span></div>'
    '<div class="hd-row"><span class="hd-piece">-со-</span>'
    '<span class="hd-gloss">CÙNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-еди́н-</span>'
    '<span class="hd-gloss">MỘT — dạng cổ của <b>оди́н</b>, như <b>еди́ный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть-ся</span>'
    '<span class="hd-gloss">đuôi + <b>-ся</b> (gắn chính mình)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gắn mình VÀO để CÙNG thành MỘT ⇒ tham gia, gia nhập. Tương lai: '
    '<b>присоединю́сь, присоедини́шься</b>. Cặp CHT: <b>присоединя́ться</b>.</div>'
    '<div class="hd-warn">Nhập vào AI/CÁI GÌ → <b>к</b> + cách 3: <b>Присоедини́тесь к нам!</b> = '
    'Tham gia cùng chúng tôi nhé!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>соедини́ть</b> nối lại · <b>объедини́ть</b> hợp nhất · '
    '<b>еди́ный</b> thống nhất · <b>Соединённые Шта́ты</b> Hoa Kỳ</div>'
)

# --------------------------------------------------------------------- присоединяться
S["присоединяться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-со-</span>'
    '<span class="hd-gloss">SÁT VÀO + CÙNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-еди́н-</span>'
    '<span class="hd-gloss">MỘT — như <b>еди́ный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́ть-ся</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành + <b>-ся</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng hình ảnh với <b>присоедини́ться</b>: <b>-и́ть → -я́ть</b> là đổi sang '
    'CHT, chia đều: <b>присоединя́юсь</b>. Vẫn <b>к</b> + cách 3, và còn nghĩa tán thành: '
    '<b>Присоединя́юсь к ва́шему мне́нию</b> tôi đồng ý với ý kiến của anh.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>присоедини́ться</b> tham gia (HT) · <b>соедини́ть</b> nối lại · '
    '<b>еди́ный</b> thống nhất · <b>оди́н</b> một</div>'
)

# --------------------------------------------------------------------- состояться
S["состояться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">CÙNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-стоя-</span>'
    '<span class="hd-gloss">ĐỨNG — gốc của <b>стоя́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть-ся</span>'
    '<span class="hd-gloss">đuôi + <b>-ся</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mọi phần đứng vào chỗ cùng nhau ⇒ sự kiện thành hình, diễn ra. Gần như chỉ '
    'dùng ngôi 3: <b>Конце́рт состои́тся за́втра</b>. Quá khứ: <b>состоя́лся</b>.</div>'
    '<div class="hd-warn"><b>состои́тся</b> trông như hiện tại nhưng là TƯƠNG LAI (từ HT): «sẽ diễn '
    'ra». Bỏ <b>-ся</b> là ra từ khác: <b>состоя́ть</b> = gồm có.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>состоя́ть</b> gồm có · <b>состоя́ние</b> trạng thái · '
    '<b>стоя́ть</b> đứng</div>'
)

B = {
    "docbangmat": 122,
    "loitubat": 1,
    "nguonsai": 0,
    "baolen": [
        "Tự sửa 1 lỗi: thẻ вы́тащить viết «sang CHT thì вы- mất nhấn» — sai với вы́глядеть (CHT vẫn nhấn вы́); đã hạ thành «thường mất nhấn».",
        "Va chạm управля́ть ⊂ руководи́ть[k137]: gỡ phía mình bằng nghĩa có thật trong gloss (control/drive/steer/govern/rule) → «quản lý, điều hành, điều khiển, lái, cai trị». Chưa chạy được `vacham` (cần Anki) — luồng chính soát lại.",
        "Ngoặc của user giữ nguyên, KHÔNG viết V: кивну́ть «gật đầu (một cái)», подра́ться «đánh nhau (một trận)».",
        "V cần duyệt: рискну́ть (bỏ «một lần» — nhãn thể trá hình), отпуска́ть/отпусти́ть (+buông, cho nghỉ, để râu), последи́ть (bỏ «giúp một lúc»), следи́ть (+giám sát, trông chừng), присоединя́ться (+tán thành, được nối vào).",
        "Không chắc (đã nói mềm trên thẻ): дра́ться ← драть «xé, giật» là nối hình thái, không ghi Mức tin; у- trong укра́сть ghi «gần như không mang nghĩa riêng» thay vì đoán nghĩa «mang đi».",
        "Báo oan của máy đã bỏ: следи́ть↔по́сле/посла́ть, красть↔кра́сный/краси́вый/расти́ (кра́сный dùng làm ô đỏ bẫy mặt chữ), подра́ться↔подро́сток/подру́га.",
    ],
}
