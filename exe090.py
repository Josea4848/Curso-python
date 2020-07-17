dados = {}
dados['Nome'] = str(input('Nome: '))
dados['Média'] = float(input(f'Média de {dados["Nome"]}: '))
if dados['Média'] < 7:
    dados['situação'] = 'Reprovado'
else:
    dados['situação'] = 'Aprovado'
for k, v in dados.items():
    print(f'{k} é igual a {v}')
