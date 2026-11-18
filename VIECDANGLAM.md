# 🎯 VIỆC ĐANG LÀM
> Phiếu bị GHI ĐÈ ở việc kế tiếp. Xong việc thì để trống, chừa đúng dòng tiêu đề.

## Thêm 100 từ B1 đầu tiên của `data/sach_b2.json` — KHÔNG Google, toàn Opus (user 18/11/2026)
User chốt 18/11: mọi đợt sách B2 bỏ Google (nghĩa Việt, câu ví dụ, chủ đề, xếp lô) → Opus,
GỘP CẢ LÔ một lượt `claude -p` (đo: 6,7K token/lượt cố định ⇒ từng từ một lượt đắt ~17×).
GIỮ OpenRussian (bảng chia) + Yandex (tiếng). Bot VPS vẫn Google. **Bị dừng ở đâu: chạy
`PYTHONIOENCODING=utf-8 python data/huongdan/kho/xephangdoi.py` — nó in bước kế tiếp.**
- [x] 1. công cụ đợt chạy lại được (`d6e5747`)
- [x] 2. cửa Opus trong `ai_client` + `xephangdoi` gọi Opus thay Google · test · commit
- [ ] 3. `chon 100 --apply` · `taothe --apply` · commit
- [ ] 4. soạn lô theo `lo.md` §1 bước 3–8, lô ĐẦU trước · commit
