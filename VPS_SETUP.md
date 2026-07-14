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
ssh -L 5900:127.0.0.1:5900 root@161.248.146.56
```

**5c.** [PC] Mở TightVNC Viewer → Remote Host gõ: `localhost::5900` → Connect.
   → Hiện ra cửa sổ Anki đang chạy trên VPS.

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
| Thêm từ | gõ thẳng từ đó, vd `хороший` |
| Đổi deck | `/deck Tên Deck` |
| Sửa thẻ đã có | `/sua хороший ví dụ ngắn hơn, đời thường hơn` |
| Ép sync ngay | `/sync` |

# Khi sửa code / thêm tính năng (trên PC)

Sửa code bằng Claude Code như bình thường, xong chạy:

```powershell
.\deploy.ps1
```

(tự động: push GitHub → VPS kéo code → restart bot, ~10 giây)

# Lệnh cứu hộ (khi có sự cố)

```bash
journalctl -u anki-bot -n 50     # xem 50 dòng log gần nhất của bot
systemctl restart anki-bot       # khởi động lại bot
docker ps                        # xem container anki có đang chạy không
docker restart anki              # khởi động lại Anki
docker logs anki --tail 50       # xem log của Anki
free -h                          # xem còn bao nhiêu RAM
```
