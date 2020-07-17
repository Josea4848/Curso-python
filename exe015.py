km = float(input('Digite quantos quilômetros foram percorridos: '))
dias = int(input('Digite quantos dias em que ele foi alugado: '))
total = (km* 0.15)+(dias * 60)
print(f'O valor total a ser pago será R${total:.2f}')


