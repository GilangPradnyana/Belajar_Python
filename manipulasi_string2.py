#operasi dan manipulasi string
#1.menyambung string(concatenate)
nama_pertama="ucup"
nama_kedua="D"
nama_terakhir='Fame'
nama_lengkap= nama_pertama+" "+nama_kedua+"'"+nama_terakhir
print(nama_lengkap)
print('='*36)
#menghitung panjang string
panjang=len(nama_lengkap)
print('panjang dari nama lengkap '+nama_lengkap+ " = " +str(panjang))
print('='*36)
#operator untuk string

#mengecek apakah ada komponen char atau karakter di string
d="d"
status= d in nama_lengkap
print(d+" " +"ada di "+nama_lengkap+"="+ str(status))


D="D"
status= D in nama_lengkap
print(D+" " +"ada di "+nama_lengkap+"="+ str(status))


d="d"
status= d not in nama_lengkap
print(d+" " +"tidak ada di "+nama_lengkap+"="+ str(status))
print('='*36)

#mengulang string
print("wkwk"*10)
print(10*"wkwk") 
print('='*36)

#indexing
print("index ke 0: " + nama_lengkap[0])
print("index ke 1: " + nama_lengkap[1])
print("index ke-(-1):" + nama_lengkap[-1])
print("index ke-(-2):" + nama_lengkap[-2])#-->jika min maka output akan dari belakang
print("index ke-[0:3]:" + nama_lengkap[0:4])#-->harus ditambah 1
print("index ke-[0:4]:" + nama_lengkap[0:5])#-->harus ditambah 1
print("index ke-[3:7]:" + nama_lengkap[3:8])#-->harus ditambah 1
print("index ke-[0,2,4,6,8]:"+ nama_lengkap[0:11:3])#-->mengambil angka dengan jeda
print('='*36)

#item paling kecil
print('item paling kecil: ',min(nama_lengkap))
#item paling besar
print('item paling besar: ',max(nama_lengkap))
print('='*36)

ascii_code=ord(" ") #-->mengetahui nilai dari sebuah karakter atau one single string
print("ASCI code untuk \"spasi\""+str(ascii_code))
data=117
print('char untuk ASCII 177 adalah:'+ chr(data))
print('='*36)

#operator dalam method
print('='*36)
data="otong surotong pararotong"
jumlah=data.count("0")#--> menghitung jumlah karakter pada suatu data
print("jumlah karakter \"o\" pada ",data,"="+str(data.count("o")))
