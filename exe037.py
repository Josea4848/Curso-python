numero = int(input('Digite um número inteiro: '))
print("""Escolha uma das bases de conversões
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL""")
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'O número {numero} convertido para BINÁRIO é {bin(numero)[2:]}')
elif opção == 2:
    print(f'O número {numero} convertido para OCTAL é {oct(numero[2:])}')
elif opção == 3:
    print(f'O número {numero} convertido para HEXADECIMAL é {hex(numero)[2:]}')
else:
    print('Digite uma opção Válida')
