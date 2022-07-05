
'''
def cetak(teks) :
    print("Subscribe to ",teks)

#pemanggilan fungsi di program utama
cetak("UWP Channel")

def hitungRata2(a,b) :
    rata = (a+b)/2
    print ("Rata-rata = ", rata)

bil1 = 16
bil2 = 30
hitungRata2(bil1,bil2) 

def maximum(data) :
    maxi=data[0]
    for each in data :
        if maxi<each :
            maxi=each
    print ("Nilai maksimum = ", maxi)

listNum = [15,67,83,23,45,65,77,90,71,29]
maximum(listNum)

def hitungPanjang(data) :
    sum = 0
    for each in data :
        sum=+1
    print("Banyak karakter: ", sum)

listData = ['a','i','u','e','o']
hitungPanjang(listData)


def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus") 

def average(data, n) :
    sum=0
    for each in data :
        sum=sum+each
    rata2=sum/n
    return rata2

listNum=[17,15,31,43,56,89] 
hasil=average(listNum, len(listNum))
print(hasil)
'''

def cek(data, x) :
    cek=False
    for each in data :
        if x==each :
            cek=True
            break    
    if cek==True:
        print ("Termasuk 10 deret pertama Fibonaci")
    else :
        print ("Tidak termasuk 10 deret pertama Fibonaci")

listFibonaci = [1,1,2,3,5,8,13,21,34,55]
cek(listFibonaci, 16)
cek(listFibonaci, 5)

import math

def hitungSisiMiring(a,b) :
    #c2 = a2 + b2
    #c = akar kuadrat (a2 + b2)
    hasil = math.sqrt(a*a + b*b)
    print ("sisi miring = ", hasil)

panjang = 12
tinggi = 5
hitungSisiMiring(panjang, tinggi)

def minimum(data) :
    mini=data[0]
    for each in data :
        if mini>each :
            mini=each
    return mini

listAngka = [1,2,3,4,5,6,7,8,9,10]
print ("Nilai minimum = ", minimum(listAngka))

