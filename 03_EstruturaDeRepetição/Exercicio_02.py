usuario = senha = ""
while(usuario == senha):
  usuario = input("Digite um nome de usuario:\n")
  senha = input("Digite uma senha:\n")
  if( senha == usuario):
    print("\nA senha deve ser diferente do usurio, tente novamente.")
