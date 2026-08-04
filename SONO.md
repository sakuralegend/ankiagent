# 💳 SỔ NỢ KỸ THUẬT

> Ghi khi vượt ngưỡng ở `CACHLAM.md` Q4 — KHÔNG sửa ngay giữa việc khác.
> **MỘT NỢ = MỘT DÒNG BẢNG** (trần ký tự ở `soat_nguong.json`, cửa **S18** đếm thật).
> Chi tiết dài thì để `git log --grep`, đừng nhét vào đây — sổ này phình là hết người đọc.
>
> 🔴 **CỘT "HẾT HẠN" LÀ BẮT BUỘC** (QD-25). Quá hạn ⇒ **S18 kêu ĐỎ, chặn deploy** cho tới khi:
> trả nợ (xoá dòng) · hoặc gia hạn kèm lý do mới trong commit. Không cho món nợ nằm im mãi.
> 🔴 **TRẢ XONG THÌ XOÁ DÒNG, đừng đánh dấu rồi để đó** (cửa **S16**, QD-24) — sổ chỉ chứa nợ
> CHƯA trả. Nợ đã trả là lịch sử, và lịch sử ở `git log`. Bài học còn sống thì dời sang nơi
> được đọc lúc cần (vùng im lặng `KIENTRUC.md`, comment cạnh đúng đoạn code), đừng giữ làm nghĩa trang.

## Nợ

| Nợ | Vì sao chưa trả | Hết hạn |
|---|---|---|
| **VPS chưa nhận code mới** của phiên 04/08 (ô `BangMay`, nhật ký phân mức, `/thongke` khai bản mã) — laptop đã có, VPS chưa | Chạm code bot ⇒ deploy riêng, không gộp vào phiên vừa đụng vùng im lặng. Trả bằng: `.\deploy.ps1` rồi `journalctl -u anki-bot` xem dòng "bản mã" | 2026-08-11 |
| **`congcu.py` nới mốc 446 → 491 dòng** (QD-26/27 thêm: đọc thẻ làm chân lý, ghi hai ô, di trú `BangMay`) | Không chuyển sang `khochung.py` được — file đó cố ý KHÔNG đụng Anki để `soatlo.py` chạy offline. Còn cách 700 (trần tách). Trả bằng: bỏ `cmd_bang` khi di trú xong | 2026-10-01 |
