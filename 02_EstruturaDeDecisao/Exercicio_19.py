print("leitor de unidades, dezenas e centenas")
valor = (input("Digite um numero inteiro menor que 1000:\n"))
digitos = len(valor)
saida = valor  + ' = '


def find_Centena(saida, centena):
  if int(centena) > 1:
      frase = saida + centena + ' centenas'
  else:
      frase = saida + centena + ' centena'
  return frase


def find_Dezena(saida, dezena):
  if int(dezena) > 1:
      frase = saida + dezena + ' dezenas'
  else:
      frase = saida + dezena + ' dezena'
  return frase


def find_Unidade(saida, unidade):
  if int(unidade) > 1:
      frase = saida + unidade + ' unidades'
  else:
      frase = saida + unidade + ' unidade'
  return frase

saida = saida + ' = '
if digitos == 3:
    centena = valor[0]
    dezena = valor[1]
    unidade = valor[2]
    saida = find_Centena(saida, centena)
    saida = saida + ', '
    saida = find_Dezena(saida, dezena)
    saida = saida + ' e '
    saida = find_Unidade(saida, unidade)
elif digitos == 2:
    dezena = valor[0]
    unidade = valor[1]
    saida = find_Dezena(saida, dezena)
    saida = saida + ' e '
    saida = find_Unidade(saida, unidade)
elif digitos == 1:
    unidade = valor[0]
    saida = find_Unidade(saida, unidade)
else:
    print("Valor invalido")
    invalido = True

print(saida)
