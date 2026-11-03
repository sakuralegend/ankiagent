# -*- coding: utf-8 -*-
# ==============================================================================
# --- CÂU VÍ DỤ: MÁY CHỌN DẠNG · AI CHỈ ĐẶT CÂU · MÁY KIỂM + ĐÁNH DẤU (QD-47) ---
# Nơi DUY NHẤT dựng lời dặn đặt câu ví dụ cho thẻ từ vựng. Bot (thẻ mới, /sua) và
# script làm sạch kho đều đi qua `sinh_vi_du()` — cùng lời dặn, cùng cổng.
#
# VÌ SAO TÁCH VIỆC NHƯ THẾ NÀY (đo thật 03/11/2026, đủ số ở `git log --grep QD-47`):
# Lời dặn cũ bắt AI làm 6 việc một lượt (nghĩa Việt, 3 câu, dịch, chủ đề, từ loại,
# tự đánh dấu chữ) và KHÔNG có cổng nào soát. Quét 5 382 câu trên thẻ thật: ~300
# câu hỏng mà máy bắt được — dùng CẶP THỂ thay từ của thẻ (`брать`→`взять`), từ
# giảm nhẹ (`стол`→`столик`), từ cùng gốc khác loại (`ярко`→`яркое`), và câu MẤT
# HẲN CHỮ cần học (AI viết thẻ đánh dấu méo `<hlиграли>`, khâu dọn thẻ lột luôn chữ).
# Thử 8 từ lỗi × 4 cấu hình: đổi sang model TO HƠN mà giữ lời dặn cũ còn TỆ hơn
# (Gemini Flash 20/24 — model càng giỏi càng hay dùng cặp thể vì nó tự nhiên hơn).
# Thứ kéo lên là LỜI DẶN: máy giao sẵn dạng cho từng câu, AI chỉ còn "đặt câu có
# đúng chữ này" ⇒ 13 từ: Gemini Lite 39/39 (1,7 s/từ), Sonnet 39/39 (11 s/từ).
#
# Ba việc máy làm thay AI, và vì sao máy làm được:
#   1. CHỌN DẠNG — có sẵn bảng chia (`GrammarJSON`) của chính thẻ. Câu ra trải đều
#      các cách/thì ⇒ thẻ điền từ sau này có ngữ cảnh đa dạng.
#   2. KIỂM — dạng được giao phải có mặt nguyên chữ; so khớp chính xác, không đoán.
#   3. ĐÁNH DẤU chữ tiếng Nga — máy biết chữ nào, nên AI hết đường viết méo thẻ.
# Từ loại/chủ đề KHÔNG hỏi ở đây nữa: OpenRussian cho sẵn từ loại; chủ đề gọi
# `call_claude_topic` riêng (`anki_the.build_card_fields`).
#
# 🔴 Cái giá đã thấy của "ép dạng": Sonnet được giao `сыне` (cách 6) viết ra
# `Ну что, сыне, …` — dùng như lối gọi cổ. Chữ khớp nên cổng chữ để lọt ⇒ thêm luật
# dạng cách 6 phải có giới từ đứng ngay trước (`_GIOI_TU_CACH_6`). Ép dạng hiếm
# thì câu gượng, nên mỗi ô chỉ chọn trong nhóm dạng PHỔ BIẾN.
# ==============================================================================
import hashlib
import re

from .ai_client import call_claude_vi_du
from .chu_nga import bare
from .utils import log_warn

_TU_NGA = re.compile(r"[А-Яа-яЁё́-]+")
_GIOI_TU_CACH_6 = {"в", "во", "на", "о", "об", "обо", "при"}
_CACH = {"nom": ("cách 1", ""), "gen": ("cách 2", "genitive"), "dat": ("cách 3", "dative"),
         "acc": ("cách 4", "accusative"), "inst": ("cách 5", "instrumental"),
         "prep": ("cách 6", "prepositional — right after в/на/о/при")}


def _gap(chu):
    """Khoá SO KHỚP (không phải để hiện): bỏ dấu nhấn, gộp ё→е — AI hay viết е cho ё."""
    return bare(chu).replace("ё", "е")


def _dau(o):
    """Ô bảng chia có thể ghi hai biến thể ("дверя́ми, дверьми́") — biến thể ĐẦU là
    thứ đưa cho AI; cổng thì nhận MỌI biến thể (`_bien_the`), vì AI viết biến thể
    sau là viết đúng (đo 03/11: `дверьми` bị cổng chặn oan)."""
    return str(o or "").split(",")[0].strip()


def khoa_dang(o):
    """Khoá so khớp của biến thể ĐẦU trong một ô bảng chia (hoặc một chữ) — để biết
    hai câu có đang dùng cùng một dạng không."""
    return _gap(_dau(o))


def _bien_the(o):
    return {_gap(p) for p in str(o or "").split(",") if p.strip()}


def _xoay(tu, o_so, ds):
    """Chọn một ứng viên, CỐ ĐỊNH theo từ: chạy lại vẫn ra cùng dạng (test lặp lại
    được), mà các từ khác nhau thì rải đều nhóm dạng."""
    ds = [x for x in ds if x[0]]
    if not ds:
        return None
    n = int(hashlib.md5(f"{tu}|{o_so}".encode("utf-8")).hexdigest(), 16)
    return ds[n % len(ds)]


def _o_cach(bang, cach, ten):
    """Một ô bảng cách -> (dạng, nhãn kiểu 'số ít, cách 6', gợi ý tiếng Anh cho AI)."""
    nhan, goi_y = _CACH[cach]
    return (str((bang or {}).get(cach) or ""), f"{ten}, {nhan}", goi_y)


def chon_dang(rec, tu):
    """GrammarJSON -> (loại, [(ô bảng chia — có thể nhiều biến thể, nhãn Việt, gợi ý tiếng Anh)] × 3)."""
    rec = rec or {}
    pos = rec.get("pos")
    if pos == "noun" and rec.get("decl"):
        sg, pl = rec["decl"].get("sg") or {}, rec["decl"].get("pl") or {}
        it = [_o_cach(sg, c, "số ít") for c in ("prep", "gen", "inst", "dat", "acc")]
        nhieu = [_o_cach(pl, c, "số nhiều") for c in ("nom", "gen", "prep")]
        dau = _o_cach(sg, "nom", "số ít") if sg.get("nom") else _o_cach(pl, "nom", "số nhiều")
        o = [dau, _xoay(tu, 2, it), _xoay(tu, 3, nhieu) or _xoay(tu, 4, it)]
        loai, du_phong = "noun", it + nhieu
    elif pos == "verb":
        hoan_thanh = rec.get("aspect") == "perfective"
        nay = rec.get("presfut") if hoan_thanh else (rec.get("present") or rec.get("presfut"))
        nay, qk, ml = nay or [], rec.get("past") or [], rec.get("imper") or []
        ten_nay = "tương lai" if hoan_thanh else "hiện tại"
        goi_nay = "future tense" if hoan_thanh else "present tense"
        ngoi = ["я", "ты", "он/она", "мы", "вы", "они"]
        gioi = ["giống đực", "giống cái", "giống trung", "số nhiều"]
        o1 = [(str(nay[i]), f"{ten_nay}, ngôi {ngoi[i]}", goi_nay) for i in (0, 2, 3, 5) if i < len(nay)]
        o2 = [(str(qk[i]), f"quá khứ, {gioi[i]}", "past tense") for i in (0, 1, 3) if i < len(qk)]
        o3 = [(str(rec.get("acc") or ""), "nguyên mẫu", "infinitive")] + (
            [(str(ml[0]), "mệnh lệnh", "imperative")] if ml else [])
        o = [_xoay(tu, 1, o1), _xoay(tu, 2, o2), _xoay(tu, 3, o3)]
        loai, du_phong = ("verb_pf" if hoan_thanh else "verb_impf"), o1 + o2 + o3
    elif pos == "adjective" and rec.get("adjDecl"):
        a = rec["adjDecl"]
        o2 = [_o_cach(a.get("f"), c, "giống cái") for c in ("nom", "acc")] + [_o_cach(a.get("n"), "nom", "giống trung")]
        o3 = [_o_cach(a.get("pl"), "nom", "số nhiều"), _o_cach(a.get("m"), "inst", "giống đực"),
              _o_cach(a.get("m"), "prep", "giống đực")]
        o = [_o_cach(a.get("m"), "nom", "giống đực"), _xoay(tu, 2, o2), _xoay(tu, 3, o3)]
        loai, du_phong = "adj", o2 + o3
    else:
        goc = (str(rec.get("acc") or tu), "nguyên dạng", "")
        return "khac", [goc] * 3
    # Hai ô trùng chữ (vd cách 1 = cách 4) thì lấp bằng dạng khác chưa dùng.
    ra, da = [], set()
    for x in [x for x in o if x and x[0]] + [x for x in du_phong if x[0]]:
        if _gap(_dau(x[0])) not in da:
            da.add(_gap(_dau(x[0])))
            ra.append(x)
        if len(ra) == 3:
            break
    if not ra:
        return "khac", [(tu, "nguyên dạng", "")] * 3
    while len(ra) < 3:
        ra.append(ra[0])
    return loai, ra


_LUAT_LOAI = {
    "noun": "Use this noun itself. Never a diminutive (стол→столик, сын→сынок) and never another word from the same root.",
    "verb_impf": ("This is an IMPERFECTIVE verb. Choose situations where the imperfective is the natural choice: "
                  "habits, repeated or ongoing actions, 'don't do X'. Never use its perfective partner ({p}) or any prefixed verb."),
    "verb_pf": "This is a PERFECTIVE verb: one completed result or a single future action. Never use its imperfective partner ({p}).",
    "adj": "Use this adjective itself — never its adverb, comparative, or a noun from the same root.",
    "khac": "Use exactly this word, unchanged — never a related adjective, noun or verb from the same root.",
}
_HE_THONG = (
    "You are a native Russian speaker writing example sentences for a Vietnamese learner. "
    "Write natural, casual, everyday Russian, like texting a friend — 5 to 12 words, each sentence in a "
    "different everyday situation. Translate each sentence naturally into English and Vietnamese, and wrap the "
    "word(s) that translate the target word in <b>...</b> in the en and vi sentences only. Also give a short "
    "Vietnamese meaning of the target word (a few words, no explanation). Return JSON only.")
def _khuon(n):
    """Khuôn JSON đúng `n` câu (n < 3 khi chỉ viết lại câu hỏng của thẻ cũ)."""
    return {"type": "object", "properties": {
        "vietnamese_meaning": {"type": "string"},
        "examples": {"type": "array", "minItems": n, "maxItems": n, "items": {
            "type": "object",
            "properties": {"ru": {"type": "string"}, "en": {"type": "string"}, "vi": {"type": "string"}},
            "required": ["ru", "en", "vi"]}}},
        "required": ["vietnamese_meaning", "examples"]}


def loi_dan(tu, nghia_anh, rec, o=None):
    """-> (lời dặn hệ thống, lời dặn từ, các ô dạng, cặp thể bị cấm).
    `o` cho trước = chỉ đặt câu cho những ô đó (viết lại câu hỏng của thẻ cũ)."""
    loai, o_mac_dinh = chon_dang(rec, tu)
    o = o or o_mac_dinh
    cap = [_dau(p) for p in ((rec or {}).get("partners") or [])]
    dong = [f"Word: {tu} ({'; '.join(nghia_anh[:3]) if nghia_anh else 'N/A'}).",
            _LUAT_LOAI[loai].format(p=", ".join(bare(c) for c in cap) or "-")]
    for i, (dang, _nhan, goi_y) in enumerate(o):
        dong.append(f"Sentence {i + 1} must contain exactly the form «{bare(_dau(dang))}»"
                    + (f" ({goi_y})" if goi_y else "") + " — do not change it.")
    return _HE_THONG, "\n".join(dong), o, cap


def kiem_cau(ru, o, cap=(), dang_khac=frozenset()):
    """Cổng một câu. Trả về None nếu qua, hoặc lý do trượt (để log).

    `dang_khac` = mọi dạng khác của CHÍNH từ này (`tat_ca_dang`). Không có dạng
    được giao mà có dạng khác ⇒ VẪN QUA: đo 03/11, giao `рыба` thì Gemini viết
    `жарить рыбу` — câu đúng, tự nhiên — mà cổng chặt loại oan, đốt lượt gọi lại
    (72 câu kẹt lại phần lớn vì thế). Cặp thể/từ cùng gốc vẫn KHÔNG có trong
    `dang_khac` nên vẫn bị chặn; đổi lại thẻ có thể ít đa dạng dạng hơn chút."""
    dang, _nhan, goi_y = o
    if not ru or "<" in ru or ">" in ru:
        return "câu rỗng hoặc còn thẻ HTML"
    chu = [_gap(t) for t in _TU_NGA.findall(ru)]
    dich = _bien_the(dang)
    trung = [i for i, c in enumerate(chu) if c in dich]
    if not trung and not any(c in dang_khac for c in chu):
        return f"thiếu dạng «{bare(_dau(dang))}»"
    if any(_gap(c) in chu for c in cap):
        return "dùng cặp thể"
    if trung and goi_y.startswith("prepositional"):
        i = trung[0]
        if not _GIOI_TU_CACH_6.intersection(chu[max(0, i - 3):i]):
            return f"«{bare(_dau(dang))}» (cách 6) không đứng sau giới từ"
    return None


def danh_dau(ru, dang, dang_khac=()):
    """Bọc <hl> quanh chữ khớp dạng được giao; không có thì chữ khớp một dạng khác
    của chính từ đó — giữ nguyên chữ như AI viết (hoa/thường, ё)."""
    for nhom in (_bien_the(dang), dang_khac):
        for m in _TU_NGA.finditer(ru):
            if _gap(m.group()) in nhom:
                return f"{ru[:m.start()]}<hl>{m.group()}</hl>{ru[m.end():]}"
    return ru


def _b_sang_hl(text):
    text = re.sub(r"<b>(.*?)</b>", r"<hl>\1</hl>", text or "", flags=re.S)
    return re.sub(r"<(?!/?hl>)[^>]*>", "", text).strip()


def sinh_vi_du(tu, nghia_anh, rec, goi=call_claude_vi_du, so_luot=2, o=None):
    """-> {"vietnamese_meaning", "simplified_examples": [{ru,en,vi} có <hl>]} hoặc None.

    Mỗi ô giữ câu ĐẦU TIÊN qua cổng qua các lượt; ô nào chưa có thì lượt sau hỏi
    lại cả bộ. Hết lượt mà còn ô trống thì trả phần đã qua (thẻ ít câu còn hơn câu
    sai); không ô nào qua ⇒ None, người gọi lo nhánh dự phòng.
    `goi` cắm được: script làm sạch kho truyền đường gọi Sonnet, bot dùng mặc định."""
    he_thong, dan, o, cap = loi_dan(tu, nghia_anh, rec, o)
    dang_khac = tat_ca_dang(rec, tu) - {_gap(c) for c in cap}
    giu, nghia = [None] * len(o), ""
    for _ in range(so_luot):
        r = goi(he_thong, dan, _khuon(len(o)))
        if not isinstance(r, dict):
            continue
        nghia = nghia or (r.get("vietnamese_meaning") or "").strip()
        for i, ex in enumerate((r.get("examples") or [])[:len(o)]):
            if giu[i] or not isinstance(ex, dict):
                continue
            ru = (ex.get("ru") or "").strip()
            ly_do = kiem_cau(ru, o[i], cap, dang_khac)
            if ly_do:
                log_warn(f"Câu ví dụ `{tu}` trượt cổng ({ly_do}): {ru}")
                continue
            giu[i] = {"ru": danh_dau(ru, o[i][0], dang_khac), "en": _b_sang_hl(ex.get("en")),
                      "vi": _b_sang_hl(ex.get("vi"))}
        if all(giu):
            break
    cau = [g for g in giu if g]
    # `chi_so`: câu nào ứng với ô nào — script làm sạch cần để đặt câu mới đúng chỗ.
    return ({"vietnamese_meaning": nghia, "simplified_examples": cau,
             "chi_so": [i for i, g in enumerate(giu) if g]} if cau else None)


# --- SOÁT CÂU ĐANG CÓ TRÊN THẺ (script làm sạch kho, 03/11/2026) ---------------
# Câu cũ do AI tự đánh dấu, nên soát CHỮ ĐƯỢC ĐÁNH DẤU: phải đúng một chữ, và chữ
# đó phải là một dạng của chính từ này trong bảng chia. Phân từ (`parts`), trạng từ
# đi kèm tính từ (`adverb`) và cặp thể KHÔNG tính — đó là từ khác, đúng loại lỗi
# đang dọn (`ярко`→`яркое`, `писать`→`написал`).
_KHOA_KHONG_PHAI_DANG = {"en", "rank", "v", "pos", "gender", "aspect", "partners", "motion", "parts",
                         "adverb", "animate", "countable", "declMode", "incomparable", "reflexive"}


def tat_ca_dang(rec, tu=""):
    ra = {_gap(tu)} if tu else set()

    def di(x):
        if isinstance(x, str):
            ra.update(_bien_the(x))
        elif isinstance(x, dict):
            for k, v in x.items():
                if k not in _KHOA_KHONG_PHAI_DANG:
                    di(v)
        elif isinstance(x, list):
            for v in x:
                di(v)
    di(rec or {})
    return ra


def kiem_cau_cu(ru, dang):
    """`ru` là câu Nga đã bóc về text có <hl>…</hl> (html_builder.parse_examples_html),
    `dang` = tat_ca_dang(...). None = qua."""
    if re.search(r"<(?!/?hl>)|(?<!<)/hl>", ru) or ru.count("<hl>") != ru.count("</hl>"):
        return "thẻ đánh dấu méo"
    hl = re.findall(r"<hl>(.*?)</hl>", ru)
    if len(hl) != 1:
        return f"có {len(hl)} chữ được đánh dấu"
    if _gap(hl[0]) not in dang:
        return f"«{hl[0]}» không phải dạng của từ này"
    return None


# --- NHÃN DẠNG cho câu điền từ (QD-48, 03/11/2026) -----------------------------
# Mặt sau thẻ điền từ in "стол → столом · số ít, cách 5": user GÕ dạng từ điển,
# còn dạng đã chia thì học thụ động qua nhãn này. Tra ngược trong bảng chia của
# CHÍNH thẻ; không thấy thì trả "" (không bịa nhãn).
_NGOI = ["ngôi я", "ngôi ты", "ngôi он/она", "ngôi мы", "ngôi вы", "ngôi они"]
_GIONG_QK = ["giống đực", "giống cái", "giống trung", "số nhiều"]
_TEN_GIONG = {"m": "giống đực", "f": "giống cái", "n": "giống trung", "pl": "số nhiều"}


def nhan_dang(rec, chu):
    """Chữ trong câu -> nhãn tiếng Việt của dạng đó ("số ít, cách 5"), hoặc ""."""
    rec, k = rec or {}, _gap(chu)
    ra = []

    def xet(o, nhan):
        if k in _bien_the(o) and nhan not in ra:
            ra.append(nhan)
    for so, ten in (("sg", "số ít"), ("pl", "số nhiều")):
        for c, o in ((rec.get("decl") or {}).get(so) or {}).items():
            if c in _CACH:
                xet(o, f"{ten}, {_CACH[c][0]}")
    for g, bang in (rec.get("adjDecl") or {}).items():
        for c, o in (bang or {}).items():
            if c in _CACH:
                xet(o, f"{_TEN_GIONG.get(g, g)}, {_CACH[c][0]}")
    hoan_thanh = rec.get("aspect") == "perfective"
    for i, o in enumerate(rec.get("presfut") if hoan_thanh else (rec.get("present") or [])):
        if i < 6:
            xet(o, f"{'tương lai' if hoan_thanh else 'hiện tại'}, {_NGOI[i]}")
    for i, o in enumerate(rec.get("past") or []):
        if i < 4:
            xet(o, f"quá khứ, {_GIONG_QK[i]}")
    for o in rec.get("imper") or []:
        xet(o, "mệnh lệnh")
    for o in rec.get("shorts") or []:
        xet(o, "dạng ngắn")
    for o in rec.get("comp") or []:
        xet(o, "so sánh hơn")
    if k in _bien_the(rec.get("acc") or ""):
        return "dạng từ điển"          # đúng chữ user gõ — nói thẳng, khỏi kê cách 1/4
    gop = {}                           # "số ít, cách 2" + "số ít, cách 6" -> "số ít, cách 2/6"
    for n in ra:
        dau, _, cach = n.rpartition(", cách ")
        if dau and cach:
            gop.setdefault(dau, []).append(cach)
        else:
            gop.setdefault(n, [])
    return " / ".join(f"{d}, cách {'/'.join(c)}" if c else d for d, c in gop.items())
