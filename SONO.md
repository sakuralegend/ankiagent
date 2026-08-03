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

- [ ] **`tgbot/dispatch.py` 430 dòng, vượt trần 400 — user duyệt 03/08: KHÔNG tách.** `on_callback`
      ~320 dòng là một chuỗi nhánh nút; tách buộc cắt ruột hàm, lưới an toàn không phủ kín, mà bot
      là nơi lỗi chết im lặng. Đổi lại luật: **cấm thêm nhánh nút mới vào `on_callback`** — nhánh
      mới viết hàm ở file riêng cùng tầng rồi gọi một dòng từ `on_callback`. (03/08/2026)
- [ ] **`CACHLAM.md` chưa nén, và mang số liệu đã cũ.** 20 609/21 000 ký tự — gần chạm trần S10 y
      như `QUYETDINH.md` trước khi nén (QD-23). Chứa "61 lô" ×2 và "43 lô còn lại" trong khi hàng
      đợi đo 03/08 là **64 lô**. Áp đúng luật số của QD-23: số không có ngày đo thì phải đi. Để
      riêng một phiên, đừng gộp vào việc khác. (03/08/2026)
- [ ] **Bot chỉ `print`, chưa có nhật ký phân mức.** `logging.basicConfig` không tồn tại ở đâu ⇒
      không lọc được theo mức, không tách được lỗi khỏi tiếng ồn. Khác với món "log bị xoá" đã trả
      trước đó: đây là chất lượng log, không phải mất log. **Đắt** (chạm cả 3 gói) mà lợi ích chưa
      cấp thiết ⇒ để sau khi hàng đợi hết lô `cho`. (31/07/2026)
- [ ] **15 chỗ nuốt lỗi im lặng** (`except: pass` / `except Exception:` trống) trong 3 gói.
      **Không sửa hết ngay.** Áp luật từ nay: mọi `except` phải log, hoặc phải có comment nói vì sao
      được phép nuốt. (31/07/2026)
- [ ] **Không gì báo khi VPS chạy CODE CŨ hơn laptop.** Đo 02/08: lần deploy đó kéo một cục **49
      file** vì VPS đứng ở commit 31/07 13:12 ⇒ bot chạy code cũ **3 ngày** mà không dấu hiệu nào.
      `deploy.ps1` chỉ bắt được lúc pull HỎNG; **quên deploy** thì nó im hoàn toàn — mà quên mới là
      ca hay gặp. Hướng rẻ nhất: bot khai `git rev-parse --short HEAD` lúc khởi động + trong
      `/trangthai`, lệch thì mắt thấy ngay. CHẠM CODE BOT ⇒ deploy riêng.
      User chốt 02/08: *"tôi sẽ xử lí sau"*. (02/08/2026)

## Ý TƯỞNG (chờ hết hàng đợi kho)

- **Lệnh `/moi` trong bot — đọc `PHIENBAN.md` ngay trong Telegram.** User xem "có gì mới" ở đúng chỗ
  họ thực sự dùng hệ thống, khỏi phải mở repo. Việc nhỏ (đọc file + gửi text, dùng `tgbot/` sẵn có)
  nhưng CHẠM CODE BOT nên phải deploy riêng có canary. User chốt 31/07/2026: *"chức năng đó để sau"*.
