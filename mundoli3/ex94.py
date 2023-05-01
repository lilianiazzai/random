data = {}
all = list()
woman = list()
ild = list()
old = {}
name = []
ag = []
count = ave = 0
while True:
    data['name'] = str(input('Enter your name: '))
    data['age'] = int(input('Enter your age: '))
    data['gender'] = str(input('Enter your gender: ')).strip().upper()[0]
    old[data['name']] = data['age']
    count += 1
    ave += data['age']
    pim = ave / count
    while data['gender'] not in 'FM':
        print('INVALID! ', end='')
        data['gender'] = str(input('Enter your gender: ')).strip().upper()[0]
    if data['gender'] == 'F':
        woman.append(data['name'])

    choo = str(input('Do you want to continue? ')).strip().upper()[0]
    while choo not in 'YN':
        print('INVALID! ', end='')
        choo = str(input('Do you want to continue? ')).strip().upper()[0]
    all.append(data.copy())
    data.clear()
    if choo == 'N':
        break
for k,v in old.items():
    if v > pim:
        ild.append(k)
        ild.append(v)
for i,s in enumerate(ild):
    if i%2 != 0:
        ag.append(s)
    else:
        name.append(s)
print('...'*20)
print(f"People registered: {count}")
print('Average age: {:.2f}'.format(pim))
print(f'Women: {woman}')
print(f'People older than the average: {name}')
print('...'*20)