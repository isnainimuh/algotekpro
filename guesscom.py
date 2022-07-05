from random import randint

def computer_guess(x) :
    low = 1
    high = x
    tebak = randint(low, high)
    feedback = 'h' 
    while feedback!='c' :
        feedback=input(f"Apakah tebakan {tebak} sudah benar? (jawab h:lebih besar, l:lebih kecil, c:correct!) ")
        if feedback=='h' :
            tebak=tebak-1
        elif feedback=='l' :
            tebak=tebak+1
    print("Horay!Tebakan komputer benar!!")

#misal kita tentuka bilangan yg harus ditebak adalah 14
computer_guess(20)














'''
#game tebak angka sederhana
def computer_guess(x) :
    bil_random = randint(1, x)
    tebak=0
    while tebak!=bil_random :
        tebak = randint(1, x)
        print (f"Saya tebak {tebak}")
        if tebak < bil_random or tebak > bil_random:
            print ("Jawaban salah, Tebak lagi!!")
    print("Horay!!Komputer berhasil menebak angka!!")

computer_guess(20)
'''