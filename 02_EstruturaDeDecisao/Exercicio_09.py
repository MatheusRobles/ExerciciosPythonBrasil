print("#### Identificador Menor Preço####")
num1 = int(input("Digite o Preço do Primeiro Produto:\n"))
num2 = int(input("Digite o Preço do Segunda Produto:\n"))
num3 = int(input("Digite o Preço do Terceiro Produto:\n"))

lista = [num1, num2, num3]
lista.sort()

print("os numeros em ordem crescente são:\n")
for var in lista:
    print(var)
