c1 = float(input('How many meters has the first side: '))
c2 = float(input('How many meters has the second side: '))
c3 = float(input('How many meters has the third side: '))

if c1<c2+c3 and c2<c1+c3 and c3<c1+c2:
    print('These sides can form a triangle ',end='')
    if c1 == c2 == c3:
        print('equilateral')
    elif c1 != c2 and c1 != c3 and c2!=c3:
        print('escalene')
    else:
        print('isosceles')

else:
    print('These sides can not form a triangle')
