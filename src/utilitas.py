"""Fungsi bantu: konversi, validasi nilai, dan format laporan."""

NILAI_MIN = 0
NILAI_MAX = 100


def ubah_ke_angka(teks):
    """Mengubah teks menjadi float. Mengembalikan None jika bukan angka."""
    try:
        return float(str(teks).strip().replace(",", "."))
    except ValueError:
        return None


def validasi_nilai(nilai):
    """True jika nilai berupa angka pada rentang 0-100 (inklusif)."""
    if isinstance(nilai, bool) or not isinstance(nilai, (int, float)):
        return False
    return NILAI_MIN <= nilai <= NILAI_MAX


def format_angka(angka):
    """Format angka dua desimal untuk tampilan."""
    return f"{angka:.2f}"


def susun_laporan(data, statistik, ketuntasan, kkm, daftar_error):
    """Menyusun teks laporan ringkas dari hasil analisis."""
    baris = [
        "=" * 44,
        "LAPORAN REKAP NILAI MATEMATIKA KELAS",
        "=" * 44,
        f"KKM                : {kkm}",
        f"Jumlah data valid  : {statistik['jumlah']}",
        f"Rata-rata          : {format_angka(statistik['rata_rata'])}",
        f"Nilai minimum      : {format_angka(statistik['minimum'])}",
        f"Nilai maksimum     : {format_angka(statistik['maksimum'])}",
        f"Jumlah tuntas      : {ketuntasan['tuntas']}",
        f"Jumlah belum tuntas: {ketuntasan['belum_tuntas']}",
        "-" * 44,
        f"{'NIM':<8}{'Nama':<14}{'Nilai':>7}  Status",
    ]
    for nim, rekam in data.items():
        status = "Tuntas" if rekam["nilai"] >= kkm else "Belum Tuntas"
        baris.append(
            f"{nim:<8}{rekam['nama']:<14}{format_angka(rekam['nilai']):>7}  {status}"
        )
    if daftar_error:
        baris.append("-" * 44)
        baris.append(f"Baris yang ditolak ({len(daftar_error)}):")
        baris.extend(f"  - {pesan}" for pesan in daftar_error)
    baris.append("=" * 44)
    return "\n".join(baris)
