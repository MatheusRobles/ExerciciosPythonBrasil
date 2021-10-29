print("### compra de frutas ###")
kgMorango = float(input("Digite o valor em Kg de morangos:\n"))
kgMaca = float(input("Digite o valor em Kg de maças:\n"))

kgTotais = kgMorango + kgMaca
valorMorango = kgMorango*2.5
valorMaca = kgMaca*1.8

if kgMorango > 5:
  valorMorango = kgMorango*2.2
if kgMaca > 5:
  valorMaca = kgMaca*1.5

valorTotal = valorMaca + valorMorango
if kgTotais > 8 or valorTotal > 25:
  valorTotal = valorTotal * 0.9

print('O Valor total a ser pago é {:.2f}R$'.format(valorTotal))
