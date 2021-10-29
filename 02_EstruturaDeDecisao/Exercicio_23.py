print("### Identificando inteiro ou decimal ###")
num = float(input("Digite um numero: \n"))

if num % 1 > 0:
    print("O numero é decimal")
else:
    print("O numero é inteiro")