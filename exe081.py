número = list()
while True:
    num = int(input('Digite um número: '))
    número.append(num)
    pergunta = str(input('Deseja continuar[S/N]: '))
    if pergunta == 'N':
        break
print(f'Foram digitados {len(número)} valores')
print(f'Essa lista em ordem decrescente fica {sorted(número, reverse= True)}')
if 5 in número:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')