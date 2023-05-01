from random import randint
from time import sleep
from operator import itemgetter
game = {}
ranking = {}
game['Player1'] = randint(1,6)
game['Player2'] = randint(1,6)
game['Player3'] = randint(1,6)
game['Player4'] = randint(1,6)
for k,v in game.items():
    print(f"{k} got {v}")
    sleep(0.4)
ranking = sorted(game.items(), key = itemgetter(1), reverse = True)
print('...'*20)
print('FINAL RANKING')
sleep(0.5)
for n, p in ranking:
    print('{:.<10}{:.>10}'. format(n, p))
print('...'*20)