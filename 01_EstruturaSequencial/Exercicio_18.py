print("##velocidade de download##")
tamanho = float(input("Digite o tamanho do arquivo para download em MB: \n"))
velocidade = float(input("Digite a velocidade da internet em  Mbps : \n"))
velocidadeDownload = velocidade * 0.125
tempo = (tamanho/velocidadeDownload)/60
print("o tempo de download do arquivo é de ", tempo, "minutos")