matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = somacol =  0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para a posição {l,c}: '))
for l in range(0,3):
    for c in range(0,3):
        if matriz[l][c] % 2 == 0:
            somapares += matriz[l][c]
    somacol += matriz[l][2]
print(f'A soma dos valores pares da matriz foi {somapares}')
print(f'A soma dos valores da terceira coluna foi {somacol}')
print(f'O maior valor da segunda linha foi {max(matriz[1])}')
