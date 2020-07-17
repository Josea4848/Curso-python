soma = 0
cont = 0
for c in range(1,7):
    n= int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        cont += 1
        soma += n
print(f'Você informou {cont} número(s) par(es), e a soma entre todos eles é {soma}')

