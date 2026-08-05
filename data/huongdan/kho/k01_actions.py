# -*- coding: utf-8 -*-
"""k01 — actions: 15 động từ lõi, trục là GỐC + TIỀN TỐ (ид-, да-, зв-, бр-, каз-)
và chỗ thân từ đổi hình khi chia.

Soạn lại hoàn toàn theo chuẩn v3 (bản cũ theo chuẩn v1 dài gấp 4-5 lần, đã bỏ).
🔴 KHÔNG dựng biến khối dùng chung — xem README §3.
🔴 KHÔNG viết bảng chia: `congcu.py nap` tự nối bảng lúc ghi. Ở đây chỉ có
   MỘT CÂU chú ý đặt cuối thẻ, tức ngay phía trên bảng (chuẩn v3 mục C).
"""

S = {}
V = {}

# ------------------------------------------------------------------ ид- ĐI
S["идти"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ид-</span>'
    '<span class="hd-gloss">ĐI (thân hiện tại)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ти́</span>'
    '<span class="hd-gloss">đuôi nguyên thể cổ, chỉ còn ở vài động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là "đi" MỘT CHIỀU: đang trên đường tới một nơi cụ thể. '
    'Đi lại nhiều chiều, đi thường xuyên thì dùng <b>ходи́ть</b> — cùng một ý "đi" '
    'mà hai thân không suy được từ nhau, phải học thành cặp.</div>'
    '<div class="hd-warn">Nga dùng từ này rộng hơn tiếng Việt: tàu chạy, mưa rơi, '
    'phim đang chiếu. Cụm phải thuộc: <b>речь идёт о</b>… = "đang nói về…".</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пойти́</b> khởi hành, bắt đầu đi · <b>войти́</b> đi vào · '
    '<b>вы́йти</b> đi ra · <b>прийти́</b> đến, tới</div>'
    '<div class="hd-warn">⚠️ Quá khứ ĐỔI HẲN THÂN, không còn <b>ид-</b> nào: '
    '<b>шёл · шла · шло · шли</b> — thuộc riêng như một từ khác.</div>'
)
V['идти'] = 'đi, đi bộ, đang đi tới'

S["войти"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO, vào trong</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о-</span>'
    '<span class="hd-gloss">nguyên âm đệm cho đọc được</span></div>'
    '<div class="hd-row"><span class="hd-piece">-йти́</span>'
    '<span class="hd-gloss">= идти́ đi</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen "đi vào". Tiền tố <b>в-</b> trơ một phụ âm không '
    'đọc nổi trước <b>йти</b> nên phải chèn <b>о</b> vào giữa — chính chữ <b>о</b> đó '
    'còn ở lại trong quá khứ <b>вошёл</b>.</div>'
    '<div class="hd-warn">Vào ĐÂU thì dùng <b>в</b> + cách 4 (chỉ hướng), không phải '
    'cách 6: <b>войти́ в ко́мнату</b> = bước vào phòng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>входи́ть</b> đi vào (đang vào, thường vào) · '
    '<b>вход</b> lối vào, cửa vào · <b>вы́йти</b> đi ra (nghĩa ngược)</div>'
    '<div class="hd-warn">⚠️ Quá khứ mượn nguyên thân bất quy tắc của <b>идти́</b>: '
    '<b>вошёл · вошла́ · вошли́</b>.</div>'
)
V['войти'] = 'đi vào, bước vào'

S["выйти"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы́-</span>'
    '<span class="hd-gloss">RA, ra khỏi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-йти</span>'
    '<span class="hd-gloss">= идти́ đi</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">"Đi ra". Tiền tố <b>вы-</b> có nét riêng đáng ghi: ở động từ '
    'hoàn thành nó HÚT trọng âm về mình, nên <b>вы́йти · вы́шел · вы́йду</b> đều nhấn ở '
    '<b>вы</b> — khác hẳn <b>войти́</b> nhấn ở đuôi.</div>'
    '<div class="hd-warn">Nghĩa phái sinh phải biết: <b>вы́йти за́муж</b> = (người nữ) '
    'đi lấy chồng · sách <b>вы́шла</b> = sách đã ra, đã xuất bản.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>выходи́ть</b> đi ra (đang ra, thường ra) · '
    '<b>вы́ход</b> lối ra, cách thoát · <b>войти́</b> đi vào (nghĩa ngược)</div>'
    '<div class="hd-warn">⚠️ Quá khứ RỤNG chữ <b>й</b>: <b>вы́шел · вы́шла · вы́шли</b>, '
    'không phải *вы́йшел.</div>'
)
V['выйти'] = 'đi ra, bước ra, ra mắt, được xuất bản'

# ------------------------------------------------------------------ да- CHO
S["давать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">да-</span>'
    '<span class="hd-gloss">CHO, đưa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва-</span>'
    '<span class="hd-gloss">hậu tố "đang / thường xuyên"</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỉ khác <b>дать</b> đúng một mảnh <b>-ва-</b>, và mảnh đó '
    'chính là dấu hiệu "đang cho, hay cho". Thấy <b>-ва-</b> chen giữa gốc và '
    '<b>-ть</b> thì đoán được ngay đây là dạng kéo dài, lặp lại.</div>'
    '<div class="hd-warn">Cụm cửa miệng: <b>дава́й</b> / <b>дава́йте</b> = "nào, ta '
    'hãy…" — <b>дава́й пойдём</b> = mình đi thôi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дать</b> cho (một lần) · <b>отда́ть</b> đưa lại, trả · '
    '<b>прода́ть</b> bán · <b>зада́ние</b> việc được giao, bài tập</div>'
    '<div class="hd-warn">⚠️ Chia hiện tại thì BỎ HẲN <b>-ва-</b>: <b>даю́ · даёшь · '
    'даю́т</b>, không phải *дава́ю.</div>'
)
V['давать'] = 'đưa, cho, trao'

# ------------------------------------------------------------------ зв- GỌI
S["звать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">зв-/зов-</span>'
    '<span class="hd-gloss">GỌI, tiếng gọi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc này có hai mặt: nguyên thể rụng nguyên âm (<b>звать</b>), '
    'chia hiện tại thì <b>о</b> mọc trở lại (<b>зову́</b>). Nhờ đó nhớ luôn câu tự giới '
    'thiệu: <b>Меня́ зову́т</b>… nghĩa đen là "người ta gọi tôi là…".</div>'
    '<div class="hd-warn">Đừng lẫn với <b>звони́ть</b> = gọi ĐIỆN THOẠI. <b>звать</b> '
    'là gọi tên, gọi ai lại, mời ai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>зов</b> tiếng gọi · <b>позва́ть</b> gọi, mời (một lần) · '
    '<b>назва́ние</b> tên gọi, tiêu đề · <b>называ́ться</b> được gọi là</div>'
    '<div class="hd-warn">⚠️ Hiện tại MỌC thêm <b>о</b> và dồn trọng âm ra đuôi: '
    '<b>зову́ · зовёшь · зову́т</b>; quá khứ giống cái cũng nhảy: <b>звала́</b>.</div>'
)
V['звать'] = 'gọi, gọi tên, mời'

# ------------------------------------------------------------------ говор- NÓI
S["разговаривать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раз-</span>'
    '<span class="hd-gloss">tán ra, qua lại hai chiều</span></div>'
    '<div class="hd-row"><span class="hd-piece">-говар-</span>'
    '<span class="hd-gloss">NÓI (gốc của говори́ть)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ть</span>'
    '<span class="hd-gloss">hậu tố "đang / thường xuyên"</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: nói qua nói lại = trò chuyện. Vì <b>раз-</b> đã hàm '
    'ý hai chiều nên từ này luôn cần ĐỐI PHƯƠNG, khác <b>говори́ть</b> (nói, phát biểu) '
    'một mình cũng được.</div>'
    '<div class="hd-warn">Trò chuyện VỚI ai → <b>с</b> + cách 5: '
    '<b>разгова́ривать с дру́гом</b>. Nói VỀ cái gì → <b>о</b> + cách 6.</div>'
    '<div class="hd-warn">Từ này không có cặp thể riêng — muốn nói "trò chuyện một lúc '
    'rồi xong" thì dùng <b>поговори́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>говори́ть</b> nói · <b>разгово́р</b> cuộc nói chuyện · '
    '<b>разгово́рный</b> thuộc khẩu ngữ</div>'
)
V['разговаривать'] = 'nói chuyện, trò chuyện'

# ------------------------------------------------------------------ прос-/праш- HỎI
S["спрашивать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-праш-</span>'
    '<span class="hd-gloss">HỎI, XIN (biến thể của прос-)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ть</span>'
    '<span class="hd-gloss">hậu tố "đang / thường xuyên"</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc là <b>прос-</b> (xin, yêu cầu). Khi thêm <b>-ива-</b> thì '
    'gốc biến hai chỗ cùng lúc: <b>с→ш</b> và <b>о→а</b>, ra <b>спра́шивать</b>. Đây là '
    'phép biến âm gặp lại ở nhiều cặp thể khác, học một lần dùng mãi.</div>'
    '<div class="hd-warn">Hỏi AI → cách 4 (<b>спроси́ть его́</b>), hỏi VỀ gì → <b>о</b> '
    '+ cách 6.</div>'
    '<div class="hd-warn">Cùng gốc mà khác nghĩa, dễ lẫn: <b>проси́ть</b> = XIN, đề '
    'nghị — không phải hỏi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>спроси́ть</b> hỏi (một lần) · <b>проси́ть</b> xin, đề nghị · '
    '<b>вопро́с</b> câu hỏi · <b>про́сьба</b> lời đề nghị</div>'
)
V['спрашивать'] = 'hỏi, đặt câu hỏi'

# ------------------------------------------------------------------ польз- LỢI
S["использовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ис-</span>'
    '<span class="hd-gloss">= из- : lấy RA, dùng cho hết</span></div>'
    '<div class="hd-row"><span class="hd-piece">-польз-</span>'
    '<span class="hd-gloss">LỢI ÍCH (по́льза)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-овать</span>'
    '<span class="hd-gloss">hậu tố biến danh từ thành động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen "rút cái lợi ra khỏi vật" = sử dụng. Hậu tố '
    '<b>-овать</b> luôn chia thành <b>-ую</b>: <b>испо́льзую · испо́льзуешь</b>, và '
    'trọng âm đứng yên ở <b>по́ль-</b> suốt bảng.</div>'
    '<div class="hd-warn">Badge ghi BI-ASP: đây là động từ DÙNG CHUNG cho cả hai thể — '
    'một dạng duy nhất, không có cặp để chọn. Rất ít từ được vậy.</div>'
    '<div class="hd-warn">Đừng lẫn với <b>по́льзоваться</b> (cũng là "dùng") — từ đó đi '
    'với cách 5: <b>по́льзоваться телефо́ном</b>, còn từ này đi với cách 4.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>по́льза</b> lợi ích · <b>поле́зный</b> có ích, hữu dụng · '
    '<b>испо́льзование</b> việc sử dụng</div>'
)
V['использовать'] = 'sử dụng, dùng'

S["дать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">да-</span>'
    '<span class="hd-gloss">CHO, đưa — gốc một âm tiết, rất cổ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>да-</b> cùng nguồn Ấn–Âu với <i>do-</i> trong tiếng Anh '
    '<i>donate</i>, <i>data</i> ("thứ được cho") — bắc cầu này chắc chắn, không phải mẹo '
    'âm thanh. Gốc trơn một âm tiết nên không chẻ thêm được.</div>'
    '<div class="hd-warn">Đòi HAI cách một lúc: vật cho ở cách 4, người nhận ở cách 3 — '
    '<b>Дай мне кни́гу</b> = đưa tôi quyển sách.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дава́ть</b> cho (đang cho, hay cho) · <b>отда́ть</b> đưa lại, '
    'trả · <b>прода́ть</b> bán · <b>зада́ние</b> việc được giao</div>'
    '<div class="hd-warn">⚠️ Bảng chia BẤT QUY TẮC, phải thuộc: số ít đuôi ngắn trơ '
    '(<b>дам · дашь · даст</b>), số nhiều mọc thêm một âm tiết và dồn trọng âm ra đuôi '
    '(<b>дади́м · дади́те · даду́т</b>); quá khứ giống cái cũng nhảy: <b>дала́</b>.</div>'
)
V['дать'] = 'đưa, cho, trao, cho phép'

# ------------------------------------------------------------------ каз- CHỈ RA
S["рассказать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рас-</span>'
    '<span class="hd-gloss">= раз- : trải ra, khắp lượt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-каз-</span>'
    '<span class="hd-gloss">CHỈ RA, cho thấy, nói ra</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>каз-</b> là "chỉ ra, cho thấy" — thấy nó ở <b>сказа́ть</b> '
    '(nói ra một câu) và <b>показа́ть</b> (chỉ cho xem). Thêm <b>рас-</b> "trải ra khắp '
    'lượt" thành: trải cả câu chuyện ra từ đầu đến cuối = kể lại.</div>'
    '<div class="hd-warn">Kể CHO AI → cách 3: <b>расскажи́ мне</b> = kể tôi nghe (đây là '
    'dạng ra lệnh, dùng suốt trong hội thoại).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>расска́з</b> truyện ngắn, mẩu chuyện · <b>расска́зывать</b> kể '
    '(đang kể, hay kể) · <b>сказа́ть</b> nói · <b>ска́зка</b> truyện cổ tích</div>'
    '<div class="hd-warn">⚠️ Chia thì gốc biến âm <b>з→ж</b>, và trọng âm chỉ ở đuôi '
    'đúng ngôi "tôi" rồi lùi về gốc: <b>расскажу́</b> nhưng <b>расска́жешь · '
    'расска́жут</b>.</div>'
)
V['рассказать'] = 'kể lại, thuật lại'

# ------------------------------------------------------------------ дел- VIỆC
S["делать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">де́л-</span>'
    '<span class="hd-gloss">VIỆC, sự việc (де́ло)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ <b>де́ло</b> (việc) mà ra: "làm việc gì đó". Đây là mẫu chia '
    'DỄ NHẤT để đối chiếu: bỏ <b>-ть</b> rồi thêm đuôi, trọng âm không hề nhích — '
    '<b>де́лаю · де́лаешь · де́лают</b>.</div>'
    '<div class="hd-warn">Hai câu cửa miệng: <b>Что ты де́лаешь?</b> = bạn đang làm gì? · '
    '<b>Что де́лать?</b> = biết làm sao bây giờ?</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>де́ло</b> việc, chuyện (số nhiều <b>дела́</b>: '
    '<b>Как дела́?</b> = dạo này thế nào) · <b>сде́лать</b> làm xong · <b>неде́ля</b> tuần '
    '— gốc là "không làm việc", tức ngày nghỉ</div>'
)
V['делать'] = 'làm, thực hiện, chế tạo'

S["знать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">зна-</span>'
    '<span class="hd-gloss">BIẾT — gốc trơn, không chẻ thêm được</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>зна-</b> cùng nguồn Ấn–Âu với <i>know</i> và '
    '<i>diagnosis</i> trong tiếng Anh — nhận ra được thì khỏi phải học. Chia đúng quy '
    'tắc, trọng âm đứng yên: <b>зна́ю · зна́ешь</b>.</div>'
    '<div class="hd-warn">Từ điển hay ghép nó với <b>узна́ть</b>, nhưng <b>узна́ть</b> '
    'KHÔNG phải "biết xong" — nó là "biết THÊM ĐƯỢC, nhận ra". Bản thân <b>знать</b> chỉ '
    'có dạng đang biết.</div>'
    '<div class="hd-warn">Biết một điều / một người thì dùng từ này; biết LÀM được việc '
    'gì là <b>уме́ть</b>: <b>я уме́ю пла́вать</b> = tôi biết bơi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>зна́ние</b> kiến thức · <b>знако́мый</b> người quen; quen '
    'biết · <b>знак</b> dấu hiệu, biển báo · <b>узна́ть</b> biết được, nhận ra</div>'
)
V['знать'] = 'biết, quen biết'

# ------------------------------------------------------------------ бр-/бер- LẤY
S["брать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бр-/бер-</span>'
    '<span class="hd-gloss">LẤY, mang, gom</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng kiểu gốc rỗng như <b>звать</b> trong lô này: nguyên thể '
    'rụng nguyên âm (<b>брать</b>), chia hiện tại thì <b>е</b> mọc trở lại '
    '(<b>беру́</b>). Nhớ một cái là suy được cái kia.</div>'
    '<div class="hd-warn">Cặp thể là <b>взять</b> (lấy một lần rồi xong) — thân khác '
    'hoàn toàn (<b>возьму́ · возьмёшь</b>), không suy được, phải học riêng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вы́брать</b> chọn ra · <b>набра́ть</b> bấm số, gom cho đủ · '
    '<b>собра́ние</b> cuộc họp (gom người lại)</div>'
    '<div class="hd-warn">⚠️ Hiện tại MỌC thêm <b>е</b> và dồn trọng âm ra đuôi: '
    '<b>беру́ · берёшь · беру́т</b>; quá khứ giống cái cũng nhảy: <b>брала́</b>.</div>'
)
V['брать'] = 'lấy, cầm, mang đi, mượn, thuê'

# ------------------------------------------------------------------ раб- LAO ĐỘNG
S["работать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рабо́т-</span>'
    '<span class="hd-gloss">CÔNG VIỆC (рабо́та)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ <b>рабо́та</b> mà ra, và <b>рабо́та</b> lại từ <b>раб</b> '
    '(nô lệ) — nên gốc này mang sẵn nét "lao dịch, làm nặng", không phải "làm" chung '
    'chung. Chia đúng quy tắc, trọng âm dính chặt ở <b>-бо́-</b>.</div>'
    '<div class="hd-warn">Không nhận tân ngữ cách 4. Làm việc Ở đâu → <b>в/на</b> + cách '
    '6; làm NGHỀ gì → cách 5 trơn: <b>рабо́тать учи́телем</b> = làm giáo viên.</div>'
    '<div class="hd-warn">Nghĩa thứ hai dùng hằng ngày: máy móc "chạy được" — '
    '<b>телефо́н не рабо́тает</b> = điện thoại không hoạt động.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рабо́та</b> công việc · <b>рабо́чий</b> công nhân; thuộc về '
    'lao động · <b>раб</b> nô lệ · <b>зарабо́тать</b> kiếm được (tiền)</div>'
)
V['работать'] = 'làm việc, đi làm, chạy, hoạt động'

# ------------------------------------------------------------------ дых- HƠI THỞ
S["отдыхать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">RỜI KHỎI, tách ra</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дых-</span>'
    '<span class="hd-gloss">HƠI THỞ (дыша́ть thở)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen "thở phào rời khỏi việc" — đúng y cách tiếng Việt nói '
    '<i>nghỉ xả hơi</i>. Chẻ ra là nhớ được, khỏi cần mẹo gì thêm.</div>'
    '<div class="hd-warn">Người Nga dùng từ này cả cho ĐI DU LỊCH, đi nghỉ mát: '
    '<b>отдыха́ть на мо́ре</b> = đi nghỉ ở biển, không chỉ là ngồi nghỉ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>о́тдых</b> sự nghỉ ngơi · <b>дыша́ть</b> thở · '
    '<b>во́здух</b> không khí · <b>вздох</b> tiếng thở dài</div>'
    '<div class="hd-warn">⚠️ Cặp thể <b>отдохну́ть</b> (nghỉ một lát rồi xong) đổi gốc '
    '<b>дых→дох</b> và mọc thêm <b>-ну-</b> — nhận ra phép đổi này thì khỏi học lại.</div>'
)
V['отдыхать'] = 'nghỉ ngơi, xả hơi, đi nghỉ mát'
