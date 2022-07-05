'''
angka = 0
while angka<10 :
    print ("Aku suka belajar Python")
    if angka==4 :
        break
    angka+=1

print ("looping sudah selesai")
'''
'''
for i in range(10) :
    if i==4 :
        break;
    print ("Aku suka belajar Python")

print ("looping sudah selesai")
'''
'''
for i in range(100) :
    if i%10==0 :
        continue
    print (i, end = ' ')
'''
data = [11,22,33,44,55,66,77,88,99,100]

cari=int(input("Input bilangan yg dicari: "))

for i in data :
    if cari==i :
        print ("ketemu")
        break
    else:
        pass

