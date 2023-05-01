print("FIBONACCI'S SEQUENCE")
print('~~~~~~' * 5)
num = int(input('Enter a number: '))
fir = 0
sec = 1
print('{} ~ {} '.format(fir, sec), end = '')
count = 3
while count <= num:
    thi = fir + sec
    print('~ {} '.format(thi), end='')
    fir = sec
    sec = thi
    count += 1
print('\nEND')