def fibo(x) :
    if x<=0 or x<=1 :
        return x
    else :
        return fibo(x-2) + fibo(x-1)


n=int(input("Masukkan jumlah deret = "))
print (n, " angka deret fibonanci : ")

for i in range(n):
  print(fibo(i), end= " ")

