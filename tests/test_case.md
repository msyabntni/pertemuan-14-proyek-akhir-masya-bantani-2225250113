# Test Case Proyek Pertemuan 14: Rekap dan Analisis Nilai

Test case dirancang sebelum implementasi penuh. Pengujian otomatis ada di `tests/test_program.py`.

Cara menjalankan:

```bash
python3 tests/test_program.py
```

| ID | Kategori | Fitur | Input/Kondisi | Expected Result | Uji otomatis | Status |
|---|---|---|---|---|---|---|
| TC01 | Normal | F03 | Nilai 80, 70, 90 | Rata-rata 80 | `test_tc01_rata_rata_normal` | Lulus |
| TC02 | Batas | F02 | Nilai 0 | Diterima sebagai nilai valid | `test_tc02_batas_nol_valid` | Lulus |
| TC03 | Batas | F02 | Nilai 100 | Diterima sebagai nilai valid | `test_tc03_batas_seratus_valid` | Lulus |
| TC04 | Invalid | F02 | Nilai 105 | Ditolak dengan pesan validasi | `test_tc04_nilai_105_ditolak` | Lulus |
| TC05 | Invalid | F01 | File tidak ada | `FileNotFoundError` ditangani, muncul pesan, program tidak crash | `test_tc05_file_tidak_ada_ditangani` | Lulus |
| TC06 | Normal | F04 | Semua nilai ≥ KKM | Jumlah tuntas = jumlah data | `test_tc06_semua_tuntas` | Lulus |
| TC07 | Invalid | F02 | Nilai `abc` (bukan angka) | Ditolak, pesan "bukan angka" | `test_tc07_nilai_bukan_angka` | Lulus |
| TC08 | Invalid | F02 | Nilai -5 | Ditolak (di bawah 0) | `test_tc08_nilai_negatif` | Lulus |
| TC09 | Batas | F04 | Nilai = KKM (75) dan 74,99 | 75 Tuntas; 74,99 Belum Tuntas | `test_tc09_nilai_sama_dengan_kkm` | Lulus |
| TC10 | Invalid | F01 | File hanya komentar/kosong | Pesan "tidak ada data valid", tidak crash | `test_tc10_tidak_ada_data_valid` | Lulus |
| TC11 | Invalid | F01 | Baris `A1,Ayu` (kolom kurang) | Baris ditolak, baris lain tetap diproses | `test_tc11_format_baris_salah` | Lulus |
| TC12 | Invalid | F01 | NIM sama muncul dua kali | Baris kedua ditolak ("duplikat") | `test_tc12_nim_duplikat` | Lulus |
| TC13 | Normal | F05 | Jalankan `python3 src/main.py` | `output/laporan.txt` terbentuk; rata-rata 71,30; tuntas 6; belum tuntas 4 | Manual | Lulus |

## Perhitungan manual TC13 (data `data/nilai_contoh.txt`, KKM 75)

- Jumlah nilai = 85 + 78 + 92 + 60 + 75 + 100 + 0 + 68 + 81 + 74 = 713
- Rata-rata = 713 / 10 = **71,30**
- Minimum = 0; maksimum = 100
- Nilai ≥ 75: 85, 78, 92, 75, 100, 81 → **6 tuntas**, **4 belum tuntas**
