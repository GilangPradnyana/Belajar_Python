#contiue,pass and break

## pass berfungsi sebagai dummy, tidak akan dieksekusi

#angka = 0

#while angka < 5:

 #   angka += 1
  #      pass #--> ini tidak akan dieksekusi
      
 #   print(angka)


##continue

angka = 0 #kondisi 1
 
print(f'angka sekarang -> {angka}') 

while angka <5 :
    angka += 1
    print(f'angka sekarang --> {angka}') #aksi 1

    if angka == 3 : # kondisi 2
        print("hehewww")
        continue #akan membuat loop ke step selanjutnya 
    
    print("wassup") #aksi 2
   
    
print("\nnice")