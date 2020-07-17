print('-=' * 5,'Cálculo de \033[1mIMC','-='*5)
alt = float(input('\033[mDigite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (alt ** 2)
print(f'O \033[34mIMC \033[mé de \033[4m{imc:.1f}')
if imc < 18.5:
    print('\033[31mEstá \033[4mabaixo do peso.')
    print('\033[0;34mÉ recomendado uma avaliação médica')
elif imc >= 18.5 and imc <= 24.9:
    print('\033[32mEstá no \033[4mpeso ideal.')
elif imc >= 25 and imc <= 29.9:
    print('\033[33mEstá com \033[4mSobrepeso')
    print('\033[0;31mCuide-se!')
elif imc >=30 and imc <=34.9:
    print('\033[35mEstá com \033[4mObesidade grau 1')
    print('\033[0;31mCuide-se!')
elif imc >= 35 and imc <= 39.9:
    print('\033[31mEstá com \033[4mObesidade grau 2')
    print('\033[0;31mAlerta, Cuide-se!')
else:
    print('\033[31mEstá com \033[4mObesidade mórbida')
    print('\033[0,31mÉ recomendado uma avaliação médica!')
