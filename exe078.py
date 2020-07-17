valor = list(int(input(f'Digite um valor para a posição {v}: '))for v in range(0,5))
print(f'Você digitou os valores {valor}')
for c, v in enumerate(valor):
    if v == max(valor):
        print(f'O maior valor foi {v} e está na posição {c}')
    if v == min(valor):
        print(f'O menor valor foi {v} e está na posição {c}')




