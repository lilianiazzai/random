n1 = int(input('Type a number: '))
n2 = int(input('Type another number: '))
if n1>n2:
    print('Between {} and {}, the major is {};'.format(n1, n2, n1))
elif n2>n1:
    print('Between {} and {}, the major is {}'.format(n1, n2, n2))
else:
    print('These numbers have the same value!')
print('Hope I helped you :)')