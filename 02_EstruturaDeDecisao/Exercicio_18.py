print("##Data Valida##")
data=(input("Insira uma data nesse formato dd/mm/aaaa:\n"))
listaData = []
listaData = data
dia = int(listaData[0:2])
mes = int(listaData[3:5])
ano = int(listaData[6:])

validaDia = True
validaMes = True

if len(listaData) == 10:
    bissexto = False
    if ano % 4 == 0:
        bissexto = True
    else:
        bissexto = False

    if (mes not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)):
        validaMes = False
    else:
        if (mes in (1, 3, 5, 7, 8, 10, 12)):
            if (dia < 1) or (dia > 31):
                valida = False
        elif (mes in (4, 6, 9, 11)):
            if (dia < 1) or (dia > 30):
                valida = False
        else:
            if (bissexto):
                if (dia < 1) or (dia > 29):
                    valida = False
            else:
                if (dia < 1) or (dia > 28):
                    valida = False

    if (validaDia and validaMes):
        print ('Data VALIDA')
    else:
        print ('Data INVALIDA')
else:
    print ('Data INVALIDA')