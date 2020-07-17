preço = float(input('Digite o valor do produto: R$'))
cond = str(input('Digite a condição de pagamento: ')).capitalize().strip()
print(f'  Preço do produto: \n   R${preço:.2f}')
if 'Dinheiro' in cond or 'Cheque' in cond:#desconto de 10%
    prefinal = preço - (10/100*(preço))
    print(f'  Desconto: \n   10%')
    print(f'  Juros: \n   0%')
    print(f'  Preço final: \n   R${prefinal:.2f}')
elif 'Cartão' in cond:
    parcelas = int(input('Quantidade de parcelas:'))
    if parcelas == 1:
        prefinal = preço - (5/100*(preço))
        print(f'  Desconto: \n   5%  ')
        print(f'  Juros: \n   0%')
        print(f'  Preço final: \n   R${prefinal:.2f}')
    elif parcelas == 2:
        print(f'  Desconto: \n   0%')
        print(f'  Juros: \n   0%')
        print(f'Preço final: \n   R${preço:.2f}')
    else:
        prefinal = preço + (20/100 * (preço))
        print(f'  Desconto: \n   0%')
        print(f'  Juros: \n   20%')
        print(f'Preço final: \n   R${prefinal:.2f}')
