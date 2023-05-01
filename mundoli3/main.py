num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
choo = int(input('Digite um numero de 0 a 20: '))
while choo>20 or choo<0:
    choo = int(input('Digite um numero de 0 a 20: '))
print(f'O numero q vc digitou foi {num[choo]}')