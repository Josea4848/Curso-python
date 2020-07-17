cont_i = cont_s = cont_m = 0
while True:
    print('='*10,'CADASTRE UMA PESSOA','='*10)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    print('='*41)
    if idade >= 18:
       cont_i += 1
    if sexo == 'M':
        cont_s += 1
    if sexo == 'F' and idade < 20:
        cont_m += 1
    s_ou_n = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    while s_ou_n not in 'SN':
        s_ou_n = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if s_ou_n == 'N':
        break
print('_'*35)
print('\033[1mDADOS:')
print(f'A) {cont_i} pessoa(s) maior(es) de 18 anos'
      f'\nB) {cont_s} homens'
      f'\nC) {cont_m} mulher(es) com menos de 20 anos')
print('_'*35)
