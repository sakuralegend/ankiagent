# -*- coding: utf-8 -*-
"""ĐỢT "THÊM N TỪ" từ `data/sach_b2.json` — chạy lại GIỮA CHỪNG là tự làm tiếp.

    python data/huongdan/kho/xephangdoi.py                  # đang ở bước nào, bước kế là gì
    python data/huongdan/kho/xephangdoi.py chon 100         # khan: in 100 từ sẽ lấy
    python data/huongdan/kho/xephangdoi.py chon 100 --apply # Opus xếp chủ đề + chia lô + GHI hangdoi.json
    python data/huongdan/kho/xephangdoi.py taothe [--apply] [--toi-da N]
                     [--chon=TU=ID] [--bo=TU]               # Opus soạn câu, rồi tạo thẻ NGƯỢC thứ tự lô

🔴 KHÔNG GOOGLE (user chốt 18/11 cho mọi đợt sách B2): nghĩa Việt, câu ví dụ, chủ đề, từ
loại do Opus làm qua `ai_client.goi_claude_code`, GỘP CẢ LÔ một lượt. Câu Opus vẫn qua
đúng cổng máy của `vi_du` (trượt thì hỏi lại riêng từ đó, tối đa 3 vòng) và được lưu
`_opus_<lô>.json` TRƯỚC khi tạo thẻ ⇒ phiên chết không mất lượt nào đã trả. GIỮ
OpenRussian (bảng chia, trọng âm) + Yandex (tiếng) — không phải AI.

Viết lại 18/11/2026 (user duyệt) trên nền bản cũ — bản cũ chạy một lần rồi chết,
còn ghi ĐÈ cả hàng đợi nếu ai chạy nhầm. Đợt A2 (16/10, `_daxong/_va_nap_a1a2.py`)
trả học phí ba chỗ mà file này chặn bằng THIẾT KẾ, không bằng trí nhớ:
① nạp trước chia sau ⇒ 20 thẻ đầu rải 7 lô, user học lẫn thẻ trống. Preset "thẻ vừa thêm
   lên trước" (thẻ mới nhất ra học trước), AnkiConnect KHÔNG đổi được vị trí (đo 16/10) ⇒ thứ tự chỉ đặt
   được LÚC NẠP. Nên `chon` CHỐT kế hoạch lô vào hangdoi.json TRƯỚC khi có thẻ nào
   (AI xếp chủ đề mỗi lần ra khác nhau — phiên chết rồi xếp lại là lệch thứ tự).
② từ lỗi bị BỎ QUA rồi nạp tiếp ⇒ nạp lại sau thì nó thành thẻ mới nhất, ra học lệch
   lô. Nên gặp lỗi đầu tiên là DỪNG; `--chon`/`--bo` chốt cách xử lý vào hàng đợi.
③ hụt AI ⇒ `process_word` vẫn tạo thẻ, chỉ thiếu nghĩa Việt (đã gặp: `лоб`);
   chạy lại thì "đã có thẻ" nên bị bỏ qua im lặng. Nên mỗi lần chạy, thẻ KHUYẾT của
   đợt được LÀM LẠI trước (`redo_note_id` giữ note ⇒ giữ vị trí).
Lô đợt mang cờ `chuaThe` tới khi đủ thẻ + bản ghi tudien.json; `congcu.py tiep` từ
chối lô còn cờ (thiếu tudien thì agent soạn mò trên cột `?`).
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
    so_lo = max(1, round(len(x) / CO), -(-len(x) // (TRAN - 1)))   # chừa ≥1 chỗ/lô để né cặp thể
    lo, dau = [], 0
    for i in range(1, so_lo):
        dich, con = round(len(x) * i / so_lo), so_lo - i
        # cận tính cả phần CÒN LẠI: chỉ chặn lô đang cắt thì lô cuối phình quá trần
        # (đo 18/11: 101 từ ra lô cuối 23)
        hop = [p for p in range(max(dau + SAN, len(x) - TRAN * con),
                                min(dau + TRAN, len(x) - SAN * con) + 1)
               if not (x[p][3] and x[p][3] == x[p - 1][3])]
        if not hop:
            continue
        hop = [p for p in hop if abs(p - dich) <= 4] or hop
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
    from anki_tools.ai_client import call_claude_topic, goi_claude_code
    from anki_tools.topics import TOPICS
    ket = {}
    for _ in range(2):                      # một lượt Opus cho cả đợt; lượt 2 vá chỗ thiếu
        ket.update(call_claude_topic([(w, "") for w in [r[0] for r in lay] if not ket.get(w)],
                                     goi=goi_claude_code))
    hut = [w for w in ket if not ket[w]]
    if len(hut) > len(lay) // 10:
        sys.exit(f"Opus không xếp được {len(hut)} từ — DỪNG, CHƯA GHI GÌ.")
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
                        "dot": "b2", "chuaThe": True, "chuDe": {r[0]: cd[r[0]] for r in g}})
        print(f"  k{i}  {len(g):2d} từ  {q['lo'][-1]['topic']:22s} {' '.join(r[0] for r in g)}")
    q["tong_tu"], q["tong_lo"] = sum(len(l["tu"]) for l in q["lo"]), len(q["lo"])
    ghi_hangdoi(q)
    print(f"ĐÃ CHỐT {len(cac_lo)} lô vào hangdoi.json. Bước kế: `taothe --apply`.")


def duong_opus(lo):
    return os.path.join(HERE, f"_opus_{lo['id']}.json")


def soan_opus(lo, can):
    """Opus soạn nghĩa Việt + câu ví dụ cho các từ `can` của lô trong MỘT lượt, máy kiểm
    bằng cổng `vi_du`, lưu đĩa sau MỖI vòng (đã lưu thì không hỏi lại).
    -> (kết quả {từ: ai_san}, lỗi dừng hoặc None)."""
    from anki_tools.ai_client import call_claude_pos, goi_claude_code
    from anki_tools.pipeline import cao_mot_tu
    from anki_tools.utils import strip_accents_perfectly
    from anki_tools.vi_du import loi_dan, loi_dan_lo, sinh_vi_du
    p = duong_opus(lo)
    kq = json.load(io.open(p, encoding="utf-8")) if os.path.exists(p) else {}
    can =[w for w in can if w not in kq]
    for vong in range(3):
        if not can:
            break
        muc, loi = {}, []
        for w in can:      # dò HẾT lô rồi mới báo: dừng ở từ đầu thì mỗi từ đồng tự tốn một lần chạy
            data, dung = cao_mot_tu(w, lo.get("chonId", {}).get(w))
            if dung and dung.get("nhieu_muc"):
                loi.append(f"ĐỒNG TỰ {w} — chọn mục rồi chạy lại kèm --chon={w}=ID:\n      " + "\n      ".join(
                    f"id={m['id']} {m['pos']} {m['en']}" for m in dung["nhieu_muc"]))
            elif dung:
                loi.append(f"{w}: OpenRussian không có trang. Bỏ từ này: --bo={w}")
            if dung:
                continue
            tu, en, rec = strip_accents_perfectly(w), data.get("english_meanings") or [], data.get("grammar") or {}
            _ht, dan, o, _cap = loi_dan(tu, en, rec)
            muc[w] = (tu, en, rec, dan, len(o), data["part_of_speech"].strip())
        if loi:
            return kq, "\n    ".join(loi)
        print(f"   {lo['id']} vòng {vong + 1}: Opus soạn {len(muc)} từ...", flush=True)
        r = goi_claude_code(*loi_dan_lo([(w, m[3]) for w, m in muc.items()])) or {}
        tra = {x.get("tu"): x for x in r.get("ket_qua") or [] if isinstance(x, dict)}
        thieu_pos = [(m[0], (m[1] or [""])[0]) for m in muc.values() if not m[5]]
        pos = call_claude_pos(thieu_pos, goi=goi_claude_code) if thieu_pos else {}
        for w, (tu, en, rec, _dan, n, _pos) in muc.items():
            bo = {k: tra.get(w, {}).get(k) for k in ("vietnamese_meaning", "examples")}
            ra = sinh_vi_du(tu, en, rec, goi=lambda *_a, bo=bo: bo, so_luot=1)
            # câu trượt cổng ⇒ hỏi lại cả từ; vòng cuối nhận bản thiếu câu (ít câu còn hơn câu sai)
            if ra and (len(ra["simplified_examples"]) == n or vong == 2):
                kq[w] = {"vi_du": bo, "topic": lo.get("chuDe", {}).get(w), "pos": pos.get(tu)}
        ghi_json(p, kq)
        can = [w for w in can if w not in kq]
    return kq, (f"Opus không soạn qua cổng được: {' '.join(can)}. Bỏ: --bo=TU" if can else None)


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
    opus, ket = {}, []
    for l in dot:      # soạn HẾT trước thẻ đầu tiên: nạp lô CUỐI trước, mà lô nào cũng có thể kẹt
        opus[l["id"]], loi = soan_opus(l, [w for ll, w, _n in viec if ll is l])
        ket += [f"  {l['id']}: {loi}"] if loi else []   # lô kẹt thì lô khác vẫn soạn + lưu tiếp
    if ket:
        dung("DỪNG — chưa tạo thẻ mới nào:\n" + "\n".join(ket))
    for i, (l, w, n) in enumerate(viec[:toi_da], 1):
        chon, ai = l.get("chonId", {}).get(w), opus[l["id"]][w]
        ok, info, err = (redo_note_id(n["noteId"], chon_id=chon, ai_san=ai) if n
                         else process_word(w, None, chon_id=chon, ai_san=ai))
        if ok and info.get("ai_degraded"):
            kq = opus[l["id"]]
            del kq[w]                       # bản Opus này hỏng lúc dựng ⇒ lần sau soạn lại
            ghi_json(duong_opus(l), kq)
            dung(f"[{i}] KHUYẾT {w} — câu Opus hỏng lúc dựng thẻ. Chạy lại: nó soạn lại rồi làm lại thẻ.")
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
    # KHÔNG `sync_now()` trơn: sync xong Anki còn khoá collection ~2 s ⇒ đọc ngay là chết
    # "Collection lifecycle operation is active" (gặp 18/11). Hàm này sync rồi CHỜ mở khoá.
    sync_truoc_khi_ghi_lo("dọn cuối đợt")
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
