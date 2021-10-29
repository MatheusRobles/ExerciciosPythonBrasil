print("### Escolha a operação ###")
num = float(input("Digite um numero: \n"))


def paridade(num):
    if num % 2 == 0:
        print("O numero é Par")
    else:
        print("O numero é Impar")


def valor(num):
    if num >= 0:
        print("O numero é positivo")
    else:
        print("O numero é negativo")


def tipo(num):
    if num % 1 > 0:
        print("O numero é decimal")
    else:
        print("O numero é inteiro")


escolha = (input("Escolha uma opção:\n[A]par ou impar\n[B]positivo ou negativo\n[C]decimal ou inteiro\n\n")).upper()

if escolha == 'A':
    paridade(num)
elif escolha == 'B':
    valor(num)
elif escolha == 'C':
    tipo(num)
else:
    print("Comando invalido")