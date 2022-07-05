
'''data = [0]


for i in range(10) :
    nilai= int(input("Masukkan nilai : "))
    data.append(nilai)
print (data)'''


'''def cetak():
    return "Welcome to Python Jungle"

#memanggil fungsi di program utama
x=cetak()
print(x)'''

'''def penjumlahan(a, b):
    hasil = a + b
    return hasil

#memanggil fungsi di program utama
print(penjumlahan(9, 17))'''


'''def volume_kerucut():
    print("Volume kerucut")
    r=int(input("Masukkan jari2: "))
    t=int(input("Masukkan t: "))
    print("Volume kerucut: ", 3.14*r*r*t/3)

def volume_bola():
    print("Volume bola")
    r=int(input("Masukkan nilai r= "))
    print("Volume bola= ", 4*3.14*r*r*r/3)


#memanggil fungsi di program utama
volume_kerucut()
volume_bola()'''

'''def faktorial(x):
    hasil=1
    for i in range(1, x+1):
        hasil=hasil*i
    return hasil

#memanggil fungsi di program utama
print(faktorial(5))'''

'''def negaraku(negara="Indonesia"):
    print("Saya dari ", negara)

negaraku("Malaysia")
negaraku("Singapore")
negaraku() #jika tidak diisi maka mengambil nilai default'''

def maksimum(data):
    maks = data[0]
    for i in data:
        if maks < i:
            maks = i
    print("Nilai maksimum: ", maks)

tinggi = [171, 180, 175, 167, 175, 181]
maksimum(tinggi)

