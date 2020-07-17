import datetime
dados = {}
dados['Nome'] = str(input('Nome: '))
dados['Idade'] = datetime.date.today().year - int(input('Ano de nascimento: '))
dados['CTPS'] = int(input('Carteira de trabalho [0, caso não tenha]: '))
if dados['CTPS'] != 0:
    dados['Ano de contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: '))
    Anosrestantes = 35 - (datetime.date.today().year - dados['Ano de contratação'])
    dados['Idade de aposentadoria'] = dados['Idade'] + Anosrestantes
for k, v in dados.items():
    if k == 'Salário':
        print(f'{k}: R${v:.2f}')
    else:
        print(f'{k}: {v}')
