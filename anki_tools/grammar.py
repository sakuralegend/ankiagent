# -*- coding: utf-8 -*-
"""Dữ liệu NGỮ PHÁP của từ (thể · sống/không sống · bảng chia) — lấy từ OpenRussian.

Vì sao tách hẳn khỏi `scraper.py`: scraper phục vụ lúc TẠO thẻ (nghĩa + ví dụ +
audio), còn file này phục vụ hai việc mới, chạy theo lô và chạy hàng loạt:

  1. **Badge** — `aspect` (hoàn thành / chưa hoàn thành) cho động từ và `animate`
     (sống / không sống) cho danh từ. Đây là hai thứ user báo là hay nhầm nhất
     mà không field nào đang chứa.
  2. **Bảng chia** — biến cách / chia ngôi ĐẦY ĐỦ, có trọng âm, do MÁY dựng.

🔴 Vì sao máy dựng bảng chứ không phải agent: các dạng từ là dữ liệu TẤT ĐỊNH,
đúng cái mà `lemma.py` đã chốt là "giao cho máy, đừng giao cho AI". Một lô 20 từ
× 12 ô biến cách = 240 dạng có trọng âm — chép tay qua model là 240 cơ hội sai mà
user KHÔNG tự kiểm được (README §1). Ở đây các dạng đi thẳng từ từ điển vào HTML,
không qua model lần nào.

Cache: `data/grammar_cache.json` — mỗi từ cào MỘT lần rồi dùng mãi. Từ điển
OpenRussian là ảnh chụp tĩnh, không có gì phải làm mới định kỳ.
"""
import io
import json
import os
import re
import time
import urllib.parse

from .utils import convert_stress_to_combining_accent, log_fail, log_warn

_HERE = os.path.dirname(os.path.abspath(__file__))
CACHE_PATH = os.path.join(_HERE, "..", "data", "grammar_cache.json")

ACUTE = "́"
VOWELS = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"

# 6 cách. Nhãn phải NGẮN: bảng nằm trong ô rộng 368px trên iPhone, ba cột.
CASES = [("nom", "1 · chủ ngữ"), ("gen", "2 · sở hữu"), ("dat", "3 · tặng"),
         ("acc", "4 · đối"), ("inst", "5 · công cụ"), ("prep", "6 · giới")]
PERSONS = ["я", "ты", "он / она́", "мы", "вы", "они́"]
PASTS = ["он", "она́", "оно́", "они́"]
GIONG_TT = [("m", "он (đực)"), ("f", "она́ (cái)"), ("n", "оно́ (trung)"), ("pl", "они́ (số nhiều)")]


# ---------------------------------------------------------------- chuẩn hoá chữ
def acc(word):
    """Dạng OpenRussian (`сто'л`) -> dấu trọng âm ghép (`стол`).

    Từ MỘT nguyên âm thì BỎ dấu: OpenRussian vẫn đánh dấu (`сто'л`, `го'д`) nhưng
    trên thẻ nó chỉ gây nhiễu — một nguyên âm thì không có chỗ nào khác để nhấn.
    Bộ soát `congcu.py soat` cũng dùng đúng luật này (chỉ đòi dấu khi >= 2 nguyên âm).
    """
    if not word:
        return ""
    out = convert_stress_to_combining_accent(word.strip())
    # Ô có nhiều biến thể: "лю'ди, челове'ки" -> xử lý từng biến thể một
    parts = [p.strip() for p in out.split(",")]
    fixed = []
    for p in parts:
        toks = []
        for t in p.split():
            if len(re.findall(f"[{VOWELS}]", t)) <= 1:
                t = t.replace(ACUTE, "")
            toks.append(t)
        fixed.append(" ".join(toks))
    return ", ".join(x for x in fixed if x)


def bare(word):
    """Bỏ dấu trọng âm, giữ nguyên ё (ё ≠ е — xem congcu.khoa_note)."""
    return (word or "").replace(ACUTE, "").replace("'", "").strip().lower()


def stress_pos(form):
    """Vị trí trọng âm tính theo THỨ TỰ NGUYÊN ÂM (1 = nguyên âm đầu).

    Đếm theo nguyên âm chứ không theo ký tự vì thân từ dài ngắn khác nhau giữa
    các ô; 0 = không xác định được (từ một nguyên âm, hoặc ô có nhiều biến thể).
    """
    form = (form or "").split(",")[0].strip()
    if "ё" in form.lower():
        form = re.sub("ё", "е" + ACUTE, form, count=1, flags=re.I)
    n = 0
    for ch in form:
        if ch in VOWELS:
            n += 1
        elif ch == ACUTE:
            return n
    # Một nguyên âm thì chính nó mang trọng âm — `acc()` đã bỏ dấu cho đỡ rối
    # mắt, nhưng ở đây phải trả lại, nếu không `стол → стола́` (trọng âm chạy từ
    # thân ra đuôi, đúng thứ cần bắt) sẽ lọt vì hai đầu cùng ra 0.
    return 1 if n == 1 else 0


# ------------------------------------------------------------------- cào + cache
def _load_cache():
    if os.path.exists(CACHE_PATH):
        try:
            return json.load(io.open(CACHE_PATH, encoding="utf-8"))
        except ValueError:
            log_warn("grammar_cache.json hỏng -> bắt đầu lại từ rỗng")
    return {}


def _save_cache(cache):
    os.makedirs(os.path.dirname(CACHE_PATH), exist_ok=True)
    io.open(CACHE_PATH, "w", encoding="utf-8").write(
        json.dumps(cache, ensure_ascii=False, indent=0, sort_keys=True))


_CACHE = None


def _cache():
    global _CACHE
    if _CACHE is None:
        _CACHE = _load_cache()
    return _CACHE


def _pick_word_object(info, want_bare):
    """Trang OpenRussian có thể trả NHIỀU mục (từ đồng tự: `мочь` động từ và
    `мочь` danh từ). Ưu tiên mục đúng chính tả và có phần ngữ pháp dày nhất."""
    words = [w for w in (info.get("words") or []) if isinstance(w, dict)]
    if not words:
        return None
    khop = [w for w in words if bare(w.get("bare", "")) == want_bare] or words
    # nhiều mục cùng chính tả -> lấy mục có bảng chia (danh từ `мочь` không có)
    def diem(w):
        return (1 if (w.get("noun") or {}).get("declension") else 0) + \
               (1 if (w.get("verb") or {}).get("presfut") else 0) + \
               (1 if (w.get("adjective") or {}).get("declension") else 0)
    return sorted(khop, key=lambda w: (-diem(w), w.get("rank") or 10 ** 9))[0]


def _family(word_obj):
    """Word family của OpenRussian -> list phẳng. Đây là DỮ LIỆU BIÊN TẬP TAY của
    từ điển, không phải suy đoán từ nguyên — chính thứ đã bắt hụt hai lần khi để
    agent tự nghĩ (`о́блако`↔`во́лос`, `целова́ть`↔`цель`, xem CHANGELOG 28/07)."""
    ra, thay = [], set()
    nhom = [g for g in (word_obj.get("groups") or []) if g.get("groupType") == "family"]
    nguon = [m.get("word") or {} for g in nhom for m in (g.get("groupMembers") or [])]
    nguon += [r.get("word") or {} for r in (word_obj.get("relateds") or [])]
    for w in nguon:
        a = acc(w.get("accented") or "")
        if not a or bare(a) in thay:
            continue
        thay.add(bare(a))
        tls = []
        for t in (w.get("translations") or []):
            tls += t.get("tls") or []
        ra.append({"w": a, "pos": (w.get("type") or "")[:3],
                   "en": ", ".join(tls[:3])})
    return ra


def _adj_declension(adj):
    """Tính từ: OpenRussian trả `declensionBase` + `declensionExt` (chỉ đuôi).
    Ghép lại thành dạng đầy đủ. `declension` có sẵn dạng đầy đủ nhưng KHÔNG phải
    mục nào cũng có -> ghép từ base là đường chắc chắn hơn."""
    day_du = adj.get("declension") or {}
    if day_du:
        return {g: {c: ", ".join(acc(x) for x in (v.get(c) or []))
                    for c, _ in CASES} for g, v in day_du.items()}
    base = adj.get("declensionBase") or ""
    ext = adj.get("declensionExt") or {}
    if not base or not ext:
        return {}
    return {g: {c: ", ".join(acc(base + e) for e in (v.get(c) or []))
                for c, _ in CASES} for g, v in ext.items()}


def normalize(word_obj):
    """`__NEXT_DATA__` -> bản ghi gọn, CHỈ giữ thứ dùng tới (cache nhẹ, đọc được)."""
    pos = word_obj.get("type") or "unknown"
    rec = {"acc": acc(word_obj.get("accented") or word_obj.get("bare") or ""),
           "wc": bare(word_obj.get("bare") or ""),
           "pos": pos, "rank": word_obj.get("rank"),
           "family": _family(word_obj)}

    n = word_obj.get("noun")
    if isinstance(n, dict) and n:
        d = n.get("declension") or {}
        rec["gender"] = n.get("gender")
        rec["animate"] = n.get("animate")
        rec["countable"] = n.get("countable")
        rec["declMode"] = n.get("declensionMode")
        rec["decl"] = {so: {c: acc((d.get(so) or {}).get(c) or "") for c, _ in CASES}
                       for so in ("sg", "pl") if d.get(so)}

    v = word_obj.get("verb")
    if isinstance(v, dict) and v:
        rec["aspect"] = v.get("aspect")
        rec["reflexive"] = bool(v.get("isReflexive"))
        rec["partners"] = [acc(x) for x in (v.get("partners") or []) if x]
        rec["presfut"] = [acc(x) for x in (v.get("presfut") or [])]
        rec["past"] = [acc(x) for x in (v.get("pasts") or [])]
        rec["imper"] = [acc(x) for x in (v.get("imperatives") or [])]
        rec["motion"] = v.get("motionDirectionality")

    a = word_obj.get("adjective")
    if isinstance(a, dict) and a:
        rec["shorts"] = [acc(x) for x in (a.get("shorts") or [])]
        rec["comp"] = [acc(x) for x in (a.get("comparatives") or [])]
        rec["super"] = [acc(x) for x in (a.get("superlatives") or [])]
        rec["adverb"] = acc(a.get("adverb") or "")
        rec["incomparable"] = bool(a.get("incomparable"))
        rec["adjDecl"] = _adj_declension(a)
    return rec


def fetch_grammar(word, refresh=False, delay=0.5):
    """Bản ghi ngữ pháp của một từ ({} nếu không có trên OpenRussian).

    Cache theo `bare(word)`. Từ đã cào MỘT lần thì không gọi mạng nữa — từ điển
    OpenRussian tĩnh, không cần làm mới. `refresh=True` để cào lại.
    Giá trị `{}` cũng được cache (từ không có trang) để khỏi thử lại vô ích.
    """
    key = bare(word)
    cache = _cache()
    if not refresh and key in cache:
        return cache[key]

    import requests
    from bs4 import BeautifulSoup
    url = "https://en.openrussian.org/ru/" + urllib.parse.quote(word.strip(), safe="")
    try:
        res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=25)
        if res.status_code != 200:
            log_fail(f"{word}: HTTP {res.status_code}")
            return {}
        soup = BeautifulSoup(res.text, "html.parser")
        tag = soup.find("script", id="__NEXT_DATA__")
        if not tag:
            log_fail(f"{word}: khong tim thay __NEXT_DATA__")
            return {}
        info = json.loads(tag.get_text(strip=True)).get(
            "props", {}).get("pageProps", {}).get("info", {})
        obj = _pick_word_object(info, key)
        rec = normalize(obj) if obj else {}
    except Exception as e:                      # mạng chập -> KHÔNG cache, thử lại sau
        log_fail(f"{word}: {e}")
        return {}

    cache[key] = rec
    _save_cache(cache)
    if delay:
        time.sleep(delay)
    return rec


def get_cached(word):
    """Chỉ đọc cache, KHÔNG gọi mạng. Dùng ở luồng soạn lô / dựng thẻ hàng loạt."""
    return _cache().get(bare(word)) or {}


# ==============================================================================
# --- BADGE THỂ ĐỘNG TỪ ---
# User chốt 29/07: *"sau quá trình học, giờ tôi bị nhầm lẫn từ khá nhiều do không
# có đủ badge"*. Thể (вид) là thứ KHÔNG field nào đang chứa — badge chỉ nói `v`,
# nên `сказа́ть` và `говори́ть` trông y hệt nhau trên mặt thẻ. README §2c đã phải
# chữa cháy bằng cách viết tay "(HOÀN THÀNH)" vào dòng tiếng Việt của từng động
# từ; có badge rồi thì dòng đề bài được trả lại cho phần NGHĨA.
#
# Chỉ động từ. Badge sống/không sống đã cân nhắc rồi BỎ (user chốt): nó chỉ đổi
# đúng cách 4, nói trong ô Hướng dẫn đúng chỗ thì hơn là chiếm một badge vĩnh viễn.
# ==============================================================================
# Nhãn badge: TIẾNG ANH, VIẾT TẮT, thống nhất với badge từ loại (`n` `v` `adj`)
# vốn đã là tiếng Anh viết tắt. User chốt 29/07: *"tag ngắn gọn đủ hiểu thôi,
# bằng tiếng anh cho thống nhất, viết tắt 3 chữ cũng được"*.
# Nhãn dài ("Chưa hoàn thành") đẩy hàng badge tràn xuống hai dòng trên iPhone và
# hút mắt khỏi chính từ đang học — badge là thứ liếc qua, không phải thứ để đọc.
NHAN_THE = {"perfective": ("pf", "PERF"),
            "imperfective": ("ipf", "IMPF"),
            "both": ("both", "BI-ASP")}

NHAN_PHAN_THAN = "REFL -ся"


def aspect_badge_html(aspect):
    """'perfective' -> HTML badge. Chuỗi rỗng nếu không phải động từ / không rõ."""
    nhan = NHAN_THE.get((aspect or "").strip().lower())
    if not nhan:
        return ""
    ma, chu = nhan
    return f'<div class="badge aspect-{ma}">{chu}</div>'


def reflexive_badge_html(phan_than):
    """Badge ĐỘNG TỪ PHẢN THÂN (đuôi -ся/-сь). Chuỗi rỗng nếu không phải.

    User yêu cầu 29/07 sau khi tự tra `учи́ться` trên OpenRussian. Nó gỡ đúng chỗ
    mơ hồ mà badge thể KHÔNG cứu được: `учи́ть` và `учи́ться` cùng là `v`, cùng
    chưa hoàn thành, nghĩa Việt cùng chứa "học" ⇒ đề bài không có đáp án xác định.
    """
    return f'<div class="badge reflexive">{NHAN_PHAN_THAN}</div>' if phan_than else ""


def suy_giong(rec):
    """Suy GIỐNG từ đuôi biến cách khi từ điển không ghi -> (mã, lý do) / (None, None).

    Cả OpenRussian lẫn `nouns.csv` đều bỏ trống `gender` ở một số danh từ, nhưng
    **bảng biến cách thì vẫn đủ** — mà giống của danh từ Nga được xác định hoàn
    toàn bởi mẫu biến cách. Đây là việc TẤT ĐỊNH, đúng loại nên giao cho máy chứ
    không phải cho AI đoán (cùng lý lẽ với `lemma.py`).

    Ô chẩn đoán tốt nhất là CÁCH 5 số ít, vì nó tách được cả ba giống:
        -ой/-ей/-ою/-ею  giống cái, biến cách I   (да́чкой)
        -ью              giống cái, biến cách III (бы́лью)  ← giống đực mềm là -ем
        -ом/-ем/-ём      đực hay trung, phân biệt bằng đuôi cách 1
        -ым/-им          tính từ danh từ hoá, cũng phân biệt bằng cách 1

    🔴 Trả (None, None) khi KHÔNG chắc. Badge sai tệ hơn badge trống — xem
    `chi_so_nhieu()`: `де́ньги` từng hiện "FEM ♀" và dạy user nói "э́та де́ньга".
    """
    sg = (rec.get("decl") or {}).get("sg") or {}
    nom, inst = bare(sg.get("nom") or ""), bare(sg.get("inst") or "").split(",")[0].strip()
    if not nom or not inst:
        return None, None
    if inst.endswith(("ой", "ей", "ою", "ею", "ёй", "ёю")):
        return "f", f"cách 5 «{sg['inst']}» đuôi -ой/-ей ⇒ giống cái biến cách I"
    if inst.endswith("ью"):
        return "f", f"cách 5 «{sg['inst']}» đuôi -ью ⇒ giống cái biến cách III"
    if inst.endswith(("ом", "ем", "ём", "ым", "им")):
        if nom.endswith(("о", "е", "ё")):
            return "n", f"cách 1 «{sg['nom']}» đuôi -о/-е + cách 5 «{sg['inst']}» ⇒ giống trung"
        if nom.endswith(("а", "я")):
            return None, None                     # `дя́дя`, `мужчи́на` — phải có từ điển
        return "m", f"cách 1 «{sg['nom']}» kết thúc phụ âm/-ь/-й + cách 5 «{sg['inst']}» ⇒ giống đực"
    return None, None


_PL_ONLY = None


def chi_so_nhieu(word):
    """Danh từ CHỈ DÙNG SỐ NHIỀU (pluralia tantum: `де́ньги`, `ша́хматы`, `щи`).

    🔴 OpenRussian ghi `gender` cho chúng theo dạng số ít về mặt LÝ THUYẾT
    (`де́ньги` -> `f`, theo `деньга́` cổ) ⇒ badge hiện "FEM ♀", mà từ này KHÔNG
    có số ít trong tiếng Nga hiện đại. Badge sai kiểu đó tệ hơn không có badge:
    nó dạy user nói "э́та де́ньга". `data/nouns.csv` có cột `pl_only` dứt khoát,
    dùng nó đè lên. Đo trên bộ sưu tập: 4 từ, 2 đang hiện sai.
    """
    global _PL_ONLY
    if _PL_ONLY is None:
        import csv
        _PL_ONLY = set()
        duong = os.path.join(_HERE, "..", "data", "nouns.csv")
        try:
            with io.open(duong, encoding="utf-8", newline="") as fh:
                for r in csv.DictReader(fh, delimiter="\t"):
                    if (r.get("pl_only") or "").strip() == "1":
                        _PL_ONLY.add((r.get("bare") or "").strip().lower().replace("ё", "е"))
        except OSError as e:
            log_warn(f"khong doc duoc nouns.csv ({e}) -> bo qua luat pluralia tantum")
    return bare(word).replace("ё", "е") in _PL_ONLY


def is_reflexive(word, rec=None):
    """Từ này có phải động từ phản thân không.

    Nguồn chính là `verb.isReflexive` của OpenRussian. Đo trên cả 88 động từ
    trong bộ sưu tập: nó khớp **100%** với việc từ có kết thúc bằng `-ся/-сь`
    hay không ⇒ dùng đuôi làm phao cho từ chưa có trong cache là an toàn.
    """
    rec = get_cached(word) if rec is None else rec
    if rec.get("pos") == "verb":
        return bool(rec.get("reflexive"))
    return False


def aspect_of(word):
    """Thể của một từ, đọc từ cache ('' nếu không biết / không phải động từ)."""
    rec = get_cached(word)
    return rec.get("aspect") or "" if rec.get("pos") == "verb" else ""


# ==============================================================================
# --- PHÁT HIỆN BẤT THƯỜNG ---
# User chốt 29/07: bảng chia CHỈ đính kèm khi từ có bất thường, và chỉ đính
# ĐÚNG PHẦN bất thường ("chia ngôi có biến đổi thì vẽ cả bảng chia ngôi; chia
# thì không khác gì thì thôi"). Nên đơn vị quyết định là KHỐI (số ít / số nhiều
# / chia ngôi / quá khứ / dạng ngắn), không phải từng ô.
#
# 🔴 Nguyên tắc: máy KHÔNG ĐƯỢC nói "đều" khi nó không hiểu. Mẫu lạ không khớp
# luật nào -> `khongro`, và `khongro` cũng kéo bảng ra. Đây đúng chỗ README §5
# đã dặn: "chưa kiểm được KHÔNG phải là đúng". Thà thừa một bảng (bảng nằm sau
# nút thu gọn, không tốn diện tích) còn hơn giấu mất một bất thường.
# ==============================================================================

# Đuôi danh từ CHUẨN. Dạng nào bóc ra còn dư thứ khác là mẫu bất thường.
# ⚠️ CỐ Ý không có `ья/ьев/ьям/ьями/ьях` — đó là số nhiều bất quy tắc
# (бра́тья · сту́лья · сыновья́), đúng thứ cần kéo bảng ra.
DUOI_DANH_TU = {
    "", "а", "я", "о", "у", "ю", "ы", "и", "е", "ё", "й", "ь",
    "ой", "ей", "ёй", "ою", "ею", "ёю", "ом", "ем", "ём", "ов", "ев", "ёв", "ью",
    "ам", "ям", "ами", "ями", "ах", "ях",
}

# Cặp đuôi SONG SONG có ở MỌI từ cùng lớp (`кни́гой` ~ `кни́гою` — dạng thứ hai
# là văn viết/thơ). Không phải nét riêng của từ nào ⇒ không tính là bất thường,
# nếu tính thì gần như mọi danh từ giống cái đều bị kêu.
DOI_CHUAN = [{"ой", "ою"}, {"ей", "ею"}, {"ёй", "ёю"}]


def _yo(s):
    return (s or "").replace("ё", "е")


def _than_danh_tu(nom):
    """Thân từ suy từ cách 1 số ít: bỏ nguyên âm/ь/й cuối, phụ âm thì giữ nguyên."""
    n = bare(nom)
    return n[:-1] if n and n[-1] in "аяоеёуюыиьй" else n


def _o_doi_chuan(o, than):
    """Ô kiểu `кни́гой, кни́гою` -> True (biến thể văn phong, bỏ qua)."""
    bt = [x.strip() for x in o.split(",")]
    if len(bt) < 2:
        return False
    duoi = {_yo(bare(x))[len(than):] for x in bt}
    return any(duoi <= cap for cap in DOI_CHUAN)


def _nguyen_am_chay(than, form):
    """Nguyên âm CHẠY — thân từ dài ngắn một nguyên âm giữa các ô.

    Hai chiều đều có thật và đều đáng học:
      · mọc thêm ở cách 2 số nhiều  — `де́вушка → де́вушек`, `окно́ → о́кон`
      · rụng đi ở các cách khác     — `ры́нок → ры́нка`, `лёд → льда`
    """
    f, t = _yo(bare(form)), _yo(than)
    # (a) thân RỤNG một nguyên âm  -> phần còn lại là đầu của dạng kia
    #     `ры́нок`+а -> `ры́нка`, `лёд` -> `льда` (chỗ nguyên âm rụng có thể mọc ь)
    fn, tn = f.replace("ь", ""), t.replace("ь", "")
    for i, ch in enumerate(tn):
        if ch in "оеиа" and fn.startswith(tn[:i] + tn[i + 1:]):
            return True
    # (b) thân MỌC thêm một nguyên âm, đuôi rỗng -> `де́вушка` -> `де́вушек`
    for i in range(1, len(t) + 1):
        for v in "оеё":
            if t[:i] + v + t[i:] == f:
                return True
    return False


def _soi_danh_tu(rec):
    """-> (co, flags, nong)
       co   : {'sg','pl'} khối cần hiện
       flags: [(mã, câu tiếng Việt)] — để in cho người soạn lô đọc
       nong : {(số, cách)} ô lệch, sẽ được tô sáng trong bảng
    """
    d = rec.get("decl") or {}
    o = {(so, c): d[so][c] for so in ("sg", "pl") if d.get(so)
         for c, _ in CASES if (d[so].get(c) or "").strip()} if d else {}
    if not o:
        return set(), [("khongbien", "Không có bảng biến cách trong từ điển.")], set()

    # Bất biến (từ mượn kiểu `метро́`, `кафе́`): mọi ô giống hệt nhau.
    if len({_yo(bare(f)) for f in o.values()}) == 1 and len(o) >= 6:
        return set(), [("batbien", "KHÔNG biến cách — mọi cách viết như nhau.")], set()

    than = _than_danh_tu(rec.get("acc") or "")
    co, flags, nong = set(), [], set()
    la_than, la_duoi, chay = [], [], []
    for (so, c), f in o.items():
        for bt in [x.strip() for x in f.split(",")]:      # ô nhiều biến thể
            b = _yo(bare(bt).split()[-1])                 # "в году́" -> "году"
            if not b.startswith(_yo(than)):
                (chay if _nguyen_am_chay(than, bt) else la_than).append((so, c, bt))
            elif b[len(than):] not in DUOI_DANH_TU:
                la_duoi.append((so, c, bt))

    for nhom, ma, mo_ta in ((la_than, "than", "thân từ ĐỔI"),
                            (la_duoi, "duoi", "đuôi KHÔNG theo mẫu chuẩn"),
                            (chay, "chay", "NGUYÊN ÂM CHẠY")):
        if nhom:
            co.update(so for so, _, _ in nhom)
            nong.update((so, c) for so, c, _ in nhom)
            flags.append((ma, f"{mo_ta}: " + " · ".join(
                f"{'ít' if s == 'sg' else 'nhiều'}/{c} {f}" for s, c, f in nhom[:4])))

    # Trọng âm dịch — thứ user KHÔNG đoán được và cũng không field nào ghi.
    goc = stress_pos(o.get(("sg", "nom")) or o.get(("pl", "nom")) or "")
    for so in ("sg", "pl"):
        vt = {stress_pos(f) for (s, _), f in o.items() if s == so and stress_pos(f)}
        if len(vt) > 1:
            co.add(so)
            flags.append(("trongam", "Trọng âm DỊCH ngay trong "
                                     f"{'số ít' if so == 'sg' else 'số nhiều'}."))
    vt_sg = {stress_pos(f) for (s, _), f in o.items() if s == "sg" and stress_pos(f)}
    vt_pl = {stress_pos(f) for (s, _), f in o.items() if s == "pl" and stress_pos(f)}
    if vt_sg and vt_pl and len(vt_sg) == 1 and len(vt_pl) == 1 and vt_sg != vt_pl:
        co.update(("sg", "pl"))
        flags.append(("trongam", "Trọng âm dịch khi sang số nhiều."))
    if any(ma == "trongam" for ma, _ in flags) and goc:
        nong.update(kc for kc, f in o.items()
                    if stress_pos(f) and stress_pos(f) != goc)

    that = [(s, c, f) for (s, c), f in o.items()
            if "," in f and not _o_doi_chuan(f, than)]
    if that:
        flags.append(("biente", "Ô có nhiều dạng song song: " + " · ".join(
            f"{'ít' if s == 'sg' else 'nhiều'}/{c} {f}" for s, c, f in that[:2])))
        co.update(s for s, _, _ in that)
        nong.update((s, c) for s, c, _ in that)
    return co, flags, nong


# Đuôi động từ ở thì hiện tại/tương lai (bóc ra để so thân từ giữa 6 ngôi)
DUOI_DONG_TU = ["ешь", "ёшь", "ишь", "ете", "ёте", "ите", "ет", "ёт", "ит",
                "ем", "ём", "им", "ут", "ют", "ат", "ят", "у", "ю"]


def _than_dong_tu(form):
    f = bare(form).split(",")[0].strip()
    if f.endswith("ся") or f.endswith("сь"):
        f = f[:-2]
    for e in DUOI_DONG_TU:
        if f.endswith(e) and len(f) - len(e) >= 2:
            return f[: -len(e)]
    return f


def _than_tu_nguyen_the(inf):
    """Các thân hiện tại CHẤP NHẬN ĐƯỢC suy thẳng từ nguyên thể (lớp có quy tắc).
    Không nằm trong tập này = phải nhìn bảng mới biết chia thế nào."""
    i = bare(inf)
    if i.endswith(("ся", "сь")):
        i = i[:-2]
    ra = set()
    for duoi in ("ть", "ать", "ять", "еть", "ить", "уть", "ыть", "оть"):
        if i.endswith(duoi):
            ra.add(_yo(i[: -len(duoi)]))
    if i.endswith(("овать", "евать")):          # рисова́ть -> рису́ю (lớp năng sản)
        ra.add(_yo(i[:-5] + "у"))
        ra.add(_yo(i[:-5] + "ю"))
    return {x for x in ra if x}


def _soi_dong_tu(rec):
    co, flags, nong = set(), [], set()
    pf = [f for f in (rec.get("presfut") or []) if f]
    inf = rec.get("acc") or ""
    if len(pf) >= 6:
        than = [_yo(_than_dong_tu(f)) for f in pf]
        chuan = than[1]                       # ngôi `ты` là dạng gốc của lớp chia
        if {t for t in than if t != chuan}:
            co.add("presfut")
            nong.update(("presfut", i) for i, t in enumerate(than) if t != chuan)
            flags.append(("bienam", "Thân từ BIẾN ÂM giữa các ngôi: "
                          + " / ".join(f"{PERSONS[i]} {pf[i]}"
                                       for i, t in enumerate(than) if t != chuan)))
        hop_le = _than_tu_nguyen_the(inf)
        if hop_le and chuan not in hop_le:
            co.add("presfut")
            flags.append(("lopla", f"Thân hiện tại ({pf[1]}) KHÔNG suy được thẳng "
                                   f"từ nguyên thể — phải nhớ riêng."))
        vt = [stress_pos(f) for f in pf]
        if len({v for v in vt if v}) > 1:
            co.add("presfut")
            nong.update(("presfut", i) for i, v in enumerate(vt) if v and v != vt[1])
            flags.append(("trongam", "Trọng âm DỊCH giữa các ngôi."))
    elif pf:
        co.add("presfut")
        flags.append(("thieu", "Bảng chia ngôi không đủ 6 dạng."))

    qk = [f for f in (rec.get("past") or []) if f]
    if len(qk) >= 4:
        goc = bare(inf)
        goc = goc[:-2] if goc.endswith("ть") else None
        if goc and not all(_yo(bare(p)).startswith(_yo(goc)) for p in qk):
            co.add("past")
            nong.update(("past", i) for i, p in enumerate(qk)
                        if not _yo(bare(p)).startswith(_yo(goc)))
            flags.append(("qkla", f"Quá khứ KHÔNG phải nguyên thể bỏ -ть + -л: "
                                  f"{qk[0]} / {qk[1]}"))
        vt = [stress_pos(f) for f in qk]
        if len({v for v in vt if v}) > 1:
            co.add("past")
            nong.update(("past", i) for i, v in enumerate(vt) if v and v != vt[0])
            flags.append(("trongam", "Trọng âm dịch trong quá khứ."))
    return co, flags, nong


def _soi_tinh_tu(rec):
    co, flags, nong = set(), [], set()
    # ⚠️ KHÔNG lọc ô rỗng: `весе́нний` thiếu dạng ngắn giống đực (`['', 'весе́ння',
    # …]`). Lọc thì chỉ số trong `nong` lệch khỏi chỉ số lúc dựng bảng, và ô tô
    # sáng nhảy sang hàng khác — sai mà nhìn vẫn thấy "có vẻ đúng".
    ngan = rec.get("shorts") or []
    co_chu = [i for i, f in enumerate(ngan) if f]
    than = _yo(bare(rec.get("acc") or ""))[:-2]      # bỏ -ый/-ий/-ой
    if co_chu:
        vt = {i: stress_pos(ngan[i]) for i in co_chu}
        goc = vt[co_chu[0]]
        gan_them = [i for i in co_chu
                    if not _yo(bare(ngan[i].split(",")[0])).startswith(than)]
        if len({v for v in vt.values() if v}) > 1 or gan_them:
            co.add("shorts")
            nong.update(("shorts", i) for i in co_chu
                        if i in gan_them or (vt[i] and vt[i] != goc))
            flags.append(("dangngan", "DẠNG NGẮN có biến đổi (trọng âm dịch / thêm "
                                      "nguyên âm) — không suy thẳng từ dạng dài: "
                          + " · ".join(ngan[i] for i in co_chu[:4])))
    # So sánh hơn: `-ее` gắn thẳng vào thân là đều (`но́вый → нове́е`) nên bỏ qua.
    # Chỉ nói khi thân ĐỔI — hoặc biến âm (`высо́кий → вы́ше`, к→ш) hoặc thay hẳn
    # bằng từ khác gốc (`хоро́ший → лу́чше`). Hai loại này phải phân biệt: gọi
    # `вы́ше` là "khác hẳn" thì user mất luôn cái luật biến âm đang có ở đó.
    ss = [f for f in (rec.get("comp") or []) if f]
    if ss and len(than) >= 3 and not any(_yo(bare(f)).startswith(than[:3]) for f in ss):
        cung_goc = any(_yo(bare(f)).startswith(than[:2]) for f in ss)
        co.add("comp")
        nong.add(("comp", 0))
        flags.append(("sscat" if cung_goc else "ssla",
                      ("So sánh hơn BIẾN ÂM ở thân: " if cung_goc
                       else "So sánh hơn là từ KHÁC HẲN: ") + " · ".join(ss[:2])))
    return co, flags, nong


def analyze(rec):
    """Soi một bản ghi -> {'khoi', 'flags', 'nong', 'pos'}.

    `flags` là câu tiếng Việt NGẮN để in cho người soạn lô đọc (`congcu.py tiep`),
    KHÔNG phải nội dung đưa thẳng lên thẻ — người soạn quyết định nói gì cho gọn.
    `nong` là các ô sẽ được tô sáng trong bảng máy dựng.
    """
    if not rec:
        return {"khoi": set(), "flags": [], "nong": set(), "pos": None}
    soi = {"noun": _soi_danh_tu, "verb": _soi_dong_tu,
           "adjective": _soi_tinh_tu}.get(rec.get("pos"))
    khoi, flags, nong = soi(rec) if soi else (set(), [], set())
    return {"khoi": khoi, "flags": flags, "nong": nong, "pos": rec.get("pos")}


# ==============================================================================
# --- DỰNG BẢNG HTML ---
# Bảng nằm TRONG ô Hướng dẫn, bọc trong <details> lồng: mặc định gấp lại nên
# KHÔNG tốn một pixel nào của trần "vừa một màn hình iPhone" (README §2). Phần
# chú ý cô đọng vẫn nằm ở trên, bảng chỉ để user bấm vào nghiên cứu thêm.
#
# 🔴 KHÔNG dùng <b> cho dạng từ trong bảng. `congcu.py soat` và `kiemtra.py` đối
# chiếu MỌI từ Nga in <b> với nouns.csv (từ điển chỉ chứa dạng NGUYÊN THỂ) — các
# dạng đã chia sẽ bị kêu oan hàng loạt, mà một bộ soát kêu oan mãi thì rồi chính
# mình sẽ bỏ qua cả tiếng kêu thật.
# ==============================================================================

def thieu_dau(form):
    """Ô từ điển QUÊN đánh trọng âm (>=2 nguyên âm mà không có dấu, không có ё).

    Đo trên cả kho: 4/5 900 ô, đúng một từ (`ва́ренный`). Hiếm, nhưng im lặng thì
    user học thuộc trọng âm sai — mà user KHÔNG tự kiểm được (README §1). Nên ô
    đó phải tự nói ra là nó không chắc.
    """
    t = (form or "").split(",")[0].strip()
    return (len([c for c in t if c in VOWELS]) >= 2
            and ACUTE not in t and "ё" not in t.lower())


def _o(text, nong=False):
    lop = "gt-v" + (" gt-nong" if nong else "")
    if text and thieu_dau(text):
        return f'<td class="{lop}">{text}<span class="gt-ngo">?</span></td>'
    return f'<td class="{lop}">{text or "—"}</td>'


def _bang_danh_tu(rec, khoi, nong):
    d = rec.get("decl") or {}
    cot = [so for so in ("sg", "pl") if d.get(so)]
    if not cot:
        return ""
    dau = "".join(f'<td class="gt-h">{"số ít" if s == "sg" else "số nhiều"}</td>'
                  for s in cot)
    rows = [f'<tr><td class="gt-h"></td>{dau}</tr>']
    for c, nhan in CASES:
        o = "".join(_o(d[s].get(c), (s, c) in nong) for s in cot)
        rows.append(f'<tr><td class="gt-k">{nhan}</td>{o}</tr>')
    return ('<div class="gt-ten">Biến cách</div>'
            f'<table class="gt-tbl">{"".join(rows)}</table>')


def _bang_dong_tu(rec, khoi, nong):
    ra = ""
    pf = rec.get("presfut") or []
    if "presfut" in khoi and len(pf) >= 6:
        ten = "Tương lai đơn" if rec.get("aspect") == "perfective" else "Hiện tại"
        rows = "".join(f'<tr><td class="gt-k">{PERSONS[i]}</td>'
                       f'{_o(pf[i], ("presfut", i) in nong)}</tr>' for i in range(6))
        ra += (f'<div class="gt-ten">Chia ngôi — {ten}</div>'
               f'<table class="gt-tbl">{rows}</table>')
    qk = rec.get("past") or []
    if "past" in khoi and len(qk) >= 4:
        rows = "".join(f'<tr><td class="gt-k">{PASTS[i]}</td>'
                       f'{_o(qk[i], ("past", i) in nong)}</tr>' for i in range(4))
        ra += ('<div class="gt-ten">Quá khứ</div>'
               f'<table class="gt-tbl">{rows}</table>')
    im = rec.get("imper") or []
    if ra and im:
        ra += f'<div class="gt-phu">Mệnh lệnh: {" · ".join(im[:2])}</div>'
    return ra


def _bang_tinh_tu(rec, khoi, nong):
    ra = ""
    ngan = rec.get("shorts") or []
    if "shorts" in khoi and ngan:
        rows = "".join(f'<tr><td class="gt-k">{GIONG_TT[i][1]}</td>'
                       f'{_o(ngan[i], ("shorts", i) in nong)}</tr>'
                       for i in range(min(4, len(ngan))))
        ra += ('<div class="gt-ten">Dạng ngắn</div>'
               f'<table class="gt-tbl">{rows}</table>')
    if "comp" in khoi and rec.get("comp"):
        ra += ('<div class="gt-ten">So sánh</div><div class="gt-phu">hơn: '
               f'<span class="gt-nong">{" · ".join(rec["comp"][:2])}</span>'
               + (f' · nhất: {" · ".join(rec["super"][:2])}' if rec.get("super") else "")
               + "</div>")
    return ra


def build_table(rec, phan_tich=None):
    """HTML bảng chia (chuỗi rỗng nếu từ này không có gì bất thường).

    Chỉ dựng ĐÚNG KHỐI có bất thường — user chốt: "chia ngôi có biến đổi thì vẽ
    cả bảng chia ngôi; những cái khác không khác biệt thì thôi".
    """
    if not rec:
        return ""
    a = phan_tich or analyze(rec)
    khoi, nong = a["khoi"], a["nong"]
    if not khoi:
        return ""
    than = {"noun": _bang_danh_tu, "verb": _bang_dong_tu,
            "adjective": _bang_tinh_tu}.get(rec.get("pos"))
    ruot = than(rec, khoi, nong) if than else ""
    if not ruot.strip():
        return ""
    ngo = ('<div class="gt-nguon">⚠️ Ô có dấu <b>?</b>: từ điển KHÔNG ghi trọng âm '
           '— chưa kiểm được, đừng học thuộc chỗ nhấn ở đó.</div>'
           if '<span class="gt-ngo">' in ruot else "")
    return ('<details class="gt-bang"><summary class="gt-sum">'
            '📋 Bảng chia đầy đủ — bấm để xem</summary>'
            f'<div class="gt-body">{ruot}{ngo}'
            '<div class="gt-nguon">Dạng &amp; trọng âm lấy thẳng từ OpenRussian '
            '(máy dựng, không qua AI). Ô sáng = chỗ biến đổi.</div>'
            '</div></details>')
