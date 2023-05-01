from random import randint
print('tenho um desafio p vc!!')
print('~' * 30)
comp = randint(0, 5)
jog = int(input('Em qual numero de 0 a 5 eu pensei?'))
print('~' * 30)
if comp == jog:
    print('acertou mano kkkkkk')
else:
    print('burrao errou ;)))')
print('pensei no {}, e nao em {}'.format(comp, jog))