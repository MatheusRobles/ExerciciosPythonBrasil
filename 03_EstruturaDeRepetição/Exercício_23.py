print('### identificador de numeros primos ###')
valida = 0
primo = []
numero = 0
entrada = int(input("digite um numero:"))
for num in range(0,entrada):
  if num > 1:
    valida = 0
    lista = list(range(2,num))
    for n in lista:
      numero +=1
      if num % n == 0:
        valida = 1
    if valida == 0:
       primo.append(num)

print('numero de divisões: {}\nnumeros primos entre 1 e {}:\n{}'.format(numero, entrada, primo))
