# -*- coding: utf-8 -*-
"""k189 — qualities (lô trộn): 6 cặp/lẻ động từ có tiền tố + danh từ/tính từ trừu tượng.

Chỗ cần nhất quán trong lô:
(1) вин- «LỖI, TỘI»: обвинить/обвинять — об- «nhắm vào ai đó» đúng như обвине́ние (k151).
(2) -ста- «ĐỨNG» + рас- TÁCH RA: расставаться/расстаться — chia y như встава́ть/встать
    (встаю́ / вста́ну), MỘT câu dẫn chiếu giống nhau ở cả hai thẻ.
(3) меш- «KHUẤY, TRỘN» (như меша́ть k96): вмешаться/вмешиваться.
(4) сущ-еств- «CÓ THẬT» (như осуществи́ть k184): осуществиться/осуществляться.
(5) стиг-/стич- (như дости́гнуть k131): достичь — dạng song song, V khớp достигнуть.
(6) гото́в- (như пригото́вить k60, подгото́виться k133): приготовиться.
Họ hàng cố ý vắng: тщательный (тща́ние cổ, chỉ còn trạng từ -о), тенденция (từ mượn đứng một mình).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "достичь": "đạt được, tới được",                          # khớp дости́гнуть/достига́ть (dạng song song, cùng nghĩa)
    "блестящий": "sáng bóng, lấp lánh, xuất sắc, rực rỡ",      # thiếu brilliant/splendid/outstanding; bỏ «lóng lánh» trùng «lấp lánh»
    "характерный": "đặc trưng, tiêu biểu, điển hình",          # nghĩa đã chốt (id 58590); typical/characteristic
}

# --------------------------------------------------------------------- обвинить
S["обвинить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">nhắm vào ai đó</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вин-</span>'
    '<span class="hd-gloss">LỖI, TỘI — như <b>вина́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2: <b>обвиню́, обвини́шь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gán LỖI vào một người ⇒ buộc tội. Cặp CHT: <b>обвиня́ть</b>.</div>'
    '<div class="hd-warn">Buộc tội AI (cách 4) VỀ việc gì (<b>в</b> + cách 6): '
    '<b>обвини́ть его́ в обма́не</b> buộc tội anh ta lừa dối.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обвине́ние</b> lời buộc tội · <b>вина́</b> lỗi · '
    '<b>винова́тый</b> có lỗi · <b>извини́ть</b> tha lỗi</div>'
)

# --------------------------------------------------------------------- обвинять
S["обвинять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">nhắm vào ai đó</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вин-</span>'
    '<span class="hd-gloss">LỖI, TỘI — như <b>вина́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành, chia đều: <b>обвиня́ю, обвиня́ешь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đang buộc tội, hay đổ lỗi: <i>Не обвиня́й себя́</i> — đừng tự trách mình. '
    'Vẫn đòi AI (cách 4) + <b>в</b> + cách 6. Cặp HT: <b>обвини́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обвиня́емый</b> bị cáo («người đang bị buộc tội») · '
    '<b>обвине́ние</b> lời buộc tội · <b>вина́</b> lỗi</div>'
)

# --------------------------------------------------------------------- достичь
S["достичь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-</span>'
    '<span class="hd-gloss">TỚI TẬN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сти-чь (стиг-)</span>'
    '<span class="hd-gloss">ĐUỔI KỊP, chạm tới — như <b>достига́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc tận cùng <i>г</i> thì nguyên thể ra <i>-чь</i>, như <b>мочь</b> (<b>могу́</b>). '
    'Nên chia vẫn hiện <i>г</i>: <b>дости́гну, дости́гнешь</b>; quá khứ <b>дости́г, дости́гла</b>.</div>'
    '<div class="hd-warn">Đòi cách 2: <b>дости́чь це́ли</b> đạt mục tiêu. Có dạng song song '
    '<b>дости́гнуть</b> — cùng nghĩa, cùng cách chia.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>достига́ть</b> đạt tới (CHT) · <b>достиже́ние</b> thành tựu</div>'
)

# --------------------------------------------------------------------- расставаться
S["расставаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рас-</span>'
    '<span class="hd-gloss">TÁCH RA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ста-ва́-ться</span>'
    '<span class="hd-gloss">ĐỨNG — như <b>встава́ть</b>, đuôi CHT <i>-ва-</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đứng tách ra mỗi người một nơi ⇒ chia tay. Hiện tại rơi <i>-ва-</i>, '
    'y như <b>встава́ть → встаю́</b>: <b>расстаю́сь, расстаёшься</b>. Cặp HT: <b>расста́ться</b>.</div>'
    '<div class="hd-warn">Chia tay VỚI ai: <b>с</b> + cách 5 — <b>расстава́ться с дру́гом</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>расста́ться</b> chia tay (HT) · <b>расстава́ние</b> sự chia ly · '
    '<b>встава́ть</b> đứng dậy · <b>остава́ться</b> ở lại</div>'
)

# --------------------------------------------------------------------- расстаться
S["расстаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рас-</span>'
    '<span class="hd-gloss">TÁCH RA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ста́-ть-ся</span>'
    '<span class="hd-gloss">ĐỨNG — như <b>встать</b>, <b>стать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đứng tách ra ⇒ chia tay (xong hẳn). Tương lai mọc <i>н</i>, y như '
    '<b>встать → вста́ну</b>: <b>расста́нусь, расста́нешься</b>. Cặp CHT: <b>расстава́ться</b>.</div>'
    '<div class="hd-warn"><b>с</b> + cách 5: <b>Они́ расста́лись с ним</b> — họ đã chia tay anh ấy.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>расстава́ться</b> (CHT) · <b>встать</b> đứng dậy · '
    '<b>оста́ться</b> ở lại · <b>стать</b> trở thành</div>'
)

# --------------------------------------------------------------------- вмешаться
S["вмешаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO TRONG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-меш-</span>'
    '<span class="hd-gloss">KHUẤY, TRỘN — như <b>меша́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть-ся</span>'
    '<span class="hd-gloss">chia đều: <b>вмеша́юсь, вмеша́ешься</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tự trộn mình VÀO chuyện người khác ⇒ xen vào, can thiệp. Cặp CHT: '
    '<b>вме́шиваться</b>.</div>'
    '<div class="hd-warn">Xen VÀO cái gì: <b>в</b> + cách 4 — <b>вмеша́ться в разгово́р</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>меша́ть</b> làm phiền, khuấy · <b>помеша́ть</b> cản trở · '
    '<b>вмеша́тельство</b> sự can thiệp</div>'
)

# --------------------------------------------------------------------- вмешиваться
S["вмешиваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO TRONG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ме́ш-</span>'
    '<span class="hd-gloss">KHUẤY, TRỘN — như <b>меша́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ть-ся</span>'
    '<span class="hd-gloss">đuôi CHT <i>-ива-</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hay xen vào, đang can thiệp. Thêm <i>-ива-</i> thì trọng âm lùi về gốc: '
    '<b>вме́шиваюсь, вме́шиваешься</b>. Vẫn <b>в</b> + cách 4. Cặp HT: <b>вмеша́ться</b>.</div>'
    '<div class="hd-warn"><b>Не вме́шивайся!</b> = Đừng xen vào!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>меша́ть</b> làm phiền, khuấy · <b>вмеша́тельство</b> sự can thiệp</div>'
)

# --------------------------------------------------------------------- приготовиться
S["приготовиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">TỚI NƠI, xong hẳn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-гото́в-ить-ся</span>'
    '<span class="hd-gloss">làm mình SẴN SÀNG — như <b>гото́вый</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm mình sẵn sàng cho việc sắp tới, thường là ngay trước mắt: '
    '<b>Пригото́вьтесь!</b> Chuẩn bị! Ngôi «tôi» <i>в → вл</i>: <b>пригото́влюсь, пригото́вишься</b>; '
    'đòi <b>к</b> + cách 3. Cặp CHT: <b>гото́виться</b>.</div>'
    '<div class="hd-warn">Bỏ <i>-ся</i> là <b>пригото́вить</b> = nấu, chuẩn bị CÁI GÌ. '
    '<b>подгото́виться</b> nghiêng về chuẩn bị kỹ bằng ôn luyện (thi, phỏng vấn).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гото́вый</b> sẵn sàng · <b>пригото́вить</b> nấu · '
    '<b>подгото́вка</b> sự chuẩn bị</div>'
)

# --------------------------------------------------------------------- осуществиться
S["осуществиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">LÀM CHO THÀNH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сущ-еств-</span>'
    '<span class="hd-gloss">CÓ THẬT — như <b>существова́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть-ся</span>'
    '<span class="hd-gloss">lớp 2 + <i>-ся</i>: tự nó thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính <b>осуществи́ть</b> (thực hiện) thêm <i>-ся</i>: điều mong ước tự trở '
    'thành CÓ THẬT — <b>Мечта́ осуществи́лась</b> ước mơ đã thành hiện thực. Ngôi «tôi» '
    '<i>в → вл</i>: <b>осуществлю́сь</b>. Cặp CHT: <b>осуществля́ться</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>осуществи́ть</b> thực hiện · <b>осуществле́ние</b> sự thực hiện · '
    '<b>существова́ть</b> tồn tại</div>'
)

# --------------------------------------------------------------------- осуществляться
S["осуществляться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">LÀM CHO THÀNH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сущ-еств-</span>'
    '<span class="hd-gloss">CÓ THẬT — như <b>существова́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-л-я́ть-ся</span>'
    '<span class="hd-gloss"><i>в</i> thêm <i>л</i> + đuôi CHT + <i>-ся</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><i>-ся</i> ở đây là «được»: <b>Прое́кт осуществля́ется</b> — dự án đang được '
    'thực hiện. Giọng sách báo. Chia đều: <b>осуществля́ется, осуществля́ются</b>. Cặp HT: '
    '<b>осуществи́ться</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>осуществля́ть</b> thực hiện (CHT) · <b>осуществле́ние</b> sự thực hiện · '
    '<b>существова́ть</b> tồn tại</div>'
)

# --------------------------------------------------------------------- препятствие
S["препятствие"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">препя́т-</span>'
    '<span class="hd-gloss">gốc CẢN — cổ, không nối được sang từ quen</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ствие</span>'
    '<span class="hd-gloss">→ danh từ giống trung, như <b>путеше́ствие</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhớ cả khối <b>препя́тств-</b> qua động từ <b>препя́тствовать</b> cản trở '
    '(+ cách 3). Trọng âm đứng yên ở <b>-пя́-</b>.</div>'
    '<div class="hd-warn"><b>без препя́тствий</b> = không gặp trở ngại, suôn sẻ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>препя́тствовать</b> cản trở · <b>беспрепя́тственно</b> không trở ngại</div>'
)

# --------------------------------------------------------------------- ограничение
S["ограничение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">BAO QUANH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-гранич-</span>'
    '<span class="hd-gloss">BIÊN, MÉP — <b>грани́ца</b>, <i>ц → ч</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vạch biên giới bao quanh một thứ ⇒ giới hạn, hạn chế: '
    '<b>ограниче́ние ско́рости</b> giới hạn tốc độ. Danh từ của <b>ограни́чить</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>грани́ца</b> biên giới · <b>ограни́чить</b> hạn chế (HT) · '
    '<b>ограни́ченный</b> hạn hẹp</div>'
)

# --------------------------------------------------------------------- резкий
S["резкий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ре́з-</span>'
    '<span class="hd-gloss">CẮT — như <b>ре́зать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-ий</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Như lưỡi dao cắt ngang ⇒ đột ngột, gắt, chói: <b>ре́зкий звук</b> tiếng '
    'chói tai. Trạng từ hay gặp hơn: <b>ре́зко</b> — <i>Це́ны ре́зко вы́росли</i> giá tăng vọt.</div>'
    '<div class="hd-warn">Dạng ngắn chen <i>о</i>: <b>ре́зок</b>, và riêng giống cái nhảy trọng âm '
    'ra đuôi. So sánh hơn <i>зк → зч</i>: <b>ре́зче</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ре́зать</b> cắt · <b>поре́зать</b> cắt (HT) · <b>отре́зать</b> cắt rời</div>'
)

# --------------------------------------------------------------------- блестящий
S["блестящий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">блест-</span>'
    '<span class="hd-gloss">LẤP LÁNH — như <b>блеск</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́щ-ий</span>'
    '<span class="hd-gloss">«đang …» — đuôi phân từ, như <b>настоя́щий</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng nghĩa đen là «đang lấp lánh» (<b>блесте́ть</b>) ⇒ sáng bóng; nghĩa bóng '
    'là xuất sắc, như <i>brilliant</i>: <b>блестя́щая иде́я</b> ý tưởng tuyệt vời.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>блесте́ть</b> lấp lánh · <b>блеск</b> ánh lấp lánh · '
    '<b>блестя́ще</b> xuất sắc</div>'
)

# --------------------------------------------------------------------- характерный
S["характерный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">характе́р-</span>'
    '<span class="hd-gloss">TÍNH CÁCH, bản chất — <b>хара́ктер</b> (từ mượn)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mang đúng bản chất của thứ đó ⇒ đặc trưng, như <i>characteristic</i>. '
    'Trọng âm DỊCH: <b>хара́ктер</b> nhưng <b>характе́рный</b>, và giữ ở <b>-те́-</b> cả trạng từ '
    '<b>характе́рно</b>.</div>'
    '<div class="hd-warn">Đặc trưng CỦA ai: <b>для</b> + cách 2 — <b>характе́рно для него́</b> '
    'đúng kiểu anh ta.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>хара́ктер</b> tính cách · <b>характери́стика</b> đặc điểm, bản nhận xét</div>'
)

# --------------------------------------------------------------------- секретный
S["секретный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">секре́т-</span>'
    '<span class="hd-gloss">BÍ MẬT — <b>секре́т</b> (từ mượn, như <i>secret</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thuộc loại bí mật, giữ kín theo quy định: <b>секре́тные докуме́нты</b> '
    'tài liệu mật, <b>секре́тный аге́нт</b> mật vụ. Trọng âm đứng yên ở <b>-ре́-</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>секре́т</b> bí mật · <b>секрета́рь</b> thư ký · '
    '<b>засекре́тить</b> xếp vào loại mật</div>'
)

# --------------------------------------------------------------------- привычный
S["привычный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">TỚI, gắn vào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-выч-</span>'
    '<span class="hd-gloss">QUEN — chính <b>-вык-</b> của <b>привыка́ть</b>, <i>к → ч</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thứ mình đã quen tới ⇒ quen thuộc, thường lệ: <b>привы́чная жизнь</b> nếp '
    'sống quen. Trạng từ <b>привы́чно</b>: <i>Мне привы́чно</i> — tôi quen rồi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>привы́чка</b> thói quen · <b>привыка́ть</b> quen với · '
    '<b>обы́чный</b> thường lệ</div>'
)

# --------------------------------------------------------------------- индивидуальный
S["индивидуальный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">индивиду-</span>'
    '<span class="hd-gloss">CÁ THỂ — từ mượn, chính là <i>individual</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́льн-ый</span>'
    '<span class="hd-gloss">đuôi tính từ mượn, như <b>норма́льный</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dành riêng cho một người: <b>индивидуа́льный подхо́д</b> cách tiếp cận '
    'riêng cho từng người. Trọng âm ở <b>-а́-</b> của đuôi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>индивидуа́льность</b> cá tính, nét riêng · <b>индиви́д</b> cá thể</div>'
)

# --------------------------------------------------------------------- тщательный
S["тщательный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">тщ-а-</span>'
    '<span class="hd-gloss">CỐ CÔNG — gốc cổ, không còn từ quen nào mang nó</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тельн-ый</span>'
    '<span class="hd-gloss">đuôi tính từ, như <b>внима́тельный</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mở đầu bằng cụm hiếm <b>тщ</b> — gõ đủ hai chữ. Hay dùng nhất là trạng từ: '
    '<b>тща́тельно прове́рить</b> kiểm tra kỹ lưỡng.</div>'
    '<div class="hd-warn">⚠️ Mức tin: gốc «cố công» là từ nguyên (từ cổ <i>тща́ние</i>), '
    'không phải luật suy ra được.</div>'
)

# --------------------------------------------------------------------- тенденция
S["тенденция"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn (Latin), không chẻ theo tiếng Nga — chính là <i>tendency</i>; '
    'đuôi <b>-ция</b> = <i>-tion</i>, luôn giống cái.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Xu hướng HƯỚNG TỚI cái gì: <b>к</b> + cách 3 — <b>тенде́нция к ро́сту</b> '
    'xu hướng tăng. Trọng âm ở <b>-де́-</b>.</div>'
)

B = {
    "docbangmat": 91,
    "loitubat": 1,
    "nguonsai": 1,
    "baolen": [
        "VA CHẠM KHÔNG GỠ ĐƯỢC từ phía lô này: подгото́виться[k133 đã nạp] = «chuẩn bị» nằm gọn trong пригото́виться = «chuẩn bị, sẵn sàng» (cùng v PERF REF). Bên bị NẰM GỌN là подгото́виться, nên đổi V của пригото́виться không gỡ được trừ khi cắt «chuẩn bị» — nghĩa chính, cấm cắt. Không viết V cho пригото́виться. Hướng gỡ (user quyết, thẻ mồ côi): thêm nghĩa thật cho подгото́виться, vd «chuẩn bị, ôn luyện» (gloss to prepare oneself / get ready; ý chuẩn bị bằng học, tập).",
        "VA CHẠM MỚI DO V, CỐ Ý theo chỉ thị luồng chính: V дости́чь = «đạt được, tới được» khớp hẳn дости́гнуть[k131] (cùng v PERF, không badge nào tách). Hai dạng song song đồng nghĩa tuyệt đối — đề bài nào cũng có 2 đáp án đúng. Đề cũ «đạt tới, đến được, đạt được» chỉ khác bằng chữ đồng nghĩa «đến/tới», tách giả. Cần user chọn: nhận cả hai đáp án, hoặc tự thêm ngoặc trên một thẻ.",
        "Nguồn sai (đã bác): BAT THUONG của характе́рный in dạng ngắn хара́ктерен · хара́ктерна… — đó là dạng ngắn của từ ĐỒNG TỰ хара́ктерный (vai tính cách, người cứng cỏi). Nghĩa đã chốt «đặc trưng» có dạng ngắn характе́рен, характе́рна, характе́рно. Thẻ không in dạng ngắn, chỉ nói trọng âm giữ ở -те́- (характе́рно).",
        "Cửa TRONG AM LECH báo резка́ (dạng ngắn giống cái của ре́зкий) ↔ danh từ ре́зка «sự cắt» trong nouns.csv — đồng tự thật, KHÔNG nới MIEN_TRU; đã viết vòng: in đậm ре́зок, giống cái chỉ nói bằng lời «nhảy trọng âm ra đuôi».",
        "Tự sửa 1 lỗi: ví dụ ở ре́зкий viết «Цены́» — cách 1 số nhiều của цена́ là це́ны; đã sửa.",
        "V cần duyệt: блестя́щий thêm «xuất sắc, rực rỡ» (gloss brilliant/splendid/outstanding — nghĩa rất thông dụng mà đề cũ thiếu), bỏ «lóng lánh» (trùng «lấp lánh»); характе́рный đổi «đặc thù» → «điển hình» theo nghĩa đã chốt id 58590. Các từ khác giữ nguyên đề cũ.",
        "Không chắc: (1) gloss пригото́виться «to be ahead / to be about to take place / to be imminent» — không đưa vào V vì nghĩa này hiếm ở dạng HT (thường là гото́виться «đang được chuẩn bị»); (2) пригото́виться ô đỏ nói подгото́виться «nghiêng về chuẩn bị kỹ bằng ôn luyện» — sắc thái, nói mềm; (3) тща́тельный ← тща́ние «cố công» có ô ⚠️ Mức tin; (4) препя́тствие: gốc -пят- để là «cổ, không nối được», không nhận chẻ пре- vì từ nguyên không chắc.",
        "Họ hàng cố ý vắng: тща́тельный (gốc cổ, chỉ còn trạng từ тща́тельно — đã đưa vào Cách nhớ), тенде́нция (từ mượn đứng một mình; тенденцио́зный hiếm, không đưa). Báo oan máy đã bỏ qua theo chỉ thị: блестя́щий↔ле́стница, индивидуа́льный↔И́ндия, дости́чь↔мо́лодость/досто́йный, расста́ться↔расстоя́ние/статья́.",
    ],
}
