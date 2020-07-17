from random import randint
print('='*5,'\033[1;34mJogo Do Adivinha\033[m','='*5)
print('Vou pensar em número entre 0 e 10 e Você terá que adivinhar!')
s = randint(1,9)
cont = 0
palpite = int(input('Qual número eu pensei: '))
while palpite != s:
    palpite = int(input('\033[31mERROU, \033[mTENTE NOVAMENTE: '))
    cont += 1
if cont == 0:
    print('\033[32mVOCÊ ACERTOU DE PRIMEIRA!')
if cont > 0:
    print(f'\033[32mAcertou!! \033[34mDepois de {cont} palpites')
