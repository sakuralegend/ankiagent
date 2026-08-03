# 💳 SỔ NỢ KỸ THUẬT

> Ghi khi vượt ngưỡng ở `CACHLAM.md` Q4 — KHÔNG sửa ngay giữa việc khác.
> Trả nợ khi: sắp sửa tiếp đúng file đó, hoặc **sổ chạm 10 mục** (dành một phiên riêng chỉ trả nợ).
> Định dạng: `- [ ] <file/hàm>: <ngưỡng nào vỡ> (ngày ghi)`
>
> 🔴 **TRẢ XONG THÌ XOÁ DÒNG ĐI, đừng đánh dấu `- [x]` rồi để đó** (cửa **S16** canh, QD-24).
> Sổ này chỉ được chứa **nợ CHƯA trả** — nợ đã trả là lịch sử, và lịch sử ở `git log`. Đo 03/08:
> xác nợ đã chiếm **67% file** và làm hỏng luôn cái ngòi "chạm 10 mục" ở trên, vì nó đếm cả xác.
> Bài học nào còn sống thì **dời sang nơi được đọc lúc cần** (bảng vùng im lặng `KIENTRUC.md`,
> comment cạnh đúng đoạn code…), đừng giữ ở đây làm nghĩa trang.

## Nợ

- [ ] **Bot chỉ `print`, chưa có nhật ký phân mức.** `logging.basicConfig` không tồn tại ở đâu ⇒
      không lọc được theo mức, không tách được lỗi khỏi tiếng ồn. Khác với món "log bị xoá" đã trả
      trước đó: đây là chất lượng log, không phải mất log. **Đắt** (chạm cả 3 gói) mà lợi ích chưa
      cấp thiết ⇒ để sau khi hàng đợi hết lô `cho`. (31/07/2026)
- [ ] **Không gì báo khi VPS chạy CODE CŨ hơn laptop.** Đo 02/08: lần deploy đó kéo một cục **49
      file** vì VPS đứng ở commit 31/07 13:12 ⇒ bot chạy code cũ **3 ngày** mà không dấu hiệu nào.
      `deploy.ps1` chỉ bắt được lúc pull HỎNG; **quên deploy** thì nó im hoàn toàn — mà quên mới là
      ca hay gặp. Hướng rẻ nhất: bot khai `git rev-parse --short HEAD` lúc khởi động + trong
      `/trangthai`, lệch thì mắt thấy ngay. CHẠM CODE BOT ⇒ deploy riêng.
      User chốt 02/08: *"tôi sẽ xử lí sau"*. (02/08/2026)
