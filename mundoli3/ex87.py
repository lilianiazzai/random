soma = c2 = count = big = 0
mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        mat[l][c] = int(input(f'Enter a number to [{l},{c}]: '))
        c += 1
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{mat[l][c]}]', end = '')
    print()
print('...' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        if mat[l][c] % 2 == 0:
            soma += mat[l][c]
        if c == 2:
            c2 += mat[l][c]
        if l == 1:
            if mat[l][0] > mat[l][1] and mat[l][0] > mat[l][2]:
                big = mat[l][0]
            if mat[l][1] > mat[l][0] and mat[l][1] > mat[l][2]:
                big = mat[l][1]
            if mat[l][2] > mat[l][0] and mat[l][2] > mat[l][1]:
                big = mat[l][2]
print(f'The addition of even numbers: {soma};')
print(f'The addition of the third column: {c2};')
print(f'The biggest number in the second line: {big};')