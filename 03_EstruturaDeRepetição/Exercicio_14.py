par = 0
impar = 0
for i in range(0, 10):
    numero = int(input('Informe um numero:\n'))
    if numero % 2 == 0:
      par +=1
    else:
      impar +=1
print ('Quantidade de numeros pares:{} e impares:{}'.format(par, impar))