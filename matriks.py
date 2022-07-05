
'''#membuat matriks ordo 2x2
matriksA = [ [5,2], [2,6] ]

#membuat matriks ordo 3x3
matriksB = [ [1,2,4], [6,5,1], [7,2,5]]

#membuat matriks ordo 3x4
matriksC= [ [1,2,3,4], [5,6,7,8], [2,4,1,5]]

#menampilkan isi matriks
for i in range (0,3) :
    for j in range (0,3) :
        print (matriksB[i][j], end = ' ')
    print ()

matX = matriksB

for i in range (0,3) :
    for j in range (0,3) :
        print (matX[i][j], end = ' ')
    print ()'''


#membuat list untuk menampung baris data
matrix = []
for a in range (3) :
    #membuat list untuk menampung data di tiap baris
    baris = []
    for b in range (4) :
        nilai = int(input("Masukkan elemen = "))
        baris.append(nilai)
    #menambahkan tiap list baris ke matrix
    #implementasi list di dalam list    
    matrix.append(baris)

#menampilkan isi list yang sudah diinputkan
for i in range (3) :
    for j in range (4) :
        print (matrix[i][j], end = ' ')
    print ()

'''
#tugas nomor 1
matAwal = [[1,2,3,4,5],[6,7,8,9,1],[4,3,2,1,5],[7,4,5,2,3],[5,6,7,8,0]]
print ("Matriks awal :")
for i in range (5) :
    for j in range (5) :
        print (matAwal[i][j], end = " ")
    print ()

matTrans=[]

for i in range (5) :
    baris = []
    for j in range (5) :
        baris.append(matAwal[j][i])
    matTrans.append(baris)

print ("Matriks transpose :")
for i in range (5) :
    for j in range (5) :
        print (matTrans[i][j], end = " ")
    print ()

'''
'''
#tugas no 2
mat = [[1,2,3,3],[2,6,7,8],[3,7,11,12],[7,8,12,15]]
#cetak matriks
for i in range (4) :
    for j in range (4) :
        print (mat[i][j], end = " ")
    print ()

cek = True
for i in range (4) :
    for j in range (4) :
        if mat[i][j]!=mat[j][i] :
            cek = False
            break

if cek==True :
    print ("Matriks simetri")
else :
    print ("Bukan matriks simetri")

'''
'''
#tugas no 3
mat1 = [[0,0,1], [0,0,0], [0,0,0], [0,0,0]]
for i in range (4) :
    for j in range (3) :
        print (mat1[i][j], end = " ")
    print ()

cek = True
#pengecekan mat1
for i in range (4) :
    for j in range (3) :
        if mat1[i][j]!=0 :
            cek = False
            break

if cek==True :
    print ("Matriks tersebut adalah matriks nol")
else:
    print ("Bukan matriks nol")


'''
'''
matrix=[[2,0,0,1],[4,6,0,0],[12,9,8,0],[1,2,3,4]]

cek = True
for i in range(4) :
    for j in range (4) :
        if j>i :
            if matrix[i][j]!=0 :
                cek=False
                break

if cek==True :
    print ("Matriks bujursangkar dan termasuk matriks segitiga bawah")
else :
    print ("Matriks bujursangkar namun bukan matriks segitiga bawah")

'''
#tugas no. 5
from random import randint

barisA = int(input("Masukkan jumlah baris mat A= "))
kolomA = int(input("Masukkan jumlah kolom mat A= "))

barisB = int(input("Masukkan jumlah baris mat B= "))
kolomB = int(input("Masukkan jumlah kolom mat B= "))

mat1 = []
for i in range (barisA) :
    isi = []
    for j in range (kolomA) :
        nilai=randint(0,9)
        isi.append(nilai)
        print (nilai, end = " ")
    mat1.append(isi)
    print ()

mat2 = []
for i in range (barisB) :
    isi = []
    for j in range (kolomB) :
        nilai=randint(0,9)
        isi.append(nilai)
        print (nilai, end = " ")
    mat2.append(isi)
    print ()

mat3 = []

if barisA==kolomB :
    for x in range(0,len(mat1)):
        row = []
        for y in range(0,len(mat1[0])):
            total = 0
            for z in range(0,len(mat1)):
                total = total + (mat1[x][z] * mat2[z][y])
            row.append(total)
        mat3.append(row)

for x in range(barisA):
    for y in range(kolomB):
        print (mat3[x][y], end=' ')
    print ()
