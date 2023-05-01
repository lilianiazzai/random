name = str(input('Type your name: '))
lower = name.lower()
strip = lower.strip()
split = strip.split()
silva = 'silva' in split
print('You do have Silva in your name: {};'.format(silva))