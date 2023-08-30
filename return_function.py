'''fungsi dengan kembalian'''
#template fungsi dengan kembalian
#def nama_fungsi (argument) :
#   badan fungsi
#   return output

#fungsi kuadrat





def kuadrat(input_angka):
    '''fungsi kuadrat'''
    output_kuadrat = input_angka**2
    return output_kuadrat    



y = kuadrat(3)
print(y)
print(kuadrat(6))
z = 10*(kuadrat(7)+10)
print(z,'\n')

# fungsi tambah

def tambah(angka1,angka2):
    '''fungsi return dengan multi input'''
    return angka1 + angka2
    

f = tambah(10,10)
print(f,'\n')

##dengan output banyak

def banyak(angka1,angka2):
    '''fungsi dengan banyak output'''
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2
    return tambah,kurang,bagi,kali


t,k,l,b = banyak(100,20)

print(f'hasil tambah = {t}')
print(f'hasil kurang = {k}')
print(f'hasil kali = {l}')
print(f'hasil bagi = {b}')



def hitung_luas_segitiga(alas, tinggi):
  luas = (alas * tinggi) / 2
  print("Luas segitiga adalah: ",luas)
  return luas

c = hitung_luas_segitiga(5,7)


print(c)


































