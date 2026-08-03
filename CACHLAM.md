# 📘 SỔ TAY CÁCH LÀM VIỆC — v1

> **Phạm vi:** từ nay về sau, mỗi lần thêm chức năng / sửa lỗi thì làm thế nào để không đẻ thêm mớ bòng bong.
> Việc **dọn cái đã tồn tại** (tài liệu kiến trúc, script soát, vá lỗi cũ) do plan riêng lo — sổ tay này chỉ nhắc tới khi giao nhau, mỗi lần một dòng.
> Sổ tay có **số hiệu luật** (`L1`…`L5`) và **số hiệu phiên bản** (v1) — commit và trao đổi sau này viện dẫn được, đúng kiểu `CHUAN.md` đã thành công.
> User duyệt và nhận vào repo chính thức ngày 30/07/2026 (`QD-01`).

---

## Q1 — Chẩn đoán: "fix lỗi và thêm chức năng dần dần" sai ở đâu, đúng ở đâu

**Đúng ở chỗ:** làm dần dần chính là cách đúng cho dự án một người. Thiết kế kiến trúc từ đầu cho một dự án mà chính chủ chưa biết mình cần gì (3 tuần trước chưa ai biết sẽ có "dây chuyền soạn kho 61 lô") gần như chắc chắn sai và lãng phí. Bằng chứng ngay trong repo: những phần tốt nhất — `CHUAN.md` có số hiệu, cửa soát `congcu.py soat`, sổ cái `hangdoi.json` — đều **mọc dần từ nhu cầu thật**, không ai vẽ trước.

**Sai ở chỗ:** không phải thiếu kiến trúc, mà thiếu **cửa soát cho code**. Hãy nhìn lại §3 của chính dự án này: chỗ nào có luật-nằm-trong-file + máy canh (nội dung thẻ) thì 18 lô không sự cố; chỗ nào luật chỉ nằm trong đầu (code) thì 10 wrapper, 4 luật chuẩn hoá, 3 nơi dựng HTML. **Cùng một con người, hai kết quả ngược nhau** — vậy biến số không phải là con người, mà là *luật có được viết ra ở chỗ người-thi-hành đọc được hay không*.

Và người-thi-hành ở đây **không phải bạn** — là AI. Mỗi phiên Claude Code là một *nhân viên mới ngày đầu tiên*, giỏi nhưng không biết gì về các phiên trước. 163 commit trong 3 tuần nghĩa là dự án này đã đi qua tay hàng chục "nhân viên mới" mà **không có sổ tay onboarding nào** (repo không có `CLAUDE.md` — đã kiểm tra, thật sự không có). 10 bản wrapper không phải là 1 người lười 10 lần; đó là 10 nhân viên mới, mỗi người một lần, đều chọn phương án an toàn nhất cho *phiên của mình*: chép thì chắc chắn chạy, import thì phải đi đọc code người khác.

**"Loạn sau 3 tuần" có bất thường không?** Không, nếu quy đổi đúng đơn vị. 7.589 dòng / 3 tuần là tốc độ mà một người gõ tay cần khoảng 4–6 tháng. Dự án tay loạn ở tháng thứ 5 là chuyện kinh điển ai cũng gặp. AI chỉ **nén thời gian lại ~8 lần** — cả tốc độ xây lẫn tốc độ loạn. Kết luận rút ra không phải "tôi kém" mà là: **mọi cơ chế phòng ngừa cũng phải rẻ và tự động tương ứng**, vì bạn không có 5 tháng để nhận ra vấn đề, bạn có 3 tuần.

**Trả lời §3.3 — vì sao nguyên tắc đúng ("MỘT chức năng MỘT script") vẫn không tự thi hành:** vì nó được phát biểu ở nơi người-thi-hành không đọc (trí nhớ của bạn, memory của một phiên chat), và không có máy nào đo nó. So sánh: *"nhãn không số hiệu là quả bom hẹn giờ"* — bạn tự viết câu đó cho nội dung thẻ. Nguyên tắc không-nằm-trong-file chính là nhãn không số hiệu của phần code. Suy ra loại lời khuyên duy nhất có tác dụng ở dự án này: **lời khuyên phải kết tinh thành (a) một dòng trong file AI tự đọc, hoặc (b) một lệnh máy chạy được**. Mọi thứ khác là trang trí. Toàn bộ sổ tay này viết theo tiêu chí đó.

---

## Q2 — Năm luật (L1–L5)

Nguyên tắc chọn: mỗi luật phải chỉ được lỗi thật ở §3.2 mà nó ngăn, và phải có **cơ chế canh rẻ** trả lời được câu *"cái gì bắt tôi làm điều này lúc 11 giờ đêm?"*. Cơ chế canh của cả 5 luật quy về đúng 2 chỗ: **file `CLAUDE.md`** (AI tự đọc mỗi phiên — chi phí 0 lượt hỏi sau khi viết một lần) và **vài lệnh grep/đếm** (vài giây). Không luật nào dựa vào tự giác.

| # | Luật (một câu) | Lỗi ở §3.2 nó ngăn | Ai/cái gì canh · tốn bao nhiêu |
|---|---|---|---|
| **L1** | Mỗi tài nguyên ngoài (AnkiConnect, mạng, AI API) chỉ được nói chuyện qua **một cửa**: AnkiConnect → `anki_client`, gọi mạng OpenRussian → `grammar.fetch_page`, AI → `ai_client`; ai cần thì import, cấm mở cửa riêng. | 10 wrapper AnkiConnect; 27 file .py đang tự trỏ thẳng `:8765` (đo hôm nay) | Dòng lệnh 2 giây: `grep -rln "8765" --include="*.py" . \| grep -v anki_client` — kết quả phải là rỗng (sau khi plan dọn xử xong tồn đọng). Câu chữ tương ứng nằm sẵn trong `CLAUDE.md` nên AI mới không mở cửa thứ 11. |
| **L2** | Script sinh ra để chạy **một lần** thì phải khai tử **trong cùng commit** dùng xong: chuyển vào `_daxong/`; thư mục gốc chỉ chứa điểm vào đang sống (`bot.py`, `main.py`). | 11 script gốc không phân biệt sống/chết; 12 file lô thế hệ 1 còn chạy được và chạy lại thì **xoá bảng chia im lặng** (đã dính 29/07) — đây là loại hỏng IM LẶNG nguy hiểm nhất | `ls *.py` — nhìn 2 giây, quá 3 file là có xác chết. `CLAUDE.md` dặn AI: *"script vá một lần đặt tên `_va_<việc>.py`, chạy xong chuyển `_daxong/` ngay trong commit đó"*. Git giữ hộ lịch sử, không sợ mất. |
| **L3** | Mỗi lần sửa code kết thúc bằng **một lệnh nghiệm thu chạy thật** do AI đề xuất ngay từ đầu việc, tối thiểu là `python -c "import bot, main"`. | Không có test nên "xong" hiện là cảm giác; bot chết giữa buổi học vì lỗi chỉ lộ lúc khởi động | AI tự canh: `CLAUDE.md` ghi *"mọi việc sửa code phải kết thúc bằng mục 'Lệnh nghiệm thu:' và chạy nó"*. Chi phí ~10 giây/lần, 0 lượt hỏi thêm (nằm trong cùng lượt). |
| **L4** | Việc chạm **vùng im lặng** — schema/field model Anki, xoá hay ghi đè hàng loạt thẻ thật, sync — là việc **đứng riêng một mình**: không gộp với việc khác, có backup trước, có kiểm `journalctl` + một lần sync tay sau. | VPS kẹt "Sync status 2" im lặng (đã xảy ra); bảng chia bị xoá im lặng; đây là các sự cố **duy nhất từng làm mất dữ liệu thật** | `CLAUDE.md` ghi danh sách vùng im lặng + lệnh cho AI: *"đụng các vùng này thì DỪNG LẠI HỎI trước khi chạy"*. Chi phí: 1 câu xác nhận + ~2 phút kiểm sau — chỉ ở loại việc hiếm (vài lần/tháng). |
| **L5** | Quyết định có ngã rẽ (chọn A thay vì B) thì ghi **4 dòng vào `QUYETDINH.md` với số hiệu `QD-nn`**; commit nào thi hành nó thì nhắc số hiệu. | `# tránh import vòng` không có vòng; README chết 9 ngày; 6 tháng sau không hiểu code của chính mình | AI viết hộ 4 dòng cuối phiên, bạn chỉ duyệt — chi phí ~20 giây đọc. Ngưỡng bắt buộc ghi ở mục Q5, không phải ghi mọi thứ. |

**Vì sao không có luật thứ 6** (kiểu "file không quá X dòng", "đừng gọi tên private"): những thứ đó là **ngưỡng cảnh báo** (Q4), không phải luật. Luật là thứ vi phạm một lần đã có hại; ngưỡng là thứ vượt qua thì ghi nợ. Trộn hai loại làm luật loãng và người ta bỏ cả gói.

---

## Q3 — Quy trình thêm MỘT chức năng (6 bước)

> In ra / ghim đầu `CLAUDE.md`. Bước 1–2 là chỗ quyết định thắng thua; bước 3–6 gần như tự chạy.

1. **Viết một câu:** *"Chức năng này để ___, dùng khi ___."* Không viết nổi một câu → chưa đủ chín, đừng làm (xem Q7).
2. **Ra yêu cầu cho AI kèm 2 câu bắt buộc** (chi tiết câu chữ ở Q6): *"Trước khi viết, liệt kê hàm/module có sẵn mà việc này nên dùng lại"* và *"muốn tạo file mới hay hàm trùng vai với hàm cũ thì phải nêu lý do trước."*
3. **Chọn chỗ đặt** theo bảng dưới.
4. AI viết. **Yêu cầu ngay từ đầu: kết thúc bằng "Lệnh nghiệm thu:"** (L3).
5. **Nghiệm thu:** chạy lệnh đó + soi diff theo 3 dấu hiệu đỏ ở Q6. Chạm vùng im lặng thì đi cửa L4.
6. Commit với phần thân khai VÌ SAO (S9 canh, xem 3c); nếu có ngã rẽ thì thêm `QD-nn` (Q5). Push → restart → liếc journalctl 10 giây.

### 3a. File cũ hay file mới?

| Tình huống | Làm gì |
|---|---|
| Sửa/mở rộng hành vi của hàm đã có | File cũ, hàm cũ |
| Chức năng mới nhưng **cùng vòng đời** với file cũ (chết cùng nhau, deploy cùng nhau, người gọi là cùng một chỗ) | File cũ, hàm mới |
| Chức năng mới mà file định thêm đã **quá trần ghi nợ** (số ở `soat_nguong.json`), hoặc phải thêm import thuộc tầng khác (file đang thuần đọc-dữ-liệu bỗng phải gọi mạng) | File mới trong cùng gói |
| Script chạy tay một lần | `_va_<việc>.py` → `_daxong/` khi xong (L2) |

Quy tắc gói (4 mảng): **cái gì chỉ bot dùng → `tgbot/`; chỉ dây chuyền soạn kho dùng → `data/huongdan/`; chỉ thẻ ngữ pháp dùng → `grammar_forms/`; từ HAI mảng trở lên cùng cần → `anki_tools/`** — và chỉ khi có người thứ hai thật sự cần, đừng "để sẵn cho tương lai". Chiều import một chiều: các mảng import `anki_tools`, `anki_tools` không import ngược ra mảng nào.

### 3b. Phép thử chép-dán (câu quan trọng nhất)

Dự án này có cả trùng lặp tai hại (10 wrapper) lẫn trùng lặp **cố ý đúng đắn** (dây chuyền soạn kho có wrapper riêng để thay đổi ở bot không giết lô đang chạy tối nay). Phép thử phân biệt, một câu hỏi:

> **"Ngày mai bản GỐC sửa mà bản CHÉP không sửa theo — đó là LỖI hay là Ý ĐỒ?"**

- **Là LỖI** (hai bản phải luôn giống nhau, lệch là hỏng im lặng — như 2 hàm chuẩn hoá `ё` cho kết quả khác nhau) → **cấm chép, bắt buộc import**. Đây là trùng lặp *hai bản cùng sống*.
- **Là Ý ĐỒ** (bản chép là **ảnh chụp cố tình đóng băng** để cách ly rủi ro) → được chép, nhưng phải trả 2 đồng thuế: (1) dòng đầu file ghi `# ẢNH CHỤP từ <gốc> ngày <d>, lý do: <1 câu>, hết hạn khi: <sự kiện>`; (2) một mục `QD-nn`. Ảnh chụp không ghi hạn chính là 12 file lô thế hệ 1 — thứ đã xoá dữ liệu thật.

### 3c. "Xong" nghĩa là gì khi không có test

Xong = đủ 3 dấu: **(1)** lệnh nghiệm thu chạy thật, ra kết quả nhìn thấy được (bot trả lời đúng trên Telegram / thẻ hiện đúng trong Anki — sản phẩm này may mắn: đầu ra nhìn được bằng mắt); **(2)** `python -c "import bot, main"` sạch — chặn loại chết-lúc-khởi-động; **(3)** với vùng im lặng: một vòng kiểm sau-sync theo L4. Thiếu dấu nào thì chưa được coi là "xong", đừng commit.

---

## Q4 — Ngưỡng cảnh báo sớm, bằng con số

Vượt ngưỡng **không có nghĩa là sửa ngay** — giữa việc khác mà tiện tay refactor là cách đẻ bug kinh điển. Hành động mặc định là **ghi một dòng vào `SONO.md`** (sổ nợ): `- [ ] <file/hàm>: <ngưỡng nào vỡ> (ghi ngày)`. Trả nợ khi: sắp sửa tiếp đúng file đó, hoặc sổ nợ chạm 10 mục.

| Ngưỡng | Con số | Đo bằng (PowerShell, vài giây) | Vượt thì |
|---|---|---|---|
| File phình | Trần ghi-nợ / trần tách: số ở `soat_nguong.json` (một nguồn duy nhất, QD-21) | `python soatkientruc.py` — cửa S13 tự soi mọi file code, khỏi đếm tay | Ghi nợ (`SONO.md` + mốc vào `da_ghi_no`) / tách trước khi thêm |
| Bản sao một đoạn | **Luật số 3**: lần 1 viết, lần 2 được phép chép *nếu qua phép thử 3b*, lần 3 **bắt buộc gom** trước khi viết bản 3 | Không cần máy — bước 2 của Q3 (bắt AI liệt kê cái có sẵn) chính là máy dò; nếu AI khai "đã có 2 bản" thì đấy là lần 3 | Gom ngay trong việc đang làm (đằng nào cũng đang viết chỗ đó) |
| Tham số hàm | **>5 tham số** | Nhìn bằng mắt lúc duyệt diff | Ghi nợ; bảo AI "gom nhóm tham số này thành một dict/dataclass" ở lần sửa sau |
| Script chết | **30 ngày không ai đụng** và không phải điểm vào | `git log -1 --format="%cr" -- <file>` | Chuyển `_daxong/` (L2). Xoá hẳn cũng được — git giữ hộ |
| Gọi tên `_private` xuyên module | **1 lần là đỏ** — đây thực chất là vi phạm L1 dạng mềm | `grep -rn "grammar\._\|client\._" --include="*.py"` (chạy khi rảnh, 5 giây) | Ghi nợ: hoặc đổi tên hàm thành public có chủ đích, hoặc cấp hàm public thay thế |
| Sổ nợ phình | **10 mục** | Đếm dòng `SONO.md` | Dành một phiên AI riêng chỉ để trả nợ, không trộn với feature |

---

## Q5 — Ghi QUYẾT ĐỊNH, không chỉ ghi thay đổi

Cơ chế số hiệu của `CHUAN.md` thành công vì 3 tính chất: **có số để viện dẫn · nằm trên đường đi công việc · một mục nhỏ tới mức không ngại viết**. Áp nguyên xi cho quyết định kỹ thuật:

- **Ở đâu:** một file `QUYETDINH.md` ở gốc repo. Không rải theo thư mục (dự án một người, một file tra được hết).
- **Một mục = đúng 4 dòng**, mới nhất trên cùng:

  ```
  ## QD-07 · 30/07/2026 · Wrapper riêng cho dây chuyền soạn kho
  Chọn: kho/ giữ wrapper AnkiConnect riêng, đóng băng.
  Thay vì: import chung anki_client.
  Vì: sửa bot không được phép giết lô đang chạy tối nay. Hết hạn: khi xong 61 lô.
  ```

- **Khi nào BẮT BUỘC ghi** (đúng 4 cửa, ngoài ra miễn): (1) chọn A thay vì B mà 6 tháng sau nhìn code **không tự thấy** lý do; (2) cố ý làm trái L1–L4 hoặc chấp nhận một ảnh-chụp-chép-dán (3b); (3) chạm schema Anki; (4) khai tử / đóng băng một thứ. Sửa bug thường, thêm từ, chỉnh câu chữ — **không ghi**, commit message có thân là đủ (3c).
- **Chống phình thành `CHANGELOG.md` 2 809 dòng thứ hai (đã đóng sổ hẳn, QD-06/QD-14):** trần cứng 4 dòng/mục; AI viết hộ cuối phiên (bạn chỉ duyệt 20 giây); và khác commit message ở tần suất — commit ghi *mỗi lần làm*, QUYETDINH chỉ ghi *mỗi lần rẽ*, ước tính 2–4 mục/tuần. 100 quyết định ≈ 400 dòng ≈ vẫn đọc hết trong 10 phút.
- **Khép vòng:** commit message thi hành quyết định thì ghi `(QD-07)` — y như tag `chuan::3` trên thẻ. Grep `QD-07` ra cả lý do lẫn code.

---

## Q6 — Làm việc với AI cho đúng (mục quan trọng nhất)

Sự thật nền: **mỗi phiên AI là nhân viên mới ngày đầu**. Mọi thứ bạn muốn nó "luôn luôn làm" phải nằm trong file nó tự đọc, không nằm trong trí nhớ của bạn hay của phiên trước.

### 6a. Thứ đặt sẵn trong repo — việc đáng làm nhất sổ tay này

Repo **chưa có `CLAUDE.md`** (đã kiểm tra hôm nay). Đó là lỗ hổng lớn nhất và cũng là món rẻ nhất: viết một lần ~40 dòng, mọi phiên Claude Code từ đó **tự động** đọc trước khi làm gì — chi phí 0 lượt hỏi mãi mãi. Nội dung tối thiểu:

1. Năm luật L1–L5 (mỗi luật một dòng).
2. Bản đồ 4 gói + quy tắc chọn chỗ đặt (bảng 3a, ~8 dòng).
3. Danh sách **vùng im lặng** + lệnh *"đụng vào thì DỪNG LẠI HỎI"* (L4).
4. Lệnh nghiệm thu chuẩn (`python -c "import bot, main"`) + yêu cầu mọi việc kết thúc bằng "Lệnh nghiệm thu:".
5. Các bẫy đã trả học phí: `ё` phải `normalize("NFC")`, đường dẫn file theo góc nhìn container Anki, callback Telegram 64 byte…

*(Plan dọn dẹp có phần viết tài liệu kiến trúc — CLAUDE.md chỉ cần 40 dòng luật, trỏ sang tài liệu đó cho phần mô tả, đừng viết trùng.)*

### 6b. Ra yêu cầu để không có wrapper thứ 11 — ở mức câu chữ

AI mặc định chép-cho-chắc vì lệnh của bạn thường chỉ nói *đích* ("thêm nút X") mà không nói *ràng buộc đường đi*. Ba câu ghép thẳng vào yêu cầu (đã nằm trong CLAUDE.md thì chỉ cần khi việc lớn):

- *"Trước khi viết, **liệt kê hàm/module có sẵn** mà việc này nên dùng lại. Đã có hàm gần giống thì dùng/mở rộng nó, **đừng viết bản mới**."*
- *"**Không tạo file mới, không viết hàm trùng vai** với hàm đã có, trừ khi nêu lý do và được tôi gật đầu trước."*
- *"Sửa **ít file nhất có thể**; xong việc, khai: đã đổi file nào, vì sao từng file."*

### 6c. Nghiệm thu khi không đọc nổi từng dòng

Đừng cố đọc code — hãy đọc **hình dạng của diff** và **lời khai của AI**. Ba dấu hiệu đỏ dễ nhận nhất, theo đúng bệnh sử §3.2:

1. **Diff to hơn lời hứa.** Xin một chức năng mà 6–7 file thay đổi, hoặc có file bị đổi mà AI không giải thích vì sao → bắt giải thích từng file trước khi nhận.
2. **Có file mới / hàm mới tên na ná cái cũ** (`get_anki_data` bên cạnh `fetch_anki`…) → hỏi đúng một câu: *"vì sao không dùng cái cũ?"*. Trả lời không thuyết phục = wrapper thứ 11 đang chào đời.
3. **Code chạm vùng im lặng mà không có lưới**: thấy `deleteNotes`, `updateNoteFields` hàng loạt, đổi model/field — mà không thấy backup, không thấy bước kiểm sau → dừng, đi cửa L4.

Kèm một thủ tục rẻ: cuối việc bắt AI **tự khai ba mục** — *đã đổi gì / lệnh nghiệm thu / rủi ro im lặng nào có thể có*. Mục thứ ba đặc biệt quý: AI biết rủi ro của code nó viết, nhưng chỉ nói khi bị hỏi.

### 6d. Khi nào bắt AI dừng lại hỏi

Ghi thẳng vào CLAUDE.md, nguyên văn đề xuất:

> *"DỪNG LẠI HỎI trước khi: (1) đổi/thêm/xoá field của model Anki hay bất cứ gì kích full sync; (2) xoá hoặc ghi đè hàng loạt thẻ/note thật; (3) tạo file .py mới ở thư mục gốc; (4) viết hàm thứ hai cùng vai với hàm đã có; (5) đụng repo/hạ tầng ngoài phạm vi việc được giao."*

Năm cửa này đều hiếm gặp nên tổng chi phí ~1 câu xác nhận vài lần mỗi tuần — rẻ hơn rất nhiều so với một lần "Sync status 2" im lặng.

---

## Q7 — Nói KHÔNG và cắt phạm vi

Ba phép thử trước khi thêm bất cứ thứ gì mới, hỏi theo đúng thứ tự:

1. **Nó phục vụ buổi học tuần này, hay nó "sẽ hay"?** "Sẽ hay" → vào `SONO.md` phần Ý TƯỞNG, không làm. (Bộ lọc này tồn tại vì sản phẩm là công cụ học *đang dùng hằng ngày* — mọi giờ xây thứ "sẽ hay" là giờ không soạn kho.)
2. **Giá nuôi, không chỉ giá xây.** Nó có chạy trên VPS 24/7 không? Hỏng nó có mất buổi học không? Nếu có — nó là *hạ tầng*, và hạ tầng thì trả tiền nuôi mãi mãi (log, restart, backup, một chỗ nữa để sync kẹt). Tính giá đó trước khi gật.
3. **Chi phí cơ hội tính bằng lô.** Ngân sách AI là ràng buộc thật và đang có chủ nợ tên là *43 lô còn lại ≈ nhiều tuần*. Câu hỏi đúng không phải "feature này có đáng không" mà là **"nó đáng hơn 2 lô soạn kho không?"** — quy đổi ra đơn vị đó rồi hãy quyết.

**Đáng đóng băng / khai tử ở hiện trạng:**

| Thứ | Đề nghị | Lý do |
|---|---|---|
| 12 file lô thế hệ 1 + script vá một lần ở gốc | Khai tử (việc của plan dọn — một dòng nhắc, không bàn thêm) | Đã xoá dữ liệu thật một lần |
| `grammar_forms/` mở rộng "các loại biến cách khác" | **Đóng băng đến khi xong 61 lô**, ghi một mục QD | Mảng này chạy được, không ai kêu; mọi giờ mở rộng nó cạnh tranh trực tiếp với dây chuyền kho — chủ nợ lớn nhất |
| Chức năng bot mới (ngoài sửa lỗi) | Feature-freeze mềm cùng lý do, cùng mốc | Bot đã phủ đủ vòng học hằng ngày |
| Ý tưởng hạ tầng mới (dashboard, web UI, thống kê…) | Vào sổ Ý TƯỞNG, hẹn xét sau mốc 61 lô | Phép thử 1 + 2 đều trượt |

**Một dòng đọc ngược từ chính dự án:** thứ đã cứu bạn không phải là chức năng thứ 20 của bot, mà là mấy cái luật nhỏ tự đặt. Khi phân vân xây gì tiếp, xây thêm *luật/cửa soát* thường lãi hơn xây thêm *chức năng*.

---

## Q8 — Thứ KHÔNG nên áp dụng (ở quy mô này)

| Thực hành | Phán quyết | Vì sao ở đây nó hại/lãng phí | Ngưỡng xét lại |
|---|---|---|---|
| Test coverage cao, pytest đủ bộ | **Không.** Chỉ giữ đúng "lệnh nghiệm thu" L3 + (đáng giá nếu muốn thêm duy nhất một thứ) 1 file smoke-test gọi vài hàm thuần như chuẩn hoá `ё` | Code AI viết thay đổi nhanh, test theo không kịp thành test dối; lỗi thật của dự án này (trọng âm sai, bảng chia mất) nằm ở **dữ liệu**, mà cửa soát dữ liệu `congcu.py soat` đã có và tốt hơn unit test | Khi một hàm thuần túy hỏng lần thứ 2 theo cùng một kiểu → viết test cho đúng hàm đó, không hơn |
| CI/CD | **Không.** Deploy hiện tại (`git push` → pull → restart 10 giây) đã tốt; chỉ thêm một dòng `python -c "import bot"` vào script restart trên VPS để chặn chết-lúc-khởi-động | CI trả phí bằng thời gian chờ mỗi lần push, cứu chủ yếu lỗi phối hợp nhiều người — ở đây không có ai để phối hợp | Có cộng tác viên thứ hai, hoặc bot chết vì push hỏng >2 lần/tháng dù đã có dòng import-check |
| Code review nghi thức | **Không** — nhưng nghiệm thu 6c *chính là* code review dạng phù hợp: review hình dạng, không review từng dòng | Không có người thứ hai; giả vờ review từng dòng code AI là kịch | Không bao giờ, ở quy mô một người |
| Nhánh git phức tạp (gitflow, PR) | **Không.** Làm thẳng trên `main` | Chi phí nhánh trả cho việc nhiều người song song — không tồn tại ở đây | Việc sửa lớn kéo dài >1 ngày mà bot phải sống: một nhánh tạm duy nhất, xong là merge xoá |
| Type hint toàn bộ | **Không.** Chỉ hint **chữ ký hàm public của `anki_tools`** (ranh giới các mảng gặp nhau) — và đây là việc AI làm không công khi viết | Hint toàn bộ 7.6k dòng là chi phí thật đổi lấy an toàn mà không có mypy nào chạy để hưởng | Nếu một ngày lỗi kiểu-dữ-liệu-sai qua ranh giới gói xảy ra lần 2 → bật mypy chỉ cho `anki_tools/` |
| Dependency injection, kiến trúc lớp | **Không.** Import thẳng, hàm gọi hàm | DI trả giá dễ-thay-thế để phục vụ test double — mà ta đã quyết không xây bộ test | Không, ở quy mô này |
| Microservice / tách repo | **Không** (và đã có quyết định cũ cùng hướng: đừng tách project làm hai) | 4 mảng gặp nhau ở bộ sưu tập Anki; tách repo biến một lần sửa xuyên mảng thành 2 PR + 2 deploy | Không, chừng nào còn một người |
| Pre-commit hook nặng (format, lint đủ bộ) | **Không.** Nhiều nhất: một hook <1 giây chạy đúng lệnh grep của L1/L2 | Hook chậm lúc 11 giờ đêm sẽ bị `--no-verify` rồi chết hẳn — cơ chế bị ghét là cơ chế chết | Nếu sau 1 tháng bạn thấy mình quên chạy grep L1 bằng tay >2 lần → nhét đúng lệnh đó (và chỉ nó) vào hook |

Mẫu số chung: các món trên đều **trả chi phí mỗi-lần-sửa để mua an toàn phối-hợp-nhiều-người**. Dự án này ngược lại: một người, ngân sách theo lượt, rủi ro nằm ở *hỏng im lặng trên dữ liệu* — nên tiền phòng ngừa phải dồn vào cửa soát dữ liệu + CLAUDE.md + vùng im lặng, không dồn vào nghi thức.

---

## 🎯 Nếu chỉ nhớ được 3 câu, nhớ 3 câu này

1. **Luật không nằm trong file AI đọc được, hoặc không có lệnh máy đo được — là luật trang trí.** (Bạn đã tự chứng minh điều này: CHUAN.md sống khoẻ, "MỘT chức năng MỘT script" chết non.)
2. **Mỗi phiên AI là nhân viên mới ngày đầu — `CLAUDE.md` là sổ tay onboarding, viết một lần, mọi phiên tự tuân.** (40 dòng, món hời nhất repo này đang thiếu.)
3. **Sợ nhất không phải code chết to tiếng, mà là dữ liệu hỏng im lặng — mọi việc chạm vùng im lặng phải đứng một mình, có backup, có một vòng kiểm sau.**
