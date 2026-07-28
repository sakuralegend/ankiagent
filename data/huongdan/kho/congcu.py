# -*- coding: utf-8 -*-
"""Bộ công cụ soạn kho — một file, bốn lệnh.

Vì sao gộp một file: 703 từ chia 56 lô, tôi sẽ gọi bộ này ~56 lần qua nhiều
phiên chat. Càng ít thứ phải nhớ càng ít chỗ sai.

    python data/huongdan/kho/congcu.py tiep          # in dữ liệu lô kế tiếp để soạn
    python data/huongdan/kho/congcu.py soat          # soát toàn bộ lô đã soạn (KHÔNG cần Anki)
    python data/huongdan/kho/congcu.py trangthai     # còn bao nhiêu
    python data/huongdan/kho/congcu.py nap [--apply] # ĐẨY vào Anki — chỉ lô đã duyệt & chưa nạp

🔴 Lô soạn xong là file `kNN_<topic>.py` CHỈ CHỨA `S = {...}` — dữ liệu thuần,
không boilerplate, không tự gọi Anki. Agent phụ KHÔNG bao giờ đụng Anki; việc
đẩy là của `nap`, do luồng chính gọi sau khi đã soát.

Từ 27/07 `nap` chạy được sau MỖI lô thay vì gom một cục cuối đường: nó chỉ đọc
lô `trangthai == "xong"` và ghi sổ `daNap` vào hangdoi.json, nên lô đang soạn dở
không thể lọt vào thẻ thật và không lô nào bị nạp hai lần.
"""
import glob
import importlib.util
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
HANGDOI = os.path.join(HERE, "hangdoi.json")
TUDIEN = os.path.join(HERE, "tudien.json")
NOUNS = os.path.join(HERE, "..", "..", "nouns.csv")
ANKI = "http://127.0.0.1:8765"
ACUTE = "́"
ZWSP = "​"

# Từ ĐỒNG TỰ — máy không phân biệt được, miễn trừ tay, mỗi mục ghi rõ lý do.
MIEN_TRU = {
    "ви́на": "số nhiều của вино́ (rượu vang); từ điển chỉ có вина́ = lỗi lầm",
    "жила́": "quá khứ giống cái của động từ жить (sống); từ điển chỉ có danh từ жи́ла = gân, mạch",
    "запа́х": "đồng tự với за́пах (mùi): запа́х = vạt áo choàng chồng lên nhau (từ запахну́ть); "
             "thẻ k05 dạy đúng cặp trọng âm này, từ điển chỉ có за́пах",
    "помо́чь": "ĐỘNG TỪ помо́чь = giúp đỡ (thể hoàn thành của помога́ть); từ điển chỉ có danh từ "
              "phương ngữ по́мочь = buổi làm giúp tập thể (số nhiều по́мочи = dây đeo quần)",
}


def bare(w):
    """Khoá TRA TỪ ĐIỂN trọng âm — gộp ё về е vì nouns.csv in ё thành е.
    ĐỪNG dùng để ghép với note Anki: xem `khoa_note`."""
    return w.replace(ACUTE, "").replace(ZWSP, "").replace("'", "").lower().replace("ё", "е")


def khoa_note(w):
    """Khoá GHÉP VỚI NOTE ANKI — GIỮ NGUYÊN ё.

    ё và е phân biệt những từ khác hẳn nhau: всё (mọi thứ) ≠ все (mọi người),
    нёбо (vòm miệng) ≠ небо (bầu trời). Dùng `bare` ở đây thì hai note gộp làm
    một khoá, và `nap` ghi nội dung của từ này đè lên thẻ của từ kia. Đã xảy ra
    thật 28/07: thẻ всё nhận nguyên ô Hướng dẫn của все.
    """
    return w.replace(ACUTE, "").replace(ZWSP, "").replace("'", "").lower()


def doc_hangdoi():
    return json.load(io.open(HANGDOI, encoding="utf-8"))


def ghi_hangdoi(q):
    io.open(HANGDOI, "w", encoding="utf-8").write(json.dumps(q, ensure_ascii=False, indent=1))


def nap_lo_da_soan(chi=None, lay_v=False):
    """Đọc mọi file kNN_*.py trong kho, trả {word: html} gộp.

    `chi` = danh sách id để chỉ đọc vài lô — dùng khi một lô tự soát mình.
    `lay_v` = trả thêm dict `V` (bản tiếng Việt sửa lại) của các lô đó.

    File lô có thể khai báo HAI dict:
      S = {từ: html ô Hướng dẫn}      — bắt buộc
      V = {từ: "nghĩa tiếng Việt"}    — tuỳ chọn, CHỈ những từ cần sửa
    """
    gop, nguon, vi = {}, {}, {}
    for path in sorted(glob.glob(os.path.join(HERE, "k[0-9][0-9]_*.py"))):
        if chi and os.path.basename(path)[:3] not in chi:
            continue
        spec = importlib.util.spec_from_file_location("lo_" + os.path.basename(path)[:3], path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        for w, html in getattr(mod, "S", {}).items():
            if w in gop:
                print(f"  !! TRUNG '{w}': {nguon[w]} va {os.path.basename(path)}")
            gop[w] = html
            nguon[w] = os.path.basename(path)
        vi.update(getattr(mod, "V", {}))
    return (gop, nguon, vi) if lay_v else (gop, nguon)


# --------------------------------------------------------------- lệnh: tiep
def cmd_tiep():
    """In dữ liệu thô của một lô — đây là input để soạn.

    Nhận id cụ thể (`tiep k07`) vì các lô chạy SONG SONG trong nhiều context
    riêng; không có id thì mỗi lô sẽ giành nhau đúng một lô đầu hàng đợi.
    """
    xin = next((a for a in sys.argv[2:] if re.fullmatch(r"k\d\d", a)), None)
    q = doc_hangdoi()
    if xin:
        lo = next((l for l in q["lo"] if l["id"] == xin), None)
        if lo is None:
            print(f"khong co lo {xin}")
            return
    else:
        lo = next((l for l in q["lo"] if l["trangthai"] == "cho"), None)
    if not lo:
        print("HET HANG DOI — 56/56 lo xong.")
        return
    words = {w["wc"]: w for w in json.load(io.open(TUDIEN, encoding="utf-8"))}
    xong = sum(1 for l in q["lo"] if l["trangthai"] == "xong")
    out = [f"### {lo['id']}  topic={lo['topic']}  ({len(lo['tu'])} tu)"
           f"   [{xong}/{q['tong_lo']} lo xong]",
           f"### file can tao: {lo['id']}_{lo['topic'].replace('::','-')}.py"]
    # Lô ghép tay mang sẵn TRỤC của nó — nói ra để agent xây khối dùng chung
    # quanh đúng trục đó, thay vì tự mò một trục khác rồi lô thành rời rạc.
    if lo.get("thucong"):
        out.append(f"### TRUC CUA LO (da ghep tay theo nghia): {lo['thucong']}")
    out.append("")
    out.append("### VIEC THU HAI: SUA FIELD TIENG VIET (dict V, xem README §2c)")
    out.append("### Dong tieng Viet duoi day la DE BAI cua deck 1-go — user GO tu Nga tu no.")
    out.append("### Mo ho la de bai khong co dap an dung: 'noi' khong phan biet duoc")
    out.append("### сказать (hoan thanh) voi говорить (chua hoan thanh).")
    out.append("### Them V[\"tu\"] = \"...\" CHI cho tu nao that su can sua.")
    out.append("")
    # LÔ SỬA (`sua: true`): thẻ ĐÃ có nội dung dùng được, chỉ vá chỗ thiếu.
    # Agent không được đụng Anki (§7), nên nội dung hiện tại phải do `tiep`
    # kéo về sẵn — nếu không agent sẽ viết đè và xoá mất phần đang tốt.
    cu_hd = {}
    if lo.get("sua"):
        try:
            ids = ac("findNotes", query="note:RU_Word")
            for n in ac("notesInfo", notes=ids):
                f = n["fields"]
                cu_hd[khoa_note(f.get("WordClean", {}).get("value", ""))] = \
                    f.get("HuongDan", {}).get("value", "")
        except Exception as e:
            out.append(f"### !! KHONG LAY DUOC NOI DUNG HIEN TAI ({e}) — DUNG LAI, bao luong chinh")
    for wc in lo["tu"]:
        w = words.get(wc, {})
        cu = "   [DE GHI DE noi dung mnemonic cu]" if w.get("cu") else ""
        # Meaning là HTML <ol><li>…  -> gộp thành một dòng, bỏ thẻ
        en = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "",
                                        re.sub(r"</li>\s*<li>", " / ", w.get("en", "")))).strip()
        out.append(f'S["{wc}"]   {w.get("w","?")}   ({w.get("pos","?")})   '
                   f'{en}   |   {w.get("vi","")}{cu}')
        if lo.get("sua"):
            hd = cu_hd.get(khoa_note(wc), "")
            out.append(f"### NOI DUNG HIEN TAI cua {wc} ({len(hd)} byte) — GIU LAI phan dang "
                       f"tot, chi va cho thieu:\n{hd or '(TRONG)'}\n")
    io.open(os.path.join(HERE, f"_input_{lo['id']}.txt"), "w", encoding="utf-8").write(
        "\n".join(out))
    print("\n".join(out))


def cmd_xong():
    """Đánh dấu lô đã soạn xong. CHỈ luồng chính gọi, sau khi đã soát —
    lô tự đánh dấu mình xong thì bộ soát mất hết ý nghĩa."""
    ids = [a for a in sys.argv[2:] if re.fullmatch(r"k\d\d", a)]
    q = doc_hangdoi()
    for l in q["lo"]:
        if l["id"] in ids:
            l["trangthai"] = "xong"
            l["file"] = f"{l['id']}_{l['topic'].replace('::', '-')}.py"
    ghi_hangdoi(q)
    print(f"danh dau xong: {' '.join(ids)}")


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

    sai, chua_tra, khong_dau, hong = [], set(), [], []
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
        for lop in ("hd-sec", "hd-fam"):
            if lop not in html:
                hong.append((word, nguon[word], f"thieu .{lop}"))

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
                chuan = nouns[b]
                if ACUTE not in chuan or token in MIEN_TRU:
                    continue          # tên riêng lưu trần -> không so được
                if token.replace(ZWSP, "").lower().replace("ё", "е") != chuan.lower().replace("ё", "е"):
                    sai.append((word, nguon[word], token, chuan))

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


# ---------------------------------------------------------- lệnh: trangthai
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
    cao = 28  # padding trên+dưới của .hd-content
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


def cmd_trangthai():
    q = doc_hangdoi()
    xong = [l for l in q["lo"] if l["trangthai"] == "xong"]
    # CHỈ đếm lô đã được luồng chính duyệt. Đếm mọi file kNN_*.py có trên đĩa
    # sẽ tính cả lô đang soạn dở của agent chạy song song -> báo cao hơn thật.
    gop, _ = nap_lo_da_soan([l["id"] for l in xong] or ["__khong_co__"])
    # trangthai "dat" = thẻ đã có nội dung ĐẠT CHUẨN sẵn, không cần soạn lại.
    # Không phải "xong" (không có file kNN_*.py, `nap` phải bỏ qua) và cũng
    # không phải "cho" (không ai phải làm gì). Thiếu trạng thái này thì bộ đếm
    # `tu:` không bao giờ chạm tổng, và phiên sau sẽ tưởng còn việc chưa làm.
    dat = [l for l in q["lo"] if l["trangthai"] == "dat"]
    n_dat = sum(len(l["tu"]) for l in dat)
    print(f"lo:  {len(xong)}/{q['tong_lo']}"
          + (f"   (+{len(dat)} lo 'dat chuan san')" if dat else ""))
    print(f"tu:  {len(gop) + n_dat}/{q['tong_tu']}  (da duyet"
          + (f", trong do {n_dat} tu dat chuan san)" if n_dat else ")"))
    da_nap = [l["id"] for l in xong if l.get("daNap")]
    chua_nap = [l["id"] for l in xong if not l.get("daNap")]
    print(f"nap: {len(da_nap)}/{len(xong)} lo da vao Anki"
          + (f"   chua nap: {' '.join(chua_nap)}" if chua_nap else ""))
    cho = [l["id"] for l in q["lo"] if l["trangthai"] == "cho"]
    print(f"con: {' '.join(cho[:12])}{' ...' if len(cho) > 12 else ''}")


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


def cmd_vacham():
    """Soi TOÀN BỘ bộ sưu tập: đề bài tiếng Việt nào có nhiều hơn một đáp án.

    User không biết trước sẽ học từ nào, nên yêu cầu là **mỗi đề bài đúng một
    đáp án**. Agent soạn một lô KHÔNG nhìn thấy 907 thẻ còn lại, nên nó không
    thể tự phát hiện va chạm — bắt buộc phải có cửa này ở luồng chính.
    """
    notes = {}
    for n in ac("notesInfo", notes=ac("findNotes", query="note:RU_Word")):
        f = n["fields"]
        notes[f.get("WordClean", {}).get("value", "")] = \
            f.get("Vietnamese", {}).get("value", "")
    vc = do_va_cham(notes)
    tong = sum(len(v) for v in vc.values())
    print(f"{len(notes)} the | {len(vc)} nghia Viet bi TRUNG, dinh {tong} luot tu\n")
    for ng, tu in sorted(vc.items(), key=lambda x: (-len(x[1]), x[0]))[:40]:
        print(f"  '{ng}'  ->  {' · '.join(tu)}")
    fn = os.path.join(HERE, "_vacham_vi.txt")
    io.open(fn, "w", encoding="utf-8").write(
        "\n".join(f"{ng}\t{' · '.join(tu)}" for ng, tu in sorted(vc.items())))
    print(f"\n-> day du: {os.path.basename(fn)}")


# --------------------------------------------------------------- lệnh: nap
def ac(action, **params):
    import urllib.request
    req = urllib.request.Request(
        ANKI, json.dumps({"action": action, "version": 6, "params": params}).encode())
    out = json.load(urllib.request.urlopen(req, timeout=300))
    if out.get("error"):
        raise RuntimeError(f"{action}: {out['error']}")
    return out["result"]


def cmd_nap():
    """Đẩy vào Anki các lô ĐÃ DUYỆT mà CHƯA nạp.

    Nạp theo từng lô (thay vì gom một cục cuối đường) an toàn nhờ ba chốt:

      1. **Chỉ đọc lô có `trangthai == "xong"`** — y hệt `trangthai`. Đọc mọi
         file kNN_*.py trên đĩa sẽ vớ luôn file đang soạn dở của agent chạy
         song song và đẩy nội dung CHƯA SOÁT vào thẻ thật.
      2. **`daNap` trong hangdoi.json là sổ cái** — lô nào đã vào Anki thì ghi
         lại, lần sau không đụng nữa. Muốn đẩy lại thì `--tatca`.
      3. **Ghi khi nội dung KHÁC** — trùng thì bỏ qua, không làm bẩn USN,
         gói sync nhẹ hơn và không đội thẻ lên khi bấm nhầm hai lần.

    Ghi field `HuongDan` KHÔNG phải schema mod (field có sẵn từ đợt trước),
    nên không kích hoạt full sync — laptop vẫn sync thường với iPhone/VPS.

    KHÔNG dùng `findNotes WordClean:<từ>` cho từng từ. Hai lý do:
      * 703 lần gọi mạng thì chậm và dễ đứt giữa chừng;
      * bộ sưu tập có thẻ TRÙNG do ký tự zero-width U+200B (`петь` vs `петь​`,
        `пить` vs `пить​`). Anki coi là hai note khác nhau, mắt thường không
        phân biệt được. Tra từng từ thì mỗi cặp sẽ bị bỏ sót một thẻ.
    ⇒ Kéo TOÀN BỘ WordClean về một lần, ghép theo khoá đã bỏ U+200B, và ghi
      vào MỌI note khớp — thẻ trùng thì cả hai đều nhận nội dung.
    """
    apply = "--apply" in sys.argv
    tatca = "--tatca" in sys.argv
    q = doc_hangdoi()
    xong = [l for l in q["lo"] if l["trangthai"] == "xong"]
    can = [l for l in xong if tatca or not l.get("daNap")]
    if not can:
        print(f"khong co lo moi de nap ({len(xong)} lo da duyet, tat ca da nap)")
        return
    ids_lo = [l["id"] for l in can]
    print(f"nap {len(can)} lo: {' '.join(ids_lo)}")
    gop, _, vi_moi = nap_lo_da_soan(ids_lo, lay_v=True)
    print(f"da soan: {len(gop)} tu" + (f" | sua tieng Viet: {len(vi_moi)} tu" if vi_moi else ""))

    ids = ac("findNotes", query="note:RU_Word")
    ban_do, hien_co, vi_co = {}, {}, {}
    for n in ac("notesInfo", notes=ids):
        # `noteId`, KHÔNG phải `id` — notesInfo trả về noteId, còn updateNoteFields
        # lại nhận khoá `id`. Hai đầu đặt tên khác nhau, dễ dính.
        nid = n["noteId"]
        ban_do.setdefault(khoa_note(n["fields"]["WordClean"]["value"]), []).append(nid)
        hien_co[nid] = n["fields"].get("HuongDan", {}).get("value", "")
        vi_co[nid] = n["fields"].get("Vietnamese", {}).get("value", "")

    # Field `Vietnamese` là ĐỀ BÀI của deck 1-go (user gõ từ Nga từ dòng này),
    # nên sửa nó là sửa cái user phải trả lời — đổi thì phải in ra để soát mắt.
    n_vi = 0
    for word, moi in vi_moi.items():
        for nid in ban_do.get(khoa_note(word), []):
            if vi_co.get(nid) == moi:
                continue
            print(f"  vi: {word:16s} '{vi_co.get(nid,'')}'  ->  '{moi}'")
            if apply:
                ac("updateNoteFields", note={"id": nid, "fields": {"Vietnamese": moi}})
            n_vi += 1
    if vi_moi:
        print(f"  -> doi tieng Viet {n_vi} note")

    ok, bo_qua, miss, doi = 0, 0, [], 0
    for word, html in gop.items():
        nids = ban_do.get(khoa_note(word), [])
        if not nids:
            miss.append(word)
            continue
        if len(nids) > 1:
            doi += 1
        for nid in nids:
            if hien_co.get(nid) == html:
                bo_qua += 1
                continue
            if apply:
                ac("updateNoteFields", note={"id": nid, "fields": {"HuongDan": html}})
            ok += 1
    print(f"ghi vao {ok} note, bo qua {bo_qua} (da trung noi dung), "
          f"{doi} tu co the trung -> ghi ca hai")
    for w in miss:
        print(f"  !! khong tim thay note cho: {w}")
    if not apply:
        print("(chua ghi gi — them --apply de ghi that)")
        return
    if miss:
        # Thiếu note = hàng đợi và bộ sưu tập lệch nhau. Đánh dấu daNap lúc này
        # sẽ chôn luôn những từ chưa vào -> để nguyên, chạy lại sau khi đã hiểu.
        print("  !! CO TU KHONG TIM THAY -> KHONG danh dau daNap. Xu ly roi chay lai.")
        return
    for l in q["lo"]:
        if l["id"] in ids_lo:
            l["daNap"] = True
    ghi_hangdoi(q)
    print(f"da ghi + danh dau daNap: {' '.join(ids_lo)}")
    print("sync: " + str(ac("sync")))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "trangthai"
    {"tiep": cmd_tiep, "soat": cmd_soat, "trangthai": cmd_trangthai,
     "xong": cmd_xong, "nap": cmd_nap, "dodai": cmd_dodai,
     "vacham": cmd_vacham}[cmd]()
