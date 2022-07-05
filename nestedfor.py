


#tugas 1 a
for i in range (10, 0, -1) :
    for j in range (i,0 , -1) :
        print (j, end = " ")
    print ()

#tugas 1b
for i in range (1,10) :
    for j in range (10, i-1, -1) :
        print (' ', end=' ')
    for k in range (0,2*i-1) :
        print (i, end=' ')
    print()

#tugas 1c
from random import randint

for i in range (1,10) :
    for j in range (10, i-1, -1) :
        print (' ', end='')
    for k in range (0,2*i-1) :
        bil=randint(1,9)
        print (bil, end='')
    print()

for i in range (1, 6) :
    for j in range (i, 6) :
        print (j, end = " ")
    print ()


'''
for i in range (10,0,-1) :
    for j in range (1, i+1) :
        print (j, end = " ")
    print ()
'''

'''
n=int(input("Masukkan n : "))

x = 2*n-1

for a in range (1,n+1) :
    for b in range(1,a+1) :
        print (" ", end = ' ')
    for c in range (x,0,-1) :
        print ("*", end = ' ')
    print ()
    x=x-2
'''
'''
for i in range (1,6) :
    for j in range (1,6) :
        print (j, end = ' ')
    print ()
'''

'''for i in range(10):
    print("Aku belajar Python")
    if i==4:
        break'''

'''jumlah = 0
for i in range(1, 11):
    jumlah = jumlah + i
print("Total= ", jumlah)'''