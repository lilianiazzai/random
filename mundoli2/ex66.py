add = num = count = 0
while True:
    num = int(input('Enter a number: '))
    if num == 999:
        break
    add += num
    count += 1
print(f'{count} numbers were typed and their addition is {add}')