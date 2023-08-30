#skurangdari=(Inputuser <3 )
#print('kurang dari 3: ',iskurangdari)
#islebihdari= (Inputuser>10)
#print('lebih dari 10: ',islebihdari)
#iscorrect=(islebihdari or iskurangdari)
#print('angka yang anda masukan:',iscorrect,"\n\n")


#print(20*"=","\n\n")
#Inputuser= float(input('masukan angka\nlebih  dari 3 dan kurang dari 10\n\n:'))
#islebihdari=(Inputuser >3)
#print('angka lebih dari 3: ',islebihdari)
#iskurangdari=(Inputuser < 10)
#print('angka kurang dari 10: ',iskurangdari)
#print('angka yang anda masukan: ',islebihdari and iskurangdari)


#------TUGAS------

Inputuser=float(input('masukan angka\nlebih dari 0\nkurang dari 5\natau\nlebih dari 8\ndan\nkurang dari 11\nmasukan angka:  '))
islebihdari0=(Inputuser>0)
print("angka lebih dari 0: ",islebihdari0)
iskurangdari5=(Inputuser <5)
print('angka kurang dari 5: ',iskurangdari5)
islebihdari8=(Inputuser >8)
print('angka lebih dari 8: ',islebihdari8)
iskurangdari11=(Inputuser<11)
print('angka yang kuraang dari 11: ',iskurangdari11)

isseluruh=(islebihdari0 and iskurangdari5) or (islebihdari8 and iskurangdari11)
print("angka yang lebih dari 0 kurang dari 5 atau lebih dari 8 dan kurang dari 11 adalah",isseluruh)




