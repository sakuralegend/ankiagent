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

## v2.3.0 — 01/09/2026

- 🗑️ **Bỏ hẳn bộ thẻ "chi phối" (17 thẻ, thư mục `GRAMMAR::chi phối`).** Bác chốt bỏ vì lo độ chính xác học thuật. Thẻ và thư mục đã xoá, đã đồng bộ — **iPhone chỉ cần bấm Sync như thường, không phải làm gì thêm**. Bản chép 17 thẻ vẫn giữ trong `backups/` nếu đổi ý. Trang web luyện chi phối cũng huỷ; `slushai` giữ đúng vai **tập nghe**.

## v2.2.0 — 01/09/2026

- 🗑️ **Bỏ lệnh `/suadeck` và nút "📚 Cả deck".** Nó làm lại TOÀN BỘ thẻ của một thư mục bằng một nút bấm — không xem trước, không hoàn tác, mà dữ liệu lấy về có chỗ sai. Nó sinh ra hồi thư mục còn chia theo NGÀY, ba ngày sau đã đổi sang CHỦ ĐỀ. **`/sua` (làm lại MỘT thẻ) và nút "✏️ Làm lại thẻ" giữ nguyên.**

## v2.1.0 — 27/08/2026

- 🔗 **Thẻ động từ nào có 3 từ cùng gốc thì hiện cả ba, kèm nghĩa từng từ.** Trước đây thẻ
  `слушать` khai bạn thể là `послушать`, còn thẻ `прослушать` lại khai bạn thể là `слушать` —
  ôn hai thẻ thấy mâu thuẫn, mà cả ba đều dán chung nhãn "hoàn thành". Giờ cả ba nằm cùng một
  chỗ: `слушать` (nghe) · `послушать` (nghe một lát) · `прослушать` (nghe hết một lượt). Chỉ
  liệt kê từ bạn ĐÃ CÓ thẻ, không thêm từ lạ. Ba nhóm bị đổi: nghe, nói, nhảy.
- ➕ **Thêm một động từ bằng cách gõ tay xong, bot hỏi luôn nửa kia của cặp thể.** Ví dụ thêm
  `готовить` thì bot mời thêm `подготовить`. Bấm ✅ mới thêm. Quét ảnh và `/tumoi` vẫn im lặng như cũ —
  thêm 30 từ mà hỏi 30 lần thì không ai bấm hết.
- 🐛 **Sửa lỗi thẻ mang bảng chia của từ khác.** Thẻ `нареза́ть` (đang thái) đang hiện dữ liệu
  của `наре́зать` (thái xong) — hai từ khác nhau, viết giống hệt, chỉ khác chỗ nhấn giọng. Máy trước
  đây tìm thẻ bằng cách bỏ dấu nhấn nên coi chúng là một rồi ghi đè lẫn nhau. Đã sửa thẻ đó và
  bịt đường gây lỗi — từ điển có 156 cặp kiểu này, 22 cặp nằm trong danh sách từ bạn sắp học.
- 🏷️ **Ô "loại từ" trên thẻ hết hiện chữ `other`.** 93 thẻ — toàn từ hay dùng như `там`, `в`, `и`, `не`, `ой` — mặt sau chỉ ghi "other", tức là có một ô mà không dạy gì. Nguyên nhân: từ điển nguồn gom trạng từ, giới từ, liên từ, trợ từ vào chung một rọ tên "other". Giờ mỗi thẻ ghi đúng loại của nó (`adverb`, `preposition`, `conjunction`, `particle`, `pronoun`, `predicative`, `interjection`), và thẻ mới thêm từ nay cũng vậy.

