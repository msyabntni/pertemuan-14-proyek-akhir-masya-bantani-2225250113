"""Logika perhitungan statistik dan ketuntasan."""


def hitung_statistik(data):
    """Menghitung jumlah, rata-rata, minimum, dan maksimum nilai."""
    nilai = [rekam["nilai"] for rekam in data.values()]
    if not nilai:
        raise ValueError("data kosong, statistik tidak dapat dihitung")
    return {
        "jumlah": len(nilai),
        "rata_rata": sum(nilai) / len(nilai),
        "minimum": min(nilai),
        "maksimum": max(nilai),
    }


def tentukan_status(nilai, kkm):
    """'Tuntas' jika nilai >= KKM, selain itu 'Belum Tuntas'."""
    return "Tuntas" if nilai >= kkm else "Belum Tuntas"


def hitung_ketuntasan(data, kkm):
    """Menghitung jumlah tuntas dan belum tuntas berdasarkan KKM."""
    tuntas = sum(
        1 for rekam in data.values() if tentukan_status(rekam["nilai"], kkm) == "Tuntas"
    )
    return {"tuntas": tuntas, "belum_tuntas": len(data) - tuntas}
