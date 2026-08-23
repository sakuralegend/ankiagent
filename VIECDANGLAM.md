# 🎯 VIỆC ĐANG LÀM

> Phiếu bị GHI ĐÈ ở việc kế tiếp. Xong phiên: để TRỐNG hoặc chừa đúng MỘT đầu
> việc (cửa **S19**, QD-25). Việc chưa tới lượt ⇒ `SONO.md` kèm HẠN XOÁ.

## Thay cây chủ đề bằng chuẩn ТРКИ — cửa 1 xong 23/08/2026, chờ duyệt kế hoạch

**Một câu:** thay 19 chủ đề tự nghĩ trong `anki_tools/topics.py` bằng 33 nhánh gom từ 34 chủ đề chuẩn ТРКИ (ros-edu.ru), giữ nguyên 10 gốc cố định, rồi gắn tag lại 1212 thẻ — để mỗi chủ đề có ĐỊNH NGHĨA thay vì có thùng rác.
**Đo 23/08 (lý do làm):** độ tinh khiết `concepts::abstract` 19% · `concepts::misc` 28% · `people::family` 30% · `places::city` 33% — bốn rọ ôm 335 thẻ. Thủ phạm là ĐỊNH NGHĨA (`misc` = *"fallback when nothing above fits"*, `places::city` = *"...cities, transport, roads"*), không phải AI gắn ẩu.
**User đã chốt:** tên nhánh GIỮ TIẾNG ANH · 275 từ ngoài chuẩn nhờ AI xếp vào cây mới
**Coi là XONG khi:** trong Anki không còn deck `concepts::misc` · `автобус` nằm ở `places::transport`, `американец` ở `people::nation` · `/thongke` ra 33 nhánh dưới 10 gốc cũ, 0 thẻ mất tag, lịch ôn FSRS không đổi
**CỐ Ý KHÔNG làm:** chưa chẻ 4 nhánh quá 100 thẻ (`actions` 237 · `qualities` 137 · `time` 127 · `language::education` 121 — to vì định nghĩa rộng, khác thùng rác) · chưa lấy ô ghi chú ngữ pháp của nguồn vào thẻ · lệnh bot xin 10 từ = việc SAU (`SONO.md`)
**Đã đo:** "ĐÃ ĐO RỒI BÁC" có dòng bác tag trình độ **OpenRussian** (`паспорт`·`яблоко`·`сахар` gắn nhầm C1) — đo lại 23/08 trên ros-edu: cả ba ra **A1** ⇒ dòng đó không phủ nguồn mới · hàm gần giống ĐÃ CÓ, dùng lại: `scripts/tag_topics.py --fix` + `scripts/build_subdecks.py`
