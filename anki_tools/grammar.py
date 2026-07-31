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
import sys
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
    # 🔴 `ё` LUÔN mang trọng âm sẵn, nên `ё` + dấu là SAI CHÍNH TẢ, không phải một
    # cách viết. Nguồn vẫn ghi thế ở vài từ (`шофё́р` 12 ô, `зачё́там`, `неё́`).
    # Vá ở ĐÂY chứ không vá file cache: 30/07 tôi sửa thẳng `grammar_cache.json`
    # rồi `--nangcap` cào lại là dấu thừa quay về đủ 15 chỗ, và một thẻ đã nạp
    # bản sai. Sửa dữ liệu thì lần cào sau mất; sửa phép biến đổi thì vĩnh viễn.
    out = out.replace("ё" + ACUTE, "ё").replace("Ё" + ACUTE, "Ё")
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


# 🔴 KHÔNG BÓC WORD FAMILY — đã có `_family()` ở đây, gỡ hẳn 29/07 (v3).
#
# Trang OpenRussian có sẵn hai khoá họ từ và ĐỪNG đọc lại chúng một cách ngây thơ:
#   · `groups[groupType="family"]` -> `groupMembers[].word`  = **cùng gốc**
#   · `relateds[].word`                                      = **nghĩa gần, KHÁC GỐC HẲN**
# `_family()` cũ gộp cả hai vào một rổ, nên `ги́бкий` kéo theo `мя́гкий`/`бога́тый`
# và `о́блако` kéo theo `ту́ча`/`не́бо`. Danh sách đó vào ô "Họ hàng" là thẻ dạy sai
# từ nguyên — đúng loại lỗi 28/07 (`о́блако`↔`во́лос`, `целова́ть`↔`цель`).
#
# Đã đo trước khi bỏ: dùng nó làm CỬA SOÁT thì kêu oan 65% (2 069 cụm / 301 thẻ),
# và `цель`/`во́лос` không có họ từ nào nên cửa cũng chỉ bắt được 1 trong 2 lỗi.
# User chốt: *"không lấy family word từ openrussian nữa"*.
#
# ⇒ Mục "Họ hàng" do agent tự nghĩ, README §2 dặn "không chắc thì bỏ mục đó".
# Muốn khôi phục thì phải bóc RIÊNG `groups` (bỏ `relateds`), tăng `BAN_GHI_V`
# và cào lại — không phải khôi phục hàm cũ. Xem [[ho-tu-openrussian-da-bac]].


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


def _decl_dai_tu(pr):
    """Đại từ: `pronoun.declension` = {giống: {cách: [dạng]}}, ô rỗng thì bỏ.

    `он` chỉ có cột `m` (vì `она́`/`они́` là mục từ riêng), `мой` có đủ bốn cột.
    """
    d = pr.get("declension") or {}
    ra = {}
    for g, v in d.items():
        cot = {c: ", ".join(acc(x) for x in (v.get(c) or []) if x) for c, _ in CASES}
        if any(cot.values()):
            ra[g] = cot
    return ra


def _decl_tu_forms(forms):
    """Số từ: mảng `forms` phẳng -> {cột: {cách: dạng}}.

    Số từ Nga KHÔNG nằm ở `noun.declension` như danh từ mà ở mảng này, và mảng
    này có tới BA dạng — bỏ sót dạng nào là mất trắng cả nhóm từ đó:

      `ru_noun_sg_gen`  số từ đếm biến cách như danh từ  (`пять`→`пяти́`, `три`→`трёх`)
      `ru_adj_m_gen`    số từ THỨ TỰ, biến cách như tính từ (`пе́рвый`→`пе́рвого`)
      `ru_base`         CHỈ có dạng gốc, KHÔNG có bảng     (`со́рок`, `де́вять`, `сто`)

    ⚠️ Nhóm `ru_base` là lỗ hổng THẬT của từ điển, không phải lỗi đọc: `со́рок`
    có biến cách trong tiếng Nga (`сорока́`) nhưng OpenRussian không lưu. Trả
    rỗng để chỗ khác biết là KHÔNG CÓ DỮ LIỆU, đừng dựng bảng nửa vời.
    """
    ra = {}
    for f in forms or []:
        loai = f.get("formType") or ""
        dang = (f.get("form") or "").strip()
        if not dang:
            continue
        m = re.fullmatch(r"ru_noun_(sg|pl)_(nom|gen|dat|acc|inst|prep)", loai)
        if m:
            ra.setdefault(m.group(1), {})[m.group(2)] = acc(dang)
            continue
        m = re.fullmatch(r"ru_adj_(m|f|n|pl)_(nom|gen|dat|acc|inst|prep)", loai)
        if m:
            ra.setdefault(m.group(1), {})[m.group(2)] = acc(dang)
    return ra


# Số hiệu bản ghi. TĂNG khi `normalize()` bắt đầu giữ thêm/bớt khoá — nhờ nó
# `cao_nguphap.py --nangcap` biết bản ghi nào cũ mà cào lại, không phải đoán qua
# việc "thiếu khoá X" (khoá có thể vắng một cách chính đáng: `сожале́ние` không
# có `usage` thật, chứ không phải chưa cào).
#   v1 (29/07) bản đầu · v2 (29/07) thêm `usage` + `idioms` · v3 (29/07) BỎ `family`
#   v4 (30/07) thêm `present` · `future` · `parts` — user chốt: bảng trên thẻ phải có
#              ĐỦ mọi thứ OpenRussian hiện ở khối bảng (Present/Future · Participles
#              gồm cả Gerund). KHÔNG lấy `usage2`/`aspectPartner` (user chốt bỏ).
#
# ⚠️ v3 là lần BỚT khoá đầu tiên, và bớt thì KHÔNG cần cào lại mạng — dữ liệu mới
# là tập con của dữ liệu cũ. `xoa_family_khoi_cache.py` gỡ khoá ngay trên file
# cache rồi đặt `v=3`, chạy trong vài giây. Chỉ lần THÊM khoá mới phải `--nangcap`.
BAN_GHI_V = 4


def ban_ghi_cu(rec):
    """Bản ghi cào theo `normalize()` ĐỜI CŨ, thiếu khoá mà đời nay có.

    🔴 MỘT chỗ duy nhất định nghĩa "cũ", vì trước 30/07 việc này bị rải ba nơi
    (`fetch_grammar` trả cache bất kể phiên bản · `get_cached` im lặng ·
    `cao_nguphap --nangcap` tự dò riêng) ⇒ tăng `BAN_GHI_V` mà quên một nơi là
    thẻ nhận bảng thiếu mục, không ai báo.

    ⚠️ Bản ghi RỖNG `{}` không phải cũ — đó là "từ này OpenRussian không có",
    cache lại cố ý để khỏi thử lại vô ích. Coi nó là cũ thì mỗi lần đọc lại gọi
    mạng một lần cho một từ vĩnh viễn không có trang.
    """
    return bool(rec) and (rec.get("v") or 0) < BAN_GHI_V


def _idioms(word_obj):
    """`expressions` -> [{w, en}] — thành ngữ / cụm cố định chứa từ này.

    Đây đúng loại nội dung ô Hướng dẫn cần: bản mẫu `сожале́ние` mà user chấm là
    "vừa súc tích vừa đủ ý" có một trong hai ô đỏ chính là **cụm phải thuộc**
    `к сожале́нию`. Từ điển có sẵn mà trước 29/07 mình vứt đi.
    """
    ra = []
    for it in (word_obj.get("expressions") or []):
        if not isinstance(it, dict):
            continue
        a = acc(it.get("accented") or it.get("bare") or "")
        tls = [t for tr in (it.get("translations") or []) for t in (tr.get("tls") or [])]
        if a:
            ra.append({"w": a, "en": ", ".join(tls[:3])})
    return ra


# Sáu ô của khối "Participles" trên OpenRussian, giữ ĐÚNG thứ tự trang hiện —
# hai ô cuối là Gerund (trạng động từ), trang gộp chung khối nên ta cũng gộp.
PHAN_TU_KHOA = ("activePresent", "activePast", "passivePresent", "passivePast",
                "gerundPresent", "gerundPast")


def _dang(x):
    """Một ô dạng từ. Gạch `-` của từ điển = KHÔNG CÓ, phải về rỗng.

    Thể hoàn thành có `present = ["-","-","-","-","-","-"]` (gạch giả, không phải
    thiếu dữ liệu). Để nguyên thì bảng in ra sáu ô gạch, nhìn như lỗi.
    """
    s = acc(x or "").strip()
    return "" if s in ("-", "—", "–") else s


def _boc_phan_tu(pp):
    """`verb.participles` -> {ô: [{'f': dạng, 'en': nghĩa}]}, bỏ ô rỗng.

    Gerund chỉ có `accented`, không có `translations` — nên `en` vắng là bình
    thường, đừng coi là hụt dữ liệu.
    """
    if not isinstance(pp, dict):
        return {}
    ra = {}
    for k in PHAN_TU_KHOA:
        ds = []
        for x in (pp.get(k) or []):
            if not isinstance(x, dict):
                continue
            f = _dang(x.get("accented"))
            if not f:
                continue
            en = ""
            for t in (x.get("translations") or []):
                tls = [s for s in (t.get("tls") or []) if (s or "").strip()]
                if tls:
                    en = tls[0].strip()
                    break
            ds.append({"f": f, "en": en} if en else {"f": f})
        if ds:
            ra[k] = ds
    return ra


def normalize(word_obj):
    """`__NEXT_DATA__` -> bản ghi gọn, CHỈ giữ thứ dùng tới (cache nhẹ, đọc được).

    🔴 Đây là TẦNG 2 — nơi quyết định GIỮ GÌ. Tầng 1 (`fetch_page`) lấy đủ.
    Cố ý KHÔNG giữ: `collocations` (6,8 KB/từ — user đã có `RawExamples` 10 ví dụ
    rồi, chồng lấn) · `sentences` (đã dùng ở luồng tạo thẻ, không cần lưu lại) ·
    `contributions` · `externalLinks`.
    """
    pos = word_obj.get("type") or "unknown"
    rec = {"v": BAN_GHI_V,
           "acc": acc(word_obj.get("accented") or word_obj.get("bare") or ""),
           "wc": bare(word_obj.get("bare") or ""),
           "pos": pos, "rank": word_obj.get("rank")}
    # KHÔNG có `family` ở đây — cố ý, xem khối comment chỗ `_adj_declension`.
    # Ghi chú CÁCH DÙNG do người biên tập viết (`по слова́м:` + cách 2). Ngắn,
    # đắt, và không suy ra được từ bảng chia.
    if (word_obj.get("usage") or "").strip():
        rec["usage"] = word_obj["usage"].strip()
    idi = _idioms(word_obj)
    if idi:
        rec["idioms"] = idi

    # ĐẠI TỪ + SỐ TỪ — hai nhóm này KHÔNG dùng `noun`/`verb`/`adjective`.
    # Bỏ sót thì 80 từ (22 đại từ + 58 số từ) ra rỗng, mà đó lại đúng là nhóm
    # biến cách bất quy tắc nhất (`он → его́ → ему́`, `три → трёх → тремя́`).
    pr = word_obj.get("pronoun")
    if isinstance(pr, dict) and pr:
        rec["proDecl"] = _decl_dai_tu(pr)
        if pr.get("declensionInfo"):
            # câu chú giải NGƯỜI THẬT viết ("The forms with н- are used if after
            # a preposition") — quý hơn mọi thứ suy ra được, giữ nguyên văn.
            rec["declInfo"] = pr["declensionInfo"]
    if word_obj.get("forms"):
        numDecl = _decl_tu_forms(word_obj["forms"])
        if numDecl:
            rec["numDecl"] = numDecl

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
        # HAI CỘT Present/Future y như OpenRussian hiện. `presfut` giữ nguyên vì
        # `analyze()` neo chỉ số `nong` vào nó — đừng thay, chỉ thêm.
        #   · thể CHƯA hoàn thành: present = dạng thật, future = `бу́ду` + nguyên thể
        #   · thể HOÀN THÀNH: present = ["-","-",…] (gạch giả), future = dạng thật
        # ⇒ phải quy gạch "-" về rỗng, nếu không bảng in ra sáu ô gạch.
        rec["present"] = [_dang(x) for x in (v.get("present") or [])]
        rec["future"] = [_dang(x) for x in (v.get("future") or [])]
        parts = _boc_phan_tu(v.get("participles"))
        if parts:
            rec["parts"] = parts

    a = word_obj.get("adjective")
    if isinstance(a, dict) and a:
        rec["shorts"] = [acc(x) for x in (a.get("shorts") or [])]
        rec["comp"] = [acc(x) for x in (a.get("comparatives") or [])]
        rec["super"] = [acc(x) for x in (a.get("superlatives") or [])]
        rec["adverb"] = acc(a.get("adverb") or "")
        rec["incomparable"] = bool(a.get("incomparable"))
        rec["adjDecl"] = _adj_declension(a)
    return rec


# ==============================================================================
# --- TẦNG 1: CÀO ---
# 🔴 NƠI DUY NHẤT trong toàn dự án gọi mạng tới OpenRussian và biết đường dẫn
# JSON `props.pageProps.info`. Trả về NGUYÊN `info`, KHÔNG cắt, KHÔNG chọn sẵn.
#
# Vì sao không chọn sẵn: mỗi mảng cần một mục khác nhau. Mảng từ vựng cần mục
# hợp chính tả nhất; mảng thẻ ngữ pháp (`grammar_forms`) BẮT BUỘC phải là danh
# từ (thẻ số nhiều chỉ có nghĩa với danh từ). Chọn sẵn ở tầng này là ép cả hai
# theo một luật, mà luật nào cũng sai với một trong hai bên.
#
# Và không cắt: `normalize()` bỏ đi `collocations` (6,8 KB), `sentences`,
# `expressions`, `usage`… — đều là dữ liệu người biên tập, có thể mảng khác cần.
# Cắt ở tầng 1 thì mảng đó phải cào lại lần nữa. Tầng 1 lấy đủ, TẦNG 2 quyết
# định giữ gì.
# ==============================================================================

# Bộ nhớ tạm TRONG MỘT LẦN CHẠY. Trong cùng một luồng tạo thẻ, `scraper.py` và
# `grammar.py` cùng cần một từ -> không tải hai lần. CÓ CHẶN SỐ LƯỢNG: mỗi trang
# vài chục KB, cào cả kho 950 từ mà giữ hết là ngốn vô ích. Không ghi ra đĩa —
# cache lâu dài là `grammar_cache.json` (bản đã gọn), không phải trang thô.
_PAGE_MEMO = {}
_PAGE_MEMO_TRAN = 16


def fetch_page(word, timeout=25, memo=True):
    """Trang OpenRussian -> NGUYÊN `info` ({} nếu hụt). Đây là TẦNG 1."""
    key = bare(word)
    if memo and key in _PAGE_MEMO:
        return _PAGE_MEMO[key]
    import requests
    from bs4 import BeautifulSoup
    url = "https://en.openrussian.org/ru/" + urllib.parse.quote(word.strip(), safe="")
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=timeout)
    if res.status_code != 200:
        log_fail(f"{word}: HTTP {res.status_code}")
        return {}
    tag = BeautifulSoup(res.text, "html.parser").find("script", id="__NEXT_DATA__")
    if not tag:
        log_fail(f"{word}: khong tim thay __NEXT_DATA__ (trang doi cau truc?)")
        return {}
    info = json.loads(tag.get_text(strip=True)).get(
        "props", {}).get("pageProps", {}).get("info", {})
    if memo:
        if len(_PAGE_MEMO) >= _PAGE_MEMO_TRAN:
            _PAGE_MEMO.pop(next(iter(_PAGE_MEMO)))
        _PAGE_MEMO[key] = info
    return info


def cac_muc_dong_tu(info, word):
    """Mọi mục ĐÚNG CHÍNH TẢ với `word` -> list (rỗng nếu không có mục nào).

    ≥2 mục nghĩa là từ ĐỒNG TỰ: `мочь` (động từ *có thể* / danh từ *sức lực*),
    `стать` (*trở nên* / *dáng vẻ*), `печь` (*nướng* / *cái lò*), `есть` (*có* /
    *ăn*). Máy KHÔNG có cách nào biết user định học nghĩa nào — user chốt 29/07:
    *"nếu tìm ra nhiều từ đồng chính tả, cho tôi chọn"*.
    """
    want = bare(word)
    return [w for w in ((info or {}).get("words") or [])
            if isinstance(w, dict) and bare(w.get("bare") or "") == want]


def tom_tat_muc(w):
    """Một dòng mô tả mục từ, để in ra cho user chọn."""
    tls = [t for tr in (w.get("translations") or []) for t in (tr.get("tls") or [])]
    return {"id": w.get("id"), "pos": w.get("type") or "?",
            "acc": acc(w.get("accented") or w.get("bare") or ""),
            "en": ", ".join(tls[:4]) or "(không có nghĩa)"}


def fetch_word_object(word, timeout=25, chon_id=None):
    """TẦNG 2 của mảng TỪ VỰNG: cào rồi chọn mục hợp với thẻ `RU_Word`.

    `chon_id` = `id` mục user đã chọn (khi từ đồng tự). Không truyền thì áp luật
    tự động (`_pick_word_object`: hợp chính tả, ưu tiên mục có bảng chia).

    `grammar_forms` KHÔNG dùng hàm này — nó gọi thẳng `fetch_page()` rồi áp luật
    chọn riêng (ép `type == "noun"`).
    """
    info = fetch_page(word, timeout=timeout)
    if chon_id is not None:
        muc = next((w for w in cac_muc_dong_tu(info, word)
                    if w.get("id") == chon_id), None)
        if muc:
            return muc
        log_warn(f"{word}: khong con muc id={chon_id} -> quay ve luat tu dong")
    return _pick_word_object(info, bare(word))


def fetch_grammar(word, refresh=False, delay=0.5):
    """Bản ghi ngữ pháp của một từ ({} nếu không có trên OpenRussian).

    Cache theo `bare(word)`. Từ đã cào MỘT lần thì không gọi mạng nữa — từ điển
    OpenRussian tĩnh, không cần làm mới. `refresh=True` để cào lại.
    Giá trị `{}` cũng được cache (từ không có trang) để khỏi thử lại vô ích.
    """
    key = bare(word)
    cache = _cache()
    if not refresh and key in cache and not ban_ghi_cu(cache[key]):
        return cache[key]
    try:
        obj = fetch_word_object(word)
        rec = bo_sung(normalize(obj), word) if obj else {}
    except Exception as e:                      # mạng chập -> KHÔNG cache, thử lại sau
        log_fail(f"{word}: {e}")
        return {}

    cache[key] = rec
    _save_cache(cache)
    if delay:
        time.sleep(delay)
    return rec


_DA_KEU = set()


def get_cached(word):
    """Chỉ đọc cache, KHÔNG gọi mạng. Dùng ở luồng soạn lô / dựng thẻ hàng loạt.

    🔴 KÊU khi bản ghi cũ phiên bản. Hàm này không được gọi mạng (luồng hàng loạt
    950 từ), nên nó KHÔNG tự chữa được — mà im lặng thì thẻ nhận bảng thiếu mục
    đúng lúc `nap` tưởng mình vừa ghi bản mới nhất. Đã dính thật 30/07: thêm
    `present`/`future`/`parts` vào `normalize()` mà cache còn v3, mọi đường đọc
    cache vẫn dựng bảng cũ không một tiếng nào.
    Kêu MỘT lần mỗi từ — 950 dòng giống nhau thì rồi chính mình sẽ bỏ qua.
    """
    rec = _cache().get(bare(word)) or {}
    if ban_ghi_cu(rec) and bare(word) not in _DA_KEU:
        _DA_KEU.add(bare(word))
        print(f"[grammar] '{word}': ban ghi v{rec.get('v', 0)} < v{BAN_GHI_V} "
              f"-> bang chia THIEU muc moi. Chay: python "
              f"data/huongdan/kho/cao_nguphap.py --nangcap", file=sys.stderr)
    return rec


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

# CHỈ "REF", KHÔNG in kèm đuôi `-ся`. User chốt 29/07: *"bạn không cần ghi đuôi
# đâu, cái đó tôi phải nhớ"* — badge nằm ở mặt ĐỀ BÀI, mà đề bài thì in sẵn đuôi
# tức là cho sẵn một phần đáp án user đang phải gõ.
NHAN_PHAN_THAN = "REF"


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


# 🔴 NGUỒN CHÂN LÝ DUY NHẤT của nhãn giống. Trước đây bảng này có ở hai nơi
# (anki_client.build_card_fields cho thẻ MỚI, scripts/backfill_badge.py cho thẻ CŨ) —
# hai nơi thì sớm muộn lệch nhau, và lệch ở đây nghĩa là thẻ mới với thẻ cũ hiện
# hai kiểu badge khác nhau cho cùng một giống.
NHAN_GIONG = {"masculine": "MASC ♂", "feminine": "FEM ♀", "neuter": "NEUT ⚧",
              "plural": "PL 👥", "common": "M/F ⚥"}
MA_GIONG = {"m": "masculine", "f": "feminine", "n": "neuter", "pl": "plural",
            "both": "common", "common": "common",
            # chấp nhận cả tên đầy đủ vì scraper.py trả về "Masculine"/"Feminine"
            "masculine": "masculine", "feminine": "feminine",
            "neuter": "neuter", "plural": "plural"}


def gender_badge_html(word, ma_giong=None, rec=None):
    """Badge giống cho MỘT danh từ. Ba tầng theo độ tin cậy giảm dần:

      1. luật CHỈ DÙNG SỐ NHIỀU (`nouns.csv pl_only`) — đè lên tất cả, vì
         `де́ньги` không có số ít nên `FEM ♀` của từ điển là dạy sai;
      2. mã giống từ điển đưa (`m`/`f`/`n`/`pl`/`both`);
      3. SUY từ đuôi biến cách (`suy_giong`) khi từ điển bỏ trống.

    Trả "" khi không chắc — badge sai tệ hơn badge trống.
    """
    if chi_so_nhieu(word):
        return f'<div class="badge plural">{NHAN_GIONG["plural"]}</div>'
    rec = get_cached(word) if rec is None else rec
    lop = MA_GIONG.get(str(ma_giong or rec.get("gender") or "").strip().lower())
    if not lop:
        ma, _ = suy_giong(rec)
        lop = MA_GIONG.get(ma or "")
    return f'<div class="badge {lop}">{NHAN_GIONG[lop]}</div>' if lop else ""


def bo_sung(rec, word):
    """Vá những chỗ OpenRussian thiếu, NGAY TRONG LUỒNG TẠO THẺ.

    Hiện chỉ có một chỗ: **số từ** mà OpenRussian chỉ lưu dạng gốc
    (`formType = "ru_base"`) — `со́рок`, `сто`, `два`… Không vá ở đây thì từ mới
    user thêm sẽ ra thẻ không có bảng, trong khi 27 từ cùng loại thêm trước đó
    lại có (vì được vá riêng một lượt) — cùng một loại từ mà hai kiểu thẻ.

    User chốt: *"những cái này cũng phải làm để tự động lấy khi lấy từ mới, vì
    những cái này thuần cào data"*.

    Import wiktionary Ở TRONG HÀM: `wiktionary.py` import ngược lại module này,
    để ở đầu file là vòng tròn.
    """
    if not rec or rec.get("pos") != "numeral" or rec.get("numDecl"):
        return rec
    from . import wiktionary
    them = wiktionary.fetch_numeral(word, delay=0)
    if them:
        rec.update(them)
    return rec


def remember(word, rec):
    """Ghi một bản ghi vào cache (dùng khi vừa cào xong ở luồng tạo thẻ).

    Nhờ vậy thẻ user thêm hằng ngày tự có mặt trong cache, không phải chạy
    `cao_nguphap.py --anki` bù về sau — user chốt: *"những cái này cũng phải làm
    để tự động lấy khi lấy từ mới, vì những cái này thuần cào data"*.
    """
    if not rec:
        return
    cache = _cache()
    cache[bare(word)] = rec
    _save_cache(cache)


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


def _goc_qua_khu(inf):
    """Thân mà quá khứ ĐÚNG QUY TẮC phải bắt đầu bằng (nguyên thể bỏ đuôi).

    🔴 Phải bóc hậu tố phản thân TRƯỚC, rồi mới bóc đuôi nguyên thể. Bản cũ chỉ
    nhận đuôi `ть` trên chuỗi thô, nên **hai lớp động từ lọt sạch cửa**:
      · đuôi `-ти` — `идти́ → шёл`, `войти́ → вошёл`, `вы́йти → вы́шел`
      · mọi động từ **phản thân** (`встре́титься`), vì chuỗi kết thúc bằng `ся`
    Mà đuôi `-ти` đúng là nhóm quá khứ bất thường nhất tiếng Nga. Bỏ sót này bắt
    được 30/07/2026 khi soạn lô k01: `tiep` chỉ gắn cờ 5/15 từ, ba từ chuyển động
    lên thẻ mà không cờ nào nhắc quá khứ.
    """
    g = bare(inf)
    if g.endswith(("ся", "сь")):
        g = g[:-2]
    for duoi in ("ть", "ти", "чь"):
        if g.endswith(duoi) and len(g) - len(duoi) >= 2:
            return g[: -len(duoi)]
    return None


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
        goc = _goc_qua_khu(inf)
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


# Nhãn cột. NGẮN hết mức: bảng 5 cột phải lọt bề ngang 368px của .hd-content.
NHAN_COT = {"sg": "ít", "pl": "nhiều",
            "m": "он", "f": "она́", "n": "оно́"}


def _bang_cach(ten, du_lieu, nong, tien_to=""):
    """Dựng MỘT bảng 6 cách từ {cột: {cách: dạng}}.

    Dùng chung cho danh từ (ít/nhiều), tính từ · đại từ · số từ (theo giống) —
    bốn nhóm khác nhau nhưng cùng một hình dạng, nên cùng một hàm. Cột nào cũng
    trống thì bỏ hẳn bảng, không in khung rỗng.
    """
    cot = [c for c in ("sg", "m", "f", "n", "pl")
           if c in du_lieu and any((du_lieu[c] or {}).values())]
    if not cot:
        return ""
    # một cột duy nhất thì bỏ luôn hàng tiêu đề — thừa một dòng là thừa
    dau = ""
    if len(cot) > 1:
        dau = ('<tr><td class="gt-h"></td>'
               + "".join(f'<td class="gt-h">{NHAN_COT.get(c, c)}</td>' for c in cot)
               + "</tr>")
    rows = "".join(
        f'<tr><td class="gt-k">{nhan}</td>'
        + "".join(_o(du_lieu[c].get(ma), (tien_to + c, ma) in nong or (c, ma) in nong)
                  for c in cot)
        + "</tr>"
        for ma, nhan in CASES)
    return (f'<div class="gt-ten">{ten}</div>'
            f'<table class="gt-tbl">{dau}{rows}</table>')


def _bang_hang(ten, nhan_o, dang, nong, khoa):
    """Bảng dạng danh sách (chia ngôi, quá khứ, dạng ngắn) — 2 cột, N hàng."""
    o = [(nhan_o[i], dang[i], (khoa, i) in nong)
         for i in range(min(len(nhan_o), len(dang))) if (dang[i] or "").strip()]
    if not o:
        return ""
    rows = "".join(f'<tr><td class="gt-k">{n}</td>{_o(d, hot)}</tr>' for n, d, hot in o)
    return f'<div class="gt-ten">{ten}</div><table class="gt-tbl">{rows}</table>'


def _bang_danh_tu(rec, nong):
    return _bang_cach("Biến cách", rec.get("decl") or {}, nong)


# Nhãn sáu ô "Participles" của OpenRussian. Ngắn hết mức: bảng 2 cột phải lọt bề
# ngang 368px của `.hd-content`, mà cột nhãn đây dài hơn mọi bảng khác.
NHAN_PHAN_TU = (("activePresent", "chủ động · hiện tại"),
                ("activePast", "chủ động · quá khứ"),
                ("passivePresent", "bị động · hiện tại"),
                ("passivePast", "bị động · quá khứ"),
                ("gerundPresent", "trạng đt · hiện tại"),
                ("gerundPast", "trạng đt · quá khứ"))


def _o_phan_tu(ds):
    """Ô phân từ: các dạng cách nhau ` · `, kèm nghĩa Anh ở dòng nhỏ bên dưới.

    🔴 Soi `thieu_dau` cho TỪNG dạng, không soi trên chuỗi đã nối — nguồn có ô
    hai dạng mà chỉ dạng đầu được đánh trọng âm (`прочита́в · прочитавши`), nối
    lại rồi soi thì chuỗi "có dấu" nên cái thiếu dấu lọt im lặng.
    """
    dang = " · ".join(
        (f['f'] + '<span class="gt-ngo">?</span>') if thieu_dau(f["f"]) else f["f"]
        for f in ds)
    en = next((f["en"] for f in ds if f.get("en")), "")
    chu = f'<div class="gt-chu">{en}</div>' if en else ""
    return f'<td class="gt-v">{dang}{chu}</td>'


def _bang_phan_tu(rec):
    """Khối Participles (gồm cả Gerund) — ô nào nguồn để trống thì bỏ hẳn hàng.

    Thể hoàn thành gần như không có phân từ hiện tại, thể chưa hoàn thành gần như
    không có phân từ bị động quá khứ ⇒ in khung rỗng là dạy sai rằng "có mà chưa
    lấy về". Bảng nằm trong `<details>` gấp lại nên KHÔNG tốn pixel nào của trần
    700px (README §2) — đó là lý do lấy đủ được mà không phá chuẩn ngắn gọn.
    """
    parts = rec.get("parts") or {}
    rows = "".join(f'<tr><td class="gt-k">{nhan}</td>{_o_phan_tu(parts[k])}</tr>'
                   for k, nhan in NHAN_PHAN_TU if parts.get(k))
    if not rows:
        return ""
    return f'<div class="gt-ten">Phân từ</div><table class="gt-tbl">{rows}</table>'


def _bang_dong_tu(rec, nong):
    # Với thể HOÀN THÀNH, `presfut` là TƯƠNG LAI chứ không phải hiện tại — gọi
    # sai tên ở đây là dạy sai đúng thứ badge PERF/IMPF vừa dựng lên để phân biệt.
    hoan_thanh = rec.get("aspect") == "perfective"
    ten = "Tương lai đơn" if hoan_thanh else "Hiện tại"
    ra = _bang_hang(f"Chia ngôi — {ten}", PERSONS, rec.get("presfut") or [],
                    nong, "presfut")
    # Cột CÒN LẠI của khối Conjugation trên OpenRussian (trang hiện Present và
    # Future cạnh nhau). Ở đây xếp DỌC vì bề ngang chỉ có 368px.
    # 🔴 Truyền mảng THÔ, đừng lọc ô rỗng trước: `_bang_hang` bỏ ô rỗng theo CHỈ SỐ
    # để khớp nhãn ngôi; lọc trước là nhãn lệch hàng mà nhìn vẫn thấy có vẻ đúng.
    khac = rec.get("present") if hoan_thanh else rec.get("future")
    khac = khac or []
    co = [x for x in khac if x]
    if co and co != [x for x in (rec.get("presfut") or []) if x]:
        ra += _bang_hang("Hiện tại" if hoan_thanh else "Tương lai (ghép)",
                         PERSONS, khac, nong, "future")
    ra += _bang_hang("Quá khứ", PASTS, rec.get("past") or [], nong, "past")
    im = [x for x in (rec.get("imper") or []) if x]
    if im:
        ra += f'<div class="gt-phu">Mệnh lệnh: {" · ".join(im[:2])}</div>'
    ra += _bang_phan_tu(rec)
    return ra


def _bang_tinh_tu(rec, nong):
    ra = _bang_cach("Biến cách", rec.get("adjDecl") or {}, nong)
    ra += _bang_hang("Dạng ngắn", [n for _, n in GIONG_TT],
                     rec.get("shorts") or [], nong, "shorts")
    phu = []
    if rec.get("comp"):
        phu.append("hơn: " + " · ".join(rec["comp"][:3]))
    if rec.get("super"):
        phu.append("nhất: " + " · ".join(rec["super"][:2]))
    if rec.get("adverb"):
        phu.append("trạng từ: " + rec["adverb"])
    if rec.get("incomparable"):
        phu.append("KHÔNG có dạng so sánh")
    if phu:
        ra += '<div class="gt-phu">' + " · ".join(phu) + "</div>"
    return ra


def _bang_dai_tu(rec, nong):
    return _bang_cach("Biến cách", rec.get("proDecl") or {}, nong)


def _bang_so_tu(rec, nong):
    return _bang_cach("Biến cách", rec.get("numDecl") or {}, nong)


_BANG = {"noun": _bang_danh_tu, "verb": _bang_dong_tu, "adjective": _bang_tinh_tu,
         "pronoun": _bang_dai_tu, "numeral": _bang_so_tu}


_BANG_RE = re.compile(r'<details class="gt-bang">.*?</details>', re.S)


def attach_table(html, rec):
    """Gắn LẠI bảng chia vào cuối một ô Hướng dẫn — NGUỒN CHÂN LÝ DUY NHẤT.

    Luôn GỠ bảng cũ trước rồi mới nối bảng mới ⇒ gọi bao nhiêu lần cũng ra một
    kết quả, không đội bảng chồng bảng.

    🔴 Phải dùng hàm này ở MỌI chỗ ghi `HuongDan`, đặc biệt là luồng LÀM LẠI THẺ
    (`pipeline.redo_note_id`): ở đó `build_card_fields()` dựng lại toàn bộ field
    từ dữ liệu cào mới, nên nếu ghi thẳng thì phần chữ do lô soạn (chẻ từ · cách
    nhớ · họ hàng) **bị xoá sạch** — người dùng bấm "làm lại thẻ" cho một từ đã
    soạn kỹ và mất trắng nội dung mà không ai báo.
    """
    than = _BANG_RE.sub("", html or "").rstrip()
    return than + build_table(rec)


def build_table(rec, phan_tich=None):
    """HTML bảng chia ĐẦY ĐỦ ('' nếu từ này không biến cách / không có dữ liệu).

    🔴 MỌI từ có biến cách đều được bảng, không chỉ từ bất thường — user đổi
    quyết định 29/07: *"toàn bộ từ sẽ có bảng toàn bộ cách chia, làm sao thu gọn
    nhất có thể; cái này để tiện tra cứu về sau"*. Bộ phát hiện bất thường
    (`analyze`) đổi vai: nó không còn quyết định CÓ bảng hay không, mà chỉ (a) tô
    sáng ô biến đổi và (b) nhắc người soạn lô viết câu chú ý ở trên — đọc câu đó
    là hiểu cả bảng, bảng chỉ để tra cứu chi tiết.

    Bảng gấp trong `<details>` lồng nên KHÔNG tốn pixel nào của trần "vừa một
    màn hình iPhone" (README §2) khi đang đóng.
    """
    if not rec:
        return ""
    nong = (phan_tich or analyze(rec))["nong"]
    than = _BANG.get(rec.get("pos"))
    ruot = than(rec, nong) if than else ""
    if not ruot.strip():
        return ""

    if rec.get("declInfo"):
        # Chú giải NGƯỜI THẬT viết trong từ điển ("The forms with н- are used if
        # after a preposition") — quý hơn mọi thứ suy ra được, và đúng loại mà
        # agent tự nghĩ hay nói sai. Giữ nguyên văn, ghi rõ là của từ điển.
        ruot += f'<div class="gt-chu">📖 {rec["declInfo"]}</div>'

    ngo = ('<div class="gt-nguon">⚠️ Ô có dấu <b>?</b>: từ điển KHÔNG ghi trọng âm '
           '— chưa kiểm được, đừng học thuộc chỗ nhấn ở đó.</div>'
           if 'class="gt-ngo"' in ruot else "")
    nguon = "Wiktionary tiếng Nga" if rec.get("nguon") == "wiktionary" else "OpenRussian"
    return ('<details class="gt-bang"><summary class="gt-sum">'
            '📋 Bảng chia đầy đủ</summary>'
            f'<div class="gt-body">{ruot}{ngo}'
            f'<div class="gt-nguon">Nguồn: {nguon} — máy dựng, không qua AI. '
            'Ô sáng = chỗ biến đổi.</div>'
            '</div></details>')


# ==============================================================================
# --- HỢP ĐỒNG PUBLIC (G4, 31/07/2026) ---
# Ba tên dưới đây đang bị mảng khác gọi qua tên PRIVATE (`grammar._cache`,
# `grammar._BANG_RE`…). Thò tay vào ruột module khác thì ngày tách file này ra
# sẽ gãy ở những chỗ không ai nhớ. Nên tuyên bố hợp đồng TRƯỚC: caller đổi dần
# sang tên public khi tiện, `soatkientruc.py` S2 vẫn để VÀNG cho tới lúc đó.
#
# THUẦN CỘNG THÊM — không xoá, không đổi tên cũ, nên không thể làm hỏng caller
# đang chạy. Đây cũng chính là bước 1 của cuộc tách `grammar.py` sau này (điều
# kiện mở: xong toàn bộ lô + soát xanh 14 ngày + S2 về 0).
# ==============================================================================
BANG_RE = _BANG_RE          # regex bóc khối bảng chia khỏi HTML thẻ
doc_cache = _cache          # đọc ảnh chụp OpenRussian trên đĩa
luu_cache = _save_cache     # ghi ảnh chụp đó xuống đĩa
