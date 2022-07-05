'''
#operator penjumlahan
a = 12
b = 7
hasil = a + b
print (a,'+',b,'=', hasil)

#operasi pengurangan
hasil = a - b
print (a,'-',b,'=', hasil)


a = 12
b = 7
#operasi perkalian
hasil = a * b
print (a,'*',b,'=', hasil)

#operasi pembagian
hasil = a / b
print (a,'/',b,'=', hasil)

a = 12
b = 7
#operasi modulus
hasil = a % b
print (a,'%',b,'=', hasil)

a = 10
b = 4
#operasi eksponen (pangkat)
hasil = a ** b
print (a,'**',b,'=', hasil)

a = 12
b = 7
#operasi floor division
hasil = a // b
print (a,'//',b,'=', hasil)

a = 10 
b = 7
c = 7
hasil = a == b
print(a ,'==' ,b,'=', hasil)
hasil = b == c
print(b ,'==' ,c,'=', hasil)
hasil = b != c
print(b ,'!=' ,c,'=', hasil)
hasil = c != a
print(c ,'!=' ,a,'=', hasil)
print (type(hasil))

tgl=int(input("Masukkan tanggal HPHT = "))
bln=int(input("Masukkan bulan HPHT = "))
thn=int(input("Masukkan tahun HPHT = "))
print("Hari Pertama Haid Terakhir = ", tgl,"-",bln,"-",thn)

bln_HPL = 0

if 3 < bln <= 12:
    bln_HPL=bln-3
    thn_HPL = thn + 1
else :
    bln_HPL=bln+9
    thn_HPL = thn

if bln==1 or bln==3 or bln==5 or bln==7 or bln==8 or bln==10 or bln==12 :
    if 1 <= tgl < 25 :
        tgl_HPL = tgl + 7
    elif 25 <= tgl <= 31:
        tgl_HPL = tgl + 7 - 31
        bln_HPL+=1
        if bln_HPL>12 :
            bln_HPL=bln_HPL-12;
            thn_HPL=thn+1;
    else :
        print ("Invalid input")
elif bln==4 or bln==6 or bln==9 or bln==11 :
    if 1 <= tgl < 24 :
        tgl_HPL = tgl + 7
    elif 24 <= tgl <= 30 :
        tgl_HPL = tgl + 7 - 30
        bln_HPL+=1
    else :
        print ("Invalid input")
elif bln==2 :
    if thn%4==0 :
        if 1 <= tgl < 23 :
            tgl_HPL = tgl + 7
        elif 23 <= tgl <= 29 :
            tgl_HPL = tgl + 7 - 29
            bln_HPL+=1
        else :
            print ("Invalid input")
    else :
        if 1 <= tgl < 22 : 
            tgl_HPL = tgl + 7
        elif 22 <= tgl <=28 :
            tgl_HPL = tgl + 7 - 28
            bln_HPL+=1
        else :
            print ("Invalid input")
else :
    print ("Invalid input")

print("Hari Perkiraan Lahir adalah = ",tgl_HPL,"-",bln_HPL,"-",thn_HPL)

'''
'''
des = int(input("desimal = "))

bin = bin(des).replace("0b","")
hex = hex(des).replace("0x","")
print(bin)
print(hex)

a= int(5)
for i in range(a):
    for j in range (i+1):
        print ("*", end="")
    print()
for i in reversed (range(a-1)):
    for j in range (i+1):
        print ("*", end="")
    print ()


jangka=int(input("Jangka cicilan (tahun): "))
print ("Harga pokok : Rp 500.000.000")
print ("Jangka cicilan : ", jangka*12, " bulan")
angsuran=((0.1*500000000*jangka)+500000000)/jangka*12
print ("Angsuran bulanan : Rp ", angsuran)
print ("Total bayar = Rp ", angsuran*jangka*12)
'''
'''
print("========================================================")
print("18. hitung ada berapa hari antara tanggal tersebut ")
print("========================================================")
import datetime
from datetime import date

def OfDays (date1, date2):
    return (date2-date1).days

data = [0, 31, 29, 31, 30, 31, 30,
    31, 31, 30, 31, 30, 31 ]

def CeDay (d,m):
    if d <= m:
        return d
    else:
        print("Tanggal yang anda masukan tidak ada")

def CeMonth (m):
    if m <= 12:
        return m
    else:
        print("Tanggal yang anda masukan tidak ada")
        

print ("Today", datetime.datetime.now())

od1 = int(input("Masukan awal hari DD:"))
op1 = int(input("Masukan awal bulan BB:"))
days1 = CeDay( od1, data[op1] )
mounths1 = CeMonth(op1)
    
od2 = int(input("Masukan awal hari DD:"))
op2 = int(input("Masukan awal bulan BB:"))
days2 = CeDay( od2, data[op2] )
mounths2 = CeMonth(op2)

date1 = date(2020, mounths1, days1)
date2 = date(2020, mounths2, days2)
    
countd = OfDays(date1, date2)
print("========================================================")
print("Jarak antara", od1, date1.strftime("%B"))
print("Sampai dengan", od2, date2.strftime("%B"))
print ("Adalah",countd, "days")
print("========================================================")
'''
listHari = ['rabu','kamis','jumat','sabtu','minggu','senin','selasa']
listJmlhari=[0,31,29,31,30,31,30,31,31,30,31,30,31]
listBulan=['jan','feb','mar','apr','mei','jun','jul','agust','sep','okt','nop','des']
listWeton = ['legi','pahing','pon','wage','kliwon']

hari=input("Masukkan hari : ")
weton=input("Masukkan weton : ")

cek=False
i=0
while cek==False :
    if listHari[i%7]==hari and listWeton[i%5]==weton :
        cek=True
        indexAwal=i
    i=i+1

sum=0
indeks=0
for i in range(indexAwal+1, 366, 35) :
    sum=sum+listJmlhari[indeks]
    tgl=i-sum
    if tgl>listJmlhari[indeks+1] and indeks!=0:
        indeks=indeks+1
        sum=sum+listJmlhari[indeks]
        tgl=i-sum
    print("Tanggal ", tgl, " ", listBulan[indeks], " 2020")
    indeks=indeks+1
    