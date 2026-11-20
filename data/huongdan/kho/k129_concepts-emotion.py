# -*- coding: utf-8 -*-
"""k129 — concepts::emotion: 21 từ cảm xúc, phần lớn là CẶP THỂ đi đôi.

Không khối hệ thống. Chỗ cần nhất quán trong lô:
(1) Cặp thể: thẻ HT (простить, проснуться, успокоиться, удивиться, напомнить) giải gốc đầy đủ,
    thẻ CHT dẫn chiếu + nói đúng một chỗ khác (đuôi -ива-/-а-, câu cửa miệng riêng).
(2) за- = BẮT ĐẦU: засмея́ться ↔ запла́кать (họ hàng của пла́кать).
(3) Gốc khớp với lô khác: прост-/прощ- = thoáng, tự do (k126 прощаться); гор- = cháy (k133 гореть).
(4) Biến âm: д→ж (горжу́сь), т→ч (забо́чусь), к→ч (пла́чу), ст→щ (прощу́), м→мл / в→вл (chèn л).
Họ hàng: cả 21 thẻ đều có.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa, ngăn bằng dấu phẩy.
V = {
    "напоминать": "nhắc, nhắc nhở, trông giống",       # bỏ dấu ';' cho đúng khuôn dấu phẩy
    "горе": "nỗi đau buồn, nỗi đau khổ",               # bỏ 'bất hạnh' — trùng несчастье
    "простить": "tha thứ",                             # bỏ 'tha lỗi' — trùng извинить
    "прощать": "tha thứ",                              # bỏ 'bỏ qua' — trùng извинять
    "успокаиваться": "bình tĩnh lại, dịu đi",          # 'bình tĩnh dần' là nhãn thể trá hình
    "грубый": "thô lỗ, cục cằn, thô ráp",              # thiếu nghĩa gốc rough/coarse
}

# ------------------------------------------------------------- напомнить
S["напомнить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">LÊN, đặt vào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-по́мн-ить</span>'
    '<span class="hd-gloss">NHỚ — chính là <b>по́мнить</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đặt lên trí nhớ (của ai)» ⇒ nhắc. Thể hoàn thành; cặp chưa hoàn thành '
    'là <b>напомина́ть</b>.</div>'
    '<div class="hd-warn">Nhắc AI → cách 3, nhắc VỀ CÁI GÌ → <b>о</b> + cách 6: '
    '<b>Напо́мни мне о встре́че</b> = nhắc tớ về buổi gặp nhé.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>по́мнить</b> nhớ · <b>вспо́мнить</b> nhớ ra · <b>па́мять</b> trí nhớ · '
    '<b>напомина́ние</b> lời nhắc</div>'
)

# ------------------------------------------------------------- напоминать
S["напоминать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-по́мн-</span>'
    '<span class="hd-gloss">đặt lên trí NHỚ — như <b>напо́мнить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-мин-а́ть</span>'
    '<span class="hd-gloss"><b>мн</b> nở thành <b>мин</b> + <b>-а́ть</b> → thể chưa hoàn thành '
    '(y như <b>вспо́мнить → вспомина́ть</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp chưa hoàn thành của <b>напо́мнить</b>. Thêm một nghĩa mà cặp kia ít '
    'dùng: «gợi ai nhớ tới ai» ⇒ trông giống.</div>'
    '<div class="hd-warn">Giống AI → cách 4, không giới từ: <b>Ты напомина́ешь мне ма́му</b> = '
    'cậu làm tôi nhớ tới mẹ / trông giống mẹ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>по́мнить</b> nhớ · <b>па́мять</b> trí nhớ · '
    '<b>напомина́ние</b> lời nhắc</div>'
)

# ------------------------------------------------------------- стремиться
S["стремиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">стрем-</span>'
    '<span class="hd-gloss">LAO VÚT về phía — thấy rõ ở <b>стреми́тельный</b> nhanh như tên</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть-ся</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2 + <b>-ся</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Lao mình về phía mục tiêu» ⇒ phấn đấu. Ngôi «tôi» chèn <b>л</b> sau '
    '<b>м</b>: <b>стремлю́сь</b> (y như <b>люби́ть → люблю́</b>).</div>'
    '<div class="hd-warn">Hướng tới CÁI GÌ → <b>к</b> + cách 3: <b>стреми́ться к успе́ху</b> = '
    'phấn đấu để thành công.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>стремле́ние</b> khát vọng · <b>стреми́тельный</b> nhanh vút</div>'
)

# ------------------------------------------------------------- впечатление
S["впечатление"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO</span></div>'
    '<div class="hd-row"><span class="hd-piece">-печат-</span>'
    '<span class="hd-gloss">IN, ĐÓNG DẤU — gốc của <b>печа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ле́ние</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cái được in vào lòng» ⇒ ấn tượng — đúng khuôn tiếng Anh '
    '<i>im-press-ion</i> (ấn vào) — chính là bản dịch sát từng mảnh.</div>'
    '<div class="hd-warn">Gây ấn tượng VỚI AI: <b>произвести́ впечатле́ние на</b> + cách 4.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>печа́ть</b> con dấu, việc in · <b>печа́тать</b> in, đánh máy · '
    '<b>впечатля́ющий</b> gây ấn tượng</div>'
)

# ------------------------------------------------------------- горе
S["горе"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">гор-</span>'
    '<span class="hd-gloss">CHÁY, ĐỐT — gốc của <b>горе́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nỗi đau «thiêu đốt» trong lòng — cùng gốc với <b>го́рький</b> (đắng) và '
    '<b>горя́чий</b> (nóng).</div>'
    '<div class="hd-warn">⚠️ Mức tin: nối với «cháy» là từ nguyên, không suy ra được. Đừng lẫn '
    '<b>го́ре</b> với <b>гора́</b> núi — khác gốc, trọng âm khác chỗ.</div>'
    '<div class="hd-warn">Cụm hay gặp: <b>с го́рем попола́м</b> = vất vả lắm mới xong.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>горе́ть</b> cháy · <b>го́рький</b> đắng · <b>горя́чий</b> nóng · '
    '<b>горева́ть</b> đau buồn</div>'
)

# ------------------------------------------------------------- жестокий
S["жестокий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">жест-</span>'
    '<span class="hd-gloss">CỨNG — cùng gốc với <b>жёсткий</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́к-ий</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cứng lòng» ⇒ tàn nhẫn. Trạng từ: <b>жесто́ко</b> một cách tàn nhẫn.</div>'
    '<div class="hd-warn">Hai từ gần như cùng mặt chữ: <b>жесто́кий</b> tàn nhẫn (có <b>-о-</b>, '
    'trọng âm giữa) ≠ <b>жёсткий</b> cứng, rắn (có <b>ё</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>жесто́кость</b> sự tàn nhẫn · <b>жёсткий</b> cứng, rắn</div>'
)

# ------------------------------------------------------------- грубый
S["грубый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn <b>груб-</b> + đuôi tính từ <b>-ый</b>, không chẻ thêm được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc là THÔ, chưa mài giũa (vải thô, tay thô ráp) → người «thô» = '
    'thô lỗ. Dạng ngắn giống cái dịch trọng âm ra cuối: <b>груб</b> · <b>груба́</b> · '
    '<b>гру́бо</b> · <b>гру́бы</b>.</div>'
    '<div class="hd-warn"><b>гру́бая оши́бка</b> = lỗi nặng, không phải «lỗi thô lỗ»; '
    '<b>гру́бо говоря́</b> = nói đại khái.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гру́бо</b> thô bạo · <b>гру́бость</b> sự thô lỗ · '
    '<b>грубия́н</b> kẻ thô lỗ</div>'
)

# ------------------------------------------------------------- гордый
S["гордый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn <b>горд-</b> + đuôi tính từ <b>-ый</b>, không chẻ thêm được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tính từ là gốc, động từ <b>горди́ться</b> sinh ra từ nó. Dạng ngắn giống '
    'cái dịch trọng âm ra cuối: <b>горд</b> · <b>горда́</b> · <b>го́рдо</b> · <b>горды́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>горди́ться</b> tự hào · <b>го́рдость</b> niềm tự hào · '
    '<b>го́рдо</b> đầy kiêu hãnh</div>'
)

# ------------------------------------------------------------- гордиться
S["гордиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">горд-</span>'
    '<span class="hd-gloss">TỰ HÀO — chính là <b>го́рдый</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть-ся</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2 + <b>-ся</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Là người <b>го́рдый</b>» ⇒ tự hào. Ngôi «tôi» đổi <b>д → ж</b>: '
    '<b>горжу́сь</b>, các ngôi khác giữ <b>д</b>: <b>горди́шься</b>.</div>'
    '<div class="hd-warn">Tự hào VỀ AI → cách 5, KHÔNG giới từ: <b>Я горжу́сь тобо́й</b> = '
    'tớ tự hào về cậu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>го́рдый</b> kiêu hãnh · <b>го́рдость</b> niềm tự hào</div>'
)

# ------------------------------------------------------------- страдать
S["страдать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">страд-</span>'
    '<span class="hd-gloss">CHỊU ĐAU — gốc của <b>страда́ние</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi động từ lớp 1, chia đều: <b>страда́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hai khung, hai nghĩa: <b>от</b> + cách 2 = khổ VÌ cái gì '
    '(<b>страда́ть от жары́</b>); cách 5 không giới từ = MẮC bệnh gì '
    '(<b>страда́ть бессо́нницей</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>страда́ние</b> nỗi đau khổ · <b>пострада́ть</b> bị thiệt hại · '
    '<b>пострада́вший</b> nạn nhân</div>'
)

# ------------------------------------------------------------- плакать
S["плакать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">плак-</span>'
    '<span class="hd-gloss">KHÓC — gốc của <b>плач</b> tiếng khóc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thì hiện tại đổi <b>к → ч</b> ở MỌI ngôi: <b>пла́чу</b>, '
    '<b>пла́чешь</b>, <b>пла́чут</b>. Bật khóc là <b>запла́кать</b> (<b>за-</b> = bắt đầu).</div>'
    '<div class="hd-warn">Chỉ trọng âm tách hai câu: <b>я пла́чу</b> = tôi khóc, '
    '<b>я плачу́</b> = tôi trả tiền (<b>плати́ть</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>плач</b> tiếng khóc · <b>запла́кать</b> bật khóc</div>'
)

# ------------------------------------------------------------- простить
S["простить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">прост-</span>'
    '<span class="hd-gloss">THOÁNG, TỰ DO — gốc của <b>просто́й</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2 «làm cho …»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thả cho nhẹ, cho tự do» ⇒ tha. Ngôi «tôi» đổi <b>ст → щ</b>: '
    '<b>прощу́</b>; cũng chữ <b>щ</b> ấy làm nên cặp <b>проща́ть</b>.</div>'
    '<div class="hd-warn">Tha AI → cách 4, tha VÌ việc gì → <b>за</b> + cách 4: '
    '<b>Прости́ меня́ за опозда́ние</b> = tha lỗi cho tớ vì đến muộn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>проще́ние</b> sự tha thứ · <b>проща́ться</b> từ biệt · '
    '<b>просто́й</b> đơn giản</div>'
)

# ------------------------------------------------------------- прощать
S["прощать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">прощ-</span>'
    '<span class="hd-gloss">= <b>прост-</b> sau khi <b>ст → щ</b>: thoáng, tự do</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành, chia đều: <b>проща́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp chưa hoàn thành của <b>прости́ть</b>. Tha cho nhau lúc chia tay ⇒ '
    '<b>проща́ться</b> từ biệt.</div>'
    '<div class="hd-warn"><b>Проща́й(те)!</b> = vĩnh biệt — chia tay lâu, có khi mãi mãi; '
    'khác hẳn <b>До свида́ния!</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>проще́ние</b> sự tha thứ · <b>проща́ться</b> từ biệt · '
    '<b>просто́й</b> đơn giản</div>'
)

# ------------------------------------------------------------- успокоиться
S["успокоиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">LÀM CHO trở nên …</span></div>'
    '<div class="hd-row"><span class="hd-piece">-споко́-</span>'
    '<span class="hd-gloss">YÊN — như <b>споко́йный</b>, <b>поко́й</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить-ся</span>'
    '<span class="hd-gloss">đuôi động từ + <b>-ся</b> = cho chính mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Làm cho chính mình trở nên yên» ⇒ bình tĩnh lại. Bỏ <b>-ся</b> là làm cho '
    'NGƯỜI KHÁC yên: <b>успоко́ить ребёнка</b> = dỗ em bé.</div>'
    '<div class="hd-warn">Câu cửa miệng: <b>Успоко́йся!</b> = bình tĩnh nào!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>споко́йный</b> bình tĩnh · <b>поко́й</b> sự yên · '
    '<b>беспоко́иться</b> lo lắng</div>'
)

# ------------------------------------------------------------- успокаиваться
S["успокаиваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-спока́-</span>'
    '<span class="hd-gloss">làm cho YÊN — <b>-поко́-</b> của <b>успоко́иться</b>, <b>о</b> đổi thành <b>а</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ть-ся</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp chưa hoàn thành của <b>успоко́иться</b>. Thêm <b>-ива-</b> thì <b>о</b> '
    'ở gốc thành <b>а</b> — đúng khuôn <b>устро́ить → устра́ивать</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>споко́йный</b> bình tĩnh · <b>поко́й</b> sự yên · '
    '<b>беспоко́иться</b> lo lắng</div>'
)

# ------------------------------------------------------------- проснуться
S["проснуться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">XUYÊN QUA, đi hết</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сн-</span>'
    '<span class="hd-gloss">NGỦ — gốc của <b>сон</b>, <b>спать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-у́ть-ся</span>'
    '<span class="hd-gloss"><b>-ну-</b> = một lần, xong ngay</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đi hết giấc ngủ, ra khỏi nó» ⇒ tỉnh dậy. Gốc ngủ chạy ba mặt: '
    '<b>сп-</b> (<b>спать</b>), <b>сн-</b> (<b>сна</b>), <b>сып-</b> (<b>просыпа́ться</b>).</div>'
    '<div class="hd-warn">Tỉnh ≠ dậy khỏi giường: <b>Я просну́лся в семь, а встал в во́семь</b> = '
    'tôi tỉnh lúc 7 giờ, 8 giờ mới dậy.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>спать</b> ngủ · <b>сон</b> giấc ngủ · <b>засну́ть</b> ngủ thiếp đi</div>'
)

# ------------------------------------------------------------- просыпаться
S["просыпаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">XUYÊN QUA, đi hết</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сып-</span>'
    '<span class="hd-gloss">NGỦ — mặt khác của <b>сп-</b>/<b>сн-</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть-ся</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp chưa hoàn thành của <b>просну́ться</b>: thói quen hằng ngày, '
    '<b>Я просыпа́юсь в семь</b>. Nghĩa «rơi vãi» trong từ điển là của một từ khác cùng mặt chữ '
    '(gốc <b>сы́пать</b> rắc) — thẻ này không học nghĩa đó.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>спать</b> ngủ · <b>сон</b> giấc ngủ · <b>засыпа́ть</b> ngủ thiếp đi</div>'
)

# ------------------------------------------------------------- заботиться
S["заботиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">забо́т-</span>'
    '<span class="hd-gloss">SỰ CHĂM LO — chính là <b>забо́та</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить-ся</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2 + <b>-ся</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Động từ của danh từ <b>забо́та</b> ⇒ chăm sóc, lo cho. Ngôi «tôi» đổi <b>т → ч</b>: '
    '<b>забо́чусь</b>, các ngôi khác giữ <b>т</b>: <b>забо́тишься</b>.</div>'
    '<div class="hd-warn">Chăm lo CHO AI → <b>о</b> + cách 6: <b>забо́титься о де́тях</b> = '
    'chăm lo cho con cái.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>забо́та</b> sự chăm lo, nỗi lo · <b>забо́тливый</b> chu đáo · '
    '<b>беззабо́тный</b> vô tư lự</div>'
)

# ------------------------------------------------------------- засмеяться
S["засмеяться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">BẮT ĐẦU</span></div>'
    '<div class="hd-row"><span class="hd-piece">-смея́ть-ся</span>'
    '<span class="hd-gloss">CƯỜI — chính là <b>смея́ться</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Bắt đầu cười» ⇒ bật cười. Chia y như <b>смея́ться</b>, chữ <b>я</b> rơi '
    'mất: <b>засмею́сь</b>, <b>засмеёшься</b>. Cùng khuôn: <b>запла́кать</b> bật khóc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>смея́ться</b> cười · <b>смех</b> tiếng cười · '
    '<b>смешно́й</b> buồn cười</div>'
)

# ------------------------------------------------------------- удивиться
S["удивиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố, không mang nghĩa riêng ở đây</span></div>'
    '<div class="hd-row"><span class="hd-piece">-див-</span>'
    '<span class="hd-gloss">ĐIỀU LẠ — <b>ди́во</b> (từ cổ)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть-ся</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2 + <b>-ся</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Gặp điều lạ» ⇒ ngạc nhiên. Ngôi «tôi» chèn <b>л</b> sau <b>в</b>: '
    '<b>удивлю́сь</b> — cũng chữ <b>л</b> ấy làm nên cặp <b>удивля́ться</b>.</div>'
    '<div class="hd-warn">Ngạc nhiên VỀ CÁI GÌ → cách 3, KHÔNG giới từ: '
    '<b>удиви́ться но́вости</b> = ngạc nhiên vì tin đó.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>удиви́тельный</b> đáng kinh ngạc · <b>удивле́ние</b> sự ngạc nhiên · '
    '<b>удиви́ть</b> làm ngạc nhiên</div>'
)

# ------------------------------------------------------------- удивляться
S["удивляться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-див-</span>'
    '<span class="hd-gloss">gặp ĐIỀU LẠ — như <b>удиви́ться</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-л-я́ть-ся</span>'
    '<span class="hd-gloss"><b>л</b> chèn sau <b>в</b> + đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp chưa hoàn thành của <b>удиви́ться</b>, chia đều: '
    '<b>удивля́юсь</b>. Cũng đòi cách 3: <b>Не удивля́йся!</b> = đừng ngạc nhiên!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>удиви́тельный</b> đáng kinh ngạc · <b>удивле́ние</b> sự ngạc nhiên · '
    '<b>удиви́ть</b> làm ngạc nhiên</div>'
)
