from datetime import date
atual = date.today().year
sexo = str(input('Qual o seu sexo? ')).strip().capitalize()
#Se for masculino
if 'Homem' in sexo or 'Masculino' in sexo:
    nasc = int(input('Digite o ano de seu nascimento: '))
    idade = atual - nasc
    print(f'Você nasceu em {nasc}, tem {idade} ano(s) em {atual}')
    if idade > 18:
        saldo = idade - 18
        print(f'\033[31mVocê deveria ter se alistado há {saldo} ano(s)')
        print(f'\033[34mSeu alistamento foi em {atual -saldo}')
    elif idade == 18:
        print(f'\033[32mÉ AGORA! Neste ano de {atual}, você terá que se alistar!')
    elif idade < 18:
        saldo = 18 - idade
        print(f'\033[34mAinda não é tempo de seu alistamento')
        print(f'Seu alistamento será daqui a {saldo} ano(s) em {atual + saldo}')
elif 'Feminino' in sexo or 'Mulher' in sexo:
    desejo = str(input('Mulheres não são obrigadas a alistarem-se, mas deseja se alistar? '))
    if 'Não' in desejo or 'Nao' in desejo:
        print('Tenha um bom dia!')
    elif 'Sim' in desejo or 'Quero':
        nasc = int(input('Digite o ano de seu nascimento: '))
        idade = atual - nasc
        print(f'Você nasceu em {nasc}, tem {idade} ano(s) em {atual}')
        if idade > 18:
            saldo = idade -18
            print(f'\033[31mVocê deveria ter se alistado a {saldo} ano(s)')
            print(f'\033[34mO seu alistamento foi em {atual-saldo}')
        elif idade == 18:
            print(f'\033[32mÉ AGORA! Neste ano de {atual}, você terá que se alistar!')
        elif idade < 18:
            saldo = 18 - idade
            print('Ainda não é tempo de seu alistamento')
            print(f'Seu alistamento será daqui a {saldo} ano(s) em {atual + saldo}')
print('\033[34mTenha um bom dia!')
