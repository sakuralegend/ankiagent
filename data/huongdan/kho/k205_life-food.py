# -*- coding: utf-8 -*-
"""k205 — life::food (lô trộn): đồ ăn, đồ dùng trong nhà, nhà ở.

Chỗ cần nhất quán trong lô:
(1) печь / испе́чь: печь ở đây là ĐỘNG TỪ «nướng» (cặp CHT của испе́чь), KHÔNG phải danh từ
    «cái lò» — danh từ chỉ được nhắc như từ trùng mặt chữ. Biến âm к/ч và quá khứ пёк giải
    thích đủ ở thẻ печь; испе́чь dẫn chiếu một dòng.
(2) угости́ть / угоща́ть: у- + гост- (гость, гости́ница) — ст → щ ở угощу́, CHT dựng từ thân щ ấy.
(3) бело́к + жир nối nhau qua nhãn thực phẩm «белки́, жиры́, углево́ды».
(4) освеще́ние: т → щ (sách vở) cạnh свеча́ т → ч (thuần Nga), cùng gốc свет.
(5) особня́к ← осо́бый; ла́мпочка ← ла́мпа; попи́ть ← пить; забо́р ← брать (như вы́бор).
Họ hàng cố ý vắng: джем (mượn thẳng tiếng Anh), те́сто (gốc cổ, không phái sinh dùng được).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "перец": "hạt tiêu, tiêu, ớt, ớt ngọt",                          # gloss có chilli, đề cũ chỉ có ớt ngọt
    "испечь": "nướng, làm bánh",                                     # «nướng xong» = nhãn thể trá hình; badge thể đã tách với печь
    "освещение": "sự chiếu sáng, đèn chiếu sáng, ánh sáng, sự đưa tin",  # gloss coverage/reporting
}

# --------------------------------------------------------------------- сливки
S["сливки"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-лив-</span>'
    '<span class="hd-gloss">RÓT RA, CHẮT RA — <b>слива́ть</b> (<i>с-</i> khỏi + <b>лить</b> rót)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-и</span>'
    '<span class="hd-gloss">đuôi danh từ, ở đây CHỈ CÓ SỐ NHIỀU</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thứ được chắt ra» — lớp béo nổi trên sữa được gạn đi ⇒ kem sữa. '
    'Không có số ít nên tính từ đi kèm cũng số nhiều: <b>све́жие сли́вки</b> kem tươi. '
    'Cách 2 chen thêm <i>о</i>: <b>сли́вок</b>.</div>'
    '<div class="hd-warn"><b>сли́вочное ма́сло</b> = BƠ (bơ làm từ kem); <b>ма́сло</b> trơn '
    'còn có thể là dầu ăn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лить</b> rót · <b>слить</b> / <b>слива́ть</b> đổ ra, chắt ra · '
    '<b>сли́вочный</b> thuộc kem, vị kem</div>'
)

# --------------------------------------------------------------------- белок
S["белок"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бел-</span>'
    '<span class="hd-gloss">TRẮNG — như <b>бе́лый</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́к</span>'
    '<span class="hd-gloss">đuôi danh từ giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Phần trắng» của quả trứng ⇒ lòng trắng; lòng trắng gần như toàn đạm '
    '⇒ chất đạm, protein (tiếng Anh <i>albumen</i> cũng từ Latin <i>albus</i> «trắng»). '
    'Song song: <b>жёлтый</b> vàng → <b>желто́к</b> lòng đỏ. Khi thêm đuôi, <i>о</i> rơi mất '
    'và trọng âm xuống đuôi: <b>белка́</b>, <b>белко́м</b>.</div>'
    '<div class="hd-warn"><b>белка́</b> (cách 2 của бело́к) ≠ <b>бе́лка</b> con sóc — '
    'chỉ khác chỗ trọng âm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бе́лый</b> trắng · <b>бельё</b> đồ lót, ga gối · '
    '<b>белко́вый</b> thuộc protein</div>'
)

# --------------------------------------------------------------------- джем
S["джем"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mượn thẳng tiếng Anh <i>jam</i> — không chẻ được. Danh từ giống đực, '
    'biến cách bình thường: <b>с дже́мом</b>.</div>'
    '<div class="hd-warn"><b>варе́нье</b> là mứt kiểu Nga: quả để nguyên trong nước đường; '
    '<b>джем</b> thì sệt, quả nấu nhừ.</div>'
)

# --------------------------------------------------------------------- тесто
S["тесто"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc cổ, không chẻ được; đuôi <i>-о</i> ⇒ giống trung. Bột trộn nước '
    'nhào được ⇒ bột nhào, bột bánh; rộng ra là mọi thứ sệt nhão. Chỉ trùng mặt chữ với '
    '<b>тест</b> bài kiểm tra (mượn tiếng Anh <i>test</i>) — không cùng gốc.</div>'
)

# --------------------------------------------------------------------- жир
S["жир"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được. Số nhiều <b>жиры́</b> trọng âm nhảy xuống '
    'đuôi — chính dạng in trên nhãn thực phẩm: <b>белки́, жиры́, углево́ды</b> đạm, béo, '
    'chất bột đường.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>жи́рный</b> béo, nhiều mỡ; (chữ) đậm · '
    '<b>обезжи́ренный</b> tách béo (sữa)</div>'
)

# --------------------------------------------------------------------- перец
S["перец"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mượn rất sớm từ tiếng Hy Lạp <i>péperi</i> — cùng gốc với <i>pepper</i>; '
    'đuôi <i>-ец</i> do tiếng Nga thêm vào. Một từ cho mọi loại: '
    '<b>чёрный пе́рец</b> tiêu đen · <b>о́стрый пе́рец</b> ớt cay · <b>сла́дкий пе́рец</b> ớt chuông. '
    '<i>е</i> rơi khi thêm đuôi: <b>пе́рца</b>; từ phái sinh đổi <i>ц → ч</i>.</div>'
    '<div class="hd-warn"><b>перча́тка</b> găng tay KHÔNG cùng gốc — nó từ <b>перст</b> '
    'ngón tay.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пе́речница</b> lọ tiêu · <b>поперчи́ть</b> rắc tiêu</div>'
)

# --------------------------------------------------------------------- угостить
S["угостить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố, nghĩa đã mờ — biến «làm khách» thành «đãi khách», HOÀN THÀNH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-гост-и́ть</span>'
    '<span class="hd-gloss">KHÁCH — chính là <b>гость</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đối đãi như khách» ⇒ mời ăn uống, thiết đãi. Ngôi «tôi» biến âm '
    '<i>ст → щ</i>: <b>угощу́</b>, <b>угости́шь</b>. Cặp CHT <b>угоща́ть</b> giữ luôn <i>щ</i> ấy.</div>'
    '<div class="hd-warn">Người được mời ở cách 4, món mời ở cách 5: '
    '<b>угости́ть дру́га ча́ем</b> mời bạn uống trà.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гость</b> khách · <b>гости́ница</b> khách sạn · '
    '<b>гости́ть</b> ở chơi, làm khách · <b>угоще́ние</b> món đãi</div>'
)

# --------------------------------------------------------------------- угощать
S["угощать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-гощ-</span>'
    '<span class="hd-gloss">KHÁCH — <i>гост-</i> đã biến âm <i>ст → щ</i>, như <b>угощу́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">→ CHƯA HOÀN THÀNH</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>угости́ть</b>, dựng từ thân ngôi «tôi» <i>угощ-</i>. '
    'Chia đều: <b>угоща́ю</b>, <b>угоща́ешь</b>. Cùng cách đòi: <b>угоща́ть госте́й ко́фе</b>.</div>'
    '<div class="hd-warn"><b>Угоща́йтесь!</b> = Mời cứ tự nhiên dùng! (chủ nhà bày đồ ăn) · '
    '<b>Я угоща́ю!</b> = Để tôi bao!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>угости́ть</b> (HT) · <b>гость</b> khách · <b>угоще́ние</b> món đãi</div>'
)

# --------------------------------------------------------------------- попить
S["попить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">MỘT CHÚT, một lúc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пить</span>'
    '<span class="hd-gloss">UỐNG — chính là <b>пить</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Uống một ít cho đỡ khát, không nói tới uống hết: <b>Дай попи́ть!</b> '
    'Cho mình uống miếng nước! Là HT, không có cặp CHT riêng — nói chung chung thì dùng '
    '<b>пить</b>. Chia y như <b>пить</b>: <b>попью́</b>, <b>попьёшь</b> — thân <i>пь-</i> không '
    'đoán được từ nguyên thể, phải thuộc. Quá khứ giống cái trọng âm xuống đuôi: '
    '<b>попила́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пить</b> uống · <b>вы́пить</b> uống cạn · <b>напи́ток</b> đồ uống · '
    '<b>пья́ный</b> say</div>'
)

# --------------------------------------------------------------------- печь (động từ)
S["печь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пек-</span>'
    '<span class="hd-gloss">NƯỚNG — gốc thật, lộ ra ở <b>пеку́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-чь</span>'
    '<span class="hd-gloss"><i>к</i> + đuôi <i>-ть</i> nhập lại — như <b>мочь</b> (<i>г</i> + <i>-ть</i>, <b>могу́</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><i>к</i> trước <i>у</i>, <i>ч</i> trước <i>е</i>: <b>пеку́</b>, '
    '<b>печёшь</b> … <b>пеку́т</b>. Quá khứ giống đực không có <i>-л</i>: <b>пёк</b>, '
    '<b>пекла́</b>, <b>пекли́</b>. Mặt trời cũng «nướng»: <b>Со́лнце печёт</b> nắng gắt. '
    'Cặp HT: <b>испе́чь</b>.</div>'
    '<div class="hd-warn">Danh từ <b>печь</b> «cái lò» (giống cái: <b>в печи́</b>) trùng mặt '
    'chữ — và cùng gốc thật: lò là chỗ để nướng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>испе́чь</b> (HT) · <b>пече́нье</b> bánh quy · '
    '<b>пека́рня</b> lò bánh mì · <b>пе́чка</b> cái lò</div>'
)

# --------------------------------------------------------------------- испечь
S["испечь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ис-</span>'
    '<span class="hd-gloss">không mang nghĩa riêng — chỉ làm HOÀN THÀNH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-печь</span>'
    '<span class="hd-gloss">NƯỚNG — chính là <b>печь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp HT của <b>печь</b>: nướng tới khi xong — <b>испе́чь торт</b> nướng '
    'một cái bánh. Chia y hệt <b>печь</b>: <b>испеку́</b>, <b>испечёшь</b>, <b>испеку́т</b>; '
    'quá khứ <b>испёк</b>, <b>испекла́</b>. Vì sao <i>к</i>/<i>ч</i> đổi chỗ: xem thẻ '
    '<b>печь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>печь</b> (CHT) · <b>пече́нье</b> bánh quy · <b>пека́рня</b> lò bánh mì</div>'
)

# --------------------------------------------------------------------- тряпка
S["тряпка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">тряп-</span>'
    '<span class="hd-gloss">GIẺ, vải vụn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-а</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mảnh vải cũ dùng để lau ⇒ giẻ lau, khăn lau. Cách 2 số nhiều chen '
    'thêm <i>о</i>: <b>тря́пок</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тряпьё</b> giẻ rách, đồ cũ nát</div>'
)

# --------------------------------------------------------------------- спичка
S["спичка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">спич-</span>'
    '<span class="hd-gloss">QUE — từ <b>спи́ца</b>, <i>ц → ч</i> trước <i>-к</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-а</span>'
    '<span class="hd-gloss">hậu tố NHỎ, giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Que nhỏ» ⇒ que diêm. Biến âm như <b>пти́ца</b> → <b>пти́чка</b>. '
    'Cách 2 số nhiều chen <i>е</i>: <b>коробо́к спи́чек</b> một hộp diêm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>спи́ца</b> nan xe, kim đan</div>'
)

# --------------------------------------------------------------------- лампочка
S["лампочка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ла́мп-</span>'
    '<span class="hd-gloss">ĐÈN — chính là <b>ла́мпа</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-очк-а</span>'
    '<span class="hd-gloss">hậu tố NHỎ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đèn nhỏ» ⇒ ngày nay chủ yếu là bóng đèn điện. Cách 2 số nhiều chen '
    '<i>е</i>: <b>ла́мпочек</b>.</div>'
    '<div class="hd-warn"><b>Мне до ла́мпочки</b> = khẩu ngữ «tôi cóc quan tâm».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ла́мпа</b> đèn</div>'
)

# --------------------------------------------------------------------- освещение
S["освещение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">PHỦ KHẮP, quanh</span></div>'
    '<div class="hd-row"><span class="hd-piece">-свещ-</span>'
    '<span class="hd-gloss">ÁNH SÁNG — <b>свет</b>, <i>т → щ</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>освети́ть</b> chiếu sáng (ngôi «tôi» <b>освещу́</b>): '
    'cho ánh sáng phủ khắp ⇒ sự chiếu sáng, hệ thống đèn. Nghĩa bóng: «rọi sáng» một sự kiện '
    '⇒ đưa tin: <b>освеще́ние собы́тий</b>. Cùng gốc, tiếng Nga thuần đổi <i>т → ч</i>: '
    '<b>свеча́</b> cây nến.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>свет</b> ánh sáng · <b>све́тлый</b> sáng · <b>свеча́</b> nến · '
    '<b>освети́ть</b> chiếu sáng · <b>светофо́р</b> đèn giao thông</div>'
)

# --------------------------------------------------------------------- клей
S["клей"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được. Đuôi <i>-й</i> ⇒ giống đực: <b>кле́я</b>, '
    '<b>кле́ем</b>. Động từ «dán» dựng thẳng từ nó.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кле́ить</b> dán · <b>прикле́ить</b> dán vào · '
    '<b>накле́йка</b> nhãn dán</div>'
)

# --------------------------------------------------------------------- жилой
S["жилой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">жи-л-</span>'
    '<span class="hd-gloss">SỐNG — thân của <b>жить</b> (<b>он жил</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́й</span>'
    '<span class="hd-gloss">đuôi tính từ, trọng âm ở đuôi</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thuộc về chỗ người sống» ⇒ để ở: <b>жило́й дом</b> nhà ở, '
    '<b>жило́й райо́н</b> khu dân cư. Tính từ quan hệ ⇒ không có dạng ngắn, không có trạng từ '
    '<i>-о</i>; chỉ nói về nhà cửa, không nói về người.</div>'
    '<div class="hd-warn"><b>пожило́й</b> = cao tuổi (người) — giống mặt chữ mà nghĩa đã '
    'khác hẳn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>жить</b> sống · <b>жи́тель</b> cư dân · <b>жильё</b> chỗ ở · '
    '<b>жизнь</b> cuộc sống</div>'
)

# --------------------------------------------------------------------- особняк
S["особняк"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">особ-</span>'
    '<span class="hd-gloss">RIÊNG, TÁCH BIỆT — như <b>осо́бый</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ня́к</span>'
    '<span class="hd-gloss">đuôi danh từ giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Nhà đứng riêng», không chung vách với ai ⇒ biệt thự, dinh thự. '
    'Trọng âm xuống đuôi ngay từ cách 2: <b>особняка́</b>, <b>особняко́м</b>.</div>'
    '<div class="hd-warn"><b>держа́ться особняко́м</b> = đứng tách riêng, không hoà vào nhóm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>осо́бый</b> đặc biệt, riêng · <b>осо́бенно</b> đặc biệt là · '
    '<b>осо́бенность</b> đặc điểm</div>'
)

# --------------------------------------------------------------------- забор
S["забор"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">ở đây: lấy VÀO, gom về</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бор</span>'
    '<span class="hd-gloss">LẤY — gốc <i>бр-/бер-/бор-</i> của <b>брать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Như <b>вы́бор</b> ← <b>вы́брать</b>: <b>забо́р</b> ← <b>забра́ть</b> '
    'lấy vào ⇒ lấy mẫu, lấy nước: <b>забо́р кро́ви</b> lấy máu xét nghiệm. Nghĩa hàng rào '
    '(hay gặp nhất) theo từ nguyên cũng từ đây — <b>забра́ть</b> xưa còn là «quây lại bằng '
    'ván».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>брать</b> lấy · <b>забра́ть</b> lấy đi · <b>вы́бор</b> sự lựa chọn · '
    '<b>собра́ть</b> gom lại</div>'
)

B = {
    "docbangmat": 78,
    "loitubat": 5,      # у- của угости́ть khai «không nghĩa riêng» (sai: có гости́ть làm khách) · слив- giấu с-+лив- · пе́рец «-ец nắn cho thành giống đực» (bịa lý do) · мочь ví với к (thật ra г) · углево́ды dịch «tinh bột» (hẹp)
    "nguonsai": 2,      # nouns.csv báo белка́ lệch (đồng tự бе́лка) · tiep đổ cụm của DANH TỪ печь (до́менная печь…) vào thẻ ĐỘNG TỪ печь — không dùng
    "baolen": [
        "THÊM 1 mục MIEN_TRU (data/huongdan/mientru.py): белка́ — đồng tự thật, cách 2 của бело́к vs бе́лка con sóc; thẻ бело́к cố ý nêu cặp này trong ô đỏ. Mặt gương của mục бе́лок (k25) đã có. Lùi lại = xoá mục đó và bỏ in đậm белка́ trong thẻ бело́к.",
        "V cần duyệt (3): перец thêm «ớt» (gloss có chilli) · испечь bỏ «nướng xong, làm xong bánh» → «nướng, làm bánh» (chữ «xong» là nhãn thể trá hình; badge thể tách với печь) · освещение thêm «sự đưa tin» (gloss coverage/reporting).",
        "KHÔNG CHẮC (từ nguyên, đã viết mềm): забо́р «hàng rào» ← забра́ть «quây lại» · перча́тка ← перст · сли́вки ← слива́ть. Theo Vasmer/Shansky theo trí nhớ, không tra được trong repo.",
        "Họ hàng cố ý vắng: джем (mượn Anh jam), те́сто (gốc cổ). Va chạm nghĩa: không có.",
    ],
}
