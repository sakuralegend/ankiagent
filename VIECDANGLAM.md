# 🎯 VIỆC ĐANG LÀM

## Vá: dọn xong mà AnkiWeb chưa nhận, bot vẫn báo "đã đẩy lên" (QD-34)

Kế hoạch user duyệt 06/08. Nguyên nhân ĐÃ ĐO TAY: `changeDeck` ghi thẳng SQL nên đồng hồ kho
không nhích, sync thoát ngay — cơ chế đầy đủ ở docstring `anki_client.cham_vao_kho()`, đừng
chép lại chỗ khác.
Đã xong: cú chạm + `_kiem_da_len_ankiweb` ba số + job đêm xét `chua_gui` + 8 test.
Còn: khai `ANKI_COLLECTION` vào `.env` trên VPS (thiếu dòng này thì cửa canh im), rồi deploy.
Nghiệm thu: `soatkientruc.py` · `import bot, main` · `unittest discover -s tests` · gõ `/don`.
Việc bị đẩy khỏi phiếu: chạy lô **k43** — pointer ở `data/huongdan/kho/TIEPTUC.md`.
