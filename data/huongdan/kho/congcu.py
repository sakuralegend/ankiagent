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


def nap_lo_da_soan(chi=None):
    """Đọc mọi file kNN_*.py trong kho, trả {word: html} gộp.

    `chi` = danh sách id để chỉ đọc vài lô — dùng khi một lô tự soát mình.
    """
    gop, nguon = {}, {}
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
    return gop, nguon


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
           f"### file can tao: {lo['id']}_{lo['topic'].replace('::','-')}.py", ""]
    for wc in lo["tu"]:
        w = words.get(wc, {})
        cu = "   [DE GHI DE noi dung mnemonic cu]" if w.get("cu") else ""
        # Meaning là HTML <ol><li>…  -> gộp thành một dòng, bỏ thẻ
        en = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "",
                                        re.sub(r"</li>\s*<li>", " / ", w.get("en", "")))).strip()
        out.append(f'S["{wc}"]   {w.get("w","?")}   ({w.get("pos","?")})   '
                   f'{en}   |   {w.get("vi","")}{cu}')
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
            token = re.sub(r"<[^>]+>", "", m).strip()
            if not re.fullmatch(r"[А-Яа-яЁё́​-]+", token) or "-" in token:
                continue
            # (b) THIẾU DẤU TRỌNG ÂM = né bộ soát, không phải "an toàn".
            # Bộ soát chỉ đối chiếu được từ CÓ dấu; bỏ dấu là tự động qua cửa.
            # Từ ≥2 nguyên âm mà không dấu, không có ё (ё luôn mang trọng âm) -> báo.
            if (len(re.findall(r"[аеёиоуыэюяАЕЁИОУЫЭЮЯ]", token)) >= 2
                    and ACUTE not in token and "ё" not in token.lower()):
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
def cmd_dodai():
    """Đo độ dài từng thẻ. Trần 6–10 KB, tối đa ~12 KB — xem README §2.

    Dài quá thì user không đọc, mà không đọc thì hỏng đúng mục đích ô này.
    """
    chi = [a for a in sys.argv[2:] if re.fullmatch(r"k\d\d", a)] or None
    gop, nguon = nap_lo_da_soan(chi)
    L = sorted(((len(v), k) for k, v in gop.items()), reverse=True)
    if not L:
        print("chua co gi")
        return
    qua = [x for x in L if x[0] > 12000]
    print(f"{len(gop)} the | trung binh {sum(n for n, _ in L) // len(L)} "
          f"| dai nhat {L[0][0]} ({L[0][1]}) | QUA 12KB: {len(qua)}")
    for n, w in qua[:15]:
        print(f"  {n:6d}  {w}   [{nguon[w]}]")


def cmd_trangthai():
    q = doc_hangdoi()
    xong = [l for l in q["lo"] if l["trangthai"] == "xong"]
    # CHỈ đếm lô đã được luồng chính duyệt. Đếm mọi file kNN_*.py có trên đĩa
    # sẽ tính cả lô đang soạn dở của agent chạy song song -> báo cao hơn thật.
    gop, _ = nap_lo_da_soan([l["id"] for l in xong] or ["__khong_co__"])
    print(f"lo:  {len(xong)}/{q['tong_lo']}")
    print(f"tu:  {len(gop)}/{q['tong_tu']}  (da duyet)")
    da_nap = [l["id"] for l in xong if l.get("daNap")]
    chua_nap = [l["id"] for l in xong if not l.get("daNap")]
    print(f"nap: {len(da_nap)}/{len(xong)} lo da vao Anki"
          + (f"   chua nap: {' '.join(chua_nap)}" if chua_nap else ""))
    cho = [l["id"] for l in q["lo"] if l["trangthai"] == "cho"]
    print(f"con: {' '.join(cho[:12])}{' ...' if len(cho) > 12 else ''}")


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
    gop, _ = nap_lo_da_soan(ids_lo)
    print(f"da soan: {len(gop)} tu")

    ids = ac("findNotes", query="note:RU_Word")
    ban_do, hien_co = {}, {}
    for n in ac("notesInfo", notes=ids):
        # `noteId`, KHÔNG phải `id` — notesInfo trả về noteId, còn updateNoteFields
        # lại nhận khoá `id`. Hai đầu đặt tên khác nhau, dễ dính.
        nid = n["noteId"]
        ban_do.setdefault(khoa_note(n["fields"]["WordClean"]["value"]), []).append(nid)
        hien_co[nid] = n["fields"].get("HuongDan", {}).get("value", "")

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
     "xong": cmd_xong, "nap": cmd_nap, "dodai": cmd_dodai}[cmd]()
