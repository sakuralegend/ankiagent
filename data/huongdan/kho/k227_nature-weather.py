# -*- coding: utf-8 -*-
"""k227 — nature::weather: thời tiết, con vật, phố xá và hai cặp động từ bay (взлет-, вылет-).

Chỗ cần nhất quán trong lô:
(1) вла́жный chỉ ẨM; мо́крый [k128] ƯỚT; сыро́й [k201] ẩm ngấm / sống.
(2) вз- LÊN, bật lên — khớp вздохну́ть, вздыха́ть [k170]; вы- RA NGOÀI — khớp вы́пустить [k185].
(3) -лет-а́ть gốc BAY, có tiền tố thì chỉ còn là cặp CHT — khớp прилета́ть [k143].
(4) свети́ть TOẢ sáng ↔ освеща́ть soi CÁI GÌ — khớp [k225].
(5) банк-ома́т = банк + автома́т [k132]; край MÉP, RÌA NGOÀI CÙNG [k07]; вс- + -юду [k43]; от- TỪ [k86, k107].
(6) -перёк ↔ вопреки́ giữ ô «Mức tin» — khớp [k211].
Họ hàng không vắng ở thẻ nào.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "загрязнение": "sự ô nhiễm, sự làm bẩn, sự nhiễm bẩn",  # «nhiễm bẩn» trơ là động từ; contamination
    "влажный": "ẩm, ẩm ướt",  # RÚT «ướt» — đó là мо́крый (wet); gloss chỉ moist / damp / humid
    "подуть": "thổi, phả hơi, gió thổi, bắt đầu thổi, thổi một lúc",  # dãy của дуть + hai nghĩa gloss riêng của HT; RÚT «nổi lên» (đọc ra «nổi trên nước»)
    "взлететь": "bay lên, cất cánh, vút lên",  # «vút lên cao» → cùng dãy взлета́ть
    "вылететь": "bay ra, cất cánh, khởi hành, lao ra",  # RÚT «bay biến» (gloss không có) → cùng dãy вылета́ть
}

# --------------------------------------------------------------------- ворона
S["ворона"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn <b>ворон-</b> quạ; <b>-а</b> là đuôi giống cái.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Con quạ hay gặp ngoài phố, trọng âm đứng yên ở <b>-ро-</b>. Ai mải há miệng nhìn mà để '
    'lỡ việc cũng bị gọi là <b>воро́на</b> ⇒ người lơ đễnh.</div>'
    '<div class="hd-warn"><b>воро́на</b> ≠ <b>во́рон</b>: <b>во́рон</b> là con quạ LỚN đen tuyền, loài khác — '
    'không phải «quạ đực».</div>'
    '<div class="hd-warn"><b>бе́лая воро́на</b> = kẻ khác người, lạc loài (nghĩa đen: con quạ trắng).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>во́рон</b> quạ lớn · <b>воронёнок</b> quạ con · <b>вороно́й</b> (ngựa) đen '
    'tuyền</div>'
)

# --------------------------------------------------------------------- верблюд
S["верблюд"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: từ mượn cổ, nay là một khối.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không có mảnh nào để suy, học cả khối. Tính từ đổi <b>д → ж</b>: <b>верблю́жий</b> — '
    'hay gặp ở nhãn <b>верблю́жья шерсть</b> len lông lạc đà.</div>'
    '<div class="hd-warn">Đừng thấy <b>блю́до</b> món ăn trong đó: hai từ không cùng họ, chỉ giống mặt chữ.</div>'
    '<div class="hd-warn">⚠️ Mức tin: từ này mượn rất cổ qua tiếng Goth, vốn chung nguồn với <i>elephant</i> '
    '«con voi» rồi lệch âm — đây là từ nguyên, không phải luật suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>верблю́жий</b> thuộc lạc đà · <b>верблюжо́нок</b> lạc đà con</div>'
)

# --------------------------------------------------------------------- комар
S["комар"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trọng âm nhảy hẳn ra đuôi ngay khi thêm đuôi: <b>кома́р</b> → <b>комара́</b>, '
    '<b>комары́</b>, <b>комаро́в</b>. Bị muỗi đốt: <b>меня́ укуси́л кома́р</b>.</div>'
    '<div class="hd-warn"><b>кома́р но́са не подто́чит</b> = không chê vào đâu được (nghĩa đen: muỗi cũng không '
    'chọc nổi vòi vào).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кома́рик</b> con muỗi nhỏ · <b>комари́ный</b> thuộc muỗi: <b>комари́ный уку́с</b> '
    'vết muỗi đốt</div>'
)

# --------------------------------------------------------------------- наводнение
S["наводнение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span><span class="hd-gloss">TRÀN LÊN, phủ lên</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вод-</span><span class="hd-gloss">NƯỚC — '
    '<b>вода́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-е́ние</span><span class="hd-gloss">→ danh từ giống trung, từ '
    '<b>наводни́ть</b> làm ngập tràn</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Việc nước tràn lên» ⇒ lũ lụt. Nhìn gốc <b>вод-</b> là ra ngay nghĩa.</div>'
    '<div class="hd-warn">Gốc <b>вод-</b> NƯỚC ở đây khác gốc <b>вод-</b> DẪN của <b>води́ть</b> — '
    '<b>наводи́ть</b> (chĩa vào, gây ra) không dính gì tới nước.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вода́</b> nước · <b>наводни́ть</b> làm ngập tràn · <b>полово́дье</b> mùa nước lên · '
    '<b>подво́дный</b> dưới nước</div>'
)

# --------------------------------------------------------------------- загрязнение
S["загрязнение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span><span class="hd-gloss">làm cho DÍNH, phủ '
    'lên</span></div>'
    '<div class="hd-row"><span class="hd-piece">-гряз-н-</span><span class="hd-gloss">BẨN — <b>грязь</b> bùn, '
    'đất bẩn → <b>гря́зный</b> bẩn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ние</span><span class="hd-gloss">→ danh từ giống '
    'trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>загрязни́ть</b> làm bẩn. «Làm cho dính bẩn» ⇒ sự làm bẩn; làm bẩn nước, '
    'không khí ⇒ sự ô nhiễm. Cái bị bẩn đứng cách 2: <b>загрязне́ние во́здуха</b> ô nhiễm không khí.</div>'
    '<div class="hd-warn"><b>загрязне́ние окружа́ющей среды́</b> = ô nhiễm môi trường — cụm phải thuộc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>грязь</b> bùn, chất bẩn · <b>гря́зный</b> bẩn · <b>загрязня́ть</b> / '
    '<b>загрязни́ть</b> làm bẩn, gây ô nhiễm</div>'
)

# --------------------------------------------------------------------- влажный
S["влажный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">влаж-</span><span class="hd-gloss">HƠI ẨM — <b>вла́га</b>, <b>г '
    '→ ж</b> trước <b>-н-</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span><span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Có hơi ẩm». Dùng cho khí hậu, không khí, da, khăn: <b>вла́жный во́здух</b>. Dạng ngắn '
    'chèn <b>-е-</b> ở giống đực, nhấn đuôi ở giống cái: <b>вла́жен</b> · <b>влажна́</b> · <b>вла́жно</b>.</div>'
    '<div class="hd-warn">Ba từ: <b>вла́жный</b> chỉ HƠI ẨM · <b>сыро́й</b> ẩm ngấm bên trong, chưa khô, hay gợi '
    'khó chịu · <b>мо́крый</b> ƯỚT, đẫm nước.</div>'
    '<div class="hd-warn"><b>вла́жные салфе́тки</b> = khăn giấy ướt — tiếng Việt nói «ướt», tiếng Nga dùng chữ '
    'ẨM.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вла́га</b> hơi ẩm · <b>вла́жность</b> độ ẩm · <b>увлажни́ть</b> làm ẩm</div>'
)

# --------------------------------------------------------------------- светить
S["светить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">свет-</span><span class="hd-gloss">ÁNH SÁNG — '
    '<b>свет</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span><span class="hd-gloss">đuôi lớp chia thứ '
    'hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">TOẢ sáng: <b>Со́лнце све́тит</b> Mặt trời chiếu sáng. Ngôi «tôi» <b>т → ч</b> và nhấn '
    'đuôi, từ ngôi sau trọng âm lùi về gốc: <b>свечу́</b> → <b>све́тишь</b>, <b>све́тят</b>.</div>'
    '<div class="hd-warn">Soi cho ai → cách 3: <b>Свети́ мне сюда́!</b> Soi vào đây cho tôi! Muốn nói soi sáng '
    'CÁI GÌ (cách 4) thì dùng <b>освеща́ть</b>.</div>'
    '<div class="hd-warn"><b>свечу́</b> «tôi soi» trùng mặt chữ với cách 4 của <b>свеча́</b> cây nến — cùng gốc, '
    'cùng phép <b>т → ч</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>све́тлый</b> sáng · <b>свети́ться</b> phát sáng · <b>освети́ть</b> chiếu sáng (cái '
    'gì) · <b>рассве́т</b> bình minh · <b>свеча́</b> nến</div>'
)

# --------------------------------------------------------------------- дуть
S["дуть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ду-</span><span class="hd-gloss">gốc THỔI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span><span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gió thổi hay miệng thổi đều dùng: <b>Ду́ет ве́тер</b> Gió thổi; thổi vào cái gì → '
    '<b>на</b> + cách 4: <b>дуть на чай</b>. Chia đều, giữ <b>у</b>: <b>ду́ю</b>, <b>ду́ешь</b>. Cặp HT: '
    '<b>поду́ть</b>.</div>'
    '<div class="hd-warn"><b>Здесь ду́ет</b> = ở đây có gió lùa — câu không chủ ngữ, rất hay nghe.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поду́ть</b> (HT) · <b>ду́нуть</b> thổi một hơi · <b>наду́ть</b> bơm phồng · '
    '<b>дунове́ние</b> làn gió thoảng</div>'
)

# --------------------------------------------------------------------- подуть
S["подуть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span><span class="hd-gloss">BẮT ĐẦU, hoặc làm MỘT '
    'LÚC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ду-ть</span><span class="hd-gloss">THỔI — '
    '<b>дуть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp HT của <b>дуть</b>. Với gió, <b>по-</b> đánh dấu lúc khởi lên: <b>Поду́л ве́тер</b> '
    'Gió nổi lên. Với người, là thổi một lúc: <b>поду́ть на чай</b> thổi cho trà nguội. Chia như <b>дуть</b>: '
    '<b>поду́ю</b>, <b>поду́ет</b>.</div>'
    '<div class="hd-warn">Cùng kiểu <b>по-</b> «bắt đầu» với <b>полете́ть</b> bay đi, <b>пойти́</b> bắt đầu '
    'đi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дуть</b> (CHT) · <b>ду́нуть</b> thổi một hơi · <b>наду́ть</b> bơm phồng · '
    '<b>дунове́ние</b> làn gió thoảng</div>'
)

# --------------------------------------------------------------------- тайга
S["тайга"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn từ các ngôn ngữ bản địa Siberia.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiếng Anh <i>taiga</i> lấy chính từ này. Số ít trọng âm luôn ở đuôi: <b>тайга́</b>, '
    '<b>тайгу́</b>, <b>в тайге́</b>. Sang tính từ <b>г → ж</b>: <b>таёжный</b>.</div>'
    '<div class="hd-warn"><b>лес</b> là rừng nói chung; <b>тайга́</b> chỉ riêng dải rừng lá kim mênh mông phương '
    'bắc, nhất là Siberia.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>таёжный</b> thuộc rừng taiga · <b>таёжник</b> người sống ở rừng taiga</div>'
)

# --------------------------------------------------------------------- биржа
S["биржа"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn (Hà Lan <i>beurs</i> / Đức <i>Börse</i>), không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc với tiếng Anh <i>bourse</i> (sở giao dịch) và <i>purse</i> (ví): đều từ Latin '
    '<i>bursa</i> «túi». Nhớ: chỗ người ta mang túi tiền đến ⇒ sàn giao dịch. Đi với <b>на</b>: <b>на '
    'би́рже</b>.</div>'
    '<div class="hd-warn"><b>би́ржа труда́</b> = trung tâm giới thiệu việc làm (cho người thất nghiệp).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>биржево́й</b> thuộc sàn giao dịch · <b>биржеви́к</b> người chơi trên sàn</div>'
)

# --------------------------------------------------------------------- бульвар
S["бульвар"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn Pháp <i>boulevard</i>, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= tiếng Anh <i>boulevard</i>. Vốn là «tường luỹ» (cùng gốc <i>bulwark</i>): luỹ cổ phá '
    'đi, chỗ ấy trồng cây làm đường dạo ⇒ phố có dải cây xanh.</div>'
    '<div class="hd-warn"><b>бульва́р</b> có lối đi dạo rợp cây; <b>проспе́кт</b> là đại lộ thẳng, rộng.</div>'
    '<div class="hd-warn"><b>бульва́рная пре́сса</b> = báo lá cải.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бульва́рный</b> thuộc đại lộ; rẻ tiền, lá cải</div>'
)

# --------------------------------------------------------------------- базар
S["базар"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn gốc Ba Tư <i>bāzār</i>, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= tiếng Anh <i>bazaar</i>. Gợi chợ phiên, chợ kiểu phương Đông; từ chung cho «chợ» là '
    '<b>ры́нок</b>. Cũng như <b>ры́нок</b>, đi với <b>на</b>: <b>на база́ре</b> ở chợ, <b>на база́р</b> ra '
    'chợ.</div>'
    '<div class="hd-warn">Khẩu ngữ: chỗ ầm ĩ cũng gọi là <b>база́р</b> — <b>Что за база́р?</b> Làm gì mà ồn như '
    'chợ thế?</div>'
    '<div class="hd-warn"><b>ба́за</b> (căn cứ, cơ sở) không cùng họ: gốc Hy Lạp, như <i>base</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>база́рный</b> thuộc chợ: <b>база́рный день</b> ngày họp chợ</div>'
)

# --------------------------------------------------------------------- банкомат
S["банкомат"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">банк-</span><span class="hd-gloss">NGÂN HÀNG — '
    '<b>банк</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ома́т</span><span class="hd-gloss">khúc cuối cắt từ '
    '<b>автома́т</b> máy tự động</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>банк</b> + <b>автома́т</b>: «máy tự động của ngân hàng» ⇒ máy ATM.</div>'
    '<div class="hd-warn">Rút tiền: <b>снять де́ньги в банкома́те</b> — nghĩa đen «gỡ tiền xuống».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>банк</b> ngân hàng · <b>автома́т</b> máy tự động · <b>банки́р</b> chủ ngân hàng · '
    '<b>ба́нковский</b> thuộc ngân hàng</div>'
)

# --------------------------------------------------------------------- окраина
S["окраина"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span><span class="hd-gloss">QUANH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-кра́-</span><span class="hd-gloss">MÉP, RÌA NGOÀI CÙNG — '
    '<b>край</b>; chữ <b>й</b> chìm vào <b>и</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ин-а</span><span class="hd-gloss">đuôi danh từ giống '
    'cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Dải rìa vòng quanh» thành phố ⇒ vùng ven, ngoại ô. Giới từ <b>на</b> + cách 6: <b>жить '
    'на окра́ине го́рода</b> sống ở ven thành phố.</div>'
    '<div class="hd-warn"><b>окра́ина</b> là RÌA của chính thành phố; <b>при́город</b> là vùng sát bên NGOÀI '
    'thành phố.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>край</b> mép, rìa · <b>кра́йний</b> ngoài cùng · <b>кра́йне</b> cực kỳ</div>'
)

# --------------------------------------------------------------------- поперёк
S["поперёк"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span><span class="hd-gloss">THEO (chiều nào đó)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-перёк</span><span class="hd-gloss">CHẮN NGANG — chỉ còn sống '
    'trong vài từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Theo chiều chắn ngang», đối của <b>вдоль</b> dọc theo. Đứng một mình hoặc kéo theo '
    'cách 2: <b>поперёк доро́ги</b> chắn ngang đường.</div>'
    '<div class="hd-warn"><b>вдоль и поперёк</b> = khắp ngang dọc, tường tận.</div>'
    '<div class="hd-warn">⚠️ Mức tin: <b>-прек-</b> của <b>вопреки́</b> bất chấp là dạng sách của chính '
    '<b>-перёк</b> — từ nguyên, không phải luật suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>попере́чный</b> nằm ngang · <b>вопреки́</b> bất chấp · <b>вдоль</b> dọc theo (đối '
    'nghĩa)</div>'
)

# --------------------------------------------------------------------- отовсюду
S["отовсюду"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-о-</span><span class="hd-gloss">TỪ, rời khỏi — chèn <b>о</b> '
    'trước cụm <b>вс-</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-вс-</span><span class="hd-gloss">TOÀN BỘ (từ '
    '<b>весь</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ю́ду</span><span class="hd-gloss">đuôi chỉ NƠI CHỐN</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>от-</b> + <b>всю́ду</b> khắp nơi ⇒ từ khắp nơi. Đứng cùng dãy «từ đâu»: '
    '<b>отку́да</b> từ đâu · <b>отсю́да</b> từ đây · <b>отту́да</b> từ đó.</div>'
    '<div class="hd-warn"><b>всю́ду</b> trả lời câu hỏi Ở ĐÂU, <b>отовсю́ду</b> trả lời TỪ ĐÂU: <b>Го́сти '
    'прие́хали отовсю́ду</b> Khách đến từ khắp nơi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>всю́ду</b> khắp nơi · <b>повсю́ду</b> khắp mọi nơi · <b>весь</b> toàn bộ · '
    '<b>отку́да</b> từ đâu</div>'
)

# --------------------------------------------------------------------- трактор
S["трактор"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">тракт-</span><span class="hd-gloss">KÉO (Latin <i>tract-</i>, '
    'như <i>attract</i> «kéo về»)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ор</span><span class="hd-gloss">cái / người làm việc đó, như '
    '<b>а́втор</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cái để kéo» ⇒ máy kéo, hệt tiếng Anh <i>tractor</i>. Số nhiều có hai dạng, dạng nhấn '
    'đuôi rất hay nghe: <b>трактора́</b> (hoặc <b>тра́кторы</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>трактори́ст</b> người lái máy kéo · <b>тра́кторный</b> thuộc máy kéo</div>'
)

# --------------------------------------------------------------------- взлетать
S["взлетать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вз-</span><span class="hd-gloss">LÊN, bật lên — như '
    '<b>вздыха́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-лет-а́ть</span><span class="hd-gloss">gốc BAY — '
    '<b>лета́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bật lên mà bay ⇒ bay lên, cất cánh. Có tiền tố rồi thì <b>лета́ть</b> hết là «bay qua '
    'lại», chỉ còn là cặp CHT của <b>взлете́ть</b>. Chia đều: <b>взлета́ю</b>, <b>взлета́ет</b>.</div>'
    '<div class="hd-warn">Trái nghĩa: <b>приземля́ться</b> hạ cánh. Đường băng là <b>взлётная полоса́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>взлете́ть</b> (HT) · <b>взлёт</b> sự cất cánh · <b>лета́ть</b> bay · '
    '<b>прилета́ть</b> bay đến · <b>самолёт</b> máy bay</div>'
)

# --------------------------------------------------------------------- взлететь
S["взлететь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вз-</span><span class="hd-gloss">LÊN, bật lên — như '
    '<b>вздохну́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-лете́ть</span><span class="hd-gloss">bay — '
    '<b>лете́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp HT của <b>взлета́ть</b>: đã rời mặt đất. Chia như <b>лете́ть</b>, ngôi «tôi» <b>т → '
    'ч</b>: <b>взлечу́</b>, <b>взлети́шь</b>, <b>взлетя́т</b>.</div>'
    '<div class="hd-warn"><b>взлете́ть на во́здух</b> = nổ tung — không phải «bay vào không khí».</div>'
    '<div class="hd-warn"><b>взлете́ть</b> = bật LÊN khỏi đất · <b>вы́лететь</b> = bay RA khỏi một nơi, khởi '
    'hành.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>взлета́ть</b> (CHT) · <b>взлёт</b> sự cất cánh · <b>полёт</b> chuyến bay · '
    '<b>улете́ть</b> bay mất</div>'
)

# --------------------------------------------------------------------- вылетать
S["вылетать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span><span class="hd-gloss">RA NGOÀI — ở thể CHT mất trọng '
    'âm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лет-а́ть</span><span class="hd-gloss">gốc BAY — '
    '<b>лета́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bay ra khỏi một nơi: chim ra khỏi tổ, máy bay rời thành phố ⇒ khởi hành. Rời đâu → '
    '<b>из</b> + cách 2: <b>Мы вылета́ем из Хано́я в семь</b>. Chia đều: <b>вылета́ю</b>. Cặp HT: '
    '<b>вы́лететь</b>.</div>'
    '<div class="hd-warn">Bảng ở sân bay: <b>Вы́лет</b> = Chuyến đi · <b>Прилёт</b> = Chuyến đến.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вы́лететь</b> (HT) · <b>вы́лет</b> chuyến bay đi · <b>улета́ть</b> bay đi · '
    '<b>выезжа́ть</b> rời đi bằng xe</div>'
)

# --------------------------------------------------------------------- вылететь
S["вылететь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы́-</span><span class="hd-gloss">RA NGOÀI — ở thể HT luôn mang '
    'trọng âm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лететь</span><span class="hd-gloss">bay — '
    '<b>лете́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp HT của <b>вылета́ть</b>. <b>вы́-</b> giữ trọng âm cả bảng, ngôi «tôi» <b>т → ч</b>: '
    '<b>вы́лечу</b>, <b>вы́летишь</b>, <b>вы́летят</b>.</div>'
    '<div class="hd-warn"><b>вы́лечу</b> còn là «tôi sẽ chữa khỏi» (<b>вы́лечить</b>, <b>вы́лечишь</b>) — chỉ '
    'ngôi «tôi» trùng, ngữ cảnh tách.</div>'
    '<div class="hd-warn"><b>вы́лететь из головы́</b> = quên béng: <b>Совсе́м вы́летело из головы́!</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вылета́ть</b> (CHT) · <b>вы́лет</b> chuyến bay đi · <b>прилете́ть</b> bay đến · '
    '<b>взлете́ть</b> cất cánh</div>'
)

B = {
    "docbangmat": 120,
    "loitubat": 3,
    "nguonsai": 4,
    "baolen": [
        "V cần duyệt (5 thẻ): загрязнение (nhiễm bẩn -> sự nhiễm bẩn) · влажный (RÚT ướt -> ẩm, ẩm ướt) · подуть (RÚT nổi lên; thêm dãy của дуть) · взлететь (vút lên cao -> vút lên) · вылететь (BỎ bay biến).",
        "влажный hết va chạm với мокрый [k128]; «ẩm» còn chung với сырой, мокрый nhưng không đề nào nằm gọn trong đề nào.",
        "подуть KHÔNG san y hệt дуть: lấy trọn dãy của дуть rồi giữ thêm «bắt đầu thổi, thổi một lúc» vì gloss của nó chỉ ghi start blowing / blow for a while, cắt đi là mất nghĩa chính (như покачать). Nếu luồng chính muốn y hệt: để «thổi, phả hơi, gió thổi» ở cả hai.",
        "взлетать/взлететь và вылетать/вылететь: trùng hết nghĩa trong cặp — badge thể tách.",
        "Câu ví dụ của подуть dịch «nổi lên» (gió): vẫn đúng trong câu, chỉ là đề bài đứng trơ thì mơ hồ.",
        "Không chắc, KHÔNG đưa lên thẻ: дуть ↔ дух (chung gốc xa), поперёк ↔ пере-, комар ↔ Đức Hummel. подушка ↔ дуть đang ở ô Mức tin của k23 nên không liệt vào Họ hàng của дуть.",
        "Máy báo тайга «trọng âm dịch trong số nhiều» là báo động giả (cách 2 số nhiều đuôi rỗng тайг) — không viết. Máy báo oan đúng như lời giao: блюдо, база (ghi câu chống lẫn); опера thì bỏ hẳn.",
        "Soát báo lệch воро́н (cách 2 số nhiều) ↔ danh từ во́рон, đồng tự: BỎ dạng đó khỏi thẻ, không nới MIEN_TRU.",
    ],
}
