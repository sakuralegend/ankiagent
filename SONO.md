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
| 🔴 **Anki trên VPS kẹt `Sync status 2`** sau schema mod 04/08 — bot vẫn chạy nhưng KHÔNG sync được, thẻ nó thêm sẽ MẤT khi tải về | Không có đường chạy bằng lệnh: AnkiConnect chỉ có `sync`, không chọn được chiều. Bắt buộc người bấm. Trả bằng: chạy `vnc.bat` → trong Anki bấm Sync → chọn **Download from AnkiWeb** | 2026-08-05 |
| **Anki VPS 25.02.7, laptop 26.5.0** — lệch một đời. Sync vẫn chạy, nhưng chép thẳng file collection giữa hai bên là hỏng | Phát hiện 04/08 khi tìm cách gỡ `Sync status 2` không cần bấm tay. Chưa gây sự cố nào; nâng ảnh Docker là việc đứng riêng (L4) | 2026-10-01 |
| **`congcu.py` nới mốc 446 → 491 dòng** (QD-26/27 thêm: đọc thẻ làm chân lý, ghi hai ô, di trú `BangMay`) | Không chuyển sang `khochung.py` được — file đó cố ý KHÔNG đụng Anki để `soatlo.py` chạy offline. Còn cách 700 (trần tách). Trả bằng: bỏ `cmd_bang` khi di trú xong | 2026-10-01 |
