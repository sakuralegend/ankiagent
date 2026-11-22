# -*- coding: utf-8 -*-
"""k185 — actions: 10 cặp thể + сотру́дничать + про́пуск, trục là TIỀN TỐ + gốc đã học.

Chỗ cần nhất quán trong lô:
(1) -пуск-/-пуст- «THẢ, BUÔNG, CHO ĐI» (khớp пропуска́ть k175, вы́пуск k177): опускать/опустить,
    выпускать/выпустить, про́пуск. Thẻ HT nói ст → щ ở ngôi «tôi» (опущу́, вы́пущу).
(2) нес-/нос- «MANG» (нести́ k116, носи́ть k72): MỘT câu luật giống nhau ở внести/вносить/
    вынести/выносить — tiền tố + нести́ → HT, tiền tố + носи́ть → CHT (như принести́/приноси́ть).
(3) вы́- ở động từ HT luôn nhấn (вы́пустить, вы́нести); ở CHT mất nhấn (выпуска́ть, выноси́ть).
(4) -ступ- «BƯỚC» (выступа́ть, поступа́ть trong bộ sưu tập), -врат-/-вращ- «QUAY» (возвраща́ть,
    поворо́т k173), -дал- «XA» (далеко́), жм-/жим- «BÓP» (пожать/пожимать).
(5) Báo oan đã bỏ: пожать↔пожар/пожалуйста, вступить↔пить, превратить↔врать.
    опустить↔пусто́й/пусть KHÔNG phải báo oan — cùng gốc thật (k175 cũng ghép).
Họ hàng: không thẻ nào vắng.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "опускать": "hạ xuống, thả xuống, bỏ xuống, đặt xuống, bỏ vào",       # thiếu let down / drop in / put in
    "опустить": "hạ xuống, thả xuống, bỏ xuống, đặt xuống, bỏ vào",       # cùng bộ với cặp
    "выпускать": "thả ra, cho ra, phát hành, sản xuất, xuất bản",        # thiếu produce/manufacture, publish
    "выпустить": "thả ra, cho ra, phát hành, sản xuất, xuất bản",        # cùng bộ với cặp
    "лезть": "trèo, leo lên, chui vào, xen vào, quấy rầy",              # thiếu meddle/butt in, pester
    "внести": "mang vào, đem vào, ghi vào, đưa vào, nộp tiền, đóng góp", # thiếu pay in, contribute, introduce
    "вносить": "mang vào, đem vào, ghi vào, đưa vào, nộp tiền, đóng góp",# cùng bộ với внести
    "вынести": "mang ra, khiêng ra, đem ra ngoài, đưa ra, chịu đựng, chịu nổi",  # thiếu endure/bear/stand
    "выносить": "mang ra, khiêng ra, đem ra ngoài, chịu đựng, chịu nổi", # theo nghĩa đã chốt (id 3731)
    "удалить": "xoá, loại bỏ, gỡ bỏ, cắt bỏ, đuổi ra",                  # thiếu remove surgically, send off/expel
    "удалять": "xoá, loại bỏ, gỡ bỏ, cắt bỏ, đuổi ra",                  # cùng bộ với cặp
    "пропуск": "thẻ ra vào, giấy thông hành, chỗ bỏ sót, chỗ trống, sự vắng mặt",  # thiếu hẳn omission/gap/absence
}

# --------------------------------------------------------------------- опускать
S["опускать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không có nghĩa riêng tách ra được</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пуск-</span>'
    '<span class="hd-gloss">THẢ, BUÔNG — như <b>пропуска́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Buông cho tụt xuống ⇒ hạ xuống, thả vào: <b>опуска́ть письмо́ в я́щик</b> '
    'bỏ thư vào hòm. Chia đều: <b>опуска́ю</b>. Cặp HT: <b>опусти́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>опусти́ть</b> (HT) · <b>спуска́ться</b> đi xuống · '
    '<b>отпуска́ть</b> thả ra · <b>пропуска́ть</b> cho qua, bỏ lỡ</div>'
)

# --------------------------------------------------------------------- опустить
S["опустить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không có nghĩa riêng tách ra được</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пуст-и́ть</span>'
    '<span class="hd-gloss">THẢ, BUÔNG — như <b>отпусти́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hạ xuống một lần. Ngôi «tôi» <i>ст → щ</i> và nhấn đuôi: <b>опущу́</b>; '
    'các ngôi khác nhấn lùi vào thân: <b>опу́стишь, опу́стят</b> — y hệt <b>пропусти́ть</b>. '
    'Cặp CHT: <b>опуска́ть</b>.</div>'
    '<div class="hd-warn"><b>опусти́ть ру́ки</b> — nghĩa đen buông thõng tay, nghĩa bóng NẢN, bỏ cuộc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>опуска́ть</b> (CHT) · <b>спусти́ться</b> đi xuống · '
    '<b>отпусти́ть</b> thả ra · <b>пусть</b> cứ để</div>'
)

# --------------------------------------------------------------------- выпускать
S["выпускать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span>'
    '<span class="hd-gloss">RA NGOÀI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пуск-</span>'
    '<span class="hd-gloss">THẢ, CHO ĐI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cho đi RA ⇒ thả (chim, tù nhân), cho ra lò (sản xuất), phát hành, '
    'cho sinh viên ra trường. Ở thể CHT này <b>вы-</b> mất nhấn, nhấn nằm ở đuôi: '
    '<b>выпуска́ю</b>. Cặp HT: <b>вы́пустить</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вы́пустить</b> (HT) · <b>вы́пуск</b> số phát hành; khoá tốt nghiệp · '
    '<b>выпускни́к</b> người tốt nghiệp · <b>пропуска́ть</b> cho qua</div>'
)

# --------------------------------------------------------------------- выпустить
S["выпустить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы́-</span>'
    '<span class="hd-gloss">RA NGOÀI — ở động từ HT luôn mang trọng âm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пуст-ить</span>'
    '<span class="hd-gloss">THẢ, CHO ĐI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thả RA một lần: <b>вы́пустить пти́цу</b> thả chim, <b>вы́пустить альбо́м</b> '
    'ra mắt album. Ngôi «tôi» <i>ст → щ</i>: <b>вы́пущу</b>; nhấn đứng yên ở <b>вы́</b> khắp bảng. '
    'Cặp CHT: <b>выпуска́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>выпуска́ть</b> (CHT) · <b>вы́пуск</b> số phát hành · '
    '<b>выпускни́к</b> người tốt nghiệp · <b>отпусти́ть</b> thả ra</div>'
)

# --------------------------------------------------------------------- пожать
S["пожать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố thể, không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-жа-ть (жм-)</span>'
    '<span class="hd-gloss">BÓP, ÉP — chính là <b>жать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bóp nhẹ tay người kia một cái ⇒ bắt tay. Nguyên thể giấu mất <i>м</i>, '
    'thân tương lai mới lộ gốc thật <b>жм-</b>: <b>пожму́, пожмёшь</b>. Cặp CHT: <b>пожима́ть</b>.</div>'
    '<div class="hd-warn"><b>пожа́ть ру́ку</b> + cách 3 — bắt tay ai · <b>пожа́ть плеча́ми</b> '
    '(cách 5, không giới từ) — nhún vai.</div>'
    '<div class="hd-warn">Có một <b>пожа́ть</b> khác = GẶT, thân <b>жн-</b>: <i>что посе́ешь, '
    'то и пожнёшь</i> gieo gì gặt nấy. Thân <b>жм-</b> mới là bóp, bắt tay.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пожима́ть</b> (CHT) · <b>нажа́ть</b> ấn, bấm · '
    '<b>сжать</b> siết chặt</div>'
)

# --------------------------------------------------------------------- пожимать
S["пожимать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố, không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-жим-</span>'
    '<span class="hd-gloss">BÓP, ÉP — gốc <b>жм-</b> nở thêm <i>и</i> ở thể CHT</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thể CHT của <b>пожа́ть</b>, chia đều: <b>пожима́ю</b>. '
    '<i>жм- → жим-</i> lặp lại ở <b>нажа́ть → нажима́ть</b> (ấn, bấm).</div>'
    '<div class="hd-warn"><b>пожима́ть ру́ку</b> + cách 3 — bắt tay ai · <b>пожима́ть плеча́ми</b> '
    '— nhún vai (cách 5).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пожа́ть</b> (HT) · <b>нажима́ть</b> ấn, bấm · <b>жать</b> bóp, ép</div>'
)

# --------------------------------------------------------------------- вступать
S["вступать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO TRONG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ступ-</span>'
    '<span class="hd-gloss">BƯỚC — như <b>выступа́ть</b>, <b>поступа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bước VÀO ⇒ gia nhập một tổ chức, bước vào một việc: '
    '<b>вступа́ть в клуб</b> vào câu lạc bộ — thường <b>в</b> + cách 4. Chia đều: <b>вступа́ю</b>. '
    'Cặp HT: <b>вступи́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вступи́ть</b> (HT) · <b>выступа́ть</b> biểu diễn, phát biểu (bước ra) · '
    '<b>поступа́ть</b> hành động; nhập học · <b>ступе́нь</b> bậc</div>'
)

# --------------------------------------------------------------------- вступить
S["вступить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO TRONG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ступ-и́ть</span>'
    '<span class="hd-gloss">BƯỚC</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bước vào một lần ⇒ gia nhập, bắt đầu. Ngôi «tôi» chèn <i>л</i> (<i>п → пл</i>) '
    'và nhấn đuôi: <b>вступлю́</b>; các ngôi khác nhấn lùi vào thân: <b>всту́пишь, всту́пят</b>. '
    'Cặp CHT: <b>вступа́ть</b>.</div>'
    '<div class="hd-warn"><b>вступи́ть в си́лу</b> — có hiệu lực (luật, hợp đồng) · '
    '<b>вступи́ть в брак</b> — kết hôn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вступа́ть</b> (CHT) · <b>вы́ступить</b> biểu diễn, phát biểu · '
    '<b>поступи́ть</b> nhập học; hành động · <b>вступле́ние</b> lời mở đầu</div>'
)

# --------------------------------------------------------------------- прятать
S["прятать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: <b>пря́т-</b> là gốc trơn, <b>-ать</b> chỉ là đuôi động từ.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cả thì hiện tại <i>т → ч</i>, không ngôi nào giữ <i>т</i>: <b>пря́чу, пря́чешь, '
    'пря́чут</b>; mệnh lệnh <b>прячь!</b> Thêm <b>-ся</b> là tự giấu mình ⇒ trốn. '
    'Cặp HT: <b>спря́тать</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>спря́тать</b> (HT) · <b>пря́таться</b> trốn · '
    '<b>пря́тки</b> trò trốn tìm</div>'
)

# --------------------------------------------------------------------- спрятать
S["спрятать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">tiền tố thể, không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-прят-ать</span>'
    '<span class="hd-gloss">GIẤU — chính là <b>пря́тать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giấu XONG: <b>спря́тать ключи́</b> giấu chìa khoá đi. Chia y như '
    '<b>пря́тать</b>, <i>т → ч</i> khắp thì tương lai: <b>спря́чу, спря́чешь</b>. Cặp CHT: <b>пря́тать</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пря́тать</b> (CHT) · <b>спря́таться</b> trốn đi · '
    '<b>пря́тки</b> trò trốn tìm</div>'
)

# --------------------------------------------------------------------- сотрудничать
S["сотрудничать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">CÙNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-труд-</span>'
    '<span class="hd-gloss">LAO ĐỘNG — như <b>труд</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-нич-</span>'
    '<span class="hd-gloss">-ник «người», <b>к → ч</b> trước đuôi sau</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm như một <b>сотру́дник</b> — người cùng lao động ⇒ hợp tác. Khớp từng '
    'mảnh tiếng Anh <i>col-labor-ate</i>. Chỉ có thể CHT, không có cặp HT. Chia đều: '
    '<b>сотру́дничаю</b>.</div>'
    '<div class="hd-warn"><b>сотру́дничать с</b> + cách 5 — hợp tác với ai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сотру́дник</b> nhân viên · <b>сотру́дничество</b> sự hợp tác · '
    '<b>труд</b> lao động · <b>тру́дный</b> khó</div>'
)

# --------------------------------------------------------------------- превратить
S["превратить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пре-</span>'
    '<span class="hd-gloss">SANG, QUA — bản cổ của <b>пере-</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-врат-и́ть</span>'
    '<span class="hd-gloss">QUAY — bản cổ của <b>-ворот-</b> (<b>поворо́т</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Quay SANG hẳn một dạng khác ⇒ biến thành: <b>преврати́ть во́ду в лёд</b> — '
    'cái bị biến ở cách 4, <b>в</b> + cách 4 là kết quả. Ngôi «tôi» <i>т → щ</i>: <b>превращу́</b>; '
    'nhấn luôn ở đuôi. Cặp CHT: <b>превраща́ть</b>.</div>'
    '<div class="hd-warn">Tự nó biến thành thì thêm <b>-ся</b>: <i>Гу́сеница преврати́лась в ба́бочку</i> '
    '— con sâu hoá bướm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>превраща́ть</b> (CHT) · <b>превраще́ние</b> sự biến đổi · '
    '<b>возвраща́ть</b> trả lại · <b>поворо́т</b> chỗ rẽ</div>'
)

# --------------------------------------------------------------------- превращать
S["превращать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пре-</span>'
    '<span class="hd-gloss">SANG, QUA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вращ-</span>'
    '<span class="hd-gloss">QUAY — <b>-врат-</b> với <i>т → щ</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thể CHT, chia đều: <b>превраща́ю</b>. <i>щ</i> chạy suốt thể CHT của cả họ '
    'y như <b>возвраща́ть</b> — gốc vẫn là <b>-врат-</b> «quay». Cặp HT: <b>преврати́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>преврати́ть</b> (HT) · <b>превраще́ние</b> sự biến đổi · '
    '<b>возвраща́ться</b> quay về · <b>враща́ть</b> xoay</div>'
)

# --------------------------------------------------------------------- лезть
S["лезть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: <b>лез-</b> là gốc trơn.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Động từ chuyển động MỘT HƯỚNG: đang leo/chui vào một chỗ. Leo trèo nói chung, '
    'nhiều lượt là <b>ла́зить</b> (<i>е → а</i>). Thân giữ <i>з</i>: <b>ле́зу, ле́зешь</b>; quá khứ '
    'giống đực không có <i>-л</i>: <b>лез</b>, nhưng <b>ле́зла</b> — như <b>нёс</b>.</div>'
    '<div class="hd-warn">Nghĩa bóng hay gặp: <i>Не лезь не в своё де́ло!</i> — Đừng xía vào chuyện '
    'người khác!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ла́зить</b> leo trèo (nhiều chiều) · <b>поле́зть</b> bắt đầu leo (HT) · '
    '<b>вылеза́ть</b> chui ra · <b>ле́стница</b> cầu thang (họ xa, theo từ nguyên)</div>'
)

# --------------------------------------------------------------------- внести
S["внести"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO TRONG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-нес-ти́</span>'
    '<span class="hd-gloss">MANG — chính là <b>нести́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mang VÀO ⇒ khiêng đồ vào, ghi vào danh sách, nộp tiền vào, đưa sửa đổi vào: '
    '<b>внести́ измене́ния</b>. Cả họ: tiền tố + <b>нести́</b> → HT, tiền tố + <b>носи́ть</b> → CHT '
    '(như <b>принести́ / приноси́ть</b>). Chia như <b>нести́</b>: <b>внесу́</b>; quá khứ '
    '<b>внёс, внесла́</b>.</div>'
    '<div class="hd-warn"><b>внести́ вклад в</b> + cách 4 — đóng góp vào (một việc, một sự nghiệp).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вноси́ть</b> (CHT) · <b>взнос</b> khoản đóng góp · '
    '<b>принести́</b> mang đến · <b>вы́нести</b> mang ra</div>'
)

# --------------------------------------------------------------------- вносить
S["вносить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO TRONG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-нос-и́ть</span>'
    '<span class="hd-gloss">MANG — chính là <b>носи́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đang mang vào, hay nộp vào. Cả họ: tiền tố + <b>нести́</b> → HT, tiền tố + '
    '<b>носи́ть</b> → CHT (như <b>принести́ / приноси́ть</b>). Chia như <b>носи́ть</b>: ngôi «tôi» '
    '<i>с → ш</i>, trọng âm lùi: <b>вношу́, вно́сишь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>внести́</b> (HT) · <b>взнос</b> khoản đóng góp · '
    '<b>приноси́ть</b> mang đến · <b>выноси́ть</b> mang ra</div>'
)

# --------------------------------------------------------------------- вынести
S["вынести"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы́-</span>'
    '<span class="hd-gloss">RA NGOÀI — ở động từ HT luôn mang trọng âm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-нес-ти</span>'
    '<span class="hd-gloss">MANG — chính là <b>нести́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mang RA ⇒ khiêng ra; nghĩa bóng: gánh nổi tới cùng ⇒ chịu đựng: '
    '<i>Я э́того не вы́несу</i> tôi không chịu nổi chuyện này. Cả họ: tiền tố + <b>нести́</b> → HT, '
    'tiền tố + <b>носи́ть</b> → CHT. Nhấn đứng yên ở <b>вы́</b>: <b>вы́несу, вы́нес, вы́несла</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>выноси́ть</b> (CHT) · <b>на вы́нос</b> mang đi (đồ ăn) · '
    '<b>внести́</b> mang vào · <b>перенести́</b> dời lại</div>'
)

# --------------------------------------------------------------------- выносить
S["выносить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span>'
    '<span class="hd-gloss">RA NGOÀI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-нос-и́ть</span>'
    '<span class="hd-gloss">MANG — chính là <b>носи́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hai nghĩa: khiêng ra (<b>выноси́ть му́сор</b> đi đổ rác) và chịu đựng. '
    'Cả họ: tiền tố + <b>нести́</b> → HT, tiền tố + <b>носи́ть</b> → CHT. Ở thể CHT <b>вы-</b> mất nhấn; '
    'ngôi «tôi» <i>с → ш</i>: <b>выношу́, выно́сишь</b>.</div>'
    '<div class="hd-warn"><i>Я его́ не выношу́!</i> — Tôi không chịu nổi hắn! (+ cách 4, gần như '
    'luôn đi với <b>не</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вы́нести</b> (HT) · <b>выно́сливый</b> dẻo dai, chịu đựng giỏi · '
    '<b>вноси́ть</b> mang vào · <b>носи́ть</b> mang</div>'
)

# --------------------------------------------------------------------- удалить
S["удалить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">RỜI ĐI, ra xa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дал-</span>'
    '<span class="hd-gloss">XA — như <b>далеко́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm cho XA khỏi chỗ ⇒ loại bỏ: <b>удали́ть файл</b> xoá tệp, '
    '<b>удали́ть зуб</b> nhổ răng. Chia đều: <b>удалю́, удали́шь</b>. Cặp CHT: <b>удаля́ть</b>.</div>'
    '<div class="hd-warn">Tính từ cùng gốc giữ nghĩa «xa»: <b>удалённая рабо́та</b> — làm việc từ xa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>удаля́ть</b> (CHT) · <b>далеко́</b> xa · <b>далёкий</b> xa xôi · '
    '<b>удале́ние</b> sự xoá</div>'
)

# --------------------------------------------------------------------- удалять
S["удалять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">RỜI ĐI, ra xa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дал-</span>'
    '<span class="hd-gloss">XA — như <b>далеко́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đang xoá, hay xoá: <b>удаля́ть ли́шние фо́тки</b> xoá bớt ảnh thừa. '
    'Chia đều: <b>удаля́ю</b>. Cặp HT: <b>удали́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>удали́ть</b> (HT) · <b>далеко́</b> xa · <b>да́льний</b> xa, đường dài</div>'
)

# --------------------------------------------------------------------- пропуск
S["пропуск"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про́-</span>'
    '<span class="hd-gloss">QUA, xuyên qua</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пуск</span>'
    '<span class="hd-gloss">THẢ, CHO ĐI — danh từ không đuôi</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thứ CHO ĐI QUA ⇒ thẻ ra vào: <i>без про́пуска не пу́стят</i> không có thẻ thì '
    'không cho vào. Chỗ bị để trôi QUA ⇒ chỗ bỏ sót, buổi vắng mặt.</div>'
    '<div class="hd-warn">Số nhiều tách theo nghĩa: thẻ ra vào → <i>пропуска́</i> (nhấn đuôi); '
    'chỗ trống, buổi nghỉ → <i>про́пуски</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пропуска́ть</b> / <b>пропусти́ть</b> cho qua, bỏ lỡ · '
    '<b>о́тпуск</b> kỳ nghỉ phép · <b>вы́пуск</b> số phát hành</div>'
)

B = {
    "docbangmat": 101,
    "loitubat": 2,
    "nguonsai": 1,
    "baolen": [
        "Lỗi tự bắt (loitubat=2): (1) пря́тать/спря́тать viết «cả bảng т → ч» — sai vì quá khứ giữ т (пря́тал) → sửa «cả thì hiện tại/tương lai»; (2) вступа́ть viết «luôn в + cách 4» — quá rộng (вступи́ть на престо́л, на путь dùng на) → «thường».",
        "Nguồn sai (nguonsai=1): bảng chia про́пуск in số nhiều пропуски́/пропуско́в (nhấn и — không có dạng này). Không chép; thẻ ghi theo chuẩn: thẻ ra vào → пропуска́, chỗ bỏ sót/buổi nghỉ → про́пуски (viết <i>, không <b>, vì пропуска trùng mặt chữ với cách 2 số ít про́пуска nên bộ soát sẽ so nhầm). Luồng chính cân nhắc sửa bảng chia trên thẻ.",
        "Đồng tự: пожа́ть soạn theo nghĩa «bắt tay» (thân жм-); thêm MỘT ô đỏ chỉ ra пожа́ть «gặt» (thân жн-, пожнёшь) để user khỏi lẫn khi gặp câu tục ngữ. выноси́ть soạn theo nghĩa «mang ra; chịu đựng» (id 3731), không nhắc вы́носить «mang thai đủ tháng».",
        "Không chắc / đã nói mềm: о- trong опусти́ть/опуска́ть ghi «không có nghĩa riêng tách ra được» (không bịa «xuống»); ле́стница trong Họ hàng của лезть ghi «họ xa, theo từ nguyên» — khớp ô Mức tin trên thẻ ле́стница (k102); пре- = «bản cổ của пере-», -врат- = «bản cổ của -ворот-» là quan hệ chuẩn (неполногласие), không ghi Mức tin.",
        "V cần duyệt (12 thẻ): опуска́ть/опусти́ть (+thả xuống, bỏ vào — let down/drop in); выпуска́ть/вы́пустить (+sản xuất, xuất bản — produce/publish); лезть (+xen vào, quấy rầy — meddle/pester); внести́/вноси́ть (cùng bộ: +đưa vào, nộp tiền, đóng góp); вы́нести (+khiêng ra, chịu đựng, chịu nổi — endure/stand); выноси́ть (+khiêng ra, chịu nổi theo nghĩa đã chốt); удали́ть/удаля́ть (+cắt bỏ, đuổi ra — remove surgically/send off); про́пуск (THIẾU hẳn omission/gap/absence → +chỗ bỏ sót, chỗ trống, sự vắng mặt; «thẻ vào cửa» → «thẻ ra vào» cho khớp k175). Không viết V cho пожа́ть, пожима́ть, вступа́ть, вступи́ть, пря́тать, спря́тать, сотру́дничать, преврати́ть, превраща́ть (đề cũ đã đúng).",
        "Báo oan đã bỏ: пожа́ть↔пожа́р/пожа́луйста/госпожа́, пожима́ть↔мать, вступи́ть↔пить, преврати́ть↔врать. опусти́ть↔пусто́й/пусть: KHÔNG phải báo oan (пусти́ть ← пусто́й, пусть là mệnh lệnh cũ của пусти́ть) — đưa пусть vào Họ hàng опусти́ть như k175 đã làm.",
    ],
}
