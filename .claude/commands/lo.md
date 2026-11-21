---
description: Chạy lô soạn kho — đường thẳng 5 bước, từ chốt lô tới commit
argument-hint: [để trống = chạy lô kế tiếp trong hàng đợi]
---

# /lo — chạy một phiên soạn lô kho

**Đây là NƠI DUY NHẤT nói về việc chạy lô.** Đừng đi tìm file nào khác, kể cả `git log`.

Hai loại nội dung, đừng trộn: **§1–§3 là việc của LUỒNG CHÍNH** (bạn) · **§4 là luật bất biến
giao cho AGENT**. Nội dung thẻ trông thế nào là việc của `data/huongdan/README.md`, không phải
ở đây.

🔴 **Luồng chính KHÔNG soạn chữ nào và KHÔNG mở file lô** (~1 000 dòng/file). Gộp nhiều lô vào
một context làm chất lượng **nhạt dần** mà chính người soạn khó tự thấy — user không kiểm được
nội dung nên đây là kiểu xuống cấp nguy hiểm nhất. **Mọi lô chạy ở Opus 5.5** (`claude-opus-5-5`, user chốt
28/09): luồng chính không phải nó ⇒ dừng, bảo user `/model`; agent **bỏ trống `model`** để kế thừa luồng chính.

---

## §1. Năm bước — chạy đúng thứ tự, không bỏ bước

🔴 **Phiên chết ở đâu cũng chạy `xephangdoi.py` khan trước**: nó in bước kế. Lô đầu soạn trước
(ra học trước). Nguồn từ: `data/sach_b2.json` (QD-51). Từ user tự thêm qua bot thì bước 1–2 thay
bằng `congcu.py moi --apply` (>22 từ: tách tay trong `hangdoi.json`), các bước sau **ghi rõ id lô**.

```bash
K=data/huongdan/kho; export PYTHONIOENCODING=utf-8
# 1. CHỐT LÔ — khan rồi ghi. Có dòng "⚠️ HỌ TỪ BỊ XÉ" ⇒ gom tay trong hangdoi.json NGAY, trước bước 2.
python $K/xephangdoi.py chon N && python $K/xephangdoi.py chon N --apply
# 2. TẠO THẺ — ngược thứ tự lô, dừng ở lỗi đầu (vì sao: đầu file xephangdoi.py).
python $K/xephangdoi.py taothe --apply
# 3. GIAO — `giao` in va chạm + ỨNG VIÊN họ từ mọi lô chờ: đọc, lọc, khai khuôn vào lời nhắn §4.
#    Mỗi lô một agent, context trắng; giao HẾT trong MỘT tin nhắn rồi đứng im.
python $K/xephangdoi.py giao
# 4. CHỐT — agent báo xong ⇒ khan (chỉ soát) rồi --apply: soát → xong → nạp → kiemtra → dolo.tsv.
#    Lô ĐỎ ở lại `cho` kèm lý do. 🔴 CẤM `SendMessage` đánh thức agent ĐÃ XONG để hỏi số: ~120K
#    token/lần (20/11 đốt ~1,1M) — số đã nằm ở `B` cuối file lô, `chot` tự đọc.
python $K/xephangdoi.py chot && python $K/xephangdoi.py chot --apply
# 5. BA CỬA + COMMIT theo đường dẫn: file lô + hangdoi.json + dolo.tsv (L3, QD-10).
python soatkientruc.py && python -c "import bot, main" && python -m unittest discover -s tests
```

## §2. Quyết định cỡ lô — đã đo, đừng nghĩ lại

- **Giá tính theo SỐ LÔ, không theo số từ**: mỗi lô ~110–140K token bất kể 12 hay 20 từ. Lô to
  rẻ hơn rõ rệt trên mỗi từ.
- **Trần 22 từ/lô. Điểm rẻ nhất đã đo là 19 từ/lô** (7,4K token/từ, 11/08). **Đừng chạy lô dưới
  10 từ** — đắt gấp ~3 lần mỗi từ; để đó, lệnh `moi` tự gộp dồn vào lô sau.
- **Hạn mức: ~10 lô/phiên** (user đo 16/10). Token/lô ~105–112K: đổi ở gói, lô không rẻ đi.
- **Dấu hiệu "lô nhỏ soi kỹ hơn" đã bị số liệu bẻ** (0,29 lỗi/từ ở lô 14 thấp hơn 0,46 ở lô 12).
  Đừng hạ trần cỡ lô vì nó. Muốn lật thì **đo ra số khác** từ `dolo.tsv`, đừng lập luận suông.
- **Chia lô theo TAG CHỦ ĐỀ, giữ họ từ chung một lô.** Tách họ từ ra hai agent là cơ chế đã làm
  **11 tên tháng viết 4 kiểu** mà không lô nào sai cả. Cặp thể (`лечь`↔`ложиться`) cũng vậy.
- **Đừng đoán nội dung lô từ tên topic** — đọc `congcu.py tiep kNN` rồi hãy mô tả trục.

## §3. Bẫy của LUỒNG CHÍNH — thứ không cửa soát nào canh

- 🔴 **ĐỌC FIELD THẬT CẢ HỌ TỪ trước khi giao, đừng chỉ đọc lô sắp giao.** Agent chỉ thấy lô mình
  nên **không thể** bắt lỗi xuyên lô. Và đọc HẾT họ rồi mới khai khuôn — suy khuôn từ 2–3 từ đã
  làm khai sai hai lần liên tiếp. Grep gốc từ phải tính cả tiền tố (`startswith('ход')` sót `выход`).
- 🔴 **Quét "chứa chuỗi" MÙ với từ cùng gốc không mang mặt chữ** (`животное` ↔ `жить`/`жизнь`).
  ⇒ Khai với agent là **"máy tìm được X"**, đừng khai **"không có"**. Danh sách giao là **SÀN**.
- 🔴 **Đừng tự viết đoạn đo va chạm** — `giao`/`vacham` đã lọc đủ 4 badge và ghi trạng thái lô
  bên kia; tự viết là dẫm lại bẫy `Gender` (field không có, trả RỖNG im lặng).
- 🔴 **Gỡ va chạm bằng RÚT GỌN, đừng thêm chữ** (xác nhận 4 lần): bỏ nghĩa nới rộng / bỏ lời giải
  thích lẫn trong đề bài làm cụm trùng biến mất mà không thêm chữ nào.
- 🔴 **CÓ LÔ CHẠY SONG SONG THÌ ĐỪNG `git add -A`** — nó quét cả file đang soạn dở vào commit,
  HEAD giữ ảnh chụp còn lỗi. Commit theo đường dẫn cụ thể.
- 🔴 **Đuôi phiên là chỗ đắt nhất** (mỗi lượt chat gửi lại cả hội thoại). Trước khi sửa tài liệu,
  **đo trần trước** (`len()` file so `soat_nguong.json`) rồi sửa **một lượt**, đừng để cửa soát
  dạy mình từng cái một. Gặp lỗi ⇒ sửa NGAY (CLAUDE.md mục 4), nhưng **giao lô xong đã** (từng đốt 5h).
- 🔧 **Mạng chớp làm cả hai agent chết cùng lúc** lúc sắp `Write` file to. Gặp thì **`SendMessage`
  cho chạy tiếp**, đừng spawn agent mới — ngữ cảnh còn nguyên.
- 🔧 **Console Windows là cp1252** ⇒ luôn `PYTHONIOENCODING=utf-8`. **Bash tool là Git Bash**:
  commit dài dùng `git commit -F - <<'EOF'`, đừng dùng here-string `@'…'@` của PowerShell.

## §4. Khuôn lời nhắn giao agent — luật BẤT BIẾN, đổi `kNN` rồi gửi nguyên

> Soạn ô "Hướng dẫn" cho lô **kNN**, dự án Anki học tiếng Nga tại `d:\Desktop\ANKI`. Bạn là người
> soạn một lô, context trắng — mọi thứ cần biết nằm trong file, đừng đoán theo trí nhớ.
>
> **1. Đọc spec TRƯỚC KHI viết:** `data/huongdan/README.md` — §2 (ba mục cốt lõi + ba con số
> cứng + bản mẫu `сожаление`), §2c (sửa field `Vietnamese`), §3, §7. 🔴 **Đừng mở `MAU.py` hay
> `k01_actions.py`** — chuẩn CŨ dài gấp 4–5 lần, chép theo là hỏng.
>
> 🔴 **BA CON SỐ CỨNG:** ① vừa **MỘT màn hình iPhone — trần 700px**, nhắm <600px (đừng canh
> byte, byte là đại lượng sai) · ② tối đa **2 ô đỏ** (`hd-warn`) · ③ **mặc định KHÔNG có khối
> hệ thống dùng chung**. Biến cách/số nhiều **đúng quy tắc thì BỎ**, chỉ liệt kê khi bất thường.
> Ba mục cốt lõi: **Chẻ từ → Cách nhớ → Họ hàng**.
>
> **2. Đề bài:** `PYTHONIOENCODING=utf-8 python data/huongdan/kho/congcu.py tiep kNN`
> Mỗi từ in kèm `BAT THUONG` (bảng chia lệch quy tắc → viết **một câu chú ý**) và
> `CUM CO DINH`/`CACH DUNG` (ứng viên ô đỏ). Là văn từ điển thô — **đừng chép nguyên**.
> Mục **"Họ hàng" cố ý không có dữ liệu máy**, tự nghĩ. Từ thật sự không có họ (gốc trơn, hư từ,
> từ mượn đứng một mình) thì **bỏ hẳn mục đó** — nhưng vắng phải là lựa chọn có ý thức.
>
> **3. Soạn** `data/huongdan/kho/kNN_<topic>.py` — CHỈ chứa `S = {...}`, `V = {...}`, `B = {...}`, không
> import, không `main()`, không gọi Anki.
> **Việc thứ hai bắt buộc — field `Vietnamese` (§2c):** dòng tiếng Việt là **đề bài của deck
> `1-go`, user GÕ từ Nga từ nó**. 🔴 **THUẦN DANH SÁCH NGHĨA, ngăn bằng dấu phẩy, KHÔNG GÌ KHÁC.**
> **CẤM bốn thứ:** ① nhãn từ loại/giống/thể/phản thân (bốn badge đã in sẵn trên mặt đề bài) ·
> ② cách chi phối (`+ C4`) · ③ lưu ý cách dùng, ví dụ, **mọi ghi chú trong ngoặc** · ④ mệnh đề
> phủ định `(không phải «X»)`. Chỉ nghĩa thông dụng mà gloss tiếng Anh xác nhận được; **đừng nới
> rộng**. Trùng hết nghĩa mà badge cũng không tách ⇒ **BÁO LÊN, cấm tự thêm ngoặc**.
>
> **4. Tự soát:** `congcu.py soat kNN` — sửa tới khi **cả ba** mục đầu `(khong co)`, rồi **đọc
> bằng mắt** danh sách "PHAI DOC BANG MAT". Và `congcu.py dodai kNN` phải báo
> `QUA 1 MAN HINH (700px): 0` **và** `QUA 2 O DO: 0`.
> 🔴 **Cửa soát báo lệch thì SỬA DỮ LIỆU CỦA MÌNH, đừng nới `MIEN_TRU`** — nới miễn trừ để lô mình
> xanh là làm mù cửa cho MỌI lô sau. Ngoại lệ duy nhất: **từ đồng tự** thật, kèm lý do và báo lên.
>
> **5. DỪNG** — không sửa `hangdoi.json`, không commit, không `nap`, không đụng Anki.
>
> **Báo cáo — GHI VÀO FILE TRƯỚC.** Cuối file lô thêm
> `B = {"docbangmat": n, "loitubat": n, "nguonsai": n, "baolen": ["một dòng mỗi điều"]}` —
> lời nói trôi mất, file thì không.
> Ba con số: ① số mục "PHẢI ĐỌC BẰNG MẮT" · ② số **lỗi nội dung bạn tự đọc lại rồi tự sửa**
> (giải thích sai, từ nguyên sai, dạng chia sai) · ③ số lần **bác dữ liệu từ điển sai** thay vì
> chép theo. 🔴 **Đếm thật, kể cả khi bằng 0** — 0 vì ngại nói thì làm hỏng phép đo.
> `baolen`: trùng nghĩa không gỡ được · chỗ KHÔNG chắc · `V` cần duyệt.

## §5. Trạng thái nằm ở đâu

| File | Là gì |
|---|---|
| `hangdoi.json` | các lô + `trangthai: cho\|xong\|dat` + `daNap` — **nguồn sự thật duy nhất**. `dat` = thẻ đã đạt chuẩn sẵn, không file, `nap` bỏ qua |
| `tudien.json` | ảnh chụp từ: WordClean, trọng âm, từ loại, gloss Anh (không có nghĩa Việt — lấy thẳng từ thẻ Anki, QD-27) |
| `kNN_*.py` | nội dung đã soạn, dữ liệu thuần. **Đường cứu hộ**: `nap --tatca` dựng lại toàn bộ ô Hướng dẫn từ đây |
| `dolo.tsv` | sổ đo từng lô — nơi duy nhất trả lời "lỗi/từ có giảm khi lô to lên không" |

`congcu.py trangthai` in tất cả, và **tự nhắc khi có từ mới** — khỏi phải nhớ chạy lệnh nào.
