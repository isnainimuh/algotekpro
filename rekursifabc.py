def kombinasi(x, b, c) :
    if b==0 :
        print(x + " ")
    else :
        for i in range(97, 97+c) :
            kombinasi(x+chr(i), b-1, c)

n=int(input("Masukkan jumlah karakter : "))
kombinasi ("",n,n)

