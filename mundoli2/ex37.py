number = int(input('Type your number: '))
print('Choose your conversion base: \n(1)Binarie;')
print('(2)Octal; \n(3)Hexadecimal;')
pick = int(input('Your choice: '))

if pick == 1:
    print('This number converted to binarie is {}'.format(bin(number)[2:]))
elif pick == 2:
    print('This number converted to octal is {}'.format(oct(number)[2:]))
elif pick == 3:
    print('This number converted to hexadecimal is {}'.format(hex(number)[2:]))
else:
    print('This option does not exist \nYou can only choose 1 to 3')
print('Hope I helped you :)')
