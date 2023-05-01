def vote(a):
    if a <= 2004:
        print('You should vote!')
    elif a > 2004 and a <= 2006:
        print('If you want, you can vote!')
    elif a > 2006:
        print('You are too young to vote!')
a = int(input('Year of birth: '))
vote(a)