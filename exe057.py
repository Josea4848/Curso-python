p = str(input('Digite seu sexo [M/F]: ')).upper().strip()
if 'MASCULINO' or 'HOMEM' or 'MACHO' or 'RAPAZ' or 'MENINO' in p:
    p = 'M'
if 'FEMININO'or'MULHER'or'MOÇA'or'MENINA' in p:
    p = 'F'
while p!= 'M' or 'F':
    p=str(input('DADOS INVÁLIDOS, informe seu sexo: ')).upper().strip()
print(f'Sexo {p} registrado com sucesso')
