# -*- coding: utf-8 -*-
"""BÓC dữ liệu từ trang OpenRussian thành bản ghi gọn (`normalize` + phụ tùng)
— tách từ grammar.py (03/08/2026, QD-19). Mảnh LÁ: chỉ import chu_nga."""
import re

from .chu_nga import CASES, acc, bare

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
    # KHÔNG có `family` ở đây — cố ý, xem khối comment đầu file.
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
