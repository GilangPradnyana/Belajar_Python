print("nested list".center(36,"="))
print("\n")



data0 = [1,2]
data1 =[3,4] 

list_biasa = [1,2,3,4]



print(f'list biasa = {list_biasa}')
print(f'list 2nd = {data0,data1,1234}\n') #list didalam list bisa diisi angka

##contoh penggunaan

peserta_0 =['ucup',25,"Laki Laki"]
peserta_1 =["otong",32,'Perempuan']
peserta_2 =["itil'",22,"non binnary"]

list_peserta = [peserta_0,peserta_1,peserta_2]

print(list_peserta,"\n")

##pakai for

for peserta in list_peserta :
    print(f'nama\t= {peserta[0]}') #untuk menjabarkan list (index 0)
    print(f'umur\t= {peserta[1]}') #untuk menjabarkan list (index 1)
    print(f'gender\t= {peserta[2]}\n') #untuk menjabarkan list (index 2)

print("deep copy nested list".center(35,"="))
print("\n")

data_0 = [1,2]
data_1 = [3,4]
data_2d = [data_0,data_1]
data_2d_copy = data_2d.copy()

print(f'data = {data_2d}')
print(f'data copy = {data_2d_copy}')

#mengambil satu data didalam data
ambil_data_1 = data_2d[0][1] #-> index pertama untuk masuk ke data dan index kedua untuk mengambil data
ambil_data_2 = data_2d[1][1]

print(f'data pertama = {data_2d[0][1]}')
print(f'data kedua = {data_2d[1][1]}\n')
 


print(f'format data = {hex(id(data_2d))}')
print(f'format data copy = {hex(id(data_2d_copy))}')
print('addres dari member ke-1')
print(f'addres asli member ke 1 = {hex(id(data_2d[0][1]))}') #-> shallow copy
print(f'addres copy member ke 1 = {hex(id(data_2d_copy[0][1]))}\n') #-> tidak mengcopy data di dalam list

##deep copy
from copy import deepcopy

data_2d = [data_0,data_1]
data_2d_deepcopy = deepcopy(data_2d)

print(f'addres asli  = {hex(id(data_2d))}') 
print(f'addres deepcopy  = {hex(id(data_2d_deepcopy))}') #-> tidak mengcopy data di dalam list


print(f'addres asli member ke 1 = {hex(id(data_2d[0]))}') #-> shallow copy
print(f'addres copy member ke 1 = {hex(id(data_2d_deepcopy[0]))}\n') #-> tidak mengcopy data di dalam list

data_2d[1][0] = 30
print(f'data = {data_2d}')
print(f'data copy = {data_2d_copy}')
print(f'data deep copy = {data_2d_deepcopy}')
























































