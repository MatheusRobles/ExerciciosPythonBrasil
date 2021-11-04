valida = 1
while(True):

  numero = int(input("Digite um numero para calcular o fatorial:\n"))
  if(numero > 16 or numero <= 0):
    print("Error")
    break
  fatorial = 1
  print(f'{numero}! =', end = ' ')
  for i in range(0,10):
      print(numero, end = '')
      if numero != 1:
        print('.',end = '')
      else:
        break
      fatorial *= numero
      numero -= 1
  print(f' = {fatorial}')