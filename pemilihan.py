#no 1
usia=int(input("Masukkan usia = "))

print ("Usia ", usia, " termasuk ", )

if 0 <= usia <= 5 :
    print ("Toddler")
elif 6 <= usia <= 12 :
    print ("Kids")
elif 13 <= usia <= 20 :
    print ("Teenager")
elif 21 <= usia <= 40 :
    print ("Young")
elif 41 <= usia <= 60 :
    print ("Adult")
elif 61 <= usia <=100 :
    print ("Old") 
else:
    print ("Invalid input!")


#no 2
bil1=int(input("Masukkan bilangan 1 = "))
operator=input("Masukkan operator = ")
bil2=int(input("Masukkan bilangan 2 = "))

if operator=='*' :
    hasil=bil1*bil2
elif operator=='/' :
    hasil=bil1/bil2
elif operator=='+' :
    hasil=bil1+bil2
elif operator=='-' :
    hasil=bil1-bil2
else:
    print ("Operator tidak dikenal!")

print (hasil)


#no 3
jml_donat=int(input("Masukkan jumlah donat = "))

if jml_donat>=6 :
    x=jml_donat//6
    potongan=x*10000
else :
    potongan=0

total_donat=jml_donat*10000
total_bayar=total_donat-potongan
print("Total harga = ", total_donat)
print("Potongan = ", potongan)
print("Total bayar = ", total_bayar)



#no 4
print("Menu PIZZA:")
print("1. Supreme Deluxe : Rp 139.300,-")
print("2. Meat Lovers : Rp 145.000,-")
print("3. Cheesy Mayo : Rp 123.799,-")

pilih=int(input("Pilih jenis pizza: "))

if (pilih==1) :
    harga=139300
elif (pilih==2) :
    harga=145000
elif (pilih==3) :
    harga=123799
else :
    print("salah input!")

jumlah=int(input("Jumlah pizza yang dibeli: "))

total_harga=jumlah*harga
ppn=total_harga*0.1
total_bayar=total_harga+ppn

#no 5
nilai1 = int(input("Input nilai 1 : "))
nilai2 = int(input("Input nilai 2 : "))
nilai3 = int(input("Input nilai 3 : "))
nilai4 = int(input("Input nilai 4 : "))
nilai5 = int(input("Input nilai 5 : "))

if (nilai1=='A') :
    bobot1 = 4
elif (nilai1=='B') :
    bobot1 = 3
elif (nilai1=='C') :
    bobot1 = 2
elif (nilai1=='D') :
    bobot1 = 1
elif (nilai1=='E') :
    bobot1 = 0
else :
    print ("Invalid input")

if (nilai2=='A') :
    bobot2 = 4
elif (nilai2=='B') :
    bobot2 = 3
elif (nilai2=='C') :
    bobot2 = 2
elif (nilai2=='D') :
    bobot2 = 1
elif (nilai2=='E') :
    bobot2 = 0
else :
    print ("Invalid input")

jumlah_TK = (bobot1*3)+(bobot2*3)
jumlah_TN = 15
IP = jumlah_TK/jumlah_TN


