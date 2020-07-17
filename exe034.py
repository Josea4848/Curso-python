sal = float(input('Digite o valor do salário:R$'))
if sal > 1250:
    taxa = 10
    amt = sal + ((10 / 100) * sal)  # Calculando aumento de 10%
else:
    taxa = 15
    amt = sal + ((15 / 100) * sal)  # Calculando aumento de 15%
print(f'O aumento foi de {taxa}% e o salária será de R${amt:.2f}')


