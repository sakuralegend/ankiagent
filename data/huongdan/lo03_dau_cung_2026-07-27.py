# -*- coding: utf-8 -*-
"""LÔ 3 — field `HuongDan`: nhóm DẤU CỨNG ъ + hai gốc `езд` (đi xe) và `ём` (lấy).

8 từ này dạy được trọn một LUẬT CHÍNH TẢ, chứ không chỉ 8 nghĩa rời:
  * khi nào viết ъ (và vì sao KHÔNG phải ь)
  * gốc `езд` và `ём` tách ra dùng lại được ở hàng chục từ khác
  * bốn tiền tố phổ dụng под- / раз- / с- / об-

Chạy: python data/huongdan/lo03_dau_cung_2026-07-27.py [--apply]
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

# --- Luật ъ: khối dùng chung cho cả 8 thẻ ---
LUAT = (
    '<div class="hd-sec">Luật dấu cứng ъ — thuộc một lần, dùng mãi</div>'
    '<div class="hd-why">Viết <b>ъ</b> khi có ĐỦ hai điều kiện: (1) đứng ngay sau một '
    '<b>TIỀN TỐ tận cùng bằng phụ âm</b>, và (2) ngay trước một trong bốn nguyên âm '
    '<b>е · ё · ю · я</b>.</div>'
    '<div class="hd-why">Nó làm nhiệm vụ <b>NGĂN ĐÔI</b>: báo cho người đọc rằng nguyên âm phía '
    'sau giữ nguyên âm "y" của nó (<i>подъезд</i> đọc "pad-YEZD" chứ không phải "pa-DEZD"), '
    'và phụ âm phía trước KHÔNG bị mềm đi.</div>'
    '<div class="hd-row"><span class="hd-piece">ъ</span>'
    '<span class="hd-gloss">sau TIỀN TỐ: <b>об</b>ъём · <b>под</b>ъе́зд · <b>раз</b>ъе́зд · <b>с</b>ъезд</span></div>'
    '<div class="hd-row"><span class="hd-piece">ь</span>'
    '<span class="hd-gloss">bên TRONG từ, không dính tiền tố: сем<b>ь</b>я́ gia đình · '
    'стат<b>ь</b>я́ bài báo · пь<b>ю</b> tôi uống</span></div>'
    '<div class="hd-why">Nhìn thấy <b>ъ</b> là biết ngay từ đó có tiền tố — tức là <b>chẻ được</b>. '
    'Đó là lý do nhóm từ này đáng học chung một chỗ.</div>'
)

EZD = (
    '<div class="hd-sec">Gốc езд / езж / ех — ĐI BẰNG PHƯƠNG TIỆN</div>'
    '<div class="hd-fam"><b>е́хать</b> đi (bằng xe) · <b>е́здить</b> đi lại thường xuyên · '
    '<b>прие́хать</b> đến nơi · <b>уе́хать</b> rời đi · <b>перее́хать</b> chuyển nhà · '
    '<b>по́езд</b> tàu hoả · <b>пое́здка</b> chuyến đi</div>'
    '<div class="hd-why">Phân biệt cốt tử với <b>идти́ / ходи́ть</b> = đi BỘ. Tiếng Nga bắt buộc '
    'phải chọn: đi bộ hay đi xe, không có từ chung chung như "đi" của tiếng Việt.</div>'
)

EM = (
    '<div class="hd-sec">Gốc ём / им / ня — LẤY, CẦM</div>'
    '<div class="hd-fam"><b>взять</b> lấy · <b>име́ть</b> có · <b>заня́ть</b> chiếm, mượn · '
    '<b>приня́ть</b> nhận · <b>подня́ть</b> nâng lên · <b>сня́ть</b> cởi ra, thuê</div>'
    '<div class="hd-why">Gốc này biến hình rất mạnh (ём / им / ня / я) nên trông như nhiều gốc '
    'khác nhau. Cứ thấy nghĩa "cầm nắm, chiếm giữ" thì khả năng cao là nó.</div>'
)

S = {}

S["подъезд"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span><span class="hd-gloss">TỚI SÁT, tiến đến gần (nghĩa gốc: ở dưới)</span></div>'
    '<div class="hd-row"><span class="hd-piece">ъ</span><span class="hd-gloss">dấu cứng — vì <b>под</b> là tiền tố tận cùng phụ âm, đứng trước <b>е</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-езд</span><span class="hd-gloss">ĐI BẰNG XE</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>chỗ xe chạy tới sát</b>. Từ đó ra hai nghĩa thực dụng — lối xe vào, và <b>cửa/sảnh chung cư</b> (chính là chỗ xe đỗ sát để người xuống). Nghĩa thứ hai bạn sẽ gặp hằng ngày khi ai đó chỉ đường trong khu nhà.</div>'
    '<div class="hd-why">So sánh cho thấy tiền tố làm chủ nghĩa: <b>подъе́зд</b> đi tới sát · <b>вы́езд</b> đi ra · <b>въезд</b> đi vào · <b>объе́зд</b> đi vòng.</div>'
    + LUAT + EZD
)

S["подъём"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span><span class="hd-gloss">TỪ DƯỚI LÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">ъ</span><span class="hd-gloss">dấu cứng — tiền tố phụ âm + nguyên âm <b>ё</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ём</span><span class="hd-gloss">LẤY, NÂNG</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>lấy từ dưới lên</b> = sự nâng lên. Từ một hình ảnh đó toả ra đủ nghĩa: dốc lên (đường), lúc thức dậy (nâng mình khỏi giường), đà phát triển (kinh tế đi lên).</div>'
    '<div class="hd-why">Động từ tương ứng là <b>подня́ть</b> (nâng lên) — cùng gốc, chỉ khác dạng: <b>-ём</b> trong danh từ, <b>-ня-</b> trong động từ.</div>'
    '<div class="hd-warn"><b>Luật trọng âm quà tặng:</b> chữ <b>ё</b> trong tiếng Nga <b>LUÔN LUÔN mang trọng âm</b>, không có ngoại lệ. Thấy ё là biết ngay nhấn ở đó, khỏi phải nhớ.</div>'
    + LUAT + EM
)

S["разъезд"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раз-</span><span class="hd-gloss">TẢN RA, tách mỗi thứ một hướng</span></div>'
    '<div class="hd-row"><span class="hd-piece">ъ</span><span class="hd-gloss">dấu cứng — tiền tố phụ âm + nguyên âm <b>е</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-езд</span><span class="hd-gloss">ĐI BẰNG XE</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>đi xe tản ra mỗi người một ngả</b>. Ra hai nghĩa: cảnh đi công tác liên miên, và <b>ga tránh tàu</b> — chỗ đường ray tách đôi cho hai tàu vượt nhau rồi lại đi ngược hướng.</div>'
    '<div class="hd-why">Tiền tố <b>раз-</b> là một trong những tiền tố sinh lợi nhất, luôn mang ý TÁCH RA: <b>разби́ть</b> đập vỡ · <b>разде́лить</b> chia · <b>рассказа́ть</b> kể ra · <b>разгово́р</b> cuộc trò chuyện.</div>'
    '<div class="hd-warn"><b>Bẫy đối nghĩa:</b> <b>разъе́зд</b> (tản ra) đứng đối diện <b>съезд</b> (tụ về). Cùng gốc <b>езд</b>, chỉ đổi tiền tố mà nghĩa lộn ngược.</div>'
    + LUAT + EZD
)

S["разъём"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раз-</span><span class="hd-gloss">TÁCH RỜI</span></div>'
    '<div class="hd-row"><span class="hd-piece">ъ</span><span class="hd-gloss">dấu cứng — tiền tố phụ âm + nguyên âm <b>ё</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ём</span><span class="hd-gloss">LẤY, CẦM</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>chỗ tháo rời ra được</b> — tức là <b>đầu nối, giắc cắm</b> (cổng USB, jack tai nghe). Từ kỹ thuật hiện đại nhưng dựng bằng đúng bộ phận tiếng Nga cổ.</div>'
    '<div class="hd-why">Đặt cạnh nhau thấy ngay sức mạnh của tiền tố: <b>подъём</b> nâng LÊN · <b>разъём</b> tháo RỜI · <b>объём</b> ôm QUANH. Cùng một gốc <b>ём</b>, ba tiền tố, ba nghĩa.</div>'
    + LUAT + EM
)

S["съезд"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span><span class="hd-gloss">TỤ LẠI MỘT CHỖ (và cả nghĩa: xuống)</span></div>'
    '<div class="hd-row"><span class="hd-piece">ъ</span><span class="hd-gloss">dấu cứng — tiền tố <b>с</b> là phụ âm, đứng trước <b>е</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-езд</span><span class="hd-gloss">ĐI BẰNG XE</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>mọi người đi xe TỤ VỀ một chỗ</b> = đại hội, hội nghị. Hình ảnh rất thật: thời chưa có máy bay, đại hội là cảnh đại biểu khắp nơi đổ xe về thủ đô.</div>'
    '<div class="hd-warn"><b>Bẫy chính tả:</b> tiền tố chỉ có MỘT chữ <b>с</b> nhưng vẫn phải có <b>ъ</b> — quy tắc tính theo "tiền tố tận cùng bằng phụ âm", dài ngắn không quan trọng. Viết <i>*сезд</i> là sai.</div>'
    '<div class="hd-why">Cặp đối: <b>съезд</b> tụ về ↔ <b>разъе́зд</b> tản ra.</div>'
    + LUAT + EZD
)

S["объём"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span><span class="hd-gloss">QUANH, bao lấy</span></div>'
    '<div class="hd-row"><span class="hd-piece">ъ</span><span class="hd-gloss">dấu cứng — tiền tố phụ âm + nguyên âm <b>ё</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ём</span><span class="hd-gloss">LẤY, CẦM</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>cái ôm lấy được xung quanh</b> = <b>thể tích</b>, dung lượng, khối lượng công việc. Hình dung hai tay vòng ôm một khối — chỗ trống bên trong vòng tay chính là объём.</div>'
    '<div class="hd-why">Tiếng Anh đi cùng đường: <i>volume</i> ← Latin <i>volvere</i> = cuộn quanh. Hai thứ tiếng đều lấy hình ảnh "vòng quanh" để gọi thể tích.</div>'
    '<div class="hd-why">Tiền tố <b>об-</b> gặp rất nhiều: <b>обня́ть</b> ôm · <b>объясни́ть</b> giải thích (làm sáng tỏ khắp lượt) · <b>обойти́</b> đi vòng quanh.</div>'
    + LUAT + EM
)

S["объявить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span><span class="hd-gloss">KHẮP LƯỢT, ra xung quanh</span></div>'
    '<div class="hd-row"><span class="hd-piece">ъ</span><span class="hd-gloss">dấu cứng — tiền tố phụ âm + nguyên âm <b>я</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-яв-</span><span class="hd-gloss">LÀM HIỆN RA, phơi bày</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span><span class="hd-gloss">đuôi nguyên thể động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>làm cho hiện ra khắp xung quanh</b> = tuyên bố, thông báo. Không phải nói cho một người, mà phát ra cho cả vòng người nghe.</div>'
    '<div class="hd-sec">Gốc яв- — HIỆN RA</div>'
    '<div class="hd-fam"><b>яви́ться</b> xuất hiện · <b>появи́ться</b> nảy ra, hiện lên · <b>явле́ние</b> hiện tượng · <b>я́вный</b> rõ rành rành · <b>объявле́ние</b> thông báo</div>'
    '<div class="hd-warn"><b>Cặp thể:</b> <b>объяви́ть</b> (hoàn thành — tuyên bố xong) đi cặp với <b>объявля́ть</b> (chưa hoàn thành — đang/thường tuyên bố). Tiếng Nga hầu như động từ nào cũng đi thành cặp như vậy; học một từ là phải biết bạn của nó.</div>'
    + LUAT
)

S["объявление"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span><span class="hd-gloss">KHẮP LƯỢT, ra xung quanh</span></div>'
    '<div class="hd-row"><span class="hd-piece">ъ</span><span class="hd-gloss">dấu cứng — tiền tố phụ âm + nguyên âm <b>я</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-явл-</span><span class="hd-gloss">LÀM HIỆN RA (dạng có <b>л</b> chèn)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span><span class="hd-gloss">hậu tố biến ĐỘNG TỪ thành DANH TỪ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Là <b>объяви́ть</b> (tuyên bố) đóng gói thành danh từ: cái được tuyên bố = <b>thông báo, mẩu quảng cáo, tờ rao vặt</b>.</div>'
    '<div class="hd-why"><b>-ение / -ание</b> là một trong những hậu tố đáng giá nhất để nhận mặt: gặp nó là biết ngay đây là DANH TỪ trừu tượng sinh từ động từ, và luôn thuộc <b>giống trung</b>. Cùng lớp: <b>упражне́ние</b> bài tập · <b>спряже́ние</b> sự chia động từ · <b>предложе́ние</b> câu · <b>явле́ние</b> hiện tượng.</div>'
    '<div class="hd-warn"><b>Chữ л từ đâu ra:</b> gốc <b>яв-</b> gặp hậu tố thì mọc thêm <b>л</b> → <b>явл-</b>. Đây là "л chèn", chuyên xuất hiện sau các phụ âm môi <b>б п в ф м</b>: люби́ть → лю<b>бл</b>ю́ (tôi yêu), купи́ть → ку<b>пл</b>ю́ (tôi sẽ mua).</div>'
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
