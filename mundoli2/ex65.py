co = 'S'
soma = count = ave = major = minor = 0
while co != 'N':
    num = int(input('Enter a number: '))
    co = str(input('Do you want to continue (Y,N): ')).strip().upper()[0]
    soma += num
    count += 1
    if count == 1:
        major = minor = num
    else:
        if num > major:
            num = major
        if num < minor:
            num = minor
ave = soma / count
print('{} numbers were typed and the average is {}'.format(count, ave))
print('The major is {} and the minor is {}'.format(major, minor))