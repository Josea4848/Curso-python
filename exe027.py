nome = str(input('Digite seu nome completo: ')).strip()
print('Prazer em conhece-lo!')
nomed = nome.split()
print(f'O seu primeiro nome é {nomed[0]}')
print(f'O seu último nome é {nomed[len(nomed)-1]}')

