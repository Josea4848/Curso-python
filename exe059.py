from time import sleep
n1 = int(input('Digite o \033[4;34m1\033[34mº \033[mvalor: '))
n2 = int(input('Digite o \033[4;34m2\033[34mº \033[mvalor: '))
opção = 0
while opção != 5:
    print("""    \033[1m[1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair""")
    opção = int(input('\033[34mOpção: '))
    if opção > 5 or opção < 1:
        print('\033[31mOpção inválida. Tente Novamente')
    if opção == 1:
        print(f'\033[4;32mSoma: {n1 + n2}')
    if opção == 2:
        print(f'\033[4;32mMultiplicação: {n1 * n2}')
    if opção == 3:
        maior = 0
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'\033[4;32mMaior número: {maior} ')
    if opção == 4:
        n1 = int(input('\033[mDigite o \033[4;34m1\033[34mº \033[mvalor: '))
        n2 = int(input('Digite o \033[4;34m2\033[34mº\033[mvalor: '))
    print('\033[m=-'*20)
print('Finalizando processo...')
sleep(2)
