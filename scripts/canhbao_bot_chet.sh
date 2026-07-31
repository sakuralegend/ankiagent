#!/usr/bin/env bash
# ==============================================================================
# CHUÔNG BÁO KHI BOT CHẾT — đường báo ĐỘC LẬP với bot (QD-04, 31/07/2026)
#
# Vì sao không dùng `tgbot/alerts.py` như mọi cảnh báo khác: alerts.py gửi tin
# QUA CHÍNH BOT. Bot chết thì lời cảnh báo chết theo — im lặng tuyệt đối, đúng
# thứ ta đang muốn diệt. Script này nói thẳng với Telegram bằng curl, không nạp
# một dòng code Python nào của dự án, nên bot hỏng kiểu gì nó vẫn kêu được.
#
# Hai chế độ:
#   bash canhbao_bot_chet.sh          # cron 15' — chỉ báo khi TRẠNG THÁI ĐỔI
#   bash canhbao_bot_chet.sh --ngay   # systemd OnFailure gọi — báo ngay lập tức
#
# Chống spam (bài học `alerts.py`): chế độ cron ghi trạng thái lần trước vào
# $MOC và chỉ nhắn khi khác đi. Bot chết cả ngày = ĐÚNG MỘT tin, không phải 96.
# Bot sống lại cũng nhắn — để bạn biết chuyện đã qua mà không phải tự đi kiểm.
# ==============================================================================
set -u

DU_AN=/root/ankiagent
ENV_FILE="$DU_AN/.env"
MOC=/root/.anki_bot_trangthai
DICH_VU=anki-bot

doc_env() {
    # Lấy giá trị một biến trong .env, bỏ nháy và ký tự xuống dòng kiểu Windows.
    grep -E "^$1=" "$ENV_FILE" 2>/dev/null | head -1 | cut -d= -f2- \
        | tr -d '\r' | sed -e 's/^"//' -e 's/"$//' -e "s/^'//" -e "s/'$//"
}

gui() {
    local token chat
    token=$(doc_env TELEGRAM_BOT_TOKEN)
    chat=$(doc_env TELEGRAM_USER_ID)
    if [ -z "$token" ] || [ -z "$chat" ]; then
        echo "canhbao_bot_chet: thieu TELEGRAM_BOT_TOKEN/TELEGRAM_USER_ID trong .env" >&2
        return 1
    fi
    curl -s -m 20 -X POST "https://api.telegram.org/bot${token}/sendMessage" \
        -d "chat_id=${chat}" --data-urlencode "text=$1" >/dev/null
}

# Vài dòng log cuối để bạn khỏi phải tự ssh vào tìm nguyên nhân.
ly_do() {
    journalctl -u "$DICH_VU" -n 6 --no-pager -o cat 2>/dev/null | tail -6
}

if [ "${1:-}" = "--ngay" ]; then
    echo chet > "$MOC"
    gui "🔴 BOT ANKI ĐÃ CHẾT HẲN (khởi động lại liên tục không lên nổi).

Sáu dòng log cuối:
$(ly_do)

Cứu: ssh root@\$VPS rồi chạy
  systemctl status anki-bot
  journalctl -u anki-bot -n 50"
    exit 0
fi

if systemctl is-active --quiet "$DICH_VU"; then
    NAY=song
else
    NAY=chet
fi
TRUOC=$(cat "$MOC" 2>/dev/null || echo song)

if [ "$NAY" != "$TRUOC" ]; then
    echo "$NAY" > "$MOC"
    if [ "$NAY" = chet ]; then
        gui "🔴 BOT ANKI ĐANG KHÔNG CHẠY (phát hiện lúc $(date '+%H:%M %d/%m')).

Sáu dòng log cuối:
$(ly_do)

Cứu: ssh vào VPS rồi 'systemctl restart anki-bot'."
    else
        gui "✅ Bot Anki đã chạy lại bình thường ($(date '+%H:%M %d/%m'))."
    fi
fi
