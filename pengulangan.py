#nomor 1
for i in range(10, 0, -1) :
    if (i!=1) :
        print ("Anak ayam turun ", i, ",mati satu tinggal ", i-1)
    else :
        print ("Anak ayam turun ", i, ",mati satu tinggal induknya")

#nomor 2
for i in range(50,100,1) :
    if (i%2!=0) :
        print (i)

#nomor 3 
for i in range(1900, 2021, 1) :
    if (i%4==0) :
        print (i)

#nomor 4
for i in range (100,200,1) :
    if (i%7==0) and (i%9==0) :
        print (i)

#nomor 5
n = int(input("Masukkan jumlah bilangan : "))

bil1=1
bil2=1
for i in range(n) :
    temp = bil1 #variabel bantu, fungsi untuk menampung bil1 sementara
    bil1 = bil2
    bil2 = temp + bil1
    print (temp, end = " ")
