
import modul_konversi

garis = "=" * 48

# ===== INPUT =====
print(garis)
print("  KALKULATOR KONSUMSI DAYA PERANGKAT EDGE AI")
print(garis)

nama = input("Masukkan Nama Perangkat AI : ")
voltase = float(input("Masukkan Voltase (Volt)    : "))
arus = float(input("Masukkan Arus (Ampere)     : "))

# ===== PROSES (memanggil fungsi dari modul) =====
daya = modul_konversi.hitung_daya(voltase, arus)
kategori = modul_konversi.kategori_konsumsi(daya)

# ===== OUTPUT =====
print()
print(garis)
print("            HASIL ANALISIS DAYA AI")
print(garis)
print(f"Nama Perangkat   : {nama}")
print(f"Daya Terhitung   : {daya:.2f} Watt")
print(f"Kategori Daya    : {kategori}")
print(garis)