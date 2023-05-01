gen = []
odd = []
even = []
for c in range(0, 7):
    gen.append(int(input('Enter a number: ')))
for num in gen:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print(f'Numbers registered: {gen}')
print(f'Odd numbers: {odd}')
print(f'Even numbers: {even}')