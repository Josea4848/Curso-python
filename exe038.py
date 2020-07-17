numero1 = int(input('\033[31mDigite um número inteiro: '))
numero2 = int(input('\033[32mDigite outro número inteiro: '))
if numero1 > numero2:
    print(f'\033[mO número \033[31m{numero1} \033[mé maior que o número \033[32m{numero2}')
elif numero2 > numero1:
    print(f'\033[mO número \033[32m{numero2} \033[mé maior que o número \033[31m{numero1}')
elif numero1 == numero2:
    print(f'\033[mOs números \033[31m{numero1} \033[me \033[32m{numero2} \033[msão iguais')
