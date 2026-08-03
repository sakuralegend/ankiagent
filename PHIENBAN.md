# 🆕 Có gì mới — dành cho NGƯỜI DÙNG

> File **duy nhất trong repo viết cho bạn**, không phải cho người sửa code. Mọi file còn lại
> (`KIENTRUC.md`, `QUYETDINH.md`, `SONO.md`, `CACHLAM.md`, `CLAUDE.md`) là tài liệu kỹ thuật —
> bạn không cần đọc.
>
> **Luật viết file này — AI phải theo:**
> 1. Chỉ ghi thứ **bạn cảm nhận được**: bot có thêm nút gì, sửa lỗi bạn từng gặp, thẻ hiện khác đi.
>    Dọn code, đổi cấu trúc, thêm cửa soát… **không ghi** — bạn không thấy chúng.
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

## v1.0.3 — 03/08/2026 (chiều)

- 📝 **47 từ bạn thêm sáng nay đã có đủ ô Hướng dẫn.** Đồ ăn · quần áo · tính từ · thiên nhiên.
- ✏️ **26 dòng nghĩa tiếng Việt được viết lại cho rõ hơn**, vì chúng là đề bài bạn nhìn để gõ từ
  Nga mà **đang trùng với từ khác trong kho** — gõ đúng vẫn bị chấm sai. Ví dụ: "cái đuôi, hàng
  đợi" nay chỉ còn *"cái đuôi (của con vật, máy bay, sao chổi)"*, còn "hàng đợi" trả về cho từ
  `очередь`. Tương tự với "đi", "tiền", "xa", "khỏe", "bây giờ", "áo khoác", "xúc xích".
- 🐟 **Vài nghĩa tiếng Việt trong kho vốn đã sai, nay đã sửa.** Đáng kể nhất: `ёрш` bị ghi là "cây
  cọ rửa" mà **mất hẳn nghĩa chính là một loài cá**; `жук` ghi "côn trùng" trong khi nó là con bọ
  **cánh cứng** (côn trùng nói chung là từ khác); `монах` ghi "nhà sư" nhưng đây là thầy tu Chính
  Thống giáo.
- 💡 Bạn không phải làm gì — mở Anki lên là thấy.

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
- 📝 45 thẻ mới có ô Hướng dẫn: **số hàng chục/trăm/nghìn · số thứ tự · đơn vị đo**.

## v1.0.1 — 02/08/2026

- ⌨️ **Sửa 23 thẻ trong deck `1-go` hiện sai mặt: đã học xong phần làm quen mà vẫn không có ô gõ.**
  Nguyên nhân: đêm 31/07 bot trên máy chủ đã nâng chúng lên chặng GÕ, nhưng sáng hôm sau laptop
  chạy một đợt cập nhật hàng loạt khi chưa tải bản mới về, nên vô tình ghi đè ngược lại. Nay 23 thẻ
  đã về đúng mặt gõ, **lịch ôn giữ nguyên**, bạn không phải làm gì cả. Cũng đã chặn để lần sau
  không lặp lại: mọi đợt cập nhật hàng loạt buộc phải tải bản mới nhất về trước khi ghi.

## v1.0.0 — 31/07/2026

Mốc đầu tiên được đánh số: bot tự nhắn nếu nó chết, sao lưu đã thử phục hồi thật (950/950 thẻ
về đúng), và từ hôm nay có máy tự kiểm code trước mỗi lần cập nhật.
