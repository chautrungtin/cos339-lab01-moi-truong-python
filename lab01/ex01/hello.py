"""Chạy thử Python sau khi thiết lập môi trường thực hành."""


def main():
    ho_ten = input("Nhập họ tên: ").strip()
    mssv = input("Nhập mã số sinh viên: ").strip()
    if not ho_ten or not mssv:
        print("Vui lòng nhập đầy đủ họ tên và mã số sinh viên.")
        return
    print(f"Xin chào {ho_ten}!")
    print(f"Mã số sinh viên: {mssv}")
    print("COS339 - Bài 1: Lập trình cơ bản với Python")
    print("Chương trình chạy thành công.")


if __name__ == "__main__":
    main()
