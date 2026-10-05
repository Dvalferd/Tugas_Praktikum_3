# =============================================================
# SISTEM KALKULASI BIAYA PENGIRIMAN PAKET EKSPIDISI AI-EKSPRESS
# =============================================================

nama_pengirim = input("masukkan nama pengirim : ")
berat_paket = float(input("masukkan berat paket (kg) : "))
jarak_pengiriman = float(input("masukkan jarak pengiriman (km) : "))
jenis_layanan = input("masukkan jenis layanan (reguler/kilat) : ")

# tarif jarak 
if jarak_pengiriman <=50 :
    tarif_per_kg = 50000
elif jarak_pengiriman <= 100:
    tarif_per_kg = 10000
else :
    tarif_per_kg = 15000

# hitung biaya dasar 
biaya_dasar = berat_paket * tarif_per_kg 

# menentukan biaya tambahan berdasarkan jenis layanan
if jenis_layanan.lower() == "kilat":
    biaya_tambahan = biaya_dasar * 0.20
else :
    biaya_tambahan = 0

# menghitung biaya akhir
total_biaya = biaya_dasar + biaya_tambahan

# struk
print("\n--- STRUK PENGIRIMAN ---")
print("Nama Pengirim :", nama_pengirim)
print("berat paket :", berat_paket, "kg")
print("jarak pengiriman :", jarak_pengiriman, "km")
print("jenis layanan :", jenis_layanan)
print("tarif per kg : Rp ", tarif_per_kg )
print("Biaya Dasar       : Rp", biaya_dasar)
print("biaya tambahan  : Rp", biaya_tambahan)
print("========================================")
print("TOTAL BIAYA   : rp", total_biaya)