print("### Dia da Semana###")
num = int(input("Informe um numero para saber o dia da semana:\n"))
lista = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado']

if (num > 0) and (num <= 7):
    print('{} - {}'.format(num, (lista[num - 1])))
else:
    print("valor inválido")
