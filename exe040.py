print('-=' * 5 ,'Analise sua nota','-=' * 5)
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
média = (nota1 + nota2)/2
if média < 5:
    print(f'\033[31mSua média foi {média:.1f} e você foi reprovado')
elif média >= 5 and média <= 6.9:
    print(f'\033[34mSua média foi {média} e você fará recuperação')
else:
    print(f'\033[32mParabéns! Sua média foi {média} e você foi aprovado')
