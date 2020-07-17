from math import factorial
n = int(input('Digite um número: '))
c = n
f = 1
print(f'\033[31mCalculando fatorial de {n}!\033[m = ',end=(' '))
while c > 0:
    print(f'{c}',end=(' '))
    if c > 1:
        print('x',end=(' '))
    else:
        print('=',end=(' '))
    c -= 1
print(factorial(n))