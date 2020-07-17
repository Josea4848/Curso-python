from random import randint
from time import sleep
from operator import itemgetter
sorteio = {}
ranking = list()
for c in range(1,5):
    sorteio[f'Jogador {c}'] = randint(1,6)
for k, v in sorteio.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(0.876)
ranking = sorted(sorteio.items(), key=itemgetter(1), reverse=True)
print(ranking)
print('='*5,'RANKING','='*5)
for p, v in enumerate(ranking):
    print(f'{p + 1}º posição: {v[0]} com {v[1]}')
    sleep(0.876)




