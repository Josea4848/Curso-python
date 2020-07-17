listafinal = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota2 + nota1) / 2
    listafinal.append([nome, [nota1, nota2], media])
    s_ou_n = str(input('Quer continuar[S/N]?')).strip().upper()[0]
    if s_ou_n == 'N':
        break
print('=' * 30)
print(f'{"N.º":<4}{"Nome":<10}{"Média"}')
for c in range(0, len(listafinal)):
    print(f'{c:<4}{listafinal[c][0]:<10}{listafinal[c][2]:>5.1f}')
while True:
    n = int(input('Mostrar as notas de qual aluno (999 interrompe): '))
    if n < len(listafinal):
        print(f'As notas de {listafinal[n][0]} foram {listafinal[n][1]}')
    if n >= len(listafinal) or n < 0 and n!= 999:
        print('Número inválido! Digite um número correspondente ao aluno!')
    if n == 999:
        print('Finalizando...')
        break

