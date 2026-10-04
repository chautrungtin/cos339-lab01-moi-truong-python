"""1.6.4: Quản lý sinh viên bằng lập trình hướng đối tượng."""
from dataclasses import dataclass


@dataclass
class SinhVien:
    ma: str
    ten: str
    diem: float

    def __post_init__(self):
        self.ma, self.ten = self.ma.strip(), self.ten.strip()
        if not self.ma or not self.ten:
            raise ValueError('Mã và tên không được rỗng')
        if not 0 <= self.diem <= 10:
            raise ValueError('Điểm phải từ 0 đến 10')

    def xep_loai(self):
        if self.diem >= 8:
            return 'Giỏi'
        if self.diem >= 6.5:
            return 'Khá'
        if self.diem >= 5:
            return 'Trung bình'
        return 'Chưa đạt'


class QuanLySinhVien:
    def __init__(self):
        self.danh_sach = {}

    def them(self, sv):
        if sv.ma in self.danh_sach:
            raise ValueError('Mã sinh viên đã tồn tại')
        self.danh_sach[sv.ma] = sv

    def tim(self, ma):
        return self.danh_sach.get(ma)

    def cap_nhat(self, ma, ten, diem):
        if ma not in self.danh_sach:
            raise ValueError('Không tìm thấy sinh viên')
        self.danh_sach[ma] = SinhVien(ma, ten, diem)

    def xoa(self, ma):
        if ma not in self.danh_sach:
            raise ValueError('Không tìm thấy sinh viên')
        return self.danh_sach.pop(ma)

    def sap_xep(self):
        return sorted(self.danh_sach.values(), key=lambda sv: (-sv.diem, sv.ma))


def hien_thi(ds):
    for sv in ds:
        print(f'{sv.ma} | {sv.ten:20} | {sv.diem:.1f} | {sv.xep_loai()}')


def main():
    ql = QuanLySinhVien()
    print('1.6.4 - QUẢN LÝ SINH VIÊN BẰNG OOP')
    ql.them(SinhVien('2410060248', 'Châu Trung Tín', 8.5))
    ql.them(SinhVien('SV02', 'Nguyễn Minh An', 6.0))
    ql.them(SinhVien('SV03', 'Trần Hoài Nam', 7.5))
    print('Sau khi thêm 3 sinh viên:')
    hien_thi(ql.sap_xep())
    print('Tìm 2410060248:', ql.tim('2410060248').ten)
    ql.cap_nhat('SV02', 'Nguyễn Minh An', 9.0)
    print('Cập nhật SV02 lên 9.0, xóa SV03:')
    ql.xoa('SV03')
    hien_thi(ql.sap_xep())
    try:
        ql.them(SinhVien('2410060248', 'Trùng mã', 7.0))
    except ValueError as loi:
        print('Kiểm tra trùng mã:', loi)


if __name__ == '__main__':
    main()
