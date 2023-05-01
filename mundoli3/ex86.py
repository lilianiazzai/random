mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        mat[l][c] = int(input(f'Enter a number to [{l},{c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{mat[l][c]}]', end = '')
    print()
