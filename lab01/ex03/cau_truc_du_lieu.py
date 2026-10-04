"""1.6.3: Năm ví dụ List, Tuple và Dictionary."""


def thong_ke(ds):
    if not ds:
        raise ValueError('Danh sách không được rỗng')
    return {'tong': sum(ds), 'trung_binh': sum(ds) / len(ds),
            'nho_nhat': min(ds), 'lon_nhat': max(ds)}


def loc_chan(ds):
    return [x for x in ds if x % 2 == 0]


def bo_trung(ds):
    return list(dict.fromkeys(ds))


def tach_sinh_vien(sv):
    ma, ten, diem = sv
    return f'{ma} | {ten} | Điểm: {diem:.1f}'


def tan_suat(s):
    ket_qua = {}
    for tu in s.lower().split():
        ket_qua[tu] = ket_qua.get(tu, 0) + 1
    return ket_qua


def main():
    print('1.6.3 - LIST, TUPLE, DICTIONARY')
    ds = [2, 4, 8, 2, 6, 4]
    print('Dữ liệu:', ds)
    print('01. Thống kê:', thong_ke(ds))
    print('02. Lọc số chẵn:', loc_chan([1, 2, 3, 4, 5, 6]))
    print('03. Bỏ phần tử trùng:', bo_trung(ds))
    print('04. Tuple:', tach_sinh_vien(('2410060248', 'Châu Trung Tín', 8.5)))
    print('05. Tần suất:', tan_suat('python git python flask git python'))


if __name__ == '__main__':
    main()
