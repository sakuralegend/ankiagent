#!/usr/bin/env python3
"""Nhắc AI ba cửa THÊM CHỨC NĂNG — chạy trước MỖI tin nhắn của user.

VÌ SAO có file này: `CLAUDE.md` đã ghi luật ba cửa, nhưng `CLAUDE.md` chỉ nạp
MỘT lần lúc mở phiên. Phiên dài 3 tiếng thì luật ở đầu context mờ dần, đúng cơ
chế đã đẻ ra 10 wrapper AnkiConnect (CACHLAM.md §3.2): AI không cố tình phá
luật, nó chỉ không còn nhớ luật. Hook này bơm lại 5 dòng vào MỖI lượt nên luật
không mờ được.

VÌ SAO user không phải gõ gì: user tự nói *"sao còn bắt tôi phải nhớ lệnh"* —
đúng. Cơ chế nào cần user nhớ thì cơ chế đó đã hỏng từ trong thiết kế.

Giá phải trả: ~60 token mỗi lượt. Rẻ hơn một lần code sai hướng phải làm lại.
Tắt: xoá mục "hooks" trong `.claude/settings.json`. (QD-09)
"""
import sys

# Windows console hay là cp1258/cp437 -> in tiếng Việt có dấu sẽ nổ UnicodeEncodeError,
# mà hook nổ thì im lặng mất tác dụng. Ép UTF-8 ngay từ đầu.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, OSError):
    pass

print("""[LUAT REPO - tu dong nhac moi luot]
User KHONG phai lap trinh vien va tu nhan "khong gioi dien dat tinh nang".
Neu tin nhan vua roi la XIN THEM/SUA MOT CHUC NANG (khong phai hoi dap, khong
phai sua loi vat): CAM viet code ngay. Doc `.claude/commands/ycau.md` roi lam
dung theo do — do truoc (bang "DA DO ROI BAC" o QUYETDINH.md), roi HOI USER bang
AskUserQuestion trac nghiem toi khi ro du 4 nhom, roi ghi VIECDANGLAM.md, roi
`.claude/commands/kehoach.md` cho user duyet. User KHONG phai go lenh gi ca.
Xong viec + 3 cua nghiem thu XANH => TU `git commit` ngay, KHONG hoi (QD-10).""")
