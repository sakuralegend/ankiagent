# 🎯 VIỆC ĐANG LÀM
> Phiếu này bị GHI ĐÈ ở việc kế tiếp. Xong phiên: để TRỐNG hoặc chừa đúng MỘT đầu
> việc (cửa **S19** đếm mục `##`, QD-25). Việc chưa tới lượt ⇒ `SONO.md` kèm HẠN XOÁ.

## ⏭️ Phiên sau: DEPLOY lên VPS, rồi chạy lô **k38**

**Việc đầu tiên, trước mọi thứ khác:** `.\deploy.ps1`. Phiên 04/08 đổi code bot
(nhật ký phân mức, `/thongke` khai bản mã) mà VPS **chưa nhận** — đang là dòng nợ
duy nhất trong `SONO.md`. Kiểm bằng `journalctl -u anki-bot` thấy dòng "bản mã"
khớp `git rev-parse --short HEAD`.

Rồi mới soạn lô: **43 lô / 662 từ duyệt / 377 chờ**, đọc `data/huongdan/kho/TIEPTUC.md`
là đủ. Trần phiên ~58 từ (1 từ ≈ 1,4% hạn mức).

🔴 **Đổi so với trước:** không còn phải "đọc field thật trong Anki rồi dán vào lời
nhắn" và không còn bước "đồng bộ dòng `V` sang `tudien.json`` — `tiep` nay tự đọc
nghĩa Việt thẳng từ thẻ (QD-27). Vẫn phải quét `vacham` trước khi giao lô.
Anki **phải đang mở**, nếu không `tiep` dừng hẳn thay vì dùng bản cũ.
