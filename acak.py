from random import randint

tampung=[]
for i in range (10) :
    bil=randint(20,50)
    print (bil)
    tampung.append(bil)

print ("Bilangan ganjil : ")
for i in tampung :
    if i%2==1 :
        print (i, end = " ")













'''
angka = randint(0,10)
print (angka)

cek=True

while cek :
    tebak=int(input("Masukkan tebakan angka = "))
    if tebak==angka :
        print ("Tebakan Anda benar!")
        break

'''


'''
sum=0
for i in range (10) :
    bil = randint (0,9)
    print (bil, end = ' ')
    sum+=bil

print ("\nTotal = ", sum)

data=[0]
for i in range(10) :
    bil = randint(0,9)
    data.append(bil)
print (data)
for each in data :
    if each%2!=0 :
        print (each)
'''

