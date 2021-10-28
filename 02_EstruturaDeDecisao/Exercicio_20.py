print("### Media de 3 notas ###")
nota1 = float(input("Digite a primeira nota: \n"))
nota2 = float(input("Digite a segunda nota: \n"))
nota3 = float(input("Digite a terceira nota: \n"))

media = (nota1+nota2+nota3)/3

if media == 10:
  print("Aprovado com Distinção")
elif media >= 7:
  print("Aprovado")
else:
  print("Reprovado")
