print("leitor de unidades, dezenas e centenas")
valor = (input("Digite um numero inteiro menor que 1000:\n"))
digitos = len(valor)
saida = valor + ' = '
centena = dezena = unidade = ''
Valido = True

def find_centena(saida, centena):
    if int(centena) > 1:
        frase = saida + centena + ' centenas'
    elif int(centena) == 1:
        frase = saida + centena + ' centena'
    else:
        frase = saida
    return frase


def find_dezena(saida, dezena):
    if int(dezena) > 1:
        frase = saida + dezena + ' dezenas'
    elif int(dezena) == 1:
        frase = saida + dezena + ' dezena'
    else:
        frase = saida
    return frase


def find_unidade(saida, unidade):
    if int(unidade) > 1:
        frase = saida + unidade + ' unidades'
    elif int(unidade) == 1:
        frase = saida + unidade + ' unidade'
    else:
        frase = saida
    return frase

if digitos == 3:
    centena = valor[0]
    dezena = valor[1]
    unidade = valor[2]
    saida = find_centena(saida, centena)
    if int(dezena) != 0 and int(unidade) != 0:
        saida = saida + ', '
    elif int(dezena) != 0 or int(unidade) != 0:
        saida = saida + ' e '
    saida = find_dezena(saida, dezena)
    if int(dezena) != 0 and int(unidade) != 0:
        saida = saida + ' e '
    saida = find_unidade(saida, unidade)
elif digitos == 2:
    dezena = valor[0]
    unidade = valor[1]
    saida = find_dezena(saida, dezena)
    if int(unidade) != 0:
        saida = saida + ' e '
    saida = find_unidade(saida, unidade)
elif digitos == 1 and int(valor) != 0:
    unidade = valor[0]
    saida = find_unidade(saida, unidade)
else:
    Valido = False

if Valido:
    print(saida)
else:
    print("Valor invalido")
