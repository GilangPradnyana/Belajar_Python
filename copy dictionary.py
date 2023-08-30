# copy dictionary


teman_teman = {
    "cp":"ucup",
    "tg":"tugung",
    "fm":"fahmi",
    "dw":"dewe",
    "gl":"gilang"
}

friend = teman_teman
print('copy dictionary'.upper().center(74,"="))
print(teman_teman , "\n")
print(friend,'\n')


print(f'format teman teman = {format(id(teman_teman))}')
print(f'format teman teman = {format(id(friend))}')


friends = teman_teman.copy()


print(f'format teman teman = {format(id(friends))}\n')

#pop dictionary 


print('pop dictionary'.upper().center(74,'='))

data_cp = friends.pop('cp') #-> menyimpan data dw
print(f'data cp = {data_cp}')
print(f'{friends}\n') #-> data "dw" hilangg

##pop item dictionary
data_terakhir = friends.popitem()
print(f'data terakhir = {data_terakhir}')
print(f'{friends}\n') #-> data terakhir hilangg














