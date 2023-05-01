def lin():
    print('...'*10)
lin()
print('A: ', end='')
for c in range(1,11):
    print(f'{c}', end=', ')
print('\nB: ', end='')
for c in range(10, -1, -2):
    print(f'{c}', end=', ')
def cont(fi, la, ra):
    if la>0:
        for c in range(fi, la+1, ra):
            print(f'{c}', end=', ')
    if la <= 0:
        for c in range(fi, la-1, ra):
            print(f'{c}', end=', ')
print()
lin()
fi = int(input('\nFirst term: '))
la = int(input('Last term: '))
ra = int(input('Ratio: '))
lin()
print('C: ', end='')
cont(fi, la, ra)
print()