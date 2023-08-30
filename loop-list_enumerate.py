#looping dari list

#for loop
print('for loop'.center(36,"="))
data_angka = [4,3,2,1,5,6]


for angka in data_angka :
    print(f'angka = {angka}')


peserta = ['otong','dadang','diding']

for p in peserta :
    print(f'peserta = {p}')

print('\n')

# for loop dan range

print('for loop and range'.center(36,"="))
kumpulan_angka = [10,5,2,7,1,9,]

panjang = len(kumpulan_angka)

for i in range (panjang) :
    print(f'angka = {kumpulan_angka[i]}')
print('\n')
# while

print('while loop'.center(36,"="))

kumpulan_angka = [10,5,2,7,1,9,]

panjang = len(kumpulan_angka)
i = 0 

while i < panjang :
    print(f'angka = {kumpulan_angka[i]}')
    i += 1

#list comperhension
print('\n')
print("list comperhension".center(36,"="))
 
data = ['cucup','didung',13,23,'otong']

[print(f'data = {i}') for i in data]

kumpulan_angka = [10,5,2,7,1,9,]

angka_kuadrat = [i**2 for i in kumpulan_angka ]
print(angka_kuadrat)


#enumerate
print("\n")
print("enumerate".center(36,"="))

data = ['cucup','didung',13,23,'otong']

for index,data in enumerate(data) :
    print(f'index = {index}, data = {data}')
































