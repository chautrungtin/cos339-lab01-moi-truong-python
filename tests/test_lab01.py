import unittest
from lab01.ex02.python_co_ban import *
from lab01.ex03.cau_truc_du_lieu import *
from lab01.ex04.quan_ly_sinh_vien import SinhVien, QuanLySinhVien


class PythonTests(unittest.TestCase):
    def test_so_hoc(self):
        self.assertEqual(tinh_toan(12, 4), (16, 8, 48, 3))
        self.assertIsNone(tinh_toan(1, 0)[3])
        self.assertEqual(tong_den_n(10), 55)
        self.assertEqual(giai_thua(0), 1)
        self.assertEqual(giai_thua(5), 120)
        with self.assertRaises(ValueError):
            giai_thua(-1)

    def test_day_va_chuoi(self):
        self.assertFalse(nguyen_to(-1))
        self.assertFalse(nguyen_to(1))
        self.assertTrue(nguyen_to(2))
        self.assertFalse(nguyen_to(49))
        self.assertEqual(fibonacci(8), [0, 1, 1, 2, 3, 5, 8, 13])
        self.assertEqual(dao_chuoi('HUTECH'), 'HCETUH')
        self.assertEqual(dem_tu('  a   b '), 2)
        self.assertEqual(doi_nhiet_do(30), 86)

    def test_cau_truc(self):
        self.assertEqual(bo_trung([2, 4, 2, 6]), [2, 4, 6])
        self.assertEqual(loc_chan([1, 2, 3, 4]), [2, 4])
        self.assertEqual(thong_ke([2, 4])['trung_binh'], 3)
        self.assertEqual(tan_suat('Git git Python'), {'git': 2, 'python': 1})
        with self.assertRaises(ValueError):
            thong_ke([])

    def test_quan_ly(self):
        ql = QuanLySinhVien()
        ql.them(SinhVien('248', 'Tín', 8.5))
        self.assertEqual(ql.tim('248').xep_loai(), 'Giỏi')
        with self.assertRaises(ValueError):
            ql.them(SinhVien('248', 'Trùng', 7))
        with self.assertRaises(ValueError):
            ql.cap_nhat('248', 'Tín', 11)
        self.assertEqual(ql.tim('248').diem, 8.5)
        ql.cap_nhat('248', 'Tín', 9)
        self.assertEqual(ql.xoa('248').diem, 9)
        self.assertIsNone(ql.tim('248'))


if __name__ == '__main__':
    unittest.main()
