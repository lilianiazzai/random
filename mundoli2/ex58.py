from random import randint
pc = randint(0, 10)
count = 1
num = int(input('Try to guess which number between 1 to 10 Im thinking: '))
while num != pc:
    if num > pc:
        print('Its Lower...',end='')
        count = count + 1
    elif num < pc:
        print('Its larger...',end='')
        count = count + 1
    num = int(input('Try again: '))
print('You needed {} turns to guess it right!'.format(count))
print('I was thinking about {}'.format(pc))