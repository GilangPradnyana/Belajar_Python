'''default argument'''
#def fungsi(argument):
# def fungsi(arrgument = nilai defaultnya):

print("DEFAULT ARGUMENT FUNCTION".center(36,'='))

def say_hello(haii = "ucup ganteng"): ##-> default argument
    '''haloo kawann'''
    print(f'haloo {haii}\n')


nama = 'ucup armageddon'

say_hello(nama)
say_hello()

def hitung(angka = 15) :
    '''hitung dikit cuyy'''
    c = angka + 15
    print(f'{angka} + 15 = {c}\n')

hitung()


def sapa_dia(nama,pesan = 'apa kabar') :
    '''fungsi dengan satu input biasa dan satu default argument'''
    print(f'hai {nama} {pesan}')

sapa_dia('gilang','apa kabar')
sapa_dia('dudung')
print('\n')


##contoh 3
def hitung_pangkat(angka,pangkat = 2):
    hasil = angka ** pangkat
    return hasil
    


print(hitung_pangkat(5))
hitung_hasil =hitung_pangkat(pangkat = 3,angka = 5)
print(hitung_hasil)

#contoh 4
def hitung(input1=2,input2=3,input3=4):
    hitung_hitung = input1 + input2 +input3
    return hitung_hitung


c = hitung(input3=10)
print(c)

def perkalian_sederhana(kali1,kali2):
    hitung_perkalian = kali1 * kali2
    print(f'hasil dari {kali1} * {kali2} = {hitung_perkalian}')
    return hitung_perkalian


kali1 = int(input('masukan angka pertama : '))
kali2 = int(input('masukan angka kedua : '))

hasil_kali = perkalian_sederhana(kali1,kali2)
print(hasil_kali)