# ==============================================================================
# --- DỰNG & ĐẨY THẺ: build field, tải audio, addNote, đọc ngược note, in tóm tắt.
# Tách từ anki_client.py (03/08/2026, QD-18). Caller vẫn import anki_client —
# mặt tiền ở đó re-export đủ tên cũ.
# ⚠️ push_to_anki() đọc các khóa dict do scraper.process_pure_next_data() trả
# về (word, english_meanings, part_of_speech, pos_full, gender,
# raw_dictionary_examples). Nếu đổi tên khóa ở scraper.py, PHẢI sửa lại đây.
# ==============================================================================
import base64
import json
import re

import requests

from . import grammar
from .chu_nga import nfc
from .config import ANKI_CONNECT_URL, MODEL_NAME, STAGE1_DECK
from .topics import TOPIC_TAG_PREFIX, topic_tag, pos_full as ten_pos_day_du
from .utils import log_warn, log_fail, strip_accents_perfectly, hl_to_bracket
from .html_builder import (
    build_examples_html,
    parse_examples_html,
    parse_gender_badge,
    parse_aspect_badge,
    parse_meaning_html,
    parse_raw_examples,
)
from .audio import fetch_audio_bytes


def store_media_file(filename, data_bytes):
    """Lưu bytes vào thư mục media của Anki (base64). Trả về True nếu thành công."""
    b64 = base64.b64encode(data_bytes).decode("ascii")
    try:
        res = requests.post(ANKI_CONNECT_URL, json={
            "action": "storeMediaFile", "version": 6,
            "params": {"filename": filename, "data": b64}
        }, timeout=20)
        if res.json().get("error"):
            log_fail(f"storeMediaFile lỗi: {res.json().get('error')}")
            return False
        return True
    except Exception as e:
        log_fail(f"storeMediaFile lỗi mạng: {e}")
        return False


def store_word_audio(clean_word):
    """Tải audio phát âm (OpenRussian -> Google TTS dự phòng khi 500) rồi lưu vào
    Anki media. Trả về (audio_field, source): '[sound:ru_audio_X.mp3]' + nguồn
    ('openrussian'/'google_tts'), hoặc ('', '') nếu cả hai nguồn đều hụt."""
    data, source = fetch_audio_bytes(clean_word)
    if not data:
        return "", ""
    filename = f"ru_audio_{clean_word}.mp3"
    if store_media_file(filename, data):
        return f"[sound:{filename}]", source
    return "", ""


def build_card_fields(word, data):
    """Dựng field thẻ (TRỪ Audio/Image) + metadata từ dữ liệu cào được. Dùng CHUNG
    cho thêm thẻ mới (push_to_anki) và làm lại thẻ (pipeline.redo_note_id) để hai
    luồng luôn tạo ra thẻ giống hệt nhau. KHÔNG đụng AnkiConnect."""
    clean_word = strip_accents_perfectly(word)
    pos_clean = data["part_of_speech"].lower().strip()
    pos_full = data["pos_full"]
    gender_lower = str(data["gender"]).lower().strip()

    # Ba badge ngữ pháp. Dựng qua grammar.* để thẻ MỚI và thẻ CŨ (scripts/backfill_badge.py)
    # luôn ra cùng một thứ — nhãn giống nay chỉ còn MỘT bảng, ở grammar.NHAN_GIONG.
    grammar_rec = data.get("grammar") or {}
    if grammar_rec:
        # Nạp cache RAM ngay: từ user thêm hằng ngày tự có mặt, không phải chạy
        # `cao_nguphap.py --anki` bù về sau.
        # 🔴 `ghi_the=False` — hàm này KHÔNG ĐỤNG AnkiConnect (xem docstring), và
        # phần ghi thẻ ở đây vốn THỪA: `GrammarJSON` đi thẳng vào `fields` ngay
        # bên dưới, `push_to_anki`/`redo_note_id` ghi nó cùng cả thẻ theo ĐÚNG
        # note id. Bản cũ ghi thêm một lần nữa bằng cách TÌM THẺ THEO TÊN đã bỏ
        # dấu nhấn ⇒ lúc tạo `наре́зать` nó đè lên thẻ `нареза́ть` đang có. Đó là
        # nguồn gốc thẻ hỏng phát hiện 27/08 (QD-39).
        grammar.remember(clean_word, grammar_rec, ghi_the=False)
    gender_badge_html = (grammar.gender_badge_html(clean_word, gender_lower, grammar_rec)
                         if pos_clean in ("n", "noun") else "")
    aspect_badge_html = grammar.aspect_badge_html(data.get("aspect", ""), clean_word)
    reflexive_badge_html = grammar.reflexive_badge_html(data.get("reflexive"))
    gender_label = re.sub(r"<[^>]+>", "", gender_badge_html)

    meaning_html = '<ol class="meaning-list">'
    for m in data["english_meanings"]: meaning_html += f"<li>{m}</li>"
    meaning_html += "</ol>"

    examples_html, vi_meaning, simplified_examples, topic_slug, pos_ai = build_examples_html(
        clean_word,
        data.get("raw_dictionary_examples", []),
        data.get("english_meanings", [])
    )

    # 🔴 TỪ LOẠI: nguồn trước, AI VÁ CHỖ NGUỒN BỎ TRỐNG (QD-41). OpenRussian trả
    # thẳng "other" cho 93/1290 thẻ (trạng từ, giới từ, liên từ, trợ từ dồn một
    # rọ) — `scraper` đã đổi rọ đó thành RỖNG, và đây là chỗ lấp.
    # Vì sao lấp ở ĐÂY chứ không gọi AI riêng: lượt AI ngay trên đằng nào cũng
    # chạy cho MỌI thẻ mới VÀ mọi lần /sua, nên từ loại đi nhờ là 0 request thêm.
    # Và vì `/sua` chui qua đúng hàm này, 93 thẻ vá xong KHÔNG bị lật ngược.
    # Nguồn nói được thì tin nguồn: nó biết chắc `noun`/`verb`, AI chỉ đoán.
    if not pos_clean and pos_ai:
        pos_clean = pos_ai
        pos_full = ten_pos_day_du(pos_ai) or ""

    fields = {
        "Word": data["word"], "WordClean": clean_word, "Meaning": meaning_html,
        "Vietnamese": vi_meaning, "PoS": pos_clean, "PoSFull": pos_full,
        "GenderBadge": gender_badge_html, "AspectBadge": aspect_badge_html,
        "ReflexiveBadge": reflexive_badge_html, "ExamplesHTML": examples_html,
        "RawExamples": json.dumps(data.get("raw_dictionary_examples", []), ensure_ascii=False),
        # separators gọn: field này thuần máy đọc, không ai mở ra ngắm.
        "GrammarJSON": (json.dumps(grammar_rec, ensure_ascii=False,
                                   separators=(",", ":")) if grammar_rec else ""),
        # BẢNG CHIA + CẶP THỂ có ngay từ lúc tạo thẻ. Chúng thuần dữ liệu cào
        # được nên không có lý do gì bắt user đợi tới lượt lô của từ đó.
        # 🔴 Vào `BangMay`, KHÔNG vào `HuongDan` nữa (QD-26): `HuongDan` từ nay
        # thuần phần người soạn, nên thẻ mới để TRỐNG ô đó cho tới khi lô soạn.
        "BangMay": grammar.khoi_may(grammar_rec),
    }

    # Thẻ "khuyết": AI thất bại -> không ví dụ, hoặc ví dụ thô thiếu tiếng Việt.
    ai_degraded = (not simplified_examples) or not any(
        (ex.get("vi") or ex.get("vietnamese") or "").strip() for ex in simplified_examples
    )

    return {
        "fields": fields,
        "clean_word": clean_word,
        "topic_slug": topic_slug,
        "simplified_examples": simplified_examples,
        "vi_meaning": vi_meaning,
        "gender_label": gender_label,
        "aspect_label": grammar.NHAN_THE.get(
            (data.get("aspect") or "").strip().lower(), ("", ""))[1],
        "reflexive_label": grammar.NHAN_PHAN_THAN if data.get("reflexive") else "",
        "pos_full": pos_full,
        "en_meanings": data["english_meanings"],
        "ai_degraded": ai_degraded,
    }


def note_to_card_info(dup):
    """Hàm NGHỊCH của build_card_fields(): note đã nằm trong Anki -> dict card_info
    ĐÚNG KHUÔN mà push_to_anki() trả về. Nhờ vậy bot hiện thẻ CŨ (tra từ điển) bằng
    đúng bộ khung hiển thị của thẻ MỚI, không phải viết hai kiểu trình bày.

    🔴 RÀNG BUỘC VĨNH VIỄN đi kèm quyết định "gõ từ đã có thẻ ⇒ trả nguyên mục từ
    điển" (21/07/2026): **mỗi hàm dựng HTML phải có hàm nghịch đọc ngược nó**. Đổi
    cấu trúc HTML mà quên sửa hàm nghịch thì bảng tra hiện **TRỐNG RỖNG** — không
    lỗi, không cảnh báo, chỉ là ô trắng. Khoá bằng test vòng tròn dựng→bóc
    (`HighlightKhongBiNuot.test_dung_roi_boc_lai_KHONG_MAT_CHU`).

    dup: 1 phần tử find_duplicate_notes() trả về (đã có sẵn fields + tags).
    Các khóa THÊM so với card_info gốc (thẻ mới chưa có): note_id, status_text,
    has_audio, image, raw_count."""
    fields = dup.get("fields") or {}
    en_meanings = parse_meaning_html(fields.get("Meaning", ""))
    topic_tags = [t for t in (dup.get("tags") or []) if t.startswith(TOPIC_TAG_PREFIX)]
    audio = fields.get("Audio", "")
    examples = parse_examples_html(fields.get("ExamplesHTML", ""))
    # Cùng định nghĩa "thẻ khuyết" như build_card_fields() -> thẻ cũ hỏng cũng
    # được cảnh báo + mời bấm nút làm lại ngay trong bảng tra từ điển.
    ai_degraded = (not examples) or not any((ex.get("vi") or "").strip() for ex in examples)
    return {
        "word": fields.get("Word", "") or dup.get("word", ""),
        "clean_word": fields.get("WordClean", ""),
        "en_meanings": en_meanings or ["(thẻ không có nghĩa tiếng Anh)"],
        "vi_meaning": fields.get("Vietnamese", "").strip(),
        "pos": fields.get("PoSFull", "") or fields.get("PoS", ""),
        "gender": parse_gender_badge(fields.get("GenderBadge", "")),
        "aspect": parse_aspect_badge(fields.get("AspectBadge", "")),
        "reflexive": parse_aspect_badge(fields.get("ReflexiveBadge", "")),
        "deck": dup.get("deck", "?"),
        "is_forced": False,
        "simplified_examples": examples,
        "ai_degraded": ai_degraded,
        "topic": topic_tags[0] if topic_tags else "",
        # Thẻ CŨ không lưu lại nguồn audio, chỉ biết có tiếng hay không
        "audio_source": "",
        "has_audio": bool(re.search(r"\[sound:[^\]]+\]", audio)),
        "image": fields.get("Image", "").strip(),
        "raw_count": len(parse_raw_examples(fields.get("RawExamples", ""))),
        "note_id": dup.get("note_id"),
        "status_text": dup.get("status_text", ""),
    }


def push_to_anki(word, data, deck_name, is_forced=False):
    """Đẩy note lên Anki. Trả về (success, card_info_dict) để hiển thị tóm tắt.

    deck_name=None -> chế độ TỰ ĐỘNG: thẻ vào STAGE1_DECK (giai đoạn LÀM QUEN);
    tag topic:: (AI chọn) ghi sẵn deck chủ đề đích. Thẻ đi tiếp theo lộ trình
    hai giai đoạn do run_don() điều khiển: 0-quen -> 1-go -> <kho>::<topic>.
    Field Stage để TRỐNG (không ghi) nên thẻ mới luôn bắt đầu ở GĐ1.
    """
    built = build_card_fields(word, data)
    clean_word = built["clean_word"]
    topic_slug = built["topic_slug"]

    # Audio: bot TỰ tải (OpenRussian -> Google TTS nếu 500) rồi lưu media, thay vì
    # để AnkiConnect tự tải từ URL (không bắt được lỗi 500 để dùng phao dự phòng).
    audio_field, audio_source = store_word_audio(clean_word)

    # Thêm trùng (force) dùng option allowDuplicate chính thống của AnkiConnect.
    # topic_tag() trả None khi slug không xếp được (QD-38) -> lọc, đừng để lọt
    # [None] vào tags: Anki sẽ nhận một tag rỗng/hỏng mà không báo gì.
    note_tags = [t for t in [topic_tag(topic_slug)] if t] if topic_slug else []

    # Chế độ tự động: thẻ mới vào deck LÀM QUEN; tag topic:: đã ghi deck đích.
    if not deck_name:
        deck_name = STAGE1_DECK
        try:
            requests.post(ANKI_CONNECT_URL, json={
                "action": "createDeck", "version": 6, "params": {"deck": deck_name}
            }, timeout=5)
        except Exception as e:
            log_warn(f"Không tạo/kiểm tra được deck '{deck_name}': {e}")

    fields = dict(built["fields"])
    fields["Audio"] = audio_field
    # KHÔNG ghi "Stage": để trống nghĩa là thẻ bắt đầu ở GĐ1 (làm quen).
    # KHÔNG còn "Image": field đã bị xoá khỏi note type 26/07/2026 — ghi vào một
    # field không tồn tại thì AnkiConnect từ chối cả note.

    payload = {
        "action": "addNote", "version": 6,
        "params": {
            "note": {
                "deckName": deck_name, "modelName": MODEL_NAME,
                "fields": fields,
                "options": {"allowDuplicate": is_forced},
                "tags": note_tags,
            }
        }
    }

    card_info = {
        "word": data["word"],
        "clean_word": clean_word,
        "en_meanings": built["en_meanings"],
        "vi_meaning": built["vi_meaning"],
        "pos": built["pos_full"],
        "gender": built["gender_label"],
        "aspect": built["aspect_label"],
        "reflexive": built["reflexive_label"],
        "deck": deck_name,
        "is_forced": is_forced,
        "simplified_examples": built["simplified_examples"],
        "ai_degraded": built["ai_degraded"],
        "topic": (topic_tag(topic_slug) or "") if topic_slug else "",
        "audio_source": audio_source,   # "openrussian" / "google_tts" / ""
    }

    try:
        res = requests.post(ANKI_CONNECT_URL, json=payload, timeout=10)
        result = res.json()
        if result.get("error"):
            log_fail(f"AnkiConnect từ chối thêm note: {result.get('error')}")
            card_info["error"] = str(result.get("error"))
            return False, card_info
        return True, card_info
    except Exception as e:
        log_fail(f"Không kết nối được AnkiConnect: {e}")
        card_info["error"] = str(e)
        return False, card_info


def print_card_summary(card_info, elapsed):
    """In tóm tắt thẻ vừa tạo - đơn giản, không bảng kẻ."""
    w = hl_to_bracket(card_info["word"])
    vi = card_info["vi_meaning"]
    en = ", ".join(card_info["en_meanings"])
    pos = card_info["pos"]
    gender = card_info["gender"]
    deck = card_info["deck"]
    forced = " ⚠️ FORCE" if card_info["is_forced"] else ""
    examples = card_info.get("simplified_examples", [])

    print(f"\n  ═══ 📇 THẺ MỚI{forced}: {w} ═══")
    print(f"  🇷🇺 Từ:         {w}")
    print(f"  🇬🇧 Nghĩa:      {en}")
    print(f"  🇻🇳 Tiếng Việt:  {vi}")
    phu = [x for x in (gender, card_info.get("aspect")) if x]
    print(f"  🏷️  Từ loại:    {pos}" + (f" ({', '.join(phu)})" if phu else ""))
    if card_info.get("topic"):
        print(f"  📂 Chủ đề:     {card_info['topic']}")
    _audio_src = card_info.get("audio_source", "")
    if _audio_src == "google_tts":
        print(f"  🔊 Audio:      [Google TTS - OpenRussian lỗi]")
    elif _audio_src == "openrussian":
        print(f"  🔊 Audio:      [OpenRussian]")
    else:
        print(f"  🔊 Audio:      [KHÔNG có - cả 2 nguồn đều hụt]")

    if examples:
        print(f"  ─────────────────────────────────────")
        for i, ex in enumerate(examples[:3]):
            ru = hl_to_bracket(ex.get("ru", ""))
            en_ex = hl_to_bracket(ex.get("en", ""))
            vi_ex = hl_to_bracket(ex.get("vi") or ex.get("vietnamese") or "")
            print(f"  💡 Ví dụ {i+1}:")
            print(f"     RU: {ru}")
            print(f"     EN: {en_ex}")
            if vi_ex:
                print(f"     VI: {vi_ex}")

    if card_info.get("ai_degraded"):
        print(f"  ⚠️  AI không tạo được ví dụ/nghĩa Việt - thẻ THIẾU nội dung, nên sửa lại sau.")

    print(f"  ─────────────────────────────────────")
    print(f"  📦 Bộ bài: {deck} │ ⏱️ {elapsed:.1f}s\n")


# ==============================================================================
# --- NHÓM ĐỘNG TỪ CÙNG GỐC (QD-39) ---
# 🔴 DANH TÍNH MỘT TỪ Ở ĐÂY LÀ `acc` (CÓ dấu nhấn), KHÔNG phải `WordClean`. Đo
# 27/08 trên 14 871 động từ: mặt chữ bỏ dấu nhấn nhập nhằng **156 ca**, `acc`
# còn **5**, `acc`+thể còn **2** — và 2 ca cuối là từ điển lặp dòng y hệt nên
# chọn mục nào cũng thế. Bỏ dấu nhấn là bỏ đúng thứ phân biệt `нареза́ть` (đang
# thái) với `наре́зать` (thái xong); chính chỗ đó đã ghi đè thẻ thật.
# Đã cân nhắc lưu `id` mục từ OpenRussian: BÁC — thêm khoá ⇒ phải cào lại cả
# 1253 thẻ, mà id là số của người khác nên không tự kiểm được; còn `acc` đem so
# với ô `Word` là biết ngay thẻ có mang nhầm dữ liệu từ khác không — chính phép
# so đó tìm ra thẻ `нареза́ть` hỏng.
# ==============================================================================
_NHOM_MEMO = None


def nhom_dong_tu(notes=None, lam_moi=False):
    """Bản đồ `acc` -> danh sách các thẻ ĐỘNG TỪ cùng gốc ĐANG CÓ trong kho.

    Mỗi thành viên: `{"acc", "aspect", "vi", "wc", "noteId", "rank", "rec",
    "may"}` — kèm luôn bản ghi và ô `BangMay` hiện tại để người gọi dựng lại mặt
    thẻ mà khỏi đọc kho lần hai. Nhóm gồm
    cả chính nó, xếp CHƯA HOÀN THÀNH trước rồi tới hạng tần suất tăng dần —
    `rank` đã nằm sẵn trên cả 1253 thẻ, không phải tra nguồn ngoài.

    Cạnh nối = `partners` thẻ này trỏ đúng `acc` thẻ kia, so khớp CHÍNH XÁC:
    đo 27/08 ra 106 cạnh khớp trong kho, 91 cạnh trỏ ra ngoài (từ chưa có thẻ —
    đúng, không phải lỗi). `notes` = `notesInfo` sẵn có, để lệnh chạy hàng loạt
    khỏi đọc kho lần hai; không đưa thì tự đọc rồi nhớ trong cùng tiến trình.
    """
    global _NHOM_MEMO
    tu_doc = notes is None
    if tu_doc:
        if _NHOM_MEMO is not None and not lam_moi:
            return _NHOM_MEMO
        from . import anki_client
        notes = anki_client._ac(
            "notesInfo", timeout=120,
            notes=anki_client._ac("findNotes", query=f'note:"{MODEL_NAME}"'))

    thanh_vien, canh = {}, {}
    for n in notes or []:
        f = n.get("fields", {})
        try:
            rec = json.loads((f.get("GrammarJSON", {}).get("value") or "").strip() or "{}")
        except ValueError:
            continue                    # ô hỏng -> bỏ qua, đừng giết cả lượt
        if rec.get("pos") != "verb":
            continue
        a = nfc(rec.get("acc"))
        if not a or a in thanh_vien:
            continue                    # `acc` trùng = thẻ mang nhầm dữ liệu; test bắt riêng
        thanh_vien[a] = {
            "acc": a, "aspect": rec.get("aspect"), "rank": rec.get("rank") or 10 ** 9,
            "wc": (f.get("WordClean", {}).get("value") or "").strip(),
            "vi": re.sub(r"<[^>]+>", "", f.get("Vietnamese", {}).get("value") or "").strip(),
            "noteId": n.get("noteId"), "rec": rec,
            "may": f.get("BangMay", {}).get("value") or "",
        }
        canh[a] = [nfc(p) for p in (rec.get("partners") or []) if p]

    ke = {a: set() for a in thanh_vien}
    for a, ps in canh.items():
        for p in ps:
            if p in thanh_vien and p != a:
                ke[a].add(p)
                ke[p].add(a)

    ra, da_xet = {}, set()
    for a in thanh_vien:
        if a in da_xet:
            continue
        cum, hang_doi = [], [a]
        while hang_doi:
            x = hang_doi.pop()
            if x in da_xet:
                continue
            da_xet.add(x)
            cum.append(x)
            hang_doi += [y for y in ke[x] if y not in da_xet]
        cum = sorted((thanh_vien[x] for x in cum),
                     key=lambda m: (m["aspect"] != "imperfective", m["rank"]))
        for m in cum:
            ra[m["acc"]] = cum
    if tu_doc:
        _NHOM_MEMO = ra
    return ra
