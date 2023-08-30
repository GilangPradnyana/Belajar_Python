## --LIST--


#Kumpulan data NUMBERS
data_angka = [1,2,3]
print(data_angka)

#Kumpulan data string 

data_str = ["ucup","otong","udang"]
print(data_str)

#Kumpulan data boolean 

data_bool = [False,True,False]
print(data_bool)

#Kumpulan data campuran

data_campuran = [1,"bala-bala",2,"anjay gujinray",3, False]
print(data_campuran)

print(36*"=","\n")


## CARA ALTERNATIF MEMBUAT LIST             
data_range = range(0,12,2,) # range (start stop step)
print(data_range)
data_list = list(data_range)
print(data_list)


#membuat list dengan for loop, list comprehension

list_pake_for = [i ** 2 for i in range(1,10)] # -> bisa dikuadratkan
print(f'{list_pake_for} \n')

#membuat list pake for pake if
list_pake_for_if = [i for i in range(0,10) if i != 5] #menghilangkan 5
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0,10) if i  % 2 == 0] #memunculkan genap saja
print(list_pake_for_if)


list_pake_for_if = [i for i in range(0,10) if i % 2 != 0 ] #memunculkan genap saja
print(list_pake_for_if)

print("\n")
print(36*"=")
print("\n")

##operasi

#index   0(-3)  1(-2)    2(-1)
data = ["ucup","otong","amrin"]

#mengambil data dari list diatas

data_ucup = data[0]
print(f'data (index 0/-3) adalah : {data_ucup}')

data_otong = data[-2]
print(f'data (index 1/-2) adalah : {data_otong} ')

data_amrin = data[-1]
print(f'data (index -1/2) adalah : {data_amrin}')

print(36*"=")

#mengambil info jumlah data dalam list

panjang_data = len(data)
print(f'\npanjang data adalah : {panjang_data} \n')

##manipulasi data list

#menambahkan item pada list sesuai posisi

print(f'data sebelum ditambah : \n{data}')

data.insert(1,"Asap")
print(f'data sesudah ditambah : \n{data}') #menambahkan data dimana saja

#menambah data diakhir list

data.append ("jajang")
print(f'data ditambah lagi : \n{data}') #-> menambahkan data diakhir


#merubah data

data[2] = "michael"
print(f'data 2 dirubah menjadi {data}')

#me remove data

data.remove("amrin") #akan error jika huruf salah
print(f'\ndata yg sudah diremove : \n{data}')

#meremove data paling belakang

data_akhir = data.pop()
print(f'data belakang yang sudah hilang : {data}')


print(f'data yg hilang dari data pop adalah {data_akhir}') #-> akan mengambil data yg hilang dari data pop

print('\n')

    













