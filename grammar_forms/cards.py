# ==============================================================================
# --- DỰNG FIELD + ĐẨY THẺ BIẾN CÁCH LÊN ANKI ---
# Mọi lệnh gọi AnkiConnect của mảng grammar_forms gom hết ở file này.
# Dùng lại store_media_file()/trigger_sync() của anki_tools (hạ tầng chung),
# nhưng model/deck/field đều là của riêng mảng này.
# ==============================================================================
import json
import os

import requests

from anki_tools.anki_client import store_media_file
from anki_tools.audio import fetch_audio_bytes
from anki_tools.config import ANKI_CONNECT_URL
from anki_tools.utils import apply_hl, log_fail, log_warn, strip_accents_perfectly

from .config import (
    CHIPHOI_CARD_NAME,
    CHIPHOI_FIELDS,
    CHIPHOI_MODEL,
    KIND_LABELS,
    PLURAL_CARD_NAME,
    PLURAL_DECK,
    PLURAL_FIELDS,
    PLURAL_MODEL,
)

_TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")


def read_template(filename):
    with open(os.path.join(_TEMPLATES_DIR, filename), encoding="utf-8") as f:
        return f.read()


def anki(action, **params):
    """Gọi AnkiConnect. Trả về result, ném RuntimeError nếu Anki báo lỗi."""
    res = requests.post(ANKI_CONNECT_URL,
                        json={"action": action, "version": 6, "params": params},
                        timeout=60)
    out = res.json()
    if out.get("error"):
        raise RuntimeError(f"{action}: {out['error']}")
    return out.get("result")


# ------------------------------------------------------------------ thiết lập
def setup_model():
    """Tạo model RU_Plural nếu chưa có, hoặc BỔ SUNG field còn thiếu cho model cũ.

    An toàn với 26 thẻ sẵn có: modelFieldAdd chỉ thêm ô rỗng vào cuối, không đụng
    nội dung hay tiến trình học. Luôn ghi đè lại template + CSS cho khớp code.
    """
    css = read_template("plural.css")
    front = read_template("plural_front.html")
    back = read_template("plural_back.html")

    if PLURAL_MODEL not in (anki("modelNames") or []):
        anki("createModel", modelName=PLURAL_MODEL, inOrderFields=PLURAL_FIELDS, css=css,
             cardTemplates=[{"Name": PLURAL_CARD_NAME, "Front": front, "Back": back}])
        print(f"✅ Đã tạo model '{PLURAL_MODEL}'.")
        return True

    existing = anki("modelFieldNames", modelName=PLURAL_MODEL) or []
    for field in PLURAL_FIELDS:
        if field not in existing:
            anki("modelFieldAdd", modelName=PLURAL_MODEL, fieldName=field)
            print(f"➕ Thêm ô '{field}' vào model '{PLURAL_MODEL}'.")

    # Tên card template của thẻ cũ có thể khác -> ghi vào đúng tên đang tồn tại
    names = list((anki("modelTemplates", modelName=PLURAL_MODEL) or {}).keys())
    card_name = names[0] if names else PLURAL_CARD_NAME
    anki("updateModelTemplates",
         model={"name": PLURAL_MODEL, "templates": {card_name: {"Front": front, "Back": back}}})
    anki("updateModelStyling", model={"name": PLURAL_MODEL, "css": css})
    print(f"✅ Đã cập nhật template + CSS cho '{PLURAL_MODEL}' (card: {card_name}).")
    return True


def setup_chiphoi_model():
    """Tạo/cập nhật model RU_ChiPhoi. Idempotent — chạy lại bao nhiêu lần cũng được.

    🔴 Lần ĐẦU chạy là **schema mod** ⇒ Anki đòi full sync. Đó là việc phải có
    tay người (laptop Upload → VPS Download); `setup.py` in cảnh báo, đừng tự
    gọi `trigger_sync()` sau hàm này — AnkiConnect không chọn được chiều sync,
    mà chọn nhầm chiều là ghi đè sạch bản còn lại, không lùi được.
    """
    css = read_template("chiphoi.css")
    front = read_template("chiphoi_front.html")
    back = read_template("chiphoi_back.html")

    if CHIPHOI_MODEL not in (anki("modelNames") or []):
        anki("createModel", modelName=CHIPHOI_MODEL, inOrderFields=CHIPHOI_FIELDS, css=css,
             cardTemplates=[{"Name": CHIPHOI_CARD_NAME, "Front": front, "Back": back}])
        print(f"✅ Đã tạo model '{CHIPHOI_MODEL}' (LẦN ĐẦU ⇒ cần full sync).")
        return "moi"

    existing = anki("modelFieldNames", modelName=CHIPHOI_MODEL) or []
    for field in CHIPHOI_FIELDS:
        if field not in existing:
            anki("modelFieldAdd", modelName=CHIPHOI_MODEL, fieldName=field)
            print(f"➕ Thêm ô '{field}' vào model '{CHIPHOI_MODEL}'.")

    names = list((anki("modelTemplates", modelName=CHIPHOI_MODEL) or {}).keys())
    card_name = names[0] if names else CHIPHOI_CARD_NAME
    anki("updateModelTemplates",
         model={"name": CHIPHOI_MODEL, "templates": {card_name: {"Front": front, "Back": back}}})
    anki("updateModelStyling", model={"name": CHIPHOI_MODEL, "css": css})
    print(f"✅ Đã cập nhật template + CSS cho '{CHIPHOI_MODEL}' (card: {card_name}).")
    return "cu"


def doc_nghia_tu_vung(tu_clean):
    """Nghĩa tiếng Việt của vài từ trong deck TỪ VỰNG -> `{WordClean: nghĩa}`.

    Dùng để đặt TÊN DECK (`в — cách 4/6 — trong, ở trong, vào`) mà không phải gõ
    lại nghĩa vào file dữ liệu: gõ lại là dựng bản chép thứ hai, rồi sửa một bên
    quên bên kia. Hỏi đúng mấy từ cần chứ không kéo cả 1138 thẻ về.
    """
    ra = {}
    for tu in tu_clean:
        try:
            ids = anki("findNotes", query=f'note:"RU_Word" WordClean:"{tu}"') or []
            if not ids:
                continue
            info = (anki("notesInfo", notes=ids[:1]) or [{}])[0]
            ra[tu] = (info.get("fields", {}).get("Vietnamese", {}).get("value") or "").strip()
        except Exception as e:
            log_warn(f"Không đọc được nghĩa của '{tu}': {e}")
    return ra


def rename_legacy_deck(old_name, new_name):
    """Đổi tên deck mà GIỮ NGUYÊN tiến trình học.

    AnkiConnect không có lệnh đổi tên deck, nên: tạo deck mới -> chuyển toàn bộ
    card sang (changeDeck KHÔNG đụng lịch ôn/interval) -> xóa vỏ deck cũ đã rỗng.
    Trả về số thẻ đã chuyển (0 nếu deck cũ không tồn tại / đã rỗng).
    """
    decks = anki("deckNames") or []
    if old_name not in decks:
        return 0
    card_ids = anki("findCards", query=f'deck:"{old_name}"') or []
    anki("createDeck", deck=new_name)
    if card_ids:
        anki("changeDeck", cards=card_ids, deck=new_name)
    # cardsToo=False: deck lúc này đã rỗng, chỉ xóa cái vỏ
    anki("deleteDecks", decks=[old_name], cardsToo=False)
    return len(card_ids)


# ------------------------------------------------------------------ dựng thẻ
def build_fields(data, ai_result, kind=""):
    """Ghép dữ liệu cào được + kết quả AI thành dict field của model RU_Plural."""
    meaning_html = '<ol class="meaning-list">'
    for m in data["english"]:
        meaning_html += f"<li>{m}</li>"
    meaning_html += "</ol>"

    examples_html = ""
    for i, ex in enumerate(ai_result["simplified_examples"]):
        open_attr = " open" if i == 0 else ""
        label = " (Xem ngay)" if i == 0 else " (Bấm để mở rộng)"
        examples_html += (
            f'<details class="example-toggle"{open_attr}>'
            f'<summary class="example-summary">💡 Example {i + 1}{label}</summary>'
            f'<div class="example-content">'
            f'<div class="ex-ru">{apply_hl(ex["ru"])}</div>'
            f'<div class="ex-en">{apply_hl(ex["en"])}</div>'
            f'<div class="ex-vi"><span class="arrow">➔</span>'
            f'<span class="vi-text">{apply_hl(ex["vi"])}</span></div>'
            f'</div></details>'
        )

    return {
        "Word": data["word"],
        "WordClean": strip_accents_perfectly(data["word"]),
        "Plural": data["plural"],
        "PluralClean": strip_accents_perfectly(data["plural"]),
        "Meaning": meaning_html,
        "Vietnamese": ai_result["vietnamese_meaning"],
        "ExamplesHTML": examples_html,
        "KindLabel": KIND_LABELS.get(kind, ""),
        "RawExamples": json.dumps(ai_result["simplified_examples"], ensure_ascii=False),
    }


def store_audio(text, prefix):
    """Tải phát âm rồi lưu vào media Anki. Trả về ('[sound:...]', nguồn) hoặc ('','').

    Dùng chung fetch_audio_bytes() của anki_tools: OpenRussian đọc trước (giọng
    tự nhiên, đọc được cả dạng số nhiều), hụt thì rơi về Google TTS.
    """
    clean = strip_accents_perfectly(text)
    if not clean:
        return "", ""
    data, source = fetch_audio_bytes(clean)
    if not data:
        return "", ""
    filename = f"{prefix}_{clean}.mp3"
    if store_media_file(filename, data):
        return f"[sound:{filename}]", source
    return "", ""


def find_existing(word_clean):
    """Tìm note RU_Plural đã có cho từ này. Trả về list note_id."""
    try:
        return anki("findNotes",
                    query=f'note:"{PLURAL_MODEL}" WordClean:"{word_clean}"') or []
    except Exception as e:
        log_warn(f"Không kiểm tra được trùng lặp: {e}")
        return []


def existing_words():
    """Tập WordClean của MỌI thẻ số nhiều đã có — để luồng thêm loạt lọc sẵn từ
    trùng bằng 1 lượt gọi, thay vì hỏi Anki từng từ một.
    Trả về set (có thể rỗng), hoặc None nếu AnkiConnect lỗi — None ≠ rỗng: lỗi
    thì KHÔNG được coi là 'chưa có từ nào' kẻo đề nghị thêm trùng cả deck."""
    try:
        note_ids = anki("findNotes", query=f'note:"{PLURAL_MODEL}"') or []
        if not note_ids:
            return set()
        notes = anki("notesInfo", notes=note_ids) or []
        words = {
            (n.get("fields", {}).get("WordClean", {}).get("value") or "").strip().lower()
            for n in notes
        }
        words.discard("")
        return words
    except Exception as e:
        log_warn(f"Không lấy được danh sách từ đã có: {e}")
        return None


def add_note(fields, deck=PLURAL_DECK, tags=None, model=PLURAL_MODEL):
    """Thêm note mới. Trả về (note_id | None, lỗi | '').

    `model` mặc định là RU_Plural để mọi lời gọi cũ không phải sửa; mảng thẻ chi
    phối truyền `CHIPHOI_MODEL` vào.
    """
    try:
        anki("createDeck", deck=deck)
        note_id = anki("addNote", note={
            "deckName": deck,
            "modelName": model,
            "fields": fields,
            "options": {"allowDuplicate": False},
            "tags": tags or [],
        })
        return note_id, ""
    except RuntimeError as e:
        return None, str(e)
    except Exception as e:
        log_fail(f"Không kết nối được AnkiConnect: {e}")
        return None, str(e)


def update_note(note_id, fields):
    """Ghi đè field vào note có sẵn (giữ nguyên note_id -> tiến trình học không đổi)."""
    try:
        anki("updateNoteFields", note={"id": note_id, "fields": fields})
        return True
    except Exception as e:
        log_fail(f"Cập nhật note {note_id} thất bại: {e}")
        return False


def get_note(note_id):
    """Đọc 1 note: {'fields': {...}, 'tags': [...]} hoặc None."""
    try:
        infos = anki("notesInfo", notes=[note_id]) or []
        if not infos:
            return None
        return {
            "fields": {k: v.get("value", "") for k, v in infos[0].get("fields", {}).items()},
            "tags": infos[0].get("tags", []),
        }
    except Exception as e:
        log_warn(f"Không đọc được note {note_id}: {e}")
        return None


def deck_note_ids(deck=PLURAL_DECK):
    """Toàn bộ note RU_Plural trong deck (cho luồng vá thẻ cũ hàng loạt)."""
    try:
        return anki("findNotes", query=f'deck:"{deck}" note:"{PLURAL_MODEL}"') or []
    except Exception as e:
        log_warn(f"Không liệt kê được thẻ deck '{deck}': {e}")
        return []
