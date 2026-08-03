# -*- coding: utf-8 -*-
"""Bộ công cụ soạn kho — MỘT điểm vào, chín lệnh.

Vì sao gộp một điểm vào: 703 từ chia 56 lô, tôi sẽ gọi bộ này ~56 lần qua nhiều
phiên chat. Càng ít thứ phải nhớ càng ít chỗ sai.

    python data/huongdan/kho/congcu.py tiep          # in dữ liệu lô kế tiếp để soạn
    python data/huongdan/kho/congcu.py soat          # soát toàn bộ lô đã soạn (KHÔNG cần Anki)
    python data/huongdan/kho/congcu.py trangthai     # còn bao nhiêu
    python data/huongdan/kho/congcu.py nap [--apply] # ĐẨY vào Anki — chỉ lô đã duyệt & chưa nạp

Ruột chia ba file cùng thư mục (03/08/2026, QD-18 — trước đó một file 912 dòng):
  `khochung.py`  lõi dùng chung (khoá chữ, hàng đợi, đọc lô, bảng chia, dấu chuẩn)
  `soatlo.py`    lệnh soát OFFLINE (`soat`, `dodai`) + lõi so va chạm nghĩa
  `congcu.py`    điểm vào + các lệnh ĐỤNG Anki (`nap`, `bang`, `moi`, `vacham`…)

🔴 Lô soạn xong là file `kNN_<topic>.py` CHỈ CHỨA `S = {...}` — dữ liệu thuần,
không boilerplate, không tự gọi Anki. Agent phụ KHÔNG bao giờ đụng Anki; việc
đẩy là của `nap`, do luồng chính gọi sau khi đã soát.

Từ 27/07 `nap` chạy được sau MỖI lô thay vì gom một cục cuối đường: nó chỉ đọc
lô `trangthai == "xong"` và ghi sổ `daNap` vào hangdoi.json, nên lô đang soạn dở
không thể lọt vào thẻ thật và không lô nào bị nạp hai lần.
"""
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(HERE, ".."))
from anki_tools import grammar, soat_nguphap                      # noqa: E402
from anki_tools.anki_client import sync_truoc_khi_ghi_lo          # noqa: E402
# Tên lấy lại từ hai file ruột — GIỮ NGUYÊN cả bộ vì `dochuan.py` import congcu
# như thư viện (congcu._BANG_RE, congcu.uoc_cao, congcu.TRAN_CAO…).
from khochung import (ACUTE, ZWSP, TUDIEN, BANG_RE, CHUAN_V, TAG_CHUAN,    # noqa: E402,F401
                      bare, khoa_note, doc_hangdoi, ghi_hangdoi,
                      nap_lo_da_soan, gan_bang, khoi_nguphap, tag_chuan)
from soatlo import (TRAN_CAO, TRAN_WARN, cmd_soat, cmd_dodai,              # noqa: E402,F401
                    do_va_cham, tach_nghia, uoc_cao)

_BANG_RE = BANG_RE          # dochuan.py đang dùng congcu._BANG_RE — giữ tên cũ sống

ANKI = "http://127.0.0.1:8765"


def ac(action, **params):
    import urllib.request
    req = urllib.request.Request(
        ANKI, json.dumps({"action": action, "version": 6, "params": params}).encode())
    out = json.load(urllib.request.urlopen(req, timeout=300))
    if out.get("error"):
        raise RuntimeError(f"{action}: {out['error']}")
    return out["result"]


def cmd_bang():
    """Nối bảng chia vào MỌI thẻ RU_Word (không chỉ thẻ đã soạn hướng dẫn).

    User chốt 29/07: *"toàn bộ từ sẽ có bảng toàn bộ cách chia... cái này để
    tiện tra cứu về sau"*. Nên đây là lệnh chạy trên cả bộ sưu tập, khác `nap`
    (chỉ đụng lô đã duyệt).
    """
    apply = "--apply" in sys.argv
    notes = ac("notesInfo", notes=ac("findNotes", query="note:RU_Word"))
    doi, giu, khong = [], 0, []
    for n in notes:
        f = n["fields"]
        wc = (f.get("WordClean", {}).get("value") or "").strip()
        cu = f.get("HuongDan", {}).get("value", "")
        moi = gan_bang(cu, wc)
        if moi == cu:
            giu += 1
            if 'class="gt-bang"' not in moi:
                khong.append(wc)
            continue
        doi.append((n["noteId"], wc, len(moi) - len(cu)))
    print(f"{len(notes)} the | se doi {len(doi)} | giu nguyen {giu}")
    print(f"  trong so giu nguyen, {len(khong)} the KHONG CO BANG (khong bien cach "
          f"hoac tu dien khong co du lieu)")
    if khong:
        print("  " + " ".join(khong[:25]) + (" ..." if len(khong) > 25 else ""))
    if not apply:
        print("(CHAY KHAN — them --apply de ghi that)")
        return
    for nid, _, _ in doi:
        # đọc lại field ngay trước khi ghi thì thừa: `notesInfo` ở trên đã là ảnh
        # chụp mới nhất, và không có ai khác ghi vào giữa chừng.
        f = next(x for x in notes if x["noteId"] == nid)["fields"]
        ac("updateNoteFields", note={"id": nid, "fields": {
            "HuongDan": gan_bang(f.get("HuongDan", {}).get("value", ""),
                                 f["WordClean"]["value"].strip())}})
    print(f"da ghi {len(doi)} note")


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
        out += khoi_nguphap(wc)
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


# ---------------------------------------------------------- lệnh: trangthai
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
    # Tự nhắc: từ mới thêm vào Anki KHÔNG tự vào hàng đợi, và `nap` bỏ qua
    # chúng vĩnh viễn cho tới khi được nối. Không nhắc thì chúng nằm im.
    try:
        da_co = {khoa_note(t) for l in q["lo"] for t in l["tu"]}
        moi = [w for w in (n["fields"].get("WordClean", {}).get("value", "").strip()
                           for n in ac("notesInfo",
                                       notes=ac("findNotes", query="note:RU_Word")))
               if w and khoa_note(w) not in da_co]
        if moi:
            print(f"\n🆕 {len(moi)} TU MOI chua vao hang doi "
                  f"-> chay: congcu.py moi --apply")
    except Exception:
        pass          # không có Anki thì thôi, `trangthai` vẫn phải chạy được


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


# ---------------------------------------------------------- lệnh: tu moi
def cmd_moi():
    """Hứng TỪ MỚI user vừa thêm vào Anki, đưa lên ĐẦU hàng đợi.

    Trước đây đây là việc làm tay và phải chạm ĐÚNG HAI file, quên một cái
    thì `tiep` in ra `?` ở mọi cột và agent soạn mò. User phải giải thích
    lại từ đầu mỗi lần thêm từ ⇒ gói thành một lệnh chạy hằng ngày.

    Gộp dồn thay vì đẻ lô mới mỗi ngày: nếu đã có một lô từ mới CHƯA chạy
    thì nối tiếp vào đó. Lô 4 từ tốn gần bằng lô 15 từ (phần cố định áp
    đảo), nên ba ngày mỗi ngày 4 từ mà chạy riêng là trả giá gấp ba.
    """
    apply = "--apply" in sys.argv
    q = doc_hangdoi()
    da_co = {khoa_note(t) for l in q["lo"] for t in l["tu"]}

    notes = ac("notesInfo", notes=ac("findNotes", query="note:RU_Word"))
    moi = {}
    for n in notes:
        f = n["fields"]
        wc = f.get("WordClean", {}).get("value", "").strip()
        if not wc or khoa_note(wc) in da_co:
            continue
        tags = [t.replace("topic::", "") for t in n.get("tags", []) if t.startswith("topic::")]
        moi[wc] = {"wc": wc, "w": f.get("Word", {}).get("value", "").strip(),
                   "en": f.get("Meaning", {}).get("value", ""),
                   "vi": f.get("Vietnamese", {}).get("value", ""),
                   "pos": f.get("PoS", {}).get("value", ""),
                   "topic": tags[0] if tags else "other", "cu": False}

    if not moi:
        print(f"khong co tu moi ({len(notes)} the, tat ca da nam trong hang doi)")
        return
    print(f"TU MOI: {len(moi)} tu chua co trong hang doi")
    for w in sorted(moi):
        print(f"  {moi[w]['w'] or w:20s} {moi[w]['pos']:6s} {moi[w]['topic']:20s} {moi[w]['vi'][:44]}")

    # lô từ mới CHƯA chạy -> nối vào; không có thì mở lô mới với id trống đầu tiên
    dich = next((l for l in q["lo"] if l.get("tuMoi") and l["trangthai"] == "cho"), None)
    if dich:
        print(f"\n-> NOI vao lo {dich['id']} dang cho ({len(dich['tu'])} -> "
              f"{len(dich['tu']) + len(moi)} tu)")
    else:
        dung = {l["id"] for l in q["lo"]}
        sid = next(f"k{n:02d}" for n in range(1, 100) if f"k{n:02d}" not in dung)
        print(f"\n-> MO lo moi {sid}, dat o DAU hang doi")

    n_sau = (len(dich["tu"]) if dich else 0) + len(moi)
    if n_sau < 10:
        print(f"   ⚠️ moi {n_sau} tu. Lo duoi 10 tu dat gap ~3 lan tren moi tu "
              f"(phan co dinh 53K/lo ap dao). Nen doi gom them roi hay chay.")
    if n_sau > 22:
        print(f"   ⚠️ {n_sau} tu, qua tran 22 — chia lam hai lo truoc khi chay.")

    if not apply:
        print("\n(CHAY KHAN — them --apply de ghi)")
        return

    td = json.load(io.open(TUDIEN, encoding="utf-8"))
    co = {x["wc"] for x in td}
    td.extend(v for k, v in sorted(moi.items()) if v["wc"] not in co)
    io.open(TUDIEN, "w", encoding="utf-8").write(json.dumps(td, ensure_ascii=False, indent=1))

    if dich:
        dich["tu"] += sorted(moi)
    else:
        q["lo"].insert(0, {
            "id": sid, "topic": "tu-moi", "tu": sorted(moi), "trangthai": "cho",
            "file": None, "tuMoi": True,
            "thucong": "TU MOI user vua them. Cac tu co the KHONG cung ho nhau — "
                       "soan tung the doc lap, dung ep mot truc chung va dung dung "
                       "khoi he thong. Chuan: README muc 2 (1 man hinh iPhone, toi da "
                       "2 o do) + muc 2c (sua field Vietnamese cho chi co 1 dap an dung)."})
    q["tong_tu"] = sum(len(l["tu"]) for l in q["lo"])
    q["tong_lo"] = len(q["lo"])
    ghi_hangdoi(q)
    print(f"DA GHI ca hai file | hang doi: {q['tong_lo']} lo / {q['tong_tu']} tu")


# --------------------------------------------------------------- lệnh: nap
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

    # Cửa dữ liệu ngữ pháp — bảng chia được nối vào lúc GHI (`gan_bang` ở dưới),
    # nên đây là chỗ CUỐI CÙNG chặn được dữ liệu nguồn tự mâu thuẫn trước khi nó
    # ra mặt thẻ user đang học. `soat`/`dodai` không thay được: chúng chỉ đo phần
    # agent viết, còn bảng thì máy nối vào sau lưng chúng (SONO.md 02/08).
    soat_nguphap.keu_neu_dao({w: grammar.get_cached(w) for w in gop}, "lo sap nap")

    # 🔴 SYNC TRƯỚC KHI ĐỌC, không chỉ trước khi ghi (QD-16): ảnh chụp `hien_co`
    # / `vi_co` lấy ngay dưới đây là thứ quyết định "ghi hay bỏ qua", nên chụp
    # trên bản cũ là vừa so sai vừa ghi đè mất thay đổi của bot trên VPS. Lô hay
    # đụng đúng thẻ user đang học: `moi` hứng từ user vừa thêm, mà thẻ mới thì
    # nằm ở `0-quen` — chính deck bot thăng cấp lúc 03:00 mỗi đêm.
    if apply and not sync_truoc_khi_ghi_lo("nap lo"):
        return
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
    can_tag = []          # note vừa nhận nội dung của lô -> gắn dấu đạt chuẩn
    for word, html in gop.items():
        nids = ban_do.get(khoa_note(word), [])
        if not nids:
            miss.append(word)
            continue
        if len(nids) > 1:
            doi += 1
        can_tag += nids
        # Bảng chia nối vào ĐÂY chứ không nằm trong file lô: dạng từ đi thẳng từ
        # từ điển vào HTML, không qua model lần nào. Agent chỉ lo câu chú ý ở trên.
        html = gan_bang(html, word)
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

    # DẤU ĐẠT CHUẨN. Gỡ mọi `chuan::*` cũ trước rồi mới gắn số hiện hành — nếu chỉ
    # thêm thì một thẻ soạn lại sẽ đeo cả `chuan::2` lẫn `chuan::3` và câu hỏi
    # "thẻ này đạt chuẩn nào" lại không có đáp án duy nhất, tức quay về đúng chỗ
    # lộn xộn mà cái dấu này sinh ra để dẹp.
    if can_tag:
        for v in range(1, CHUAN_V + 1):
            ac("removeTags", notes=can_tag, tags=tag_chuan(v))
        ac("addTags", notes=can_tag, tags=tag_chuan())
        print(f"gan dau {tag_chuan()} cho {len(set(can_tag))} note")
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
     "vacham": cmd_vacham, "moi": cmd_moi, "bang": cmd_bang}[cmd]()
