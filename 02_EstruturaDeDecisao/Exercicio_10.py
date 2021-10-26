print("#### Identificador de Sexo ####")
valor = (input("selecione o Turno que você estuda:\n[M]Matutino ou [V]Vespertino ou [N]Noturno: \n")).upper()

if valor == "M":
    print("Bom dia!")
elif valor == "V":
    print("Boa Tarde!")
elif valor == "N":
    print("Boa Noite!")
else:
    print("Valor inválido.")