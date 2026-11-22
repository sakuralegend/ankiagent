# -*- coding: utf-8 -*-
"""k169 — language::communication (lô trộn): lời nói, giao tiếp, thời điểm, việc làm.

Chỗ cần nhất quán trong lô:
(1) họ предупреди́ть / предупрежда́ть / предупрежде́ние: gốc ПРЕД «trước» (như пе́ред), đọc
    пред-у-пред-: chữ пред hiện hai lần. д→жд lối Slav cổ — cùng kiểu твёрдый → утвержда́ть.
    Máy ghép ждать/дать = báo oan, không dùng.
(2) по́лдень / по́лночь: пол- = NỬA (như полови́на), KHÔNG phải пол- ĐẦY của по́лный.
    Giống theo vế sau: по́лдень giống đực (день), по́лночь giống cái (ночь).
(3) обеща́ние / приглаше́ние / про́сьба: chẻ khớp thẻ обеща́ть [k96], приглаша́ть [k71],
    проси́ть [k85].
(4) врать / навра́ть: thân вр- không có nguyên âm (вру, врёшь); навра́ть dẫn chiếu врать.
Họ hàng cố ý vắng: không có — từ mượn визи́т/ми́нимум vẫn có phái sinh Nga thật.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
# Thẻ đang có ngoặc (информационный, предупредить, наврать, формирование) là chú thích
# của USER — không viết V cho chúng.
V = {
    "предупреждение": "lời cảnh báo, sự báo trước, sự phòng ngừa",   # thiếu prevention
    "предупреждать": "cảnh báo, báo trước, ngăn ngừa",              # thiếu prevent/avert
    "утверждать": "khẳng định, quả quyết, phê duyệt",               # thiếu approve/ratify
    "общаться": "giao tiếp, trò chuyện, giao lưu",                  # thiếu socialize
    "покупка": "việc mua, món đồ đã mua, sự mua sắm",              # bỏ dấu ; + shopping
}

# --------------------------------------------------------------------- просьба
S["просьба"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">прос-</span>'
    '<span class="hd-gloss">XIN, THỈNH CẦU — gốc của <b>проси́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ьба</span>'
    '<span class="hd-gloss">đuôi danh từ chỉ việc, giống cái — như <b>борьба́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Việc xin ai làm gì ⇒ lời nhờ, lời đề nghị. Nhờ ai LÀM thì là '
    '<b>проси́ть</b>, còn hỏi để BIẾT là <b>спроси́ть</b> — danh từ này đi theo vế «nhờ».</div>'
    '<div class="hd-warn"><b>У меня́ к вам про́сьба.</b> — Tôi có việc muốn nhờ anh. '
    '<b>по про́сьбе</b> + cách 2 = theo lời đề nghị của ai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>проси́ть</b> xin, nhờ · <b>попроси́ть</b> (HT) · '
    '<b>вопро́с</b> câu hỏi · <b>спроси́ть</b> hỏi</div>'
)

# --------------------------------------------------------------------- обещание
S["обещание"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">bao quanh, ràng vào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ещ-</span>'
    '<span class="hd-gloss">gốc NÓI trang trọng, mặt cũ là <b>-вет-</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ние</span>'
    '<span class="hd-gloss">ra danh từ giống trung, từ <b>обеща́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Lời nói ra để tự ràng mình ⇒ lời hứa. Chính là danh từ của '
    '<b>обеща́ть</b>; mức tin của chuyện <b>-ещ-</b> = <b>-вет-</b> ghi ở thẻ đó.</div>'
    '<div class="hd-warn"><b>дать обеща́ние</b> = hứa · <b>сдержа́ть обеща́ние</b> = giữ lời hứa.'
    '</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обеща́ть</b> hứa · <b>пообеща́ть</b> (HT) · xa hơn, gốc '
    '<b>-вет-</b>: <b>отве́т</b> câu trả lời, <b>сове́т</b> lời khuyên</div>'
)

# --------------------------------------------------------------------- предупреждение
S["предупреждение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">предупрежд-</span>'
    '<span class="hd-gloss">thân của <b>предупреди́ть</b> báo TRƯỚC, <b>д→жд</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ние</span>'
    '<span class="hd-gloss">ra danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Việc báo TRƯỚC cho ai ⇒ lời cảnh báo; chặn TRƯỚC cái xấu ⇒ sự phòng '
    'ngừa. Cách chẻ gốc <b>пред</b> «trước» nằm ở thẻ <b>предупреди́ть</b>.</div>'
    '<div class="hd-warn"><b>без предупрежде́ния</b> — không báo trước: '
    '<b>Он пришёл без предупрежде́ния.</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>предупреди́ть</b> cảnh báo (HT) · <b>предупрежда́ть</b> (CHT) · '
    '<b>пе́ред</b> trước</div>'
)

# --------------------------------------------------------------------- приглашение
S["приглашение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">tới gần, về phía mình</span></div>'
    '<div class="hd-row"><span class="hd-piece">-глаш-</span>'
    '<span class="hd-gloss">TIẾNG GỌI — gốc <b>глас-</b>, tức <b>го́лос</b> giọng, tiếng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ние</span>'
    '<span class="hd-gloss">ra danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiếng gọi ai về phía mình ⇒ lời mời; viết ra giấy ⇒ thiếp mời. Danh từ của '
    '<b>приглаша́ть</b>, giữ <b>ш</b> như vế CHT.</div>'
    '<div class="hd-warn"><b>приглаше́ние на</b> + cách 4: <b>на сва́дьбу</b> mời dự cưới · '
    '<b>по приглаше́нию</b> + cách 2 = theo lời mời của ai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>приглаша́ть</b> mời · <b>пригласи́ть</b> (HT) · <b>го́лос</b> giọng · '
    '<b>соглаше́ние</b> thoả thuận</div>'
)

# --------------------------------------------------------------------- информационный
S["информационный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">информаци-</span>'
    '<span class="hd-gloss">thân của <b>информа́ция</b> thông tin</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́нный</span>'
    '<span class="hd-gloss">đuôi tính từ = <i>-ional</i> tiếng Anh</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chữ-đối-chữ <i>informational</i>. Trọng âm dời ra đuôi: '
    '<b>информа́ция</b> → <b>информацио́нный</b> — cùng khuôn <b>традицио́нный</b> truyền thống.</div>'
    '<div class="hd-warn"><b>информацио́нные техноло́гии</b> — công nghệ thông tin (IT).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>информа́ция</b> thông tin · <b>информи́ровать</b> thông báo · '
    '<b>фо́рма</b> hình dạng</div>'
)

# --------------------------------------------------------------------- визит
S["визит"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn (Pháp <i>visite</i>), không chẻ được — cùng gốc Latin với '
    '<i>visit</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cuộc thăm có tính chính thức hoặc lịch sự: <b>визи́т к врачу́</b> đi khám '
    'bác sĩ (<b>к</b> + cách 3). Bạn bè ghé chơi nhà nhau thì thường nói <b>идти́ в го́сти</b> '
    'hơn.</div>'
    '<div class="hd-warn"><b>нанести́ визи́т</b> + cách 3 — đến thăm ai (văn trang trọng).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>визи́тка</b> danh thiếp · <b>визи́тная ка́рточка</b> danh thiếp</div>'
)

# --------------------------------------------------------------------- предупредить
S["предупредить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пред-</span>'
    '<span class="hd-gloss">TRƯỚC — gốc của <b>пе́ред</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-у-пред-</span>'
    '<span class="hd-gloss">«làm trước, chặn trước»: <b>пред</b> lần thứ hai</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia 2, thể hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">TRƯỚC hai lần: báo trước để chặn trước ⇒ cảnh báo, báo trước, ngăn ngừa. '
    'Báo AI: cách 4; báo VỀ gì: <b>о</b> + cách 6 — <b>предупреди́ть дру́га об опа́сности</b>.</div>'
    '<div class="hd-warn">Ngôi «tôi» <b>д→ж</b>: <b>предупрежу́</b>. Còn <b>предупрежда́ть</b>, '
    '<b>предупрежде́ние</b> mang <b>жд</b> — lối Slav cổ, y như <b>твёрдый</b> → '
    '<b>утвержда́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>предупрежда́ть</b> (CHT) · <b>предупрежде́ние</b> lời cảnh báo · '
    '<b>пе́ред</b> trước · <b>вперёд</b> tiến lên</div>'
)

# --------------------------------------------------------------------- предупреждать
S["предупреждать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">предупрежд-</span>'
    '<span class="hd-gloss">пред-у-пред- TRƯỚC hai lần, <b>д→жд</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành, chia đều: <b>предупрежда́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vế CHT của <b>предупреди́ть</b>: cảnh báo nhiều lần, hoặc đang cảnh báo. '
    'Cùng cách đòi: AI ở cách 4, VỀ gì <b>о</b> + cách 6. Chẻ gốc kỹ ở thẻ '
    '<b>предупреди́ть</b>.</div>'
    '<div class="hd-warn"><b>Я тебя́ предупрежда́ю!</b> — Tôi cảnh cáo cậu đấy!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>предупреди́ть</b> (HT) · <b>предупрежде́ние</b> lời cảnh báo · '
    '<b>пе́ред</b> trước</div>'
)

# --------------------------------------------------------------------- утверждать
S["утверждать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">làm cho thành</span></div>'
    '<div class="hd-row"><span class="hd-piece">-твержд-</span>'
    '<span class="hd-gloss">CỨNG, CHẮC — chính là <b>твёрд-</b> của <b>твёрдый</b>, '
    '<b>д→жд</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm cho CHẮC: nói chắc ⇒ khẳng định; đóng dấu chắc ⇒ phê duyệt. Đúng hình '
    'ảnh của <i>af-firm</i>, <i>con-firm</i> (Latin <i>firmus</i> chắc) — giống cách nghĩ, không cùng '
    'gốc. Cặp HT: <b>утверди́ть</b>.</div>'
    '<div class="hd-warn"><b>Он утвержда́ет, что</b>… — anh ta quả quyết rằng… (thường hàm ý: '
    'chưa chắc đã đúng).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>твёрдый</b> cứng · <b>твёрдо</b> dứt khoát · '
    '<b>утвержде́ние</b> lời khẳng định · <b>утверди́ть</b> (HT)</div>'
)

# --------------------------------------------------------------------- врать
S["врать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn <b>вр-</b>, không chẻ được — thân không có nguyên âm nào.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chia theo thân trơ <b>вр-</b>: <b>вру, врёшь, врут</b>. Quá khứ giống cái '
    'dồn trọng âm ra đuôi: <b>врал, врала́, вра́ли</b>. Khẩu ngữ, thô hơn <b>лгать</b> — gần với '
    '«xạo». Cặp HT: <b>навра́ть</b>, <b>совра́ть</b>.</div>'
    '<div class="hd-warn"><b>Не ври!</b> — Đừng xạo! · <b>Часы́ вру́т.</b> — Đồng hồ chạy sai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>враньё</b> lời nói dối · <b>вру́н</b> kẻ hay nói dối · '
    '<b>навра́ть</b> nói dối (HT)</div>'
)

# --------------------------------------------------------------------- наврать
S["наврать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">đánh dấu XONG, kèm sắc thái «cả một mớ»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-врать</span>'
    '<span class="hd-gloss">chính là <b>врать</b> — nói dối</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đã nói dối ai (cách 3): <b>Он мне навра́л.</b> Còn nghĩa «làm sai, nhầm»: '
    '<b>навра́ть в расчётах</b> tính sai. Chia y như <b>врать</b>: <b>навру́, наврёшь</b>; quá '
    'khứ <b>наврала́</b>.</div>'
    '<div class="hd-warn"><b>навра́ть с три ко́роба</b> — nói dối cả ba bồ, bịa một đống.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>врать</b> nói dối (CHT) · <b>совра́ть</b> nói dối (HT) · '
    '<b>враньё</b> lời nói dối</div>'
)

# --------------------------------------------------------------------- общаться
S["общаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">общ-</span>'
    '<span class="hd-gloss">CHUNG — gốc của <b>о́бщий</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi động từ, chia đều: <b>обща́юсь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">với nhau, qua lại</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Có cái CHUNG qua lại với nhau ⇒ giao tiếp, giao lưu. Cùng gốc '
    '<b>сообща́ть</b> báo tin: ở đó là một chiều, ở đây là hai chiều.</div>'
    '<div class="hd-warn">Với AI: <b>с</b> + cách 5 — <b>обща́ться с друзья́ми</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обще́ние</b> sự giao tiếp · <b>о́бщий</b> chung · '
    '<b>о́бщество</b> xã hội · <b>сообща́ть</b> báo tin</div>'
)

# --------------------------------------------------------------------- вскоре
S["вскоре"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">trong</span></div>'
    '<div class="hd-row"><span class="hd-piece">-скор-</span>'
    '<span class="hd-gloss">NHANH — như <b>ско́ро</b>, <b>ско́рый</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е</span>'
    '<span class="hd-gloss">đuôi trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trong một quãng NHANH ⇒ chẳng bao lâu sau. Khác <b>ско́ро</b> «sắp» nhìn '
    'về tương lai, <b>вско́ре</b> hay dùng để kể chuyện đã qua: <b>Вско́ре он уе́хал.</b> Ít lâu '
    'sau anh ấy đi.</div>'
    '<div class="hd-warn"><b>вско́ре по́сле</b> + cách 2 — ngay sau khi: '
    '<b>вско́ре по́сле обе́да</b> ít lâu sau bữa trưa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ско́ро</b> sắp · <b>ско́рый</b> nhanh · <b>ско́рость</b> tốc độ</div>'
)

# --------------------------------------------------------------------- постепенно
S["постепенно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">theo từng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-степен-</span>'
    '<span class="hd-gloss">BẬC — từ <b>сте́пень</b> bậc, mức độ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-но</span>'
    '<span class="hd-gloss">tính từ <b>-ный</b> → trạng từ <b>-о</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Theo từng bậc một ⇒ dần dần. Đúng hình ảnh tiếng Anh <i>by degrees</i> — '
    '<i>degree</i> cũng là «bậc». Trọng âm dời: <b>сте́пень</b> → <b>постепе́нно</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>постепе́нный</b> dần dần (tính từ) · <b>сте́пень</b> bậc, mức độ</div>'
)

# --------------------------------------------------------------------- полдень
S["полдень"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пол-</span>'
    '<span class="hd-gloss">NỬA — như <b>полови́на</b> (không phải «đầy» của <b>по́лный</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-день</span>'
    '<span class="hd-gloss">NGÀY — chính là <b>день</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nửa ngày ⇒ giữa trưa, 12 giờ. Giống đực theo <b>день</b>. Các cách khác '
    '<b>пол-</b> nở lại thành <b>полу́-</b>, <b>е</b> của день rơi: <b>полу́дня</b>, '
    '<b>полу́днем</b> (cách 2 còn gặp <b>по́лдня</b>).</div>'
    '<div class="hd-warn"><b>до полу́дня</b> trước trưa · <b>по́сле полу́дня</b> buổi chiều — '
    'tức AM / PM.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>по́лночь</b> nửa đêm · <b>полови́на</b> một nửa · '
    '<b>полчаса́</b> nửa tiếng · <b>день</b> ngày</div>'
)

# --------------------------------------------------------------------- полночь
S["полночь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пол-</span>'
    '<span class="hd-gloss">NỬA — như <b>полови́на</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ночь</span>'
    '<span class="hd-gloss">ĐÊM — chính là <b>ночь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nửa đêm. Giống CÁI theo <b>ночь</b> — trong khi <b>по́лдень</b> giống đực '
    'theo <b>день</b>: giống do vế sau quyết định. Các cách khác <b>пол-</b> thành <b>полу́-</b>: '
    '<b>полу́ночи</b> (cũng gặp <b>по́лночи</b>).</div>'
    '<div class="hd-warn"><b>в по́лночь</b> lúc nửa đêm · <b>до полу́ночи</b> trước nửa đêm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>по́лдень</b> giữa trưa · <b>полови́на</b> một nửa · '
    '<b>полчаса́</b> nửa tiếng · <b>ночь</b> đêm</div>'
)

# --------------------------------------------------------------------- минимум
S["минимум"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn Latin <i>minimum</i>, không chẻ được — chữ-đối-chữ tiếng Anh.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mức thấp nhất. Còn đứng một mình như trạng từ «ít nhất»: <b>ми́нимум два '
    'часа́</b> ít nhất hai tiếng. Trái nghĩa: <b>ма́ксимум</b>.</div>'
    '<div class="hd-warn"><b>как ми́нимум</b> — ít nhất là, tối thiểu là.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>минима́льный</b> tối thiểu (trọng âm dời ra <b>-а́льный</b>)</div>'
)

# --------------------------------------------------------------------- покупка
S["покупка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố, không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-куп-</span>'
    '<span class="hd-gloss">MUA — như <b>купи́ть</b>, <b>покупа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một lần mua, hoặc món vừa mua về. Số nhiều cách 2 chèn <b>о</b>: '
    '<b>поку́пок</b>.</div>'
    '<div class="hd-warn"><b>де́лать поку́пки</b> — đi mua sắm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>покупа́ть</b> mua (CHT) · <b>купи́ть</b> mua (HT) · '
    '<b>покупа́тель</b> khách mua</div>'
)

# --------------------------------------------------------------------- формирование
S["формирование"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">форм-</span>'
    '<span class="hd-gloss">HÌNH, KHUÔN — chính là <b>фо́рма</b> (Latin <i>forma</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ирова-</span>'
    '<span class="hd-gloss">khuôn động từ mượn châu Âu: <b>формирова́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ние</span>'
    '<span class="hd-gloss">ra danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúc thành hình ⇒ sự hình thành, <i>formation</i>. Nghĩa thứ hai cũng y '
    'tiếng Anh: <i>formation</i> = một đội hình, đơn vị quân.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>фо́рма</b> hình dạng · <b>формирова́ть</b> hình thành · '
    '<b>информа́ция</b> thông tin</div>'
)

# --------------------------------------------------------------------- поступок
S["поступок"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố, nghĩa riêng đã mờ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ступ-</span>'
    '<span class="hd-gloss">BƯỚC CHÂN — như <b>поступа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ок</span>'
    '<span class="hd-gloss">đuôi danh từ, <b>о</b> rơi khi thêm đuôi: <b>посту́пка</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một bước mình đã bước ⇒ việc làm, hành vi — thứ người ta khen chê được: '
    '<b>хоро́ший посту́пок</b>, <b>глу́пый посту́пок</b>. Hành động nói chung, không phán xét, '
    'là <b>де́йствие</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поступа́ть</b> cư xử, thi vào · <b>поступи́ть</b> (HT) · '
    '<b>ступе́нька</b> bậc thang</div>'
)

B = {
    "docbangmat": 86,
    "loitubat": 4,
    "nguonsai": 1,
    "baolen": [
        "VA CHẠM KHÔNG GỠ ĐƯỢC: обеща́ние «lời hứa» nằm gọn trong сло́во [k10 đã nạp]. Gloss обещание chỉ có «promise» — không có nghĩa thông dụng nào khác để thêm. Để nguyên, không viết V.",
        "4 thẻ đang có NGOẶC nên theo luật 22/11 tôi KHÔNG viết V: информационный «thông tin (tính từ)», предупредить «cảnh báo, báo trước (một lần)», наврать «nói dối (một lần, xong)», формирование «sự hình thành; đơn vị (quân)». Cả bốn trông giống nhãn kiểu AI cũ (từ loại / thể) hơn là chú thích user — nhờ user xem có muốn tự sửa không. Lưu ý: tôi thêm «ngăn ngừa» cho предупреждать nhưng không thêm được cho предупредить (bị ngoặc khoá) ⇒ cặp thể lệch nghĩa trên đề.",
        "V cần duyệt: предупреждение (+sự báo trước, sự phòng ngừa), предупреждать (+ngăn ngừa), утверждать (+phê duyệt — approve/ratify), общаться (+giao lưu — socialize), покупка (bỏ dấu «;», thêm sự mua sắm — shopping).",
        "Nguồn sai bác: gloss полдень có «middle-age» — đó là nghĩa bóng văn chương (по́лдень жи́зни), không đưa vào thẻ hay V.",
        "Không chắc: (a) chẻ предупреди́ть thành пред-у-пред-и́ть (пред- + упреди́ть «làm trước») — mặt chữ lộ rõ, nhưng là từ nguyên; (b) trọng âm thành ngữ «с три ко́роба» (danh từ gốc là коро́б); (c) quá khứ навра́ть: tôi ghi наврала́, từ điển có nơi cho cả навра́ла.",
        "Họ hàng: không thẻ nào vắng mục này (kể cả từ mượn визи́т → визи́тка, ми́нимум → минима́льный).",
    ],
}
