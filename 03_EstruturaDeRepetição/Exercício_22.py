print('### identificador de numeros primos ###')
valida = 0
divisivel = []
num = int(input("Digite um numero:\n"))
if num > 2:
  lista = list(range(2,num))
  for n in lista:
    if num % n == 0:
      valida = 1
      divisivel.append(n)
     
  if valida == 0:
    print("O numero {} é primo".format(num))
  else:
    print("O numero {} não é primo".format(num))
    print("{} é divisivel por :".format(num), end ="  ")
    for n in divisivel:print(n, end = " ")
elif num == 2:
  print("O numero {} é primo".format(num))
elif num == 1:
  print("O numero um não é considerado primo")
else:
  print("Operação invalida")
  
