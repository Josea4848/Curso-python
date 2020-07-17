listacompleta = list()
dados = list()
leve = 0
pesada = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso:')))
    print(dados)
    if len(listacompleta) == 0:
        leve = pesada = dados[1]
    else:
        if dados[1] > pesada:
            pesada = dados[1]
        if dados[1] < leve:
            leve = dados[1]
    listacompleta.append(dados[:])
    dados.clear()
    s_ou_n = str(input('Deseja continuar[S/N]? ')).strip().upper()[0]
    if s_ou_n == 'N':
        break
print(f'Ao todo foram cadastradas {len(listacompleta)} pessoas')
print(f'As pessoas mais pesadas pesam {pesada}Kg')
for p in listacompleta:
    if p[1] == pesada:
        print(p[0])
print(f'A pessoa mais leve pesa {leve}Kg')
for p in listacompleta:
    if p[1] == leve:
        print(p[0])
