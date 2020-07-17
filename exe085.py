numerosgerais = [],[]
for c in range(1,8):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        numerosgerais[0].append(num)
    else:
        numerosgerais[1].append(num)
print(f'Os valores pares foram {numerosgerais[0]}\nOs valores ímpares foram {numerosgerais[1]}')
