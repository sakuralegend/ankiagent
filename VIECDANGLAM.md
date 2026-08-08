# 🎯 VIỆC ĐANG LÀM

> Phiếu này bị GHI ĐÈ ở việc kế tiếp. Xong phiên: để TRỐNG hoặc chừa đúng MỘT đầu
> việc (cửa **S19**, QD-25). Việc chưa tới lượt ⇒ `SONO.md` kèm HẠN XOÁ.

## Sửa logic TÔ bảng chia (`anki_tools/hinh_thai.py`) — user báo lỗi 08/08

Thẻ `крокодил` có ô đỏ "cách 4 mượn hình cách 2" mà bảng dưới không tô ô nào.
Đo ra 5 chỗ: ① cách 4 = cách 2 vô hình (102 ô/64 từ) · ② cùng hiện tượng lại
ĐƯỢC tô ở 8 từ (`президент`…) kèm nhãn sai · ③ danh từ chia như tính từ bị gán
nhãn bịa rồi tô 10/12 ô · ④ trọng âm ở nguyên âm ĐẦU bị coi là "không có"
(`окунь`) · ⑤ 97 từ sáng quá nửa bảng — **user chốt GIỮ NGUYÊN ⑤** ("suy ra
được thì thôi, nhảy trọng âm hay khác từ là tô ngay"). Sửa ①②③④ rồi dựng lại
cả 1065 thẻ.
