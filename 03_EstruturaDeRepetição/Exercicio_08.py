soma = 0
for i in range(0, 5):
    numero = int(input('Informe um numero: '))
    soma += numero
media = soma/5
print ('A soma dos numeros digitados é {} e a media é {}'.format(soma, media))