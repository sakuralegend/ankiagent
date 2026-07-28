# -*- coding: utf-8 -*-
"""k52 — language::grammar: LÔ SỬA. Hai luật chính tả mặt chữ (dấu cứng ъ sau
tiền tố phụ âm; ЧА ЩА / ЧУ ЩУ / ЖИ ШИ), nhưng KHÔNG dựng khối hệ thống lặp:
luật được hoà vào chính từ đang học, mỗi thẻ đứng một mình.

Sửa so với bản cũ:
  · BỎ hai khối lặp ('Luật chính tả trẻ con Nga nào cũng thuộc' x11 thẻ,
    'Luật dấu cứng ъ' x7 thẻ) — README §3, và đó cũng là thứ đẩy mọi thẻ
    vượt một màn hình.
  · THÊM mục 'Họ hàng' cho объявление · плащ · щи · щука · грач · луч.
  · Sửa hai lỗi trọng âm trong bản cũ: вра́чебная -> враче́бная (đã bỏ hẳn
    cụm này), разде́лить -> раздели́ть.
"""

S = {}
V = {}

# ---------------------------------------------------------------- врач
S["врач"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вра-</span>'
    '<span class="hd-gloss">gốc cổ nghĩa NÓI, đọc thần chú</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ч</span>'
    '<span class="hd-gloss">hậu tố NGƯỜI LÀM (như -чик, -щик)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc kể một câu chuyện: thời xưa người chữa bệnh là người '
    '<b>đọc thần chú</b>, nên <b>врач</b> họ hàng xa với <b>врать</b> '
    '(nghĩa cổ: nói; nghĩa nay: nói dối).</div>'
    '<div class="hd-warn">⚠️ Mức tin: đây là <b>từ nguyên</b>, không phải thứ người Nga '
    'hôm nay còn cảm thấy — hai nghĩa đã tách hẳn.</div>'
    '<div class="hd-warn"><b>врач</b> luôn là <b>giống đực</b> về ngữ pháp, kể cả khi bác sĩ '
    'là phụ nữ: <b>«Она́ хоро́ший врач»</b>. Cùng nhóm nghề bất biến: <b>инжене́р</b>, '
    '<b>дире́ктор</b>, <b>профе́ссор</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>враче́бный</b> thuộc y khoa (cùng gốc) · cùng lĩnh vực: '
    '<b>лечи́ть</b> chữa bệnh · <b>лека́рство</b> thuốc</div>'
)

# ---------------------------------------------------------------- грач
S["грач"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ <b>gốc trơn</b>, không chẻ được. Nghĩa: <b>quạ đen mỏ trắng</b> '
    '(loài rook), họ hàng gần với quạ thường.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tên gọi bắt chước tiếng kêu «gra-gra» — cùng kiểu đặt tên với '
    '<b>куку́шка</b> (chim cu, kêu «ku-ku»).</div>'
    '<div class="hd-why">Vì sao người Nga ai cũng biết từ này: <b>грачи́</b> là '
    '<b>chim báo xuân</b>, bay về sớm nhất sau mùa đông. Bức tranh '
    '<i>«Грачи́ прилете́ли»</i> là tranh phong cảnh nổi tiếng nhất nước Nga.</div>'
    '<div class="hd-warn"><b>Nhóm vần dễ lẫn</b> — bốn từ một âm tiết kết bằng <b>-ч</b>: '
    '<b>врач</b> bác sĩ · <b>грач</b> quạ đen · <b>плач</b> tiếng khóc · <b>луч</b> tia sáng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>грачи́</b> (số nhiều) · <b>грачо́нок</b> quạ con · '
    '<b>грачи́ный</b> thuộc về loài quạ đen</div>'
)

# ---------------------------------------------------------------- защита
S["защита"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">CHE PHÍA SAU, chắn lại</span></div>'
    '<div class="hd-row"><span class="hd-piece">-щит-</span>'
    '<span class="hd-gloss">щит — CÁI KHIÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen trong veo: <b>đưa cái khiên ra chắn</b> = sự bảo vệ. '
    'Chẻ ra rồi thì khỏi phải học thuộc — bạn đã có sẵn <b>щит</b> trong bộ thẻ.</div>'
    '<div class="hd-why">Tiền tố <b>за-</b> mang ý «chắn, phía sau»: <b>закры́ть</b> đóng lại · '
    '<b>забы́ть</b> quên (để lại phía sau).</div>'
    '<div class="hd-warn"><b>Nghĩa bạn sẽ gặp ở trường:</b> <b>защи́та дипло́ма</b> = bảo vệ '
    'luận văn. Đúng hình ảnh: đứng trước hội đồng, giơ khiên đỡ câu hỏi.</div>'
    '<div class="hd-sec">Họ hàng — gốc щит</div>'
    '<div class="hd-fam"><b>щит</b> cái khiên · <b>защища́ть</b> bảo vệ · '
    '<b>защи́тник</b> người bảo vệ, hậu vệ</div>'
)

# ---------------------------------------------------------------- луч
S["луч"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ <b>gốc trơn</b> một âm tiết. Nghĩa: <b>tia sáng</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ này có <b>họ hàng Ấn–Âu rất xa mà vẫn nhận ra được</b>: Latin '
    '<i>lux</i> (ánh sáng), tiếng Anh <i>lucid</i>, <i>translucent</i>. Cùng một gốc cổ '
    'nghĩa «sáng».</div>'
    '<div class="hd-why">Dùng thật: <b>луч со́лнца</b> tia nắng · '
    '<b>рентге́новские лучи́</b> tia X.</div>'
    '<div class="hd-warn"><b>Bẫy nhìn nhầm:</b> <b>луч</b> (tia sáng) KHÔNG liên quan gì tới '
    '<b>лу́чше</b> (tốt hơn) — hai từ khác gốc hoàn toàn, chỉ trùng mấy chữ đầu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лучево́й</b> thuộc tia, phóng xạ · <b>лучи́стый</b> rạng rỡ · '
    '<b>излуче́ние</b> bức xạ</div>'
)

# ---------------------------------------------------------------- объявить
S["объявить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">KHẮP LƯỢT, ra xung quanh</span></div>'
    '<div class="hd-row"><span class="hd-piece">ъ</span>'
    '<span class="hd-gloss">dấu cứng — tiền tố tận cùng phụ âm, trước <b>я</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-яв-</span>'
    '<span class="hd-gloss">LÀM HIỆN RA, phơi bày</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi nguyên thể động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>làm cho hiện ra khắp xung quanh</b> = tuyên bố. '
    'Không phải nói cho một người, mà phát ra cho cả vòng người nghe.</div>'
    '<div class="hd-warn"><b>Cặp thể:</b> <b>объяви́ть</b> (hoàn thành — tuyên bố xong) đi cặp '
    'với <b>объявля́ть</b> (chưa hoàn thành — đang/thường tuyên bố).</div>'
    '<div class="hd-sec">Họ hàng — gốc яв- HIỆN RA</div>'
    '<div class="hd-fam"><b>яви́ться</b> xuất hiện · <b>появи́ться</b> nảy ra · '
    '<b>явле́ние</b> hiện tượng · <b>я́вный</b> rõ rành rành · <b>объявле́ние</b> thông báo</div>'
)

# ---------------------------------------------------------------- объявление
S["объявление"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">KHẮP LƯỢT, ra xung quanh</span></div>'
    '<div class="hd-row"><span class="hd-piece">ъ</span>'
    '<span class="hd-gloss">dấu cứng — tiền tố phụ âm, trước <b>я</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-явл-</span>'
    '<span class="hd-gloss">LÀM HIỆN RA (dạng có <b>л</b> chèn)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">hậu tố biến ĐỘNG TỪ thành DANH TỪ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Là <b>объяви́ть</b> (tuyên bố) đóng gói thành danh từ: cái được tuyên '
    'bố = <b>tờ thông báo, mẩu rao vặt</b>.</div>'
    '<div class="hd-why"><b>-ение / -ание</b> là hậu tố đáng giá nhất để nhận mặt: gặp nó là '
    'biết ngay DANH TỪ trừu tượng sinh từ động từ, và luôn <b>giống trung</b>.</div>'
    '<div class="hd-warn"><b>Chữ л từ đâu ra:</b> gốc <b>яв-</b> gặp hậu tố thì mọc thêm '
    '<b>л</b> → <b>явл-</b>. «л chèn» này chuyên xuất hiện sau phụ âm môi <b>б п в ф м</b>: '
    '<b>люби́ть</b> → <b>люблю́</b>, <b>купи́ть</b> → <b>куплю́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>объяви́ть</b> tuyên bố · <b>объявля́ть</b> đang tuyên bố · '
    '<b>явле́ние</b> hiện tượng · <b>упражне́ние</b> bài tập (cùng đuôi -ение)</div>'
)

# ---------------------------------------------------------------- объём
S["объём"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">QUANH, bao lấy</span></div>'
    '<div class="hd-row"><span class="hd-piece">ъ</span>'
    '<span class="hd-gloss">dấu cứng — tiền tố phụ âm, trước <b>ё</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ём</span>'
    '<span class="hd-gloss">LẤY, CẦM</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>cái ôm lấy được xung quanh</b> = <b>thể tích</b>. '
    'Hình dung hai tay vòng ôm một khối — chỗ trống bên trong vòng tay chính là объём.</div>'
    '<div class="hd-why">Tiếng Anh đi cùng đường: <i>volume</i> ← Latin <i>volvere</i> = '
    'cuộn quanh. Hai thứ tiếng đều lấy hình ảnh «vòng quanh» để gọi thể tích.</div>'
    '<div class="hd-why">Tiền tố <b>об-</b> gặp rất nhiều: <b>обня́ть</b> ôm · '
    '<b>объясни́ть</b> giải thích · <b>обойти́</b> đi vòng quanh.</div>'
    '<div class="hd-sec">Họ hàng — gốc ём/им/ня LẤY, CẦM</div>'
    '<div class="hd-fam"><b>взять</b> lấy · <b>заня́ть</b> chiếm, mượn · <b>приня́ть</b> nhận · '
    '<b>подня́ть</b> nâng lên · <b>сня́ть</b> cởi ra, thuê</div>'
)

# ---------------------------------------------------------------- плач
S["плач"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">плач-</span>'
    '<span class="hd-gloss">KHÓC — từ động từ <b>пла́кать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Kiểu <b>danh từ trần</b>: lấy động từ, cắt trụi đuôi, thành danh từ '
    'chỉ chính hành động đó. <b>пла́кать</b> (khóc) → <b>плач</b> (tiếng khóc). Cùng kiểu: '
    '<b>крича́ть</b> hét → <b>крик</b> tiếng hét.</div>'
    '<div class="hd-warn"><b>BẪY quan trọng nhất của từ này:</b> <b>плач</b> (không ь) = '
    'DANH TỪ, tiếng khóc. <b>плачь</b> (có ь) = MỆNH LỆNH «khóc đi!». Danh từ giống đực không '
    'đội <b>-ь</b>, còn động từ mệnh lệnh thì có.</div>'
    '<div class="hd-sec">Họ hàng — gốc плак/плач</div>'
    '<div class="hd-fam"><b>пла́кать</b> khóc · <b>запла́кать</b> oà khóc · '
    '<b>пла́кса</b> đứa hay khóc nhè · <b>плакси́вый</b> hay mè nheo</div>'
)

# ---------------------------------------------------------------- плащ
S["плащ"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ <b>gốc trơn</b>, không chẻ được. Nghĩa: <b>áo mưa, áo choàng dài</b> '
    'khoác ngoài che mưa gió.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nối với nhóm thời tiết: trời <b>дождли́вый</b> (mưa dai) hay '
    '<b>ве́треный</b> (gió) thì mặc <b>плащ</b>.</div>'
    '<div class="hd-warn"><b>Bẫy chính tả:</b> kết thúc bằng <b>щ</b> trần, KHÔNG có dấu mềm — '
    '<b>плащ</b> chứ không phải <i>*плащь</i>. Đây là danh từ <b>giống đực</b>; chỉ danh từ '
    'GIỐNG CÁI mới đội <b>-ь</b> sau ж ш ч щ.</div>'
    '<div class="hd-sec">Nhóm cùng đuôi rít — dấu mềm báo GIỐNG</div>'
    '<div class="hd-fam">đực, không ь: <b>плащ</b> áo mưa · <b>нож</b> con dao ↔ cái, có ь: '
    '<b>по́мощь</b> sự giúp đỡ · <b>вещь</b> đồ vật · <b>мышь</b> con chuột</div>'
)

# ---------------------------------------------------------------- подъезд
S["подъезд"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span>'
    '<span class="hd-gloss">TỚI SÁT, tiến đến gần</span></div>'
    '<div class="hd-row"><span class="hd-piece">ъ</span>'
    '<span class="hd-gloss">dấu cứng — <b>под</b> tận cùng phụ âm, trước <b>е</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-езд</span>'
    '<span class="hd-gloss">ĐI BẰNG XE</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>chỗ xe chạy tới sát</b>. Ra hai nghĩa — lối xe vào, và '
    '<b>cửa/sảnh chung cư</b> (chính là chỗ xe đỗ sát để người xuống).</div>'
    '<div class="hd-warn"><b>Luật dấu cứng ъ — thuộc một lần dùng mãi:</b> viết <b>ъ</b> khi nó '
    'đứng ngay sau một TIỀN TỐ tận cùng bằng phụ âm VÀ ngay trước <b>е ё ю я</b>. Nó NGĂN ĐÔI: '
    '<i>подъезд</i> đọc «pad-YEZD» chứ không phải «pa-DEZD».</div>'
    '<div class="hd-why">Tiền tố làm chủ nghĩa: <b>подъе́зд</b> đi tới sát · <b>вы́езд</b> đi ra · '
    '<b>въезд</b> đi vào · <b>объе́зд</b> đi vòng.</div>'
    '<div class="hd-sec">Họ hàng — gốc езд/езж/ех ĐI BẰNG XE</div>'
    '<div class="hd-fam"><b>е́хать</b> đi (bằng xe) · <b>е́здить</b> đi lại thường xuyên · '
    '<b>прие́хать</b> đến nơi · <b>по́езд</b> tàu hoả · <b>пое́здка</b> chuyến đi</div>'
)

# ---------------------------------------------------------------- подъём
S["подъём"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span>'
    '<span class="hd-gloss">TỪ DƯỚI LÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">ъ</span>'
    '<span class="hd-gloss">dấu cứng — tiền tố phụ âm, trước <b>ё</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ём</span>'
    '<span class="hd-gloss">LẤY, NÂNG</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>lấy từ dưới lên</b> = sự nâng lên. Từ một hình ảnh đó '
    'toả ra đủ nghĩa: dốc lên (đường), lúc thức dậy (nâng mình khỏi giường), đà đi lên '
    '(kinh tế).</div>'
    '<div class="hd-why">Động từ tương ứng là <b>подня́ть</b> (nâng lên) — cùng gốc, khác dạng: '
    '<b>-ём</b> trong danh từ, <b>-ня-</b> trong động từ.</div>'
    '<div class="hd-warn"><b>Luật trọng âm quà tặng:</b> chữ <b>ё</b> trong tiếng Nga LUÔN mang '
    'trọng âm, không có ngoại lệ. Thấy ё là biết ngay nhấn ở đó.</div>'
    '<div class="hd-sec">Họ hàng — gốc ём/им/ня LẤY, CẦM</div>'
    '<div class="hd-fam"><b>взять</b> lấy · <b>име́ть</b> có · <b>заня́ть</b> chiếm, mượn · '
    '<b>приня́ть</b> nhận · <b>подня́ть</b> nâng lên · <b>сня́ть</b> cởi ra, thuê</div>'
)

# ---------------------------------------------------------------- помощь
S["помощь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố, ý «góp vào, làm một lượt»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мощ-</span>'
    '<span class="hd-gloss">SỨC MẠNH — biến âm từ <b>мог-</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ь</span>'
    '<span class="hd-gloss">dấu mềm — dấu hiệu DANH TỪ GIỐNG CÁI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>góp sức vào</b> = sự giúp đỡ. Gốc <b>мощ-</b> chính là '
    '<b>мочь / могу́</b> (có thể) — cùng một gốc, ba mặt nạ: <b>мог</b> → <b>мож</b> → '
    '<b>мощ</b>.</div>'
    '<div class="hd-why">Chuỗi biến âm <b>г → ж → щ</b> là một trong những chuỗi năng suất nhất '
    'tiếng Nga. Nhận ra nó thì cả chùm dưới đây gộp lại chỉ còn MỘT gốc phải nhớ.</div>'
    '<div class="hd-warn"><b>Luật giống cái đuôi -ь:</b> danh từ tận cùng <b>-ь</b> mà trước đó '
    'là ж ш ч щ thì <b>luôn GIỐNG CÁI</b>: <b>по́мощь</b>, <b>вещь</b>, <b>мышь</b>, '
    '<b>рожь</b>, <b>дочь</b>.</div>'
    '<div class="hd-sec">Họ hàng — gốc мог/мож/мощ</div>'
    '<div class="hd-fam"><b>мочь</b> có thể · <b>мо́жно</b> được phép · <b>мощь</b> sức mạnh · '
    '<b>помога́ть</b> giúp đỡ · <b>возмо́жность</b> khả năng</div>'
)

# ---------------------------------------------------------------- пощада
S["пощада"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố hoàn thành</span></div>'
    '<div class="hd-row"><span class="hd-piece">-щад-</span>'
    '<span class="hd-gloss">THA, nương tay (<b>щади́ть</b> = tha cho)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa: <b>sự tha, sự nương tay</b> — hay gặp nhất ở dạng phủ định '
    '<b>без поща́ды</b> = không thương tiếc.</div>'
    '<div class="hd-why">Ít dùng trong hội thoại, nhưng nó là <b>ví dụ sạch của luật ЩА viết '
    'А</b>: <b>поща́да</b>, không đời nào là <i>*пощяда</i>. Cùng luật: ЧУ ЩУ viết У, '
    'ЖИ ШИ viết И — vì ч щ tự thân đã mềm, ж ш tự thân đã cứng.</div>'
    '<div class="hd-sec">Họ hàng — gốc щад-</div>'
    '<div class="hd-fam"><b>щади́ть</b> tha, nương tay · <b>беспоща́дный</b> tàn nhẫn, không '
    'thương tiếc</div>'
)

# ---------------------------------------------------------------- разъезд
S["разъезд"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раз-</span>'
    '<span class="hd-gloss">TẢN RA, mỗi thứ một hướng</span></div>'
    '<div class="hd-row"><span class="hd-piece">ъ</span>'
    '<span class="hd-gloss">dấu cứng — tiền tố phụ âm, trước <b>е</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-езд</span>'
    '<span class="hd-gloss">ĐI BẰNG XE</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>đi xe tản ra mỗi người một ngả</b>. Ra hai nghĩa: cảnh đi '
    'công tác liên miên, và <b>ga tránh tàu</b> — chỗ đường ray tách đôi cho hai tàu vượt '
    'nhau.</div>'
    '<div class="hd-warn"><b>Bẫy đối nghĩa:</b> <b>разъе́зд</b> (tản ra) đứng đối diện '
    '<b>съезд</b> (tụ về). Cùng gốc <b>езд</b>, chỉ đổi tiền tố mà nghĩa lộn ngược.</div>'
    '<div class="hd-sec">Họ hàng — tiền tố раз- TÁCH RA</div>'
    '<div class="hd-fam"><b>разби́ть</b> đập vỡ · <b>раздели́ть</b> chia · '
    '<b>рассказа́ть</b> kể ra · <b>разгово́р</b> cuộc trò chuyện</div>'
)

# ---------------------------------------------------------------- разъём
S["разъём"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раз-</span>'
    '<span class="hd-gloss">TÁCH RỜI</span></div>'
    '<div class="hd-row"><span class="hd-piece">ъ</span>'
    '<span class="hd-gloss">dấu cứng — tiền tố phụ âm, trước <b>ё</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ём</span>'
    '<span class="hd-gloss">LẤY, CẦM</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>chỗ tháo rời ra được</b> — tức là <b>đầu nối, giắc '
    'cắm</b> (cổng USB, jack tai nghe). Từ kỹ thuật hiện đại nhưng dựng bằng đúng bộ phận '
    'tiếng Nga cổ.</div>'
    '<div class="hd-why">Đặt cạnh nhau thấy ngay sức mạnh của tiền tố: <b>подъём</b> nâng LÊN · '
    '<b>разъём</b> tháo RỜI · <b>объём</b> ôm QUANH. Cùng một gốc <b>ём</b>, ba tiền tố, ba '
    'nghĩa.</div>'
    '<div class="hd-sec">Họ hàng — gốc ём/им/ня</div>'
    '<div class="hd-fam"><b>взять</b> lấy · <b>сня́ть</b> cởi ra, tháo ra · '
    '<b>приня́ть</b> nhận · <b>заня́ть</b> chiếm, mượn</div>'
)

# ---------------------------------------------------------------- съезд
S["съезд"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">TỤ LẠI MỘT CHỖ (và cả nghĩa: xuống)</span></div>'
    '<div class="hd-row"><span class="hd-piece">ъ</span>'
    '<span class="hd-gloss">dấu cứng — <b>с</b> là tiền tố phụ âm, trước <b>е</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-езд</span>'
    '<span class="hd-gloss">ĐI BẰNG XE</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>mọi người đi xe TỤ VỀ một chỗ</b> = đại hội. Hình ảnh rất '
    'thật: thời chưa có máy bay, đại hội là cảnh đại biểu khắp nơi đổ xe về thủ đô.</div>'
    '<div class="hd-warn"><b>Bẫy chính tả:</b> tiền tố chỉ có MỘT chữ <b>с</b> nhưng vẫn phải có '
    '<b>ъ</b> — luật tính theo «tiền tố tận cùng bằng phụ âm», dài ngắn không quan trọng. Viết '
    '<i>*сезд</i> là sai.</div>'
    '<div class="hd-sec">Họ hàng — gốc езд</div>'
    '<div class="hd-fam"><b>е́хать</b> đi (bằng xe) · <b>съе́здить</b> đi một chuyến rồi về · '
    '<b>по́езд</b> tàu hoả · <b>разъе́зд</b> sự tản ra (nghĩa ngược)</div>'
)

# ---------------------------------------------------------------- хвощ
S["хвощ"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">хво-</span>'
    '<span class="hd-gloss">từ <b>хвост</b> — CÁI ĐUÔI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-щ</span>'
    '<span class="hd-gloss"><b>ст</b> của хвост bị làm mềm thành <b>щ</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa: <b>cỏ đuôi ngựa</b> — loài cây thân đốt trông đúng như cái đuôi. '
    'Tiếng Anh gọi y hệt: <i>horsetail</i>.</div>'
    '<div class="hd-why"><b>Mẹo chẻ chữ щ:</b> phần lớn <b>щ</b> không phải chữ gốc, nó là '
    '<b>ск · ст · т</b> bị làm mềm khi thêm hậu tố. Gặp щ thì thử thay ngược, thường lòi ra từ '
    'quen: <b>хвост</b> → <b>хвощ</b> · <b>пусти́ть</b> thả → <b>пущу́</b> tôi sẽ thả · '
    '<b>чи́стить</b> lau → <b>чи́щу</b> tôi lau.</div>'
    '<div class="hd-warn">Từ hiếm, gần như chỉ gặp trong sách sinh học. Đừng tốn sức nhớ nghĩa — '
    'hãy nhớ nó vì <b>cái luật biến âm</b> nó minh hoạ.</div>'
    '<div class="hd-sec">Họ hàng — gốc хвост</div>'
    '<div class="hd-fam"><b>хвост</b> cái đuôi · <b>хво́стик</b> đuôi nhỏ, chỏm tóc · '
    '<b>хвоста́тый</b> có đuôi</div>'
)

# ---------------------------------------------------------------- щи
S["щи"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ <b>gốc trơn</b>, chỉ hai chữ cái — một trong những từ ngắn nhất '
    'tiếng Nga. Nghĩa: <b>xúp bắp cải</b>, món quốc hồn quốc tuý của Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-warn"><b>Chỉ có SỐ NHIỀU:</b> <b>щи</b> không có dạng số ít, y như tiếng Việt '
    'nói «bún riêu» chứ không đếm. Cùng nhóm: <b>де́ньги</b> tiền · <b>часы́</b> đồng hồ · '
    '<b>очки́</b> kính · <b>кани́кулы</b> kỳ nghỉ.</div>'
    '<div class="hd-why">Có câu tục ngữ người Nga nào cũng biết: '
    '<b>«Щи да ка́ша — пи́ща на́ша»</b> = «Xúp bắp cải với cháo, ấy là cơm của ta».</div>'
    '<div class="hd-sec">Đi cùng nhau</div>'
    '<div class="hd-fam"><b>щи</b> nấu từ <b>капу́ста</b> bắp cải · <b>борщ</b> thêm củ dền · '
    '<b>суп</b> món xúp nói chung</div>'
)

# ---------------------------------------------------------------- щит
S["щит"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ <b>gốc trơn</b> một âm tiết — <b>щ</b> ở đây là chữ gốc, không thay '
    'ngược ra được từ nào quen. Nghĩa: <b>cái khiên</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là <b>từ mẹ</b> của cả một chùm, nên đáng nhớ kỹ hơn chính nghĩa '
    'của nó: từ <b>щит</b> mọc ra <b>защи́та</b> (sự bảo vệ) và <b>защища́ть</b> (bảo vệ) — hai '
    'từ bạn dùng nhiều hơn hẳn từ gốc.</div>'
    '<div class="hd-why">Nghĩa hiện đại rất đời thường: <b>щит</b> còn là bảng điện, bảng quảng '
    'cáo lớn — bất cứ tấm phẳng nào chắn phía trước.</div>'
    '<div class="hd-sec">Họ hàng — gốc щит</div>'
    '<div class="hd-fam"><b>защи́та</b> sự bảo vệ · <b>защища́ть</b> bảo vệ · '
    '<b>защи́тник</b> người bảo vệ, hậu vệ (bóng đá)</div>'
)

# ---------------------------------------------------------------- щука
S["щука"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ <b>gốc trơn</b>. Nghĩa: <b>cá măng, cá chó</b> — loài cá dữ răng '
    'nhọn ở sông hồ Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ví dụ sạch của luật <b>ЩУ viết У</b>: <b>щу́ка</b>, không đời nào là '
    '<i>*щюка</i>.</div>'
    '<div class="hd-why"><b>Щу́ка</b> là nhân vật cổ tích ai cũng biết — trong '
    '<i>«По щу́чьему веле́нию»</i> («Theo lệnh cá măng»), chàng lười Emelya bắt được cá măng '
    'thần và mọi ước đều thành.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>щу́чий</b> thuộc về cá măng · <b>щурёнок</b> cá măng con · '
    '<b>по щу́чьему веле́нию</b> «theo lệnh cá măng»</div>'
)

# ---------------------------------------------------------------- щётка
S["щётка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">щёт-</span>'
    '<span class="hd-gloss">từ <b>щети́на</b> — LÔNG CỨNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-а</span>'
    '<span class="hd-gloss">hậu tố vật nhỏ + đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>cái có lông cứng</b> = bàn chải. Từ bạn dùng mỗi sáng: '
    '<b>зубна́я щётка</b> = bàn chải đánh răng.</div>'
    '<div class="hd-why">Hậu tố <b>-ка</b> ở đây là «vật nhỏ, đồ dùng» — cực kỳ năng suất: '
    '<b>ру́чка</b> cái bút · <b>ча́шка</b> cái chén · <b>ло́жка</b> cái thìa.</div>'
    '<div class="hd-warn">Chữ <b>ё</b> LUÔN mang trọng âm — thấy <b>щётка</b> là biết nhấn ngay '
    'ở đó, khỏi phân vân.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>щети́на</b> lông cứng, râu lởm chởm · '
    '<b>чи́стить щёткой</b> chải, cọ</div>'
)


# ====================================================================
# V — sửa field Vietnamese (README §2c). Dòng này là ĐỀ BÀI của deck
# 1-go: user nhìn nó rồi GÕ từ Nga, nên phải chỉ có MỘT đáp án đúng.
# ====================================================================

# Nghĩa cũ SAI hẳn: "chim sáo" là скворец (starling), không phải грач (rook).
V["грач"] = "quạ đen mỏ trắng (loài rook — chim báo mùa xuân ở Nga)"

# защита (danh từ) đụng защищать (động từ) khi dịch thành "bảo vệ".
V["защита"] = "sự bảo vệ, sự che chắn (DANH TỪ)"

# "thông báo" một mình không phân biệt thể, cũng không phân biệt với danh từ объявление.
V["объявить"] = "tuyên bố, công bố cho mọi người biết (HOÀN THÀNH — một lần, xong việc)"
V["объявление"] = "tờ thông báo, mẩu rao vặt dán/đăng công khai (danh từ)"

# "khối lượng" trong nghĩa cũ đụng масса/вес; объём là chỗ chiếm trong không gian.
V["объём"] = "thể tích, dung tích (chỗ chiếm trong không gian)"

# плач (danh từ) đụng плакать (động từ) và рёв ("tiếng khóc thét").
V["плач"] = "tiếng khóc (DANH TỪ, không phải động từ khóc)"

# "áo choàng" đụng пальто ("áo khoác dài").
V["плащ"] = "áo mưa, áo khoác ngoài che mưa gió"

# "lối vào" đụng thẳng вход ("cổng vào, lối đi, vé vào cửa").
V["подъезд"] = "sảnh/cửa vào của khu chung cư; lối cho xe chạy tới sát"

# Nghĩa cũ rời rạc, không nhận ra là một từ; gom lại thành dấu vân tay của подъём.
V["подъём"] = "sự nâng lên; đoạn dốc đi lên; lúc thức dậy (một danh từ mang cả ba)"

# помощь (danh từ) đụng động từ "giúp đỡ".
V["помощь"] = "sự giúp đỡ, sự cứu giúp (DANH TỪ giống cái)"

# "khoan dung / thương hại" đụng милосердие, жалость.
V["пощада"] = "sự tha, sự nương tay (không giết, không trừng phạt)"

V["разъезд"] = "việc đi công tác liên miên bằng xe; ga tránh tàu"
V["разъём"] = "giắc cắm, đầu nối tháo rời được (cổng USB, jack tai nghe)"

# "cuộc họp lớn" đụng собрание/конференция; giữ nét ĐI XE TỤ VỀ của съезд.
V["съезд"] = "đại hội (đại biểu khắp nơi đi xe tụ về một chỗ)"

V["щи"] = "xúp bắp cải Nga (từ chỉ dùng ở SỐ NHIỀU)"

# "bảng quảng cáo" trong nghĩa cũ làm loãng; giữ nghĩa gốc để khỏi đụng защита.
V["щит"] = "cái khiên, tấm chắn phẳng"

# "bàn chải" đụng кисть (bút lông, chổi quét sơn).
V["щётка"] = "bàn chải (đánh răng, chải quần áo)"
