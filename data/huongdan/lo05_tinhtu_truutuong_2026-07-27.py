# -*- coding: utf-8 -*-
"""LÔ 5 — field `HuongDan`: TÍNH TỪ TRỪU TƯỢNG + hai hậu tố quốc tế.

Nhóm này dạy ba thứ dùng được rất xa:
  * `-альный` = tính từ quốc tế — user biết tiếng Anh nên đây là kho từ MIỄN PHÍ
  * `-тельный` = tính từ sinh từ ĐỘNG TỪ
  * `-ость`    = hậu tố biến tính từ thành DANH TỪ trừu tượng (= `-ness`)
Kèm hai tiền tố cổ điển: `со-` (cùng, = Latin con-) và `ино-` (khác).

Chạy: python data/huongdan/lo05_tinhtu_truutuong_2026-07-27.py [--apply]
"""
raise SystemExit("KHAI TU 30/07/2026: chuan v1 — chay lai se XOA BANG CHIA the that. Xem QD-03.")
import json
import sys
import urllib.request
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from anki_tools import grammar

ANKI = "http://127.0.0.1:8765"

QUOCTE = (
    '<div class="hd-sec">-альный: kho từ MIỄN PHÍ cho người biết tiếng Anh</div>'
    '<div class="hd-why">Tiếng Nga mượn hàng nghìn tính từ gốc Latin y như tiếng Anh, chỉ thay '
    'đuôi <i>-al</i> thành <b>-а́льный</b>. Biết một từ tiếng Anh là gần như biết luôn từ Nga.</div>'
    '<div class="hd-fam"><i>normal</i> → <b>норма́льный</b> · <i>central</i> → <b>центра́льный</b> · '
    '<i>natural</i> → <b>натура́льный</b> · <i>actual</i> → <b>актуа́льный</b> · '
    '<i>professional</i> → <b>профессиона́льный</b> · <i>social</i> → <b>социа́льный</b></div>'
    '<div class="hd-warn"><b>Cái giá phải trả:</b> trọng âm LUÔN rơi vào <b>-а́ль-</b>, không giống '
    'tiếng Anh (<i>NORmal</i> → <b>норМАЛЬный</b>). Đây là chỗ duy nhất bạn phải sửa thói quen.</div>'
)

TELN = (
    '<div class="hd-sec">-тельный: tính từ sinh ra từ ĐỘNG TỪ</div>'
    '<div class="hd-why">Thấy đuôi <b>-тельный</b> là biết ngay: từ này vốn là một động từ, được '
    'đóng gói lại thành tính từ mang nghĩa "có tính chất làm việc đó".</div>'
    '<div class="hd-fam"><b>положи́тельный</b> tích cực · <b>отрица́тельный</b> tiêu cực · '
    '<b>значи́тельный</b> đáng kể · <b>внима́тельный</b> chăm chú · '
    '<b>обяза́тельный</b> bắt buộc · <b>удиви́тельный</b> đáng ngạc nhiên</div>'
)

S = {}

S["отрицательный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span><span class="hd-gloss">RỜI RA, đẩy ra xa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-риц-</span><span class="hd-gloss">NÓI — cùng họ với <b>речь</b> (lời nói)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тельн-</span><span class="hd-gloss">biến động từ → tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span><span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>nói đẩy ra</b>, nói ngược lại = phủ định, tiêu cực. Tiếng Anh dựng y hệt: <i>negative</i> ← Latin <i>negare</i> = <b>nói không</b>. Hai thứ tiếng cùng chọn hành động NÓI để đặt tên cho sự phủ định.</div>'
    '<div class="hd-why">Cặp đối hoàn hảo với <b>положи́тельный</b> (tích cực): cái kia là "đặt xuống, chốt lại", cái này là "nói gạt đi". Học hai từ cùng lúc rẻ hơn hẳn học rời.</div>'
    '<div class="hd-sec">Họ hàng — gốc рек/реч/риц (nói)</div>'
    '<div class="hd-fam"><b>речь</b> lời nói, bài phát biểu · <b>отрица́ть</b> phủ nhận · <b>отрица́ние</b> sự phủ định · <b>наре́чие</b> trạng từ (nghĩa đen: cái nói thêm vào)</div>'
    + TELN
)

S["современный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span><span class="hd-gloss">CÙNG, chung với (đúng bằng <i>con-/com-</i> của tiếng Anh)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-времен-</span><span class="hd-gloss">вре́мя — THỜI GIAN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span><span class="hd-gloss">hậu tố + đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>cùng thời</b> = hiện đại, đương đại. Và đây là chỗ đẹp nhất — tiếng Anh <i>contemporary</i> ghép <b>y hệt từng mảnh một</b>: <i>con-</i> (cùng) + <i>tempus</i> (thời gian). Hai ngôn ngữ dịch nhau từng morphem.</div>'
    '<div class="hd-why">Tiền tố <b>со-</b> là một trong những tiền tố đáng thuộc nhất: <b>сосе́д</b> hàng xóm (cùng ngồi) · <b>сою́з</b> liên minh · <b>сотру́дник</b> đồng nghiệp (cùng làm) · <b>соглаша́ться</b> đồng ý (cùng tiếng nói).</div>'
    '<div class="hd-warn"><b>Bẫy chính tả:</b> thân từ là <b>времен-</b> chứ không phải <b>время-</b>. Danh từ <b>вре́мя</b> thuộc nhóm bất quy tắc, khi biến cách luôn mọc thêm <b>-ен-</b>: вре́мя → вре́мени → времена́. Cùng nhóm: и́мя (tên) → и́мени.</div>'
    '<div class="hd-sec">Họ hàng — вре́мя</div>'
    '<div class="hd-fam"><b>вре́мя</b> thời gian · <b>вре́менный</b> tạm thời · <b>совреме́нник</b> người cùng thời · <b>всё вре́мя</b> suốt, luôn luôn</div>'
)

S["иностранный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ино-</span><span class="hd-gloss">KHÁC, thứ khác (cùng họ <b>ино́й</b> = khác)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-стран-</span><span class="hd-gloss">страна́ — ĐẤT NƯỚC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span><span class="hd-gloss">hậu tố + đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen trong veo: <b>thuộc nước khác</b> = ngoại quốc. Chẻ ra rồi thì không thể quên — <b>ино</b> (khác) + <b>стран</b> (nước).</div>'
    '<div class="hd-why"><b>Ино-</b> mở ra một chùm: <b>иностра́нец</b> người nước ngoài · <b>ина́че</b> cách khác, nếu không thì · <b>ино́й</b> khác · <b>иногда́</b> đôi khi (nghĩa đen: vào lúc khác).</div>'
    '<div class="hd-warn"><b>Bẫy hai chữ н:</b> <b>стран</b> đã có sẵn <b>н</b> cuối, cộng thêm <b>-н-</b> của hậu tố → <b>-нн-</b>. Đếm được lý do thì không bao giờ viết thiếu.</div>'
    '<div class="hd-sec">Họ hàng — страна́</div>'
    '<div class="hd-fam"><b>страна́</b> đất nước · <b>иностра́нец</b> người nước ngoài · <b>стра́нный</b> kỳ lạ (nghĩa gốc: từ xứ khác tới!) · <b>сторона́</b> phía, bên</div>'
)

S["множественный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">множеств-</span><span class="hd-gloss">мно́жество — số lượng lớn, tập hợp</span></div>'
    '<div class="hd-row"><span class="hd-piece">-енн-</span><span class="hd-gloss">hậu tố tạo tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span><span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Truy ngược tới tận gốc thì đây chính là <b>мно́го</b> (nhiều) — từ bạn đã biết. Đường đi: <b>мно́го</b> nhiều → <b>мно́жить</b> nhân lên → <b>мно́жество</b> số nhiều → <b>мно́жественный</b> thuộc số nhiều. Chú ý <b>г → ж</b>, đúng luật biến âm ở lô thời tiết.</div>'
    '<div class="hd-warn"><b>Đây là THUẬT NGỮ NGỮ PHÁP bạn sẽ gặp mỗi ngày:</b> <b>мно́жественное число́</b> = SỐ NHIỀU, đối lại <b>еди́нственное число́</b> = số ít. Nhớ nguyên cụm chứ đừng nhớ từ lẻ.</div>'
    '<div class="hd-sec">Họ hàng — мног/множ (nhiều)</div>'
    '<div class="hd-fam"><b>мно́го</b> nhiều · <b>мно́гие</b> nhiều người · <b>мно́жество</b> vô số · <b>умножа́ть</b> nhân (phép toán)</div>'
)

S["особенность"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">особ-</span><span class="hd-gloss">RIÊNG, tách ra một mình (<b>осо́бый</b> = riêng biệt)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-енн-</span><span class="hd-gloss">hậu tố tính từ (<b>осо́бенный</b> = đặc biệt)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ость</span><span class="hd-gloss">biến TÍNH TỪ → DANH TỪ trừu tượng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Xem đường xây ba tầng: <b>осо́бый</b> (riêng) → <b>осо́бенный</b> (đặc biệt) → <b>осо́бенность</b> (nét đặc biệt). Mỗi tầng thêm một hậu tố, nghĩa cũng leo lên một bậc trừu tượng.</div>'
    '<div class="hd-why"><b>-ость là hậu tố đáng giá bậc nhất</b> — đúng bằng <i>-ness</i> của tiếng Anh, và cứ gắn vào tính từ là ra danh từ. Một điều LUÔN đúng, nhớ là dùng được ngay: danh từ đuôi <b>-ость</b> <b>bao giờ cũng GIỐNG CÁI</b>.</div>'
    '<div class="hd-fam"><b>но́вый</b> mới → <b>но́вость</b> tin tức · <b>сла́бый</b> yếu → <b>сла́бость</b> điểm yếu · <b>возмо́жный</b> có thể → <b>возмо́жность</b> khả năng · <b>тру́дный</b> khó → <b>тру́дность</b> khó khăn</div>'
    '<div class="hd-warn"><b>Trọng âm thì ĐỪNG đoán:</b> phần lớn giữ nguyên chỗ cũ (сла́бый → сла́бость), nhưng có từ dịch hẳn — <b>молодо́й</b> (trẻ) → <b>мо́лодость</b> (tuổi trẻ), nhảy từ cuối về đầu. Gặp từ mới cứ tra, đừng suy.</div>'
    '<div class="hd-warn"><b>Từ cùng gốc dùng cực nhiều:</b> <b>осо́бенно</b> = <i>đặc biệt là, nhất là</i>. Chỉ khác đuôi mà thành trạng từ.</div>'
)

S["нормальный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">норм-</span><span class="hd-gloss">но́рма — chuẩn mực (<i>norm</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-альн-</span><span class="hd-gloss">hậu tố tính từ quốc tế, đúng <i>-al</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span><span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bạn đã biết từ này rồi qua tiếng Anh — việc duy nhất cần học là <b>đuôi và trọng âm</b>.</div>'
    '<div class="hd-warn"><b>Sắc thái RẤT hay dùng:</b> trong hội thoại, <b>норма́льно</b> là câu trả lời mặc định cho "Как дела́?" — nghĩa là <b>"ổn, bình thường thôi"</b>, hoàn toàn tích cực. Đừng dịch cứng thành "bình thường" theo kiểu chê bai của tiếng Việt.</div>'
    + QUOCTE
)

S["центральный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">центр-</span><span class="hd-gloss">центр — trung tâm (<i>centre</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-альн-</span><span class="hd-gloss">hậu tố tính từ quốc tế</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span><span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đã biết sẵn nghĩa, chỉ cần nhớ mặt chữ: chữ <b>ц</b> của tiếng Nga làm việc của <i>c</i> trong <i>centre</i> — cùng một âm "ts" mà nhiều thứ tiếng châu Âu đều có.</div>'
    '<div class="hd-why">Bạn sẽ gặp ngay ngoài đời: <b>Центра́льный вокза́л</b> ga trung tâm · <b>центр го́рода</b> trung tâm thành phố · <b>торго́вый центр</b> trung tâm thương mại.</div>'
    + QUOCTE
)

S["натуральный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">натур-</span><span class="hd-gloss">нату́ра — tự nhiên (<i>nature</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-альн-</span><span class="hd-gloss">hậu tố tính từ quốc tế</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span><span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giống <i>natural</i>, nhưng phạm vi hẹp hơn: tiếng Nga dùng <b>натура́льный</b> chủ yếu cho <b>thực phẩm và vật liệu</b> — sữa nguyên chất, da thật, nước ép nguyên chất. Là chữ bạn sẽ đọc trên bao bì trong siêu thị.</div>'
    '<div class="hd-warn"><b>Bẫy nghĩa:</b> muốn nói "thiên nhiên" (rừng núi, phong cảnh) thì KHÔNG dùng từ này mà dùng <b>приро́да</b>. Còn "tự nhiên, không gượng" (cách cư xử) là <b>есте́ственный</b>. Một từ Anh <i>natural</i> tách thành ba từ Nga.</div>'
    + QUOCTE
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
