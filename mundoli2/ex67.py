num = 0
while True:
    num = int(input('Choose a number: '))
    if num >= 0:
        for c in range (1, 11):
            print(f'{num} . {c} = {num * c}')
        print('~~~' * 10)
    if num < 0:
        break