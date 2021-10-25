print("##loja de tintas_2##")
area = float(input("Digite o valor em metros quadrados da area a ser pintada: \n"))
litros = area/6
quantidadeLatas = int(litros/18)
quantidadeGaloes =int(litros/3.6)

if (litros % 18 != 0):
    quantidadeLatas += 1
preçoLatas = quantidadeLatas * 80
if (litros % 3.6 != 0):
    quantidadeGaloes += 1
preçoGaloes = quantidadeGaloes * 25

mixLatas = int(litros/18)
mixgaloes = int((litros - (mixLatas * 18.0))/3.6)
print(mixgaloes)
if ((litros - (mixLatas * 18.0) % 3.6 != 0)):
    mixgaloes += 1

print("a quantidade só de Latas a serem compradas é de:", quantidadeLatas)
print("a quantidade só de galoes a serem compradas é de:", quantidadeGaloes)
print("o valor a ser pago nos galoes é de:", preçoGaloes, "R$")
print("o valor a ser pago nas latas é de:", preçoLatas, "R$")

print('quantidade de Latas:', mixLatas, 'e de galoes:', mixgaloes, '. Valor a pagar: ',(mixLatas * 80)+(mixgaloes*25), "R$")
