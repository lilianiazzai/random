print('REGISTER')
age = countg = cm = cf = ca = 0
gen = 'F' or 'M'
opt = 'YES' or 'NO'
while True:
    age = int(input('Age: '))
    gen = str(input('Gender [F/M]: ')).strip().upper()[0]
    countg += 1
    if gen == 'M':
        cm +=1
        if age > 18:
            ca += 1
    if gen == 'F':
        if age < 20:
            cf += 1
        if age > 18:
            ca += 1
    opt = str(input('Do you want to continue? ')).upper().strip()[0]
    while opt not in 'YN':
        opt = str(input('Do you want to continue? ')).upper().strip()[0]
    if opt == 'N':
        break
print(f'{countg} people were registered;')
print(f'There are {ca} majors among them;')
print(f'There are {cm} men among them;')
print(f'There are {cf} women lower than 20 years;')
