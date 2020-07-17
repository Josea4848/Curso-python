distancia = float(input('Qual a distância da viagem: '))
preço1 = distancia * 0.50
preço2 = distancia * 0.45
if distancia > 200:
    print(f'O preço de sua viagem será de R${preço2:.2f}')
else:
    print(f'O preço da viagem será de R${preço1:.2f}')

