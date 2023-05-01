gender = str(input('Type your gender [F/M]: ')).strip().upper()[0]
while gender not in 'FM':
    gender = str(input('Invalid option...Please, type your gender [F/M]: ')).strip().upper()[0]
print('thank you')