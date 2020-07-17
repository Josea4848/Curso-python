from random import randint
#O pc escolhe 5 números aleatórios de 0 á 9
Sorteio = randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9)
print('Os números sorteados foram:',end=' ')
for n in Sorteio:
    print(n, end=', ')
#tem essa forma > print(f'\nO maior valor foi {sorted(Sorteio)[-1]} e o menor valor foi {sorted(Sorteio)[0]}')
#e essa:
print(f'\nO maior valor foi {max(Sorteio)}')
print(f'O menor valor foi {min(Sorteio)}')
