numero = int(input('Digite um numero inteiro: '))
div = numero % 2
if div == 0:
    print('O numero {} é par'.format(numero))
else:
    print('O numero {} é impar'.format(numero))