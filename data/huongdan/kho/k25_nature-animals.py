# -*- coding: utf-8 -*-
"""k25 — nature::animals: tên loài vật, nơi cái khó không nằm ở nghĩa mà ở THÂN TỪ —
gần nửa lô có nguyên âm rơi mất hoặc trọng âm nhảy ra đuôi ngay khi thêm đuôi."""

# 🔴 KHÔNG dựng biến khối dùng chung (HE/LUAT/THE…) rồi cộng vào mọi thẻ (README §3).

S = {}

S["рыба"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ры́б-</span>'
    '<span class="hd-gloss">CÁ — gốc, giữ nguyên mặt chữ trong cả họ từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi -а ⇒ giống cái, biến cách đều</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thấy chuỗi <b>ры́б-</b> mở đầu một từ lạ thì gần như chắc từ đó '
    'dính tới cá: nghề cá, món cá, người đánh cá.</div>'
    '<div class="hd-warn">Cụm phải thuộc: <b>как ры́ба в воде́</b> — “như cá gặp nước”, '
    'ở đâu cũng thấy thoải mái, thạo việc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рыба́к</b> người đánh cá · <b>рыболо́в</b> người câu cá · '
    '<b>ры́бный</b> thuộc về cá · <b>ры́бка</b> con cá nhỏ</div>'
)

S["коза"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">коз-</span>'
    '<span class="hd-gloss">DÊ — gốc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́</span>'
    '<span class="hd-gloss">đuôi giống cái, và ở số ít nó GIỮ trọng âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Con vật quen nên tiếng Nga tách hẳn hai từ: <b>коза́</b> là dê cái '
    'và cũng là từ nói chung về loài dê, <b>козёл</b> là dê đực.</div>'
    '<div class="hd-warn">Trọng âm nhảy: số ít nằm ở đuôi (<b>коза́</b>, <b>козы́</b>), '
    'sang số nhiều rút về gốc (<b>ко́зы</b>, <b>ко́зам</b>). Nhớ cặp <b>коза́ / ко́зы</b> '
    'là nhớ được cả bảng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>козёл</b> dê đực · <b>козлёнок</b> dê con · '
    '<b>ко́зий</b> (sữa, thịt) dê</div>'
)

S["белка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бе́л-</span>'
    '<span class="hd-gloss">gốc, cùng mặt chữ với бе́лый (trắng)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">đuôi -а ⇒ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tên con sóc được cho là bắt nguồn từ một giống sóc lông trắng thời '
    'cổ, chứ không phải từ màu lông nâu bạn thấy ngoài công viên.</div>'
    '<div class="hd-warn">⚠️ Mức tin: <b>бе́лка</b> ↔ <b>бе́лый</b> là từ nguyên (giả thuyết '
    'phổ biến), không phải luật suy ra được — đừng nhân cách nối này ra từ khác.</div>'
    '<div class="hd-warn">Số nhiều cách 2 chèn thêm «о»: <b>пять бе́лок</b> (năm con sóc). '
    'Đừng lẫn với <b>бело́к</b> = lòng trắng trứng, chất đạm: cùng mặt chữ, khác trọng âm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бельчо́нок</b> sóc con · <b>бе́личий</b> thuộc về sóc</div>'
)

S["кошка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кош-</span>'
    '<span class="hd-gloss">MÈO — gốc, biến từ кот (т đổi thành ш)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">đuôi -а ⇒ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Phép đổi т → ш trước đuôi mềm còn gặp lại ở <b>коша́чий</b>; '
    'nhận ra nó là đọc được cả nhóm từ về mèo.</div>'
    '<div class="hd-warn">Chọn từ: <b>ко́шка</b> là mèo cái, và cũng là từ mặc định khi nói '
    'chung về loài mèo; <b>кот</b> chỉ dùng cho mèo đực.</div>'
    '<div class="hd-warn">Số nhiều cách 2 chèn «е»: <b>мно́го ко́шек</b> (nhiều mèo) — '
    'thân ко́шк- không đứng trần được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кот</b> mèo đực · <b>котёнок</b> mèo con · '
    '<b>коша́чий</b> thuộc về mèo</div>'
)

S["муха"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">му́х-</span>'
    '<span class="hd-gloss">RUỒI — gốc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi -а ⇒ giống cái, biến cách đều</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">х cuối gốc đổi thành ш khi thêm đuôi nhỏ: <b>му́ха</b> → '
    '<b>му́шка</b>. Đây là phép biến âm chạy khắp tiếng Nga: г/к/х → ж/ч/ш.</div>'
    '<div class="hd-warn">Thành ngữ rất hay gặp: <b>де́лать из му́хи слона́</b> — '
    '“biến con ruồi thành con voi”, tức chuyện bé xé ra to.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>му́шка</b> con ruồi nhỏ; đầu ruồi để ngắm bắn · '
    '<b>мухомо́р</b> nấm ruồi (nấm độc đỏ đốm trắng)</div>'
)

S["лев"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">лев</span>'
    '<span class="hd-gloss">dạng trần, chỉ dùng ở cách 1</span></div>'
    '<div class="hd-row"><span class="hd-piece">льв-</span>'
    '<span class="hd-gloss">thân dùng cho mọi cách còn lại</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chữ е chỉ có mặt khi từ đứng trần; thêm bất cứ đuôi nào là nó rơi '
    'mất và trọng âm dồn ra đuôi.</div>'
    '<div class="hd-warn">Nguyên âm chạy: <b>льва́</b>, <b>льву́</b>, <b>льво́м</b>, '
    'số nhiều <b>львы́</b> — thân chỉ còn льв-.</div>'
    '<div class="hd-warn">Luật đúng cho mọi con vật: danh từ chỉ vật SỐNG lấy hình cách 2 '
    'làm cách 4 — <b>ви́жу льва́</b> (tôi thấy sư tử), không phải <i>ви́жу лев</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>льви́ца</b> sư tử cái · <b>львёнок</b> sư tử con · '
    '<b>льви́ный</b> thuộc về sư tử</div>'
)

S["ёж"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ёж</span>'
    '<span class="hd-gloss">dạng trần, chỉ dùng ở cách 1</span></div>'
    '<div class="hd-row"><span class="hd-piece">еж-</span>'
    '<span class="hd-gloss">thân khi thêm đuôi: ё đổi thành е</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chữ ё trong tiếng Nga luôn tự mang trọng âm, nên không bao giờ đóng '
    'thêm dấu lên nó. Khi thêm đuôi, trọng âm rời sang đuôi thì ё phải nhường chỗ cho е.</div>'
    '<div class="hd-warn">Bảng chia: <b>ежа́</b>, <b>ежу́</b>, <b>ежо́м</b>, số nhiều '
    '<b>ежи́</b> — trọng âm ra đuôi hết.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ёжик</b> chú nhím; kiểu tóc đầu đinh · '
    '<b>ежеви́ка</b> quả mâm xôi đen (bụi đầy gai như lưng nhím)</div>'
)

S["хек"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được: <b>хек</b> là tên thương mại châu Âu của '
    'loài cá này (Anh hake, Hà Lan heek) mượn nguyên khối vào tiếng Nga, nên không mảnh nào '
    'mang nghĩa riêng.</div>'
    '<div class="hd-why">Bù lại nó biến cách hoàn toàn đều và trọng âm đứng yên ở gốc — '
    'không có gì phải thuộc riêng. Cũng không có từ phái sinh Nga nào nên thẻ này bỏ hẳn '
    'mục Họ hàng.</div>'
    '<div class="hd-warn">Đừng lẫn tên cá: <b>хек</b> là cá biển thịt trắng, họ hàng gần của '
    '<b>треска́</b> (cá tuyết) nhưng là loài khác.</div>'
)

S["зяблик"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">зябл-</span>'
    '<span class="hd-gloss">từ зя́бнуть = chịu rét, bị cóng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ик</span>'
    '<span class="hd-gloss">đuôi tạo tên gọi giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen là “con chim chịu rét”: nó có mặt ở Nga từ đầu xuân còn '
    'lạnh tới tận cuối thu. Đuôi <b>-ик</b> ở đây chỉ tạo tên, không mang nghĩa nhỏ bé.</div>'
    '<div class="hd-warn">Nghĩa loài: <b>зя́блик</b> là chaffinch (Fringilla coelebs), '
    'chim sẻ nhỏ châu Âu ngực nâu hồng — không phải chim chích bông.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>зя́бнуть</b> bị lạnh, cóng · <b>озя́бнуть</b> cóng người (một lần) · '
    '<b>зя́бкий</b> hay thấy lạnh; lạnh lẽo</div>'
)

S["орёл"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">орёл</span>'
    '<span class="hd-gloss">dạng trần, chỉ dùng ở cách 1</span></div>'
    '<div class="hd-row"><span class="hd-piece">орл-</span>'
    '<span class="hd-gloss">thân khi thêm đuôi: ё rơi mất</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chữ ё chỉ sống được khi nó mang trọng âm; thêm đuôi là trọng âm ra '
    'đuôi, ё không còn chỗ đứng nên thân rút lại thành <b>орл-</b>.</div>'
    '<div class="hd-warn">Bảng chia: <b>орла́</b>, <b>орлу́</b>, <b>орло́м</b>, số nhiều '
    '<b>орлы́</b>.</div>'
    '<div class="hd-warn">Phải thuộc: <b>орёл и́ли ре́шка</b> = “ngửa hay sấp” khi tung đồng '
    'xu — mặt có đại bàng là mặt орёл.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>орли́ца</b> đại bàng cái · <b>орлёнок</b> đại bàng con · '
    '<b>орли́ный</b> (mũi, mắt) đại bàng</div>'
)

S["пёс"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пёс</span>'
    '<span class="hd-gloss">dạng trần, chỉ dùng ở cách 1</span></div>'
    '<div class="hd-row"><span class="hd-piece">пс-</span>'
    '<span class="hd-gloss">thân khi thêm đuôi: ё rơi mất</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trần thì có ё, thêm đuôi là ё rơi mất và trọng âm ra đuôi — '
    'thân chỉ còn hai phụ âm <b>пс-</b>.</div>'
    '<div class="hd-warn">Bảng chia: <b>пса́</b>, <b>псу́</b>, <b>псо́м</b>, số nhiều '
    '<b>псы́</b>.</div>'
    '<div class="hd-warn">Chọn từ: <b>соба́ка</b> là từ trung tính cho “con chó”; <b>пёс</b> '
    'là con chó đực, giọng dân dã, hay dùng cho chó to hoặc khi mắng người.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пёсик</b> cún, chó nhỏ · <b>пси́на</b> con chó to; mùi chó</div>'
)

S["кот"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кот-</span>'
    '<span class="hd-gloss">MÈO ĐỰC — gốc trơn; cách 1 không có đuôi ⇒ giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thêm đuôi -ка thì т đổi thành ш: <b>кот</b> → <b>ко́шка</b>. '
    'Hai từ cùng gốc nhưng dùng khác nhau.</div>'
    '<div class="hd-warn">Trọng âm không ở lại thân: <b>кота́</b>, <b>коту́</b>, '
    '<b>кото́м</b>, số nhiều <b>коты́</b>, <b>кото́в</b> — luôn ra đuôi.</div>'
    '<div class="hd-warn">Chọn từ: <b>кот</b> chỉ dùng cho mèo đực; nói chung về loài mèo '
    'thì dùng <b>ко́шка</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ко́шка</b> mèo cái, mèo nói chung · <b>котёнок</b> mèo con · '
    '<b>ко́тик</b> mèo cưng; hải cẩu lông</div>'
)

S["голубь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">го́луб-</span>'
    '<span class="hd-gloss">BỒ CÂU — gốc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ь</span>'
    '<span class="hd-gloss">dấu mềm khép cuối, không phải nguyên âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc này còn cho ra tên một màu: <b>голубо́й</b> (xanh da trời) — '
    'theo từ nguyên là màu ánh cổ chim bồ câu.</div>'
    '<div class="hd-warn">Đuôi -ь phần lớn báo giống cái, nhưng <b>го́лубь</b> là giống ĐỰC. '
    'Phải nhớ riêng, không suy ra được.</div>'
    '<div class="hd-warn">Số nhiều: cách 1 giữ trọng âm gốc <b>го́луби</b>, các cách còn lại '
    'dồn ra đuôi — <b>голубе́й</b>, <b>голубя́м</b>, <b>голубя́ми</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>голубо́й</b> xanh da trời · <b>голу́бка</b> bồ câu mái; “em yêu” · '
    '<b>голубя́тня</b> chuồng bồ câu</div>'
)

S["окунь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о́кун-</span>'
    '<span class="hd-gloss">gốc trơn, không chẻ nhỏ hơn được</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ь</span>'
    '<span class="hd-gloss">dấu mềm khép cuối, không phải nguyên âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đừng nối với <b>окуну́ть</b> (nhúng xuống nước): nghe rất giống '
    'nhưng khác gốc. <b>о́кунь</b> không có từ phái sinh thông dụng nên thẻ này bỏ hẳn mục '
    'Họ hàng.</div>'
    '<div class="hd-warn">Đuôi -ь thường báo giống cái, nhưng <b>о́кунь</b> giống ĐỰC. '
    'Số nhiều <b>о́куни</b> giữ trọng âm gốc, các cách còn lại ra đuôi: <b>окуне́й</b>, '
    '<b>окуня́м</b>.</div>'
    '<div class="hd-warn">Nghĩa loài: đây là cá rô châu Âu (perch), cá NƯỚC NGỌT vây gai '
    'lưng — không phải cá chạch, cũng không phải cá biển.</div>'
)


# ---------------------------------------------------------------------------
# Field `Vietnamese` — ĐỀ BÀI của deck 1-go, user nhìn dòng này rồi GÕ từ Nga.
# Chỉ sửa từ nào bản cũ để lọt nhiều hơn một đáp án đúng (README §2c).
# KHÔNG ghi từ loại / giống / thể — mặt đề bài đã in sẵn bốn badge.
V = {}

# кошка · кот · пёс: ba từ đâm nhau nặng nhất trong lô.
V['кошка'] = 'con mèo, mèo cái'
V["кот"] = "con mèo đực"
V['пёс'] = 'con chó đực, con chó'

# коза: 'con dê' trần để lọt cả козёл (dê đực).
V["коза"] = "con dê cái"

# ёж: 'con nhím' trần để lọt cả дикобраз (nhím lông dài).
V['ёж'] = 'con nhím gai'

# орёл: bản cũ ghi kèm nghĩa 'mặt ngửa đồng xu' -> đề bài hai đường, bỏ.
V["орёл"] = "con đại bàng"

# Ba tên loài dưới đây bản cũ dịch SAI hoặc quá mơ hồ — xem báo cáo lô.
V['зяблик'] = 'chim chaffinch, sẻ ngực hồng'
V['окунь'] = 'cá rô châu Âu, cá perch'
V['хек'] = 'cá hake'
