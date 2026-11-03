# -*- coding: utf-8 -*-
"""LÀM SẠCH CÂU VÍ DỤ CỦA THẺ ĐANG CÓ — script chạy MỘT LẦN (L2), xong chuyển `_daxong/`.

Vì sao (QD-47, đo 03/11/2026): ~300/5 382 câu trên thẻ thật hỏng mà máy bắt được
(dùng cặp thể, từ giảm nhẹ, từ cùng gốc, mất chữ), cộng ước ~4% câu sai nghĩa/gượng
máy KHÔNG bắt được. Gemini Lite chỉ 500 lượt/ngày ⇒ chạy Sonnet qua Claude Code
trên laptop (`ai_client.goi_claude_code`, ăn hạn mức gói).

    python scripts/_va_lam_sach_vi_du.py quet [--gioi-han N]  # máy soát + Sonnet chấm — KHÔNG ghi Anki
    python scripts/_va_lam_sach_vi_du.py viet                 # Sonnet viết lại câu hỏng — KHÔNG ghi Anki
    python scripts/_va_lam_sach_vi_du.py baocao               # HTML trước/sau cho user duyệt
    python scripts/_va_lam_sach_vi_du.py ghi [--apply]        # khan: in số · --apply: sync + backup + ghi
    python scripts/_va_lam_sach_vi_du.py khoiphuc <file>      # trả ô ExamplesHTML về bản đã chụp

Ba bước đầu chạy lại bao nhiêu lần cũng được: tiến độ ở `backups/lam_sach_vi_du/`,
hết hạn mức giữa chừng thì chạy lại là đi tiếp. Câu TỐT giữ nguyên từng byte (cùng
tiếng đọc): chỉ khối hỏng bị thay (`html_builder.thay_vi_du`).
"""
import hashlib
import html
import json
import os
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor

# Chay duoc tu bat cu dau: file nay khong nam o goc repo (G3, 31/07/2026).
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from anki_tools import goi_anki
from anki_tools.ai_client import goi_claude_code
from anki_tools.anki_client import (doc_notes_cua_model, gan_tieng_vi_du, sync_truoc_khi_ghi_lo,
                                    trigger_sync)
from anki_tools.config import MODEL_NAME
from anki_tools.html_builder import parse_examples_html, parse_meaning_html, thay_vi_du
from anki_tools.utils import log_fail, log_warn
from anki_tools.vi_du import chon_dang, khoa_dang, kiem_cau_cu, sinh_vi_du, tat_ca_dang

GOC = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "backups", "lam_sach_vi_du")
TRANG_THAI = os.path.join(GOC, "trangthai.json")
SO_LUONG = 3        # 3 lượt `claude -p` song song: laptop chịu được, hạn mức gói không cháy một lúc
CO_LO_CHAM = 20     # 20 từ/lượt chấm: một lượt ~60 câu, đủ ngắn để Sonnet không trả thiếu
_khoa = threading.RLock()   # 3 luồng cùng sửa `tt` rồi ghi file: sửa + ghi phải cùng một khoá

CHAM_HE_THONG = (
    "You are a native Russian editor checking example sentences on a Vietnamese learner's flashcards. "
    "Each sentence illustrates the card's target word (marked <hl>). Flag a sentence ONLY if a native "
    "speaker would clearly correct it: grammar or case error, wrong preposition, unnatural or illogical "
    "meaning, the target word used in a sense unrelated to the card's meaning, or a Vietnamese translation "
    "that contradicts the Russian. Do NOT flag style preferences or sentences that are merely simple. "
    "Give each reason in short Vietnamese. Return JSON only.")
CHAM_KHUON = {"type": "object", "properties": {"loi": {"type": "array", "items": {
    "type": "object", "properties": {"id": {"type": "string"}, "cau": {"type": "integer"},
                                     "ly_do": {"type": "string"}},
    "required": ["id", "cau", "ly_do"]}}}, "required": ["loi"]}


def _doc_tt():
    if os.path.exists(TRANG_THAI):
        with open(TRANG_THAI, encoding="utf-8") as f:
            return json.load(f)
    return {}


def _ghi_tt(tt):
    os.makedirs(GOC, exist_ok=True)
    with _khoa:
        tam = TRANG_THAI + ".tam"
        with open(tam, "w", encoding="utf-8") as f:
            json.dump(tt, f, ensure_ascii=False, indent=0)
        os.replace(tam, TRANG_THAI)


def _bam(s):
    return hashlib.md5((s or "").encode("utf-8")).hexdigest()


def _the():
    """note id -> dữ liệu cần dùng. `doc_notes_cua_model` đã lọc note:"RU_Word"."""
    ra = {}
    for n in doc_notes_cua_model(MODEL_NAME):
        f = {k: v["value"] for k, v in n["fields"].items()}
        try:
            rec = json.loads(f.get("GrammarJSON") or "{}")
        except ValueError:
            rec = {}
        ra[str(n["noteId"])] = {"tu": f["WordClean"], "rec": rec, "html": f.get("ExamplesHTML", ""),
                                "nghia": parse_meaning_html(f.get("Meaning", "")), "viet": f.get("Vietnamese", ""),
                                "cau": parse_examples_html(f.get("ExamplesHTML", ""))}
    return ra


def quet(gioi_han=None):
    the, tt = _the(), _doc_tt()
    ids = sorted(the)[:gioi_han] if gioi_han else sorted(the)
    for nid in ids:                                  # 1) máy soát — rẻ, chạy lại mỗi lần
        t = the[nid]
        cu = tt.get(nid, {})
        if cu.get("bam") and cu["bam"] != _bam(t["html"]):
            cu = {}                                  # thẻ đã đổi từ lần quét trước -> chấm lại từ đầu
        dang = tat_ca_dang(t["rec"], t["tu"])
        loi = {str(i): ly for i, c in enumerate(t["cau"]) if (ly := kiem_cau_cu(c["ru"], dang))}
        loi.update({str(i): "thiếu câu" for i in range(len(t["cau"]), 3)})
        tt[nid] = {**cu, "tu": t["tu"], "bam": _bam(t["html"]), "loi_may": loi}
    _ghi_tt(tt)
    con = [nid for nid in ids if not tt[nid].get("da_cham")]
    print(f"Máy soát {len(ids)} thẻ: {sum(len(tt[n]['loi_may']) for n in ids)} câu hỏng. "
          f"Sonnet còn phải chấm {len(con)} thẻ ({(len(con) + CO_LO_CHAM - 1) // CO_LO_CHAM} lượt).")

    def cham(lo):                                    # 2) Sonnet chấm câu máy để lọt
        dong = []
        for nid in lo:
            t = the[nid]
            dong.append(f"[{nid}] {t['tu']} ({'; '.join(t['nghia'][:2])} / {t['viet']})")
            for i, c in enumerate(t["cau"]):
                if str(i) not in tt[nid]["loi_may"]:
                    dong.append(f"  {i + 1}. {c['ru']} | {c['vi']}")
        r = goi_claude_code(CHAM_HE_THONG, "\n".join(dong), CHAM_KHUON)
        if not isinstance(r, dict):
            log_warn(f"Lượt chấm hỏng ({lo[0]}…) — chạy lại `quet` sau")
            return
        with _khoa:
            for m in r.get("loi") or []:
                nid, i = str(m.get("id", "")).strip("[] "), m.get("cau")
                if nid in lo and isinstance(i, int) and 1 <= i <= 3:
                    tt[nid].setdefault("loi_sonnet", {})[str(i - 1)] = m.get("ly_do", "")
            for nid in lo:
                tt[nid]["da_cham"] = True
            _ghi_tt(tt)
        print(f"  chấm xong {len(lo)} thẻ ({time.strftime('%H:%M:%S')})")
    with ThreadPoolExecutor(SO_LUONG) as ex:
        list(ex.map(cham, [con[i:i + CO_LO_CHAM] for i in range(0, len(con), CO_LO_CHAM)]))
    _ghi_tt(tt)
    hong = sum(len(set(v.get("loi_may", {})) | set(v.get("loi_sonnet", {}))) for v in tt.values())
    print(f"Tổng câu cần viết lại: {hong} trên {sum(1 for v in tt.values() if v.get('loi_may') or v.get('loi_sonnet'))} thẻ.")


def _can_viet(v):
    return sorted({int(i) for i in list(v.get("loi_may", {})) + list(v.get("loi_sonnet", {}))} - {int(i) for i in v.get("moi", {})})


def viet():
    the, tt = _the(), _doc_tt()
    viec = [nid for nid, v in tt.items() if _can_viet(v) and nid in the]
    print(f"Sonnet viết lại câu cho {len(viec)} thẻ…")

    def mot(nid):
        t, v = the[nid], tt[nid]
        hong = _can_viet(v)
        _l, o_tat_ca = chon_dang(t["rec"], t["tu"])
        da_dung = {khoa_dang(c["ru"].split("<hl>")[1].split("</hl>")[0]) for i, c in enumerate(t["cau"])
                   if i not in hong and "<hl>" in c["ru"]}
        trong = [x for x in o_tat_ca if khoa_dang(x[0]) not in da_dung]
        o = [trong.pop(0) if trong else o_tat_ca[i % 3] for i in hong]
        r = sinh_vi_du(t["tu"], t["nghia"], t["rec"], goi=goi_claude_code, o=o)
        if not r:
            log_warn(f"{t['tu']}: chưa viết được câu nào qua cổng — chạy lại `viet` sau")
            return
        with _khoa:
            for k, ex in zip(r["chi_so"], r["simplified_examples"]):
                v.setdefault("moi", {})[str(hong[k])] = ex
            _ghi_tt(tt)
        print(f"  {t['tu']}: {len(r['chi_so'])}/{len(hong)} câu ({time.strftime('%H:%M:%S')})")
    with ThreadPoolExecutor(SO_LUONG) as ex:
        list(ex.map(mot, viec))
    _ghi_tt(tt)
    con = sum(len(_can_viet(v)) for v in tt.values())
    print(f"Còn {con} câu chưa có bản viết lại qua cổng.")


def baocao():
    the, tt = _the(), _doc_tt()
    hang = []
    for nid, v in sorted(tt.items(), key=lambda x: x[1].get("tu", "")):
        if not v.get("moi") or nid not in the:
            continue
        t = the[nid]
        for i in sorted(v["moi"], key=int):
            cu = t["cau"][int(i)] if int(i) < len(t["cau"]) else {"ru": "", "vi": ""}
            ly = v.get("loi_may", {}).get(i) or v.get("loi_sonnet", {}).get(i, "")
            moi = v["moi"][i]
            hang.append(f"<tr><td><b>{html.escape(t['tu'])}</b></td><td class=c>{html.escape(cu['ru'])}<br><i>{html.escape(cu['vi'])}</i>"
                        f"<div class=l>{html.escape(ly)}</div></td><td class=m>{html.escape(moi['ru'])}<br><i>{html.escape(moi['vi'])}</i></td></tr>")
    trang = ("<!DOCTYPE html><html lang=vi><head><meta charset=utf-8><meta name=viewport content='width=device-width, initial-scale=1'>"
             "<title>Làm sạch câu ví dụ — trước/sau</title><style>body{font-family:sans-serif;margin:16px}table{border-collapse:collapse;width:100%}"
             "td{border-bottom:1px solid #ddd;padding:6px;vertical-align:top}.c{color:#a33}.m{color:#174}.l{font-size:12px;color:#777}</style></head><body>"
             f"<h1>Làm sạch câu ví dụ — {len(hang)} câu thay mới</h1><p>Cột giữa: câu đang có + lý do bị loại. Cột phải: câu mới (đã qua cổng máy).</p>"
             "<table><tr><th>Từ</th><th>Câu cũ</th><th>Câu mới</th></tr>" + "".join(hang) + "</table></body></html>")
    duong = os.path.join(GOC, "baocao.html")
    with open(duong, "w", encoding="utf-8") as f:
        f.write(trang)
    print(f"{len(hang)} câu → {duong}")


def ghi(apply):
    the, tt = _the(), _doc_tt()
    viec = {nid: v for nid, v in tt.items() if v.get("moi") and not v.get("da_ghi") and nid in the}
    lech = [nid for nid in viec if _bam(the[nid]["html"]) != viec[nid]["bam"]]
    print(f"Sẽ thay {sum(len(v['moi']) for v in viec.values())} câu trên {len(viec)} thẻ; "
          f"{len(lech)} thẻ đã đổi sau lần quét (BỎ QUA, quét lại đã).")
    if not apply:
        print("Chạy KHAN — chưa ghi gì. Thêm --apply để ghi thật.")
        return
    if not sync_truoc_khi_ghi_lo("làm sạch câu ví dụ"):
        log_fail("Không kéo được AnkiWeb về — DỪNG, chưa ghi gì.")
        return
    the = _the()                                   # đọc lại SAU khi kéo sync
    viec = {nid: v for nid, v in viec.items() if _bam(the[nid]["html"]) == v["bam"]}
    os.makedirs(GOC, exist_ok=True)
    chup = os.path.join(GOC, f"truoc_khi_ghi_{time.strftime('%Y-%m-%d_%H%M')}.json")
    with open(chup, "w", encoding="utf-8") as f:
        json.dump({nid: the[nid]["html"] for nid in viec}, f, ensure_ascii=False)
    print(f"Đã chụp ô cũ của {len(viec)} thẻ → {chup}")
    for k, (nid, v) in enumerate(viec.items(), 1):
        moi_html = the[nid]["html"]
        for i in sorted(v["moi"], key=int):
            moi_html = thay_vi_du(moi_html, int(i), v["moi"][i], gan_tieng=gan_tieng_vi_du)
        goi_anki("updateNoteFields", note={"id": int(nid), "fields": {"ExamplesHTML": moi_html}})
        v["da_ghi"] = True
        if k % 50 == 0:
            _ghi_tt(tt)
            print(f"  {k}/{len(viec)}")
    _ghi_tt(tt)
    print("Đẩy lên AnkiWeb:", "OK" if trigger_sync() else "HỎNG — xem log, chạy lại sync")


def khoiphuc(duong):
    with open(duong, encoding="utf-8") as f:
        cu = json.load(f)
    if not sync_truoc_khi_ghi_lo("khôi phục câu ví dụ"):
        log_fail("Không kéo được AnkiWeb về — DỪNG.")
        return
    for nid, h in cu.items():
        goi_anki("updateNoteFields", note={"id": int(nid), "fields": {"ExamplesHTML": h}})
    print(f"Đã trả {len(cu)} thẻ về bản chụp. Đẩy lên AnkiWeb:", "OK" if trigger_sync() else "HỎNG")


if __name__ == "__main__":
    a = sys.argv[1:]
    lenh = a[0] if a else ""
    if lenh == "quet":
        quet(int(a[a.index("--gioi-han") + 1]) if "--gioi-han" in a else None)
    elif lenh == "viet":
        viet()
    elif lenh == "baocao":
        baocao()
    elif lenh == "ghi":
        ghi("--apply" in a)
    elif lenh == "khoiphuc" and len(a) > 1:
        khoiphuc(a[1])
    else:
        print(__doc__)
