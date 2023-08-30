'''latihan fungsi'''

import os

#program menghitung luas persegi panjang

#membuat header programnya
#os.system('cls')
#print(f'{"PROGRAM MENGHITUNG LUAS":^40}')
#print(f'{"DAN PERSEGI PANJANG":^40}')
#print(f'{"-"*40:^40}')

# mengambil input user
#LEBAR = int(input('Masukan lebar: '))
#PANJANG = int(input('Masukan panjang: '))

#program menhitung luas
#LUAS = PANJANG * LEBAR
#KELILING = 2 * (PANJANG + LEBAR)

#tampilkan hasilnya
#print(f'Hasil perhitungan luas = {LUAS}')
#print(f'Hasil perhitungan keliling adalah = {KELILING}')

def Header():
    '''fungsi header'''
    os.system('cls')
    print(f'{"PROGRAM MENGHITUNG LUAS":^40}')
    print(f'{"DAN PERSEGI PANJANG":^40}')
    print(f'{"-"*40:^40}')

def inputUser():
    lebar = int(input('Masukan lebar: '))
    panjang = int(input('Masukan panjang: '))

    return lebar,panjang

def keliling(lebar,panjang):
    '''menhitung keliling'''
    return 2 * (lebar + panjang )
    
def luas(lebar,panjang):
    '''mehitung luas'''
    return panjang * lebar

def display(message,value):
    '''display functionnya'''
    print(f'hasil perhitungan {message} = {value}')

while True :
    Header()
    LEBAR,PANJANG = inputUser()
    KELILING=keliling(LEBAR,PANJANG)
    LUAS=luas(LEBAR,PANJANG)
    
    display('luas',LUAS)
    display('keliling',KELILING)
    
    isContinue = input('Apakah anda ingin melanjutkan program ? (y/n) ')
    if isContinue == 'n':
        print('Program selesai')
        break




































