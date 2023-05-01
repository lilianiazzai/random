n1 = int(input('Type  number: '))
n2 = int(input('Type a number: '))
print('Choose an option: 1)add  2)multipie  3)larger    4)Type new numbers  5)Finish')
choose = int(input('Your option: '))

while choose != 5:
    if choose == 1:
        print('{} + {} = {}'.format(n1, n2, n1+n2))
        print('~~~~~~' * 20)
        print('Choose an option: 1)add  2)multipie  3)larger    4)Type new numbers  5)Finish')
        choose = int(input('Your option: '))

    elif choose == 2:
        print('{} * {} = {}'.format(n1, n2, n1*n2))
        print('~~~~~~' * 20)
        print('Choose an option: 1)add  2)multipie  3)larger    4)Type new numbers  5)Finish')
        choose = int(input('Your option: '))

    elif choose == 3:
        if n1 > n2:
            print('{} > {}'.format(n1, n2))
            print('~~~~~~' * 20)
            print('Choose an option: 1)add  2)multipie  3)larger    4)Type new numbers  5)Finish')
            choose = int(input('Your option: '))
        if n1 == n2:
            print('{} = {}'.format(n1, n2))
            print('~~~~~~' * 20)
            print('Choose an option: 1)add  2)multipie  3)larger    4)Type new numbers  5)Finish')
            choose = int(input('Your option: '))
        if n2 > n1:
            print('{} > {}'.format(n2, n1))
            print('~~~~~~' * 20)
            print('Choose an option: 1)add  2)multipie  3)larger    4)Type new numbers  5)Finish')
            choose = int(input('Your option: '))

    elif choose == 4:
        print('Type new numbers:')
        n1 = int(input('Type  number: '))
        n2 = int(input('Type a number: '))
        print('Choose an option: 1)add  2)multipie  3)larger    4)Type new numbers  5)Finish')
        choose = int(input('Your option: '))

print('Finish! Youre welcome')