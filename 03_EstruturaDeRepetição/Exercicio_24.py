print('### media de N numeros ###')
totalNotas=float(input('Informe o total de notas que você quer calcular: '))
cont=1
media=soma=0
while cont <= totalNotas:
    nota=float(input('Informe a {}ª nota:'.format(cont)))
    cont+=1
    soma+=nota
media=soma/totalNotas
print('A média é {:.2f}'.format(media))
