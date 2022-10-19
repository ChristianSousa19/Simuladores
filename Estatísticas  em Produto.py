menor=cont=0
r=" "
pm=0
total=0
while True:
    produto=str(input("Digite o nome do produto: "))
    preço=float(input("Digite o preço do produto R$: "))
    cont+=1
    total+=preço
    r=" "
    if cont==1:
        menor==preço
    else:
        if preço<menor:
            menor=preço
    if preço>1000:
        pm+=1
    while  r not in "SN":
     r=(str(input("Deseja Continuar? [S/N] :"))).strip().upper()[0]
    if r=="N":
     break
print(f"O valor total das compras custam R$: {total}")
print(f"Ao total temos {pm} produtos que custam mais de R$: 1000")
print(f"O produto com menor preço custa R$: {preço}")