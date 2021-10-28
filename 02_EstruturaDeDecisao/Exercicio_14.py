print("##Media##")
nota1 = float(input("Digite a primeira nota: \n"))
nota2 = float(input("Digite a segunda nota: \n"))
media = (nota1+nota2)/2

if media >= 9.0:
    print("Sua media foi A")
elif media >= 7.5:
    print("Sua media foi B")
elif media >= 6.0:
    print("Sua media foi C")
elif media >= 4.0:
    print("Sua media foi D")
else:
    print("Sua media foi E")
