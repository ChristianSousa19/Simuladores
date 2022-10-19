while True:
 t=int(input("Digite um numero para ver sua tabuada"))
 if t<0:
  print("Programa encerrado")
  break
 for c in range(1, 11):
  print(f"{t} x {c} é igual a : {t*c}")
