# 🎯 VIỆC ĐANG LÀM

> Phiếu bị GHI ĐÈ ở việc kế tiếp. Xong phiên: để TRỐNG hoặc chừa đúng MỘT đầu
> việc (cửa **S19**, QD-25). Việc chưa tới lượt ⇒ `SONO.md` kèm HẠN XOÁ.

## Thẻ động từ hiện CẢ NHÓM cùng gốc, và gợi ý bạn thể lúc thêm từ

**Một câu:** để lúc ôn thấy ngay ba từ cùng gốc khác nhau sắc thái chỗ nào.
**User chốt:** liệt kê cả nhóm nhưng CHỈ từ đã có thẻ · lúc thêm từ gợi ý ĐÚNG 1 bạn thể · dọn 49 bạn thể còn thiếu bằng script MỘT LẦN, KHÔNG tạo lệnh bot · BỎ HẲN họ tiền tố.
**XONG khi:** thẻ `слушать` hiện 3 dòng `слушать`/`послушать`/`прослушать` kèm nghĩa Việt; thêm `готовить` xong bot hỏi "thiếu `подготовить`?".
**CỐ Ý KHÔNG:** họ tiền tố `записать` (không phải biến thể, `/tumoi` lo rồi) · gợi ý quá 1 bạn thể.
**Đã đo:** `partners[0]` = bạn thể phổ biến nhất (38/38) ⇒ khỏi dump/ngưỡng · lật QD-26: lý do cũ cấm in từ CHƯA HỌC, đây chỉ in từ đã có thẻ.

### Kế hoạch (duyệt 27/08)
1. `anki_the.py`: `nhom_dong_tu()` nối động từ bằng `partners`; **bỏ** `remember()` ghi-theo-tên lúc dựng thẻ (thừa — `GrammarJSON` đã vào ô của chính thẻ; nó là thủ phạm ghi đè `нарезать`). 2. `bang_chia.py`: `cap_the_html(rec, nhom=None)` — nhóm ≥3 in cả nhóm, còn lại y hệt hôm nay. 3. `anki_client.ghi_grammar_json` nhận `note_id`; lệnh hàng loạt ghi theo id thẻ. 4. `congcu.py bang` đọc `GrammarJSON` của CHÍNH thẻ, không tra theo tên. 5. `flow_add.py`: thêm động từ xong mà `partners[0]` chưa có ⇒ hỏi 1 nút. 6. Script `_va_` dọn 49 bạn thể + sửa thẻ `нареза́ть`, chết trong cùng commit (L2). 7. Test: `acc` khớp `Word` mọi thẻ · nhóm 2 từ in y hệt cũ.
**Danh tính từ = `acc` + thể** (đã lưu sẵn 1253 thẻ; đo: tên bỏ dấu nhập nhằng 156 ca → `acc` còn 5 → +thể còn 2, mà 2 ca đó là dòng lặp y hệt). KHÔNG dùng id OpenRussian: phải cào lại 1253 từ, và id không tự kiểm được còn `acc` so được với `Word`.
