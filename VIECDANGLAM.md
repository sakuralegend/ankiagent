# 🎯 VIỆC ĐANG LÀM
> Phiếu bị GHI ĐÈ ở việc kế tiếp. Xong việc thì để trống, chừa đúng dòng tiêu đề.

## Làm sạch câu ví dụ + đổi cách bot đặt câu — ĐANG LÀM (duyệt 03/11/2026)
Số đo đủ: `git log -p VIECDANGLAM.md` (03/11). Gốc lỗi = lời dặn bắt AI làm 6 việc + KHÔNG cổng, không
phải model nhỏ: lời dặn gọn (máy chọn dạng, máy đánh dấu) ⇒ Gemini Lite 39/39 (1,7 s), Sonnet 39/39.
User chốt: bot giữ Gemini Lite · làm sạch thẻ cũ bằng Sonnet `claude -p` trên laptop (Gemini 500 lượt/ngày).
Sau đó: câu điền từ (`ClozeHTML`, full sync). Báo cáo: https://claude.ai/artifact/RJ3QZHRqnYXexXnXnZiskY · Azure: nút 🎤 trong thẻ (`git log --grep Azure`); đang thử thẻ dò micro `_THU_MICRO` — XOÁ nó + media `_thu_micro.js` `_micro.js` `_mic_v*.js` (bản nháp mới nhất = `_mic_v4.js`, chép ra trước khi xoá).

### Kế hoạch (đã duyệt 03/11) — bước 1–2 XONG + deploy (`7391b5e`); bước 3 đang chạy
1–2. XONG (`git log --grep QD-47`): `vi_du.py` máy chọn dạng + cổng; bot dùng nó, đã deploy.
3. Việc ĐỨNG RIÊNG (L4): `scripts/_va_lam_sach_vi_du.py` — máy soát 5 382 câu → Sonnet chấm câu còn lại
   → Sonnet viết lại câu hỏng → cổng → backup + kéo sync → ghi `--apply` + tiếng Yandex câu mới.
   **14:40 03/11** (user chốt Gemini viết, Sonnet chỉ chấm): chấm 1794/1794; 538 câu hỏng; 466 có câu mới (428 Sonnet duyệt, 38 chưa chấm);
   72 câu thiếu = Gemini hết lượt ngày (429) + cổng chặt: giao `рыба` mà Gemini viết `рыбу` (đúng) bị loại, thẻ
   `многие` bị giao `многий` ⇒ đề xuất cổng nhận MỌI dạng của từ (`tat_ca_dang`). Tiếp: `viet`→`cham_moi`→`baocao`
   →user duyệt→`ghi --apply`→script vào `_daxong/`, XOÁ `goi_claude_code`, mốc ai_client 469→438, deploy.
