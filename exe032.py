from datetime import date
from calendar import  isleap
ano = int(input('Digite o ano: '))
ano6 = isleap(ano)
if ano6 is True:
    print(f'O ano de {ano} é bissexto')
else:
    print(f'O ano de {ano} não é bissexto')


