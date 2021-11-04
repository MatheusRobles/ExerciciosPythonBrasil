numero = int(input("Digite o termo da serie fibonacci:\n"))
n1=0
n2=1
soma=0
listaFibonacci=[n1,n2]

for i in range(0,1000):
    soma = n1 + n2
    listaFibonacci.append(soma)
    n1 = n2
    n2 = soma
print('O {}º termo da serie Fibonacci é:{}'.format(numero,listaFibonacci[numero+1]))
