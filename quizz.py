kendaraan = input("masukan nama kendaraan(motor/mobil):")
jenisbensin = input("masukan jenis bensin(pertalite,pertamax,pertamax turbo):")
tujuan = input("masukan kota tujuan(jakarta,bekasi,depok,tangerang,bogor): ")

if jenisbensin == "pertalite":
    harga_liter = 10000
    jarak_tempuh = 12
elif jenisbensin == "pertamax":
    harga_liter = 14000
    jarak_tempuh = 13

elif jenisbensin == "pertamax turbo":
    harga_liter = 17000
    jarak_tempuh = 13.5

else:
    print("tidak tersedia")

if tujuan == "jakarta":
    jarak_kota = 20

elif tujuan == "bogor":
    jarak_kota = 120.6

elif tujuan == "bekasi":
    jarak_kota = 75

elif tujuan == "tangerang":
    jarak_kota = 99

elif tujuan == "depok":
    jarak_kota = 5
#else:
#   print("kota tidak tersedia")
#   exit()
pemakaian_bensin = jarak_kota / jarak_tempuh
total_harga = pemakaian_bensin * harga_liter

print("nama kendaraan=",kendaraan)
print("jenisbensin",jenisbensin)
print("kotadituju",tujuan)
print("pemakaianbensin","{:,.2f}".format(pemakaian_bensin), "liter")
print("totalhargaperbensin","{:,.2f}".format(total_harga),"rupiah")

