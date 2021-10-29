print("### Compra de Carnes ###")
tipoCarne=int(input('Escolha o tipo de carne que deseja comprar:\n[1]Filé Duplo \ [2]Alcatra \ [3]Picanha \n'))
qtdCarne=float(input('Escolha a quantidade de carne que deseja comprar:\n'))
pagamento=int(input('Escolha o tipo de pagamento:\n[1] Cartão Tabajara ou [2] Á vista\n '))

if tipoCarne==1:
    nome='Filé duplo'
    if qtdCarne <=5.00:
        preço=qtdCarne*4.90
    else:
        preço=qtdCarne*5.80
elif tipoCarne==2:
    nome='Alcatra'
    if qtdCarne<=5.00:
        preço=qtdCarne*5.90
    else:
        preço=qtdCarne*6.80
elif tipoCarne==3:
    nome='Picanha'
    if qtdCarne<=5.00:
        preço=qtdCarne*6.90
    else:
        preço=qtdCarne*7.80

if pagamento==1:
    pag='Cartao Tabajara'
    desconto=(preço*5)/100
    totCompra=preço-desconto
else:
    pag='Dinheiro á vista'
    desconto=0
    totCompra=preço

espace = ""

print('-'*10,'Hipermercado Tabajara','-'*10)
print('Recibo')
print('Tipo de carne {:>38}'.format(nome))
print('Quantidade (kg) {:>30}'.format(qtdCarne))
print('Tipo de pagamento {:>39}'.format(pag))
print('Preço total R$: {:>26}{:.2f}'.format(espace, preço))
print('Descontos R$: {:>28}{:.2f}'.format(espace, desconto))
print('Valor a pagar R$: {:>24}{:.2f}'.format(espace, totCompra))
