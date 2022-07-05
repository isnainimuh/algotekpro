'''
# 1. cara membuat string
data = 'ini adalah teks'

print (data)
print (type(data))

print ('"Ayo belajar bersama!"')
print ("'Selamat belajar python'")

print (""Ayo coba lagi"")
'''
'''
print ("Indonesia \tmerdeka")
print ("Indonesia \bmerdeka")
print ("Indonesia \nmerdeka")
'''
'''

# 1. menggabung string
nama1 = "Algoritma"
nama2 = "Teknik"
nama3 = "Pemrograman"
namalengkap = nama1 + ' & ' + nama2 + ' ' + nama3
print (namalengkap)

print (len(namalengkap))

d = 'd'
status = d in namalengkap
print (d, " ada di ", namalengkap, " = ", status)

l = 'l'
status = l in namalengkap
print (l, " ada di ", namalengkap, " = ", status)

status = d not in namalengkap
print (d, " ada di ", namalengkap, " = ", status)
'''
'''
namalengkap = "Algoritma & Teknik Pemrograman"

print ("paling kecil = ", min(namalengkap))

print ("paling besar = ", max(namalengkap))

'''


'''
print ("index ke-0 : ", namalengkap[0])
print ("index ke-6 : ", namalengkap[6])
print ("index ke-(-1) : ", namalengkap[-1])
print ("index ke-(-5) : ", namalengkap[-5])
print ("index ke-[0-4] : ", namalengkap[0:4])
print ("index ke-[3-10] : ", namalengkap[3:10])
print ("index ke-[0,2,4,6,8,10] : ", namalengkap[0:11:2])
'''
'''
ascii_spasi = ord(" ")
print("Kode ascii dari spasi = ", ascii_spasi)

print("Kode ascii dari 'A' = ", ord('A'))
print("Kode ascii dari 'Z' = ", ord('Z'))
print("Kode ascii dari 'a' = ", ord('a'))
print("Kode ascii dari 'z' = ", ord('z'))

data = 117
print("char untuk ASCII 117 adalah ", chr(data))
karakter = 89
print("char untuk ASCII 89 adalah ", chr(karakter))

teks = "Indonesia Tanah Air Beta"
print ("Jumlah huruf a pada teks di atas = ", teks.count('a'))
print ("JUmlah huruf t pada teks di atas = ", teks.count('t'))

myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

x = " ".join(myTuple)
print(x)


txt = "I like bananas"
print(txt)

x = txt.replace("bananas", "apples")
print(x)

x = txt.replace("a", "i")
print(x)

#setiap elemen dipisahkan oleh koma dan spasi ", "
txt = "apple, banana, cherry"

x = txt.rsplit(", ")
print(x)

txt = "Indonesia tanah air beta"
print (txt.split())
'''


# nomor 1
kata1=input("Masukkan teks 1= ")
print (kata1)
kata2=input("Masukkan teks 2= ")
print (kata2)

kata3=kata1+" "+kata2
print ("Hasil gabungan = ", kata3)

#nomor 2
kata=input("Masukkan kalimat = ")
print ("Panjang karakter = ", len(kata))

#nomor 3
kalimat="Indonesia Merdeka"
print(kalimat)
subkalimat=kalimat[0:10]
print (subkalimat)

#nomor 4
kal = input("Masukkan kalimat = ")
print (kal)
cek = input("Masukkan karakter yg akan dicek = ")
sum=0
for i in kal :
    if i==cek :
        sum=sum+1

print ("Jumlah karakter ", cek, " adalah ", sum)

#nomor 5
print ("Perhitungan Pembelian Motor")
print()
print ("Pilih motor yang akan dibeli : ")
print ("1. Vixion")
print ("2. Honda CBR")
motor=int(input("Masukkan jenis motor : "))

print ("Pilih metode pembayaran : ")
print ("1. Tunai")
print ("2. Kredit")
bayar=int(input("Masukkan jenis pembayaran : "))

if motor==1 and bayar==1 :
    print ("Harga motor = Rp 24.500.000,-")
    print ("Silakan bayar tunai, Terima kasih!")
elif motor==2 and bayar==1 :
    print ("Harga motor = Rp 70.000.000,-")
    print ("Silakan bayar tunai, Terima kasih!")
elif motor==1 and bayar==2 :
    dp=int(input("Masukkan jumlah uang muka : "))
    jangka=int(input("Masukkan jangka pembayaran : "))
    bunga=0.01*(24500000-dp)
    pokok=(24500000-dp)/jangka
    cicilan=pokok+bunga
    total=dp+(cicilan*jangka)
    print ("Harga motor = Rp 24.500.000")
    print ("Uang muka = ", dp)
    print ("Jangka pembayaran = ", jangka)
    print ("Angsuran pokok = ", pokok)
    print ("Bunga per bulan = ", bunga)
    print ("cicilan per bulan = ", cicilan)
    print ("Total bayar = ", total)
elif motor==2 and bayar==2 :
    dp=int(input("Masukkan jumlah uang muka : "))
    jangka=int(input("Masukkan jangka pembayaran : "))
    bunga=0.01*(70000000-dp)
    pokok=(70000000-dp)/jangka
    cicilan=pokok+bunga
    total=dp+(cicilan*jangka)
    print ("Harga motor = Rp 70.000.000")
    print ("Uang muka = ", dp)
    print ("Jangka pembayaran = ", jangka)
    print ("Angsuran pokok = ", pokok)
    print ("Bunga per bulan = ", bunga)
    print ("cicilan per bulan = ", cicilan)
    print ("Total bayar = ", total)
else :
    print ("Invalid Input!!")


