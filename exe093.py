contador = 0
listadegols = list()
dados = {}
dados['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
for c in range(0,partidas):
    gol = int(input(f'Quantos gols {dados["Nome"]} fez na {c + 1}º partida?'))
    listadegols.append(gol)
    contador += gol
dados['Gols'] = listadegols[:]
dados['totais'] = contador
print('=-'*30)
print(f'O jogador {dados["Nome"]} jogou {partidas} partidas.')
for i, g in enumerate(dados['Gols']):
    print(f'   => Na {i + 1}º partida, fez {g} gol(s).')
print(f'Foi um total de {contador} gols.')

