print("##Digite números inteiros e um número real##")
numInt1 = int(input("Digite o primeiro numero inteiro: \n"))
numInt2 = int(input("Digite o segundo numero inteiro: \n"))
numReal = float(input("Digite o numero real: \n"))

print("\na)O produto do dobro do primeiro com a metade do segundo:", int(numInt1 * 2 * numInt2 / 2))

print("\nb)A soma do triplo do primeiro com o terceiro:", float(numInt1 * 3 + numReal))

print("\nc)O terceiro elevado ao cubo", pow(numReal, 3))
