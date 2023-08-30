#Multi keys & Nesting dictionary

import datetime

mahasiswa_1 = {
    'nama':'giyu',
    'nim':'0093213',
    'sks_lulus':112,
    'beasiswa':False,
    'lahir':datetime.datetime(2029,1,17)
}

mahasiswa_2 = {
    'nama':'gilangg',
    'nim':'00938482',
    'sks_lulus':130,
    'beasiswa':False,
    'lahir':datetime.datetime(2007,2,11)
}

mahasiswa_3 = {
    'nama':'dewe',
    'nim':'00394930',
    'sks_lulus':114,
    'beasiswa':True,
    'lahir':datetime.datetime(2006,6,23)
}


data_mahasiswa = {
    'MAH001':mahasiswa_1,
    'MAH002':mahasiswa_2,
    'MAH003':mahasiswa_3
}

print(f'{"KEY":<6} {"Nama":<17} {"NIM":<9} {"SKS":<9} {"Beasiswa":<9} {"Lahir":<10}')
print(60*'=')

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa

    NAMA = data_mahasiswa[KEY]['nama'].capitalize()
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]["sks_lulus"]
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

    print(f'{KEY:<6} {NAMA:<17} {NIM:<9} {SKS:<9} {BEASISWA:<9} {LAHIR:<3}')


















