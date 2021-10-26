print("#### Identificador de Sexo ####")
sexo = (input("selecione um sexo:\n[F]Feminino ou [M]Masculino: \n")).upper()

if sexo == "F":
    print("Você selecionou o sexo Feminino.")
elif sexo == "M":
    print("Você selecionou o sexo Masculino.")
else:
    print("Sexo inválido.")
