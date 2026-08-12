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

## v1.0.6 — 12/08/2026

- ⚡ **Sửa đúng cái bạn báo: thêm từ bỗng chậm hẳn, có lúc 12-13 giây.** Không phải tại model
  mới như bạn nghi. Thỉnh thoảng AI trả lời thừa một dấu phẩy, bot đọc không ra nên **tưởng AI
  hỏng và hỏi lại từ đầu 2-3 lần** — mỗi lần hỏi lại tốn thêm mấy giây. Đo được cứ khoảng 10 từ
  thì 1 từ dính, và có ca tốn tới 26 giây cho một từ. Nay bot đọc được luôn, hỏi đúng một lần.
- 🔍 **Chuyện đáng nói: model bạn tưởng đã đổi thì thật ra chưa bao giờ đổi.** Máy chủ có một
  cài đặt riêng đè lên, vẫn giữ model cũ suốt từ 06/08. Nay đã sửa cho khớp, và **bot tự khai
  model nó đang chạy mỗi lần khởi động** để lần sau không ai phải đoán nữa.

## v1.0.5 — 06/08/2026

- 🩹 **Sửa đúng cái bạn gặp sáng nay: dọn xong mà iPhone bấm sync mãi vẫn thấy thẻ ở `1-go`.**
  Bot đã chuyển thẻ thật, nhưng kết quả **nằm lại trên VPS 7 tiếng** mà nó vẫn báo "đã đẩy lên
  AnkiWeb". Nay sau khi dọn, bot **tự kiểm lại xem AnkiWeb đã nhận thật chưa** rồi mới dám nói.
- 🚨 **Chưa tới AnkiWeb thì bot nhắn báo động cho bạn**, kèm câu phải làm: mở Anki trên laptop
  bấm Sync một lần. Trước đây nó im lặng, nên bạn chỉ biết bằng cách bấm mò trên điện thoại.
- ⚠️ **Câu trả lời của `/don` đổi lời.** Giờ nó nói một trong ba: *"AnkiWeb đã nhận"* · *"CHƯA
  tới AnkiWeb"* · *"chưa kiểm được"*. Câu giữa nghĩa là **đừng tin là xong**, phải làm gì đó.

## v1.0.4 — 04/08/2026

- 🪨 **402 thẻ "hoá thạch" đã được gỡ.** Đó là những từ bạn từng bấm Again nhiều lần rồi Anki
  đánh dấu khó vĩnh viễn — có gõ đúng bao nhiêu lần cũng không hạ xuống được. Lần Optimize hôm
  nay của bạn đã gỡ gần hết; số còn kẹt lại sẽ tự thoát trong vài tuần.
- 🔧 **Ba nhóm deck bị bỏ quên nay đã dùng chung thiết lập với các deck còn lại.** Trước đó
  `0-quen` và `1-go` vẫn chạy thiết lập cũ từ tháng trước, nên mọi từ mới đều đi qua đúng chỗ
  gây ra chuyện "hoá thạch" ở trên.
- ⏳ **Chu kì ôn sắp tới sẽ ngắn lại khoảng một phần ba.** Đây là điều bạn muốn hay không tuỳ
  cách nhìn, nhưng nó đúng: Anki vừa học lại từ dữ liệu thật của bạn và thấy nó đang cho bạn
  nghỉ hơi lâu. Ngày đến hạn của thẻ đang có **không đổi** — chỉ lần ôn tới mới áp mức mới.

<sub>Bản cũ hơn đã xoá — `git log` giữ đủ. v1.0.2 và v1.0.1 là cùng một lỗi: thẻ trong
`0-quen` hiện sai mặt vì học trên máy chưa tải bản mới; bot đã tự canh việc đó mỗi 30 phút từ
03/08. v1.0.0 là mốc hạ tầng, không đổi lõi thẻ.</sub>
