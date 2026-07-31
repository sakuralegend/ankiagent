#!/usr/bin/env bash
# Cài git hook cho repo này. Chạy MỘT LẦN trên mỗi máy:
#     bash scripts/caidat_hook.sh
#
# Hook không nằm trong thứ git đẩy đi (`.git/hooks/` là cục bộ từng máy), nên
# phải cài tay — đó cũng là lý do `soatkientruc.py` S9 vẫn giữ nguyên làm lớp
# chặn thứ hai, đi cùng repo tới mọi máy và mọi AI.
set -e
GOC=$(cd "$(dirname "$0")/.." && pwd)
cp "$GOC/scripts/hook-commit-msg" "$GOC/.git/hooks/commit-msg"
chmod +x "$GOC/.git/hooks/commit-msg"
echo "✅ Da cai hook commit-msg."
echo "   Tu nay commit dung file code ma khong co phan than giai thich VI SAO"
echo "   se bi chan NGAY luc commit, khong phai doi toi luc deploy."
