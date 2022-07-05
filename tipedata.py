from datetime import datetime, timedelta

tanggal_awal = int(input("Masukkan tanggal awal : "))
bulan_awal = int(input("Masukkan bulan awal : "))
tanggal_akhir = int(input("Masukkan tanggal akhir : "))
bulan_akhir = int(input("Masukkan bulan awal : "))

dt_awal = datetime(2020, bulan_awal, tanggal_awal)
dt_akhir = datetime(2020, bulan_akhir, tanggal_akhir)

d = dt_akhir - dt_awal

print("\nJarak antara tanggal {} {} dan {} {} adalah {} hari".format(tanggal_awal,dt_awal.strftime("%B"), tanggal_akhir, dt_akhir.strftime("%B"), d.days))