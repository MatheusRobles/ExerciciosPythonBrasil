print("### 5 perguntas sobre o crime ###")
print("responda com [sim] ou [não]")
culpado = 0
dado = (input("Telefonou para a vítima?\n")).upper()
if dado == 'SIM':
  culpado += 1
dado = (input("Esteve no local do crime?\n")).upper()
if dado == 'SIM':
  culpado += 1
dado = (input("Mora perto da vítima?\n")).upper()
if dado == 'SIM':
  culpado += 1
dado = (input("Devia para a vítima?\n")).upper()
if dado == 'SIM':
  culpado += 1
dado = (input("Já trabalhou com a vítima??\n")).upper()
if dado == 'SIM':
  culpado += 1

if culpado == 5:
  print("Assassino")
elif 3 <= culpado <=4:
  print("Cúmplice")
elif culpado == 2:
  print("Suspeito")
else:
  print("Inocente")


