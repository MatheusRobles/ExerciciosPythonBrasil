import random
print('### Conjunto de numero ###')
N = 10
lista = [random.randint(0,1000) for n in range(N)]
print(lista)
print('maior valor = {}'.format(max(lista)))
print('menor valor = {}'.format(min(lista)))
print('soma dos valores = {}'.format(sum(lista)))