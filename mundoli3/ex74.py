from random import randint
n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'The random numbers are : {n}')
new = sorted(n)
print(f'The smallest numbers is {new[0]} \nThe biggest number is {new[4]}')