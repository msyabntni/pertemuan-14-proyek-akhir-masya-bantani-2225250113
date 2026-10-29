"""Pengujian otomatis sesuai tests/test_case.md. Jalankan: python3 tests/test_program.py"""
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from analisis import hitung_ketuntasan, hitung_statistik, tentukan_status  # noqa: E402
from data_io import baca_data  # noqa: E402
from main import main  # noqa: E402
from utilitas import validasi_nilai  # noqa: E402


def buat_file(isi):
    berkas = tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8")
    berkas.write(isi)
    berkas.close()
    return berkas.name


def data_dari(*nilai):
    return {f"N{i}": {"nama": f"S{i}", "nilai": n} for i, n in enumerate(nilai)}


class TestProgram(unittest.TestCase):
    def test_tc01_rata_rata_normal(self):
        self.assertEqual(hitung_statistik(data_dari(80, 70, 90))["rata_rata"], 80)

    def test_tc02_batas_nol_valid(self):
        self.assertTrue(validasi_nilai(0))

    def test_tc03_batas_seratus_valid(self):
        self.assertTrue(validasi_nilai(100))

    def test_tc04_nilai_105_ditolak(self):
        self.assertFalse(validasi_nilai(105))
        data, galat = baca_data(buat_file("A1,Ayu,105\n"))
        self.assertEqual(data, {})
        self.assertIn("di luar 0-100", galat[0])

    def test_tc05_file_tidak_ada_ditangani(self):
        with self.assertRaises(FileNotFoundError):
            baca_data("tidak_ada.txt")
        self.assertEqual(main(["tidak_ada.txt"]), 1)

    def test_tc06_semua_tuntas(self):
        data = data_dari(75, 80, 95)
        self.assertEqual(hitung_ketuntasan(data, 75)["tuntas"], len(data))

    def test_tc07_nilai_bukan_angka(self):
        data, galat = baca_data(buat_file("A1,Ayu,abc\n"))
        self.assertEqual(data, {})
        self.assertIn("bukan angka", galat[0])

    def test_tc08_nilai_negatif(self):
        self.assertFalse(validasi_nilai(-5))

    def test_tc09_nilai_sama_dengan_kkm(self):
        self.assertEqual(tentukan_status(75, 75), "Tuntas")
        self.assertEqual(tentukan_status(74.99, 75), "Belum Tuntas")

    def test_tc10_tidak_ada_data_valid(self):
        path = buat_file("# hanya komentar\n\n")
        self.assertEqual(main([path]), 1)

    def test_tc11_format_baris_salah(self):
        data, galat = baca_data(buat_file("A1,Ayu\nA2,Budi,80\n"))
        self.assertEqual(list(data), ["A2"])
        self.assertIn("format", galat[0])

    def test_tc12_nim_duplikat(self):
        data, galat = baca_data(buat_file("A1,Ayu,80\nA1,Budi,70\n"))
        self.assertEqual(len(data), 1)
        self.assertIn("duplikat", galat[0])


if __name__ == "__main__":
    unittest.main(verbosity=2)
