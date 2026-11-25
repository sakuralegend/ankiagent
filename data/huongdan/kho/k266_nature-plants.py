# -*- coding: utf-8 -*-
"""k266 — cây cỏ, sân khấu – tranh, quần áo, từ lẻ; trục là HÌNH ẢNH đặt tên lộ ra từ gốc (đinh, thổi, đốm, cổng, sồi).

Chỗ cần nhất quán với lô đã nạp:
(1) -вяз- BUỘC, THẮT: khớp вязать k252. (2) -влек- KÉO, LÔI + -а́-тельный: khớp увлекательный k221.
(3) про- QUA MẤT: khớp проиграть k140; сп- NGỦ: khớp выспаться k223. (4) врата́ dạng cổ của ворота: khớp k174.
(5) про-ду́к- «dẫn ra» + -ция: khớp продукция k163. (6) гвоздь ĐINH: khớp k203. (7) ду- THỔI: khớp дуть k227.
(8) душ-/дух- HƠI THỞ: khớp воздух k103. (9) -и́ческ-ий: khớp исторический k93. (10) -и́ст/-и́зм: khớp турист k69.
Họ hàng cố ý vắng: không có (từ nào cũng có họ thật).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "антракт": "giờ nghỉ giữa các màn, giờ nghỉ giữa buổi diễn",     # «màn nghỉ» không phải tiếng Việt
    "репродукция": "bản sao, tranh in lại, bản in lại",              # «bản in sao» không phải tiếng Việt
    "проспать": "ngủ quên, ngủ quá giấc, ngủ mà bỏ lỡ, ngủ suốt",     # + to sleep through (the night)
    "гвоздика": "hoa cẩm chướng, đinh hương",                        # + cloves
    "хвойный": "lá kim, thuộc cây lá kim",                           # «có mùi lá kim» ngoài gloss
    "душно": "ngột ngạt, bí hơi, oi bức",                            # «khó thở» ngoài gloss; + muggy / sultry
}

# ------------------------------------------------------------------ керамика
S["керамика"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кера́м-</span>'
    '<span class="hd-gloss">ĐẤT SÉT làm gốm — Hy Lạp <i>keramos</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ика</span>'
    '<span class="hd-gloss">đuôi danh từ mượn, giống cái = Anh <i>-ic(s)</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng là tiếng Anh <i>ceramics</i>; âm «k» của Hy Lạp tiếng Nga giữ nguyên thành <i>к</i>. '
    'Chỉ cả chất liệu, cả nghề, cả đống đồ gốm gom lại — danh từ khối, chỉ dùng số ít: '
    '<b>дре́вняя кера́мика</b> đồ gốm cổ.</div>'
    '<div class="hd-warn">Sang tính từ, trọng âm bị kéo về <i>-и́-</i>: <b>керами́ческая пли́тка</b> = gạch men ốp lát.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>керами́ческий</b> bằng gốm · <b>керами́ст</b> nghệ nhân gốm</div>'
)

# ------------------------------------------------------------------- гравюра
S["гравюра"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">грав-</span>'
    '<span class="hd-gloss">KHẮC — Pháp <i>graver</i>, như Anh <i>en-grave</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ю́ра</span>'
    '<span class="hd-gloss">đuôi mượn Pháp <i>-ure</i>, như <b>брошю́ра</b> cuốn sách mỏng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cái được khắc ra»: khắc hình lên gỗ hay kim loại, lăn mực rồi IN ra giấy — '
    'từ này chỉ tờ tranh in ra đó. Khắc trên gì thì <b>на</b> + cách 6: <b>гравю́ра на де́реве</b> tranh khắc gỗ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гравирова́ть</b> khắc, chạm · <b>гравёр</b> thợ khắc · <b>гравиро́вка</b> chữ / hình khắc</div>'
)

# ------------------------------------------------------------------ оперетта
S["оперетта"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">опер-</span>'
    '<span class="hd-gloss">OPERA — <b>о́пера</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́тта</span>'
    '<span class="hd-gloss">đuôi Ý «nhỏ, nhẹ» = <i>-ette</i> trong <i>kitchenette</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Opera nhỏ» ⇒ vở nhạc kịch vui, nhẹ nhàng, hát xen NÓI và nhảy. Trọng âm rời âm đầu của '
    '<b>о́пера</b> sang đuôi: <b>опере́тта</b>; viết hai <i>т</i>. Đi xem thì: '
    '<b>пойти́ на опере́тту</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>о́пера</b> opera · <b>о́перный</b> thuộc về opera · <b>опере́точный</b> thuộc operetta</div>'
)

# -------------------------------------------------------------- сатирический
S["сатирический"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сатир-</span>'
    '<span class="hd-gloss">TRÀO PHÚNG — <b>сати́ра</b> = Anh <i>satire</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ческ-ий</span>'
    '<span class="hd-gloss">đuôi tính từ cho từ mượn = Anh <i>-ical</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><i>satirical</i>: cười để VẠCH cái xấu, không chỉ để vui. Đuôi này luôn kéo trọng âm về '
    '<i>-и́-</i>: <b>сати́ра → сатири́ческий</b>, như <b>исто́рия → истори́ческий</b>. '
    'Hay gặp: <b>сатири́ческий расска́з</b> truyện trào phúng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сати́ра</b> sự trào phúng, văn trào phúng · <b>сати́рик</b> nhà văn trào phúng</div>'
)

# ------------------------------------------------------------------- антракт
S["антракт"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">антр-</span>'
    '<span class="hd-gloss">GIỮA — Pháp <i>entre</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́кт</span>'
    '<span class="hd-gloss">MÀN kịch — <b>акт</b>, Anh <i>act</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Pháp <i>entracte</i> «giữa hai màn» ⇒ giờ nghỉ khi xem kịch, hoà nhạc. Trong giờ nghỉ đó: '
    '<b>в антра́кте</b>. Vở có nghỉ giữa chừng: <b>спекта́кль с антра́ктом</b>.</div>'
    '<div class="hd-warn">Chỉ dùng cho buổi DIỄN. Nghỉ giữa giờ làm, giữa trận đấu là <b>переры́в</b>; '
    'ra chơi giữa hai tiết học là <b>переме́на</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>акт</b> màn kịch; hành vi · <b>актёр</b> diễn viên</div>'
)

# --------------------------------------------------------------- репродукция
S["репродукция"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ре-</span>'
    '<span class="hd-gloss">LẠI — Latin <i>re-</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-про-ду́к-</span>'
    '<span class="hd-gloss">«dẫn ra», làm ra — như <b>проду́кция</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ция</span>'
    '<span class="hd-gloss">= <i>-tion</i>, luôn giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Làm ra lại lần nữa» = <i>reproduction</i>. Ngoài đời từ này hay nói về TRANH: '
    'bản in lại của một bức tranh, đăng trong sách hay treo tường. Của bức nào thì cách 2: '
    '<b>репроду́кция карти́ны</b>.</div>'
    '<div class="hd-warn"><b>ко́пия</b> rộng hơn: bản sao giấy tờ, tệp, kể cả tranh người ta VẼ lại. '
    '<b>репроду́кция</b> là bản IN lại.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>проду́кция</b> hàng sản xuất ra · <b>проду́кт</b> sản phẩm · '
    '<b>репродукти́вный</b> thuộc sinh sản</div>'
)

# ------------------------------------------------------------------ дублёнка
S["дублёнка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дубл-ён-</span>'
    '<span class="hd-gloss">ĐÃ THUỘC (da) — <b>дублёный</b>, từ <b>дуби́ть</b> thuộc da</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">gói «tính từ + danh từ» lại thành một danh từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Da xưa được thuộc bằng vỏ cây SỒI — <b>дуб</b> → <b>дуби́ть</b> → <b>дублёный</b>. '
    'Áo may từ da cừu thuộc, lông quay vào TRONG; <b>шу́ба</b> thì lông ở ngoài.</div>'
    '<div class="hd-warn">Chú ý bảng chia: cách 2 số nhiều chen <i>о</i> trước <i>к</i> — <b>мно́го дублёнок</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дуб</b> cây sồi · <b>дуби́ть</b> thuộc da · <b>дублёный</b> đã thuộc</div>'
)

# ------------------------------------------------------------------- вязаный
S["вязаный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вя́з-а-</span>'
    '<span class="hd-gloss">BUỘC, THẮT ⇒ đan — <b>вяза́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">→ tính từ «được làm bằng cách đó»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đồ được thắt từng mắt sợi ⇒ đan, móc: <b>вя́заный сви́тер</b>, <b>вя́заная ша́пка</b>. '
    'Trọng âm lùi về đầu so với động từ: <b>вяза́ть → вя́заный</b>.</div>'
    '<div class="hd-warn">Một <i>н</i> vì từ động từ CHT, đứng một mình. Từ HT <b>связа́ть</b> thì hai <i>н</i>: '
    '<b>свя́занный</b> — đan xong; bị trói; có liên quan.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вяза́ть</b> đan, buộc · <b>вяза́ние</b> việc đan lát · <b>завяза́ть</b> buộc, thắt · '
    '<b>связь</b> mối liên hệ</div>'
)

# ----------------------------------------------------------- развлекательный
S["развлекательный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раз-</span>'
    '<span class="hd-gloss">TẢN RA, về các phía</span></div>'
    '<div class="hd-row"><span class="hd-piece">-влек-</span>'
    '<span class="hd-gloss">KÉO, LÔI — như <b>увлека́ться</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́-тельный</span>'
    '<span class="hd-gloss">«có sức gây ra việc đó»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Kéo đầu óc TẢN RA khỏi việc ⇒ để giải trí; hình ảnh giống hệt <i>dis-tract</i>. '
    'Dạng ngắn giống đực chèn <i>е</i>, trọng âm đứng yên: '
    '<b>развлека́телен</b>, <b>развлека́тельна</b>.</div>'
    '<div class="hd-warn"><b>торго́во-развлека́тельный центр</b> (viết tắt ТРЦ) = trung tâm mua sắm giải trí, '
    'hay thấy trên biển hiệu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>развлека́ть</b> giúp vui · <b>развлече́ние</b> trò giải trí · '
    '<b>увлека́тельный</b> cuốn hút · <b>привлека́тельный</b> hấp dẫn</div>'
)

# ------------------------------------------------------------------ проспать
S["проспать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">QUA MẤT, làm tới mức lỡ — như <b>проигра́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-сп-ать</span>'
    '<span class="hd-gloss">NGỦ — <b>спать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ngủ mà để lỡ: <b>Я проспа́л!</b> Tôi ngủ quên! Lỡ CÁI GÌ → cách 4: <b>проспа́ть по́езд</b>. '
    'Kèm khoảng thời gian thì <i>про-</i> là «TRỌN»: <b>проспа́ть весь день</b> ngủ suốt ngày.</div>'
    '<div class="hd-warn">Chú ý bảng chia: như <b>спать</b>, chỉ ngôi «tôi» chèn <i>л</i> — <b>просплю́</b>, <b>проспи́шь</b>; '
    'quá khứ chỉ giống cái nhấn đuôi — <b>проспала́</b>.</div>'
    '<div class="hd-warn"><b>просыпа́ться</b> không phải cặp của từ này: nó là «tỉnh dậy», cặp của <b>просну́ться</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>спать</b> ngủ · <b>вы́спаться</b> ngủ đủ giấc · <b>сон</b> giấc ngủ · '
    '<b>просну́ться</b> tỉnh dậy</div>'
)

# ----------------------------------------------------------------- альпинист
S["альпинист"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">альпин-</span>'
    '<span class="hd-gloss">thuộc dãy ALPS — <b>А́льпы</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ст</span>'
    '<span class="hd-gloss">NGƯỜI làm việc đó, luôn mang trọng âm — như <b>тури́ст</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Người của dãy Alps» = Anh <i>alpinist</i>: môn leo núi cao ra đời ở đó, rồi gọi chung cho '
    'mọi dãy núi. Đổi đuôi ra tên môn: <b>альпини́ст ↔ альпини́зм</b>, y như <b>тури́ст ↔ тури́зм</b>.</div>'
    '<div class="hd-warn"><b>альпини́ст</b> chinh phục ĐỈNH núi; người leo vách đá là <b>скалола́з</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>альпини́зм</b> môn leo núi · <b>альпини́стка</b> nữ vận động viên leo núi · '
    '<b>А́льпы</b> dãy Alps</div>'
)

# ------------------------------------------------------------------- вратарь
S["вратарь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">врат-</span>'
    '<span class="hd-gloss">CỔNG — <b>врата́</b>, dạng cổ của <b>воро́та</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́рь</span>'
    '<span class="hd-gloss">NGƯỜI làm việc đó — như <b>библиоте́карь</b> thủ thư</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Người giữ cổng» mà <b>воро́та</b> cũng là khung thành ⇒ thủ môn. '
    '<i>-ра-</i> cổ ứng với <i>-оро-</i> thường ngày: <b>врата́ – воро́та</b>, <b>град – го́род</b>. '
    'Không dính gì tới <b>врать</b> nói dối.</div>'
    '<div class="hd-warn">Chú ý bảng chia: hễ có đuôi là trọng âm xuống đuôi — <b>вратаря́</b>, <b>вратарём</b>, '
    '<b>вратари́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>воро́та</b> cổng, khung thành · <b>врата́</b> cổng (cổ, trang trọng)</div>'
)

# ------------------------------------------------------------------ гвоздика
S["гвоздика"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">гвозд-</span>'
    '<span class="hd-gloss">CÁI ĐINH — <b>гвоздь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ка</span>'
    '<span class="hd-gloss">đuôi hay gặp ở tên cây, quả — như <b>голуби́ка</b> việt quất</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nụ gia vị khô trông như cái đinh ⇒ ĐINH hương, tiếng Việt cũng gọi theo đinh. '
    'Hoa cẩm chướng mang chung tên; thường giải thích là vì mùi nó giống đinh hương.</div>'
    '<div class="hd-warn">Cẩm chướng đỏ là hoa TƯỞNG NIỆM: ngày 9/5 người Nga đặt <b>кра́сные гвозди́ки</b> ở đài liệt sĩ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гвоздь</b> cái đinh · <b>гво́здик</b> cái đinh nhỏ (trọng âm đầu, giống đực)</div>'
)

# ------------------------------------------------------------------- ромашка
S["ромашка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được bằng tiếng Nga ngày nay; <i>-ка</i> ở cuối chỉ là đuôi giống cái quen mặt.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bông cúc dại cánh trắng nhuỵ vàng. Pha uống là <b>рома́шковый чай</b> trà hoa cúc. '
    'Chú ý bảng chia: cách 2 số nhiều chen <i>е</i> — <b>буке́т рома́шек</b>.</div>'
    '<div class="hd-warn"><b>гада́ть на рома́шке</b> = bứt từng cánh bói tình duyên: <b>лю́бит — не лю́бит</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рома́шковый</b> thuộc hoa cúc dại, làm từ hoa cúc</div>'
    '<div class="hd-warn">⚠️ Mức tin: tên thường được giải thích từ Latin <i>romana</i> «(cúc) La Mã», '
    'qua tiếng Ba Lan — từ nguyên, không phải luật suy ra được.</div>'
)

# -------------------------------------------------------------------- рябина
S["рябина"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ряб-</span>'
    '<span class="hd-gloss">LỐM ĐỐM — <b>рябо́й</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́на</span>'
    '<span class="hd-gloss">đuôi hay gặp ở tên cây — như <b>оси́на</b> dương lá rung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cây lốm đốm những chùm quả đỏ cam. Một từ cho cả CÂY lẫn QUẢ; '
    'nói quả thì dùng số ít gom cả mớ: <b>варе́нье из ряби́ны</b> mứt quả thanh lương trà.</div>'
    '<div class="hd-warn">⚠️ Mức tin: nối với <b>рябо́й</b> là từ nguyên, không phải luật suy ra được. '
    'Nghĩa hiếm «vết rỗ» của từ này thì rõ là từ <b>рябо́й</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ряби́новый</b> thuộc cây thanh lương trà · <b>рябо́й</b> lốm đốm, mặt rỗ · '
    '<b>рябь</b> gợn sóng lăn tăn</div>'
)

# ------------------------------------------------------------------- хвойный
S["хвойный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">хво́й-</span>'
    '<span class="hd-gloss">LÁ KIM — <b>хво́я</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">→ tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nói về cây có lá kim như <b>сосна́</b>, <b>ель</b>: <b>хво́йный лес</b> rừng lá kim. '
    'Phía bên kia là <b>ли́ственный лес</b> rừng lá rộng, từ <b>лист</b>.</div>'
    '<div class="hd-warn">Chú ý bảng: dạng ngắn giống đực đổi <i>й</i> thành <i>е</i> — <b>хво́ен</b>, nhưng <b>хво́йна</b>. '
    'Tính từ chỉ LOẠI nên hầu như không ai dùng dạng ngắn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>хво́я</b> lá kim, cành lá kim · <b>хвои́нка</b> một chiếc lá kim</div>'
)

# ----------------------------------------------------------------- одуванчик
S["одуванчик"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">QUANH, khắp mọi phía</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ду-в-</span>'
    '<span class="hd-gloss">THỔI — <b>дуть</b>; <i>в</i> chen giữa như <b>надува́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́н-чик</span>'
    '<span class="hd-gloss"><i>-чик</i> gọi nhỏ, thân mật</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bông hoa thổi một cái là bay tứ phía ⇒ bồ công anh. Gọi cho cả bông vàng lẫn chòm bông trắng: '
    '<b>дуть на одува́нчик</b> thổi bồ công anh.</div>'
    '<div class="hd-warn"><b>бо́жий одува́нчик</b> (đùa) = bà cụ hiền lành, mảnh khảnh như gió thổi là bay.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дуть</b> thổi · <b>поду́ть</b> thổi (HT) · <b>наду́ть</b> bơm phồng · '
    '<b>надувно́й</b> bơm hơi</div>'
)

# --------------------------------------------------------------------- душно
S["душно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">душ-</span>'
    '<span class="hd-gloss">HƠI THỞ — <b>дух</b>, <i>х</i> hoá <i>ш</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-о</span>'
    '<span class="hd-gloss">từ tính từ <b>ду́шный</b>, thay đuôi bằng <i>-о</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỗ làm hơi thở nặng nề ⇒ ngột ngạt. Nói trống, không chủ ngữ; ai thấy thì cách 3: '
    '<b>Здесь ду́шно</b>, <b>Мне ду́шно</b>. Khác <b>жа́рко</b> nóng: ở đây là thiếu không khí.</div>'
    '<div class="hd-warn"><b>душ</b> vòi sen KHÁC gốc (mượn Pháp <i>douche</i>). Còn <b>равноду́шно</b> thờ ơ thì có: '
    '<i>душ-</i> của nó là <b>душа́</b>, cũng từ «hơi thở».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ду́шный</b> ngột ngạt · <b>духота́</b> sự ngột ngạt · <b>дыша́ть</b> thở · '
    '<b>во́здух</b> không khí</div>'
)

B = {
    "docbangmat": 74,
    "loitubat": 2,   # керамика (lời giải «c Latin → к» sai đường mượn) · репродукция («gần như chỉ nói về tranh» quá tay)
    "nguonsai": 4,   # nghĩa Việt có sẵn: «màn nghỉ», «bản in sao» không phải tiếng Việt; «có mùi lá kim», «khó thở» ngoài gloss
    "baolen": [
        "V cần duyệt: гвоздика thêm «đinh hương» (gloss cloves) · проспать thêm «ngủ suốt» (sleep through) · душно bỏ «khó thở», thêm «oi bức»",
        "V cần duyệt: антракт, репродукция, хвойный thay cụm nghe không tự nhiên / ngoài gloss",
        "Không chắc tuyệt đối: hoa cẩm chướng mang tên đinh hương vì mùi (thẻ viết «thường giải thích») · рябина < рябой, ромашка < romana (đã ghi Mức tin)",
        "Topic của lô là nature::plants nhưng 13/18 từ không phải cây cỏ — tag chủ đề của từng thẻ không do file lô quyết",
    ],
}
