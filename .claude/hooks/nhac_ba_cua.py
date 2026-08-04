#!/usr/bin/env python3
"""Bơm lại LUẬT SỐ 1 của repo vào MỖI tin nhắn của user.

VÌ SAO có file này: `CLAUDE.md` đã ghi các luật, nhưng `CLAUDE.md` chỉ nạp MỘT
lần lúc mở phiên. Phiên dài 3 tiếng thì luật ở đầu context mờ dần, đúng cơ chế
đã đẻ ra 10 wrapper AnkiConnect (CACHLAM.md §3.2): AI không cố tình phá luật,
nó chỉ không còn nhớ luật. Hook này bơm lại nên luật không mờ được.

VÌ SAO user không phải gõ gì: user tự nói *"sao còn bắt tôi phải nhớ lệnh"* —
đúng. Cơ chế nào cần user nhớ thì cơ chế đó đã hỏng từ trong thiết kế.

🔴 TRẦN CỨNG: **TỐI ĐA 3 LUẬT**. Đây không phải chỗ chép sổ tay vào. Hook trả
tiền bằng token ở MỌI lượt, nên nhồi thêm vào đây chính là bệnh loãng ở bản
đắt tiền nhất — nó vi phạm đúng luật số 2 mà nó đang đi rao. Muốn thêm luật
thứ tư thì phải BỎ một luật đang có, và ghi `QD-nn` cho việc đổi. Tiêu chuẩn
để một luật được nằm ở đây: **quan trọng số 1 VÀ ảnh hưởng lâu dài** (user
chốt 01/08/2026) — luật chỉ đúng cho một việc thì viết vào phiếu việc.

Giá phải trả: ~110 token mỗi lượt. Rẻ hơn một lần code sai hướng phải làm lại.
Tắt: xoá mục "hooks" trong `.claude/settings.json`. (QD-09, QD-13)
Cửa canh: `soatkientruc.py` mục S11 — file này hỏng thì chặn deploy, vì hook
chết là chết IM LẶNG.
"""
import sys

# Windows console hay là cp1258/cp437 -> in tiếng Việt có dấu sẽ nổ UnicodeEncodeError,
# mà hook nổ thì im lặng mất tác dụng. Ép UTF-8 ngay từ đầu, và văn bản dưới đây
# cố ý KHÔNG dấu để còn đọc được cả khi ép encoding thất bại.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, OSError):
    pass  # CỐ Ý nuốt: ép encoding hỏng cũng không được làm chết hook (lý do ngay trên)

print("""[LUAT REPO - tu dong nhac moi luot]
User KHONG phai lap trinh vien va tu nhan "khong gioi dien dat tinh nang".

1. XIN THEM/SUA CHUC NANG (khong phai hoi dap, khong phai sua loi vat) => CAM
   viet code ngay. Doc `.claude/commands/ycau.md`: DO truoc (bang "DA DO ROI
   BAC" o QUYETDINH.md), HOI user bang AskUserQuestion trac nghiem, ghi
   VIECDANGLAM.md, roi `kehoach.md` cho user duyet. User KHONG go lenh gi ca.
2. CHONG LOANG: them dong vao repo phai TRA GIA bang cat cho khac. File co san
   chua duoc thi CAM de file moi. CHANGELOG.md 2809 dong chet vi khong ai chiu
   noi "khong" (QD-06). NGAN GON THANG DAY DU.
3. Quyet dinh nao DOI CODE => de lai vet NGAY, 1 dong o QUYETDINH.md (QD-12).
   Xong viec + 3 cua nghiem thu XANH => TU commit, KHONG hoi (QD-10).""")


# ---------------------------------------------------------------------------
# CANH BAO LỆCH VPS (QD-31, 05/08/2026)
#
# ⚠️ ĐÂY KHÔNG PHẢI "LUẬT THỨ TƯ" — trần 3 luật ở trên vẫn nguyên. Luật thì bơm
# mọi lượt; cái này là một SỰ THẬT VỀ TRẠNG THÁI, và nó **im hoàn toàn** khi
# không có gì lệch. Không lệch = 0 token, đúng nghĩa đen.
#
# Vì sao có: user chốt 05/08 — *"tôi thấy toàn phải để tôi nhắc bạn mới làm,
# không nhắc y như rằng lại lệch VPS với laptop"*. Đúng cơ chế đã hỏng ở khắp
# nơi trong repo này: việc nhớ rơi vào user. Đo lúc đó: laptop hơn VPS **7
# commit**, VPS đứng ở bản cũ mà không gì báo.
#
# 🔴 CHỈ ĐẾM COMMIT ĐỤNG CODE VPS THẬT SỰ CHẠY. Đây là phần quan trọng nhất, và
# là lý do bản đầu tiên bị vứt: trong 7 commit lệch hôm đó, **0 cái** đụng code
# bot — toàn tài liệu, cửa soát, test. Nhắc kiểu "có 7 commit chưa deploy" là
# BÁO ĐỘNG GIẢ NGAY TỪ LẦN ĐẦU, mà báo động giả vài lần là bị bỏ qua vĩnh viễn
# (đúng bài học `tgbot/alerts.py` đã trả học phí: cảnh báo phải có tiết chế).
# Kiểm ngược trên lịch sử: khoảng trước lần deploy 04/08 ra **1** ⇒ lẽ ra phải
# kêu; khoảng hiện tại ra **0** ⇒ đúng là im. Bộ lọc đúng cả hai chiều.
#
# Danh sách đường dẫn = thứ `bot.py` kéo theo (đo bằng đồ thị import, không đoán)
# + file hạ tầng deploy đụng tới. `soat/`, `tests/`, `scripts/`, `data/huongdan/`
# CỐ Ý không có: VPS không chạy chúng.
# ---------------------------------------------------------------------------
VPS_CHAY = ["bot.py", "tgbot", "anki_tools", "grammar_forms",
            "requirements.txt", "*.service"]

try:
    import subprocess
    n = subprocess.run(
        ["git", "rev-list", "--count", "origin/main..main", "--", *VPS_CHAY],
        capture_output=True, text=True, timeout=5).stdout.strip()
    if n.isdigit() and int(n) > 0:
        print(f"\n[LECH VPS] {n} commit dung CODE BOT ma chua deploy — VPS dang chay ban CU.\n"
              f"Chay `.\\deploy.ps1` truoc khi lam tiep, hoac noi ro cho user biet la dang lech.")
except Exception:
    pass    # CỐ Ý nuốt: không git / chưa có `origin/main` / máy khác — hook mà
    # chết thì mất luôn 3 luật ở trên, đắt hơn nhiều so với việc bỏ lỡ một lời nhắc
