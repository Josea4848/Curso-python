números = 'Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quartoze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte'
while True:
    escolha = int(input('Digite um número de 0 á 20: '))
    if 0<= escolha <= 20:
        break
    print('Tente novamente.',end=' ')
print(f'Você digitou o número {números[escolha]}')
