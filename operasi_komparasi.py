#----Is dan Is not adalah untuk membandingkan memori tempat menyimpan obyek

y=5
x=5
print(hex(id(y)))
print(hex(id(x)))

c= y is not x
e= y is x
print(e)
print(c)
