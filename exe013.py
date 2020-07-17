s=float(input('Digite seu salário atual: R$'))
d=float(input('Digite o valor do aumento(%): '))
vd=s+(d/100)*s
print(f'O seu atual salário é de R${s}, Com a promoção de {d}% ele passará a ser R${vd:.2f}')
