#membuat matematika sederhana

print("matematika sederhana".center(20,"="))

input_angka = float(input("masukan angka pertama : "))
operator = input("+ , - , * , / : ")
input_angka2 = float(input("masukan angka kedua : "))

if operator == "+" :
    hasil_tambah = input_angka + input_angka2
    print(f'hasil dari penjumlahan anda adalah : {hasil_tambah}')

