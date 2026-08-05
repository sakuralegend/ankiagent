# -*- coding: utf-8 -*-
"""k34 — people::family: người trong nhà, tên gọi và việc làm quen.

Trục của lô: gốc `зна-/-ком-` (biết → quen) đẻ ra ba từ và gốc `род-`
(sinh/dòng dõi) đẻ ra hai từ ngay trong lô, nên chẻ từ ở đây trả lãi liền.
Nhóm thứ ba là bộ ba tên gọi Nga и́мя + о́тчество + фами́лия.

Lưu ý khi sửa: thẻ chỉ được nói về CHÍNH TỪ ĐÓ, không được nhắc tới "lô" —
user nhìn một thẻ mỗi lần và không biết lô là gì.
"""

S = {}

S["сын"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сын-</span>'
    '<span class="hd-gloss">gốc Ấn–Âu, nghĩa CON TRAI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ thêm được. Bù lại nó cùng gốc với '
    'tiếng Anh <i>son</i> và tiếng Đức <i>Sohn</i> — nhìn mặt chữ là đoán ra nghĩa. '
    'Đi cặp với <b>дочь</b> (con gái).</div>'
    '<div class="hd-warn">Số nhiều đổi hẳn khuôn: <b>сыновья́</b>, cách 2 '
    '<b>сынове́й</b> — thân từ dài ra <b>-овь-</b> và trọng âm nhảy ra tận đuôi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сыно́к</b> con trai (gọi thân) · '
    '<b>па́сынок</b> con riêng của vợ/chồng</div>'
)

S["отчество"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">отч-</span>'
    '<span class="hd-gloss">từ <b>оте́ц</b> cha, ц đổi thành ч</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ество</span>'
    '<span class="hd-gloss">đuôi làm ra danh từ trừu tượng, giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen là “cái thuộc về cha”: lấy tên bố rồi thêm '
    '<b>-ович</b> (con trai) hoặc <b>-овна</b> (con gái). Bố tên <b>Ива́н</b> ⇒ '
    'con là <b>Ива́нович</b> / <b>Ива́новна</b>.</div>'
    '<div class="hd-warn">Gọi lịch sự một người Nga là и́мя + о́тчество '
    '(<b>Ива́н Ива́нович</b>), KHÔNG dùng họ như kiểu Mr. + surname.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оте́ц</b> cha · <b>оте́чество</b> tổ quốc · '
    '<b>оте́ческий</b> như cha, ân cần</div>'
)

S["знакомство"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">зна-</span>'
    '<span class="hd-gloss">biết (từ <b>знать</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ком-</span>'
    '<span class="hd-gloss">thân của <b>знако́мый</b> đã quen</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ство</span>'
    '<span class="hd-gloss">đuôi làm ra danh từ trừu tượng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cộng lại: “cái sự biết nhau” ⇒ sự làm quen, và cả mối '
    'quen biết đã có sẵn. Đuôi <b>-ство</b> chỉ SỰ VIỆC chứ không chỉ người — '
    'người quen là <b>знако́мый</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>знать</b> biết · <b>знако́мый</b> người quen · '
    '<b>знако́миться</b> làm quen · <b>познако́миться</b> quen được</div>'
)

S["брат"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">брат-</span>'
    '<span class="hd-gloss">gốc Ấn–Âu, nghĩa ANH EM TRAI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc trơn, cùng gốc tiếng Anh <i>brother</i>. Tiếng Nga '
    'KHÔNG tách anh với em; cần nói rõ thì thêm <b>ста́рший</b> (lớn) hoặc '
    '<b>мла́дший</b> (nhỏ). Đi cặp với <b>сестра́</b> (chị/em gái).</div>'
    '<div class="hd-warn">Số nhiều đổi khuôn: <b>бра́тья</b>, cách 2 '
    '<b>бра́тьев</b> — thêm <b>-ья</b> giống <b>сыновья́</b> nhưng trọng âm đứng yên.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бра́тский</b> huynh đệ · <b>бра́тство</b> tình anh em</div>'
)

S["китаец"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">Кита́й-</span>'
    '<span class="hd-gloss">nước Trung Quốc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ец</span>'
    '<span class="hd-gloss">người thuộc nơi đó, giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tên nước + <b>-ец</b> = người của nước đó. Ba từ luôn đi '
    'thành bộ: <b>кита́ец</b> (nam) — <b>китая́нка</b> (nữ) — <b>кита́йский</b> '
    '(tính từ).</div>'
    '<div class="hd-warn">Biến cách thì thân từ đổi mặt: chữ <b>е</b> của <b>-ец</b> '
    'chạy mất, còn chữ <b>й</b> của <b>Кита́й</b> quay lại — <b>кита́йца</b>, '
    '<b>кита́йцу</b>, <b>кита́йцем</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>Кита́й</b> Trung Quốc · <b>кита́йский</b> thuộc Trung Quốc · '
    '<b>китая́нка</b> phụ nữ Trung Quốc</div>'
)

S["американец"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">Аме́рик-</span>'
    '<span class="hd-gloss">nước Mỹ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ан-</span>'
    '<span class="hd-gloss">chèn thêm trước đuôi chỉ người</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ец</span>'
    '<span class="hd-gloss">người thuộc nơi đó, giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng khuôn với <b>кита́ец</b>, chỉ khác là có chèn thêm '
    '<b>-ан-</b>: <b>америка́нка</b> (nữ), <b>америка́нский</b> (tính từ). Chữ '
    '<b>е</b> cũng chạy mất khi biến cách — <b>америка́нца</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>Аме́рика</b> nước Mỹ · <b>америка́нский</b> thuộc Mỹ · '
    '<b>америка́нка</b> phụ nữ Mỹ</div>'
)

S["отец"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">gốc rất cổ, nghĩa CHA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ец</span>'
    '<span class="hd-gloss">hậu tố cũ; ở đây KHÔNG có nghĩa “người của nơi nào” '
    'như <b>кита́ец</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>от-</b> (biến thành <b>отч-</b>) đẻ ra cả họ: '
    '<b>о́тчество</b> tên đệm theo cha, <b>оте́чество</b> tổ quốc — đúng là “đất của cha”.</div>'
    '<div class="hd-warn">Nguyên âm <b>е</b> chạy mất và trọng âm nhảy ra đuôi: '
    '<b>отца́</b>, <b>отцу́</b>, <b>отцо́м</b>.</div>'
    '<div class="hd-warn">Đây là từ trang trọng, dùng khi nói VỀ cha. Gọi trong '
    'nhà thì dùng <b>па́па</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>о́тчество</b> tên đệm · <b>оте́чество</b> tổ quốc · '
    '<b>оте́ческий</b> như cha</div>'
)

S["молодёжь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">молод-</span>'
    '<span class="hd-gloss">trẻ (từ <b>молодо́й</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ёжь</span>'
    '<span class="hd-gloss">đuôi hiếm, gom cả lớp người thành MỘT KHỐI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">“Cái khối những người trẻ” ⇒ giới trẻ nói chung. Dấu '
    '<b>ь</b> đứng sau ж/ш/ч/щ là báo hiệu chắc chắn của danh từ giống cái '
    '(<b>ночь</b>, <b>дочь</b>, <b>рожь</b>).</div>'
    '<div class="hd-warn">Là danh từ TẬP HỢP: luôn ở số ít, động từ theo cũng chia '
    'số ít — <b>молодёжь лю́бит</b>… Muốn nói MỘT người trẻ thì phải dùng '
    '<b>молодо́й челове́к</b>, không dùng từ này.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>молодо́й</b> trẻ · <b>мо́лодость</b> tuổi trẻ · '
    '<b>моло́же</b> trẻ hơn</div>'
)

S["родитель"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">род-</span>'
    '<span class="hd-gloss">sinh ra, dòng dõi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-</span>'
    '<span class="hd-gloss">âm nối của <b>роди́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-тель</span>'
    '<span class="hd-gloss">NGƯỜI làm việc đó, giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">“Người sinh ra mình”. Đuôi <b>-тель</b> mở khoá cả một '
    'lớp từ chỉ người: <b>учи́тель</b> người dạy, <b>писа́тель</b> người viết.</div>'
    '<div class="hd-warn">Số ít là MỘT người — bố hoặc mẹ. Muốn nói “bố mẹ” thì '
    'phải dùng số nhiều <b>роди́тели</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>роди́ться</b> chào đời · <b>род</b> dòng họ · '
    '<b>ро́дина</b> quê hương</div>'
)

S["мать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мат-</span>'
    '<span class="hd-gloss">gốc Ấn–Âu, nghĩa MẸ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc trơn rất cổ, cùng gốc với tiếng Anh <i>mother</i> và '
    'tiếng Latin <i>mater</i> — nhìn mặt chữ là đoán ra nghĩa.</div>'
    '<div class="hd-warn">Thân từ DÀI RA thành <b>матер-</b> ở mọi cách còn lại: '
    '<b>ма́тери</b>, <b>ма́терью</b>. Cùng kiểu với <b>дочь</b> → <b>до́чери</b>.</div>'
    '<div class="hd-warn">Đây là từ trang trọng, dùng trong giấy tờ và khi nói VỀ '
    'mẹ. Gọi trong nhà thì dùng <b>ма́ма</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>матери́нский</b> thuộc về mẹ · <b>матери́нство</b> '
    'thiên chức làm mẹ</div>'
)

S["национальность"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">наци-</span>'
    '<span class="hd-gloss">từ <b>на́ция</b> dân tộc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-альн-</span>'
    '<span class="hd-gloss">đuôi tính từ của kho từ quốc tế</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ость</span>'
    '<span class="hd-gloss">biến tính từ thành danh từ chỉ TÍNH CHẤT, giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đi ba bước là ra: <b>на́ция</b> → <b>национа́льный</b> → '
    '<b>национа́льность</b>: <b>-альный</b> làm ra tính từ, <b>-ость</b> biến tính '
    'từ đó thành danh từ chỉ tính chất.</div>'
    '<div class="hd-warn">Nga tách hai thứ tiếng Việt hay gộp: từ này là dân tộc, '
    'gốc gác; còn quốc tịch ghi trên giấy tờ là <b>гражда́нство</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>на́ция</b> dân tộc · <b>национа́льный</b> thuộc dân tộc · '
    '<b>интернациона́льный</b> quốc tế</div>'
)

S["дядя"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дя-дя</span>'
    '<span class="hd-gloss">lặp âm, từ trong tiếng trẻ con — không chẻ ra nghĩa được</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi <b>-я</b> trông y như từ giống cái, nhưng đây là giống '
    'ĐỰC: biến cách vẫn theo mẫu <b>-я</b>, còn tính từ và động từ đi kèm thì theo '
    'giống đực — <b>мой дя́дя пришёл</b>.</div>'
    '<div class="hd-warn">Số nhiều có hai lối: <b>дя́ди</b> (thường gặp) và '
    '<b>дядья́</b>, <b>дядья́м</b> — lối sau kéo trọng âm ra đuôi, cùng kiểu <b>бра́тья</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дя́дюшка</b> chú/bác (gọi thân mật)</div>'
)

S["фамилия"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">фамил-</span>'
    '<span class="hd-gloss">mượn thẳng tiếng Latin <i>familia</i> nhà, gia đình</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ия</span>'
    '<span class="hd-gloss">đuôi quen thuộc của từ mượn, giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mượn nguyên chữ nhưng NGHĨA ĐÃ DỊCH CHỖ: trong tiếng Nga '
    'nó là cái HỌ, tức tên chung của cả nhà. Cụm hay gặp: <b>по фами́лии</b> = '
    'theo họ, gọi bằng họ.</div>'
    '<div class="hd-warn">Bạn giả kinh điển: đây KHÔNG phải <i>family</i>. '
    '“Gia đình” trong tiếng Nga là <b>семья́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>фамилья́рный</b> suồng sã, thân quá mức</div>'
)

S["имя"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">им- / имен-</span>'
    '<span class="hd-gloss">gốc, nghĩa TÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-я</span>'
    '<span class="hd-gloss">đuôi của nhóm danh từ giống trung <b>-мя</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tên đầy đủ của người Nga gồm ba phần, và đây là phần đầu: '
    '<b>и́мя</b> tên riêng + <b>о́тчество</b> đệm theo tên cha + <b>фами́лия</b> họ.</div>'
    '<div class="hd-warn">Thuộc nhóm 10 danh từ <b>-мя</b>: thân từ dài ra thành '
    '<b>имен-</b> khi biến cách — <b>и́мени</b>, <b>и́менем</b>. Y hệt <b>вре́мя</b> → '
    '<b>вре́мени</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>имени́ны</b> ngày lễ vị thánh trùng tên mình · '
    '<b>имени́тельный паде́ж</b> cách 1, đúng nghĩa “cách gọi tên”</div>'
)

S["няня"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ня-ня</span>'
    '<span class="hd-gloss">lặp âm, từ trong tiếng trẻ con — không chẻ ra nghĩa được</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng kiểu “từ nôi” với <b>ма́ма</b>, <b>па́па</b>, '
    '<b>дя́дя</b>: hai âm tiết lặp cho trẻ dễ gọi. Ở đây đuôi <b>-я</b> khớp đúng '
    'giống cái, biến cách đều đặn nên không có gì phải thuộc riêng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ня́нчить</b> bế, trông trẻ · <b>ня́нька</b> bảo mẫu '
    '(nói suồng)</div>'
)

S["родиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">род-</span>'
    '<span class="hd-gloss">sinh ra, dòng dõi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-</span>'
    '<span class="hd-gloss">âm nối, xếp từ này vào lớp chia thứ hai</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ться</span>'
    '<span class="hd-gloss">phản thân: việc quay ngược về chính mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>роди́ть</b> là “sinh ra ai đó”; thêm <b>-ся</b> quay '
    'về mình thành “được sinh ra” ⇒ chào đời.</div>'
    '<div class="hd-warn">Ngôi “tôi” biến âm д→ж: <b>я рожу́сь</b>. Quá khứ thì '
    'trọng âm chạy: <b>он роди́лся</b> nhưng <b>она́ родила́сь</b>.</div>'
    '<div class="hd-warn">Nói năm hoặc nơi sinh thì đi với <b>в</b> + cách 6: '
    '<b>роди́лся в Москве́</b>, <b>в 1990 году́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>роди́тель</b> bố hoặc mẹ · <b>рожде́ние</b> sự ra đời · '
    '<b>ро́дина</b> quê hương</div>'
)

S["знакомиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">зна-</span>'
    '<span class="hd-gloss">biết (từ <b>знать</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ком-</span>'
    '<span class="hd-gloss">thân của <b>знако́мый</b> đã quen</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-ться</span>'
    '<span class="hd-gloss">phản thân: làm cho CHÍNH MÌNH quen</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chuỗi ba bước: <b>знать</b> biết → <b>знако́мый</b> đã quen '
    '→ <b>знако́миться</b> đang tự làm quen với ai.</div>'
    '<div class="hd-warn">Bắt buộc đi với <b>с</b> + cách 5: <b>знако́миться с '
    'людьми́</b>. Không dùng cách 4.</div>'
    '<div class="hd-warn">Ngôi “tôi” chèn thêm <b>-л-</b>: <b>я знако́млюсь</b> '
    '(м → мл, y hệt <b>люби́ть</b> → <b>люблю́</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>знать</b> biết · <b>знако́мый</b> người quen · '
    '<b>знако́мство</b> sự quen biết · <b>познако́миться</b> quen được</div>'
)

S["познакомиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố chỉ để đóng việc lại, KHÔNG thêm nghĩa riêng nào</span></div>'
    '<div class="hd-row"><span class="hd-piece">знако́миться</span>'
    '<span class="hd-gloss">đang làm quen</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thêm mỗi <b>по-</b> là việc làm quen có ĐIỂM KẾT: từ chỗ '
    'lạ thành chỗ quen. <b>Мы познако́мились в шко́ле</b> = chúng tôi quen nhau hồi đi học.</div>'
    '<div class="hd-warn">Câu phải thuộc: <b>Прия́тно познако́миться!</b> = Rất vui '
    'được làm quen.</div>'
    '<div class="hd-warn">Vẫn đi với <b>с</b> + cách 5, và ngôi “tôi” vẫn chèn '
    '<b>-л-</b>: <b>я познако́млюсь с ним</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>знако́миться</b> đang làm quen · <b>знако́мство</b> '
    'sự quen biết · <b>знако́мый</b> người quen</div>'
)

S["тётя"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">тё-тя</span>'
    '<span class="hd-gloss">lặp âm, từ trong tiếng trẻ con — không chẻ ra nghĩa được</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp đôi với <b>дя́дя</b>: chị hoặc em gái của bố mẹ, và '
    'cũng dùng cho vợ của chú bác. Chữ <b>ё</b> luôn mang trọng âm nên từ này không '
    'bao giờ phải đánh dấu.</div>'
    '<div class="hd-warn">Số nhiều cách 2 có hai lối song song: <b>тёть</b> và '
    '<b>тётей</b> — dùng lối nào cũng đúng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тётушка</b> cô/dì (gọi thân mật) · <b>тётка</b> bà cô '
    '(nói suồng)</div>'
)

S["семья"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сем-</span>'
    '<span class="hd-gloss">gốc, nghĩa NGƯỜI NHÀ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ья</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái, trọng âm rơi vào nó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>сем-</b> lộ ra ngay ở các từ cùng nhà: '
    '<b>семе́йный</b> thuộc gia đình, <b>семе́йство</b> họ (trong sinh học).</div>'
    '<div class="hd-warn">Sang số nhiều trọng âm chạy ngược về đầu — <b>се́мьи</b>; '
    'riêng cách 2 số nhiều chèn thêm е và giữ trọng âm ở đuôi — <b>семе́й</b>.</div>'
    '<div class="hd-warn">Đừng lẫn với <b>фами́лия</b>: từ đó là HỌ, không phải gia đình.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>семе́йный</b> thuộc gia đình · <b>семе́йство</b> họ '
    '(sinh học) · <b>семьяни́н</b> người chăm lo gia đình</div>'
)


# =========================================================================
# V — sửa field `Vietnamese` (đề bài deck 1-go). CHỈ những từ cần làm rõ.
# Không ghi từ loại / giống / thể / phản thân: mặt đề bài đã in sẵn badge.
# =========================================================================
V = {
    'знакомство': 'sự làm quen, mối quen biết',
    'знакомиться': 'làm quen',
    'познакомиться': 'làm quen, quen được',
    'имя': 'tên riêng, phần tên gọi của một người',
    'фамилия': 'họ, tên chung của cả nhà',
    'отчество': 'tên đệm lấy theo tên bố',
    'отец': 'cha, bố',
    'мать': 'mẹ, người mẹ',
    'родитель': 'bố hoặc mẹ, tính riêng một người',
    'молодёжь': 'giới trẻ, thanh niên',
    'национальность': 'dân tộc, tộc người',
    'родиться': 'chào đời, được sinh ra',
    'семья': 'gia đình',
}

