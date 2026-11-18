# -*- coding: utf-8 -*-
"""ĐỢT "THÊM N TỪ" từ `data/sach_b2.json` — chạy lại GIỮA CHỪNG là tự làm tiếp.

    python data/huongdan/kho/xephangdoi.py                  # đang ở bước nào, bước kế là gì
    python data/huongdan/kho/xephangdoi.py chon 200         # khan: in 200 từ sẽ lấy
    python data/huongdan/kho/xephangdoi.py chon 200 --apply # xếp chủ đề + chia lô + GHI hangdoi.json
    python data/huongdan/kho/xephangdoi.py taothe [--apply] [--toi-da N]
                     [--chon=TU=ID] [--bo=TU]               # tạo thẻ, NGƯỢC thứ tự lô

Viết lại 18/11/2026 (user duyệt) trên nền bản cũ — bản cũ chạy một lần rồi chết,
còn ghi ĐÈ cả hàng đợi nếu ai chạy nhầm. Đợt A2 (16/10, `_daxong/_va_nap_a1a2.py`)
trả học phí ba chỗ mà file này chặn bằng THIẾT KẾ, không bằng trí nhớ:
① nạp trước chia sau ⇒ 20 thẻ đầu rải 7 lô, user học lẫn thẻ trống. Preset "thẻ vừa thêm
   lên trước" (thẻ mới nhất ra học trước), AnkiConnect KHÔNG đổi được vị trí (đo 16/10) ⇒ thứ tự chỉ đặt
   được LÚC NẠP. Nên `chon` CHỐT kế hoạch lô vào hangdoi.json TRƯỚC khi có thẻ nào
   (AI xếp chủ đề mỗi lần ra khác nhau — phiên chết rồi xếp lại là lệch thứ tự).
② từ lỗi bị BỎ QUA rồi nạp tiếp ⇒ nạp lại sau thì nó thành thẻ mới nhất, ra học lệch
   lô. Nên gặp lỗi đầu tiên là DỪNG; `--chon`/`--bo` chốt cách xử lý vào hàng đợi.
③ hết lượt Google ⇒ `process_word` vẫn tạo thẻ, chỉ thiếu nghĩa Việt (đã gặp: `лоб`);
   chạy lại thì "đã có thẻ" nên bị bỏ qua im lặng. Nên mỗi lần chạy, thẻ KHUYẾT của
   đợt được LÀM LẠI trước (`redo_note_id` giữ note ⇒ giữ vị trí).
Lô đợt mang cờ `chuaThe` tới khi đủ thẻ + bản ghi tudien.json; `congcu.py tiep` từ
chối lô còn cờ (thiếu tudien thì agent soạn mò trên cột `?`).
🔴 HẠN MỨC GOOGLE 500 lượt/NGÀY chung với bot: mỗi thẻ 1 lượt, `chon` 1 lượt/25 từ.
"""
import io
import json
import os
import re
import statistics
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
GOC = os.path.join(HERE, "..", "..", "..")
sys.path.insert(0, GOC)
sys.path.insert(0, HERE)
from khochung import (TUDIEN, khoa_note, bare, doc_hangdoi, ghi_hangdoi,   # noqa: E402
                      ghi_json, ban_ghi_tudien)

SACH = os.path.join(GOC, "data", "sach_b2.json")
CO, TRAN, SAN = 20, 22, 10          # cỡ nhắm / trần / sàn mỗi lô — lo.md §2


# ------------------------------------------------- phần THUẦN (test được, không Anki)
def khoa_co(w, da_co, co_yo):
    """Từ đã có thẻ? Sách hay in е thay ё ⇒ thử cả bản ё của thẻ (`co_yo`)."""
    return khoa_note(w) in da_co or bare(w) in co_yo


def chon_tu(ds, da_co, da_len_ke, n):
    """-> (n từ đầu CHƯA có thẻ & chưa lên kế hoạch, [từ 'khong-OR' bị gác]).
    KHÔNG cắt đôi cặp thể: từ thứ n còn bạn thể ngay sau thì kéo theo."""
    lay, gac, co_yo = [], [], {bare(x) for x in da_co if "ё" in x}
    for rec in ds:
        w, _muc, _hang, cap, ghichu = rec
        if khoa_co(w, da_co, co_yo) or khoa_note(w) in da_len_ke:
            continue
        if "khong-OR" in ghichu:
            gac.append(w)
            continue
        if len(lay) >= n and not (cap and lay and lay[-1][3] == cap):
            break
        lay.append(rec)
    return lay, gac


def chia_lo(tu, chu_de, thu_tu_cd):
    """tu: [rec sách], chu_de: {từ: slug}. -> list lô, mỗi lô list rec.
    Xếp theo (chủ đề, gốc cặp viết NGƯỢC) ⇒ hậu tố chung nằm liền nhau, cặp thể
    liền nhau; rồi cắt ~CO từ/lô, ưu tiên cắt ở ranh chủ đề, cấm cắt giữa cặp."""
    def k(r):
        return (thu_tu_cd.get(chu_de[r[0]], 999), chu_de[r[0]],
                bare(r[3] or r[0])[::-1], r[0])
    x = sorted(tu, key=k)
    so_lo = max(1, round(len(x) / CO))
    lo, dau = [], 0
    for i in range(1, so_lo):
        dich = round(len(x) * i / so_lo)
        hop = [p for p in range(max(dau + SAN, dich - 4), min(len(x) - SAN, dich + 4) + 1)
               if p - dau <= TRAN and not (x[p][3] and x[p][3] == x[p - 1][3])]
        if not hop:
            continue
        ranh = [p for p in hop if chu_de[x[p][0]] != chu_de[x[p - 1][0]]]
        cat = min(ranh or hop, key=lambda p: abs(p - dich))
        lo.append(x[dau:cat])
        dau = cat
    lo.append(x[dau:])
    return lo


def la_khuyet(fields):
    """Thẻ hụt AI: có thẻ nhưng thiếu nghĩa Việt hoặc ví dụ."""
    return not all((fields.get(f, {}).get("value") or "").strip()
                   for f in ("Vietnamese", "ExamplesHTML"))


def thu_tu_nap(lo_dot):
    """Lô CUỐI nạp trước, trong lô từ cuối nạp trước ⇒ từ đầu lô đầu là thẻ mới nhất
    ⇒ ra học đầu tiên (preset "thẻ vừa thêm lên trước"). -> [(lô, từ)]."""
    return [(l, w) for l in reversed(lo_dot) for w in reversed(l["tu"])]


# ------------------------------------------------------------ phần đụng Anki/AI
def doc_the():
    from anki_tools.anki_client import doc_notes_cua_model
    from anki_tools.config import MODEL_NAME
    the = {khoa_note(n["fields"]["WordClean"]["value"].strip()): n
           for n in doc_notes_cua_model(MODEL_NAME)
           if n["fields"].get("WordClean", {}).get("value", "").strip()}
    # Anki đang sync thì đọc ra RỖNG (đo 15/10) ⇒ tưởng chưa có thẻ nào, nạp trùng cả đợt.
    if not the:
        sys.exit("Không đọc được thẻ từ Anki (đang sync / chưa mở?) — DỪNG, thử lại sau.")
    return the


def tim_the(w, the):
    if khoa_note(w) in the:
        return the[khoa_note(w)]
    return next((n for k, n in the.items() if "ё" in k and bare(k) == bare(w)), None)


def lo_dot(q):
    return [l for l in q["lo"] if l.get("dot")]


def cmd_chon(n, apply):
    q = doc_hangdoi()
    dang = [l["id"] for l in lo_dot(q) if l.get("chuaThe")]
    if dang:
        sys.exit(f"Đợt trước còn lô CHƯA ĐỦ THẺ: {' '.join(dang)} — chạy `taothe` cho xong trước.")
    ds = json.load(io.open(SACH, encoding="utf-8"))["tu"]
    da_len_ke = {khoa_note(w) for l in q["lo"] for w in l["tu"] + l.get("bo", [])}
    lay, gac = chon_tu(ds, set(doc_the()), da_len_ke, n)
    print(f"{len(lay)} từ: {lay[0][0]} … {lay[-1][0]}" if lay else "HẾT sách — không còn từ.")
    if gac:
        print(f"⚠️ gác {len(gac)} từ OpenRussian không có trang (thêm tay qua bot): {' '.join(gac)}")
    if not lay or not apply:
        print("" if apply else "(CHẠY KHAN — thêm --apply để xếp chủ đề + ghi hàng đợi)")
        return
    sys.path.insert(0, os.path.join(GOC, "scripts"))
    from tag_topics import xep_bang_ai                   # cùng cửa AI với lệnh gắn tag
    from anki_tools.topics import TOPICS
    ket = xep_bang_ai([(r[0], r[0], "") for r in lay])
    if sum(v is None for v in ket.values()) > len(lay) // 2:
        sys.exit("AI không xếp được quá nửa (hết lượt Google?) — DỪNG, CHƯA GHI GÌ.")
    cd = {r[0]: ket.get(r[0]) or "khac" for r in lay}
    dau_cap = {}
    for r in lay:                    # cặp thể theo chủ đề của từ đứng trước trong cặp
        if r[3]:
            cd[r[0]] = dau_cap.setdefault(r[3], cd[r[0]])
    hang = {r[0]: r[2] for r in lay}
    cac_lo = sorted(chia_lo(lay, cd, {s: i for i, s in enumerate(TOPICS)}),
                    key=lambda g: statistics.median(hang[r[0]] for r in g))
    so = max(int(m) for l in q["lo"] for m in re.findall(r"\d+", l["id"]))
    for i, g in enumerate(cac_lo, so + 1):
        cds = [cd[r[0]] for r in g]
        q["lo"].append({"id": f"k{i}", "topic": max(set(cds), key=cds.count),
                        "tu": [r[0] for r in g], "trangthai": "cho", "file": None,
                        "dot": "b2", "chuaThe": True})
        print(f"  k{i}  {len(g):2d} từ  {q['lo'][-1]['topic']:22s} {' '.join(r[0] for r in g)}")
    q["tong_tu"], q["tong_lo"] = sum(len(l["tu"]) for l in q["lo"]), len(q["lo"])
    ghi_hangdoi(q)
    print(f"ĐÃ CHỐT {len(cac_lo)} lô vào hangdoi.json. Bước kế: `taothe --apply`.")


def cmd_taothe(apply, toi_da):
    from anki_tools.pipeline import process_word, redo_note_id
    q = doc_hangdoi()
    for a in sys.argv:                      # chốt cách xử lý từ lỗi VÀO hàng đợi
        if a.startswith("--chon="):
            w, nid = a[7:].split("=")
            next(l for l in lo_dot(q) if w in l["tu"]).setdefault("chonId", {})[w] = int(nid)
        if a.startswith("--bo="):
            l = next(l for l in lo_dot(q) if a[5:] in l["tu"])
            l["tu"].remove(a[5:])
            l.setdefault("bo", []).append(a[5:])
    ghi_hangdoi(q)
    dot = [l for l in lo_dot(q) if l.get("chuaThe")]
    if not dot:
        print("Không có lô nào thiếu thẻ.")
        return
    the = doc_the()
    viec = [(l, w, tim_the(w, the)) for l, w in thu_tu_nap(dot)]
    viec = [(l, w, n) for l, w, n in viec if n is None or la_khuyet(n["fields"])]
    print(f"{len(dot)} lô thiếu thẻ: {len(viec)} việc "
          f"({sum(n is not None for *_, n in viec)} thẻ KHUYẾT làm lại trước)")
    if not apply:
        print("(CHẠY KHAN — thêm --apply)")
        return
    from anki_tools.anki_client import sync_now, sync_truoc_khi_ghi_lo
    if viec and not sync_truoc_khi_ghi_lo("tạo thẻ đợt"):
        sys.exit(1)
    viec.sort(key=lambda v: v[2] is None)   # khuyết trước: nó đã nằm ĐÚNG vị trí

    def dung(loi):                          # đẩy phần đã tạo lên AnkiWeb rồi mới chết
        print("sync:", sync_now())
        sys.exit(loi)
    for i, (l, w, n) in enumerate(viec[:toi_da], 1):
        chon = l.get("chonId", {}).get(w)
        ok, info, err = (redo_note_id(n["noteId"], chon_id=chon) if n
                         else process_word(w, None, chon_id=chon))
        if ok and info.get("ai_degraded"):
            dung(f"[{i}] KHUYẾT {w} — AI hụt (hết lượt Google?). DỪNG; mai chạy lại là nó tự làm lại thẻ này.")
        if not ok:
            if info and info.get("nhieu_muc"):
                err = "ĐỒNG TỰ — chọn mục rồi chạy lại kèm --chon=" + w + "=ID:\n    " + \
                      "\n    ".join(f"id={m['id']} {m['pos']} {m['en']}" for m in info["nhieu_muc"])
            dung(f"[{i}] DỪNG ở {w} ({l['id']}): {err}\n  Bỏ từ này: --bo={w}")
        moi = khoa_note(info.get("clean_word") or w)
        if moi != khoa_note(w):     # thẻ ra khác chữ sách (ё, dạng ngắn) ⇒ ghi NGAY, kẻo lần sau tạo trùng
            l["tu"][l["tu"].index(w)] = moi
            ghi_hangdoi(q)
        print(f"[{i}/{len(viec)}] OK  {l['id']} {moi}", flush=True)
    print("sync:", sync_now())
    hoan_tat(q, doc_the())


def hoan_tat(q, the):
    """Lô nào đủ thẻ lành ⇒ chép bản ghi vào tudien.json, chữ lô theo WordClean thật, gỡ cờ."""
    td = json.load(io.open(TUDIEN, encoding="utf-8"))
    co = {x["wc"] for x in td}
    for l in [l for l in lo_dot(q) if l.get("chuaThe")]:
        nn = [tim_the(w, the) for w in l["tu"]]
        if any(n is None or la_khuyet(n["fields"]) for n in nn):
            continue
        l["tu"] = [n["fields"]["WordClean"]["value"].strip() for n in nn]
        td += [r for r in map(ban_ghi_tudien, nn) if r["wc"] not in co]
        del l["chuaThe"]
        print(f"  {l['id']}: đủ {len(nn)} thẻ — sẵn sàng giao agent")
    ghi_json(TUDIEN, td)
    ghi_hangdoi(q)


def cmd_trangthai():
    dot = lo_dot(doc_hangdoi())
    thieu = [l["id"] for l in dot if l.get("chuaThe")]
    cho = [l["id"] for l in dot if l["trangthai"] == "cho" and not l.get("chuaThe")]
    if thieu:
        print(f"BƯỚC KẾ: `taothe --apply` — lô chưa đủ thẻ: {' '.join(thieu)}")
    elif cho:
        print(f"BƯỚC KẾ: soạn lô theo lo.md §1 bước 3–8, lô ĐẦU trước: {' '.join(cho)}")
    else:
        print("Không có đợt dở. Thêm từ: `chon N` (khan) rồi `chon N --apply`.")


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["chon"]:
        cmd_chon(int(a[1]), "--apply" in a)
    elif a[:1] == ["taothe"]:
        cmd_taothe("--apply" in a, int(a[a.index("--toi-da") + 1]) if "--toi-da" in a else 10 ** 6)
    else:
        cmd_trangthai()
