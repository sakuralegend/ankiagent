# 🆕 Có gì mới — dành cho NGƯỜI DÙNG

> File **duy nhất trong repo viết cho bạn**, không phải cho người sửa code. Mọi file còn lại
> (`KIENTRUC.md`, `QUYETDINH.md`, `SONO.md`, `CACHLAM.md`, `CLAUDE.md`) là tài liệu kỹ thuật —
> bạn không cần đọc.
>
> **Luật viết file này — AI phải theo:**
> 1. Chỉ ghi khi **cấu trúc lõi đổi**: bot có thêm nút gì, sửa lỗi bạn từng gặp, cách app cư xử
>    khác đi. Dọn code, thêm cửa soát… **không ghi** — bạn không thấy chúng.
> 🔴 **THÊM TỪ / SOẠN LÔ KHO / SỬA NGHĨA TIẾNG VIỆT ⇒ TUYỆT ĐỐI KHÔNG GHI** (user bác 02/08, nhắc
>    lại 04/08 — xem QD-07). Đó là việc chạy hằng ngày, không phải "có gì mới". Mục cũ trong file
>    này từng ghi kiểu đó là **SAI, đã xoá** — đừng lấy chúng làm mẫu.
> 2. Ngôn ngữ thường, **không thuật ngữ**. Mỗi mục một dòng.
> 3. **Bản cũ quá thì XOÁ** — lịch sử đầy đủ đã có `git log` lo. Trần số bản và số mục mỗi bản
>    nằm ở `soat_nguong.json`, máy tự canh (cửa S14) — file này mà dài là đi đường `CHANGELOG.md` cũ.
> 4. Số hiệu: `vMAJOR.MINOR.PATCH` — **MAJOR** khi bạn phải tự làm gì đó (vd đồng bộ lại điện
>    thoại) · **MINOR** khi có tính năng mới · **PATCH** khi chỉ sửa lỗi.

---

## v2.5.0 — 30/10/2026

- 🔽 **Ô nghĩa tiếng Anh gọn lại.** Chỉ hiện 3 nghĩa đầu; từ nhiều nghĩa hơn có mũi tên nhỏ màu xanh ngay dưới, chạm để xem hết, chạm lần nữa để gấp. Nhờ vậy ô tiếng Việt và nhãn từ loại không còn bị đẩy khỏi màn hình điện thoại. Áp dụng cả thẻ từ vựng lẫn thẻ số nhiều. Chỉ cần Sync như thường.

## v2.4.0 — 19/10/2026

- 🔊 **Giọng đọc mới cho cả kho: Yandex "alena".** Đọc đúng trọng âm và đủ âm. Giọng cũ (OpenRussian) có từ cụt âm đầu (vd. согла́сный), có từ sai trọng âm.
- 💬 **Câu ví dụ có tiếng.** Cuối mỗi câu tiếng Nga có một dấu ▶ nhỏ, mờ; bấm vào thì đọc câu đó. Câu **không tự đọc** khi lật thẻ.
- 🐢 **Nghe chậm khi cần.** Đáy mặt sau thẻ có chữ mờ "· 1× ·"; chạm vào để đổi 1× → 0,75× → 0,5×, rồi bấm ▶ (từ hoặc câu) là nghe chậm. Lật thẻ thì từ vẫn tự đọc ở tốc độ thường; sang thẻ khác tự về 1×.
- 📲 Lần Sync đầu tiên điện thoại tải khoảng **190 MB** tiếng mới. **Không phải làm gì thêm.**
- ⚠️ Từ **01/11** Yandex hết miễn phí (khoảng 4 500–22 000 đồng/tháng tuỳ số từ thêm). Nếu thẻ mới bỗng **không có tiếng**, có thể tài khoản Yandex hết tiền: vào Yandex Cloud → **Billing** để nạp.

## v2.3.0 — 01/09/2026

- 🗑️ **Bỏ hẳn bộ thẻ "chi phối" (17 thẻ, thư mục `GRAMMAR::chi phối`).** Bác chốt bỏ vì lo độ chính xác học thuật. Thẻ và thư mục đã xoá, đã đồng bộ — **iPhone chỉ cần bấm Sync như thường, không phải làm gì thêm**. Bản chép 17 thẻ vẫn giữ trong `backups/` nếu đổi ý. Trang web luyện chi phối cũng huỷ; `slushai` giữ đúng vai **tập nghe**.

## v2.2.0 — 01/09/2026

- 🗑️ **Bỏ lệnh `/suadeck` và nút "📚 Cả deck".** Nó làm lại TOÀN BỘ thẻ của một thư mục bằng một nút bấm — không xem trước, không hoàn tác, mà dữ liệu lấy về có chỗ sai. Nó sinh ra hồi thư mục còn chia theo NGÀY, ba ngày sau đã đổi sang CHỦ ĐỀ. **`/sua` (làm lại MỘT thẻ) và nút "✏️ Làm lại thẻ" giữ nguyên.**
