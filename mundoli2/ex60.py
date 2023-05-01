n1 = int(input('Enter a number to calculate its factorial: '))
c = n1
fact = 1
print('{}! = '.format(n1), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c>1 else ' = ', end='')
    fact = fact * c
    c -= 1
print('{}'.format(fact))