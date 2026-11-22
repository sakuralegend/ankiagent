# -*- coding: utf-8 -*-
"""k170 — concepts::mind: chờ đợi, nhận biết, nhìn xét, nghĩ ra, chịu đựng, thở dài.

Chỗ cần nhất quán trong lô:
(1) họ ждать: ожида́ние / неожи́данный — `жд-` gốc CHỜ như thẻ ждать; ожида́ть hiện gốc
    thành `-жид-`. Máy ghép да́нный = BÁO OAN, không dùng.
(2) họ знать: признава́ть / призна́ть / призна́ться / при́знак — `зна-` BIẾT, gốc của знать
    (đúng chữ thẻ знак). Bẫy đắt nhất: признаю́ (IMPF) ↔ призна́ю (PF) chỉ khác trọng âm.
(3) `-мотр-` NHÌN như thẻ смотре́ть: рассма́тривать / рассмотре́ть / предусма́тривать /
    предусмотре́ть; luật о → а trước `-ива-` giải thích `-сматр-`.
(4) `дум-` Ý NGHĨ như thẻ ду́мать: приду́мать / приду́мывать.
(5) `дох-/дых-/дух-` THỞ: вздохну́ть / вздыха́ть / духо́вный cùng một gốc với дыша́ть.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
# придумать / скучать / вздохнуть: ngoặc trên thẻ là máy tạo thẻ sinh ra (deck B2-pending,
# user chưa mở) — luồng chính chốt ngoại lệ, sẽ gỡ ngoặc trên thẻ trước khi nạp.
V = {
    "придумать": "nghĩ ra, bày ra, bịa ra",                           # bỏ «(được)»
    "скучать": "nhớ, mong nhớ, buồn chán",                            # bỏ «(ai)»; long for / be bored
    "вздохнуть": "thở dài, thở phào, hít một hơi",                    # bỏ «(một lần)»; take breath
    "ожидание": "sự chờ đợi, sự mong đợi, kỳ vọng",                  # expectation
    "намерение": "ý định, mục đích, dự định",                         # purpose / plan
    "заключение": "kết luận, phần kết, sự giam giữ, sự ký kết",       # ending / imprisonment / signing
    "духовный": "tinh thần, tâm linh, nội tâm, tôn giáo",            # inner / religious
    "признавать": "thừa nhận, công nhận, thú nhận",                   # confess / own up to
    "рассматривать": "ngắm kỹ, xem xét, coi là",                      # regard (as)
    "рассмотреть": "xem xét, nhìn rõ",                                # chỉ đổi «;» -> «,»
    "предусматривать": "lường trước, dự liệu, quy định",              # foresee / provide
    "предусмотреть": "lường trước, dự liệu, quy định",                # stipulate
    "придумывать": "nghĩ ra, bày ra, bịa ra",                         # make up / fabricate
    "способность": "khả năng, năng lực, năng khiếu",                  # va chạm возможность
    "сумасшедший": "điên, khùng, mất trí, người điên",                # insane / madman
    "вздыхать": "thở dài, thở phào, mong nhớ",                        # sigh of relief / pine for
    "терпеть": "chịu đựng, nhẫn nhịn, dung thứ, kiên nhẫn",           # va chạm переносить
    "неожиданный": "bất ngờ, đột ngột, không ngờ tới, gây ngạc nhiên",  # va chạm внезапный
    "признак": "dấu hiệu, triệu chứng, đặc điểm, đặc trưng",          # va chạm знак
}

# --------------------------------------------------------------------- ожидание
S["ожидание"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-жид-</span>'
    '<span class="hd-gloss">gốc CHỜ — chính là <b>жд-</b> của <b>ждать</b>, chen thêm и</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ание</span>'
    '<span class="hd-gloss">→ danh từ (từ động từ <b>ожида́ть</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>ожида́ть</b> chờ đợi, mong đợi ⇒ sự chờ đợi. Số nhiều '
    '<b>ожида́ния</b> là những kỳ vọng: <b>оправда́ть ожида́ния</b> đáp ứng kỳ vọng.</div>'
    '<div class="hd-warn"><b>зал ожида́ния</b> phòng chờ (ga, sân bay) · <b>в ожида́нии</b> + '
    'cách 2: trong lúc chờ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ждать</b> chờ · <b>ожида́ть</b> chờ đợi, mong đợi · '
    '<b>неожи́данный</b> bất ngờ · <b>подожда́ть</b> chờ một lát</div>'
)

# --------------------------------------------------------------------- намерение
S["намерение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">VÀO, nhắm vào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мер-</span>'
    '<span class="hd-gloss">ĐO — như <b>ме́ра</b>, <b>ме́рить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đo ngắm trước vào một đích ⇒ ý định: <b>с наме́рением</b> + nguyên thể '
    'với ý định làm gì.</div>'
    '<div class="hd-warn">«Tôi định…» trang trọng: dạng ngắn <b>наме́рен</b> + nguyên thể — '
    '<b>я наме́рен уйти́</b> tôi định đi. Trạng từ <b>наме́ренно</b> = cố ý.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ме́ра</b> mức độ, biện pháp · <b>ме́рить</b> đo · '
    '<b>намерева́ться</b> định làm · <b>наме́ренный</b> cố ý</div>'
)

# --------------------------------------------------------------------- заключение
S["заключение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">ĐÓNG LẠI, khép</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ключ-</span>'
    '<span class="hd-gloss">KHOÁ — gốc của <b>ключ</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ (từ <b>заключи́ть</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Khoá lại» cho ra cả ba nghĩa: khoá một lập luận ⇒ kết luận; khoá '
    'người vào ngục ⇒ sự giam giữ; khoá một thoả thuận ⇒ sự ký kết '
    '(<b>заключе́ние догово́ра</b>).</div>'
    '<div class="hd-warn"><b>в заключе́ние</b> để kết thúc, cuối cùng (mở phần kết bài nói) · '
    '<b>заключённый</b> tù nhân.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ключ</b> chìa khoá · <b>заключи́ть</b> kết luận, ký kết · '
    '<b>исключе́ние</b> ngoại lệ · <b>включа́ть</b> bật</div>'
)

# --------------------------------------------------------------------- духовный
S["духовный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дух-</span>'
    '<span class="hd-gloss">HƠI THỞ → TINH THẦN (danh từ <b>дух</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-овн-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hơi thở được coi là linh hồn — cùng lối nghĩ (không cùng gốc) với '
    'tiếng Anh <i>spirit</i>, vốn từ Latin «thở». Nên <b>духо́вный</b> = thuộc tinh thần, tâm '
    'linh, tôn giáo: <b>духо́вная жизнь</b> đời sống tinh thần. Dạng ngắn hiếm gặp, giống đực '
    'chèn -е-: <b>духо́вен</b>.</div>'
    '<div class="hd-warn">Dễ lẫn: <b>душе́вный</b> (từ <b>душа́</b>) = chân tình, ấm áp — '
    '<b>душе́вный челове́к</b> người tốt bụng. <b>духо́вный</b> nghiêng về trí tuệ, tôn giáo.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дух</b> tinh thần · <b>душа́</b> tâm hồn · <b>дыша́ть</b> thở · '
    '<b>во́здух</b> không khí · <b>духи́</b> nước hoa</div>'
)

# --------------------------------------------------------------------- признавать
S["признавать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">tiền tố, nghĩa ở đây mờ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-зна-</span>'
    '<span class="hd-gloss">BIẾT — gốc của <b>знать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва-ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp thể của <b>призна́ть</b>: nhận ra (BIẾT) điều gì là thật rồi chấp '
    'nhận nó ⇒ thừa nhận, công nhận.</div>'
    '<div class="hd-why"><b>-ва-</b> rụng ở hiện tại, trọng âm ra đuôi: <b>признаю́</b>, '
    '<b>признаёшь</b> — đúng khuôn <b>дава́ть → даю́</b>, <b>узнава́ть → узнаю́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>призна́ние</b> sự công nhận, lời thú nhận · <b>при́знак</b> dấu '
    'hiệu · <b>узнава́ть</b> nhận ra · <b>знать</b> biết</div>'
)

# --------------------------------------------------------------------- признать
S["признать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">tiền tố, nghĩa ở đây mờ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-зна-</span>'
    '<span class="hd-gloss">BIẾT — gốc của <b>знать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể; thể hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc là «nhận ra» — khẩu ngữ vẫn nói <b>я его́ не призна́л</b> tôi '
    'không nhận ra anh ta. Nhận ra điều gì là thật ⇒ thừa nhận: <b>призна́ть оши́бку</b>. Chia '
    'như <b>знать</b>: <b>призна́ю</b>, <b>призна́ешь</b>.</div>'
    '<div class="hd-warn">Chỉ trọng âm tách hai thể: <b>признаю́</b> tôi (đang) thừa nhận — '
    '<b>признава́ть</b> · <b>призна́ю</b> tôi sẽ thừa nhận — <b>призна́ть</b>.</div>'
    '<div class="hd-warn">Công nhận ai LÀ gì: + cách 4 + cách 5 — <b>суд призна́л его́ '
    'вино́вным</b> toà tuyên anh ta có tội.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>призна́ние</b> sự công nhận · <b>при́знак</b> dấu hiệu · '
    '<b>узна́ть</b> nhận ra · <b>знать</b> biết</div>'
)

# --------------------------------------------------------------------- признаться
S["признаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-зна-ть</span>'
    '<span class="hd-gloss">thừa nhận — <b>зна-</b> BIẾT, gốc của <b>знать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">về chính mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thừa nhận điều về chính mình ⇒ thú nhận, thú thật. Điều thú nhận đi '
    'với <b>в</b> + cách 6: <b>призна́ться в оши́бке</b>. Cặp thể: <b>признава́ться</b> '
    '(<b>признаю́сь</b>, <b>признаёшься</b>).</div>'
    '<div class="hd-warn"><b>призна́ться в любви́</b> tỏ tình · Đầu câu <b>Признаю́сь, …</b> = '
    'thú thật là…</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>призна́ние</b> lời thú nhận, lời tỏ tình · <b>призна́ть</b> thừa '
    'nhận · <b>знать</b> biết</div>'
)

# --------------------------------------------------------------------- признак
S["признак"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при́-</span>'
    '<span class="hd-gloss">tiền tố, mang trọng âm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-знак</span>'
    '<span class="hd-gloss">DẤU — <b>зна-</b> BIẾT, gốc của <b>знать</b>, như <b>знак</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nét lộ ra giúp nhận BIẾT một điều ⇒ dấu hiệu, triệu chứng, đặc điểm. '
    'Đi với cách 2: <b>при́знак боле́зни</b> triệu chứng bệnh, <b>при́знаки весны́</b> dấu hiệu '
    'mùa xuân.</div>'
    '<div class="hd-warn">Khác <b>знак</b>: <b>знак</b> thường là ký hiệu, biển, dấu do người '
    'tạo ra; <b>при́знак</b> là nét TỰ LỘ RA, nhờ nó đoán được điều khác.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>знак</b> dấu hiệu · <b>призна́ть</b> thừa nhận · '
    '<b>узна́ть</b> nhận ra · <b>знать</b> biết</div>'
)

# --------------------------------------------------------------------- рассматривать
S["рассматривать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рас-</span>'
    '<span class="hd-gloss">RA KHẮP, từng phần</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сматр-</span>'
    '<span class="hd-gloss">= <b>-смотр-</b> NHÌN (gốc <b>-мотр-</b> như <b>смотре́ть</b>), о → а</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhìn khắp mọi chỗ ⇒ ngắm kỹ, xem xét: <b>рассма́тривать вопро́с</b> xem '
    'xét vấn đề. Thêm <b>-ива-</b> thì gốc đổi о → а — luật lặp khắp nơi: '
    '<b>спроси́ть → спра́шивать</b>, <b>опозда́ть → опа́здывать</b>.</div>'
    '<div class="hd-warn"><b>рассма́тривать как</b> + cách 4 = coi như: <b>рассма́тривать э́то '
    'как оши́бку</b> coi đó là sai lầm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>смотре́ть</b> nhìn · <b>рассмотре́ть</b> xem xét, nhìn rõ · '
    '<b>осмотре́ть</b> xem quanh, khám · <b>предусма́тривать</b> lường trước</div>'
)

# --------------------------------------------------------------------- рассмотреть
S["рассмотреть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рас-</span>'
    '<span class="hd-gloss">RA KHẮP, từng phần</span></div>'
    '<div class="hd-row"><span class="hd-piece">-смотр-</span>'
    '<span class="hd-gloss">NHÌN (gốc <b>-мотр-</b> như <b>смотре́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-еть</span>'
    '<span class="hd-gloss">đuôi lớp chia 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp hoàn thành của <b>рассма́тривать</b>, hai nghĩa: xem xét xong '
    '(<b>рассмотре́ть заявле́ние</b> xét đơn) và nhìn RÕ được (<b>в темноте́ не рассмотре́л</b> '
    'trong tối không nhìn rõ). Trọng âm dịch y như <b>смотре́ть</b>: <b>рассмотрю́</b>, '
    '<b>рассмо́тришь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>смотре́ть</b> nhìn · <b>рассмотре́ние</b> sự xem xét · '
    '<b>пересмотре́ть</b> xem lại · <b>предусмотре́ть</b> lường trước</div>'
)

# --------------------------------------------------------------------- предусматривать
S["предусматривать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пред-</span>'
    '<span class="hd-gloss">TRƯỚC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-у-</span>'
    '<span class="hd-gloss">tiền tố thứ hai, không mang nghĩa riêng ở đây</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сматр-</span>'
    '<span class="hd-gloss">= <b>-смотр-</b> NHÌN, о → а như <b>рассма́тривать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhìn TRƯỚC ⇒ lường trước, dự liệu. Trong luật, hợp đồng: '
    '<b>зако́н предусма́тривает</b>… luật quy định… — văn bản đã «nhìn trước» trường hợp đó. '
    'Chia đều -аю: <b>предусма́триваю</b>, <b>предусма́триваешь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>предусмотре́ть</b> lường trước (HT) · <b>смотре́ть</b> nhìn · '
    '<b>предусмотри́тельный</b> biết lo xa · <b>рассма́тривать</b> xem xét</div>'
)

# --------------------------------------------------------------------- предусмотреть
S["предусмотреть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пред-</span>'
    '<span class="hd-gloss">TRƯỚC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-у-</span>'
    '<span class="hd-gloss">tiền tố thứ hai, không mang nghĩa riêng ở đây</span></div>'
    '<div class="hd-row"><span class="hd-piece">-смотр-</span>'
    '<span class="hd-gloss">NHÌN (gốc <b>-мотр-</b> như <b>смотре́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-еть</span>'
    '<span class="hd-gloss">đuôi lớp chia 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhìn TRƯỚC ⇒ lường trước: <b>всё предусмотре́ть</b> lường trước mọi '
    'thứ. Tiếng Anh có đúng hình ảnh này (không cùng gốc): <i>provide</i> ← Latin '
    '<i>pro-videre</i> «nhìn trước» — nên <b>предусмотре́ть</b> = <i>provide for</i>. Trọng âm '
    'dịch như <b>смотре́ть</b>: <b>предусмотрю́</b>, <b>предусмо́тришь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>предусма́тривать</b> lường trước (CHT) · <b>предусмотри́тельный</b> '
    'biết lo xa · <b>смотре́ть</b> nhìn · <b>рассмотре́ть</b> xem xét</div>'
)

# --------------------------------------------------------------------- придумать
S["придумать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">TỚI ĐÍCH — đạt được kết quả</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дум-</span>'
    '<span class="hd-gloss">Ý NGHĨ (như <b>ду́мать</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể; thể hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩ cho TỚI khi ra một thứ mới ⇒ nghĩ ra, bày ra, bịa ra: '
    '<b>приду́мать игру́</b> nghĩ ra trò chơi. Trọng âm đứng yên ở <b>-ду́-</b> như '
    '<b>ду́мать</b>.</div>'
    '<div class="hd-warn">Đừng lẫn với <b>поду́мать</b>: nghĩ một lát (chưa chắc ra gì). '
    '<b>Приду́мал!</b> = Nghĩ ra rồi!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ду́мать</b> nghĩ · <b>приду́мывать</b> nghĩ ra (CHT) · '
    '<b>вы́думать</b> bịa ra · <b>заду́маться</b> trầm ngâm</div>'
)

# --------------------------------------------------------------------- придумывать
S["придумывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-дум-</span>'
    '<span class="hd-gloss">nghĩ TỚI ĐÍCH — như <b>приду́мать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp thể của <b>приду́мать</b>, chia đều -аю: <b>приду́мываю</b>, '
    '<b>приду́мываешь</b>. Hay dùng cho việc bịa lặp đi lặp lại: <b>Он всё приду́мывает</b> '
    'anh ta toàn bịa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ду́мать</b> nghĩ · <b>приду́мать</b> nghĩ ra (HT) · '
    '<b>вы́думать</b> bịa ra · <b>заду́маться</b> trầm ngâm</div>'
)

# --------------------------------------------------------------------- способность
S["способность"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">спосо́бн-</span>'
    '<span class="hd-gloss">có năng lực (<b>спосо́бный</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ость</span>'
    '<span class="hd-gloss">→ danh từ giống cái chỉ tính chất</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tính chất của người <b>спосо́бный</b> ⇒ năng lực, năng khiếu. Trọng âm '
    'giữ ở <b>-со́-</b> như tính từ.</div>'
    '<div class="hd-warn">Khác <b>возмо́жность</b>: đó là điều CÓ THỂ xảy ra, cơ hội; '
    '<b>спосо́бность</b> là cái người/vật LÀM ĐƯỢC. Số nhiều = năng khiếu: '
    '<b>спосо́бности к языка́м</b> năng khiếu ngoại ngữ (к + cách 3).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>спо́соб</b> cách · <b>спосо́бный</b> có năng lực · '
    '<b>неспосо́бный</b> không có khả năng</div>'
)

# --------------------------------------------------------------------- сумасшедший
S["сумасшедший"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сума-</span>'
    '<span class="hd-gloss">= <b>с ума́</b> «ra khỏi trí óc» (<b>ум</b>, cách 2)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сше́дш-ий</span>'
    '<span class="hd-gloss">«đã đi ra» — phân từ quá khứ của <b>сойти́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cụm <b>сойти́ с ума́</b> phát điên (đi ra khỏi trí óc) dồn lại thành một '
    'tính từ ⇒ người đã «ra khỏi trí óc» = điên. Dùng luôn làm danh từ: <b>сумасше́дший</b> '
    'người điên.</div>'
    '<div class="hd-warn"><b>Ты с ума́ сошёл?</b> Mày điên à? · Khẩu ngữ phóng đại: '
    '<b>сумасше́дшие де́ньги</b> tiền nhiều khủng khiếp.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ум</b> trí óc · <b>у́мный</b> thông minh · <b>сойти́ с ума́</b> phát '
    'điên · <b>сумасше́ствие</b> sự điên rồ</div>'
)

# --------------------------------------------------------------------- вздохнуть
S["вздохнуть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вз-</span>'
    '<span class="hd-gloss">LÊN, bật lên (như <b>взлете́ть</b> cất cánh)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дох-</span>'
    '<span class="hd-gloss">THỞ — cùng gốc <b>дыша́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ну-ть</span>'
    '<span class="hd-gloss">MỘT LẦN</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một hơi thở bật lên ⇒ thở dài một cái, thở phào. Đuôi <b>-ну-</b> là '
    '«làm một cái» — chính nó tách khỏi cặp thể <b>вздыха́ть</b> (đang thở dài, thở dài nhiều '
    'lần).</div>'
    '<div class="hd-warn"><b>вздохну́ть с облегче́нием</b> thở phào nhẹ nhõm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вздох</b> tiếng thở dài · <b>дыша́ть</b> thở · <b>о́тдых</b> nghỉ ngơi '
    '(lấy lại hơi) · <b>во́здух</b> không khí</div>'
)

# --------------------------------------------------------------------- вздыхать
S["вздыхать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вз-</span>'
    '<span class="hd-gloss">LÊN, bật lên</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дых-</span>'
    '<span class="hd-gloss">THỞ — dạng khác của <b>-дох-</b> (như <b>дыша́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp thể của <b>вздохну́ть</b>: gốc đổi о → ы (<b>-дох-</b> → '
    '<b>-дых-</b>), chia đều: <b>вздыха́ю</b>, <b>вздыха́ешь</b>.</div>'
    '<div class="hd-warn"><b>вздыха́ть по</b> + cách 3 = thầm mong nhớ ai — cùng khuôn với '
    '<b>скуча́ть по</b>: <b>вздыха́ть по ней</b> thầm thương nhớ cô ấy.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вздох</b> tiếng thở dài · <b>дыша́ть</b> thở · <b>отдыха́ть</b> nghỉ '
    'ngơi · <b>во́здух</b> không khí</div>'
)

# --------------------------------------------------------------------- скучать
S["скучать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">скуч-</span>'
    '<span class="hd-gloss">= <b>скук-</b> nỗi chán, nỗi nhớ (<b>ску́ка</b>), к → ч</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi lớp chia 1</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một nỗi, hai nghĩa: chán (<b>скуча́ть на ле́кции</b> chán trong giờ giảng) '
    'và nhớ ai — thiếu người đó thì thấy trống, chán. Nói «tôi chán» thì '
    '<b>мне ску́чно</b> thông dụng hơn.</div>'
    '<div class="hd-warn">Nhớ AI: <b>по</b> + cách 3 — <b>я скуча́ю по тебе́</b> tôi nhớ bạn, '
    '<b>скуча́ть по до́му</b> nhớ nhà. Đã nhớ rồi: <b>я соску́чился</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ску́ка</b> nỗi chán · <b>ску́чный</b> chán · <b>ску́чно</b> chán quá · '
    '<b>соску́читься</b> nhớ (HT)</div>'
)

# --------------------------------------------------------------------- терпеть
S["терпеть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">терп-</span>'
    '<span class="hd-gloss">CHỊU ĐỰNG — gốc trơn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е-ть</span>'
    '<span class="hd-gloss">đuôi lớp chia 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ngôi «tôi» chêm л: <b>терплю́</b>, các ngôi khác trọng âm lùi: '
    '<b>те́рпишь</b>, <b>те́рпит</b> — như <b>люби́ть → люблю́</b>, <b>лю́бишь</b>. Cặp hoàn '
    'thành <b>потерпе́ть</b>: chịu một lúc, hoặc chịu thua (<b>потерпе́ть пораже́ние</b>).</div>'
    '<div class="hd-warn"><b>Терпе́ть не могу́</b> + cách 4 / nguyên thể = ghét cay ghét đắng '
    '(nghĩa đen: không chịu nổi): <b>Терпе́ть не могу́ ложь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>терпе́ние</b> sự kiên nhẫn · <b>терпели́вый</b> kiên nhẫn · '
    '<b>нетерпе́ние</b> sự nóng lòng · <b>потерпе́ть</b> chịu (HT)</div>'
)

# --------------------------------------------------------------------- ненависть
S["ненависть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ненави́д-</span>'
    '<span class="hd-gloss">như <b>ненави́деть</b> ghét: <b>не</b> + <b>вид-</b> «nhìn»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сть</span>'
    '<span class="hd-gloss">→ danh từ (д + т → ст, như <b>за́висть</b> ↔ <b>зави́довать</b>)</span></div>'
    '<div class="hd-warn">⚠️ Mức tin: nối với <b>ви́деть</b> («không muốn nhìn thấy») là từ '
    'nguyên, không phải luật suy ra được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>ненави́деть</b>, nhưng trọng âm nhảy lên đầu: '
    '<b>не́нависть</b>. Ghét AI/cái gì: <b>к</b> + cách 3 — <b>не́нависть к войне́</b> lòng căm '
    'ghét chiến tranh.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ненави́деть</b> ghét · <b>ненави́стный</b> đáng ghét · '
    '<b>за́висть</b> sự ghen tị · <b>ви́деть</b> thấy</div>'
)

# --------------------------------------------------------------------- неожиданный
S["неожиданный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не-</span>'
    '<span class="hd-gloss">KHÔNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ожи́да-</span>'
    '<span class="hd-gloss">CHỜ ĐỢI (<b>ожида́ть</b>; gốc <b>жд-</b> CHỜ của <b>ждать</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-нн-ый</span>'
    '<span class="hd-gloss">«được …» — đuôi phân từ bị động</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Không được chờ đợi» ⇒ bất ngờ: <b>неожи́данный гость</b> khách không '
    'báo trước. Trạng từ <b>неожи́данно</b> bất ngờ thay. Dạng ngắn giống đực rụng một н: '
    '<b>неожи́дан</b>; còn lại giữ -нн-: <b>неожи́данна</b>, <b>неожи́данны</b>.</div>'
    '<div class="hd-warn">Gần <b>внеза́пный</b> nhưng nhấn chỗ khác: <b>неожи́данный</b> = ngoài '
    'dự tính, không ai chờ; <b>внеза́пный</b> = xảy ra thình lình, trong tích tắc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ждать</b> chờ · <b>ожида́ть</b> chờ đợi · <b>ожида́ние</b> sự chờ '
    'đợi · <b>неожи́данно</b> bất ngờ thay</div>'
)

B = {
    "docbangmat": 118,
    "loitubat": 0,
    "nguonsai": 0,
    "baolen": [
        "Va chạm: CHƯA đo lại bằng do_va_cham với V mới (agent không đọc Anki). Hướng gỡ: неожи́данный +«không ngờ tới, gây ngạc nhiên» (unexpected/surprising) ↔ внеза́пный · терпе́ть +«nhẫn nhịn, dung thứ, kiên nhẫn» (tolerate/be patient) ↔ переноси́ть · при́знак +«triệu chứng, đặc điểm, đặc trưng» (symptom/feature) ↔ знак · спосо́бность +«năng lực, năng khiếu» (capacity/talent) ↔ возмо́жность. Cần luồng chính chạy `vacham` xác nhận.",
        "V viết cho придумать / скучать / вздохнуть theo ngoại lệ luồng chính (ngoặc do máy tạo thẻ sinh, không phải user) — soat có thể đỏ nếu thẻ còn ngoặc lúc nạp; luồng chính gỡ ngoặc trước.",
        "V cần duyệt: рассмотре́ть giữ «nhìn rõ» (đã có sẵn trên thẻ, nghĩa thật «make out») dù gloss chỉ ghi consider/examine; chỉ đổi «;» → «,». сумасше́дший +«người điên» (gloss madman). предусма́тривать và предусмотре́ть cùng đề «lường trước, dự liệu, quy định» — badge thể tách.",
        "Chỗ KHÔNG chắc: не́нависть ← не + вид- (đã để ô ⚠️ Mức tin) · наме́рение: на- + мер- «đo» theo từ nguyên наме́риться «nhắm», viết thành cách nhớ, không có ô mức tin · духо́вный ↔ spirit chỉ là cùng lối nghĩ, đã ghi rõ «không cùng gốc»; provide ← pro-videre ở предусмотре́ть cũng vậy.",
        "Họ дох-/дых-/дух- (вздохну́ть, вздыха́ть, духо́вный ↔ дыша́ть, во́здух, о́тдых, душа́, духи́) máy không quét ra, tôi tự nối — cùng gốc theo từ nguyên phổ biến.",
        "Không chép dạng bảng chia nào từ BAT THUONG nguyên văn; dữ liệu từ điển của lô này không thấy chỗ sai nên nguonsai = 0.",
    ],
}
