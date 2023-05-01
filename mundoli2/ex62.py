print('~' * 10, 'PA', '~' * 10)
ft = int(input('Enter the first term: '))
ratio = int(input('Enter the ratio: '))
i = ft
count = 1
choo = 10
total = 0
while choo != 0:
    total += choo
    while count <= total:
        print('{} ~ '.format(i), end='')
        i += ratio
        count += 1
    print('end')
    choo = int(input('How many terms do you want to show: '))
print('PA finished within {} terms;'.format(total))