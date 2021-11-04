print("### Taboada ###")
num = int(input('Digite um numero para calcular a taboada\n'))
print('Taboada do {}:'.format(num))
for n in range(1,11):
  resultado = num * n
  print('{} X {} = {}'.format(num,n,resultado))