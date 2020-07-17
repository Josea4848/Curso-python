listafinal = list()
contgol = 0
listadegols = list()
dados = {}
while True:
    contgol = 0
    dados['Nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou?'))
    for c in range(0, partidas):
        gol = int(input(f'Quantos gols {dados["Nome"]} fez na {c+1}º partida?'))
        contgol += gol
        listadegols.append(gol)
    dados['Gols'] = listadegols[:]
    dados['Total'] = contgol
    listafinal.append(dados.copy())
    listadegols.clear()
    dados.clear()
    while True:
        s_ou_n = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if s_ou_n not in 'SN':
            print('ERRO, digite apenas S ou N!')
        else:
            break
    if s_ou_n == 'N':
        break
print('=-'*30)
print(f'{"Cód.":<5}{"Nome":<12}{"Gols":<23}{"Total"}')
for i, v in enumerate(listafinal):
    print(f'{i:>3}  {v["Nome"]:<12}{str(v["Gols"]):<23} {v["Total"]}')
while True:
    while True:
        perg = int(input('Mostrar dados de qual jogador[999 imterrompe]: '))
        if perg >= len(listafinal) and perg != 999:
                print('Digite um código válido')
        else:
          break
    if perg == 999:
        break
    print(f'--Mostrando dados do {listafinal[perg]["Nome"]}')
    for c in range(0,len(listafinal[perg]['Gols'])):
        print(f'No jogo {c} fez {listafinal[perg]["Gols"][c]} gols.')
    print("="*30)
