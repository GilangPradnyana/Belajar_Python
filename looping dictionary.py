# looping dictionary
# values adalah iterable


teman_teman = {
    'cup': 'ucup',
    'tg' : 'tagen',
    'ql' : 'qila'


}


for teman in teman_teman :
    print(teman) #-> outputnya adalah "keys"


print(36*'=')
print('mengambil keys dalam data dict'.center(36,"="))
# operator untuk mengambil keys dari data dict
print('mengambil keys dari data dicr')
keys = teman_teman.keys()
print(keys)
for key in teman_teman.keys() : # mengambil value dari keys
    print(teman_teman.get(key))


print('mengambil value dalam data dict'.center(36,"="))
values = teman_teman.values()
print(values)

for values in teman_teman.values() :
    print(values)

print('mengambil seluruh data dalam data dict'.center(36,"="))
item = teman_teman.items()
print(item)

for items in teman_teman.items() :
    print(items)

for key,value in teman_teman.items() :
    print(f'{key} | value : {value}')































