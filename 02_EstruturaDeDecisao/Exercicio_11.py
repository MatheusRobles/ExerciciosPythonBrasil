def salario_atual(porcentagem, salario):
  salarioAtual = salario * porcentagem
  return salarioAtual

def valor_aumento(salarioAtual, salario):
  aumento = salarioAtual - salario
  return aumento

def exibir(salario, porcentagem, aumento, salarioAtual):
  print("\nSalario antes do reajuste:\n{:.2f}R$".format(salario))
  print("\nO porcentual do aumento é de:\n{:.0f}%".format((porcentagem*100)-100))
  print("\nO valor do aumento foi de:\n{:.2f}R$".format(aumento))
  print("\nValor do novo salario a ser recebido:\n{:.2f}R$".format(salarioAtual))

print("#### Reajuste Salarial ####")
salario = float(input("Digite o salario atual:\n"))

if salario <= 0:
  print("Valor inválido.")

elif (salario <= 280.00):
  porcentagem = 1.20
  salarioAtual=salario_atual(porcentagem, salario)
  aumento=valor_aumento(salarioAtual, salario)
  exibir(salario, porcentagem, aumento, salarioAtual)

elif salario <= 700.00:
  porcentagem = 1.15
  salarioAtual=salario_atual(porcentagem, salario)
  aumento=valor_aumento(salarioAtual, salario)
  exibir(salario, porcentagem, aumento, salarioAtual)
elif salario <= 1500.00:
  porcentagem = 1.10
  salarioAtual=salario_atual(porcentagem, salario)
  aumento=valor_aumento(salarioAtual, salario)
  exibir(salario, porcentagem, aumento, salarioAtual)
elif salario > 1500.00:
  porcentagem = 1.05
  salarioAtual=salario_atual(porcentagem, salario)
  aumento=valor_aumento(salarioAtual, salario)
  exibir(salario, porcentagem, aumento, salarioAtual)
else:
  print("Valor inválido.")
