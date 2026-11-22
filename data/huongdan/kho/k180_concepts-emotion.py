# -*- coding: utf-8 -*-
"""k180 — concepts::emotion (lô trộn): cảm xúc, tính cách, vài động từ tâm trí.

Chỗ cần nhất quán trong lô:
(1) предполага́ть / предположи́ть / предположе́ние: пред- TRƯỚC + по-лаг-/по-лож- ĐẶT, khớp thẻ
    положи́ть, положе́ние [k155], предлага́ть/предложи́ть [k124]. Bẫy chung: thiếu по- là ra
    họ ĐỀ NGHỊ (предлага́ть, предложе́ние).
(2) сосредото́читься / сосредота́чиваться: со- + сред- GIỮA (khớp сре́дний [k40], середи́на).
    Mảnh -точ- ≈ то́чка chỉ ghi kèm Mức tin.
(3) открове́нный ← кров-/кры- CHE, khớp кры́ша [k118], откры́ть [k87] (ы ↔ о: откро́ю).
(4) любопы́тный ← люб- + пыт- THỬ, DÒ — khớp о́пыт [k120], пыта́ться [k117] (xem B).
(5) позо́р ← по- + зор- NHÌN (зре́ние [k162]) — Mức tin.
(6) мстить / отомсти́ть: ст → щ ở ngôi я (мщу, отомщу́).
(7) жа́лость, сме́лость, уве́ренность: khớp chẻ của сожале́ние [k57], сме́лый [k88], уве́ренный [k99].
Họ hàng cố ý vắng: không có (mọi từ trong lô đều có họ thật).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "предполагать": "cho rằng, giả định, phỏng đoán, dự định, đòi hỏi",  # thiếu intend/plan, presuppose/entail
    "любопытный": "tò mò, hiếu kỳ, thú vị, đáng chú ý",                # «thú vị đáng chú ý» dính liền -> tách bằng dấu phẩy
    "печальный": "buồn, buồn rầu, u sầu, đáng buồn",                  # va chạm грустный: thêm sorrowful/grievous; bỏ «thê lương» (văn chương)
}

# --------------------------------------------------------------------- предполагать
S["предполагать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пред-</span>'
    '<span class="hd-gloss">TRƯỚC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-по-лаг-</span>'
    '<span class="hd-gloss">ĐẶT — mặt CHT của <b>-лож-</b> trong <b>положи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">thể chưa hoàn thành, chia đều: <b>предполага́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">ĐẶT sẵn một điều ra TRƯỚC khi biết chắc ⇒ giả định, cho rằng — cùng hình ảnh với '
    'tiếng Anh <i>presuppose</i> (<i>pre-</i> trước, <i>pose</i> đặt). Câu hay gặp: <b>Предполага́ется, что…</b> = người ta cho rằng / '
    'dự kiến là… Cặp thể: <b>предположи́ть</b>.</div>'
    '<div class="hd-warn">Bỏ mảnh <b>по-</b> là sang họ khác: <b>предлага́ть</b> = ĐỀ NGHỊ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>предположи́ть</b> giả định (HT) · <b>предположе́ние</b> giả định, phỏng đoán · '
    '<b>положе́ние</b> vị trí, tình thế</div>'
)

# --------------------------------------------------------------------- предположить
S["предположить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пред-</span>'
    '<span class="hd-gloss">TRƯỚC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-по-лож-и-ть</span>'
    '<span class="hd-gloss">ĐẶT — chính là <b>положи́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thể HOÀN THÀNH của <b>предполага́ть</b>: <b>пред-</b> + <b>положи́ть</b> = «đặt ra '
    'trước» ⇒ giả định. Trọng âm dịch y như <b>положи́ть</b>: <b>я предположу́</b> nhưng '
    '<b>ты предполо́жишь</b>, <b>они́ предполо́жат</b>.</div>'
    '<div class="hd-warn"><b>Предполо́жим, что…</b> = Giả sử rằng… — câu mở đầu rất hay dùng.</div>'
    '<div class="hd-warn">Bỏ mảnh <b>по-</b> là sang họ khác: <b>предложи́ть</b> = ĐỀ NGHỊ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>предполага́ть</b> cho rằng (CHT) · <b>предположе́ние</b> giả định · '
    '<b>положи́ть</b> đặt</div>'
)

# --------------------------------------------------------------------- предположение
S["предположение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пред-</span>'
    '<span class="hd-gloss">TRƯỚC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-по-лож-</span>'
    '<span class="hd-gloss">ĐẶT — như <b>положи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ние</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>предположи́ть</b>: điều được đặt ra trước khi biết chắc ⇒ '
    'giả định, phỏng đoán. Cùng khuôn với <b>положе́ние</b>. Câu quen: '
    '<b>У меня́ есть предположе́ние.</b> = Tôi có một phỏng đoán.</div>'
    '<div class="hd-warn">Đừng lẫn <b>предложе́ние</b> = lời đề nghị, câu — chỉ thiếu đúng mảnh '
    '<b>по-</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>предположи́ть</b> giả định · <b>предполага́ть</b> cho rằng · '
    '<b>положе́ние</b> vị trí, tình thế</div>'
)

# --------------------------------------------------------------------- сосредоточиться
S["сосредоточиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">CÙNG, gom lại — như <i>con-</i> trong <i>concentrate</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-сред-оточ-</span>'
    '<span class="hd-gloss">TÂM ĐIỂM — <b>сред-</b> GIỮA như <b>сре́дний</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-ть-ся</span>'
    '<span class="hd-gloss">đuôi động từ + -ся = cho chính mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Gom bản thân về một tâm điểm» ⇒ tập trung — cùng hình ảnh với '
    '<i>con-centr-ate</i>. Tập trung VÀO: <b>на</b> + cách 6 — <b>сосредото́читься на рабо́те</b>. '
    'Thể HT; CHT là <b>сосредота́чиваться</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: <b>-оточ-</b> gợi <b>то́чка</b> (điểm) là từ nguyên, '
    'không phải luật suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сосредота́чиваться</b> tập trung (CHT) · <b>сосредото́ченный</b> chăm chú · '
    '<b>сре́дний</b> ở giữa · <b>середи́на</b> chính giữa</div>'
)

# --------------------------------------------------------------------- сосредотачиваться
S["сосредотачиваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-сред-от-</span>'
    '<span class="hd-gloss">gom về tâm điểm — xem <b>сосредото́читься</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ч-ива-</span>'
    '<span class="hd-gloss"><b>-ива-</b> tạo thể CHT, kéo <b>о</b> của <b>-оч-</b> thành <b>а</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть-ся</span>'
    '<span class="hd-gloss">đuôi động từ + -ся</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thể CHT của <b>сосредото́читься</b>: đang / thường xuyên tập trung. '
    '<b>о → а</b> khi thêm <b>-ива-</b> là luật lặp lại: <b>спроси́ть → спра́шивать</b>. '
    'Chia đều: <b>сосредота́чиваюсь</b>. Vẫn đi với <b>на</b> + cách 6.</div>'
    '<div class="hd-warn">Từ điển cũng ghi dạng <b>сосредото́чиваться</b> — hai cách viết, một từ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сосредото́читься</b> tập trung (HT) · <b>сре́дний</b> ở giữa · '
    '<b>середи́на</b> chính giữa</div>'
)

# --------------------------------------------------------------------- паника
S["паника"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: từ mượn, chính là tiếng Anh <i>panic</i> (gốc Hy Lạp, '
    'từ tên thần Pan — vị thần gây hoảng sợ bất chợt).</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa y như <i>panic</i>. Trọng âm dịch khi thêm hậu tố: '
    '<b>па́ника → пани́ческий</b>. Cụm hay dùng: <b>впасть в па́нику</b> = rơi vào hoảng loạn.</div>'
    '<div class="hd-warn"><b>Без па́ники!</b> = Đừng hoảng! (nghĩa đen «không hoảng loạn»).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пани́ческий</b> hoảng loạn (tính từ) · <b>паникова́ть</b> hoảng lên · '
    '<b>паникёр</b> kẻ hay hoảng</div>'
)

# --------------------------------------------------------------------- привычка
S["привычка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">TỚI, gắn vào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-выч-</span>'
    '<span class="hd-gloss">QUEN — chính <b>-вык-</b> của <b>привыка́ть</b>, <b>к → ч</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">→ danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái mình đã <b>привы́кнуть</b> (quen) tới ⇒ thói quen. Cách 2 số nhiều '
    'chen nguyên âm chạy: <b>привы́чек</b> (như <b>то́чка → то́чек</b>).</div>'
    '<div class="hd-warn"><b>по привы́чке</b> = theo thói quen · <b>войти́ в привы́чку</b> = '
    'thành thói quen.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>привыка́ть</b> quen với · <b>привы́кнуть</b> quen (HT) · '
    '<b>привы́чный</b> quen thuộc · <b>обы́чный</b> thường lệ</div>'
)

# --------------------------------------------------------------------- строгий
S["строгий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: <b>строг-</b> là gốc trơn. KHÔNG cùng họ với '
    '<b>стро́ить</b> (xây) — chỉ giống mặt chữ.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dạng ngắn: giống cái nhảy trọng âm ra đuôi — <b>строга́</b>; còn lại giữ gốc: '
    '<b>строг, стро́го, стро́ги</b>. So sánh hơn đổi <b>г → ж</b>: <b>стро́же</b> '
    '(như <b>друг → дру́жба</b>).</div>'
    '<div class="hd-warn"><b>стро́го запрещено́</b> = nghiêm cấm (biển báo).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>стро́го</b> nghiêm khắc, nghiêm ngặt · <b>стро́гость</b> sự nghiêm khắc</div>'
)

# --------------------------------------------------------------------- искренний
S["искренний"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: gốc cổ đã mờ, tiếng Nga hiện đại không còn từ nào để '
    'dựa vào.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi <b>-ний</b> là tính từ MỀM (như <b>си́ний</b>, <b>сре́дний</b>) ⇒ '
    '<b>и́скренняя</b>, <b>и́скреннее</b>. Dạng ngắn chen <b>е</b>: <b>и́скренен</b>. Trạng từ '
    'thường gặp là <b>и́скренне</b> (đuôi <b>-е</b>, vì gốc mềm).</div>'
    '<div class="hd-warn"><b>И́скренне ваш</b> = Trân trọng (cuối thư) — đúng như <i>Sincerely yours</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>и́скренне</b> chân thành (trạng từ) · <b>и́скренность</b> sự chân thành</div>'
)

# --------------------------------------------------------------------- откровенный
S["откровенный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">gỡ ra, rời khỏi — như <b>откры́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-кров-</span>'
    '<span class="hd-gloss">CHE — mặt kia của <b>-кры-</b> trong <b>кры́ша</b>, <b>откры́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-енн-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>откры́ть</b> là gỡ cái che khỏi cửa ⇒ mở; <b>открове́нный</b> là gỡ cái che '
    'khỏi lòng ⇒ thẳng thắn, không giấu. <b>ы ↔ о</b> đổi nhau y như <b>откры́ть → я откро́ю</b>. '
    'Dạng ngắn mất một <b>н</b>: <b>открове́нен</b>.</div>'
    '<div class="hd-warn"><b>открове́нно говоря́</b> = nói thật thì…, thú thật là…</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>откры́ть</b> mở · <b>откры́тый</b> cởi mở · <b>открове́нно</b> thẳng thắn · '
    '<b>кры́ша</b> mái nhà</div>'
)

# --------------------------------------------------------------------- любопытный
S["любопытный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">люб-о-</span>'
    '<span class="hd-gloss">THÍCH — như <b>люби́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-пыт-</span>'
    '<span class="hd-gloss">DÒ, THỬ — như <b>пыта́ться</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thích dò hỏi» ⇒ tò mò. Nói về NGƯỜI là tò mò; nói về VẬT là thú vị, đáng '
    'chú ý: <b>любопы́тный факт</b>. Trạng từ mở câu: <b>Любопы́тно, что…</b> = Thú vị là…</div>'
    '<div class="hd-warn">⚠️ Mức tin: ghép <b>люб-</b> + <b>пыт-</b> là từ nguyên, không phải luật '
    'suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>любопы́тство</b> sự tò mò · <b>люби́ть</b> yêu, thích · '
    '<b>пыта́ться</b> cố thử</div>'
)

# --------------------------------------------------------------------- печальный
S["печальный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">печа́ль-</span>'
    '<span class="hd-gloss">NỖI BUỒN — <b>печа́ль</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">danh từ → tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>печа́ль</b> + <b>-ный</b> = mang nỗi buồn — khuôn y như '
    '<b>гру́стный ← грусть</b>. Khác <b>гру́стный</b>: <b>печа́льный</b> nặng và trang trọng hơn, '
    'hay dùng cho SỰ VIỆC — <b>печа́льная но́вость</b> tin buồn, '
    '<b>печа́льные после́дствия</b> hậu quả đáng buồn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>печа́ль</b> nỗi buồn · <b>печа́льно</b> buồn, đáng buồn · '
    '<b>печа́литься</b> buồn rầu</div>'
)

# --------------------------------------------------------------------- позор
S["позор"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-зор</span>'
    '<span class="hd-gloss">NHÌN — cùng gốc <b>зре́ние</b> (thị lực)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc là «cảnh bị đem ra cho thiên hạ NHÌN» ⇒ bị bêu ra ⇒ nỗi nhục.</div>'
    '<div class="hd-warn"><b>Како́й позо́р!</b> = Nhục quá! / Thật đáng xấu hổ!</div>'
    '<div class="hd-warn">⚠️ Mức tin: nối <b>-зор</b> với <b>зре́ние</b> là từ nguyên, '
    'không phải luật suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>позо́рный</b> nhục nhã · <b>опозо́рить</b> làm nhục · '
    '<b>зре́ние</b> thị lực</div>'
)

# --------------------------------------------------------------------- беспокоить
S["беспокоить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бес-</span>'
    '<span class="hd-gloss">KHÔNG — <b>без-</b> thành <b>бес-</b> trước <b>п</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-поко́-</span>'
    '<span class="hd-gloss">SỰ YÊN — <b>поко́й</b>, như trong <b>споко́йный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-ть</span>'
    '<span class="hd-gloss">LÀM CHO</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm cho mất yên ⇒ làm lo, làm phiền. Người bị phiền ở cách 4: '
    '<b>Тебя́ что́-то беспоко́ит?</b> = Có gì làm em lo à? Thêm <b>-ся</b> là TỰ mình lo: '
    '<b>беспоко́иться</b>.</div>'
    '<div class="hd-warn"><b>Извини́те, что беспоко́ю</b> = Xin lỗi đã làm phiền (câu mở đầu khi hỏi, '
    'gọi điện).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>беспоко́иться</b> lo, bận tâm · <b>беспоко́йство</b> sự lo âu · '
    '<b>споко́йный</b> bình tĩnh · <b>успоко́ить</b> làm cho yên</div>'
)

# --------------------------------------------------------------------- мстить
S["мстить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мст-</span>'
    '<span class="hd-gloss">BÁO THÙ — chính là <b>месть</b>, rơi mất <b>е</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi động từ lớp chia 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trả thù AI → cách 3, VÌ cái gì → <b>за</b> + cách 4: '
    '<b>мстить врагу́ за отца́</b>. Ngôi <b>я</b> đổi <b>ст → щ</b>: <b>мщу</b>, nhưng '
    '<b>ты мсти́шь</b> (như <b>прости́ть → прощу́</b>). Thể HT: <b>отомсти́ть</b>.</div>'
    '<div class="hd-warn"><b>мсти́тель</b> = kẻ báo thù — phim «<b>Мсти́тели</b>» chính là <i>Avengers</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>месть</b> sự báo thù · <b>отомсти́ть</b> trả thù (HT) · '
    '<b>мсти́тель</b> kẻ báo thù</div>'
)

# --------------------------------------------------------------------- отомстить
S["отомстить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ото-</span>'
    '<span class="hd-gloss">tiền tố thể HT, không mang nghĩa riêng; <b>о</b> chen vào vì cụm '
    '<b>мст</b> khó đọc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мст-и-ть</span>'
    '<span class="hd-gloss">BÁO THÙ — chính là <b>мстить</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thể HT của <b>мстить</b>: trả thù xong một lần. Cách đòi giữ nguyên: AI → cách 3, '
    'VÌ gì → <b>за</b> + cách 4. Ngôi <b>я</b> đổi <b>ст → щ</b>: <b>я отомщу́</b>, '
    '<b>ты отомсти́шь</b>.</div>'
    '<div class="hd-warn"><b>Я тебе́ отомщу́!</b> = Tao sẽ trả thù mày!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мстить</b> trả thù (CHT) · <b>месть</b> sự báo thù · '
    '<b>мсти́тель</b> kẻ báo thù</div>'
)

# --------------------------------------------------------------------- жалость
S["жалость"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">жал-</span>'
    '<span class="hd-gloss">THƯƠNG XÓT, tiếc — như <b>жаль</b>, <b>сожале́ние</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ость</span>'
    '<span class="hd-gloss">→ danh từ trừu tượng, giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cảm giác <b>жаль</b> thành danh từ ⇒ lòng thương, sự thương hại: '
    '<b>из жа́лости</b> = vì thương hại.</div>'
    '<div class="hd-warn"><b>Кака́я жа́лость!</b> = Tiếc quá! — ở đây là «điều đáng tiếc», '
    'không phải thương ai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>жаль</b> tiếc · <b>жа́лко</b> đáng tiếc · <b>жале́ть</b> thương, tiếc · '
    '<b>сожале́ние</b> sự tiếc nuối · <b>пожа́луйста</b> làm ơn</div>'
)

# --------------------------------------------------------------------- смелость
S["смелость"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">смел-</span>'
    '<span class="hd-gloss">DÁM — <b>сме́лый</b> dũng cảm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ость</span>'
    '<span class="hd-gloss">→ danh từ trừu tượng, giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tính chất của người <b>сме́лый</b> ⇒ lòng dũng cảm. <b>-ость</b> biến mọi '
    'tính từ thành «tính chất ấy»: <b>сме́лый → сме́лость</b>.</div>'
    '<div class="hd-warn"><b>набра́ться сме́лости</b> = lấy hết can đảm (cách 2: «gom lấy một ít '
    'dũng cảm»).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сме́лый</b> dũng cảm · <b>сметь</b> dám · <b>сме́ло</b> mạnh dạn</div>'
)

# --------------------------------------------------------------------- уверенность
S["уверенность"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-вер-енн-</span>'
    '<span class="hd-gloss">ĐƯỢC LÀM CHO TIN — <b>уве́ренный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ость</span>'
    '<span class="hd-gloss">→ danh từ trừu tượng, giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>уве́ренный</b> + <b>-ость</b> ⇒ sự chắc chắn, sự tự tin. Chắc VÀO gì: '
    '<b>в</b> + cách 6 — <b>уве́ренность в побе́де</b> niềm tin chắc vào chiến thắng.</div>'
    '<div class="hd-warn"><b>уве́ренность в себе́</b> = sự tự tin (nghĩa đen «chắc về bản thân»).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уве́ренный</b> tự tin, chắc chắn · <b>ве́рить</b> tin · '
    '<b>уве́ренно</b> một cách tự tin</div>'
)

# --------------------------------------------------------------------- депрессия
S["депрессия"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga: từ mượn, chính là tiếng Anh <i>depression</i> '
    '(Latin <i>de-</i> XUỐNG + <i>press</i> ẤN ⇒ «bị đè xuống»).</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hai nghĩa y như tiếng Anh: tâm lý (trầm cảm) và kinh tế (suy thoái). '
    'Đang trầm cảm: <b>в</b> + cách 6 — <b>Он в депре́ссии.</b></div>'
    '<div class="hd-warn"><b>Вели́кая депре́ссия</b> = cuộc Đại suy thoái (1929).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>депресси́вный</b> trầm cảm, gây chán nản</div>'
)

# --------------------------------------------------------------------- происшествие
S["происшествие"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-ис-</span>'
    '<span class="hd-gloss">tiến RA KHỎI — <b>из</b> thành <b>ис</b> trước <b>ш</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ше-</span>'
    '<span class="hd-gloss">ĐI — như <b>шёл</b> (quá khứ của <b>идти́</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ствие</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>произойти́</b> (quá khứ <b>произошёл</b>): «cái đã xảy ra» ⇒ '
    'sự cố, vụ việc — thường là chuyện bất ngờ, không hay.</div>'
    '<div class="hd-warn"><b>доро́жно-тра́нспортное происше́ствие</b> (ДТП) = tai nạn giao thông.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>произойти́</b> xảy ra · <b>происходи́ть</b> diễn ra · '
    '<b>происхожде́ние</b> nguồn gốc</div>'
)

B = {
    "docbangmat": 110,
    "loitubat": 2,   # сосредотачиваться: các mảnh chẻ thiếu -от-, cộng lại không ra từ -> sửa
                     # предполагать: «ghép y hệt pre-sup-pose» nói quá (sup- ≠ по-) -> hạ thành «cùng hình ảnh»
    "nguonsai": 0,   # từ điển lô này không có chỗ sai phải bác; chỉ tách «thú vị đáng chú ý» dính liền
    "baolen": [
        "VA CHẠM KHÔNG GỠ ĐƯỢC TỪ LÔ NÀY: chiều thật là гру́стный [k98, đã nạp] = chỉ «buồn» ⊆ печа́льный "
        "(không phải ngược lại). V của печальный đã thêm «u sầu, đáng buồn» nhưng giữ «buồn» (nghĩa chính) "
        "⇒ đề «buồn» của гру́стный vẫn hai đáp án. Muốn tách phải sửa thẻ гру́стный (vd «buồn, buồn bã, "
        "rầu rĩ» nếu gloss của nó xác nhận) — ngoài lô, chờ user.",
        "PHẢN BIỆN bối cảnh luồng chính: «о́пыт KHÔNG cùng gốc любопы́тный» có vẻ sai. Vasmer/Wiktionary: "
        "любопы́тный = любо- + пыта́ть, о́пыт cũng ← пыта́ть; chính thẻ о́пыт [k120] và пыта́ться [k117] đã ghi "
        "«пыт- THỬ». Thẻ любопы́тный chẻ -пыт- = пыта́ться (kèm Mức tin) nhưng KHÔNG ghi о́пыт vào Họ hàng — "
        "luồng chính xem lại.",
        "Chỗ KHÔNG chắc (đều đã gắn ⚠️ Mức tin trên thẻ): -оточ- trong сосредото́читься ≈ то́чка; "
        "позо́р ← -зор- NHÌN (cùng зре́ние); люб- + пыт- trong любопы́тный.",
        "открове́нный: chẻ -кров- = -кры- CHE (откры́ть, кры́ша) — từ nguyên khá vững (Vasmer: từ "
        "открове́ние ← откры́ть), không gắn Mức tin vì luân phiên ы↔о thấy ngay trong откро́ю.",
        "V cần duyệt (3): предполагать thêm «dự định, đòi hỏi» (gloss intend/plan, presuppose/entail); "
        "любопытный tách «thú vị, đáng chú ý»; печальный «buồn, buồn rầu, u sầu, đáng buồn» (bỏ «thê lương»).",
    ],
}
