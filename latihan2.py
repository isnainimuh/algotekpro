'''#input detik awal
detik1=int(input("Masukkan detik = "))

#proses hitung
hari = detik1//86400
jam = detik1%86400//3600
menit = detik1%86400%3600//60
detik = detik1%86400%3600%60

#cetak hasil
print (detik1, " detik = ", hari, " hari,", jam, " jam,", menit, " menit," , detik, " detik")
print (type(hari))'''
import math
'''F1 = int(input("masukkan F1 : "))
F2 = int(input("masukkan F2 : "))
sudutcos = int(input("masukkan cos : "))

if sudutcos != 30 :
    print("Tidak dihitung")
elif sudutcos == 30 :
    R = math.sqrt(F1*F1) + math.sqrt(F2*F2) + math.sqrt(2)*F1*F2*math.cos(math.radians(30))
if sudutcos != 45 :
    print("Tidak dihitung")
elif sudutcos == 45 :
    R = math.sqrt(F1*F1) + math.sqrt(F2*F2) + math.sqrt(2)*F1*F2*math.cos(math.radians(45))
if sudutcos != 60 :
     print("Tidak dihitung")
elif sudutcos == 60 :
     R = math.sqrt(F1*F1) + math.sqrt(F2*F2) + math.sqrt(2*F1*F2*math.cos(math.radians(60)))
if sudutcos != 90 :
   print("Tidak dihitung")
elif sudutcos == 90 :
    R = math.sqrt(F1*F1) + math.sqrt(F2*F2) + math.sqrt(2*F1*F2*math.cos(math.radians(90)))

print("R :", R)'''

'''nama = 'UNIVERSITAS WIJAYA PUTRA'
for i in range(len(nama)):
    for j in range(i+1):
        print(" ", end=' ')
    for k in range(i-0,len(nama)-i):
        print(nama[k], end=' ')
    for l in range(i,len(nama)-i):
        print(" ", end=' ')
    print()

n = int(input("Masukkan n: "))

x = 2*n - 1

for a in range(1, n+1):
    for b in range(1, a+1):
        print(" ", end=' ')
    for c in range(x, 0, -1):
        print("*", end=' ')
    print()
    x=x-2'''

'''teks = input("Masukkan kalimat: ")
jumlah_karakter = len(teks)
print("Panjang karakter = ", jumlah_karakter)'''

'''#input jumlah mangga
jumlah = int(input("Jumlah mangga yg dibeli: "))

#hitung total pembelian
total = jumlah * 5000
print ("Total awal: ", total)

#cek diskon
if total>100000:
    total -= total*0.1

#cetak total akhir
print("Total bayar: ", total)'''

'''bilangan = int(input("Masukkan bilangan: "))

if bilangan%2 != 0:
    print("Ini bilangan ganjil")
else:
    print("Ini bilangan genap")'''

'''#input nilai
nilai = int(input("Masukkan nilai: "))

#cek kategori nilai
if nilai >= 90:
    print("Excellent")
elif 80 <= nilai <=89:
    print("Good Job")
elif 60 <= nilai <=79:
    print("Study Harder")
else:
    print("Sorry, you failed!")'''

'''nama = input("Masukkan nama: ")
gapok = int(input("Masukkan gaji pokok: "))
tunjangan = gapok * 0.2
pajak = gapok * 0.11
gaji_bersih = gapok + tunjangan - pajak
print("Tunjangan: ", tunjangan)
print("Pajak: ", pajak)
print("Gaji bersih: ", gaji_bersih)'''

'''count = 0
while count < 10 :
    print("Aku suka pemrograman")
    count += 1
print("Good bye")'''

'''nilai = [80, 67, 89, 75, 81]

sum = 0
for i in nilai:
    sum = sum + i

print("Jumlah seluruh data: ", sum)
print("Rata-rata nilai: ", sum/len(nilai))'''

'''#ascending
for i in range(100, 125, 2):
    print(i, end=' ')

print()
#descending
for j in range(50, 0, -5):
    print(j, end=' ')'''
