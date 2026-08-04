# -*- coding: utf-8 -*-
"""k32 — people::body: bộ phận cơ thể, phần lớn là GỐC TRƠN không chẻ được.

Trục của lô: cái đáng dạy ở đây không phải cấu tạo từ (các từ này là gốc cổ,
không có tiền tố/hậu tố để chẻ) mà là (1) chỗ trọng âm NHẢY trong bảng chia —
голова́/нога́/рука́ cùng một kiểu, глаз và у́хо mỗi từ một kiểu riêng — và
(2) các cặp dễ lẫn: нёбо/не́бо, вдох/вздох, у́ха/уха́, нож/нога́.
Hai từ duy nhất chẻ được là вдох và вы́дох (tiền tố в- ↔ вы- trên cùng gốc -дох-).
"""

S = {}

S["голова"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc trơn <b>голов-</b> "đầu", không chẻ thêm được. Cái đáng nhớ là '
    'bộ đôi âm: dạng Nga thuần có <b>-оло-</b> (<b>голова́</b>), dạng Slav nhà thờ rút gọn '
    'thành <b>-ла-</b> — nên <b>гла́вный</b> (chính, chủ yếu) và <b>глава́</b> (chương sách) '
    'chính là cùng một gốc với nó.</div>'
    '<div class="hd-warn">⚠️ Trọng âm nhảy: <b>голова́</b> nhưng cách 4 <b>го́лову</b>, '
    'số nhiều <b>го́ловы</b>. Đuôi giữ trọng âm ở phần lớn ô, thân từ chỉ giành lại đúng ở '
    'cách 4 số ít và ở số nhiều.</div>'
    '<div class="hd-warn">⚠️ Thuộc cụm <b>от головы́ до ног</b> — từ đầu đến chân.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>голо́вка</b> đầu nhỏ; củ (tỏi) · <b>заголо́вок</b> tiêu đề · '
    '<b>гла́вный</b> chính, chủ yếu · <b>глава́</b> chương sách</div>'
)

S["нога"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc trơn <b>ног-</b>, không chẻ được. Thứ mở khoá cả một lớp từ là '
    'phép biến âm <b>г → ж</b> khi thêm hậu tố: <b>нога́</b> → <b>но́жка</b> (chân nhỏ; chân '
    'bàn ghế). Luật này lặp lại ở hầu hết từ có <b>г</b> cuối gốc.</div>'
    '<div class="hd-warn">⚠️ Trọng âm nhảy y hệt <b>голова́</b>: <b>нога́</b>, cách 2 <b>ноги́</b>, '
    'nhưng cách 4 <b>но́гу</b> và số nhiều <b>но́ги</b>. Cách 2 số nhiều rụng sạch đuôi: <b>ног</b>.</div>'
    '<div class="hd-warn">⚠️ <b>нож</b> (con dao) KHÔNG cùng gốc — giống nhau ba chữ đầu chỉ là tình cờ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>но́жка</b> chân nhỏ; chân bàn ghế · <b>подно́жка</b> bậc lên xe; cú ngáng chân</div>'
)

S["рука"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc trơn <b>рук-</b>. Cùng luật biến âm như <b>нога́</b>, ở đây là '
    '<b>к → ч</b>: <b>рука́</b> → <b>ру́чка</b> (cái bút; tay nắm cửa), <b>ручно́й</b> (bằng tay).</div>'
    '<div class="hd-warn">⚠️ Tiếng Nga KHÔNG tách "bàn tay" với "cánh tay" — <b>рука́</b> ôm cả hai. '
    'Muốn nói riêng phần lòng bàn tay mới dùng <b>ладо́нь</b>.</div>'
    '<div class="hd-warn">⚠️ Trọng âm nhảy cùng kiểu <b>голова́</b>: <b>рука́</b>, cách 2 <b>руки́</b>, '
    'nhưng cách 4 <b>ру́ку</b>, số nhiều <b>ру́ки</b>, cách 2 số nhiều <b>рук</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ру́чка</b> cái bút; tay nắm · <b>ручно́й</b> bằng tay; đã thuần · '
    '<b>рука́в</b> tay áo · <b>руководи́тель</b> người lãnh đạo</div>'
)

S["коса"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một mặt chữ, ba nghĩa rời nhau: <b>коса́</b> = bím tóc · lưỡi hái (dao '
    'dài để cắt cỏ) · doi cát chạy dài ra biển. Nghĩa "lưỡi hái" nối thẳng với động từ '
    '<b>коси́ть</b> (cắt cỏ); hai nghĩa kia đều là hình ảnh một dải dài thắt lại.</div>'
    '<div class="hd-warn">⚠️ Số ít trọng âm ở đuôi (<b>коса́</b>, <b>косы́</b>, <b>косе́</b>), '
    'sang số nhiều nhảy về thân: <b>ко́сы</b>, <b>кос</b>, <b>ко́сам</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: "bím tóc" và "lưỡi hái" có chung gốc cổ hay chỉ trùng mặt chữ '
    'thì từ nguyên còn tranh cãi — cứ học như hai từ riêng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>коси́ть</b> cắt cỏ bằng lưỡi hái · <b>коса́рь</b> thợ cắt cỏ · '
    '<b>коси́лка</b> máy cắt cỏ</div>'
)

S["глаз"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc trơn <b>глаз-</b>, không chẻ được. Đây là từ "mắt" đời thường; '
    'tiếng Nga cổ dùng <b>о́ко</b>, nay chỉ còn trong thơ và trong vài từ phái sinh.</div>'
    '<div class="hd-warn">⚠️ Số nhiều lấy đuôi <b>-а́</b> chứ không phải <b>-ы</b>: <b>глаза́</b>, '
    'cách 2 rụng sạch đuôi thành <b>глаз</b>. Sau <b>в</b> có dạng riêng <b>в глазу́</b>.</div>'
    '<div class="hd-warn">⚠️ <b>очки́</b> (cái kính) KHÔNG mọc ra từ <b>глаз</b> mà từ <b>о́ко</b> — '
    'hai gốc khác nhau cùng chỉ con mắt.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>глазно́й</b> thuộc về mắt · <b>глазо́к</b> mắt nhỏ; lỗ nhòm ở cửa</div>'
)

S["нёбо"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không chẻ được. Chữ <b>ё</b> luôn mang trọng âm, nên cả bảng chia của từ '
    'này không có dấu trọng âm nào cả. Nghĩa hẹp: cái "trần" của khoang miệng, phần vòm phía '
    'trên lưỡi.</div>'
    '<div class="hd-warn">⚠️ <b>нёбо</b> (vòm miệng) và <b>не́бо</b> (bầu trời) khác nhau đúng một chữ '
    'mà là hai từ hoàn toàn khác. Từ nguyên coi vòm miệng là "bầu trời của cái miệng" — nhớ được '
    'thì khỏi lẫn nghĩa, nhưng khi gõ vẫn phải chọn đúng <b>ё</b> hay <b>е</b>.</div>'
)

S["ухо"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc trơn <b>ух-</b>. Ở số nhiều và ở mọi từ phái sinh nó đổi thành '
    '<b>уш-</b> (<b>у́ши</b>, <b>ушно́й</b>, <b>нау́шники</b>) — đúng phép biến âm <b>х → ш</b>.</div>'
    '<div class="hd-warn">⚠️ Số nhiều đổi cả thân lẫn trọng âm: cách 1 và 4 là <b>у́ши</b>, còn các '
    'cách gián tiếp đẩy trọng âm ra đuôi — <b>уше́й</b>, <b>уша́м</b>, <b>уша́ми</b>.</div>'
    '<div class="hd-warn">⚠️ <b>у́ха</b> (cách 2 của "tai") trùng mặt chữ với <b>уха́</b> (canh cá) — '
    'chỉ chỗ đặt trọng âm tách được hai từ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ушно́й</b> thuộc về tai · <b>нау́шники</b> tai nghe</div>'
)

S["вдох"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дох-</span>'
    '<span class="hd-gloss">THỞ (biến thể của дых-/дух-)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">"Thở" + "vào" = hơi hít vào. Cùng gốc với <b>дыша́ть</b> (thở) và '
    '<b>во́здух</b> (không khí) — chính thứ được hít vào.</div>'
    '<div class="hd-warn">⚠️ <b>вдох</b> (hơi hít vào) khác <b>вздох</b> (tiếng thở dài) đúng một '
    'chữ <b>з</b>. Hai từ, hai nghĩa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вдохну́ть</b> hít vào · <b>вдыха́ть</b> đang hít vào · '
    '<b>дыша́ть</b> thở · <b>во́здух</b> không khí</div>'
)

S["выдох"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span>'
    '<span class="hd-gloss">RA NGOÀI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дох-</span>'
    '<span class="hd-gloss">THỞ (cùng gốc với вдох)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc <b>-дох-</b> với <b>вдох</b>, chỉ đổi tiền tố: <b>в-</b> (vào) '
    '↔ <b>вы-</b> (ra ngoài). Nên <b>вдох</b> là hơi hít vào, <b>вы́дох</b> là hơi thở ra.</div>'
    '<div class="hd-warn">⚠️ Tiền tố <b>вы-</b> hút trọng âm về chính nó ở danh từ và động từ hoàn '
    'thành: <b>вы́дох</b>, <b>вы́ход</b>, <b>вы́дохнуть</b> — riêng dạng chưa hoàn thành '
    '<b>выдыха́ть</b> thì trả trọng âm về đuôi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вы́дохнуть</b> thở ra · <b>выдыха́ть</b> đang thở ra · '
    '<b>вы́ход</b> lối ra</div>'
)

S["грудь"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc trơn <b>груд-</b>, không chẻ được. Danh từ giống cái tận cùng bằng dấu '
    'mềm <b>-ь</b>: cách 2 và cách 3 số ít đều là <b>гру́ди</b>, cách 5 lấy đuôi <b>-ью</b> → '
    '<b>гру́дью</b>. Từ này chỉ cả lồng ngực lẫn bầu ngực.</div>'
    '<div class="hd-warn">⚠️ Cách 6 đẩy trọng âm ra đuôi: <b>в груди́</b> (trong lồng ngực). '
    'Số nhiều cũng đẩy — <b>груде́й</b>, <b>грудя́м</b> — dù cách 1 vẫn là <b>гру́ди</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>грудно́й</b> thuộc về ngực; còn bú (<b>грудно́й ребёнок</b> trẻ sơ sinh) · '
    '<b>гру́дка</b> ức gà</div>'
)

S["ладонь"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không chẻ được. Phân vai cho rõ: <b>ладо́нь</b> chỉ đúng phần lòng bàn tay '
    '(mặt trong, chỗ trũng), còn cả bàn tay lẫn cánh tay đều gọi là <b>рука́</b>. Bảng chia đều '
    'đặn, trọng âm đứng yên một chỗ ở mọi ô.</div>'
    '<div class="hd-warn">⚠️ Thuộc cụm <b>как на ладо́ни</b> — "rõ như trong lòng bàn tay", tức '
    'nhìn thấy rành rành, không giấu được gì.</div>'
)

S["сыпь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сып-</span>'
    '<span class="hd-gloss">RẮC, VÃI (thứ dạng hạt)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ь</span>'
    '<span class="hd-gloss">dấu mềm khép lại: động từ → danh từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Suy thẳng từ động từ <b>сы́пать</b> (rắc, đổ thứ dạng hạt): <b>сыпь</b> '
    'là cái được "rắc" lên da — những nốt ban nổi rải rác.</div>'
    '<div class="hd-warn">⚠️ Đây là NỐT BAN, mẩn đỏ do dị ứng hoặc sốt phát ban — không phải mụn '
    'trứng cá (<b>прыщ</b>) và cũng không phải tên một căn bệnh da nào.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сы́пать</b> rắc, đổ · <b>сы́паться</b> rơi lả tả · '
    '<b>на́сыпь</b> nền đắp, bờ đắp (đường ray)</div>'
)


# ── VIỆC THỨ HAI: field `Vietnamese` = ĐỀ BÀI deck 1-go (README §2c) ───────────
# Không ghi từ loại/giống/thể — bốn badge trên mặt đề bài đã in sẵn.
V = {
    # từ điển ghi "đầu, trí tuệ, ý kiến, người đứng đầu": "ý kiến" không phải nghĩa
    # của голова, còn "người đứng đầu" đụng đúng chữ đã dùng cho `метр`.
    "голова": "đầu (bộ phận cơ thể)",
    # нога ôm cả cẳng chân lẫn bàn chân; bản cũ tách "chân (cơ thể)/chân (động vật)"
    # là hai nhánh không tồn tại trong tiếng Nga.
    "нога":   "chân (cả cẳng chân lẫn bàn chân)",
    # bỏ "nét chữ viết tay" — nghĩa hiếm, và để trong đề bài thì đụng по́черк.
    "рука":   "tay (cả cánh tay lẫn bàn tay)",
    # từ điển ĐÁNH RƠI nghĩa "lưỡi hái" (gloss Anh có "scythe") và thay bằng "doi cát".
    "коса":   "bím tóc (cùng mặt chữ còn là: lưỡi hái, doi cát)",
    # "lưỡi gà" là uvula (язычо́к), KHÔNG phải нёбо. Bỏ.
    "нёбо":   "vòm miệng (trần của khoang miệng)",
    # вдох ↔ выдох phải tách dứt khoát: cả hai đều là DANH TỪ chỉ một nhịp thở.
    "вдох":   "hơi hít vào (một nhịp hít)",
    "выдох":  "hơi thở ra (một nhịp thở ra)",
    # từ điển nới "rash" thành cả lớp "bệnh da liễu", lại thêm "mụn" (= прыщ).
    "сыпь":   "nốt ban, mẩn đỏ trên da",
}
