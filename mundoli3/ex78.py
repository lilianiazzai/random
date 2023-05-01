list = []
for c in range (0, 5):
    list.append(int(input(f'Enter a number to the {c} position: ')))
print(list)
list.sort()
print(f'The smallest is {list[0]} on the position {c}')
print(f'The largest is {list[4]} on the position {c}')
# ta errado (a resposta do guanab nn rodou aq)