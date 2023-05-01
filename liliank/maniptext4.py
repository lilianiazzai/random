name = str(input('Type your name: '))
edie = name.lower().strip()
a = edie.count('a')
b= edie.find('a')
print('You have {} letters a in your name;'.format(a))
print('The first letter a appears'
      ''
      ' at {} space'.format(b))