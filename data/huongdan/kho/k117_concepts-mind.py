# -*- coding: utf-8 -*-
"""k117 — concepts::mind: ý nghĩ, cảm xúc và sự cố gắng — 20 từ, soạn từng thẻ độc lập.

Chỗ cần nhất quán trong lô:
(1) gốc мн-/-мин- «nghĩ»: мне́ние (điều mình nghĩ) và воспомина́ние (по́мнить) — hai thẻ dẫn chiếu nhau;
(2) bộ ba «cố/thử»: so стара́ться ↔ пыта́ться ↔ про́бовать trải ở thẻ стара́ться, пыта́ться chỉ dẫn chiếu;
(3) gốc на-де- «đặt lên»: từ nguyên đặt ở наде́жда (kèm Mức tin), наде́яться dẫn chiếu;
(4) cặp thể отказа́ться/отка́зываться: cách chi phối viết ở thẻ hoàn thành, thẻ kia dẫn chiếu.
Họ hàng không vắng thẻ nào — cả 20 từ đều có từ cùng gốc thật.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    # bỏ 'giỏi' — va chạm хороший (k40, xong)
    "способный": "có năng lực, có năng khiếu",
    # bỏ ngoặc '(dứt khoát)'; 'bỏ' -> 'từ bỏ' (give up / renounce)
    "отказаться": "từ chối, từ bỏ",
    # bỏ ngoặc '(một lần)'
    "постараться": "cố gắng",
    # 'cố' trơn lẫn với стараться (cùng IPF + REF); 'thử' để lại cho пробовать (k122)
    "пытаться": "cố thử, tìm cách",
    "попытаться": "cố thử, tìm cách",
    # bỏ 'lo lắng' — va chạm волноваться (k98, xong) mà cả 4 badge đều trùng
    "беспокоиться": "lo, bận tâm",
}

# -------------------------------------------------------------------- тайна
S["тайна"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">тай-</span>'
    '<span class="hd-gloss">GIẤU — gốc của <b>таи́ть</b> che giấu</span></div>'
    '<div class="hd-row"><span class="hd-piece">-на</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Điều bị GIẤU đi ⇒ bí mật, cả điều bí ẩn: <b>та́йна приро́ды</b> '
    'bí ẩn của tự nhiên.</div>'
    '<div class="hd-warn">Giữ bí mật: <b>держа́ть в та́йне</b> (в + cách 6). Bí mật vặt '
    'thường ngày người ta cũng hay nói <b>секре́т</b> (từ mượn, như <i>secret</i>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>таи́ть</b> che giấu · <b>та́йный</b> bí mật, kín · '
    '<b>та́йно</b> lén, bí mật</div>'
)

# ------------------------------------------------------------------ желание
S["желание"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">жела-</span>'
    '<span class="hd-gloss">MONG — gốc của <b>жела́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ние</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>жела́ть</b> mong + <b>-ние</b> = sự mong muốn. Cùng khuôn với '
    '<b>мне́ние</b>, <b>настрое́ние</b>, <b>воспомина́ние</b> trong lô này: thấy '
    '<b>-ние</b> là biết danh từ giống trung.</div>'
    '<div class="hd-warn">Muốn LÀM gì: <b>жела́ние</b> + động từ nguyên thể — '
    '<b>У меня́ нет жела́ния спо́рить</b> (tôi chẳng muốn cãi).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>жела́ть</b> mong, chúc · <b>пожела́ть</b> chúc · '
    '<b>пожела́ние</b> lời chúc · <b>жела́тельно</b> nên, tốt hơn là</div>'
)

# ------------------------------------------------------------- воспоминание
S["воспоминание"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вос-</span>'
    '<span class="hd-gloss">LÊN, dậy lên (cùng tiền tố với вс-/вз-)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-помин-</span>'
    '<span class="hd-gloss">NHỚ — gốc của <b>по́мнить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-</span>'
    '<span class="hd-gloss">thân chưa hoàn thành, như <b>вспомина́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ние</span>'
    '<span class="hd-gloss">→ danh từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Điều đã qua được kéo dậy LÊN trong trí NHỚ ⇒ một ký ức cụ thể. '
    'Còn khả năng nhớ nói chung là <b>па́мять</b>.</div>'
    '<div class="hd-warn">Động từ viết <b>вс-</b>, danh từ viết <b>вос-</b>: '
    '<b>вспомина́ть</b> → <b>воспомина́ние</b>. Gõ thiếu chữ <b>о</b> là sai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>по́мнить</b> nhớ · <b>вспо́мнить</b> / <b>вспомина́ть</b> nhớ lại · '
    '<b>па́мять</b> trí nhớ · <b>мне́ние</b> ý kiến (gốc мн- «nghĩ»)</div>'
)

# ------------------------------------------------------------------- мнение
S["мнение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мн-</span>'
    '<span class="hd-gloss">NGHĨ, cho rằng — gốc cổ, nay còn trong <b>по́мнить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Điều mình NGHĨ» ⇒ ý kiến. <b>по́мнить</b> = giữ trong ý nghĩ ⇒ nhớ '
    '— cùng gốc, xem thẻ <b>воспомина́ние</b>.</div>'
    '<div class="hd-warn">Theo ý AI: <b>по мне́нию</b> + cách 2 — <b>по мне́нию враче́й</b> '
    'theo các bác sĩ. Của mình: <b>по моему́ мне́нию</b> = <b>по-мо́ему</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>по́мнить</b> nhớ · <b>воспомина́ние</b> ký ức · '
    '<b>мни́тельный</b> đa nghi, hay lo vớ vẩn</div>'
)

# ---------------------------------------------------------------- способный
S["способный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">спо́соб-</span>'
    '<span class="hd-gloss">CÁCH, phương cách (danh từ <b>спо́соб</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ный</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Có CÁCH làm được ⇒ có năng lực. Trọng âm dịch: <b>спо́соб</b> → '
    '<b>спосо́бный</b>. Dạng ngắn chen thêm <b>-е-</b>: <b>спосо́бен</b>, '
    '<b>спосо́бна</b>, <b>спосо́бны</b>.</div>'
    '<div class="hd-warn">Làm ĐƯỢC gì: <b>спосо́бен</b> + nguyên thể. Có khiếu VỀ gì: '
    'к + cách 3 — <b>спосо́бен к языка́м</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>спо́соб</b> cách, phương pháp · <b>спосо́бность</b> khả năng, '
    'năng khiếu · <b>неспосо́бный</b> không có khả năng</div>'
)

# ------------------------------------------------------------------- глупый
S["глупый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn <b>глуп-</b> + đuôi tính từ <b>-ый</b>. Không chẻ thêm được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trái nghĩa của <b>у́мный</b>. Trạng từ <b>глу́по</b> hay đứng làm '
    'câu bình luận: <b>Э́то глу́по!</b> — Thật ngớ ngẩn! Dạng ngắn: <b>глуп</b>, '
    '<b>глупа́</b> (giống cái nhấn đuôi), <b>глу́по</b>, <b>глу́пы</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>глу́пость</b> điều ngớ ngẩn, sự dại dột · '
    '<b>глупе́ц</b> kẻ ngốc</div>'
)

# --------------------------------------------------------------- отказаться
S["отказаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">RỜI XA, khỏi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-каз-</span>'
    '<span class="hd-gloss">NÓI, chỉ ra — gốc của <b>сказа́ть</b>, <b>показа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать-ся</span>'
    '<span class="hd-gloss">đuôi động từ + phản thân</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Nói để đẩy XA khỏi mình» ⇒ từ chối, từ bỏ. Chia y như '
    '<b>сказа́ть</b>: з → ж ở mọi ngôi, ngôi 1 số ít nhấn đuôi, còn lại nhấn gốc — '
    '<b>откажу́сь</b>, <b>отка́жешься</b>, <b>отка́жутся</b>.</div>'
    '<div class="hd-warn">Bỏ CÁI GÌ: от + cách 2 — <b>отказа́ться от сигаре́т</b>. '
    'Từ chối LÀM gì: + nguyên thể — <b>отказа́лся помо́чь</b>.</div>'
    '<div class="hd-warn">Bỏ <b>-ся</b> thành <b>отказа́ть</b> + cách 3 = từ chối AI '
    '(không cho): <b>Ему́ отказа́ли в ви́зе</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отка́з</b> sự từ chối · <b>сказа́ть</b> nói · '
    '<b>показа́ть</b> chỉ cho xem · <b>заказа́ть</b> đặt (món, hàng)</div>'
)

# ------------------------------------------------------------- отказываться
S["отказываться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">RỜI XA, khỏi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-каз-</span>'
    '<span class="hd-gloss">NÓI — gốc của <b>сказа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-</span>'
    '<span class="hd-gloss">dấu thể CHƯA hoàn thành</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть-ся</span>'
    '<span class="hd-gloss">đuôi động từ + phản thân</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chèn <b>-ыва-</b> vào <b>отказа́ться</b> là ra thể chưa hoàn thành, '
    'trọng âm lùi về <b>-ка́з-</b>. Chia đều: <b>отка́зываюсь</b>, <b>отка́зываешься</b>. '
    'Cách đòi y hệt cặp kia — xem thẻ <b>отказа́ться</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">Cùng khuôn <b>-ка́зывать</b>: <b>пока́зывать</b> chỉ cho xem · '
    '<b>расска́зывать</b> kể · <b>зака́зывать</b> đặt (món, hàng)</div>'
)

# ---------------------------------------------------------------- стараться
S["стараться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">стар-</span>'
    '<span class="hd-gloss">gốc — không suy được nghĩa từ mảnh, phải thuộc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать-ся</span>'
    '<span class="hd-gloss">đuôi động từ + phản thân</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dồn sức làm cho TỐT ⇒ cố gắng; nhấn vào CÔNG SỨC bỏ ra: '
    '<b>Я стара́юсь говори́ть по-ру́сски</b>. Chia đều: <b>стара́юсь</b>, '
    '<b>стара́ешься</b>. Cặp hoàn thành: <b>постара́ться</b>.</div>'
    '<div class="hd-warn">Ba từ «cố/thử»: <b>стара́ться</b> dồn sức làm cho tốt · '
    '<b>пыта́ться</b> cố làm việc khó, chưa chắc được · <b>про́бовать</b> thử xem ra sao '
    '(cả nếm món ăn).</div>'
    '<div class="hd-warn">⚠️ Mức tin: trông giống <b>ста́рый</b> «già» — chuyện hai từ cùng '
    'gốc còn tranh cãi, đừng dựa vào đó để nhớ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>стара́ние</b> sự cố gắng · <b>стара́тельный</b> chăm chỉ, '
    'cần mẫn</div>'
)

# -------------------------------------------------------------- постараться
S["постараться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tạo thể HOÀN THÀNH — không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">стара́ться</span>'
    '<span class="hd-gloss">cố gắng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một lần cố cho một việc cụ thể. Thể hoàn thành nên '
    '<b>постара́юсь</b> là TƯƠNG LAI: <b>Я постара́юсь прийти́</b> — tôi sẽ cố đến.</div>'
    '<div class="hd-warn"><b>Постара́юсь!</b> đứng một mình = «Tôi sẽ cố!» — câu đáp rất hay '
    'gặp khi được nhờ việc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>стара́ться</b> cố gắng · <b>стара́ние</b> sự cố gắng</div>'
)

# ---------------------------------------------------------------- пытаться
S["пытаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пыт-</span>'
    '<span class="hd-gloss">THỬ, dò — cùng gốc <b>о́пыт</b> (điều đã thử qua)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать-ся</span>'
    '<span class="hd-gloss">đuôi động từ + phản thân</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cố THỬ làm việc khó, chưa chắc thành — hay đi với kết cục hỏng: '
    '<b>Я пыта́лся позвони́ть, но…</b> Chia đều: <b>пыта́юсь</b>, <b>пыта́ешься</b>. '
    'Khác <b>стара́ться</b> / <b>про́бовать</b> thế nào: xem thẻ <b>стара́ться</b>.</div>'
    '<div class="hd-warn">Đừng rơi <b>-ся</b>: <b>пыта́ть</b> = TRA KHẢO, tra tấn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>попы́тка</b> lần thử · <b>о́пыт</b> kinh nghiệm, thí nghiệm · '
    '<b>испыта́ние</b> thử thách, cuộc thử nghiệm</div>'
)

# -------------------------------------------------------------- попытаться
S["попытаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tạo thể HOÀN THÀNH — không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">пыта́ться</span>'
    '<span class="hd-gloss">cố thử</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một lần thử cụ thể: <b>Попыта́юсь объясни́ть</b> — để tôi thử giải '
    'thích. Danh từ là <b>попы́тка</b>: trọng âm dời về <b>-пы́т-</b>.</div>'
    '<div class="hd-warn"><b>Попы́тка — не пы́тка</b>: «thử thì có mất gì» (nghĩa đen: thử '
    'đâu phải bị tra tấn) — câu cửa miệng chơi chữ đúng gốc <b>пыт-</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>попы́тка</b> lần thử · <b>пы́тка</b> sự tra tấn · '
    '<b>о́пыт</b> kinh nghiệm</div>'
)

# ------------------------------------------------------------------ надежда
S["надежда"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">LÊN, vào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-де-</span>'
    '<span class="hd-gloss">ĐẶT (gốc cổ)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-жда</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái — cùng khuôn <b>оде́жда</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Điều mình ĐẶT lòng LÊN ⇒ niềm hy vọng. Cùng khuôn '
    '<b>оде́жда</b> (cái đặt lên người = quần áo). Cũng là tên nữ phổ biến, gọi thân '
    '<b>На́дя</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: nghĩa «đặt» của <b>-де-</b> là từ nguyên học, không '
    'phải luật suy ra được — dùng làm móc nhớ, đừng suy rộng.</div>'
    '<div class="hd-warn">Cụm hay gặp: <b>луч наде́жды</b> tia hy vọng · '
    '<b>подаю́щий наде́жды</b> đầy hứa hẹn (nói về người trẻ).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>наде́яться</b> hy vọng · <b>надёжный</b> đáng tin cậy · '
    '<b>безнадёжный</b> vô vọng</div>'
)

# --------------------------------------------------------------- надеяться
S["надеяться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">LÊN, vào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-де-</span>'
    '<span class="hd-gloss">ĐẶT (gốc cổ — xem thẻ <b>наде́жда</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ять-ся</span>'
    '<span class="hd-gloss">đuôi động từ + phản thân</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đặt mình LÊN ai ⇒ trông cậy, hy vọng. Chia đều: '
    '<b>наде́юсь</b>, <b>наде́ешься</b>. <b>Наде́юсь!</b> đứng một mình = mong là vậy.</div>'
    '<div class="hd-warn">Trông cậy VÀO ai: на + cách 4 — <b>Я наде́юсь на тебя́</b>. '
    'Hy vọng RẰNG: <b>наде́юсь, что…</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>наде́жда</b> niềm hy vọng · <b>надёжный</b> đáng tin cậy</div>'
)

# --------------------------------------------------------------- настроение
S["настроение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">LÊN, vào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-стро-</span>'
    '<span class="hd-gloss">XẾP, dựng — gốc của <b>стро́ить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>настро́ить</b> = lên dây đàn, chỉnh cho đúng ⇒ '
    '<b>настрое́ние</b> = lòng mình đang «lên dây» ra sao ⇒ tâm trạng.</div>'
    '<div class="hd-warn">Tâm trạng tốt: <b>в хоро́шем настрое́нии</b> (в + cách 6) hoặc '
    '<b>у меня́ хоро́шее настрое́ние</b>. <b>Нет настрое́ния</b> = không có hứng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>стро́ить</b> xây dựng · <b>настро́ить</b> lên dây, chỉnh · '
    '<b>настро́йки</b> mục Cài đặt (điện thoại)</div>'
)

# ------------------------------------------------------------------ усталый
S["усталый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">уста́л-</span>'
    '<span class="hd-gloss">quá khứ của <b>уста́ть</b> «mệt»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">biến dạng quá khứ thành tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đã mệt» ⇒ mệt mỏi, dùng để TẢ: <b>уста́лый вид</b> dáng mệt mỏi, '
    '<b>уста́лые глаза́</b> đôi mắt mệt mỏi.</div>'
    '<div class="hd-warn">Nói «Tôi mệt» thì gần như luôn dùng ĐỘNG TỪ quá khứ: '
    '<b>Я уста́л</b> / <b>Я уста́ла</b> — không phải tính từ này.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уста́ть</b> / <b>устава́ть</b> mệt · <b>уста́лость</b> sự mệt mỏi</div>'
)

# ----------------------------------------------------------------- страшный
S["страшный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">страш-</span>'
    '<span class="hd-gloss">NỖI SỢ — <b>страх</b>, х → ш trước -н-</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ный</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gây ra nỗi sợ ⇒ đáng sợ; nói quá thành «khủng khiếp»: '
    '<b>стра́шный хо́лод</b> lạnh khủng khiếp. Dạng ngắn chen <b>-е-</b>: <b>стра́шен</b>; '
    'giống cái nhấn đuôi: <b>страшна́</b>.</div>'
    '<div class="hd-warn"><b>Мне стра́шно</b> = Tôi sợ (người sợ ở cách 3).</div>'
    '<div class="hd-warn"><b>Ничего́ стра́шного!</b> = Không sao đâu! — câu đáp khi ai '
    'xin lỗi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>страх</b> nỗi sợ · <b>стра́шно</b> đáng sợ; rất, kinh khủng</div>'
)

# ------------------------------------------------------------- неприятность
S["неприятность"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не-</span>'
    '<span class="hd-gloss">KHÔNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-прия́тн-</span>'
    '<span class="hd-gloss">DỄ CHỊU — thân của <b>прия́тный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ость</span>'
    '<span class="hd-gloss">→ danh từ trừu tượng, luôn giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Điều không dễ chịu» ⇒ chuyện không hay, rắc rối. Đuôi '
    '<b>-ость</b> gắn vào tính từ: <b>неприя́тный</b> → <b>неприя́тность</b>.</div>'
    '<div class="hd-warn">Hay dùng số nhiều: <b>У него́ неприя́тности</b> — anh ta đang gặp '
    'rắc rối.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>прия́тный</b> dễ chịu · <b>О́чень прия́тно!</b> rất hân hạnh · '
    '<b>неприя́тный</b> khó chịu</div>'
)

# ------------------------------------------------------------- беспокоиться
S["беспокоиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бес-</span>'
    '<span class="hd-gloss">KHÔNG — là <b>без-</b>, viết <b>бес-</b> trước phụ âm vô thanh</span></div>'
    '<div class="hd-row"><span class="hd-piece">-поко-</span>'
    '<span class="hd-gloss">YÊN — gốc của <b>поко́й</b>, <b>споко́йный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить-ся</span>'
    '<span class="hd-gloss">đuôi động từ + phản thân</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mất YÊN trong lòng ⇒ lo, bận tâm. Chia loại II: '
    '<b>беспоко́юсь</b>, <b>беспоко́ишься</b>. <b>Не беспоко́йтесь!</b> = Đừng lo!</div>'
    '<div class="hd-warn">Lo VỀ việc gì: о + cách 6; lo CHO ai: за + cách 4 — '
    '<b>беспоко́юсь за сы́на</b>.</div>'
    '<div class="hd-warn">Bỏ <b>-ся</b>: <b>беспоко́ить</b> = làm phiền — '
    '<b>Извини́те за беспоко́йство</b> (xin lỗi đã làm phiền).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поко́й</b> sự yên tĩnh · <b>споко́йный</b> bình tĩnh · '
    '<b>успоко́иться</b> bình tĩnh lại · <b>беспоко́йство</b> nỗi lo, sự phiền</div>'
)

# ------------------------------------------------------------------ бояться
S["бояться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn <b>бо-</b> «sợ» + <b>-ять-ся</b>; không có dạng bỏ '
    '<b>-ся</b>. Không chẻ thêm được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chia loại II, <b>-я-</b> rụng: <b>бою́сь</b>, <b>бои́шься</b>, '
    '<b>боя́тся</b>. Mệnh lệnh: <b>Не бо́йся!</b> — Đừng sợ!</div>'
    '<div class="hd-warn">Sợ CÁI GÌ: + cách 2, không phải cách 4 — <b>Я бою́сь соба́к</b>. '
    'Sợ LÀM gì: + nguyên thể. Lo CHO ai: за + cách 4.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>боя́знь</b> nỗi sợ · <b>боязли́вый</b> nhút nhát</div>'
)
