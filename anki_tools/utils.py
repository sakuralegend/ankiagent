# ==============================================================================
# --- TIỆN ÍCH XỬ LÝ CHỮ + LOG TỐI GIẢN ---
# Các hàm nhỏ, không phụ thuộc module khác, dùng chung ở khắp nơi trong project.
# ==============================================================================
import re


def _print_safe(msg):
    """print() nhưng không crash nếu console không hỗ trợ encode ký tự (vd cp1252 trên Windows)."""
    try:
        print(msg)
    except UnicodeEncodeError:
        print(msg.encode("ascii", errors="replace").decode("ascii"))


def log_warn(msg):
    _print_safe(f"⚠️  {msg}")


def log_fail(msg):
    _print_safe(f"❌ {msg}")


def strip_accents_perfectly(text):
    return text.replace("\u0301", "").replace("'", "").lower()


def convert_stress_to_combining_accent(word):
    """Chuyển ' sau nguyên âm -> combining acute accent U+0301."""
    return re.sub(r"([а-яёА-ЯЁ])\'", lambda m: m.group(1) + "\u0301", word)


def hl_to_bracket(text):
    """Chuyển <hl>...</hl> thành [...] để hiển thị (dùng khi in ra terminal)."""
    return text.replace("<hl>", "[").replace("</hl>", "]")


def apply_hl(text):
    """Chuyển <hl>...</hl> thành <span class="hl">...</span> để hiển thị trong Anki."""
    if not text:
        return ""
    return text.replace("<hl>", '<span class="hl">').replace("</hl>", "</span>")
