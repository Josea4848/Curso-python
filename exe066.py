cont = s = 0
while True:
    n = int(input('Digite um número [\033[31m999 para parar\033[m]: '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'Foram {cont} números digitados e a soma entre eles é {s}')
