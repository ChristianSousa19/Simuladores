n=s=0
c=0
while True:
  n=int(input("Digite um valor,[999] se desejar parar a sequencia"))
  if n==999:
   break
  c+=1
  s+=n
print(f" Você digitou {c} numeros e a  soma entre eles e equivalente a  {s}")