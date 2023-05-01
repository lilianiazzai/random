print("Welcome to the schools's website")
n1 = float(input('Type your first grade: '))
n2 = float(input('Type your second grade: '))
media = (n1 + n2)/2

if media < 5:
    print('You are dissaproved! Study more...')
elif media < 6.9:
    print('You have to do the final test! \nAsk your teacher when it is going to be;')
elif media >= 7:
    print('Congratulations! You are aproved!')
