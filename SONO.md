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
- [ ] **RÁC TẦNG DỮ LIỆU NGỮ PHÁP — 7 lô đã bắt, agent chỉ dán băng được bằng lời trên thẻ.**
      Bảng chia do `congcu.py bang` nối vào thẻ lúc ghi, nên rác chảy thẳng ra mặt thẻ trong khi
      `soat`/`dodai` chỉ đo phần agent VIẾT ⇒ **không cửa máy nào canh lớp này**. Đã bắt:
      `тётя` acc pl in `те́тей` (mất `ё`) · `жена́тый` mọc dòng trạng từ `жена́то` không có thật ·
      `челове́ки/челове́ков` và `кня́зи` in không nhãn "lối cổ" · **`педагоги́ческый`/`педагоги́ческым`
      (chữ `ы` thay `и`) là dạng KHÔNG TỒN TẠI** · `фотограф` **đảo cách 3 số ít với số nhiều** +
      một ô mất trọng âm · cách 5 lối cổ `-ою/-ею` in không nhãn ở hàng chục bảng giống cái ·
      `москва` bị cờ `BAT THUONG` báo THỪA vì ô `Москв` hết nguyên âm nên `stress_pos` lệch.
      ✅ **Cách trả nợ đã biết rồi, làm một lần rồi (ca `спра́ва` 04/08):** sửa thẳng field
      `GrammarJSON` của note qua `anki_client.ghi_grammar_json` (cửa L1, QD-11 — thẻ là nơi DUY
      NHẤT dữ liệu này tồn tại, **không có file cache nào**), sao lưu bản cũ vào `backups/` trước,
      rồi `nap --apply --tatca` để dựng lại mặt thẻ. Mỗi ca ~5 phút. (04/08/2026)
