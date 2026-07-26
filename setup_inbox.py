# ==============================================================================
# --- THIẾT LẬP HAI DECK CỦA LỘ TRÌNH HỌC (0-quen + 1-go) + LUẬT THỨ TỰ HỌC ---
# Chạy 1 lần trên máy có Anki + AnkiConnect mở (idempotent, chạy lại vô hại):
#   python setup_inbox.py
#
# Việc script làm:
# 1. Tạo hai deck của lộ trình hai giai đoạn (xem config.py):
#      STAGE1_DECK (0-quen) — LÀM QUEN, thẻ mới rơi vào đây
#      STAGE2_DECK (1-go)   — GÕ, thẻ tốt nghiệp GĐ1 chuyển sang
# 2. Preset "Default" (mọi deck RUSSIAN): ép luật cứng do user chốt 19/07/2026 —
#    ôn HẾT thẻ cũ (đến hạn cũ nhất trước) rồi mới được hiện thẻ mới, không xen.
#    (newMix=1: new sau review; reviewOrder=0: theo ngày đến hạn tăng dần)
# 3. Preset riêng cho MỖI giai đoạn: từ THÊM GẦN NHẤT học trước
#    (newGatherPriority=2). Hai preset tách rời để mỗi chặng có hạn mức thẻ mới
#    ĐỘC LẬP — gộp một deck thì Anki rút theo vị trí và có thể lĩnh trọn suất
#    cho GĐ1, không còn suất nào cho GĐ2.
# 4. ⚠️ Trần thẻ mới của DECK CHA đặt = TỔNG hai con. Scheduler v3 lấy trần cha
#    kẹp cả cây, nên quên bước này là hai deck con bị bóp lại (đã trả giá
#    21/07/2026: RUSSIAN=20 kẹp inbox 70 xuống 20).
# 5. Gom thẻ CHƯA HỌC (is:new) đang rải rác trong các deck chủ đề về GĐ1
#    (thẻ đã/đang học để yên). Deck config sync bình thường -> VPS/iPhone tự có.
# ==============================================================================
import sys

import requests

from anki_tools.config import (
    ANKI_CONNECT_URL, STAGE1_DECK, STAGE2_DECK, TOPIC_DECK_PARENT,
)

# Mỗi chặng 70 thẻ mới/ngày. Vì mỗi từ đi qua hàng đợi "thẻ mới" HAI lượt (một
# lần vào GĐ1, một lần nữa sau khi forgetCards để vào GĐ2), muốn thật sự gặp
# N từ mới/ngày thì mỗi deck để N và deck cha để 2N.
STAGE_NEW_PER_DAY = 70
PARENT_NEW_PER_DAY = STAGE_NEW_PER_DAY * 2


def call(action, **params):
    r = requests.post(ANKI_CONNECT_URL, json={"action": action, "version": 6, "params": params}, timeout=60)
    j = r.json()
    if j.get("error"):
        raise SystemExit(f"AnkiConnect lỗi ({action}): {j['error']}")
    return j["result"]


def ensure_preset(deck, preset_name, clone_from):
    """Đảm bảo `deck` dùng preset tên `preset_name` (tạo bằng cách clone nếu
    chưa có), rồi áp luật thứ tự + hạn mức. Trả về config đã lưu."""
    cfg = call("getDeckConfig", deck=deck)
    if cfg["name"] != preset_name:
        new_id = call("cloneDeckConfigId", name=preset_name, cloneFrom=clone_from)
        call("setDeckConfigId", decks=[deck], configId=new_id)
        cfg = call("getDeckConfig", deck=deck)
    cfg["newMix"] = 1
    cfg["reviewOrder"] = 0
    cfg["newGatherPriority"] = 2          # từ thêm gần nhất học trước
    cfg["new"]["perDay"] = STAGE_NEW_PER_DAY
    call("saveDeckConfig", config=cfg)
    print(f"🎛 '{deck}' → preset '{preset_name}': mới nhất trước, "
          f"{STAGE_NEW_PER_DAY} thẻ mới/ngày")
    return cfg


def main():
    sys.stdout.reconfigure(encoding="utf-8")

    call("createDeck", deck=STAGE1_DECK)
    call("createDeck", deck=STAGE2_DECK)
    print(f"📥 GĐ1 làm quen: {STAGE1_DECK}")
    print(f"⌨️  GĐ2 gõ      : {STAGE2_DECK}")

    # --- Luật thứ tự cho MỌI deck dùng preset Default ---
    default_cfg = call("getDeckConfig", deck=TOPIC_DECK_PARENT)
    default_cfg["newMix"] = 1      # thẻ mới chỉ hiện SAU khi ôn hết thẻ cũ
    default_cfg["reviewOrder"] = 0  # ôn theo hạn: quá hạn lâu nhất trước
    call("saveDeckConfig", config=default_cfg)
    print(f"⚖️ Preset '{default_cfg['name']}': ôn hết thẻ cũ (cũ nhất trước) rồi mới tới thẻ mới")

    # --- Preset riêng cho từng chặng ---
    ensure_preset(STAGE2_DECK, "inbox", default_cfg["id"])
    ensure_preset(STAGE1_DECK, "stage1-quen", default_cfg["id"])

    # --- Trần deck CHA phải chứa nổi cả hai con ---
    parent_cfg = call("getDeckConfig", deck=TOPIC_DECK_PARENT)
    if parent_cfg["new"]["perDay"] < PARENT_NEW_PER_DAY:
        parent_cfg["new"]["perDay"] = PARENT_NEW_PER_DAY
        call("saveDeckConfig", config=parent_cfg)
    print(f"🔓 Preset '{parent_cfg['name']}' (deck cha): {parent_cfg['new']['perDay']} thẻ mới/ngày")

    # --- Gom thẻ chưa học về GĐ1 ---
    new_cards = call("findCards", query=(
        f'deck:"{TOPIC_DECK_PARENT}" is:new '
        f'-deck:"{STAGE1_DECK}" -deck:"{STAGE2_DECK}"'
    ))
    if new_cards:
        call("changeDeck", cards=new_cards, deck=STAGE1_DECK)
        print(f"📦 Đã gom {len(new_cards)} thẻ chưa học từ deck chủ đề về {STAGE1_DECK}")
    else:
        print("📦 Không có thẻ chưa học nào nằm ngoài lộ trình")

    print("⏳ Sync AnkiWeb...")
    call("sync")
    print("☁️ Xong.")


if __name__ == "__main__":
    main()
