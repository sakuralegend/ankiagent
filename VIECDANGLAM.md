# 🎯 VIỆC ĐANG LÀM

> Phiếu bị GHI ĐÈ ở việc kế tiếp. Xong phiên: để TRỐNG hoặc chừa đúng MỘT đầu
> việc (cửa **S19**, QD-25). Việc chưa tới lượt ⇒ `SONO.md` kèm HẠN XOÁ.

## Lệnh /tumoi xin 10 từ mới — CODE XONG 23/08, chờ thử thật trên bot sau deploy

**Một câu:** bấm một lệnh trong bot là hiện 10 từ mới **dễ nhất còn thiếu** theo chuẩn ТРКИ kèm nghĩa; bấm ✅ thì bot thêm cả 10 vào Anki như thêm tay. Cần thêm nữa thì bấm lại.
**Đo 23/08:** còn thiếu **178 từ A1 · 296 A2 · 703 B1** (≈118 lần bấm là hết B1). Nguồn từ đã nằm sẵn ở `data/rosedu_muc.json`.
**User đã chốt:** lấy THEO TRÌNH ĐỘ, không gom theo chủ đề · bấm ✅ mới thêm (luật 19/07: bot không bao giờ tự thêm) · từ đã loại thì KHÔNG hiện lại · ô Hướng dẫn để trống, đợi soạn lô.
**Coi là XONG khi:** gõ lệnh → hiện 10 từ A1 kèm nghĩa → bấm ✅ → 10 thẻ vào Anki, có tag chủ đề, deck khớp tag · bấm lại ra 10 từ KHÁC · "bỏ 3 7" thì hai từ đó không bao giờ hiện lại.
**CỐ Ý KHÔNG làm:** không tự động theo giờ (user tự bấm) · không đổi được số 10 · không đụng ô Hướng dẫn.
**Đã đo:** trùng "ĐÃ ĐO RỒI BÁC"? KHÔNG · dùng lại có sẵn: `chay_hang_loat` (chạy lô + nút ⏹) · `_scan_list_text_keyboard` (danh sách + ✅ + "bỏ 3 7") · `_already_has_card` · `process_word`.

### Kế hoạch (đã duyệt 23/08/2026)
1. Bộ chọn từ ở `tgbot/flow_add.py`: bản chụp − thẻ đã có − từ đã loại, sắp theo mức (A1 hết mới sang A2).
2. Nhấc phần vẽ danh sách chờ duyệt (số thứ tự · ✅/🚫 · "bỏ 3 7") sang `tgbot/core.py` — luồng CẤM import ngang luồng (S3), mà `core.py` đã là nhà của `chay_hang_loat`. Chạm trần 400 dòng thì ghi `SONO.md`.
3. Chạy lô bằng `chay_hang_loat` + `process_word`; `tumoi_bo_qua.json` ở gốc + gitignore; lệnh cắm vào `app.py`, nút vào `dispatch.py`.
**Nghiệm thu:** 3 cửa L3 + 1 test bộ chọn từ (bỏ đúng 3 nhóm, trả đúng 10) + thử thật trên bot.
