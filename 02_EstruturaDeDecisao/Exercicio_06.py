print("#### Identificador Maior numero####")
num1 = int(input("Digite o Primeiro Numero:\n"))
num2 = int(input("Digite o Segunda Numero:\n"))
num3 = int(input("Digite o Terceiro Numero:\n"))

if (num1 > num2) and (num1 > num3):
    print("O maior numero é:", num1)
elif num2 > num3:
    print("O maior numero é:", num2)
else:
    print("O maior numero é:", num3)
