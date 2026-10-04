"""Hiển thị thông tin thực tế của môi trường Python và Git."""
import platform
import subprocess
import sys
from pathlib import Path

print("COS339 - KIỂM TRA MÔI TRƯỜNG", flush=True)
print("Python:", platform.python_version(), flush=True)
print("Kiến trúc:", platform.machine(), flush=True)
print("macOS:", platform.mac_ver()[0], flush=True)
print("Trình thông dịch:", sys.executable, flush=True)
print("Môi trường ảo:", sys.prefix != sys.base_prefix, flush=True)
subprocess.run(["git", "--version"], check=True)
thu_muc = Path(__file__).resolve().parent
if (thu_muc / ".git").exists():
    subprocess.run(["git", "remote", "-v"], cwd=thu_muc, check=True)
else:
    print("Bản source ZIP không kèm lịch sử Git.")
    print("Repository: https://github.com/chautrungtin/cos339-lab01-moi-truong-python")
