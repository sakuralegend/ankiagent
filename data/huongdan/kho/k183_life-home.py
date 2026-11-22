# -*- coding: utf-8 -*-
"""k183 — life::home (lô trộn): ba cặp động từ việc làm + đồ trong nhà + vài từ y tế.

Chỗ cần nhất quán trong lô:
(1) Ba cặp thể trình bày cùng một khuôn: cuối «Cách nhớ» ghi «Cặp HT/CHT: …», Họ hàng
    mở đầu bằng từ cặp kèm (HT)/(CHT) — như k171.
(2) зараба́тывать/зарабо́тать: раб-/рабо́т- khớp рабо́тать, зарпла́та. Máy ghép ара́б = báo oan.
(3) нанима́ть/наня́ть: -ним-/-ня- «LẤY» khớp k122 (подня́ть, снять). Máy ghép мать = báo oan.
(4) уво́лить/увольня́ть: -вол- khớp во́ля, позво́лить [k157]; khuôn -ить → -ять như позво́лить/позволя́ть.
(5) обстано́вка: gốc ста-/стан- khớp станови́ться [k113] «gốc ста- mọc н, như остано́вка».
(6) Từ mượn: г thay h (го́спиталь, như исто́рия, геро́й); -y → -ия, -tion → -ция.
Họ hàng cố ý vắng: холл (từ mượn đứng một mình).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "обстановка": "tình hình, hoàn cảnh, bối cảnh, không khí, đồ đạc, cách bày trí",  # thiếu furnishings/decor/atmosphere — nghĩa «nhà» của chính topic
    "аренда": "sự thuê, sự cho thuê, tiền thuê",            # bỏ «hợp đồng thuê» = договор аренды (nới rộng)
}

# --------------------------------------------------------------- зарабатывать
S["зарабатывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">ĐẠT LẤY nhờ làm việc đó</span></div>'
    '<div class="hd-row"><span class="hd-piece">-рабат-</span>'
    '<span class="hd-gloss">LÀM VIỆC — <i>рабо́т-</i> của <b>рабо́тать</b>, о → а</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm việc để LẤY về ⇒ kiếm tiền: <b>зараба́тывать на жизнь</b> kiếm sống. '
    'Chia đều: <b>зараба́тываю</b>. Cặp HT: <b>зарабо́тать</b>.</div>'
    '<div class="hd-warn">Luật suy ra được: hậu tố <b>-ыва-</b> hay biến <b>о</b> của gốc thành '
    '<b>а</b>: <b>зарабо́тать → зараба́тывать</b>, <b>опозда́ть → опа́здывать</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>зарабо́тать</b> kiếm được (HT) · <b>рабо́тать</b> làm việc · '
    '<b>за́работок</b> tiền kiếm được · <b>зарпла́та</b> lương (= <b>за́работная пла́та</b>)</div>'
)

# --------------------------------------------------------------- заработать
S["заработать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">ĐẠT LẤY nhờ làm · hoặc BẮT ĐẦU</span></div>'
    '<div class="hd-row"><span class="hd-piece">-рабо́т-ать</span>'
    '<span class="hd-gloss">LÀM VIỆC — như <b>рабо́тать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm để đạt lấy ⇒ kiếm được: <b>зарабо́тать де́ньги</b>. Chia như '
    '<b>рабо́тать</b>: <b>зарабо́таю, зарабо́таешь</b>. Cặp CHT: <b>зараба́тывать</b>.</div>'
    '<div class="hd-warn"><b>за-</b> «BẮT ĐẦU» (như <b>запла́кать</b> bật khóc): '
    '<b>Мото́р зарабо́тал</b> — máy bắt đầu chạy. Nghĩa này <b>зараба́тывать</b> không có.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>зараба́тывать</b> kiếm tiền (CHT) · <b>рабо́тать</b> làm việc · '
    '<b>за́работок</b> tiền kiếm được · <b>зарпла́та</b> lương</div>'
)

# --------------------------------------------------------------- нанимать
S["нанимать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng rõ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ним-</span>'
    '<span class="hd-gloss">LẤY — như <b>снима́ть</b>, <b>понима́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Lấy» người về làm cho mình ⇒ thuê, tuyển: <b>нанима́ть рабо́чих</b> '
    'thuê thợ. Chia đều: <b>нанима́ю</b>. Cặp HT: <b>наня́ть</b>.</div>'
    '<div class="hd-warn">Thuê NGƯỜI → <b>нанима́ть</b>. Thuê NHÀ để ở, người Nga hay nói '
    '<b>снима́ть кварти́ру</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>наня́ть</b> thuê (HT) · <b>наём</b> sự thuê · '
    '<b>наёмник</b> lính đánh thuê · cùng gốc «lấy»: <b>снима́ть</b>, <b>принима́ть</b></div>'
)

# --------------------------------------------------------------- нанять
S["нанять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">tiền tố, không mang nghĩa riêng rõ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ня-ть</span>'
    '<span class="hd-gloss">LẤY — mặt ngắn của <i>-ним-</i>, như <b>поня́ть</b>, <b>снять</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thuê, tuyển xong một người. Tương lai phải nhớ riêng: <b>-ня-</b> thành '
    '<b>-йм-</b>: <b>найму́, наймёшь</b> — giống <b>заня́ть → займу́</b>, <b>поня́ть → пойму́</b>. '
    'Quá khứ nhấn nhảy: <b>на́нял, наняла́, на́няли</b>. Cặp CHT: <b>нанима́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>нанима́ть</b> thuê (CHT) · <b>наём</b> sự thuê · '
    '<b>заня́ть</b> chiếm · <b>поня́ть</b> hiểu</div>'
)

# --------------------------------------------------------------- уволить
S["уволить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">RỜI KHỎI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вол-</span>'
    '<span class="hd-gloss">TỰ DO, Ý MUỐN — <b>во́ля</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vốn là «thả về tự do» ⇒ cho thôi việc, sa thải: <b>уво́лить с рабо́ты</b>. '
    'Chia <b>уво́лю, уво́лишь</b>. Cặp CHT: <b>увольня́ть</b> — đúng khuôn '
    '<b>позво́лить → позволя́ть</b>.</div>'
    '<div class="hd-warn">Thêm <b>-ся</b> là TỰ nghỉ: <b>Я уво́лился</b> — tôi đã xin nghỉ việc. '
    'Không <b>-ся</b> + cách 4 là đuổi người khác: <b>уво́лить сотру́дника</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>увольня́ть</b> sa thải (CHT) · <b>увольне́ние</b> sự sa thải · '
    '<b>во́ля</b> ý muốn, tự do · <b>позво́лить</b> cho phép</div>'
)

# --------------------------------------------------------------- увольнять
S["увольнять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">RỜI KHỎI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-воль-</span>'
    '<span class="hd-gloss">TỰ DO — <i>вол-</i> của <b>во́ля</b>, л mềm trước я</span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thả về tự do» ⇒ sa thải, cho thôi việc (đang diễn ra, lặp lại): '
    '<b>Его́ увольня́ют</b> — anh ấy đang bị cho nghỉ. Chia đều: <b>увольня́ю</b>. '
    'Cặp HT: <b>уво́лить</b>.</div>'
    '<div class="hd-warn"><b>увольня́ть в запа́с</b> — cho xuất ngũ, chuyển sang dự bị: '
    'vẫn là «thả về», nhưng cho lính.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уво́лить</b> sa thải (HT) · <b>увольне́ние</b> sự sa thải · '
    '<b>во́ля</b> ý muốn, tự do · <b>позволя́ть</b> cho phép</div>'
)

# --------------------------------------------------------------- горничная
S["горничная"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">го́рнич-</span>'
    '<span class="hd-gloss">PHÒNG — <b>го́рница</b> phòng sạch trong nhà gỗ xưa; ц → ч như '
    '<b>у́лица → у́личный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ая</span>'
    '<span class="hd-gloss">đuôi tính từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«(Cô) của phòng» ⇒ người hầu phòng, nay là nhân viên dọn phòng khách sạn. '
    'Tính từ đứng làm danh từ nên chia y như tính từ: <b>го́рничной, го́рничную</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>го́рница</b> phòng (nhà xưa) · cùng kiểu tính từ thành danh từ: '
    '<b>столо́вая</b> nhà ăn · <b>ва́нная</b> phòng tắm · <b>гости́ная</b> phòng khách</div>'
)

# --------------------------------------------------------------- предок
S["предок"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пред-</span>'
    '<span class="hd-gloss">TRƯỚC — như <b>пе́ред</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ок</span>'
    '<span class="hd-gloss">đuôi danh từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người có TRƯỚC mình ⇒ tổ tiên. Đối xứng: <b>пото́мок</b> con cháu, người '
    'đến sau. <b>о</b> của <b>-ок</b> rụng khi biến cách: <b>пре́док → пре́дка, пре́дки</b>.</div>'
    '<div class="hd-warn">Khẩu ngữ giới trẻ: <b>мои́ пре́дки</b> = bố mẹ tôi («các cụ nhà tôi»).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пе́ред</b> trước · <b>впереди́</b> phía trước · '
    'đối nghĩa: <b>пото́мок</b> con cháu</div>'
)

# --------------------------------------------------------------- аренда
S["аренда"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn châu Âu (gốc Latin), không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thuê có hợp đồng, thường dài hạn: nhà, đất, xe, mặt bằng. Danh từ là gốc, '
    'động từ mọc ra từ nó: <b>арендова́ть</b> thuê.</div>'
    '<div class="hd-warn">Hai chiều chỉ khác động từ: <b>сдава́ть в аре́нду</b> cho thuê · '
    '<b>брать в аре́нду</b> đi thuê.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>арендова́ть</b> thuê · <b>аренда́тор</b> người thuê · '
    '<b>аре́ндная пла́та</b> tiền thuê</div>'
)

# --------------------------------------------------------------- верёвка
S["верёвка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">верёв-</span>'
    '<span class="hd-gloss">DÂY — từ cổ <i>вервь</i> dây thừng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dây chắc để buộc, kéo, phơi đồ. Số nhiều cách 2 chen thêm <b>о</b>: '
    '<b>верёвок</b> — danh từ đuôi <b>-ка</b> đều thế (<b>остано́вка → остано́вок</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>верёвочка</b> sợi dây nhỏ · <b>верёвочная ле́стница</b> thang dây</div>'
)

# --------------------------------------------------------------- обстановка
S["обстановка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">XUNG QUANH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-станов-</span>'
    '<span class="hd-gloss">ĐẶT CHO ĐỨNG — gốc <i>ста-</i> mọc <i>н</i>, như <b>остано́вка</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">→ danh từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Những thứ được đặt quanh mình ⇒ đồ đạc bày trong phòng ⇒ rộng ra là '
    'hoàn cảnh, tình hình, không khí: <b>в споко́йной обстано́вке</b> trong không khí yên ổn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>остано́вка</b> chỗ dừng · <b>станови́ться</b> trở nên · '
    '<b>поста́вить</b> đặt · <b>обстоя́тельство</b> hoàn cảnh (об- + стоя́-)</div>'
)

# --------------------------------------------------------------- свеча
S["свеча"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">свеч-</span>'
    '<span class="hd-gloss">ÁNH SÁNG — <b>свет</b>, т → ч</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vật cho ánh sáng ⇒ nến. Theo hình cây nến: <b>свеча́ зажига́ния</b> bugi '
    '(«nến đánh lửa»), thuốc đặt. Trọng âm ở đuôi, trừ số nhiều cách 1 và 4: <b>све́чи</b> — '
    'còn lại về đuôi: <b>свече́й, свеча́м</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>свет</b> ánh sáng · <b>све́тлый</b> sáng · '
    '<b>подсве́чник</b> chân nến</div>'
)

# --------------------------------------------------------------- бумажник
S["бумажник"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бума́ж-</span>'
    '<span class="hd-gloss">GIẤY — <b>бума́га</b>, г → ж</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ник</span>'
    '<span class="hd-gloss">đồ vật gắn với thứ đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái đựng tiền GIẤY ⇒ ví gập (thường của nam). Ví nói chung, đựng cả '
    'tiền xu: <b>кошелёк</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бума́га</b> giấy · <b>бума́жный</b> bằng giấy</div>'
)

# --------------------------------------------------------------- холл
S["холл"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn tiếng Anh <i>hall</i> — giữ cả hai chữ <b>л</b>; không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Sảnh rộng ở lối vào khách sạn, toà nhà, nhà hát: <b>в хо́лле гости́ницы</b> '
    'ở sảnh khách sạn. Khác <b>зал</b>: phòng lớn để họp, xem biểu diễn.</div>'
)

# --------------------------------------------------------------- ремонт
S["ремонт"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn tiếng Pháp (<i>remonte</i>), không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Sửa chữa máy móc, sửa sang nhà cửa: <b>де́лать ремо́нт</b> sửa nhà.</div>'
    '<div class="hd-warn"><b>на ремо́нте</b> đang sửa (cách 6: ở đâu) · '
    '<b>закры́то на ремо́нт</b> đóng cửa để sửa (cách 4: hướng tới).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ремонти́ровать</b> sửa (CHT) · <b>отремонти́ровать</b> sửa xong (HT) · '
    '<b>ремо́нтник</b> thợ sửa</div>'
)

# --------------------------------------------------------------- пыль
S["пыль"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giống CÁI dù tận cùng <b>-ь</b> — đuôi này không tự nói giống, phải nhớ. '
    'Gần như chỉ dùng số ít: <b>вытира́ть пыль</b> lau bụi.</div>'
    '<div class="hd-warn"><b>пусти́ть пыль в глаза́</b> — «tung bụi vào mắt» = làm màu, khoe mẽ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пы́льный</b> bụi bặm · <b>пыли́нка</b> hạt bụi · '
    '<b>пылесо́с</b> máy hút bụi (bụi + <i>сос-</i> hút)</div>'
)

# --------------------------------------------------------------- слепой
S["слепой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">слеп-</span>'
    '<span class="hd-gloss">MÙ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́й</span>'
    '<span class="hd-gloss">đuôi tính từ, nhấn ở đuôi</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dạng ngắn trọng âm nhảy, phải nhớ: <b>слеп, слепа́, сле́по, сле́пы</b>. '
    'Đứng một mình làm danh từ: <b>слепо́й</b> người mù.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>осле́пнуть</b> bị mù · <b>ослепи́тельный</b> chói loá («làm mù mắt») · '
    '<b>вслепу́ю</b> mò mẫm, không nhìn</div>'
)

# --------------------------------------------------------------- госпиталь
S["госпиталь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn Latin <i>hospitale</i> = tiếng Anh <i>hospital</i>; <b>г</b> thay '
    '<i>h</i> như <b>исто́рия</b> (history), <b>геро́й</b> (hero). Không chẻ tiếp.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giống ĐỰC dù tận cùng <b>-ь</b>: <b>в го́спитале</b>.</div>'
    '<div class="hd-warn">Ngày nay chủ yếu là bệnh viện QUÂN Y. Bệnh viện thường: <b>больни́ца</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>госпитализа́ция</b> sự nhập viện (mọi bệnh viện) · '
    '<b>госпитализи́ровать</b> cho nhập viện</div>'
)

# --------------------------------------------------------------- аллергия
S["аллергия"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">аллерг-</span>'
    '<span class="hd-gloss">= <i>allergy</i> (Hy Lạp <i>allos</i> khác + <i>ergon</i> tác động)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́я</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái, ứng với <i>-y</i> tiếng Anh</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ quốc tế: <i>-y</i> → <b>-ия</b>, nhấn ở <b>и́</b>.</div>'
    '<div class="hd-warn">Dị ứng VỚI cái gì → <b>на</b> + cách 4: <b>У меня́ аллерги́я на ко́шек</b> '
    '— tôi dị ứng với mèo.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>аллерги́ческий</b> (thuộc) dị ứng · <b>аллерге́н</b> chất gây dị ứng</div>'
)

# --------------------------------------------------------------- инфекция
S["инфекция"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">инфе́к-</span>'
    '<span class="hd-gloss">= <i>infec-</i> (Latin)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ция</span>'
    '<span class="hd-gloss">= <i>-tion</i>, như <b>ста́нция</b>, <b>информа́ция</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhiễm trùng, sự lây nhiễm. Trọng âm rơi vào nguyên âm ngay trước <b>-ция</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>инфекцио́нный</b> truyền nhiễm · <b>дезинфе́кция</b> khử trùng</div>'
)

B = {
    "docbangmat": 89,
    "loitubat": 1,   # инфекция: chẻ «инфе́кц- + -ия» mà gloss lại nói -ция -> chẻ lại «инфе́к- + -ция»
    "nguonsai": 1,   # аренда: đề bài cũ có «hợp đồng thuê» (= договор аренды, nới rộng; gloss Anh chỉ «rent»)
    "baolen": [
        "V cần duyệt: обстановка thêm «không khí, đồ đạc, cách bày trí» (gloss có atmosphere/furnishings/decor — nghĩa «nhà» của đúng topic này mà đề cũ thiếu); аренда bỏ «hợp đồng thuê».",
        "Không viết V cho заработать dù gloss có «earn oneself (something bad) / come down with» mà cặp зарабатывать có «tự gây ra cho mình»: badge thể đã tách cặp, đề không mơ hồ.",
        "Từ điển báo BAT THUONG «nguyên âm chạy» cho обстановка/верёвка (обстано́вок, верёвок): thực ra là quy tắc chung của đuôi -ка -> dạy MỘT lần như luật ở верёвка, bỏ ở обстановка.",
        "Nguồn bẩn: аллергия gloss «allergy，» (dấu phẩy toàn khổ) + CACH DUNG «过敏» (tiếng Trung) — không dùng; đề Việt vẫn đúng nên không sửa.",
        "Chỗ KHÔNG chắc tuyệt đối (không gắn Mức tin vì là từ nguyên phổ thông): уволить <- во́ля «thả về tự do» (Vasmer); горничная <- го́рница; верёвка <- вервь; ремонт <- Pháp remonte; аренда gốc Latin.",
        "заработать: khẳng định nghĩa «bắt đầu chạy» KHÔNG có ở зарабатывать (za- khởi phát thường chỉ có HT, như заплакать) — khá chắc, nhưng là khẳng định phủ định.",
        "нанять quá khứ: ghi на́нял/наняла́/на́няли; từ điển chuẩn còn chấp nhận наня́л — chọn dạng chính.",
        "холл cố ý không có Họ hàng (từ mượn tiếng Anh đứng một mình).",
    ],
}
