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

## v1.0.2 — 03/08/2026

- 🔄 **Sửa 21 thẻ trong deck `0-quen` sáng nay bị lật sang mặt gõ.** Đêm qua máy chủ đã nâng chúng
  lên chặng gõ, nhưng sáng nay bạn học chúng trên thiết bị **chưa tải bản mới về**, nên khi đồng bộ
  thì thẻ bị kéo ngược về deck cũ mà cái nhãn "đã lên chặng gõ" thì còn nguyên — thành ra sai mặt.
  Nay 21 thẻ đã về đúng mặt làm quen, bạn không phải làm gì. Đêm nay máy chủ sẽ tự nâng chúng lên
  chặng gõ như bình thường (và xoá lịch ôn của chúng — đó vốn là mục đích của chặng gõ).
- 🔄 **Từ nay bot tự canh việc này mỗi 30 phút.** Thẻ nào hiện sai mặt thì nó tự sửa rồi nhắn cho
  bạn biết; lúc mọi thứ bình thường thì nó im lặng, không thêm tin nhắn nào.
- 💡 **Vẫn nên: buổi sáng để app Anki đồng bộ xong rồi mới bắt đầu học.** Nếu app đã mở sẵn từ tối
  hôm trước, nó không tự tải bản mới về — cửa canh chỉ sửa lại được sau đó, không ngăn được.

<sub>Bản cũ hơn đã xoá — `git log` giữ đủ. v1.0.1 là cùng một lỗi mặt thẻ với v1.0.2 ở trên;
v1.0.0 là mốc hạ tầng (bot, sao lưu, máy soát code), không phải thứ đổi lõi thẻ.</sub>
