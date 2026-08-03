# ==============================================================================
# --- THIẾT LẬP MÔI TRƯỜNG ANKI: model, field, CSS, template (chạy lúc khởi động).
# Tách từ anki_client.py (03/08/2026, QD-18). Caller vẫn import anki_client.
# ==============================================================================
import os
import requests

from .config import ANKI_CONNECT_URL, MODEL_NAME

_TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")


def _read_template(filename):
    with open(os.path.join(_TEMPLATES_DIR, filename), "r", encoding="utf-8") as f:
        return f.read()


def setup_anki_environment():
    # Từ khi gỡ nút AI Refine khỏi thẻ, back_template.html là HTML tĩnh thuần,
    # không còn placeholder nào cần tiêm (API key không còn bị nhúng vào thẻ).
    shared_css = _read_template("card.css")
    front_template = _read_template("front_template.html")
    back_template = _read_template("back_template.html")

    print("--- ⚙️ Thiết lập môi trường Anki...", end=" ", flush=True)
    try:
        res = requests.post(ANKI_CONNECT_URL, json={"action": "modelNames", "version": 6}, timeout=5)
        existing_models = res.json().get("result", [])

        if MODEL_NAME not in existing_models:
            res_create = requests.post(ANKI_CONNECT_URL, json={
                "action": "createModel", "version": 6,
                "params": {
                    "modelName": MODEL_NAME,
                    # HuongDan: phân tích chẻ gốc + cách nhớ + họ hàng, do Opus 5 soạn
                    #   ĐỊNH KỲ THEO LÔ (không sinh lúc tạo thẻ) — push_to_anki không ghi
                    #   field này nên thẻ mới để trống, soạn bù sau.
                    #   (Tên cũ "Mnemonic" đã đổi 27/07/2026: hướng mnemonic bị bỏ, để
                    #   tên cũ chỉ gây nhầm. Đổi tên field KHÔNG phải schema mod — đã đo,
                    #   sync bình thường — vì số lượng và thứ tự field không đổi.)
                    # Stage: giai đoạn học. RỖNG = GĐ1 làm quen (không ô gõ),
                    #   "type" = GĐ2 gõ. Template chọn mặt thẻ theo field này —
                    #   khối điều kiện của Anki không đọc được tên deck nên bắt
                    #   buộc phải có field. Thẻ mới để trống = vào thẳng GĐ1.
                    # (Field "Image" đã bỏ 26/07/2026: 0/870 note từng dùng tới.)
                    # AspectBadge: thể động từ (HOÀN THÀNH / CHƯA HOÀN THÀNH) —
                    #   thêm 29/07/2026. Để RIÊNG một field chứ không nhét chung
                    #   vào GenderBadge: user chốt "làm hẳn 1 field mới cho dễ bảo
                    #   trì". Danh từ/tính từ để trống -> khối điều kiện trong
                    #   template làm badge biến mất, không có ô rỗng lơ lửng.
                    # ReflexiveBadge: động từ phản thân (-ся) — thêm 29/07/2026
                    #   cùng đợt với AspectBadge. Nó gỡ chỗ badge thể KHÔNG cứu
                    #   được: `учи́ть`/`учи́ться` cùng `v`, cùng chưa hoàn thành.
                    # GrammarJSON: TOÀN BỘ dữ liệu ngữ pháp cào được, dạng JSON,
                    #   ẨN (không template nào hiện). Cùng khuôn với `RawExamples`
                    #   vốn đã lưu JSON câu gốc. User chốt 29/07: *"cào rồi đặt
                    #   vào một field nào đó trong thẻ, để sau này muốn lấy để xử
                    #   lí cũng dễ"* — trước đó dữ liệu chỉ nằm ở
                    #   `data/grammar_cache.json` trên laptop nên bot trên VPS
                    #   không với tới. Để trong thẻ thì nó tự sync đi khắp nơi và
                    #   thẻ trở thành tự chứa, không phụ thuộc file ngoài.
                    #   Đo thật: 0,8 MB cho 950 thẻ (trung bình 888 B, to nhất 6 KB).
                    "inOrderFields": ["Word", "WordClean", "Meaning", "Vietnamese", "PoS", "PoSFull", "GenderBadge", "AspectBadge", "ReflexiveBadge", "ExamplesHTML", "RawExamples", "GrammarJSON", "Audio", "HuongDan", "Stage"],
                    "css": shared_css, "cardTemplates": [{"Name": "Pure Engine Typing Card v25", "Front": front_template, "Back": back_template}]
                }
            }, timeout=5)
            if res_create.json().get("error"):
                print(f"\n❌ Tạo model thất bại: {res_create.json().get('error')}")
            else:
                print("✅", end=" ")
        else:
            print("✅", end=" ")
            # Model ĐÃ CÓ SẴN thì `createModel` ở trên không chạy, nên field mới
            # phải thêm riêng. Bọc trong `if thiếu` để chạy lại nhiều lần vẫn yên:
            # `modelFieldAdd` gọi lần hai sẽ báo lỗi trùng tên.
            # 🔴 Thêm field LÀ schema mod -> Anki đòi full sync một lần. Đã nói
            # trước với user (29/07). Sau khi sync phải kiểm `journalctl` trên VPS:
            # mọi schema mod đều làm VPS kẹt "Sync status 2" mà KHÔNG báo Telegram.
            res_f = requests.post(ANKI_CONNECT_URL, json={
                "action": "modelFieldNames", "version": 6,
                "params": {"modelName": MODEL_NAME}}, timeout=5)
            dang_co = res_f.json().get("result") or []
            for ten, vi_tri in (("AspectBadge", 7), ("ReflexiveBadge", 8),
                                ("GrammarJSON", 11)):
                if ten in dang_co:
                    continue
                res_add = requests.post(ANKI_CONNECT_URL, json={
                    "action": "modelFieldAdd", "version": 6,
                    "params": {"modelName": MODEL_NAME, "fieldName": ten,
                               "index": vi_tri}}, timeout=10)
                if res_add.json().get("error"):
                    print(f"\n❌ Thêm field {ten} thất bại: {res_add.json().get('error')}")
                else:
                    print(f"\n🆕 Đã thêm field {ten} — Anki sẽ đòi FULL SYNC một lần.")

        res_style = requests.post(ANKI_CONNECT_URL, json={"action": "updateModelStyling", "version": 6, "params": {"model": {"name": MODEL_NAME, "css": shared_css}}}, timeout=5)
        if res_style.json().get("error"):
            print(f"\n❌ CSS thất bại: {res_style.json().get('error')}")

        res_tmpl = requests.post(ANKI_CONNECT_URL, json={"action": "updateModelTemplates", "version": 6, "params": {
            "model": {"name": MODEL_NAME, "templates": {"Pure Engine Typing Card v25": {"Front": front_template, "Back": back_template}}}
        }}, timeout=5)
        if res_tmpl.json().get("error"):
            print(f"\n❌ Templates thất bại: {res_tmpl.json().get('error')}")

        print("Hoàn tất. ---")
    except Exception as e:
        print(f"\n❌ Không kết nối được AnkiConnect: {e}")
