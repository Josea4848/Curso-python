from random import randint
from time import sleep
import playsound
n = randint(0,5) #Computador está selecionando um número!
print('\033[33m=-'*5,'Jogo do adivinha','=-'*5)
print('\033[2;30mVou escolher um número de 0 á 5, e Você terá que adivinhar!\033[m')
print('\033[36mPensando...\033[m')
sleep(4)
resposta = int(input('\033[32mDigite qual número eu pensei: \033[m'))#Jogador tenta adivinhar qual número
print('\033[35m=\033[m'*20)
print('\033[30mE Você...')
sleep(2)
if resposta == n:
    print(f'\033[1;32mACERTOU! o número é \033[1m{n}!'), playsound.playsound('exe028acertou.mp3')
    print('\033[36mPARABÉNS! MAS DESTA VEZ VOCÊ TEVE SORTE')

else:
    print(f'\033[1;31mERROU! o número que eu pensei foi \033[1;32m{n}'), playsound.playsound('exe028errou.mp3')
    print('\033[30mTENTE NOVAMENTE')


