numeros = list()
numeros_par = list()
numeros_impar = list()
while True:
    numeros.append(int(input('Digite um valor: ')))
    perg = str(input('Quer continuar [S/N]: ')).strip()[0].upper()
    if perg == 'N':
        break
for c, valor in enumerate(numeros):
    print(valor)
    if valor % 2 == 0:
        numeros_par.append(valor)
    else:
        numeros_impar.append(valor)
print(f'Os números digitados foram {numeros}')
print(f'Os valores pares foram {numeros_par}')
print(f'Os valores ímpares foram {numeros_impar}')


