print('Hi, Good Morning!')

nome = str(input('Type your name: '))
price = float(input('Type the price of the house: '))
salary = float(input('Type your salary: '))
year = float(input('In how many years do you pretend to fnish the payment: '))

pm = price / (year * 12)
max = (salary * 30)/100

if pm > max:
    print('You can not buy this house')
elif pm == max:
    print('Alright! \nYou will pay {} for {} months!'.format(pm, year * 12))
else:
    pm < max
    print('Alright! \nYou will pay {} for {} months!'.format(pm, year * 12))