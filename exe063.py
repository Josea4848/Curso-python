print('_'*30)
print('\nSequência de Fibonacci')
print('_'*30)
termo = int(input('Digite quantos termos você quer mostrar: '))
t1 = 0
t2 = 1
print(f'{t1} ➞ {t2}', end=' ')
cont = 3
while cont <= termo:
    t3 = t1 + t2
    print(f'➞ {t3}', end=' ')
    t1 = t2
    t2 = t3
    t3 = t1 + t2
    cont += 1