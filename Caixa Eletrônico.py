s=int(input("Quando você deseja sacar R$: "))
tots=s
totced=0
ced=50
while True:
 if tots>=ced:
     tots-=ced
     totced+=1
 else:
     print(f"Total de {totced} cédulas de  R${ced} ")
     if ced==50:
         ced==20
     elif ced==20:
         ced==10
     elif ced==10:
         ced==1
     totced=0
     if tots==0:
         break
