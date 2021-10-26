print("#### Identificador vogal/consoante ####")
Letra = (input("Digite uma Letra:\n")).upper()

if 'AEIOU'.find(Letra) >= 0:
    print("A letra digitada é uma vogal.")
elif len(Letra) == 1 and ('123456789!@#$%¨&*()-=*+/?;:.,><'.find(Letra) < 0):
    print("A letra digitada é uma consoante.")
else:
    print("Letra inválido.")
