data_angka = [2,3,12,5,6,8,3,4,5,7,5]
print(f'data angka = {data_angka}')

#count data

count_3 = data_angka.count(3) # menghitung jumlah satu data yg ada
count_4 = data_angka.count(4) #-----------------------------------
print(f'jumlah angka 3 = {count_3}')
print(f'jumlah angka 4 = {count_4} ')
print("\n")

#ambil posisi data 

data = ["ucup","dadang","otong"]
print(data)

index_dadang = data.index("dadang")
print(f'dadang berada dibaris ke {index_dadang}')
print("\n")


# mengurutkan list
print(f'data angka sebelum sort = \n{data_angka}')
data_angka.sort()
print(f'data angka sesudah sort = \n{data_angka}\n')


print(f'data sebelum sort = \n{data}')
data.sort() 
print(f'data sesudah sort = \n{data}') #-> diurut berdasarkan huruf terawal

# balik listnya
print(f'data angka sebelum direverse = \n{data_angka}')
data_angka.reverse()
print(f'data angka sesudah direverse = \n{data_angka}')

print(36*"=",'\n')


##copy list

print('copy list '.center(36,'='))
print('\n')


a = ["otong","dudung","mimi"]
print(f'a = {a}')

b = a #-> pass by reference
print(f'b = {b}')

#merubah member dari a

## ini akan merubah kedua list
a[1] = "michael"

b.sort()
print(f'a = {a}')
print(f'b = {b}')

## addres dari kedua list a dan b 
print(f'addres a = {hex(id(a))}')
print(f'addres b = {hex(id(b))}')

##menduplikat list dengan copy
print('membuat list c dengan copy a()')
c = a.copy() #-> membuat list baru dengan addres yg berbeda

print(f'addres a = {hex(id(a))}')
print(f'addres b = {hex(id(b))}')
print(f'addres c = {hex(id(c))}') #-> berbeda

print('kita ubah data 0')
c[0] = "dadang" #-> tidak mengubah data a dan b

print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')
































