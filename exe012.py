p = float(input('Digite o preço do produto: R$'))
d = float(input('Digite o valor do desconto(%): '))
dv = p-(d/100)*p
print(f'O produto que custava R${p}, Com {d}% de desconto o produto custará R${dv:.2f}')



