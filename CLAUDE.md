# CLAUDE.md — luật làm việc trong repo này (đọc trước khi làm bất cứ gì)

## ⛔ VIỆC KẾ TIẾP — đọc mục này trước mọi thứ khác (đặt 30/07/2026)

**LÔ SOẠN KHO ĐANG ĐÓNG BĂNG.** Đừng chạy `congcu.py tiep`, đừng soạn lô mới, kể cả khi
`data/huongdan/kho/TIEPTUC.md` nói lô kế tiếp là `k17`. Chỉ mở băng khi user nói rõ **"mở lại lô"**.

Đang thi hành **đợt dọn dự án G0→G4**, chia làm 3 phiên:

| Phiên | Nội dung |
|---|---|
| **A′ = 2 vá 🔴 + G0 + G1** | ← **BẮT ĐẦU TỪ ĐÂY** nếu chưa có commit nào mang `(G0)` |
| B = G2 + G3 mở rộng | tài liệu (`KIENTRUC.md`) + dọn gốc **về đúng 3 file `.py`** |
| C = G4 + tổng kết | phiên duy nhất chạm bot 24/7 |

**Phiên A′ mở đầu bằng hai món 🔴 trong `SONO.md`** — làm TRƯỚC G0 (~40 phút), vì cả hai là bảo hiểm
cho chính đợt dọn: ① ghim `requirements.txt` bằng `==` (deploy đang tự `pip install` mỗi lần ⇒ một bản
lib mới có thể giết bot mà nguyên nhân không nằm trong diff của bạn); ② khôi phục thử một `.apkg` vào
profile Anki RỖNG rồi ghi các bước vào `VPS_SETUP.md` (hiện **không có đường khôi phục nào**).
Cuối phiên A′ thêm ~20 phút: script CHỈ ĐỌC đo bất đồng 4 luật chuẩn hoá tiếng Nga (xem `SONO.md`).

**Hai file phải đọc trước khi bắt tay:**
1. `_fable_plan.md` — đặc tả G0–G4: làm gì, file nào, kiểm chứng thế nào, cái gì KHÔNG làm
2. `C:\Users\Asus\.claude\plans\c-v-sau-m-t-linear-emerson.md` — chia phiên A/B/C, thứ tự từng bước, trần chi phí

**Biết đang ở đâu:** `git log --oneline -20 | Select-String "\(G[0-4]\)"` — G nào đã có commit là đã
xong. Chưa có gì ⇒ chạy **phiên A, bước A1**: chụp baseline vào `_baseline_don.md` **TRƯỚC khi sửa
bất cứ thứ gì**.

**Hai trần cứng của phiên A:** ① đọc 12 file `data/huongdan/lo01…lo12_*.py` bằng `limit=15`, **đừng
đọc cả file** (chúng chứa ~270 KB nội dung thẻ ≈ 70K token, mà ta chỉ chèn 3 dòng đầu); ② quá **4
vòng** gỡ lỗi `soatkientruc.py` thì dừng phiên, commit thứ đang có — nó là file độc lập, phiên sau
đọc lại làm tiếp không mất gì.

### 🔀 Model nào cho bước nào — AI PHẢI TỰ NHẮC, user không cần nhớ

| Bước | Model | Vì sao |
|---|---|---|
| Ghim `requirements.txt` · khôi phục thử backup · **G0** | **Sonnet** | thi hành theo spec, sửa cơ học |
| **G1** viết `soatkientruc.py` | **Opus** | thiết kế + gỡ lỗi nhiều vòng; cửa soát kêu oan còn tệ hơn không có cửa |
| Đo bất đồng chuẩn hoá | **Sonnet** | script chỉ đọc |
| **G2** viết `KIENTRUC.md` | **Opus** | việc khó là quyết định cái gì KHÔNG viết vào; sai tầng là đẻ ra README thứ hai |
| **G3** dọn gốc · **G4** alias + deploy | **Sonnet** | `git mv` + diff nhỏ; an toàn nằm ở canary chứ không ở model |

**Luật cho AI:** trước khi bắt tay MỖI bước trên, tự đối chiếu model đang chạy với bảng này. Lệch thì
**DỪNG LẠI, nói user gõ `/model` đổi trước**, đừng làm rồi mới báo. Nguyên tắc chung ngoài bảng:
**Opus khi việc là QUYẾT ĐỊNH, Sonnet khi việc là THI HÀNH theo spec đã có.**

**Xong đợt dọn thì xoá nguyên mục này** và trả `TIEPTUC.md` về vai trò cũ.

---

Sổ tay đầy đủ: `CACHLAM.md` (luật `L1`–`L5`, có số hiệu để viện dẫn). Quyết định kỹ thuật: `QUYETDINH.md` (`QD-nn`). Nợ kỹ thuật: `SONO.md`. Mọi lần sửa xong: ghi `CHANGELOG.md` (mới nhất trên cùng, kèm **vì sao**).

## 5 luật

- **L1 — Một cửa cho tài nguyên ngoài.** AnkiConnect → `anki_tools/anki_client.py`; cào OpenRussian → `grammar.fetch_page`; AI API → `ai_client`. CẤM viết wrapper mới / trỏ thẳng `:8765`. Ngoại lệ duy nhất: `data/huongdan/kho/` cố tình đóng băng (QD-01).
- **L2 — Script một lần phải chết trong cùng commit.** Đặt tên `_va_<việc>.py`, chạy xong chuyển vào `_daxong/` ngay. Thư mục gốc chỉ chứa điểm vào đang sống (`bot.py`, `main.py`).
- **L3 — Mọi việc sửa code kết thúc bằng mục "Lệnh nghiệm thu:" và CHẠY nó.** Tối thiểu: `python -c "import bot, main"`.
- **L4 — Vùng im lặng đứng riêng một mình** (danh sách bên dưới): không gộp việc khác, backup trước, kiểm sau.
- **L5 — Rẽ nhánh thì ghi `QUYETDINH.md`**: mục 4 dòng (Chọn / Thay vì / Vì / Hết hạn), số hiệu `QD-nn`, commit thi hành nhắc số hiệu.

## DỪNG LẠI HỎI trước khi

1. Đổi/thêm/xoá field của model Anki hay bất cứ gì kích full sync (schema mod → VPS kẹt "Sync status 2" **im lặng**, đã xảy ra thật).
2. Xoá hoặc ghi đè hàng loạt thẻ/note thật.
3. Tạo file `.py` mới ở thư mục gốc.
4. Viết hàm thứ hai cùng vai với hàm đã có — trước khi viết bất cứ gì, **liệt kê hàm/module có sẵn dùng lại được**; có cái gần giống thì mở rộng nó.
5. Đụng hạ tầng/repo ngoài phạm vi việc được giao.

## Chỗ đặt code (4 mảng, gặp nhau CHỈ ở bộ sưu tập Anki)

- Chỉ bot dùng → `tgbot/` · chỉ dây chuyền soạn kho → `data/huongdan/` · chỉ thẻ ngữ pháp → `grammar_forms/` · từ HAI mảng trở lên thật sự cần → `anki_tools/`.
- Chiều import một chiều: các mảng import `anki_tools`; `anki_tools` không import ngược.
- File >400 dòng: đừng thêm vào nữa, ghi `SONO.md`; >700 dòng: tách trước khi thêm.
- Chép-dán chỉ hợp lệ khi là **ảnh chụp cố ý**: dòng đầu file ghi `# ẢNH CHỤP từ <gốc> ngày <d>, lý do, hết hạn khi <sự kiện>` + một mục QD. Còn lại: import.
- Agent soạn lô kho: KHÔNG chạm Anki, KHÔNG chạm git, chỉ đẻ file dữ liệu.

## Nghiệm thu (khai cuối mỗi việc)

Ba mục: **đã đổi gì (từng file, vì sao) · lệnh nghiệm thu · rủi ro im lặng nào có thể có**. Sửa ít file nhất có thể; diff to hơn lời hứa thì giải thích trước khi nhận.

## Bẫy đã trả học phí

- Chuẩn hoá tiếng Nga phải `unicodedata.normalize("NFC", ...)` — hai hàm lệch nhau là `ё` hỏng **im lặng**.
- Anki trên VPS chạy trong Docker (uid 1000): đường dẫn file trong lệnh AnkiConnect theo góc nhìn **của Anki trong container** + quyền đọc được; luôn thử thật trên VPS.
- Callback data Telegram trần 64 byte → nút mang chỉ số, không mang chuỗi dài.
- Mọi `findNotes` phải lọc `note:"<model>"` — một từ có thể có cả thẻ từ vựng lẫn thẻ ngữ pháp.
- `getReviewsOfCards` phải truyền int, không truyền str.
- Cảnh báo cho user đi qua `tgbot/alerts.py`, không `send_message` thẳng (chống spam).
- KHÔNG in nghiêng chữ Nga trong HTML thẻ (đổi mặt chữ, mất dấu trọng âm).
