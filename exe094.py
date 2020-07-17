totalidade = 0
pessoas = []
dados = {}
while True:
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('Erro, digite apenas M ou F!')
    dados['idade'] = int(input('Idade: '))
    totalidade += dados['idade']
    pessoas.append(dados.copy())
    dados.clear()
    while True:
        s_ou_n = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
        if s_ou_n in 'SN':
            break
        print('Erro, digite apenas S ou N!')
    if s_ou_n == 'N':
        break
media = totalidade/len(pessoas)
print('=-'*30)
print(f'Foram cadastradas no total {len(pessoas)} pessoas.')
print(f'A média das idades é {media:5.2f} anos.')
print('As pessoas de sexo feminino são:',end=' ')
for i, v in enumerate(pessoas):
    if 'F' in v['sexo']:
        print(f'{v["nome"]}',end=' ')
print('\nLista de pessoas que estão acima da média de idade:')
for i, v in enumerate(pessoas):
    if v['idade'] >= media:
        print()
        print(f'Nome = {v["nome"]}; Sexo = {v["sexo"]}; Idade = {v["idade"]}')
print('Finalizando...')

