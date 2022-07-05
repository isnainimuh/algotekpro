
file = open("fileku.txt", "r")
data = file.read()
jumlahKarakter = len(data)
print ("Jumlah karakter pada file tsb = ", jumlahKarakter)

file = open("fileku.txt", "r")
data = file.read()
print(type(data))
sum = 0
for each in data :
    if each == 'a' :
        sum+=1
print ("Jumlah karakter a pada file tsb = ", sum)





'''
#nomor 1
file = open("contoh.doc")
data = file.read()
kata=0
for i in data :
    if i==' ' or i=='.' :
        kata+=1

print ("Jumlah kata = ", kata)

#nomor 2
fi = open("fileku.txt")
teks = fi.read()
fi.close

karakter = input("Karakter yang ingin di-replace= ")
replace = input("Karakter pengganti= ")
fi = open("fileku.txt", "w")
for i in teks :
    if i==karakter :
        fi.write(replace)
    else :
        fi.write(i)
fi.close

fi = open("fileku.txt")
print (fi.read())



#nomor 3
f1 = open("d1.doc")
data1=f1.read()
f1.close

f2 = open("d2.doc")
data2=f2.read()
f2.close

f1=open("d1.doc", "w")
f1.write(data2)
f1.close

f1=open("d1.doc")
print (f1.read())

f2=open("d2.doc", "w")
f2.write(data1)
f2.close

f2=open("d2.doc")
print (f2.read())

'''



