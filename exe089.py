listafinal = list()
listamedia = list()
listatemp = list()
while True:
    nome = str(input('Nome: '))
    listatemp.append(nome)
    nota1 = float(input('Nota 1: '))
    listatemp.append(nota1)
    nota2 = float(input('Nota 2: '))
    listatemp.append(nota2)
    listamedia.append((nota1 + nota2)/2)
    listafinal.append(listatemp[:])
    listatemp.clear()
    s_ou_n = str(input('Deseja continuar[S/N]? ')).strip().upper()[0]
    if s_ou_n == 'N':
        break
print('\033[1mN.  Nome                   Média\033[m')
for c in range(0,len(listafinal)):
    print(f'{c}   {listafinal[c][0]:<20}   {listamedia[c]}')
while True:
    mostrarnotas = int(input('Mostrar notas de qual aluno(999 interrompe): '))
    if mostrarnotas < len(listamedia):
        print(
            f'As notas de {listafinal[mostrarnotas][0]} são {listafinal[mostrarnotas][1]} e {listafinal[mostrarnotas][2]}')
    if mostrarnotas == 999:
        break
    if mostrarnotas >= len(listamedia) and mostrarnotas != 999:
        print('\033[31mDigite um número válido\033[m')

