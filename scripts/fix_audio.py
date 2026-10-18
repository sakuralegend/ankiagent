# ==============================================================================
# --- CHUYỂN / VÁ TIẾNG: từ + câu ví dụ sang giọng Yandex (anki_tools/audio.py) ---
# Hai bước TÁCH HẲN, user chốt 18/10/2026: "chỉ khi tải xong TOÀN BỘ âm thanh mới
# được đổi Anki" — không bao giờ để kho nửa giọng cũ nửa giọng mới vì tải hụt giữa chừng.
#   --tai    CHỈ ĐỌC Anki, tải mọi tiếng còn thiếu vào data/tieng_yandex/. Chạy lại
#            bao nhiêu lần cũng được (file đã có thì bỏ qua) — tới khi "thiếu 0".
#   --apply  TỪ CHỐI nếu thư mục còn thiếu dù 1 file. Đủ thì: backup, sync trước,
#            ghi ô Audio/PluralAudio/ExamplesHTML, sync sau. `--note id,id` = chỉ
#            ghi vài thẻ (thử trên iPhone trước khi ghi cả kho).
# Không lệnh nào ⇒ chỉ đếm. File cũ vẫn nằm trong media (tên mới `ya_…`) ⇒ lùi được.
# Chỉ sửa nội dung ô — không đụng model ⇒ KHÔNG kích full sync.
# ==============================================================================
import argparse
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor

# Chay duoc tu bat cu dau: file nay khong con nam o goc repo nen phai tu tro
# duong dan goc vao sys.path truoc khi import anki_tools (G3, 31/07/2026).
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from anki_tools.anki_client import (doc_notes_cua_model, gan_tieng_vi_du, setup_anki_environment,
                                    store_word_audio, sync_truoc_khi_ghi_lo, trigger_sync,
                                    update_note_fields)
from anki_tools.audio import THU_MUC_TIENG, lay_tieng, ten_file_audio, ten_file_cau
from anki_tools.backup import run_backup
from anki_tools.config import MODEL_NAME
from anki_tools.html_builder import gan_nut_nghe
from grammar_forms.cards import setup_model as setup_mau_so_nhieu
from grammar_forms.config import PLURAL_MODEL

# (model, ô audio, ô chứa chữ CÓ DẤU, prefix tên file)
O_AUDIO = [(MODEL_NAME, "Audio", "Word", "ru_audio"),
           (PLURAL_MODEL, "Audio", "Word", "ru_audio"),
           (PLURAL_MODEL, "PluralAudio", "Plural", "ru_plural")]


def _chu(fields, o):
    return re.sub(r"<[^>]+>", "", fields.get(o, {}).get("value", "")).strip()


def doc_kho():
    """{model: [note]} — CHỈ ĐỌC."""
    return {m: doc_notes_cua_model(m) for m in (MODEL_NAME, PLURAL_MODEL)}


def can_tai(kho):
    """{tên file: chữ cần đọc} cho MỌI thẻ. Câu ví dụ liệt kê bằng CHÍNH gan_nut_nghe
    (hàm nhận câu trả None ⇒ không đổi gì) để danh sách tải khớp từng câu với lúc ghi."""
    can = {}
    for model, o, o_chu, prefix in O_AUDIO:
        for n in kho[model]:
            chu = _chu(n["fields"], o_chu)
            if chu:
                can[ten_file_audio(prefix, chu)] = chu
    for model in kho:
        for n in kho[model]:
            gan_nut_nghe(n["fields"].get("ExamplesHTML", {}).get("value", ""),
                         lambda cau: can.__setitem__(ten_file_cau(cau), cau))
    return can


def con_thieu(can):
    return {t: c for t, c in can.items() if not os.path.exists(os.path.join(THU_MUC_TIENG, t))}


def tai(can):
    thieu = con_thieu(can)
    print(f"Cần {len(can)} file · đã có {len(can) - len(thieu)} · phải tải {len(thieu)}")
    xong = [0]

    def mot(item):
        ok = lay_tieng(item[1], item[0]) is not None
        xong[0] += 1
        if xong[0] % 200 == 0:
            print(f"  … {xong[0]}/{len(thieu)}", flush=True)
        return ok
    with ThreadPoolExecutor(4) as pool:   # 4 luồng: nhanh gấp ~4 mà chưa chạm hạn mức Yandex
        list(pool.map(mot, thieu.items()))
    con = con_thieu(can)
    print(f"✅ Tải xong. Còn thiếu {len(con)}" + (" — chạy lại --tai." if con else " — ĐỦ, được phép --apply."))
    for t, c in list(con.items())[:20]:
        print(f"   thiếu: {c[:60]}")


def ghi(kho, chi_note):
    # Mẫu thẻ mới (dòng "· 1× ·" + CSS nút ▶) đi CÙNG lượt ghi. Chỉ đổi nội dung mẫu,
    # không thêm/bớt field ⇒ không full sync (bot vẫn đẩy mẫu mỗi lần khởi động).
    setup_anki_environment()
    setup_mau_so_nhieu()
    da, giu, loi = 0, 0, []
    for model, notes in kho.items():
        for n in notes:
            if chi_note and n["noteId"] not in chi_note:
                continue
            f, moi = n["fields"], {}
            for m, o, o_chu, prefix in O_AUDIO:
                if m == model and _chu(f, o_chu):
                    moi[o] = store_word_audio(_chu(f, o_chu), prefix)[0]
            moi["ExamplesHTML"] = gan_tieng_vi_du(f.get("ExamplesHTML", {}).get("value", ""))
            moi = {k: v for k, v in moi.items() if v and v != f.get(k, {}).get("value", "")}
            if not moi:
                giu += 1
            elif update_note_fields(n["noteId"], moi):
                da += 1
            else:
                loi.append(_chu(f, "Word"))
    print(f"✅ Đã ghi {da} thẻ · giữ nguyên {giu} · ❌ ghi lỗi {len(loi)} {', '.join(loi[:20])}")
    return da


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description="Chuyển/vá tiếng sang Yandex")
    ap.add_argument("--tai", action="store_true", help="tải tiếng về máy (chỉ đọc Anki)")
    ap.add_argument("--apply", action="store_true", help="ghi vào Anki (cần đã tải đủ)")
    ap.add_argument("--note", default="", help="chỉ ghi các note id này, ngăn bằng dấu phẩy")
    args = ap.parse_args()

    kho = doc_kho()
    can = can_tai(kho)
    if args.tai:
        return tai(can)
    thieu = con_thieu(can)
    print(f"Cần {len(can)} file tiếng · còn thiếu {len(thieu)}")
    if not args.apply:
        print("(Chỉ đếm. --tai để tải, --apply để ghi Anki.)")
        return
    if thieu:
        raise SystemExit(f"❌ TỪ CHỐI ghi Anki: còn thiếu {len(thieu)} file. Chạy --tai cho tới khi thiếu 0.")
    if not sync_truoc_khi_ghi_lo("chuyển tiếng Yandex"):
        raise SystemExit("❌ Không kéo được AnkiWeb về — dừng, chưa ghi gì.")
    res, _ = run_backup()
    if not res["path"]:
        raise SystemExit("❌ Backup thất bại — dừng, chưa ghi gì.")
    print(f"💾 Backup: {res['path']}")
    chi = {int(x) for x in args.note.split(",") if x.strip()}
    if ghi(doc_kho(), chi):
        print("☁️ Sync xong." if trigger_sync() else "⚠️ Sync thất bại — thử /sync trong bot.")


if __name__ == "__main__":
    main()
