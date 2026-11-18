# -*- coding: utf-8 -*-
"""k112 — numbers (tên topic KHÔNG phải trục): lô hỗn hợp hư từ + danh từ + hai cặp thể,
soạn từng thẻ độc lập.

Chỗ cần nhất quán trong lô:
(1) -нибудь «… nào cũng được» (кто́-нибудь, когда́-нибудь) — cùng cách giải thích với thẻ
    что́-нибудь; phép so -то ↔ -нибудь mỗi thẻ chỉ một câu về CHÍNH từ đó;
(2) gốc зв-/зов-/-зыв- «gọi» (назва́ть / называ́ть) — cùng cách chẻ với звать, называ́ться;
(3) gốc чит-/чёт «đếm» (счита́ть / посчита́ть) — cùng cách chẻ với чита́ть, счёт;
(4) за/по + cách 5/6 của то (зате́м) — cùng khuôn với пото́м, заче́м.
Họ hàng cố ý vắng: ну (thán từ), ведь (hư từ; gốc cổ chỉ ghi ở mức tin), те́ма (mượn đứng
một mình), пора́ (gốc trơn — chỉ có cụm cố định, đưa vào ô đỏ).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "бы": "thì sẽ, thì đã",
    "ведь": "chẳng phải… sao, vì… mà",
    "кто-нибудь": "bất kỳ ai, có ai",
    "предложение": "đề nghị, lời đề xuất, câu",
    "называть": "gọi là, đặt tên",
    "пора": "đã đến lúc, thời kỳ",
    "затем": "tiếp đó, kế đó",
    "ряд": "hàng, dãy, một loạt",
    "более": "hơn",
    "считать": "cho rằng, coi là, đếm, tính",
}

# ---------------------------------------------------------------------- ну
S["ну"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Thán từ, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đứng đầu câu để mở lời, giục, hay chịu thua: <b>Ну, пошли́!</b> '
    'Nào, đi thôi! · <b>Ну, не зна́ю…</b> Ừ thì, tôi không biết… Giọng lên ở <b>Ну?</b> '
    '= «Rồi sao?», giục người kia nói tiếp.</div>'
    '<div class="hd-warn">Hai cụm phải thuộc: <b>Ну и что?</b> = Thì sao nào? · '
    '<b>Ну что ж</b> = Thôi được, đành vậy.</div>'
)

# ---------------------------------------------------------------------- бы
S["бы"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Tiểu từ GIẢ ĐỊNH, không chẻ được — vốn là một dạng cổ của '
    '<b>быть</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiếng Nga không có thì riêng cho «would»: chỉ cần <b>бы</b> + động từ '
    'ở dạng QUÁ KHỨ, dù đang nói chuyện bây giờ hay sau này. <b>Я бы пошёл</b> = tôi thì sẽ '
    'đi (nhưng không đi được). <b>бы</b> đứng trước hay sau động từ đều được.</div>'
    '<div class="hd-warn">Cụm phải thuộc: <b>е́сли бы</b> = giá mà, nếu như (chuyện không có '
    'thật): <b>Е́сли бы я знал…</b> · <b>хоте́л бы</b> = tôi muốn (lịch sự hơn '
    '<b>хочу́</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>что́бы</b> để, để mà · <b>быть</b> là, có</div>'
)

# -------------------------------------------------------------------- ведь
S["ведь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Hư từ, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Kéo người nghe vào điều HAI BÊN ĐỀU BIẾT. Nhắc lại: <b>Ты ведь '
    'обеща́л!</b> = Chẳng phải cậu đã hứa sao! Nêu lý do ai cũng thấy: <b>Возьми́ зонт, ведь '
    'идёт дождь</b> = Cầm ô đi, vì trời đang mưa mà.</div>'
    '<div class="hd-warn">⚠️ Mức tin: đây là từ nguyên, không phải luật — nhiều khả năng từ gốc '
    'cổ <i>вед-</i> «biết», nên nghĩa gốc gần «(anh) biết đấy», y như <i>you know</i>.</div>'
)

# -------------------------------------------------------------- кто-нибудь
S["кто-нибудь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кто</span>'
    '<span class="hd-gloss">AI (từ hỏi)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-нибудь</span>'
    '<span class="hd-gloss">«… nào cũng được» — chưa xác định (<i>ни</i> + <i>будь</i>: cứ '
    'là… nào)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người nói KHÔNG biết là ai, có khi chưa có ai: dùng trong câu hỏi, câu '
    'nhờ: <b>Кто́-нибудь звони́л?</b> Có ai gọi không? · <b>Помоги́те кто́-нибудь!</b> Ai '
    'giúp với! Chỉ phần <b>кто</b> biến cách: <b>кого́-нибудь</b>.</div>'
    '<div class="hd-warn">Đã có thật một người, chỉ không biết tên ⇒ <b>кто́-то</b>: '
    '<b>Кто́-то звони́л</b> = Có người đã gọi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кто</b> ai · <b>кто́-то</b> ai đó · <b>что́-нибудь</b> bất cứ thứ '
    'gì · <b>когда́-нибудь</b> một ngày nào đó · <b>никто́</b> không ai</div>'
)

# -------------------------------------------------------------------- тема
S["тема"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn từ Hy Lạp <i>théma</i>, không chẻ được — chính là <i>theme</i> '
    'của tiếng Anh.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chủ đề của câu chuyện, bài viết, bài học: <b>те́ма уро́ка</b> chủ đề '
    'bài học.</div>'
    '<div class="hd-warn">Nói VỀ một đề tài thì dùng <b>на</b> + cách 4: <b>поговори́ть на '
    'э́ту те́му</b> = nói về chuyện này · <b>смени́ть те́му</b> = đổi chủ đề.</div>'
)

# ------------------------------------------------------------- предложение
S["предложение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пред-</span>'
    '<span class="hd-gloss">TRƯỚC, ra phía trước</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лож-</span>'
    '<span class="hd-gloss">ĐẶT (nằm) — gốc của <b>положи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đặt ra trước mặt» ⇒ đề nghị — ghép y hệt <i>pro-pose</i> (trước + '
    'đặt) của tiếng Anh. Trong ngữ pháp nó còn là «CÂU»: <b>просто́е предложе́ние</b> câu '
    'đơn.</div>'
    '<div class="hd-warn">Cụm phải thuộc: <b>сде́лать предложе́ние</b> = cầu hôn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>предложи́ть</b> đề nghị · <b>предлага́ть</b> đề nghị · '
    '<b>положи́ть</b> đặt · <b>положе́ние</b> vị trí, tình hình</div>'
)

# ---------------------------------------------------------------- разговор
S["разговор"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раз-</span>'
    '<span class="hd-gloss">tán ra, qua lại hai chiều</span></div>'
    '<div class="hd-row"><span class="hd-piece">-говор</span>'
    '<span class="hd-gloss">NÓI (gốc của <b>говори́ть</b>), không thêm đuôi</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <b>разгова́ривать</b> bỏ đuôi động từ: nói qua nói lại ⇒ cuộc '
    'trò chuyện. Với ai: <b>с</b> + cách 5; về gì: <b>о</b> + cách 6 — <b>разгово́р с '
    'дру́гом о рабо́те</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>говори́ть</b> nói · <b>разгова́ривать</b> trò chuyện · '
    '<b>разгово́рный</b> thuộc khẩu ngữ · <b>разгово́рник</b> sách hội thoại</div>'
)

# ------------------------------------------------------------------ назвать
S["назвать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không tách ra nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-зва-ть</span>'
    '<span class="hd-gloss">gốc GỌI — chính là <b>звать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thể HOÀN THÀNH của <b>называ́ть</b>: gọi tên một lần là xong — đặt '
    'tên cho em bé, nêu ra một cái tên. Cùng cách đòi: ai/cái gì ở cách 4, TÊN ở cách 5: '
    '<b>Его́ назва́ли Ива́ном</b>.</div>'
    '<div class="hd-warn">⚠️ Tương lai lấy thân <b>зов-</b> y như <b>зову́</b> của '
    '<b>звать</b>: <b>назову́, назовёшь</b>; quá khứ giống cái nhảy trọng âm: '
    '<b>назвала́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>звать</b> gọi · <b>называ́ть</b> gọi là · <b>назва́ние</b> tên gọi · '
    '<b>называ́ться</b> được gọi là</div>'
)

# ----------------------------------------------------------------- называть
S["называть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không tách ra nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-зыва́-</span>'
    '<span class="hd-gloss">gốc GỌI — biến thể của <b>звать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>-ыва-</b> chen vào gốc là dấu hiệu thể CHƯA HOÀN THÀNH, y như '
    '<b>расска́зывать</b>, <b>пока́зывать</b> (cặp: <b>назва́ть</b>). Chia đều: <b>называ́ю, '
    'называ́ешь</b>.</div>'
    '<div class="hd-warn">Gọi AI là GÌ: người/vật ở cách 4, cái tên ở cách 5 — <b>Мы называ́ем '
    'его́ дру́гом</b> = Chúng tôi gọi anh ấy là bạn. Thêm <b>-ся</b> thì tên về cách 1: '
    '<b>Го́род называ́ется Москва́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>звать</b> gọi · <b>назва́ть</b> đặt tên · <b>назва́ние</b> tên gọi · '
    '<b>называ́ться</b> được gọi là</div>'
)

# --------------------------------------------------------------- информация
S["информация"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ин-</span>'
    '<span class="hd-gloss">VÀO (Latin <i>in</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-форм-</span>'
    '<span class="hd-gloss">HÌNH, khuôn — chính là <b>фо́рма</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ция</span>'
    '<span class="hd-gloss">= <i>-ation</i>, ra danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chữ-đối-chữ với <i>information</i>. Dùng như danh từ không đếm '
    'được, gần như chỉ ở số ít.</div>'
    '<div class="hd-warn">Đuôi <b>-ция</b> có cách 3 và cách 6 là <b>-ии</b>: <b>об '
    'информа́ции</b>, không phải «-е».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>фо́рма</b> hình dạng · <b>информи́ровать</b> thông báo · '
    '<b>информацио́нный</b> thuộc về thông tin</div>'
)

# --------------------------------------------------------------------- пора
S["пора"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc là «thời kỳ, mùa»; đứng một mình làm vị ngữ thì thành «đã '
    'tới lúc». Người cần đi ở cách 3: <b>Мне пора́ идти́</b> = Tôi phải đi rồi. Đứng trơn '
    '<b>Пора́!</b> = Đến giờ rồi!</div>'
    '<div class="hd-warn">Hai cụm phải thuộc, chứa <b>пор</b> (cách 2 số nhiều): <b>до сих '
    'пор</b> = cho tới giờ · <b>с тех пор</b> = từ đó tới nay.</div>'
)

# -------------------------------------------------------------------- затем
S["затем"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за</span>'
    '<span class="hd-gloss">giới từ «đằng sau»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-те́м</span>'
    '<span class="hd-gloss">cách 5 của <b>то</b> (cái đó)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đằng sau cái đó» ⇒ bước kế tiếp. Cùng lối giới từ + đại từ với '
    '<b>пото́м</b>, nhưng <b>зате́м</b> là giọng sách vở, hay dùng khi kể từng bước: '
    '<i>Снача́ла…, зате́м…</i></div>'
    '<div class="hd-warn">Chỉ khác một chữ: <b>заче́м</b> = để làm gì? (<b>чем</b> = cái '
    'gì) — <b>зате́м</b> (<b>тем</b> = cái đó) là câu trả lời về thứ tự, không phải mục '
    'đích.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">cùng khuôn giới từ + <b>то</b>: <b>пото́м</b> sau đó · '
    '<b>потому́</b> vì thế</div>'
)

# ------------------------------------------------------------- когда-нибудь
S["когда-нибудь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">когда́</span>'
    '<span class="hd-gloss">KHI NÀO</span></div>'
    '<div class="hd-row"><span class="hd-piece">-нибудь</span>'
    '<span class="hd-gloss">«… nào cũng được» — chưa xác định</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Lúc nào cũng được». Nói về tương lai: <b>Когда́-нибудь я пое́ду в '
    'Москву́</b> = Một ngày nào đó… Trong câu hỏi: <b>Ты когда́-нибудь был там?</b> = Bạn đã '
    'bao giờ ở đó chưa? Trả lời «chưa bao giờ» thì đổi sang <b>никогда́ не</b>.</div>'
    '<div class="hd-warn">Đã xảy ra thật trong quá khứ ⇒ <b>когда́-то</b> = ngày xưa, đã có '
    'lúc. <b>-нибудь</b> chỉ cho lúc chưa xác định.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>когда́</b> khi nào · <b>никогда́</b> không bao giờ · '
    '<b>кто́-нибудь</b> bất kỳ ai · <b>что́-нибудь</b> bất cứ thứ gì</div>'
)

# ---------------------------------------------------------------------- ряд
S["ряд"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn «hàng, dãy», không chẻ được — nhưng là gốc của cả họ bên '
    'dưới.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một hàng thứ xếp nối nhau ⇒ hàng ghế, dãy nhà; nhiều việc nối nhau ⇒ '
    '«một loạt»: <b>ряд вопро́сов</b> một loạt câu hỏi (+ cách 2). Số nhiều nhấn đuôi: '
    '<b>ряды́</b>.</div>'
    '<div class="hd-warn">Cách 6 tách theo nghĩa: <b>в пе́рвом ряду́</b> = ở hàng đầu · <b>в '
    'ря́де слу́чаев</b> = trong một số trường hợp.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ря́дом</b> ngay cạnh · <b>поря́док</b> trật tự · <b>наряду́</b> '
    'ngang hàng với</div>'
)

# -------------------------------------------------------------------- более
S["более"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бол-</span>'
    '<span class="hd-gloss">LỚN, NHIỀU — cùng thân với <b>бо́льше</b>, <b>большо́й</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ее</span>'
    '<span class="hd-gloss">đuôi SO SÁNH HƠN</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Việc chính: đứng trước tính từ để dựng so sánh hơn, như <i>more</i>: '
    '<b>бо́лее интере́сный</b> thú vị hơn. Trước con số thì là «hơn, trên»: <b>бо́лее ста '
    'челове́к</b> hơn trăm người. Còn «nhiều hơn» đứng một mình (ăn nhiều hơn, biết nhiều hơn) thì nói '
    '<b>бо́льше</b>.</div>'
    '<div class="hd-warn">Hai cụm phải thuộc: <b>тем бо́лее</b> = huống chi, càng thêm · '
    '<b>бо́лее того́</b> = hơn thế nữa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бо́льше</b> nhiều hơn · <b>большо́й</b> to, lớn · '
    '<b>большинство́</b> đa số</div>'
)

# ------------------------------------------------------------ единственный
S["единственный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">един-</span>'
    '<span class="hd-gloss">MỘT — cùng gốc với <b>оди́н</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ственн-ый</span>'
    '<span class="hd-gloss">đuôi tính từ «mang tính»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Chỉ có MỘT» ⇒ duy nhất: <b>еди́нственный сын</b> con trai một. Hầu '
    'như chỉ dùng dạng dài; dạng ngắn giống đực chèn <b>-е-</b> (<b>еди́нственен</b>) và rất '
    'hiếm gặp.</div>'
    '<div class="hd-warn">Thuật ngữ ngữ pháp: <b>еди́нственное число́</b> = số ít.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оди́н</b> một · <b>еди́ный</b> thống nhất, duy nhất · '
    '<b>едини́ца</b> đơn vị, số 1</div>'
)

# ------------------------------------------------------------------ слишком
S["слишком"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с</span>'
    '<span class="hd-gloss">giới từ «VỚI» (+ cách 5)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лишком</span>'
    '<span class="hd-gloss">cách 5 của <b>ли́шек</b> «phần DƯ» — gốc của <b>ли́шний</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Kèm phần dư» ⇒ quá mức cần, gần như luôn là chê: <b>сли́шком до́рого</b> '
    'đắt quá · <b>сли́шком мно́го</b> quá nhiều.</div>'
    '<div class="hd-warn">Đừng lẫn với <b>о́чень</b> = rất (khen được): <b>о́чень краси́во</b> '
    'rất đẹp, nhưng <b>сли́шком краси́во</b> là đẹp tới mức thừa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ли́шний</b> thừa, dư</div>'
)

# ------------------------------------------------------------------ столько
S["столько"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Hư từ, không chẻ ra mảnh mang nghĩa riêng. Nhưng nó nằm trong một '
    'cặp: hỏi bằng <b>к-</b>, trỏ lại bằng <b>т-</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>ско́лько</b> bao nhiêu? → <b>сто́лько</b> bấy nhiêu, y như '
    '<b>как</b> → <b>так</b>. Cũng kéo danh từ sang cách 2: <b>сто́лько книг</b>, <b>сто́лько '
    'рабо́ты</b>.</div>'
    '<div class="hd-warn">Cụm hay gặp: <b>сто́лько же</b> = cũng chừng ấy · <b>не сто́лько…, '
    'ско́лько…</b> = không hẳn là… mà là…</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ско́лько</b> bao nhiêu · <b>не́сколько</b> một vài</div>'
)

# ---------------------------------------------------------------- посчитать
S["посчитать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố thể, KHÔNG mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">считать</span>'
    '<span class="hd-gloss">đếm, cho rằng — xem thẻ <b>счита́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thể HOÀN THÀNH của <b>счита́ть</b> ở nghĩa ĐẾM, TÍNH: đếm xong, tính ra '
    'một con số — <b>Посчита́й, ско́лько нас</b> = Đếm xem bọn mình bao nhiêu người. Chia đều: '
    '<b>посчита́ю, посчита́ешь</b>.</div>'
    '<div class="hd-warn">Nghĩa «cho rằng» thì vẫn dùng <b>счита́ть</b> là chính; '
    '<b>посчита́ть</b> ở nghĩa này hay gặp trong cụm <b>посчита́л ну́жным…</b> = thấy cần '
    'phải…</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>счита́ть</b> đếm, cho rằng · <b>счёт</b> hóa đơn, tỉ số · '
    '<b>чита́ть</b> đọc</div>'
)

# ------------------------------------------------------------------ считать
S["считать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">GỘP LẠI, cộng vào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-чит-</span>'
    '<span class="hd-gloss">gốc ĐẾM — cùng gốc <b>чита́ть</b> đọc, <b>счёт</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể, chia đều: <b>счита́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đếm gộp lại ⇒ ĐẾM, TÍNH; tính trong đầu ⇒ CHO RẰNG — y như <i>reckon</i> '
    'tiếng Anh cũng vừa «tính» vừa «nghĩ». <b>Я счита́ю, что…</b> = Tôi cho rằng…</div>'
    '<div class="hd-warn">Coi AI là GÌ: người ở cách 4, cái «là» ở cách 5 — <b>Я счита́ю его́ '
    'дру́гом</b> = Tôi coi anh ấy là bạn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>посчита́ть</b> đếm xong · <b>счёт</b> hóa đơn, tỉ số · '
    '<b>чита́ть</b> đọc · <b>расчёт</b> sự tính toán</div>'
)
