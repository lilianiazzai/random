lim = []
countim = 0
while True:
    nim = int(input('Enter a number: '))
    lim.append(nim)
    bim = str(input('Do you want to continue [Y,N]: ')).strip().upper()[0]
    while bim not in 'YN':
        print('Invalid.', end = '')
        bim = str(input('Do you want to continue [Y,N]: ')).strip().upper()[0]
    if bim == 'N':
        break
    if nim == 5:
        countim += 1
print('.....' * 7)
print(f'{len(lim)} numbers were typed;')
lim.sort(reverse = True)
print(lim)
if countim >= 1:
    print(f'The number 5 was typed {countim + 1} times;')
if countim == 0:
    print(f'There isnt 5 in the list;')