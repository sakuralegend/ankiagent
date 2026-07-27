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
> và `data/huongdan/kho/k01_actions.py` làm chuẩn văn phong + mật độ nội dung.
> **2. Đề bài:** `PYTHONIOENCODING=utf-8 python data/huongdan/kho/congcu.py tiep kNN`
> **3. Soạn** `data/huongdan/kho/kNN_<topic>.py`, chỉ chứa `S = {...}`. ‹gợi ý hệ thống trục›
> **4. Tự soát:** `… congcu.py soat kNN` — sửa tới khi **cả ba** mục đầu báo `(khong co)`,
> rồi **đọc bằng mắt** danh sách "PHAI DOC BANG MAT".
> **5. DỪNG** — không sửa `hangdoi.json`, không commit, không `nap`, không đụng Anki.
> (Ngoại lệ: gặp **từ đồng tự** thật thì được thêm dòng vào `MIEN_TRU` kèm lý do, và phải báo lên.)
>
> **Báo cáo:** số từ · kết quả 3 mục soát · **những chỗ KHÔNG chắc đã hạ mức tin**.

Chạy **4–5 lô song song** là vừa. Chúng độc lập nhau nên không tranh chấp.

## Khi một lô báo xong

```bash
PYTHONIOENCODING=utf-8 python data/huongdan/kho/congcu.py soat kNN   # tự soát lại, ĐỪNG tin báo cáo suông
PYTHONIOENCODING=utf-8 python data/huongdan/kho/congcu.py xong kNN   # chỉ luồng chính được gọi
git add -A && git commit …
```

⚠️ **Lô không được tự đánh dấu mình xong** — tự chấm điểm mình thì bộ soát mất hết ý nghĩa.
Đọc kỹ mục "chỗ tôi không chắc" trong báo cáo: lô động từ/tính từ gần như **không được bộ soát
đỡ** (`nouns.csv` chỉ có 382/703 từ là danh từ), nên đó là chỗ duy nhất bắt được lỗi nội dung.

## Khi HẾT 56 lô

Hỏi user trước, rồi:

```bash
PYTHONIOENCODING=utf-8 python data/huongdan/kho/congcu.py nap            # chạy khan
PYTHONIOENCODING=utf-8 python data/huongdan/kho/congcu.py nap --apply    # ghi thật + sync
python data/huongdan/kiemtra.py                                          # soát lại TRÊN THẺ THẬT
```

⚠️ **Thẻ trong Anki chưa bị đụng chữ nào.** User chốt: *"để riêng ra một chỗ, lúc nào xong toàn
bộ tôi sẽ nhờ bạn đẩy vào một thể"*. Chỉ chạy `--apply` khi user bảo.

Sau khi nạp xong toàn bộ 870 thẻ: **xoá khối CSS `mn-*` di sản** trong
`anki_tools/templates/card.css` (di sản của hướng mnemonic đã bỏ).

## Việc còn nợ

- ⚠️ **Lô k04 phình dài** — 13/15 thẻ vượt 12 KB (đỉnh `реплика` 16,9 KB) vì chồng **ba** khối
  hệ thống lên cùng một thẻ. Nội dung **không sai**, chỉ dài. Trần đã ghi vào README §2
  (6–10 KB, **tối đa 2 khối dùng chung mỗi thẻ**) và các lô sau phải theo. Lúc nào rảnh thì
  quay lại gọt k04: bỏ bớt khối thứ ba ở những thẻ mà nó không thật sự liên quan.
  Kiểm bằng `congcu.py dodai`.
- **Thẻ trùng do U+200B** (`петь`/`пить`) — `nap` đã ghi vào cả hai note nên không sót nội
  dung, nhưng bộ sưu tập vẫn thừa 2 thẻ. **Hỏi user** có muốn gộp không; đừng tự xoá thẻ.

## Bẫy đã dính, đừng dính lại

- **Console Windows là cp1252** — in tiếng Nga ra là `UnicodeEncodeError`.
  Luôn `PYTHONIOENCODING=utf-8`, và dữ liệu lớn thì ghi ra file.
- **Bash tool là Git Bash, KHÔNG phải PowerShell.** Đừng dùng here-string `@'…'@` cho commit
  message — nó tạo commit tên `@`. Dùng `git commit -F - <<'EOF'`.
- **Bộ sưu tập có thẻ TRÙNG do zero-width U+200B**: `петь`/`петь​`, `пить`/`пить​`. Anki coi là
  hai note, mắt thường không phân biệt được. `nap` đã xử lý (ghép theo khoá đã bỏ U+200B, ghi
  vào **cả hai** note) — đừng "sửa" nó về `findNotes` từng từ.
