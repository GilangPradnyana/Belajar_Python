## perulangan(loop)

# for kondisi:
    #aksi

#ini adalah list
angka2_list = [0,1,2,3,4,5] #ini adalah list
for i in angka2_list :
    print(f'i sekarang --> {i}')

print('akhir dari program1'.center(36,"="))

#ini dengan range
angka2_range = range(10)
for i in angka2_range :
    print(f'i sekarang --> {i}') #--> akhir tidak ditambil

print('akhir dari program2'.center(36,"="))

angka2_range = range(2,10) #angka dibelakang koma adalah awalan
for i in angka2_range :
#    print(f'i sekarang --> {i}') #--> bisa diganti oleh apapun
    print("saya keren")

print('akhir dari program3'.center(36,"="))

##untuk string

data_str = "saya gilang"

for huruf in data_str :
    print(huruf) #-->akan me-looping satu persatu karakter


print("\n\n")

## while loop

angka = 0

while angka < 5:
    angka += 1
    print(f'--> {angka}')