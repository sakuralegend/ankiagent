"""Vá 7 dòng `vi` SAI trong `tudien.json` (chạy 02/08/2026, một lần).

Agent soạn k26/k27 bác 7 chỗ; luồng chính kiểm lại từng chỗ và thấy **gloss
tiếng Anh của nguồn vẫn ĐÚNG, chỉ dòng `vi` sai** — đúng vệt "nguồn dịch sai
tên loài" đã ghi ở `TIEPTUC.md` (`грач`, `зя́блик`, `о́кунь`).

Không vá thì lô sau soạn lại sẽ chép ra đúng lỗi cũ: `nap` ghi field
`Vietnamese` từ `V` của file lô, nhưng `congcu.py tiep` lấy đề bài từ
`tudien.json` — hai nơi khác nhau.

Bản sửa lấy NGUYÊN VĂN từ `V` của file lô để hai nơi khớp nhau.
L2: script một lần, đã nằm sẵn ở `_daxong/`, chết trong cùng commit."""
import sys, json, pathlib

sys.stdout.reconfigure(encoding="utf-8")
GOC = pathlib.Path(__file__).resolve().parent.parent
F = GOC / "data" / "huongdan" / "kho" / "tudien.json"

# wc -> (vi CŨ phải khớp y nguyên, vi MỚI)
SUA = {
    "липа":   ("cây bồ đề (linden tree) hoặc đồ giả/hàng nhái (slang)",
               "cây đoan (linden, lime tree — cây bóng mát, hoa pha trà)"),
    "озеро":  ("ao, hồ", "hồ (hồ nước)"),
    "степь":  ("đồng cỏ mênh mông", "thảo nguyên (đồng cỏ khô mênh mông)"),
    "сад":    ("vườn, công viên, mẫu giáo", "vườn cây, khu vườn"),
    "ёлка":   ("cây thông Noel", "cây vân sam nhỏ; cây thông Noel"),
    "гроза":  ("bão tố, sấm sét", "cơn giông có sấm sét"),
    "облако": ("đám mây, dịch vụ lưu trữ đám mây", "đám mây trắng trên trời"),
}

d = json.loads(F.read_text(encoding="utf-8"))
xong = 0
for r in d:
    wc = r.get("wc")
    if wc in SUA:
        cu, moi = SUA[wc]
        if r.get("vi") != cu:                    # dữ liệu đã đổi -> DỪNG, đừng đè bừa
            print(f"KHONG KHOP {wc}: dang la {r.get('vi')!r}")
            raise SystemExit(1)
        r["vi"] = moi
        xong += 1
        print(f"{wc}: {cu!r} -> {moi!r}")

assert xong == len(SUA), f"chi va duoc {xong}/{len(SUA)}"
F.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"da ghi {xong} muc vao tudien.json ({len(d)} tu)")
