# 💳 SỔ NỢ KỸ THUẬT

> Ghi khi vượt ngưỡng ở `CACHLAM.md` Q4 — KHÔNG sửa ngay giữa việc khác.
> **MỘT NỢ = MỘT DÒNG BẢNG** (trần ký tự ở `soat_nguong.json`, cửa **S18** đếm thật).
> Chi tiết dài thì để `git log --grep`, đừng nhét vào đây — sổ này phình là hết người đọc.
>
> 🔴 **CỘT "HẾT HẠN" LÀ BẮT BUỘC** (QD-25). Quá hạn ⇒ **S18 kêu ĐỎ, chặn deploy** cho tới khi:
> trả nợ (xoá dòng) · hoặc gia hạn kèm lý do mới trong commit. Không cho món nợ nằm im mãi.
> 🔴 **TRẢ XONG THÌ XOÁ DÒNG, đừng đánh dấu rồi để đó** (cửa **S16**, QD-24) — sổ chỉ chứa nợ
> CHƯA trả. Nợ đã trả là lịch sử, và lịch sử ở `git log`. Bài học còn sống thì dời sang nơi
> được đọc lúc cần (vùng im lặng `KIENTRUC.md`, comment cạnh đúng đoạn code), đừng giữ làm nghĩa trang.

## Nợ

| Nợ | Vì sao chưa trả | Hết hạn |
|---|---|---|
| `soatlo.py:123` bỏ so khi chuẩn không có dấu sắc, `:125` gộp `ё→е` ⇒ **từ trọng âm ở `ё` chưa bao giờ được soi** (bắt 05/08: `тве́рдость`). | Sửa công cụ giữa phiên chạy lô đã đốt trọn một cửa sổ 5h. Cần phiên riêng + đo trước xem bỏ chốt `ё` thì kêu oan mấy chỗ. | 2026-08-20 |
| Bảng chia máy nối vào thẻ in dạng cách 5 **`-ою` (lối cổ/thi ca) KHÔNG có nhãn nào** ⇒ mọi danh từ giống cái đều dạy người mới rằng hai dạng ngang nhau (bắt 07/08 ở cả 10 danh từ cái của k09). | Sửa ở `grammar.go_bang()`, đụng **mọi thẻ đã nạp** ⇒ phải đo trước rồi nạp lại cả kho. L4 cấm gộp vào phiên chạy lô. | 2026-08-27 |
| Mẫu phiếu việc ở `ycau.md`/`kehoach.md` **không lọt nổi trần 14 dòng của S19**, và `kehoach.md` bắt thêm mục `##` thứ hai mà S19 chỉ cho 1 (bắt 06/08 khi đi đúng ba cửa). | Phải chọn: nới trần hay viết lại hai mẫu. Đang giữa việc vá sync, L4 cấm gộp. | 2026-08-20 |

🔴 **Trước khi thêm dòng, hỏi: đây có phải NỢ không?** Nợ = việc mình BIẾT phải làm
mà cố ý hoãn. KHÔNG phải nợ, và cấm ghi vào đây:
· **Con số trần** (dòng/ký tự) — chúng ở `soat_nguong.json`, cửa S13/S10 canh thật.
  Chép sang đây là dựng sổ thứ hai, mà hai sổ song song thì không sổ nào được tin.
· **Sự thật về môi trường** đã có quyết định "để yên" — chỗ của nó là bảng
  "📏 ĐÃ ĐO RỒI BÁC" ở `QUYETDINH.md`, để phiên sau khỏi đề xuất lại.
