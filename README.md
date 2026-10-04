# COS339 Bài thực hành 01

Cài đặt và kiểm tra môi trường Python trên macOS Apple Silicon.

## Môi trường đã kiểm tra

- Python 3.14.0, arm64 (Homebrew).
- Git 2.50.1 (Apple Git-155).
- Visual Studio Code 1.140.0, arm64.
- Microsoft Python, Pylance, Python Debugger và Python Environments.

## Chạy mã nguồn nộp kèm

Giải nén ZIP, mở Terminal tại thư mục source rồi chạy:

```sh
python3 -m venv .venv
source .venv/bin/activate
python kiem_tra_moi_truong.py
python lab01/ex01/hello.py
```

Trong VS Code, mở thư mục source, chọn Python: Select Interpreter rồi chọn
`.venv/bin/python`. Có thể chạy file bằng Run Python File in Terminal.
Không cần thư viện ngoài. `.venv` và `__pycache__` không đóng gói.

## Repository đã tạo và clone

https://github.com/chautrungtin/cos339-lab01-moi-truong-python

```sh
git clone https://github.com/chautrungtin/cos339-lab01-moi-truong-python.git
```

Mã nguồn gồm chương trình hello, kiểm tra môi trường và cấu hình VS Code.
Phần thiết lập môi trường thực hiện theo mục 1.6.1 của ghi chú buổi 20/09/2026.
