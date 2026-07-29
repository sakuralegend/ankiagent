# -*- coding: utf-8 -*-
"""LÔ 9 — field `HuongDan`: 14 DANH TỪ đời sống (đồ ăn, đồ dùng, nơi chốn).

Nhóm này ít chẻ được nên trục là ba thứ khác, đều dùng suốt đời:
  * LUẬT GIỐNG — nhìn chữ cuối là biết giống, thứ quyết định mọi đuôi đi kèm
  * TỪ MƯỢN QUỐC TẾ — nhận ra là có ngay hàng trăm từ miễn phí
  * HẬU TỐ NHỎ -ка/-очка/-ик — vừa làm từ nhỏ đi, vừa làm giọng thân mật

Chạy: python data/huongdan/lo09_doisong_2026-07-27.py [--apply]
"""
import json
import sys
import urllib.request
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from anki_tools import grammar

ANKI = "http://127.0.0.1:8765"

GIONG = (
    '<div class="hd-sec">Luật giống — nhìn chữ CUỐI là biết</div>'
    '<div class="hd-why">Giống của danh từ quyết định mọi thứ đi kèm nó: tính từ, đại từ, '
    'động từ quá khứ. Nên đây là luật phải nắm trước tất cả.</div>'
    '<div class="hd-row"><span class="hd-piece">-а · -я</span>'
    '<span class="hd-gloss">GIỐNG CÁI: капу́ст<b>а</b> · ча́шк<b>а</b> · земл<b>я́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">phụ âm</span>'
    '<span class="hd-gloss">GIỐNG ĐỰC: сала́<b>т</b> · борщ · музе́<b>й</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-о · -е</span>'
    '<span class="hd-gloss">GIỐNG TRUNG: блю́д<b>о</b> · мо́р<b>е</b> · по́л<b>е</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ь</span>'
    '<span class="hd-gloss">PHẢI NHỚ TỪNG TỪ — trừ khi trước <b>ь</b> là ж ш ч щ thì luôn giống cái</span></div>'
)

MUON = (
    '<div class="hd-sec">Từ mượn quốc tế — kho từ gần như miễn phí</div>'
    '<div class="hd-why">Tiếng Nga mượn rất nhiều từ châu Âu, phần lớn qua tiếng Pháp, Đức, Ý. '
    'Bạn biết tiếng Anh nên nhận ra chúng gần như tức thì — chỉ phải học <b>mặt chữ Kirin</b> '
    'và <b>chỗ nhấn</b>.</div>'
    '<div class="hd-fam"><b>сала́т</b> <i>salad</i> · <b>шокола́д</b> <i>chocolate</i> · '
    '<b>конфе́та</b> <i>confection</i> · <b>музе́й</b> <i>museum</i> · <b>фи́рма</b> <i>firm</i> · '
    '<b>буфе́т</b> <i>buffet</i> · <b>шофёр</b> <i>chauffeur</i></div>'
    '<div class="hd-warn">Cái giá luôn là <b>trọng âm</b>: tiếng Nga hầu như luôn nhấn về cuối từ '
    'hơn tiếng Anh. <i>SAlad</i> → <b>сала́т</b> · <i>MUseum</i> → <b>музе́й</b>.</div>'
)

NHO = (
    '<div class="hd-sec">Hậu tố NHỎ -ка / -очка / -ик</div>'
    '<div class="hd-why">Cực kỳ năng suất, và làm HAI việc cùng lúc: làm vật nhỏ đi, và làm giọng '
    '<b>thân mật, âu yếm</b>. Người Nga dùng nó nhiều hơn ta tưởng — trong bếp, với trẻ con, với người thân.</div>'
    '<div class="hd-fam">ча́ша bát lớn → <b>ча́шка</b> cái chén · да́ча nhà vườn → <b>да́чка</b> căn nhà vườn nhỏ · '
    'дом nhà → <b>до́мик</b> ngôi nhà nhỏ · со́лнце mặt trời → <b>со́лнышко</b> "cục vàng" (gọi người thương)</div>'
    '<div class="hd-warn">Hậu tố này gần như luôn kéo theo <b>giống cái</b> (đuôi <b>-ка</b>) — kể cả khi từ gốc là giống khác.</div>'
)

S = {}

# ---------- ĐỒ ĂN ----------

S["помидор"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn nguyên khối từ tiếng Ý <b>pomo d\'oro</b> — nghĩa đen là <b>"quả táo VÀNG"</b>. Cà chua vào châu Âu thế kỷ 16 thì giống vàng chứ chưa đỏ như bây giờ.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chẻ theo tiếng Ý: <b>помидо́р</b> = <i>pomo</i> (quả) + <i>d\'oro</i> (bằng vàng). Tiếng Pháp cũng từng gọi <i>pomme d\'amour</i>. Nhớ hình ảnh "quả vàng" là nhớ được cả mặt chữ.</div>'
    '<div class="hd-warn"><b>Trọng âm ở âm tiết CUỐI:</b> помидо́р. Và số nhiều là <b>помидо́ры</b> — dạng bạn sẽ gặp nhiều hơn, vì cà chua thường mua cả cân.</div>'
    + GIONG
)

S["капуста"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn qua Latin <b>caput</b> = <b>CÁI ĐẦU</b>. Bắp cải là "cái đầu" mọc trên luống.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiếng Anh đi đúng con đường ấy: <i>cabbage</i> ← tiếng Pháp cổ <i>caboche</i> = cái đầu. Hai thứ tiếng độc lập cùng gọi bắp cải là "cái đầu" — nhớ một là ra cả hai.</div>'
    '<div class="hd-why">Đây là rau nền tảng của bếp Nga: <b>щи</b> (xúp bắp cải) và <b>борщ</b> đều cần nó, <b>ки́слая капу́ста</b> = bắp cải muối chua, món ăn kèm quanh năm.</div>'
    '<div class="hd-warn">Đuôi <b>-а</b> ⇒ giống cái ⇒ mọi tính từ đi kèm phải là dạng giống cái: <b>све́жая капу́ста</b> (bắp cải tươi), không phải <i>*свежий</i>.</div>'
    + GIONG
)

S["картошка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">картош-</span><span class="hd-gloss">từ <b>карто́фель</b> — khoai tây (dạng trang trọng)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-а</span><span class="hd-gloss">hậu tố NHỎ / thân mật + đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là <b>dạng đời thường</b> của <b>карто́фель</b>. Hai từ cùng nghĩa nhưng khác giọng: <b>карто́фель</b> nằm trên bao bì và thực đơn, còn <b>карто́шка</b> là từ người ta dùng trong bếp và ngoài chợ. Bạn sẽ nghe <b>карто́шка</b> nhiều hơn hẳn.</div>'
    '<div class="hd-why">Bản thân <b>карто́фель</b> mượn từ tiếng Đức <i>Kartoffel</i>, vốn từ tiếng Ý <i>tartufolo</i> = <b>củ nấm truffle</b> — người ta thấy khoai tây mọc dưới đất giống nấm truffle.</div>'
    '<div class="hd-warn">Để ý biến âm: <b>карто́фель</b> → <b>карто́шка</b>, chữ <b>ф</b> thành <b>ш</b>. Đây không phải luật đều đặn, chỉ là chuyện riêng của từ này.</div>'
    + NHO + GIONG
)

S["борщ"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ <b>gốc trơn</b>, một âm tiết, kết thúc bằng <b>щ</b> trần — không dấu mềm, nên <b>giống đực</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tên món đến từ cây <b>борщеви́к</b> (cây gấu chó) — thời xưa xúp này nấu từ chính loại cây đó, mãi sau mới đổi sang củ dền. Cái tên ở lại còn nguyên liệu thì đã thay.</div>'
    '<div class="hd-why">Phân biệt với món bạn cũng có thẻ: <b>борщ</b> có <b>củ dền</b> nên đỏ tía, còn <b>щи</b> chỉ bắp cải nên nhạt màu. Hai món xúp trụ cột của bếp Nga và Ukraina.</div>'
    '<div class="hd-warn"><b>Nhắc lại luật đã học:</b> <b>борщ</b> giống đực nên KHÔNG có <b>-ь</b>, y như <b>плащ</b>. Chỉ danh từ giống cái mới đội dấu mềm sau ж ш ч щ.</div>'
    + GIONG
)

S["салат"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn qua tiếng Ý <b>salata</b> = "đã ướp <b>MUỐI</b>" ← Latin <i>sal</i> (muối). Rau trộn ngày xưa là rau ướp muối.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc với những từ bạn đã biết trong tiếng Anh: <i>salad</i>, <i>salt</i>, <i>salary</i> (lương — xưa lính La Mã được trả bằng muối!). Tiếng Nga giữ luôn gốc đó: <b>соль</b> = muối.</div>'
    '<div class="hd-warn"><b>Hai nghĩa, phải phân biệt theo ngữ cảnh:</b> <b>сала́т</b> vừa là <b>món rau trộn</b>, vừa là <b>cây xà lách</b>. Ngoài chợ hỏi мука́ салата là mua rau, trong nhà hàng gọi салат là gọi món.</div>'
    + MUON + GIONG
)

S["конфета"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn qua tiếng Ý <b>confetto</b> ← Latin <i>conficere</i> = "làm ra, chế biến". Cùng gốc với tiếng Anh <i>confection</i>, <i>confectionery</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa: <b>viên kẹo</b> — loại có giấy bọc, không phải sô cô la thanh. Người Nga có truyền thống tặng nhau hộp kẹo, nên đây là từ bạn sẽ gặp trong mọi dịp lễ.</div>'
    '<div class="hd-warn"><b>Bẫy nghĩa:</b> đừng nhầm với tiếng Anh <i>confetti</i> (giấy vụn tung trong tiệc) — cùng gốc Latin thật, nhưng hai nhánh nghĩa đã tách hẳn từ lâu.</div>'
    + MUON + GIONG
)

S["шоколад"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ đi vòng quanh thế giới: tiếng Aztec <b>xocolātl</b> → Tây Ban Nha <i>chocolate</i> → Pháp → Nga. Gốc gác không phải châu Âu chút nào.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bạn đã biết từ này rồi, chỉ cần nhớ mặt chữ Kirin và chỗ nhấn: <b>шокола́д</b>, nhấn âm tiết CUỐI — khác hẳn tiếng Anh <i>CHOcolate</i>.</div>'
    '<div class="hd-warn"><b>Chữ Ш:</b> trong tiếng Nga chữ này luôn CỨNG, kể cả khi sau nó là <b>и</b> hay <b>е</b>. Đó là lý do có luật <b>ЖИ ШИ viết И</b> mà bạn đã gặp.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>шокола́д</b> sô cô la · <b>шокола́дка</b> thanh sô cô la (dạng nhỏ, thân mật) · <b>шокола́дный</b> thuộc sô cô la, màu nâu</div>'
    + MUON + GIONG
)

S["блюдо"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ <b>gốc trơn</b>, đuôi <b>-о</b> nên <b>giống trung</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một từ, <b>hai nghĩa nối nhau bằng hình ảnh</b>: <b>cái đĩa lớn</b> → <b>món ăn</b> đựng trên đĩa đó. Tiếng Việt cũng đi đúng đường ấy: "một đĩa" nghĩa là một món.</div>'
    '<div class="hd-why">Ghép với thứ bạn vừa học: <b>о́строе блю́до</b> = món cay. Chú ý tính từ phải ở dạng <b>giống trung</b> (<b>о́строе</b>, không phải <i>острый</i>) vì <b>блю́до</b> là giống trung — đây chính là chỗ luật giống có tác dụng thật.</div>'
    '<div class="hd-warn"><b>Cụm rất hay gặp:</b> <b>национа́льное блю́до</b> = món ăn dân tộc · <b>пе́рвое блю́до</b> = món khai vị (thường là xúp) · <b>второ́е блю́до</b> = món chính.</div>'
    + GIONG
)

S["чашка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">чаш-</span><span class="hd-gloss">ча́ша — BÁT LỚN, chén thánh</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-а</span><span class="hd-gloss">hậu tố NHỎ + đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>ча́ша</b> là bát to, cốc lễ; thêm <b>-ка</b> thành <b>ча́шка</b> = cái chén, cái tách uống trà. Quan hệ to–nhỏ nhìn thấy ngay trong mặt chữ.</div>'
    '<div class="hd-warn"><b>Cụm bạn sẽ dùng mỗi ngày:</b> <b>ча́шка ча́я</b> = một tách trà · <b>ча́шка ко́фе</b> = một tách cà phê. Từ chỉ vật chứa luôn kéo theo <b>cách 2</b> cho thứ bên trong.</div>'
    '<div class="hd-warn"><b>Đừng nhầm:</b> <b>ча́шка</b> (tách, có quai) khác <b>стака́н</b> (cốc thuỷ tinh, không quai). Người Nga phân biệt rất rõ hai thứ này.</div>'
    + NHO + GIONG
)

# ---------- NƠI CHỐN, ĐỒ VẬT ----------

S["буфет"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn nguyên từ tiếng Pháp <b>buffet</b>. Trong tiếng Nga nó giữ CẢ HAI nghĩa gốc.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-row"><span class="hd-piece">nghĩa 1</span><span class="hd-gloss">TỦ CHÉN — cái tủ kính bày bát đĩa trong phòng ăn</span></div>'
    '<div class="hd-row"><span class="hd-piece">nghĩa 2</span><span class="hd-gloss">QUẦY ĂN NHẸ — ở trường, nhà ga, nhà hát</span></div>'
    '<div class="hd-why">Nghĩa 2 là nghĩa bạn sẽ gặp thật: mọi trường học và nhà ga Nga đều có <b>буфе́т</b> bán bánh, trà, xúp — chỗ ăn nhanh giữa giờ.</div>'
    '<div class="hd-warn">Đừng dịch cứng thành "tiệc buffet" kiểu tiếng Việt — cái đó tiếng Nga gọi là <b>шве́дский стол</b> (nghĩa đen: "bàn Thuỵ Điển").</div>'
    + MUON + GIONG
)

S["музей"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ Hy Lạp <b>mouseion</b> = <b>đền của các nàng Thơ (Muses)</b> — nơi dành cho nghệ thuật và tri thức. Cùng gốc với <i>music</i>: cả âm nhạc lẫn bảo tàng đều là "việc của các nàng Thơ".</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-warn"><b>Đuôi -й:</b> <b>музе́й</b> kết thúc bằng phụ âm <b>й</b> nên là <b>GIỐNG ĐỰC</b>. Cả một lớp từ mượn cùng khuôn: <b>музе́й</b> · <b>лице́й</b> · <b>санато́рий</b> · <b>сцена́рий</b>.</div>'
    '<div class="hd-warn"><b>Trọng âm ở CUỐI:</b> музе́й, khác hẳn <i>muSEum</i> tiếng Anh. Và cách 6 (nơi chốn) là <b>в музе́е</b> = ở trong bảo tàng.</div>'
    + MUON + GIONG
)

S["фирма"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn qua tiếng Ý <b>firma</b> = <b>CHỮ KÝ</b> ← Latin <i>firmus</i> (vững chắc). Công ty là cái tên đã ký, đã đóng dấu — nên "vững".</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiếng Anh giữ đúng cả hai nhánh nghĩa: <i>firm</i> vừa là "công ty", vừa là "chắc chắn". Cùng một gốc Latin.</div>'
    '<div class="hd-warn"><b>Trọng âm ở ĐẦU:</b> <b>фи́рма</b> — đây là ngoại lệ so với hầu hết từ mượn khác trong lô này (vốn nhấn cuối). Đừng suy, cứ nhớ riêng.</div>'
    '<div class="hd-warn"><b>Sắc thái:</b> <b>фи́рменный</b> (tính từ) nghĩa là <b>"chính hãng, xịn"</b> — <i>фи́рменный магази́н</i> = cửa hàng chính hãng. Nghĩa khen, không trung tính.</div>'
    + MUON + GIONG
)

S["дачка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дач-</span><span class="hd-gloss">да́ча — nhà vườn ngoại ô</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-а</span><span class="hd-gloss">hậu tố NHỎ / thân mật + đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc đẹp và rất Nga: <b>да́ча</b> ← <b>дать</b> (cho, ban) — nghĩa đen là <b>"phần đất được BAN"</b>. Thời Sa hoàng, đất ngoại ô được ban cho quan lại; thời Liên Xô, nhà nước chia đất cho dân trồng rau. Cái tên giữ nguyên lịch sử ấy.</div>'
    '<div class="hd-why"><b>Да́ча</b> không dịch được gọn sang tiếng Việt: nó là nhà nghỉ cuối tuần kiêm vườn rau, và là một phần đời sống Nga — cả gia đình kéo nhau ra đó suốt mùa hè.</div>'
    '<div class="hd-warn">Dạng <b>да́чка</b> mang giọng <b>thân mật, hơi đùa</b> — "cái nhà vườn bé bé của mình". Đừng dùng trong văn viết trang trọng.</div>'
    '<div class="hd-sec">Họ hàng — gốc да (cho)</div>'
    '<div class="hd-fam"><b>дать</b> cho · <b>дава́ть</b> đưa, cho (chưa HT) · <b>да́ча</b> nhà vườn · <b>зада́ние</b> nhiệm vụ (cái được giao) · <b>прода́ть</b> bán (cho đi)</div>'
    + NHO + GIONG
)

S["шофёр"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn nguyên từ tiếng Pháp <b>chauffeur</b>, nghĩa đen là <b>"người ĐỐT LÒ"</b> ← <i>chauffer</i> (đun nóng). Xe hơi đời đầu chạy bằng hơi nước nên tài xế đúng là người đốt lò.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiếng Anh mượn y hệt từ đó (<i>chauffeur</i>) và cũng giữ nghĩa "tài xế riêng". Ba thứ tiếng dùng chung một từ Pháp.</div>'
    '<div class="hd-warn"><b>ё luôn mang trọng âm</b> ⇒ <b>шофёр</b> nhấn ở cuối. Đây cũng là dấu vết của tiếng Pháp, vốn luôn nhấn âm cuối.</div>'
    '<div class="hd-warn"><b>Từ thông dụng hơn:</b> đời sống hằng ngày người Nga hay nói <b>води́тель</b> (người lái) — dựng từ gốc <b>вод-</b> (dẫn) mà bạn đã gặp ở <b>перево́дчик</b>. <b>Шофёр</b> nghe hơi cũ và thiên về tài xế chuyên nghiệp.</div>'
    + MUON + GIONG
)


# ---------------------------------------------------------------------------
def ac(action, **params):
    req = urllib.request.Request(
        ANKI, json.dumps({"action": action, "version": 6, "params": params}).encode())
    out = json.load(urllib.request.urlopen(req, timeout=180))
    if out.get("error"):
        raise RuntimeError(f"{action}: {out['error']}")
    return out["result"]


def main():
    apply = "--apply" in sys.argv
    ok, miss = [], []
    for word, html in S.items():
        ids = ac("findNotes", query=f'note:RU_Word WordClean:{word}')
        if len(ids) != 1:
            miss.append((word, len(ids)))
            continue
        if apply:
            # 🔴 GIỮ BẢNG CHIA. Script này viết 27/07, trước khi ô Hướng dẫn có
            # bảng chia máy dựng ở cuối. Ghi thẳng `html` là XOÁ MẤT bảng, im
            # lặng, chỉ phát hiện khi mở thẻ ra xem. `attach_table` nối lại bảng
            # từ dữ liệu từ điển nên chạy lại script cũ cũng không phá gì.
            ac("updateNoteFields", note={"id": ids[0], "fields": {
                "HuongDan": grammar.attach_table(html, grammar.get_cached(word))}})
        ok.append(word)
    print(f"khop: {len(ok)}/{len(S)}")
    for w, n in miss:
        print(f"  !! {w}: tim thay {n} note")
    if apply:
        print("da ghi. sync:", ac("sync"))
    else:
        print("(chua ghi gi — them --apply de ghi that)")


if __name__ == "__main__":
    main()
