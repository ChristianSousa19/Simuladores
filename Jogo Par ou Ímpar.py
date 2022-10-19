import random
print("VAMOS JOOGAR PAR OU IMPAR!!!!!")
v=0
while True:
 n=" "
 s=0
 l=" "
 c=random.randint(0,11,)
 j=int(input("Digite um valor:"))
 while l not in "Pp,Ii":
  l=str(input("Par ou Impar [P/I]")).strip().upper()[0]
 s=j+c
 print(f"Você jogou {j} e o computador jogou {c}.Total de {s}")
 print("DEU PAR"if s%2==0 else "DEU IMPAR")
 if l=="P":
   if s%2==0:
    print("Jogador Ganhou")
    v += 1
   else:
     print("Jogador Perdeu")
     break
 if l=="I":
     if s%2==1:
         print("Jogador Ganhou")
         v+=1
     else:
         print("Jogador Perdeu")
         break
 print(" Tente Novamente")
print(f"FIM DE JOGO ")
