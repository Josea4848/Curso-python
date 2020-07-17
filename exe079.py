números = list()
while True:
    valor = int(input('Digite um valor: '))
    if valor not in números:
        números.append(valor)
    else:
        print('Número duplicado não será adicionado')
    s_ou_n = str(input('Deseja continuar[S/N]: ')).strip()[0].upper()
    if s_ou_n == 'N':
        break
print(f'Os valores digitados foram {sorted(números)}')

