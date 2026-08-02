"""Vá MỘT ô rác trong `GrammarJSON` của thẻ `степь` (chạy 02/08/2026, một lần).

Cách 5 số ít đang là `сте́пью сте́ипю` — dạng thứ hai KHÔNG có thật, là rác
nguồn OpenRussian. Agent soạn lô k26 bắt được; luồng chính quét cả 976 thẻ để
biết đây là ca lẻ hay lỗi hệ thống: **217 ô có nhiều dạng, 216 ô ngăn bằng dấu
phẩy và đều là biến thể thật** (`-ой, -ою` cổ, `в лесу́` cách vị trí…), chỉ mình
ô này hỏng ⇒ ca lẻ, vá tay là đủ.

🔴 Đây đúng lớp lỗi "máy nối vào thẻ" mà `soat`/`dodai` MÙ — chúng chỉ đo phần
agent viết, trong khi `congcu.py bang` nối bảng chia vào mọi thẻ lúc ghi. Cùng
họ với ca `кеды` (QD-15) và `шофё́р`.

L2: script một lần, đã nằm sẵn ở `_daxong/`, chết trong cùng commit."""
import sys, json, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
sys.stdout.reconfigure(encoding="utf-8")

from anki_tools.anki_client import (
    doc_grammar_json_tat_ca, ghi_grammar_json, sync_truoc_khi_ghi_lo)

RAC = "сте́пью сте́ипю"
DUNG = "сте́пью"

sync_truoc_khi_ghi_lo("va rac GrammarJSON cua степь")   # QD-16

d = doc_grammar_json_tat_ca()
rec = d["степь"]
cu = rec["decl"]["sg"]["inst"]
print("TRUOC:", repr(cu))
if cu != RAC:
    print("DU LIEU KHONG NHU MONG DOI -> DUNG, khong ghi gi")
    raise SystemExit(1)

bk = pathlib.Path(__file__).resolve().parent.parent / "backups"
bk.mkdir(exist_ok=True)
(bk / "_backup_grammarjson_step.json").write_text(
    json.dumps({"степь": rec}, ensure_ascii=False, indent=1), encoding="utf-8")
print("da sao luu backups/_backup_grammarjson_step.json")

rec["decl"]["sg"]["inst"] = DUNG
print("ghi:", ghi_grammar_json("степь", rec))
print("SAU :", repr(doc_grammar_json_tat_ca()["степь"]["decl"]["sg"]["inst"]))
