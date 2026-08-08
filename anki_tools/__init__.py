# anki_tools package: chia nhỏ nw.py gốc thành các module theo cụm chức năng.

# --- CỬA CHUNG cho script NGOÀI gói (L1) -------------------------------------
# `goi_anki` là tên public của `anki_client._ac`. Script bên ngoài cần một lệnh
# AnkiConnect thô (`findNotes`, `notesInfo`…) thì gọi qua đây, KHÔNG tự mở
# `http://127.0.0.1:8765` và cũng KHÔNG gõ thẳng `_ac` — gõ tên private xuyên gói
# là cửa S2 kêu đỏ. Alias đặt ở `__init__.py` chứ không đặt trong `anki_client.py`
# vì file đó đã chạm mốc nợ dòng (S13); thêm vào đấy là nới trần bằng cửa sau.
from .anki_client import _ac as goi_anki                                # noqa: F401
