# -*- coding: utf-8 -*-
"""LÔ 4 — field `HuongDan`: TÍNH TỪ THỜI TIẾT + phép biến âm phụ âm gốc lưỡi.

8 từ này dạy chung một việc: biến DANH TỪ thành TÍNH TỪ bằng hậu tố `-н-`,
và luật biến âm đi kèm — **г / к / х mềm thành ж / ч / ш** trước `-н-`.
Đây là phép biến âm chạy khắp tiếng Nga, học một lần dùng cả đời.

Chạy: python data/huongdan/lo04_thoitiet_2026-07-27.py [--apply]
"""
import json
import sys
import urllib.request
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from anki_tools import grammar

ANKI = "http://127.0.0.1:8765"

LUAT = (
    '<div class="hd-sec">Luật: danh từ → tính từ bằng -н-</div>'
    '<div class="hd-why">Muốn nói "thuộc về X, có tính chất X" thì lấy danh từ dán <b>-ный</b>. '
    'Đây là hậu tố tính từ phổ biến nhất tiếng Nga.</div>'
    '<div class="hd-row"><span class="hd-piece">-ный</span>'
    '<span class="hd-gloss">có/thuộc về: моро́з băng giá → моро́з<b>ный</b> giá buốt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ливый</span>'
    '<span class="hd-gloss">HAY, đầy, dễ bị: дождь mưa → дожд<b>ли́вый</b> mưa nhiều</span></div>'
    '<div class="hd-sec">Biến âm bắt buộc thuộc: г·к·х → ж·ч·ш</div>'
    '<div class="hd-why">Ba phụ âm <b>г к х</b> không chịu đứng trước <b>-н-</b> hay các nguyên âm '
    'mềm, nên chúng đổi mặt: <b>г→ж</b>, <b>к→ч</b>, <b>х→ш</b>.</div>'
    '<div class="hd-fam">снег tuyết → сне́<b>ж</b>ный · рука́ tay → ру́<b>ч</b>ка cái bút · '
    'у́хо tai → у́<b>ш</b>и đôi tai · друг bạn → дру<b>ж</b>ба tình bạn · '
    'бума́га giấy → бума́<b>ж</b>ный bằng giấy</div>'
    '<div class="hd-why">Nhận ra luật này thì hàng loạt từ "lạ" bỗng hoá quen — chúng chỉ là từ '
    'bạn đã biết, mặc áo khác.</div>'
)

S = {}

S["снежный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">снеж-</span><span class="hd-gloss">снег (tuyết) — chữ <b>г</b> đã mềm thành <b>ж</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-</span><span class="hd-gloss">hậu tố tạo tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span><span class="hd-gloss">đuôi tính từ, giống đực số ít</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là <b>ví dụ mẫu</b> của luật <b>г → ж</b>. Nếu không biết luật, bạn sẽ tưởng <b>снег</b> và <b>сне́жный</b> là hai từ khác nhau phải học riêng. Biết rồi thì chỉ còn một từ.</div>'
    '<div class="hd-why">Cùng gốc: <b>снегови́к</b> người tuyết · <b>снежи́нка</b> bông tuyết · <b>Снегу́рочка</b> Cô Bé Tuyết (cháu gái ông già Tuyết — nhân vật Năm Mới của Nga).</div>'
    + LUAT
)

S["морозный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мороз-</span><span class="hd-gloss">моро́з — băng giá, rét cắt da (dưới 0°C)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-</span><span class="hd-gloss">hậu tố tạo tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span><span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ghép sạch, không biến âm — lấy từ này làm mẫu chuẩn rồi soi các từ khác lệch chỗ nào.</div>'
    '<div class="hd-why"><b>Моро́з</b> là một trong những từ Nga nhất: <b>Дед Моро́з</b> = Ông già Tuyết (nghĩa đen "Ông Nội Băng Giá"), nhân vật Năm Mới thay cho ông già Noel.</div>'
    '<div class="hd-warn"><b>Phân biệt sắc thái:</b> <b>моро́зный</b> = rét ÂM ĐỘ, băng đóng. Còn <b>холо́дный</b> chỉ là lạnh nói chung. Người Nga tách bạch hai mức này rất rõ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>моро́з</b> băng giá · <b>моро́женое</b> kem (nghĩa đen: thứ đã bị làm đông) · <b>морози́льник</b> tủ đông · <b>замёрзнуть</b> chết cóng</div>'
    + LUAT
)

S["облачный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">облач-</span><span class="hd-gloss">о́блако (đám mây) — chữ <b>к</b> đã mềm thành <b>ч</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-</span><span class="hd-gloss">hậu tố tạo tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span><span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ví dụ mẫu của nhánh <b>к → ч</b>. Cặp <b>о́блако → о́блачный</b> song song hoàn hảo với <b>снег → сне́жный</b> — cùng một luật, chỉ khác phụ âm.</div>'
    '<div class="hd-why">Bản thân <b>о́блако</b> chẻ được nữa: <b>об-</b> (quanh) + gốc <b>-волок-</b> (bọc, kéo phủ) — đám mây là "cái bọc quanh trời". Cùng gốc với <b>во́лос</b> (sợi tóc) theo hình ảnh sợi kéo dài.</div>'
    '<div class="hd-why">Nghĩa hiện đại: <b>о́блачное хране́ние</b> = lưu trữ đám mây, đúng như tiếng Anh <i>cloud storage</i>.</div>'
    + LUAT
)

S["ветреный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ветр-</span><span class="hd-gloss">ве́тер (gió) — chữ <b>е</b> rụng khi thêm hậu tố</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ен-</span><span class="hd-gloss">hậu tố tạo tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span><span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa bóng mới là chỗ đáng học: <b>ве́треный челове́к</b> = người <b>nông nổi, đứng núi này trông núi nọ</b> — đầu óc bị gió thổi bay. Tiếng Việt có hình ảnh gần y hệt: "gió chiều nào theo chiều ấy".</div>'
    '<div class="hd-warn"><b>Ngoại lệ chính tả NỔI TIẾNG:</b> <b>ве́треный</b> viết MỘT chữ <b>н</b>, trong khi hầu hết tính từ cùng lớp viết hai (<b>-енный</b>). Đây là ngoại lệ mà học sinh Nga cũng phải học thuộc riêng. Nhưng hễ thêm tiền tố thì lại quay về hai <b>н</b>: <b>безве́тренный</b> (lặng gió).</div>'
    '<div class="hd-warn"><b>Chữ е rụng:</b> ве́т<b>е</b>р → ве́тр-. Hiện tượng "nguyên âm chạy" này gặp liên tục: оте́ц cha → отца́ · день ngày → дня · у́гол góc → угла́.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ве́тер</b> gió · <b>ветеро́к</b> làn gió nhẹ · <b>ветряно́й</b> chạy bằng sức gió · <b>прове́трить</b> mở cửa cho thoáng</div>'
    + LUAT
)

S["дождливый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дожд-</span><span class="hd-gloss">дождь (mưa)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лив-</span><span class="hd-gloss">HAY, ĐẦY, dễ bị — hậu tố chỉ khuynh hướng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span><span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không phải <b>-ный</b> mà là <b>-ливый</b> — hậu tố này thêm sắc thái <b>"hay bị, đầy tính chất đó"</b>. Không phải "thuộc về mưa" mà là <b>mưa dai, mưa nhiều</b>.</div>'
    '<div class="hd-why">Nắm <b>-ливый</b> là mở khoá cả một lớp tính từ tả tính cách — nhóm từ bạn sẽ cần rất sớm khi tả người: <b>счастли́вый</b> hạnh phúc · <b>терпели́вый</b> kiên nhẫn · <b>тала́нтливый</b> có tài · <b>лени́вый</b> lười · <b>молчали́вый</b> ít nói.</div>'
    '<div class="hd-warn"><b>Bẫy phát âm:</b> <b>дождь</b> có cụm <b>-ждь</b> rất khó, và người Nga đọc mỗi vùng một kiểu. Cứ viết đúng mặt chữ, đừng cố suy chính tả từ cái tai nghe được.</div>'
    + LUAT
)

S["солнечный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">солн-</span><span class="hd-gloss">со́лнце (mặt trời)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ечн-</span><span class="hd-gloss">hậu tố tính từ, chữ <b>ц</b> của со́лнце mềm thành <b>ч</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span><span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thêm một nhánh của luật biến âm: <b>ц → ч</b>, cùng họ với <b>к → ч</b>. So sánh cả bộ: снег→сне́<b>ж</b>ный · о́блако→о́бла<b>ч</b>ный · со́лнце→со́лне<b>ч</b>ный.</div>'
    '<div class="hd-warn"><b>Bẫy chính tả kinh điển:</b> chữ <b>л</b> trong <b>со́лнце</b> KHÔNG được đọc — người Nga nói "SON-tse". Nhưng <b>viết thì bắt buộc phải có л</b>. Đây đúng loại lỗi bạn sẽ mắc ở ô gõ nếu chép theo tai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>со́лнце</b> mặt trời · <b>со́лнечный</b> có nắng · <b>подсо́лнух</b> hoa hướng dương (nghĩa đen: cái dưới mặt trời) · <b>со́лнышко</b> mặt trời bé bỏng — cách gọi âu yếm người thân, y như "cục vàng" tiếng Việt</div>'
    + LUAT
)

S["пасмурный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">па-</span><span class="hd-gloss">tiền tố cổ, ý "phủ lên, hơi hướng"</span></div>'
    '<div class="hd-row"><span class="hd-piece">-смур-</span><span class="hd-gloss">U ÁM, tối sầm — cùng họ <b>хму́рый</b> (cau có, u ám)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span><span class="hd-gloss">hậu tố + đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trời <b>âm u xám xịt</b>, mây phủ kín không thấy mặt trời. Nặng hơn <b>о́блачный</b> (chỉ có mây) — <b>па́смурный</b> là kín đặc, tối trời.</div>'
    '<div class="hd-why">Dùng cho cả người: <b>па́смурное лицо́</b> = gương mặt u ám. Tiếng Nga rất hay mượn thời tiết để tả tâm trạng, và bạn cũng dùng được luôn kiểu đó.</div>'
    '<div class="hd-warn">⚠️ Chỗ này tôi nói mức <b>vừa đủ tin</b>: cách chẻ <b>па- + смур-</b> là theo lối phân tích từ nguyên, không phải thứ người Nga hôm nay còn cảm thấy. Cứ nhớ nó gắn với <b>хму́рый</b> (u ám) là đủ dùng.</div>'
    + LUAT
)

S["будничный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">будн-</span><span class="hd-gloss">бу́дни — ngày thường, ngày đi làm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ичн-</span><span class="hd-gloss">hậu tố tạo tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span><span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiếng Nga chia tuần thành hai nửa có tên riêng: <b>бу́дни</b> (ngày thường phải đi làm) và <b>выходны́е</b> (ngày nghỉ). <b>Бу́дничный</b> = thuộc về nửa phải đi làm.</div>'
    '<div class="hd-why">Từ đó ra nghĩa bóng rất hay dùng: <b>đều đều, tẻ nhạt, không có gì đặc biệt</b> — <b>бу́дничный го́лос</b> = giọng nói dửng dưng như mọi ngày.</div>'
    '<div class="hd-warn"><b>Nối với từ bạn đã có:</b> <b>выходно́й</b> (ngày nghỉ) trong bộ thẻ của bạn chính là vế đối của từ này. Học cặp đối luôn rẻ hơn học hai từ rời.</div>'
    + LUAT
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
