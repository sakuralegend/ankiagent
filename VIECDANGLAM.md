# 🎯 VIỆC ĐANG LÀM

> Phiếu bị GHI ĐÈ ở việc kế tiếp. Xong phiên: để TRỐNG hoặc chừa đúng MỘT đầu
> việc (cửa **S19**, QD-25). Việc chưa tới lượt ⇒ `SONO.md` kèm HẠN XOÁ.

(trống — 13/09/2026: sửa bot ngốn 1 GB RAM trên VPS (cửa canh 30′ tải `cardsInfo`
cả kho). Còn MỘT việc kiểm sau deploy ≥1 giờ: trên VPS
`ps -o rss= -p $(systemctl show -p MainPID --value anki-bot)` phải dưới ~200000 kB;
cao hơn ⇒ `git revert` commit "Cua canh 30'" rồi `deploy.ps1` và tìm tiếp.)
