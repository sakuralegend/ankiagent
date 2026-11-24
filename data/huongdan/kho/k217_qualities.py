# -*- coding: utf-8 -*-
"""k217 — qualities (lô trộn): ba cặp thể, tính từ phẩm chất/chất liệu, sắt thép.

Chỗ cần nhất quán trong lô:
(1) -ра- gốc Slav cổ ↔ -оро- Nga: кра́ткий/коро́ткий và драг-/дорог- — hai thẻ nhắc nhau.
(2) -пас- CHE CHỞ giữ lời thẻ спаса́ть/спасти́; -гад- ĐOÁN giữ lời зага́дка; -крат- NGẮN giữ lời сократи́ть.
(3) кас-/кос- giữ lời каса́ться/косну́ться; điểm mới: прикаса́ться đòi к + C3 (каса́ться đòi C2).
(4) Dạng ngắn giống đực chen е của nhóm -ный/-льный: mỗi thẻ một câu, không dựng khối chung.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "ускорить": "đẩy nhanh, tăng tốc, làm nhanh hơn",             # cặp thể: cùng một dãy
    "ускорять": "đẩy nhanh, tăng tốc, làm nhanh hơn",
    "спасаться": "tự cứu mình, thoát thân, lánh",                 # cặp thể: cùng một dãy
    "спастись": "tự cứu mình, thoát thân, lánh",                  # «sống sót» = вы́жить; «được» là việc của badge thể
    "ширина": "chiều rộng, bề rộng",                              # «khổ rộng» lủng củng, trùng ý
    "автоматически": "tự động",                                   # «một cách» lặp badge adv; «theo quán tính» gloss không có
    "скользкий": "trơn, trơn trượt",                              # «nhẵn trượt» vô nghĩa; nhẵn = гла́дкий
    "краткий": "ngắn gọn, vắn tắt, súc tích, ngắn ngủi",          # thêm gloss short-lived
    "стальной": "bằng thép, cứng như thép",                       # steely; «cứng rắn» rộng quá
    "фальшивый": "giả, giả mạo, giả tạo, lạc điệu",               # forged · insincere · off-key; «làm giả» là động từ
    "громадный": "khổng lồ, to tướng",                            # gỡ bao trùm огро́мный (khổng lồ, to lớn)
    "старомодный": "lỗi mốt, lỗi thời, cổ lỗ",                    # «cũ kiểu» ngược trật tự; nghĩa gốc là lỗi MỐT
    "драгоценный": "quý giá, quý báu",                            # «đá quý» là danh từ (драгоце́нный ка́мень)
    "стандартный": "tiêu chuẩn, thông thường",                    # «bình thường» = обы́чный/норма́льный
    "формальный": "hình thức, mang tính thủ tục",                 # bỏ «chính thức»: gỡ va chạm официа́льный
    "универсальный": "vạn năng, đa năng, phổ quát",               # «dùng chung» = о́бщий
    "благотворительный": "từ thiện, gây quỹ",                     # «nhân đạo» = гуманита́рный
}

# ------------------------------------------------------------------- ускорить
S["ускорить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">LÀM CHO thành ra thế — như <b>укрепи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-скор-</span>'
    '<span class="hd-gloss">NHANH — gốc của <b>ско́рый</b>, <b>ско́рость</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai; thể hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm cho NHANH lên ⇒ đẩy nhanh, tăng tốc. Đi thẳng cách 4: '
    '<b>уско́рить проце́сс</b> đẩy nhanh quá trình. Chia đều, trọng âm đứng yên: '
    '<b>уско́рю</b>, <b>уско́ришь</b>. Cặp thể: <b>ускоря́ть</b>.</div>'
    '<div class="hd-warn">Phải có CÁI ĐƯỢC đẩy nhanh. Tự nó nhanh lên thì thêm <i>-ся</i>: '
    '<b>По́езд уско́рился.</b> Tàu tăng tốc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ускоре́ние</b> sự tăng tốc, gia tốc · <b>ско́рый</b> nhanh, gấp · '
    '<b>ско́рость</b> tốc độ · <b>скоре́е</b> mau lên</div>'
)

# ------------------------------------------------------------------- ускорять
S["ускорять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">LÀM CHO thành ra thế</span></div>'
    '<div class="hd-row"><span class="hd-piece">-скор-</span>'
    '<span class="hd-gloss">NHANH — <b>ско́ро</b>, <b>ско́рость</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ nhất; thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thể CHT của <b>уско́рить</b>: <i>-ить</i> đổi thành <i>-ять</i>, trọng âm nhảy từ gốc '
    'ra đuôi — <b>ускоря́ю</b>, <b>ускоря́ешь</b>. Hay gặp: <b>ускоря́ть шаг</b> rảo bước.</div>'
    '<div class="hd-warn">Trông giống mà khác gốc: <b>оскорбля́ть</b> (xúc phạm) là gốc <i>скорб-</i> '
    'ĐAU BUỒN, không dính gì tới «nhanh».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ускоря́ться</b> tự tăng tốc · <b>ускоре́ние</b> sự tăng tốc, gia tốc · '
    '<b>ско́ро</b> sắp · <b>ско́рая</b> xe cấp cứu</div>'
)

# ----------------------------------------------------------------- прикасаться
S["прикасаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">TỚI SÁT, áp vào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-кас-</span>'
    '<span class="hd-gloss">CHẠM (trong cặp thể đổi thành <i>кос-</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть-ся</span>'
    '<span class="hd-gloss">đuôi CHT + <i>-ся</i> bắt buộc</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đưa tay tới SÁT rồi chạm ⇒ chạm vào, sờ nhẹ. Chia đều: <b>прикаса́юсь</b>, '
    '<b>прикаса́ешься</b>. Cặp thể: <b>прикосну́ться</b>.</div>'
    '<div class="hd-warn">Đòi <b>к</b> + cách 3: <b>прикаса́ться к руке́</b>; còn <b>каса́ться</b> '
    'đòi cách 2 trần: <b>каса́ться руки́</b>. Nghĩa «liên quan đến» là việc của <b>каса́ться</b>.</div>'
    '<div class="hd-warn">✍️ Viết <i>кас</i> khi ngay sau có <i>а</i>, còn lại viết <i>кос</i>: '
    '<b>прикаса́ться</b> — <b>прикосну́ться</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>каса́ться</b> chạm, liên quan · <b>косну́ться</b> chạm (HT) · '
    '<b>прикоснове́ние</b> sự chạm</div>'
)

# ---------------------------------------------------------------- прикоснуться
S["прикоснуться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">TỚI SÁT, áp vào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-кос-</span>'
    '<span class="hd-gloss">CHẠM — cùng gốc <i>кас-</i>, ngay sau không có <i>а</i> nên viết <i>о</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ну́ть-ся</span>'
    '<span class="hd-gloss">MỘT lần, một cái + <i>-ся</i> bắt buộc</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chạm vào một cái là xong ⇒ thể HT của <b>прикаса́ться</b>. Vẫn đòi <b>к</b> + cách 3: '
    '<b>прикосну́ться к плечу́</b> chạm vào vai. Chia: <b>прикосну́сь</b>, <b>прикоснёшься</b>.</div>'
    '<div class="hd-warn">Bóng: <b>прикосну́ться к исто́рии</b> = «chạm» vào lịch sử, lần đầu được nếm trải.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>прикоснове́ние</b> sự chạm · <b>косну́ться</b> chạm, đề cập (HT) · '
    '<b>каса́ться</b> chạm, liên quan · <b>неприкоснове́нный</b> bất khả xâm phạm</div>'
)

# ------------------------------------------------------------------ спасаться
S["спасаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-пас-а́ть</span>'
    '<span class="hd-gloss">CỨU — <i>-пас-</i> che chở, trông giữ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">chính MÌNH</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cứu chính mình ⇒ thoát thân, lánh. Khỏi cái gì: <b>от</b> + cách 2 — '
    '<b>спаса́ться от жары́</b> lánh nóng. Bằng cái gì: cách 5 — <b>спаса́ться бе́гством</b> tháo chạy. '
    'Chia đều: <b>спаса́юсь</b>, <b>спаса́ешься</b>. Cặp thể: <b>спасти́сь</b>.</div>'
    '<div class="hd-warn"><b>Спаса́йся, кто мо́жет!</b> = Mạnh ai nấy chạy!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>спаса́ть</b> cứu (người khác) · <b>спасе́ние</b> sự cứu thoát · '
    '<b>спаса́тель</b> nhân viên cứu hộ · <b>спаси́бо</b> cảm ơn</div>'
)

# ------------------------------------------------------------------- спастись
S["спастись"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-пас-ти́</span>'
    '<span class="hd-gloss">CỨU — <i>-пас-</i> che chở, trông giữ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сь</span>'
    '<span class="hd-gloss">chính MÌNH (<i>-ся</i> sau nguyên âm rút thành <i>-сь</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thể HT của <b>спаса́ться</b>: thoát thân thành công. '
    '<b>спасти́сь от пожа́ра</b> thoát khỏi đám cháy; <b>чу́дом спасти́сь</b> thoát nạn thần kỳ. '
    'Tương lai: <b>спасу́сь</b>, <b>спасёшься</b>.</div>'
    '<div class="hd-warn">Quá khứ: giống đực nhấn gốc, hai <i>с</i>, không có <i>-л</i> — <b>спа́сся</b>; '
    'các dạng kia nhấn đuôi: <b>спасла́сь</b>, <b>спасло́сь</b>, <b>спасли́сь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>спасти́</b> cứu (người khác) · <b>спасе́ние</b> sự cứu thoát · '
    '<b>спаса́тель</b> nhân viên cứu hộ · <b>спаси́бо</b> cảm ơn</div>'
)

# --------------------------------------------------------------------- ширина
S["ширина"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">шир-</span>'
    '<span class="hd-gloss">RỘNG, bề ngang — như <b>широ́кий</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ина́</span>'
    '<span class="hd-gloss">→ danh từ chỉ số đo, giống cái — như <b>глубина́</b>, <b>толщина́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái «rộng» đem ra ĐO ⇒ chiều rộng. Số ít trọng âm luôn ở đuôi. Nói số đo: '
    '<b>ширина́ стола́ — оди́н метр</b> bàn rộng một mét, '
    'hoặc dùng cách 5: <b>стол ширино́й в оди́н метр</b>.</div>'
    '<div class="hd-warn"><b>в ширину́</b> = theo chiều rộng: <b>два ме́тра в ширину́</b> rộng hai mét.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>широ́кий</b> rộng · <b>широко́</b> (trạng từ) rộng · '
    '<b>расши́рить</b> / <b>расширя́ть</b> mở rộng</div>'
)

# --------------------------------------------------------------- автоматически
S["автоматически"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">автома́т-</span>'
    '<span class="hd-gloss">MÁY TỰ ĐỘNG — <b>автома́т</b>, <i>авто-</i> = TỰ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ческ-</span>'
    '<span class="hd-gloss">đuôi tính từ = <i>-ic(al)</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и</span>'
    '<span class="hd-gloss">đuôi trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= <i>automatically</i>: cứ như máy, tự chạy. Tính từ <i>-ский</i> bỏ <i>й</i> là ra '
    'trạng từ: <b>автомати́ческий</b> → <b>автомати́чески</b> (không phải <i>-о</i>). '
    'Trọng âm rời <i>-ма́т</i> sang <i>-ти́-</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>автома́т</b> máy tự động · <b>автомати́ческий</b> tự động (tính từ) · '
    '<b>банкома́т</b> máy ATM</div>'
)

# ------------------------------------------------------------------ скользкий
S["скользкий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ско́льз-</span>'
    '<span class="hd-gloss">TRƯỢT — như <b>скользи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-ий</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dễ TRƯỢT ⇒ trơn: <b>ско́льзкий пол</b> sàn trơn. Câu hay nghe mùa đông: '
    '<b>На у́лице ско́льзко.</b> Ngoài đường trơn lắm. Dạng ngắn: giống đực chen <i>о</i> — <b>ско́льзок</b>; '
    'giống cái nhấn gốc hay nhấn đuôi đều được: <b>ско́льзка</b>, <b>скользка́</b>.</div>'
    '<div class="hd-warn"><b>гла́дкий</b> = nhẵn, mịn · <b>ско́льзкий</b> = trơn, dễ ngã, dễ tuột. '
    'Bóng: <b>ско́льзкая те́ма</b> chủ đề tế nhị, khó nói.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>скользи́ть</b> trượt · <b>ско́льзко</b> trơn (trạng từ)</div>'
)

# -------------------------------------------------------------------- краткий
S["краткий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">крат-</span>'
    '<span class="hd-gloss">NGẮN — dạng Slav cổ của <i>корот-</i> (<i>-ра-</i> ↔ <i>-оро-</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-ий</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Anh em của <b>коро́ткий</b> nhưng giọng sách vở: ngắn về LỜI và THỜI GIAN — '
    '<b>кра́ткий отве́т</b> câu trả lời ngắn gọn. Tên chữ <i>й</i> chính là '
    '<b>и кра́ткое</b> «i ngắn». Dạng ngắn: giống đực chen <i>о</i> — <b>кра́ток</b>; '
    'chỉ giống cái nhấn đuôi — <b>кратка́</b>.</div>'
    '<div class="hd-warn">Đo độ dài đồ vật thì phải <b>коро́ткий</b>: <b>коро́ткие во́лосы</b> tóc ngắn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кра́тко</b> ngắn gọn (trạng từ) · <b>вкра́тце</b> vắn tắt · '
    '<b>сократи́ть</b> rút ngắn · <b>прекрати́ть</b> chấm dứt · <b>коро́ткий</b> ngắn</div>'
)

# ------------------------------------------------------------------- стальной
S["стальной"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сталь-</span>'
    '<span class="hd-gloss">THÉP — <b>сталь</b>, mượn gốc Đức <i>Stahl</i>, họ với Anh <i>steel</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-о́й</span>'
    '<span class="hd-gloss">đuôi tính từ, tự mang trọng âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thép + đuôi tính từ ⇒ bằng thép: <b>стальна́я дверь</b> cửa thép. Bóng, y như tiếng Việt: '
    '<b>стальны́е не́рвы</b> thần kinh thép. Dạng ngắn gần như không dùng, giống đực không có hẳn; '
    'nhìn bảng chỉ cần nhớ trọng âm luôn ở đuôi.</div>'
    '<div class="hd-warn">Đừng nhầm với <b>остально́й</b> (còn lại): từ <b>оста́ться</b>, '
    'không dính gì tới thép.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сталь</b> thép (giống cái)</div>'
)

# ------------------------------------------------------------------ фальшивый
S["фальшивый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">фальш-</span>'
    '<span class="hd-gloss">GIẢ — <b>фальшь</b>, mượn gốc Đức <i>falsch</i>, họ với Anh <i>false</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́в-ый</span>'
    '<span class="hd-gloss">đuôi tính từ — như <b>краси́вый</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một chữ <i>false</i> cho ba chỗ: tiền, giấy tờ GIẢ — <b>фальши́вый па́спорт</b>; '
    'người GIẢ TẠO — <b>фальши́вая улы́бка</b>; nhạc LẠC ĐIỆU — <b>фальши́вая но́та</b>.</div>'
    '<div class="hd-warn"><b>фальши́вый</b> = giả để LỪA. Đồ nhân tạo (hoa, da, trí tuệ) là '
    '<b>иску́сственный</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>фальшь</b> sự giả dối · <b>фальши́вить</b> hát/đàn lạc điệu</div>'
)

# ------------------------------------------------------------------ громадный
S["громадный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">грома́д-</span>'
    '<span class="hd-gloss">KHỐI ĐỒ SỘ — <b>грома́да</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">To như cả một KHỐI sừng sững ⇒ khổng lồ: <b>грома́дный чемода́н</b> vali to tướng. '
    'Gần như thay được cho <b>огро́мный</b>, nhưng <b>огро́мный</b> là từ dùng thường hơn. '
    'Dạng ngắn giống đực chen <i>е</i>: <b>грома́ден</b>.</div>'
    '<div class="hd-warn">Cụm đóng khuôn thì giữ <b>огро́мный</b>: <b>Огро́мное спаси́бо!</b> Cảm ơn rất nhiều!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>грома́да</b> khối đồ sộ · <b>огро́мный</b> khổng lồ</div>'
)

# ----------------------------------------------------------------- старомодный
S["старомодный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">стар-</span>'
    '<span class="hd-gloss">CŨ — như <b>ста́рый</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-о-</span>'
    '<span class="hd-gloss">nguyên âm nối hai gốc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мо́д-н-ый</span>'
    '<span class="hd-gloss">MỐT — <b>мо́да</b> + đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Theo mốt CŨ = <i>old-fashioned</i> ⇒ lỗi mốt, cổ lỗ; nói được cả về người lẫn lối nghĩ. '
    'Dạng ngắn giống đực chen <i>е</i>: <b>старомо́ден</b>.</div>'
    '<div class="hd-warn"><b>старомо́дный</b> = cũ so với mốt, thường chê · '
    '<b>стари́нный</b> = cổ, có giá trị thời xưa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ста́рый</b> cũ, già · <b>мо́да</b> mốt · <b>мо́дный</b> hợp mốt (trái nghĩa)</div>'
)

# ----------------------------------------------------------------- драгоценный
S["драгоценный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">драг-о-</span>'
    '<span class="hd-gloss">QUÝ — dạng Slav cổ của <i>дорог-</i> (<b>дорого́й</b>) + nguyên âm nối</span></div>'
    '<div class="hd-row"><span class="hd-piece">-це́н-н-ый</span>'
    '<span class="hd-gloss">CÓ GIÁ — <b>це́нный</b>, <b>цена́</b>; hai <i>н</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Quý giá» ghép đúng từng mảnh như tiếng Việt. <i>-ра-</i> ↔ <i>-оро-</i> y như cặp '
    '<b>кра́ткий</b> – <b>коро́ткий</b>. <b>драгоце́нное вре́мя</b> thời gian quý báu. '
    'Dạng ngắn giống đực chen <i>е</i>: <b>драгоце́нен</b>.</div>'
    '<div class="hd-warn">Tự nó không phải «đá quý»; phải thêm danh từ: <b>драгоце́нный ка́мень</b> đá quý, '
    '<b>драгоце́нный мета́лл</b> kim loại quý.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>драгоце́нности</b> đồ trang sức quý · <b>дорого́й</b> đắt, thân mến · '
    '<b>це́нный</b> có giá trị · <b>оце́нка</b> sự đánh giá</div>'
)

# ----------------------------------------------------------------- стандартный
S["стандартный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">станда́рт-</span>'
    '<span class="hd-gloss">TIÊU CHUẨN — mượn Anh <i>standard</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng theo chuẩn chung ⇒ tiêu chuẩn, thông thường: '
    '<b>станда́ртный разме́р</b> cỡ tiêu chuẩn. Tiếng Anh để nguyên <i>standard</i> làm tính từ, '
    'tiếng Nga phải thêm <i>-ный</i>. Trọng âm vẫn ở <i>-да́-</i>. '
    'Dạng ngắn giống đực chen <i>е</i>: <b>станда́ртен</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>станда́рт</b> tiêu chuẩn · <b>нестанда́ртный</b> khác thường, độc đáo</div>'
)

# ------------------------------------------------------------------ загадочный
S["загадочный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-га́д-оч-</span>'
    '<span class="hd-gloss">ĐIỀU BÍ ẨN — <b>зага́дка</b> (<i>-гад-</i> ĐOÁN): chen <i>о</i>, <i>к → ч</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Như một câu đố, bắt người ta phải đoán ⇒ bí ẩn: '
    '<b>зага́дочная улы́бка</b> nụ cười bí ẩn. Cùng phép đổi với <b>ска́зка</b> → <b>ска́зочный</b>. '
    'Dạng ngắn giống đực chen <i>е</i>: <b>зага́дочен</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>зага́дка</b> câu đố, điều bí ẩn · <b>гада́ть</b> đoán, bói · '
    '<b>угада́ть</b> đoán trúng · <b>догада́ться</b> đoán ra</div>'
)

# ------------------------------------------------------------------ формальный
S["формальный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">форм-</span>'
    '<span class="hd-gloss">HÌNH DẠNG, KHUÔN — <b>фо́рма</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́льный</span>'
    '<span class="hd-gloss">→ tính từ (như <i>-al</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Theo đúng KHUÔN, có khi rỗng ruột ⇒ hình thức, theo thủ tục: '
    '<b>форма́льный отве́т</b> câu trả lời cho có lệ. Dạng ngắn giống đực: <i>ь</i> thay bằng <i>е</i> — '
    '<b>форма́лен</b>.</div>'
    '<div class="hd-warn">Chính thức vì do CƠ QUAN đưa ra là <b>официа́льный</b>; '
    '<b>форма́льный</b> = đúng về mặt hình thức, nghi thức.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>фо́рма</b> hình dạng, khuôn · <b>формирова́ть</b> tạo dựng, hình thành · <b>форма́льность</b> thủ tục hình thức · '
    '<b>неформа́льный</b> thân mật, không nghi thức · <b>оформле́ние</b> việc làm thủ tục</div>'
)

# --------------------------------------------------------------- универсальный
S["универсальный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">универс-</span>'
    '<span class="hd-gloss">TOÀN THỂ — Latin, như <i>universe</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́льный</span>'
    '<span class="hd-gloss">→ tính từ (như <i>-al</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= <i>universal</i>: hợp với MỌI thứ ⇒ vạn năng, đa năng — '
    '<b>универса́льный ключ</b> chìa vạn năng. Dạng ngắn giống đực: <i>ь</i> thay bằng <i>е</i> — '
    '<b>универса́лен</b>.</div>'
    '<div class="hd-warn"><b>универса́льный магази́н</b> = bách hoá, nói tắt thành <b>универма́г</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>универма́г</b> bách hoá · <b>универса́м</b> siêu thị · '
    '<b>университе́т</b> đại học (cùng gốc Latin «toàn thể»)</div>'
)

# ------------------------------------------------------------ благотворительный
S["благотворительный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">благо-</span>'
    '<span class="hd-gloss">TỐT LÀNH — <b>бла́го</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-твор-и́-</span>'
    '<span class="hd-gloss">LÀM RA, tạo — như <b>тво́рчество</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-тель-ный</span>'
    '<span class="hd-gloss">NGƯỜI làm (<i>-тель</i>) + đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thuộc về người «làm điều lành» ⇒ từ thiện: <b>благотвори́тельный конце́рт</b> hoà nhạc '
    'gây quỹ, <b>благотвори́тельный фонд</b> quỹ từ thiện. Dạng ngắn giống đực chen <i>е</i>: '
    '<b>благотвори́телен</b> (hiếm gặp).</div>'
    '<div class="hd-warn">Gần mặt chữ mà khác nghĩa: <b>благотво́рный</b> = có lợi, tốt lành '
    '(<b>благотво́рное влия́ние</b> ảnh hưởng tốt).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>благотвори́тель</b> nhà hảo tâm · <b>благотвори́тельность</b> việc từ thiện · '
    '<b>благодари́ть</b> cảm ơn · <b>благоро́дный</b> cao thượng</div>'
)

# --------------------------------------------------------------------- железо
S["железо"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — <i>желез-</i> SẮT là gốc trơn, thêm đuôi giống trung <i>-о</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhớ kèm <b>желе́зная доро́га</b> đường sắt. Trọng âm đứng yên ở <i>-ле́-</i>; '
    'là chất liệu nên chỉ dùng số ít. Còn là chất sắt trong thức ăn, và dân máy tính gọi phần cứng là '
    '<b>желе́зо</b>.</div>'
    '<div class="hd-warn">Đổi trọng âm là ra từ khác: <b>железа́</b> (giống cái) = TUYẾN trong cơ thể. '
    'Sắt thì cách nào cũng nhấn <i>-ле́-</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>желе́зный</b> bằng sắt · <b>железнодоро́жный</b> thuộc đường sắt</div>'
)

# ------------------------------------------------------------------- BÁO CÁO
B = {
    "docbangmat": 124,
    "loitubat": 6,      # форма́льный «chỉ đúng hình thức» đá câu ví dụ thiệp mời · ширина́ trọng âm «luôn» ở đuôi -> chỉ số ít · вкра́тце «tóm lại» -> vắn tắt · благотво́рный «bỏ khúc giữa là ra» (không phải phép cắt) · сталь/фальшь «= steel/false» -> chỉ là họ hàng qua tiếng Đức · прикаса́ться «liên quan CHỈ là каса́ться» quá tay
    "nguonsai": 2,      # CACH DUNG кра́ткий/коро́ткий nói коро́ткий chỉ cho vật chất (sai: коро́ткий разгово́р, đã in trên thẻ коро́ткий) · dạng ngắn стальна́/стально́ in như dạng sống, thực tế gần như không dùng
    "baolen": [
        "Va chạm громадный/огромный: gỡ bằng V громадный «khổng lồ, to tướng» (bỏ «to lớn, mênh mông»); «to lớn» cũng là nghĩa của huge nên CẦN DUYỆT. Không dùng «đồ sộ» vì sẽ trùng HẾT với гигантский (k214: khổng lồ, đồ sộ).",
        "Va chạm формальный/официальный: bỏ «chính thức» ở формальный; nhưng câu ví dụ của thẻ «формальное приглашение» đang dịch «thiệp mời chính thức» — luồng chính cân sửa bản dịch câu đó.",
        "Câu ví dụ драгоценный «драгоценным кольцом» dịch «chiếc nhẫn đá quý» — chính là nguồn nghĩa sai «đá quý»; nên dịch «nhẫn quý».",
        "V cần duyệt: ускорить/ускорять chung một dãy · спасаться/спастись chung «tự cứu mình, thoát thân, lánh» (bỏ «sống sót» = выжить) · ширина bỏ «khổ rộng» · автоматически còn «tự động» (bỏ «theo quán tính») · скользкий bỏ «nhẵn trượt» · краткий thêm «ngắn ngủi» (short-lived) · стальной «cứng rắn» -> «cứng như thép» · фальшивый thêm «giả mạo, lạc điệu», bỏ «làm giả» · старомодный thêm «lỗi mốt», bỏ «cũ kiểu» · драгоценный bỏ «đá quý» · стандартный bỏ «bình thường» · универсальный «dùng chung» -> «vạn năng» · благотворительный bỏ «nhân đạo» (гуманитарный).",
        "прикасаться/прикоснуться và железо, загадочный: giữ nguyên field, không khai V.",
        "KHÔNG CHẮC (từ nguyên theo trí nhớ, không tra được trong repo): сталь và фальшь mượn gốc Đức (có thể qua Ba Lan) · скорб- của оскорблять · громада cùng gốc огромный (giữ khớp thẻ огромный).",
    ],
}
