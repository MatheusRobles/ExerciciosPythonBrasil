print("##Triangulo##")
lado1 = float(input("Digite o primeiro lado de um triangulo \n"))
lado2 = float(input("Digite o segundo lado de um triangulo: \n"))
lado3 = float(input("Digite o triangulo lado de um triangulo: \n"))

if lado1+lado2 > lado3 and lado1+lado3 > lado2 and lado2+lado3 > lado1:
    if lado1 == lado2 == lado3:
        print("Forma um triangulo Equilátero!")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Forma um triangulo Isósceles!")
    else:
        print("Forma um triangulo Escaleno!")
else:
    print("Não forma um triangulo")
