from datetime import date
anoatual = date.today().year
idademaior = 0
idademenor = 0
for c in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    idade = anoatual - ano
    if idade > 18:
        idademaior += 1
    else:
        idademenor += 1
print(f'Temos {idademaior} maior(es) de idade\nE {idademenor} menor(es) de idade')
