# -*- coding: utf-8 -*-
"""k86 — tu-moi: 21 từ user vừa thêm (phần lớn trạng từ/hư từ), KHÔNG cùng họ nhau.

Mỗi thẻ soạn độc lập, không khối hệ thống. Chỗ cần nhất quán:
(1) cặp давно́/неда́вно, ста́рший/мла́дший, отку́да/сюда́ (+ туда́ k49) viết khớp nhau;
(2) khớp khuôn đã có: за + чем «để làm cái gì» (k17 почему́), млад- là bản song sinh
    của молод- (k40), при- + род «cái sinh ra quanh ta» (k57), пол- NỬA (k84),
    бы́стро tốc độ / ско́ро thời điểm (k43).
"""

S = {}

# ---------------------------------------------------------------- вдруг
S["вдруг"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ theo nghĩa hiện đại được: hai mảnh <b>в</b> + '
    '<b>друг</b> đã dính lại từ thời cổ, nghĩa «bỗng nhiên» không suy ra từ «bạn» — '
    'học nguyên khối.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đứng đầu một việc xảy ra bất ngờ: <b>Вдруг пошёл дождь</b> = '
    'bỗng trời đổ mưa.</div>'
    '<div class="hd-warn"><b>А вдруг…?</b> = «nhỡ đâu…?», hỏi về khả năng chưa xảy ra: '
    '<b>А вдруг он не придёт?</b> = nhỡ anh ấy không đến thì sao?</div>'
)

# ---------------------------------------------------------------- давно
S["давно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">давн-</span>'
    '<span class="hd-gloss">XA XƯA, LÂU (như <b>да́вний</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́</span>'
    '<span class="hd-gloss">đuôi trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đi với quá khứ = đã lâu: <b>Э́то бы́ло давно́</b> = chuyện '
    'đó lâu rồi. Đi với HIỆN TẠI = việc bắt đầu từ lâu và VẪN CÒN: <b>Я давно́ живу́ '
    'здесь</b> = tôi sống ở đây lâu rồi. Tiếng Anh phải dùng <i>have been</i>, '
    'tiếng Nga chỉ cần thì hiện tại — y như tiếng Việt.</div>'
    '<div class="hd-warn"><b>Давно́ не ви́делись!</b> = Lâu rồi không gặp! — câu '
    'chào quen thuộc nhất của từ này.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>неда́вно</b> gần đây · <b>да́вний</b> lâu đời, từ xưa</div>'
)

# -------------------------------------------------------------- недавно
S["недавно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не-</span>'
    '<span class="hd-gloss">KHÔNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-да́вно</span>'
    '<span class="hd-gloss">thẻ <b>давно́</b> — đã lâu</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Không lâu» ⇒ gần đây, mới đây — nhìn về QUÁ KHỨ: '
    '<b>Я неда́вно прие́хал</b> = tôi mới đến. Trọng âm nhảy lên <b>-да́-</b>, khác '
    'với <b>давно́</b> nhấn cuối.</div>'
    '<div class="hd-warn">Đừng lẫn với <b>ско́ро</b> = sắp, nhìn về TƯƠNG LAI: '
    '<b>неда́вно</b> vừa mới xảy ra · <b>ско́ро</b> chưa xảy ra.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>давно́</b> đã lâu · <b>да́вний</b> lâu đời, từ xưa</div>'
)

# ---------------------------------------------------------------- скоро
S["скоро"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">скор-</span>'
    '<span class="hd-gloss">NHANH (như <b>ско́рый</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc là NHANH, nhưng trạng từ này nói về THỜI ĐIỂM: việc '
    'sẽ tới nhanh ⇒ sắp, chẳng mấy chốc. <b>Он ско́ро придёт</b> = anh ấy sắp đến. '
    'Nhanh về TỐC ĐỘ là <b>бы́стро</b>; sớm hơn giờ hẹn là <b>ра́но</b>.</div>'
    '<div class="hd-warn"><b>ско́рая по́мощь</b>, gọi tắt <b>ско́рая</b> = xe cấp '
    'cứu, nghĩa đen «cứu giúp nhanh» — chỗ gốc NHANH còn nguyên.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ско́рый</b> nhanh · <b>ско́рость</b> tốc độ · '
    '<b>скоре́е</b> nhanh lên; đúng hơn là</div>'
)

# ---------------------------------------------------------------- почти
S["почти"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Hư từ, không chẻ được — học nguyên khối.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đứng ngay TRƯỚC cái «gần đủ»: <b>почти́ всё</b> gần như tất '
    'cả · <b>почти́ два часа́</b> gần hai tiếng. Đứng trước động từ quá khứ thì '
    'thành «suýt»: <b>Я почти́ упа́л</b> = tôi suýt ngã.</div>'
    '<div class="hd-warn"><b>почти́ не…</b> = hầu như không: <b>Я почти́ не '
    'сплю</b> = tôi gần như không ngủ.</div>'
)

# ---------------------------------------------------------------- зачем
S["зачем"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за</span>'
    '<span class="hd-gloss">ĐỂ LẤY, VÌ (như <b>пойти́ за хле́бом</b> đi mua bánh mì)</span></div>'
    '<div class="hd-row"><span class="hd-piece">чем</span>'
    '<span class="hd-gloss">cách 5 của <b>что</b> — cái gì</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đi để lấy CÁI GÌ» ⇒ hỏi MỤC ĐÍCH, nhìn tới phía trước: '
    '<b>Заче́м ты пришёл?</b> = đến để làm gì? Hỏi NGUYÊN NHÂN (nhìn lùi về sau) '
    'là <b>почему́</b>.</div>'
    '<div class="hd-warn">Đáp đúng cặp: <b>Заче́м?</b> → <b>Что́бы…</b> (để…) · '
    '<b>Почему́?</b> → <b>Потому́ что…</b> (vì…).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">cùng khuôn giới từ + <b>что</b>: <b>почему́</b> vì sao · '
    '<b>отчего́</b> do đâu · <b>не́зачем</b> chẳng cần, chẳng để làm gì</div>'
)

# --------------------------------------------------------------- откуда
S["откуда"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">TỪ, rời khỏi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ку́да</span>'
    '<span class="hd-gloss"><b>куда́</b> — tới đâu</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bộ ba câu hỏi nơi chốn: <b>где</b> ở đâu · <b>куда́</b> '
    'tới đâu · <b>отку́да</b> từ đâu. Thêm <b>от-</b> vào câu trả lời cũng thế: '
    '<b>отсю́да</b> từ đây, <b>отту́да</b> từ đó.</div>'
    '<div class="hd-warn"><b>Отку́да ты?</b> = bạn từ đâu tới / quê đâu? Đáp bằng '
    '<b>из</b> + cách 2: <b>Я из Вьетна́ма</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>куда́</b> tới đâu · <b>отсю́да</b> từ đây · '
    '<b>отту́да</b> từ đó</div>'
)

# ----------------------------------------------------------------- сюда
S["сюда"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сю-</span>'
    '<span class="hd-gloss">NÀY — gốc cổ, còn sống trong <b>сего́дня</b> «của ngày này»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-да́</span>'
    '<span class="hd-gloss">đuôi chỉ HƯỚNG ĐI TỚI (như <b>туда́</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đi cặp với <b>туда́</b> tới đó. Tiếng Nga tách «ở đây» và '
    '«tới đây»: <b>здесь</b> là chỗ đứng yên, <b>сюда́</b> là chỗ đi tới.</div>'
    '<div class="hd-warn">Có chuyển động thì bắt buộc <b>сюда́</b>: <b>Иди́ сюда́!</b> '
    '= lại đây! — nói <b>иди́ здесь</b> là sai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отсю́да</b> từ đây · <b>туда́</b> tới đó · '
    '<b>сего́дня</b> hôm nay</div>'
)

# ---------------------------------------------------------------- никто
S["никто"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ни-</span>'
    '<span class="hd-gloss">KHÔNG MỘT — phủ định tuyệt đối</span></div>'
    '<div class="hd-row"><span class="hd-piece">-кто́</span>'
    '<span class="hd-gloss"><b>кто</b> — ai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Biến cách y như <b>кто</b>: <b>никого́</b>, <b>никому́</b>, '
    '<b>нике́м</b>.</div>'
    '<div class="hd-warn">Phủ định KÉP là bắt buộc — động từ vẫn giữ <b>не</b>: '
    '<b>Никто́ не пришёл</b> = không ai đến.</div>'
    '<div class="hd-warn">Có giới từ thì nó chen VÀO GIỮA <b>ни</b> và phần <b>кто</b>: '
    '<b>ни у кого́</b>, <b>ни с кем</b> — tách thành ba chữ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ничего́</b> không gì · <b>никогда́</b> không bao giờ · '
    '<b>нигде́</b> không ở đâu</div>'
)

# ----------------------------------------------------------------- даже
S["даже"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">да-</span>'
    '<span class="hd-gloss">hư từ «và, thêm nữa»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-же</span>'
    '<span class="hd-gloss">hư từ NHẤN MẠNH (như <b>ты же зна́ешь</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thêm cả cái này nữa, nhấn mạnh» ⇒ ngay cả. Đứng ngay TRƯỚC '
    'từ được nhấn: <b>Да́же он зна́ет</b> = ngay cả anh ấy cũng biết.</div>'
    '<div class="hd-warn"><b>да́же не</b> = thậm chí không: <b>Он да́же не '
    'позвони́л</b> = anh ấy thậm chí không gọi điện.</div>'
    '<div class="hd-warn">⚠️ Mức tin: chẻ <b>да</b> + <b>же</b> là từ nguyên, '
    'không phải luật suy ra được.</div>'
)

# ------------------------------------------------------------ известный
S["известный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">из-</span>'
    '<span class="hd-gloss">TỪ TRONG RA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вест-</span>'
    '<span class="hd-gloss">TIN, BIẾT (như <b>весть</b> tin tức)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Tin đã lan ra ngoài» ⇒ được biết tới, nổi tiếng. '
    'Cụm <b>стн</b> đọc nuốt chữ <b>т</b>. Dạng ngắn giống đực chèn thêm <b>е</b>: '
    '<b>изве́стен</b>, còn lại đều theo dạng dài: <b>изве́стна</b>, <b>изве́стно</b>.</div>'
    '<div class="hd-warn"><b>Как изве́стно</b> = như đã biết · <b>Мне изве́стно</b> = '
    'tôi được biết.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>изве́стие</b> tin tức · <b>неизве́стный</b> vô danh, '
    'chưa rõ · <b>весть</b> tin · <b>со́весть</b> lương tâm</div>'
)

# -------------------------------------------------------------- старший
S["старший"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">стар-</span>'
    '<span class="hd-gloss">GIÀ (thẻ <b>ста́рый</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ш-ий</span>'
    '<span class="hd-gloss">dấu bậc HƠN (như <b>лу́чший</b>, <b>мла́дший</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Già hơn» trong một nhóm ⇒ lớn tuổi hơn, cấp trên: '
    '<b>ста́рший брат</b> anh trai · <b>ста́ршая сестра́</b> chị gái. Đối lập: '
    '<b>мла́дший</b>.</div>'
    '<div class="hd-warn">So sánh «già hơn AI» thì không dùng từ này mà dùng '
    '<b>ста́рше</b>: <b>Он ста́рше меня́</b> = anh ấy hơn tuổi tôi. <b>ста́рший</b> '
    'đứng trước danh từ, <b>ста́рше</b> đi với «hơn AI» + cách 2.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ста́рый</b> già, cũ · <b>ста́рше</b> già hơn · '
    '<b>стари́к</b> ông lão · <b>ста́рость</b> tuổi già</div>'
)

# -------------------------------------------------------------- младший
S["младший"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">млад-</span>'
    '<span class="hd-gloss">TRẺ — bản Slav cổ của <b>молод-</b> (thẻ <b>молодо́й</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ш-ий</span>'
    '<span class="hd-gloss">dấu bậc HƠN (như <b>ста́рший</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Trẻ hơn» trong một nhóm ⇒ em, cấp dưới: <b>мла́дший брат</b> '
    'em trai · <b>мла́дшая сестра́</b> em gái. Tiếng Việt có sẵn chữ «em», tiếng Nga '
    'phải ghép từ này vào.</div>'
    '<div class="hd-warn">«Trẻ hơn AI» thì dùng <b>моло́же</b>: <b>Она́ моло́же '
    'меня́</b> = cô ấy ít tuổi hơn tôi — không dùng <b>мла́дший</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>молодо́й</b> trẻ · <b>моло́же</b> trẻ hơn · '
    '<b>младе́нец</b> trẻ sơ sinh</div>'
)

# ----------------------------------------------------------------- лицо
S["лицо"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">лиц-</span>'
    '<span class="hd-gloss">MẶT — trước <b>-н-</b> đổi <b>ц → ч</b> (<b>ли́чный</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́</span>'
    '<span class="hd-gloss">đuôi giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mặt đại diện cho cả người ⇒ trong giấy tờ <b>лицо́</b> là '
    '«một cá nhân»: <b>юриди́ческое лицо́</b> = pháp nhân. Số nhiều trọng âm lùi về '
    'đầu: <b>ли́ца</b>.</div>'
    '<div class="hd-warn">Trong ngữ pháp, <b>лицо́</b> là NGÔI: <b>пе́рвое лицо́</b> '
    'ngôi thứ nhất (я, мы) — sách ngữ pháp Nga dùng chữ này liên tục.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ли́чный</b> cá nhân, riêng · <b>ли́чность</b> nhân cách · '
    '<b>нали́чные</b> tiền mặt</div>'
)

# ------------------------------------------------------------- половина
S["половина"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пол-</span>'
    '<span class="hd-gloss">NỬA (thẻ <b>пол</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ови́н(а)</span>'
    '<span class="hd-gloss">hậu tố tạo danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>пол-</b> phải dính vào từ khác (<b>полго́да</b>); '
    '<b>полови́на</b> là chữ «nửa» đứng riêng, kéo theo cách 2: <b>полови́на '
    'я́блока</b> nửa quả táo.</div>'
    '<div class="hd-warn">Giờ giấc đếm tới giờ SẮP tới, y như <b>полпе́рвого</b>: '
    '<b>полови́на второ́го</b> = 1 giờ 30, không phải 2 giờ 30.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>полго́да</b> nửa năm · <b>полчаса́</b> nửa giờ · '
    '<b>по́лдень</b> giữa trưa · <b>полови́нка</b> một nửa nhỏ</div>'
)

# -------------------------------------------------------------- природа
S["природа"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">KÈM BÊN, ở cạnh</span></div>'
    '<div class="hd-row"><span class="hd-piece">-род-</span>'
    '<span class="hd-gloss">SINH RA, DÒNG GIỐNG (thẻ <b>род</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái được sinh ra QUANH ta ⇒ thiên nhiên. Cái sinh ra KÈM '
    'theo mình ⇒ bản chất, bẩm sinh. Một hình ảnh gánh cả hai nghĩa.</div>'
    '<div class="hd-warn"><b>на приро́де</b> = ra ngoài trời, về vùng quê (đi '
    'picnic) — dùng <b>на</b>, không dùng <b>в</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>приро́дный</b> tự nhiên, bẩm sinh · <b>род</b> dòng '
    'giống · <b>ро́дина</b> quê hương · <b>наро́д</b> nhân dân</div>'
)

# ---------------------------------------------------------------- наука
S["наука"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">cho ĐẦY, tới nơi tới chốn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ук-</span>'
    '<span class="hd-gloss">HỌC, DẠY — chính là <b>уч-</b> của <b>учи́ть</b> trước khi '
    '<b>к</b> hoá <b>ч</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cái được dạy cho tới nơi» ⇒ khoa học, môn học. Thêm '
    '<b>-н-</b> thì <b>к</b> lại hoá <b>ч</b>: <b>нау́чный</b> thuộc khoa học — '
    'cùng phép biến âm với <b>река́ → речно́й</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>нау́чный</b> khoa học · <b>учёный</b> nhà khoa học · '
    '<b>учи́ть</b> học, dạy · <b>научи́ть</b> dạy cho biết</div>'
)

# ----------------------------------------------------------- искусство
S["искусство"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ис-</span>'
    '<span class="hd-gloss">RA (dạng của <b>из-</b> trước <b>к</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-кус-</span>'
    '<span class="hd-gloss">THỬ, NẾM (như <b>вкус</b> vị)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ств(о)</span>'
    '<span class="hd-gloss">danh từ trừu tượng, giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tay nghề có được qua thử đi thử lại ⇒ tài khéo, rồi nghệ '
    'thuật. Nghĩa «tài khéo» vẫn dùng: <b>иску́сство гото́вить</b> = nghệ thuật nấu '
    'ăn. Làm bằng tài khéo chứ không mọc tự nhiên ⇒ <b>иску́сственный</b> nhân tạo.</div>'
    '<div class="hd-warn">Hai chữ <b>сс</b>: một của <b>-кус-</b>, một của '
    '<b>-ство</b> — viết một chữ <b>с</b> là sai chính tả.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>иску́сственный</b> nhân tạo · <b>иску́сный</b> khéo tay, '
    'lành nghề · <b>вкус</b> vị</div>'
)

# ----------------------------------------------------------------- река
S["река"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc Slav trơn, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trọng âm nhảy ngay trong số ít: <b>река́</b> nhưng cách 4 '
    '<b>ре́ку</b>, và số nhiều <b>ре́ки</b> — cùng kiểu với <b>цена́ → це́ну</b>.</div>'
    '<div class="hd-warn">Ở bên sông, trên sông = <b>на реке́</b> (<b>на</b> + cách 6), '
    'như <b>на мо́ре</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ре́чка</b> sông nhỏ · <b>речно́й</b> thuộc sông — '
    '<b>к → ч</b></div>'
)

# ----------------------------------------------------------------- цена
S["цена"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">цен-</span>'
    '<span class="hd-gloss">GIÁ, GIÁ TRỊ — gốc trơn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một gốc đi từ GIÁ tiền tới GIÁ TRỊ rồi tới ĐÁNH GIÁ — '
    'nên điểm số ở trường là <b>оце́нка</b>. Trọng âm nhảy ngay trong số ít: '
    'cách 4 <b>це́ну</b>, số nhiều <b>це́ны</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>це́нный</b> quý giá · <b>цени́ть</b> quý trọng · '
    '<b>оце́нка</b> điểm số, sự đánh giá</div>'
)

# --------------------------------------------------------------- тренер
S["тренер"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">трен-</span>'
    '<span class="hd-gloss">mượn tiếng Anh <i>train</i> — tập luyện</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ер</span>'
    '<span class="hd-gloss">NGƯỜI làm việc ấy = <i>-er</i> tiếng Anh</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>trainer</i>: huấn luyện viên thể thao, phòng gym. '
    'Trọng âm ở đầu: <b>тре́нер</b>. Thầy dạy chữ là <b>учи́тель</b>, không dùng từ này.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>трениро́вка</b> buổi tập · <b>тренирова́ться</b> tập '
    'luyện · <b>тренажёр</b> máy tập</div>'
)

V = {
    # Bỏ "nhanh" (trùng бы́стро), "sớm" (trùng ра́но), không dùng "sắp" (trùng сейча́с);
    # giữ các nghĩa soon/shortly/before long.
    "скоро": "chẳng mấy chốc, không lâu nữa, sớm thôi",
    # Bỏ "tại sao" (trùng почему́); gloss what for / for what purpose.
    "зачем": "để làm gì, nhằm mục đích gì",
    # "huấn luyện" là động từ, không phải nghĩa của danh từ.
    "тренер": "huấn luyện viên",
    # "anh, chị" là nghĩa của cụm старший брат/сестра, không phải của tính từ; gloss elder/eldest/senior.
    "старший": "lớn tuổi hơn, lớn tuổi nhất, cấp trên",
    # Khớp cặp với старший; gloss younger/youngest/junior.
    "младший": "nhỏ tuổi hơn, nhỏ tuổi nhất, cấp dưới",
}
