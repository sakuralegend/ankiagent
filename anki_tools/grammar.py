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

Bộ nhớ đệm: CHỈ TRONG RAM, lấp một lần từ ô `GrammarJSON` của thẻ Anki lúc chạy
(QD-11, 02/08/2026) — thẻ là nguồn DUY NHẤT, không còn file trên đĩa. Trước đó
có `data/grammar_cache.json` làm bộ đệm dự phòng, nhưng hai bản giống hệt nhau
sớm muộn SẼ lệch (đã có 89 thẻ lệch nhiều tuần không ai biết) nên bỏ hẳn.
"""
import io
import json
import os
import sys
import time
import urllib.parse

from .utils import log_fail, log_warn

# --- MẶT TIỀN (QD-19): ruột đã chia 4 mảnh lá, tên cũ (kể cả private) giữ đủ ---
# Bốn mảnh KHÔNG import ngược grammar nên không có vòng; vòng thật duy nhất vẫn
# là grammar↔wiktionary/anki_client, bẻ bằng import-trong-hàm như cũ (KIENTRUC §5).
from .chu_nga import (ACUTE, VOWELS, CASES, PERSONS, PASTS, GIONG_TT,          # noqa: F401
                      acc, bare, stress_pos)
from .boc_tudien import (BAN_GHI_V, PHAN_TU_KHOA, ban_ghi_cu, normalize,       # noqa: F401
                         _adj_declension, _decl_dai_tu, _decl_tu_forms,
                         _idioms, _dang, _boc_phan_tu)
from .hinh_thai import (DUOI_DANH_TU, DOI_CHUAN, DUOI_DONG_TU, analyze,        # noqa: F401
                        _yo, _than_danh_tu, _o_doi_chuan, _nguyen_am_chay,
                        _soi_danh_tu, _than_dong_tu, _than_tu_nguyen_the,
                        _goc_qua_khu, _soi_dong_tu, _soi_tinh_tu)
from .bang_chia import (NHAN_COT, NHAN_PHAN_TU, thieu_dau, go_bang, khoi_may,  # noqa: F401
                        cap_the_html, _nhan_bien_the, build_table,
                        _BANG_RE, _BANG, _o, _bang_cach,
                        _bang_hang, _bang_danh_tu, _o_phan_tu, _bang_phan_tu,
                        _bang_dong_tu, _bang_tinh_tu, _bang_dai_tu, _bang_so_tu)

_HERE = os.path.dirname(os.path.abspath(__file__))


# ------------------------------------------------------------------- cào + cache
_CACHE = None


def _cache():
    """Bộ nhớ đệm CHỈ TRONG RAM — không còn file trên đĩa (QD-11). Rỗng cho tới
    khi `_lap_dem_tu_the()` lấp từ thẻ Anki, hoặc `remember()`/`fetch_grammar()`
    tự thêm từ vừa cào.

    🔴 Trước 02/08/2026 có `data/grammar_cache.json` làm bản sao trên đĩa — bỏ
    hẳn vì Anki tự chuẩn hoá NFC lúc ghi field, còn file thì không, nên hai bản
    giống hệt nhau LỆCH NHAU VĨNH VIỄN (bug thật: `бу́ква` mang `U+0341` lỗi thời
    thay vì `U+0301`, 31/07/2026). Một nguồn thì không lệch được với chính nó."""
    global _CACHE
    if _CACHE is None:
        _CACHE = {}
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
# bộ nhớ đệm lâu dài giờ là ô `GrammarJSON` trong chính thẻ Anki (QD-11), không
# phải trang thô này.
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

    if rec:
        remember(word, rec)                   # ghi RAM + thẳng vào thẻ (nếu thẻ đã có)
    else:
        cache[key] = rec                      # {} cũng cache lại, khỏi thử lại vô ích
    if delay:
        time.sleep(delay)
    return rec


_DA_KEU = set()


_DA_HOI_THE = False


def _lap_dem_tu_the():
    """Lấp bộ nhớ đệm RAM bằng dữ liệu trong THẺ ANKI — chạy nhiều nhất MỘT lần
    mỗi tiến trình, và là NGUỒN DUY NHẤT (QD-11) — không còn file cache dự phòng.

    CHỈ THÊM khoá còn thiếu, TUYỆT ĐỐI không đè bản ghi đang có trong RAM (ví dụ
    từ vừa `remember()` trong CHÍNH lần chạy này — thẻ đang tạo mới, chưa kịp ghi
    lên Anki).

    🔴 Anki đóng / AnkiConnect lỗi ⇒ KÊU TO rồi NÉM LỖI THẲNG, CẤM âm thầm coi là
    "không có dữ liệu": thẻ giờ là nguồn DUY NHẤT, im lặng ở đây là mất trắng dữ
    liệu ngữ pháp của toàn bộ lệnh đang chạy — đúng cơ chế từng làm 89 thẻ lệch
    cache nhiều tuần không ai biết (bug cũ, nay không còn "cache" để lệch nữa)."""
    global _DA_HOI_THE
    if _DA_HOI_THE:
        return
    _DA_HOI_THE = True
    from . import anki_client                # trong hàm: anki_client import ngược module này
    try:
        tu_the = anki_client.doc_grammar_json_tat_ca()
    except Exception as e:
        log_fail(f"KHONG DOC DUOC du lieu ngu phap tu THE ANKI ({e})")
        raise RuntimeError(
            "[grammar] The la nguon DUY NHAT (QD-11), khong con file cache du "
            "phong. Mo Anki (AnkiConnect dang chay) roi chay lai.") from e
    cache = _cache()
    them = 0
    for w, rec in tu_the.items():
        khoa = bare(w)
        if khoa not in cache and rec:
            cache[khoa] = rec
            them += 1
    if them:
        print(f"[grammar] lay {them} tu tu THE ANKI vao bo dem", file=sys.stderr)


def get_cached(word):
    """Dữ liệu ngữ pháp của một từ, đọc từ THẺ ANKI (QD-11) — không còn file
    cache trên đĩa. KHÔNG gọi mạng OpenRussian (luồng hàng loạt 950 từ).

    🔴 Đọc thẻ không được (Anki đóng / AnkiConnect lỗi) ⇒ `_lap_dem_tu_the()` KÊU
    TO rồi ném lỗi thẳng lên đây — CẤM bắt rồi trả rỗng, vì rỗng ở đây từng khiến
    lô soạn ghi thẻ THIẾU bảng chia mà không ai biết.

    Từ THẬT SỰ chưa từng cào (Anki đọc được, chỉ là từ đó chưa có dữ liệu) vẫn
    trả `{}` bình thường — đó là "chưa có dữ liệu", khác với "không đọc được
    nguồn".

    🔴 KÊU khi bản ghi cũ phiên bản. Hàm này không gọi mạng nên KHÔNG tự chữa
    được — mà im lặng thì thẻ nhận bảng thiếu mục đúng lúc `nap` tưởng mình vừa
    ghi bản mới nhất. Đã dính thật 30/07: thêm `present`/`future`/`parts` vào
    `normalize()` mà cache còn v3, mọi đường đọc cache vẫn dựng bảng cũ không một
    tiếng nào. Kêu MỘT lần mỗi từ — 950 dòng giống nhau thì rồi cũng bị bỏ qua.
    """
    _lap_dem_tu_the()
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
        # 🔴 BẪY: `дя́дя`, `па́па`, `де́душка` là giống ĐỰC nhưng biến cách Y HỆT
        # giống cái (`дя́дей`) — hình thái KHÔNG phân biệt nổi. Bản đầu trả "f"
        # cho cả nhóm này; comment cảnh báo `дя́дя` lại nằm nhầm ở nhánh -ом/-ем
        # bên dưới nên vô tác dụng. Test `test_KHONG_DOAN_BUA_voi_dya_dya` bắt
        # được 31/07/2026 (đo: chưa thẻ nào sai vì từ điển đã ghi giống cho cả
        # nhóm, nhưng sẽ nổ ngay khi user thêm một từ như vậy).
        # Dấu hiệu DUY NHẤT dùng được: đồ vật đuôi -а/-я thì luôn giống cái;
        # chỉ NGƯỜI mới có ngoại lệ giống đực ⇒ animate rõ ràng False mới dám
        # kết luận. Thiếu dữ liệu animate cũng không kết luận — badge sai tệ hơn
        # badge trống.
        if nom.endswith(("а", "я")) and rec.get("animate") is not False:
            return None, None
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
    """Ghi một bản ghi vào RAM + thẳng vào ô `GrammarJSON` của thẻ NẾU thẻ đã có
    (dùng khi vừa cào xong, hoặc vá lại dữ liệu cho từ cũ).

    Thẻ CHƯA tồn tại (đang tạo mới) thì bỏ qua phần ghi thẻ — không phải lỗi,
    `build_card_fields()` tự đưa `rec` vào field `GrammarJSON` lúc `addNote`,
    ghi hai lần chỉ tốn một lượt gọi mạng vô ích.

    🔴 Thẻ ĐÃ có mà ghi hụt vì Anki đóng/lỗi ⇒ KÊU TO (raise) — không còn file
    cache dự phòng để giữ tạm dữ liệu lỡ ghi thẻ không thành (QD-11)."""
    if not rec:
        return
    key = bare(word)
    _cache()[key] = rec
    from . import anki_client
    try:
        anki_client.ghi_grammar_json(key, rec)
    except Exception as e:
        log_fail(f"remember('{word}'): ghi THE ANKI that bai ({e})")
        raise RuntimeError(
            f"[grammar] remember('{word}'): ghi THE ANKI that bai ({e}). Khong "
            "con file cache du phong — mo Anki roi thu lai (QD-11).") from e


# ==============================================================================
# --- HỢP ĐỒNG PUBLIC (G4, 31/07/2026) ---
# Ba tên dưới đây đang bị mảng khác gọi qua tên PRIVATE (`grammar._cache`,
# `grammar._BANG_RE`…). Thò tay vào ruột module khác thì ngày tách file này ra
# sẽ gãy ở những chỗ không ai nhớ. Nên tuyên bố hợp đồng TRƯỚC: caller đổi dần
# sang tên public khi tiện, `soatkientruc.py` S2 vẫn để VÀNG cho tới lúc đó.
#
# THUẦN CỘNG THÊM — không xoá, không đổi tên cũ, nên không thể hỏng caller đang
# chạy. (Tách grammar.py xong 03/08 — QD-19; mặt tiền đầu file giữ đủ tên.)
# ==============================================================================
BANG_RE = _BANG_RE          # regex bóc khối bảng chia khỏi HTML thẻ
doc_cache = _cache          # đọc bộ nhớ đệm RAM (lấp từ thẻ Anki, QD-11)
lap_dem_tu_the = _lap_dem_tu_the   # ép lấp đệm từ thẻ Anki NGAY (vd đầu cao_nguphap.py main())
