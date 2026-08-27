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

## v2.0.0 — 23/08/2026

- 🔴 **BẠN PHẢI LÀM MỘT VIỆC, nếu không máy chủ sẽ chạy sai:** trên laptop mở Anki, bấm
  `Tools → Sync` và chọn **Upload**; sau đó trên máy chủ mở `vnc.bat`, bấm Sync và chọn
  **Download**. Cần bước này vì các thư mục học đã bị sắp xếp lại, Anki không tự trộn được.
- 📂 **Kho từ được chia lại từ 19 nhóm thành 35 nhóm.** Trước đây có hai nhóm kiểu "linh tinh"
  và "trừu tượng" — thứ gì không biết xếp đâu thì bị bỏ vào đó, lâu ngày phình lên **335 thẻ
  nằm sai chỗ**. Hai nhóm đó nay **bỏ hẳn**, và từ nay không nhóm nào được mang nghĩa
  "phần còn lại" nữa.
- 🚌 **497 thẻ được xếp lại cho đúng.** Ví dụ: *xe buýt, toa tàu* trước nằm chung với *trường
  học, cửa hàng*, nay có nhóm **phương tiện đi lại** riêng; *người Mỹ, người nước ngoài* trước
  nằm trong nhóm **gia đình**, nay ở nhóm **quốc tịch**; các từ chỉ **màu sắc** về đúng nhóm màu.
- ♾️ **Bỏ giới hạn 20 thẻ mới mỗi ngày.** Trước đây có giới hạn này mà bạn không biết. Nay học
  bao nhiêu từ mới một ngày là tuỳ bạn.
- ✅ **Không mất thẻ nào và không mất tiến độ ôn.** Đã đếm lại: đủ 1.212 thẻ từ vựng, 124 thẻ
  số nhiều, 17 thẻ chi phối. Lịch ôn của từng thẻ giữ nguyên như cũ.

---

## v1.0.6 — 12/08/2026

- ⚡ **Sửa đúng cái bạn báo: thêm từ bỗng chậm hẳn, có lúc 12-13 giây.** Không phải tại model
  mới như bạn nghi. Thỉnh thoảng AI trả lời sai vài dấu câu, bot đọc không ra nên **tưởng AI
  hỏng và hỏi lại từ đầu 2-3 lần** — mỗi lần hỏi lại tốn thêm mấy giây, có ca tốn tới 26 giây
  cho một từ. Nay bot **bắt AI trả lời đúng khuôn ngay từ đầu**, không còn cửa cho kiểu hỏng
  này. Đo lại trên máy chủ: 20 từ liền, **không từ nào phải hỏi lại**, mỗi từ khoảng 5-6 giây.
- 🔍 **Chuyện đáng nói: model bạn tưởng đã đổi thì thật ra chưa bao giờ đổi.** Máy chủ có một
  cài đặt riêng đè lên, vẫn giữ model cũ suốt từ 06/08. Nay đã sửa cho khớp, và **bot tự khai
  model nó đang chạy mỗi lần khởi động** để lần sau không ai phải đoán nữa.
