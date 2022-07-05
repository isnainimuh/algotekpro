# set integer 
my_set = {1,2,3} 
print(my_set) 

# set dengan menggunakan fungsi set() 
my_set = set([1,2,3]) 
print(my_set) 

# set data campuran 
my_set = {1, 2.0, "Python", (3,4,5)} 
print(my_set) 

# bila kita mengisi duplikasi, set akan menghilangkan salah satu 
# output: {1,2,3} 
my_set = {1,2,2,3,3,3} 
print(my_set) 



daftar={'a','b','c','d','e','f','g','h','i','j','k'}
kalimat="Indonesia Tanah Air Beta"

irisan = [huruf if huruf in daftar else '*' for huruf in kalimat]
print(" ".join(irisan))

