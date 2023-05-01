gen = list()
peo = list()
count = fat = ski = 0
fot = sko = ''
while True:
    peo.append(str(input('Type your name: ')))
    peo.append(float(input('Type your weight: ')))
    count += 1
    gen.append(peo[:])
    peo.clear()
    choo = str(input('Do you want to continue [Y,N]: ')).upper().strip()[0]
    while choo not in 'YN':
        print('INVALID!', end = '')
        choo = str(input('Do you want to continue [Y,N]: ')).upper().strip()[0]
    for p in gen:
        if count == 1:
            fat = ski = p[1]
            fot = sko = p[0]
        elif p[1] > fat:
            fat = p[1]
            fot = p[0]
        elif p[1] < ski:
            ski = p[1]
            sko = p[0]
    if choo == 'N':
        break
print('...' * 20)
print(gen)
print(f'{count} people were registered;')
print(f'The fattest person is {fot} with {fat}kg')
print(f'The skinniest person is {sko} with {ski}kg')
print('...' * 20)