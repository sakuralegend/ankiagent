# -*- coding: utf-8 -*-
"""k102 — life-food: từ mới A2 rời nhau, soạn từng thẻ độc lập; hai cặp thể варить/сварить, одеваться/одеться soạn như một họ."""

# 🔴 KHÔNG dựng biến khối dùng chung (HE/LUAT/THE…) rồi cộng vào mọi thẻ — README §3.

S = {}
V = {}

S["аппетит"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ bằng phụ tố Nga: mượn Latin <i>appetitus</i> «sự thèm muốn» — cùng gốc tiếng Anh <i>appetite</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gần như đọc theo tiếng Anh; viết hai chữ <b>п</b> như hai chữ <i>p</i>. Giống đực, biến cách đều.</div>'
    '<div class="hd-warn">Câu chúc trước bữa ăn: <b>Прия́тного аппети́та!</b> — Chúc ngon miệng! Đứng ở cách 2 vì ngầm hiểu <b>жела́ю</b> «tôi chúc», mà động từ chúc đòi cách 2.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>аппети́тный</b> trông ngon, hấp dẫn</div>'
)

S["варить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вар-</span><span class="hd-gloss">gốc ĐUN SÔI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-ть</span><span class="hd-gloss">đuôi động từ, lớp chia 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mọi kiểu <b>вари́ть</b> đều nấu TRONG NƯỚC, món bị nấu ở cách 4: <i>вари́ть суп</i> nấu canh, <i>вари́ть яйцо́</i> luộc trứng, <i>вари́ть ко́фе</i> pha cà phê. Chỉ ngôi «tôi» nhấn đuôi: <b>варю́</b>, còn lại lùi về thân: <b>ва́ришь, ва́рит … ва́рят</b>. Cặp hoàn thành: <b>свари́ть</b>.</div>'
    '<div class="hd-warn">Nấu nói chung, nhất là rán, nướng, là <b>гото́вить</b>. Không có nước thì không dùng <b>вари́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>по́вар</b> đầu bếp · <b>варе́нье</b> mứt · <b>варёный</b> đã luộc</div>'
)
V["варить"] = "nấu, luộc, đun sôi, pha"

S["сварить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span><span class="hd-gloss">tiền tố HOÀN THÀNH — ở nghĩa «nấu» không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">вар-</span><span class="hd-gloss">gốc ĐUN SÔI, như <b>вари́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-ть</span><span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Là <b>вари́ть</b> đã nấu XONG: <i>Я свари́л суп</i> — tôi nấu xong nồi canh. Trọng âm nhảy y hệt cặp của nó: <b>сварю́</b> nhưng <b>сва́ришь, сва́рит …</b> — và đây là tương lai, không phải hiện tại. Ở nghĩa «hàn» kim loại, đọc <b>с-</b> là «lại với nhau» thì khớp: nung chảy cho hai mảnh dính vào nhau.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сва́рка</b> sự hàn · <b>сва́рщик</b> thợ hàn</div>'
)
V["сварить"] = "nấu chín, luộc, đun sôi, pha, hàn"

S["висеть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вис-</span><span class="hd-gloss">gốc TREO</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е-ть</span><span class="hd-gloss">đuôi động từ trạng thái, lớp chia 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tả TRẠNG THÁI đang treo, không có tân ngữ: <i>Карти́на виси́т на стене́</i> — bức tranh treo trên tường (chỗ tiếng Anh chỉ nói <i>is</i>). Ngôi «tôi» đổi <b>с→ш</b>: <b>вишу́</b>; mọi ngôi khác giữ <b>с</b>: <b>виси́шь, вися́т</b>.</div>'
    '<div class="hd-warn">Treo một vật LÊN (có tân ngữ, cách 4) là động từ khác: <b>ве́шать</b> / <b>пове́сить</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ве́шать</b>, <b>пове́сить</b> treo lên · <b>ве́шалка</b> móc áo · <b>зави́сеть</b> phụ thuộc — «treo vào», y như tiếng Anh <i>depend</i></div>'
)

S["грипп"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn Pháp <i>grippe</i> (bệnh cúm).</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giữ hai chữ <b>п</b> như tiếng Pháp. Giống đực, biến cách đều: <b>гри́ппа, гри́ппом</b>.</div>'
    '<div class="hd-warn">Bị cúm: <b>боле́ть гри́ппом</b> / <b>заболе́ть гри́ппом</b> — sau hai động từ này, tên bệnh đứng ở cách 5.</div>'
)

S["душ"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn Pháp <i>douche</i> (vòi sen).</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giống đực vì tận cùng phụ âm. Trọng âm đứng yên ở thân: <b>в ду́ше</b>. Tắm vòi sen là <b>принима́ть душ</b> — «nhận» vòi sen.</div>'
    '<div class="hd-warn">Đừng lẫn với <b>душа́</b> tâm hồn — khác gốc hoàn toàn, chỉ giống mặt chữ. Trọng âm tách hai từ: <b>в ду́ше</b> trong phòng tắm, <b>в душе́</b> trong lòng.</div>'
)

S["коридор"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ bằng phụ tố Nga: mượn Ý <i>corridore</i>, từ <i>correre</i> «chạy» — cùng gốc tiếng Anh <i>corridor</i>, <i>courier</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hành lang là «lối chạy qua» giữa các phòng. Giống đực, biến cách đều, trọng âm đứng yên: <b>в коридо́ре</b>.</div>'
)

S["ксерокс"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: tên hãng <i>Xerox</i> biến thành danh từ chung.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>кс</b> chính là chữ <i>X</i>; trọng âm ở đầu. Một từ hai nghĩa: vừa là cái máy, vừa là bản chụp ra — <i>сде́лать ксе́рокс</i> photo một bản.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ксероко́пия</b> bản sao chụp (cách nói trang trọng)</div>'
)

S["лекарство"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">лек-</span><span class="hd-gloss">gốc CHỮA bệnh</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ар-</span><span class="hd-gloss">hậu tố chỉ người — <b>ле́карь</b> thầy lang</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ств-о</span><span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: «thứ của thầy chữa bệnh». Gốc <b>лек-</b> đổi <b>к→ч</b> thành <b>лечи́ть</b> chữa bệnh — cùng phép biến âm <b>к→ч</b> đã gặp.</div>'
    '<div class="hd-warn">Uống thuốc thường nói <b>принима́ть лека́рство</b>. Thuốc chữa bệnh gì: <b>от</b> + cách 2 — <i>лека́рство от гри́ппа</i> thuốc cúm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лечи́ть</b> chữa bệnh · <b>лече́ние</b> sự điều trị · <b>лека́рственный</b> thuộc về thuốc</div>'
)

S["лестница"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ле́ст-</span><span class="hd-gloss">gốc cổ «TRÈO»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ниц-а</span><span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cái để trèo lên» — cả cầu thang lẫn cái thang đều là <b>ле́стница</b>. Đi bằng cầu thang: <b>по</b> + cách 3 — <i>подня́ться по ле́стнице</i>.</div>'
    '<div class="hd-warn">Cụm <b>стн</b> đọc nuốt mất <b>т</b> (như <b>изве́стный</b>, <b>че́стный</b>) nhưng VIẾT vẫn phải có <b>т</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: nối <b>ле́ст-</b> với «trèo» là từ nguyên (qua dạng cổ <i>лѣствица</i>, họ xa với <b>лезть</b>), không phải luật suy ra được.</div>'
)

S["лимон"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: từ mượn (gốc Ba Tư, qua châu Âu) — cùng gốc tiếng Anh <i>lemon</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giống đực, biến cách đều. Trà chanh: <i>чай с лимо́ном</i> — <b>с</b> + cách 5.</div>'
    '<div class="hd-warn"><b>лимо́н</b> là chanh VÀNG quả to. Chanh xanh nhỏ quen ở Việt Nam là <b>лайм</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лимо́нный</b> thuộc về chanh — <i>лимо́нный сок</i> nước cốt chanh · <b>лимона́д</b> nước chanh, nước ngọt</div>'
)

S["носок"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">нос-</span><span class="hd-gloss">MŨI — như <b>нос</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́к</span><span class="hd-gloss">hậu tố NHỎ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cái mũi nhỏ»: nghĩa mũi giày, đầu mũi bàn chân vẫn còn dùng; chiếc tất là thứ bọc lấy phần đó. Nguyên âm <b>о</b> của <b>-ок</b> rụng ở mọi dạng khác: <b>носки́, носко́в</b> — và trọng âm luôn ở đuôi.</div>'
    '<div class="hd-warn"><b>нос-</b> ở đây là MŨI, không phải gốc «mang» của <b>носи́ть</b> — giống mặt chữ, khác gốc. Đi tất: <i>носи́ть носки́</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>нос</b> mũi · <b>но́сик</b> mũi nhỏ, vòi ấm</div>'
)

S["овощной"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">овощ-</span><span class="hd-gloss">RAU CỦ — như <b>о́вощ</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-</span><span class="hd-gloss">→ tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́й</span><span class="hd-gloss">đuôi tính từ mang trọng âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ → tính từ bằng <b>-н-</b>, trọng âm nhảy từ <b>о́вощ</b> sang đuôi: <b>овощно́й</b>. Chỉ nghĩa «thuộc về rau» nên không có dạng ngắn: <i>овощно́й суп</i> súp rau, <i>овощно́й магази́н</i> cửa hàng rau.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>о́вощ</b> một loại rau · <b>о́вощи</b> rau củ</div>'
)

S["одеваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span><span class="hd-gloss">BAO QUANH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-де-</span><span class="hd-gloss">gốc ĐẶT, KHOÁC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва-</span><span class="hd-gloss">hậu tố CHƯA HOÀN THÀNH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть-ся</span><span class="hd-gloss">cho CHÍNH MÌNH</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Khoác bao quanh chính mình». Chia đều lớp 1, <b>-ва-</b> giữ nguyên: <b>одева́юсь, одева́ешься</b>. Còn chỉ cách ăn mặc: <i>Она́ хорошо́ одева́ется</i> — cô ấy ăn mặc đẹp. Cặp hoàn thành: <b>оде́ться</b>.</div>'
    '<div class="hd-warn">Không kèm món đồ: <i>Я одева́юсь</i> — tôi mặc đồ. Mặc MỘT MÓN vào là <b>надева́ть</b>: <i>надева́ть ку́ртку</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оде́жда</b> quần áo · <b>одева́ть</b> mặc cho ai · <b>раздева́ться</b> cởi đồ · <b>переодева́ться</b> thay đồ</div>'
)

S["одеться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span><span class="hd-gloss">BAO QUANH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-де-</span><span class="hd-gloss">gốc ĐẶT, KHOÁC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть-ся</span><span class="hd-gloss">cho CHÍNH MÌNH</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Là <b>одева́ться</b> bỏ <b>-ва-</b> ⇒ hoàn thành: mặc xong. Thân tương lai mọc thêm <b>-н-</b>, phải nhớ riêng: <b>оде́нусь, оде́нешься … оде́нутся</b> — y như <b>наде́ну</b>, <b>разде́нусь</b>. <i>Оде́нься тепло́!</i> — Mặc ấm vào!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оде́жда</b> quần áo · <b>разде́ться</b> cởi đồ · <b>переоде́ться</b> thay đồ</div>'
)
V["одеться"] = "mặc quần áo, mặc đồ"

S["поэзия"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">поэ́з-</span><span class="hd-gloss">Hy Lạp <i>poiesis</i> «sự LÀM RA»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ия</span><span class="hd-gloss">đuôi danh từ mượn, giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc <b>поэ́т</b> «người làm ra»: thơ ca là «cái được làm ra». Đuôi <b>-ия</b> ≈ đuôi <i>-y</i> tiếng Anh (<b>исто́рия</b> <i>history</i>, <b>эне́ргия</b> <i>energy</i>). Viết <b>э</b> sau <b>о</b> như <b>поэ́т</b>. Chỉ dùng số ít.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поэ́т</b> nhà thơ · <b>поэ́ма</b> trường ca · <b>поэти́ческий</b> thuộc về thơ</div>'
)

S["роль"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn Pháp <i>rôle</i> — cùng gốc tiếng Anh <i>role</i> và <i>roll</i> (cuộn giấy chép lời của một vai).</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi <b>-ь</b> mà là giống CÁI: <b>ро́ли, ро́лью</b>. Số nhiều <b>ро́ли</b>, nhưng các cách khác (trừ cách 4) nhảy trọng âm ra đuôi: <b>роле́й, роля́м, роля́ми, роля́х</b>.</div>'
    '<div class="hd-warn">Đóng vai, có vai trò: <b>игра́ть роль</b>. Phủ định thì sang cách 2: <b>Э́то не игра́ет ро́ли</b> — chuyện đó không quan trọng.</div>'
)

S["сигарета"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сигар-</span><span class="hd-gloss">XÌ GÀ — <b>сига́ра</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ет-а</span><span class="hd-gloss">hậu tố NHỎ, từ Pháp <i>-ette</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen «xì gà nhỏ», y như tiếng Anh <i>cigarette</i>. Giống cái, biến cách đều; trọng âm ở <b>-ре́-</b>, khác <b>сига́ра</b>. Hút thuốc: <i>кури́ть сигаре́ту</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сига́ра</b> xì gà</div>'
)
