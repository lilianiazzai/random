from random import randint
num = []
som = 0
def add():
    num.append(randint(0, 100))
add()
add()
add()
add()
add()
print(f'List: {num}')
for alg in num:
    if alg % 2 == 0:
        som += alg
print(f'Adding even numbers: {som}')