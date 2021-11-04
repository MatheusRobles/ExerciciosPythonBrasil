print('### identificador de numeros primos ###')
valida = 0

num = int(input("Digite um numero:\n"))
if num > 2:
  lista = list(range(2,num))
  for n in lista:
    if num % n == 0:
      print("O numero {} não é primo".format(num))
      valida = 1
      break
  if valida == 0:
    print("O numero {} é primo".format(num))
elif num == 2:
  print("O numero {} é primo".format(num))
elif num == 1:
  print("O numero um não é considerado primo")
else:
  print("Operação invalida")
