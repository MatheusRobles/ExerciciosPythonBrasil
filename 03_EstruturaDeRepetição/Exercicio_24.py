print('### media de N numeros ###')
continuar = True
lista = []
while(continuar):
  numero = int(input("insira um numero:\n"))
  lista.append(numero)

  continua = input("Deseja inserir mais numeros?\n[S]Sim / [N]Não\n").upper()
  if (continua == 'N'):
    continuar = False
  else:
    continuar = True

soma = sum(lista)
media = soma/(len(lista))
print('A media dos numeros é {}'.format(media))
