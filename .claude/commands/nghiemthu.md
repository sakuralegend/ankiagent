---
description: Chạy đủ 3 cửa soát + soi diff có to hơn lời hứa không, rồi đóng phiếu việc
---

# /nghiemthu — cửa số 3: "xong" phải có bằng chứng, không phải cảm giác

Chạy sau khi viết code xong, **trước** khi `.\deploy.ps1`.

## Bước 1 — Chạy đủ ba lệnh (L3), CHẠY THẬT, không được chỉ nhắc tên

```
python soatkientruc.py                  # kiến trúc (S1–S10) — ĐỎ là dừng
python -c "import bot, main"            # chết-lúc-khởi-động
python -m unittest discover -s tests -q # lỗi LOGIC: badge sai giống, ё hỏng im lặng, regex nuốt chữ
```

Đỏ bất kỳ cửa nào → **sửa rồi chạy lại**, không được đi tiếp, không được giải thích vòng vo
rằng "lỗi này không liên quan".

## Bước 2 — Soi HÌNH DẠNG diff (`CACHLAM.md` 6c)

User không đọc nổi từng dòng code, nên **bạn phải tự soi hộ** rồi khai. `git diff --stat` +
đối chiếu với mục *Kế hoạch* trong `VIECDANGLAM.md`. Ba dấu hiệu đỏ:

1. **Diff to hơn lời hứa** — có file bị đổi mà kế hoạch không nhắc tới → **khai từng file, vì
   sao**, đừng lặng lẽ nhận.
2. **File mới / hàm mới tên na ná cái cũ** (`get_anki_data` bên cạnh `fetch_anki`…) → trả lời
   thẳng: *vì sao không dùng cái cũ?* Không thuyết phục = wrapper thứ 11 đang chào đời, gỡ đi.
3. **Chạm vùng im lặng mà không có lưới** — thấy `deleteNotes`, `updateNoteFields` hàng loạt,
   đổi model/field mà không có backup, không có bước kiểm sau → **dừng, đi cửa L4**.

Thêm hai thứ chỉ riêng repo này mới có:

- **Script chạy một lần** còn nằm ở thư mục gốc? → chuyển `_daxong/` **ngay trong commit này** (L2).
- **Sửa bug?** → viết thêm **MỘT test** cho đúng bug đó vào `tests/`. Đó là cách nó không quay
  lại lần thứ hai. Không có test = việc chưa xong.

## Bước 3 — Đối chiếu với phiếu việc

Mở `VIECDANGLAM.md`, tick từng dòng ở mục **Coi là XONG khi**. Có dòng chưa tick → nói rõ dòng
nào và vì sao, **đừng báo xong**.

Kiểm luôn mục **CỐ Ý KHÔNG LÀM**: đã lỡ làm thứ nằm trong đó chưa? Lỡ rồi thì khai.

## Bước 4 — Khai ba mục với user (bắt buộc, ngôn ngữ thường)

1. **Đã đổi gì** — từng file, vì sao file đó.
2. **Lệnh nghiệm thu** — đã chạy, kết quả thật (dán output, đừng tóm tắt thành "ổn").
3. **Rủi ro im lặng nào có thể có** — mục quý nhất: thứ hỏng mà **không ai được báo**.
   Không nghĩ ra thì nói "không thấy", đừng bỏ trống.

## Bước 5 — Đóng sổ

- Có rẽ nhánh → thêm mục `QD-nn` 4 dòng vào `QUYETDINH.md`, commit nhắc số hiệu.
- Nợ mới (file >400 dòng, hàm >5 tham số…) → một dòng vào `SONO.md`.
- User **cảm nhận được** thay đổi (nút mới, lỗi họ từng gặp đã hết, thẻ hiện khác đi)?
  → thêm mục `vX.Y.Z` vào `PHIENBAN.md`, ≤5 gạch đầu dòng, **không thuật ngữ** (QD-07).
  Dọn code / đổi cấu trúc / thêm cửa soát thì **KHÔNG ghi** — user không thấy chúng.
- **Commit NGAY, không hỏi user** (QD-10): dòng tiêu đề + **phần thân khai VÌ SAO** (S9 chặn deploy
  nếu thiếu thân). Commit chỉ ghi vào máy — cửa thật là `deploy.ps1`, nên đừng chờ xin phép.
- **Xoá sạch nội dung `VIECDANGLAM.md`**, để lại đúng dòng tiêu đề — phiếu đã dùng xong.

Rồi nhắc user: *"chạy `.\deploy.ps1` để đẩy lên VPS"*. **Đừng tự chạy deploy.**
