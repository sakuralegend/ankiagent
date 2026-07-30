# 🗺️ KIẾN TRÚC — hệ thống là gì, chạy thế nào, sửa ở đâu

> **Đọc file này khi:** sửa việc **xuyên mảng**, hoặc đụng một file đã quá ngưỡng ở `SONO.md`,
> hoặc lần đầu vào dự án. Việc trong một mảng thì `CLAUDE.md` là đủ.
>
> **File này CỐ Ý không chứa con số đếm được** (số dòng, số file, số lô, số thẻ). Mọi dòng ở đây
> phải qua được phép thử: *"còn đúng nguyên văn sau khi thêm 10 lô mới và 5 lệnh bot mới không?"*
> Con số trôi từng ngày — đó chính là thứ đã giết `README.md` cũ. Cần số thì chạy lệnh, đừng chép
> vào đây. Lịch sử → `CHANGELOG.md` · vì sao chọn A không chọn B → `QUYETDINH.md` · chuẩn nội dung
> thẻ → `data/huongdan/CHUAN.md` · cách soạn một lô → `data/huongdan/README.md`.

---

## 1. Bốn mảng, và chiều import một chiều

Hệ thống là **bốn mảng gần như độc lập**, gặp nhau CHỈ ở một chỗ: **bộ sưu tập Anki**. Không mảng
nào gọi hàm của mảng khác — chúng chỉ cùng đọc/ghi lên cùng một kho thẻ.

| Mảng | Thư mục | Nuôi cái gì |
|---|---|---|
| Bot Telegram | `tgbot/` | mọi thứ user chạm từ điện thoại |
| Dây chuyền soạn kho | `data/huongdan/` | field `HuongDan` của thẻ từ vựng, soạn theo lô |
| Thẻ ngữ pháp | `grammar_forms/` | model thẻ riêng cho dạng bất quy tắc |
| Lõi dùng chung | `anki_tools/` | cào · dựng HTML · gọi AI · nói chuyện với Anki |

**Chiều import là MỘT CHIỀU và không được phép đảo:**

```
tgbot/  ─┐
data/huongdan/  ─┼─→  anki_tools/  ─→  (không import ngược lên bất cứ mảng nào)
grammar_forms/  ─┘
```

`anki_tools` không biết bot tồn tại, không biết dây chuyền kho tồn tại. Đó là thứ giữ cho một thay
đổi ở bot không giết được lô đang soạn tối nay. Bên trong `tgbot/` còn một tầng nữa:
`core ← flow_* ← dispatch ← app` — **flow không gọi flow**, vì hai màn hình dính nhau thì sửa một
cái là cái kia đổi theo âm thầm.

Chỗ đặt code mới: chỉ một mảng dùng → để trong mảng đó; **từ hai mảng trở lên thật sự cần** →
`anki_tools/`. Không có mảng thứ năm nào được sinh ra mà không ghi `QUYETDINH.md`.

## 2. Dòng dữ liệu — một từ đi từ đâu tới đâu

```
user gõ từ (Telegram / CLI)
   └→ pymorphy3 đưa về dạng từ điển (offline, tất định — không giao AI)
      └→ OpenRussian: nghĩa · trọng âm · bảng chia · ví dụ
         └→ AI: chọn nghĩa, dịch tiếng Việt, chọn chủ đề
            └→ TTS: OpenRussian đọc trước, hụt thì Google
               └→ AnkiConnect ghi thẻ  ─→  Anki trên VPS  ─→  AnkiWeb  ─→  iPhone
```

Hai điều phải nhớ về khúc cuối: **AnkiWeb luôn là bản mới nhất** (bot sync ngay sau mọi thao tác),
nên trên điện thoại luôn chọn *Download from AnkiWeb*. Và **Anki trên VPS chạy trong Docker** — mọi
đường dẫn file đưa cho AnkiConnect phải theo góc nhìn *của Anki trong container*, không phải của
tiến trình gọi nó.

## 3. Các cửa ra thế giới ngoài (L1)

Mỗi tài nguyên ngoài chỉ có **một cửa**. Ai cần thì import; cấm mở cửa riêng.

| Tài nguyên | Cửa duy nhất |
|---|---|
| AnkiConnect | `anki_tools/anki_client.py` — địa chỉ cổng định nghĩa ở `anki_tools/config.py` |
| Mạng OpenRussian | `anki_tools/grammar.fetch_page` — nơi DUY NHẤT gọi mạng, không cắt không chọn sẵn |
| AI API | `anki_tools/ai_client.py` |
| TTS | `anki_tools/audio.py` |

**Ngoại lệ đã hợp thức, đừng "sửa" nó:** `data/huongdan/kho/` có wrapper AnkiConnect riêng, CỐ Ý
đóng băng (`QD-01`) — để một thay đổi ở bot không giết lô đang chạy. Ngoại lệ này hết hạn khi xong
toàn bộ lô soạn kho.

Cửa nào bị mở lậu thì `soatkientruc.py` mục S1 kêu.

## 4. Coupling ẩn — chỗ hai mảng dính nhau mà không qua import

Đây là loại phụ thuộc nguy hiểm nhất vì **grep `import` không thấy**:

- **`data/nouns.csv`**: `grammar_forms/irregular_plurals.py` **tải nó về** (dump từ GitHub);
  `anki_tools/grammar.py` **đọc nó** để biết từ nào chỉ dùng số nhiều; dây chuyền kho cũng đọc nó
  để soát trọng âm. Đổi định dạng file này là chạm cả ba mảng cùng lúc.
- **`data/grammar_cache.json`**: ảnh chụp OpenRussian trên máy soạn kho. Bot chạy trên VPS ghi dữ
  liệu ngữ pháp vào **field ẩn của chính thẻ**, nên cache trên laptop luôn hụt đúng bằng số từ mới
  thêm qua bot — *hụt ở đây không có nghĩa là thiếu dữ liệu*.
- **`hangdoi.json` là nguồn sự thật duy nhất** về trạng thái từng lô; `tudien.json` là ảnh chụp
  nghĩa/trọng âm. Thêm từ mới phải chạm **cả hai**, thiếu một cái thì công cụ in ra `?` và người
  soạn sẽ soạn mò.

⚠️ `nouns.csv` và `grammar_cache.json` **cùng thượng nguồn OpenRussian** — hai nguồn trùng nhau
KHÔNG chứng minh dữ liệu đúng. Đối chiếu chéo chúng không bắt được lớp lỗi có sẵn từ nguồn.

## 5. Vòng import thật, và cách đang bẻ

`anki_tools/wiktionary.py` import `grammar` ở **mức module**; `grammar.py` cần `wiktionary` để vá
chỗ OpenRussian thiếu, nên nó import **ở trong hàm**, không ở đầu file. Đó là một vòng thật, đang
bị bẻ có chủ ý — **đừng "dọn" bằng cách kéo import lên đầu file**, làm vậy là gãy ngay lúc khởi động.

(Trong `tgbot/` cũng có một import nằm trong hàm với lý do ghi là "tránh import vòng" — chỗ đó
**không** có vòng thật; xem `SONO.md`.)

## 6. Vùng im lặng — hỏng mà không ai báo

Đây là danh sách thứ đã **thật sự làm mất dữ liệu**. Chạm vào các vùng này thì theo luật `L4`:
việc đứng riêng một mình, backup trước, kiểm sau — và với AI thì **DỪNG LẠI HỎI trước khi chạy**.

| Vùng | Triệu chứng khi hỏng | Cứu bằng gì |
|---|---|---|
| Đổi/thêm/xoá **field hay model Anki** | VPS kẹt `Sync status 2` **không báo Telegram**; điện thoại hiện bảng chọn chiều sync | `journalctl -u anki-bot` ngay sau khi đổi; nhìn tận mắt màn hình Anki VPS bằng `vnc.bat` |
| **Full sync chọn nhầm chiều** | Ghi đè sạch bản còn lại, không lùi được | Backup `.apkg` theo ngày; đường khôi phục ghi ở `VPS_SETUP.md` |
| **Xoá/ghi đè hàng loạt** thẻ thật | Nội dung mất không tiếng kêu | Backup tay (`/backup`) trước khi chạy |
| Chạy lại **script lô thế hệ 1** | Xoá bảng chia trên thẻ thật, im lặng | Đã tháo ngòi (`QD-03`); `soatkientruc.py` S7 canh guard |
| Hai hàm cùng vai **lệch nhau** (vd chuẩn hoá `ё`) | Thẻ sai âm thầm, không lỗi nào nổ | Đo bằng script chỉ đọc trước khi gộp, không gộp mò |

🔧 **`vnc.bat` là đường DUY NHẤT nhìn thấy màn hình Anki trên VPS.** Khi nghi kẹt sync mà log không
nói gì, đó là công cụ cuối cùng còn lại — lý do nó được giữ ở thư mục gốc.

## 7. Năm bất biến của dây chuyền soạn kho

Dây chuyền này là phần **có kỷ luật nhất** của dự án, và nó giữ được nhờ đúng năm điều dưới. Sửa
công cụ soạn kho mà phá một trong số này là phá thứ đang chạy tốt:

1. **Lô soạn xong là dữ liệu thuần** — file chỉ chứa `S = {...}`, không boilerplate, không tự gọi Anki.
2. **Người soạn lô không chạm Anki, không chạm git** — chỉ đẻ file dữ liệu. Việc đẩy vào thẻ là của
   lệnh `nap`, chạy sau khi đã soát.
3. **`nap` chỉ đọc lô đã đánh dấu xong** — lô đang soạn dở không thể lọt vào thẻ thật.
4. **Sổ cái `daNap` chống nạp hai lần**; thiếu note thì **không** được đánh dấu đã nạp — hàng đợi
   lệch bộ sưu tập là thứ phải hiểu trước khi chạy tiếp.
5. **Mỗi lô một context trắng** — gộp nhiều lô vào một phiên làm chất lượng nhạt dần, mà nhạt dần
   thì chính người soạn khó tự thấy.

Và một giới hạn phải biết khi đọc kết quả soát: **cửa soát chỉ soi phần người soạn VIẾT** — bảng
chia do máy nối vào lúc ghi thẻ nằm ngoài tầm nhìn của nó.

## 8. Điểm vào — cái gì chạy được

Thư mục gốc chứa **đúng ba** file `.py` — không hơn (`L2`, canh bằng mục S6):

| Chạy cái gì | Để làm gì |
|---|---|
| `python bot.py` | Bot Telegram (bản chạy 24/7 trên VPS) |
| `python main.py` | Thêm từ bằng dòng lệnh trên PC |
| `python soatkientruc.py` | Cửa soát kiến trúc — bậc 1 của mọi lệnh nghiệm thu |
| `.\deploy.ps1` | Soát → import-check → push → VPS kéo code → restart bot |

Mọi thứ khác nằm ở hai thư mục theo **tuổi thọ**, không theo chức năng:

- **`scripts/`** — script vận hành còn dùng lại (gắn tag, dựng cây deck, vá audio, điền badge…).
  Đều **idempotent** và mặc định chạy khan, phải thêm `--apply` mới ghi thật.
- **`_daxong/`** — script sinh ra để chạy **một lần**, đã khai tử. Giữ để đọc lại, không để chạy lại.

⚠️ Script ở hai thư mục này **phải tự chèn đường dẫn gốc vào `sys.path`** (ba dòng đầu file) —
chúng import `anki_tools`, mà thư mục cha không nằm sẵn trên đường tìm module như hồi còn ở gốc.
Thêm script mới vào đây mà quên ba dòng đó thì nó chạy được trên máy bạn đúng một lần, rồi gãy.

---

## Khối máy đọc — `soatkientruc.py` mục S8 so khối này với thực tế

Tài liệu nói dối thì máy chỉ mặt. Sửa cấu trúc dự án mà quên sửa khối dưới đây là **ĐỎ**.

```soat-manifest
{
  "goi": ["anki_tools", "tgbot", "grammar_forms"],
  "diem_vao": ["bot.py", "main.py", "soatkientruc.py"],
  "du_lieu_chung": [
    "data/nouns.csv",
    "data/grammar_cache.json",
    "data/huongdan/kho/hangdoi.json",
    "data/huongdan/kho/tudien.json"
  ],
  "cong_cu_cuu_ho": ["vnc.bat"]
}
```
