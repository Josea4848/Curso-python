from datetime import date
nasc = int(input('Digite o ano de nascimento do atleta: '))
atual = date.today().year
idade = atual - nasc
if idade <= 9:
    print(f'\033[34mO atleta com {idade} ano(s), pertence a categoria \033[1mMIRIM')
elif idade > 9 and idade <=14:
    print(f'\033[32mO atleta com {idade} anos, pertence a categoria \033[1mINFANTIL')
elif idade > 14 and idade <= 19:
    print(f'\033[35mO atleta com {idade} anos, pertence a categoria \033[1mJUNIOR')
elif idade > 19 and idade <=20:
    print(f'\033[33mO atleta com {idade} anos, pertence a categoria \033[1mSÊNIOR')
elif idade > 20:
    print(f'\033[31mO atleta com {idade} anos, pertence a categoria \033[1mMASTER')
