# 🎯 VIỆC ĐANG LÀM — phiên soạn kho 02/08/2026
> Phiếu này bị GHI ĐÈ ở việc kế tiếp. Xong việc thì xoá nội dung, để lại đúng dòng tiêu đề.

**Chạy 5 lô: k17(14) · k18(8) · k19(14) · k20(17) · k21(21) = 74 từ** (ngân sách phiên ~80 từ).
`moi` báo không có từ mới (976 thẻ đều đã trong hàng đợi) ⇒ lấy thẳng 5 lô đầu hàng chờ.
Mốc vào phiên: **18/61 lô · 260/976 từ duyệt · nap 18/18**.

- [x] 5 agent phụ đã giao, mỗi lô một context trắng. Luồng chính **đứng im chờ**, không soạn chữ nào.
- [ ] Mỗi lô báo xong → luồng chính chạy lại `soat` + `dodai` (đừng tin báo cáo suông) → ghi
      một dòng `dolo.tsv` → `xong kNN` → `nap --apply` → đối chiếu "ghi vào N note" với số từ.
- [ ] Commit sau mỗi lô nạp xong (QD-10: 3 cửa xanh thì tự commit, không hỏi).
- [ ] Cập nhật `data/huongdan/kho/TIEPTUC.md` phần đầu: mốc mới + bài học của phiên.

✅ **Đã kiểm đầu phiên:** AnkiConnect sống (version 6); `tiep k17` chạy tốt sau QD-11 —
công cụ nay in `[grammar] lay 976 tu tu THE ANKI vao bo dem`, tức đã đọc thẳng `GrammarJSON`,
không còn `grammar_cache.json`.
