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
#    cho GĐ1, không còn suất nào cho GĐ2. Nhưng 21 THAM SỐ FSRS thì CHÉP từ
#    Default (xem ensure_preset) — ⚠️ nghĩa là mỗi lần bấm Optimize trong Anki,
#    CHẠY LẠI FILE NÀY để hai chặng không bị bỏ lại phía sau.
# 4. ⚠️ Trần thẻ mới của DECK CHA đặt = TỔNG hai con. Scheduler v3 lấy trần cha
#    kẹp cả cây, nên quên bước này là hai deck con bị bóp lại (đã trả giá
#    21/07/2026: RUSSIAN=20 kẹp inbox 70 xuống 20).
# 5. Gom thẻ CHƯA HỌC (is:new) đang rải rác trong các deck chủ đề về GĐ1
#    (thẻ đã/đang học để yên). Deck config sync bình thường -> VPS/iPhone tự có.
# ==============================================================================
import sys

import requests

# Chay duoc tu bat cu dau: file nay khong con nam o goc repo nen phai tu tro
# duong dan goc vao sys.path truoc khi import anki_tools (G3, 31/07/2026).
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from anki_tools.config import (
    ANKI_CONNECT_URL, STAGE1_DECK, STAGE2_DECK, TOPIC_DECK_PARENT,
)

# KHÔNG CÒN TRẦN THẺ MỚI (user chốt 26/07/2026: "học đến bao giờ hết thì thôi").
# 9999 là mức cao nhất Anki nhận — đặt nó nghĩa là "gỡ trần", không phải "9999 thẻ".
#
# ⚠️ Muốn đặt trần trở lại thì sửa ĐÚNG hai hằng số này rồi chạy lại file này; đừng
# chỉnh tay trong GUI vì lần chạy sau sẽ ghi đè. Vì mỗi từ đi qua hàng đợi "thẻ mới"
# HAI lượt (vào GĐ1, rồi lại vào GĐ2 sau forgetCards), muốn thật sự gặp N từ mới/ngày
# thì mỗi deck để N và deck cha để 2N.
#
# ⚠️ Preset deck cha vẫn mang tên cũ `russian-parent-70` — TÊN GIỜ SAI, nó không còn
# giới hạn 70. Không đổi tên vì user nhìn tên đó trong GUI Anki.
STAGE_NEW_PER_DAY = 9999
PARENT_NEW_PER_DAY = 9999


def call(action, **params):
    r = requests.post(ANKI_CONNECT_URL, json={"action": action, "version": 6, "params": params}, timeout=60)
    j = r.json()
    if j.get("error"):
        raise SystemExit(f"AnkiConnect lỗi ({action}): {j['error']}")
    return j["result"]


def preset_deck_chu_de():
    """Preset đang cai quản các deck CHỦ ĐỀ — nơi gần như toàn bộ thẻ nằm.

    ⚠️ KHÔNG lấy qua `TOPIC_DECK_PARENT`. Deck cha "RUSSIAN" có preset RIÊNG
    (`russian-parent-70`, chỉ để nới trần thẻ mới) và KHÔNG chứa thẻ nào — lấy
    nhầm chỗ đó là đọc phải một bộ tham số không xếp lịch cho thẻ nào cả. Đã sập
    bẫy này thật 04/08/2026: chép tham số cho hai chặng nhưng chép từ preset deck
    cha, ra bộ cũ hơn bộ vừa Optimize."""
    for d in sorted(call("deckNames")):
        if d.startswith(f"{TOPIC_DECK_PARENT}::") and d not in (STAGE1_DECK, STAGE2_DECK):
            return call("getDeckConfig", deck=d)
    raise SystemExit(f"Không thấy deck chủ đề nào dưới '{TOPIC_DECK_PARENT}'")


def ensure_preset(deck, preset_name, default_cfg):
    """Đảm bảo `deck` dùng preset tên `preset_name` (tạo bằng cách clone nếu
    chưa có), rồi áp luật thứ tự + hạn mức + tham số FSRS. Trả về config đã lưu.

    🔴 21 tham số FSRS LUÔN chép từ preset Default (user chốt 04/08/2026). Hai
    preset này sinh ra bằng cách clone Default, nên chúng chép tham số đúng MỘT
    lần lúc tạo (26/07) rồi đông cứng ở đó — bấm Optimize cho Default về sau
    không với tới. Hậu quả đo được 04/08: sau khi tối ưu Default, thẻ ở deck chủ
    đề hết sạch hoá thạch (402 -> 0 thẻ có độ khó >= 90%), còn 25/63 thẻ trong
    `1-go` vẫn kẹt vì preset của nó giữ w7 = 0,001 (mức làm độ khó KHÔNG BAO GIỜ
    hạ lại được). Chép chứ không tối ưu riêng: `0-quen` thường có 0 thẻ nên
    Optimize ở đó không đủ dữ liệu, trong khi lịch sử học của giai đoạn làm quen
    ĐÃ nằm sẵn trong tập huấn luyện của Default (8 085/14 276 lượt).

    Muốn hai chặng có tham số riêng thì phải bỏ dòng này TRƯỚC, đừng chỉnh tay
    trong GUI — lần chạy sau sẽ ghi đè."""
    cfg = call("getDeckConfig", deck=deck)
    if cfg["name"] != preset_name:
        new_id = call("cloneDeckConfigId", name=preset_name, cloneFrom=default_cfg["id"])
        call("setDeckConfigId", decks=[deck], configId=new_id)
        cfg = call("getDeckConfig", deck=deck)
    cu = cfg.get("fsrsParams6")
    cfg["fsrsParams6"] = default_cfg["fsrsParams6"]
    cfg["newMix"] = 1
    cfg["reviewOrder"] = 0
    cfg["newGatherPriority"] = 2          # từ thêm gần nhất học trước
    cfg["new"]["perDay"] = STAGE_NEW_PER_DAY
    call("saveDeckConfig", config=cfg)
    print(f"🎛 '{deck}' → preset '{preset_name}': mới nhất trước, "
          f"{STAGE_NEW_PER_DAY} thẻ mới/ngày"
          + ("" if cu == cfg["fsrsParams6"] else "  |  ĐÃ ĐỒNG BỘ tham số FSRS theo Default"))
    return cfg


def main():
    sys.stdout.reconfigure(encoding="utf-8")

    call("createDeck", deck=STAGE1_DECK)
    call("createDeck", deck=STAGE2_DECK)
    print(f"📥 GĐ1 làm quen: {STAGE1_DECK}")
    print(f"⌨️  GĐ2 gõ      : {STAGE2_DECK}")

    # --- Luật thứ tự cho MỌI deck dùng preset Default ---
    default_cfg = preset_deck_chu_de()
    default_cfg["newMix"] = 1      # thẻ mới chỉ hiện SAU khi ôn hết thẻ cũ
    default_cfg["reviewOrder"] = 0  # ôn theo hạn: quá hạn lâu nhất trước
    call("saveDeckConfig", config=default_cfg)
    print(f"⚖️ Preset '{default_cfg['name']}': ôn hết thẻ cũ (cũ nhất trước) rồi mới tới thẻ mới")

    # --- Preset riêng cho từng chặng ---
    ensure_preset(STAGE2_DECK, "inbox", default_cfg)
    ensure_preset(STAGE1_DECK, "stage1-quen", default_cfg)

    # --- Trần deck CHA phải chứa nổi cả hai con ---
    parent_cfg = call("getDeckConfig", deck=TOPIC_DECK_PARENT)
    # Deck cha không chứa thẻ nào nên tham số của nó hiện không xếp lịch cho ai —
    # vẫn đồng bộ để nó không thành quả mìn nếu sau này có thẻ rơi thẳng vào đây.
    if (parent_cfg["new"]["perDay"] < PARENT_NEW_PER_DAY
            or parent_cfg["fsrsParams6"] != default_cfg["fsrsParams6"]):
        parent_cfg["new"]["perDay"] = max(parent_cfg["new"]["perDay"], PARENT_NEW_PER_DAY)
        parent_cfg["fsrsParams6"] = default_cfg["fsrsParams6"]
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
