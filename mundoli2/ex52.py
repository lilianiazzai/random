numb = int(input('Type a number: '))
tot = 0
for b in range(1, numb + 1):
    rest = numb % b
    if rest == 0:
        print('\033[m', end=' ')
        tot += 1
    else:
        print('\33[m')
