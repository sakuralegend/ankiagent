# -*- coding: utf-8 -*-
"""Điền lại TOÀN BỘ badge ngữ pháp cho thẻ đã có trong Anki.

    python backfill_badge.py                        # CHẠY KHAN — in ra, không ghi gì
    python backfill_badge.py --apply                # ghi thật, CẢ BỐN chiều
    python backfill_badge.py --chi-tuloai --apply   # ghi ĐÚNG chiều từ loại

Bốn field, bốn chiều ngữ pháp, không chiều nào chồng chiều nào:

  GenderBadge     danh từ   MASC ♂ · FEM ♀ · NEUT ⚧ · PL 👥
  AspectBadge     động từ   PERF · IMPF · BI-ASP
  ReflexiveBadge  động từ   REFL -ся
  PoS / PoSFull   MỌI thẻ   n · v · adj · adv · num · pron · prep · conj · part · pred · interj

🔴 CHIỀU THỨ TƯ (từ loại) LÀ CHIỀU DUY NHẤT PHẢI HỎI AI, và chỉ hỏi cho thẻ mà
nguồn bỏ trống. OpenRussian trả thẳng chữ "other" cho 93/1290 thẻ (đo 01/09/2026)
— trạng từ, giới từ, liên từ, trợ từ dồn chung một rọ, badge in ra `oth` tức là
mặt thẻ có một ô mà không dạy gì. Hỏi lại nguồn KHÔNG cứu được: 74/93 nó vẫn trả
"other", và nó trả SAI 2 từ (`тут`, `справа` -> nó bảo là DANH TỪ). Xem QD-41.

⚠️ Vì thế chạy khan CŨNG tốn lượt gọi AI, và `--apply` gọi lại lượt nữa (kết quả
có thể lệch vài từ hai-từ-loại so với bản vừa xem). Đây là cùng một nết với
`scripts/tag_topics.py` — giữ giống nhau để khỏi phải nhớ hai kiểu.

Thẻ tạo từ 29/07/2026 trở đi tự có đủ ba (scraper lấy `verb.aspect` +
`verb.isReflexive` lúc cào). Script này lo phần quá khứ: 950 thẻ có sẵn.

Nguồn là `data/grammar_cache.json` (đã cào sẵn cả bộ sưu tập). Từ nào chưa có
trong cache thì gọi mạng lấy về, nên chạy được cả với thẻ mới thêm sau này.

`быть` được CHỪA THẬT từ 01/09/2026 — bảng `grammar.THE_NGUON_SAI` thi hành,
không còn là lời dặn suông trong docstring này (xem QD-43). `использовать` cũng
mang `aspect=both` nhưng KHÔNG chừa: nó là động từ hai thể thật.

🔴 TRƯỚC KHI CHẠY: hai field mới phải tồn tại. Chạy `setup_anki_environment()`
một lần (nó tự thêm qua `modelFieldAdd`). Thêm field LÀ schema mod ⇒ Anki đòi
FULL SYNC một lần ⇒ gom hết thay đổi schema rồi Upload MỘT lần, và sau đó kiểm
`journalctl` trên VPS: VPS kẹt sync IM LẶNG, không báo Telegram.
"""
import json
import os
import re
import sys
import urllib.request

# Chay duoc tu bat cu dau: file nay khong con nam o goc repo nen phai tu tro
# duong dan goc vao sys.path truoc khi import anki_tools (G3, 31/07/2026).
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from anki_tools import grammar
from anki_tools.anki_client import sync_truoc_khi_ghi_lo
from anki_tools.ai_client import call_claude_pos
from anki_tools.config import ANKI_CONNECT_URL, MODEL_NAME
from anki_tools.topics import normalize_pos, pos_full as ten_pos_day_du

# 🔴 KHÔNG khai lại bảng nhãn ở đây. Nó từng có bản sao riêng trong file này và
# một bản trong `anki_client.build_card_fields()` — hai bản thì sớm muộn lệch
# nhau, mà lệch nghĩa là thẻ MỚI và thẻ CŨ hiện hai kiểu badge cho cùng một
# giống. Nguồn duy nhất nay là `grammar.NHAN_GIONG` / `grammar.gender_badge_html`.
GIONG = grammar.NHAN_GIONG


def ac(action, **params):
    req = urllib.request.Request(
        ANKI_CONNECT_URL,
        json.dumps({"action": action, "version": 6, "params": params}).encode())
    out = json.load(urllib.request.urlopen(req, timeout=120))
    if out.get("error"):
        raise RuntimeError(f"{action}: {out['error']}")
    return out["result"]


def chu(html):
    return re.sub(r"<[^>]+>", "", html or "").strip()


def _badge(lop):
    return f'<div class="badge {lop}">{GIONG[lop]}</div>' if lop else ""


def gender_badge_wc(wc, rec, badge_cu, suy_ra):
    """Badge giống, BỐN tầng theo thứ tự tin cậy giảm dần.

    Dùng chung `grammar.NHAN_GIONG` / `MA_GIONG` / `suy_giong` với luồng tạo thẻ
    mới — file này CHỈ thêm hai việc mà luồng kia không cần:
      · tầng 3 đọc lại NHÃN CŨ trên thẻ (thẻ mới tinh thì làm gì có nhãn cũ);
      · ghi bằng chứng vào `suy_ra` để in cho user soát.

      1. CHỈ DÙNG SỐ NHIỀU (`nouns.csv pl_only`) — đè lên tất cả, vì `де́ньги`
         không có số ít nên badge "FEM ♀" của từ điển là dạy sai;
      2. `gender` của từ điển;
      3. nhãn CŨ đang có trên thẻ — có danh từ OpenRussian không ghi giống nhưng
         thẻ đang hiện đúng (lúc tạo thẻ lấy được, hoặc user sửa tay). Dựng lại
         máy móc từ từ điển sẽ XOÁ MẤT badge đang đúng: đổi nhãn cho đẹp mà làm
         mất thông tin thì là lỗ, không phải lãi;
      4. SUY từ đuôi biến cách. Máy suy thay từ điển thì phải chìa ra căn cứ,
         không được im lặng.
    """
    if grammar.chi_so_nhieu(wc):
        return _badge("plural")
    lop = grammar.MA_GIONG.get((rec.get("gender") or "").strip().lower())
    if not lop:
        # So NHAN voi NHAN. Ban cu so nhan hien thi ("FEM ♀") voi 4 ky tu dau
        # cua KHOA ("femi") — hai thu chi trung nhau do tinh co o masculine/neuter,
        # nen FEM/PL/M-F truot het va tang 3 XOA MAT badge dung, trai nguoc voi
        # dieu docstring hua ngay tren.
        cu = chu(badge_cu)
        lop = next((k for k, nhan in GIONG.items() if nhan == cu), None)
    if lop:
        return _badge(lop)
    ma, ly_do = grammar.suy_giong(rec)
    lop = grammar.MA_GIONG.get(ma or "")
    if lop:
        suy_ra.append((wc, GIONG[lop], ly_do))
    return _badge(lop)


# Chiều nào được phép GHI. Mặc định cả bốn; `--chi-tuloai` bó lại còn ô từ loại.
#
# 🔴 VÌ SAO CẦN BÓ (bắt 01/09/2026, lúc vá 93 thẻ `oth`). Chạy khan hôm đó đòi đổi
# 93 ô từ loại — đúng việc — KÈM 2 ô thể KHÔNG ai nhờ:
#     быть      IMPF -> BI-ASP   (nguồn ghi aspect="both")
#     нарезать  IMPF -> PERF     (наре́зать/нареза́ть trùng tên khi bỏ dấu nhấn)
# Ca `быть` chính là ca docstring trên đã dặn CHỪA từ 12/08 — nhưng lời dặn nằm ở
# CHỮ, không có dòng code nào thi hành, nên `--apply` vẫn ghi đè nó. Ca `нарезать`
# là bẫy đồng tự của QD-40: một tên bỏ dấu, hai động từ khác thể.
# Cả hai phải cân từng ca, mà L4 cấm gộp việc đó vào việc đang làm.
CHIEU = {
    "tuloai": ("PoS", "PoSFull"),
    "badge": ("GenderBadge", "AspectBadge", "ReflexiveBadge"),
}


def main():
    apply = "--apply" in sys.argv
    chi = CHIEU["tuloai"] if "--chi-tuloai" in sys.argv else None

    co = ac("modelFieldNames", modelName=MODEL_NAME)
    thieu = [f for f in ("AspectBadge", "ReflexiveBadge") if f not in co]
    if thieu:
        print(f"❌ Model {MODEL_NAME} chưa có field: {', '.join(thieu)}")
        print("   Chạy setup_anki_environment() một lần để nó tự thêm, rồi chạy lại.")
        return

    notes = ac("notesInfo", notes=ac("findNotes", query=f'note:"{MODEL_NAME}"'))
    print(f"{len(notes)} thẻ {MODEL_NAME}")

    # --- CHIỀU 4 chạy TRƯỚC vòng lặp vì nó hỏi AI theo LÔ ---
    # Chỉ hỏi cho thẻ mà ô từ loại hiện KHÔNG đọc được ("oth"/"other"/rỗng/rác).
    # Thẻ đang ghi `noun`/`verb`... thì nguồn đã nói chắc, AI chỉ đoán -> không đụng.
    can_xep = [n for n in notes
               if not normalize_pos((n["fields"].get("PoS", {}).get("value") or ""))]
    xep_pos = {}
    if can_xep:
        print(f"🤖 {len(can_xep)} thẻ chưa có từ loại đọc được -> nhờ AI xếp "
              f"({(len(can_xep) + 24) // 25} lượt gọi)...")
        xep_pos = call_claude_pos([
            (n["fields"]["WordClean"]["value"].strip(),
             chu(n["fields"].get("Meaning", {}).get("value", ""))[:80])
            for n in can_xep])
        chua = [w for w, ma in xep_pos.items() if not ma]
        if chua:
            print(f"   ⚠️ {len(chua)} từ AI KHÔNG xếp được -> để TRỐNG, không ép "
                  f"'other': {' · '.join(chua[:20])}")

    doi, giu, ngo, goi_mang, suy_ra = [], 0, [], 0, []
    for n in notes:
        f = n["fields"]
        wc = (f.get("WordClean", {}).get("value") or "").strip()
        if not wc:
            continue
        # 🔴 ĐỌC GrammarJSON CỦA CHÍNH THẺ TRƯỚC, bộ đệm theo TÊN chỉ là phao
        # (QD-40 + QD-43). Bỏ dấu nhấn thì `нареза́ть` (đang thái, CHƯA hoàn thành)
        # và `наре́зать` (thái xong, HOÀN THÀNH) trùng tên nhau, nên bộ đệm tra
        # theo tên trả CÙNG một bản ghi cho hai thẻ khác thể — đo 01/09: nó trả
        # `perfective` cho cả hai, tức sắp dán nhãn SAI lên thẻ đang đúng.
        # GrammarJSON nằm trong chính note nên không thể lẫn sang từ khác.
        rec = {}
        try:
            rec = json.loads(f.get("GrammarJSON", {}).get("value") or "{}") or {}
        except (ValueError, TypeError):
            rec = {}
        if not rec:
            rec = grammar.get_cached(wc)
        if not rec:
            rec = grammar.fetch_grammar(wc, note_id=n["noteId"])
            goi_mang += 1
        pos_the = (f.get("PoS", {}).get("value") or "").strip().lower()
        la_dong_tu = rec.get("pos") == "verb" or pos_the in ("v", "verb")
        la_danh_tu = rec.get("pos") == "noun" or pos_the in ("n", "noun")

        moi = {
            "GenderBadge": (gender_badge_wc(wc, rec,
                                            f.get("GenderBadge", {}).get("value", ""), suy_ra)
                            if la_danh_tu else ""),
            "AspectBadge": (grammar.aspect_badge_html(rec.get("aspect"), wc)
                            if la_dong_tu else ""),
            "ReflexiveBadge": (grammar.reflexive_badge_html(grammar.is_reflexive(wc, rec))
                               if la_dong_tu else ""),
        }
        # Từ loại: giữ nguyên nếu ô hiện tại đọc được; không thì lấy bản AI vừa
        # xếp. AI cũng chịu -> để RỖNG. 🔴 KHÔNG ép về "other": rọ "phần còn lại"
        # làm thẻ TRÔNG NHƯ đã xếp xong nên không ai đi tìm lại (QD-38, QD-41).
        ma_pos = normalize_pos(f.get("PoS", {}).get("value") or "") or xep_pos.get(wc)
        moi["PoS"] = ma_pos or ""
        moi["PoSFull"] = ten_pos_day_du(ma_pos) or ""

        if la_dong_tu and not moi["AspectBadge"]:
            ngo.append(f"{wc}(thể)")
        if la_danh_tu and not moi["GenderBadge"]:
            ngo.append(f"{wc}(giống)")

        khac = {k: v for k, v in moi.items()
                if v != f.get(k, {}).get("value", "") and (chi is None or k in chi)}
        if not khac:
            giu += 1
            continue
        cu = {k: f.get(k, {}).get("value", "") for k in khac}
        doi.append((n["noteId"], wc, cu, khac))

    pham_vi = (" — CHỈ chiều " + "/".join(chi)) if chi else " — cả bốn chiều"
    print(f"\n=== SẼ ĐỔI {len(doi)} thẻ (giữ nguyên {giu}){pham_vi} ===")
    dem = {}
    for _, _, cu, khac in doi:
        for k, v in khac.items():
            key = f"{k:15s} {chu(cu[k]) or '(trống)':16s} -> {chu(v) or '(xoá)'}"
            dem[key] = dem.get(key, 0) + 1
    for mo_ta, sl in sorted(dem.items(), key=lambda x: (-x[1], x[0])):
        print(f"  {sl:4d}×  {mo_ta}")

    if suy_ra:
        print(f"\n🔎 {len(suy_ra)} thẻ TỪ ĐIỂN KHÔNG GHI GIỐNG — máy suy từ đuôi biến cách."
              f"\n   (đọc bằng chứng rồi hãy cho chạy --apply)")
        for wc, nhan, ly_do in suy_ra:
            print(f"   {wc:14s} -> {nhan:10s} {ly_do}")

    if ngo:
        print(f"\n⚠️ {len(ngo)} thẻ KHÔNG nguồn nào cho biết, cũng không suy được "
              f"-> badge để trống:")
        print("   " + " · ".join(ngo[:40]))
    if goi_mang:
        print(f"\n({goi_mang} từ chưa có trong cache, đã gọi mạng lấy về)")

    if not apply:
        print("\n(CHẠY KHAN — thêm --apply để ghi thật)")
        return
    if not sync_truoc_khi_ghi_lo("backfill badge"):
        return
    for nid, _, _, khac in doi:
        ac("updateNoteFields", note={"id": nid, "fields": khac})
    print(f"\n✅ Đã ghi {len(doi)} thẻ.")


if __name__ == "__main__":
    main()
