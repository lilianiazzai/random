count = 0
n0 = int(input('Enter a number: '))
n1 = int(input('Enter a number: '))
n2 = int(input('Enter a number: '))
n3 = int(input('Enter a number: '))
tup = (n0, n1, n2, n3)
print(f'The number 9 apears {tup.count(9)} times')
if n0 == 3 or n1 == 3 or n2 == 3 or n3 == 3:
    print(f'The number 3 apears on the {tup.index(3)} position')
else:
    print('There is no 3 in tuple')
if n0%2 == 0:
    count += 1
if n1%2 == 0:
    count += 1
if n2%2 == 0:
    count += 1
if n3%2 == 0:
    count += 1
print(f'There are {count} even numbers')