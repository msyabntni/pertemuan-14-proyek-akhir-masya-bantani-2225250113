# pertemuan-14-proyek-akhir-masya-bantani-2225250113

| **Keterangan** | **Data** |
|---|---|
| **Nama** | Masya Bantani |
| **NIM** | 2225250113 |
| **Kelas** | 3-E |
| **Jurusan** | Pendidikan Matematika |


## Deskripsi

Program Python berbasis terminal untuk guru matematika. Program membaca data nilai dari file, memvalidasi, menghitung statistik kelas, menentukan status ketuntasan berdasarkan KKM, dan menyimpan laporan ke file teks. Rancangan lengkap ada di [`proposal.md`](proposal.md).

## Fitur Wajib

- Membaca file nilai (`NIM,Nama,Nilai`)
- Memvalidasi nilai pada rentang 0–100, format baris, dan duplikat NIM
- Menghitung rata-rata, minimum, dan maksimum
- Menghitung jumlah tuntas/belum tuntas berdasarkan KKM
- Menyimpan laporan ke `output/laporan.txt`

## Cara Menjalankan

Prasyarat: Python 3 (tanpa library tambahan).

```bash
# 1. Pastikan Python aktif
python3 --version

# 2. Jalankan dengan data contoh (KKM default 75)
python3 src/main.py

# 3. Opsi: file lain dan KKM sendiri
python3 src/main.py data/nilai_contoh.txt --kkm 70

# 4. Uji validasi dengan data yang sengaja salah
python3 src/main.py data/nilai_ada_invalid.txt
```

Di Windows, gunakan `python` atau `py` jika `python3` tidak dikenali.

**Format file nilai:** satu siswa per baris, `NIM,Nama,Nilai`. Baris kosong dan baris berawalan `#` diabaikan.

## Cara Menjalankan Test

```bash
python3 tests/test_program.py
```

Daftar test case (13 kasus: normal, batas, invalid) ada di [`tests/test_case.md`](tests/test_case.md).

## Contoh Output

```text
============================================
LAPORAN REKAP NILAI MATEMATIKA KELAS
============================================
KKM                : 75
Jumlah data valid  : 10
Rata-rata          : 71.30
Nilai minimum      : 0.00
Nilai maksimum     : 100.00
Jumlah tuntas      : 6
Jumlah belum tuntas: 4
--------------------------------------------
NIM     Nama            Nilai  Status
A001    Ayu             85.00  Tuntas
A002    Budi            78.00  Tuntas
A003    Citra           92.00  Tuntas
A004    Dimas           60.00  Belum Tuntas
A005    Eka             75.00  Tuntas
A006    Fajar          100.00  Tuntas
A007    Gita             0.00  Belum Tuntas
A008    Hana            68.00  Belum Tuntas
A009    Indra           81.00  Tuntas
A010    Jaya            74.00  Belum Tuntas
============================================
```

## Struktur Folder

```text
proyek-akhir-masya-bantani/
|-- README.md
|-- proposal.md
|-- .gitignore
|-- data/
|   |-- nilai_contoh.txt
|   `-- nilai_ada_invalid.txt
|-- src/
|   |-- main.py        # mengatur alur program
|   |-- data_io.py     # baca file, simpan laporan
|   |-- analisis.py    # statistik dan ketuntasan
|   `-- utilitas.py    # validasi, konversi, format laporan
|-- tests/
|   |-- test_case.md
|   `-- test_program.py
`-- output/
    `-- .gitkeep
```

## Exit Ticket

### Penilaian Diri

- [x] Saya dapat menjelaskan masalah proyek dalam 2–3 kalimat.
- [x] Saya dapat menjelaskan pengguna dan manfaat program.
- [x] Saya dapat menunjukkan hubungan kebutuhan → IPO → fungsi → test case.
- [x] Saya dapat menjelaskan struktur folder dan pembagian modul.
- [x] Saya memahami kontribusi saya pada proyek ini.
- [x] Saya dapat menunjukkan commit rancangan di GitHub.

### Refleksi

- Bagian rancangan yang paling siap adalah **kebutuhan dan IPO**, karena fitur wajib F01–F05 sudah terhubung ke fungsi dan test case, serta sudah dibuktikan lewat 12 uji otomatis yang lulus.
- Bagian yang masih berisiko adalah **fitur tambahan F06 (statistik per kategori)** yang belum dirancang, dan **format input** yang hanya mendukung file teks dengan pemisah koma. Data dari Excel/CSV dengan format lain belum dicoba.
- Test case yang paling penting adalah **TC04 (nilai 105 ditolak)** karena validasi rentang 0–100 adalah inti kebenaran data. Jika nilai salah lolos, seluruh statistik dan status ketuntasan ikut salah.
- Target pribadi sebelum Pertemuan 15 adalah memeriksa kembali semua test case di VS Code, mencoba data dengan KKM berbeda, merapikan README, dan memastikan commit di GitHub bertahap serta bermakna.

## Catatan

Bantuan AI digunakan dalam penyusunan rancangan dan draf kode. Seluruh isi proyek sudah dipelajari dan dapat dijelaskan sendiri.
