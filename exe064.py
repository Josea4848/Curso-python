print('Para finalizar o progama digite \033[34m999\033[m')
cont = soma = n = 0
n = int(input('Digite um número: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número: '))
print(f'Foram digitados {cont} número(s) e a soma entre eles foi {soma}')

