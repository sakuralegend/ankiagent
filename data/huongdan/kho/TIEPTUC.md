# Chạy tiếp kho — đọc file này là đủ

Bạn (user) chỉ cần gõ một câu: **"chạy tiếp kho"**. Phần dưới là cho tôi.

---

## Trạng thái nằm ở đâu

| File | Là gì |
|---|---|
| `hangdoi.json` | 56 lô + `trangthai: cho\|xong` — **nguồn sự thật duy nhất** |
| `tudien.json` | ảnh chụp đông lạnh 703 từ (WordClean, trọng âm, từ loại, nghĩa). **Đừng sửa** |
| `kNN_*.py` | nội dung đã soạn, dữ liệu thuần `S = {...}` |

```bash
PYTHONIOENCODING=utf-8 python data/huongdan/kho/congcu.py trangthai
```

## Mở lô kế tiếp — quy tắc bất di bất dịch

🔴 **MỖI LÔ MỘT AGENT PHỤ, MỘT CONTEXT TRẮNG.** Luồng chính **không soạn chữ nào**.
User đã chốt cách này sau khi chỉ ra: gộp nhiều lô vào một context làm chất lượng **nhạt dần**
— người soạn bắt đầu chép khuôn lô trước thay vì nghĩ lại cho từ mới, mà nhạt dần thì **chính
người soạn khó tự thấy**. User không kiểm được nội dung, nên đây là kiểu xuống cấp nguy hiểm nhất.

Khuôn lời nhắn giao cho agent phụ (đổi `kNN` và phần chủ đề):

> Soạn ô "Hướng dẫn" cho lô **kNN**, dự án Anki học tiếng Nga tại `d:\Desktop\ANKI`.
>
> **1. Đọc spec TRƯỚC KHI viết** — toàn bộ `data/huongdan/README.md` (đặc biệt §2, §5, **§7**),
> và `data/huongdan/kho/MAU.py` làm chuẩn văn phong + mật độ nội dung.
> (**Đừng đọc `k01_actions.py`** — 64 KB, MAU.py 19 KB đã đủ.)
> **2. Đề bài:** `PYTHONIOENCODING=utf-8 python data/huongdan/kho/congcu.py tiep kNN`
> **3. Soạn** `data/huongdan/kho/kNN_<topic>.py`, chỉ chứa `S = {...}`. ‹gợi ý hệ thống trục›
> **4. Tự soát:** `… congcu.py soat kNN` — sửa tới khi **cả ba** mục đầu báo `(khong co)`,
> rồi **đọc bằng mắt** danh sách "PHAI DOC BANG MAT".
> **5. DỪNG** — không sửa `hangdoi.json`, không commit, không `nap`, không đụng Anki.
> (Ngoại lệ: gặp **từ đồng tự** thật thì được thêm dòng vào `MIEN_TRU` kèm lý do, và phải báo lên.)
>
> **Báo cáo:** số từ · kết quả 3 mục soát · **những chỗ KHÔNG chắc đã hạ mức tin**.

🔴 **MỖI PHIÊN 2 LÔ, VÀ PHIÊN ĐÓ CHỈ ĐƯỢC CHẠY LÔ.**
Đo thật phiên tối 27/07: k09 = **191K token**, k10 = **171K** ⇒ ~**180K/lô**, hai lô ~360K.
Nhưng phiên đó chạm 99% *không phải* chỉ vì hai lô — luồng chính còn viết lại `nap`, truy bug
`noteId`, sửa docs, 5 lần commit. **Trộn việc sửa công cụ vào phiên chạy lô chính là thứ đội
hạn mức lên.** (Trước đó: 8 lô = trọn cửa sổ 5h + $25 credit.)

- **2 lô** nếu phiên chỉ chạy lô — **giao cả hai ngay từ tin nhắn đầu**, chạy song song, luồng
  chính đứng im chờ. Đó là lúc rẻ nhất.
- **1 lô** nếu còn phải sửa công cụ / gọt k04 / bàn việc khác.
- Luồng chính **KHÔNG đọc file lô** (~1000 dòng mỗi file) — tin ba cửa soát, đó là lý do dựng chúng.

Hết quota thì **dừng và báo cáo**, để user tự quyết.

**Mọi lô dùng Opus** — user chốt 27/07 sau khi biết chi phí. Không hạ model để tiết kiệm.

## Khi một lô báo xong

```bash
PYTHONIOENCODING=utf-8 python data/huongdan/kho/congcu.py soat kNN        # tự soát lại, ĐỪNG tin báo cáo suông
PYTHONIOENCODING=utf-8 python data/huongdan/kho/congcu.py xong kNN        # chỉ luồng chính được gọi
PYTHONIOENCODING=utf-8 python data/huongdan/kho/congcu.py nap --apply     # đẩy vào Anki ngay + sync
git add data/huongdan/kho/kNN_*.py data/huongdan/kho/hangdoi.json && git commit …
```

**Nạp NGAY sau mỗi lô, không gom một cục cuối đường** (user chốt 27/07). Ba chốt giữ cho
tiến trình không loạn:
1. `nap` **chỉ đọc lô `trangthai == "xong"`** — file agent đang soạn dở không thể lọt vào thẻ thật,
   nên nạp được cả khi có lô khác đang chạy song song.
2. **`daNap` trong `hangdoi.json` là sổ cái** — lô đã vào Anki thì lần sau không đụng lại
   (`--tatca` để ép đẩy lại toàn bộ).
3. **Thiếu note thì KHÔNG đánh dấu `daNap`** — hàng đợi lệch bộ sưu tập phải hiểu rồi mới chạy tiếp.

Ghi field `HuongDan` **không phải schema mod** (field có sẵn) ⇒ **không kích hoạt full sync**,
laptop vẫn sync thường với iPhone và VPS. Sửa nội dung note (laptop) và lịch sử ôn (iPhone) là hai
loại dữ liệu khác nhau, Anki gộp được — không phải chọn chiều.

⚠️ **Lô không được tự đánh dấu mình xong** — tự chấm điểm mình thì bộ soát mất hết ý nghĩa.
Đọc kỹ mục "chỗ tôi không chắc" trong báo cáo: lô động từ/tính từ gần như **không được bộ soát
đỡ** (`nouns.csv` chỉ có 382/703 từ là danh từ), nên đó là chỗ duy nhất bắt được lỗi nội dung.

## Khi HẾT 48 lô

```bash
python data/huongdan/kiemtra.py     # soát lại TRÊN THẺ THẬT, sau khi đã nạp hết
```

Sau khi nạp xong toàn bộ thẻ: **xoá khối CSS `mn-*` di sản** (6 quy tắc) trong
`anki_tools/templates/card.css`.

⚠️ **Chưa xoá được bây giờ.** Đo 28/07 trên 869 thẻ: 163 thẻ đã có hướng dẫn mới ·
**222 thẻ mang nội dung cũ** · 484 thẻ rỗng. Trong 222 thẻ cũ đó, **chỉ 54 thẻ là mnemonic
thật** (class `mn-story`/`mn-tip`/`mn-read`) — 168 thẻ còn lại **đã đúng định dạng `hd-*`**,
chỉ mỏng hơn (1–2 KB). Xoá CSS khi 54 thẻ kia còn sống là vỡ giao diện chúng.

**Đừng xoá nội dung mnemonic cũ đi cho gọn** (đã cân nhắc và bác 28/07): cả 54 thẻ là mnemonic
**thuần**, không thẻ nào có sẵn phần `hd-*`, nên xoá là để lại ô trống hàng tuần liền. Mà nội
dung đó không phải rác — ngoài phần phiên âm thô đã bị bác, mỗi thẻ còn nêu **từ họ hàng**
(`лев`↔lion, `хлеб`↔loaf) và **luật vô thanh hoá âm cuối** (`в→f`, `б→p`), đều đúng. Chúng tự
bị viết đè khi lô của chúng tới lượt.

## Việc còn nợ

- ⚠️ **Lô k04 phình dài** — 13/15 thẻ vượt 12 KB (đỉnh `реплика` 16,9 KB) vì chồng **ba** khối
  hệ thống lên cùng một thẻ. Nội dung **không sai**, chỉ dài. Trần đã ghi vào README §2
  (6–10 KB, **tối đa 2 khối dùng chung mỗi thẻ**) và các lô sau phải theo. Lúc nào rảnh thì
  quay lại gọt k04: bỏ bớt khối thứ ba ở những thẻ mà nó không thật sự liên quan.
  Kiểm bằng `congcu.py dodai`.
- ~~Thẻ trùng do U+200B~~ **XONG 28/07**: user duyệt xoá, đã bỏ hai bản 12/07 (bản mang U+200B
  trong field `Word`, ít lượt ôn hơn), giữ hai bản 04/07 sạch chữ. Bộ sưu tập **871 → 869 note**.
  Sao lưu đầy đủ cả 4 note kèm revlog ở `_backup_the_trung.json` (không commit).

## Bẫy đã dính, đừng dính lại

- 🔴 **KHI CÓ LÔ CHẠY SONG SONG, ĐỪNG `git add -A`.** Nó quét cả file đang soạn dở của lô khác
  vào commit, và HEAD giữ **ảnh chụp còn lỗi** trong khi bản đã sửa nằm trên đĩa. Đã dính thật
  ở k08. Commit theo **đường dẫn cụ thể**: `git add data/huongdan/kho/kNN_*.py hangdoi.json`.

- 🔴 **`ё` KHÔNG được gộp về `е` khi ghép với note Anki.** `bare()` gộp ё→е (đúng, vì
  `nouns.csv` in ё thành е), nhưng dùng chính nó làm khoá ghép note thì **всё và все thành một
  khoá** — và `nap` ghi ô Hướng dẫn của từ này đè lên thẻ của từ kia. Đã xảy ra thật 28/07.
  Nay `nap` dùng **`khoa_note()`** (giữ ё). Cặp còn lại chưa nổ: **`нёбо` (vòm miệng) / `небо`
  (bầu trời)** — nhớ khi tới lô của chúng.
  **Sau mỗi lần nạp, đối chiếu "ghi vào N note" với số từ của lô.** Lệch là có chuyện; chính con
  số 33-note-cho-32-từ đã tố giác lỗi này.

- ⚠️ **Bộ soát KHÔNG kiểm cụm in đậm nhiều chữ.** Mọi token có dấu cách bị bỏ qua hoàn toàn,
  nên trọng âm sai trong collocation (`между́ строк` thay vì `ме́жду строк`) lọt sạch ba cửa.
  Lô nào có nhiều cụm in đậm thì phải **rà tay**. Chưa vá.

- 🌐 **Mạng chớp = cả hai agent chết cùng lúc.** Đã dính 28/07: hai agent độc lập cùng báo
  "Connection closed mid-response" đúng lúc sắp `Write` file ~100 KB. Cách chữa: dặn agent
  **ghi từng khúc 3–4 từ** (Write khung trước, rồi Edit chèn thêm), và khi gặp lỗi này thì
  **`SendMessage` cho chạy tiếp** thay vì spawn agent mới — ngữ cảnh còn nguyên, không phải
  soạn lại.

- **AnkiConnect đặt tên khoá LỆCH nhau ở hai đầu**: `notesInfo` trả về `noteId`, còn
  `updateNoteFields` lại nhận `{"id": …}`. Code cũ đọc `n["id"]` nên `nap` **chưa bao giờ chạy
  được thật** — và nó sẽ nổ đúng ở bước cuối cùng, sau khi đã soạn xong cả 703 từ. Bài học:
  **chạy khan đường ống ghi từ sớm**, đừng để dành tới cuối.

- **Nội dung `HuongDan` cũ đã sao lưu** ở `_backup_huongdan.json` (271 note, không commit vì
  nặng và là dữ liệu chết). Nội dung mới thì nguồn thật nằm ở các file `kNN_*.py` trong git,
  nạp lại lúc nào cũng được — Anki chỉ là bản sao.

- **Console Windows là cp1252** — in tiếng Nga ra là `UnicodeEncodeError`.
  Luôn `PYTHONIOENCODING=utf-8`, và dữ liệu lớn thì ghi ra file.
- **Bash tool là Git Bash, KHÔNG phải PowerShell.** Đừng dùng here-string `@'…'@` cho commit
  message — nó tạo commit tên `@`. Dùng `git commit -F - <<'EOF'`.
- **Bộ sưu tập có thẻ TRÙNG do zero-width U+200B**: `петь`/`петь​`, `пить`/`пить​`. Anki coi là
  hai note, mắt thường không phân biệt được. `nap` đã xử lý (ghép theo khoá đã bỏ U+200B, ghi
  vào **cả hai** note) — đừng "sửa" nó về `findNotes` từng từ.
