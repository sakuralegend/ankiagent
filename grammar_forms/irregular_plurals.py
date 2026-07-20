# ==============================================================================
# --- DỰNG DANH SÁCH DANH TỪ CÓ SỐ NHIỀU BẤT QUY TẮC ---
# Chạy MỘT LẦN (offline, không đụng Anki) để sinh data/irregular_plurals.tsv —
# nguồn từ cho deck GRAMMAR::plural-irregular.
#
# Cách làm: KHÔNG chép danh sách từ giáo trình (dễ sót, dễ sai) mà SUY RA từ
# chính dữ liệu OpenRussian: với mỗi danh từ, dự đoán số nhiều CHUẨN theo quy
# tắc, so với số nhiều THẬT trong từ điển — lệch nhau = bất quy tắc.
#
# Mẹo quan trọng: thân từ suy từ GENITIVE số ít, không phải nominative. Nhờ vậy
# nguyên âm chạy (отец/отца -> отцы) không bị coi nhầm là bất quy tắc, vì nó
# xuất hiện ở MỌI cách chứ không riêng số nhiều.
#
# Chạy:  python -m grammar_forms.irregular_plurals
# ==============================================================================
import csv
import json
import os
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

import requests
from bs4 import BeautifulSoup

from anki_tools.utils import log_warn, strip_accents_perfectly

_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(_PROJECT_ROOT, "data")

# Dump từ điển OpenRussian (~8MB, 27k danh từ, đủ 12 ô biến cách + tần suất).
# Gitignore: tải lại bằng chính script này khi cần.
NOUNS_CSV = os.path.join(DATA_DIR, "nouns.csv")
NOUNS_URL = "https://raw.githubusercontent.com/Badestrand/russian-dictionary/master/nouns.csv"

# Cache level/plural cào từ web (1 request/từ) — để chạy lại không tải lại.
CACHE_FILE = os.path.join(DATA_DIR, "openrussian_cache.json")
OUT_TSV = os.path.join(DATA_DIR, "irregular_plurals.tsv")

# Chỉ xét N danh từ thông dụng nhất (nouns.csv xếp sẵn theo tần suất).
# 2500 phủ trọn A1-B1 và phần lớn B2 — xa hơn nữa toàn từ hiếm không đáng học.
TOP_N = 2500

# ⚠️ KHÔNG dùng level làm bộ lọc — đã thử và phải bỏ. OpenRussian chỉ gắn level
# cho một tập nhỏ, phần còn lại bị đẩy lên C1/C2 vô tội vạ: юг (rank 889) = C1,
# паспорт = C1, яблоко = C1, сахар = C1, село = C2, повар = C2 — toàn từ A2/B1.
# Lọc theo level làm mất 63/133 từ, trong đó rất nhiều từ lõi. Thứ hạng tần suất
# (TOP_N) mới là thước đo đáng tin. Level vẫn được ghi ra TSV để tham khảo.
LEVELS_KEEP = {"A1", "A2", "B1", "B2"}

VELAR = "гкх"        # sau г/к/х: viết и chứ không viết ы
HUSH = "жчшщ"        # sau ж/ч/ш/щ: cũng viết и
TSITSE = "ц"         # sau ц: số nhiều viết ы, nhưng trung tính -е -> -а

# TÍNH TỪ ĐƯỢC DÙNG NHƯ DANH TỪ: прихожая (phòng ngoài), подчинённый (cấp dưới),
# набережная (bờ kè), лёгкое (lá phổi). Chúng biến theo quy tắc TÍNH TỪ (-ые/-ие)
# nên bộ dò danh từ luôn báo lệch — dương tính giả, phải loại.
ADJ_SG_ENDINGS = ("ое", "ее", "ая", "яя", "ый", "ий", "ой")
ADJ_PL_ENDINGS = ("ые", "ие")


def _bare(s):
    """Bỏ dấu nhấn (' và U+0301) + về chữ thường, để so sánh dạng từ."""
    return strip_accents_perfectly(s or "").strip()


def download_nouns_csv():
    """Tải dump danh từ nếu chưa có. Trả về True nếu file sẵn sàng."""
    if os.path.exists(NOUNS_CSV) and os.path.getsize(NOUNS_CSV) > 1_000_000:
        return True
    os.makedirs(DATA_DIR, exist_ok=True)
    print(f"⬇️  Đang tải dump từ điển ({NOUNS_URL})...")
    try:
        r = requests.get(NOUNS_URL, timeout=120)
        r.raise_for_status()
    except Exception as e:
        log_warn(f"Không tải được nouns.csv: {e}")
        return False
    with open(NOUNS_CSV, "wb") as f:
        f.write(r.content)
    print(f"✅ Đã tải {len(r.content) // 1024} KB.")
    return True


def guess_gender(sg_nom):
    """Đoán giống khi cột gender của dump bỏ trống (khá nhiều dòng bị trống)."""
    sg = _bare(sg_nom)
    if not sg:
        return ""
    if sg.endswith(("а", "я")):
        return "f"
    if sg.endswith(("о", "е", "ё", "мя")):
        return "n"
    if sg.endswith("ь"):
        return "f"      # đoán thiên về giống cái; giống đực -ь vẫn ra đuôi -и
    return "m"


def predict_plurals(sg_nom, sg_gen, gender):
    """Mọi dạng số nhiều CHUẨN có thể có. Trả về set (nhiều biến thể vì thân từ
    suy được từ cả nominative lẫn genitive, và luật chính tả có chỗ chồng nhau)."""
    sg, gen = _bare(sg_nom), _bare(sg_gen)
    if not sg:
        return set()

    # Thân từ từ nominative (luôn dùng) + từ genitive (bắt nguyên âm chạy).
    stem_nom = sg[:-1] if sg[-1] in "аяьйеоё" else sg
    stems = {stem_nom}
    # ⚠️ Chỉ mượn thân genitive khi nó NGẮN ĐI (отец/отца -> отц): đó mới là
    # nguyên âm chạy, hiện tượng của mọi cách. Khi thân genitive DÀI RA thì đó
    # là phụ tố mọc thêm (мать/матери, дочь/дочери) và chính nó LÀ cái bất quy
    # tắc cần bắt — mượn vào sẽ khiến мать/дочь bị coi nhầm là đúng quy tắc.
    if gen and gen[-1] in "аяыиую" and len(gen) - 1 <= len(stem_nom):
        stems.add(gen[:-1])
    stems.discard("")

    soft = sg[-1] in "яьйеё"
    out = set()
    for stem in stems:
        if not stem:
            continue
        last = stem[-1]
        if gender == "n":
            # Trung tính: -о -> -а, -е -> -я (nhưng sau ж/ч/ш/щ/ц thì viết -а)
            out.add(stem + ("а" if (not soft or last in HUSH + TSITSE) else "я"))
        else:
            # Đực/cái: -ы, đổi thành -и sau г/к/х/ж/ч/ш/щ hoặc khi thân mềm
            out.add(stem + ("и" if (last in VELAR + HUSH or soft) else "ы"))
    return out


def classify(sg_nom, pl_nom, gender):
    """Đặt tên kiểu bất quy tắc để bạn duyệt danh sách cho nhanh."""
    sg, pl = _bare(sg_nom), _bare(pl_nom)
    stem = sg[:-1] if sg and sg[-1] in "аяьйоеё" else sg

    if pl.endswith("ья"):
        return "ья"          # брат -> братья, стул -> стулья
    if pl.endswith("ена"):
        return "ена"         # имя -> имена, время -> времена
    if pl.endswith("ане") or pl.endswith("яне"):
        return "ане"         # гражданин -> граждане
    if pl.endswith("еса"):
        return "еса"         # чудо -> чудеса, небо -> небеса
    if pl.endswith("ева"):
        return "ева"         # хозяин -> хозяева
    if pl.endswith("ята") or pl.endswith("ата"):
        return "ята"         # ребёнок -> ребята, котёнок -> котята
    if pl.endswith("ери"):
        return "ер"          # мать -> матери, дочь -> дочери
    # Thân từ đổi hẳn (suppletive): человек -> люди, ребёнок -> дети.
    # Phải chuẩn hóa ё -> е trước khi so, kẻo жена/жёны cũng bị coi là đổi gốc.
    if stem and not pl.replace("ё", "е").startswith(stem.replace("ё", "е")[:2]):
        return "thay-goc"
    # Chỉ khác nhau ở е <-> ё: жена -> жёны, сестра -> сёстры
    if pl.replace("ё", "е") in predict_plurals(sg_nom, "", gender):
        return "e-yo"
    if gender == "m" and pl.endswith(("а", "я")):
        return "a-я"         # дом -> дома, город -> города
    if gender == "n" and pl.endswith(("и", "ы")):
        return "o-i"         # плечо -> плечи, ухо -> уши
    return "khac"


def find_candidates(top_n=TOP_N):
    """Quét dump, trả về list dict ứng viên bất quy tắc (chưa lọc trình độ)."""
    with open(NOUNS_CSV, encoding="utf-8") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    print(f"📖 Dump có {len(rows)} danh từ, xét {min(top_n, len(rows))} từ thông dụng nhất.")

    out, checked = [], 0
    for rank, r in enumerate(rows[:top_n], 1):
        if r["indeclinable"] == "1" or r["sg_only"] == "1" or r["pl_only"] == "1":
            continue
        pl_raw = (r["pl_nom"] or "").strip()
        sg_raw = (r["sg_nom"] or "").strip() or (r["accented"] or "").strip()
        # "*дом" = dạng OpenRussian đánh dấu hiếm/lý thuyết; "a, b" = 2 biến thể
        if not pl_raw or not sg_raw or pl_raw.startswith("*") or " " in _bare(pl_raw):
            continue
        pl_raw = pl_raw.split(",")[0].strip()
        checked += 1

        if _bare(sg_raw).endswith(ADJ_SG_ENDINGS) and _bare(pl_raw).endswith(ADJ_PL_ENDINGS):
            continue    # tính từ danh từ hóa -> biến theo quy tắc tính từ

        gender = (r["gender"] or "").strip() or guess_gender(sg_raw)
        if _bare(pl_raw) in predict_plurals(sg_raw, r["sg_gen"], gender):
            continue

        out.append({
            "rank": rank,
            "bare": r["bare"],
            "accented": r["accented"] or sg_raw,
            "plural": pl_raw,
            "plural_clean": _bare(pl_raw),
            "gender": gender,
            "kind": classify(sg_raw, pl_raw, gender),
            "en": (r["translations_en"] or "").strip(),
        })

    print(f"🔎 Kiểm tra {checked} danh từ -> {len(out)} ứng viên bất quy tắc.")
    return out


# ------------------------------------------------------------------ trình độ
def _load_cache():
    try:
        with open(CACHE_FILE, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def _save_cache(cache):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=1, sort_keys=True)


def fetch_word_meta(word):
    """Cào level (A1..C2) + số nhiều + giống của 1 từ từ trang OpenRussian.
    Dump không có cột level nên phải lấy từ web. Trả về dict (rỗng nếu hụt)."""
    url = f"https://en.openrussian.org/ru/{urllib.parse.quote(word, safe='')}"
    try:
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=20)
        if r.status_code != 200:
            return {}
        soup = BeautifulSoup(r.text, "html.parser")
        tag = soup.find("script", id="__NEXT_DATA__")
        if not tag:
            return {}
        words = json.loads(tag.get_text()).get("props", {}).get("pageProps", {}) \
                    .get("info", {}).get("words", [])
        w = next((x for x in words if x.get("type") == "noun"), None)
        if not w:
            return {}
        noun = w.get("noun") or {}
        return {
            "level": w.get("level") or "",
            "gender": noun.get("gender") or "",
            "plural": ((noun.get("declension") or {}).get("pl") or {}).get("nom") or "",
        }
    except Exception as e:
        log_warn(f"Không cào được level của '{word}': {e}")
        return {}


def enrich_levels(cands, workers=6):
    """Bổ sung level + ĐỐI CHIẾU dạng số nhiều với trang web (dùng cache).

    Dump trên GitHub là ảnh chụp cũ của OpenRussian nên có dòng lệch/hỏng:
    дядя ghi "дядья" (web nay ghi "дяди" — đúng quy tắc), год ghi "лета",
    цех ghi "цеха", воронко ghi sai cả từ gốc. Web là bản mới hơn nên ưu tiên
    web; ứng viên nào hóa ra ĐÚNG quy tắc theo web thì bị loại luôn.
    Trả về (giữ lại, bị loại vì thật ra đúng quy tắc)."""
    cache = _load_cache()
    todo = [c["bare"] for c in cands if c["bare"] not in cache]
    if todo:
        print(f"🌐 Cào level cho {len(todo)} từ còn thiếu (cache đã có {len(cache)})...")
        with ThreadPoolExecutor(max_workers=workers) as pool:
            for word, meta in zip(todo, pool.map(fetch_word_meta, todo)):
                cache[word] = meta or {}
        _save_cache(cache)

    kept, regular = [], []
    for c in cands:
        meta = cache.get(c["bare"]) or {}
        c["level"] = meta.get("level") or ""
        if meta.get("gender"):
            c["gender"] = meta["gender"]
        # Web cào được nhưng KHÔNG có dạng số nhiều -> danh từ không đếm được
        # (сахар = đường). Dump cũ vẫn ghi bừa dạng số nhiều -> phải loại, kẻo
        # tạo thẻ hỏi cái không tồn tại. (meta rỗng = cào lỗi -> giữ, đừng loại.)
        if meta and not (meta.get("plural") or "").strip():
            regular.append(c)
            continue
        web_pl = (meta.get("plural") or "").split(",")[0].strip()
        if web_pl and _bare(web_pl) != c["plural_clean"]:
            c["plural_dump"] = c["plural"]      # giữ dạng cũ để còn soát lại
            c["plural"] = web_pl
            c["plural_clean"] = _bare(web_pl)
            c["kind"] = classify(c["accented"], web_pl, c["gender"])
        if c["plural_clean"] in predict_plurals(c["accented"], "", c["gender"]):
            regular.append(c)
        else:
            kept.append(c)
    return kept, regular


def write_tsv(rows, path=OUT_TSV):
    os.makedirs(DATA_DIR, exist_ok=True)
    cols = ["rank", "bare", "accented", "plural", "plural_clean",
            "gender", "kind", "level", "en"]
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, delimiter="\t", extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    print(f"💾 Đã ghi {len(rows)} dòng -> {path}")


def main():
    if not download_nouns_csv():
        return
    cands, regular = enrich_levels(find_candidates())
    if regular:
        print(f"🧹 Bỏ {len(regular)} từ mà web nói ĐÚNG quy tắc (dump cũ/sai): "
              + ", ".join(f"{c['bare']}→{c['plural']}" for c in regular[:8]))

    for c in cands:
        c["level"] = c["level"] or "?"
    rows = sorted(cands, key=lambda c: c["rank"])
    write_tsv(rows)

    from collections import Counter
    lv = Counter(c["level"] for c in rows)
    print(f"\n📊 Giữ {len(rows)} từ trong TOP_N={TOP_N} từ thông dụng nhất.")
    print("   Theo kiểu:", dict(Counter(c["kind"] for c in rows)))
    print("   Theo level:", dict(lv))
    print(f"   (level chỉ để THAM KHẢO — xem ghi chú ở LEVELS_KEEP, "
          f"{lv['C1'] + lv['C2']} từ bị OpenRussian gắn C1/C2 nhưng vẫn giữ)")


if __name__ == "__main__":
    main()
