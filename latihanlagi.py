'''
teks = {"Universtas", "Wijaya", "Putra"}
tipe = {300, 400, 500, 200}
campur = {"Python", 89, 'c', 98.78}

print (teks)
print (tipe)
print (campur)


teks = ["Belajar", "Python", "yuuuk"] #list menggunakan kurung kotak
print(type(teks))
 
teks = ("Belajar", "Python", "yuuuk") #tupple menggunakan tanda kurung biasa
print(type(teks))
 
teks = {"Belajar", "Python", "yuuuk"} #set menggunakan kurung kurawal
print(type(teks))


teks = {"For", "Python", "for", "all", "Python", "programming", "language"}
 
print(teks[0])

data1 = {11,12,13,14,15,16}
data2 = {13,14,15,16,17,18}

print (data1 | data2) #operasi gabungan (union)
print (data1 & data2) #operasi irisan (intersection)


data = {(1,2,3), (4,5,6), 90, 88, "Hai"}
print (data)

#data2 = {1,3,4,[7,6]}
#print (data2)
'''

'''# Frozensets
# initialize A and B
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

print(A.isdisjoint(B))
print(A.difference(B))
A.add(4)'''

'''#Update dictionary python
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8; # Mengubah entri yang sudah ada
dict['School'] = "DPS School" # Menambah entri baru

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])'''

'''
#Contoh cara menghapus pada Dictionary Python
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First', 'School':'SD DI'}

del dict['Name'] # hapus entri dengan key 'Name'

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])
'''
'''
a = chr(218) #pojok kiri atas
b = chr(172) #pojok kanan atas
c = chr(192) #pojok kiri bawah
d = chr(217) #pojok kanan bawah
e = chr(196) #horizontal
f = chr(179) #vertikal
g = chr(219) #blok kotak
h = chr(255) #kotak kosong

print(a)
print(b)'''

angka=[1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9]
for i in range(10):
    for j in range(i,10):
        print(" ", end=' ')
    for k in range(0,2*i+1):
        print(angka[k],end=' ')
    print()

