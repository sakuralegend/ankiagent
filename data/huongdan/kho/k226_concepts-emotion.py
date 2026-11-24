# -*- coding: utf-8 -*-
"""k226 — concepts::emotion: tính nết (kiên nhẫn, chu đáo, dịu dàng…) và cơn giận, nỗi ngại, sự xúc phạm.

Chỗ cần nhất quán trong lô:
(1) -лив- «có tính…»: терпели́вый, забо́тливый — khớp ве́жливый, счастли́вый.
(2) вздра́гивать / вздро́гнуть: вз- BỪNG LÊN (khớp взволнова́ть [k208]), дрог- = дрож- RUN (дрожа́ть [k187]).
(3) унижа́ть / уни́зить: у- LÀM CHO + низ-/ниж- THẤP — khớp униже́ние [k208].
(4) серди́ться / рассерди́ться: серд- TIM (се́рдце [k83]); рас- BÙNG LÊN (разозли́ться [k188]).
(5) оскорби́ть / оскорбля́ть: скорб- NỖI ĐAU BUỒN (KHÔNG dính ско́рый); обожа́ть: Бог (KHÔNG dính освобожда́ть).
(6) напряжённый: -пряг-/-пряж- BUỘC ÁCH — khớp спряже́ние [k51], спряга́ться [k54].
(7) стесня́ться: тесн- ÉP SÁT — khớp те́сный [k197].
Họ hàng không vắng ở thẻ nào.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "агрессивный": "hung hăng, hung dữ, hiếu chiến",                # «dữ» trơ là злой / ди́кий
    "порядочный": "đứng đắn, tử tế, lương thiện, kha khá",          # THIẾU considerable / fair-sized / quite a
    "романтик": "người lãng mạn, người theo trường phái lãng mạn",  # «người mộng mơ» là мечта́тель, gloss không có; Romanticist
    "лень": "sự lười biếng, tính lười nhác, sự lười",               # «lười biếng» trơ là tính từ лени́вый
    "вздрагивать": "giật mình, giật nảy người, rùng mình",          # «nảy người» đứng một mình cụt nghĩa
    "вздрогнуть": "giật mình, giật nảy người, rùng mình",           # như trên
    "унижать": "làm nhục, hạ nhục, hạ thấp",                        # «coi rẻ» là khinh (презира́ть), không phải humiliate
    "унизить": "làm nhục, hạ nhục, hạ thấp",                        # như trên; abase / belittle
    "оскорбить": "xúc phạm, lăng mạ",                               # RÚT «làm tổn thương» — đó là оби́деть
    "оскорблять": "xúc phạm, lăng mạ",                              # RÚT «làm nhục» — đó là унижа́ть
    "стесняться": "ngại, ngượng, rụt rè, e dè, mắc cỡ, xấu hổ",     # «cảm thấy không thoải mái» quá rộng; THIẾU ashamed
}

# --------------------------------------------------------------------- терпеливый
S["терпеливый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">терпе-</span>'
    '<span class="hd-gloss">CHỊU ĐỰNG — <b>терпе́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ли́в-ый</span>'
    '<span class="hd-gloss">→ tính từ «có tính…», như <b>счастли́вый</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Có tính chịu đựng được» ⇒ kiên nhẫn. Tiếng Anh cùng hình ảnh: <i>patient</i> từ Latin '
    '<i>pati</i> «chịu đựng». Giữ chữ <b>е</b> của <b>терпе́ть</b> trước <b>-лив-</b>. '
    'Kiên nhẫn VỚI ai → <b>с</b> + cách 5: <b>терпели́в с детьми́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>терпе́ть</b> chịu đựng · <b>терпе́ние</b> sự kiên nhẫn · '
    '<b>нетерпели́вый</b> nóng vội · <b>терпели́во</b> một cách kiên nhẫn</div>'
)

# --------------------------------------------------------------------- заботливый
S["заботливый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">забо́т-</span>'
    '<span class="hd-gloss">SỰ CHĂM LO — <b>забо́та</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-лив-ый</span>'
    '<span class="hd-gloss">→ tính từ «có tính…», như <b>ве́жливый</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Hay chăm lo» ⇒ chu đáo, ân cần với người khác: <b>забо́тливая мать</b> người mẹ chu đáo. '
    'Trọng âm đứng yên ở <b>забо́т-</b>.</div>'
    '<div class="hd-warn"><b>озабо́ченный</b> cũng từ <b>забо́та</b> nhưng ra nhánh «nỗi lo»: lo lắng, đăm chiêu '
    '— không phải chu đáo.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>забо́та</b> sự chăm lo, nỗi lo · <b>забо́титься</b> chăm sóc · '
    '<b>забо́тливо</b> ân cần (trạng từ) · <b>беззабо́тный</b> vô tư lự</div>'
)

# --------------------------------------------------------------------- ласковый
S["ласковый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ла́ск-</span>'
    '<span class="hd-gloss">SỰ ÂU YẾM — <b>ла́ска</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ов-ый</span>'
    '<span class="hd-gloss">đuôi danh từ → tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đầy âu yếm» ⇒ dịu dàng, trìu mến. Dịu dàng VỚI ai → <b>с</b> + cách 5: '
    '<b>Он ла́сков с детьми́.</b></div>'
    '<div class="hd-warn"><b>ла́сковый</b> là cách cư xử hướng tới người khác (lời nói, con mèo quấn người); '
    '<b>не́жный</b> còn tả cảm giác khi chạm: <b>не́жная ко́жа</b> làn da mềm mại.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ла́ска</b> sự âu yếm · <b>ласка́ть</b> vuốt ve · '
    '<b>ла́сково</b> một cách trìu mến</div>'
)

# --------------------------------------------------------------------- агрессивный
S["агрессивный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">агресс-</span>'
    '<span class="hd-gloss">= <i>aggress-</i>, gốc Latin «BƯỚC TỚI đánh»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́в-ный</span>'
    '<span class="hd-gloss">= đuôi <i>-ive</i> của từ quốc tế</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>aggressive</i>. Mảnh <b>-гресс-</b> «bước» cũng nằm trong <b>прогре́сс</b>. '
    'Dạng ngắn giống đực chen <b>е</b>: <b>агресси́вен</b>, còn lại đều: <b>агресси́вна</b>.</div>'
    '<div class="hd-warn">Tiếng Anh hai <i>g</i> hai <i>s</i>; tiếng Nga chỉ <b>MỘT г</b>, vẫn hai <b>с</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>агре́ссия</b> sự gây hấn · <b>агре́ссор</b> kẻ xâm lược · '
    '<b>агресси́вно</b> hung hăng (trạng từ) · <b>агресси́вность</b> tính hung hăng</div>'
)

# --------------------------------------------------------------------- напряжённый
S["напряжённый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không còn tách nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пряж-</span>'
    '<span class="hd-gloss">BUỘC ÁCH, kéo căng — như <b>спряже́ние</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ённый</span>'
    '<span class="hd-gloss">đuôi «đã bị…»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đã bị kéo căng» như dây buộc ách ⇒ căng thẳng; hay tả ngày, tình hình, sự im lặng: '
    '<b>напряжённый день</b>. Dạng ngắn giống đực còn <b>một н</b>: <b>напряжён</b>; các dạng kia giữ hai: '
    '<b>напряжённа</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: gốc «buộc ách» là từ nguyên, không phải luật suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>напряже́ние</b> sự căng thẳng; điện áp · <b>напряга́ть</b> căng, gồng (CHT) · '
    '<b>напряжённо</b> căng thẳng (trạng từ) · <b>спряже́ние</b> phép chia động từ</div>'
)

# --------------------------------------------------------------------- порядочный
S["порядочный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">поря́доч-</span>'
    '<span class="hd-gloss">TRẬT TỰ — <b>поря́док</b>, к → ч trước -н-</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi danh từ → tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đúng phép tắc» ⇒ đứng đắn, tử tế; rồi «cỡ ra trò» ⇒ kha khá. Tiếng Anh <i>decent</i> đi '
    'đúng hai nghĩa ấy: <b>поря́дочный челове́к</b> người tử tế · <b>поря́дочная су́мма</b> món tiền kha khá. '
    'Dạng ngắn chen <b>е</b>: <b>поря́дочен</b>, <b>поря́дочна</b>.</div>'
    '<div class="hd-warn">KHÔNG phải «ngăn nắp», dù <b>поря́док</b> là sự ngăn nắp. Người ngăn nắp là '
    '<b>аккура́тный</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поря́док</b> trật tự · <b>поря́дочность</b> sự đứng đắn · '
    '<b>непоря́дочный</b> không đàng hoàng · <b>беспоря́док</b> sự lộn xộn</div>'
)

# --------------------------------------------------------------------- романтик
S["романтик"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рома́нт-</span>'
    '<span class="hd-gloss">= <i>romant-</i>, cùng nhà với <b>рома́н</b> tiểu thuyết, chuyện tình</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ик</span>'
    '<span class="hd-gloss">NGƯỜI (giống đực)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người sống như trong tiểu thuyết ⇒ người lãng mạn. Nói về nữ cũng được: '
    '<b>Она́ рома́нтик.</b></div>'
    '<div class="hd-warn">Thêm <b>-а</b> thành chữ khác: <b>рома́нтика</b> (giống cái) = chất lãng mạn. '
    'Trùng mặt chữ với cách 2 và 4 của <b>рома́нтик</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рома́н</b> tiểu thuyết · <b>рома́нтика</b> chất lãng mạn · '
    '<b>романти́ческий</b> thuộc lãng mạn · <b>романти́чный</b> lãng mạn</div>'
)

# --------------------------------------------------------------------- лень
S["лень"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn Slav, không chẻ được. Giống cái kết bằng <b>-ь</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chữ <b>е</b> đứng yên khi biến cách — <b>ле́ни</b>, <b>ле́нью</b> — không rụng như '
    '<b>день → дня</b>. Không có số nhiều.</div>'
    '<div class="hd-warn">Dùng nhiều nhất là khuôn <b>người ở cách 3 + лень + nguyên thể</b>: '
    '<b>Мне лень встава́ть</b> = tôi lười dậy. Quá khứ lấy <b>бы́ло</b>: <b>Мне бы́ло лень.</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лени́вый</b> lười · <b>лени́ться</b> lười (động từ) · '
    '<b>лентя́й</b> kẻ lười · <b>лени́во</b> uể oải</div>'
)

# --------------------------------------------------------------------- вздрагивать
S["вздрагивать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вз-</span>'
    '<span class="hd-gloss">BỪNG LÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дра́г-</span>'
    '<span class="hd-gloss">RUN — <b>дрож-</b> của <b>дрожа́ть</b> (г/ж), о → а</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ть</span>'
    '<span class="hd-gloss">đuôi kéo dài, lặp lại → chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giật mình hết lần này đến lần khác. <b>-ива-</b> đẩy <b>о</b> thành <b>а</b> có trọng âm, '
    'y như <b>спроси́ть → спра́шивать</b>. Chia đều: <b>вздра́гиваю</b>.</div>'
    '<div class="hd-warn">Giật mình VÌ gì → <b>от</b> + cách 2: <b>вздра́гивать от шу́ма</b> = giật mình vì tiếng ồn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вздро́гнуть</b> (HT) · <b>дрожа́ть</b> run · <b>дрожь</b> cơn run</div>'
)

# --------------------------------------------------------------------- вздрогнуть
S["вздрогнуть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вз-</span>'
    '<span class="hd-gloss">BỪNG LÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дро́г-</span>'
    '<span class="hd-gloss">RUN — <b>дрожа́ть</b> (г/ж)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ну-ть</span>'
    '<span class="hd-gloss">MỘT LẦN, bật ra một cái → hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Bật run lên một cái» ⇒ giật mình. Cùng khuôn một-cái với <b>крича́ть → кри́кнуть</b>. '
    'Quá khứ GIỮ <b>-ну-</b>: <b>вздро́гнул</b>, <b>вздро́гнула</b> (khác <b>привы́кнуть → привы́к</b>). '
    'Giật mình vì gì: <b>от</b> + cách 2.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вздра́гивать</b> (CHT) · <b>дрожа́ть</b> run · <b>дрожь</b> cơn run</div>'
)

# --------------------------------------------------------------------- унижать
S["унижать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">LÀM CHO thành — như trong <b>увели́чить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ниж-</span>'
    '<span class="hd-gloss">THẤP — <b>ни́зкий</b>, з → ж như <b>ни́же</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́-ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Làm cho ai thấp xuống» ⇒ làm nhục. Chữ <b>ж</b> có ở MỌI ngôi, chia đều lớp 1: '
    '<b>унижа́ю, унижа́ешь</b>. Người bị hạ nhục ở cách 4: <b>Не унижа́й бра́та!</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уни́зить</b> (HT) · <b>униже́ние</b> sự hạ nhục · <b>унижа́ться</b> tự hạ mình · '
    '<b>ни́зкий</b> thấp</div>'
)

# --------------------------------------------------------------------- унизить
S["унизить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">LÀM CHO thành — như trong <b>увели́чить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ни́з-</span>'
    '<span class="hd-gloss">THẤP — <b>ни́зкий</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Làm cho thấp xuống» ⇒ hạ nhục; tiếng Anh cùng hình ảnh: <i>humiliate</i> từ Latin '
    '<i>humilis</i> «thấp». Chỉ ngôi «tôi» đổi <b>з → ж</b>: <b>уни́жу</b>, rồi <b>уни́зишь</b>, <b>уни́зит</b>.</div>'
    '<div class="hd-warn"><b>уни́зить</b> là hạ thấp phẩm giá một người; <b>оскорби́ть</b> là nói hay làm điều xúc phạm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>унижа́ть</b> (CHT) · <b>униже́ние</b> sự hạ nhục · <b>унизи́тельный</b> nhục nhã · '
    '<b>пони́зить</b> hạ xuống</div>'
)

# --------------------------------------------------------------------- обожать
S["обожать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">LÀM THÀNH, coi như</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бож-</span>'
    '<span class="hd-gloss">CHÚA — <b>Бог</b>, г → ж như <b>Бо́же мой!</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́-ть</span>'
    '<span class="hd-gloss">đuôi động từ lớp 1</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Coi như Chúa» ⇒ tôn thờ; nay thường chỉ là mê, cực thích — y như <i>adore</i> từ Latin '
    '<i>adorare</i> «thờ lạy». Chỉ có thể chưa hoàn thành; chia đều: <b>обожа́ю, обожа́ешь</b>.</div>'
    '<div class="hd-warn">+ cách 4 hoặc nguyên thể: <b>Обожа́ю ко́фе</b> · <b>Обожа́ю гото́вить</b>. Đã mạnh sẵn, '
    'không cần thêm <b>о́чень</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>Бог</b> Chúa · <b>боже́ственный</b> thần thánh · <b>обожа́ние</b> sự sùng bái · '
    '<b>обожа́тель</b> người hâm mộ</div>'
)

# --------------------------------------------------------------------- оскорбить
S["оскорбить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">LÀM CHO</span></div>'
    '<div class="hd-row"><span class="hd-piece">-скорб-</span>'
    '<span class="hd-gloss">NỖI ĐAU BUỒN — <b>скорбь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Làm cho đau buồn» ⇒ xúc phạm. Chỉ ngôi «tôi» chêm <b>л</b>: <b>оскорблю́</b>, rồi '
    '<b>оскорби́шь</b>. Người bị xúc phạm ở cách 4, bằng gì ở cách 5: <b>оскорби́ть дру́га шу́ткой</b>.</div>'
    '<div class="hd-warn">Nặng hơn <b>оби́деть</b>: <b>оби́деть</b> là làm ai tủi, có khi vô ý; <b>оскорби́ть</b> '
    'là chạm tới danh dự.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оскорбля́ть</b> (CHT) · <b>оскорбле́ние</b> lời xúc phạm · '
    '<b>оскорби́тельный</b> xúc phạm · <b>скорбь</b> nỗi đau buồn</div>'
)

# --------------------------------------------------------------------- оскорблять
S["оскорблять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-скорбл-</span>'
    '<span class="hd-gloss">gốc <b>скорбь</b> NỖI ĐAU BUỒN, như <b>оскорби́ть</b>, chêm <b>л</b> sau б</span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́-ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Làm cho đau buồn» ⇒ xúc phạm. Chữ <b>л</b> chỉ lộ ở ngôi «tôi» của <b>оскорби́ть</b> thì '
    'ở đây có ở MỌI ngôi, lớp 1: <b>оскорбля́ю, оскорбля́ешь</b> — cùng khuôn <b>влюби́ться → влюбля́ться</b>. '
    'Người bị xúc phạm ở cách 4.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оскорби́ть</b> (HT) · <b>оскорбле́ние</b> lời xúc phạm · '
    '<b>оскорбля́ться</b> tự ái, thấy bị xúc phạm</div>'
)

# --------------------------------------------------------------------- рассердиться
S["рассердиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рас-</span>'
    '<span class="hd-gloss">BÙNG LÊN tới mức — như <b>разозли́ться</b> (з → с trước с)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-серд-</span>'
    '<span class="hd-gloss">TIM, cơn giận — <b>се́рдце</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть-ся</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai, phản thân</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cơn giận bùng lên tới nơi ⇒ nổi giận. Viết <b>hai с</b>: một của <b>рас-</b>, một của '
    '<b>серд-</b>. Ngôi «tôi» đổi <b>д → ж</b> và nhấn đuôi: <b>рассержу́сь</b>; từ ngôi «bạn» trọng âm lùi: '
    '<b>рассе́рдишься</b>.</div>'
    '<div class="hd-warn">Giận AI → <b>на</b> + cách 4: <b>Она́ рассерди́лась на му́жа.</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>серди́ться</b> đang giận (CHT) · <b>серди́тый</b> cáu, giận · '
    '<b>рассерди́ть</b> chọc giận · <b>се́рдце</b> trái tim</div>'
)

# --------------------------------------------------------------------- сердиться
S["сердиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">серд-</span>'
    '<span class="hd-gloss">TIM — <b>се́рдце</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть-ся</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai, phản thân</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Tim nổi lên» ⇒ giận, cáu. Ngôi «tôi» đổi <b>д → ж</b> và nhấn đuôi: <b>сержу́сь</b>; từ ngôi '
    '«bạn» trọng âm lùi về gốc: <b>се́рдишься</b>, <b>се́рдится</b>.</div>'
    '<div class="hd-warn">Giận AI → <b>на</b> + cách 4: <b>Не серди́сь на меня́!</b> = Đừng giận tớ! '
    'Giận VÌ chuyện gì → <b>из-за</b> + cách 2.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рассерди́ться</b> nổi giận (HT) · <b>серди́тый</b> cáu, giận · '
    '<b>серди́то</b> giận dữ (trạng từ) · <b>се́рдце</b> trái tim</div>'
)

# --------------------------------------------------------------------- стесняться
S["стесняться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">DỒN LẠI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тесн-</span>'
    '<span class="hd-gloss">ÉP SÁT, chật — <b>те́сный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́ть-ся</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành, quay về CHÍNH MÌNH</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Tự thấy mình bị bó chật» ⇒ ngại, ngượng. Chia đều lớp 1: <b>стесня́юсь, стесня́ешься</b>. '
    '<b>Не стесня́йтесь!</b> = Cứ tự nhiên!</div>'
    '<div class="hd-warn">Ngại AI/CÁI GÌ → <b>cách 2</b>, không giới từ, như <b>боя́ться</b>: '
    '<b>стесня́ться своего́ акце́нта</b>. Ngại LÀM gì → nguyên thể: <b>стесня́юсь спроси́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>постесня́ться</b> (HT) · <b>стесни́тельный</b> hay ngại · '
    '<b>те́сный</b> chật · <b>теснота́</b> sự chật chội</div>'
)

B = {
    "docbangmat": 113,
    "loitubat": 3,   # обожать: viết «không thêm о́чень» như luật cấm — nói quá -> «không cần thêm»
                     # напряжённый: khai на- là «tiền tố thể hoàn thành» (напряга́ть CHT cũng mang на-) -> «không còn tách nghĩa riêng»
                     # лень: viết «giống cái DÙ kết bằng -ь» (-ь giống cái là thường) -> bỏ «dù»
    "nguonsai": 0,   # không bác dòng từ điển nào; nghĩa Việt sửa nằm hết ở V
    "baolen": [
        "Va chạm оскорби́ть ⊇ оби́деть [k136]: ĐÃ GỠ phía lô này — RÚT «làm tổn thương»; còn {xúc phạm, lăng mạ} ↔ {làm tổn thương, xúc phạm}, chỉ chung «xúc phạm» (cả обижа́ть ↔ оскорбля́ть). Chưa chạy lại vacham với V mới (không đọc Anki).",
        "V cần duyệt (11 thẻ): агрессивный (dữ -> hung dữ) · порядочный (THÊM kha khá) · романтик (BỎ người mộng mơ, nhà lãng mạn -> người theo trường phái lãng mạn) · лень (lười biếng trơ -> sự lười biếng) · вздрагивать, вздрогнуть (nảy người -> giật nảy người) · унижать, унизить (BỎ coi rẻ; cùng dãy làm nhục, hạ nhục, hạ thấp) · оскорбить, оскорблять (cùng dãy xúc phạm, lăng mạ) · стесняться (BỎ cảm thấy không thoải mái; THÊM ngượng, xấu hổ).",
        "сердиться / рассердиться KHÔNG san cùng dãy: nghĩa thật khác (đang giận ↔ nổi giận), đúng như злиться / разозлиться. «nổi giận» ở сердиться hơi lệch sang nghĩa khởi phát nhưng GIỮ: bỏ đi thì {tức giận, giận, cáu} nằm gọn trong злиться, cùng badge.",
        "Trùng hết nghĩa trong lô chỉ có 3 cặp thể (вздр-, униж-, оскорб-) — badge thể tách.",
        "Họ máy báo đều ĐÚNG (порядочный, романтик, обожать, оскорбить, стесняться, сердиться, унижать, вздрогнуть). Máy sót: напряжённый ↔ спряже́ние / спряга́ться (có thẻ, г/ж).",
        "Mức tin: напряжённый ← «buộc ách» ghi ô đỏ từ nguyên (khớp k54). стесняться ← те́сный, оскорбить ← скорбь, обожать ← Бог: mối nối còn thấy rõ mặt chữ nên không ghi.",
        "Không chắc, KHÔNG đưa lên thẻ: лень ↔ Latin lenis (lenient); ла́ска «âu yếm» ↔ ла́ска «con chồn».",
    ],
}
