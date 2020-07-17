numero = int(input('Digite o número: '))
tot = 0
for c in range (1, numero + 1):
    if numero % c == 0:
        print(f'\033[34m{c}', end=' ')
        tot += 1
    else:
        print(f'\033[31m{c}',end=' ')
print(f'\n\033[mO número {numero} é divisivel {tot} vezes')
if tot > 2:
    print('Portanto este número não é primo')
else:
    print('Portanto o número é primo')
