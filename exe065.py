soma = cont = média = maior = menor =  0
decisão = 'S'
while decisão == 'S':
    n = int(input('Digite um número: '))
    decisão = str(input('Quer continuar? [S/N] ')).upper()
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if  n < menor:
            menor = n
média = soma / cont
print(f'Você digitou {cont} número(s) e a média foi {média}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')
