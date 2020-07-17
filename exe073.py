import random
tabela = ('Santos','Palmeiras','Flamengo','Atlético-MG','Corinthians','São Paulo','Internacional','Athletico-PR','Botafogo','Bahia','Ceará SC','Goiás','Grêmio','Fortaleza','Vasco da Gama','Fluminense','Chapecoense','Cruzeiro','CSA','Avaí')
print(f'Os 5 primeiros colocados são {tabela[:5]}')
print(f'Os 4 últimos colocados são {tabela[-4:]}')
print(f'Organizados em ordem alfabética temos {sorted(tabela)}')
print(f'A Chapecoense está na {tabela.index("Chapecoense")+1}ª posição')
print('='*10,'Tabela','='*10)


