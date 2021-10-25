print("##Calculo multa sobre peso excedente##")
peso = float(input("Digite o peso do peixe: \n"))
excesso = peso-50
if excesso>0:
    multa = excesso*4
    print("O excesso de peso registrado para esse peixe é de:", excesso, "Kg")
    print("O valor da multa a ser pago é de:", multa, "R$")
else:
    print("Não há excesso de peso")
