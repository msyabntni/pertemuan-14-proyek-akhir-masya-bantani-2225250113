"""Program Rekap dan Analisis Nilai Matematika Kelas (console).

Contoh:
    python3 src/main.py
    python3 src/main.py data/nilai_contoh.txt --kkm 75
"""
import argparse
from pathlib import Path

from analisis import hitung_ketuntasan, hitung_statistik
from data_io import baca_data, simpan_laporan
from utilitas import susun_laporan, validasi_nilai

ROOT = Path(__file__).resolve().parent.parent
PATH_DATA = ROOT / "data" / "nilai_contoh.txt"
PATH_LAPORAN = ROOT / "output" / "laporan.txt"
KKM_DEFAULT = 75


def main(argv=None):
    parser = argparse.ArgumentParser(description="Rekap dan analisis nilai kelas")
    parser.add_argument("path", nargs="?", default=str(PATH_DATA), help="file nilai")
    parser.add_argument("--kkm", type=float, default=KKM_DEFAULT, help="nilai KKM")
    parser.add_argument("--output", default=str(PATH_LAPORAN), help="file laporan")
    args = parser.parse_args(argv)

    if not validasi_nilai(args.kkm):
        print("Kesalahan: KKM harus berada pada rentang 0-100.")
        return 1

    try:
        data, daftar_error = baca_data(args.path)
    except FileNotFoundError:
        print(f"Kesalahan: file '{args.path}' tidak ditemukan.")
        return 1

    if not data:
        print("Tidak ada data valid yang dapat dianalisis.")
        for pesan in daftar_error:
            print(f"  - {pesan}")
        return 1

    statistik = hitung_statistik(data)
    ketuntasan = hitung_ketuntasan(data, args.kkm)
    laporan = susun_laporan(data, statistik, ketuntasan, args.kkm, daftar_error)
    print(laporan)
    simpan_laporan(laporan, args.output)
    print(f"\nLaporan disimpan di: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
