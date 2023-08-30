#program list buku

list_buku = []
while True :
    print("masukan data buku".center(36,"="))
    judul = input('Masukan judul buku\t: ')
    penulis = input('Masukan penulis buku\t: ') 

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)
   

    print("data buku".center(36,"="))
    for index,buku in enumerate(list_buku) :
        print(f'{index+1} | {buku[0]} | {buku[1]}')

    islanjut = input("Apakah ingin menginput data lagi ? (y/n)")

    if islanjut == "n" :
        break
    
    else :
        break

    
print("program selesai".center(36))