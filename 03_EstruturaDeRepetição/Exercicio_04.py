populacao_A = 80000
populacao_B = 200000
ano = 0

while(populacao_B > populacao_A):
  populacao_A *=  1.03
  populacao_B *=  1.015
  ano += 1
  print(f' A:{populacao_A} B:{populacao_B} ano:{ano}')
print(f'quantidade de anos:{ano}')