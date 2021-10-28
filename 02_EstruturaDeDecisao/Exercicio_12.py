print("#### Calculo folha de pagamento ####")
valorHora = float(input("Digite o valor da sua hora de trabalho:\n"))
horasTrabalhadas = float(input("Digite o numero de horas trabalhadas no mes:\n"))
salarioBruto = valorHora * horasTrabalhadas

def imposto_de_renda(salarioBruto):
    if  salarioBruto <= 0:
        print("Valor inválido.")
    elif salarioBruto <= 900.00:
        porcentagem=0
        IR=0
    elif salarioBruto <= 1500.00:
        porcentagem=0.05
        IR=salarioBruto*porcentagem
    elif salarioBruto <= 2500.00:
        porcentagem=0.10
        IR=salarioBruto*porcentagem
    else:
        porcentagem=0.20
        IR=salarioBruto*porcentagem
    return IR, porcentagem

def sindicato(salarioBruto):
    valorSindicato = salarioBruto * 0.03
    return valorSindicato

def FGTS(salarioBruto):
    valorFGTS = salarioBruto * 0.11
    return valorFGTS

def salario_liquido(salarioBruto, valorSindicato, IR):
    salario = salarioBruto - valorSindicato - IR
    return salario

def descontoTotal(salarioBruto, IR, valorSindicato):
    desconto = salarioBruto - salario
    return desconto

IR, porcentagem = imposto_de_renda(salarioBruto)
valorSindicato = sindicato(salarioBruto)
valorFGTS = FGTS(salarioBruto)
salario = salario_liquido(salarioBruto, valorSindicato, IR)
desconto = descontoTotal(salarioBruto, IR, valorSindicato)

print ('Salário Bruto ({:.2f} * {:2.0f})        R$ {:8.2f}'.format(valorHora,horasTrabalhadas, salarioBruto))
print ('(-) IR {:2.0f}%:                        R$ {:8.2f}'.format((porcentagem*100),IR))
print ('(-) Sindicato ( 3 %):              R$ {:8.2f}'.format(valorSindicato))
print ('FGTS ( 11 %):                      R$ {:8.2f}'.format(valorFGTS))
print ('Total de Descontos:                R$ {:8.2f}'.format(desconto))
print ('Salario Liquido:                   R$ {:8.2f}'.format(salario))