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
| Thẻ AI bị khuyết (thiếu ví dụ) | bot cảnh báo kèm 2 nút: 🔧 Tự sửa (đổi ví dụ) / ⏭ Bỏ qua |
| Sửa thẻ đã có | `/sua` (hoặc nút ✏️) → bot hỏi từ → gõ từ → chọn nút 1 Ngắn hơn / 2 Đổi ví dụ / 3 Dài hơn / Tự viết |
| Sửa theo ý mình | trong bảng kiểu sửa bấm "Tự viết yêu cầu" → gõ thẳng yêu cầu |
| Menu nút bấm | `/menu` |
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
