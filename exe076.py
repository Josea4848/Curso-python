total = 0
listagem = ('Coca-cola',8,'Biscoito',1.50,
          'Arroz',675,'Feijão',3.50)
print(f'{"LISTAGEM":=^40}')
for c in range(0,len(listagem)):
    if c % 2 == 0:
        print(f'{listagem[c]:.<30}',end='')
    else:
        print(f'R${listagem[c]:>7.2f}')
print('='*40)

