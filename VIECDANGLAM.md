# 🎯 VIỆC ĐANG LÀM

> Phiếu bị GHI ĐÈ ở việc kế tiếp. Xong phiên: để TRỐNG hoặc chừa đúng MỘT đầu
> việc (cửa **S19**, QD-25). Việc chưa tới lượt ⇒ `SONO.md` kèm HẠN XOÁ.

## Thay cây chủ đề bằng chuẩn ТРКИ — cửa 1+2 xong 23/08/2026

**Một câu:** thay 19 chủ đề tự nghĩ trong `anki_tools/topics.py` bằng 35 nhánh dựng theo chuẩn ТРКИ (ros-edu.ru), giữ 10 gốc cũ, rồi để AI xếp lại tag cho 1212 thẻ.
**Đo 23/08 (lý do làm):** độ tinh khiết `concepts::abstract` 19% · `concepts::misc` 28% · `people::family` 30% · `places::city` 33% — bốn rọ ôm 335 thẻ. Thủ phạm là ĐỊNH NGHĨA (`misc` = *"fallback when nothing above fits"*), không phải AI gắn ẩu.
**User đã chốt:** tên nhánh giữ TIẾNG ANH · từ nguồn CHỈ lấy danh sách + trình độ, chủ đề tự phân loại hết.
**Coi là XONG khi:** hết deck `concepts::misc` · `автобус` ở `places::transport`, `американец` ở `people::nation`, `мама` cùng chỗ `папа` · `/thongke` ra 0 thẻ chưa tag · lịch ôn FSRS không đổi.
**CỐ Ý KHÔNG làm:** chưa chẻ 4 nhánh quá 100 thẻ (to vì định nghĩa rộng, khác thùng rác) · chưa lấy ô ghi chú ngữ pháp của nguồn · lệnh bot xin 10 từ = việc SAU (`SONO.md`).

### Kế hoạch (đã duyệt 23/08/2026)
1. `data/rosedu_muc.json` = 4361 từ + mức (QD-A: ảnh chụp, không cào lúc chạy). 🔴 Nhãn chủ đề của nguồn ĐÃ THỬ RỒI BỎ — 6/16 cặp từ đối nhau bị tách (`папа` ở "Семья" mà `мама` ở "Жизнь человека").
2. `topics.py`: 35 nhánh/10 gốc · **QD-B: bỏ `FALLBACK_TOPIC`**, không xếp được thì để TRỐNG tag.
3. `call_claude_topic` nhận CẢ LÔ 25 từ (≈49 lượt thay vì 1212) · `tag_topics.py` bỏ bảng chép tay.
4. `/backup` → `tag_topics.py --fix` nháp → `--apply` → `build_subdecks.py` nháp → `--apply`.
**Nghiệm thu:** 3 cửa L3 · `/thongke` 0 thẻ chưa tag · 4 test mới.
