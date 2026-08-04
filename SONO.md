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
| 🔴 **Rác bảng chia tầng dữ liệu, 7 ca**: `тётя` · `жена́тый` · `челове́ки` · `кня́зи` · `педагоги́ческый` · `фотограф` · cách 5 `-ою` không nhãn | Cửa máy không đo phần máy nối vào thẻ. Vá phải quyết dạng tiếng Nga đúng ⇒ cần agent context sạch, tốn cỡ một lô. Cách vá: `git show c6a3f94` | 2026-09-04 |
| **Bot chỉ `print`, chưa có nhật ký phân mức** — không lọc được theo mức, không tách lỗi khỏi tiếng ồn | Chạm cả 3 gói ⇒ đắt, mà chưa cấp thiết. CHẠM CODE BOT ⇒ deploy riêng, cấm gộp vào phiên chạy lô | 2026-10-01 |
| **Không gì báo khi VPS chạy CODE CŨ hơn laptop** — đã có lần bot chạy code cũ 3 ngày mà im. Hướng rẻ: bot khai `git rev-parse --short HEAD` lúc khởi động + trong `/trangthai` | User chốt 02/08 *"tôi sẽ xử lí sau"*. CHẠM CODE BOT ⇒ deploy riêng | 2026-10-01 |
