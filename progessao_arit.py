# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

from time import sleep
print('~~~~~~' * 26)
sleep(0.5)
print('1O TERMS OF A P.A')
sleep(0.5)
print('~~~~~~' * 26)

pt = int(input('Type the firt term of the P.A: '))
ratio = int(input('Type the ratio of the P.A: '))
last = 9 * ratio + pt
print('The first 10 numbers of your P.A are: ', end='')
for c in range(pt, last + 1, ratio):
    print(c, end=' ')

