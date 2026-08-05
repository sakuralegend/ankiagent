# -*- coding: utf-8 -*-
"""k39 — places::city: chỗ chốn trong thành phố, phần lớn là TỪ MƯỢN QUỐC TẾ.

Trục thật của lô (đọc `tiep` rồi mới chốt, không đoán theo nhãn topic): 13/16 từ
là từ mượn Hy Lạp/Latin/Anh nên "Cách nhớ" bắc cầu thẳng sang chữ tiếng Anh user
đã biết; 3 từ Slav gốc (собор · площадь · деревня) thì chẻ được thật, và đó là
chỗ đáng bỏ công nhất. KHÔNG dựng khối dùng chung (README §3).
"""

S = {}

S["бар"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mượn thẳng tiếng Anh <i>bar</i> — không chẻ ra được, '
    'cả từ là một khối. Nghĩa cũng bê nguyên: vừa là cái quầy rượu, vừa là quán '
    'có cái quầy đó.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ба́рмен</b> người đứng quầy pha rượu — đuôi <b>-мен</b> '
    'chính là <i>-man</i> tiếng Anh mượn vào, cùng khuôn với <b>бизнесме́н</b>, '
    '<b>спортсме́н</b>.</div>'
    '<div class="hd-warn">Chỗ ăn uống tiếng Nga chia theo việc chính: <b>бар</b> để '
    'uống, <b>кафе́</b> ngồi nhẹ, <b>рестора́н</b> để ăn một bữa đàng hoàng.</div>'
)

S["собор"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">CÙNG, chung lại</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бор-</span>'
    '<span class="hd-gloss">GOM, nhặt lấy</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen là "chỗ mọi người GOM lại". Từ đó ra hai nghĩa '
    'của <b>собо́р</b>: nhà thờ CHÍNH mà cả vùng đổ về, và cuộc công đồng, hội '
    'nghị của giới tăng lữ.</div>'
    '<div class="hd-warn">Nhà thờ nói chung là <b>це́рковь</b>; <b>собо́р</b> chỉ '
    'dùng cho nhà thờ lớn, nhà thờ chính — đúng như <i>cathedral</i> phân biệt với '
    '<i>church</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>собра́ние</b> cuộc họp, bộ sưu tập · <b>собира́ть</b> '
    'thu gom, nhặt lại · <b>сбор</b> sự thu, cuộc tập hợp.</div>'
)

S["театр"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng chữ <i>theatre</i>, mượn qua tiếng Pháp từ Hy Lạp '
    '<i>théatron</i> = "chỗ để XEM" — một khối liền, không chẻ ra được. Nhớ nghĩa '
    'gốc thì hiểu ngay vì sao <b>теа́тр</b> vừa là toà nhà, vừa là cả ngành kịch '
    'nghệ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>театра́льный</b> thuộc nhà hát, thuộc sân khấu · '
    '<b>кинотеа́тр</b> rạp chiếu phim.</div>'
    '<div class="hd-warn">Hai cụm hay gặp: <b>идти́ в теа́тр</b> = đi xem kịch (đi '
    'TỚI → cách 4), <b>быть в теа́тре</b> = đang ở trong nhà hát (Ở → cách 6).</div>'
)

S["кинотеатр"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кино-</span>'
    '<span class="hd-gloss">PHIM, điện ảnh</span></div>'
    '<div class="hd-row"><span class="hd-piece">-теа́тр</span>'
    '<span class="hd-gloss">NHÀ HÁT</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ghép thẳng hai mảnh: "nhà hát chiếu phim". Trọng âm ở '
    'nguyên chỗ cũ của <b>теа́тр</b> nên từ dài ra mà vẫn đọc <b>кинотеа́тр</b>.'
    '</div>'
    '<div class="hd-warn"><b>кинотеа́тр</b> là TOÀ NHÀ có phòng chiếu. Bộ phim cụ '
    'thể là <b>фильм</b>; còn <b>кино́</b> bị dùng lẫn cho cả hai nghĩa nên đừng '
    'lấy nó làm đáp án cho "rạp".</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кино́</b> phim, điện ảnh · <b>теа́тр</b> nhà hát (mảnh '
    'sau của chính từ này).</div>'
)

S["центр"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng chữ <i>centre</i>, mượn từ Hy Lạp <i>kéntron</i> — '
    'vốn là MŨI NHỌN của cái compa cắm xuống giấy. Chỗ mũi nhọn cắm chính là tâm, '
    'nên từ này đi từ "mũi nhọn" sang "chỗ chính giữa".</div>'
    '<div class="hd-warn">Cụm phải thuộc: <b>в це́нтре го́рода</b> = ở trung tâm '
    'thành phố (sau <b>в</b> thì <b>центр</b> đi cách 6).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>центра́льный</b> ở trung tâm, chủ chốt · '
    '<b>эпице́нтр</b> tâm chấn (của trận động đất).</div>'
)

S["автобус"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">авто-</span>'
    '<span class="hd-gloss">TỰ, tự chạy</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бус</span>'
    '<span class="hd-gloss">cắt từ <i>omnibus</i> = "cho TẤT CẢ"</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Xe ngựa công cộng ngày xưa gọi là <i>omnibus</i> (tiếng '
    'Latin: "cho tất cả mọi người"). Khi nó có động cơ tự chạy thì thành '
    '<b>авто́бус</b>. Mảnh <b>-бус</b> từ đó lan sang <b>тролле́йбус</b>.</div>'
    '<div class="hd-warn">Đi bằng phương tiện gì thì dùng <b>на</b> + cách 6: '
    '<b>на авто́бусе</b> = bằng xe buýt.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тролле́йбус</b> xe buýt chạy điện · '
    '<b>автомоби́ль</b> ô tô (cùng mảnh <b>авто-</b>).</div>'
)

S["университет"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">универс-</span>'
    '<span class="hd-gloss">TOÀN THỂ, chung tất cả (<i>universe</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ите́т</span>'
    '<span class="hd-gloss">đuôi mượn, ứng với <i>-ity</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Latin <i>universitas</i> = "toàn thể thầy và trò gộp lại" '
    '⇒ trường gom đủ MỌI ngành. Đuôi <b>-ите́т</b> luôn kéo trọng âm về chính nó, '
    'nên cả lớp từ này đều nhấn ở âm cuối.</div>'
    '<div class="hd-warn"><b>университе́т</b> là đại học TỔNG HỢP nhiều khoa. '
    'Trường bậc đại học chỉ dạy một ngành thì tiếng Nga gọi là <b>институ́т</b>.'
    '</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>авторите́т</b> uy tín · <b>суверените́т</b> chủ quyền · '
    '<b>приорите́т</b> sự ưu tiên.</div>'
)

S["проспект"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">XUYÊN QUA, về phía trước</span></div>'
    '<div class="hd-row"><span class="hd-piece">-спект-</span>'
    '<span class="hd-gloss">NHÌN (như <i>inspect</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Latin <i>prospectus</i> = "cái nhìn thẳng ra phía trước". '
    'Phố nào thẳng tắp, nhìn hút tầm mắt thì Nga gọi là <b>проспе́кт</b>. Cũng chữ '
    'ấy khi là tờ giấy in thì thành "bản giới thiệu, tờ gấp".</div>'
    '<div class="hd-warn"><b>проспе́кт</b> là phố lớn và thẳng, thường mang tên '
    'riêng (<b>Не́вский проспе́кт</b>); phố thường vẫn là <b>у́лица</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>перспекти́ва</b> viễn cảnh, phối cảnh · '
    '<b>инспе́ктор</b> thanh tra (người "nhìn vào").</div>'
)

S["институт"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng chữ <i>institute</i>, Latin <i>institutum</i> = "cái '
    'được LẬP RA, được dựng lên". Tiếng Nga mượn nguyên một khối nên không chẻ ra '
    'được; trọng âm rơi vào âm tiết cuối như mọi từ mượn cùng lớp '
    '(<b>университе́т</b>, <b>авторите́т</b>).</div>'
    '<div class="hd-warn"><b>институ́т</b> có hai nghĩa rời hẳn nhau: trường bậc '
    'đại học chỉ dạy MỘT ngành, và viện nghiên cứu khoa học. Cả hai đều không phải '
    '<b>университе́т</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>конститу́ция</b> hiến pháp — cùng gốc Latin "dựng lên, '
    'đặt ra".</div>'
)

S["площадь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">площ-</span>'
    '<span class="hd-gloss">PHẲNG, bẹt (gốc <b>плоск-</b>, <b>ск</b> đổi thành '
    '<b>щ</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-адь</span>'
    '<span class="hd-gloss">đuôi danh từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỗ đất PHẲNG và rộng giữa phố → quảng trường. Cũng vì '
    '"bề mặt phẳng" mà trong hình học <b>пло́щадь</b> lại là diện tích. Một từ, hai '
    'nghĩa, cùng đi ra từ "phẳng".</div>'
    '<div class="hd-warn">Số nhiều gãy làm đôi: cách 1 và 4 vẫn <b>пло́щади</b>, '
    'nhưng từ cách 2 trở đi trọng âm nhảy xuống đuôi — <b>площаде́й</b>, '
    '<b>площадя́м</b>, <b>площадя́ми</b>, <b>площадя́х</b>.</div>'
    '<div class="hd-warn">Ở quảng trường nói <b>на пло́щади</b>, không dùng '
    '<b>в</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пло́ский</b> phẳng, bẹt · <b>площа́дка</b> sân nhỏ, bãi '
    '(trọng âm dịch xuống <b>-а́д-</b>).</div>'
)

S["автомобиль"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">авто-</span>'
    '<span class="hd-gloss">TỰ, tự thân</span></div>'
    '<div class="hd-row"><span class="hd-piece">-моби́ль</span>'
    '<span class="hd-gloss">DI ĐỘNG (Latin <i>mobilis</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ghép lại là "cái TỰ di động" — đúng chữ <i>automobile</i>. '
    'Mảnh <b>авто-</b> gặp lại ở <b>авто́бус</b>, mảnh <b>-моби́ль</b> gặp lại ở '
    '<b>моби́льный</b> (di động, như điện thoại di động).</div>'
    '<div class="hd-warn"><b>автомоби́ль</b> là từ trang trọng, dùng trong văn bản '
    'và kỹ thuật. Nói hằng ngày người Nga gọi cái xe là <b>маши́на</b>.</div>'
    '<div class="hd-warn">Cụm phải thuộc: <b>легково́й автомоби́ль</b> = xe con chở '
    'người, đối lại <b>грузови́к</b> xe tải.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>моби́льный</b> di động · <b>авто́бус</b> xe buýt.</div>'
)

S["индия"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">Инд-</span>'
    '<span class="hd-gloss">tên con sông <b>Инд</b> (<i>Indus</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ия</span>'
    '<span class="hd-gloss">đuôi tên nước, luôn giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người Hy Lạp gọi vùng đất bên kia sông Инд là <i>India</i>, '
    'tiếng Nga mượn nguyên. Đuôi <b>-ия</b> là khuôn chuẩn của tên nước '
    '(<b>Ита́лия</b>, <b>Испа́ния</b>, <b>Росси́я</b>) và cả nhóm chia y như nhau.'
    '</div>'
    '<div class="hd-warn"><b>инди́ец</b> = người Ấn Độ, còn <b>инде́ец</b> = thổ '
    'dân châu Mỹ (người da đỏ). Lệch đúng một chữ, và người Nga phân biệt rất chặt.'
    '</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>инди́йский</b> thuộc Ấn Độ · <b>инди́ец</b> người Ấn Độ.'
    '</div>'
)

S["академия"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không chẻ được: gốc là TÊN RIÊNG — khu vườn <i>Akademeia</i> '
    'ở Athens, nơi Platon giảng bài. Tên của chỗ dạy học ấy thành tên chung cho '
    '"viện hàn lâm". Đuôi <b>-ия</b> giống cái, chia y như <b>Росси́я</b>.</div>'
    '<div class="hd-warn">Trọng âm KHÔNG đứng yên: <b>акаде́мия</b> và '
    '<b>акаде́мик</b> giữ ở <b>-де́-</b>, nhưng sang tính từ nó nhảy một bậc — '
    '<b>академи́ческий</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>акаде́мик</b> viện sĩ · <b>академи́ческий</b> thuộc học '
    'thuật, hàn lâm.</div>'
)

S["россия"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">Росс-</span>'
    '<span class="hd-gloss">biến thể Hy Lạp của <b>Русь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ия</span>'
    '<span class="hd-gloss">đuôi tên nước</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người Hy Lạp Byzantine viết <b>Русь</b> thành <i>Rhosia</i>; '
    'chữ đó quay ngược về tiếng Nga thành <b>Росси́я</b>. Nên <b>Рус-</b> và '
    '<b>Росс-</b> là một gốc, chỉ khác đường đi.</div>'
    '<div class="hd-warn">Cặp người Nga phân biệt rất nghiêm: <b>ру́сский</b> nói '
    'về DÂN TỘC và tiếng nói; <b>росси́йский</b> nói về NHÀ NƯỚC — mọi công dân đều '
    '<b>росси́йский</b>, kể cả người không thuộc dân tộc Nga.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>росси́йский</b> thuộc nhà nước Nga · <b>россия́нин</b> '
    'công dân Nga · <b>ру́сский</b> thuộc dân tộc Nga; tiếng Nga.</div>'
)

S["франция"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">Франц-</span>'
    '<span class="hd-gloss">bộ tộc <b>фра́нки</b> (người Frank)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ия</span>'
    '<span class="hd-gloss">đuôi tên nước</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Latin <i>Francia</i> = "đất của người Frank" — tên nước '
    'lấy thẳng tên bộ tộc rồi gắn đuôi <b>-ия</b> vào là xong.</div>'
    '<div class="hd-warn">Trọng âm nhảy ngay khi rời tên nước: <b>Фра́нция</b> '
    'nhưng <b>францу́з</b>, <b>францу́зский</b>. Và người Pháp không theo khuôn '
    '<b>-ец</b> như <b>не́мец</b> — phải thuộc riêng <b>францу́з</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>францу́з</b> người Pháp · <b>францу́зский</b> thuộc '
    'Pháp; tiếng Pháp · <b>по-францу́зски</b> bằng tiếng Pháp.</div>'
)

S["деревня"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дерев-</span>'
    '<span class="hd-gloss">gốc còn tranh cãi (xem ô đỏ)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ня</span>'
    '<span class="hd-gloss">đuôi hay chỉ NƠI CHỐN: <b>спа́льня</b> chỗ ngủ, '
    '<b>пека́рня</b> chỗ nướng bánh</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi <b>-ня</b> đặt tên cho một CHỖ, và <b>дере́вня</b> là '
    'chỗ người ta ở ngoài thành phố. Ở quê thì nói <b>в дере́вне</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: nhiều người nối <b>дере́вня</b> với '
    '<b>де́рево</b> (cây) cho dễ nhớ, nhưng từ điển từ nguyên nghiêng về gốc '
    '<b>драть</b> — "đất phát quang khỏi rừng". Từ nguyên còn tranh cãi, đừng coi '
    'là luật.</div>'
    '<div class="hd-warn">Số nhiều lệch hai chỗ: cách 2 chèn thêm chữ <b>е</b> vào '
    'giữa (<b>дереве́нь</b>), và từ cách 2 trở đi trọng âm nhảy xuống đuôi — '
    '<b>деревня́м</b>, <b>деревня́ми</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дереве́нский</b> thuộc làng quê, nhà quê.</div>'
)


# ---- ĐỀ BÀI tiếng Việt (README §2c): chỉ sửa từ nào đang có nhiều hơn 1 đáp án.
# Không ghi từ loại / giống / thể — mặt đề bài đã in sẵn badge.
V = {
    'университет': 'trường đại học',
    'институт': 'viện nghiên cứu, học viện, trường đại học chuyên ngành',
    'академия': 'viện hàn lâm, học viện',
    'деревня': 'làng nhỏ, xóm, vùng quê, nông thôn',
    'кинотеатр': 'rạp chiếu phim',
    'автомобиль': 'ô tô, xe hơi',
    'проспект': 'đại lộ, tờ giới thiệu',
    'площадь': 'quảng trường, diện tích',
    'театр': 'nhà hát, kịch nghệ',
    'центр': 'trung tâm, chỗ chính giữa',
}
