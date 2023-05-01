print('Hi! Welcome to the military enlistment website.')
name = str(input('Type your name: '))
print('Type (1) for male and (2) for female')
gender = str(input('Your gender: '))
if len(gender) > 3:
    print('This option is invalid! Try again later...')
age = int(input('Type your age: '))

if gender == 2:
    print('Woman can not enlist!')

elif age == 18:
    print('You are ready to enlist yourself!')
elif age>18:
    time = age - 18
    print('You had to enlist yourself {} years ago!'.format(time))
elif age<18:
    time = 18 - age
    print('''You are too young for the enlistment
    Come back here after {} year'''.format(time))

print('Thanks for the contact, {}!'.format(name))