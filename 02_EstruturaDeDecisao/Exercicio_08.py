print("#### Identificador Menor Preço####")
num1 = float(input("Digite o Preço do Primeiro Produto:\n"))
num2 = float(input("Digite o Preço do Segunda Produto:\n"))
num3 = float(input("Digite o Preço do Terceiro Produto:\n"))

if (num1 < num2) and (num1 < num3):
    print(f'Compre o produto que custa {num1} R$')
elif num2 < num3:
    print(f'Compre o produto que custa {num2} R$')
else:
    print(f'Compre o produto que custa {num3} R$')