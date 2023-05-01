print('Welcome to the Natinal Swimming Conference')
print('To show you your categorie, I have to know your age')
age = int(input('So, please, tell me your age: '))

if age <= 25 and age>19:
    print('You are senior')
elif age <= 9:
    print('You are minor')
elif age <= 14 and age >9:
    print('You are junior')
elif age <= 19 and age>14:
    print('You are teen')

else:
    print('I am sorry... but you are too old:((')
