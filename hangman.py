from random import choice
from words import data
import string

def cek_kata() :
    cek = choice(data)
    if ('-' in cek) :
        cek = choice(data)
    return cek

def hangman() :
    #mengambil salah satu kata dalam daftar kata-kata di file words melalui fungsi cek_kata()
    kata = cek_kata().upper() #method untuk mengubah menjadi huruf besar
    #mengubah word ke dalam data set untuk mengecek himpunan data
    set_kata = set(kata)
    terinput = set()
    #memberi nilai awal untuk kesempatan salah tebak 
    nyawa = 10

    while len(set_kata) > 0 and nyawa > 0 :
        #menyuruh user input huruf tebakannya
        tebak_huruf=input("Masukkan 1 huruf tebakan: ").upper()
        if (tebak_huruf in set_kata) :
            print ("Good, tebakan Anda benar!")
            set_kata.remove(tebak_huruf)

        elif (tebak_huruf in terinput) :
            print ("Huruf tersebut sudah ada, coba yang lain!!")

        else :
            nyawa=nyawa-1
            print (f"Uwooo,, tebakan salah. Coba lagi!! Tinggal {nyawa} kesempatan")

        #masukkan huruf yang sudah ditebak dalam data set lain
        terinput.add(tebak_huruf)  
        print ("Huruf yang sudah dimasukkan : ", " ".join(terinput))
        #mencetak susunan huruf yang sudah ditebak
        daftar_huruf=[i if i in terinput else '-' for i in kata]
        print ("Susunan huruf = ", " ".join(daftar_huruf))   
    
    if (len(set_kata)==0) :
        print (f"Huray!!Selamat anda berhasil menebak kata {kata} !!")
    else :
        print (f"Oopssie... anda gagal menebak kata {kata}")


hangman()


