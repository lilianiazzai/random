n = add = count = 0
n = int(input('Enter a number: '))
while n != 999:
    print('Type 999 to finish')
    add += n
    count += 1
    n = int(input('Enter a number: '))
print('{} numbers were typed, and their adittion is {}'.format(count, add))