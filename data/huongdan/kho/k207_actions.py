# -*- coding: utf-8 -*-
"""k207 — actions: 4 cặp thể + họ từ của các thẻ đã có (беседа, точный, развитие, образование…).

Chỗ cần nhất quán trong lô:
(1) уточни́ть/уточня́ть: -точн- CHÍNH XÁC, gốc точ- CHẤM (khuôn k57 то́чка, k108 то́чный);
    у- LÀM CHO TRỞ NÊN (khuôn улу́чшить).
(2) разви́ть/развива́ть: раз- TÁCH RA, MỞ BUNG + -ви- CUỘN, XOẮN (khuôn k113, k138).
(3) образова́ть/образо́вывать: образ- HÌNH ẢNH, HÌNH DẠNG + -ова- LÀM CHO thành (khuôn k09).
(4) соотноше́ние: со- CÙNG + отноше́ние (khuôn k114). пя́теро: khuôn k126 че́тверо.
Họ hàng vắng: không thẻ nào.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "пятеро": "năm người",                                        # khuôn трое «ba người», четверо «bốn người»
    "разойтись": "giải tán, tan ra, chia tay nhau, ly hôn, khác nhau",  # thiếu get divorced / differ
    "ухаживать": "chăm sóc, trông nom, săn sóc, tán tỉnh",        # thiếu court / woo
    "образовать": "tạo thành, hình thành, cấu thành, lập nên",    # thiếu make up / constitute
    "образовывать": "tạo thành, hình thành, cấu thành, lập nên",  # thiếu found / establish / set up
}

# -------------------------------------------------------------------- собеседник
S["собеседник"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">CÙNG nhau</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бесед-</span>'
    '<span class="hd-gloss">cuộc trò chuyện — <b>бесе́да</b> (trong đó <i>-сед-</i> là NGỒI)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ник</span>'
    '<span class="hd-gloss">đuôi chỉ NGƯỜI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Người cùng trò chuyện» ⇒ người đối thoại, bất cứ ai đang nói chuyện với mình — cả qua điện thoại. Nghe hợp chuyện thì khen: <b>интере́сный собесе́дник</b>. Nữ: <b>собесе́дница</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бесе́да</b> cuộc trò chuyện · <b>бесе́довать</b> trò chuyện · <b>собесе́дование</b> buổi phỏng vấn xin việc</div>'
)

# -------------------------------------------------------------------- автоответчик
S["автоответчик"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">авто-</span>'
    '<span class="hd-gloss">TỰ, tự động (Hy Lạp, như <i>auto-</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ответ-</span>'
    '<span class="hd-gloss">TRẢ LỜI — <b>отве́т</b>, gốc <i>-вет-</i> LỜI NÓI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-чик</span>'
    '<span class="hd-gloss">đuôi chỉ người làm việc — ở đây là CÁI MÁY làm việc đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Kẻ tự trả lời» ⇒ máy trả lời tự động, hộp thư thoại. Đuôi <i>-чик</i> gắn cho cả người (<b>лётчик</b> phi công) lẫn máy móc.</div>'
    '<div class="hd-warn">Để lại lời nhắn TRÊN máy: <b>на</b> + cách 6 — <b>оста́вить сообще́ние на автоотве́тчике</b>.</div>'
    '<div class="hd-warn">Bỏ <i>авто-</i> đi là sang nghĩa khác hẳn: <b>отве́тчик</b> = BỊ ĐƠN trước toà.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отве́т</b> câu trả lời · <b>отвеча́ть</b> trả lời · <b>автома́т</b> máy tự động · <b>перево́дчик</b> người dịch (cùng đuôi)</div>'
)

# -------------------------------------------------------------------- умолять
S["умолять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng rõ rệt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мол-</span>'
    '<span class="hd-gloss">KHẨN CẦU — như <b>моли́ться</b> cầu nguyện</span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́-ть</span>'
    '<span class="hd-gloss">đuôi động từ, chia đều</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Xin mà tha thiết như cầu nguyện ⇒ van nài — mạnh hơn <b>проси́ть</b> nhiều. Chia đều, trọng âm đứng yên: <b>умоля́ю, умоля́ешь</b>. Van AI làm gì: người ở cách 4 + nguyên thể — <b>Он умоля́л её оста́ться.</b></div>'
    '<div class="hd-warn">Một mình <b>Умоля́ю!</b> chen giữa câu = «tôi van đấy!»: <b>Умоля́ю тебя́, не уходи́!</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>моли́ться</b> cầu nguyện · <b>моли́тва</b> lời cầu nguyện · <b>мольба́</b> lời khẩn cầu</div>'
)

# -------------------------------------------------------------------- уточнить
S["уточнить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">làm cho TRỞ NÊN… — như <b>улу́чшить</b> làm cho tốt hơn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-точн-</span>'
    '<span class="hd-gloss">CHÍNH XÁC — <b>то́чный</b>, gốc <i>точ-</i> CHẤM, ĐIỂM</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Làm cho chính xác hơn» ⇒ hỏi lại cho rõ, làm rõ chi tiết. Trọng âm ở đuôi suốt: <b>уточню́, уточни́шь</b>. Cặp CHT: <b>уточня́ть</b>.</div>'
    '<div class="hd-warn">Khác <b>вы́яснить</b>: <b>вы́яснить</b> là chưa biết mà tìm ra; <b>уточни́ть</b> là biết đại khái rồi, hỏi lại cho khỏi sai: <b>Я хочу́ уточни́ть вре́мя.</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>то́чный</b> chính xác · <b>то́чка</b> dấu chấm · <b>уточне́ние</b> sự làm rõ</div>'
)

# -------------------------------------------------------------------- уточнять
S["уточнять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">làm cho TRỞ NÊN… — như <b>улучша́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-точн-</span>'
    '<span class="hd-gloss">CHÍNH XÁC — <b>то́чный</b>, gốc <i>точ-</i> CHẤM, ĐIỂM</span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́-ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thể CHT của <b>уточни́ть</b>: đang hỏi lại, hay hỏi lại cho chính xác. <i>-ить</i> đổi thành <i>-ять</i>, y như <b>объясни́ть → объясня́ть</b>. Chia đều: <b>уточня́ю, уточня́ешь</b>.</div>'
    '<div class="hd-warn">Cái cần làm rõ ở cách 4, hỏi AI thì <b>у</b> + cách 2: <b>уточня́ть а́дрес у клие́нта</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уточни́ть</b> (HT) · <b>то́чный</b> chính xác · <b>то́чность</b> độ chính xác · <b>уточне́ние</b> sự làm rõ</div>'
)

# -------------------------------------------------------------------- регулярный
S["регулярный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">регуляр-</span>'
    '<span class="hd-gloss">= Anh <i>regular</i> (Latin <i>regula</i> cây thước, quy tắc)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đúng theo thước» ⇒ đều đặn, đúng nhịp, đúng lịch. Trạng từ: <b>регуля́рно</b>. Dạng ngắn giống đực chèn <i>е</i>: <b>регуля́рен</b>, nhưng <b>регуля́рна</b>; trọng âm đứng yên.</div>'
    '<div class="hd-warn"><b>регуля́рная а́рмия</b> = quân đội CHÍNH QUY (có tổ chức thường trực).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>регуля́рно</b> một cách đều đặn · <b>нерегуля́рный</b> thất thường · <b>регули́ровать</b> điều chỉnh</div>'
)

# -------------------------------------------------------------------- ночевать
S["ночевать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ноч-</span>'
    '<span class="hd-gloss">ĐÊM — <b>ночь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ева́-ть</span>'
    '<span class="hd-gloss">đuôi động từ (chính là <i>-ова-</i>, viết <i>е</i> sau <i>ч</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Biến «đêm» thành động từ ⇒ ngủ lại qua đêm ở đâu. Khi chia <i>-ева-</i> thành <i>-у-</i>: <b>ночу́ю, ночу́ешь, ночу́ют</b>. Cặp HT: <b>переночева́ть</b> (qua hết một đêm).</div>'
    '<div class="hd-warn">Ngủ lại nhà AI → <b>у</b> + cách 2: <b>ночева́ть у друзе́й</b>. Từ này nói về NƠI qua đêm; hành động ngủ là <b>спать</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ночь</b> đêm · <b>ночно́й</b> thuộc về đêm · <b>ночле́г</b> chỗ ngủ qua đêm · <b>переночева́ть</b> ngủ lại một đêm (HT)</div>'
)

# -------------------------------------------------------------------- соотношение
S["соотношение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">CÙNG, đặt cạnh nhau</span></div>'
    '<div class="hd-row"><span class="hd-piece">-от-нош-</span>'
    '<span class="hd-gloss">đưa sang phía kia + MANG — như <b>отноше́ние</b> quan hệ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Quan hệ CÙNG nhau» giữa hai đại lượng ⇒ tỉ lệ, tương quan. Anh cũng dựng y vậy: <i>cor-relation</i> (<i>cor-</i> cùng + <i>relation</i>).</div>'
    '<div class="hd-warn">Hai cụm hay gặp: <b>соотноше́ние сил</b> tương quan lực lượng · <b>соотноше́ние цены́ и ка́чества</b> giá so với chất lượng.</div>'
    '<div class="hd-warn">Con người quan hệ với nhau thì dùng <b>отноше́ния</b>; <b>соотноше́ние</b> là giữa các CON SỐ, các mặt.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отноше́ние</b> quan hệ, thái độ · <b>соотноси́ть</b> đối chiếu hai thứ · <b>носи́ть</b> mang</div>'
)

# -------------------------------------------------------------------- пятеро
S["пятеро"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пят-</span>'
    '<span class="hd-gloss">NĂM — như <b>пять</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-еро</span>'
    '<span class="hd-gloss">đuôi số TẬP HỢP từ 4 trở lên, như <b>че́тверо</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gọi cả NHÓM NĂM, luật y như <b>че́тверо</b>: kéo cách 2 số nhiều — <b>пя́теро дете́й</b> năm đứa trẻ, <b>нас бы́ло пя́теро</b> chúng tôi có năm người. Các cách khác đổi thân, trọng âm ra đuôi: <b>пятеры́х</b>, <b>пятеры́м</b>.</div>'
    '<div class="hd-warn">Dùng cho nam, trẻ con và danh từ chỉ có số nhiều (<b>пя́теро су́ток</b>). Nhóm toàn nữ thì dùng <b>пять</b>: <b>пять подру́г</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пять</b> năm · <b>впятеро́м</b> năm người cùng nhau · <b>пятёрка</b> điểm 5 · <b>че́тверо</b> bốn người</div>'
)

# -------------------------------------------------------------------- литр
S["литр"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn (Pháp <i>litre</i>) — không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giống đực, trọng âm nằm yên ở <i>ли</i> mọi dạng. Đếm: <b>два ли́тра</b> (2–4 → cách 2 số ít), <b>пять ли́тров</b> (5+ → cách 2 số nhiều). Chất lỏng đi sau ở cách 2: <b>литр молока́</b>.</div>'
    '<div class="hd-warn">Nửa lít: <b>пол-ли́тра</b> — có gạch nối vì <i>пол-</i> đứng trước chữ <i>л</i>. Một lít rưỡi: <b>полтора́ ли́тра</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>литро́вый</b> một lít (chai, bình) · <b>миллили́тр</b> mi-li-lít</div>'
)

# -------------------------------------------------------------------- разойтись
S["разойтись"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">разо-</span>'
    '<span class="hd-gloss">TÁCH RA nhiều phía (<i>раз-</i> thêm <i>о</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-йти-</span>'
    '<span class="hd-gloss">ĐI — chính là <b>идти́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-сь</span>'
    '<span class="hd-gloss">phản thân: mỗi người tự đi phía mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Mỗi người đi một ngả» ⇒ đám đông giải tán; vợ chồng chia tay; ý kiến khác nhau. Chia như <b>идти́</b>: <b>разойду́сь, разойдёшься</b>; quá khứ mượn <i>шёл</i>: <b>разошёлся, разошла́сь, разошли́сь</b>. Cặp CHT: <b>расходи́ться</b>.</div>'
    '<div class="hd-warn">Chia tay VỚI ai: <b>с</b> + cách 5 — <b>Она́ разошла́сь с му́жем.</b> Khác nhau VỀ gì: <b>в</b> + cách 6 — <b>Мы разошли́сь во мне́ниях.</b></div>'
    '<div class="hd-warn">Vợ chồng <b>разошли́сь</b> là thôi sống với nhau; ly hôn có giấy tờ thì rõ nhất là <b>развести́сь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>расходи́ться</b> (CHT) · <b>идти́</b> đi · <b>прийти́</b> đến · <b>расхо́д</b> khoản chi (tiền «đi tản ra»)</div>'
)

# -------------------------------------------------------------------- развивать
S["развивать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раз-</span>'
    '<span class="hd-gloss">TÁCH RA, mở bung</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ви-</span>'
    '<span class="hd-gloss">CUỘN, XOẮN — gốc của <b>вить</b> (bện)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва́-ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Tháo cuộn ra, mở dần ra» ⇒ phát triển — đúng hình ảnh của Anh <i>develop</i>. Chia đều: <b>развива́ю, развива́ешь</b>. Cặp HT: <b>разви́ть</b>.</div>'
    '<div class="hd-warn">Phát triển CÁI GÌ → cách 4: <b>развива́ть би́знес</b>, <b>развива́ть па́мять</b> rèn trí nhớ. Cái đó TỰ phát triển thì phải có <i>-ся</i>: <b>Би́знес развива́ется.</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>разви́ть</b> (HT) · <b>разви́тие</b> sự phát triển · <b>развива́ться</b> tự phát triển · <b>вить</b> xoắn, bện</div>'
)

# -------------------------------------------------------------------- развить
S["развить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раз-</span>'
    '<span class="hd-gloss">TÁCH RA, mở bung</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ви́-</span>'
    '<span class="hd-gloss">CUỘN, XOẮN — gốc của <b>вить</b> (bện)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thể HT của <b>развива́ть</b>: đã «mở cuộn» tới kết quả — <b>разви́ть ско́рость</b> đạt được tốc độ, <b>разви́ть тала́нт</b> phát triển tài năng. Thêm <i>-ся</i> là TỰ phát triển: <b>разви́ться</b>.</div>'
    '<div class="hd-warn">Thân tương lai phải thuộc riêng: <b>разовью́, разовьёшь</b> — <i>раз-</i> thêm <i>о</i>, <i>-ви-</i> thành <i>-вь-</i>, theo đúng <b>вить → вью, вьёшь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>развива́ть</b> (CHT) · <b>разви́тие</b> sự phát triển · <b>разви́ться</b> tự phát triển · <b>вить</b> xoắn, bện</div>'
)

# -------------------------------------------------------------------- ухаживать
S["ухаживать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không suy thẳng ra nghĩa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ха́ж-</span>'
    '<span class="hd-gloss">ĐI — gốc <i>ход-</i> của <b>ходи́ть</b> (<i>о → а</i>, <i>д → ж</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành, chỉ việc kéo dài</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đi quanh đi quẩn bên ai» ⇒ chăm sóc người ốm, cây, vườn; và cũng ⇒ theo tán tỉnh. Trọng âm luôn ngay trước <i>-ива-</i>: <b>уха́живаю, уха́живаешь</b>.</div>'
    '<div class="hd-warn">Luôn đòi <b>за</b> + cách 5, cả hai nghĩa: <b>уха́живать за больны́м</b> chăm người bệnh · <b>уха́живать за де́вушкой</b> thường là tán tỉnh cô gái.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ходи́ть</b> đi lại · <b>ухо́д</b> sự chăm sóc; sự rời đi · <b>ухажёр</b> anh chàng theo tán</div>'
)

# -------------------------------------------------------------------- демонстрировать
S["демонстрировать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">демонстр-</span>'
    '<span class="hd-gloss">= Anh <i>demonstr-</i> (Latin «chỉ ra»)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ровать</span>'
    '<span class="hd-gloss">= Anh <i>-ate</i>, đuôi động từ mượn</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gần y <i>demonstrate</i>: cho người ta THẤY — trình diễn sản phẩm, chiếu phim, thể hiện thái độ. Khi chia <i>-ова-</i> thành <i>-у-</i>: <b>демонстри́рую, демонстри́руешь</b>. Cặp HT: <b>продемонстри́ровать</b>.</div>'
    '<div class="hd-warn">Danh từ <b>демонстра́ция</b> hay mang nghĩa «biểu tình», nhưng ĐI biểu tình thường nói <b>идти́ на демонстра́цию</b>, không dùng động từ này.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>демонстра́ция</b> sự trình diễn; cuộc biểu tình · <b>демонстра́нт</b> người biểu tình · <b>продемонстри́ровать</b> (HT)</div>'
)

# -------------------------------------------------------------------- гарантировать
S["гарантировать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">гарант-</span>'
    '<span class="hd-gloss">= Anh <i>guarant(ee)</i> — như <b>гара́нтия</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ровать</span>'
    '<span class="hd-gloss">đuôi động từ mượn</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Động từ của <b>гара́нтия</b> ⇒ bảo đảm, cam kết. Khi chia <i>-ова-</i> thành <i>-у-</i>: <b>гаранти́рую, гаранти́руешь</b>. Bảo đảm CHO AI ở cách 3, CÁI GÌ ở cách 4: <b>Я гаранти́рую вам успе́х.</b></div>'
    '<div class="hd-warn">Một dạng dùng cho CẢ HAI thể: <b>гаранти́рую</b> vừa là «đang bảo đảm» vừa là «sẽ bảo đảm».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гара́нтия</b> sự bảo đảm, bảo hành · <b>гаранти́йный</b> thuộc bảo hành · <b>гара́нт</b> người bảo lãnh</div>'
)

# -------------------------------------------------------------------- воровать
S["воровать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вор-</span>'
    '<span class="hd-gloss">KẺ TRỘM — <b>вор</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова́-ть</span>'
    '<span class="hd-gloss">đuôi động từ: làm việc của…</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Làm việc của kẻ trộm» ⇒ ăn cắp, hay nói THÓI trộm cắp. Khi chia <i>-ова-</i> thành <i>-у-</i>: <b>вору́ю, вору́ешь</b>. Trộm một lần xong thì thường dùng <b>укра́сть</b> (khác gốc).</div>'
    '<div class="hd-warn">Trộm CỦA AI → <b>у</b> + cách 2, y như <b>укра́сть</b>: <b>Он вору́ет де́ньги у друзе́й.</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вор</b> kẻ trộm · <b>воровство́</b> sự trộm cắp · <b>вори́шка</b> kẻ trộm vặt</div>'
)

# -------------------------------------------------------------------- образовать
S["образовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">образ-</span>'
    '<span class="hd-gloss">HÌNH ẢNH, HÌNH DẠNG — <b>о́браз</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова́-ть</span>'
    '<span class="hd-gloss">hậu tố động từ: LÀM CHO thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Làm cho thành hình» ⇒ tạo thành, lập nên: <b>образова́ть коми́ссию</b> lập một uỷ ban. Khi chia <i>-ова-</i> thành <i>-у-</i>: <b>образу́ю, образу́ешь</b>. Cặp CHT: <b>образо́вывать</b>.</div>'
    '<div class="hd-warn"><b>образу́ет</b> dùng được cả cho HIỆN TẠI, hay gặp trong sách vở: <b>Го́ры образу́ют кольцо́.</b> Núi tạo thành một vòng. Riêng quá khứ <b>образова́л</b> chỉ là «đã tạo xong».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>о́браз</b> hình ảnh · <b>образова́ние</b> sự hình thành; học vấn · <b>образе́ц</b> mẫu · <b>образо́ванный</b> có học</div>'
)

# -------------------------------------------------------------------- образовывать
S["образовывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">образ-</span>'
    '<span class="hd-gloss">HÌNH ẢNH, HÌNH DẠNG — <b>о́браз</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́в-</span>'
    '<span class="hd-gloss">LÀM CHO thành — rút từ <i>-ова-</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-ть</span>'
    '<span class="hd-gloss">đuôi kéo dài → thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thể CHT của <b>образова́ть</b>: tạo thành, lập nên (đang, lặp lại). Trọng âm luôn ngay trước <i>-ыва-</i>: <b>образо́вываю, образо́вываешь</b>.</div>'
    '<div class="hd-warn">Có <i>-ыва-</i> thì chia đều, GIỮ nguyên <i>-ов-</i>: <b>образо́вывает</b>. Chỉ <b>образова́ть</b> mới đổi <i>-ова-</i> thành <i>-у-</i>: <b>образу́ет</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>образова́ть</b> (HT) · <b>о́браз</b> hình ảnh · <b>образова́ние</b> sự hình thành; học vấn · <b>образе́ц</b> mẫu</div>'
)

B = {
    "docbangmat": 113,
    "loitubat": 2,
    "nguonsai": 1,
    "baolen": [
        "Va chạm KHÔNG gỡ được: ворова́ть «ăn cắp, trộm, lấy trộm» ⊇ красть «ăn cắp, trộm» (cùng v IMPF). Gloss cả hai chỉ có «to steal» nên không cắt, không thêm gì ở ворова́ть. Lối gỡ phải do user duyệt.",
        "V cần duyệt (bỏ 1 nghĩa): пя́теро «năm, năm người» → «năm người» (gloss «five of them»; khuôn дво́е/тро́е/че́тверо = «hai/ba/bốn người»). Hết va chạm với пять.",
        "V cần duyệt (chỉ THÊM nghĩa gloss xác nhận): разойти́сь + «ly hôn, khác nhau» (get divorced / differ) · уха́живать + «tán tỉnh» (court / woo) · образова́ть + «cấu thành» (make up / constitute) · образо́вывать + «lập nên» (found / establish / set up). Chạy thử trong bộ nhớ trên mọi thẻ: 12 → 11 va chạm, không đẻ va chạm mới.",
        "Bác từ điển: уха́живать ghi HT = поуха́живать — đó là «chăm một lúc», không phải cặp thể thật; không đưa lên thẻ.",
        "Chỗ KHÔNG chắc: у- trong умоля́ть / уха́живать ghi thẳng là không suy ra nghĩa; «đi quanh đi quẩn» ở уха́живать là diễn giải từ ходи́ть, không phải luật.",
        "Tự sửa 2: гаранти́ровать bỏ câu «không có cặp» (chỉ giữ «một dạng dùng cho cả hai thể», khớp badge BI-ASP); образова́ть đổi ví dụ gượng «Ре́ки образу́ют о́зеро» → «Го́ры образу́ют кольцо́».",
    ],
}
