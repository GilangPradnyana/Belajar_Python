##Widht And Multiline

#data
data_nama= "ucup"
umur= 11
tinggi=167.5
nomor_sepatu=43

#data string
data_string=f"nama: {data_nama}"f"umur: {umur}"f"tinggi badan saya: {tinggi}"f'ukuran sepatu saya: {nomor_sepatu}'
print("Data String".center(20,"="))
print(data_string)
print(36*"="+"\n")

#string multiline
data_string=f"nama: {data_nama}"f"\numur: {umur}"f"\ntinggi badan saya: {tinggi}"f'\nukuran sepatu saya: {nomor_sepatu}'
print("Data String Multiline (n)".center(20,"="))
print(data_string)
print(36*"="+"\n")

#string multiline(kutip triplets) --> bebas taruh dmana saja 
data_string= f"""
nama = {data_nama}   
umur = {umur}
tinggi badan = {tinggi}
ukuran sepatu = {nomor_sepatu}
"""
print("Data String Multiline Triplets".center(20,"="))
print(data_string)
print(36*"="+"\n")

#mengatur lebar
data_string= f"""
nama (sebelum)= {data_nama}  
nama (sesudah)= {data_nama:<10}
umur = {umur}
tinggi badan = {tinggi}
ukuran sepatu = {nomor_sepatu}
"""
print("Data String Multiline Triplets".center(20,"="))
print(data_string)
print(36*"="+"\n")
