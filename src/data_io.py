"""Membaca data nilai dari file dan menyimpan laporan ke file."""
import os

from utilitas import ubah_ke_angka, validasi_nilai


def baca_data(path):
    """Membaca file berformat NIM,Nama,Nilai.

    Mengembalikan (data, daftar_error).
    data         : {nim: {"nama": str, "nilai": float}} hanya baris valid.
    daftar_error : pesan untuk setiap baris yang ditolak.
    Melempar FileNotFoundError jika file tidak ada (ditangani di main).
    """
    data = {}
    daftar_error = []
    with open(path, "r", encoding="utf-8") as berkas:
        for no, baris in enumerate(berkas, start=1):
            baris = baris.strip()
            if not baris or baris.startswith("#"):
                continue
            kolom = [k.strip() for k in baris.split(",")]
            if len(kolom) != 3 or not kolom[0] or not kolom[1]:
                daftar_error.append(f"Baris {no}: format harus NIM,Nama,Nilai")
                continue
            nim, nama, teks_nilai = kolom
            nilai = ubah_ke_angka(teks_nilai)
            if nilai is None:
                daftar_error.append(f"Baris {no}: nilai '{teks_nilai}' bukan angka")
            elif not validasi_nilai(nilai):
                daftar_error.append(f"Baris {no}: nilai {teks_nilai} di luar 0-100")
            elif nim in data:
                daftar_error.append(f"Baris {no}: NIM {nim} duplikat")
            else:
                data[nim] = {"nama": nama, "nilai": nilai}
    return data, daftar_error


def simpan_laporan(teks, path):
    """Menulis laporan ke file teks; folder dibuat jika belum ada."""
    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(path, "w", encoding="utf-8") as berkas:
        berkas.write(teks + "\n")
    return path
