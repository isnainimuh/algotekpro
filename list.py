'''
data = [1,2,3,4,5,6,7,8,9,10]

#cara akses
print (data[3])
print (data[-1])


subdata1 = data[0:4]
print(subdata1)
subdata2 = data[2:]
print (subdata2)
subdata3 = data[:4]
print (subdata3)

subdata4 = data[:-4]
print (subdata4) 
subdata5 = data[-7:]
print (subdata5)

data2 = [11,12,13,14,15,16,17,18,19,20]

data3 = data + data2

print (data3)

data.append(30)
print (data)

'''

#nomor 1
angka = [1,2,3,4,5,6,7,8,9,10]
print (angka[1])
print (angka[4])

#nomor 2
ganjil = []

for i in range (1,100,2) :
    ganjil.append(i)

print (ganjil)

#nomor 3
data_list = []
for i in range (1,101) :
    data_list.append(i)

print (data_list)

#nomor 4
data = []
sum = 0
N = int(input("masukkan jumlah nilai : "))
for i in range (N):
    nilai = int(input("input nilai : "))
    data.append(nilai)
    sum = sum + nilai
print (data)
rata = sum/N
print ("Rata-rata : ", rata)
print ("Nilai min : ", min(data))
print ("Nilai max : ", max(data))
