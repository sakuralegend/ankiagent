# 📌 QUYẾT ĐỊNH KỸ THUẬT (`QD-nn`)

> **Một quyết định = MỘT dòng bảng, trần 250 ký tự** (số ở `soat_nguong.json`, cửa **S15** đếm thật).
> Mới nhất TRÊN CÙNG. Commit thi hành thì nhắc số hiệu, ví dụ `(QD-01)`.
> Toàn văn bàn bạc: `git log --grep QD-nn` (đo 04/08: 265 commit, thân trung bình 928 ký tự — dày
> thật, tra được). Mục đã rời sổ: `QUYETDINH-LUUTRU.md`. Đây chỉ là **mục lục của phần còn sống**.
>
> ♻️ **SINH PHẢI BẰNG TỬ (QD-29) — luật quan trọng nhất ở đây.** Sổ có **sức chứa CỐ ĐỊNH**, cửa
> **S20** đếm thật. Muốn thêm một dòng thì phải **bỏ một dòng**, và bỏ thì rẻ: đẩy nguyên văn sang
> `QUYETDINH-LUUTRU.md`, số hiệu vẫn `grep` ra, **không mất gì**.
> 🔴 **CẤM nén chữ để nhét thêm.** Nén là cắt phần *vì sao* — thứ duy nhất còn dùng được khi gặp
> tình huống mới. Chạm trần nghĩa là **đến lúc cho một mục chết**, không phải đến lúc viết ngắn lại.
>
> ⚰️ **KHI NÀO MỘT MỤC CHẾT — hỏi một câu có đáp án đúng/sai.** *"Tình huống nào người ta cần biết
> điều này? Trong tình huống đó họ CHẮC CHẮN đã đang mở file nào / chạy lệnh nào / đọc lời báo lỗi
> nào?"* · **Có một chỗ như thế** ⇒ chép lý do vào đúng chỗ đó (docstring · comment · lời báo lỗi
> của cửa soát), rồi đẩy dòng sang kho lưu trữ. · **Không có — phải BIẾT TRƯỚC mới nghĩ ra đi tra**
> ⇒ **GIỮ**. Loại duy nhất đáng chiếm chỗ: đánh đổi người phải tự cân lại.
>
> 🔢 **LUẬT SỐ (QD-23).** Con số chỉ được ở lại nếu **đóng dấu ngày đo**. Số **mô tả hiện trạng** thì
> CẤM — *"repo 92 file .py"* thối rữa im lặng (đo 03/08: thật là 128). Số **ràng buộc** ở
> `soat_nguong.json` (QD-21). Điều kiện "hết hạn" **cấm dùng số tuyệt đối** — viết theo trạng thái
> đo được: *"khi hàng đợi hết lô `cho`"*, *"khi 0 thẻ còn tag X"*.

---

## 📏 ĐÃ ĐO RỒI BÁC — đừng làm lại, đã tốn tiền một lần

> Mỗi dòng dưới đây là một hướng **nghe rất hợp lý**, đã thử và **loại bỏ bằng số liệu thật**.
> Đây là loại lỗi đắt nhất: AI phiên sau thấy "chỗ này tối ưu được" rồi làm lại từ đầu.
> **Trước khi "tối ưu" thứ gì trong bảng này, đọc cột Vì.** Muốn lật một dòng: ĐO LẠI ra số khác,
> không lật bằng lập luận suông. 🔴 **Nhưng số đo dùng để BÁC cũng HẾT HẠN** — "88 thẻ thiếu"
> (31/07) đo lại 02/08 ra **0**, và hướng từng bị bác thành hướng thi hành. Việc nay đụng lại một
> dòng ⇒ **đo lại trước**, đừng viện dòng cũ rồi thôi.

| Hướng nghe hợp lý | Phán quyết | Vì (số liệu thật) |
|---|---|---|
| Dùng `_family()` của OpenRussian để dựng mục "Họ hàng" | **BÁC** | Nó gộp `groups` (cùng gốc) với `relateds` (đồng nghĩa **khác gốc hẳn**) vào một rổ ⇒ dạy sai từ nguyên. Mục Họ hàng do người soạn tự nghĩ, cố ý không có cửa máy |
| Lọc từ theo tag trình độ A1–C2 của OpenRussian | **BÁC** | `паспорт`, `яблоко`, `сахар` bị gắn **C1**. Dùng **thứ hạng tần suất** thay thế (top 2500 danh từ ≈ A1→B2) |
| Đối chiếu chéo `nouns.csv` với `grammar_cache.json` để bắt lỗi dữ liệu | **KHÔNG ĐỦ** | Hai file **cùng thượng nguồn OpenRussian** ⇒ trùng nhau không chứng minh đúng. `фон` sai ở **cả hai**. Cửa duy nhất còn lại là người đọc bằng mắt |
| Forget/Reset thẻ "hoá thạch" (Difficulty kẹt cao, không tự hồi phục) | **HẾT CẦN từ 04/08** — đừng đụng thẻ | Optimize đưa `w7` 0.001→0.0486 (610 lần Good → ~14): hoá thạch **402 → 0** mà không phải sửa thẻ nào. Số: `data/fsrs_moc.json` |
| Suy ra "user đổi cách bấm nút" từ việc tỷ lệ Again giảm | **BÁC** (AI đã suy sai 04/08) | revlog **không chứa** tiêu chí bấm nút; user khai tiêu chí KHÔNG đổi từ đầu (**sai 1 ký tự = Again**) ⇒ mọi số "nhớ được" ở repo là thang **gõ đúng từng ký tự**, đừng đọc như "nhớ nghĩa". Cải thiện thật: **cùng chu kì 1 ngày 49,9% → 66,3%** (nhóm quên ≥6 lần), mà chu kì nhóm đó lại DÀI ra ⇒ không phải "câu hỏi dễ đi". Nguyên nhân không tách bạch được. Phép kiểm giả thuyết user: `scripts/do_fsrs.py --giathuyet` |
| Gộp 4 hàm chuẩn hoá tiếng Nga làm một cho gọn | **CHƯA CẦN** | Đo 1748 từ Nga thật (31/07/2026): **0 bất đồng** ở cả hai cặp hàm cùng mục đích. Rủi ro `ё` tổ hợp có thật về lý thuyết nhưng chưa chạm dữ liệu nào ⇒ **đo lại trước khi gộp**, đừng gộp mò |
| "Lô soạn kho càng to càng lợi" | **ĐÚNG MỘT NỬA** | Đúng về token, nhưng lý do thứ hai (khối dùng chung gánh nhiều thẻ) **chết rồi** — chuẩn v3 cấm khối dùng chung, đo ra `0%`. Cỡ lô do CHẤT LƯỢNG quyết định: chốt 16–18 từ |
| Dựng "agent soát riêng" để kiểm lô sau khi soạn | **BÁC** | Lô 22 từ + agent rà lại ≈ **7,9K token/từ**, đắt hơn lô 14 từ tự soát (**7,3K**) mà chưa chắc tốt hơn: người viết biết chỗ mình lăn tăn, người rà phải dựng lại từ đầu |
| Cài bộ "spec-driven-claude-code" (hoặc kit SDLC 12 bước tương tự) vào repo | **BÁC** | Đo 31/07/2026: kit thêm **99 file / 21.852 dòng** luật (repo khi đó 4.033 dòng), **28 file nói C#, 36 nói .NET, chỉ 8 nói Python**, và `.claude/CLAUDE.md` 616 dòng của nó đánh nhau với `CLAUDE.md` ở đây. Đã lấy tinh hoa thành 3 lệnh — xem QD-09 |
| Cho VPS tự động "Download from AnkiWeb" theo lịch cho an toàn | **BÁC — NGUY HIỂM** | Lệnh đó **ghi đè sạch** collection trên VPS (xoá thẻ bot vừa thêm), và không cứu được gì khi quên sync điện thoại vì dữ liệu ôn lúc đó nằm **trong điện thoại** |
| Nâng Anki trong Docker VPS cho khớp laptop (VPS `25.02.7` · laptop `26.5.0`, đo 04/08) | **BÁC — user chốt ≥2 lần** | *"Docker chạy tốt thì để yên"*. Không phải Anki gốc mà là ảnh của một tác giả GitHub ⇒ đổi thứ không ai bảo hành để lấy **0 lợi**: sync vẫn chạy ở hai đời. Hệ quả: **cấm chép thẳng `collection.anki2`** giữa hai máy |

---

## 🗂️ SỔ QUYẾT ĐỊNH

> Chỉ còn mục **không có nhà nào khác** — mọi mục đã có cửa soát canh, đã thành sự thật trong cây
> code, hoặc đã có lý do nằm sẵn trong docstring đều ở `QUYETDINH-LUUTRU.md`.
> — = quyết định trước khi có sổ (15/07–29/07), **cố ý không đánh số**: commit hồi đó không nhắc số
> nên `git log --grep` ra rỗng, đánh số là đẻ ra lời hứa sai.

| QD | Ngày | Quyết định | Vì sao (ngắn) |
|---|---|---|---|
| QD-29 | 04/08 | **Sinh = tử.** Sổ có sức chứa CỐ ĐỊNH (S20 đếm); mục rời sổ về `QUYETDINH-LUUTRU.md`, ngoài ngân sách đọc | Vế sinh đã tự động, vế chết phó mặc ý chí ⇒ phình mãi. Trần ký tự không tạo tỷ lệ chết, chỉ bắt nén — nén thì mất *vì sao* |
| QD-30 | 04/08 | Ngân sách đọc chia HAI TẦNG: `batbuoc` (nạp tự động, trần TỔNG chặt) tách khỏi tra-khi-cần | Đo 04/08: **không máy nào bắt đọc 14/16 file** — chỉ `CLAUDE.md` nạp tự động. Tổng cũ đo thứ chưa chắc xảy ra, mà đau nén chữ thì thật |
| QD-15 | 02/08 | Cửa canh DỮ LIỆU ngữ pháp `anki_tools/soat_nguphap.py` đứng riêng, KHÔNG import `grammar` | Tránh đẻ vòng import. Cửa đòi lệch cả hai chiều mới báo ⇒ đo 516 thẻ ra 0 kêu oan. Chỉ IN RA, không tự sửa |
| QD-04 | 31/07 | Cảnh báo "bot chết" gọi thẳng Telegram bằng `curl`, KHÔNG qua `tgbot/alerts.py` | `alerts.py` gửi qua chính con bot ⇒ bot chết thì cảnh báo chết theo. Đường báo không được nạp dòng Python nào của dự án |
| QD-01 | 30/07 | Nhận hệ CACHLAM v1 + `CLAUDE.md`; wrapper riêng của `data/huongdan/kho/` đóng băng làm ngoại lệ L1 | 🔴 Hết hạn khi hàng đợi hết lô `cho`. Đã bị nới ba lần (QD-11/16/19) ⇒ gần như đã chết, giữ để chặn viết wrapper mới |
| — | 29/07 | Gom 3 luồng chạy nền của bot về một hàm `core.chay_hang_loat()` | Ba bản sao lệch nhau âm thầm; nguyên tắc user chốt: **một chức năng một script**, trùng thì tách tầng chứ đừng đồng bộ tay |
| — | 26/07 | Gỡ sạch trần thẻ mới (`new/perDay = 9999` cả 3 preset) | User: *"học đến bao giờ hết thì thôi"*. 🔴 Hằng số nguồn ở **`scripts/setup_inbox.py`** — script này **ghi đè GUI mỗi lần chạy**, chỉnh tay trong Anki là vô ích |
| — | 22/07 | Gợi ý (hint) dựng bằng **JS trong mặt trước thẻ**, KHÔNG thêm card template | Chỉ card template mới nhân đôi số thẻ — thêm template là tự nhân đôi cả bộ sưu tập |
| — | 22/07 | Bỏ deck lọc "phòng tập", cày thẳng trong inbox bằng **undo** | Deck lọc rút thẻ khỏi inbox nên hai bên lệch nhau; undo hoàn nguyên trọn vẹn cả revlog lẫn lịch |
| — | 21/07 | Gõ từ **đã có thẻ** ⇒ trả nguyên mục từ điển, không báo "trùng" suông | Kéo theo ràng buộc vĩnh viễn: mỗi hàm dựng HTML phải có **hàm nghịch** đọc ngược; đổi HTML mà quên sửa hàm nghịch ⇒ bảng tra hiện **trống rỗng** |
| — | 21/07 | **pymorphy3 offline làm trọng tài** đưa từ Nga về dạng từ điển; AI chỉ lo đọc ảnh | Lemma là việc **tất định**, không nên đoán bằng AI. `reconcile_lemma` có 4 luật giữ phần AI đúng — 🔴 đừng "đơn giản hoá" thành *từ điển luôn thắng* |
| — | 20/07 | Thẻ ngữ pháp tách hẳn thành mảng `grammar_forms/`, phụ thuộc **một chiều** vào `anki_tools` | User: *"ít ảnh hưởng đến deck RUSSIAN đang chạy ngon"* — ưu tiên tuyệt đối là không làm hỏng thứ đang chạy |
| — | 20/07 | Bot **tự tải bytes** audio rồi `storeMediaFile`, không để AnkiConnect tải hộ qua URL | OpenRussian trả 500 thì AnkiConnect ghi **nguyên câu lỗi** vào ô Audio ⇒ thẻ hỏng nhận ra bằng *thiếu `[sound:]`*, KHÔNG phải ô rỗng |
| — | 20/07 | `/sua` = **làm lại thẻ hoàn toàn** (cào + sinh lại), xoá hẳn cơ chế "preset tinh chỉnh" cũ | Preset gần như không ai dùng; làm lại dùng chung `build_card_fields` với thêm thẻ mới nên **một chức năng một lõi** |
| — | 19/07 | Nới toàn cục timeout Telegram (connect 15 / read 30 / media 60) | VPS VN → `api.telegram.org` **~230ms RTT**, trần mặc định 5s làm luồng gửi ảnh chết ngay câu trả lời đầu |
| — | 19/07 | `bot.py` chỉ còn ~10 dòng điểm vào, ruột tách vào gói `tgbot/` 4 tầng | Tầng một chiều `core ← flows ← dispatch ← app`; **`dispatch` chỉ chia việc**, cấm để logic nghiệp vụ vào đó (S3 canh) |
