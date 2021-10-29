print('### Caixa Eletronico ###')
valor = int(input("Qual o valor do Saque?"))

if valor >= 10 and valor <= 600:
    notas_100 = valor // 100
    notas_50 = (valor % 100) // 50
    notas_10 = ((valor % 100) % 50) // 10
    notas_5 = (((valor % 100) % 50) % 10) // 5
    notas_1 = ((((valor % 100) % 50) % 10) % 5) // 1
    saida = (f'Para sacar a quantia de {valor} reais, serão fornecidas ')

    valida = 0
    if notas_100 > 0:
        valida += 1
    if notas_50 > 0:
        valida += 1
    if notas_10 > 0:
        valida += 1
    if notas_5 > 0:
        valida += 1
    if notas_1 > 0:
        valida += 1

    if notas_100 > 0:
        if notas_100 == 1:
            saida = saida + (f'{notas_100} nota de 100 ')
        else:
            saida = saida + (f'{notas_100} notas de 100 ')

        if valor % 100 > 0 and valida > 2:
            saida = saida + ", "
            valida -= 1
        elif valor % 100 > 0:
            saida = saida + "e "

    if notas_50 > 0:
        if notas_50 == 1:
            saida = saida + (f'{notas_50} nota de 50 ')
        else:
            saida = saida + (f'{notas_50} notas de 50 ')

        if valor % 50 > 0 and valida > 2:
            saida = saida + ", "
            valida -= 1
        elif valor % 50 > 0:
            saida = saida + "e "

    if notas_10 > 0:
        if notas_10 == 1:
            saida = saida + (f'{notas_10} nota de 10 ')
        else:
            saida = saida + (f'{notas_10} notas de 10 ')
        if valor % 10 > 0 and valida > 2:
            saida = saida + ", "
            valida -= 1
        elif valor % 10 > 0:
            saida = saida + "e "

    if notas_5 > 0:
        if notas_5 == 1:
            saida = saida + (f'{notas_5} nota de 5 ')
        else:
            saida = saida + (f'{notas_5} notas de 5 ')
        if notas_1 > 0:
            saida = saida + "e "
    if notas_1 > 0:
        if notas_1 == 1:
            saida = saida + (f'{notas_1} nota de 1 ')
        else:
            saida = saida + (f'{notas_1} notas de 1 ')
    print(saida)



else:
    print('O valor não é valido')