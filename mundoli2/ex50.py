soma = 0
count = 0
for li in range(0, 6):
    num = int(input('Type a number: '))
    par = num % 2
    if par == 0:
        soma = soma + num
        count = count + 1
print('A soma dos {} numeros pares digitados é {}.'.format(count, soma))