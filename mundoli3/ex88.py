from random import randint
from time import sleep
gg = []
game = []
turn = int(input('How many turns: '))
tot = 0
while tot < turn:
    count = 0
    while True:
        num = randint(1, 60)
        if num not in gg:
            gg.append(num)
            count += 1
        if count >= 6:
            break
    gg.sort()
    game.append(gg[:])
    gg.clear()
    tot += 1
for i, l in enumerate(game):
    print(f'Game {i+1}: {l}')