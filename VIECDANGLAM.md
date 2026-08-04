# 🎯 VIỆC ĐANG LÀM
> Phiếu này bị GHI ĐÈ ở việc kế tiếp. Xong phiên: để TRỐNG hoặc chừa đúng MỘT đầu
> việc (cửa **S19** đếm mục `##`, QD-25). Việc chưa tới lượt ⇒ `SONO.md` kèm HẠN XOÁ.

## ⏭️ Phiên sau: gỡ `Sync status 2` trên VPS, rồi chạy lô **k38**

🔴 **Trước mọi thứ khác** — Anki trên VPS đang kẹt, bot chạy nhưng không sync được.
Hỏi user đã bấm chưa: `vnc.bat` → trong Anki bấm **Sync** → chọn **Download from
AnkiWeb** (KHÔNG chọn Upload — bản VPS thiếu nội dung ô `BangMay`).
Kiểm sau khi bấm: `curl` vào `:8765` trên VPS thấy field `BangMay` và
`journalctl -u anki-bot` hết dòng `[WARN ] Sync AnkiWeb lỗi`.
Chưa gỡ xong thì **đừng thêm thẻ bằng bot** — thẻ đó chỉ nằm trên VPS và sẽ mất.

Rồi mới soạn lô: **43 lô / 662 từ duyệt / 377 chờ**, đọc `data/huongdan/kho/TIEPTUC.md`
là đủ. Trần phiên ~58 từ (1 từ ≈ 1,4% hạn mức).

🔴 **Đổi so với trước:** bỏ bước "đọc field thật trong Anki dán vào lời nhắn" và bước
"đồng bộ dòng `V` sang `tudien.json`" — `tiep` nay đọc nghĩa Việt thẳng từ thẻ (QD-27).
Vẫn phải quét `vacham` trước khi giao lô. Anki **phải đang mở**, không thì `tiep`
dừng hẳn thay vì lặng lẽ dùng bản cũ.
