# -*- coding: utf-8 -*-
"""k258 — concepts::state (nhà nước, chính trị) + qualities::eval: trục là GỐC đã học + từ quốc tế đối chiếu tiếng Anh.

Chỗ cần nhất quán với lô đã nạp:
(1) у- làm cho TRỞ NÊN + so sánh hơn + -е́ние: khớp улучшение k221. (2) у-да-ч-: khớp уда́чный k190; -лив- «có tính…»: khớp терпеливый k226.
(3) без- KHÔNG CÓ: khớp безграничный k248; -образ-: khớp разнообразный k197; -дар-: khớp даром k250. (4) гуман-: khớp гуманитарный k146.
(5) ввоз/вывоз: в- VÀO, вы- RA NGOÀI + -воз CHỞ: khớp вывозить k224. (6) демо-, -крат-: khớp демократ k221, демократический k138.
(7) -итет = -ity: khớp авторитет k204. (8) -и́рова-ть chia -у-: khớp рекламировать k256. (9) -ящ- «ĐANG»: khớp служащий k233.
(10) вол- Ý MUỐN: khớp воля k159; -ев-о́й: khớp нулевой k236. Họ hàng cố ý vắng: không có (từ nào cũng có họ thật).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "ухудшение": "sự xấu đi, sự tệ đi, sự suy giảm",            # «sự tệ hơn» không thành tiếng Việt
    "удачливый": "hay gặp may, may mắn, thành công",                         # rút «hên» (khẩu ngữ, của везу́чий k244)
    "безобразный": "xấu xí, gớm ghiếc, quá quắt, tệ hại",       # «kinh khủng» là ужа́сный; «bỉ ổi» là по́длый
    "гуманный": "nhân đạo, nhân ái",                            # rút «nhân văn» (của гуманита́рный k146)
    "бездарный": "bất tài, kém cỏi, dở tệ, nhạt nhẽo",          # «vô tài» không thành tiếng Việt
    "плодотворный": "có kết quả tốt, nhiều thành quả, hiệu quả",  # «bổ ích» là поле́зный
    "ввоз": "nhập khẩu, việc chở vào, việc đưa vào",            # khuôn chung với вывоз
    "вывоз": "xuất khẩu, việc chở ra, việc chở đi",
    "демографический": "thuộc nhân khẩu học, thuộc dân số",     # «nhân khẩu, dân số» đọc ra danh từ
    "консервативный": "bảo thủ",                                # «cổ hủ» nới rộng
    "демократичный": "dân chủ, bình dân, giản dị, gần gũi, phải chăng",  # + affordable / moderate (price)
    "бюрократ": "kẻ quan liêu, người câu nệ thủ tục, người câu nệ hình thức",  # «quan liêu» trơ là tính từ
    "оккупировать": "chiếm đóng, chiếm giữ",                    # «chiếm dụng» nới rộng; «chiếm» trơ là заня́ть k131
    "волевой": "có ý chí, cương nghị, thuộc về ý chí",          # rút «quyết đoán» (của реши́тельный k136); + volitional
}

# --------------------------------------------------------------- ухудшение
S["ухудшение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">làm cho TRỞ NÊN…</span></div>'
    '<div class="hd-row"><span class="hd-piece">-худш-</span>'
    '<span class="hd-gloss">TỆ HƠN — như <b>ху́дший</b> tệ nhất, <b>ху́же</b> tệ hơn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ние</span>'
    '<span class="hd-gloss">đuôi danh từ, giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Khuôn y hệt <b>улучше́ние</b>, chỉ đổi lõi: <b>лу́чше → улу́чшить → '
    'улучше́ние</b>; <b>ху́же → уху́дшить → ухудше́ние</b>. Việc trở nên tệ hơn ⇒ sự xấu đi. Xấu đi CÁI GÌ '
    'thì cách 2: <b>ухудше́ние здоро́вья</b> sức khoẻ sa sút, <b>ухудше́ние пого́ды</b> thời tiết xấu '
    'đi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уху́дшить</b> / <b>ухудша́ть</b> làm tệ đi · <b>уху́дшиться</b> tệ đi · '
    '<b>ху́дший</b> tệ nhất · <b>улучше́ние</b> sự cải thiện (cặp ngược)</div>'
)

# --------------------------------------------------------------- удачливый
S["удачливый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-да́-ч-</span>'
    '<span class="hd-gloss">VẬN MAY — <b>уда́ча</b>, «cái được trao cho» (<i>-да-</i> CHO)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лив-ый</span>'
    '<span class="hd-gloss">→ tính từ «có tính…», như <b>терпели́вый, счастли́вый</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người mà <b>уда́ча</b> cứ theo hoài ⇒ may mắn; làm gì được nấy ⇒ thành công: '
    '<b>уда́чливый бизнесме́н</b>. Trọng âm giữ ở <i>-да́-</i> như <b>уда́ча</b>. Gần như chỉ nói về '
    'NGƯỜI.</div>'
    '<div class="hd-warn">Cùng gốc, khác chủ nhân: VIỆC trót lọt là <b>уда́чный</b> (<b>уда́чный '
    'день</b>), NGƯỜI may là <b>уда́чливый</b>. <b>везу́чий</b> cũng là người may, nhưng khẩu ngữ hơn '
    '(hên).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уда́ча</b> may mắn · <b>уда́чный</b> trót lọt · <b>неуда́чник</b> kẻ thất bại '
    '· <b>уда́ться</b> thành, làm được</div>'
)

# ------------------------------------------------------------- безобразный
S["безобразный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">без-</span>'
    '<span class="hd-gloss">KHÔNG CÓ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-обра́з-</span>'
    '<span class="hd-gloss">HÌNH DẠNG, hình ảnh — <b>о́браз</b>, như <b>разнообра́зный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Không còn ra hình dạng gì» ⇒ xấu xí, gớm ghiếc; chuyển sang hành vi ⇒ «không ra '
    'thể thống gì», quá quắt: <b>безобра́зное поведе́ние</b> cách cư xử quá quắt. Dạng ngắn giống đực chen '
    '<i>е</i>: <b>безобра́зен</b>.</div>'
    '<div class="hd-warn"><b>Э́то безобра́зие!</b> = Thật không ra thể thống gì! — câu phàn nàn rất hay '
    'nghe.</div>'
    '<div class="hd-warn">Trọng âm giữ nghĩa: <b>безобра́зный</b> xấu xí. Nhấn <b>безо́бразный</b> là từ '
    'khác, thuật ngữ «không có hình tượng».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>безобра́зие</b> điều quá quắt · <b>о́браз</b> hình ảnh · <b>образе́ц</b> mẫu · '
    '<b>разнообра́зный</b> đa dạng</div>'
)

# ---------------------------------------------------------------- гуманный
S["гуманный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">гума́н-</span>'
    '<span class="hd-gloss">CON NGƯỜI, tính người (Latin <i>humanus</i>, như <i>human</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ ⇒ hai chữ <i>н</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= <i>humane</i>: đối xử cho ra con người ⇒ nhân đạo, nhân ái. Chữ <i>h</i> Latin '
    'sang tiếng Nga thành <i>г</i>. <b>гума́нное отноше́ние к живо́тным</b> đối xử nhân đạo với động vật '
    '(<b>к</b> + cách 3). Dạng ngắn giống đực chen <i>е</i>: <b>гума́нен</b>.</div>'
    '<div class="hd-warn"><i>humane</i> ↔ <i>humanitarian</i>: <b>гума́нный</b> tả TẤM LÒNG, cách đối xử; '
    '<b>гуманита́рный</b> chỉ LĨNH VỰC (<b>гуманита́рная по́мощь</b> viện trợ nhân đạo).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гума́нность</b> lòng nhân đạo · <b>гумани́зм</b> chủ nghĩa nhân văn · '
    '<b>гумани́ст</b> người theo chủ nghĩa nhân văn · <b>гуманита́рный</b> nhân văn, nhân đạo</div>'
)

# --------------------------------------------------------------- бездарный
S["бездарный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">без-</span>'
    '<span class="hd-gloss">KHÔNG CÓ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-да́р-</span>'
    '<span class="hd-gloss">MÓN QUÀ — <b>дар</b>, ở đây là quà trời cho: tài năng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Y hệt Anh <i>gift</i> → <i>ungifted</i>: không được trời cho món nào ⇒ bất tài. '
    'Nói cả về người lẫn thứ họ làm ra: <b>безда́рный актёр</b> diễn viên bất tài, <b>безда́рный фильм</b> '
    'phim dở tệ. Dạng ngắn giống đực chen <i>е</i>: <b>безда́рен</b>.</div>'
    '<div class="hd-warn">Lời chê NẶNG. Trái nghĩa: <b>тала́нтливый</b>, <b>одарённый</b> (<i>gifted</i> — '
    '«được tặng quà»).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дар</b> món quà, tài năng · <b>безда́рность</b> sự bất tài; kẻ bất tài · '
    '<b>одарённый</b> có năng khiếu · <b>дари́ть</b> tặng</div>'
)

# ------------------------------------------------------------ закономерный
S["закономерный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">закон-о-</span>'
    '<span class="hd-gloss">LUẬT, quy luật — <b>зако́н</b>; <i>о</i> nối hai gốc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ме́р-</span>'
    '<span class="hd-gloss">ĐO, mức — <b>ме́ра</b>, như <b>изме́рить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đúng theo thước đo của quy luật» ⇒ hợp quy luật, tất yếu: <b>закономе́рный '
    'результа́т</b> kết quả tất yếu. Dạng ngắn giống đực chen <i>е</i>: <b>закономе́рен</b>; câu hay gặp: '
    '<b>Э́то закономе́рно</b> — chuyện tất yếu thôi.</div>'
    '<div class="hd-warn"><b>зако́нный</b> là hợp PHÁP luật (nhà nước đặt); <b>закономе́рный</b> là hợp '
    'QUY luật (sự việc tự nó phải thế).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>закономе́рность</b> tính quy luật · <b>зако́н</b> luật · <b>ме́ра</b> thước '
    'đo, mức độ · <b>равноме́рный</b> đều đặn</div>'
)

# ------------------------------------------------------------ плодотворный
S["плодотворный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">плод-о-</span>'
    '<span class="hd-gloss">QUẢ, trái — <b>плод</b>; <i>о</i> nối hai gốc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тво́р-</span>'
    '<span class="hd-gloss">TẠO RA — <b>твори́ть</b>, như <b>тво́рчество</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Tạo ra quả» — đúng hình ảnh của <i>fruitful</i> ⇒ có kết quả tốt, nhiều thành '
    'quả: <b>плодотво́рная рабо́та</b>, <b>плодотво́рное сотру́дничество</b> hợp tác hiệu quả. Dạng ngắn '
    'giống đực chen <i>е</i>: <b>плодотво́рен</b>.</div>'
    '<div class="hd-warn">Chỉ dùng nghĩa BÓNG (công việc, ý tưởng). Đất màu mỡ thì là <b>плодоро́дный</b> '
    '(«sinh ra quả»).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>плод</b> quả; thành quả · <b>плодоро́дный</b> màu mỡ · <b>твори́ть</b> sáng '
    'tạo · <b>тво́рческий</b> sáng tạo (tính từ)</div>'
)

# ---------------------------------------------------------------- цениться
S["цениться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">цен-</span>'
    '<span class="hd-gloss">GIÁ — <b>цена́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">ở đây: ĐƯỢC người ta… (bị động)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>цени́ть</b> là quý cái gì; thêm <i>-ся</i> thì chính cái đó được quý ⇒ được '
    'đánh giá cao, có giá trị: <b>Хоро́шие специали́сты высоко́ це́нятся.</b> Người giỏi rất được coi '
    'trọng. Gần như chỉ gặp ngôi 3, trọng âm lùi về gốc: <b>це́нится, це́нятся</b> (còn ngôi «tôi» ở đuôi '
    'như <b>ценю́</b>).</div>'
    '<div class="hd-warn"><b>цени́ться на вес зо́лота</b> = quý như vàng (tính theo cân vàng).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>цени́ть</b> quý trọng · <b>цена́</b> giá · <b>це́нный</b> có giá trị · '
    '<b>оцени́ть</b> đánh giá</div>'
)

# ------------------------------------------------------------- равноправие
S["равноправие"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">равн-о-</span>'
    '<span class="hd-gloss">BẰNG NHAU — <b>ра́вный</b>; <i>о</i> nối hai gốc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пра́в-</span>'
    '<span class="hd-gloss">QUYỀN — <b>пра́во</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ие</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Quyền bằng nhau» ⇒ bình quyền: <b>равнопра́вие мужчи́н и же́нщин</b> nam nữ bình '
    'quyền. Đuôi <i>-ие</i> nên luôn giống trung, như <b>правосу́дие</b>.</div>'
    '<div class="hd-warn"><b>ра́венство</b> là bằng nhau nói chung (cả trong toán); <b>равнопра́вие</b> '
    'chỉ bằng nhau về QUYỀN.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>равнопра́вный</b> bình đẳng về quyền · <b>беспра́вный</b> vô quyền · '
    '<b>ра́венство</b> sự bình đẳng · <b>пра́во</b> quyền</div>'
)

# -------------------------------------------------------------------- ввоз
S["ввоз"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO TRONG, ở đây là vào nước mình</span></div>'
    '<div class="hd-row"><span class="hd-piece">-воз</span>'
    '<span class="hd-gloss">CHỞ — <b>вози́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Việc chở VÀO qua biên giới ⇒ nhập khẩu. Là <b>ввози́ть</b> bỏ đuôi, như '
    '<b>вход</b> từ <b>входи́ть</b>. Chở CÁI GÌ thì cách 2: <b>ввоз това́ров</b>. Vào đâu: <b>в</b> + cách '
    '4 — <b>ввоз в Росси́ю</b>.</div>'
    '<div class="hd-warn"><b>ввоз</b> ↔ <b>вы́воз</b> là cặp gốc Nga của <b>и́мпорт</b> ↔ <b>э́кспорт</b>. '
    'Nhớ viết HAI chữ <i>в</i>: một của tiền tố, một của gốc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ввози́ть</b> / <b>ввезти́</b> chở vào, nhập khẩu · <b>вы́воз</b> xuất khẩu, '
    'việc chở ra · <b>вози́ть</b> chở · <b>перево́зка</b> sự vận chuyển</div>'
)

# ------------------------------------------------------------------- вывоз
S["вывоз"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы́-</span>'
    '<span class="hd-gloss">RA NGOÀI, ở đây hay là ra khỏi nước</span></div>'
    '<div class="hd-row"><span class="hd-piece">-воз</span>'
    '<span class="hd-gloss">CHỞ — <b>вози́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Việc chở RA: ra khỏi nước ⇒ xuất khẩu (<b>вы́воз капита́ла</b> chuyển vốn ra nước '
    'ngoài), ra khỏi nhà ⇒ dọn đi, chở đi (<b>вы́воз му́сора</b> thu gom rác). Chở CÁI GÌ thì cách 2.</div>'
    '<div class="hd-warn">Động từ <b>вывози́ть</b> nhấn đuôi, nhưng danh từ bỏ đuôi thì trọng âm về tiền '
    'tố: <b>вы́воз</b>, <b>вы́ход</b>, <b>вы́вод</b>, <b>вы́бор</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вывози́ть</b> / <b>вы́везти</b> chở ra · <b>ввоз</b> nhập khẩu, việc chở vào · '
    '<b>перево́зка</b> sự vận chuyển</div>'
)

# --------------------------------------------------------- демографический
S["демографический"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">демо-</span>'
    '<span class="hd-gloss">Hy Lạp <i>demos</i> DÂN — như <b>демокра́т</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-граф-</span>'
    '<span class="hd-gloss">VIẾT, MÔ TẢ — như <b>геогра́фия</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ческий</span>'
    '<span class="hd-gloss">đuôi tính từ = Anh <i>-ic</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Mô tả dân cư» = <i>demographic</i> ⇒ thuộc dân số, nhân khẩu học. Khuôn '
    '<b>демогра́фия → демографи́ческий</b>, trọng âm rơi vào <i>и́</i> như <b>географи́ческий</b>. Hay '
    'gặp: <b>демографи́ческий кри́зис</b> khủng hoảng dân số, <b>демографи́ческий взрыв</b> bùng nổ dân '
    'số.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>демогра́фия</b> nhân khẩu học · <b>демо́граф</b> nhà nhân khẩu học · '
    '<b>демокра́тия</b> nền dân chủ · <b>биогра́фия</b> tiểu sử (cùng <i>-граф-</i>)</div>'
)

# ---------------------------------------------------------------- правящий
S["правящий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пра́в-</span>'
    '<span class="hd-gloss">điều khiển, CAI TRỊ — <b>пра́вить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ящ-ий</span>'
    '<span class="hd-gloss">«ĐANG làm» — lớp 2 thì <i>-ящ-/-ащ-</i>, như <b>слу́жащий</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Phân từ dựng từ ngôi «họ»: <b>пра́вят</b> bỏ <i>т</i> thêm <i>щий</i> → '
    '<b>пра́вящий</b> «đang cai trị» ⇒ cầm quyền. Hay gặp: <b>пра́вящая па́ртия</b> đảng cầm quyền, '
    '<b>пра́вящий класс</b> giai cấp thống trị.</div>'
    '<div class="hd-warn">Đừng lẫn với <b>пра́вый</b> (bên phải; đúng): <b>пра́вая па́ртия</b> là đảng '
    'cánh hữu, không phải đảng cầm quyền.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пра́вить</b> cai trị · <b>прави́тель</b> nhà cai trị · <b>прави́тельство</b> '
    'chính phủ · <b>управля́ть</b> điều hành</div>'
)

# ---------------------------------------------------------- консервативный
S["консервативный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">консерв-</span>'
    '<span class="hd-gloss">GIỮ GÌN — Latin <i>conservare</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ати́в-н-ый</span>'
    '<span class="hd-gloss">= Anh <i>-ative</i>, đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Muốn GIỮ nguyên cái cũ ⇒ bảo thủ = <i>conservative</i>: <b>консервати́вные '
    'взгля́ды</b> quan điểm bảo thủ. Dạng ngắn giống đực chen <i>е</i>: <b>консервати́вен</b>.</div>'
    '<div class="hd-warn">Trong y khoa không hề chê: <b>консервати́вное лече́ние</b> = điều trị bảo tồn, '
    'không mổ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>консерва́тор</b> người bảo thủ · <b>консервати́зм</b> chủ nghĩa bảo thủ · '
    '<b>консе́рвы</b> đồ hộp (thức ăn được «giữ») · <b>консервато́рия</b> nhạc viện</div>'
)

# -------------------------------------------------------------- суверенный
S["суверенный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сувере́н-</span>'
    '<span class="hd-gloss">CHỦ, người nắm quyền tối cao — Pháp <i>souverain</i>, Anh '
    '<i>sovereign</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ ⇒ hai chữ <i>н</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không ai đứng trên mình ⇒ có chủ quyền, tự chủ: <b>сувере́нное госуда́рство</b> '
    'quốc gia có chủ quyền. Dạng ngắn giống đực chen <i>е</i>: <b>сувере́нен</b>.</div>'
    '<div class="hd-warn">Nhìn giống <b>уве́ренный</b> (tự tin) nhưng không họ hàng gì: từ kia là gốc '
    '<i>-вер-</i> TIN.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>суверените́т</b> chủ quyền · <b>сувере́н</b> người nắm chủ quyền, quân chủ</div>'
)

# ----------------------------------------------------------- демократичный
S["демократичный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">демо-</span>'
    '<span class="hd-gloss">Hy Lạp <i>demos</i> DÂN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-крат-</span>'
    '<span class="hd-gloss">Hy Lạp <i>kratos</i> quyền cai trị</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́чн-ый</span>'
    '<span class="hd-gloss">đuôi tính từ, ở đây chỉ PHẨM CHẤT — như <b>практи́чный</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Có chất dân»: cư xử không kiểu cách ⇒ bình dân, gần gũi (<b>демократи́чный '
    'нача́льник</b> sếp dễ gần); giá dân thường trả được ⇒ phải chăng (<b>демократи́чные це́ны</b>). Dạng '
    'ngắn giống đực chen <i>е</i>: <b>демократи́чен</b>.</div>'
    '<div class="hd-warn"><i>-и́ческий</i> = THUỘC VỀ chế độ: <b>демократи́ческая страна́</b>. '
    '<i>-и́чный</i> = TÍNH CÁCH, phong cách: <b>демократи́чный стиль</b>. Cùng luật: <b>практи́ческий</b> '
    '↔ <b>практи́чный</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>демокра́тия</b> nền dân chủ · <b>демокра́т</b> người theo dân chủ · '
    '<b>демократи́ческий</b> dân chủ (chế độ)</div>'
)

# ----------------------------------------------------------------- делегат
S["делегат"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">делег-</span>'
    '<span class="hd-gloss">Latin <i>delegare</i> — CỬ ai đi thay mình</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́т</span>'
    '<span class="hd-gloss">đuôi Latin <i>-atus</i> «được …» ⇒ người ĐƯỢC cử</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= <i>delegate</i>: một người trong <b>делега́ция</b>. Cùng khuôn với '
    '<b>депута́т</b>. Đại biểu CỦA cuộc họp nào thì cách 2: <b>делега́т съе́зда</b> đại biểu đại hội; được '
    'cử từ đâu: <b>делега́т от Росси́и</b> (<b>от</b> + cách 2).</div>'
    '<div class="hd-warn"><b>делега́т</b> được cử đi dự MỘT cuộc họp, họp xong là hết vai; <b>депута́т</b> '
    'được bầu giữ ghế cả nhiệm kỳ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>делега́ция</b> phái đoàn · <b>делеги́ровать</b> cử đi, uỷ quyền</div>'
)

# ---------------------------------------------------------------- бюрократ
S["бюрократ"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бюро-</span>'
    '<span class="hd-gloss">VĂN PHÒNG, bàn giấy — <b>бюро́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-кра́т</span>'
    '<span class="hd-gloss">quyền cai trị; ở cuối từ chỉ NGƯỜI — như <b>демокра́т</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người «cai trị bằng bàn giấy» ⇒ kẻ quan liêu, câu nệ thủ tục = <i>bureaucrat</i>. '
    'Trọng âm ở <i>-кра́т</i> suốt bảng: <b>бюрокра́ты</b>.</div>'
    '<div class="hd-warn">Gần như luôn là lời CHÊ. Gọi trung tính: <b>госслу́жащий</b> công chức nhà nước; '
    '<b>чино́вник</b> quan chức (hơi chê).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бюрокра́тия</b> bộ máy quan liêu · <b>бюрократи́ческий</b> quan liêu (tính từ) '
    '· <b>бюро́</b> văn phòng · <b>аристокра́т</b> quý tộc</div>'
)

# ------------------------------------------------------------- суверенитет
S["суверенитет"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">суверен-</span>'
    '<span class="hd-gloss">CHỦ, người nắm quyền tối cao — Pháp <i>souverain</i>, Anh '
    '<i>sovereign</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ите́т</span>'
    '<span class="hd-gloss">= Anh <i>-ity</i>, danh từ giống đực — như <b>авторите́т, '
    'университе́т</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= <i>sovereignty</i>, chủ quyền. Trọng âm rời <b>сувере́нный</b> chạy xuống đuôi '
    '<i>-ите́т</i> rồi đứng yên. Chủ quyền CỦA ai: cách 2 — <b>суверените́т госуда́рства</b>; đối với cái '
    'gì: <b>над</b> + cách 5 — <b>суверените́т над о́стровом</b>.</div>'
    '<div class="hd-warn"><b>наруше́ние суверените́та</b> = sự xâm phạm chủ quyền — cụm thường trực trên '
    'thời sự.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сувере́нный</b> có chủ quyền · <b>сувере́н</b> người nắm chủ quyền, quân chủ</div>'
)

# ----------------------------------------------------------- реформировать
S["реформировать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ре-</span>'
    '<span class="hd-gloss">LẠI — tiền tố Latin, như <i>re-</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-форм-</span>'
    '<span class="hd-gloss">HÌNH DẠNG — <b>фо́рма</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́рова-ть</span>'
    '<span class="hd-gloss">đuôi động từ mượn; khi chia <i>-ова-</i> → <i>-у-</i>: '
    '<b>реформи́рую</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Nặn lại hình dạng» = <i>reform</i> ⇒ cải cách, cải tổ. Cải cách CÁI GÌ: cách 4 — '
    '<b>реформи́ровать систе́му образова́ния</b> cải cách hệ thống giáo dục. Một dạng dùng cho CẢ HAI '
    'thể.</div>'
    '<div class="hd-warn">Trọng âm khác nhau: <b>реформи́ровать</b> nhấn <i>и́</i>, còn '
    '<b>формирова́ть</b> (hình thành) nhấn <i>а́</i>: <b>реформи́рую</b> ↔ <b>формиру́ю</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рефо́рма</b> cải cách · <b>реформа́тор</b> nhà cải cách · <b>фо́рма</b> hình '
    'dạng · <b>формирова́ть</b> hình thành</div>'
)

# ------------------------------------------------------------ оккупировать
S["оккупировать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">оккуп-</span>'
    '<span class="hd-gloss">CHIẾM — Latin <i>occupare</i>, Anh <i>occupy</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́рова-ть</span>'
    '<span class="hd-gloss">đuôi động từ mượn; khi chia <i>-ова-</i> → <i>-у-</i>: '
    '<b>оккупи́рую</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= <i>occupy</i> bằng quân đội ⇒ chiếm đóng (cách 4): <b>оккупи́ровать '
    'страну́</b>, <b>оккупи́рованная террито́рия</b> vùng bị chiếm đóng. Viết hai <i>к</i> nhưng MỘT '
    '<i>п</i>. Một dạng dùng cho CẢ HAI thể.</div>'
    '<div class="hd-warn"><i>occupy</i> chỗ ngồi, chức vụ, thời gian thì KHÔNG dùng từ này mà dùng '
    '<b>занима́ть / заня́ть</b>: <b>заня́ть ме́сто</b> giữ chỗ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оккупа́ция</b> sự chiếm đóng · <b>оккупа́нт</b> kẻ chiếm đóng</div>'
)

# ----------------------------------------------------------------- волевой
S["волевой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вол-</span>'
    '<span class="hd-gloss">Ý MUỐN, ý chí — <b>во́ля</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ев-о́й</span>'
    '<span class="hd-gloss">đuôi danh từ → tính từ, nhấn ở cuối — như <b>нулево́й</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đầy <b>во́ля</b> ⇒ có ý chí, cương nghị: <b>волево́й челове́к</b>, <b>волево́й '
    'хара́ктер</b>, cả gương mặt cũng được: <b>волево́е лицо́</b>. Nghĩa gốc là «thuộc về ý chí»: '
    '<b>волево́е уси́лие</b> sự gắng sức của ý chí.</div>'
    '<div class="hd-warn"><b>волево́е реше́ние</b> = quyết định bằng ý chí, áp xuống không bàn cãi — nhiều '
    'khi là lời chê.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>во́ля</b> ý chí, tự do · <b>безво́льный</b> nhu nhược · <b>доброво́льный</b> '
    'tự nguyện · <b>позво́лить</b> cho phép</div>'
)

# loitubat 4: удачливый «ba chữ một gốc» (везучий khác gốc); закономерный измерить sai trọng âm → изме́рить;
# удачливый «chỉ nói về NGƯỜI» và бюрократ «luôn là lời chê» nói quá → «gần như».
B = {
    "docbangmat": 120,
    "loitubat": 4,
    "nguonsai": 0,
    "baolen": [
        "демократичный — демократический (k138) «dân chủ» vẫn nằm gọn trong đề này: «dân chủ» là nghĩa chính nên giữ; V thêm «gần gũi», «phải chăng» (gloss affordable/moderate price) để dãy dài hẳn. Không gỡ được từ trong lô.",
        "удачливый — V rút «hên» ⇒ «may mắn, thành công»; hết trùng trọn với везучий (k244) «may mắn, hên», còn chung «may mắn».",
        "гуманный — V rút «nhân văn», thêm «nhân ái» (humane) ⇒ «nhân đạo, nhân ái»; hết trùng trọn với гуманитарный (k146) «nhân văn, nhân đạo».",
        "волевой — V rút «quyết đoán» (решительный k136), thêm «thuộc về ý chí» (gloss volitional).",
        "безобразный — V bỏ «kinh khủng» (nghĩa của ужасный) và «bỉ ổi», thay bằng «gớm ghiếc, quá quắt, tệ hại» (hideous/outrageous/disgraceful). Cần duyệt.",
        "плодотворный — V bỏ «bổ ích» (полезный), консервативный — bỏ «cổ hủ», оккупировать — bỏ «chiếm dụng» và «chiếm» trơ (занимать/занять k131). Cần duyệt.",
        "делегат, закономерный, правящий, равноправие, суверенный, суверенитет, реформировать, цениться — giữ nguyên field tiếng Việt; «đại diện» ở делегат hơi rộng nhưng bỏ đi thì còn «đại biểu» trơ, gần депутат (k105).",
        "V mới CHƯA chạy lại vacham (người soạn không đụng Anki): nhờ luồng chính soi ввоз với импорт, оккупировать với завоевать.",
        "безобразный — chonId 8689 đúng (безобра́зный); thẻ có ô đỏ nhắc từ đồng tự безо́бразный.",
    ],
}
