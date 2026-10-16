# -*- coding: utf-8 -*-
"""k96 — actions: 18 từ mới (đợt A1-A2 TRKI), tám cặp thể soạn như một họ.

Không khối hệ thống. Chỗ cần nhất quán:
(1) tám cặp thể chung lô — mỗi vế nói phần của nó, không chép nhau;
(2) gốc -ход-/-йти khớp khuôn đã có: на- «chạm tới» (находи́ться k49), -йти = идти́
    (прийти́ k49, пойти́ k75), пере- «QUA» + -вод- «DẪN» (перево́дчик k58);
(3) плыть/пла́вать đối lập một chiều/nhiều chiều như идти́/ходи́ть (k64); bảng so sánh
    đặt ở плыть, пла́вать chỉ dẫn chiếu; поплы́ть theo khuôn по- «bắt đầu đi» của пойти́.
"""

S = {}

# -------------------------------------------------------- мешать
S["мешать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">меш-</span>'
    '<span class="hd-gloss">gốc KHUẤY, TRỘN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi động từ, chia đều: <b>меша́ю, меша́ешь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc là khuấy trộn; thọc tay khuấy vào việc của người khác ⇒ '
    'làm phiền, cản trở. Cùng gốc Ấn-Âu xa với Latin <i>miscēre</i> → Anh <i>mix</i>. '
    'Cặp thể: <b>помеша́ть</b>.</div>'
    '<div class="hd-warn">Hai nghĩa, hai cách: làm phiền AI → cách 3 (<b>Не меша́й мне!</b> '
    'Đừng làm phiền tôi!); khuấy CÁI GÌ → cách 4 (<b>меша́ть суп</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>помеша́ть</b> làm phiền, khuấy (HT) · <b>смеша́ть</b> trộn lẫn · '
    '<b>поме́ха</b> vật cản, nhiễu</div>'
)

# -------------------------------------------------------- помешать
S["помешать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">đánh dấu XONG; với nghĩa khuấy thì thêm sắc thái «một lát»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-меш-а́ть</span>'
    '<span class="hd-gloss">chính là <b>меша́ть</b> — khuấy; làm phiền</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một lần cản trở cụ thể, đã xảy ra: <b>Дождь помеша́л нам.</b> '
    'Cơn mưa đã cản chúng tôi. Chia đều: <b>помеша́ю, помеша́ешь</b>.</div>'
    '<div class="hd-warn">Người bị cản ở cách 3, việc bị cản là nguyên thể: '
    '<b>Шум помеша́л мне спать.</b> Tiếng ồn làm tôi không ngủ được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>меша́ть</b> làm phiền, khuấy (CHT) · <b>поме́ха</b> vật cản, nhiễu</div>'
)

# -------------------------------------------------------- молчать
S["молчать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">молч-</span>'
    '<span class="hd-gloss">gốc IM, KHÔNG NÓI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi động từ — nhưng chia theo lớp 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi <b>-ать</b> mà chia lớp 2, phải thuộc riêng (như <b>слы́шать</b>): '
    '<b>молчу́, молчи́шь, молча́т</b> — không có «молчаешь». Đừng suy theo <b>меша́ть</b> '
    '(<b>меша́ю</b>, lớp 1).</div>'
    '<div class="hd-warn"><b>Молчи́!</b> = Im đi! — rất cộc. Nhờ người lạ nhỏ tiếng thì nói '
    '<b>Ти́ше, пожа́луйста</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>молча́ние</b> sự im lặng · <b>мо́лча</b> lặng lẽ, không nói gì · '
    '<b>замолча́ть</b> im bặt</div>'
)

# -------------------------------------------------------- найти
S["найти"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">CHẠM TỚI, trúng vào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-йти</span>'
    '<span class="hd-gloss">ĐI — chính là <b>идти́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đi mà chạm trúng ⇒ tìm THẤY. Chia như <b>идти́</b>: '
    '<b>найду́, найдёшь</b>; quá khứ mượn <b>шёл</b> nên phải thuộc: '
    '<b>нашёл, нашла́, нашли́</b>. Cặp thể: <b>находи́ть</b>.</div>'
    '<div class="hd-warn"><b>найти́</b> là THẤY (có kết quả), <b>иска́ть</b> là đang TÌM: '
    '<b>Я иска́л, но не нашёл.</b> Tôi đã tìm mà không thấy.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>находи́ть</b> tìm thấy (CHT) · <b>найти́сь</b> tự lộ ra · '
    '<b>нахо́дка</b> vật nhặt được · <b>идти́</b> đi bộ</div>'
)

# -------------------------------------------------------- находить
S["находить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">CHẠM TỚI, trúng vào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ход-</span>'
    '<span class="hd-gloss">ĐI — gốc của <b>ходи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp thể của <b>найти́</b>: hay tìm thấy, lần nào cũng thấy. '
    'Chia y như <b>ходи́ть</b>: ngôi «tôi» <b>д→ж</b> và trọng âm ở đuôi <b>нахожу́</b>, '
    'còn lại lùi vào gốc <b>нахо́дишь</b>.</div>'
    '<div class="hd-warn">«Thấy ai/cái gì THẾ NÀO»: vật ở cách 4, nhận xét ở cách 5 — '
    '<b>Я нахожу́ э́ту кни́гу интере́сной.</b> Tôi thấy cuốn sách này thú vị.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>найти́</b> tìm thấy (HT) · <b>находи́ться</b> nằm ở, tọa lạc · '
    '<b>нахо́дка</b> vật nhặt được</div>'
)

# -------------------------------------------------------- насорить
S["насорить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">đánh dấu XONG, như <b>на-</b> trong <b>написа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-сор-</span>'
    '<span class="hd-gloss">gốc RÁC — <b>сор</b> là rác vụn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đã làm vương rác ra rồi: <b>Кто здесь насори́л?</b> '
    'Ai xả rác ở đây thế? Chia đều: <b>насорю́, насори́шь</b>. Cặp thể: <b>сори́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сори́ть</b> xả rác (CHT) · <b>сор</b> rác vụn · '
    '<b>сорня́к</b> cỏ dại</div>'
)

# -------------------------------------------------------- сорить
S["сорить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сор-</span>'
    '<span class="hd-gloss">RÁC — <b>сор</b> là rác vụn, bụi bẩn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi biến danh từ thành động từ, lớp chia 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ <b>сор</b> + <b>-ить</b> = vãi rác ra. Câu nhắc hay gặp: '
    '<b>Не сори́!</b> Chia đều: <b>сорю́, сори́шь</b>. Cặp thể: <b>насори́ть</b>.</div>'
    '<div class="hd-warn"><b>сори́ть деньга́ми</b> (tiền ở cách 5) = vung tiền như rác.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>насори́ть</b> xả rác (HT) · <b>со́рный</b> thuộc rác · '
    '<b>сорня́к</b> cỏ dại (cỏ rác)</div>'
)

# -------------------------------------------------------- обещать
S["обещать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">bao quanh, ràng vào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ещ-</span>'
    '<span class="hd-gloss">gốc NÓI trang trọng, mặt cũ là <b>-вет-</b> (rụng <b>в</b>, <b>т→щ</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi động từ, chia đều: <b>обеща́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nói ra một lời tự ràng mình ⇒ hứa. Người được hứa ở cách 3: '
    '<b>Я обеща́ю тебе́ позвони́ть.</b> Từ điển xếp <b>обеща́ть</b> vào cả hai thể; '
    'muốn nói rõ «đã hứa xong» thì người ta dùng <b>пообеща́ть</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: <b>-ещ-</b> = <b>-вет-</b> là từ nguyên, mặt chữ hiện đại '
    'không lộ ra — đừng dùng nó làm luật suy từ khác.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пообеща́ть</b> hứa (HT) · <b>обеща́ние</b> lời hứa · '
    'xa hơn, gốc <b>-вет-</b>: <b>отве́т</b> câu trả lời, <b>сове́т</b> lời khuyên</div>'
)

# -------------------------------------------------------- пообещать
S["пообещать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">chỉ đánh dấu XONG, không thêm nghĩa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-обеща́ть</span>'
    '<span class="hd-gloss">chính là <b>обеща́ть</b> — hứa</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một lần hứa cụ thể, đã nói ra rồi: <b>Он пообеща́л прийти́.</b> '
    'Anh ấy đã hứa sẽ đến. Chia đều: <b>пообеща́ю, пообеща́ешь</b>; người được hứa vẫn ở '
    'cách 3 như <b>обеща́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обеща́ть</b> hứa (CHT) · <b>обеща́ние</b> lời hứa</div>'
)

# -------------------------------------------------------- объяснить
S["объяснить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">bao quanh, khắp lượt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ъ-</span>'
    '<span class="hd-gloss">dấu cứng: giữ <b>я</b> đọc tách sau tiền tố</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ясн-</span>'
    '<span class="hd-gloss">RÕ — chính là <b>я́сно</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia 2: <b>объясню́, объясни́шь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm cho rõ từ mọi phía ⇒ giải thích, và giải thích XONG. '
    'Người nghe ở cách 3. Cặp thể: <b>объясня́ть</b>.</div>'
    '<div class="hd-warn">Câu xin hằng ngày: <b>Объясни́те мне, пожа́луйста…</b> '
    'Làm ơn giải thích giúp tôi…</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>объясня́ть</b> giải thích (CHT) · <b>я́сно</b> rõ · '
    '<b>я́сный</b> rõ ràng · <b>объясне́ние</b> lời giải thích</div>'
)

# -------------------------------------------------------- объяснять
S["объяснять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">объ-ясн-</span>'
    '<span class="hd-gloss">làm cho RÕ — như <b>объясни́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành, chia đều: <b>объясня́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đổi <b>-и́ть</b> thành <b>-я́ть</b> là sang thể chưa xong: đang '
    'giảng, hay giảng, giảng mãi. <b>Учи́тель объясня́ет пра́вило.</b> Thầy đang giảng quy '
    'tắc. Người nghe vẫn ở cách 3.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>объясни́ть</b> giải thích (HT) · <b>я́сно</b> rõ · '
    '<b>объясне́ние</b> lời giải thích</div>'
)

# -------------------------------------------------------- перевести
S["перевести"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пере-</span>'
    '<span class="hd-gloss">QUA, từ bên này sang bên kia</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вес-ти́</span>'
    '<span class="hd-gloss">DẪN — gốc thật là <b>вед-</b> (cùng <b>-вод-</b> của <b>води́ть</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dẫn qua bên kia: dẫn ý sang tiếng khác (dịch), dẫn tiền sang tài khoản '
    'khác, dẫn người qua đường. Gốc <b>вед-</b> đổi <b>д→с</b> trước <b>-ти</b> và rụng '
    '<b>д</b> trước <b>-л</b>: <b>переведу́</b> nhưng <b>перевёл, перевела́</b>.</div>'
    '<div class="hd-warn">Dịch TỪ tiếng nào thì <b>с</b> + cách 2, SANG tiếng nào thì <b>на</b> '
    '+ cách 4: <b>перевести́ с ру́сского на вьетна́мский</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>переводи́ть</b> dịch (CHT) · <b>перево́д</b> bản dịch, sự chuyển '
    'tiền · <b>перево́дчик</b> phiên dịch viên · <b>води́ть</b> dẫn, lái xe</div>'
)

# -------------------------------------------------------- переводить
S["переводить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пере-</span>'
    '<span class="hd-gloss">QUA, từ bên này sang bên kia</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вод-</span>'
    '<span class="hd-gloss">DẪN — gốc của <b>води́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp thể của <b>перевести́</b>: đang dịch, hay dịch, làm nghề dịch. '
    'Chia y như <b>ходи́ть</b>: <b>перевожу́</b> (<b>д→ж</b>, trọng âm ở đuôi), rồi '
    '<b>перево́дишь</b> (trọng âm lùi vào gốc).</div>'
    '<div class="hd-warn"><b>Я перевожу́ с ру́сского.</b> Tôi dịch từ tiếng Nga — cách dùng '
    '<b>с … на …</b> giống hệt <b>перевести́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>перевести́</b> dịch (HT) · <b>перево́д</b> bản dịch · '
    '<b>перево́дчик</b> phiên dịch viên · <b>води́ть</b> dẫn, lái xe</div>'
)

# -------------------------------------------------------- перейти
S["перейти"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пере-</span>'
    '<span class="hd-gloss">QUA, từ bên này sang bên kia</span></div>'
    '<div class="hd-row"><span class="hd-piece">-йти</span>'
    '<span class="hd-gloss">ĐI — chính là <b>идти́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đi qua bên kia: <b>перейти́ у́лицу</b> (cách 4, không cần giới từ). '
    'Nghĩa bóng: chuyển sang việc khác, đề tài khác. Chia như <b>идти́</b>: <b>перейду́</b>; '
    'quá khứ mượn <b>шёл</b>: <b>перешёл, перешла́</b>.</div>'
    '<div class="hd-warn"><b>Дава́й перейдём на «ты»!</b> = Mình xưng «ты» với nhau nhé — câu '
    'người Nga nói khi muốn bỏ lối xưng hô trang trọng <b>вы</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>переходи́ть</b> băng qua (CHT) · <b>перехо́д</b> lối qua đường · '
    '<b>прийти́</b> đến nơi · <b>идти́</b> đi bộ</div>'
)

# -------------------------------------------------------- переходить
S["переходить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пере-</span>'
    '<span class="hd-gloss">QUA, từ bên này sang bên kia</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ход-</span>'
    '<span class="hd-gloss">ĐI — gốc của <b>ходи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp thể của <b>перейти́</b>: đang băng qua, hay băng qua. Chia y như '
    '<b>ходи́ть</b>: <b>перехожу́</b> (<b>д→ж</b>), rồi <b>перехо́дишь</b>.</div>'
    '<div class="hd-warn"><b>переходи́ть от слов к де́лу</b> = chuyển từ lời nói sang việc làm, '
    'thôi nói mà bắt tay vào làm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>перейти́</b> băng qua (HT) · <b>перехо́д</b> lối qua đường · '
    '<b>ходи́ть</b> đi lại · <b>вы́ход</b> lối ra</div>'
)

# -------------------------------------------------------- плыть
S["плыть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">плы-</span>'
    '<span class="hd-gloss">gốc BƠI, TRÔI trên nước — trong bảng chia hiện ra <b>плыв-</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thân hiện tại chèn <b>в</b>, phải thuộc: <b>плыву́, плывёшь</b>. '
    'Quá khứ giống cái trọng âm ra đuôi: <b>плыла́</b>. Vật cũng «плыть» được: mây trôi, '
    'thuyền trôi.</div>'
    '<div class="hd-warn"><b>плыть</b> là bơi MỘT CHIỀU, đang tới đích, như <b>идти́</b>; '
    '<b>пла́вать</b> là bơi nói chung, qua lại, như <b>ходи́ть</b>. <b>Я плыву́ к бе́регу</b> '
    '(đang bơi vào bờ) ↔ <b>Я пла́ваю в бассе́йне</b> (tôi đi bơi ở bể).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поплы́ть</b> bắt đầu bơi (HT) · <b>пла́вать</b> bơi lội · '
    '<b>пла́вание</b> bơi lội (môn) · <b>плове́ц</b> người bơi</div>'
)

# -------------------------------------------------------- плавать
S["плавать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пла́в-</span>'
    '<span class="hd-gloss">gốc BƠI, TRÔI — cùng gốc với <b>плыть</b> (<b>ы</b> ↔ <b>ав</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">đuôi động từ, chia đều: <b>пла́ваю, пла́ваешь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Động từ NHIỀU CHIỀU của cặp <b>плыть</b>/<b>пла́вать</b> — so sánh '
    'đầy đủ nằm ở thẻ <b>плыть</b>. Dùng cho bơi như một kỹ năng, một thói quen: '
    '<b>Я не уме́ю пла́вать.</b> Tôi không biết bơi. Đồ vật thì <b>пла́вать</b> là nổi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>плыть</b> bơi một chiều · <b>пла́вание</b> bơi lội (môn) · '
    '<b>плове́ц</b> người bơi · <b>пла́вки</b> quần bơi</div>'
)

# -------------------------------------------------------- поплыть
S["поплыть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">BẮT ĐẦU, cất bước một chặng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-плыть</span>'
    '<span class="hd-gloss">chính là <b>плыть</b> — bơi một chiều</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng khuôn <b>пойти́</b>: <b>по-</b> gắn vào động từ chuyển động một '
    'chiều = BẮT ĐẦU đi ⇒ bơi đi, thuyền rời bến. Bảng chia theo hẳn <b>плыть</b>: '
    '<b>поплыву́, поплывёшь</b>; <b>поплы́л, поплыла́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>плыть</b> bơi một chiều (CHT) · <b>пла́вать</b> bơi lội · '
    '<b>пла́вание</b> bơi lội (môn)</div>'
)


# ------------------------------------------------------------------ VIỆT
V = {
    # Tiếng Anh có "to mix" mà đề bài thiếu; "khuấy đều" rút về "khuấy".
    "мешать": "làm phiền, cản trở, khuấy, trộn",
    # Trùng trọn "bơi" với плавать, cùng cả ba badge. Gỡ theo tiền lệ ехать/ездить:
    # một chiều giữ chữ trơn + "đang … tới", nhiều chiều nhận "bơi lội / qua lại".
    "плыть": "bơi, đang bơi tới, đi thuyền, trôi",
    "плавать": "bơi lội, bơi qua lại, nổi, đi biển",
    # Bỏ ngoặc "(tiêu tiền như nước)" — cấm ghi chú trong ngoặc.
    "сорить": "xả rác, vứt rác bừa bãi, phung phí",
    # Thiếu hẳn nghĩa "transfer to another place / relocate" mà tiếng Anh xếp ngay sau "dịch".
    "перевести": "dịch, chuyển tiền, điều chuyển",
}
