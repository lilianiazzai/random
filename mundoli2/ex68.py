from random import randint
print('Lets play odd or even')
num = comp = s = count = 0
choo = 'even' or 'odd'
while True:
    num = int(input('Enter a number between 0 and 10: '))
    choo = str(input('odd or even: ')).strip().lower()
    comp = randint(0, 10)
    res = (num + comp)
    if res % 2 == 0:
        if choo == 'even':
            print('You won!')
            print(f'I said {comp} and you {num}, and their add is {choo}!')
            count += 1
        elif choo == 'odd':
            print('You lost!')
            print(f'I said {comp} and you {num}, and their add is not {choo}!')
            break
    else:
        if choo == 'odd':
            print('You won!')
            print(f'I said {comp} and you {num}, and their add is {choo}!')
            count += 1
        if choo == 'even':
            print('You lost!')
            print(f'I said {comp} and you {num}, and their add is not {choo}!')
            break
print(f'GAME OVER! You won {count} times!')