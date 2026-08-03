# 📌 QUYẾT ĐỊNH KỸ THUẬT (`QD-nn`)

> **Một quyết định = MỘT dòng bảng, trần 250 ký tự** (số ở `soat_nguong.json`, cửa **S15** đếm thật).
> Mới nhất TRÊN CÙNG. Commit thi hành thì nhắc số hiệu, ví dụ `(QD-01)`.
> Muốn biết đầy đủ vì sao: `git log --grep QD-nn` — toàn văn bản dài nằm nguyên trong lịch sử git,
> đây chỉ là **mục lục**. Chỉ ghi khi RẼ NHÁNH (4 cửa ở `CACHLAM.md` Q5); việc thường thì `git log` lo.
>
> 🔢 **LUẬT SỐ (QD-23).** Con số chỉ được ở lại nếu **đóng dấu ngày đo**: *"Đo 02/08: 23/25 thẻ sai
> mặt"* nói về một phép đo đã xong nên không bao giờ cũ. Số **mô tả hiện trạng** thì CẤM — *"repo 92
> file .py"* thối rữa im lặng (đo 03/08: thật là 128), và sổ này đã phải tự đính chính *"61 lô → 64"*.
> Số **ràng buộc** thì không nằm ở đây: chúng ở `soat_nguong.json` (QD-21).
> Điều kiện "hết hạn" **cấm dùng con số tuyệt đối** — viết theo trạng thái đo được:
> *"khi hàng đợi hết lô `cho`"*, *"khi 0 thẻ còn tag X"*.
>
> ⚰️ **KHI NÀO MỘT MỤC CHẾT.** Đừng cân "cái nào quan trọng hơn" — không ai xếp được. Hỏi đúng một
> câu **có đáp án đúng/sai**: *"Có máy nào bắt được tôi nếu tôi phá luật này mà KHÔNG đọc file này
> không?"* · **Có** (cửa soát / test / hook) ⇒ đánh dấu ⚰️, lý do sống trong lời báo lỗi của chính
> cửa đó. · **Không, nhưng đã thành sự thật trong code** ⇒ ⚰️. · **Không, và vẫn là đánh đổi người
> phải tự cân lại** ⇒ **GIỮ**. Loại duy nhất đáng chiếm chỗ.

---

## 📏 ĐÃ ĐO RỒI BÁC — đừng làm lại, đã tốn tiền một lần

> Mỗi dòng dưới đây là một hướng **nghe rất hợp lý**, đã có người (hoặc AI) thử, **đo bằng số liệu
> thật rồi loại bỏ**. Đây là loại lỗi đắt nhất: AI phiên sau đọc code thấy "chỗ này tối ưu được"
> rồi làm lại từ đầu. **Trước khi "tối ưu" bất cứ thứ gì trong bảng này, đọc cột Vì.**
> Muốn lật một dòng: phải ĐO LẠI ra số khác, không được lật bằng lập luận suông.
> 🔴 **Nhưng số đo dùng để BÁC cũng HẾT HẠN.** "88 thẻ thiếu" (31/07) đo lại 02/08 ra **0**, và
> chính hướng từng bị bác trở thành hướng thi hành. Dòng nào chống lưng bằng số đo cũ mà việc nay
> đụng lại nó ⇒ **đo lại trước**, đừng viện dòng cũ rồi thôi.

| Hướng nghe hợp lý | Phán quyết | Vì (số liệu thật) |
|---|---|---|
| Dùng `_family()` của OpenRussian để dựng mục "Họ hàng" | **BÁC** | Nó gộp `groups` (cùng gốc) với `relateds` (đồng nghĩa **khác gốc hẳn**) vào một rổ ⇒ dạy sai từ nguyên. Mục Họ hàng do người soạn tự nghĩ, cố ý không có cửa máy |
| Lọc từ theo tag trình độ A1–C2 của OpenRussian | **BÁC** | `паспорт`, `яблоко`, `сахар` bị gắn **C1**. Dùng **thứ hạng tần suất** thay thế (top 2500 danh từ ≈ A1→B2) |
| Đối chiếu chéo `nouns.csv` với `grammar_cache.json` để bắt lỗi dữ liệu | **KHÔNG ĐỦ** | Hai file **cùng thượng nguồn OpenRussian** ⇒ trùng nhau không chứng minh đúng. `фон` sai ở **cả hai**. Cửa duy nhất còn lại là người đọc bằng mắt |
| Chờ Difficulty của thẻ tự hồi phục khi trả lời Good | **HẾT HẠN 04/08** — đo lại ra số khác | Đo 25/07 (`w7=0.001`): **610 lần** Good mới về 50%, **0/84 thẻ** hồi phục. Sau Optimize 04/08 (`w7=0.0486`, ~14 lần): hoá thạch **402 → 0**, **77%** trong 675 thẻ từng quên ≥3 lần đang có chuỗi ≥3 lượt đúng ⇒ hết cần Forget/Reset. Số: `data/fsrs_moc.json` |
| Suy ra "user đổi cách bấm nút" từ việc tỷ lệ Again giảm | **BÁC** (AI đã suy sai 04/08) | revlog **không chứa** tiêu chí bấm nút. User khai tiêu chí KHÔNG đổi từ đầu: **sai 1 ký tự = Again**, Hard chỉ dành cho "đúng mà khựng" ⇒ mọi con số "nhớ được" ở repo này là thang **gõ đúng từng ký tự**, đừng đọc như "nhớ nghĩa". Cải thiện thật nằm ở **cùng chu kì 1 ngày: 49,9% → 66,3%** (nhóm quên ≥6 lần), trong khi chu kì ≥2 ngày đi ngang/xấu đi; chu kì nhóm đó lại DÀI ra (1→2 ngày) nên không phải "câu hỏi dễ đi". Nguyên nhân (GĐ0 · nội dung hướng dẫn · thêm vài tuần học) **không tách bạch được** — mọi cách chia nhóm đều lẫn với độ chín của thẻ. 🔎 User nêu giả thuyết *"qua 2–3 chu kì ngắn thì từ mới thấm, thấm rồi nhớ lâu"* — CHƯA đủ dữ liệu; phép kiểm + ngưỡng phán đã cắm sẵn: `python scripts/do_fsrs.py --giathuyet` |
| Gộp 4 hàm chuẩn hoá tiếng Nga làm một cho gọn | **CHƯA CẦN** | Đo 1748 từ Nga thật (31/07/2026): **0 bất đồng** ở cả hai cặp hàm cùng mục đích. Rủi ro `ё` tổ hợp có thật về lý thuyết nhưng chưa chạm dữ liệu nào ⇒ **đo lại trước khi gộp**, đừng gộp mò |
| "Lô soạn kho càng to càng lợi" | **ĐÚNG MỘT NỬA** | Đúng về token, nhưng lý do thứ hai (khối dùng chung gánh nhiều thẻ) **chết rồi** — chuẩn v3 cấm khối dùng chung, đo ra `0%`. Cỡ lô do CHẤT LƯỢNG quyết định: chốt 16–18 từ |
| Dựng "agent soát riêng" để kiểm lô sau khi soạn | **BÁC** | Lô 22 từ + agent rà lại ≈ **7,9K token/từ**, đắt hơn lô 14 từ tự soát (**7,3K**) mà chưa chắc tốt hơn: người viết biết chỗ mình lăn tăn, người rà phải dựng lại từ đầu |
| Cài bộ "spec-driven-claude-code" (hoặc kit SDLC 12 bước tương tự) vào repo | **BÁC** | Đo 31/07/2026: kit thêm **99 file / 21.852 dòng** luật (toàn repo khi đó 4.033 dòng), **28 file nói C#, 36 nói .NET, chỉ 8 nói Python**; `.claude/CLAUDE.md` 616 dòng của nó **đánh nhau** với `CLAUDE.md` 4-mảng ở đây, và cửa TDD ≥80% khoá cứng repo 92 file .py / 1 test. Đã lấy tinh hoa thành 3 lệnh — xem QD-09 |
| Cho VPS tự động "Download from AnkiWeb" theo lịch cho an toàn | **BÁC — NGUY HIỂM** | Lệnh đó **ghi đè sạch** collection trên VPS (xoá thẻ bot vừa thêm), và không cứu được gì khi quên sync điện thoại vì dữ liệu ôn lúc đó nằm **trong điện thoại** |

---

## 🗂️ SỔ QUYẾT ĐỊNH

> ⚰️ = đã chết hoặc đã thi hành xong, giữ số hiệu vì code/test/tài liệu còn trỏ tới.
> — = quyết định trước khi có sổ (15/07–29/07), **cố ý không đánh số**: commit hồi đó không nhắc số
> nào nên `git log --grep` sẽ ra rỗng, đánh số là đẻ ra một lời hứa sai.

| QD | Ngày | Quyết định | Vì sao (ngắn) |
|---|---|---|---|
| QD-25 | 03/08 | Luật "mọi `except` phải log hoặc khai lý do" thành cửa **S17** có ratchet, thay vì chỉ nằm trong sổ nợ | Đo 03/08: sổ ghi "15 chỗ", đếm thật ra **8** — luật bằng chữ vừa trôi vừa mang số cũ. Mốc 8 chốt vào baseline, chỉ cho GIẢM |
| QD-24 | 03/08 | Sổ nợ chỉ chứa nợ CHƯA trả — trả xong là XOÁ dòng, bài học dời sang nơi được đọc (S16 canh); mọi `.md` trong git đều có trần | Đo 03/08: xác nợ chiếm **67%** `SONO.md`, và làm hỏng luôn ngòi "chạm 10 mục" vì nó đếm cả xác |
| QD-23 | 03/08 | Sổ thành MỘT bảng, mỗi quyết định một dòng ≤250 ký tự; số không có ngày đo thì cấm ở lại | Đo 03/08: 40 câu chứa số, 3 câu sai ngay hôm đó; sổ phải tự đính chính "61 lô→64". Cửa S15 đếm thật |
| QD-22 | 03/08 | Tách ruột `soatkientruc.py` vào gói `soat/`, giữ tên điểm vào | Chạm trần 700 dòng. QD-02 chỉ đòi stdlib · không import module dự án · gõ được tên cũ. 🔴 Test trỏ gốc qua `khung.dat_goc()`, sai là test soi repo thật rồi xanh giả |
| QD-21 | 03/08 | Mọi CON SỐ TRẦN về `soat_nguong.json`, tài liệu chỉ trỏ; S12–S14 canh | Bản sao thì sớm muộn lệch, nguồn thì bất khả. 🔴 Số trong QD cũ là LỊCH SỬ — số hiệu lực chỉ ở `soat_nguong.json` |
| ⚰️ QD-20 | 03/08 | Trần đọc đo bằng KÝ TỰ, không bằng dòng — S10 canh | Ký tự/dòng chạy từ 49 tới 140 tuỳ file ⇒ đếm dòng bỏ lọt hẳn file nặng 30 KB. Đừng "dọn" ngược về đếm dòng |
| QD-19 | 03/08 | Tách `grammar.py` thành 4 mảnh lá; `grammar.py` làm MẶT TIỀN re-export đủ tên cũ kể cả private | Caller và test không đổi một dòng. Nghiệm thu bằng "file vàng": chạy trên từ thật, diff phải = 0. `soat_nguphap.py` vẫn để RIÊNG |
| ⚰️ QD-18 | 03/08 | Tách 6 file quá trần theo khuôn "file vàng" — đã xong | Khuôn còn dùng cho mọi refactor sau: chạy hàm chỉ-đọc trên dữ liệu thật + so ast từng hàm, diff ≠ 0 là hoàn tác. `dispatch.py` cố ý KHÔNG tách |
| QD-17 | 03/08 | Cửa canh thẻ sai mặt bám đuôi nhịp sync 30′, gọi lại lõi `thang_cap_gd2()` | Chỉ chạy khi nhịp đó kéo về THÀNH CÔNG. 🔴 `forgetCards` là MỤC ĐÍCH của GĐ2, không phải tác dụng phụ — đừng "giữ tiến độ ôn cho lành" |
| QD-16 | 02/08 | Ghi hàng loạt lên note thì kéo sync về TRƯỚC; kéo hỏng thì DỪNG | Sync xử xung đột "ai sửa sau thắng TRỌN note" ⇒ bản cũ đè bản mới. Đổi deck sống sót vì nó nằm trên THẺ ⇒ thẻ đúng deck, sai mặt, không lỗi nào bật |
| QD-15 | 02/08 | Cửa canh DỮ LIỆU ngữ pháp `anki_tools/soat_nguphap.py` đứng riêng, KHÔNG import `grammar` | Tránh đẻ vòng import. Cửa đòi lệch cả hai chiều mới báo ⇒ đo 516 thẻ ra 0 kêu oan. Chỉ IN RA, không tự sửa |
| ⚰️ QD-14 | 02/08 | Xoá hẳn `CHANGELOG.md` khỏi cây làm việc — file không còn tồn tại | Lịch sử về `git log` (QD-06) |
| ⚰️ QD-13 | 01/08 | Hook nhắc luật phải có cửa canh — S11 chạy THẬT lệnh hook mỗi lần soát | Kiểu chết hay gặp là `python` không có trên PATH: cửa chỉ nhìn tên file sẽ báo XANH trên đúng cái máy hook đang chết |
| QD-12 | 01/08 | Quyết định nào ĐỔI CODE thì ghi vết NGAY, dạng NGẮN; muốn sâu thì tra `git log` | Đo 01/08: cả hai tuần đầu dựng bot không để lại vết nào, dù đổi code nhiều nhất. NGẮN là thứ chặn sổ đi lại đường `CHANGELOG.md` |
| QD-11 | 31/07 | Bỏ hẳn `grammar_cache.json`, ô `GrammarJSON` trong thẻ là nguồn DUY NHẤT | Một nguồn thì không lệch được; hai bản giống hệt sớm muộn SẼ lệch âm thầm (89 thẻ lệch nhiều tuần). Anki đóng thì kêu to rồi DỪNG, cấm trả rỗng |
| QD-10 | 31/07 | AI TỰ commit khi việc xong + ba cửa xanh, không hỏi user | Luật cũ chỉ nói commit VIẾT THẾ NÀO, không nói KHI NÀO ⇒ việc nhớ rơi vào user. `commit` không đẩy đi đâu, cửa thật là `deploy.ps1` |
| QD-09 | 31/07 | Ba playbook `/ycau`→`/kehoach`→`/nghiemthu` + phiếu `VIECDANGLAM.md`, AI TỰ kích hoạt qua hook | Kit SDLC 12 bước quá nặng (số ở bảng trên). 🔴 Cơ chế nào bắt user nhớ lệnh là đã hỏng từ thiết kế |
| ⚰️ QD-08 | 31/07 | Thẻ Anki là nguồn sự thật, cache chỉ là bộ đệm | CHẾT — QD-11 thay cùng ngày, bỏ hẳn file cache |
| QD-07 | 31/07 | `PHIENBAN.md` là file DUY NHẤT viết cho user, ngôn ngữ thường; S14 canh trần | Mọi file khác đều viết cho người làm. 🔴 Phiên soạn lô KHÔNG ghi vào đây (user bác 02/08) — mốc là DEPLOY, không phải "user cảm nhận được" |
| ⚰️ QD-06 | 31/07 | Đóng sổ `CHANGELOG.md`, lịch sử về `git log` — S9 canh "commit có thân" | Commit message gắn chặt với diff nên không nói dối được; tài liệu song song thì lệch mà không ai biết |
| ⚰️ QD-05 | 31/07 | Cache ngữ pháp ra ngoài repo | CHẾT — QD-11 thay cùng ngày, bỏ hẳn file cache |
| QD-04 | 31/07 | Cảnh báo "bot chết" gọi thẳng Telegram bằng `curl`, KHÔNG qua `tgbot/alerts.py` | `alerts.py` gửi qua chính con bot ⇒ bot chết thì cảnh báo chết theo. Đường báo không được nạp dòng Python nào của dự án |
| ⚰️ QD-03 | 31/07 | Tháo ngòi 12 file lô thế hệ 1 bằng `raise SystemExit` thay vì xoá — S7 canh | ⏳ Còn nợ: khi 168 thẻ k51–k60 đủ tag `chuan::3` thì xoá hẳn. Chạy nhầm là XOÁ bảng chia thẻ thật không một tiếng kêu |
| QD-02 | 31/07 | `soatkientruc.py` là điểm vào thứ 3 ở gốc, chỉ stdlib, ratchet một chiều, cắm vào `deploy.ps1` | Chỗ có máy đo thì sạch, chỗ chỉ có luật viết ra thì trôi. Ratchet chỉ cho GIẢM; nới được thì nó thành bảng ghi nợ chứ không phải cửa |
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
