
def hitung_daya(voltase, arus):
    """Menghitung daya listrik (Watt) = Voltase (Volt) x Arus (Ampere)."""
    return voltase * arus


def kategori_konsumsi(daya):
    """Menentukan kategori konsumsi berdasarkan nilai daya (Watt)."""
    if daya < 10:
        return "Hemat (Low Power)"
    elif daya <= 50:
        return "Normal"
    else:
        return "Tinggi (High Power - Perlu Heatsink)"