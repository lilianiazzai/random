all = {}
tot = 0
while True:
    all['name'] = str(input("Player's name: "))
    all['match'] = int(input("Player's matches: "))
    for c in range(1, all['match'] + 1):
        all[f'pont{c}'] = int(input(f"{c} Match points: "))
        tot += all[f'pont{c}']
    choo = str(input('Finish? ')).strip().upper()[0]
    while choo not in 'YN':
        print('INVALID! ', end='')
        choo = str(input('Finish? ')).strip().upper()[0]
    if choo == 'Y':
        break
print(all)
print(tot)
#incompletojkkkkjk