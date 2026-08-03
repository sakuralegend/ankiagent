# ==============================================================================
# --- CHỤP MỐC FSRS — chạy TRƯỚC và SAU mỗi lần bấm Optimize trong Anki ---
#   python scripts/do_fsrs.py            # chụp mốc mới + so với mốc liền trước
#   python scripts/do_fsrs.py --xem      # chỉ xem lại, KHÔNG ghi mốc mới
#
# 🔴 CHỈ ĐỌC. Không gọi lệnh ghi nào của AnkiConnect, không đụng thẻ.
# Mốc ghi nối vào `data/fsrs_moc.json` (một file, mỗi lần đo một mục — QD-12:
# cấm đẻ file `anki_baseline_<ngày>.json` mới).
#
# ⚠️ Anki đang mở thì khoá collection.anki2 → script CHÉP file ra thư mục tạm
# rồi đọc bản chép. Bản chép chỉ nhất quán khi file `-wal` rỗng (Anki vừa ghi
# xong); script kiểm điều đó và kêu nếu không.
# ==============================================================================
import collections
import datetime
import json
import os
import shutil
import sqlite3
import statistics
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from anki_tools.anki_client import get_deck_fsrs_config          # noqa: E402

sys.stdout.reconfigure(encoding="utf-8", errors="replace")   # console Windows là cp1252

REPO = Path(__file__).resolve().parent.parent
MOC_FILE = REPO / "data" / "fsrs_moc.json"
COL_GOC = Path(os.environ.get(
    "ANKI_COLLECTION",
    Path.home() / "AppData/Roaming/Anki2/User 1/collection.anki2"))
DECK_GOC = ["RUSSIAN", "GRAMMAR"]


def _mo_ban_chep():
    """Chép collection ra temp rồi mở BẢN CHÉP. Trả (connection, đường dẫn tạm).

    Chép cả `-wal`/`-shm`: Anki chạy WAL nên phần ghi mới nhất còn nằm trong
    `-wal`; chép thiếu là đọc phải dữ liệu cũ vài giờ mà không có dấu hiệu gì.
    Mở bản chép ở chế độ ghi (không `mode=ro`) để SQLite gộp `-wal` vào — bản
    chép là file rác trong temp, ghi vào nó không đụng gì tới Anki thật."""
    if not COL_GOC.exists():
        sys.exit(f"❌ Không thấy collection: {COL_GOC}\n"
                 f"   Đặt biến môi trường ANKI_COLLECTION nếu để chỗ khác.")
    tam = Path(tempfile.gettempdir()) / "do_fsrs_col.anki2"
    for hau_to in ("", "-wal", "-shm"):
        nguon = COL_GOC.with_name(COL_GOC.name + hau_to)
        dich = tam.with_name(tam.name + hau_to)
        dich.unlink(missing_ok=True)
        if nguon.exists():
            shutil.copy2(nguon, dich)
    return sqlite3.connect(tam), tam


def _tu_phan_vi(xs):
    xs = sorted(xs)
    return {"min": round(xs[0], 2), "p25": round(xs[len(xs) // 4], 2),
            "trung_vi": round(statistics.median(xs), 2),
            "p75": round(xs[3 * len(xs) // 4], 2), "max": round(xs[-1], 2),
            "trung_binh": round(statistics.mean(xs), 2)}


def _thong_ke_the(cards, decks, hom_nay, prefix):
    """D (độ khó 1–10) · S (độ bền, ngày) · chu kì · lịch đến hạn 14 ngày tới."""
    ds, ss, ivls, den_han = [], [], [], collections.Counter()
    n = 0
    for _cid, did, odid, typ, q, ivl, due, data in cards:
        if not decks.get(odid or did, "").startswith(prefix):
            continue
        n += 1
        if data:
            try:
                j = json.loads(data)
            except ValueError:
                j = {}
            if j.get("d") is not None:
                ds.append(j["d"])
            if j.get("s"):
                ss.append(j["s"])
        if typ == 2 and q == 2:                       # thẻ đang ôn thật sự
            ivls.append(ivl)
            if due - hom_nay <= 14:
                den_han[max(due - hom_nay, 0)] += 1
    if not n:
        return None
    # D trong file là thang 1..10; quy về % cho dễ đọc: (D-1)/9*100
    nhom = collections.Counter()
    for d in ds:
        p = (d - 1) / 9 * 100
        nhom["duoi_50" if p < 50 else "50_70" if p < 70 else
             "70_90" if p < 90 else "tren_90"] += 1
    return {"so_the": n, "so_the_dang_on": len(ivls),
            "D_thang_1_10": _tu_phan_vi(ds) if ds else None,
            "D_phan_nhom_pct": dict(nhom) if ds else None,
            "S_ngay": _tu_phan_vi(ss) if ss else None,
            "chu_ki_ngay": _tu_phan_vi(ivls) if ivls else None,
            "den_han_14_ngay_toi": {str(k): den_han[k] for k in sorted(den_han)}}


def _thong_ke_nut(cur, cid_ok, tu_ms=None):
    """Tỷ lệ 4 nút, tách theo loại lượt: ôn tập / học mới / học lại.
    `nho_duoc_pct` = 100 - %Again, tức retention THẬT (Anki gọi 'true retention')."""
    dem = collections.Counter()
    for rid, cid, ease, typ in cur.execute(
            "select id, cid, ease, type from revlog where ease > 0"):
        if cid in cid_ok and not (tu_ms and rid < tu_ms):
            dem[(typ, ease)] += 1
    ra = {}
    for ten, typ in [("on_tap", 1), ("hoc_moi", 0), ("hoc_lai", 2)]:
        tong = sum(v for (t, _e), v in dem.items() if t == typ)
        if not tong:
            continue
        nut = {n: dem[(typ, i)] for i, n in enumerate(["again", "hard", "good", "easy"], 1)}
        ra[ten] = {"tong": tong,
                   "pct_nut": {k: round(v / tong * 100, 1) for k, v in nut.items()},
                   "nho_duoc_pct": round((tong - nut["again"]) / tong * 100, 1)}
    return ra


def chup(ghi_chu=""):
    con, tam = _mo_ban_chep()
    cur = con.cursor()
    decks = {r[0]: r[1].replace("\x1f", "::") for r in cur.execute("select id, name from decks")}
    cards = cur.execute("select id, did, odid, type, queue, ivl, due, data from cards").fetchall()
    crt = cur.execute("select crt from col").fetchone()[0]
    hom_nay = int((datetime.datetime.now().timestamp() - crt) // 86400)

    try:
        cfg = get_deck_fsrs_config(DECK_GOC[0])
    except Exception as e:
        con.close()
        sys.exit(f"❌ Không đọc được preset qua AnkiConnect ({e}) — Anki phải đang mở.")

    snap = {"ngay": datetime.date.today().isoformat(), "ghi_chu": ghi_chu,
            "preset": cfg["name"], "fsrsParams6": cfg["fsrsParams6"],
            "desiredRetention": cfg["desiredRetention"],
            "ignoreRevlogsBeforeDate": cfg["ignoreRevlogsBeforeDate"],
            "tong_lan_on": cur.execute(
                "select count(*) from revlog where ease > 0").fetchone()[0]}
    for d in DECK_GOC:
        snap[d] = _thong_ke_the(cards, decks, hom_nay, d)
        cid_ok = {c[0] for c in cards if decks.get(c[2] or c[1], "").startswith(d)}
        snap[f"nut_bam_{d}"] = _thong_ke_nut(cur, cid_ok)
    con.close()
    for hau_to in ("", "-wal", "-shm"):
        tam.with_name(tam.name + hau_to).unlink(missing_ok=True)
    return snap


def in_so_sanh(cu, moi):
    """In cạnh nhau hai mốc — đây là thứ người đọc thật sự cần, không phải JSON."""
    print(f"\n=== {cu['ngay']}  →  {moi['ngay']} ===")
    print(f"desiredRetention: {cu.get('desiredRetention')} → {moi.get('desiredRetention')}"
          f"   | tổng lượt ôn: {cu.get('tong_lan_on')} → {moi.get('tong_lan_on')}")
    a, b = cu.get("fsrsParams6") or [], moi.get("fsrsParams6") or []
    if a and b and len(a) == len(b):
        print("\n21 tham số FSRS (w0..w20), ▲/▼ = đổi trên 10%:")
        for i, (x, y) in enumerate(zip(a, b)):
            dau = "  " if abs(y - x) <= abs(x) * 0.1 else ("▲" if y > x else "▼")
            print(f"  w{i:<2d} {x:>12.6f} → {y:>12.6f} {dau}")
    for d in DECK_GOC:
        ca, cb = cu.get(d), moi.get(d)
        if not (ca and cb):
            continue
        print(f"\n{d}: {ca['so_the']} → {cb['so_the']} thẻ")
        for khoa, ten in [("chu_ki_ngay", "chu kì (ngày)"), ("D_thang_1_10", "độ khó D"),
                          ("S_ngay", "độ bền S (ngày)")]:
            x, y = ca.get(khoa), cb.get(khoa)
            if x and y:
                print(f"  {ten:<16s} trung vị {x['trung_vi']:>6} → {y['trung_vi']:<6}"
                      f"  | trung bình {x['trung_binh']:>6} → {y['trung_binh']}")
        x, y = ca.get("D_phan_nhom_pct"), cb.get("D_phan_nhom_pct")
        if x and y:
            print(f"  thẻ D ≥ 90%      {x.get('tren_90')} → {y.get('tren_90')}")
        # Mốc 25/07 (viết tay, trước khi có script này) không có khối nút bấm.
        x = (cu.get(f"nut_bam_{d}") or {}).get("on_tap")
        y = (moi.get(f"nut_bam_{d}") or {}).get("on_tap")
        if x and y:
            print(f"  nhớ được (ôn tập) {x['nho_duoc_pct']}% → {y['nho_duoc_pct']}%"
                  f"  | Again {x['pct_nut']['again']}% → {y['pct_nut']['again']}%"
                  f"  | Hard {x['pct_nut']['hard']}% → {y['pct_nut']['hard']}%")


def main():
    goc = json.loads(MOC_FILE.read_text(encoding="utf-8")) if MOC_FILE.exists() else \
        {"ghi_chu_file": "Các MỐC đo FSRS — mỗi lần đo thêm MỘT mục vào 'moc', "
                         "KHÔNG đẻ file mới. Chụp bằng scripts/do_fsrs.py.", "moc": []}
    if "--xem" in sys.argv:
        if len(goc["moc"]) >= 2:
            in_so_sanh(goc["moc"][-2], goc["moc"][-1])
        else:
            print(json.dumps(goc["moc"], ensure_ascii=False, indent=1))
        return
    ghi_chu = " ".join(a for a in sys.argv[1:] if not a.startswith("--"))
    moi = chup(ghi_chu)
    if goc["moc"]:
        in_so_sanh(goc["moc"][-1], moi)
    goc["moc"].append(moi)
    MOC_FILE.write_text(json.dumps(goc, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\n✅ Đã ghi mốc {moi['ngay']} vào {MOC_FILE.relative_to(REPO)} "
          f"({len(goc['moc'])} mốc).")


if __name__ == "__main__":
    main()
