números = tuple(int(input(f'Digite o {i+1}º numero: ')) for i in range(4))
print(f'Você digitou os números {números}')
print(f'O número 9 aparece {números.count(9)} vez(es)')
if 3 in números:
    print(f'O valor 3 foi digitado primeiramente na posição {números.index(3)}')
else:
    print('Não teve 3 digitado!')
print('Os valores pares foram:',end=' ')
for t in números:
    if t % 2 == 0:
        print(t,end=' ')
