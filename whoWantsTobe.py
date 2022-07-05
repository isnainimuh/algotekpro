from listQuestion import question, a,b,c,d, answer
from random import choice

def cek_status() :
    simpan=input("Apakah Anda ingin lanjut ? (y/n)")
    if simpan=='y' or simpan=='Y':
        return True
    else :
        return False

def fifty(a,b,c,d,jawab) :
    if jawab=='a' :
        result=a
    elif jawab=='b' :
        result=b
    elif jawab=='c' :
        result=c
    else:
        result=d
    
    result2=''
    acak=''
    for i in range(5) :
        acak=choice(['a','b','c','d'])
        if acak!=jawab :
            if acak=='a' :
                result2=a
            elif acak=='b' :
                result2=b
            elif acak=='c' :
                result2=c
            else :
                result2=d
            break
        else :
            acak=choice(['a','b','c','d']) 
    
    print("Kami telah menghilangkan dua jawaban yang salah, sehingga tersisa jawaban berikut : ")
    if ord(jawab) < ord(acak) :
        print(result)
        print(result2)
    else :
        print(result2)
        print(result)

nilai= ["100.000", "200.000","300.000","500.000","1.000.000","2.000.000","4.000.000","8.000.000","16.000.000","32.000.000","64.000.000","125.000.000","250.000.000","500.000.000","1.000.000.000"]
status=True
posisi=0
nomor=1
help=0

print("..:::::::::::::::::::::::::::::::..")
print(".: WHO WANTS TO BE A MILLIONAIRE :.")
print("GOOD LUCK!")

while status==True and nomor<=15:
    print("__________________________________________________")
    print(f"Pertanyaan {nomor} senilai Rp {nilai[posisi]}")
    print("__________________________________________________")
    print(question[posisi])
    print(f"{a[posisi]}\t\t\t {c[posisi]} ")
    print(f"{b[posisi]}\t\t\t {d[posisi]} ")
    if help==0 :
        pilih=(input("Apakah anda ingin menggunakan pilihan bantuan (y/n) ?"))
        if pilih=="y" or pilih=="Y" :
            help=1
            fifty(a[posisi],b[posisi],c[posisi],d[posisi],answer[posisi])
    else :
        print("Bantuan sudah digunakan / tidak tersedia")
    jawab=(input("Masukkan pilihan jawaban Anda (a,b,c,d) = "))
    if answer[posisi]==jawab:
        print("Jawaban Anda benar!\n")
        posisi+=1
        nomor+=1
        if nomor<=15 :
            status = cek_status()

    else :
        print("Ooopss jawaban Anda salah, permainan berakhir disini.")
        break

    print(".::Huraayyy!! Congratulation... you won 1 billions rupiahs::.\n")




