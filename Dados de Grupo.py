tot=0
totm=0
totf=0
while  True:
    sexo=" "
    print("CADASTRE UMA PESSOA!!!")
    i=int(input("Idade: "))
    while sexo not in "M,F":
     sexo = str(input(" Sexo [M/F]: ")).strip().upper()[0]

    if i >=18:
      tot+=1
    if sexo== "M":
         totm+=1
    if sexo=="F" and i >20:
         totf=+1
    s=" "
    while s not in "SN":
      s = str(input("Deseja continuar? [S/N]")).strip().upper()[0]
    if s == "N":
     break

print(f"Ao todo temos {tot} pessoas maiores de idade.")
print(f"Ao todo temos {totm} homens maiores de idade")
print(f"Ao todo temos {totf} mulheres com menos de 20 anos.")





