# -*- coding: utf-8 -*-
"""Bộ công cụ soạn kho — một file, bốn lệnh.

Vì sao gộp một file: 703 từ chia 56 lô, tôi sẽ gọi bộ này ~56 lần qua nhiều
phiên chat. Càng ít thứ phải nhớ càng ít chỗ sai.

    python data/huongdan/kho/congcu.py tiep          # in dữ liệu lô kế tiếp để soạn
    python data/huongdan/kho/congcu.py soat          # soát toàn bộ lô đã soạn (KHÔNG cần Anki)
    python data/huongdan/kho/congcu.py trangthai     # còn bao nhiêu
    python data/huongdan/kho/congcu.py nap [--apply] # ĐẨY vào Anki — chỉ chạy khi user bảo

🔴 Lô soạn xong là file `kNN_<topic>.py` CHỈ CHỨA `S = {...}` — dữ liệu thuần,
không boilerplate, không tự gọi Anki. Việc đẩy là của `nap`, một lần, cuối cùng.
Nhờ vậy user "để riêng ra một chỗ" được đúng như yêu cầu: thẻ trong Anki không
bị đụng cho tới lúc user cho phép.
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
}


def bare(w):
    return w.replace(ACUTE, "").replace(ZWSP, "").replace("'", "").lower().replace("ё", "е")


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

    dai = sorted(x for x in chua_tra if len(x) >= 4)
    print(f"\n=== PHAI DOC BANG MAT: {len(dai)} tu ===")
    print("  " + ", ".join(dai))
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
    gop, _ = nap_lo_da_soan()
    print(f"lo:  {len(xong)}/{q['tong_lo']}")
    print(f"tu:  {len(gop)}/{q['tong_tu']}")
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
    """Đẩy TẤT CẢ lô đã soạn vào Anki — chỉ chạy khi user bảo.

    KHÔNG dùng `findNotes WordClean:<từ>` cho từng từ. Hai lý do:
      * 703 lần gọi mạng thì chậm và dễ đứt giữa chừng;
      * bộ sưu tập có thẻ TRÙNG do ký tự zero-width U+200B (`петь` vs `петь​`,
        `пить` vs `пить​`). Anki coi là hai note khác nhau, mắt thường không
        phân biệt được. Tra từng từ thì mỗi cặp sẽ bị bỏ sót một thẻ.
    ⇒ Kéo TOÀN BỘ WordClean về một lần, ghép theo khoá đã bỏ U+200B, và ghi
      vào MỌI note khớp — thẻ trùng thì cả hai đều nhận nội dung.
    """
    apply = "--apply" in sys.argv
    gop, _ = nap_lo_da_soan()
    print(f"da soan: {len(gop)} tu")

    ids = ac("findNotes", query="note:RU_Word")
    ban_do = {}
    for n in ac("notesInfo", notes=ids):
        ban_do.setdefault(bare(n["fields"]["WordClean"]["value"]), []).append(n["id"])

    ok, miss, doi = 0, [], 0
    for word, html in gop.items():
        nids = ban_do.get(bare(word), [])
        if not nids:
            miss.append(word)
            continue
        if len(nids) > 1:
            doi += 1
        for nid in nids:
            if apply:
                ac("updateNoteFields", note={"id": nid, "fields": {"HuongDan": html}})
            ok += 1
    print(f"ghi vao {ok} note ({doi} tu co the trung, ghi ca hai)")
    for w in miss:
        print(f"  !! khong tim thay note cho: {w}")
    print("da ghi. sync: " + str(ac("sync")) if apply
          else "(chua ghi gi — them --apply de ghi that)")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "trangthai"
    {"tiep": cmd_tiep, "soat": cmd_soat, "trangthai": cmd_trangthai,
     "xong": cmd_xong, "nap": cmd_nap, "dodai": cmd_dodai}[cmd]()
