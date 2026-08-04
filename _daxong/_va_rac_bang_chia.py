"""Vá 6 ca RÁC TẦNG DỮ LIỆU trong `GrammarJSON` của thẻ thật (chạy 04/08/2026, một lần).

Món nợ cuối cùng của `SONO.md` dòng 1. Công thức đã chứng minh ở `c6a3f94`
(`справа`): thẻ là nguồn DUY NHẤT (QD-11) nên gốc sửa được ngay — sửa thẳng
`GrammarJSON` qua cửa L1 `anki_client.ghi_grammar_json`, sao lưu bản cũ trước.

Ca thứ 7 trong sổ nợ (cách 5 `-ою` không nhãn) KHÔNG nằm ở đây: nó không phải
dữ liệu sai mà là dữ liệu THIẾU CHÚ THÍCH, và nó đụng **309 ô** chứ không phải
một từ ⇒ vá bằng CODE (`bang_chia._nhan_bien_the`), không vá bằng dữ liệu.

Từng ca, và vì sao bản mới đúng:

  педагогический — từ điển ghi `педагоги́ческый` / `педагоги́ческым` (chữ **ы**).
      Sau `к` tiếng Nga KHÔNG BAO GIỜ viết `ы` (quy tắc chính tả cơ bản) ⇒ phải
      là `-ий` / `-им`. Lỗi gõ của nguồn, không phải biến thể.

  фотограф — ba ô bị TRÁO: cách 3 số ít đang giữ dạng số nhiều (`фото́графам`),
      cách 3 số nhiều đang giữ dạng số ít (`фото́графу`), cách 5 số nhiều thì mất
      trọng âm và cụt đuôi (`фотографам`, đáng lẽ `фото́графами`).

  женатый — ô "trạng từ" ghi `жена́то`, nhưng đó là DẠNG NGẮN GIỐNG TRUNG (đã có
      sẵn trong `shorts`), không phải trạng từ. `жена́тый` không có trạng từ —
      in ra là dạy user một từ không tồn tại.

  человек — số nhiều đang xếp `челове́ки/челове́ков/челове́кам…` NGANG HÀNG với
      `лю́ди/люде́й/лю́дям…`. Dạng `челове́к-` số nhiều là cổ/đùa, đời nay không
      dùng. GIỮ LẠI đúng một chỗ: cách 2 `люде́й, челове́к` — `челове́к` ở đây là
      dạng THẬT và hay gặp, dùng sau số đếm (`пять челове́к` = năm người).

  князь — số nhiều cách 1 ghi `князья́, кня́зи`; `кня́зи` là dạng cổ. Các cách còn
      lại của từ này nguồn đã ghi đúng theo `князья́-`.

  тётя — cách 2/4 số nhiều ghi `те́тей`: sai **ё → е** và sai luôn chỗ nhấn. Đúng
      là `тётей`. (Đây chính là kiểu lỗi `ё` im lặng mà `CLAUDE.md` cảnh báo.)

L2: script một lần, đặt sẵn ở `_daxong/`, chết trong cùng commit.
Chạy: python _daxong/_va_rac_bang_chia.py [--apply]
"""
import copy
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
GOC = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(GOC))

from anki_tools import grammar                                   # noqa: E402
from anki_tools.anki_client import ghi_grammar_json              # noqa: E402

APPLY = "--apply" in sys.argv

# từ -> danh sách (đường dẫn khoá trong bản ghi, giá trị CŨ phải khớp, giá trị MỚI)
# Khớp giá trị cũ là chốt an toàn: nguồn đổi/đã ai đó vá rồi thì DỪNG, không ghi mù.
SUA = {
    "педагогический": [
        (("adjDecl", "m", "nom"), "педагоги́ческый", "педагоги́ческий"),
        (("adjDecl", "n", "inst"), "педагоги́ческым", "педагоги́ческим"),
    ],
    "фотограф": [
        (("decl", "sg", "dat"), "фото́графам", "фото́графу"),
        (("decl", "pl", "dat"), "фото́графу", "фото́графам"),
        (("decl", "pl", "inst"), "фотографам", "фото́графами"),
    ],
    "женатый": [
        (("adverb",), "жена́то", ""),
    ],
    "человек": [
        (("decl", "pl", "nom"), "лю́ди, челове́ки", "лю́ди"),
        (("decl", "pl", "gen"), "люде́й, челове́ков, челове́к", "люде́й, челове́к"),
        (("decl", "pl", "dat"), "лю́дям, челове́кам", "лю́дям"),
        (("decl", "pl", "acc"), "люде́й, челове́ков", "люде́й"),
        (("decl", "pl", "inst"), "людьми́, челове́ками", "людьми́"),
        (("decl", "pl", "prep"), "лю́дях, челове́ках", "лю́дях"),
    ],
    "князь": [
        (("decl", "pl", "nom"), "князья́, кня́зи", "князья́"),
    ],
    # CHỈ cách 4 sai. Cách 2 nguồn đã ghi đúng `тёть, тётей` — chốt "khớp giá trị
    # cũ" bắt được đúng chỗ mình đọc vội, đó là lý do nó tồn tại.
    "тётя": [
        (("decl", "pl", "acc"), "тёть, те́тей", "тёть, тётей"),
    ],
}


def lay(rec, duong):
    cho = rec
    for k in duong[:-1]:
        cho = (cho or {}).get(k) or {}
    return cho.get(duong[-1])


def dat(rec, duong, gia_tri):
    cho = rec
    for k in duong[:-1]:
        cho = cho[k]
    cho[duong[-1]] = gia_tri


def main():
    grammar.get_cached("мама")                 # ép lấp bộ đệm từ THẺ (QD-11)
    luu, hong = {}, []
    for tu, sua in SUA.items():
        cu = grammar.get_cached(tu)
        if not cu:
            hong.append(f"{tu}: KHONG CO ban ghi trong the")
            continue
        luu[tu] = copy.deepcopy(cu)
        moi = copy.deepcopy(cu)
        for duong, gia_cu, gia_moi in sua:
            that = lay(moi, duong)
            if that != gia_cu:
                hong.append(f"{tu}.{'.'.join(duong)}: dang la {that!r}, "
                            f"khong phai {gia_cu!r} -> BO QUA ca tu nay")
                break
            dat(moi, duong, gia_moi)
        else:
            for duong, gia_cu, gia_moi in sua:
                print(f"  {tu:16s} {'.'.join(duong):22s} {gia_cu!r} -> {gia_moi!r}")
            if APPLY:
                if not ghi_grammar_json(tu, moi):
                    hong.append(f"{tu}: khong tim thay note de ghi")

    if hong:
        print("\n!! CO VAN DE:")
        for h in hong:
            print("   " + h)
    if not APPLY:
        print("\n(CHAY KHAN — them --apply de ghi that)")
        return
    duong_luu = GOC / "backups" / "_backup_grammarjson_racbang_2026-08-04.json"
    duong_luu.parent.mkdir(exist_ok=True)
    duong_luu.write_text(json.dumps(luu, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\nda ghi {len(luu) - len({h.split(':')[0] for h in hong})} tu | "
          f"ban cu luu o {duong_luu}")


if __name__ == "__main__":
    main()
