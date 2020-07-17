from random import randint
vitorias = 0
while True:
    e_pc = randint(0,11)
    print('='*5,'PAR OU ÍMPAR','='*5)
    e_player = int(input('Digite um número: '))
    soma = (e_pc + e_player)
    par_impar = str(input('DESEJA PAR OU ÍMPAR [P/I]: ')).upper().strip()[0]
    while par_impar not in 'PI':
        par_impar = str(input('DESEJA PAR OU ÍMPAR [P/I]: ')).upper().strip()[0]
    print(f'Você jogou {e_player} e o computador {e_pc}. Total de {soma}')
    if par_impar == 'P':
        if soma % 2 == 0:
            vitorias += 1
            print('\033[32mVocê ganhou um ponto!\033[m')
        else:
            print('\033[31mVocê perdeu!\033[31m')
            break
    if par_impar == 'I':
        if soma % 2 != 0:
            print('\033[32mVocê ganhou um ponto!\033[m')
            vitorias += 1
        else:
            print('\033[31mVocê perdeu!\033[31m')
            break
print(f'GAME OVER!\033[m Você ganhou {vitorias} vez(es)!')

