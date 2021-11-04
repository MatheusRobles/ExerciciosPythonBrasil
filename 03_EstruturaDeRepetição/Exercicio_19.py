import random
print('### Conjunto de numero ###')
N = 10
lista = [random.randint(0,1500) for n in range(N)]
new_lista = []
delete = []
print(lista)
for n in lista:
  if (n < 1000):
    new_lista.append(n)

print(new_lista)
print('maior valor = {}'.format(max(new_lista)))
print('menor valor = {}'.format(min(new_lista)))
print('soma dos valores = {}'.format(sum(new_lista)))