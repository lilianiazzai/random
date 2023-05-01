exp = str(input('Type the expression: '))
l1 = []
l2 = []
for som in exp:
    if som == '(':
        l1.append(som)
    if som == ')':
        l2.append(som)
if len(l1) == len(l2):
    print('This expression can be resolved')
else:
    print('This can not be solved')