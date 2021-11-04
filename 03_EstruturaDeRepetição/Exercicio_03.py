nome = input("Digite um nome com mais de 3 caracteres:\n")
if (len(nome) >= 3):
    print("nome ok")
idade = input("Digite uma idade de 0 a 150:\n")
if (int(idade) >= 0 and int(idade) <= 150):
    print("idade ok")
salario = input("Digite um salario maior que 0:\n")
if (int(salario) > 0):
  print("salario ok")
sexo = input("Selecione um sexo:\n[f]feminino ou [m]masculino\n").upper()
print(sexo)
if(sexo == 'M' or sexo == 'F'):
  print('sexo ok')
estado_civil = input("Selecione um estado civil:\n[s] [c] [v] [d]\n").lower()
if 'scvd'.find(estado_civil) >= 0:
  print('estado civil ok')