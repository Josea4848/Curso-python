tupla = 'Jaca', 'Python', 'Bola'
for x in range(0,len(tupla)):
    print(f'Na palavra {tupla[x]} temos:')
    for vogal in tupla[x]:
        if vogal in 'aeiou':
            print(vogal)
