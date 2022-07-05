from random import randint

#game tebak angka sederhana
def guess(x) :
    bil_random = randint(1, x)
    tebak=0
    while tebak!=bil_random :
        tebak=int(input("Tebak angka = "))
        if tebak<bil_random :
            print("Bilangan terlalu kecil")
        elif tebak>bil_random :
            print("Bilangan terlalu besar")
    print ("Horay! Tebakan Anda Benar!!")

guess(20)