# -*- coding: utf-8 -*-
"""k16 — language::grammar: 14 ĐẠI TỪ.

Trục: ba đại từ nhân xưng có thân biến cách ĐỔI HẲN (я→мен-, мы→н-, он→е-/н-);
ba đại từ sở hữu ngôi 3 (его́/её/их) BẤT BIẾN, đối lập với мой/твой/наш/ваш biến
cách theo mẫu tính từ; сам nhấn mạnh chủ thể; чей hỏi "của ai".
"""

S = {}
V = {}

S["я"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">я</span>'
    '<span class="hd-gloss">TÔI — gốc trơn, không chẻ nhỏ hơn được</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỉ dạng chủ ngữ là <b>я</b>; mọi cách còn lại đổi hẳn sang '
    'thân <b>м-</b>: <b>меня́</b>, <b>мне</b>, <b>мной</b> — chính là chữ <i>me</i> của '
    'tiếng Anh và <i>me</i> Latin.</div>'
    '<div class="hd-warn">Tiếng Nga hay nói "với tôi thì…", nên dạng gặp nhiều nhất '
    'lại là cách 3 <b>мне</b>: <b>мне нра́вится</b> tôi thích · <b>мне на́до</b> tôi cần.</div>'
    '<div class="hd-warn"><b>мне не́когда</b> = tôi không rảnh, tôi đang bận.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мой</b> của tôi — mọc ra từ chính thân <b>м-</b> đó</div>'
)

S["ты"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ты</span>'
    '<span class="hd-gloss">BẠN (một người, thân mật) — gốc trơn</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ Ấn–Âu cổ còn nguyên hình: Latin <i>tu</i>, Pháp <i>tu</i>, '
    'Anh cổ <i>thou</i>. Hễ rời chủ ngữ là thân đổi sang <b>теб-/тоб-</b>: '
    '<b>тебя́</b>, <b>тебе́</b>, <b>тобо́й</b>.</div>'
    '<div class="hd-warn">Chỉ dùng với bạn bè, người nhà, trẻ con. Với người lạ hoặc '
    'người trên phải chuyển sang <b>вы</b> — gọi nhầm bằng <b>ты</b> là mất lịch sự.</div>'
    '<div class="hd-warn"><b>ух ты!</b> = ồ! chà! — ở đây <b>ты</b> đã mất hẳn nghĩa "bạn".</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>твой</b> của bạn — cùng thân <b>т-</b></div>'
)

S["мы"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мы</span>'
    '<span class="hd-gloss">CHÚNG TÔI, CHÚNG TA — gốc trơn</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chủ ngữ là <b>мы</b>, nhưng mọi cách khác bỏ hẳn chữ <b>м</b> '
    'để sang thân <b>н-</b>: <b>нас</b>, <b>нам</b>, <b>на́ми</b> — cùng gốc với Latin '
    '<i>nos</i>, Pháp <i>nous</i>.</div>'
    '<div class="hd-warn"><b>у нас</b> = ở chỗ chúng tôi, ở nước chúng tôi — cụm dùng '
    'hằng ngày, và nó luôn là <b>нас</b> chứ không bao giờ là <b>мы</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>наш</b> của chúng tôi — mọc thẳng ra từ thân <b>н-</b></div>'
)

S["вы"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы</span>'
    '<span class="hd-gloss">CÁC BẠN; NGÀI, QUÝ VỊ — gốc trơn</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Song sinh với <b>мы</b>, chỉ đổi phụ âm đầu: <b>мы</b> cho '
    '<b>нас · нам · на́ми</b> thì <b>вы</b> cho <b>вас · вам · ва́ми</b>. Gốc chung với '
    'Latin <i>vos</i>, Pháp <i>vous</i>.</div>'
    '<div class="hd-warn">Nói với MỘT người lạ vẫn phải dùng <b>вы</b>, và động từ vẫn '
    'chia số nhiều: <b>Вы говори́те</b>. Trong thư từ thì viết hoa <b>Вы</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ваш</b> của các bạn — cùng thân <b>в-</b></div>'
)

S["он"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">он</span>'
    '<span class="hd-gloss">ANH ẤY / NÓ — gốc trơn</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Lại một thân đổi hẳn: chủ ngữ <b>он</b>, còn lại là '
    '<b>его́</b>, <b>ему́</b>, <b>им</b>. Đừng dịch cứng thành "anh ấy" — mọi danh từ '
    'giống đực đều là <b>он</b>, cái bàn <b>стол</b> cũng vậy, lúc đó dịch là "nó".</div>'
    '<div class="hd-warn">Hễ đứng SAU GIỚI TỪ là mọc thêm <b>н-</b>: <b>у него́</b>, '
    '<b>к нему́</b>, <b>с ним</b>. Không có giới từ thì không có <b>н</b>: '
    '<b>я ви́жу его́</b> tôi thấy anh ấy.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>его́</b> của anh ấy · <b>она́</b> cô ấy · <b>они́</b> họ</div>'
)

S["его"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">его́</span>'
    '<span class="hd-gloss">CỦA ANH ẤY — không chẻ được, đây là cách 2 của '
    '<b>он</b> đem dùng làm sở hữu</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vì vốn đã là một dạng biến cách rồi nên nó KHÔNG biến cách '
    'thêm lần nữa: <b>его́ дом</b>, <b>его́ кни́га</b>, <b>его́ де́ти</b> — một dạng duy '
    'nhất cho mọi giống, mọi số, mọi cách.</div>'
    '<div class="hd-warn">Đuôi <b>-его́ / -ого́</b> đọc chữ <b>г</b> thành "в". Cùng luật '
    'với <b>сего́дня</b> hôm nay và <b>ничего́</b> không sao.</div>'
    '<div class="hd-warn">Sở hữu thì KHÔNG thêm <b>н-</b> sau giới từ: '
    '<b>у его́ бра́та</b> = ở chỗ anh trai của anh ấy, khác hẳn <b>у него́</b> = ở chỗ anh ấy.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>он</b> anh ấy · <b>её</b> của cô ấy · <b>их</b> của họ</div>'
)

S["её"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">её</span>'
    '<span class="hd-gloss">CỦA CÔ ẤY — cách 2 của <b>она́</b> dùng làm sở hữu</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bất biến như <b>его́</b>: <b>её брат</b>, <b>её кни́га</b>, '
    '<b>её де́ти</b>. Chữ <b>ё</b> luôn mang trọng âm nên từ này không bao giờ cần '
    'đánh dấu — cứ thấy <b>ё</b> là đọc nhấn vào đó.</div>'
    '<div class="hd-warn">Một mặt chữ hai vai: <b>её кни́га</b> = sách của cô ấy (sở hữu), '
    'còn <b>я ви́жу её</b> = tôi thấy cô ấy (tân ngữ của <b>она́</b>). Đứng ngay trước '
    'danh từ là sở hữu, đứng một mình là tân ngữ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>она́</b> cô ấy · <b>его́</b> của anh ấy · <b>их</b> của họ</div>'
)

S["их"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">их</span>'
    '<span class="hd-gloss">CỦA HỌ — cách 2 số nhiều của <b>они́</b> dùng làm sở hữu</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bộ ba <b>его́ · её · их</b> là những đại từ sở hữu DUY NHẤT '
    'không biến cách: <b>их дом</b>, <b>их кни́га</b>, <b>их де́ти</b>. Trái hẳn với '
    '<b>мой</b>, <b>твой</b>, <b>наш</b>, <b>ваш</b> — bốn từ kia phải chia theo mẫu tính từ.</div>'
    '<div class="hd-warn">Không có từ <b>и́хний</b> trong tiếng Nga chuẩn. Nghe thấy '
    'ngoài đường thì đó là lối nói bình dân, viết ra là sai.</div>'
    '<div class="hd-warn">Sở hữu giữ nguyên sau giới từ: <b>у их дру́га</b> = ở chỗ bạn '
    'của họ; còn <b>у них</b> = ở chỗ họ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>они́</b> họ · <b>его́</b> của anh ấy · <b>её</b> của cô ấy</div>'
)

S["мой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">м-</span>'
    '<span class="hd-gloss">TÔI — cùng thân với <b>меня́</b>, <b>мне</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ой</span>'
    '<span class="hd-gloss">đuôi chia y như một tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vì mang đuôi tính từ nên nó hợp giống và số với VẬT được sở '
    'hữu, không phải với người sở hữu: <b>моя́ кни́га</b> sách của tôi · <b>моё окно́</b> '
    'cửa sổ của tôi · <b>мои́ де́ти</b> các con tôi. Trọng âm luôn dồn ra đuôi: '
    '<b>моего́</b>, <b>мои́м</b>.</div>'
    '<div class="hd-warn"><b>по-мо́ему</b> = theo tôi thì, theo ý tôi — chính là dạng '
    'cách 3 <b>моему́</b> gắn thêm tiền tố <b>по-</b>, rồi trọng âm lùi về <b>мо́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>я</b> tôi — cùng thân <b>м-</b></div>'
)

S["твой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">тв-</span>'
    '<span class="hd-gloss">BẠN — từ <b>ты</b> (<b>тебя́</b>, <b>тебе́</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ой</span>'
    '<span class="hd-gloss">cùng đuôi tính từ với <b>мой</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chia đúng khuôn <b>мой</b>, chỉ đổi thân <b>м-</b> thành <b>тв-</b>: '
    '<b>твоя́</b>, <b>твоё</b>, <b>твои́</b>, <b>твоего́</b> — trọng âm cũng luôn ở đuôi.</div>'
    '<div class="hd-warn">Đi liền một cặp với <b>ты</b>: đã xưng <b>ты</b> mới được dùng '
    '<b>твой</b>. Với người lạ hay người trên thì phải là <b>ваш</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ты</b> bạn · <b>по-тво́ему</b> theo ý bạn</div>'
)

S["наш"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">наш-</span>'
    '<span class="hd-gloss">CHÚNG TÔI — mọc từ thân <b>н-</b> của <b>мы</b> '
    '(<b>нас</b>, <b>нам</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cũng chia như tính từ (<b>на́ша</b>, <b>на́ше</b>, <b>на́ши</b>), '
    'nhưng khác <b>мой/твой</b> ở một điểm dễ nhớ: trọng âm ĐỨNG YÊN ở <b>на-</b> suốt '
    'cả bảng — <b>на́шего</b>, <b>на́шему</b>, <b>на́шими</b>.</div>'
    '<div class="hd-warn">Số nhiều viết <b>на́ши</b> chứ không phải "нашы": sau <b>ш</b> '
    'không bao giờ được viết <b>ы</b>, phải thay bằng <b>и</b> (luật ЖИ ШИ).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мы</b> chúng tôi · <b>по-на́шему</b> theo ý chúng tôi</div>'
)

S["ваш"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ваш-</span>'
    '<span class="hd-gloss">CÁC BẠN, QUÝ VỊ — mọc từ thân <b>в-</b> của <b>вы</b> '
    '(<b>вас</b>, <b>вам</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Sinh đôi với <b>наш</b>, đổi đúng chữ đầu: <b>ва́ша</b>, '
    '<b>ва́ше</b>, <b>ва́ши</b>, <b>ва́шего</b> — trọng âm cũng nằm yên ở <b>ва-</b>.</div>'
    '<div class="hd-warn"><b>Как ва́ши дела́?</b> = dạo này anh/chị thế nào? — câu hỏi '
    'thăm chuẩn mực, học thuộc cả cụm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вы</b> các bạn · <b>по-ва́шему</b> theo ý các bạn</div>'
)

S["сам"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сам-</span>'
    '<span class="hd-gloss">TỰ, CHÍNH — gốc trơn, không chẻ nhỏ hơn được</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Việc của nó là NHẤN MẠNH chủ thể: chính người đó làm, không '
    'nhờ ai — <b>он сам сде́лал</b> chính anh ấy tự làm. Nên nó hợp giống và số với '
    'từ mà nó nhấn: <b>сама́</b>, <b>само́</b>, <b>са́ми</b>.</div>'
    '<div class="hd-why">Trọng âm nhảy giữa chừng ở số nhiều: chủ cách là <b>са́ми</b> '
    '(nhấn đầu) nhưng các cách còn lại dồn hết ra đuôi — <b>сами́х</b>, <b>сами́м</b>, '
    '<b>сами́ми</b>.</div>'
    '<div class="hd-warn">Khác <b>себя́</b>: <b>себя́</b> làm TÂN NGỮ (làm gì đó với chính '
    'mình), còn <b>сам</b> chỉ đứng cạnh chủ ngữ để nhấn, không bao giờ làm tân ngữ.</div>'
    '<div class="hd-warn">Đừng lẫn với <b>са́мый</b> — từ đó dùng để tạo so sánh nhất '
    '(<b>са́мый большо́й</b> to nhất) và trọng âm luôn nằm ở đầu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>самолёт</b> máy bay (tự + bay) · <b>самова́р</b> ấm samovar '
    '(tự + đun) · <b>са́мый</b> nhất</div>'
)

S["чей"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">чь-</span>'
    '<span class="hd-gloss">CỦA AI — thân thật, luôn mềm: <b>чья</b>, <b>чьё</b>, '
    '<b>чьи</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hỏi "của ai?" nhưng hợp giống và số với VẬT được hỏi, không '
    'phải với người chủ: <b>Чей э́то дом?</b> · <b>Чья э́то кни́га?</b> · '
    '<b>Чьи э́то де́ти?</b></div>'
    '<div class="hd-why">Chữ <b>е</b> chỉ mọc ra để đỡ dạng trần <b>чей</b>; thêm bất cứ '
    'đuôi nào là nó rơi mất, chỉ còn thân mềm — <b>чья</b>, <b>чьё</b>, <b>чьи</b>, '
    '<b>чьего́</b>.</div>'
    '<div class="hd-warn">Câu trả lời cho <b>чей?</b> chính là bốn từ <b>мой · твой · '
    'наш · ваш</b>, hoặc bộ bất biến <b>его́ · её · их</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кто</b> ai · <b>что</b> gì — cùng bộ từ để hỏi</div>'
)

# --- field Vietnamese (đề bài deck 1-go) — README §2c -------------------------
# Lô toàn `pron` nên badge KHÔNG tách được cặp nào. Gỡ bằng cách LIỆT KÊ ĐỦ
# nghĩa (§2c), không dùng ngoặc chú thích:
#   ты/вы  — số ít thân mật vs số nhiều & trang trọng: bộ đại từ xưng hô
#            tiếng Việt của hai bên vốn khác nhau, liệt kê đủ là tự tách.
#   твой/ваш — cùng khuôn với cặp trên.
#   сам    — bỏ "bản thân, chính mình" (vốn là себя́ ở k51), giữ đúng nghĩa
#            NHẤN MẠNH chủ thể.
# ты / твой GIỮ NGUYÊN bản cũ; chỉ cần gỡ "bạn" khỏi phía вы/ваш là hai cặp
# hết chồng nhau — sửa ít thẻ hơn, và đó cũng là bộ nghĩa đúng của вы/ваш.
V["вы"] = "các bạn, các anh, các chị, ngài, quý vị"
V["ваш"] = "của các bạn, của các anh, của các chị, của ngài, của quý vị"
V["сам"] = "tự mình, đích thân"
# его/её cho khớp bộ nghĩa của он/она; наш bỏ "của ta" mơ hồ.
V["его"] = "của anh ấy, của ông ấy, của nó"
V["её"] = "của cô ấy, của bà ấy"
V["наш"] = "của chúng tôi, của chúng ta"
