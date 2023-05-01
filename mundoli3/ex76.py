tup = ('Rímel', 10,
       'Blush líquido', 7.90,
       'Gloss', 8.75,
       'Bruma fixadora', 16.99,
       'Glitter em gel', 4.90,
       'Primer', 9.99,
       'Corretivo líquido', 12)
for c in range (0, len(tup)):
       if c % 2 == 0:
              print('{:.<25}'.format(tup[c]), end = '')
       else:
              print('R${:>5.2f}'.format(tup[c]))
