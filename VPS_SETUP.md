# Hướng dẫn đưa bot lên VPS (làm 1 lần duy nhất)

> Làm tuần tự từ trên xuống. Mỗi bước đều có lệnh sẵn để copy-paste.
> Chỗ nào ghi **[PC]** là gõ trên máy tính (PowerShell), **[VPS]** là gõ trong cửa sổ SSH.

## Chuẩn bị sẵn
- IP VPS + mật khẩu root (nhà cung cấp gửi)
- File `.env` đã có sẵn trong thư mục project trên PC
- Tài khoản AnkiWeb (email + mật khẩu)

---

## Bước 1 — [PC] Vào VPS lần đầu

Mở PowerShell, gõ (thay IP nếu khác):

```powershell
ssh root@161.248.146.56
```

- Lần đầu nó hỏi `Are you sure...?` → gõ `yes` → Enter.
- Nhập mật khẩu root (gõ không hiện gì là bình thường) → Enter.
- Thấy dấu nhắc `root@...:~#` là đã vào được VPS.

## Bước 2 — [VPS] Tạo chìa khóa để VPS tải code từ GitHub

Repo GitHub là private nên VPS cần "chìa khóa" (deploy key) để đọc. Dán từng lệnh:

```bash
ssh-keygen -t ed25519 -N "" -f ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub
```

Nó in ra 1 dòng bắt đầu bằng `ssh-ed25519 AAAA...` → **bôi đen copy cả dòng**.

Rồi trên trình duyệt:
1. Vào `https://github.com/sakuralegend/ankiagent/settings/keys`
2. Bấm **Add deploy key**
3. Title: `vps` — Key: dán dòng vừa copy — **KHÔNG** tick "Allow write access"
4. Bấm **Add key**

## Bước 3 — [VPS] Tải code về và cài đặt

```bash
git clone git@github.com:sakuralegend/ankiagent.git /root/ankiagent
```
(nó hỏi `Are you sure...?` → gõ `yes`)

```bash
cd /root/ankiagent
bash setup_vps.sh
```

Chờ 3–5 phút. Script tự làm: cài Docker, tạo swap 2GB, kéo container Anki, cài thư viện Python, cài service bot. Cuối cùng in ra "✅ CÀI ĐẶT XONG".

## Bước 4 — [PC] Copy file bí mật .env lên VPS

Mở **PowerShell MỚI trên PC** (đứng ở thư mục project `d:\Desktop\ANKI`):

```powershell
scp .env root@161.248.146.56:/root/ankiagent/.env
```

## Bước 5 — Đăng nhập AnkiWeb (1 lần duy nhất, qua VNC)

Anki trong container cần đăng nhập AnkiWeb để sync. Làm như sau:

**5a.** [PC] Tải VNC Viewer (miễn phí): https://www.tightvnc.com/download.php
   → chọn bản Installer 64-bit, cài chỉ cần **TightVNC Viewer** (bỏ tick Server nếu được hỏi).

**5b.** [PC] Mở PowerShell, tạo "đường hầm" tới VPS (cửa sổ này phải để mở suốt lúc dùng VNC):

```powershell
ssh -L 15900:127.0.0.1:5900 root@161.248.146.56
```

(dùng cổng 15900 phía PC vì cổng 5900 trên Windows thường bị hệ thống giữ,
sẽ báo `bind ... Permission denied` — nếu 15900 cũng bị, đổi số khác, vd 25900)

**5c.** [PC] Mở TightVNC Viewer → Remote Host gõ: `localhost::15900` → Connect.
   (chú ý 2 dấu hai chấm) → Hiện ra cửa sổ Anki đang chạy trên VPS.

**5d.** Trong cửa sổ Anki đó:
1. Bấm nút **Sync** (biểu tượng vòng tròn 2 mũi tên, góc trên phải)
2. Nhập email + mật khẩu AnkiWeb
3. Nếu nó hỏi chọn hướng đồng bộ → chọn **Download from AnkiWeb**
   (để kéo toàn bộ thẻ hiện có của bạn về VPS)
4. Chờ sync xong (có audio/media thì hơi lâu), rồi đóng VNC Viewer.

## Bước 5b — [VPS] Lưới an toàn (setup_vps.sh đã tự làm, đây là để KIỂM)

`setup_vps.sh` bước [6/6] tự cài bốn thứ dưới đây. Chúng **không cần thiết để bot chạy**, nhưng
thiếu chúng thì hệ thống mất lưới an toàn **trong im lặng** — nên sau khi cài xong hãy kiểm:

```bash
systemctl list-unit-files | grep anki-bot-alert   # chuông báo khi bot chết
crontab -l | grep canhbao                          # vòng kiểm 15 phút
ls /root/anki-cache/                               # cache bot, NGOÀI repo (QD-05)
grep SystemMaxUse /etc/systemd/journald.conf       # trần dung lượng log
```

Thử chuông báo có thật sự tới điện thoại không (nên làm một lần):

```bash
systemctl start anki-bot-alert.service   # phải nhận được tin Telegram
```

⚠️ **Vì sao phải kiểm:** bốn thứ này từng chỉ được cấu hình bằng tay và không ghi ở đâu — dựng lại
máy mới là mất sạch mà không ai biết. Đúng loại lỗi "sao lưu chưa từng khôi phục thử", ở tầng cao
hơn. Nay đã tự động hoá trong `setup_vps.sh`, nhưng vẫn kiểm vì tự động hoá cũng hỏng được.

## Bước 6 — [VPS] Khởi động bot

```bash
systemctl start anki-bot
journalctl -u anki-bot -f
```

Thấy dòng `🚀 Bot đang chạy (long polling)` là xong. Bấm `Ctrl+C` để thoát xem log (bot vẫn chạy).

## Bước 7 — Kiểm tra từ điện thoại

Mở Telegram → tìm bot của bạn → gõ `/start` → gõ thử 1 từ tiếng Nga (vd `привет`).
Bot trả về thẻ mới + tự sync. Mở app Anki trên iPhone → bấm sync → thấy thẻ. 🎉

---

# Dùng hằng ngày

| Muốn làm gì | Gõ trong Telegram |
|---|---|
| Bắt đầu phiên | nhắn gì đó → bấm nút chọn deck (📂 có sẵn — liệt kê hết / ➕ tạo mới) |
| Thêm từ | gõ thẳng từ đó, vd `хороший` |
| Từ không có trên OpenRussian | AI đoán từ nguyên mẫu → bấm nút ✅ xác nhận / 🚫 Hủy |
| Đổi deck | `/deck` (hoặc nút 📚 trong menu) → bảng chọn deck bằng nút |
| Thẻ AI bị khuyết (thiếu ví dụ) | bot cảnh báo kèm 2 nút: 🔄 Làm lại thẻ / ⏭ Bỏ qua |
| Làm lại thẻ đã có | `/sua` → bot hỏi từ → gõ từ → cào lại + AI sinh lại, **giữ nguyên tiến trình học** |
| Làm lại TOÀN BỘ deck (ít dùng) | `/suadeck` → chọn deck → xác nhận → tiến độ tự cập nhật, có nút ⏹ Dừng |
| Thẻ ngữ pháp (số nhiều bất quy tắc) | `/dacbiet` → ➕ thêm 1 từ / 📋 thêm loạt / 🔄 làm lại / 🩹 vá thẻ thiếu |
| Sao lưu ngay | `/backup` — bấm **trước** khi làm gì mạo hiểm |
| Menu nút bấm | `/menu` (3 nút chính; công cụ sửa lỗi nằm sau nút 🛠) |
| Ép sync ngay | `/sync` |

Nghỉ >3 phút: bot tự reset phiên (chỉ quên deck đang chọn, thẻ không mất gì)
và gửi đúng 1 tin: báo đã reset + menu nút bấm.

# Khi sửa code / thêm tính năng (trên PC)

Sửa code bằng Claude Code như bình thường, xong **double-click file `deploy.bat`**
(hoặc chạy `.\deploy.ps1` trong PowerShell — như nhau).

(tự động: push GitHub → VPS kéo code → restart bot, ~10 giây; không hỏi mật khẩu
vì PC đã cài SSH key lên VPS)

# Lỗi thường gặp

**⚠️ QUAN TRỌNG — app Anki trên điện thoại hiện bảng "Upload to AnkiWeb / Download from AnkiWeb":**
LUÔN chọn **Download from AnkiWeb**. Vì bot trên VPS sync lên AnkiWeb ngay sau MỌI thao tác,
AnkiWeb luôn là bản mới nhất — chọn Upload sẽ lấy bản cũ trên điện thoại ĐÈ MẤT thẻ mới
(đã từng làm mất deck + thẻ ngày 14/07/2026).

Lưu ý kèm theo: Download **xóa luôn phần ôn tập bạn vừa làm trên điện thoại mà chưa sync lên**.
Nên bật **tự động sync** trong app Anki (sync khi mở và khi đóng app) để không bao giờ rơi vào
cảnh phải chọn. Bảng này chỉ hiện khi hai bên đã lệch schema (vd vừa thêm field cho model).

**Bảng đó hiện phía VPS (bot báo "Sync status 2"):** đây là lúc buộc phải **full sync một lần**.
Thao tác: `/backup` cho chắc → mở Anki desktop trên PC → Sync → chọn **Upload to AnkiWeb**
(đẩy bản đầy đủ nhất lên) → rồi điện thoại chọn Download. Đây là thao tác dễ mất dữ liệu nhất
trong Anki, luôn backup trước.

**Sao lưu tự động:** 3h30 sáng bot xuất từng deck ra `.apkg` (kèm lịch ôn) vào `backups/`, giữ 7
bản gần nhất. Thành công thì im lặng; **thất bại sẽ nhắn Telegram** — thấy tin đó thì phải xử lý
ngay, vì lúc đó kho đang không có bản sao lưu mới. Đổi chỗ lưu/số bản: `BACKUP_DIR`, `BACKUP_KEEP`
trong `.env`.

**Khôi phục thử một bản `.apkg` (đã kiểm chứng thật 31/07/2026 — 950/950 note phục hồi đúng):**
1. Đóng Anki đang chạy (Task Manager hoặc `taskkill /IM anki.exe`) — nó tự lưu, không mất gì.
2. Mở lại: `anki.exe -p "RestoreTest"` (hoặc mở Anki thường rồi ở màn hình chọn profile bấm
   **Add**, gõ tên bất kỳ) — bấm **Add** để tạo profile MỚI RỖNG, đừng chọn profile thật.
3. Đợi AnkiConnect sống lại (`curl 127.0.0.1:8765` trả `version`), gọi `importPackage` với
   `path` là đường dẫn file `.apkg` cần kiểm (vd `backups/2026-07-29_1225/RUSSIAN.apkg`).
4. Kiểm bằng AnkiConnect: `findNotes deck:*` (so số note với lúc backup) + `notesInfo` một note
   bất kỳ, đọc field xem chữ Nga/tiếng Việt còn nguyên không.
5. Đóng Anki, xoá thư mục profile test (`%APPDATA%\Anki2\RestoreTest`), mở lại đúng profile
   thật (`anki.exe -p "User 1"`) — kiểm `deckNames` phải thấy đủ deck cũ (RUSSIAN + GRAMMAR).
6. Không đụng gì tới file backup gốc hay profile thật trong lúc test — toàn bộ diễn ra trong
   profile rỗng riêng, xoá đi là sạch, không rủi ro với dữ liệu đang học.

**❌ Đừng đặt VPS tự động "Download from AnkiWeb" theo lịch.** Lệnh đó ghi đè sạch collection trên
VPS (xóa thẻ bot vừa thêm chưa kịp đẩy lên), và cũng không cứu được gì khi bạn quên sync điện
thoại — dữ liệu ôn tập lúc đó nằm trong điện thoại chứ không phải trên AnkiWeb.

**Anki báo "could not create its data folder" (trong VNC):** thư mục `anki-data`
bị sai quyền. Sửa trên VPS:

```bash
cd /root/ankiagent
docker compose down && chmod -R 777 anki-data && docker compose up -d
```

rồi chờ ~20 giây và kết nối lại VNC.

**Bot chờ mãi "⏳ Chờ AnkiConnect..." / `curl 127.0.0.1:8765` trả KQ=56:**
addon AnkiConnect trong container bị volume che mất (symlink lúc build image).
Sửa trên VPS:

```bash
cd /root/ankiagent
docker exec anki cp -r /app/anki-connect/plugin /data/addons21/AnkiConnectDev
python3 -c "import json; p='anki-data/addons21/AnkiConnectDev/config.json'; c=json.load(open(p)); c['webBindAddress']='0.0.0.0'; json.dump(c, open(p,'w'), indent=2); print('OK')"
docker restart anki
```

(setup_vps.sh bản mới đã tự làm việc này.)

# Lệnh cứu hộ (khi có sự cố)

```bash
journalctl -u anki-bot -n 50     # xem 50 dòng log gần nhất của bot
systemctl restart anki-bot       # khởi động lại bot
docker ps                        # xem container anki có đang chạy không
docker restart anki              # khởi động lại Anki
docker logs anki --tail 50       # xem log của Anki
free -h                          # xem còn bao nhiêu RAM
```
