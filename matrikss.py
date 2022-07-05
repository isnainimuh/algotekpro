'''
matA = [[1,2,3], [4,5,6], [7,8,9]]
matB = [[1,1,1], [1,1,1], [1,1,1]]

for i in range (3) :
    for j in range (3) :
        matC=matA[i][j]+matB[i][j]
        print (matC, end=" ")
    print ()
'''
'''
#no 2
matA = []
matB = []

b = int(input("Baris matriks = "))
k = int(input("Kolom matriks = "))

for i in range (b) :
    matAelemen= []
    for j in range (k) :
        bil=int(input("Masukkan elemen : "))
        matAelemen.append(bil)
    matA.append(matAelemen)

for i in range (b) :
    matBelemen= []
    for j in range (k) :
        bil=int(input("Masukkan elemen : "))
        matBelemen.append(bil)
    matB.append(matBelemen)

for i in range (b) :
    for j in range (k) :
        matC=matA[i][j]-matB[i][j]
        print (matC, end=" ")
    print ()

'''
'''
from random import randint
matriks=[]

for i in range (3) :
    elemen = []
    for j in range (4) :
        bil = randint(1,9)
        print (bil, end = " ")
        elemen.append(bil)
    print ()
    matriks.append(elemen)
'''