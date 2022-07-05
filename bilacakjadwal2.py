#bangkitkan bilangan acak antara 0 sampai 62 sebanyak 100  
from abc import abstractproperty
from random import randint, random, shuffle
from randomshuffle import randomJadwalPagi, randomJadwalMalam
kodematkul=[]
semester=[1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8]
daftarMK=[]
jadwal=[]  
daftarDosen=[11, 13, 14, 1, 3, 4, 1, 2, 8, 1, 15, 8, 2, 1, 1, 3, 1, 1, 4, 5, 2, 8, 5, 7, 1, 5, 4, 7, 8, 3, 5, 4, 5, 3, 7, 7, 5, 14, 2, 9, 12, 4, 7, 5, 9, 10, 8, 4, 7, 5, 1, 8, 3, 3, 11, 13, 14, 1, 3, 4, 1, 2, 8, 1, 15, 8, 6, 1, 1, 3, 1, 1, 6, 5, 6, 8, 5, 7, 1, 5, 4, 3, 8, 3, 5, 4, 7, 3, 3, 7, 6, 14, 6, 9, 12, 6, 7, 5, 9, 10, 6, 4, 8, 2, 1, 6, 3, 6]
lab = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def generate_data(): 
    for i in range(108):
        kodematkul.append(i+1)
    
    print("Kode Matkul")
    for i in range(108):
        print(kodematkul[i], end=" ")

    print("\nSemester")
    for i in range(108):
        print(semester[i], end=" ")
    
def generate_populasi(smt):
    for i in range(108):
        if smt==1:
            if semester[i]%2!=0:
                daftarMK.append(kodematkul[i])   
        else:
            if semester[i]%2==0:
                daftarMK.append(kodematkul[i])

    print("\nDaftar Matkul")
    for i in range(len(daftarMK)):
        print(daftarMK[i], end=" ")
    
    print("\nJadwal")
    
    jadwalMalam=[]
    jadwalPagi=[]
    for i in range(len(daftarMK)):
        if daftarMK[i]>=54:
            jadwalMalam.append(daftarMK[i])
        else:
            jadwalPagi.append(daftarMK[i])
    print(len(jadwalPagi))
    print(len(jadwalMalam))

    #tambahkan jadwal pagi dengan jam kosong
    for i in range(len(jadwalPagi), 60):
        jadwalPagi.append(0)
    
    #tambahkan jadwal malam dengan jam kosong
    for i in range(len(jadwalMalam), 40):
        jadwalMalam.append(0)

    #generate random jadwal untuk pagi dan malam
    for i in range(100):
        shuffle(jadwalPagi)
        #print(jadwalPagi)
        
    for i in range(100):
        shuffle(jadwalMalam)
        #print(jadwalMalam)

generate_data()
print()
generate_populasi(1)

defaultnya=[]
for i in range(100):
    defaultnya.append(i)

indexMalam=[]
satu=3
dua=4
for i in range(20):
    indexMalam.append(satu)
    indexMalam.append(dua)
    satu += 5
    dua += 5
indexPagi=[value for value in defaultnya if value not in indexMalam]

randomJadwal=[]
#gabung random pagi dan malam dalam 1 kromosom
for i in range(100):
    temp=[]
    pagi=0
    malam=0
    for j in range(100):
        if j in indexMalam:
            temp.append(randomJadwalMalam[i][malam])
            malam += 1
        else:
            temp.append(randomJadwalPagi[i][pagi])
            pagi += 1
    randomJadwal.append(temp)

'''
#tampilkan randomJadwal
print("\nRandom Jadwal")
for i in range(100):
    print(randomJadwal[i])
    print()
'''

indexLab=[0,1,2,3,4,20,21,22,23,24,40,41,42,43,44,60,61,62,63,64,80,81,82,83,84]
dataLab=[value for value in defaultnya if value not in indexLab]
indexLabPagi=[0,1,2,20,21,22,40,41,42,60,61,62,80,81,82]
indexLabMalam=[3,4,23,24,43,44,63,64,83,84]
nonLabMalam=[value for value in indexMalam if value not in indexLabMalam]
nonLabPagi=[value for value in indexPagi if value not in indexLabPagi]
indexD=[28,29,33,34,38,39,88,89,93,94,98,99]
dataD=[value for value in defaultnya if value not in indexD]
''''''
for iteration in range(4000):
    smt_temp=[]
    dosen_temp=[]
    lab_temp=[]
    
    for a in range(100):
        temp=[]
        for b in range(100):
            if randomJadwal[a][b]==0:
                temp.append(0)
            else:
                temp.append(semester[randomJadwal[a][b]-1])
        smt_temp.append(temp)
    
    #print("Cek semester temp")
    #print(smt_temp[0])
    #print(smt_temp[20])
    #print(smt_temp[60])
    #print(smt_temp[83])'''

    for a in range(100):
        temp=[]
        for b in range(100):
            if randomJadwal[a][b]==0:
                temp.append(0)
            else:
                temp.append(daftarDosen[randomJadwal[a][b]-1])
        dosen_temp.append(temp)

    #print("Cek dosen temp")
    #print(dosen_temp[0])
    #print(dosen_temp[20])
    #print(dosen_temp[60])
    #print(dosen_temp[83])

    fitnessValue=[]
    for i in range(100):
        fitnessValue.append(0)

    smt_ganti=[]
    value_ganti=[]
    #print("\nCek apakah ada semester yang sama:")
    for total in range(0, 100):
        temp=[]
        temp2=[]
        awal=0
        jarakHari=5
        for ulang in range(5):
            for i in range(awal, jarakHari):
                if smt_temp[total][i]!=0 and smt_temp[total][i]==smt_temp[total][i+5] :
                    fitnessValue[total] += 1
                    temp.append(i+5)
                    temp2.append(randomJadwal[total][i])
                    #print(fitnessValue[index], end=" ")
                #else:
                    #print('-', end=' ')
                if smt_temp[total][i]!=0 and smt_temp[total][i]==smt_temp[total][i+10] :
                    fitnessValue[total] += 1
                    temp.append(i+10)
                    temp2.append(randomJadwal[total][i])
                    #print(fitnessValue[index], end=" ")
                #else:
                    #print('-', end=' ')
                if smt_temp[total][i]!=0 and smt_temp[total][i]==smt_temp[total][i+15] :
                    fitnessValue[total] += 1
                    temp.append(i+15)
                    temp2.append(randomJadwal[total][i])
                    #print(fitnessValue[index], end=" ")
                #else:
                    #print('-', end=' ')
                if smt_temp[total][i+5]!=0 and smt_temp[total][i+5]==smt_temp[total][i+10] :
                    fitnessValue[total] += 1
                    temp.append(i+10)
                    temp2.append(randomJadwal[total][i+5])
                    #print(fitnessValue[index], end=" ")
                #else:
                    #print('-', end=' ')
                if smt_temp[total][i+5]!=0 and smt_temp[total][i+5]==smt_temp[total][i+15] :
                    fitnessValue[total] += 1
                    temp.append(i+15)
                    temp2.append(randomJadwal[total][i+5])
                    #print(fitnessValue[index], end=" ")
                #else:
                    #print('-', end=' ')
                if smt_temp[total][i+10]!=0 and smt_temp[total][i+10]==smt_temp[total][i+15] :
                    fitnessValue[total] += 1
                    temp.append(i+15)
                    temp2.append(randomJadwal[total][i+10])
                    #print(fitnessValue[index], end=" ")
                #else:
                    #print('-', end=' ')
            awal += 20
            jarakHari +=20
        smt_ganti.append(temp)
        value_ganti.append(temp2)
    #print("cek isi variabel smt_ganti dan value_ganti")
    #print(randomJadwal[0])
    #print(smt_ganti[0])
    #print(value_ganti[0])

    #print("\nFitnes Value Semester")
    #for i in range(100):
        #print(fitnessValue[i], end=' ')

    #print("\nCek apakah ada Dosen yang mengajar pada jam dan hari yang sama:")
    for total in range(0, 100):
        awal=0
        jarakHari=5
        for ulang in range(5):
            for i in range(awal, jarakHari):
                if dosen_temp[total][i]!=0 and dosen_temp[total][i]==dosen_temp[total][i+5] :
                    fitnessValue[total] += 1
                    #print(fitnessValue[index], end=" ")
                #else:
                    #print('-', end=' ')
                if dosen_temp[total][i]!=0 and dosen_temp[total][i]==dosen_temp[total][i+10] :
                    fitnessValue[total] += 1
                    #print(fitnessValue[index], end=" ")
                #else:
                    #print('-', end=' ')
                if dosen_temp[total][i]!=0 and dosen_temp[total][i]==dosen_temp[total][i+15] :
                    fitnessValue[total] += 1
                    #print(fitnessValue[index], end=" ")
                #else:
                    #print('-', end=' ')
                if dosen_temp[total][i+5]!=0 and dosen_temp[total][i+5]==dosen_temp[total][i+10] :
                    fitnessValue[total] += 1
                    #print(fitnessValue[index], end=" ")
                #else:
                    #print('-', end=' ')
                if dosen_temp[total][i+5]!=0 and dosen_temp[total][i+5]==dosen_temp[total][i+15] :
                    fitnessValue[total] += 1
                    #print(fitnessValue[index], end=" ")
                #else:
                    #print('-', end=' ')
                if dosen_temp[total][i+10]!=0 and dosen_temp[total][i+10]==dosen_temp[total][i+15] :
                    fitnessValue[total] += 1
                    #print(fitnessValue[index], end=" ")
                #else:
                    #print('-', end=' ')
            awal += 20
            jarakHari +=20

    #print("\nFitnes Value Dosen")
    #for i in range(100):
        #print(fitnessValue[i], end=' ')

    #print("\nCek apakah ada Dosen A mengajar pada jam dan hari yang sama dengan Dosen B:")
    #dapatkan index dari pengajaran dosen A dan B saja
    indexAB=[]
    for a in range(100):
        temp=[]
        for b in range(100):
            if dosen_temp[a][b]==4 or dosen_temp[a][b]==5:
                temp.append(1)
            else:
                temp.append(0)
        indexAB.append(temp)

    for total in range(0, 100):
        awal=0
        jarakHari=5
        for ulang in range(5):
            for i in range(awal, jarakHari):
                if indexAB[total][i]!=0 and indexAB[total][i]==indexAB[total][i+5] :
                    fitnessValue[total] += 1
                    #print(fitnessValue[index], end=" ")
                #else:
                    #print('-', end=' ')
                if indexAB[total][i]!=0 and indexAB[total][i]==indexAB[total][i+10] :
                    fitnessValue[total] += 1
                    #print(fitnessValue[index], end=" ")
                #else:
                    #print('-', end=' ')
                if indexAB[total][i]!=0 and indexAB[total][i]==indexAB[total][i+15] :
                    fitnessValue[total] += 1
                    #print(fitnessValue[index], end=" ")
                #else:
                    #print('-', end=' ')
                if indexAB[total][i+5]!=0 and indexAB[total][i+5]==indexAB[total][i+10] :
                    fitnessValue[total] += 1
                    #print(fitnessValue[index], end=" ")
                #else:
                    #print('-', end=' ')
                if indexAB[total][i+5]!=0 and indexAB[total][i+5]==indexAB[total][i+15] :
                    fitnessValue[total] += 1
                    #print(fitnessValue[index], end=" ")
                #else:
                    #print('-', end=' ')
                if indexAB[total][i+10]!=0 and indexAB[total][i+10]==indexAB[total][i+15] :
                    fitnessValue[total] += 1
                    #print(fitnessValue[index], end=" ")
                #else:
                    #print('-', end=' ')
            awal += 20
            jarakHari +=20

    #print("\nFitnes Value Dosen A dan B")
    #for i in range(100):
        #print(fitnessValue[i], end=' ')

    #print("\nCek apakah ada Dosen C mengajar pada Senin, Selasa, dan Rabu saja:")

    for i in range(100):
        for j in range(60,100) :
            temp=[]
            if dosen_temp[i][j]==8:
                fitnessValue[i] += 1

    #print("\nFitnes Value Dosen C")
    #for i in range(100):
        #print(fitnessValue[i], end=' ')


        
    #cek apakah Dosen D ngajar di hari selain Selasa dan Jumat Malam saja
    indexD=[]
    for i in range(100):
        temp=[]
        for j in dataD:
            if dosen_temp[i][j]==6:
                fitnessValue[i] += 1
                temp.append(j)
        indexD.append(temp)

    #print("Cek index D")
    #print(indexD[0])
    #print(indexD[20])
    #print(indexD[55])'''

    #print("\nFitnes Value Dosen D")
    #for i in range(100):
        #print(fitnessValue[i], end=' ')
    #print()
    #cek penempatan matkul tertentu yang menggunakan lab

    print()
    print("\nFitnes Value ke-", iteration)
    for i in range(100):
        print(fitnessValue[i], end=' ')

    #memilih fitness value yang terbaik
    urutkan=[i[0] for i in sorted(enumerate(fitnessValue), key=lambda x:x[1])]
    #print("\nFitness setelah diurut")
    #print(urutkan)
    #for i in urutkan:
        #print(fitnessValue[i], end=' ')
    #print()

    urutanTerpilih=[]
    for i in range(100):
        urutanTerpilih.append(urutkan[i])

    indexTerpilih=[]
    for i in range(20):
        indexTerpilih.append(urutkan[i])

    print("\nIndex Terpilih")
    print(indexTerpilih)
    #print(indexTerpilih)
    genTerpilih=[]
    for i in indexTerpilih:
        temp=[]
        for j in range(100):
            temp.append(randomJadwal[i][j])
        genTerpilih.append(temp)

    #print("\nGen Terpilih")
    #print(genTerpilih[0])
    #print(genTerpilih[19])
    #print(randomJadwal[0])
    #proses crossover, hapus MK Lab di gen pasangan yang tidak di taurh di lab
    #pindahkan ke gen pasangan dimana ruang lab kosong
    #cek index lab yang kosong di tiap kelas
    #print()
    indexLabKosongPagi=[]
    indexLabKosongMalam=[]

    for i in range(20):
        temp=[]
        for j in indexLabPagi:
            if genTerpilih[i][j]==0:
                temp.append(j)
        indexLabKosongPagi.append(temp)

    for i in range(20):
        temp=[]
        for j in indexLabMalam:
            if genTerpilih[i][j]==0:
                temp.append(j)
        indexLabKosongMalam.append(temp) 


    #cek matkul non lab yang diletakkan di lab
    labMalam=[]
    gantiLabMalam=[]
    for i in range(20):
        temp=[]
        temp2=[]
        for j in indexLabMalam:
            if genTerpilih[i][j]!=0 and lab[genTerpilih[i][j]]==0:
                temp.append(genTerpilih[i][j])
                temp2.append(j)
        labMalam.append(temp)
        gantiLabMalam.append(temp2)
    

    #print("\nnon lab index malam")
    #print(labMalam[0])
    #print(gantiLabMalam[0])

    labPagi=[]
    gantiLabPagi=[]
    for i in range(20):
        temp=[]
        temp2=[]
        for j in indexLabPagi:
            if genTerpilih[i][j]!=0 and lab[genTerpilih[i][j]-1]==0:
                temp.append(genTerpilih[i][j])
                temp2.append(j)
        labPagi.append(temp)
        gantiLabPagi.append(temp2)

    #print("\nnon lab index pagi")
    #print(labPagi[0])

    #Ubah matkul pada lab menjadi 0 (kosongkan)
    for i in range(20):
        for j in gantiLabMalam[i]:
            genTerpilih[i][j]=0
    
    for i in range(20):
        for j in gantiLabPagi[i]:
            genTerpilih[i][j]=0
    
    #print('Setelah non lab dihapus')
    #print(genTerpilih[0])

    #pindahkan ke index non lab yang kosong
    for i in range(20):
        ibantu=0
        for j in nonLabMalam:
            if genTerpilih[i][j]==0 and ibantu < len(labMalam[i]):
                genTerpilih[i][j]=labMalam[i][ibantu]
                ibantu += 1
    
    for i in range(20):
        ibantu=0
        for j in nonLabPagi:
            if genTerpilih[i][j]==0 and ibantu < len(labPagi[i]):
                genTerpilih[i][j]=labPagi[i][ibantu]
                ibantu += 1
    #print('Setelah non lab dimasukkan kelas non lab')
    #print(genTerpilih[0])


    #mutasi acak kelas pagi dg pagi malam dg malam
    acakMalam=nonLabMalam
    acakPagi=nonLabPagi

    shuffle(acakMalam)
    shuffle(acakPagi)
    copyMalam=[]
    for i in range(30):
        copyMalam.append(acakMalam[i])

    copyPagi=[]
    for i in range(30):
        copyPagi.append(acakPagi[i])

    #print("\nAcak malam:", copyMalam, end=' ')
    #print("\nAcak pagi:", copyPagi, end=' ')

    for i in range(20):
        for j in range(0,29,2):
            temp1=genTerpilih[i][copyMalam[j]]
            temp2=genTerpilih[i][copyPagi[j]]
            genTerpilih[i][copyMalam[j]]=genTerpilih[i][copyMalam[j+1]]
            genTerpilih[i][copyPagi[j]]=genTerpilih[i][copyPagi[j+1]]
            genTerpilih[i][copyMalam[j+1]]=temp1
            genTerpilih[i][copyPagi[j+1]]=temp2
        
    print("setelah mutasi acak")
    print(genTerpilih[0])

    print("\nGen Terpilih 19")
    print(genTerpilih[19])
    print("\nSebelum penggantian :")
    print(randomJadwal[urutanTerpilih[99]])

    #elitism
    index = 0
    for i in range(80,100):
        randomJadwal[urutanTerpilih[i]]=genTerpilih[index]
        index +=  1

    print("Setelah penggantian :")
    print(randomJadwal[urutanTerpilih[99]])

    #tampilkan randomJadwal
    print("\nJadwal Terbaik")
    print(genTerpilih[0])


    