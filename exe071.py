print('=' * 5,'BANCO JOSÉ','=' * 5)
sacar = int(input('Deseja sacar quanto? R$'))
total = sacar
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de {céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        if total == 0:
            break
print('Processo finalizado, tenha um bom dia!')
