# ==============================================================================
# ✅ ĐÃ CHẠY 27/08/2026 (`--sua --apply`): thẻ `нареза́ть` đã nhận lại bản ghi
#    của chính nó. Giữ ở đây làm biên bản, KHÔNG chạy lại.
# --- SCRIPT MỘT LẦN (L2 — chuyển `_daxong/` ngay trong commit này) ---
# Hai việc dọn tồn kho đi kèm QD-39/QD-40:
#   `--sua`     sửa thẻ `нареза́ть` đang mang bản ghi của `наре́зать` (ghi theo
#               NOTE ID, backup ô cũ ra `backups/` trước)
#   `--lietke`  in các động từ đang thiếu bạn thể, kèm nghĩa, để user gạt tay
#   `--them`    thêm các từ user đã duyệt (đi qua pipeline như mọi từ khác)
# Vì sao script chứ không phải lệnh bot: việc dọn chạy MỘT lần, mà từ nay
# `flow_add` hỏi ngay lúc thêm từ nên chỗ hổng không tích lại nữa (user chốt).
# ==============================================================================
import json
import os
import sys
import time

from anki_tools import grammar
from anki_tools.anki_client import _ac
from anki_tools.anki_the import nhom_dong_tu
from anki_tools.chu_nga import nfc as _nfc
from anki_tools.chu_nga import bare
from anki_tools.config import MODEL_NAME

GOC = os.path.dirname(os.path.abspath(__file__))


def _the():
    return _ac("notesInfo", timeout=120,
               notes=_ac("findNotes", query=f'note:"{MODEL_NAME}"'))


def sua_narezat():
    """Thẻ `нареза́ть` (chưa hoàn thành) đang mang bản ghi của `наре́зать`.

    Nguyên nhân: `ghi_grammar_json` cũ tìm thẻ theo `WordClean` đã bỏ dấu nhấn
    -> hai từ này ra chung một truy vấn -> ghi đè lẫn nhau (QD-40, đã bịt).
    """
    notes = [n for n in _the()
             if (n["fields"]["WordClean"]["value"] or "").strip() == "нарезать"]
    print(f"tim thay {len(notes)} the 'нарезать'")
    if len(notes) != 2:
        print("KHONG dung 2 the -> dung lai, xem bang mat")
        return
    tep = os.path.join(GOC, "backups", "_backup_narezat.json")
    os.makedirs(os.path.dirname(tep), exist_ok=True)
    with open(tep, "w", encoding="utf-8") as f:
        json.dump([{"noteId": n["noteId"], "fields":
                    {k: v["value"] for k, v in n["fields"].items()}} for n in notes],
                  f, ensure_ascii=False, indent=1)
    print(f"backup -> {tep}")

    trang = grammar.fetch_page("нарезать")
    muc = {(_ac_asp(m)): m for m in grammar.cac_muc_dong_tu(trang, "нарезать")}
    print("  tren tu dien:", {k: m.get("accented") for k, m in muc.items()})
    for n in notes:
        word = _nfc(n["fields"]["Word"]["value"])
        rec_cu = json.loads(n["fields"]["GrammarJSON"]["value"] or "{}")
        if _nfc(rec_cu.get("acc")) == word:
            print(f"  {word}: da dung, bo qua")
            continue
        dung = next((m for m in muc.values()
                     if _nfc(grammar.acc(m.get("accented") or "")) == word), None)
        if not dung:
            print(f"  🔴 {word}: khong tim thay muc khop tren tu dien -> BO QUA")
            continue
        rec = grammar.bo_sung(grammar.normalize(dung), bare(word))
        if "--apply" not in sys.argv:
            print(f"  (khan) {word}: se ghi lai acc={rec.get('acc')} the={rec.get('aspect')}")
            continue
        grammar.remember(bare(word), rec, note_id=n["noteId"])
        print(f"  ✅ {word}: ghi acc={rec.get('acc')} the={rec.get('aspect')} "
              f"vao note {n['noteId']}")


def _ac_asp(m):
    return f"{m.get('accented')}|{(m.get('verb') or {}).get('aspect')}"


def lietke():
    """Động từ đã có thẻ mà bạn thể phổ biến nhất (`partners[0]`) chưa có thẻ."""
    notes = _the()
    nhom = nhom_dong_tu(notes)
    co = {a for a in nhom}
    ra = []
    for n in notes:
        try:
            rec = json.loads((n["fields"]["GrammarJSON"]["value"] or "").strip() or "{}")
        except ValueError:
            continue
        if rec.get("pos") != "verb":
            continue
        ban = next((_nfc(p) for p in (rec.get("partners") or []) if p), "")
        if not ban or ban in co:
            continue
        the = _ac("cardsInfo", cards=_ac("findCards", query=f'nid:{n["noteId"]}'))
        ra.append((-sum(c.get("reps", 0) for c in the), _nfc(rec.get("acc")),
                   ban, rec.get("aspect"),
                   (n["fields"]["Vietnamese"]["value"] or "")[:40]))
    ra.sort()
    print(f"{len(ra)} dong tu thieu ban the — xep theo SO LAN DA ON tu goc:\n")
    for i, (am_reps, goc, ban, asp, vi) in enumerate(ra, 1):
        print(f"{i:>3}. {goc:<18} -> {ban:<18} (da on {-am_reps:>3} lan)  {vi}")


if __name__ == "__main__":
    if "--sua" in sys.argv:
        sua_narezat()
    elif "--lietke" in sys.argv:
        lietke()
    else:
        print(__doc__ or "dung: --sua | --lietke  [--apply]")
