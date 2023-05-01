import math
ang = float(input('digite seu angulo: '))
s = math.sin(math.radians(ang))
c = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print(' Seno = {:.2f} \n Cosseno = {:.2f} \n Tangente = {:.2f}'.format(s, c, tg))