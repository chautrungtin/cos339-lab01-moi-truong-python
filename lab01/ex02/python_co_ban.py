"""1.6.2: Mười ví dụ Python cơ bản."""
from math import isqrt


def tinh_toan(a, b):
    return a + b, a - b, a * b, a / b if b != 0 else None


def chan_le(n):
    return 'Chẵn' if n % 2 == 0 else 'Lẻ'


def lon_nhat(a, b, c):
    return max(a, b, c)


def tong_den_n(n):
    if n < 0:
        raise ValueError('n phải không âm')
    return sum(range(n + 1))


def giai_thua(n):
    if n < 0:
        raise ValueError('n phải không âm')
    ket_qua = 1
    for i in range(2, n + 1):
        ket_qua *= i
    return ket_qua


def nguyen_to(n):
    return n >= 2 and all(n % i != 0 for i in range(2, isqrt(n) + 1))


def fibonacci(n):
    if n < 0:
        raise ValueError('Số phần tử phải không âm')
    a, b, day = 0, 1, []
    for _ in range(n):
        day.append(a)
        a, b = b, a + b
    return day


def dao_chuoi(s):
    return s[::-1]


def dem_tu(s):
    return len(s.split())


def doi_nhiet_do(c):
    return c * 9 / 5 + 32


def main():
    print('1.6.2 - PYTHON CƠ BẢN | Châu Trung Tín - 2410060248')
    print('01. Tổng, hiệu, tích, thương (12, 4):', tinh_toan(12, 4))
    print('02. Kiểm tra 248:', chan_le(248))
    print('03. Lớn nhất của 8, 5, 9:', lon_nhat(8, 5, 9))
    print('04. Tổng 1 đến 10:', tong_den_n(10))
    print('05. 5! =', giai_thua(5))
    print('06. 29 là số nguyên tố:', nguyen_to(29))
    print('07. 8 số Fibonacci:', fibonacci(8))
    print('08. Đảo chuỗi HUTECH:', dao_chuoi('HUTECH'))
    print('09. Số từ:', dem_tu('Thực hành bảo mật thông tin'))
    print('10. 30 độ C =', doi_nhiet_do(30), 'độ F')


if __name__ == '__main__':
    main()
