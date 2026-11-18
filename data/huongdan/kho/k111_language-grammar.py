# -*- coding: utf-8 -*-
"""k111 — language-grammar: 21 hư từ B1 (giới từ, tiểu từ, liên từ, đại từ bất định).

Chỗ cần nhất quán trong lô:
(1) cặp ра́зве ↔ неуже́ли: phép so trải ở ра́зве, thẻ неуже́ли dẫn chiếu một dòng;
(2) -то (како́й-то, что́-то) theo đúng cách chẻ của кто́-то (k110); so -то ↔ -нибудь không lặp lại;
(3) chiều đi–về của giới từ: в→из, на→с (đã dạy ở thẻ с/из), lô này thêm к→от;
(4) над/под đối nhau, so với на ở thẻ над.
Họ hàng cố ý vắng: ра́зве, кро́ме, неуже́ли (hư từ không có từ phái sinh đáng dạy;
неуже́ли thì các mảnh đã nằm sẵn trong Chẻ từ).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "неужели": "chẳng lẽ, thật sao",
    "разве": "lẽ nào",
    "из-за": "do",
    "против": "chống lại",
    "над": "phía trên",
    "же": "mà, chứ",
    "среди": "trong số",
    "ли": "liệu ... không",
    "однако": "tuy nhiên",
}

# ------------------------------------------------------------------- из-за
S["из-за"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">из</span>'
    '<span class="hd-gloss">TỪ TRONG ra</span></div>'
    '<div class="hd-row"><span class="hd-piece">за</span>'
    '<span class="hd-gloss">PHÍA SAU</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen «từ phía sau ra», kéo cách 2: <b>из-за угла́</b> = từ sau góc '
    'phố · <b>встать из-за стола́</b> = đứng dậy rời bàn. Từ đó ra nghĩa «vì»: cái lý do đứng '
    'đằng sau sự việc.</div>'
    '<div class="hd-warn">Lý do thường là chuyện XẤU: <b>из-за дождя́</b> = vì mưa (nên hỏng '
    'việc). Lý do tốt thì nói <b>благодаря́</b> = nhờ có.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>из</b> từ trong ra · <b>за</b> phía sau · <b>из-под</b> từ bên '
    'dưới ra (cùng khuôn)</div>'
)

# ------------------------------------------------------------------ против
S["против"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Giới từ gốc, không chẻ ra mảnh mang nghĩa riêng được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Kéo cách 2: <b>про́тив войны́</b> = chống chiến tranh · '
    '<b>Я про́тив</b> = tôi phản đối. Nghĩa «đối diện» cũng có, nhưng nói vị trí thì người Nga '
    'thường dùng <b>напро́тив</b> (thẻ đã học).</div>'
    '<div class="hd-warn">Câu xin phép lịch sự hằng ngày: <b>Вы не про́тив?</b> = Anh/chị '
    'không phiền chứ? (nghĩa đen «không phản đối chứ?»)</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>напро́тив</b> đối diện, trái lại · <b>проти́вник</b> đối thủ · '
    '<b>противополо́жный</b> đối lập</div>'
)

# --------------------------------------------------------------------- над
S["над"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Giới từ một âm, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Phía trên, KHÔNG chạm» — khác <b>на</b> là nằm trên mặt. Luôn kéo '
    'cách 5: <b>ла́мпа над столо́м</b> = đèn treo phía trên bàn · <b>кни́га на столе́</b> = '
    'sách nằm trên bàn. Cặp đối của nó là <b>под</b> (phía dưới).</div>'
    '<div class="hd-warn">Nghĩa bóng phải thuộc theo động từ: <b>рабо́тать над прое́ктом</b> = '
    'làm một dự án · <b>смея́ться над ним</b> = cười nhạo anh ta.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">Tiền tố над- giữ nghĩa «ở trên»: <b>на́дпись</b> dòng chữ ghi lên '
    '(trên bề mặt) · <b>надзо́р</b> sự giám sát (nhìn từ trên xuống)</div>'
)

# ------------------------------------------------------------------- перед
S["перед"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Giới từ gốc, không chẻ được — nhưng gốc <i>перед-/перёд-</i> «phía '
    'trước» còn sống trong các từ ở Họ hàng.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Kéo cách 5. Không gian: <b>пе́ред до́мом</b> = trước nhà. Thời gian: '
    '<b>пе́ред сном</b> = ngay trước khi ngủ.</div>'
    '<div class="hd-warn">«Trước» thời gian có hai từ: <b>пе́ред обе́дом</b> = SÁT trước bữa '
    'trưa · <b>до обе́да</b> (cách 2) = cả khoảng thời gian trước bữa trưa.</div>'
    '<div class="hd-warn">Xin lỗi AI thì dùng пе́ред: <b>извини́ться пе́ред дру́гом</b> = xin '
    'lỗi bạn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вперёд</b> tiến lên phía trước · <b>впереди́</b> ở phía trước · '
    '<b>пере́дний</b> ở đằng trước</div>'
)

# --------------------------------------------------------------------- под
S["под"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Giới từ một âm, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giống <b>на</b>/<b>в</b>, cách nói lên đứng yên hay chuyển động: '
    '<b>под столо́м</b> (cách 5) = đang ở dưới bàn · <b>под стол</b> (cách 4) = chui/đặt xuống '
    'dưới bàn. Đối xứng với <b>над</b> phía trên.</div>'
    '<div class="hd-warn">Cạnh tên thành phố thì là «vùng ven», không phải «dưới»: '
    '<b>под Москво́й</b> = ở ngoại ô Mát-xcơ-va.</div>'
    '<div class="hd-warn">Với âm nhạc, cách 4: <b>под му́зыку</b> = theo tiếng nhạc, có nhạc đệm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">Tiền tố под- giữ cả hai nghĩa «dưới» và «sát gần»: '
    '<b>подзе́мный</b> dưới mặt đất · <b>подписа́ть</b> ký (viết ở dưới) · '
    '<b>подойти́</b> lại gần</div>'
)

# ------------------------------------------------------------------- разве
S["разве"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Tiểu từ, không chẻ ra mảnh mang nghĩa riêng được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đặt đầu câu hỏi khi mình NGHI, tưởng sự việc khác cơ: <b>Ра́зве ты '
    'не зна́ешь?</b> = Lẽ nào cậu không biết? (tôi tưởng cậu biết).</div>'
    '<div class="hd-warn">Cặp dễ lẫn: <b>ра́зве</b> = nghi ngờ, hơi phản bác · '
    '<b>неуже́ли</b> = ngạc nhiên thật sự trước điều vừa biết: <b>Неуже́ли ты всё сде́лал?</b> = '
    'Cậu làm xong hết rồi thật á?</div>'
    '<div class="hd-warn">Cụm cố định: <b>ра́зве что</b> = trừ phi, may ra chỉ.</div>'
)

# ---------------------------------------------------------------------- же
S["же"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Tiểu từ một âm, không chẻ được, không mang trọng âm.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không đứng một mình — luôn đuôi theo từ mình muốn nhấn: <b>Я же '
    'говори́л!</b> = Tôi nói rồi mà! · <b>Ты же зна́ешь</b> = Cậu biết rồi còn gì. Sau từ chỉ '
    'định nó thành «chính, cùng»: <b>тот же</b> = cùng cái đó · <b>сейча́с же</b> = ngay bây '
    'giờ.</div>'
    '<div class="hd-warn">Một dấu cách đổi nghĩa: <b>то́же</b> = cũng · <b>то же са́мое</b> = '
    'cùng một thứ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>то́же</b> cũng (то + же) · <b>та́кже</b> ngoài ra (так + же)</div>'
)

# ------------------------------------------------------------------- кроме
S["кроме"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Giới từ gốc, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Kéo cách 2, và y như «ngoài … ra» của tiếng Việt, nó vừa LOẠI RA vừa '
    'CỘNG THÊM: <b>Все, кро́ме него́, пришли́</b> = Mọi người đến, trừ anh ta · <b>Кро́ме '
    'него́ пришли́ ещё дво́е</b> = Ngoài anh ta còn hai người nữa.</div>'
    '<div class="hd-warn">Cụm nối câu phải thuộc: <b>кро́ме того́</b> = ngoài ra, hơn nữa.</div>'
)

# ------------------------------------------------------------------- среди
S["среди"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сред-</span>'
    '<span class="hd-gloss">GIỮA — gốc của <b>сре́дний</b>, <b>среда́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́</span>'
    '<span class="hd-gloss">đuôi cũ, nay không mang nghĩa riêng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Ở giữa một ĐÁM», kéo cách 2: <b>среди́ друзе́й</b> = trong đám bạn bè. '
    'Cũng dùng cho giữa một khoảng thời gian: <b>среди́ но́чи</b> = giữa đêm.</div>'
    '<div class="hd-warn">Giữa HAI bên thì dùng <b>ме́жду</b> + cách 5: <b>ме́жду до́мом и '
    'шко́лой</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сре́дний</b> ở giữa, trung bình · <b>середи́на</b> chính giữa · '
    '<b>среда́</b> thứ Tư; môi trường · <b>посреди́</b> ở chính giữa</div>'
)

# ---------------------------------------------------------------------- ли
S["ли"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Tiểu từ một âm, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Biến câu thành «có … không?» và đứng NGAY SAU từ được hỏi: <b>Зна́ешь '
    'ли ты?</b> = Cậu có biết không? Chỗ gặp nhiều nhất là câu hỏi gián tiếp: <b>Не зна́ю, '
    'придёт ли он</b> = Không biết liệu anh ấy có đến không.</div>'
    '<div class="hd-warn">Bẫy của người biết tiếng Anh: <i>if</i> = «liệu» thì dùng ли, KHÔNG '
    'dùng <b>е́сли</b> — е́сли chỉ là «nếu» điều kiện.</div>'
    '<div class="hd-warn">Cụm hay gặp: <b>вряд ли</b> = khó mà, chắc là không.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>и́ли</b> hoặc (и + ли) · <b>неуже́ли</b> chẳng lẽ (не + уже́ + ли)</div>'
)

# ----------------------------------------------------------------- неужели
S["неужели"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не</span>'
    '<span class="hd-gloss">không</span></div>'
    '<div class="hd-row"><span class="hd-piece">уже́</span>'
    '<span class="hd-gloss">đã, rồi (thẻ đã học)</span></div>'
    '<div class="hd-row"><span class="hd-piece">ли</span>'
    '<span class="hd-gloss">liệu … không</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Lẽ nào đã… thật sao?» — ngạc nhiên trước điều vừa biết: <b>Неуже́ли '
    'ты всё сде́лал?</b> Đứng một mình làm câu đáp: — Я вы́играл. — <b>Неуже́ли?</b> = Thật á?</div>'
    '<div class="hd-why">So với <b>ра́зве</b>: xem thẻ ра́зве.</div>'
    '<div class="hd-warn">⚠️ Mức tin: cách chẻ ba mảnh là từ nguyên, giúp nhớ chứ không phải '
    'luật ghép từ còn dùng.</div>'
)

# ------------------------------------------------------------------- любой
S["любой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">люб-</span>'
    '<span class="hd-gloss">YÊU, ưa — gốc của <b>люби́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́й</span>'
    '<span class="hd-gloss">đuôi tính từ ⇒ đổi theo giống, số, cách</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cái nào mình ưa cũng được» ⇒ bất kỳ: <b>в любо́е вре́мя</b> = lúc nào '
    'cũng được.</div>'
    '<div class="hd-warn"><b>ка́ждый</b> = MỖI cái, lần lượt tất cả · <b>любо́й</b> = cái NÀO '
    'cũng được, chọn một.</div>'
    '<div class="hd-warn">Cụm phải thuộc: <b>в любо́м слу́чае</b> = dù sao đi nữa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>люби́ть</b> yêu, thích · <b>любо́вь</b> tình yêu · '
    '<b>люби́мый</b> yêu thích</div>'
)

# ---------------------------------------------------------------- никакой
S["никакой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ни-</span>'
    '<span class="hd-gloss">KHÔNG MỘT … nào</span></div>'
    '<div class="hd-row"><span class="hd-piece">како́й</span>'
    '<span class="hd-gloss">nào (thẻ đã học)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Không một loại nào», đổi đuôi như како́й: <b>никака́я</b>, '
    '<b>никаки́х</b>.</div>'
    '<div class="hd-warn">Phủ định KÉP là bắt buộc, động từ vẫn phải có не/нет: <b>Я не '
    'ви́жу никако́й ра́зницы</b> = Tôi chẳng thấy khác gì cả · <b>Нет никаки́х пробле́м</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">Cùng ни-: <b>никто́</b> không ai · <b>ничего́</b> không gì · '
    '<b>никогда́</b> không bao giờ</div>'
)

# ------------------------------------------------------------------- итак
S["итак"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">и</span>'
    '<span class="hd-gloss">và</span></div>'
    '<div class="hd-row"><span class="hd-piece">так</span>'
    '<span class="hd-gloss">như thế (thẻ đã học)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Và như thế thì…» ⇒ vậy là, tóm lại — mở đầu câu chốt lại hoặc chuyển '
    'sang việc chính: <b>Ита́к, начнём</b> = Vậy thì, ta bắt đầu nào.</div>'
    '<div class="hd-warn">Viết liền <b>ита́к</b> = vậy là · viết rời <b>и так</b> = và cứ thế: '
    '<b>И так ка́ждый день</b> = Và ngày nào cũng thế.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>так</b> như thế · <b>тако́й</b> như thế (đi với danh từ) · '
    '<b>та́кже</b> ngoài ra</div>'
)

# ------------------------------------------------------------------ совсем
S["совсем"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со</span>'
    '<span class="hd-gloss">CÙNG VỚI</span></div>'
    '<div class="hd-row"><span class="hd-piece">всем</span>'
    '<span class="hd-gloss">cách 5 của <b>весь</b> — tất cả</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cùng với tất cả» ⇒ trọn vẹn, hoàn toàn: <b>совсе́м но́вый</b> = mới '
    'tinh.</div>'
    '<div class="hd-warn">Vị trí của не đổi nghĩa: <b>совсе́м не уста́л</b> = chẳng mệt CHÚT '
    'NÀO · <b>не совсе́м так</b> = KHÔNG HẲN là thế.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>весь</b> toàn bộ · <b>всё</b> mọi thứ · <b>все</b> mọi người</div>'
)

# ------------------------------------------------------------------ однако
S["однако"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">одн-</span>'
    '<span class="hd-gloss">MỘT — gốc của <b>оди́н</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ко</span>'
    '<span class="hd-gloss">phần còn lại, nay không mang nghĩa riêng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đằng nào cũng như một» ⇒ tuy nhiên, dù vậy. Trang trọng hơn <b>но</b>, '
    'và đứng được giữa câu, kẹp dấu phẩy: <b>Он, одна́ко, не пришёл</b> = Thế nhưng anh ta lại '
    'không đến.</div>'
    '<div class="hd-warn">⚠️ Mức tin: nối với оди́н là từ nguyên (giúp nhớ), không phải luật '
    'suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оди́н</b> một · <b>одна́жды</b> có lần · <b>одина́ковый</b> giống '
    'hệt nhau</div>'
)

# --------------------------------------------------------------- насколько
S["насколько"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">ĐẾN (mức)</span></div>'
    '<div class="hd-row"><span class="hd-piece">ско́лько</span>'
    '<span class="hd-gloss">bao nhiêu (thẻ đã học)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đến bao nhiêu» ⇒ đến mức nào: <b>Наско́лько э́то ва́жно?</b> = Điều '
    'đó quan trọng đến mức nào?</div>'
    '<div class="hd-warn">Cụm hằng ngày: <b>наско́лько я зна́ю</b> = theo như tôi biết.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ско́лько</b> bao nhiêu · <b>сто́лько</b> bấy nhiêu · '
    '<b>насто́лько</b> đến mức ấy (câu đáp của наско́лько)</div>'
)

# ---------------------------------------------------------------- какой-то
S["какой-то"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">како́й</span>'
    '<span class="hd-gloss">nào (thẻ đã học)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-то</span>'
    '<span class="hd-gloss">«… nào đó» — có thật, chỉ là không biết hoặc không nói ra</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Y như <b>кто́-то</b>: <b>Тебе́ звони́л како́й-то мужчи́на</b> = Có ông '
    'nào đó gọi cho cậu. Chỉ phần како́й đổi đuôi: <b>кака́я-то</b>, <b>каки́е-то</b>.</div>'
    '<div class="hd-warn">Nghĩa thứ hai «… thế nào ấy», hơi chê: <b>Он како́й-то стра́нный</b> = '
    'Anh ta lạ lạ thế nào ấy.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>како́й</b> nào · <b>кто́-то</b> ai đó · <b>что́-то</b> cái gì đó</div>'
)

# ------------------------------------------------------------------ что-то
S["что-то"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">что</span>'
    '<span class="hd-gloss">cái gì</span></div>'
    '<div class="hd-row"><span class="hd-piece">-то</span>'
    '<span class="hd-gloss">«… nào đó» — có thật, chỉ là không biết hoặc không nói ra</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một thứ CÓ THẬT mà chưa gọi tên: <b>Я что́-то слы́шал</b> = Tôi nghe thấy '
    'gì đó. Chỉ phần что biến cách: <b>чего́-то</b>, <b>о чём-то</b>. So với что́-нибудь: xem '
    'thẻ кто́-то.</div>'
    '<div class="hd-warn">Khẩu ngữ còn dùng nó như «sao đó, hơi hơi»: <b>Мне что́-то хо́лодно</b> = '
    'Không hiểu sao tôi thấy hơi lạnh.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>что</b> cái gì · <b>кто́-то</b> ai đó · <b>како́й-то</b> nào đó · '
    '<b>что́-нибудь</b> bất cứ thứ gì</div>'
)

# ---------------------------------------------------------------------- от
S["от"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Giới từ một âm, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Kéo cách 2, «rời xa một ĐIỂM, một NGƯỜI» — chiều ngược của <b>к</b>: '
    '<b>к врачу́</b> → <b>от врача́</b>. Đủ bộ ba đi–về: в→из, на→с, к→от. Từ người nào thì '
    'cũng là от: <b>пода́рок от ма́мы</b> = quà của mẹ.</div>'
    '<div class="hd-warn">Nguyên nhân của cảm xúc, cơ thể: <b>пла́кать от ра́дости</b> = khóc vì '
    'vui · <b>дрожа́ть от хо́лода</b> = run vì lạnh.</div>'
    '<div class="hd-warn">Thuốc «chống» bệnh: <b>лека́рство от ка́шля</b> = thuốc trị ho.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">Tiền tố от- «rời ra»: <b>отку́да</b> từ đâu · <b>откры́ть</b> mở (gỡ '
    'cái che ra) · <b>отойти́</b> bước ra xa</div>'
)

# ----------------------------------------------------------------- поэтому
S["поэтому"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по</span>'
    '<span class="hd-gloss">theo, do</span></div>'
    '<div class="hd-row"><span class="hd-piece">э́тому</span>'
    '<span class="hd-gloss">cách 3 của <b>э́то</b> — cái này</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Do cái này» ⇒ vì vậy: vế sau nó là KẾT QUẢ. Cùng khuôn với '
    '<b>почему́</b> (do cái gì?).</div>'
    '<div class="hd-warn">Đảo vế là đổi từ: <b>Я люблю́ ко́фе, поэ́тому пью его́</b> (sau = kết '
    'quả) · <b>Я пью ко́фе, потому́ что люблю́ его́</b> (sau = lý do).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>почему́</b> tại sao · <b>потому́</b> vì thế · <b>э́тот</b> này</div>'
)
