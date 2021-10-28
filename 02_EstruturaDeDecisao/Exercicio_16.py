print("##Equação de Segundo Grau##")
a = float(input("Digite o valor de a:\n"))
if a == 0:
    print("A equação não é de segundo grau")
else:
    b = float(input("Digite o valor de b:\n"))
    c = float(input("Digite o valor de c:\n"))
    delta = b**2 - 4 * a * c
    x1 = (-b + delta ** (1/2))/(2*a)
    x2 = (-b - delta ** (1/2))/(2*a)

    if delta < 0:
        print("A equação não possui raizes reais")
    elif delta == 0:
        print("A equação possui apenas uma raiz: x={:.2f}".format(x1))
    else:
        print("A equação possui duas raizes reais: x1={:.2f} e x2={:.2f}".format(x1,x2))

