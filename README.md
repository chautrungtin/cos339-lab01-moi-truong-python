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

## Bài 01 theo ghi chú ngày 20/09/2026

Các ví dụ mục 1.6.2 và 1.6.3 minh họa các chủ đề được giao.

```sh
python lab01/ex02/python_co_ban.py
python lab01/ex03/cau_truc_du_lieu.py
python lab01/ex04/quan_ly_sinh_vien.py
python -m unittest discover -s tests -v
```

- 1.6.2: 10 ví dụ về số học, điều kiện, vòng lặp, hàm và chuỗi.
- 1.6.3: 5 ví dụ List, Tuple, Dictionary.
- 1.6.4: lớp SinhVien và QuanLySinhVien; thêm, tìm, sửa, xóa, sắp xếp.
- Dữ liệu điểm và sinh viên bổ sung là dữ liệu minh họa.

## Bài 02 — Caesar, Playfair và Flask

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python lab02/caesar.py
python lab02/playfair.py
python -m lab02.app
```

Mở http://127.0.0.1:5001. Dừng máy chủ bằng Control+C.
Nếu cổng đang được dùng, chạy `python -m flask --app lab02.app run --port 5002`.

Caesar giữ nguyên ký tự ngoài A-Z/a-z. Playfair gộp J vào I,
loại ký tự ngoài A-Z, dùng X làm đệm (Q nếu ký tự là X).
Kết quả giải mã Playfair giữ đệm vì không thể tự động phân biệt đệm với chữ gốc.
Đây là mã hóa cổ điển phục vụ học tập, không dành cho dữ liệu cần bảo mật thực tế.

Chạy kiểm thử: `python -m unittest discover -s tests -v`.
Bộ kiểm thử gồm ví dụ chuẩn, khóa âm, chữ lặp, đầu vào lỗi và giao diện Flask.

Mã nguồn được tổ chức trên các nhánh `lab-01` và `lab-02`;
Pull Request có nhánh đích `main`.
