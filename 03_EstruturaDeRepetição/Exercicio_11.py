num1 = int(input('Digite um numero inteiro:\n'))
num2 = int(input('Digite outro numero inteiro:\n'))
soma = 0

if num1 < num2:
  for i in range(num1,num2):
    print(i)
    soma += i
else:
  for i in range(num2,num1):
    print(i)
    soma += i

print('soma: {}'.format(soma))