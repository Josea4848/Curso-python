print('-=' * 20)
print('Analisador de triângulos')
print('-=' * 20)
reta1 = float(input('Primeiro segmento: '))
reta2 = float(input('Segundo segmento: '))
reta3 = float(input('Terceito segmento: '))
if reta1 + reta2 > reta3 or reta2 + reta3 > reta1 or reta1 + reta3 > reta2:
   print('Dá para formar um triângulo', end=' ')
   if reta1 == reta2 == reta3:
       print('EQUILÁTERO!')
   elif reta1 != reta2 != reta3 != reta1:
       print('ESCALENO!')
   else:
       print('ISÓSCELES')
else:
   print('Não dá para formar um triângulo!')

