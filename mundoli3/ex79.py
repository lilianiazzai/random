list = []
while True:
    num = int(input('Enter a number: '))
    if num not in list:
        list.append(num)
    choo = str(input('Do you want to continue [Y/N]: ')).strip().upper()[0]
    while choo not in 'YN':
        print('Invalid...')
        choo = str(input('Do you want to continue [Y/N]: ')).strip().upper()[0]
    if choo == 'N':
        break
list.sort()
print(list)