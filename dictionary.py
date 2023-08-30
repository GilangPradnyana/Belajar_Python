# list -> array, mrngakses dengan 
# menggunakan index

data_list = ['ucup','otong','dudung']
print(f'index 0 = {data_list[0]}\n')


#dictionary (dict) -> associative array 
#identyfier -> key
#index == key

print('dictionary'.center(34,"="))
data_dict = {
    'key':'value',
    'cp':'otong',
    'tg':'ucup',
    'dg':'dudung',
    'nmbr':1454,
    'list':data_list


}

print(f'data cp adalah : {data_dict["cp"]}')
print(f'data tg adalah : {data_dict["tg"]}')
print(f'data dg adalah : {data_dict["dg"]}')
print(f'data nmbr adalah : {data_dict["nmbr"]}')
print(f'data list adalah : {data_dict["list"]} \n')


print("operasi dictionary".center(36,"="))
print("\n")

data_dict = {
    'key':'value',
    'cp':'otong',
    'tg':'ucup',
    'dg':'dudung',
    'nmbr':1454,
    'list':data_list
}

#panjang dictionary
print('panjang data dict'.center(36,'='))
LENDICT = len(data_dict)

print(f'panjang data dictionary = {LENDICT}')
print('\n')
#mengecek key exist atau tidak
print('mengecheck suatu key exist'.center(36,'='))
KEY = 'cp'
CHECKKEY = KEY in data_dict
print(f'key \'cp\' in data dictionary = {CHECKKEY}')
print('\n')

#mengakses value (read) dengan get
print('mengakses value dengan get'.center(36,'='))
cari = data_dict.get('cp')

print(f'cp = {cari}')
print(data_dict.get('nmbr'))
print(data_dict['tg'])
print(data_dict.get('kiss','key \'kiss\' tidak ditemukan ')) # check key dengan message tidak ditemukan
print('\n')

# mengupdate data
print('mengupdate data'.center(36,'='))
data_dict['cp'] = 'ucup dagang bakso'
print(data_dict)

print(36*'=')

data_dict['sp'] = 'asepp masyep'
print(data_dict)

print(36*'=')

data_dict.update({'cp':'otong'})
print(data_dict)

print(36*'=')
 
data_dict.update({'qila':'qila anak pick me'})
print(data_dict)
print('\n')

# mendelete data pada dictionary 
print('men delete data dict'.center(36,'='))
del data_dict['qila']
print(data_dict)


















