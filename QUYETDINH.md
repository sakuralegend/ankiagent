# 📌 QUYẾT ĐỊNH KỸ THUẬT (`QD-nn`)

> **Một quyết định = MỘT dòng bảng, trần 250 ký tự** (số ở `soat_nguong.json`, cửa **S15** đếm thật).
> Mới nhất TRÊN CÙNG. Commit thi hành thì nhắc số hiệu, ví dụ `(QD-01)`.
> Toàn văn bàn bạc: `git log --grep QD-nn` (đo 04/08: 265 commit, thân trung bình 928 ký tự — dày
> thật, tra được — và **đó chính là kho lưu trữ**). Đây chỉ là **mục lục của phần còn sống**.
>
> ♻️ **SINH PHẢI BẰNG TỬ (QD-29) — luật quan trọng nhất ở đây.** Sổ có **sức chứa CỐ ĐỊNH**, cửa
> **S20** đếm thật. Muốn thêm một dòng thì phải **bỏ một dòng**, và bỏ thì rẻ: đẩy nguyên văn sang
> `git log` (thân commit dài gấp 6–16 lần dòng bảng), `git log --grep QD-nn` vẫn ra, **không mất gì**.
> 🔴 **CẤM nén chữ để nhét thêm.** Nén là cắt phần *vì sao* — thứ duy nhất còn dùng được khi gặp
> tình huống mới. Chạm trần nghĩa là **đến lúc cho một mục chết**, không phải đến lúc viết ngắn lại.
>
> ⚰️ **KHI NÀO MỘT MỤC CHẾT — hỏi một câu có đáp án đúng/sai.** *"Tình huống nào người ta cần biết
> điều này? Trong tình huống đó họ CHẮC CHẮN đã đang mở file nào / chạy lệnh nào / đọc lời báo lỗi
> nào?"* · **Có một chỗ như thế** ⇒ chép lý do vào đúng chỗ đó (docstring · comment · lời báo lỗi
> của cửa soát), rồi cho dòng chết. · **Không có — phải BIẾT TRƯỚC mới nghĩ ra đi tra**
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
> Bảng có trần (`soat_nguong.json`, cửa **S20**) và đã CHẠM trần 01/09. Thêm dòng ⇒ phải
> giết một dòng, và **giết dòng có ngày đo CŨ NHẤT** — đó là dòng dễ đã thối rữa nhất.
> Vì sao mỗi dòng phải đóng dấu ngày: bảng từng có **7/14 dòng không ngày** (vá 01/09),
> mà số không ngày thì không ai biết nó hết hạn chưa.

| Hướng nghe hợp lý | Phán quyết | Vì (số liệu thật) |
|---|---|---|
| Dựng sync server riêng bỏ AnkiWeb | **BÁC — user chốt** | Sập 26/08/2026: 3,5h, 0 thẻ mất (bot dồn trên VPS, đẩy sau). Đổi server = full sync 2 CHIỀU ⇒ "dựng sẵn, sập thì bật" vô dụng. Chuyển hẳn ⇒ App Store nâng Anki iPhone: sync chết im lặng |
| Cào lại OpenRussian để sửa từ loại 93 thẻ `other` | **BÁC** | Đo 01/09/2026: hỏi lại cả 93 từ thì **74 vẫn trả "other"**, và nó trả SAI 2 từ — `тут` ("ở đây") với `справа` ("bên phải") nó xếp là DANH TỪ. Nguồn không biết thì hỏi lại lần nữa vẫn không biết |
| Sửa field `animate` của nguồn cho đúng (sai ở `ме́неджер`·`о́кунь`·`коза́`·`матрёшка`) | **BÁC** | **Đo 09/08.** Bảng chia thôi đọc nó từ QD-35. Chỗ DUY NHẤT còn đọc là bộ đoán giống, theo chiều NGƯỢC — "đồ vật + đuôi -а" mới dám kết luận giống cái ⇒ sửa thành "sinh vật" là bắt nó im ở 2 từ đang trả lời đúng |
| Dùng `_family()` của OpenRussian để dựng mục "Họ hàng" | **BÁC** | **Đo 31/07.** Nó gộp `groups` (cùng gốc) với `relateds` (đồng nghĩa **khác gốc hẳn**) vào một rổ ⇒ dạy sai từ nguyên. Mục Họ hàng do người soạn tự nghĩ, cố ý không có cửa máy |
| Lọc từ theo tag trình độ A1–C2 của OpenRussian | **BÁC** | **Đo 31/07.** `паспорт`, `яблоко`, `сахар` bị gắn **C1**. Dùng **thứ hạng tần suất** thay thế (top 2500 danh từ ≈ A1→B2) |
| Đối chiếu chéo `nouns.csv` với `grammar_cache.json` để bắt lỗi dữ liệu | **KHÔNG ĐỦ** | **Đo 31/07.** Hai file **cùng thượng nguồn OpenRussian** ⇒ trùng nhau không chứng minh đúng. `фон` sai ở **cả hai**. Cửa duy nhất còn lại là người đọc bằng mắt |
| Forget/Reset thẻ "hoá thạch" (Difficulty kẹt cao, không tự hồi phục) | **HẾT CẦN từ 04/08** — đừng đụng thẻ | Optimize đưa `w7` 0.001→0.0486 (610 lần Good → ~14): hoá thạch **402 → 0** mà không phải sửa thẻ nào. Số: `data/fsrs_moc.json` |
| Suy ra "user đổi cách bấm nút" từ việc tỷ lệ Again giảm | **BÁC** (AI đã suy sai 04/08) | revlog **không chứa** tiêu chí bấm nút; user khai tiêu chí KHÔNG đổi từ đầu (**sai 1 ký tự = Again**) ⇒ mọi số "nhớ được" ở repo là thang **gõ đúng từng ký tự**, đừng đọc như "nhớ nghĩa". Cải thiện thật: **cùng chu kì 1 ngày 49,9% → 66,3%** (nhóm quên ≥6 lần), mà chu kì nhóm đó lại DÀI ra ⇒ không phải "câu hỏi dễ đi". Nguyên nhân không tách bạch được. Phép kiểm giả thuyết user: `scripts/do_fsrs.py --giathuyet` |
| Gộp 4 hàm chuẩn hoá tiếng Nga làm một cho gọn | **CHƯA CẦN** | Đo 1748 từ Nga thật (31/07/2026): **0 bất đồng** ở cả hai cặp hàm cùng mục đích. Rủi ro `ё` tổ hợp có thật về lý thuyết nhưng chưa chạm dữ liệu nào ⇒ **đo lại trước khi gộp**, đừng gộp mò |
| "Lô soạn kho càng to càng lợi" | **ĐÚNG MỘT NỬA** | **Đo 31/07.** Đúng về token, nhưng lý do thứ hai (khối dùng chung gánh nhiều thẻ) **chết rồi** — chuẩn v3 cấm khối dùng chung, đo ra `0%`. Cỡ lô do CHẤT LƯỢNG quyết định: chốt 16–18 từ |
| Dựng "agent soát riêng" để kiểm lô sau khi soạn | **BÁC** | **Đo 31/07.** Lô 22 từ + agent rà lại ≈ **7,9K token/từ**, đắt hơn lô 14 từ tự soát (**7,3K**) mà chưa chắc tốt hơn: người viết biết chỗ mình lăn tăn, người rà phải dựng lại từ đầu |
| Cài bộ "spec-driven-claude-code" (hoặc kit SDLC 12 bước tương tự) vào repo | **BÁC** | Đo 31/07/2026: kit thêm **99 file / 21.852 dòng** luật (repo khi đó 4.033 dòng), **28 file nói C#, 36 nói .NET, chỉ 8 nói Python**, và `.claude/CLAUDE.md` 616 dòng của nó đánh nhau với `CLAUDE.md` ở đây. Đã lấy tinh hoa thành 3 lệnh — xem QD-09 |
| Cho VPS tự động "Download from AnkiWeb" theo lịch cho an toàn | **BÁC — NGUY HIỂM** | **Đo 31/07.** Lệnh đó **ghi đè sạch** collection trên VPS (xoá thẻ bot vừa thêm), và không cứu được gì khi quên sync điện thoại vì dữ liệu ôn lúc đó nằm **trong điện thoại** |
| Nâng Anki trong Docker VPS cho khớp laptop (VPS `25.02.7` · laptop `26.5.0`, đo 04/08) | **BÁC — user chốt ≥2 lần** | *"Docker chạy tốt thì để yên"*. Không phải Anki gốc mà là ảnh của một tác giả GitHub ⇒ đổi thứ không ai bảo hành để lấy **0 lợi**: sync vẫn chạy ở hai đời. Hệ quả: **cấm chép thẳng `collection.anki2`** giữa hai máy |

---

## 🗂️ SỔ QUYẾT ĐỊNH

> 🔴 **CHỈ GHI VÀO ĐÂY QUYẾT ĐỊNH VỀ THỨ **KHÔNG CÓ TRONG CODE** (cửa **S26** canh thật).**
> Trích được `QD-nn` ở một file `.py` nghĩa là **có chỗ cắm lý do** ⇒ cắm vào đó rồi cho dòng sổ
> CHẾT ngay. Số hiệu không mất: `so_hieu_da_biet()` đọc cả `git log`, `git log --grep QD-nn` ra
> nguyên văn dài gấp 6–16 lần dòng bảng. Thứ sổ này giữ được mà không gì thay được, chỉ có hai
> loại: **code ĐÃ XOÁ** (không còn file để cắm — nhưng thử viết TEST "file này phải không tồn
> tại" trước đã) và **thứ nằm ngoài repo** (cấu hình trong Anki, thói quen của user).
>
> 📏 **Đo 01/09/2026 lúc dựng S26 — vì sao phải có lằn ranh này.** Sổ từng bị dọn sạch về **0**
> ngày 09/08, rồi đầy lại **10 dòng trong 23 ngày**, **5 dòng trong một phiên**. Soi ra **8/10
> dòng đã có nhà đầy đủ trong code** (643–2.089 ký tự, gấp 3–8 lần dòng bảng). Thủ phạm là chính
> luật cũ: nó bắt chọn 🔨 hay ⚖️, mà 🔨 **chặn deploy** ⇒ mọi phiên chọn ⚖️ — rẻ cho người viết,
> không đúng cho repo. Kết quả: **10/10 dòng ⚖️, 0 dòng 🔨**. Nhãn không ai thi hành thì không
> phải cơ chế, chỉ là lời hứa; nên nay có cửa đếm thật.
>
> 🔴 **DẤU vẫn giữ** (cửa **S25**): · 🔨 = xây được cửa/test mà CHƯA xây ⇒ việc chưa xong, S25
> kêu ĐỎ. · ⚖️ = đánh đổi người phải tự cân. — = quyết định trước khi có sổ (15/07–29/07), cố ý
> không đánh số vì commit hồi đó không nhắc số.

| QD | Ngày | Quyết định | Vì sao (ngắn) |
|---|---|---|---|
| QD-36 | 23/08 | ⚖️ Gộp 4 preset deck thành **1**, bỏ trần thẻ mới/ngày | Đo 23/08: 3 preset cai quản **0 thẻ**, 21 tham số FSRS + bước học giống hệt. Giá: hết tinh chỉnh riêng `0-quen` (không gõ) vs `1-go` (gõ từng ký tự) |
| — | 22/07 | ⚖️ Bỏ deck lọc "phòng tập", cày thẳng trong inbox bằng **undo** | Deck lọc rút thẻ khỏi inbox nên hai bên lệch nhau; undo hoàn nguyên trọn vẹn cả revlog lẫn lịch |
