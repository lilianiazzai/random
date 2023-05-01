print('TERMS OF PA')
ft = int(input('Enter the first term: '))
ratio = int(input('Enter the ratio: '))
count = 1
c = ft
while count <= 10:
    print('{} ~ '.format(c), end='')
    c += ratio
    count += 1
print('Finish')