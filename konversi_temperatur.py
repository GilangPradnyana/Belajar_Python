#----KONVERSI TEMPERATUR----#   

#--Progrgam konversi celsius ke satuan lain --# 
print ("\nKonversi Temperatur \n")

Celsius = float(input("masukan suhu dalam celsius "))
print('suhu adalah ', Celsius , "Celcius")
#Reamur
#Rumus reamur --> 4/5 * c 
Reamur= (4/5) * Celsius
print ('konversi dari celcius ke reamur adalah ', Reamur, "reamur")
#Fahrenheit
Fahrenheit = ((9/5) * Celsius) + 32
print ('konversi suhu dari celcius ke fahrenheit adalah ', Fahrenheit, 'Fahrenheit')
#Kelvin
Kelvin = Celsius + 273
print('konversi suhu dari celcius ke kelvin adalah ', Kelvin ,"kelvin" )