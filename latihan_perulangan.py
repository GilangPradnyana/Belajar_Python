## latihan membuat segitiga

sisi = 4

#1.menggunakan for

#dummy variable
print('Awal for')


count = 1
for i in range (sisi) :
    print("*" * count)
    count += 1


#2.menggunakan while 

print("\nAwal while")

count = 1
while True :
    print("*" * count)
    count += 1

    if count > 4 :
        break


#hanya ganjil saja

print("awal while")
count = 1
while True:
	if (count%2):
		# Print jika ganjil
		print("*"*count)
		count += 1
	else:
		# akan kembali ke atas jika ganjil
		count += 1
		continue

	# akan break jika count melebihi sisi
	if count > sisi:
		break

print("akhier while")

# 4. hanya ganjil saja

print("awal while")
count = 1
spasi = int(sisi/2)

while True:
	if (count%2):
		# Print jika ganjil
		print(" "*spasi,"+"*count)
		spasi -= 1
		count += 1
	else:
		# akan kembali ke atas jika ganjil
		count += 1
		continue

	# akan break jika count melebihi sisi
	if count > sisi:
		break

print("akhier while")








