from time import sleep
valor =  float(input('Qual o valor da Casa? R$'))#Pergutando o valor da casa
sal = float(input('Qual o seu salária? R$'))#Perguntando o Salário
anos = int(input('Em quantos anos você vai pagar? '))#Perguntando em quantos ano irá pagar
taxa = (30/100)*sal#Calculando porcentagem
prestaçao = valor/(anos*12)#Quanto será pago por mês
print('Aguarde...')
sleep(2)
if prestaçao <= taxa:
    print(f'\033[1;32mSeu empréstimo foi aprovado, a prestação mensal será de R${prestaçao:.2f}')
else:
    print(f'\033[31mO seu empréstimo foi negado!\033[30m Para pagar uma casa de R${valor:.2f} em {anos} anos', end=' ')
    print(f'a prestação seria de \033[34mR${prestaçao:.2f}')
print('\033[30mTenha um bom dia!')


