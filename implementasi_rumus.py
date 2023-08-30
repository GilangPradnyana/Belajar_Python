import os
os.system('cls')



def hitung_kecepatan():
    print('hitung kecepatan ready')
    jarak = float(input('masukan jarak'))
    waktu = float(input('masukan waktu'))
    kecepatan = (jarak) * (waktu)
    print ('kecepatan:' ,kecepatan, '\n')

def luas_segitiga():
    print('hitung luas segitiga ready')
    alas = float(input('masukan alas'))
    tinggi = float(input('masukan tinggi'))
    luas = 0.5 * (alas * tinggi)
    print ('Luas segitiga adalah:' ,luas, '\n')

def luas_balok():
    print('hitung luas balok ready')
    panjang = float(input('masukan panjang '))
    lebar = float(input('masukan lebar '))
    tinggi = float(input('masukan tinggi '))
    luas = (2* (panjang * lebar + panjang * lebar + panjang * lebar + panjang * lebar))
    print ('Luas balok adalah: '  , luas, '\n')

def luas_bola():
    print('hitung luas bola ready')
    phi = 22/7 #error salah rumus
    jari_jari = float(input('masukan r2 '))
    dasar_bola = float(4)
    luas = (dasar_bola * phi * jari_jari )
    print ('Luas bola adalah: '  , luas, '\n')






while True :
    
    user_input = int(input('pilih rumus yang akan dipakai: \n1.Hitung Kecepatan\n2.Hitung luas segitiga \n3.Luas balok\n4.Luas bola\nPilih nomor berapa: \n\n0 keluar\nPilihan =  '))
    if (user_input == 1):
        hitung_kecepatan()


    elif (user_input == 2):
        luas_segitiga()

    elif (user_input == 3):
        luas_balok()

    elif (user_input == 4):
        luas_bola()

    else:
        break
