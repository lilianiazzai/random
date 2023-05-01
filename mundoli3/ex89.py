ind = []
gen = []
liave = []
while True:
    ind.append(str(input('Students name: ')))
    n1 = float(input('First grade: '))
    ind.append(n1)
    n2 = float(input('Second grade: '))
    ind.append(n2)
    ave = (n1 + n2)/2
    ind.append(ave)
    choo = str(input('Do you want to continue: ')).strip().upper()[0]
    while choo not in 'YN':
        print('INVALID!', end='')
        choo = str(input('Do you want to continue: ')).strip().upper()[0]
    gen.append(ind[:])
    ind.clear()
    if choo == 'N':
        break
for peo in gen:
    print('{:.<20}'.format(peo[0]), end='')
    print(' {:.>5} '.format(peo[3]))
while True:
    print('To stop, enter LOL')
    cont = str(input('Whose student do you want to see the grades: '))
    for peo in gen:
        if cont == peo[0]:
            print(f'{peo[0]} 1 grade:    {peo[1]}')
            print(f'{peo[0]} 2 grade:    {peo[2]}')
    if cont == 'LOL':
        break