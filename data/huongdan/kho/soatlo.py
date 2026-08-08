# -*- coding: utf-8 -*-
"""Cụm SOÁT OFFLINE của bộ công cụ soạn kho — tách từ congcu.py (03/08/2026, QD-18).

Ba việc, đều KHÔNG cần AnkiConnect: `soat` (nội dung lô đã soạn), `dodai`
(chiều cao dựng hình + ô đỏ), và lõi so va chạm nghĩa tiếng Việt (`cmd_vacham`
ở congcu.py gọi sang vì phần đọc thẻ cần Anki). Điểm vào vẫn là congcu.py.
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(HERE, ".."))
from khochung import ACUTE, ZWSP, NOUNS, bare, nap_lo_da_soan, BANG_RE    # noqa: E402
from mientru import MIEN_TRU                                              # noqa: E402

_BANG_RE = BANG_RE          # tên nội bộ giữ nguyên để ruột `uoc_cao` không đổi


def lech_trong_am(token, chuan):
    """Cụm in đậm có lệch trọng âm so với từ điển không? (`True` = lệch, phải báo)

    🔴 `ё` LÀ TRỌNG ÂM SẴN nên chuẩn mang `ё` thì so được ngay cả khi nó không có
    dấu sắc. Bản cũ bỏ qua mọi ô không có dấu sắc, tức thả nổi **5 230 dạng** của
    `nouns.csv` (đo 08/08) — đúng cửa để lọt `тве́рдость` (thật: `твёрдость`).

    Chuẩn có `ё` ⇒ so NGUYÊN VĂN: viết `е` chỗ đáng lẽ `ё` là sai chính tả.
    Chuẩn không có `ё` ⇒ vẫn gộp `ё→е` như cũ, vì lúc đó `ё` bên phía thẻ có thể
    là dạng ĐÚNG mà `nouns.csv` in thiếu (1 094/26 983 dòng có `ё`, phần còn lại
    in trần) — bắt bẻ ở đó là kêu oan.
    """
    co_yo = "ё" in chuan.lower()
    if (ACUTE not in chuan and not co_yo) or token in MIEN_TRU:
        return False          # tên riêng lưu trần -> không so được
    a = token.replace(ZWSP, "").lower()
    c = chuan.lower()
    return (a != c) if co_yo else (a.replace("ё", "е") != c.replace("ё", "е"))


# --------------------------------------------------------------- lệnh: soat
def load_nouns():
    import csv
    d = {}
    with io.open(NOUNS, encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            b = (row.get("bare") or "").strip().lower().replace("ё", "е")
            acc = (row.get("accented") or "").strip()
            if b and acc and b not in d:
                d[b] = acc.replace("'", ACUTE)
    return d


def cmd_soat():
    """Soát nội dung ĐÃ SOẠN NHƯNG CHƯA ĐẨY — không cần AnkiConnect.

    Đây là điểm khác duy nhất so với kiemtra.py: nguồn là file, không phải thẻ.
    Nhờ vậy soát được ngay trong lúc thẻ trong Anki còn nguyên chưa bị đụng.
    """
    chi = [a for a in sys.argv[2:] if re.fullmatch(r"k\d\d", a)] or None
    nouns = load_nouns()
    gop, nguon = nap_lo_da_soan(chi)
    print(f"tu dien: {len(nouns)} danh tu | dang soat: {len(gop)} tu"
          f"{' (lo ' + ' '.join(chi) + ')' if chi else ''}\n")

    sai, chua_tra, khong_dau, hong, khong_ho = [], set(), [], [], []
    for word, html in gop.items():
        # (a) CẤU TRÚC: thẻ mở/đóng phải cân, và phải có đủ mục
        # Đếm theo CẶP là chưa đủ: <b>…<b>…</b>…</b> vẫn cân bằng nhưng thẻ đóng
        # bên trong cắt in đậm giữa chừng khi hiển thị. Phải quét theo ĐỘ SÂU.
        for tag in ("div", "span", "b", "i", "u"):
            sau = 0
            for mt in re.finditer(f"<{tag}[ >]|</{tag}>", html):
                sau += 1 if mt.group()[1] != "/" else -1
                if sau < 0 or (tag in ("b", "i", "u") and sau > 1):
                    hong.append((word, nguon[word],
                                 f"<{tag}> long/lech tai vi tri {mt.start()}"))
                    break
            if sau > 0:
                hong.append((word, nguon[word], f"thieu {sau} the dong </{tag}>"))
        if "hd-sec" not in html:
            hong.append((word, nguon[word], "thieu .hd-sec"))
        # 🔴 THIẾU `.hd-fam` KHÔNG PHẢI LỖI — user chốt 29/07: *"những từ thực sự
        # không có như vậy thì không cần họ hàng, cái này để agent quyết định"*.
        #
        # Trước đó đây là lỗi cấu trúc, và lô phải sạch cửa này mới được duyệt.
        # Hậu quả thấy ngay ở k48: `бассе́йн` mượn thẳng tiếng Pháp `bassin`, không
        # có từ phái sinh Nga nào, agent buộc phải dựng một ô `.hd-fam` mà nội dung
        # chỉ là lời thú nhận "không có họ hàng gốc Nga" — viết ra để im cửa chứ
        # không phải để dạy. Lần đó agent trung thực nên vô hại; lần sau nó có thể
        # chọn cách rẻ hơn là BỊA một từ cùng gốc, đúng thứ README §2 cấm.
        # Đây chính là cơ chế "cửa kêu oan ⇒ lô sau thêm nội dung giả cho im cửa"
        # đã ghi ở cửa (b) — nay áp cho cả cửa này.
        #
        # Vẫn ĐẾM và in ra, chỉ không chặn: mục Họ hàng vắng phải là một lựa chọn
        # có ý thức của agent, không phải chỗ nó quên.
        if "hd-fam" not in html:
            khong_ho.append((word, nguon[word]))

        # (c) CHỮ TRỘN CYRILLIC + LATIN — lỗi gõ MẮT KHÔNG THẤY.
        # `а о е р с х у` Nga và Latin vẽ giống hệt nhau. Một chữ lọt vào giữa
        # từ Nga thì thẻ trông vẫn đúng nhưng đó không còn là từ đó nữa.
        # Lô k07 tự viết script bắt được `гốc` và `цapтa` — giữ lại thành cửa chung.
        # ⚠️ Dải chữ Latin phải viết TƯỜNG MINH. Viết tắt kiểu `À-ỹ` nuốt trọn cả
        # bảng Cyrillic (U+0400 nằm trong U+00C0–U+1EF9) -> báo nhầm mọi từ Nga.
        LAT = r"A-Za-zÀ-ɏḀ-ỿ"
        for tok in re.findall(rf"[{LAT}А-Яа-яЁё́]{{2,}}", re.sub(r"<[^>]+>", " ", html)):
            if re.search(r"[А-Яа-яЁё]", tok) and re.search(rf"[{LAT}]", tok):
                hong.append((word, nguon[word], f"chu TRON Cyrillic+Latin: {tok}"))

        for m in re.findall(r"<b>(.*?)</b>", html):
            noi_dung = re.sub(r"<[^>]+>", "", m).strip()
            # (d) CỤM NHIỀU CHỮ phải tách ra soi TỪNG CHỮ.
            # `fullmatch` trượt ngay ở dấu cách, nên trước đây MỌI cụm in đậm
            # (collocation, ví dụ ngắn) đi qua cửa mà không bị kiểm chút nào —
            # `между́ строк` lọt cả ba cửa, đúng phải là `ме́жду строк`.
            chu = [t.strip(".,;:!?()[]«»\"'…") for t in noi_dung.split()]
            # Cụm THUẦN NGA (mọi chữ đều Cyrillic) mới là collocation thật -> soi
            # cả dấu trọng âm. Còn câu tiêu đề tiếng Việt có kèm một từ Nga thì từ
            # đó thường được CỐ Ý viết trần để nêu mặt chữ; đòi dấu ở đó là kêu oan,
            # mà kêu oan thì lô sau sẽ thêm dấu giả cho im cửa — đúng thứ cần tránh.
            thuan_nga = all(re.fullmatch(r"[А-Яа-яЁё́​-]*", t) for t in chu)
            for i, token in enumerate(chu):
                if not re.fullmatch(r"[А-Яа-яЁё́​-]+", token) or "-" in token:
                    continue
                # `не́`/`ни́` hút trọng âm của từ đứng sau (не́ было, не́ был) ->
                # từ sau nó MẤT dấu là đúng chính tả, không phải thiếu sót.
                sau_ne = i > 0 and chu[i - 1].lower() in ("не́", "ни́")
                # (b) THIẾU DẤU TRỌNG ÂM = né bộ soát, không phải "an toàn".
            # Bộ soát chỉ đối chiếu được từ CÓ dấu; bỏ dấu là tự động qua cửa.
                # Từ ≥2 nguyên âm mà không dấu, không có ё (ё luôn mang trọng âm) -> báo.
                if (len(re.findall(r"[аеёиоуыэюяАЕЁИОУЫЭЮЯ]", token)) >= 2
                        and ACUTE not in token and "ё" not in token.lower()
                        and thuan_nga and not sau_ne):
                    khong_dau.append((word, nguon[word], token))

                b = bare(token)
                if b not in nouns:
                    chua_tra.add(b)
                    continue
                if lech_trong_am(token, nouns[b]):
                    sai.append((word, nguon[word], token, nouns[b]))

    print("=== CAU TRUC HTML ===")
    print("  (khong co)" if not hong else "")
    for w, f, ly in hong:
        print(f"  [{f}] {w:16s} {ly}")

    print("\n=== TU NGA IN DAM MA THIEU DAU TRONG AM ===")
    print("  (khong co)" if not khong_dau else "")
    for w, f, t in sorted(set(khong_dau))[:40]:
        print(f"  [{f}] the {w:16s} -> {t}")
    if len(set(khong_dau)) > 40:
        print(f"  ... con {len(set(khong_dau)) - 40}")

    # KHÔNG nằm trong "ba mục phải sạch" — đây là dòng để ĐỌC, không phải cửa.
    print(f"\n=== KHONG CO MUC HO HANG: {len(khong_ho)} the (khong phai loi) ===")
    if khong_ho:
        print("  " + " · ".join(w for w, _ in khong_ho[:25])
              + (" ..." if len(khong_ho) > 25 else ""))
        print("  -> Dung neu tu do that su khong co ho hang chac chan (tu goc tron,")
        print("     hu tu, tu muon dung mot minh). SAI neu chi la quen. Agent quyet dinh.")

    print("\n=== TRONG AM LECH so voi tu dien ===")
    if not sai:
        print("  (khong co)")
    seen = set()
    for w, f, mine, ref in sai:
        if (mine, ref) in seen:
            continue
        seen.add((mine, ref))
        print(f"  [{f}] the {w:16s} toi viet {mine:20s} tu dien {ref}")

    # Danh sách này dài tới ~950 từ khi soát cả kho. In hết vào màn hình là đổ
    # thẳng vào context của người đọc — tốn vô ích, mà đọc một mạch 950 từ thì
    # cũng không ai đọc nổi. Ghi ra file, màn hình chỉ giữ phần xem được.
    dai = sorted(x for x in chua_tra if len(x) >= 4)
    fn = os.path.join(HERE, "_phaidocbangmat.txt")
    io.open(fn, "w", encoding="utf-8").write("\n".join(dai))
    print(f"\n=== PHAI DOC BANG MAT: {len(dai)} tu ===")
    if chi:                      # soát một lô -> in hết, đó là việc của lô đó
        print("  " + ", ".join(dai))
    else:                        # soát cả kho -> chỉ trích, phần còn lại ở file
        print("  " + ", ".join(dai[:60]))
        print(f"  ... {len(dai) - 60} tu nua -> {os.path.basename(fn)}")
    print("\n⚠️ 'Chua tra duoc' KHONG phai 'dung' — nouns.csv chi co DANH TU.")


# ---------------------------------------------------------- lệnh: dodai
TRAN_WARN = 2        # số ô đỏ (.hd-warn) tối đa mỗi thẻ

# ---- TRẦN THẬT: VỪA MỘT MÀN HÌNH iPHONE (user chốt 28/07) ----------------
# Byte là đại lượng SAI để đo cái user thật sự quan tâm. User nói thẳng:
# "toàn bộ nội dung đó chỉ được hiện trên 1 mặt màn hình iPhone thôi".
# Nên đo bằng CHIỀU CAO DỰNG HÌNH ước lượng, theo đúng số trong card.css.
#
# MÁY THẬT CỦA USER: iPhone 16 Pro Max = 440 x 956 pt (CSS px).
# Ghi rõ từng bước trừ để sau này đổi máy thì sửa được, đừng đoán lại:
#   BỀ RỘNG  440 − .card-container padding 20×2 = 400 − .hd-content 16×2 = 368px
#   CHIỀU CAO 956 − thanh trên + Dynamic Island ~103 − nút trả lời ~100 = ~753px
#             − thanh "Hướng dẫn (bấm để mở rộng)" ~40px  ->  ~713px
#   Lấy 700px cho chẵn và chừa sai số.
TRAN_CAO = 700       # px — quá số này là PHẢI CUỘN, tức vỡ yêu cầu "1 mặt màn hình"
NHAM_CAO = 600       # px — nhắm dưới mức này cho thoải mái
BE_RONG = 368        # px bề rộng chữ trong .hd-content


def _dong(chu, px_font, be_rong=BE_RONG):
    """Số dòng khi chữ tự xuống hàng. Bề rộng ký tự trung bình ~0,5 cỡ chữ
    với font sans tỉ lệ (-apple-system). Chữ Việt có dấu không rộng thêm."""
    moi_dong = max(1, int(be_rong / (px_font * 0.5)))
    return max(1, -(-len(chu) // moi_dong))


def uoc_cao(html):
    """Ước lượng chiều cao dựng hình (px) của một ô Hướng dẫn.

    Không phải trình duyệt, nên đây là XẤP XỈ — nhưng sai số vài chục px
    không đổi kết luận, còn byte thì sai hẳn về CHẤT: một bảng 6 dòng và
    một đoạn văn cùng số byte chiếm chiều cao khác nhau tới ba lần.
    """
    # 🔴 GỠ BẢNG CHIA TRƯỚC KHI ĐO. Bảng gấp trong <details> lồng nên lúc đóng
    # nó chiếm đúng một dòng tiêu đề — tính cả ruột bảng vào thì mọi thẻ đều
    # "vỡ trần 700px" và cái trần mất hết ý nghĩa. Trần đo phần user PHẢI đọc,
    # còn bảng là thứ user chủ động bấm vào mới xem.
    co_bang = 'class="gt-bang"' in (html or "")     # phải hỏi TRƯỚC khi gỡ
    html = _BANG_RE.sub("", html or "")
    cao = 28 + (30 if co_bang else 0)               # thanh tiêu đề bảng lúc đóng
    for m in re.finditer(
            r'<div class="(hd-sec|hd-row|hd-why|hd-fam|hd-warn)"[^>]*>(.*?)</div>\s*(?=<div|$)',
            html, re.S):
        lop, ruot = m.group(1), re.sub(r"<[^>]+>", "", m.group(2)).strip()
        if lop == "hd-sec":
            cao += 16 + 21                       # 10px chữ + margin 14/7
        elif lop == "hd-row":
            cao += _dong(ruot, 13, BE_RONG - 74) * 24 + 6   # cột nghĩa hẹp hơn
        elif lop == "hd-why":
            cao += _dong(ruot, 14) * 22.4 + 8
        elif lop == "hd-fam":
            cao += _dong(ruot, 13) * 22.75
        elif lop == "hd-warn":
            cao += _dong(ruot, 13, BE_RONG - 25) * 19.5 + 25
    return int(cao)


def cmd_dodai():
    """Đo độ dài VÀ đếm ô đỏ từng thẻ — xem README §2b.

    🔴 Đếm ô đỏ mới là cửa quan trọng. Suốt 16 lô đầu chỉ có trần byte, nên
    thẻ "đạt" 12 KB vẫn có tới 16 ô đỏ và user đọc xong không nhớ gì — đúng
    thứ mà độ dài định phục vụ thì lại hỏng. Trần byte một mình KHÔNG đủ.
    """
    chi = [a for a in sys.argv[2:] if re.fullmatch(r"k\d\d", a)] or None
    gop, nguon = nap_lo_da_soan(chi)
    L = sorted(((len(v), k) for k, v in gop.items()), reverse=True)
    if not L:
        print("chua co gi")
        return
    W = {k: v.count("hd-warn") for k, v in gop.items()}
    C = {k: uoc_cao(v) for k, v in gop.items()}
    cao = sorted(((n, k) for k, n in C.items() if n > TRAN_CAO), reverse=True)
    do = sorted(((n, k) for k, n in W.items() if n > TRAN_WARN), reverse=True)
    print(f"{len(gop)} the | CAO tb {sum(C.values()) // len(C)}px "
          f"| cao nhat {max(C.values())}px ({max(C, key=C.get)}) "
          f"| QUA 1 MAN HINH ({TRAN_CAO}px): {len(cao)}")
    print(f"{'':>9} o do tb {sum(W.values()) / len(W):.1f} "
          f"| nhieu nhat {max(W.values())} "
          f"({max(W, key=W.get)}) | QUA {TRAN_WARN} O DO: {len(do)}")
    print(f"{'':>9} byte tb {sum(n for n, _ in L) // len(L)} (tham khao)")

    # KHỐI DÙNG CHUNG: mục .hd-sec nào xuất hiện ở >=50% số thẻ thì đó là khối
    # lặp, không phải nội dung của từ. §3 — mặc định phải là 0%; ở k04 nó nuốt
    # 80% độ dài thẻ và đẩy chính cái từ ra rìa.
    dem, dai = {}, {}
    for v in gop.values():
        p = re.split(r'<div class="hd-sec">(.*?)</div>', v)
        for i in range(1, len(p), 2):
            ten = re.sub(r"<[^>]+>", "", p[i]).strip()
            dem[ten] = dem.get(ten, 0) + 1
            dai[ten] = dai.get(ten, 0) + len(p[i]) + (len(p[i + 1]) if i + 1 < len(p) else 0)
    coc = {"Chẻ từ", "Cách nhớ", "Họ hàng"}
    chung = [(t, c) for t, c in dem.items() if c >= len(gop) * 0.5 and t not in coc]
    tong = sum(len(v) for v in gop.values())
    pc = 100 * sum(dai[t] for t, _ in chung) / tong if tong else 0
    print(f"{'':>9} khoi dung chung: {pc:.0f}% do dai the"
          f"{'  <- QUA NHIEU, xem README §3' if pc > 15 else ''}")
    for t, c in sorted(chung, key=lambda x: -x[1]):
        print(f"     lap x{c}/{len(gop)}  {dai[t]:6d}b  {t[:60]}")

    for n, w in cao[:15]:
        print(f"  cao   {n:6d}px  {w}   [{nguon[w]}]  = {n / TRAN_CAO:.1f} man hinh")
    for n, w in do[:15]:
        print(f"  o do  {n:6d}    {w}   [{nguon[w]}]")


# ------------------------------------------------- va chạm nghĩa tiếng Việt
def tach_nghia(vi):
    """Tách một dòng tiếng Việt thành các nghĩa rời để so trùng.

    `Vietnamese` viết kiểu "nói, bảo, cho biết" — mỗi cụm là MỘT đáp án mà
    user có thể nhìn vào rồi gõ. Nên so trùng phải so từng cụm, không so cả
    dòng: "nói, bảo" và "nói, trò chuyện" khác nhau nguyên dòng nhưng cùng
    chứa "nói", tức vẫn là đề bài hai đáp án.
    """
    vi = re.sub(r"<[^>]+>", " ", vi or "").lower()
    vi = re.sub(r"\([^)]*\)", " ", vi)          # bỏ phần chú trong ngoặc
    ra = set()
    for cum in re.split(r"[,;/·|]|\bhoặc\b|\bhay là\b", vi):
        cum = re.sub(r"\s+", " ", cum).strip(" .…")
        # cụm quá ngắn hoặc chỉ là hư từ thì bỏ, kẻo báo trùng tràn lan
        if len(cum) >= 2 and cum not in ("và", "là", "của", "cho", "một"):
            ra.add(cum)
    return ra


def do_va_cham(notes):
    """{nghĩa Việt: [các từ Nga cùng mang nghĩa đó]} — chỉ giữ nghĩa >= 2 từ."""
    theo = {}
    for wc, vi in notes.items():
        for ng in tach_nghia(vi):
            theo.setdefault(ng, set()).add(wc)
    return {k: sorted(v) for k, v in theo.items() if len(v) > 1}
