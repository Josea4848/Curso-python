from time import sleep
velocidade = float(input('Qual a velocidade(km/h) atual do carro: ' ))
multa = float(velocidade-80)*7
print('Processando...')
sleep(2)
if velocidade > 80:
    print(f'MULTADO! você excedeu o limite de 80km/h!\ne sua multa será de R${multa:.2f}')
else:
    print('Você não excedeu o limite de 80km/h!')
print('Tenha um bom dia e dirija com segurança!')






