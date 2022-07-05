data1 = [1,2,3,4,5,6,7,8,9]
data2 = [5,4,6,9,2,1,7,8,3]

posisi = [2,3,4,5]
index=[]
for i in posisi:
    for j in range(len(data2)):
        if data1[i]==data2[j]:
            data2[j]=0



index=[]
for i in posisi:
    for j in range(len(data1)):
        if data2[i]==data1[j]:
            data1[j]=0

print(data1)
print(data2)

'''for i in range(len(data1)):
    for j in posisi:'''

data1.pop(0)
print(data1)      

simpan1=[]
simpan2=[]
for i in data1:
    if i!=0:
        simpan1.append(i)

print(simpan1)
