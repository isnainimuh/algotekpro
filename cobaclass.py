class Student:
    #create class variable
    student_count=0
    
    #create constructor 
    def __init__(self, nama, npm, jk, alamat):
        self.nama=nama
        self.npm=npm
        self.jk=jk
        self.alamat=alamat
        Student.student_count +=1
    
    #create method
    def cetak(self):
        print(self.student_count) 
        print(self.nama)
        print(self.npm)
        print(self.jk)
        print(self.alamat)

mhs1 = Student("Ali","1234","Laki-laki","Surabaya")
mhs1.cetak()
mhs2 = Student("Diah","1111","Perempuan","Gresik")
mhs2.cetak()