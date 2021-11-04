n1=0
n2=1
soma=0
listaFibonacci=[n1,n2]

for i in range(0,1000):
    soma = n1 + n2
    listaFibonacci.append(soma)
    n1 = n2
    n2 = soma
    if soma > 500:
      break
print(f'lista Fibonacci:\n{listaFibonacci}')


