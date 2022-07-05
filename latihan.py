'''
#NO 1
celcius = float(input("Masukkan celcius: "))
fahrenheit = celcius * 1.8 + 32
print("Fahrenheit : ", fahrenheit)

#No 2
PHI = 3.14
jari2 = float(input("Masukkan jari-jari: "))
tinggi = float(input("Masukkan tinggi: "))
volume = PHI * jari2 * jari2 * tinggi
print("Volume= ", volume)


#No 3
#input meter
meter=float(input("Masukkan satuan meter: "))

#proses konversi
kaki=meter/0.3048
inchi=meter/0.0254
yard=meter/0.9144

#cetak hasil
print (meter, " meter = ", kaki, " kaki")
print (meter, " meter = ", inchi, " inchi")
print (meter, " meter = ", yard, " yard")


#konversi detik ke hari, jam, menit, detik
detik_input=int(input("Masukkan waktu dalam detik: "))

#proses konversi
hari = detik_input // 86400
jam = detik_input % 86400 // 3600
menit = detik_input % 86400 % 3600 // 60
detik = detik_input % 86400 % 3600 % 60

#cetak hasilnya
print("Waktu ", detik_input, " detik setara dengan ", hari, "hari", jam, "jam", menit,"menit",detik,"detik")



a = 5
b = 7
print("Nilai awal a=", a, "b=",b)
c = a
a = b
b = c
print("Nilai akhir a=", a, "b=",b)


nama=input("Masukkan nama= ")
gapok=float(input("Masukkan gaji pokok= "))
tunjangan=gapok*0.2
pajak=gapok*0.11
gaji_bersih=gapok + tunjangan - pajak
print("Nama : ", nama)
print("Gaji pokok: ", gapok)
print("Tunjangan : ", tunjangan)
print("Pajak : ", pajak)
print("Gaji bersih : ", gaji_bersih)




x1 = int(input("Masukkan titik P1 (x1): "))
y1 = int(input("Masukkan titik P1 (y1): "))
x2 = int(input("Masukkan titik P2 (x2): "))
y2 = int(input("Masukkan titik P2 (y2): "))
x3 = (x1+x2)/2
y3 = (y1+y2)/2
print("Titik tengah P3 adalah (", x3, ",", y3,")")




tinggi = int(input("Masukkan tinggi badan (dalam cm)= "))
bb_ideal = tinggi - 100 - ((tinggi - 100) * 0.1)
print ("Berat badan ideal untuk tinggi", tinggi, "cm adalah", bb_ideal, "kg")
print (f'askdaksjnaknasndasjnaj {tinggi} ajdnjkadjajfbasf {bb_ideal} ajnsajdaj')



jari=float(input("Masukkan jari-jari="))
tinggi=int(input("Masukkan tinggi="))
volume=3.14*jari*jari*tinggi
volume=volume/1000
waktu=volume/0.25
print(f"Waktu yg dibutuhkan untuk mengisi ember adalah {waktu} detik")


gapok = 5000000
kos = 500000
laundry=int(input("Biaya laudry : "))
makan=int(input("Biaya makan: "))
pulsa=int(input("Biaya pulsa: "))
takterduga=int(input("Biaya tak terduga: "))
entertain=int(input("Persentase entertain: "))
sisa=gapok-kos-laundry-makan-pulsa-takterduga
entertain=entertain/100*sisa
sisa=sisa- entertain
print("Gapok = ", gapok)
print("Laundry = ", laundry)
print("Makan = ", makan)
print("Biaya tak terduga = ", takterduga)
print("Entertain = ", entertain)
print("Sisa gaji = ", sisa)



usia = int(input("Masukkan usia: "))

if  0 <= usia <= 5:
    print("Toddler")
elif 6 <= usia <= 12:
    print("Kids")
elif 13 <= usia <= 20:
    print("Teenager")
elif 21 <= usia <= 40:
    print("Young")
elif 41 <= usia <= 60:
    print("Adult")
elif 60 <= usia <=120:
    print("Old")
else:
    print("Invalid Input")



operand1 = int(input("Masukkan bilangan 1= " ))
operator = input("Masukkan operator= ")
operand2 = int(input("Masukkan bilangan 2= "))

if operator=='*':
    hasil=operand1*operand2
elif operator=='/':
    hasil=operand1/operand2
elif operator=='+':
    hasil=operand1+operand2
elif operator=='-':
    hasil=operand1-operand2
else:
    hasil="Invalid input"

print("Hasil = ", hasil)

jumlah_beli = int(input("Berapa donat yang dibeli? "))
total = 10000*jumlah_beli
print("Total awal = ", total)
kelipatan=jumlah_beli//6
if kelipatan>0 :
    total = total - (kelipatan*10000)
print("Total akhir = ", total)


#jawaban tugas pemilihan nomor 1
print("1.Supreme Deluxe : Rp 139300")
print("2.Meat Lovers : Rp 145000")
print("3.Cheesy Mayo : Rp 123799")

jenis=int(input("Pilih jenis pizza yang mau dibeli: "))
jumlah=int(input("Masukkan jumlah pizza yang dibeli: "))

if jenis==1:
    harga=139300
    nama="Supreme Deluxe"
elif jenis==2:
    harga=145000
    nama="Meat Lovers"
elif jenis==3:
    harga=123799
    nama="Cheesy Mayo"
else:
    harga=0
    nama="Invalid input"

total=harga*jumlah
ppn=0.1*total
total_bayar=total+ppn
print(f"Rincian total harga Rp {total} plus PPN 10% Rp {ppn} ")
print(f"Pembelian {jumlah} pizza jenis {nama} total bayar Rp {total_bayar}")


#jawaban soal nomor 2
nilai1=input("Masukkan nilai matkul ke-1: ")
nilai2=input("Masukkan nilai matkul ke-2: ")
nilai3=input("Masukkan nilai matkul ke-3: ")
nilai4=input("Masukkan nilai matkul ke-4: ")
nilai5=input("Masukkan nilai matkul ke-5: ")

if nilai1=='A' or nilai1=='a':
    skor1=4
elif nilai1=='B' or nilai1=='b':
    skor1=3
elif nilai1=='C' or nilai1=='c':
    skor1=2
elif nilai1=='D' or nilai1=='d':
    skor1=1
elif nilai1=='E' or nilai1=='e':
    skor1=0
else:
    print("Invalid Input!")


if nilai2=='A' or nilai2=='a':
    skor2=4
elif nilai2=='B' or nilai2=='b':
    skor2=3
elif nilai2=='C' or nilai2=='c':
    skor2=2
elif nilai2=='D' or nilai2=='d':
    skor2=1
elif nilai2=='E' or nilai2=='e':
    skor2=0
else:
    print("Invalid Input!")


if nilai3=='A' or nilai3=='a':
    skor3=4
elif nilai3=='B' or nilai3=='b':
    skor3=3
elif nilai3=='C' or nilai3=='c':
    skor3=2
elif nilai3=='D' or nilai3=='d':
    skor3=1
elif nilai3=='E' or nilai3=='e':
    skor3=0
else:
    print("Invalid Input!")


if nilai4=='A' or nilai4=='a':
    skor4=4
elif nilai4=='B' or nilai4=='b':
    skor4=3
elif nilai4=='C' or nilai4=='c':
    skor4=2
elif nilai4=='D' or nilai4=='d':
    skor4=1
elif nilai4=='E' or nilai4=='e':
    skor4=0
else:
    print("Invalid Input!")


if nilai5=='A' or nilai5=='a':
    skor5=4
elif nilai5=='B' or nilai5=='b':
    skor5=3
elif nilai5=='C' or nilai5=='c':
    skor5=2
elif nilai5=='D' or nilai5=='d':
    skor5=1
elif nilai5=='E' or nilai5=='e':
    skor5=0
else:
    print("Invalid Input!")


total_nilai=(skor1*3)+(skor2*3)+(skor3*3)+(skor4*3)+(skor5*3)
total_sks=3*5
IP=total_nilai/total_sks
print(f"Nilai IP mahasiswa tersebut adalah {IP}")


n=int(input("Masukkan nilai N: "))

for i in range(n):
    print("Wow aku suka pemrograman")

sum = 1
n=int(input("Masukkan nilai n: "))

for i in range(1,n+1):
    sum = sum * i

print("Hasil = ", sum)

# 1,3,5,7 dst...

for i in range(100):
    if i%2!=0:
        print(i, end=' ')



sum = 1

n=int(input("Masukkan nilai N: "))

for i in range(1,n+1,1):
    sum = sum * i

print("Hasil = ", sum)



for i in range(1,100,2):
    print(i, end=' ')


import matplotlib.pyplot as plt
import numpy as np

xpoints = [0, 6]
ypoints = [0, 250]

plt.plot(xpoints, ypoints)
plt.show()

'''

#Jawaban tugas pengulangan 
#nomor 1
'''
n=int(input("Anak ayam turun: "))

for i in range(n,0,-1):
    if i!=1 :
        print(f"Anak ayam turun {i}, mati satu tinggallah {i-1}")
    else:
        print(f"Anak ayam turun {i}, mati satu tinggal induknya")


#nomor 2
for i in range(50,100):
    if i%2!=0:
        print(i, end=' ')


for i in range(1900, 2021):
    if i%100==0 :
        if i%400==0:
            print(i, end=' ')
    elif i%4==0:
        print(i, end=' ')

#nomor 4
for i in range(100,200):
    if i%7==0 and i%9==0:
        print(i, end=' ')'''
'''
#nomor 5
n=int(input("Masukkan nlai n: "))
bil1=1
bil2=1
for i in range(n):
    temp = bil1
    bil1 = bil2
    bil2 = temp + bil1
    print(temp, end=' ')






print ("Tahun Kabisat : ")
tahun_awal = int(input('Tahun awal:'))
tahun_akhir = int(input('Tahun akhir: '))
for kabisat in range (tahun_awal,tahun_akhir+1):
    if kabisat % 100==0 and kabisat%400==0:
        print(kabisat, end=' ')
    elif kabisat % 4 == 0 : 
        print (kabisat,end =" " )
    

nilai=[]

for i in range(5):
    data=input(f"Masukkan nilai ke-{i+1}:")
    nilai.append(data)

skor=[]
for i in range(5):
    if nilai[i]=='A':
        data=4
    elif nilai[i]=='B':
        data=3
    elif nilai[i]=='C':
        data=2
    elif nilai[i]=='D':
        data=1
    else:
        data=0
    skor.append(data)

sum=0
for i in range(5):
    sum = sum + (skor[i]*3)

totalsks=3*5

IP=sum/totalsks
print("IP= ", IP)


#tugas list
#no 1
nilai=[]
sum=0
n=int(input('Masukkan nilai n: '))
for i in range(n):
    temp=int(input(f'Masukkan nilai ke-{i+1} : '))
    nilai.append(temp)
    sum=sum + temp

rata=sum/n
minim=nilai[0]
maxim=nilai[0]
for i in range(n):
    if nilai[i] < minim :
        minim = nilai[i]
    if nilai[i] > maxim :
        maxim = nilai[i]

for i in nilai:
    print(i, end=' ')
print()
print("Rata-rata: ", rata)
print("Nilai min: ", minim)
print("Nilai max: ", maxim)

kota=[]
for i in range(5):
    data=input(f'Masukkan nama kota ke-{i+1} : ')
    kota.append(data)

kota.sort()
print(kota)


n=int(input("Masukkan sejumlah uang = Rp "))
uang=[100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]
jumlah=[]
for i in range(10):
    temp=n//uang[i]
    sisa=n%uang[i]
    n=sisa
    if temp!=0:
        jumlah.append(temp)
    else:
        jumlah.append(0)

print("Uang tersebut terdiri dari : ")
for i in range(10):
    if jumlah[i]!=0:
        print(f"{jumlah[i]} unit uang senilai {uang[i]}")


#JAWABAN TUGAS NESTED FOR
#NO 1
for i in range(10,0,-1):
    for j in range(i,0,-1):
        print(j, end=' ')
    print()

#no 2
for i in range(1,10):
    for j in range(9,i-1,-1):
        print(' ', end = ' ')
    for k in range(2*i-1):
        print(i, end=' ')
    print()

#no 3
p=int(input('Masukkan panjang: '))
l=int(input('Masukkan lebar: '))
for i in range(l):
    for j in range(p):
        print('*', end=' ')
    print()


#no 4
a=0
b=2
c=0
for i in range(1,6):
    for j in range(9, a, -1):
        print(' ', end='')
    a += 2
    for k in range(1, b):
        print('*', end='')
    for l in range(17,c,-1):
        print(' ', end='')
    c += 4
    for m in range(1, b):
        print('*', end='')
    b += 4
    print()

y=0
x=0
for i in range(10):
    for j in range(0, y):
        print(' ', end='')
    y += 2
    for k in range(37, x, -1):
        print('*', end='')
    x += 4
    print()



kalimat="Belajar butuh usaha keras"

p=len(kalimat)
for i in range(p):
    if i!=p-1:
        if kalimat[i+1]==' ': 
            print('',end='')
        else:
            print(kalimat[i], end='')
    else:
        print('', end='')


from math import sqrt

a=int(input("Nilai a: "))
b=int(input("Nilai b: "))
c=int(input("Nilai c: "))

diskriminan=b**2 - 4*a*c
print("D = ", diskriminan)
if diskriminan<0:
    print('Akar imajiner')
elif diskriminan>0:
    x1=(-b + sqrt(diskriminan))/2
    x2=(-b - sqrt(diskriminan))/2
    print("x1 = ", x1, "x2 = ", x2)
else:
    x1=(-b + sqrt(diskriminan))/2
    x2=x1
    print("x1 = ", x1, "x2 = ", x2)



print('Tahun penyelenggaraan Thomas Cup:')
x = 3
tahun = 1949
while (tahun < 2021):
    print(tahun, end=' ')
    tahun += x
    if tahun==1982:
        x = 2


pem1=int(input("Pembilang p1: "))
pen1=int(input("Penyebut p1: "))
pem2=int(input("Pembilang p2: "))
pen2=int(input("Penyebut p2: "))

if (pen1 != pen2):
    pem_jumlah=(pem1*pen2)+(pem2*pen1)
    pen_jumlah=(pen1*pen2)
    pem_kurang=(pem1*pen2)-(pem2*pen1)
    pen_kurang=pen_jumlah
else:
    pem_jumlah=pem1+pem2
    pem_kurang=pem1-pem2

pem_kali=pem1*pem2
pen_kali=pen1*pen2

pem_bagi=pem1*pen2
pen_bagi=pem2*pen1

print(f"Hasil {pem1}/{pen1} + {pem2}/{pen2} = {pem_jumlah}/{pen_jumlah}")
print(f"Hasil {pem1}/{pen1} - {pem2}/{pen2} = {pem_kurang}/{pen_kurang}")
print(f"Hasil {pem1}/{pen1} * {pem2}/{pen2} = {pem_kali}/{pen_kali}")
print(f"Hasil {pem1}/{pen1} / {pem2}/{pen2} = {pem_bagi}/{pen_bagi}")



n=int(input("Masukkan tahun prediksi: "))
penduduk=270000000
for i in range(2020, n):
    penduduk = penduduk + (penduduk * 0.0112)

print(f'Jumlah penduduk Indonesia pada tahun {n} adalah {penduduk}')


bil1=0
bil2=1
fibo=[]
for i in range(10):
    temp = bil1
    bil1 = bil2
    bil2 = temp + bil1
    fibo.append(temp)
print(fibo)

for i in range(1,51):
    if i not in fibo:
        print(i, end=' ')

import math
x = int(input("Masukkan jumlah pinjaman : "))
n = int(input("Masukkan angsuran pada bulan n : "))
i = float(input("Masukkan bunga pertahun dalam % : "))
y = int(input("Masukkan jangka waktu kredit (bulan): "))

angsuran_pokok=x/y
for iteration in range(n):
    bunga=x*i/100*(30/360)
    cicilan=angsuran_pokok+bunga
    x=x-angsuran_pokok

print(f"Bunga bulan ke {n}: {bunga}")
print(f"Cicilan bulan ke {n}: {cicilan}")


pem1=int(input("masukkan pem1 : "))
pen1=int(input("masukkan pen1 : "))
pem2=int(input("masukkan pem2 : "))
pen2=int(input("masukkan pen2 : "))
if (pen1==pen2):
    jumlah=pem1+pem2
    kurang=pem1-pem2
    pen=pen1
else:
    pen=pen1*pen2
    jumlah=(pem1*pen2)+(pem2*pen1)
    kurang=(pem1*pen2)-(pem2*pen1)
print(f'Hasil penjumlahan {pem1}/{pen1} + {pem2}/{pen2} = {jumlah}/{pen}')
print(f'Hasil pengurangan {pem1}/{pen1} - {pem2}/{pen2} = {kurang}/{pen}')

pem_kali=pem1*pem2
pen_kali=pen1*pen2

pem_bagi=pem1*pen2
pen_bagi=pem2*pen1

print(f'Hasil perkalian {pem1}/{pen1} * {pem2}/{pen2} = {pem_kali}/{pen_kali}')
print(f'Hasil pembagian {pem1}/{pen1} / {pem2}/{pen2} = {pem_bagi}/{pen_bagi}')


fibonaci=[0,1,2,3,5,8,13,21,34]
data=[]
for i in range(1,51):
    if i not in fibonaci:
        print(i, end=' ')


n = int(input("masukkan tahun : "))
penduduk=270
for i in range(2020, n):
    penduduk = penduduk + (penduduk*0.0112)

print(f"jadi penduduk Indonesia pada tahun {n} adalah {penduduk} juta jiwa ")

#awal
pecahan=[1000,900,500,400,100,90,50, 40,10,9,5,4,1]
romawi=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']

desimal=int(input('Masukkan bil desimal: '))
hasil=''
while(desimal > 0) :
    for i in range(len(pecahan)):
        if desimal>=pecahan[i]:
            hasil += romawi[i]
        desimal %= pecahan[i]

print("Hasil= ", hasil)


#perbaikan
pecahan=[1000,900,500,400,100,90,50, 40,10,9,5,4,1]
romawi=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']

desimal=int(input('Masukkan bil desimal: '))
hasil=''
while(desimal > 0) :
    for i in range(len(pecahan)):
        if desimal>=pecahan[i]:
            if pecahan[i]==100 or pecahan[i]==10 or pecahan[i]==1:
                hasil += romawi[i] * (desimal//pecahan[i])
            else:
                hasil += romawi[i]
        desimal %= pecahan[i]

print("Hasil= ", hasil)

import math
print('KPR rumah senilai Rp 500.000.000,-')
dp = int(input("Masukkan DP (min 10%): "))
n = int(input("Masukkan bulan yang ditanyakan (n) : "))
i = float(input("Masukkan bunga pertahun dalam % : "))
y = int(input("Masukkan jangka waktu kredit (dalam tahun): "))

hutang = 500000000 - (dp/100*500000000)
angsuran_pokok=hutang/(y*12)
for iteration in range(n):
    bunga=hutang*i/100*(30/360)
    cicilan=angsuran_pokok+bunga
    hutang -= angsuran_pokok

print(f"Bunga bulan ke {n}: {bunga}")
print(f"Angsuran pokok : {angsuran_pokok}")
print(f"Cicilan bulan ke {n}: {cicilan}")

'''
'''
for i in range(1,11):
    for j in range(10,i-1,-1):
        print(i, end=' ')
    print()
'''
'''for i in range(10,0,-1):
    for j in range(i,11):
        print(j, end=' ')
    print()'''
'''
from random import randint

matrixA = []
matrixB = []


a = int(input('banyak baris matriks a: '))
b = int(input('banyak kolom matriks b: '))
c = int(input('banyak kolom matriks a atau baris matriks b: '))


for i in range(a):
    baris = []
    for j in range(c):
        acak = randint(1, 5)
        baris.append(acak)
    matrixA.append(baris)

print('Matriks A:')
for i in range(a):
    for j in range(c):
        print(matrixA[i][j], end= ' ')
    print()

for i in range(c):
    baris = []
    for j in range(b):
        acak = randint(1, 5)
        baris.append(acak)
    matrixB.append(baris)

print('Matriks B:')
for i in range(c):
    for j in range(b):
        print(matrixB[i][j], end= ' ')
    print()

total = [[0 for i in range(a)] for j in range(b)]


for i in range(a):
    for j in range(b):
        for k in range(c):
            total[i][j] = total[i][j] + matrixA[i][j] * matrixB[i][j]

print('Hasil : ')
for i in range(a):
    for j in range(b):
        print(total[i][j], end=" ")
    print()'''

#jawaban tugas fungsi

'''def lastday(hari):
    days=['senin','selasa','rabu','kamis','jumat','sabtu','minggu']
    if hari in days:
        x=days.index(hari)
        print(days[x-1])
    else:
        print('hari tidak dikenali')

lastday('senin')

def pangkat(n, y):
    sum=1
    for i in range(y):
        sum = sum * n
    return sum

print(pangkat(5,3))

def urut(data):
    hasil=[]
    for i in range(5):
        minim=data[0]
        for each in data:
            if minim>each:
                minim=each
        hasil.append(minim)
        data.remove(minim)
    return hasil

nomor=[23,11,46,52,8]
print(urut(nomor))

def faktorial(n):
    sum=1
    for index in range(1, n+1):
        sum *= index
    return sum

print(faktorial(5))

def cekpitagoras(a,b,c):
    if a*a + b*b - c*c == 0:
        print(True)
    elif b*b + c*c - a*a == 0:
        print(True)
    elif a*a + c*c - b*b == 0:
        print(True)
    else:
        print(False)
    
cekpitagoras(13,6,12)'''

'''
mat=[[1,2,3,4],[2,6,7,8],[3,7,11,12],[4,8,12,15]]

#bagaimana ngecek baris == kolom
if len(mat) == len(mat[0]):
    cek=True
    print('bujur sangkar')
else:
    print('bukan bujur sangkar')

cekSimetri=True
if cek==True:
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]!=mat[j][i]:
                cekSimetri=False
                
if cekSimetri==False:
    print('Bukan matriks simetri')
else:
    print('Matriks Simetri')'''

'''def cekpitagoras(a,b,c):
    if a*a + b*b - c*c == 0:
        print(True)
    elif b*b + c*c - a*a == 0:
        print(True)
    elif a*a + c*c - b*b == 0:
        print(True)
    else:
        print(False)
   
cekpitagoras(13,5,12)'''

'''
def urut(list):

    for j in range(len(list)-1, 0, -1):

        for i in range(j):

            if list[i] > list[i+1]:

                list[i], list[i+1] = list[i+1], list[i]

    return list



list = []

banyak = int(input("masukan jumlah inputan : "))

for i in range(banyak):

    inputan = int(input("masukan angka list :"))

    list.append(inputan)

print("sorted list", urut(list))'''

'''
#variabel angka di matriks
a11=8
a12=2
a13=8
a21=-1
a22=-1
a23=8
a31=1
a32=8
a33=6
print()
#Mengecek bentuk Matriks
print(a11,a12,a13)
print(a21,a22,a23)
print(a31,a32,a33)
print()
#Masukkan Variabel diatas dalam bentuk Determinan Sarrus
print("metode Det. sarrus :")
print(a11,a12,a13,"|",a11,a12)
print(a21,a22,a23,"|",a21,a22)
print(a31,a32,a33,"|",a31,a32)
#menghitung sesuai dengan rumus Det. Sarrus
H1=(int(a11)*int(a22)*int(a33))
H2=(int(a12)*int(a23)*int(a31))
H3=(int(a13)*int(a21)*int(a32))
H4=(int(a31)*int(a22)*int(a13))
H5=(int(a32)*int(a23)*int(a11))
H6=(int(a33)*int(a21)*int(a12))
HA=int(H1)+int(H2)+int(H3)
HB=int(H4)+int(H5)+int(H6)
HX=int(HA)-int(HB)
print()
print("Hasil metode Det. Sarrus :", HX)
print()

'''


