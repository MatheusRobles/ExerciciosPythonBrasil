print("### venda de combustível ###")
litros = float(input("Informe a quantidade de litros?\n"))
tipo = (input("Informe o tipo de Combustível\n[A]Alcool ou [G]Gasolina\n")).upper()

if tipo == 'G':
  valor = litros * 2.5
elif tipo == 'A':
  valor = litros * 1.9
else:
  "Valor invalido"

print("O valor a ser pago é de {:.2f}R$".format(valor))