
def faktorial(bilangan) :
    sum=1
    for i in range(1, bilangan+1) :
        sum=sum*i
    print ("Hasil faktorial = ", sum)

faktorial(4)
faktorial(7)
faktorial(10)

def faktorialre(bilangan) :
    if bilangan==0 :
        return 1
    else :
        return bilangan * faktorialre(bilangan-1)

print("Hasil faktorial = ", faktorialre(4))
print("Hasil faktorial = ", faktorialre(7))
print("Hasil faktorial = ", faktorialre(10))

from math import factorial

print (factorial(4))
print (factorial(7))
print (factorial(0))


def destohexa(bil) :
    deret=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    hasil=[]
    bagi=0
    indeks=0
    sisa=0
    while bil>0 :
        bagi=bil//16
        sisa=bil%16
        x=deret[sisa]
        hasil.append(x)
        bil=bagi
        if bil==0:
            break
        else :
            indeks=indeks+1
    for i in range(indeks, 0-1, -1) :
        print (hasil[i], end="")
    print()

destohexa(10)
destohexa(15)
destohexa(16)
destohexa(48)
'''
'''
def destohexa(bil) :
    deret=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    if bil>=16 :
        destohexa(bil//16)
    hasil=deret[bil%16]
    print(hasil, end="")
    

destohexa(10)
print()
destohexa(16)
print()
destohexa(867)

def shuffle(bil) :
    hasil=bil%10
    if hasil!=0:
        print (hasil, end="")
    if bil>0 :
        shuffle(bil//10)

shuffle(4567)

'''

def kombinasi(jumlah) :
    karakter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
'''