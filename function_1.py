##function

#template
#def nama_fungsi(argument):
#   Badan fungsi

def hello_world(nama):
    print('fungsi hello world menerima input dengan variable')
    print(f'\nselamat datang dunia wahai {nama}\n')

hello_world('dewe')

##program tambah

def program_tambah(angka1,angka2) :
    hasil = angka1+angka2
    print(f'{angka1} + {angka2} = {hasil}')


program_tambah(5,5)

def nama_peserta(anjay_goreng):
    '''hhi keluarga kecil'''
    anjay_goreng[1] = 'asyep'
    keluarga = anjay_goreng.copy()
    for peserta1 in keluarga :
        print(f'haii {peserta1}')





anggota_keluarga = ['gilang','dewe','giyu']

    

nama_peserta(anggota_keluarga)
print(anggota_keluarga[1])














