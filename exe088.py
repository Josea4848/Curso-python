from time import sleep
from random import randint
print('='*5, 'Sorteador mega-sena','='*5)
quantidade = int(input('Quantos jogos deseja sortear? '))
print('='*5,f'Sorteando {quantidade} jogo(s)','='*5)
lista = list()
contador1 = 1
jogos = list()
while contador1 <= quantidade:
    contador2 = 0
    while True:
        sorteio = randint(1,60)
        if sorteio not in lista:
            lista.append(sorteio)
            contador2 += 1
        if contador2 >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    contador1 += 1
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print('='*31)

