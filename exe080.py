maior = menor = 0
números = list()
for c in range(0,5):
    n = int(input(f'Digite o valor da posição {c}: '))
    if c == 0 or n > números[-1]:
        números.append(n)
    else:
        pos = 0
        while pos < len(números):
            if n <= números[pos]:
                números.insert(pos,n)
                break
            pos += 1
print(números)
