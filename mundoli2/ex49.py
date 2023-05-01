n = int(input('Type a number: '))
for c in range(0, 11):
    print('{} . {} = '.format(n, c), end='')
    print(c * n)
print('Have a nice day!')