cont = total = menor = cont1 = nomem =   0
while True:
    nome = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o preço do produto: '))
    cont1 += 1
    if cont1 == 1:
        menor = preço
        nomem = nome
    if preço > 1000:
        cont += 1
    if preço < menor:
        menor = preço
        nomem = nome
    total += preço
    s_ou_n = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    while s_ou_n not in 'SN':
        s_ou_n = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if s_ou_n == 'N':
        break
print(f'O gasto total será de R${total:.2f}')
print(f'{cont} produto(s) custam mais de R$1000,00')
print(f'O produto mais barato foi a/o {nomem} custando R${menor:.2f}')
