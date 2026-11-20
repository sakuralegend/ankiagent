# -*- coding: utf-8 -*-
"""k127 — people::professions: người trong gia đình, sống/chết, nghề và chợ búa.

Không khối hệ thống. Chỗ cần nhất quán trong lô:
(1) промы́шленный/промы́шленность cùng chẻ про- + мышл- (= мысл- «ý nghĩ», с→ш);
    -ость biến tính từ thành danh từ;
(2) това́р / торго́вля / покупа́тель là ba vai của cái chợ — mỗi thẻ dẫn sang hai thẻ kia;
(3) погиба́ть/поги́бнуть: mỗi vế chỉ nói phần của nó (vế HT giữ chuyện quá khứ поги́б).
"""

S = {}

S["борода"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được — nhưng cùng gốc Ấn-Âu với tiếng Anh '
    '<i>beard</i>, Latin <i>barba</i> (→ <i>barber</i> thợ cạo).</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><i>b-r-d</i> ↔ <i>b-r-d</i>: <b>борода́</b> ≈ <i>beard</i>.</div>'
    '<div class="hd-warn">Trọng âm nhảy lên đầu ở <b>бо́роду</b> (cách 4) và <b>бо́роды</b> '
    '(số nhiều cách 1) — còn lại nằm sau: <b>бороды́</b>, <b>боро́д</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>подборо́док</b> cái cằm (под «dưới» + râu) · '
    '<b>борода́тый</b> có râu · <b>боро́дка</b> chòm râu nhỏ</div>'
)

S["желудок"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">желуд-</span>'
    '<span class="hd-gloss">gốc, xem mức tin bên dưới</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ок</span>'
    '<span class="hd-gloss">hậu tố danh từ, chữ <i>о</i> là nguyên âm chạy</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thêm đuôi là <i>о</i> rơi mất: <b>желу́док</b> → <b>желу́дка</b>, '
    '<b>в желу́дке</b> (trong dạ dày). Trọng âm đứng yên ở <i>-лу́-</i>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: đây là từ nguyên, không phải luật — từ điển từ nguyên '
    'thường nối với <b>жёлудь</b> «quả sồi» (hình dáng giống). Dùng để nhớ, đừng suy ra từ khác.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>желу́дочный</b> thuộc dạ dày (<i>к → ч</i>)</div>'
)

S["взрослый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вз-</span>'
    '<span class="hd-gloss">LÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-рос-л-</span>'
    '<span class="hd-gloss">ĐÃ LỚN — như quá khứ <b>рос</b>, <b>росла́</b> của <b>расти́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen «đã lớn lên hẳn». Gốc lớn đổi qua lại <i>раст-/рос-</i>: '
    'nguyên thể <b>расти́</b> có <i>а</i>, còn <b>взро́слый</b> mang <i>о</i> của quá khứ.</div>'
    '<div class="hd-warn">Dùng như danh từ: <b>взро́слые</b> = người lớn — <b>для взро́слых</b> '
    'dành cho người lớn. Không cần danh từ đi kèm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>расти́</b> lớn lên · <b>вы́расти</b> lớn lên, trưởng thành · '
    '<b>рост</b> chiều cao, sự tăng trưởng</div>'
)

S["жених"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">жен-</span>'
    '<span class="hd-gloss">VỢ, cưới — như <b>жена́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-их</span>'
    '<span class="hd-gloss">hậu tố chỉ người, không mang nghĩa riêng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người sắp có <b>жена́</b> ⇒ chú rể. Trọng âm luôn nằm ở đuôi khi có đuôi: '
    '<b>жениха́</b>, <b>женихи́</b>.</div>'
    '<div class="hd-warn">Cặp của nó là <b>неве́ста</b> (cô dâu) — KHÁC gốc, phải thuộc riêng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>жена́</b> vợ · <b>жени́ться</b> lấy vợ</div>'
)

S["погибать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố thể, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-гиб-</span>'
    '<span class="hd-gloss">gốc DIỆT VONG — như <b>ги́бель</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành, chia đều: <b>погиба́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vế CHT của <b>поги́бнуть</b>: chết đang xảy ra hoặc lặp lại — '
    '<b>Ка́ждый год погиба́ют ты́сячи</b> mỗi năm hàng nghìn người thiệt mạng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поги́бнуть</b> bỏ mạng (HT) · <b>ги́бель</b> cái chết, sự diệt vong · '
    '<b>ги́бнуть</b> tiêu vong, chết</div>'
)

S["погибнуть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố thể hoàn thành, không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-гиб-</span>'
    '<span class="hd-gloss">gốc DIỆT VONG — như <b>ги́бель</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ну-ть</span>'
    '<span class="hd-gloss">đuôi động từ, <i>-ну-</i> rụng ở quá khứ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Quá khứ rụng <i>-ну-</i>, giống đực rụng luôn <i>-л</i>: <b>поги́б</b>, '
    '<b>поги́бла</b>, <b>поги́бли</b>. Dạng <b>поги́бнул</b> có trong từ điển nhưng hiếm.</div>'
    '<div class="hd-warn">Chết vì tai nạn, chiến tranh, thảm hoạ = <b>поги́бнуть</b> '
    '(<b>поги́б на войне́</b>). Chết vì già, bệnh = <b>умере́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>погиба́ть</b> bỏ mạng (CHT) · <b>ги́бель</b> cái chết, sự diệt vong · '
    '<b>поги́бший</b> người tử nạn</div>'
)

S["прожить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">XUYÊN SUỐT một khoảng thời gian</span></div>'
    '<div class="hd-row"><span class="hd-piece">-жить</span>'
    '<span class="hd-gloss">SỐNG — chính là <b>жить</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Sống trọn một quãng: <b>про́жил 10 лет в Москве́</b> — thời gian đứng '
    'thẳng sau động từ, không cần giới từ. Chia y như <b>жить</b>: <i>в</i> hiện ra — '
    '<b>проживу́</b>, <b>проживёшь</b>.</div>'
    '<div class="hd-warn">Quá khứ trọng âm nhảy lên tiền tố: <b>про́жил</b>, <b>про́жили</b> — '
    'riêng giống cái về đuôi: <b>прожила́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>жить</b> sống · <b>жизнь</b> cuộc sống · <b>жи́тель</b> cư dân · '
    '<b>прожива́ть</b> cư trú (CHT)</div>'
)

S["человечество"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">человеч-</span>'
    '<span class="hd-gloss"><b>челове́к</b> con người, <i>к → ч</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ество</span>'
    '<span class="hd-gloss">danh từ TẬP HỢP / trừu tượng, giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gộp mọi <b>челове́к</b> thành một khối ⇒ nhân loại. Không có số nhiều '
    'trong dùng thường ngày.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>челове́к</b> người · <b>челове́ческий</b> thuộc con người · '
    '<b>челове́чный</b> có tình người</div>'
)

S["традиция"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn (Latin <i>traditio</i>), không chẻ theo tiếng Nga. Đuôi '
    '<i>-ция</i> = <i>-tion</i> tiếng Anh: <b>тради́ция</b> = <i>tradition</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đổi <i>-tion</i> → <i>-ция</i> là ra hàng loạt danh từ giống cái. '
    'Tính từ của chính từ này: <b>традицио́нный</b> = <i>traditional</i>.</div>'
    '<div class="hd-warn"><b>по тради́ции</b> = theo truyền thống (по + cách 3).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>традицио́нный</b> truyền thống, theo lối cũ</div>'
)

S["зарплата"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">зар-</span>'
    '<span class="hd-gloss">viết tắt <b>зарабо́тная</b> «do làm ra»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пла́та</span>'
    '<span class="hd-gloss"><b>пла́та</b> tiền trả</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ ghép rút gọn của <b>зарабо́тная пла́та</b> = «tiền trả cho công làm ra». '
    'Trọng âm giữ đúng chỗ của <b>пла́та</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>плати́ть</b> trả tiền · <b>пла́та</b> tiền trả, phí · '
    '<b>зарабо́тать</b> kiếm được tiền · <b>рабо́та</b> công việc</div>'
)

S["хирург"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn Hy Lạp, không chẻ theo tiếng Nga: <i>kheir</i> «tay» + '
    '<i>ergon</i> «việc» = người làm việc bằng tay.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc tiếng Anh <i>surgeon</i> (qua tiếng Pháp cổ <i>cirurgien</i>) — '
    'tiếng Nga giữ sát hình Hy Lạp hơn: <i>хир-</i> ≈ <i>chiro-</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>хирурги́я</b> ngành phẫu thuật · <b>хирурги́ческий</b> thuộc phẫu thuật</div>'
)

S["промышленный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">tiền tố, nghĩa ở đây đã mờ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мышл-</span>'
    '<span class="hd-gloss">= <i>мысл-</i> Ý NGHĨ (<b>мысль</b>), <i>сл → шл</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-енный</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đi từ <b>про́мысел</b> «nghề kiếm sống» — nghĩ ra cách làm ăn — rồi lớn '
    'thành công nghiệp. Trạng từ dùng thật: <b>промы́шленно разви́тые стра́ны</b> các nước '
    'công nghiệp phát triển.</div>'
    '<div class="hd-warn">⚠️ Mức tin: đường nghĩa «ý nghĩ → nghề → công nghiệp» là từ nguyên, '
    'không phải luật. Phần chắc là chữ: <i>мышл</i> = <i>мысл</i> biến âm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>промы́шленность</b> nền công nghiệp · <b>про́мысел</b> nghề kiếm sống · '
    '<b>мысль</b> ý nghĩ</div>'
)

S["промышленность"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">промышленн-</span>'
    '<span class="hd-gloss"><b>промы́шленный</b> công nghiệp</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ость</span>'
    '<span class="hd-gloss">tính từ → danh từ, giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bỏ <i>-ый</i>, gắn <i>-ость</i>: tính từ thành danh từ — mẹo này mở cả lớp '
    'từ. Gốc <i>мышл-</i> = <i>мысл-</i> «ý nghĩ» — chẻ chi tiết ở thẻ <b>промы́шленный</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>промы́шленный</b> công nghiệp · <b>про́мысел</b> nghề kiếm sống · '
    '<b>мысль</b> ý nghĩ</div>'
)

S["товар"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, mượn từ tiếng Turk cổ (<i>tavar</i> «của cải, hàng») — '
    'không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một món: <b>това́р</b>; cả gian hàng: <b>това́ры</b>. Người mua nó là '
    '<b>покупа́тель</b>, việc bán nó là <b>торго́вля</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: <b>това́рищ</b> (bạn, đồng chí) thường được giải là từ '
    '<b>това́р</b> — gốc là «bạn buôn chung». Từ nguyên, đừng suy ra luật.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>това́рный</b> thuộc hàng hoá · <b>това́рищ</b> bạn, đồng chí</div>'
)

S["покупатель"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">покупа-</span>'
    '<span class="hd-gloss"><b>покупа́ть</b> MUA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тель</span>'
    '<span class="hd-gloss">NGƯỜI LÀM việc đó, giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Động từ bỏ <i>-ть</i>, gắn <i>-тель</i> ⇒ người làm: như <b>жи́тель</b> '
    '(<b>жить</b>). Trọng âm giữ chỗ của động từ: <b>покупа́ть</b> → <b>покупа́тель</b>.</div>'
    '<div class="hd-warn">Khách cửa hàng = <b>покупа́тель</b>; khách của ngân hàng, luật sư, '
    'dịch vụ = <b>клие́нт</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>покупа́ть</b> / <b>купи́ть</b> mua · <b>поку́пка</b> món đồ mua · '
    '<b>това́р</b> hàng hoá · <b>торго́вля</b> thương mại</div>'
)

S["премия"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn (Latin <i>praemium</i> «phần thưởng»), không chẻ theo tiếng Nga. '
    'Cùng gốc tiếng Anh <i>premium</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hai nghĩa đều là «tiền trao để thưởng»: tiền thưởng ở cơ quan, và giải '
    'thưởng có tiền — <b>Но́белевская пре́мия</b> giải Nobel.</div>'
    '<div class="hd-warn">Huân chương, phần thưởng nói chung = <b>награ́да</b>; khoản tiền hay '
    'giải mang tên = <b>пре́мия</b>.</div>'
)

S["торговля"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">торг-</span>'
    '<span class="hd-gloss">BUÔN BÁN, mặc cả</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ов-</span>'
    '<span class="hd-gloss">mảnh của <b>торгова́ть</b>, không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ля</span>'
    '<span class="hd-gloss">danh từ chỉ HOẠT ĐỘNG, giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Việc <b>торгова́ть</b> ⇒ thương mại. Bán <b>това́р</b> cho '
    '<b>покупа́тель</b>. Gần như chỉ dùng số ít.</div>'
    '<div class="hd-warn"><b>торго́вый центр</b> = trung tâm thương mại — tính từ '
    '<b>торго́вый</b> cùng gốc, gặp hằng ngày.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>торгова́ть</b> buôn bán · <b>торго́вый</b> thuộc thương mại · '
    '<b>торг</b> sự mặc cả</div>'
)

S["дочка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">доч-</span>'
    '<span class="hd-gloss"><b>дочь</b> con gái</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">đuôi thân mật</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cách gọi thường ngày, ấm áp hơn <b>дочь</b>. Số nhiều cách 2 chèn '
    '<i>е</i> như phần lớn từ đuôi <i>-ка</i>: <b>до́чек</b>.</div>'
    '<div class="hd-warn">Lợi thế lớn: <b>до́чка</b> chia ĐỀU như danh từ <i>-а</i> thường '
    '(<b>до́чки</b>, <b>до́чку</b>), còn <b>дочь</b> bất quy tắc (<b>до́чери</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дочь</b> con gái · <b>до́ченька</b> con gái cưng</div>'
)

S["семейный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">семей-</span>'
    '<span class="hd-gloss"><b>семья́</b> GIA ĐÌNH — âm <i>й</i> ẩn trong <i>-ья</i> lộ ra</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ный</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thuộc về <b>семья́</b>»: <b>семе́йный бюдже́т</b> ngân sách gia đình. '
    'Trọng âm lùi về <i>-ме́-</i>.</div>'
    '<div class="hd-warn"><b>семе́йный челове́к</b> = người đã có vợ/chồng con. Thuộc «nhà» '
    '(nấu ở nhà, vật nuôi) thì là <b>дома́шний</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>семья́</b> gia đình · <b>семьяни́н</b> người của gia đình</div>'
)

V = {
    "борода": "râu",
    "прожить": "sống được, sống qua",
    "погибать": "bỏ mạng",
    "погибнуть": "bỏ mạng",
    "покупатель": "người mua",
    "товар": "hàng hoá",
    "семейный": "của gia đình",
    "торговля": "thương mại, buôn bán",
}
