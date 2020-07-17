print('-=' * 20)
print('Analisador de triângulos')
print('-=' * 20)
reta1 = float(input('Primeiro segmento: '))
reta2 = float(input('Segundo segmento: '))
reta3 = float(input('Terceito segmento: '))
if reta1 + reta2 > reta3 and reta3 > reta2 - reta1:
   print('Dá para formar um triângulo!')
else:
   print('Não dá para formar um triângulo!')
