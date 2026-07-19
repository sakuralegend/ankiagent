# ==============================================================================
# --- THIẾT LẬP DECK INBOX (RUSSIAN::0-inbox) + LUẬT THỨ TỰ HỌC ---
# Chạy 1 lần trên máy có Anki + AnkiConnect mở (idempotent, chạy lại vô hại):
#   python setup_inbox.py
#
# Việc script làm:
# 1. Tạo deck inbox (INBOX_DECK trong config.py) — chỗ hứng MỌI từ mới của bot.
# 2. Preset "Default" (mọi deck RUSSIAN): ép luật cứng do user chốt 19/07/2026 —
#    ôn HẾT thẻ cũ (đến hạn cũ nhất trước) rồi mới được hiện thẻ mới, không xen.
#    (newMix=1: new sau review; reviewOrder=0: theo ngày đến hạn tăng dần)
# 3. Preset riêng "inbox" cho deck inbox: từ THÊM GẦN NHẤT học trước
#    (newGatherPriority=2) — 40-50 từ mỗi ngày được ưu tiên, ~200 từ tồn đọng
#    lấp phần hạn mức còn lại; tối đa 50 từ mới/ngày (đổi trong Deck Options).
# 4. Gom thẻ CHƯA HỌC (is:new) đang rải rác trong các deck chủ đề về inbox
#    (thẻ đã/đang học để yên). Deck config sync bình thường -> VPS/iPhone tự có.
# ==============================================================================
import sys

import requests

from anki_tools.config import ANKI_CONNECT_URL, INBOX_DECK, TOPIC_DECK_PARENT

INBOX_NEW_PER_DAY = 50


def call(action, **params):
    r = requests.post(ANKI_CONNECT_URL, json={"action": action, "version": 6, "params": params}, timeout=60)
    j = r.json()
    if j.get("error"):
        raise SystemExit(f"AnkiConnect lỗi ({action}): {j['error']}")
    return j["result"]


def main():
    sys.stdout.reconfigure(encoding="utf-8")

    call("createDeck", deck=INBOX_DECK)
    print(f"📥 Deck hứng: {INBOX_DECK}")

    # --- Luật thứ tự cho MỌI deck dùng preset Default ---
    default_cfg = call("getDeckConfig", deck=TOPIC_DECK_PARENT)
    default_cfg["newMix"] = 1      # thẻ mới chỉ hiện SAU khi ôn hết thẻ cũ
    default_cfg["reviewOrder"] = 0  # ôn theo hạn: quá hạn lâu nhất trước
    call("saveDeckConfig", config=default_cfg)
    print(f"⚖️ Preset '{default_cfg['name']}': ôn hết thẻ cũ (cũ nhất trước) rồi mới tới thẻ mới")

    # --- Preset riêng cho inbox ---
    inbox_cfg = call("getDeckConfig", deck=INBOX_DECK)
    if inbox_cfg["name"] != "inbox":
        new_id = call("cloneDeckConfigId", name="inbox", cloneFrom=default_cfg["id"])
        call("setDeckConfigId", decks=[INBOX_DECK], configId=new_id)
        inbox_cfg = call("getDeckConfig", deck=INBOX_DECK)
    inbox_cfg["newMix"] = 1
    inbox_cfg["reviewOrder"] = 0
    inbox_cfg["newGatherPriority"] = 2          # từ thêm gần nhất học trước
    inbox_cfg["new"]["perDay"] = INBOX_NEW_PER_DAY
    call("saveDeckConfig", config=inbox_cfg)
    print(f"🎛 Preset 'inbox': từ mới nhất trước, tối đa {INBOX_NEW_PER_DAY} từ mới/ngày")

    # --- Gom thẻ chưa học về inbox ---
    new_cards = call("findCards", query=f'deck:"{TOPIC_DECK_PARENT}" is:new -deck:"{INBOX_DECK}"')
    if new_cards:
        call("changeDeck", cards=new_cards, deck=INBOX_DECK)
        print(f"📦 Đã gom {len(new_cards)} thẻ chưa học từ các deck chủ đề về inbox")
    else:
        print("📦 Không có thẻ chưa học nào nằm ngoài inbox")

    print("⏳ Sync AnkiWeb...")
    call("sync")
    print("☁️ Xong.")


if __name__ == "__main__":
    main()
