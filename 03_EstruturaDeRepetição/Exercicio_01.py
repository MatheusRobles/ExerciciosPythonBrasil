nota = 11
while(nota not in range(0,11)):
  nota = int(input("Digite uma nota de 0 a 10:\n"))
  if (nota > 10) or (nota < 0):
    print("Nota Invalida")