# -*- coding: utf-8 -*-
"""S9 · S11 — hai cửa soi QUY TRÌNH chứ không soi code: commit message có khai
VÌ SAO không, và cái hook nhắc luật còn sống không.

Cả hai đều CHẠY tiến trình ngoài (`git`, lệnh hook) — chỗ duy nhất trong bộ soát
làm việc đó, nên gom chung một file để biết ngay phải nghi ngờ ở đâu khi chậm.
"""
import json
import subprocess

from . import khung
from .khung import PhatHien


def _chay(lenh, cho=20):
    """Gọi tiến trình ngoài. Trả `(CompletedProcess, None)`, hoặc `(None, lỗi)` khi
    không chạy nổi — S11 cần chính CÁI LỖI đó để nói ra kiểu chết.

    🔴 PHẢI khai encoding="utf-8": mặc định text=True dùng cp1252 (Windows),
    commit message có tiếng Việt/Nga ⇒ UnicodeDecodeError trong thread nền,
    stdout thành None và cửa này chết. Đã dính thật 31/07/2026.
    """
    try:
        return subprocess.run(lenh, cwd=str(khung.GOC), capture_output=True, text=True,
                              encoding="utf-8", errors="replace", timeout=cho), None
    except (OSError, subprocess.SubprocessError) as e:
        return None, e


# ---------------------------------------------------------------------------
# S9 — commit đụng code mà không khai VÌ SAO
# ---------------------------------------------------------------------------
def s9_commit_thieu_vi_sao():
    """Commit đụng code phải khai VÌ SAO trong THÂN, không chỉ tiêu đề — commit
    message gắn chặt với diff nên không nói dối được (thay cửa CHANGELOG, QD-06).
    Chỉ soi commit CHƯA PUSH: code đã rời PC thì kêu cũng muộn."""
    def _git(*doi_so):
        """Goi git, tra stdout hoac None. Goi nhieu lan thay vi gop bang ky tu
        phan cach — ban gop tung lam ky tu dieu khien lot vao source."""
        r, _ = _chay(["git", *doi_so])
        if r is None:
            return None
        return r.stdout if r.returncode == 0 else None

    danh_sach = _git("log", "origin/main..HEAD", "--format=%H")
    if not danh_sach:
        return []          # khong git / chua co origin/main / khong co commit nao

    ra = []
    for sha in [d.strip() for d in danh_sach.splitlines() if d.strip()]:
        tieu_de = (_git("log", "-1", "--format=%s", sha) or "").strip()
        than = (_git("log", "-1", "--format=%b", sha) or "").strip()

        ten_file = _git("show", "--name-only", "--format=", sha)
        if ten_file is None:
            continue
        da_doi = {d.strip() for d in ten_file.splitlines() if d.strip()}

        la_code = [d for d in da_doi
                   if d.endswith((".py", ".ps1", ".sh", ".service"))
                   and not d.startswith("_daxong/")]
        if not la_code:
            continue                               # chỉ sửa tài liệu -> không bắt buộc

        # Ngưỡng cố ý THẤP: chỉ chặn commit trần trụi một dòng. Không chấm điểm văn
        # hay — bộ soát khắt khe về câu chữ sẽ bị vô hiệu hoá bằng vài từ vô nghĩa.
        if len(than.strip()) < 40:
            ra.append(PhatHien(
                f"commit {sha[:8]}", 0,
                f"dung {len(la_code)} file code ma message KHONG co phan than giai thich "
                f"vi sao (\"{tieu_de[:50]}\") — sua bang `git commit --amend`"))
    return ra


# ---------------------------------------------------------------------------
# S11 — hook nhắc luật còn sống không
# ---------------------------------------------------------------------------
def s11_hook_con_song():
    """Hook `UserPromptSubmit` bơm lại luật mỗi lượt — nó chết là chết IM LẶNG
    (QD-13). Phải CHẠY THẬT lệnh hook chứ không chỉ kiểm file tồn tại: kiểu chết
    hay gặp nhất là `python` không có trên PATH, nhìn tên file sẽ báo XANH oan.
    CỐ Ý không chấm nội dung hook — cửa chấm câu chữ bị vô hiệu bằng vài từ (S9)."""
    p_cai_dat = khung.GOC / ".claude" / "settings.json"
    if not p_cai_dat.exists():
        return [PhatHien(".claude/settings.json", 0,
                         "khong ton tai -> hook nhac luat KHONG chay, luat se mo dan trong phien dai")]
    try:
        cau_hinh = json.loads(p_cai_dat.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        return [PhatHien(".claude/settings.json", 0, f"doc/parse that bai ({e}) -> hook coi nhu chet")]

    lenh = [h.get("command", "")
            for nhom in cau_hinh.get("hooks", {}).get("UserPromptSubmit", [])
            for h in nhom.get("hooks", []) if h.get("type") == "command"]
    if not lenh:
        return [PhatHien(".claude/settings.json", 0,
                         "khong con hook UserPromptSubmit nao -> luat khong duoc bom lai moi luot (QD-09)")]

    ra = []
    for cau in lenh:
        phan = cau.split()
        # Đối số nào trông như đường dẫn trong repo thì phải tồn tại thật.
        for doi_so in phan[1:]:
            if doi_so.endswith(".py") and not (khung.GOC / doi_so).exists():
                ra.append(PhatHien(f"hook|{doi_so}", 0,
                                   f"settings.json goi '{doi_so}' nhung file KHONG ton tai"))
        if ra:
            continue
        r, loi = _chay(phan, cho=10)
        if r is None:
            ra.append(PhatHien(f"hook|{cau[:40]}", 0,
                               f"KHONG chay duoc tren may nay ({type(loi).__name__}) — "
                               f"hay gap nhat: lenh 'python' khong co tren PATH"))
            continue
        if r.returncode != 0:
            ra.append(PhatHien(f"hook|{cau[:40]}", 0,
                               f"chay xong nhung exit {r.returncode} -> Claude Code bo qua ket qua"))
        elif not (r.stdout or "").strip():
            ra.append(PhatHien(f"hook|{cau[:40]}", 0,
                               "chay duoc nhung KHONG in ra gi -> bom vao context mot chuoi rong"))
    return ra
