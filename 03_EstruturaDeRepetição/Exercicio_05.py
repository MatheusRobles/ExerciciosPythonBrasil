while(True):
  populacao_A = float(input("Digite o valor inicial da população A:\n"))
  populacao_B = float(input("Digite o valor inicial da população B:\n"))
  taxa_A = float(input("Digite a taxa de crescimento da população A:\n"))
  taxa_B = float(input("Digite a taxa de crescimento da população B:\n"))
  ano = 0
  if((populacao_A > 0) and (populacao_B > 0) and (taxa_A > 0) and (taxa_B > 0) and (populacao_B > populacao_A) and (taxa_B < taxa_A)):
      while(populacao_B >= populacao_A):
        populacao_A *=  taxa_A
        populacao_B *=  taxa_B
        ano += 1
        print(f' A:{populacao_A} B:{populacao_B} ano:{ano}')
      print(f'quantidade de anos:{ano}')
      break
  else:
      print("valores invalidos, tente novamente.\n")