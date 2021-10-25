print("##salario no mes referido##")
salarioH = float(input("Digite o salario recebido por hora: \n"))
horasTrabalhadas = float(input("Digite a quantidade de horas trabalhadas no mes: \n"))
salarioRecebido = salarioH*horasTrabalhadas
print("Salário Bruto", salarioRecebido, "R$")
print("IR", 0.11*salarioRecebido, "R$")
print("INSS", 0.08*salarioRecebido, "R$")
print("Sindicato", 0.05*salarioRecebido, "R$")
print("Salário Liquido", 0.76*salarioRecebido, "R$")