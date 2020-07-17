primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro + (10 - 1) * razao
for c in range (primeiro, termo + 1, razao):
    print(c, end=' → ')
print('Acabou!')
