from time import sleep
while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    if n < 0:
        break
    print('=' * 5, 'Tabuada', '=' * 5)
    for c in range (1,11):
        print(f'{n} x {c:2} = {n * c}')
print('PROGRAMA TABUADA sendo encerrado...')
sleep(2)
