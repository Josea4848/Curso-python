primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 0
while cont <= 9:
    print(f'{termo} > ', end=(' '))
    termo = termo + razao
    cont += 1
print('Fim')
