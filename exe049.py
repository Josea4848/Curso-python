n = int(input('Escolha um número: '))
print('='*5,'TABUADA','='*5)
for c in range (1, 11):
    tab = n * c
    print(f'{n} x {c:2} = {tab}')
print('='*19)
