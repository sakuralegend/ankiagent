# -*- coding: utf-8 -*-
# ==============================================================================
# --- PHÁT HIỆN BẤT THƯỜNG hình thái (tách từ grammar.py 03/08/2026, QD-19) ---
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
from .chu_nga import CASES, PERSONS, bare, stress_pos

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


# Đuôi TÍNH TỪ. Danh từ chia bằng bộ đuôi này (`живо́тное`, `насеко́мое`) là
# chuyện có thật và có luật trong sách — xem `_chia_nhu_tinh_tu`.
DUOI_TINH_TU = {
    "ый", "ий", "ой", "ая", "яя", "ое", "ее", "ые", "ие",
    "ого", "его", "ому", "ему", "ым", "им", "ую", "юю", "ых", "их",
    "ыми", "ими", "ом", "ем", "ей", "ыx",
}


def _yo(s):
    return (s or "").replace("ё", "е")


def _bang_o(a, b):
    """Hai ô viết GIỐNG NHAU (so biến thể đầu, bỏ ё và dấu trọng âm)."""
    if not a or not b:
        return False
    return _yo(bare(a.split(",")[0].strip())) == _yo(bare(b.split(",")[0].strip()))


def _chia_nhu_tinh_tu(o):
    """Danh từ chia bằng bộ đuôi TÍNH TỪ -> trả về thân, không thì None.

    `живо́тное`, `насеко́мое`, `проше́дшее` là tính từ được danh từ hoá: thân đứng
    yên, mọi đuôi là đuôi tính từ. Đem so với mẫu đuôi DANH TỪ thì **mọi ô đều
    lệch** — bản cũ vì thế gắn cho `живо́тным` nhãn "NGUYÊN ÂM CHẠY" (không có
    nguyên âm nào chạy) rồi tô 10/12 ô. Cả hai lời khai đều sai, và agent soạn
    lô k68 (08/08/2026) đã bác đúng chỗ này.

    Đây là luật có trong sách giáo khoa nên **không tô ô nào** — chỉ nêu tên hệ
    thống để người soạn viết một câu. Đúng luật user chốt 08/08: *"có quy tắc
    suy ra được thì thôi, nhảy trọng âm hay khác từ mới tô"*.
    """
    nom = o.get(("sg", "nom")) or o.get(("pl", "nom")) or ""
    n = _yo(bare(nom.split(",")[0].strip()))
    for duoi in sorted(DUOI_TINH_TU, key=len, reverse=True):
        if not n.endswith(duoi) or len(n) - len(duoi) < 3:
            continue
        than = n[: -len(duoi)]
        dang = [_yo(bare(x.strip())) for f in o.values() for x in f.split(",") if x.strip()]
        if all(d.startswith(than) and d[len(than):] in DUOI_TINH_TU for d in dang):
            return than
    return None


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

    if _chia_nhu_tinh_tu(o):
        return ({so for so, _ in o},
                [("tinhtu", "Chia như TÍNH TỪ — thân đứng yên, đuôi là đuôi "
                            "tính từ (danh từ hoá).")], set())

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

    # CÁCH 4 VIẾT NHƯ CÁCH 2 — thứ không cửa nào cũ bắt được, vì đuôi (`-а`,
    # `-ов`) hoàn toàn chuẩn: cái lệch nằm ở QUAN HỆ giữa hai ô, không ở mặt chữ.
    # User bắt được 08/08/2026: thẻ `крокоди́л` có hẳn ô đỏ dạy điều này mà bảng
    # dưới không tô ô nào, trong khi `президе́нт` cùng hiện tượng lại được tô.
    #
    # 🔴 CỐ Ý không đọc field `animate` của nguồn — đo 08/08 trên 575 danh từ:
    # `ме́неджер`, `о́кунь`, `коза́`, `матрёшка` đều là sinh vật mà bị ghi `False`.
    # Điều quan sát được (hai ô viết giống nhau) đáng tin hơn lời khai của nguồn.
    # Cũng cố ý KHÔNG giải thích "vì là sinh vật" — máy chỉ trỏ chỗ, câu giải
    # thích là của người soạn lô (README §2).
    cach4 = {(so, "acc") for so in ("sg", "pl")
             if _bang_o(o.get((so, "acc")), o.get((so, "gen")))}
    if cach4:
        co.update(so for so, _ in cach4)
        nong.update(cach4)
        flags.append(("cach4", "CÁCH 4 viết như CÁCH 2: " + " · ".join(
            f"{'ít' if s == 'sg' else 'nhiều'} {o[(s, c)]}" for s, c in sorted(cach4))))

    # Ô có hai dạng thật (`дете́й, ребя́т`) — nhưng BỎ QUA ô vừa nhận là cách 4,
    # vì ở đó dạng thứ hai chỉ là ô mặc định của danh từ chỉ đồ vật mà nguồn in
    # kèm (`президе́нта, президе́нт`), không phải hai dạng song song. Đo 08/08:
    # đúng 1 từ dính khuôn đó; 7 từ còn lại (`ребёнок` · `сын` · `тётя` · `среда`
    # · `род` · `цех` · `чу́до`) có hai dạng vì lý do thật ⇒ nhãn cũ ĐÚNG, giữ.
    that = [(s, c, f) for (s, c), f in o.items()
            if "," in f and not _o_doi_chuan(f, than) and (s, c) not in cach4]
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
