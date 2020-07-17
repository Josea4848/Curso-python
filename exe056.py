soma = 0
media = 0
maiorm = 0
nomev = ''
totmulher = 0
for p in range(1, 5):
    print('='*5,f'{p}ª Pessoa','='*5)
    nome = str(input(f'Digite o nome: ')).strip()
    ida = int(input(f'Digite a idade: '))
    sexo = str(input(f'Digite o sexo [M/F]: ')).strip().upper()
    soma = soma + ida
    if p == 1 and sexo == 'M':
        maiorm = ida
        nomev = nome
    if 'M' in sexo and ida > maiorm:
        maiorm = ida
        nomev = nome
    if 'F' in sexo and ida < 20:
        totmulher += 1
media = soma/4
print(f'A média de idade do grupo é {media} anos.')
print(f'O homem mais velho tem {maiorm} anos e se chama {nomev}')
print(f'Ao todo são {totmulher} mulheres menore(s) de 20 anos')
