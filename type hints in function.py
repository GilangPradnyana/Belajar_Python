'''Type hints untuk fungsi'''

##bentuk standar fungsi yg kita pelajari  
print('TYPE HINTS'.center(36,'='))
'''
studi kasus
#def fungsi(parameter):
#    print(parameter**2)
#fungsi(1)
#fungsi('ucup')
#fungsi(True)
'''

#penggunaan type hints

def fungsi_dengan_hints(arguments:int)->int:
    """FUNGSI DENGAN HINTS"""
    output = 10**arguments
    
    return output

hasil = fungsi_dengan_hints(2)
print(hasil)


def display(argument:str) -> str:
    print(argument)
    
display(f'hasil dari 10 ** 2 = {hasil}\n\n')


print('*args'.center(36,'='))
'''*args'''
#memasukan data/argument

'''normal'''
def data_diri(nama,tinggi,umur) :
    print(f'nama saya adalah {nama}\ntinggi : {tinggi}cm\numur : {umur} tahun\n')

data_diri = data_diri('dewe',155,15)

'''pakai list'''

def data_diri(data_list):
    '''normal'''
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    umur = data[2]
    print(f'nama saya adalah {nama}\ntinggi : {tinggi}cm\numur : {umur} tahun\n')

data_diri(['oppenheimer',155,15])

#introduce *args
def fungsi(*args):#---
    '''pakai *args'''#---
    nama = args[0] #------> args == *
    tinggi = args[1]#---
    umur = args[2]#---
    print(f'nama saya adalah {nama}\ntinggi : {tinggi}cm\numur : {umur} tahun\n')

fungsi('dewe',155,15)

def biodata(*biodata):
    '''pakai args'''
    nama = biodata[0]
    tinggi = biodata[1]
    umur = biodata[2]
    print(f'nama saya adalah {nama}\ntinggi : {tinggi}cm\numur : {umur} tahun\n')

biodata('giyuu',155.5,16)


def biodata(*biodata):
    '''pakai args'''
    nama = biodata[0]
    tinggi = biodata[1]
    umur = biodata[2]
    return nama,tinggi,umur
n,t,u = biodata('gilaang',155.5,15)
print(f'nama saya adalah {n}')
print(f'tinggi : {t}')
print(f'umur : {u}\n')

def hitung(*penjumlahan:int):
    output = 0
    for angka in penjumlahan:
        output += angka
    return output

hasil=hitung(1,2,3,4,5,6,7,8,9)
print(f'hasil = {hasil}\n')

print('*KEYWORD ARGS'.center(36,'='))

'''*kwargs'''

def fungsi(nama,tinggi,umur):
    '''fungsi normal'''
    print(f'nama saya {nama}\ntinggi :{tinggi}\numur : {umur}\n')

fungsi('gilang',165.5,16)

def function(**kwargs):
    '''fungsi kwargs'''
    nama = kwargs['nama']
    tinggi = kwargs['tinggi']
    umur = kwargs['umur']
    print(f'nama saya adalah {nama}\ntinggi : {tinggi}\numur : {umur} tahun')

function(nama = 'dewe',tinggi = 158,umur = 13)






























