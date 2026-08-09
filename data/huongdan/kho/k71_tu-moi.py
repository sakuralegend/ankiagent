# -*- coding: utf-8 -*-
"""k71 — tu-moi: người (họ hàng · nghề nghiệp) + hành động gặp gỡ / tìm kiếm.

Các từ KHÔNG cùng một họ, nên mỗi thẻ đứng độc lập, không có khối hệ thống dùng chung.
"""

S = {}

S["внучка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вну́к-</span>'
    '<span class="hd-gloss">cháu</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ч-</span>'
    '<span class="hd-gloss">← <b>к</b> mềm đi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Lấy <b>внук</b> (cháu trai) gắn thêm đuôi giống cái <b>-ка</b>; '
    'chữ <b>к</b> cuối gốc đứng trước <b>-ка</b> buộc phải đổi thành <b>ч</b> — đúng phép '
    'biến âm <b>г/к/х → ж/ч/ш</b> gặp khắp nơi.</div>'
    '<div class="hd-warn">Số nhiều cách 2 chèn thêm <b>е</b> cho đọc được: <b>вну́чек</b>, '
    'chứ không phải «внучк».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>внук</b> cháu trai — cùng một gốc, đây là dạng giống đực.</div>'
)

S["встать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">vào, lên</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ста-</span>'
    '<span class="hd-gloss">ĐỨNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>-ста-</b> là "đứng" — nhận ra nó ở <b>стоя́ть</b> (đứng), '
    '<b>остано́вка</b> (chỗ dừng). Thêm <b>в-</b> "chuyển vào thế đứng" ⇒ đứng dậy, và nếu '
    'đang nằm trên giường thì là thức dậy.</div>'
    '<div class="hd-warn">Thì tương lai mọc thêm một chữ <b>н</b> không có trong nguyên thể: '
    '<b>вста́ну, вста́нешь…</b> — chỗ này phải nhớ, không suy ra được.</div>'
    '<div class="hd-warn"><b>встать</b> và <b>уста́ть</b> (mệt lử) cùng gốc, chia giống hệt '
    'nhau (<b>вста́ну / уста́ну</b>) — đổi mỗi tiền tố mà nghĩa lệch hẳn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>стоя́ть</b> đứng · <b>поста́вить</b> đặt đứng lên · '
    '<b>вста́вить</b> chèn vào · <b>остано́вка</b> chỗ dừng</div>'
)

S["встретить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">встре́т-/встре́ч-</span>'
    '<span class="hd-gloss">gốc GẶP</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi lớp chia 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một gốc hai mặt chữ: <b>т</b> ở nguyên thể, <b>ч</b> ở danh từ '
    '<b>встре́ча</b> (cuộc gặp). Đây là thể hoàn thành: gặp được MỘT lần, xong việc.</div>'
    '<div class="hd-warn">Chỉ ngôi «tôi» đổi <b>т → ч</b>: <b>я встре́чу</b>; năm ngôi còn '
    'lại giữ nguyên <b>т</b>: <b>встре́тишь, встре́тит…</b></div>'
    '<div class="hd-warn">Gặp AI thì người đó ở cách 4, không cần giới từ. Muốn nói "gặp '
    'NHAU" phải chuyển sang dạng phản thân <b>встре́титься</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>встреча́ть</b> thể chưa hoàn thành · <b>встре́титься</b>, '
    '<b>встреча́ться</b> gặp nhau · <b>встре́ча</b> cuộc gặp</div>'
)

S["встречать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">встреч-</span>'
    '<span class="hd-gloss">gốc GẶP</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc <b>встре́тить</b>, chỉ đổi đuôi thành <b>-а́ть</b> để kéo '
    'dài hành động ⇒ đang gặp, hay gặp. Bù lại nó chia đều tay <b>встреча́ю, встреча́ешь…</b>, '
    'không biến âm ngôi nào.</div>'
    '<div class="hd-warn">Nghĩa thứ hai dùng hằng ngày: RA ĐÓN người mới tới — đón ở nhà ga, '
    'sân bay. Vẫn là "gặp", chỉ khác ở chỗ mình chủ động chờ sẵn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>встре́тить</b> thể hoàn thành · <b>встреча́ться</b> gặp gỡ, hẹn hò '
    '· <b>встре́ча</b> cuộc gặp</div>'
)

S["гид"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn thẳng tiếng Pháp <i>guide</i>, một âm tiết, '
    'không mang tiền tố hay hậu tố Nga nào.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng chữ <i>guide</i> của tiếng Anh viết lại bằng chữ Nga: <b>г</b> '
    'thay <i>g</i>, bỏ <i>-e</i> câm. Một âm tiết nên trọng âm không có chỗ nào để dịch: '
    '<b>гид, ги́да, ги́ды</b> đều nhấn đúng chỗ đó.</div>'
    '<div class="hd-warn"><b>гид</b> luôn là danh từ giống đực, kể cả khi người hướng dẫn là '
    'phụ nữ — tính từ đi kèm vẫn để giống đực: <b>наш гид</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">Tiếng Nga không đẻ ra từ phái sinh nào từ <b>гид</b>; chỉ có từ ghép '
    '<b>аудиоги́д</b> máy thuyết minh trong bảo tàng.</div>'
)

S["искать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">иск-/ищ-</span>'
    '<span class="hd-gloss">gốc TÌM</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vào thì hiện tại, gốc <b>иск-</b> biến thành <b>ищ-</b> '
    '(<b>ск → щ</b>), nên bản hiện tại trông khác hẳn nguyên thể: <b>ищу́, и́щешь, и́щут</b> '
    '— thấy <b>ищ-</b> là biết đang nói về <b>иска́ть</b>.</div>'
    '<div class="hd-warn">Trọng âm chỉ nhảy ra đuôi ở ngôi «tôi»: <b>ищу́</b>; năm ngôi còn '
    'lại kéo về gốc: <b>и́щешь, и́щет…</b></div>'
    '<div class="hd-warn"><b>иска́ть</b> mới chỉ là ĐANG tìm, không hứa thấy. "Tìm ra" là một '
    'từ khác hẳn, không cùng gốc: <b>найти́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>по́иск</b> sự tìm kiếm (chữ trên nút tìm) · <b>иска́тель</b> '
    'người đi tìm</div>'
)

S["клиент"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кли-</span>'
    '<span class="hd-gloss">Latin <i>cliens</i>: người nhờ cậy</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́нт</span>'
    '<span class="hd-gloss">đuôi chỉ NGƯỜI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi <b>-е́нт/-а́нт</b> mượn từ Latin, gắn vào là ra tên một hạng '
    'NGƯỜI: <b>студе́нт</b>, <b>пацие́нт</b>, <b>официа́нт</b>. Trọng âm nằm ngay trên đuôi đó '
    'và không dịch đi đâu: <b>клие́нт, клие́нта, клие́нтов</b>.</div>'
    '<div class="hd-warn">Tiếng Anh tách <i>client</i> với <i>customer</i>; tiếng Nga gộp cả '
    'hai vào <b>клие́нт</b> — khách của ngân hàng lẫn khách của quán đều gọi thế.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">Cùng đuôi <b>-ент/-ант</b>: <b>пацие́нт</b> bệnh nhân · '
    '<b>студе́нт</b> sinh viên · <b>официа́нт</b> phục vụ bàn</div>'
)

S["пациент"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">паци-</span>'
    '<span class="hd-gloss">Latin <i>pati</i>: chịu đựng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́нт</span>'
    '<span class="hd-gloss">đuôi chỉ NGƯỜI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc Latin với <i>patient</i> tiếng Anh, nghĩa đen là "người '
    'đang chịu đựng". Tiếng Anh giữ cả hai nhánh nghĩa, tiếng Nga chỉ mượn nhánh người '
    'đang chữa bệnh.</div>'
    '<div class="hd-warn">Nên đừng suy ngược: <b>пацие́нт</b> không bao giờ mang nghĩa "kiên '
    'nhẫn" như <i>patient</i>; kiên nhẫn là <b>терпели́вый</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">Cùng đuôi <b>-ент</b> chỉ người: <b>клие́нт</b> khách hàng · '
    '<b>студе́нт</b> sinh viên</div>'
)

S["племянник"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">племя́н-</span>'
    '<span class="hd-gloss">← <b>пле́мя</b> dòng giống</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ник</span>'
    '<span class="hd-gloss">đuôi chỉ NGƯỜI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: "người trong dòng giống mình", tức con của anh/chị/em '
    'ruột. Mẹo phân biệt: ai gọi mình bằng <b>дя́дя</b>/<b>тётя</b> thì là '
    '<b>племя́нник</b>; ai gọi mình bằng ông/bà mới là <b>внук</b>.</div>'
    '<div class="hd-warn">Viết HAI chữ <b>н</b>: <b>племя́н-</b> đã có sẵn một <b>н</b>, đuôi '
    '<b>-ник</b> thêm chữ thứ hai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>племя́нница</b> cháu gái (con anh chị em) · <b>пле́мя</b> bộ tộc, '
    'dòng giống</div>'
)

S["повар"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố, không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вар-</span>'
    '<span class="hd-gloss">ĐUN, NẤU SÔI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>вар-</b> là "đun sôi": nó nằm trong <b>самова́р</b> '
    '(<i>само-</i> tự + <i>вар</i> đun = ấm tự đun) và <b>варе́нье</b> (mứt, quả nấu với '
    'đường). Người lo việc đun nấu ⇒ <b>по́вар</b>.</div>'
    '<div class="hd-warn">Số nhiều đổi cả đuôi lẫn trọng âm: <b>по́вар → повара́</b>, không '
    'phải «повары»; rồi nhấn cuối suốt: <b>поваро́в, повара́м</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ва́ренный</b> luộc, nấu chín · <b>самова́р</b> ấm tự đun · '
    '<b>варе́нье</b> mứt quả</div>'
)

S["приглашать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">tới gần, về phía mình</span></div>'
    '<div class="hd-row"><span class="hd-piece">-глаш-/-глас-</span>'
    '<span class="hd-gloss">TIẾNG GỌI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cất tiếng gọi ai đó về phía mình ⇒ mời. Thể hoàn thành trả '
    '<b>ш</b> về lại <b>с</b>: <b>пригласи́ть</b> — cặp thể của từ này chỉ khác nhau đúng '
    'chỗ đó.</div>'
    '<div class="hd-warn">Người được mời để ở CÁCH 4: <b>приглаша́ю тебя́</b>; nơi đến thì '
    'thêm <b>в</b> hoặc <b>на</b> rồi cũng cách 4.</div>'
    '<div class="hd-warn"><b>звать</b> cũng dịch được là "mời" nhưng nghiêng về gọi to, gọi '
    'tên; lời mời hẳn hoi thì dùng <b>приглаша́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>го́лос</b> giọng nói · <b>приглаше́ние</b> lời mời</div>'
)

S["сосед"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">cùng, chung</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сед-</span>'
    '<span class="hd-gloss">NGỒI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiền tố <b>со-</b> "cùng nhau" đóng đúng vai của <i>co-</i> trong '
    '<i>co-worker</i>; ghép với gốc "ngồi" ra "người ngồi cạnh mình" ⇒ hàng xóm. Cùng gốc đó '
    'có <b>сиде́ть</b> ngồi.</div>'
    '<div class="hd-warn">Số nhiều bỏ hẳn bộ đuôi cứng, chuyển sang đuôi MỀM: '
    '<b>сосе́ди, сосе́дей, сосе́дям</b> — không phải «соседы, соседов».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сосе́дка</b> nữ hàng xóm · <b>сосе́дний</b> bên cạnh, kế bên</div>'
)

S["улыбка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лыб-</span>'
    '<span class="hd-gloss">nhếch mép cười</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">động từ → danh từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Lấy động từ <b>улыба́ться</b> (mỉm cười), bỏ đuôi động từ, thêm '
    '<b>-ка</b> là ra tên của chính hành động đó — đúng khuôn đã gặp ở <b>остано́вка</b> '
    '(dừng → chỗ dừng) và <b>оши́бка</b> (nhầm → lỗi).</div>'
    '<div class="hd-warn">Cả ba từ <b>-ка</b> đó đều chèn thêm nguyên âm ở số nhiều cách 2: '
    '<b>улы́бок, остано́вок, оши́бок</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>улыба́ться</b> mỉm cười · cùng khuôn <b>-ка</b>: '
    '<b>остано́вка</b>, <b>оши́бка</b></div>'
)

# --- Field Vietnamese (đề bài deck 1-go) — README §2c ---------------------
V = {
    "внучка": "cháu gái, cháu nội, cháu ngoại",
    "встретить": "gặp",
    "встречать": "gặp, đón",
    "племянник": "cháu trai",
}
