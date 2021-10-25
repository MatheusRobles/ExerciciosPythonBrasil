print("##loja de tintas##")
area = float(input("Digite o valor em metros quadrados da area a ser pintada: \n"))
litros = area/3
quantidadeTintas = int(litros/18)
if (litros % 18 != 0):
    quantidadeTintas +=1
preço = quantidadeTintas * 80
print("a quantidade de tintas a serem compradas é de:", quantidadeTintas)
print("o valor a ser pago é de:", preço, "R$")

