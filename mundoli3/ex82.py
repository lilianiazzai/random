list =[]
odd = []
even = []
while True:
    num = int(input('Enter a number: '))
    list.append(num)
    choo = str(input('Do you want to continue [Y,N]: ')).upper().strip()[0]
    while choo not in 'YN':
        print('Invalid.', end = '')
        choo = str(input('Do you want to continue [Y,N]: ')).upper().strip()[0]
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
    if choo == 'N':
        break
print(f'The complete list: {list}')
print(f'The odd list: {odd}')
print(f'The even list: {even}')