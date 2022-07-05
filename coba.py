harga_rumah = 500000000

uang_muka =int(input("masukkan uang muka= "))
jangka =int(input("masukkan jangka pembayaran(dalam tahun)= "))
tahun = jangka
bulan = tahun*12
if uang_muka >= 5000000 :
    sisa_cicilan = harga_rumah - uang_muka
    cicilan_pokok = sisa_cicilan/bulan
    bunga = sisa_cicilan*10//100/12
    total_angsuran = cicilan_pokok + bunga 
    total_seluruh_pembayaran =int(total_angsuran*bulan+uang_muka)
    
    print("Detail Pembayaran")
    print("1. Harga pokok rumah : Rp ", harga_rumah)
    print("2. Uang muka : Rp ", uang_muka)
    print("3. jangka pembayaran : ",tahun, "tahun atau",bulan, " bulan")
    print("4. cicilan per bulan : Rp ",int(total_angsuran))
    print("5. Total pembayaran seluruhnya : Rp " ,total_seluruh_pembayaran)